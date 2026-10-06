#!/usr/bin/env python3
"""Stage 5 (GPU): J-lens and logit-lens readouts, written as compact files to pull.

At every layer and every exported position:
    J-lens      z = unembed(J_l h)   (the published lens map; identity at the final layer)
    logit lens  z = unembed(h)
Kept: the top-K token ids with their probabilities, and the Yes - No score
(log-sum-exp of the Yes-token scores minus that of the No tokens).

Exported positions: prefix from the last user-prompt token to the end of the post-response
boundary; each wording from the question's first token to the end of the post-answer boundary.

Output, per model (exports/<model>/):
  manifest.json                   transcripts, labels, wordings, self-report answers
  vocab.json                      token id -> decoded string
  <set>/<tid>/<part>.json         tokens, ids, segments (positions relative to the part),
                                  abs_start, layers, top_k, texts, and the array layout of:
  <set>/<tid>/<part>.bin          J ids, LL ids (uint32 [layers, T, K]), J probs, LL probs
                                  (float16 [layers, T, K]), scores (float16 [2, layers, T])
Rerunnable: a part is skipped when its files exist and were made from the same tokens and with
the current label (the manifest is always rewritten). Forward rows of transcripts that are no
longer selected (e.g. after a re-judgment changed the selection) are left out.

GPU memory: only the final norm, the unembedding and the lens maps go on the GPU (about 10 GB for
a 27B model); the model body stays on the CPU (about 54 GB of RAM for a 27B model in bf16). So a
48 GB card such as an L40S is enough. --full-model puts the whole model on the GPU, as before.

The extra unrelated set has no saved residual streams: forward.py --inline-readout exports its
parts with the same function (export_part) straight from the forward pass. This script then only
skips them and lists them in the manifest.

Usage: python3 src/readout.py --model qwen3.6-27b [--top-k 16] [--full-model]
"""
import argparse
import hashlib
import json
import os
import sys
import time

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from models import gpu_sanity, load_lens, load_model, logger, read_jsonl, seg, setup_logging, slug  # noqa: E402

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
YES = ["Yes", " Yes", "yes", " yes", "YES", " YES"]
NO = ["No", " No", "no", " no", "NO", " NO"]


def single_ids(tok, surfaces):
    out = {}
    for s in surfaces:
        ids = tok.encode(s, add_special_tokens=False)
        if len(ids) == 1 and ids[0] not in out.values():
            out[s] = ids[0]
    return out


def setup(L, model_name, top_k):
    """What the export needs besides the model: the lens maps on the device, the Yes / No token
    ids and the layer list. Shared by this script and by forward.py --inline-readout."""
    import torch
    lens = load_lens(model_name)
    final = L.n_layers - 1
    layers = list(range(L.n_layers))
    missing = [l for l in layers if l != final and l not in lens.jacobians]
    if missing:
        sys.exit(f"FATAL: the lens has no map for layers {missing}")
    J = {l: lens.jacobians[l].to(L.device, torch.float32) for l in layers if l != final}
    yes, no = single_ids(L.tokenizer, YES), single_ids(L.tokenizer, NO)
    return dict(J=J, final=final, layers=layers, K=top_k, yes=yes, no=no,
                yes_ids=sorted(yes.values()), no_ids=sorted(no.values()))


def write_vocab(L, out_dir):
    vocab_path = os.path.join(out_dir, "vocab.json")
    if os.path.exists(vocab_path):
        return
    tok = L.tokenizer
    # the unembedding can be wider than the tokenizer (padding rows); those decode to ""
    V = max(len(tok), L.hf_model.get_output_embeddings().weight.shape[0])

    def dec(i):
        try:
            return tok.decode([i])
        except Exception:
            return ""
    with open(vocab_path, "w") as f:
        json.dump([dec(i) for i in range(V)], f, ensure_ascii=False)


def part_span(r):
    """(first, last, fingerprint) of the positions a part exports: the prefix from the last
    user-prompt token, a wording from the question's first token; both to the end."""
    if r["part"] == "prefix":
        first = seg(r["segments"], "user_prompt")["end"] - 1
    else:
        first = r["saved_start"]
    last = len(r["ids"])
    return first, last, hashlib.md5(json.dumps(r["ids"][first:last]).encode()).hexdigest()


