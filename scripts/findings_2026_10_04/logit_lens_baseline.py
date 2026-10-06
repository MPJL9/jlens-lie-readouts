"""Baseline for the draft's Section 4.6: the logit lens at the same token, with more than the one `lie` row.
User's question, 2026-10-05: "what about other families of logit lens?"

Qwen3.6-27B, the newline after the response, band layers 35 to 58, top 16, build split; unrelated chats = the
first set of 158, as in the tables of 4.1. Three parts:
  A. the ten families of 4.1 with one fixed token list (the J-lens's draft lists), read with each lens;
  B. the detectors of 4.4 with the same lists, read with each lens (build split only, in-sample);
  C. the logit lens's own draft families at this token (proposed from the logit lens's frequency table), those
     in 20% or more of lies or of truths.

Run from the project root:
python3 scripts/findings_2026_10_04/logit_lens_baseline.py > analysis/findings_2026_10_04/logit_lens_baseline.md"""
import json
import os
import sys
from collections import defaultdict

import numpy as np

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
import common as C  # noqa: E402
import presence as P  # noqa: E402

M, POS = "qwen3.6-27b", "postresp_slot1"
TEN = ["lie", "fake", "conceal", "misinformation", "deceive", "falsehood", "fabricate", "false", "mislead", "dishonest"]
EIGHT = [n for n in TEN if n not in ("conceal", "dishonest")]
LENS_NAME = {"J": "J-lens", "LL": "logit lens"}


def families(lens):
    with open(os.path.join(C.ROOT, "analysis", "families", "families_draft.json")) as f:
        ents = json.load(f)["entries"]
    fam, side, toks = defaultdict(set), {}, defaultdict(list)
    for e in ents:
        if e["model"] == M and e["lens"] == lens and e["part"] == "prefix" and e["position"] == POS and e["status"] == "keep":
            fam[e["name"]] |= {x["id"] for x in e["members"]}
            side[e["name"]] = e["side"]
            toks[e["name"]] += [x.get("token", "") for x in e["members"]]
    return fam, side, toks


def auroc(pos, neg):
    """The probability that a random positive scores above a random negative (ties count half)."""
    pos, neg = np.asarray(pos, float), np.asarray(neg, float)
    return float(((pos[:, None] > neg[None, :]).sum() + 0.5 * (pos[:, None] == neg[None, :]).sum()) / (len(pos) * len(neg)))


def cell(m, g):
    return f"{int((m & g).sum())} ({(m & g).sum() / g.sum():.0%})"


