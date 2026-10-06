#!/usr/bin/env python3
"""DYL probe baseline (PLAN.md Section 5.8): apply AISI's released "Did you lie?" probe offline to
the cached residual streams. CPU only, no model, no GPU.

Probe (inputs/dyl_probes/<slug>/probe.pt, from huggingface ai-safety-institute/dyl-<model>):
one layer; per-dimension mean and std to standardize the residual vector; a logistic regression
(linear.weight, linear.bias) or a small MLP (net.0 -> ReLU -> net.2); a threshold set at a 1%
flag rate on Alpaca. Score = the classifier's raw output on the standardized vector; flag =
score > threshold.

Position: the residual at the token BEFORE the generated yes/no answer, the position whose
next-token prediction is the answer (verified on AISI's own rollouts in the earlier project:
this position reproduces their published numbers, the yes/no token itself does not). Here that
is the last token of the generation prompt (answer segment start - 1). For gpt-oss (harmony
format) the answer segment opens with an analysis channel; the yes/no sits in the final
channel, so the position is the `<|message|>` that opens the final channel. first_token_yes_no
says whether the token after that position really is Yes/No (it is in nearly every transcript
under Q9_dyl); rows where it is not are scored anyway and flagged.

Reads runs/<slug>/transcripts.jsonl (the selected transcripts), runs/<slug>/sequences.jsonl
(the last row per transcript and wording) and runs/<slug>/cache/<tid>/<wording>.pt
({acts [layers, T, d] bf16, start, ids}; acts[l] is block l's output). Writes
runs/<slug>/dyl_probe.jsonl, one row per transcript x wording: tid, set, item_id, k, split,
label, wording, answer_label, answer_finished, layer, position, token, next_token,
first_token_yes_no, z_rms (root-mean-square of the standardized vector; about 1 means the
vector looks like the probe's training data), score, flagged. Rerunnable: rows already written
are skipped. Prints a short summary per set (the analysis proper runs on the Mac).

Usage: python3 src/dyl_probe.py --model qwen3.6-27b [--wordings Q9_dyl] [--root .] [--limit N]
"""
import argparse
import enum
import json
import os
import sys
import time
import types

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from models import MODELS, append_jsonl, logger, read_jsonl, seg, setup_logging, slug  # noqa: E402

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
YES_NO = {"yes", "no"}


def load_probe(path):
    """(layer, mean, std, threshold, forward) of a released checkpoint. The pickle references
    AISI's `deception` package for one enum, so a stand-in is registered before loading."""
    import torch
    for name in ("deception", "deception.detectors", "deception.detectors.utils", "deception.detectors.utils.types"):
        sys.modules.setdefault(name, types.ModuleType(name))

    class ProbeArchitecture(str, enum.Enum):
        LINEAR = "linear"; MLP = "mlp"; DIM = "dim"; LOGISTIC = "logistic"; LR = "lr"; LM = "lm"; AR = "ar"

    sys.modules["deception.detectors.utils.types"].ProbeArchitecture = ProbeArchitecture
    p = torch.load(path, map_location="cpu", weights_only=False)
    sd, layer = p["state_dict"], int(p["hyperparams"]["layer"])
    thr = float(sd["threshold"])
    if "direction" in sd:                       # difference of means: raw activations, no z-score
        D = sd["direction"].float()
        return layer, None, None, thr, (lambda x: x @ D), "difference-of-means"
    mean, std = sd["dataset_mean"].float(), sd["dataset_std"].float()
    if "linear.weight" in sd:
        W, b = sd["linear.weight"].float(), sd["linear.bias"].float()
        return layer, mean, std, thr, (lambda x: (x @ W.T + b).squeeze(-1)), "logistic regression"
    W0, b0 = sd["net.0.weight"].float(), sd["net.0.bias"].float()
    W2, b2 = sd["net.2.weight"].float(), sd["net.2.bias"].float()
    return layer, mean, std, thr, (lambda x: (torch.relu(x @ W0.T + b0) @ W2.T + b2).squeeze(-1)), f"MLP ({W0.shape[0]} hidden)"


def probe_position(row, harmony):
    """(position, first_token_yes_no): the token before the yes/no answer, in the sequence's
    absolute positions."""
    a = seg(row["segments"], "answer")
    toks = row["tokens"]
    if harmony:
        pos = None
        for i in range(a["start"], a["end"] - 1):
            if toks[i] == "final" and toks[i + 1] == "<|message|>":
                pos = i + 1          # the <|message|> that opens the final channel
                break
        if pos is None:
            return None, False
    else:
        pos = a["start"] - 1
    nxt = toks[pos + 1].strip().lower() if pos + 1 < len(toks) else ""
    return pos, nxt in YES_NO