def export_part(L, R, r, t, acts, out_dir, chunk=128):
    """Write <set>/<tid>/<part>.json and .bin for one part. acts: [layers, T, d], the residual
    streams of positions first..last of part_span(r) (bf16 on the CPU, as forward.py makes them).
    r is the part's sequences.jsonl row, t its transcripts.jsonl row, R the dict of setup()."""
    import numpy as np
    import torch
    dev, K, layers, final, J = L.device, R["K"], R["layers"], R["final"], R["J"]
    first, last, fingerprint = part_span(r)
    part_dir = os.path.join(out_dir, t["set"], t["tid"])
    os.makedirs(part_dir, exist_ok=True)
    bin_path = os.path.join(part_dir, r["part"] + ".bin")
    T = acts.shape[1]
    if T != last - first:
        sys.exit(f"FATAL: {r['tid']} {r['part']}: {T} residual positions for {last - first} tokens")
    out = {"J_ids": np.zeros((len(layers), T, K), np.uint32), "LL_ids": np.zeros((len(layers), T, K), np.uint32),
           "J_p": np.zeros((len(layers), T, K), np.float16), "LL_p": np.zeros((len(layers), T, K), np.float16),
           "scores": np.zeros((2, len(layers), T), np.float16)}
    with torch.no_grad():
        for li, l in enumerate(layers):
            for c0 in range(0, T, chunk):
                h = acts[l, c0:c0 + chunk].to(dev, torch.float32)
                for lens_i, name in enumerate(("J", "LL")):
                    hh = h @ J[l].T if (name == "J" and l != final) else h
                    z = L.lens_model.unembed(hh).float()
                    lse = torch.logsumexp(z, -1, keepdim=True)
                    vals, idx = z.topk(K, -1)
                    out[f"{name}_ids"][li, c0:c0 + len(h)] = idx.cpu().numpy().astype(np.uint32)
                    out[f"{name}_p"][li, c0:c0 + len(h)] = (vals - lse).exp().cpu().numpy().astype(np.float16)
                    s = torch.logsumexp(z[:, R["yes_ids"]], -1) - torch.logsumexp(z[:, R["no_ids"]], -1)
                    out["scores"][lens_i, li, c0:c0 + len(h)] = s.clamp(-6e4, 6e4).cpu().numpy().astype(np.float16)
    layout, offset = [], 0
    with open(bin_path + ".tmp", "wb") as f:
        for name in ("J_ids", "LL_ids", "J_p", "LL_p", "scores"):
            a = np.ascontiguousarray(out[name])
            f.write(a.tobytes())
            layout.append(dict(name=name, dtype=str(a.dtype), shape=list(a.shape), offset=offset))
            offset += a.nbytes
    segs = r["segments"]
    rel = [dict(name=s["name"], start=max(s["start"], first) - first, end=min(s["end"], last) - first)
           for s in segs if s["end"] > first and s["start"] < last]
    header = dict(tid=r["tid"], part=r["part"], set=t["set"], item_id=t["item_id"], k=t["k"],
                  split=t["split"], label=t["label"], abs_start=first, layers=layers, top_k=K,
                  ids=r["ids"][first:last], ids_md5=fingerprint, tokens=r["tokens"][first:last],
                  segments=rel, arrays=layout)
    if r["part"] == "prefix":
        header.update(system=t["system"], user_prompt=t["user_prompt"], response=t["response"],
                      stance=t["stance"], quote=t["quote"])
    else:
        header.update(question=r["question"], answer_text=r["answer_text"], answer_label=r["answer_label"],
                      answer_finished=r["answer_finished"], answer_limit=r.get("answer_limit"))
    with open(os.path.join(part_dir, r["part"] + ".json"), "w") as f:
        json.dump(header, f, ensure_ascii=False)
    os.replace(bin_path + ".tmp", bin_path)