def main():
    famJ, _, _ = families("J")
    data = {lens: P.load(M, lens) for lens in ("J", "LL")}
    out = {}
    for lens, d in data.items():
        cls = d["cls"]
        hv = P.have_mask(d, "prefix", POS)
        first = np.array([t["set"] != "unrelated_extra" for t in d["transcripts"]])
        groups = {"lies": (cls == "lie") & hv, "truths": (cls == "truth") & hv, "no-pressure truths": (cls == "np_truth") & hv,
                  "unrelated": (cls == "unrelated") & hv & first}
        out[lens] = (d, hv, groups)
    gJ = out["J"][2]
    head = " | ".join(f"{k} ({int(v.sum())})" for k, v in gJ.items())

    print("# The logit lens at the newline after the response (baseline for Section 4.6)\n")
    print("Qwen3.6-27B, layers 35 to 58, top 16 per layer, build split. A family is present when one of its tokens is in")
    print("the top 16 at one or more band layers. Unrelated chats: the first set of 158, as in the tables of 4.1.\n")
    print("## A. The ten families of 4.1, one fixed token list (the J-lens's draft lists), read with each lens\n")
    print(f"| family | tokens | lens | {head} |")
    print("|---|---|---|---|---|---|---|")
    masks = {}
    for n in TEN:
        for lens in ("J", "LL"):
            d, hv, g = out[lens]
            m = P.present_mask(d, "prefix", POS, famJ[n]) & hv
            masks[(lens, n)] = m
            print(f"| {n if lens == 'J' else ''} | {len(famJ[n]) if lens == 'J' else ''} | {LENS_NAME[lens]} | " + " | ".join(cell(m, v) for v in g.values()) + " |")

    print("\n## B. The detectors of 4.4 with the same lists, read with each lens (build split, in-sample)\n")
    print(f"| detector | lens | {head} | AUROC, lies against truths |")
    print("|---|---|---|---|---|---|---|")
    for lens in ("J", "LL"):
        d, hv, g = out[lens]
        cnt = sum(masks[(lens, n)].astype(int) for n in EIGHT)
        rows = [("the `lie` family", masks[(lens, "lie")], masks[(lens, "lie")].astype(int)),
                ("one or more of the eight", cnt >= 1, (cnt >= 1).astype(int)),
                ("two or more of the eight", cnt >= 2, (cnt >= 2).astype(int)),
                ("the count of the eight, as a score", None, cnt)]
        for name, m, score in rows:
            cells = " | ".join(cell(m, v) for v in g.values()) if m is not None else " |  |  | "
            print(f"| {name} | {LENS_NAME[lens]} | {cells} | {auroc(score[g['lies']], score[g['truths']]):.2f} |")

    famL, sideL, toksL = families("LL")
    d, hv, g = out["LL"]
    own = [n for n in EIGHT if n in famL]
    ownm = {n: P.present_mask(d, "prefix", POS, famL[n]) & hv for n in own}
    cnt = sum(ownm[n].astype(int) for n in own)
    print(f"| the `lie` family, the logit lens's own list | logit lens | " + " | ".join(cell(ownm["lie"], v) for v in g.values())
          + f" | {auroc(ownm['lie'][g['lies']].astype(int), ownm['lie'][g['truths']].astype(int)):.2f} |")
    for k in (1, 2):
        print(f"| {'one' if k == 1 else 'two'} or more of the logit lens's own families of the same names ({', '.join(own)}) | logit lens | "
              + " | ".join(cell(cnt >= k, v) for v in g.values()) + f" | {auroc((cnt >= k)[g['lies']].astype(int), (cnt >= k)[g['truths']].astype(int)):.2f} |")
    print(f"| the count of those {len(own)}, as a score | logit lens |  |  |  |  | {auroc(cnt[g['lies']], cnt[g['truths']]):.2f} |")
    print("\nThe word lists of the first eight rows were chosen from the J-lens's readouts, which favours the J-lens. The last")
    print("four rows use the lists proposed from the logit lens's own readouts. It has no `misinformation` family: its `falsehood`")
    print("family holds the tokens `misinformation` and 虚假信息.")

    print("\n## C. The logit lens's own draft families at this token, in 20% or more of lies or of truths\n")
    rows = []
    for n in famL:
        m = P.present_mask(d, "prefix", POS, famL[n]) & hv
        a, b = (m & g["lies"]).sum() / g["lies"].sum(), (m & g["truths"]).sum() / g["truths"].sum()
        if max(a, b) >= 0.20:
            rows.append((a - b, n, m))
    rows.sort(key=lambda r: -r[0])
    print(f"{len(famL)} draft families were kept for the logit lens at this token; {len(rows)} are in 20% or more of lies or of truths.")
    print("Sorted by the share of lies minus the share of truths.\n")
    print(f"| family | side | members (a selection) | {head} | lies minus truths |")
    print("|---|---|---|---|---|---|---|---|")
    for gap, n, m in rows:
        sel = ", ".join(f"`{t.strip()}`" for t in toksL[n][:5] if t.strip()) + (f" … ({len(famL[n])} tokens)" if len(famL[n]) > 5 else "")
        print(f"| {n} | {sideL[n]} | {sel} | " + " | ".join(cell(m, v) for v in g.values()) + f" | {gap * 100:+.0f} points |")


if __name__ == "__main__":
    main()
