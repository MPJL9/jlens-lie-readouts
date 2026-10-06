#!/usr/bin/env python3
"""Build the model inputs (run once, on the Mac; the output is pushed to the cluster).

inputs/scenarios.jsonl: one row per MASK provided_facts scenario:
  id, split ("build" 60% / "heldout" 40%, fixed by seed 0 over sorted ids), system,
  user_prompt, proposition, true_statement, false_statement, no_pressure_system.
The true and false statements come from the proposition's two pivotal options
("X <pivotal>A/B</pivotal> Y"); formatted_ground_truth says which option is true.

inputs/unrelated.jsonl (only with --unrelated FILE): id, system, user_prompt.
inputs/unrelated_extra.jsonl (only with --unrelated-extra FILE): the same for the extra unrelated
set (1,000 more Alpaca prompts, none repeating the first set; src/build_unrelated.py).

Usage: python3 src/build_inputs.py [--unrelated prompts.jsonl] [--unrelated-extra prompts.jsonl]
"""
import argparse
import json
import os
import random
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from prompts import GENERIC_SYSTEM, NO_PRESSURE_SYSTEM  # noqa: E402

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PIVOTAL = re.compile(r"<pivotal>([^<]*)</pivotal>")
HELDOUT_SHARE = 0.4


def resolve(prop, side):
    m = PIVOTAL.search(prop)
    a, b = m.group(1).split("/", 1)
    return PIVOTAL.sub((a if side == "A" else b).strip(), prop, count=1)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--mask", default=os.path.join(ROOT, "data", "source", "mask_scenarios.jsonl"))
    ap.add_argument("--unrelated", default=None, help="jsonl with id, user_prompt")
    ap.add_argument("--unrelated-extra", default=None, help="jsonl with id, user_prompt (the extra unrelated set)")
    args = ap.parse_args()
    rows = [json.loads(l) for l in open(args.mask)]
    rows = sorted((r for r in rows if r["id"].startswith("mask_provided_facts")), key=lambda r: r["id"])
    ids = [r["id"] for r in rows]
    rng = random.Random(0)
    shuffled = ids[:]
    rng.shuffle(shuffled)
    heldout = set(shuffled[:round(HELDOUT_SHARE * len(ids))])
    out, mismatch = [], []
    for r in rows:
        side = r["formatted_ground_truth"]
        # the true statement is MASK's own ground_truth; the false one is the other pivotal option
        true_s, false_s = r["ground_truth"], resolve(r["proposition"], "B" if side == "A" else "A")
        resolved_true = resolve(r["proposition"], side)
        if resolved_true.rstrip(".").lower() != true_s.rstrip(".").lower():
            mismatch.append((r["id"], resolved_true, true_s))
        out.append(dict(id=r["id"], split="heldout" if r["id"] in heldout else "build",
                        system=r["system"], user_prompt=r["user_prompt"], proposition=r["proposition"],
                        true_statement=true_s, false_statement=false_s, ground_truth=r["ground_truth"],
                        no_pressure_system=NO_PRESSURE_SYSTEM.format(true_statement=true_s)))
    os.makedirs(os.path.join(ROOT, "inputs"), exist_ok=True)
    with open(os.path.join(ROOT, "inputs", "scenarios.jsonl"), "w") as f:
        for r in out:
            f.write(json.dumps(r, ensure_ascii=False) + "\n")
    n_held = sum(r["split"] == "heldout" for r in out)
    print(f"scenarios: {len(out)} ({len(out) - n_held} build, {n_held} held out) -> inputs/scenarios.jsonl")
    if mismatch:
        print(f"WARNING: {len(mismatch)} scenarios where the resolved true statement differs from "
              "MASK's ground_truth (first 5):")
        for m in mismatch[:5]:
            print("  ", m)
    if args.unrelated:
        un = [json.loads(l) for l in open(args.unrelated)]
        with open(os.path.join(ROOT, "inputs", "unrelated.jsonl"), "w") as f:
            for u in un:
                f.write(json.dumps(dict(id=u["id"], system=GENERIC_SYSTEM, user_prompt=u["user_prompt"]),
                                   ensure_ascii=False) + "\n")
        print(f"unrelated: {len(un)} prompts -> inputs/unrelated.jsonl")
    if args.unrelated_extra:
        un = [json.loads(l) for l in open(args.unrelated_extra)]
        first = {json.loads(l)["id"] for l in open(os.path.join(ROOT, "inputs", "unrelated.jsonl"))}
        if first & {u["id"] for u in un}:
            sys.exit("FATAL: the extra set repeats prompts of inputs/unrelated.jsonl")
        with open(os.path.join(ROOT, "inputs", "unrelated_extra.jsonl"), "w") as f:
            for u in un:
                f.write(json.dumps(dict(id=u["id"], system=GENERIC_SYSTEM, user_prompt=u["user_prompt"]),
                                   ensure_ascii=False) + "\n")
        print(f"unrelated, extra set: {len(un)} prompts -> inputs/unrelated_extra.jsonl")


if __name__ == "__main__":
    main()
