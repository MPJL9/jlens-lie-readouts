#!/usr/bin/env python3
"""Labelled counts behind the user's family decisions (PLAN.md Section 5.4; asked for on 2026-10-01,
when the user chose to see the lie / truth split before editing the families).

Reads the presence index (scripts/presence_index.py: build split and unrelated set only; the
held-out split is not read) and the merged family files (analysis/families/<unit>_merged.json).
Writes analysis/families/CHECKS.md and checks.json. For each group of readout tokens it counts the
transcripts in which the group is present in the band at a position, split into four classes:
scenario lies, scenario truths, no-pressure truths, unrelated chats. For Qwen's positions from
the self-report question on, it also splits lies and truths by the self-report answer.

Sections:
  1. the noun `truth`
  2. families whose side is "unclear" (moral and legal words, and others)
  3. single characters and word pieces that one replicate accepted and the other called ambiguous
  4. the borderline words (true, false, correct, wrong, accurate, fact ...)
The echo check (words of the context copied into the readout) is scripts/echo_check.py.

Usage: python3 scripts/family_checks.py
"""
from __future__ import annotations

import glob
import json
import os
import re
import sys
from collections import Counter, defaultdict

import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import common as C  # noqa: E402
import presence as P  # noqa: E402

FAM = os.path.join(C.ROOT, "analysis", "families")
QWEN = "qwen3.6-27b"
# moral and legal family names always listed in Section 2, whatever side the replicates gave them
MORAL_LEGAL = ["refuse", "violate", "violation", "ethics", "ethical", "unethical", "comply", "compliance", "illegal",
               "legal", "lawful", "moral", "immoral", "conscience", "unauthorized"]
MIN_SHARE = 0.05          # a position is listed when the group is present in at least this share of scenario transcripts

TRUTH_LATIN = {"truth", "truths", "wahrheit", "vérité", "verdad", "verdade", "verità", "правда"}
TRUTH_OTHER = {"真相", "实话", "说实话", "真理", "实情", "सच्चाई", "सत्य"}


def norm(s):
    return re.sub(r"\s+", " ", s.strip().lower())


def truth_ids(vocab):
    """The noun `truth` and its translations, by a fixed list of word forms."""
    return {i for i, s in enumerate(vocab) if s.strip(" _.").lower() in TRUTH_LATIN or s.strip() in TRUTH_OTHER}


def merged_files():
    out = []
    for p in sorted(glob.glob(os.path.join(FAM, "*_merged.json"))):
        with open(p) as f:
            out.append(json.load(f))
    return out


def borderline_group(s):
    s = s.lower()
    for key, name in (("incorrect", "incorrect"), ("inaccura", "inaccurate"), ("untru", "false"), ("fals", "false"),
                      ("wrong", "wrong"), ("mistake", "wrong"), ("error", "wrong"), ("correct", "correct"), ("accura", "accurate"),
                      ("fact", "fact"), ("truth", "truth"), ("true", "true"), ("real", "true"), ("right", "right"),
                      ("valid", "valid"), ("genuine", "genuine"), ("authentic", "genuine")):
        if key in s:
            return name
    return "other"


def rows_for(d, ids, part, min_share=MIN_SHARE, wording_split=True):
    """One row per position of the part where the group is visible enough."""
    out = []
    for pos in P.positions(d, part):
        c = P.counts(d, part, pos, ids)
        n_s = c["lie"][1] + c["truth"][1]
        if not n_s or (c["lie"][0] + c["truth"][0]) / n_s < min_share:
            continue
        row = dict(part=part, position=pos, **{k: list(v) for k, v in c.items()})
        if part != "prefix" and wording_split:
            ans, pm, hm = P.answer(d, part), P.present_mask(d, part, pos, ids), P.have_mask(d, part, pos)
            for lab in ("lie", "truth"):
                for a in ("admit", "deny"):
                    sel = hm & (d["cls"] == lab) & (ans == a)
                    row[f"{lab}_{a}"] = [int((pm & sel).sum()), int(sel.sum())]
        out.append(row)
    return out


