#!/usr/bin/env python3
"""Stage 4 (GPU): self-report answers and residual streams.

For every transcript:
  1. Prefix pass. One forward pass over [system][user][response] plus the post-response
     turn boundary (everything before the self-report question). Its residual streams are
     the only source for every prefix position, so those readouts are identical for all
     wordings.
  2. For each self-report wording: render [system][user][response][question] plus the
     generation prompt, generate the answer greedily (limit 256 new tokens; 1024 for gpt-oss,
     which reasons first), append the turn boundary that follows a finished answer, run one
     forward pass, and keep the residual streams from the question's first token onward.

Residual stream = the output of each block, at every layer (bf16).
  --save full   prefix positions from the first token (needed for PCA over whole transcripts)
  --save crop   prefix positions from the last user-prompt token onward

Output: runs/<model>/cache/<tid>/prefix.pt and <wording>.pt, each {acts [layers, T, d],
start (absolute position of acts[:, 0]), ids}; runs/<model>/sequences.jsonl (one row per
transcript x part, with tokens and segments). Rerunnable: finished parts are skipped.

--inline-readout (the extra unrelated set; user decision, 2026-10-01): the residual streams are
not saved. Each part's J-lens and logit-lens readouts are computed straight from the forward pass
and written by readout.py's export_part, in the same files the readout stage writes; the manifest
is rewritten at the end. Needs --save crop (the exported positions) and the whole model on the GPU.
--probe-vector: with --inline-readout, still keep one small file per transcript for the DYL probe
baseline: cache/<tid>/Q9_dyl.pt with the residual at the token before the yes/no answer only
(all layers, one position; about 0.7 MB for a 27B model), in the layout src/dyl_probe.py reads.
--template-residuals: with --inline-readout, also keep the residual streams at the template
positions only (for Experiment 3's fits on unrelated chats): cache/<tid>/template_<part>.pt =
{acts [layers, n, d] bf16, positions (absolute), ids}. Prefix part: the turn boundary before the
response and the one after it. Wording part: the question, the generation prompt and the turn
boundary after the answer. Response and answer tokens are not kept. About 105 MB per transcript
for Qwen3.6-27B (about 160 positions).

Usage: python3 src/forward.py --model qwen3.6-27b --save full [--sets scenario nopressure unrelated]
       python3 src/forward.py --model qwen3.6-27b --save crop --sets unrelated_extra --inline-readout --probe-vector
"""
import argparse
import os
import sys
import time

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from models import (ANSWER_LIMIT, append_jsonl, classify_answer, decode_generation, encode_marked,  # noqa: E402
                    generate, gpu_sanity, limit_for, load_model, logger, read_jsonl, seg,
                    setup_logging, slug)
from prompts import ANSWER_STYLE, SELF_REPORT  # noqa: E402

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
NAMES = ["system", "user_prompt", "response", "self_q"]


