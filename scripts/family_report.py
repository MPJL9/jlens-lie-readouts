#!/usr/bin/env python3
"""PLAN.md Section 5.4: the family report for one unit (model x lens x part x position group),
from the two replicate files written by the family-generation subagents
(analysis/families/<slug>_<lens>_<part>_<group>_rep{1,2}.json).

Per family: members, layer profile (the band layers at which the family is present in at least
one transcript, and the three layers with the most transcripts; description only), visibility
(the number of build-split scenario transcripts in which at least one member is present at the
position; pooled, and split by label only with --with-labels). Then: the overlap between the
replicates (for each family of replicate 1, the replicate-2 family at the same position that
shares the most members, by Jaccard of member ids), candidate opposite pairs (a lie-side and a
truth-side family at the same position whose names or glosses contain antonym words from a
short list), and families whose name recurs at 3 or more positions.

Also writes the merged candidate list analysis/families/<unit>_merged.json: the union of the two
replicates' families, with members merged where a replicate-2 family matches a replicate-1
family (Jaccard >= 0.5); this is the file the user edits into families_v1.json.

Usage: python3 scripts/family_report.py --model gemma-3-27b-it --lens J --part prefix --group postresp [--with-labels]
"""
from __future__ import annotations

import argparse
import json
import os
import sys
from collections import defaultdict

import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import common as C  # noqa: E402
from frequency_tables import part_positions, prefix_positions  # noqa: E402

FAM = os.path.join(C.ROOT, "analysis", "families")
ANTONYMS = [("deceiv", "honest"), ("decept", "honest"), ("lie", "truth"), ("lying", "truthful"), ("dishonest", "honest"),
            ("hide", "reveal"), ("hid", "disclos"), ("conceal", "disclos"), ("conceal", "reveal"), ("secret", "open"),
            ("mislead", "candid"), ("evade", "admit"), ("evasi", "admit"), ("den", "admit"), ("den", "confess"),
            ("fake", "genuine"), ("pretend", "sincere"), ("withh", "share"), ("cover", "transparen")]


def load_reps(unit):
    reps = {}
    for k in (1, 2):
        p = os.path.join(FAM, f"{unit}_rep{k}.json")
        if os.path.exists(p):
            with open(p) as f:
                reps[k] = json.load(f)
    return reps


def presence(model, lens, part, families, band):
    """{(rep, family index): {tid: [layers present]}} over build-split scenario transcripts."""
    man = C.load_manifest(model)
    entries = C.entries(man, set="scenario", split="build")
    layers = man["layers"]
    layer_idx = [i for i, l in enumerate(layers) if band[0] <= l <= band[1]]
    members = {key: {m["id"] for m in fam["members"]} for key, fam in families.items()}
    out = {key: {} for key in families}
    labels = {}
    for e in entries:
        header, arrays = C.read_part(model, e, part)
        ids = arrays[lens + "_ids"]
        pos_map = prefix_positions(header) if part == "prefix" else part_positions(header)
        if part != "prefix" and not header.get("answer_finished", True):
            pos_map = {k: v for k, v in pos_map.items() if not k.startswith("postans_slot")}
        labels[e["tid"]] = e["label"]
        for key, fam in families.items():
            p = pos_map.get(fam["position"])
            if p is None:
                continue
            present = [layers[li] for li in layer_idx if any(int(t) in members[key] for t in ids[li, p])]
            if present:
                out[key][e["tid"]] = present
    return out, labels, len(entries)


def jaccard(a, b):
    return len(a & b) / len(a | b) if a | b else 0.0


