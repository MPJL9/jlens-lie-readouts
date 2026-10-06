#!/usr/bin/env python3
"""family_findings.md Section 11, steps 3 and 4: compare the readings of the 69 responses (missed lies, false
alarms, caught lies, quiet truths). Two blind readers (A, B: sheets without labels) and two labelled readers
(C, D: sheets with the judge's label, the group and the families present) each gave every response one type:
false_fact, implication, evade, true_fact, mixed. Prompt: prompts/misses_reading.md.

Writes analysis/misses/READINGS.md:
  1. agreement between the two readers of each version;
  2. the types by group, blind and labelled;
  3. the five guesses of Section 11, each against the readings;
  4. the cases whose type changes between the blind and the labelled reading (where the label steers the reader);
  5. every case in one table.
Run from the project root after the readers have written analysis/misses/readings/*.json:
python3 scripts/findings_2026_10_02/misses_readings.py
"""
from __future__ import annotations

import json
import os
import sys
from collections import Counter, defaultdict

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
import common as C  # noqa: E402

D = os.path.join(C.ROOT, "analysis", "misses")
TYPES = ["false_fact", "implication", "evade", "true_fact", "mixed"]
GROUPS = ["miss", "caught lie", "false alarm", "quiet truth"]
READERS = {"blind": ["A", "B"], "labelled": ["C", "D"]}


def load_reading(version, r):
    with open(os.path.join(D, "readings", f"{version}_{r}.json")) as f:
        rows = json.load(f)
    out = {}
    for x in rows:
        t = x["type"].strip().lower()
        assert t in TYPES, (version, r, x)
        out[x["code"]] = dict(type=t, confidence=x.get("confidence", ""), note=x.get("note", ""))
    return out


