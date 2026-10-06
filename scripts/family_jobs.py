#!/usr/bin/env python3
"""The list of family-generation units (PLAN.md Section 5.3) and the filled caller text for each
subagent call. Units: per model, the post-response slots (part "prefix"); for Qwen also, per
wording, the question tokens (in chunks of at most 8 positions, so one call reads at most 8
tables), the pre-answer slots, the think slots and the post-answer slots. Two replicates each.
A unit is done when analysis/families/<unit>_rep<k>.json exists.

Usage: python3 scripts/family_jobs.py [--lens J|LL] [--pending] [--show UNIT_REP]
"""
from __future__ import annotations

import argparse
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import common as C  # noqa: E402

sys.path.insert(0, os.path.join(C.ROOT, "src"))
from prompts import SELF_REPORT  # noqa: E402

FAM = os.path.join(C.ROOT, "analysis", "families")
CHUNK = 8


def units(lens):
    out = []
    for m in C.MODELS:
        with open(os.path.join(C.ROOT, "analysis", "freq", f"{C.slug(m)}_{lens}.json")) as f:
            tables = json.load(f)["tables"]
        out.append(dict(model=m, lens=lens, part="prefix", group="postresp", positions=sorted(tables["prefix"]), question="none"))
        if m != "qwen3.6-27b":
            continue
        for w in C.WORDINGS:
            names = sorted(tables[w], key=lambda nm: (nm.split("_")[0], int("".join(ch for ch in nm if ch.isdigit()) or 0)))
            q = [n for n in names if n.startswith("q_tok")]
            chunks = [q[i:i + CHUNK] for i in range(0, len(q), CHUNK)]
            for ci, chunk in enumerate(chunks):
                g = "question" if len(chunks) == 1 else f"question{chr(ord('a') + ci)}"
                out.append(dict(model=m, lens=lens, part=w, group=g, positions=chunk, question=SELF_REPORT[w]))
            for g in ("preans", "think", "postans"):
                out.append(dict(model=m, lens=lens, part=w, group=g, positions=[n for n in names if n.startswith(g + "_slot")], question=SELF_REPORT[w]))
    return out


def unit_name(u):
    return f"{C.slug(u['model'])}_{u['lens']}_{u['part']}_{u['group']}"


def caller_text(u, rep):
    name = unit_name(u)
    out = f"analysis/families/{name}_rep{rep}.json"
    q = u["question"] if u["question"] == "none" else f'"{u["question"]}"'
    if u["part"] == "prefix":
        q = "none (these positions come before the self-report question)"
    return f"""Project root: /Users/tliu/Desktop/Workspace/J-lens_lie_studies/redo_analysis (run every command from there).

Read /Users/tliu/Desktop/Workspace/J-lens_lie_studies/redo_analysis/prompts/family_generation.md and follow it exactly. The placeholders for this call:
- {{MODEL}} = {u['model']}
- {{SLUG}} = {C.slug(u['model'])}
- {{LENS}} = {u['lens']}
- {{PART}} = {u['part']}
- {{GROUP}} = {u['group']}
- {{POSITIONS}} = {' '.join(u['positions'])}
- {{QUESTION}} = {q}
- {{REPLICATE}} = {rep}
- {{OUT}} = {out}

So the table file is analysis/freq/{C.slug(u['model'])}_{u['lens']}_{u['part']}.md (read the first 400 rows of each of the {len(u['positions'])} position tables named above, and no other position), the matcher is scripts/match_seeds.py (pass --lens {u['lens']}), and you write only the {{OUT}} file (valid JSON; check it parses with python3 -c "import json; json.load(open('{out}'))"). Do not read any other file, and in particular nothing else under analysis/families/ and no table of the other lens (files with _{'J' if u['lens'] == 'LL' else 'LL'}_ in the name). If you need temporary files, put them in a private folder named after this call under your scratch directory (other calls run at the same time and share that directory). Finish with one line per position: the position name and the family names found."""


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--lens", default="J", choices=C.LENSES)
    ap.add_argument("--pending", action="store_true", help="list only calls whose output file is missing")
    ap.add_argument("--show", default=None, help="print the caller text for UNIT_rep<k>")
    args = ap.parse_args()
    us = units(args.lens)
    if args.show:
        for u in us:
            for rep in (1, 2):
                if f"{unit_name(u)}_rep{rep}" == args.show:
                    print(caller_text(u, rep))
                    return
        sys.exit("no such call")
    n_done = 0
    for u in us:
        for rep in (1, 2):
            done = os.path.exists(os.path.join(FAM, f"{unit_name(u)}_rep{rep}.json"))
            n_done += done
            if args.pending and done:
                continue
            print(f"{unit_name(u)}_rep{rep}  [{len(u['positions'])} positions]  {'done' if done else 'pending'}")
    print(f"\n{len(us)} units, {2 * len(us)} calls, {n_done} done")


if __name__ == "__main__":
    main()
