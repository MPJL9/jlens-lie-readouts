#!/usr/bin/env python3
"""PLAN.md Section 5.3, step 2 of "every variant is included": find every readout token at the
given positions that matches a seed word. Reads the frequency tables (analysis/freq/<slug>_<lens>.json,
written by scripts/frequency_tables.py); searches at any frequency, including tokens seen in one
transcript.

Matching rule: a token matches a seed when the seed, lower-cased and Unicode-normalized, is a
substring of the token, lower-cased, Unicode-normalized, with leading spaces and the "▁" marker
removed. So the seed "conceal" matches " conceal", "Conceal", "concealed", "concealment", and
"unconcealed"; the seed "lie" matches " lie", "lied", "believe" and "client" (the caller rejects
those). Seeds in other scripts match the same way (substring).

Usage:
  python3 scripts/match_seeds.py --model gemma-3-27b-it --lens J --part prefix \\
      --positions postresp_slot0 postresp_slot1 ... --seeds conceal hide 隐瞒 [--min-n 1] [--out file.json]
Prints a table per position: token, id, n (transcripts), layers with the count at each, and the
seeds it matched. --out also writes the matches as JSON.
"""
from __future__ import annotations

import argparse
import json
import os
import sys
import unicodedata

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import common as C  # noqa: E402

FREQ = os.path.join(C.ROOT, "analysis", "freq")


def norm(s):
    s = unicodedata.normalize("NFKC", s).replace("▁", " ").strip().lower()
    return s


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--model", required=True, choices=C.MODELS)
    ap.add_argument("--lens", default="J", choices=C.LENSES)
    ap.add_argument("--part", default="prefix", help='"prefix" (post-response slots) or a wording such as Q1_bare')
    ap.add_argument("--positions", nargs="+", required=True)
    ap.add_argument("--seeds", nargs="+", required=True)
    ap.add_argument("--min-n", type=int, default=1)
    ap.add_argument("--out", default=None)
    args = ap.parse_args()
    with open(os.path.join(FREQ, f"{C.slug(args.model)}_{args.lens}.json")) as f:
        data = json.load(f)
    seeds = [(s, norm(s)) for s in args.seeds]
    out = {}
    for pos in args.positions:
        table = data["tables"].get(args.part, {}).get(pos)
        if table is None:
            sys.exit(f"no table for part {args.part!r} position {pos!r} (available: {list(data['tables'].get(args.part, {}))})")
        hits = []
        for tid, row in table.items():
            ns = norm(row["s"])
            matched = [s for s, sn in seeds if sn and sn in ns]
            if matched and row["n"] >= args.min_n:
                hits.append({"token": row["s"], "id": int(tid), "n": row["n"], "layers": row["layers"], "seeds": matched})
        hits.sort(key=lambda h: (-h["n"], h["id"]))
        out[pos] = hits
        print(f"\n## {pos}: {len(hits)} matching tokens (of {len(table)}; {data['n_transcripts'][args.part][pos]} transcripts)")
        print("| token | id | n | layers (layer:count) | seeds |")
        print("|---|---|---|---|---|")
        for h in hits:
            tok = h["token"].replace("\n", "\\n").replace("|", "\\|")
            if tok.startswith(" "):
                tok = "␣" + tok[1:]
            lay = " ".join(f"{l}:{c}" for l, c in h["layers"].items())
            print(f"| `{tok}` | {h['id']} | {h['n']} | {lay} | {', '.join(h['seeds'])} |")
    if args.out:
        with open(args.out, "w") as f:
            json.dump({"model": args.model, "lens": args.lens, "part": args.part, "seeds": args.seeds, "matches": out}, f, ensure_ascii=False, indent=1)
        print(f"\nwritten: {args.out}")


if __name__ == "__main__":
    main()
