#!/usr/bin/env python3
"""The survey of readouts that are not about deception: sorting tokens into kinds and counting.

Qwen3.6-27B, J-lens, band 35-58; positions as in scripts/junk_sheets.py. Kinds: analysis/junk/kinds.json
(merged from the two stage-1 proposals).

  python3 scripts/junk_report.py --prepare
      Sorts by a fixed rule the tokens of the three "no meaning" kinds (chat-template tokens; blank
      space; tokens with no letter and no digit) and writes the rest to analysis/junk/tokens_to_sort.md,
      the list two subagents sort (prompts/junk_assign.md -> assign_rep1.json, assign_rep2.json).

  python3 scripts/junk_report.py
      Reads the two assignments and writes analysis/junk/JUNK.md: for each position the share of the
      readout entries (16 per band layer) that each kind takes, over the build-split scenario
      transcripts and the unrelated chats. A token counts for a kind when the rule gives it or when
      both subagents chose it; tokens they disagree on and tokens outside the sorted list are shown
      as their own columns.
"""
from __future__ import annotations

import argparse
import json
import os
import sys
import unicodedata
from collections import Counter, defaultdict

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import common as C  # noqa: E402
from junk_sheets import OUT, READ_POSITIONS, REFERENCE, TOKEN_AT, COVER, TOP_N, show  # noqa: E402

TEMPLATE_EXTRA = {"<think>", "</think>", "<tool_call>", "</tool_call>", "<tool_response>", "</tool_response>"}
POSITIONS = [p for _, p in READ_POSITIONS] + [REFERENCE[1]]


def by_rule(tok):
    """The kind a fixed rule gives a token, or None."""
    s = tok.strip()
    if (s.startswith("<|") and s.endswith("|>")) or s in TEMPLATE_EXTRA:
        return "template"
    if s == "":
        return "whitespace"
    if not any(unicodedata.category(ch)[0] in "LN" for ch in tok):
        return "punctuation"
    return None


def load():
    with open(os.path.join(OUT, "top_tokens.json")) as f:
        top = json.load(f)
    with open(os.path.join(OUT, "kinds.json")) as f:
        kinds = json.load(f)["kinds"]
    return top, kinds


def listed(top):
    """{token id: (token, [positions])}: at each position the tokens up to COVER of the entries."""
    out = {}
    for pos in POSITIONS:
        cum = 0.0
        for r in top[pos][:TOP_N]:
            out.setdefault(r["id"], (r["token"], []))[1].append(pos)
            cum += r["share"]
            if cum >= COVER:
                break
    return out


def prepare():
    top, _ = load()
    todo = {i: v for i, v in listed(top).items() if by_rule(v[0]) is None}
    L = ["# Tokens to sort into kinds", "", "One line per token: its id, the token, the positions where it is frequent.",
         "`␣` is a leading space.", ""]
    for i, (tok, pos) in sorted(todo.items(), key=lambda x: (-len(x[1][1]), x[0])):
        L.append(f"{i}\t`{show(tok)}`\t{', '.join(pos)}")
    with open(os.path.join(OUT, "tokens_to_sort.md"), "w") as f:
        f.write("\n".join(L) + "\n")
    n = len(listed(top))
    print(f"listed tokens: {n}; sorted by rule: {n - len(todo)}; left for the subagents: {len(todo)}")


def pct(x):
    return f"{100 * x:.0f}%" if x >= 0.005 else ("0%" if x == 0 else "<1%")


