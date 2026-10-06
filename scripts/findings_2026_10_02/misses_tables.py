#!/usr/bin/env python3
"""family_findings.md Section 11.2: what the readouts of the 19 missed lies hold at post-response slot 1.

Table 1: fixed word groups (the member tokens are printed) among the 19 misses, the 133 caught lies, the 81
truths and the 138 no-pressure truths: present = in the top-16 at one or more band layers (35-58).
Table 2: one row per miss, numbered as in viewer/misses.html: the lie-side families outside the eight that
are present, and the content tokens with the most band layers (chat-template tokens, blank space and
punctuation left out, by the junk survey's kinds).
Writes analysis/misses/MISSES_TABLES.md. Run from the project root: python3 scripts/findings_2026_10_02/misses_tables.py
"""
from __future__ import annotations

import json
import os
import sys
from collections import defaultdict

import numpy as np

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
import common as C  # noqa: E402
import presence as P  # noqa: E402

M = "qwen3.6-27b"
POS = "postresp_slot1"
EIGHT = ["lie", "fake", "falsehood", "misinformation", "deceive", "fabricate", "false", "mislead"]
OUT = os.path.join(C.ROOT, "analysis", "misses", "MISSES_TABLES.md")
SKIP_KINDS = {"template", "whitespace", "punctuation"}
# fixed lists: a token belongs to a group if its text, stripped and lower-cased, is one of these words
GROUPS = {
    "reply / response / answer": ["reply", "replied", "replies", "response", "respond", "responded", "answer", "answered",
                                  "answers", "回答", "的回答", "回复", "答复", "回应", "答", "回答了"],
    "refuse": ["refuse", "refused", "refusal", "refuses", "refusing", "拒绝", "拒", "拒不", "拒絕"],
    "claim": ["claim", "claims", "claimed", "claiming", "声称", "宣称"],
    "deny": ["deny", "denied", "denial", "denies", "denying", "否认", "否認"],
    "explain": ["explain", "explained", "explanation", "explanations", "解释"],
    "polite": ["polite", "politely", "礼貌"],
}


def main():
    d = P.load(M, "J")
    cls, trs, vocab = d["cls"], d["transcripts"], C.load_vocab(M)
    with open(os.path.join(C.ROOT, "analysis", "families", "families_draft.json")) as f:
        ents = json.load(f)["entries"]
    fam, side = defaultdict(set), {}
    for e in ents:
        if e["model"] == M and e["lens"] == "J" and e["part"] == "prefix" and e["position"] == POS and e["status"] == "keep":
            fam[e["name"]] |= {x["id"] for x in e["members"]}
            side[e["name"]] = e["side"]
    with open(os.path.join(C.ROOT, "analysis", "junk", "kind_of_token.json")) as f:
        kind = {int(k): v for k, v in json.load(f).items()}
    hv = P.have_mask(d, "prefix", POS)
    masks = {n: P.present_mask(d, "prefix", POS, ids) & hv for n, ids in fam.items()}
    cnt = sum(masks[n].astype(int) for n in EIGHT)
    lies, truths, npt = (cls == "lie") & hv, (cls == "truth") & hv, (cls == "np_truth") & hv
    miss, caught = lies & (cnt == 0), lies & (cnt >= 1)
    other_lie = [n for n in fam if side[n] == "lie" and n not in EIGHT]
    tab = d["present"]["prefix"][POS]
    classes = [("misses", miss), ("caught lies", caught), ("truths", truths), ("no-pressure truths", npt)]

    def find(words):
        w = set(words)
        return sorted(i for i in tab if vocab[i].strip().lower() in w)

    L = ["# The readouts of the 19 missed lies at post-response slot 1 (Qwen3.6-27B, J-lens, band 35-58, build split)", "",
         "Written by `scripts/findings_2026_10_02/misses_tables.py`. In-sample. *present* = in the top 16 at one or more band layers.", "",
         "## Table 1. Fixed word groups", "",
         "| group | member tokens found at this position | misses | caught lies | truths | no-pressure truths |", "|---|---|---|---|---|---|"]
    for g, words in GROUPS.items():
        ids = find(words)
        cells = []
        for _, m in classes:
            a = int((P.present_mask(d, "prefix", POS, ids) & m).sum())
            cells.append(f"{a}/{int(m.sum())} ({100 * a / m.sum():.0f}%)")
        L.append(f"| {g} | {', '.join('`' + P.tok(vocab[i]) + '`' for i in ids)} | " + " | ".join(cells) + " |")
    ids = find(["隐瞒", "掩盖", "瞒"])
    cells = [f"{int((P.present_mask(d, 'prefix', POS, ids) & m).sum())}/{int(m.sum())} ({100 * (P.present_mask(d, 'prefix', POS, ids) & m).sum() / m.sum():.0f}%)" for _, m in classes]
    L.append(f"| conceal (the draft family) | {', '.join('`' + P.tok(vocab[i]) + '`' for i in ids)} | " + " | ".join(cells) + " |")
    L.append("")

    # Table 2, numbered as in the page
    miss_idx = sorted(np.where(miss)[0].tolist(), key=lambda i: (any(masks[n][i] for n in other_lie), i))
    rec = C.load_transcripts(M)
    L += ["## Table 2. Each miss: lie-side families outside the eight, and the content tokens with the most band layers", "",
          "Numbers as in `viewer/misses.html`. *content tokens* = chat-template tokens, blank space and punctuation left out;",
          "the number in brackets is how many of the 24 band layers hold the token in their top 16.", "",
          "| # | scenario | tokens | lie-side families outside the eight | content tokens with the most band layers |", "|---|---|---|---|---|"]
    for n, i in enumerate(miss_idx, 1):
        t = trs[i]
        top = []
        for tok_id, (ti, nl) in tab.items():
            h = np.where(ti == i)[0]
            if len(h) and kind.get(tok_id) not in SKIP_KINDS:
                top.append((int(nl[h[0]]), tok_id))
        top.sort(key=lambda x: (-x[0], x[1]))
        words = ", ".join(f"`{P.tok(vocab[tok_id])}` ({k})" for k, tok_id in top[:6])
        fams = ", ".join(x for x in other_lie if masks[x][i]) or "–"
        L.append(f"| {n} | {t['item_id'][-6:]} k{rec[t['tid']]['k']} | {rec[t['tid']]['n_tokens']} | {fams} | {words} |")
    L.append("")
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    with open(OUT, "w") as f:
        f.write("\n".join(L) + "\n")
    print("\n".join(L))
    print(f"written: {OUT}")


if __name__ == "__main__":
    main()