def main():
    with open(os.path.join(D, "key.json")) as f:
        key = json.load(f)
    with open(os.path.join(D, "cases.json")) as f:
        cases = {c["idx"]: c for c in json.load(f)}
    R = {v: {r: load_reading(v, r) for r in rs} for v, rs in READERS.items()}
    codes = sorted(key)
    for v, rs in READERS.items():
        for r in rs:
            missing = [c for c in codes if c not in R[v][r]]
            assert not missing, (v, r, missing)
    L = ["# Missed lies and false alarms: the readings", "",
         "Written by `scripts/findings_2026_10_02/misses_readings.py`. Four readers (subagents) typed the 69 responses:",
         "A and B blind (no label on the sheet), C and D with the judge's label, the group and the families shown. Types:",
         "`false_fact` states the false fact; `implication` misleads by implication, framing or omission; `evade` gives",
         "neither fact; `true_fact` states the true fact; `mixed` states the true fact and something false, or fits no type.",
         "Prompt: `prompts/misses_reading.md`. Groups: 19 misses, 10 false alarms, 20 caught lies and 20 quiet truths",
         "(the last two drawn at random).", ""]

    # 1. agreement
    L += ["## 1. Agreement between the two readers of each version", "", "| version | readers agree | of | disagreements (type A / type B) |", "|---|---|---|---|"]
    for v, (r1, r2) in READERS.items():
        agree = sum(R[v][r1][c]["type"] == R[v][r2][c]["type"] for c in codes)
        pairs = Counter((R[v][r1][c]["type"], R[v][r2][c]["type"]) for c in codes if R[v][r1][c]["type"] != R[v][r2][c]["type"])
        L.append(f"| {v} ({r1}, {r2}) | {agree} | {len(codes)} | " + ", ".join(f"{a} / {b}: {n}" for (a, b), n in pairs.most_common()) + " |")
    L.append("")

    # consensus per version: the type if both agree, else "split (a / b)"
    def cons(v, c):
        a, b = (R[v][r][c]["type"] for r in READERS[v])
        return a if a == b else f"split"

    # 2. types by group
    for v in READERS:
        L += [f"## 2{'a' if v == 'blind' else 'b'}. Types by group, {v} reading", "",
              "Each reader's types are counted (two readers, so each group's row sums to twice its size).", "",
              "| group | n | " + " | ".join(TYPES) + " | both readers agree |", "|---|---|" + "---|" * (len(TYPES) + 1)]
        for g in GROUPS:
            cs = [c for c in codes if key[c]["group"] == g]
            cnt = Counter(R[v][r][c]["type"] for c in cs for r in READERS[v])
            agree = sum(cons(v, c) != "split" for c in cs)
            L.append(f"| {g} | {len(cs)} | " + " | ".join(str(cnt.get(t, 0)) for t in TYPES) + f" | {agree}/{len(cs)} |")
        L.append("")

    # 3. the five guesses
    def share(g, v, types):
        cs = [c for c in codes if key[c]["group"] == g]
        n = sum(R[v][r][c]["type"] in types for c in cs for r in READERS[v])
        return f"{n}/{2 * len(cs)}"

    L += ["## 3. The five guesses of Section 11", "",
          "Counts are reader-votes (two per case), blind reading unless said otherwise.", ""]
    L.append(f"1. **Misses are lies by implication or omission.** Votes for `implication` or `evade`: misses {share('miss', 'blind', {'implication', 'evade'})}, "
             f"caught lies {share('caught lie', 'blind', {'implication', 'evade'})}. Votes for `false_fact`: misses {share('miss', 'blind', {'false_fact'})}, "
             f"caught lies {share('caught lie', 'blind', {'false_fact'})}.")
    L.append(f"2. **Misses are borderline or wrong labels.** Blind votes for `true_fact` or `mixed` among misses: {share('miss', 'blind', {'true_fact', 'mixed'})} "
             f"(caught lies {share('caught lie', 'blind', {'true_fact', 'mixed'})}). Labelled readers who disagree with the judge's label: see Section 5.")
    L.append("3. **Misses have the lie far from the end.** By script (`COMPARISONS.md`): no. Misses 616 characters from the end against 554 for caught lies; the bins match.")
    L.append(f"4. **False alarms are truths that repeat the false claim to reject it, or contain a false statement.** Blind votes for `mixed` or `false_fact` among false alarms: "
             f"{share('false alarm', 'blind', {'mixed', 'false_fact'})} (quiet truths {share('quiet truth', 'blind', {'mixed', 'false_fact'})}); for `implication`: "
             f"{share('false alarm', 'blind', {'implication'})} ({share('quiet truth', 'blind', {'implication'})}); for `true_fact`: {share('false alarm', 'blind', {'true_fact'})} ({share('quiet truth', 'blind', {'true_fact'})}).")
    L.append("5. **False alarms come from a few scenarios.** By script: no. The 10 false alarms are 10 scenarios, and 7 of them have a lie sample that is caught.")
    L.append("")

    # 4. where the label steers
    L += ["## 4. Cases whose type changes between the blind and the labelled reading", "",
          "The blind consensus (both blind readers agree) against the labelled consensus. `split` = the two readers differ.", "",
          "| code | group | judge's label | blind | labelled | eight families |", "|---|---|---|---|---|---|"]
    changed = 0
    for c in codes:
        b, l = cons("blind", c), cons("labelled", c)
        if b != l:
            changed += 1
            L.append(f"| {c} | {key[c]['group']} | {key[c]['label']} | {b} | {l} | {', '.join(cases[key[c]['idx']]['eight']) or '–'} |")
    L += ["", f"{changed} of {len(codes)} cases change (counting a move into or out of a split).", ""]
    # direction: among lies, does the labelled reading move toward false_fact; among truths toward true_fact?
    moves = Counter()
    for c in codes:
        for rb in READERS["blind"]:
            for rl in READERS["labelled"]:
                tb, tl = R["blind"][rb][c]["type"], R["labelled"][rl][c]["type"]
                if tb != tl:
                    moves[(key[c]["label"], tb, tl)] += 1
    L += ["Reader-pair moves (each blind reader against each labelled reader, so four pairs per case), by the judge's label:", "",
          "| judge's label | blind type | labelled type | pairs |", "|---|---|---|---|"]
    for (lab, tb, tl), n in sorted(moves.items(), key=lambda x: -x[1])[:16]:
        L.append(f"| {lab} | {tb} | {tl} | {n} |")
    L.append("")

    # 5. every case
    L += ["## 5. Every case", "",
          "Answers = the five self-report answers Q1 Q2 Q6 Q7 Q9 (a admit, d deny, o other). Disagree = labelled readers who say the judge's label is wrong (from their notes: contains 'disagree').", "",
          "| code | group | label | answers | eight | A | B | C | D | disagree | C's note |", "|---|---|---|---|---|---|---|---|---|---|---|"]
    for c in codes:
        k = key[c]
        cs = cases[k["idx"]]
        ans = " ".join((cs["answers"][w][0] or "?")[0] for w in C.WORDINGS)
        dis = sum(1 for r in READERS["labelled"] if "disagree" in R["labelled"][r][c]["note"].lower() and "not disagree" not in R["labelled"][r][c]["note"].lower())
        note = R["labelled"]["C"][c]["note"].replace("|", "\\|").replace("\n", " ")[:220]
        L.append(f"| {c} | {k['group']} | {k['label']} | {ans} | {', '.join(cs['eight']) or '–'} | {R['blind']['A'][c]['type']} | {R['blind']['B'][c]['type']} | "
                 f"{R['labelled']['C'][c]['type']} | {R['labelled']['D'][c]['type']} | {dis} | {note} |")
    L.append("")
    with open(os.path.join(D, "READINGS.md"), "w") as f:
        f.write("\n".join(L) + "\n")
    print(f"written: {os.path.join(D, 'READINGS.md')}")


if __name__ == "__main__":
    main()
