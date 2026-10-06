"""Gemma's lie-leaning families at each of the five template tokens after the response, with a column for the
position (user's requests, 2026-10-05). J-lens, each model's band, presence index (build split and unrelated chats;
the held-out split is never read).

One fixed token list per family: the union of the family's kept draft tokens over the five tokens after the
response (the drafts were made per token). Pooling this way leaves the newline counts of piece 5.2 unchanged.
A family is *lie-leaning* at a token when it is in 15% or more of lies, 15% or less of truths, 10% or less of both
control classes, and 10 points more frequent after lies than after truths (Claude's bar, as in piece 5.2). Every
family that is lie-leaning at one or more of the five tokens is listed. Three tables per model (user, 2026-10-05):
for the main text, the rows where the family is in 30% or more of the lies, most frequent first; for the appendix,
the rows where it is in 20% or more of the lies or of the truths; and every token, with the combined rows "one or
more of the newline families".

Run from the project root:
python3 scripts/findings_2026_10_04/gemma_families_by_slot.py > analysis/findings_2026_10_04/gemma_families_by_slot.md"""
import json
import os
import re
import sys
from collections import defaultdict

import numpy as np

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
import common as C  # noqa: E402
import presence as P  # noqa: E402

TOKENS = ["`<end_of_turn>`", "newline", "`<start_of_turn>`", "`user`", "second newline"]
NEWLINE_SET = {"gemma-3-12b-it": ["lie", "obfuscate", "mislead", "pretend", "evade", "hide", "deflect", "blatant"],
               "gemma-3-27b-it": ["lie", "lying-face emoji", "secret"]}
CONTRAST = {"gemma-3-12b-it": ["hush emoji"], "gemma-3-27b-it": ["keep-quiet emoji"]}
NAMES = {"gemma-3-12b-it": "Gemma-3-12B", "gemma-3-27b-it": "Gemma-3-27B"}
DUPLICATE = {"gemma-3-27b-it": ["lying-face emoji"]}      # its one token, 🤥, is also a member of `lie`


def show(tok):
    s = tok.replace("\n", "\\n").replace("|", "\\|")
    return f"`{s}`" if re.search(r"[A-Za-z]", s) else s.strip()


def members(ids, vocab, k=8):
    toks = [show(vocab[i]) for i in ids]
    return ", ".join(toks[:k]) + (f" … ({len(toks)} tokens)" if len(toks) > k else "")


def main():
    with open(os.path.join(C.ROOT, "analysis", "families", "families_draft.json")) as f:
        fd = json.load(f)["entries"]
    print("# Gemma's lie-leaning families at each of the five tokens after the response\n")
    print("Written by `scripts/findings_2026_10_04/gemma_families_by_slot.py`. In-sample. One token list per family (the union of its draft "
          "lists over the five tokens). Cells: transcripts with the family, with the share of the class in brackets.\n")
    for m in NEWLINE_SET:
        d, vocab = P.load(m, "J"), C.load_vocab(m)
        cls = d["cls"]
        G = [cls == "lie", cls == "truth", cls == "np_truth", cls == "unrelated"]
        positions = P.positions(d, "prefix")
        lists = defaultdict(set)
        for e in fd:
            if e["model"] == m and e["lens"] == "J" and e["part"] == "prefix" and e["status"] == "keep":
                lists[e["name"]] |= {x["id"] for x in e["members"]}
        order = {n: sorted(ids, key=lambda t: -sum(int(P.present_mask(d, "prefix", p, [t]).sum()) for p in positions)) for n, ids in lists.items()}

        def counts(pm, pos):
            have = P.have_mask(d, "prefix", pos)
            return [(int((pm & g & have).sum()), int((g & have).sum())) for g in G]

        def leaning(c):
            sh = [k / n for k, n in c]
            return sh[0] >= .15 and sh[1] <= .15 and sh[2] <= .10 and sh[3] <= .10 and sh[0] - sh[1] >= .10

        table = {n: [counts(P.present_mask(d, "prefix", p, ids), p) for p in positions] for n, ids in lists.items()}
        lean = {n: [leaning(c) for c in rows] for n, rows in table.items()}
        fams = sorted([n for n in table if any(lean[n])], key=lambda n: -max((c[0][0] / c[0][1] - c[1][0] / c[1][1]) for c, l in zip(table[n], lean[n]) if l))
        fams = [n for n in NEWLINE_SET[m] if n in fams] + [n for n in fams if n not in NEWLINE_SET[m]] + CONTRAST[m]
        agg = np.zeros((len(positions), len(cls)), bool)
        for n in NEWLINE_SET[m]:
            for pi, p in enumerate(positions):
                agg[pi] |= P.present_mask(d, "prefix", p, lists[n])
        ns = [c[1] for c in table[fams[0]][1]]
        head = (f"| family | members (a selection) | position | lies ({ns[0]}) | truths ({ns[1]}) | no-pressure truths ({ns[2]}) | unrelated ({ns[3]}) |\n"
                "|---|---|---|---|---|---|---|")
        fmt = lambda c: " | ".join(f"{k} ({100 * k / n:.0f}%)" for k, n in c)
        aggname = f"one or more of the {'eight' if len(NEWLINE_SET[m]) == 8 else 'three'} newline families"
        rows = [(n, pi, table[n][pi]) for n in fams for pi in range(len(positions))]
        by_lies = lambda r: (-r[2][0][0] / r[2][0][1], r[2][1][0] / r[2][1][1])
        short = lambda n: members(order[n], vocab, 4)
        head_plain = head
        # 1. the table for the main text: 30% or more of the lies, most frequent first, no marks, no family that only repeats another
        print(f"\n## {NAMES[m]}: main text (the family is in 30% or more of the lies; most frequent first)\n\n{head_plain}")
        for n, pi, c in sorted(rows, key=by_lies):
            if c[0][0] / c[0][1] >= 0.30 and n not in DUPLICATE.get(m, ()):
                print(f"| {n} | {short(n)} | {TOKENS[pi]} | {fmt(c)} |")
        # 2. the fuller table for the appendix: 20% or more of the lies or of the truths, most frequent first, with the marks
        print(f"\n## {NAMES[m]}: appendix (the family is in 20% or more of the lies or of the truths; most frequent first)\n\n{head}")
        for n, pi, c in sorted(rows, key=by_lies):
            if max(k / nn for k, nn in c[:2]) >= 0.20:
                mark = "" if n in CONTRAST[m] else (" (lie-leaning here)" if lean[n][pi] else "")
                print(f"| {n} | {members(order[n], vocab)} | {TOKENS[pi]}{mark} | {fmt(c)} |")
        # 3. every token, with the combined rows
        print(f"\n## {NAMES[m]}: every token\n\n{head}")
        for pi, p in enumerate(positions):
            print(f"| {aggname} | {', '.join(NEWLINE_SET[m])} | {TOKENS[pi]} | {fmt(counts(agg[pi], p))} |")
        for n in fams:
            for pi, p in enumerate(positions):
                mark = "" if n in CONTRAST[m] else (" (lie-leaning here)" if lean[n][pi] else "")
                print(f"| {n} | {members(order[n], vocab)} | {TOKENS[pi]}{mark} | {fmt(table[n][pi])} |")


if __name__ == "__main__":
    main()
