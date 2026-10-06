#!/usr/bin/env python3
"""Which positions hold useful readouts (asked for by the user on 2026-10-02).

Qwen3.6-27B, J-lens, band 35-58. For every position that has draft families
(analysis/families/families_draft.json; kept entries, entries with the same name at one position
pooled, as in DRAFT_by_position_min20_TMP.md) it reports

  families     how many families are present in 20% or more of one or more groups
  fill         the share of readout entries (16 per band layer) taken by tokens of any draft
               family at that position, in scenario transcripts and in unrelated chats (entries
               excluded from scoring, such as the question's own word, count here too)
  lie-leaning  families present far more after lies: gap >= GAP and the truth rate <= CAP
  truth-leaning  the reverse
  everywhere   families present in 50% or more of unrelated chats
  situation    families present after 40% or more of lies and of truths, and in 10% or less of
               no-pressure truths and of unrelated chats

Before the self-report question the two rates are the shares among lies and among truths. From the
question on they are the shares among the lies and the truths whose self-report answer is a denial.

Class of a position (a provisional rule, to be replaced by the user's thresholds):
  signal      one or more lie-leaning families
  truth only  no lie-leaning family, one or more truth-leaning families
  words       three or more families, none leaning
  empty       fewer than three families

Reads the presence index (build split and unrelated set only; the held-out split is not read).
Writes analysis/positions/POSITION_MAP.md and position_map.json.

Usage: python3 scripts/position_map.py
"""
from __future__ import annotations

import json
import os
import sys
from collections import defaultdict

import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import common as C  # noqa: E402
import presence as P  # noqa: E402
from frequency_tables import part_positions  # noqa: E402

QWEN = "qwen3.6-27b"
OUT = os.path.join(C.ROOT, "analysis", "positions")
GAP, CAP = 0.30, 0.20
MIN_SHARE = 0.20
K = 16
CLASS_MARK = {"signal": "**S**", "truth only": "T", "words": "w", "empty": "·"}


def tokens_at_positions():
    """{part: {position: token text}} from one build-split transcript."""
    man = C.load_manifest(QWEN)
    e = next(x for x in man["transcripts"] if x["set"] == "scenario" and x["split"] == "build")
    out = {}
    h, _ = C.read_part(QWEN, e, "prefix", readouts=False)
    pm = C.positions({"tokens": h["tokens"], "segments": h["segments"]})
    out["prefix"] = {k: h["tokens"][v] for k, v in pm.items() if k.startswith("postresp_slot")}
    for w in C.WORDINGS:
        h, _ = C.read_part(QWEN, e, w, readouts=False)
        out[w] = {k: h["tokens"][v] for k, v in part_positions(h).items() if not k.startswith("ans_tok")}
    return out


def show(tok):
    return "`" + tok.replace("\n", "\\n").replace("|", "\\|") + "`"


def share(mask, sel):
    n = int(sel.sum())
    return (int((mask & sel).sum()) / n) if n else float("nan")


def fill(d, part, position, ids, sel):
    """Share of the readout entries of the selected transcripts taken by the tokens in ids."""
    tab = d["present"].get(part, {}).get(position, {})
    total = 0
    for t in ids:
        hit = tab.get(t)
        if hit is not None:
            total += int(hit[1][sel[hit[0].astype(int)]].sum())
    n = int(sel.sum())
    return total / (n * len(d["band_layers"]) * K) if n else float("nan")