def exported(r, t, out_dir):
    """True if the part's files exist and were made from the same tokens and the current label."""
    part_dir = os.path.join(out_dir, t["set"], t["tid"])
    head_path = os.path.join(part_dir, r["part"] + ".json")
    if not (os.path.exists(os.path.join(part_dir, r["part"] + ".bin")) and os.path.exists(head_path)):
        return False
    with open(head_path) as f:
        old = json.load(f)
    return old.get("ids_md5") == part_span(r)[2] and old.get("label") == t["label"]


def write_manifest(L, R, model_name, run_dir, out_dir):
    """manifest.json over every part in sequences.jsonl whose transcript is still selected."""
    trs = {t["tid"]: t for t in read_jsonl(os.path.join(run_dir, "transcripts.jsonl"))}
    latest = {}
    for r in read_jsonl(os.path.join(run_dir, "sequences.jsonl")):
        latest[(r["tid"], r["part"])] = r          # a redone part replaces the earlier row
    seqs = [r for r in latest.values() if r["tid"] in trs]     # drop no-longer-selected transcripts
    by_tid = {}
    for r in seqs:
        t = trs[r["tid"]]
        e = by_tid.setdefault(r["tid"], dict(tid=t["tid"], set=t["set"], item_id=t["item_id"], k=t["k"],
                                             split=t["split"], label=t["label"], stance=t["stance"],
                                             n_tokens=t["n_tokens"], wordings={}))
        if r["part"] != "prefix":
            e["wordings"][r["part"]] = dict(answer_label=r["answer_label"], answer_finished=r["answer_finished"])
    manifest = dict(model=model_name, hf=L.spec["hf"], layers=R["layers"], top_k=R["K"], yes_tokens=R["yes"], no_tokens=R["no"],
                    wordings=sorted({r["part"] for r in seqs if r["part"] != "prefix"}),
                    transcripts=list(by_tid.values()))
    with open(os.path.join(out_dir, "manifest.json"), "w") as f:
        json.dump(manifest, f)
    return trs, seqs, by_tid


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--model", required=True)
    ap.add_argument("--top-k", type=int, default=16)
    ap.add_argument("--chunk", type=int, default=128, help="positions per unembedding call")
    ap.add_argument("--device", default=None)
    ap.add_argument("--full-model", action="store_true",
                    help="load the whole model on the GPU (needs an 80 GB card for a 27B model)")
    args = ap.parse_args()
    setup_logging()
    gpu_sanity()
    import torch

    run_dir = os.path.join(ROOT, "runs", slug(args.model))
    out_dir = os.path.join(ROOT, "exports", slug(args.model))
    os.makedirs(out_dir, exist_ok=True)
    trs = {t["tid"]: t for t in read_jsonl(os.path.join(run_dir, "transcripts.jsonl"))}
    latest = {}
    for r in read_jsonl(os.path.join(run_dir, "sequences.jsonl")):
        latest[(r["tid"], r["part"])] = r          # a redone part replaces the earlier row
    seqs = [r for r in latest.values() if r["tid"] in trs]     # drop no-longer-selected transcripts
    L = load_model(args.model, args.device, head_only=not args.full_model)
    R = setup(L, args.model, args.top_k)
    write_vocab(L, out_dir)

    t0 = time.time()
    for n, r in enumerate(seqs, 1):
        t = trs[r["tid"]]
        if exported(r, t, out_dir):
            continue                                   # already exported from these tokens
        first, last, _ = part_span(r)
        blob = torch.load(os.path.join(run_dir, "cache", r["tid"], r["part"] + ".pt"))
        acts = blob["acts"][:, first - blob["start"]:last - blob["start"]]   # [layers, T, d]
        export_part(L, R, r, t, acts, out_dir, args.chunk)
        del acts, blob
        if n % 25 == 0 or n == len(seqs):
            logger.info("%d/%d parts (%.0f s)", n, len(seqs), time.time() - t0)

    _, _, by_tid = write_manifest(L, R, args.model, run_dir, out_dir)
    print(f"READOUT DONE: {len(by_tid)} transcripts -> {out_dir}  ({time.time() - t0:.0f} s)")


if __name__ == "__main__":
    main()
