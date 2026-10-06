#!/usr/bin/env python3
"""PLAN.md Section 5.4, across units: one summary of the family-generation output for the user's
edit step. Reads analysis/families/<unit>_rep{1,2}.json (all units of both lenses that exist) and
writes analysis/families/SUMMARY.md and analysis/families/summary.json. No labels are read.

Contents:
  1. Coverage: per lens and model, units, replicate files, family entries.
  2. Where families are: per unit and position, the number of families per replicate and the
     positions both replicates left without families.
  3. Family names across units: for each family name, the number of units and positions where
     it appears, the sides the replicates gave it, and its most frequent members. Names are
     compared after lower-casing and trimming.
  4. Recurring judgement calls, each as a table of how the replicate files handled it:
       truth          is `truth` a family, a borderline word, or excluded?
       derived forms  under each wording, are derived forms of the question word (deceive for
                      "deceptive", liar / truth for "lie" / "truthful") families or exclusions?
       double reading families flagged double_reading (admit, deny, acknowledge, ...)
       unclear sides  the family names most often given side "unclear"
       emoji          families whose members are emoji
       single-character and fragment members accepted in one replicate and listed as
                      ambiguous in the other
  5. Borderline tokens: the most frequent borderline tokens with the family they would join.

Usage: python3 scripts/family_summary.py
"""
from __future__ import annotations

import json
import os
import re
import sys
from collections import Counter, defaultdict

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import common as C  # noqa: E402
import family_jobs as FJ  # noqa: E402

FAM = os.path.join(C.ROOT, "analysis", "families")
EMOJI = re.compile("[\U0001F300-\U0001FAFF☀-➿]")
QUESTION_ROOTS = {
    "Q1_bare": {"deceive": ["deceiv", "decept", "deceit", "欺骗", "骗"]},
    "Q2_after": {"deceive": ["deceiv", "decept", "deceit", "欺骗", "骗"]},
    "Q6_factual": {"false": ["false", "falsehood", "虚假", "假"]},
    "Q7_ab": {"lie": ["lie", "liar", "lying", "谎"], "truth": ["truth", "真相", "实话"]},
    "Q9_dyl": {"lie": ["lie", "liar", "lying", "谎"]},
}


def norm_name(s):
    return re.sub(r"\s+", " ", s.strip().lower())


def load_all():
    """[(lens, unit dict, rep number, json)] for every replicate file that exists."""
    out = []
    for lens in C.LENSES:
        for u in FJ.units(lens):
            for k in (1, 2):
                p = os.path.join(FAM, f"{FJ.unit_name(u)}_rep{k}.json")
                if os.path.exists(p):
                    with open(p) as f:
                        out.append((lens, u, k, json.load(f)))
    return out


def tok(s):
    s = s.replace("\n", "\\n").replace("|", "\\|")
    return "␣" + s[1:] if s.startswith(" ") else s


