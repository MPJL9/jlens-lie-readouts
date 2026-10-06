#!/usr/bin/env python3
"""Apply the user's family decisions of 2026-10-01 to every unit's merged candidate list and write
the draft family list with the lie / truth split (PLAN.md Section 5.4). This is a draft, not the
freeze: the user still merges and deletes families and decides the pending items; nothing is scored.

Rules (each is one decision; the numbers are the user's):
  2  The question's own word is excluded at positions from the question on, under that wording:
     deceive (Q1, Q2), false (Q6), lie and truth / truthful (Q7), lie (Q9), with derived forms
     (liar, deception) and translations, including translations that straddle two words (诚实 =
     honest / truthful under Q7; 假 = fake / false under Q6). A token is a form of the question's
     word if it matches a fixed list of stems below, or if a replicate logged it as copied from
     the question. A family that loses half or more of its members this way is dropped whole.
  3  Families named admit, deny (denial) or acknowledge are excluded everywhere.
  4  Moral and legal families keep the side "unclear"; they are listed, not given a side.
  5  Emoji stay as members.
  6  Single Chinese characters: 藏, 掩, 遮 and 隐 join the conceal family at every position where
     they occur; 欺 and 哄 join the deceive family (or, where there is none, a family with a
     member containing 骗). 哄 is flagged: its only relevant word is 哄骗, Qwen's vocabulary has
     no token for that word, and the character alone means to coax (OBSERVATIONS.md,
     "Difficulties in reading the readouts"). Under Q1 and Q2 these deceive characters fall
     under rule 2 from the question on.
  1  `truth` (the noun) is excluded at positions from the question on (it can be confounded with
     the model's answer there); at the post-response slots it stays a truth-side family.
  7  Borderline words (true, false, correct, incorrect, wrong, accurate, inaccurate, fact, right,
     truth, objective) all join a family. A token a replicate had already put in a family stays
     there. Every other borderline token joins, at each position where it occurs, the family
     named after its group (the suggestion the replicates gave most often for that token). Sides
     by meaning: true, correct, accurate, fact, right, truth are truth-side; false, incorrect,
     inaccurate, wrong are lie-side; objective is unclear. Rules 2 and 1 then apply (so `false`
     is out from the question on under Q6, and `truth` from the question on everywhere).
  -  Other single characters and word pieces the replicates disagreed on (accepted by one, called
     ambiguous by the other) are held back until the user decides them.

Inputs: analysis/families/<unit>_merged.json, <unit>_rep{1,2}.json, the presence index.
Outputs: analysis/families/families_draft.json (every entry with its status and removed members),
analysis/families/DRAFT.md (what the rules did; the family list per model and lens with the label
split; all family names), analysis/families/draft/<unit>.md (per position, every kept family).
The label split uses the build split only.

Usage: python3 scripts/apply_family_decisions.py
"""
from __future__ import annotations

import glob
import json
import os
import re
import sys
from collections import Counter, defaultdict

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import common as C  # noqa: E402
import presence as P  # noqa: E402
import family_jobs as FJ  # noqa: E402
from family_checks import TRUTH_LATIN, TRUTH_OTHER, borderline_group, norm  # noqa: E402

FAM = os.path.join(C.ROOT, "analysis", "families")
OUT_DIR = os.path.join(FAM, "draft")
QWEN = "qwen3.6-27b"
DATE = "2026-10-01"

EXCLUDED_NAMES = {"admit", "admission", "deny", "denial", "acknowledge", "acknowledgement", "acknowledgment"}
TO_CONCEAL = ["藏", "掩", "遮", "隐"]
TO_DECEIVE = ["欺", "哄"]
NO_FAMILY = []
# borderline groups: family name -> (gloss, side by meaning)
BORDERLINE = {"true": ("true, real", "truth"), "correct": ("correct", "truth"), "accurate": ("accurate", "truth"),
              "fact": ("fact, factual", "truth"), "right": ("right", "truth"), "truth": ("the truth", "truth"),
              "false": ("false, untrue", "lie"), "incorrect": ("incorrect", "lie"), "inaccurate": ("inaccurate", "lie"),
              "wrong": ("wrong, mistaken", "lie"), "objective": ("objective", "unclear")}
