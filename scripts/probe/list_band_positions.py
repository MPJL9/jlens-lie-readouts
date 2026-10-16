#!/usr/bin/env python3
"""Lists the template positions of the four bands of scripts/probe/bands.py for one model, to be cut on the
cluster by src/cut_positions.py into runs/<model>/exp3_bands/: the data for scripts/probe/score_bands.py, which
redoes the post's difference-of-means probe (sections 4.4 and 4.6) on the other models (user, 2026-10-09).

Transcripts: the selection with commentary dropped (common.load_manifest), BOTH splits.
  prefix part     the scenario and no-pressure sets: every template token between the response and the
                  self-report question (the band after_response).
  each wording    the scenario set, answers that finished and open with yes or no (answer_label deny or admit):
                  every template token between the question and the answer (before_answer), the answer token
                  (answer) and every template token after the answer (after_answer). --wordings restricts the
                  wordings (all five by default; the post's 4.6 used Q9).
The token at every named position is checked to be the same across transcripts (the answer token excepted); a
transcript whose answer token cannot be placed (gpt-oss: no final-channel header) is listed under no wording
part and counted. Building the list reads the token positions of the held-out transcripts, not their labels or
readouts.

Output: inputs/exp3_cut_list_bands_<slug>.jsonl, rows as scripts/exp3/build_cut_list.py writes them (tid, set,
part, names, positions, ids; the cluster job checks the ids against the cache). Pushed by scripts/push_to_cluster.sh.
Then, on the cluster (the user submits; CPU job; LAYERS = the model's five band layers of Experiment 3 plus the
released probe's layer; DTYPE=float32 where the residual stream has values above 65,000):
  MODEL=gemma-3-12b-it LAYERS="17 23 29 35 40 46" LIST=inputs/exp3_cut_list_bands_gemma_3_12b_it.jsonl DTYPE=float32 OUT=exp3_bands sbatch --export=ALL slurm/exp3_cut.sh
  MODEL=gemma-3-27b-it LAYERS="27 33 39 46 52 58" LIST=inputs/exp3_cut_list_bands_gemma_3_27b_it.jsonl DTYPE=float32 OUT=exp3_bands sbatch --export=ALL slurm/exp3_cut.sh
  MODEL=gpt-oss-20b LAYERS="10 13 15 16 18 20" LIST=inputs/exp3_cut_list_bands_gpt_oss_20b.jsonl DTYPE=float32 OUT=exp3_bands sbatch --export=ALL slurm/exp3_cut.sh
Then scripts/pull_from_cluster.sh (it pulls exp3*/*.npy) and scripts/probe/score_bands.py --model ...

Usage: python3 scripts/probe/list_band_positions.py --model gemma-3-12b-it [--wordings Q9_dyl ...]
"""
import argparse
import collections
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.dirname(HERE))
sys.path.insert(0, HERE)
import common as C  # noqa: E402
import bands as B  # noqa: E402

D_MODEL = {"gemma-3-12b-it": 3840, "gemma-3-27b-it": 5376, "qwen3.6-27b": 5120, "gpt-oss-20b": 2880}   # for the size estimate only


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--model", required=True, choices=C.MODELS)
    ap.add_argument("--wordings", nargs="+", default=C.WORDINGS, choices=C.WORDINGS)
    args = ap.parse_args()
    model = args.model
    man = C.load_manifest(model)
    rows = {}
    for r in C.read_jsonl(os.path.join(C.RUNS, C.slug(model), "sequences.jsonl")):
        rows[(r["tid"], r["part"])] = r          # the last row per transcript and part is the current one

    out, n_vec, n_tr, skipped = [], collections.Counter(), collections.Counter(), collections.Counter()
    expect = {}                                   # (part kind, name) -> the token seen first; every other transcript must match
    for e in man["transcripts"]:
        if e["set"] not in ("scenario", "nopressure"):
            continue
        todo = [("prefix", None)]
        if e["set"] == "scenario":
            for w in args.wordings:
                a = e["wordings"][w]
                if a["answer_finished"] and a["answer_label"] in ("deny", "admit"):
                    todo.append((w, w))
                else:
                    skipped[(w, "answer not finished" if not a["answer_finished"] else f"answer {a['answer_label']}")] += 1
        n_tr[(e["set"], e["split"])] += 1
        for part, w in todo:
            r = rows[(e["tid"], part)]
            if part == "prefix":
                found = B.prefix_positions(r["tokens"], r["segments"])
            else:
                found, why = B.wording_positions(model, r["tokens"], r["segments"])
                if found is None:
                    skipped[(w, why)] += 1
                    continue
            for name, p in found:
                tok = r["tokens"][p]
                if name == "ans_tok0":
                    continue
                key = ("prefix" if part == "prefix" else "wording", name)
                if key not in expect:
                    expect[key] = tok
                elif expect[key] != tok:
                    sys.exit(f"FATAL: {e['tid']} {part} {name} is {tok!r}, every earlier transcript had {expect[key]!r}")
            names = [k for k, _ in found]
            out.append(dict(tid=e["tid"], set=e["set"], part=part, names=names,
                            positions=[p for _, p in found], ids=[r["ids"][p] for _, p in found]))
            for k in names:
                n_vec[(e["set"], e["split"], part, k)] += 1

    path = os.path.join(C.ROOT, "inputs", f"exp3_cut_list_bands_{C.slug(model)}.jsonl")
    with open(path, "w") as f:
        for row in out:
            f.write(json.dumps(row) + "\n")
    total = sum(n_vec.values())
    print(f"{len(out)} rows, {total} vectors -> {path}")
    print("transcripts per set and split:", dict(sorted(n_tr.items())))
    print("positions and the token at each (the same in every transcript):")
    for (kind, name), tok in sorted(expect.items(), key=lambda kv: (kv[0][0] != "prefix", B.order_key(kv[0][1]))):
        print(f"  {kind:8s} {name:15s} {tok!r}")
    print("vectors per position (scenario build / scenario held-out / no-pressure build / no-pressure held-out):")
    parts = ["prefix"] + list(args.wordings)
    for part in parts:
        names = sorted({k for (s, sp, p, k) in n_vec if p == part}, key=B.order_key)
        for k in names:
            c = [n_vec[(s, sp, part, k)] for s in ("scenario", "nopressure") for sp in ("build", "heldout")]
            print(f"  {part:11s} {k:15s} " + " / ".join(f"{v:3d}" for v in c))
    if skipped:
        print("transcripts listed under no wording part:")
        for (w, why), v in sorted(skipped.items()):
            print(f"  {w:11s} {why}: {v}")
    d = D_MODEL[model]
    print(f"size of the cut: {total} vectors x L layers x {d} x 4 bytes = {total * d * 4 / 1e9:.2f} GB per layer in float32 "
          f"({total * d * 2 / 1e9:.2f} GB in float16)")


if __name__ == "__main__":
    main()
