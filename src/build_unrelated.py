#!/usr/bin/env python3
"""Build the unrelated-chat prompts from Alpaca (tatsu-lab/alpaca, CC BY-NC 4.0). Runs on the Mac.

Alpaca is the benign set used for false-alarm calibration by Goldowsky-Dill et al. 2025
(arXiv:2502.03407), Liars' Bench (arXiv:2511.16035) and UK AISI (arXiv:2606.12618).

Filtering, in order:
  1. drop instructions that ask for false, wrong, opposite or made-up content, or for role
     play or fiction (these are the known false alarms of deception detectors on Alpaca);
  2. drop exact duplicates;
  3. drop prompts under 20 or over 1,000 characters;
  4. draw N prompts at random (seed 0), stratified over prompt-length quartiles.
The prompt is the instruction, followed by a blank line and the input when there is one.

Output: data/source/alpaca_unrelated.jsonl (id, user_prompt, dropped-rule counts in the log);
then run  python3 src/build_inputs.py --unrelated data/source/alpaca_unrelated.jsonl

The extra set (user decision, 2026-10-01: 1,000 more prompts, none repeating the first 300) is
drawn the same way from the prompts that are left after removing the first set, with seed 1:
    python3 src/build_unrelated.py --n 1000 --seed 1 --exclude data/source/alpaca_unrelated.jsonl \
        --out data/source/alpaca_unrelated_extra.jsonl
    python3 src/build_inputs.py --unrelated-extra data/source/alpaca_unrelated_extra.jsonl
The length bands are the quartiles of the whole filtered pool, as for the first set.

Usage: python3 src/build_unrelated.py [--n 300] [--seed 0] [--exclude FILE] [--out FILE]
"""
import argparse
import json
import os
import random
import re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
REPO, FILE = "tatsu-lab/alpaca", "data/train-00000-of-00001-a09b74b3ef9c3b56.parquet"
FALSEHOOD = re.compile(
    r"\b(incorrect(ly)?|false(ly|hood)?|untrue|wrong(ly)?|lie|lies|lying|liar|mislead\w*|deceiv\w*|decept\w*"
    r"|fake|fabricat\w*|made[- ]up|make up|invent(ed)?|pretend\w*|imagin\w*|fiction\w*|story|stories"
    r"|poem|role[- ]?play|opposite|contradict\w*|antonym\w*|sarcas\w*|exaggerat\w*|mistake|error|typo)\b",
    re.I)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--n", type=int, default=300)
    ap.add_argument("--seed", type=int, default=0)
    ap.add_argument("--exclude", default=None, help="jsonl of prompts already drawn (their ids are left out)")
    ap.add_argument("--out", default=os.path.join(ROOT, "data", "source", "alpaca_unrelated.jsonl"))
    args = ap.parse_args()
    import pandas as pd
    from huggingface_hub import hf_hub_download
    df = pd.read_parquet(hf_hub_download(REPO, FILE, repo_type="dataset"))
    rows = []
    for i, r in df.iterrows():
        prompt = r["instruction"].strip() + (("\n\n" + r["input"].strip()) if r["input"].strip() else "")
        rows.append((i, prompt))
    n0 = len(rows)
    rows = [(i, p) for i, p in rows if not FALSEHOOD.search(p)]
    n1 = len(rows)
    seen, uniq = set(), []
    for i, p in rows:
        if p not in seen:
            seen.add(p)
            uniq.append((i, p))
    rows = [(i, p) for i, p in uniq if 20 <= len(p) <= 1000]
    print(f"Alpaca {n0} -> {n1} after the falsehood/fiction filter -> {len(uniq)} unique -> {len(rows)} by length")
    rows.sort(key=lambda x: len(x[1]))
    q = len(rows) // 4
    taken = set()
    if args.exclude:
        taken = {json.loads(l)["id"] for l in open(args.exclude) if l.strip()}
        print(f"leaving out the {len(taken)} prompts of {args.exclude}")
    rng = random.Random(args.seed)
    pick = []
    for b in range(4):
        band = rows[b * q:(b + 1) * q] if b < 3 else rows[3 * q:]
        band = [(i, p) for i, p in band if f"alpaca_{i}" not in taken]
        pick += rng.sample(band, args.n // 4 + (1 if b < args.n % 4 else 0))
    pick.sort()
    assert not {f"alpaca_{i}" for i, _ in pick} & taken
    out = args.out
    with open(out, "w") as f:
        for i, p in pick:
            f.write(json.dumps(dict(id=f"alpaca_{i}", user_prompt=p), ensure_ascii=False) + "\n")
    print(f"{len(pick)} prompts -> {out}")


if __name__ == "__main__":
    main()