QCOPY = re.compile(r"copied|self-report|inflection of|translation of|from the question|in the question|question word|question's (own )?word", re.I)
NOT_QCOPY = re.compile(r"user's question|answers? the user|scenario", re.I)


def bare(s):
    return s.strip(" _.-/\"'“”(),:=>").lower()


def lie_form(s):
    return bare(s) in {"lie", "lies", "lied", "lying", "liar", "liars"} or any(x in s for x in ("谎", "謊")) \
        or bare(s).startswith(("lüg", "mentir", "mentira", "mensong")) or "거짓" in s or "лож" in s.lower()


def truth_form(s):
    return "truth" in bare(s) or bare(s) in TRUTH_LATIN or any(x in s for x in ("真相", "实话", "如实", "真理", "实情", "诚实", "誠實"))


def deceive_form(s):
    return any(x in bare(s) for x in ("deceiv", "decept", "deceit")) or any(x in s for x in ("欺", "骗", "騙", "哄"))


def false_form(s):
    return "fals" in bare(s) or "虚假" in s or s.strip() in {"假", "假的", "真假"}


QUESTION_FORMS = {"Q1_bare": [("deceive", deceive_form)], "Q2_after": [("deceive", deceive_form)],
                  "Q6_factual": [("false", false_form)], "Q7_ab": [("lie", lie_form), ("truth", truth_form)],
                  "Q9_dyl": [("lie", lie_form)]}


def truth_noun(s):
    return s.strip(" _.").lower() in TRUTH_LATIN or s.strip() in TRUTH_OTHER


def name_parts(name):
    return [p.split()[0] for p in re.split(r"\s*/\s*|\s+or\s+|\s*,\s*", norm(name)) if p.split()]