def cell(v):
    return f"{v[0]}/{v[1]} ({P.pct(*v)})"


def table(rows, with_answers):
    head = "| part | position | lies | truths | no-pressure truths | unrelated |"
    sep = "|---|---|---|---|---|---|"
    if with_answers:
        head += " lies: admit | lies: deny | truths: admit | truths: deny |"
        sep += "---|---|---|---|"
    L = [head, sep]
    for r in rows:
        line = f"| {r['part']} | {r['position']} | {cell(r['lie'])} | {cell(r['truth'])} | {cell(r['np_truth'])} | {cell(r['unrelated'])} |"
        if with_answers:
            line += " " + " | ".join(cell(r[k]) if k in r else "" for k in ("lie_admit", "lie_deny", "truth_admit", "truth_deny")) + " |"
        L.append(line)
    return L


def main():
    files = merged_files()
    vocabs = {m: C.load_vocab(m) for m in C.MODELS}
    js = {}
    L = ["# Labelled counts behind the family decisions", "",
         "Written by `scripts/family_checks.py`. Build split only (the held-out split is not read), commentary",
         "transcripts dropped. Each cell is `present / transcripts (share)`: the number of transcripts in which at",
         "least one token of the group is in the top-16 readout at one or more band layers at that position.",
         "Classes: scenario lies, scenario truths, no-pressure truths (the same facts, no reason to lie), unrelated",
         "chats (Alpaca). For Qwen's positions from the question on, lies and truths are also split by the",
         f"self-report answer under that wording. A position is listed when the group is present in at least {MIN_SHARE:.0%}",
         "of the scenario transcripts. These counts were shown to the user before the family edits (user decision,",
         "2026-10-01), so AUROCs on the build split are partly in-sample; the held-out split is untouched.", ""]

    # ---------------------------------------------------------------- 1. truth
    L += ["## 1. The noun `truth`", "",
          "Token forms: `truth`, `truths` (any capitalization, leading space, `_` or `.`), 真相, 实话, 说实话, 真理, 实情,",
          "Wahrheit, vérité, verdad, verdade, verità, правда, सच्चाई, सत्य. `truthful` and 如实 are not included.", ""]
    js["truth"] = {}
    for m in C.MODELS:
        ids = truth_ids(vocabs[m])
        for lens in C.LENSES:
            d = P.load(m, lens)
            rows = sum((rows_for(d, ids, part) for part in d["present"]), [])
            js["truth"][f"{m}|{lens}"] = rows
            L += [f"### {m}, {'J-lens' if lens == 'J' else 'logit lens'}", ""]
            L += table(rows, m == QWEN) if rows else ["Not present in 5% of scenario transcripts at any position."]
            L.append("")

    # ---------------------------------------------------------------- 2. unclear families
    by_name = defaultdict(lambda: {"sides": Counter(), "entries": []})
    for f in files:
        for fam in f["families"]:
            e = by_name[norm(fam["name"])]
            e["sides"][fam["side"]] += 1
            e["entries"].append((f["model"], f["lens"], f["part"], fam))
    unclear = sorted((n for n, e in by_name.items() if n in MORAL_LEGAL
                      or (e["sides"]["unclear"] * 2 >= sum(e["sides"].values()) and sum(e["sides"].values()) >= 8)),
                     key=lambda n: -sum(by_name[n]["sides"].values()))
    L += ["## 2. Families whose side is \"unclear\"", "",
          "Family names given the side \"unclear\" in at least half of their entries (names with 8 or more entries),",
          "plus the moral and legal names (" + ", ".join(MORAL_LEGAL) + ") whatever their side.",
          "Each row is one family at one position, with that position's own member list. A family that is about the",
          "situation rather than the act should be as frequent in scenario truths as in scenario lies, and rarer in",
          "no-pressure truths.", ""]
    js["unclear"] = {}
    for m in C.MODELS:
        for lens in C.LENSES:
            d = P.load(m, lens)
            rows = []
            for n in unclear:
                for (m2, l2, part, fam) in by_name[n]["entries"]:
                    if (m2, l2) != (m, lens):
                        continue
                    ids = {x["id"] for x in fam["members"]}
                    c = P.counts(d, part, fam["position"], ids)
                    n_s = c["lie"][1] + c["truth"][1]
                    if n_s and (c["lie"][0] + c["truth"][0]) / n_s >= MIN_SHARE:
                        r = dict(name=n, part=part, position=fam["position"], **{k: list(v) for k, v in c.items()})
                        if part != "prefix":
                            ans, pm, hm = P.answer(d, part), P.present_mask(d, part, fam["position"], ids), P.have_mask(d, part, fam["position"])
                            for lab in ("lie", "truth"):
                                sel = hm & (d["cls"] == lab) & (ans == "deny")
                                r[f"{lab}_deny"] = [int((pm & sel).sum()), int(sel.sum())]
                        rows.append(r)
            js["unclear"][f"{m}|{lens}"] = rows
            pre = [r for r in rows if r["part"] == "prefix"]
            L += [f"### {m}, {'J-lens' if lens == 'J' else 'logit lens'}: post-response slots", ""]
            if pre:
                L += ["| family | position | lies | truths | no-pressure truths | unrelated |", "|---|---|---|---|---|---|"]
                for r in sorted(pre, key=lambda r: (r["name"], P.position_key(r["position"]))):
                    L.append(f"| {r['name']} | {r['position']} | {cell(r['lie'])} | {cell(r['truth'])} | {cell(r['np_truth'])} | {cell(r['unrelated'])} |")
            else:
                L.append("None present in 5% of scenario transcripts.")
            L.append("")
            if m == QWEN:
                L += [f"### {m}, {'J-lens' if lens == 'J' else 'logit lens'}: positions from the question on (each family's most visible position per wording and group)", "",
                      "| family | wording | position | lies | truths | no-pressure truths | unrelated | lies that deny | truths that deny |", "|---|---|---|---|---|---|---|---|---|"]
                best = {}
                for r in rows:
                    if r["part"] == "prefix":
                        continue
                    key = (r["name"], r["part"], r["position"].split("_")[0])
                    if key not in best or r["lie"][0] + r["truth"][0] > best[key]["lie"][0] + best[key]["truth"][0]:
                        best[key] = r
                for key in sorted(best, key=lambda k: (k[0], k[1], P.position_key(best[k]["position"]))):
                    r = best[key]
                    L.append(f"| {r['name']} | {r['part']} | {r['position']} | {cell(r['lie'])} | {cell(r['truth'])} | {cell(r['np_truth'])} | {cell(r['unrelated'])} | {cell(r['lie_deny'])} | {cell(r['truth_deny'])} |")
                L.append("")

    # ---------------------------------------------------------------- 3. disputed pieces
    L += ["## 3. Single characters and word pieces the two replicates disagreed on", "",
          "Tokens that one replicate accepted as a family member and the other listed as an ambiguous piece, in the",
          "same unit. Each row is one token at one position (positions with the token in 5% of scenario transcripts).", ""]
    disputed = defaultdict(set)             # (model, lens) -> token ids
    for p in sorted(glob.glob(os.path.join(FAM, "*_rep1.json"))):
        p2 = p.replace("_rep1.json", "_rep2.json")
        if not os.path.exists(p2):
            continue
        reps = [json.load(open(p)), json.load(open(p2))]
        acc = [{x["id"] for fam in r.get("families", []) for x in fam.get("members", [])} for r in reps]
        amb = [{a.get("id") for a in r.get("ambiguous_pieces", [])} for r in reps]
        disputed[(reps[0]["model"], reps[0]["lens"])] |= ((acc[0] & amb[1]) | (acc[1] & amb[0])) - {0, None}
    js["disputed"] = {}
    for m in C.MODELS:
        for lens in C.LENSES:
            d = P.load(m, lens)
            rows = []
            for t in sorted(disputed[(m, lens)]):
                for part in d["present"]:
                    for r in rows_for(d, {t}, part):
                        rows.append(dict(token=vocabs[m][t], id=t, **r))
            js["disputed"][f"{m}|{lens}"] = rows
            L += [f"### {m}, {'J-lens' if lens == 'J' else 'logit lens'}", ""]
            if rows:
                with_ans = m == QWEN
                L += ["| token | part | position | lies | truths | no-pressure truths | unrelated |" + (" lies that deny | truths that deny |" if with_ans else ""),
                      "|---|---|---|---|---|---|---|" + ("---|---|" if with_ans else "")]
                for r in rows:
                    line = f"| `{P.tok(r['token'])}` | {r['part']} | {r['position']} | {cell(r['lie'])} | {cell(r['truth'])} | {cell(r['np_truth'])} | {cell(r['unrelated'])} |"
                    if with_ans:
                        line += f" {cell(r['lie_deny']) if 'lie_deny' in r else ''} | {cell(r['truth_deny']) if 'truth_deny' in r else ''} |"
                    L.append(line)
            else:
                L.append("None present in 5% of scenario transcripts.")
            L.append("")

    # ---------------------------------------------------------------- 4. borderline words
    L += ["## 4. Borderline words", "",
          "Tokens the replicates listed as borderline, grouped by the family they would join (the most frequent",
          "suggestion per token): true (with real), false (with untrue), correct, incorrect, wrong, accurate,",
          "inaccurate, fact, right. The noun `truth` is Section 1.", ""]
    groups = defaultdict(lambda: defaultdict(Counter))       # (model, lens) -> token id -> group votes
    for f in files:
        for b in f.get("borderline", []):
            if b.get("id"):
                groups[(f["model"], f["lens"])][b["id"]][borderline_group(b.get("family_if_accepted", ""))] += 1
    js["borderline"] = {}
    order = ["true", "false", "correct", "incorrect", "wrong", "accurate", "inaccurate", "fact", "right"]
    for m in C.MODELS:
        tr = truth_ids(vocabs[m])
        for lens in C.LENSES:
            d = P.load(m, lens)
            by_group = defaultdict(set)
            for t, votes in groups[(m, lens)].items():
                g = votes.most_common(1)[0][0]
                if t not in tr and g != "truth" and t < len(vocabs[m]):
                    by_group[g].add(t)
            L += [f"### {m}, {'J-lens' if lens == 'J' else 'logit lens'}", ""]
            for g in order:
                ids = by_group.get(g, set())
                if not ids:
                    continue
                rows = sum((rows_for(d, ids, part) for part in d["present"]), [])
                js["borderline"][f"{m}|{lens}|{g}"] = dict(tokens=sorted(vocabs[m][t] for t in ids), rows=rows)
                forms = ", ".join(f"`{P.tok(vocabs[m][t])}`" for t in sorted(ids, key=lambda t: vocabs[m][t].strip().lower())[:25])
                L += [f"**{g}** ({len(ids)} token forms: {forms}{' …' if len(ids) > 25 else ''})", ""]
                L += table(rows, m == QWEN) if rows else ["Not present in 5% of scenario transcripts at any position."]
                L.append("")
    with open(os.path.join(FAM, "CHECKS.md"), "w") as f:
        f.write("\n".join(L))
    with open(os.path.join(FAM, "checks.json"), "w") as f:
        json.dump(js, f, ensure_ascii=False)
    print(f"CHECKS.md written ({len(L)} lines); unclear family names: {len(unclear)}")


if __name__ == "__main__":
    main()