def main():
    os.makedirs(OUT, exist_ok=True)
    d = P.load(QWEN, "J")
    cls = d["cls"]
    with open(os.path.join(C.ROOT, "analysis", "families", "families_draft.json")) as f:
        entries = [e for e in json.load(f)["entries"] if e["model"] == QWEN and e["lens"] == "J"]
    kept, every = defaultdict(lambda: defaultdict(set)), defaultdict(set)
    for e in entries:
        ids = {m["id"] for m in e["members"]} | {m["id"] for m in e.get("removed", [])}
        every[(e["part"], e["position"])] |= ids
        if e["status"] == "keep":
            kept[(e["part"], e["position"])][e["name"]] |= {m["id"] for m in e["members"]}
    toks = tokens_at_positions()
    scen = np.isin(cls, ["lie", "truth"])
    rows = []
    for part in ["prefix"] + C.WORDINGS:
        ans = P.answer(d, part) if part != "prefix" else None
        for pos in P.positions(d, part):
            hv = P.have_mask(d, part, pos)
            if part == "prefix":
                a_sel, b_sel = hv & (cls == "lie"), hv & (cls == "truth")
            else:
                a_sel, b_sel = hv & (cls == "lie") & (ans == "deny"), hv & (cls == "truth") & (ans == "deny")
            fams = []
            for name, ids in kept.get((part, pos), {}).items():
                pm = P.present_mask(d, part, pos, ids)
                r = dict(name=name, lie=share(pm, hv & (cls == "lie")), truth=share(pm, hv & (cls == "truth")),
                         np=share(pm, hv & (cls == "np_truth")), un=share(pm, hv & (cls == "unrelated")),
                         a=share(pm, a_sel), b=share(pm, b_sel))
                if max(r["lie"], r["truth"], r["np"], r["un"], r["a"], r["b"]) >= MIN_SHARE:
                    fams.append(r)
            lie_lean = sorted([r for r in fams if r["a"] - r["b"] >= GAP and r["b"] <= CAP], key=lambda r: r["b"] - r["a"])
            truth_lean = sorted([r for r in fams if r["b"] - r["a"] >= GAP and r["a"] <= CAP], key=lambda r: r["a"] - r["b"])
            everywhere = [r for r in fams if r["un"] >= 0.5]
            situation = [r for r in fams if r["lie"] >= 0.4 and r["truth"] >= 0.4 and r["np"] <= 0.1 and r["un"] <= 0.1]
            kind = ("signal" if lie_lean else "truth only" if truth_lean else "words" if len(fams) >= 3 else "empty")
            rows.append(dict(part=part, position=pos, token=toks[part].get(pos, "?"), families=len(fams), kind=kind,
                             fill_scenario=fill(d, part, pos, every[(part, pos)], hv & scen),
                             fill_unrelated=fill(d, part, pos, every[(part, pos)], hv & (cls == "unrelated")),
                             lie_lean=[(r["name"], r["a"], r["b"]) for r in lie_lean],
                             truth_lean=[(r["name"], r["a"], r["b"]) for r in truth_lean],
                             everywhere=len(everywhere), situation=len(situation),
                             n_a=int(a_sel.sum()), n_b=int(b_sel.sum())))
    with open(os.path.join(OUT, "position_map.json"), "w") as f:
        json.dump(rows, f, ensure_ascii=False, indent=1)

    def lean(xs, n=3):
        return ", ".join(f"{name} {100 * a:.0f}/{100 * b:.0f}" for name, a, b in xs[:n]) + (f" (+{len(xs) - n})" if len(xs) > n else "")

    L = ["# Which positions hold useful readouts (Qwen3.6-27B, J-lens, band 35-58)", "",
         "Written by `scripts/position_map.py`. Build split only; every number is in-sample. The class rule is",
         f"provisional: a family is *lie-leaning* when its rate after lies is {100 * GAP:.0f} points or more above its rate",
         f"after truths and the truth rate is {100 * CAP:.0f}% or less (*truth-leaning*: the reverse). From the question on,",
         "both rates are taken among the transcripts whose self-report answer is a denial.", "",
         "- **S** signal: one or more lie-leaning families.",
         "- T truth only: no lie-leaning family, one or more truth-leaning families.",
         "- w words: three or more families reach 20% in some group, none leans.",
         "- · empty: fewer than three families reach 20%.", "",
         "## 1. Template positions", "",
         "Each cell: class, then the number of families that reach 20% in some group.", "",
         "| position | token | " + " | ".join(w.split("_")[0] for w in C.WORDINGS) + " |", "|---|---|" + "---|" * len(C.WORDINGS)]
    by = {(r["part"], r["position"]): r for r in rows}
    template = [p for p in P.positions(d, "Q9_dyl") if not p.startswith("q_tok")]
    post = ["| position | token | class | families |", "|---|---|---|---|"]
    for pos in P.positions(d, "prefix"):
        r = by[("prefix", pos)]
        post.append(f"| {pos} | {show(r['token'])} | {CLASS_MARK[r['kind']]} | {r['families']} |")
    for pos in template:
        cells = []
        for w in C.WORDINGS:
            r = by.get((w, pos))
            cells.append(f"{CLASS_MARK[r['kind']]} {r['families']}" if r else "–")
        L.append(f"| {pos} | {show(by[('Q9_dyl', pos)]['token'])} | " + " | ".join(cells) + " |")
    L += ["", "Post-response slots (before the question; the same under every wording):", ""] + post
    L += ["", "## 2. Every position, with the leaning families", "",
          "`fill` = share of readout entries taken by tokens of any draft family, in scenario transcripts / in",
          "unrelated chats. Leaning families are shown as `name lie rate/truth rate` in percent (among deniers",
          "from the question on), strongest first, at most three.", ""]
    for part in ["prefix"] + C.WORDINGS:
        L += [f"### {'post-response slots' if part == 'prefix' else part}", "",
              "| position | token | class | families | fill | lie-leaning | truth-leaning | everywhere | situation |",
              "|---|---|---|---|---|---|---|---|---|"]
        for r in rows:
            if r["part"] != part:
                continue
            L.append(f"| {r['position']} | {show(r['token'])} | {CLASS_MARK[r['kind']]} | {r['families']} | "
                     f"{100 * r['fill_scenario']:.0f}% / {100 * r['fill_unrelated']:.0f}% | {lean(r['lie_lean']) or '–'} | "
                     f"{lean(r['truth_lean']) or '–'} | {r['everywhere']} | {r['situation']} |")
        L.append("")
    with open(os.path.join(OUT, "POSITION_MAP.md"), "w") as f:
        f.write("\n".join(L) + "\n")
    print(f"written: {os.path.join(OUT, 'POSITION_MAP.md')}")


if __name__ == "__main__":
    main()