def main():
    os.makedirs(OUT_DIR, exist_ok=True)
    units = []
    for p in sorted(glob.glob(os.path.join(FAM, "*_merged.json"))):
        with open(p) as f:
            units.append(json.load(f))
    vocabs = {m: C.load_vocab(m) for m in C.MODELS}
    unit_positions = {FJ.unit_name(x): x["positions"] for lens in C.LENSES for x in FJ.units(lens)}

    # tokens a replicate logged as copied from the question, per (model, lens, wording)
    qcopy = defaultdict(set)
    borderline = defaultdict(set)            # (model, lens) -> token ids listed as borderline by a replicate
    votes = defaultdict(Counter)             # token string -> group votes, over all files
    for u in units:
        for b in u.get("borderline", []):
            if b.get("id"):
                borderline[(u["model"], u["lens"])].add(b["id"])
                g = borderline_group(b.get("family_if_accepted", ""))
                votes[b["token"]][g if g != "other" else norm(b.get("family_if_accepted", ""))] += 1
        if u["part"] == "prefix":
            continue
        for e in u.get("exclusions", []):
            r = e.get("reason", "")
            if e.get("id") and QCOPY.search(r) and not NOT_QCOPY.search(r):
                qcopy[(u["model"], u["lens"], u["part"])].add(e["id"])
    group_of = {t: v.most_common(1)[0][0] for t, v in votes.items()}
    group_of = {t: g for t, g in group_of.items() if g in BORDERLINE}
    # pieces accepted by one replicate and called ambiguous by the other, per (model, lens)
    disputed = defaultdict(set)
    for p in sorted(glob.glob(os.path.join(FAM, "*_rep1.json"))):
        p2 = p.replace("_rep1.json", "_rep2.json")
        if not os.path.exists(p2):
            continue
        reps = [json.load(open(p)), json.load(open(p2))]
        acc = [{x["id"] for fam in r.get("families", []) for x in fam.get("members", [])} for r in reps]
        amb = [{a.get("id") for a in r.get("ambiguous_pieces", [])} for r in reps]
        disputed[(reps[0]["model"], reps[0]["lens"])] |= ((acc[0] & amb[1]) | (acc[1] & amb[0])) - {0, None}
    held_pieces = defaultdict(Counter)       # token string -> names of the families it was accepted into

    entries = []
    log = Counter()
    removed_by_rule = defaultdict(Counter)       # rule -> token string -> entries
    for u in units:
        m, lens, part = u["model"], u["lens"], u["part"]
        vocab = vocabs[m]
        d = P.load(m, lens)
        char_ids = {ch: {i for i, s in enumerate(vocab) if s.strip() == ch} for ch in TO_CONCEAL + TO_DECEIVE + NO_FAMILY}
        decided_ids = set().union(*char_ids.values())
        fams = [dict(f, members=[dict(x) for x in f["members"]], removed=[], status="keep") for f in u["families"]]
        by_pos = defaultdict(list)
        for f in fams:
            by_pos[f["position"]].append(f)

        def strip(f, pred, rule):
            keep = []
            for x in f["members"]:
                if pred(x):
                    f["removed"].append(dict(token=x["token"], id=x["id"], rule=rule))
                    removed_by_rule[rule][x["token"]] += 1
                else:
                    keep.append(x)
            f["members"] = keep

        own = sorted(unit_positions[u["unit"]], key=P.position_key)      # the positions of this unit only
        # ---- rule 6: single characters
        for pos in own:
            tab = d["present"][part][pos]
            here = by_pos.get(pos, [])
            for f in here:
                strip(f, lambda x: x["id"] in decided_ids, "6 single character (moved or left out)")
            for chars, target, gloss in ((TO_CONCEAL, "conceal", "to conceal, to hide"), (TO_DECEIVE, "deceive", "the act of deceiving")):
                add = [dict(token=vocab[i], id=i, n=int(len(tab[i][0]))) for ch in chars for i in char_ids[ch] if i in tab]
                if not add:
                    continue
                fam = next((f for f in here if norm(f["name"]) == target), None) \
                    or next((f for f in here if target in norm(f["name"])), None)
                if fam is None and target == "deceive":
                    fam = next((f for f in here if any("骗" in x["token"] for x in f["members"])), None)
                if fam is None and target == "conceal":
                    fam = next((f for f in here if norm(f["name"]) in ("hide", "hide / conceal", "cover up")), None)
                if fam is None:
                    fam = dict(position=pos, name=target, gloss=gloss, side="lie", seeds=[], members=[], removed=[], status="keep",
                               notes=f"created for the single characters (user decision, {DATE})")
                    fams.append(fam)
                    by_pos[pos].append(fam)
                    here = by_pos[pos]
                    log["families created for single characters"] += 1
                fam["members"] += add
                log["single characters placed"] += len(add)

        # ---- rule 7: borderline words join a family
        for pos in own:
            tab = d["present"][part][pos]
            here = by_pos.get(pos, [])
            placed = {x["id"] for f in here for x in f["members"]}
            for i in sorted(borderline[(m, lens)]):
                if i not in tab or i in placed or i >= len(vocab) or vocab[i] not in group_of:
                    continue
                g = group_of[vocab[i]]
                fam = next((f for f in here if norm(f["name"]) == g), None) or next((f for f in here if g in name_parts(f["name"])), None)
                if fam is None:
                    fam = dict(position=pos, name=g, gloss=BORDERLINE[g][0], side=BORDERLINE[g][1], seeds=[], members=[], removed=[],
                               status="keep", notes=f"borderline words joined by the user's decision of {DATE}")
                    fams.append(fam)
                    by_pos[pos].append(fam)
                    here = by_pos[pos]
                    log["families created for borderline words"] += 1
                fam["members"].append(dict(token=vocab[i], id=i, n=int(len(tab[i][0]))))
                placed.add(i)
                log["borderline tokens placed"] += 1

        for f in fams:
            # ---- rule 3: admit / deny / acknowledge
            if any(p_ in EXCLUDED_NAMES for p_ in name_parts(f["name"])):
                f["status"] = "excluded: admit / deny / acknowledge"
                continue
            # ---- rule 2: the question's own word
            if part != "prefix":
                n0 = len(f["members"])
                for word, form in QUESTION_FORMS[part]:
                    strip(f, lambda x: form(x["token"]), f"2 form of the question's word ({word})")
                strip(f, lambda x: x["id"] in qcopy[(m, lens, part)], "2 logged by a replicate as copied from the question")
                gone = sum(r["rule"].startswith("2 ") for r in f["removed"])
                if n0 and gone * 2 >= n0:
                    f["status"] = "excluded: the question's own word"
                    continue
                # ---- rule 1: the noun truth, held back from the question on
                strip(f, lambda x: truth_noun(x["token"]), "1 the noun truth (excluded from the question on)")
                if not f["members"] and any(r["rule"].startswith("1 ") for r in f["removed"]):
                    f["status"] = "excluded: truth from the question on"
                    continue
            # ---- pieces and borderline tokens the replicates disagreed on
            for x in f["members"]:
                if x["id"] in disputed[(m, lens)] and x["id"] not in decided_ids and x["id"] not in borderline[(m, lens)]:
                    held_pieces[x["token"]][norm(f["name"])] += 1
            strip(f, lambda x: x["id"] in disputed[(m, lens)] and x["id"] not in decided_ids and x["id"] not in borderline[(m, lens)],
                  "- piece the replicates disagreed on (held back)")
            if not f["members"]:
                f["status"] = "held back: no undisputed member left"
        for f in fams:
            log[f["status"].split(":")[0]] += 1
            entries.append(dict(model=m, lens=lens, part=part, group=u["group"], unit=u["unit"], position=f["position"],
                                name=f["name"], gloss=f.get("gloss", ""), side=f["side"], status=f["status"],
                                members=[dict(token=x["token"], id=x["id"]) for x in f["members"]], removed=f["removed"],
                                double_reading=bool(f.get("double_reading")), notes=f.get("notes", "")))

    # ---- visibility with the label split, for kept entries
    for e in entries:
        if e["status"] != "keep":
            continue
        d = P.load(e["model"], e["lens"])
        ids = {x["id"] for x in e["members"]}
        e["counts"] = {k: list(v) for k, v in P.counts(d, e["part"], e["position"], ids).items()}
        if e["part"] != "prefix":
            ans, pm, hm = P.answer(d, e["part"]), P.present_mask(d, e["part"], e["position"], ids), P.have_mask(d, e["part"], e["position"])
            for lab in ("lie", "truth"):
                sel = hm & (d["cls"] == lab) & (ans == "deny")
                e["counts"][f"{lab}_deny"] = [int((pm & sel).sum()), int(sel.sum())]

    with open(os.path.join(FAM, "families_draft.json"), "w") as f:
        json.dump(dict(date=DATE, status="draft, not frozen", rules=__doc__.split("Inputs:")[0], entries=entries), f, ensure_ascii=False)

    # ---------------------------------------------------------------- reports
    cell = lambda v: f"{v[0]}/{v[1]} ({P.pct(*v)})"
    vis = lambda e: e["counts"]["lie"][0] + e["counts"]["truth"][0]
    kept = [e for e in entries if e["status"] == "keep"]

    def members_cell(es, k=10):
        c = Counter()
        for e in es:
            for x in e["members"]:
                c[x["token"]] += 1
        s = ", ".join(f"`{P.tok(t)}`" for t, _ in c.most_common(k))
        return s + (f" … (+{len(c) - k})" if len(c) > k else "")

    L = [f"# Draft family list after the user's decisions of {DATE} (not frozen)", "",
         "Written by `scripts/apply_family_decisions.py` (the rules are in its header). Every entry, with its status and",
         "the members each rule removed, is in `families_draft.json`. Per-position tables are in `draft/<unit>.md`.",
         "Counts are `present / transcripts (share)` on the build split: scenario lies, scenario truths, no-pressure",
         "truths, unrelated chats; for Qwen's positions from the question on, also the lies and truths whose",
         "self-report answer is a denial. The held-out split has not been read.", "",
         "## 1. What the rules did", "", "| | entries |", "|---|---|"]
    L += [f"| merged candidate entries (one family at one position) | {len(entries)} |"]
    for k in ("keep", "excluded", "held back"):
        L.append(f"| {k} | {log[k]} |")
    for st, n in Counter(e["status"] for e in entries if e["status"] != "keep").most_common():
        L.append(f"| &nbsp;&nbsp;{st} | {n} |")
    L += [f"| single characters placed in conceal / deceive (member additions) | {log['single characters placed']} |",
          f"| families created to hold them | {log['families created for single characters']} |",
          f"| borderline tokens placed in a family (member additions) | {log['borderline tokens placed']} |",
          f"| families created to hold them | {log['families created for borderline words']} |", "",
          "Members removed from families that were kept or dropped, by rule (distinct tokens; the most frequent):", ""]
    for rule in sorted(removed_by_rule):
        c = removed_by_rule[rule]
        L.append(f"- **{rule}**: {len(c)} tokens, {sum(c.values())} removals. " + ", ".join(f"`{P.tok(t)}` ({n})" for t, n in c.most_common(30)))
    L.append("")
    L += ["Held-back pieces (accepted by one replicate, called ambiguous by the other; not decided by the user yet), with the",
          "families the accepting replicate put them in:", "",
          "| token | family it was accepted into (entries) |", "|---|---|"]
    for t, c in sorted(held_pieces.items(), key=lambda kv: -sum(kv[1].values())):
        L.append(f"| `{P.tok(t)}` | " + ", ".join(f"{n} ({k})" for n, k in c.most_common(4)) + " |")
    L.append("")
    dbl = Counter(norm(e["name"]) for e in kept if e["double_reading"])
    L += ["Kept families that a replicate flagged as having two readings (the model's act, or its answer to the user), other",
          "than admit / deny / acknowledge: " + (", ".join(f"{n} ({c})" for n, c in dbl.most_common()) or "none") + ".", ""]

    # ---- per model and lens
    L += ["## 2. Families per model and lens", "",
          "One row per family name. The position shown is the one where the family is present in the most scenario",
          "transcripts (lies and truths pooled, so the choice does not use the label). Rows are sorted by that count.", ""]
    for m in C.MODELS:
        for lens in C.LENSES:
            sub = [e for e in kept if e["model"] == m and e["lens"] == lens]
            L += [f"### {m}, {'J-lens' if lens == 'J' else 'logit lens'}", ""]
            parts = ["prefix"] + (C.WORDINGS if m == QWEN else [])
            for part in parts:
                es = [e for e in sub if e["part"] == part]
                by = defaultdict(list)
                for e in es:
                    by[norm(e["name"])].append(e)
                rows = []
                for n, lst in by.items():
                    best = max(lst, key=vis)
                    if vis(best) == 0:
                        continue
                    rows.append((vis(best), n, lst, best))
                rows.sort(key=lambda r: -r[0])
                title = "post-response slots" if part == "prefix" else f"wording {part}, positions from the question on"
                L += [f"**{title}** ({len(rows)} family names present in at least one build transcript)", ""]
                if not rows:
                    L += ["None.", ""]
                    continue
                head = "| family | side | positions | members | most visible position | lies | truths | no-pressure truths | unrelated |"
                sep = "|---|---|---|---|---|---|---|---|---|"
                if part != "prefix":
                    head += " lies that deny | truths that deny |"
                    sep += "---|---|"
                L += [head, sep]
                for _, n, lst, best in rows:
                    c = best["counts"]
                    sides = "/".join(sorted({e["side"] for e in lst}))
                    line = (f"| {n} | {sides} | {len(lst)} | {members_cell(lst)} | {best['position']} | {cell(c['lie'])} | {cell(c['truth'])} | "
                            f"{cell(c['np_truth'])} | {cell(c['unrelated'])} |")
                    if part != "prefix":
                        line += f" {cell(c['lie_deny'])} | {cell(c['truth_deny'])} |"
                    L.append(line)
                L.append("")

    # ---- all names
    L += ["## 3. All family names (for merging)", "",
          "| family | sides (lie / truth / unclear) | kept entries | models and lenses | most frequent members |", "|---|---|---|---|---|"]
    by = defaultdict(list)
    for e in kept:
        by[norm(e["name"])].append(e)
    for n, lst in sorted(by.items(), key=lambda kv: -len(kv[1])):
        s = Counter(e["side"] for e in lst)
        ml = sorted({f"{e['model'].split('-')[0]}{'-' + e['model'].split('-')[2] if e['model'].startswith('gemma') else ''} {e['lens']}" for e in lst})
        L.append(f"| {n} | {s['lie']} / {s['truth']} / {s['unclear']} | {len(lst)} | {', '.join(ml)} | {members_cell(lst, 8)} |")
    L.append("")
    with open(os.path.join(FAM, "DRAFT.md"), "w") as f:
        f.write("\n".join(L))

    # ---- per-unit tables
    for u in units:
        es = [e for e in entries if e["unit"] == u["unit"]]
        with_ans = u["part"] != "prefix"
        U = [f"# Draft families: {u['model']}, {'J-lens' if u['lens'] == 'J' else 'logit lens'}, part {u['part']}, group {u['group']}", "",
             f"Written by `scripts/apply_family_decisions.py` ({DATE}; draft, not frozen). Counts are `present / transcripts (share)`",
             "on the build split.", ""]
        for pos in sorted({e["position"] for e in es}, key=P.position_key):
            U += [f"## {pos}", "",
                  "| family | side | members | lies | truths | no-pressure truths | unrelated |" + (" lies that deny | truths that deny |" if with_ans else ""),
                  "|---|---|---|---|---|---|---|" + ("---|---|" if with_ans else "")]
            here = [e for e in es if e["position"] == pos and e["status"] == "keep"]
            for e in sorted(here, key=lambda e: -vis(e)):
                c = e["counts"]
                line = (f"| {e['name']} ({e['gloss']}) | {e['side']} | " + ", ".join(f"`{P.tok(x['token'])}`" for x in e["members"]) +
                        f" | {cell(c['lie'])} | {cell(c['truth'])} | {cell(c['np_truth'])} | {cell(c['unrelated'])} |")
                if with_ans:
                    line += f" {cell(c['lie_deny'])} | {cell(c['truth_deny'])} |"
                U.append(line)
            out = [e for e in es if e["position"] == pos and e["status"] != "keep"]
            if out:
                U += ["", "Not in the draft: " + "; ".join(f"{e['name']} ({e['status']})" for e in out)]
            U.append("")
        with open(os.path.join(OUT_DIR, u["unit"] + ".md"), "w") as f:
            f.write("\n".join(U))
    print(f"{len(entries)} entries: " + ", ".join(f"{k} {v}" for k, v in log.items()))
    for rule in sorted(removed_by_rule):
        c = removed_by_rule[rule]
        print(f"  {rule}: {len(c)} tokens, {sum(c.values())} removals; top: " + ", ".join(f"{t.strip()}({n})" for t, n in c.most_common(25)))


if __name__ == "__main__":
    main()
