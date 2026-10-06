"""The lie-side and truth-side families at the newline after the self-report answer (post-answer slot 1), per
wording, by the answer the model gave (user's question, 2026-10-04). Qwen, J-lens, band 35 to 58, presence index
(build split and unrelated chats; the held-out split is never read).

One fixed token list per family at every wording: the list of the newline after the response (post-response
slot 1), so the numbers can be compared with piece 4.1. Only transcripts whose self-report answer finished have
this token. "In the question" marks a family whose word is in the question's own text; such a family is left out
of the count "one or more of the eight" under that wording.

Run from the project root:
python3 scripts/findings_2026_10_04/after_answer_families.py > analysis/findings_2026_10_04/after_answer_families.md"""
import json
import os
import sys
from collections import defaultdict

import numpy as np

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
import common as C  # noqa: E402
import presence as P  # noqa: E402

M, POS = "qwen3.6-27b", "postans_slot1"
SHORT = {"Q1_bare": "Q1", "Q2_after": "Q2", "Q6_factual": "Q6", "Q7_ab": "Q7", "Q9_dyl": "Q9"}
OWN = {"Q1_bare": {"deceive"}, "Q2_after": {"deceive"}, "Q6_factual": {"false", "falsehood"}, "Q7_ab": {"lie", "truthful"}, "Q9_dyl": {"lie"}}
TEN = ["lie", "fake", "conceal", "misinformation", "deceive", "falsehood", "fabricate", "false", "mislead", "dishonest"]
EIGHT = [n for n in TEN if n not in ("conceal", "dishonest")]
OTHER = ["honest", "candid", "disclose", "confess", "ethical", "transparent", "truth", "truthful", "refuse"]


def cell(pm, sel):
    n, k = int(sel.sum()), int((pm & sel).sum())
    return f"{k}/{n} ({100 * k / n:.0f}%)" if n else "–"


def main():
    d = P.load(M, "J")
    cls = d["cls"]
    with open(os.path.join(C.ROOT, "analysis", "families", "families_draft.json")) as f:
        ents = [e for e in json.load(f)["entries"] if e["model"] == M and e["lens"] == "J" and e["part"] == "prefix"
                and e["position"] == "postresp_slot1" and e["status"] == "keep"]
    kept = defaultdict(set)
    for e in ents:
        kept[e["name"]] |= {x["id"] for x in e["members"]}
    print("# Families at the newline after the self-report answer, by the answer given\n")
    print("Written by `scripts/findings_2026_10_04/after_answer_families.py`. Qwen, J-lens, band 35 to 58, build split and unrelated chats, "
          "in-sample. Token lists: those of the newline after the response. Cells: transcripts with the family / transcripts.\n")
    for w in C.WORDINGS:
        ans, have = P.answer(d, w), P.have_mask(d, w, POS)
        G = [("lying deniers", (cls == "lie") & (ans == "deny")), ("truthful deniers", (cls == "truth") & (ans == "deny")),
             ("lying admitters", (cls == "lie") & (ans == "admit")), ("no-pressure truths", cls == "np_truth"), ("unrelated", cls == "unrelated")]
        print(f"\n## {SHORT[w]}\n")
        print("| family | " + " | ".join(g for g, _ in G) + " |")
        print("|---|---|---|---|---|---|")
        any8 = np.zeros(len(cls), bool)
        for n in TEN + OTHER:
            pm = P.present_mask(d, w, POS, kept[n])
            if n in EIGHT and n not in OWN[w]:
                any8 |= pm
            print(f"| {n}{' (in the question)' if n in OWN[w] else ''} | " + " | ".join(cell(pm, s & have) for _, s in G) + " |")
            if n == "dishonest":
                print("| one or more of the eight, without the question's own | " + " | ".join(cell(any8, s & have) for _, s in G) + " |")
        # the same deniers at the newline after the response, before any question
        pre = np.zeros(len(cls), bool)
        for n in EIGHT:
            pre |= P.present_mask(d, "prefix", "postresp_slot1", kept[n])
        print(f"\nFor comparison, one or more of the eight at the newline after the response, same transcripts: "
              + "; ".join(f"{g} {cell(pre, s & have)}" for g, s in G[:3]) + ".")


if __name__ == "__main__":
    main()