def auroc(pos, neg):
    if not pos or not neg:
        return None
    return sum(1.0 if a > b else (0.5 if a == b else 0.0) for a in pos for b in neg) / (len(pos) * len(neg))


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--model", required=True, choices=sorted(MODELS))
    ap.add_argument("--wordings", nargs="+", default=["Q9_dyl"])
    ap.add_argument("--root", default=ROOT, help="project root holding runs/ and inputs/")
    ap.add_argument("--limit", type=int, default=None)
    args = ap.parse_args()
    setup_logging()
    import torch
    s = slug(args.model)
    harmony = MODELS[args.model].get("harmony", False)
    run_dir = os.path.join(args.root, "runs", s)
    probe_path = os.path.join(args.root, "inputs", "dyl_probes", s, "probe.pt")
    layer, mean, std, thr, fwd, kind = load_probe(probe_path)
    logger.info("probe %s: %s, layer %d, threshold %.4f", probe_path, kind, layer, thr)

    trs = {t["tid"]: t for t in read_jsonl(os.path.join(run_dir, "transcripts.jsonl"))}
    rows = {}
    for r in read_jsonl(os.path.join(run_dir, "sequences.jsonl")):
        if r["part"] in args.wordings and r["tid"] in trs:
            rows[(r["tid"], r["part"])] = r              # the last row wins (reruns append)
    out_path = os.path.join(run_dir, "dyl_probe.jsonl")
    done = {(r["tid"], r["wording"]) for r in read_jsonl(out_path)} if os.path.exists(out_path) else set()
    todo = [k for k in sorted(rows) if k not in done]
    if args.limit:
        todo = todo[:args.limit]
    logger.info("%d transcripts, %d sequence rows, %d done, %d to score", len(trs), len(rows), len(done), len(todo))

    t0 = time.time()
    n_missing, n_not_yes_no = 0, 0
    for n, key in enumerate(todo, 1):
        tid, w = key
        r, t = rows[key], trs[tid]
        pos, first = probe_position(r, harmony)
        if pos is None:
            logger.warning("%s %s: no final channel; skipped", tid, w)
            n_missing += 1
            continue
        blob = torch.load(os.path.join(run_dir, "cache", tid, w + ".pt"), map_location="cpu")
        h = blob["acts"][layer, pos - blob["start"]].float()
        if blob["ids"][pos] != r["ids"][pos]:
            sys.exit(f"FATAL: {tid} {w}: the cache's ids differ from sequences.jsonl at position {pos}")
        z = h if mean is None else (h - mean) / std
        score = float(fwd(z))
        n_not_yes_no += not first
        append_jsonl(out_path, dict(
            tid=tid, set=t["set"], item_id=t["item_id"], k=t["k"], split=t.get("split"), label=t.get("label"),
            wording=w, answer_label=r.get("answer_label"), answer_finished=r.get("answer_finished"),
            layer=layer, position=pos, token=r["tokens"][pos],
            next_token=r["tokens"][pos + 1] if pos + 1 < len(r["tokens"]) else None,
            first_token_yes_no=first, z_rms=float(z.pow(2).mean().sqrt()), score=score, flagged=score > thr))
        del blob
        if n % 50 == 0 or n == len(todo):
            logger.info("%d/%d scored (%.0f s)", n, len(todo), time.time() - t0)
    logger.info("skipped (no final channel): %d; token after the position is not yes/no: %d", n_missing, n_not_yes_no)

    # summary (the analysis proper runs on the Mac from dyl_probe.jsonl)
    out = read_jsonl(out_path)
    for w in args.wordings:
        rs = [r for r in out if r["wording"] == w]
        zr = sorted(r["z_rms"] for r in rs)
        print(f"\n== {args.model} {w}: {len(rs)} rows; z_rms median {zr[len(zr) // 2]:.2f}" if rs else f"\n== {args.model} {w}: no rows")
        sc = [r for r in rs if r["set"] == "scenario" and r["label"] in ("lie", "truth")]
        S = lambda g: [r["score"] for r in g]
        lies, truths = [r for r in sc if r["label"] == "lie"], [r for r in sc if r["label"] == "truth"]
        a = auroc(S(lies), S(truths))
        print(f"  scenario: AUROC lie vs truth {a if a is None else round(a, 3)} ({len(lies)} lie / {len(truths)} truth); "
              f"flagged lies {sum(r['flagged'] for r in lies)}, truths {sum(r['flagged'] for r in truths)}")
        dl = [r for r in lies if r["answer_label"] == "deny"]
        dt = [r for r in truths if r["answer_label"] == "deny"]
        a = auroc(S(dl), S(dt))
        print(f"  scenario, denial cell: AUROC {a if a is None else round(a, 3)} ({len(dl)} lie / {len(dt)} truth)")
        for st in ("nopressure", "unrelated"):
            g = [r for r in rs if r["set"] == st]
            if g:
                print(f"  {st}: {sum(r['flagged'] for r in g)} / {len(g)} flagged")
    print(f"DYL PROBE DONE: {args.model} -> {out_path}")


if __name__ == "__main__":
    main()