def report():
    top, kinds = load()
    keys = [k["key"] for k in kinds]
    reps = []
    for n in (1, 2):
        with open(os.path.join(OUT, f"assign_rep{n}.json")) as f:
            reps.append({int(i): k for i, k in json.load(f).items()})
    lst = listed(top)
    todo = [i for i, v in lst.items() if by_rule(v[0]) is None]
    missing = [i for i in todo if i not in reps[0] or i not in reps[1]]
    bad = [(i, r[i]) for r in reps for i in todo if i in r and r[i] not in keys]
    if missing or bad:
        sys.exit(f"assignment files incomplete: {len(missing)} tokens missing, {len(bad)} with an unknown kind: {missing[:10]} {bad[:10]}")
    agree = sum(reps[0][i] == reps[1][i] for i in todo)
    kind_of = {}
    for i, (tok, _) in lst.items():
        k = by_rule(tok)
        kind_of[i] = k if k else (reps[0][i] if reps[0][i] == reps[1][i] else "disagree")
    cols = keys + ["disagree", "not sorted"]
    table = {}
    for pos in POSITIONS:
        for group in ("share", "scenario", "unrelated"):
            c = Counter()
            for r in top[pos]:
                c[kind_of.get(r["id"]) or (by_rule(r["token"]) or "not sorted")] += r[group]
            table[(pos, group)] = c
    fam = {pos: sum(r["share"] for r in top[pos] if r["family"]) for pos in POSITIONS}
    level = {k["key"]: k["level"] for k in kinds}
    levels = []
    for k in kinds:
        if k["level"] not in levels:
            levels.append(k["level"])
    name = {k["key"]: k["name"] for k in kinds}
    name.update({"disagree": "the two readers disagree", "not sorted": "rare tokens, not sorted"})
    members = defaultdict(list)
    weight = Counter()
    for pos in POSITIONS[:-1]:
        for r in top[pos]:
            weight[r["id"]] += r["share"]
    for i in sorted(lst, key=lambda i: -weight[i]):
        members[kind_of[i]].append(lst[i][0])

    L = ["# Readouts that are not about deception: kinds and how often (Qwen3.6-27B, J-lens, band 35-58)", "",
         "Written by `scripts/junk_report.py`. Shares are shares of the readout entries (16 tokens per layer, 24 band",
         "layers) over the build-split scenario transcripts (lies and truths) and the unrelated chats together.",
         "Positions under the wording Q9_dyl. Kinds were proposed by two subagents that each read 25 transcripts",
         "(`kinds_repA.json`, `kinds_repB.json`), merged into `kinds.json`. The first three kinds are sorted by a fixed",
         f"rule. The other frequent tokens ({len(todo)}) were sorted by two subagents independently; they agree on",
         f"{agree} ({100 * agree / len(todo):.0f}%). A token counts for a kind only when both agree.", "",
         "## 1. The kinds", "", "| kind | level | description | most frequent members |", "|---|---|---|---|"]
    for k in kinds:
        ex = "  ".join(f"`{show(t)}`" for t in members[k["key"]][:12])
        L.append(f"| {k['name']} | {k['level']} | {k['description'].replace('|', chr(92) + '|')} | {ex} |")
    L += ["", "## 2. Share of the readout by level", "",
          "| position | token | " + " | ".join(levels) + " | readers disagree | rare, not sorted | family words (draft) |",
          "|---|---|" + "---|" * (len(levels) + 3)]
    for pos in POSITIONS:
        c = table[(pos, "share")]
        cells = [pct(sum(v for k, v in c.items() if level.get(k) == lv)) for lv in levels]
        mark = " (reference)" if pos == REFERENCE[1] else ""
        L.append(f"| {pos}{mark} | `{TOKEN_AT[pos].replace('|', chr(92) + '|')}` | " + " | ".join(cells) + f" | {pct(c['disagree'])} | {pct(c['not sorted'])} | {pct(fam[pos])} |")
    L += ["", "The last column is a cross-check from the draft families: the share taken by tokens that are in any draft",
          "family at that position. It overlaps the other columns.", "",
          "## 3. Share of the readout by kind", "",
          "| position | " + " | ".join(name[k] for k in cols) + " |", "|---|" + "---|" * len(cols)]
    for pos in POSITIONS:
        c = table[(pos, "share")]
        L.append(f"| {pos} | " + " | ".join(pct(c[k]) for k in cols) + " |")
    L += ["", "## 4. Scenario transcripts against unrelated chats", "",
          "Share taken by the kind `deception and the situation`, and by all `no meaning` kinds together.", "",
          "| position | deception and the situation: scenario | unrelated | no meaning: scenario | unrelated |", "|---|---|---|---|---|"]
    for pos in POSITIONS:
        s, u = table[(pos, "scenario")], table[(pos, "unrelated")]
        nm = lambda c: sum(v for k, v in c.items() if level.get(k) == "no meaning")  # noqa: E731
        L.append(f"| {pos} | {pct(s['deception_situation'])} | {pct(u['deception_situation'])} | {pct(nm(s))} | {pct(nm(u))} |")
    with open(os.path.join(OUT, "JUNK.md"), "w") as f:
        f.write("\n".join(L) + "\n")
    with open(os.path.join(OUT, "kind_of_token.json"), "w") as f:
        json.dump({str(i): kind_of[i] for i in lst}, f)
    print(f"written: {os.path.join(OUT, 'JUNK.md')}; agreement {agree}/{len(todo)}")


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--prepare", action="store_true")
    args = ap.parse_args()
    prepare() if args.prepare else report()