def residuals(L, ids, start):
    """[layers, len(ids) - start, d] bf16 on CPU: every block's output from position start on."""
    import torch
    from jlens.hooks import ActivationRecorder
    with torch.no_grad(), ActivationRecorder(L.lens_model.layers, at=range(L.n_layers)) as rec:
        L.lens_model.forward(torch.tensor([ids], device=L.device))
        acts = torch.stack([rec.activations[l][0, start:].detach().to(torch.bfloat16).cpu()
                            for l in range(L.n_layers)])
    return acts


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--model", required=True)
    ap.add_argument("--save", choices=["full", "crop"], required=True)
    ap.add_argument("--sets", nargs="+", default=["scenario", "nopressure", "unrelated"])
    ap.add_argument("--wordings", nargs="+", default=list(SELF_REPORT))
    ap.add_argument("--limit", type=int, default=None)
    ap.add_argument("--answer-limit", type=int, default=None, help="override (smoke tests)")
    ap.add_argument("--inline-readout", action="store_true",
                    help="export the readouts from the forward pass and do not save the residual streams")
    ap.add_argument("--probe-vector", action="store_true",
                    help="with --inline-readout: keep the residual at the token before the Q9_dyl answer")
    ap.add_argument("--template-residuals", action="store_true",
                    help="with --inline-readout: keep the residual streams at the template positions")
    ap.add_argument("--top-k", type=int, default=16, help="readout size (with --inline-readout)")
    ap.add_argument("--device", default=None)
    args = ap.parse_args()
    setup_logging()
    gpu_sanity()
    import torch

    run_dir = os.path.join(ROOT, "runs", slug(args.model))
    cache_dir = os.path.join(run_dir, "cache")
    seq_path = os.path.join(run_dir, "sequences.jsonl")
    rows_so_far = read_jsonl(seq_path)
    trs = [t for t in read_jsonl(os.path.join(run_dir, "transcripts.jsonl")) if t["set"] in args.sets]
    if args.limit:
        trs = trs[:args.limit]
    if args.inline_readout and args.save != "crop":
        sys.exit("FATAL: --inline-readout needs --save crop")
    if (args.probe_vector or args.template_residuals) and not args.inline_readout:
        sys.exit("FATAL: --probe-vector and --template-residuals are for --inline-readout "
                 "(otherwise the whole residual stream is saved)")

    def save_template(tdir, part, acts, start, pos, ids):
        torch.save({"acts": acts[:, [p - start for p in pos]].clone(), "positions": pos, "ids": [ids[p] for p in pos]},
                   os.path.join(tdir, f"template_{part}.pt"))
    L = load_model(args.model, args.device)
    tok = L.tokenizer
    ans_limit = args.answer_limit or limit_for(L.spec, ANSWER_LIMIT)
    if args.inline_readout:
        import readout as RO
        from dyl_probe import probe_position
        out_dir = os.path.join(ROOT, "exports", slug(args.model))
        os.makedirs(out_dir, exist_ok=True)
        R = RO.setup(L, args.model, args.top_k)
        RO.write_vocab(L, out_dir)
    # a wording part is done only if it was made with the current answer limit; otherwise it is
    # redone and the new row (appended later in the file) replaces the old one downstream
    done = {(r["tid"], r["part"]) for r in rows_so_far
            if r["part"] == "prefix" or r.get("answer_limit") == ans_limit}
    logger.info("%d transcripts, wordings %s, answer limit %d, save %s",
                len(trs), args.wordings, ans_limit, args.save)

    t0 = time.time()
    for n, t in enumerate(trs, 1):
        parts = ["prefix"] + args.wordings
        if all((t["tid"], p) in done for p in parts):
            continue
        base = [{"role": "system", "content": t["system"]}, {"role": "user", "content": t["user_prompt"]},
                {"role": "assistant", "content": t["response"]}]
        rendered = {}
        for w in args.wordings:
            rendered[w] = encode_marked(L, base + [{"role": "user", "content": SELF_REPORT[w]}], NAMES, True)
        # the prefix (everything before the question) must be the same tokens for every wording
        q_starts = {w: seg(s, "self_q")["start"] for w, (_, s) in rendered.items()}
        w0 = args.wordings[0]
        ids0, segs0 = rendered[w0]
        q0 = q_starts[w0]
        for w, (ids, _) in rendered.items():
            if q_starts[w] != q0 or ids[:q0] != ids0[:q0]:
                sys.exit(f"FATAL: the prefix of {t['tid']} tokenizes differently under {w}")
        prefix_ids = ids0[:q0]
        resp = seg(segs0, "response")
        tail = ids0[resp["end"]:q0]                      # post-response turn boundary
        tdir = os.path.join(cache_dir, t["tid"])
        os.makedirs(tdir, exist_ok=True)

        if (t["tid"], "prefix") not in done:
            start = 0 if args.save == "full" else seg(segs0, "user_prompt")["end"] - 1
            acts = residuals(L, prefix_ids, start)
            prefix_segs = [s for s in segs0 if s["name"] != "self_q" and s["name"] != "gen_prompt"]
            prefix_segs.append({"name": "post_response", "start": resp["end"], "end": q0})
            row = dict(tid=t["tid"], part="prefix", set=t["set"], ids=prefix_ids,
                       tokens=[tok.decode([i]) for i in prefix_ids], segments=prefix_segs, saved_start=start)
            if args.inline_readout:
                RO.export_part(L, R, row, t, acts, out_dir)
                if args.template_residuals:
                    pos = list(range(seg(segs0, "user_prompt")["end"], resp["start"])) + list(range(resp["end"], q0))
                    save_template(tdir, "prefix", acts, start, pos, prefix_ids)
            else:
                torch.save({"acts": acts, "start": start, "ids": prefix_ids}, os.path.join(tdir, "prefix.pt"))
            append_jsonl(seq_path, row)
            done.add((t["tid"], "prefix"))
            del acts

        for w in args.wordings:
            if (t["tid"], w) in done:
                continue
            ids, segs = rendered[w]
            g = decode_generation(L, generate(L, ids, ans_limit)[0])
            full = ids + g["ids"] + tail
            acts = residuals(L, full, q0)
            a0, a1 = len(ids), len(ids) + len(g["ids"])
            segs = [s for s in segs] + [{"name": "answer", "start": a0, "end": a1},
                                        {"name": "post_answer", "start": a1, "end": len(full)}]
            row = dict(
                tid=t["tid"], part=w, set=t["set"], ids=full, tokens=[tok.decode([i]) for i in full],
                segments=segs, saved_start=q0, question=SELF_REPORT[w],
                answer_text=g["text"], answer_reasoning=g["reasoning"], answer_finished=g["finished"],
                answer_n_tokens=g["n_tokens"], answer_limit=ans_limit,
                answer_label=classify_answer(g["text"], ANSWER_STYLE.get(w, "yesno")))
            if args.inline_readout:
                RO.export_part(L, R, row, t, acts, out_dir)
                if args.template_residuals:
                    save_template(tdir, w, acts, q0, list(range(q0, a0)) + list(range(a1, len(full))), full)
                if args.probe_vector and w == "Q9_dyl":
                    pos, _ = probe_position(row, bool(L.spec.get("harmony")))
                    if pos is not None:
                        torch.save({"acts": acts[:, pos - q0:pos - q0 + 1].clone(), "start": pos, "ids": full},
                                   os.path.join(tdir, f"{w}.pt"))
            else:
                torch.save({"acts": acts, "start": q0, "ids": full}, os.path.join(tdir, f"{w}.pt"))
            append_jsonl(seq_path, row)
            done.add((t["tid"], w))
            del acts
        if L.device.type == "cuda":
            torch.cuda.empty_cache()
        if n % 10 == 0 or n == len(trs):
            logger.info("%d/%d transcripts (%.0f s)", n, len(trs), time.time() - t0)
    if args.inline_readout:
        _, _, by_tid = RO.write_manifest(L, R, args.model, run_dir, out_dir)
        print(f"INLINE READOUT DONE: manifest lists {len(by_tid)} transcripts -> {out_dir}")
    print(f"FORWARD DONE: {args.model} -> {cache_dir}")


if __name__ == "__main__":
    main()