def tok(s):
    s = s.replace("\n", "\\n").replace("|", "\\|")
    return "␣" + s[1:] if s.startswith(" ") else s


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--model", required=True, choices=C.MODELS)
    ap.add_argument("--lens", default="J", choices=C.LENSES)
    ap.add_argument("--part", default="prefix")
    ap.add_argument("--group", default="postresp")
    ap.add_argument("--with-labels", action="store_true", help="also show visibility split by lie / truth")
    args = ap.parse_args()
    unit = f"{C.slug(args.model)}_{args.lens}_{args.part}_{args.group}"
    reps = load_reps(unit)
    if not reps:
        sys.exit(f"no replicate files for {unit}")
    band = (C.BANDS if args.lens == "J" else C.BANDS_LL)[args.model]
    families = {}
    for k, rep in reps.items():
        for i, fam in enumerate(rep["families"]):
            families[(k, i)] = fam
    pres, labels, n_build = presence(args.model, args.lens, args.part, families, band)

    L = [f"# Family report: {args.model}, {'J-lens' if args.lens == 'J' else 'logit lens'}, band {band[0]}-{band[1]}, part {args.part}, group {args.group}", "",
         f"Written by `scripts/family_report.py` from `{unit}_rep1.json` and `_rep2.json` (prompt",
         f"`prompts/family_generation.md`). Visibility = build-split scenario transcripts (of {n_build}) in which",
         "at least one member is present at the position within the band. Layer profile = band layers where",
         "the family is present in at least one transcript, and the three layers with the most transcripts",
         "(description only; scoring uses the whole band).", ""]
    positions = sorted({f["position"] for f in families.values()},
                       key=lambda nm: (nm.split("_")[0], int("".join(ch for ch in nm if ch.isdigit()) or 0)))
    for pos in positions:
        L += [f"## {pos}", "",
              "| rep | family | side | members | visibility" + (" (lie / truth)" if args.with_labels else "") + " | layer profile |",
              "|---|---|---|---|---|---|"]
        for key in sorted(families, key=lambda k: (k[0], k[1])):
            fam = families[key]
            if fam["position"] != pos:
                continue
            pr = pres[key]
            vis = len(pr)
            if args.with_labels:
                nl = sum(1 for t in pr if labels[t] == "lie")
                vis_s = f"{vis} ({nl} / {vis - nl})"
            else:
                vis_s = str(vis)
            counts = defaultdict(int)
            for t, ls in pr.items():
                for l in ls:
                    counts[l] += 1
            if counts:
                lo, hi = min(counts), max(counts)
                top = sorted(counts, key=lambda l: -counts[l])[:3]
                prof = f"L{lo}-{hi}; most at " + ", ".join(f"L{l} ({counts[l]})" for l in sorted(top))
            else:
                prof = "—"
            mem = ", ".join(f"`{tok(m['token'])}`" for m in fam["members"])
            L.append(f"| {key[0]} | {fam['name']} ({fam['gloss']}) | {fam['side']} | {mem} | {vis_s} | {prof} |")
        L.append("")

    # replicate overlap
    if len(reps) == 2:
        L += ["## Replicate overlap", "", "For each replicate-1 family, the replicate-2 family at the same position sharing the most members.", "",
              "| position | rep-1 family | best rep-2 family | Jaccard of member ids | only in rep 1 | only in rep 2 |", "|---|---|---|---|---|---|"]
        matched2 = set()
        for key in sorted(k for k in families if k[0] == 1):
            f1 = families[key]
            ids1 = {m["id"] for m in f1["members"]}
            best, bj = None, 0.0
            for k2 in (k for k in families if k[0] == 2 and families[k]["position"] == f1["position"]):
                j = jaccard(ids1, {m["id"] for m in families[k2]["members"]})
                if j > bj:
                    best, bj = k2, j
            if best is not None:
                ids2 = {m["id"] for m in families[best]["members"]}
                matched2.add(best)
                only1 = ", ".join(f"`{tok(m['token'])}`" for m in f1["members"] if m["id"] not in ids2) or "—"
                only2 = ", ".join(f"`{tok(m['token'])}`" for m in families[best]["members"] if m["id"] not in ids1) or "—"
                L.append(f"| {f1['position']} | {f1['name']} | {families[best]['name']} | {bj:.2f} | {only1} | {only2} |")
            else:
                L.append(f"| {f1['position']} | {f1['name']} | — | 0 | all | — |")
        unmatched = [families[k] for k in families if k[0] == 2 and k not in matched2]
        L += ["", "Replicate-2 families not the best match of any replicate-1 family: " +
              (", ".join(f"{f['position']}: {f['name']}" for f in unmatched) or "none"), ""]

    # recurring names
    by_name = defaultdict(set)
    for fam in families.values():
        by_name[fam["name"].lower()].add(fam["position"])
    rec = {n: ps for n, ps in by_name.items() if len(ps) >= 3}
    L += ["## Families whose name recurs at 3 or more positions", ""]
    L += [f"- {n}: {', '.join(sorted(ps))}" for n, ps in sorted(rec.items())] or ["- none"]
    L.append("")

    # merged candidate list
    merged = []
    used2 = set()
    for key in sorted(k for k in families if k[0] == 1):
        f1 = dict(families[key])
        ids1 = {m["id"] for m in f1["members"]}
        for k2 in (k for k in families if k[0] == 2 and families[k]["position"] == f1["position"] and k not in used2):
            f2 = families[k2]
            if jaccard(ids1, {m["id"] for m in f2["members"]}) >= 0.5:
                used2.add(k2)
                have = {m["id"] for m in f1["members"]}
                f1["members"] = f1["members"] + [m for m in f2["members"] if m["id"] not in have]
                f1["merged_from"] = [f1["name"], f2["name"]]
                break
        merged.append(f1)
    for k2 in (k for k in families if k[0] == 2 and k not in used2):
        merged.append(dict(families[k2]))
    with open(os.path.join(FAM, f"{unit}_merged.json"), "w") as f:
        json.dump({"unit": unit, "model": args.model, "lens": args.lens, "part": args.part, "group": args.group, "band": list(band),
                   "families": merged,
                   "borderline": sum((r.get("borderline", []) for r in reps.values()), []),
                   "ambiguous_pieces": sum((r.get("ambiguous_pieces", []) for r in reps.values()), []),
                   "exclusions": sum((r.get("exclusions", []) for r in reps.values()), [])}, f, ensure_ascii=False, indent=1)
    # opposite pairs, on the merged list
    L += ["## Candidate opposite pairs (same position, lie side vs truth side, antonym words in the names or glosses; merged list)", ""]
    pairs = []
    for fa in merged:
        for fb in merged:
            if fa["position"] != fb["position"] or fa["side"] != "lie" or fb["side"] != "truth":
                continue
            ta, tb = (fa["name"] + " " + fa["gloss"]).lower(), (fb["name"] + " " + fb["gloss"]).lower()
            if any(x in ta and y in tb for x, y in ANTONYMS):
                pairs.append(f"- {fa['position']}: {fa['name']} / {fb['name']}")
    L += sorted(set(pairs)) or ["- none found by the word list; the user pairs by meaning"]
    L.append("")
    L += [f"Merged candidate list: `{unit}_merged.json` ({len(merged)} families; replicate-2 families sharing at least half",
          "their members with a replicate-1 family at the same position are folded into it).", ""]
    with open(os.path.join(FAM, f"{unit}_report.md"), "w") as f:
        f.write("\n".join(L))
    print(f"written: {unit}_report.md, {unit}_merged.json ({len(families)} families from {len(reps)} replicates)")


if __name__ == "__main__":
    main()