def main():
    files = load_all()
    L = ["# Family generation: summary across units (PLAN.md Section 5.4)", "",
         "Written by `scripts/family_summary.py` from the replicate files in this folder. No labels were",
         "read. A *unit* is one model × lens × part × position group; each unit has two replicate files",
         "written by independent subagents with the frozen prompt `prompts/family_generation.md`.", ""]

    # 1. coverage
    cov = defaultdict(lambda: {"units": set(), "files": 0, "families": 0})
    for lens, u, k, d in files:
        c = cov[(lens, u["model"])]
        c["units"].add(FJ.unit_name(u))
        c["files"] += 1
        c["families"] += len(d.get("families", []))
    L += ["## 1. Coverage", "", "| lens | model | units | replicate files | family entries |", "|---|---|---|---|---|"]
    for (lens, m), c in sorted(cov.items()):
        L.append(f"| {lens} | {m} | {len(c['units'])} | {c['files']} | {c['families']} |")
    L.append("")

    # 2. where families are
    per_pos = defaultdict(lambda: defaultdict(dict))        # (lens, unit) -> position -> rep -> n
    for lens, u, k, d in files:
        name = FJ.unit_name(u)
        cnt = Counter(f["position"] for f in d.get("families", []))
        for pos in u["positions"]:
            per_pos[(lens, name)][pos][k] = cnt.get(pos, 0)
    L += ["## 2. Families per position (replicate 1 / replicate 2)", "",
          "Positions where both replicates found no family are marked **none**.", "",
          "| lens | unit | families per position |", "|---|---|---|"]
    empty = []
    for (lens, name), pos in sorted(per_pos.items()):
        cells = []
        for p_, reps in pos.items():
            a, b = reps.get(1), reps.get(2)
            if a == 0 and b == 0:
                cells.append(f"{p_} **none**")
                empty.append((lens, name, p_))
            else:
                cells.append(f"{p_} {'–' if a is None else a}/{'–' if b is None else b}")
        L.append(f"| {lens} | {name} | {'; '.join(cells)} |")
    L.append("")

    # 3. family names across units
    names = defaultdict(lambda: {"units": set(), "positions": 0, "sides": Counter(), "members": Counter(), "double": 0})
    for lens, u, k, d in files:
        for f in d.get("families", []):
            e = names[(lens, norm_name(f["name"]))]
            e["units"].add(FJ.unit_name(u))
            e["positions"] += 1
            e["sides"][f.get("side", "?")] += 1
            e["double"] += bool(f.get("double_reading"))
            for m in f.get("members", []):
                e["members"][m["token"]] += m.get("n", 0)
    for lens in C.LENSES:
        rows = sorted(((n, e) for (l, n), e in names.items() if l == lens), key=lambda x: (-len(x[1]["units"]), -x[1]["positions"]))
        L += [f"## 3. Family names across units, {'J-lens' if lens == 'J' else 'logit lens'} (names in 4 or more units)", "",
              "| family | units | entries | sides (lie / truth / unclear) | most frequent members |", "|---|---|---|---|---|"]
        for n, e in rows:
            if len(e["units"]) < 4:
                continue
            s = e["sides"]
            mem = ", ".join(f"`{tok(t)}`" for t, _ in e["members"].most_common(6))
            L.append(f"| {n} | {len(e['units'])} | {e['positions']} | {s.get('lie', 0)} / {s.get('truth', 0)} / {s.get('unclear', 0)} | {mem} |")
        L.append("")

    # 4. recurring judgement calls
    L += ["## 4. Recurring judgement calls", "",
          "Each table counts replicate files. Decide each once; the decision is then applied to every unit.", ""]
    # truth
    tr = defaultdict(Counter)
    for lens, u, k, d in files:
        fam = any(norm_name(f["name"]).startswith("truth") and not norm_name(f["name"]).startswith("truthful") for f in d.get("families", []))
        bor = any(re.fullmatch(r"\s?truths?", b.get("token", ""), re.I) or b.get("token") in ("真相",) for b in d.get("borderline", []))
        exc = any(re.fullmatch(r"\s?truths?", b.get("token", ""), re.I) or b.get("token") in ("真相",) for b in d.get("exclusions", []))
        if fam or bor or exc:
            tr[(lens, u["part"])]["family" if fam else ("borderline" if bor else "excluded")] += 1
    L += ["### 4.1 `truth` (the noun): family, borderline, or excluded", "",
          "| lens | part | family | borderline | excluded |", "|---|---|---|---|---|"]
    for (lens, part), c in sorted(tr.items()):
        L.append(f"| {lens} | {part} | {c['family']} | {c['borderline']} | {c['excluded']} |")
    L.append("")
    # derived forms of question words
    L += ["### 4.2 Forms of the question's own word: kept as a family or excluded", "",
          "Counted over files of the wording's units. \"family\" = a family whose member tokens contain the",
          "root; \"excluded\" = the root appears among the exclusions.", "",
          "| lens | part | question word | files with a family | files excluding it |", "|---|---|---|---|---|"]
    for lens in C.LENSES:
        for part, roots in QUESTION_ROOTS.items():
            for word, pieces in roots.items():
                fam = exc = 0
                for l2, u, k, d in files:
                    if l2 != lens or u["part"] != part:
                        continue
                    has = lambda toks: any(any(p_ in t.lower() for p_ in pieces) for t in toks)
                    fam += has([m["token"] for f in d.get("families", []) for m in f.get("members", [])
                                if not any(x in m["token"].lower() for x in ("believ", "client", "repl", "earl", "truthful"))] if word != "truth"
                               else [m["token"] for f in d.get("families", []) for m in f.get("members", [])])
                    exc += has([e.get("token", "") for e in d.get("exclusions", [])])
                L.append(f"| {lens} | {part} | {word} | {fam} | {exc} |")
    L.append("")
    # double reading
    dbl = Counter()
    for (lens, n), e in names.items():
        if e["double"]:
            dbl[n] += e["double"]
    L += ["### 4.3 Families flagged as having two readings (the model's act, or the answer to the user)", "",
          ", ".join(f"{n} ({c})" for n, c in dbl.most_common(15)), ""]
    # unclear sides
    unc = Counter()
    tot = Counter()
    for (lens, n), e in names.items():
        unc[n] += e["sides"].get("unclear", 0)
        tot[n] += sum(e["sides"].values())
    L += ["### 4.4 Family names most often given side \"unclear\" (entries unclear / all entries)", "",
          ", ".join(f"{n} ({unc[n]}/{tot[n]})" for n, _ in unc.most_common(40) if unc[n] >= 5), ""]
    # side disagreement
    dis = [(n, e["sides"]) for (lens, n), e in names.items() if e["sides"].get("lie", 0) and e["sides"].get("truth", 0)]
    L += ["### 4.5 Family names given both the lie side and the truth side somewhere", "",
          ", ".join(f"{n} (lie {s['lie']}, truth {s['truth']})" for n, s in sorted(dis)) or "none", ""]
    # emoji
    em = Counter()
    for lens, u, k, d in files:
        for f in d.get("families", []):
            for m in f.get("members", []):
                if EMOJI.search(m["token"]):
                    em[(lens, u["model"], m["token"])] += 1
    L += ["### 4.6 Emoji accepted as family members (lens, model, emoji: entries)", "",
          ", ".join(f"{l} {m} {t}: {c}" for (l, m, t), c in em.most_common(20)) or "none", ""]
    # accepted in one, ambiguous in the other
    acc = defaultdict(set)
    amb = defaultdict(set)
    for lens, u, k, d in files:
        name = FJ.unit_name(u)
        for f in d.get("families", []):
            for m in f.get("members", []):
                acc[(name, m["token"])].add(k)
        for a in d.get("ambiguous_pieces", []):
            amb[(name, a.get("token", ""))].add(k)
    split = Counter()
    for key in acc:
        if key in amb and acc[key] != amb[key]:
            split[key[1]] += 1
    L += ["### 4.7 Tokens accepted as a family member in one replicate and listed as an ambiguous piece in the other (units)", "",
          ", ".join(f"`{tok(t)}` ({c})" for t, c in split.most_common(40)) or "none", ""]

    # 5. borderline
    bor = Counter()
    fam_of = defaultdict(Counter)
    for lens, u, k, d in files:
        for b in d.get("borderline", []):
            t = b.get("token", "")
            bor[t] += 1
            fam_of[t][b.get("family_if_accepted", "")] += 1
    L += ["## 5. Borderline tokens (true / false / correct / wrong …), most frequent across files", "",
          "| token | files | family if accepted |", "|---|---|---|"]
    for t, c in bor.most_common(40):
        L.append(f"| `{tok(t)}` | {c} | {fam_of[t].most_common(1)[0][0]} |")
    L.append("")

    with open(os.path.join(FAM, "SUMMARY.md"), "w") as f:
        f.write("\n".join(L))
    with open(os.path.join(FAM, "summary.json"), "w") as f:
        json.dump({"n_files": len(files), "empty_positions": empty,
                   "names": {f"{l}|{n}": {"units": len(e["units"]), "entries": e["positions"], "sides": dict(e["sides"])} for (l, n), e in names.items()}}, f, ensure_ascii=False)
    print(f"SUMMARY.md written from {len(files)} replicate files; {len(empty)} positions without families in both replicates")


if __name__ == "__main__":
    main()
