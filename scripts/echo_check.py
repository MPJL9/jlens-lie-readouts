#!/usr/bin/env python3
"""Echo check: is a family's readout word a copy of a word in the conversation?

MASK system prompts often contain words such as "do not disclose" or "conceal". A readout word
at a post-response slot could then be a copy of the context rather than a description of the
model's act. For every family at the post-response slots (merged candidate lists, both lenses)
this script looks at the text the model has read at that point (system prompt, user prompt,
response) and asks whether it contains a form of the family's word.

A form of the word = a word in the text that starts with one of the family's stems (the seed
words the family-generation subagents named, plus the members themselves; Latin script only,
three letters or more, case ignored). The conversations are in English, so members in other
scripts cannot be copies of the text.

Per family and position:
  - the share of scenario transcripts whose system prompt, user prompt or response has the word;
  - how often the family is present in the readout when the context has the word, and when it
    does not;
  - over the scenarios that gave both a lie and a truth (the two share the system prompt and the
    user prompt, so a copy of the prompt would show in both): the number of scenarios where the
    family is present in both, in the lie only, in the truth only, in neither;
and, per model, the share of scenario system prompts that contain a word of any lie-side family.

Build split only; commentary transcripts dropped. Writes analysis/families/ECHO.md and echo.json.

Usage: python3 scripts/echo_check.py
"""
from __future__ import annotations

import glob
import json
import os
import re
import sys
from collections import defaultdict

import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import common as C  # noqa: E402
import presence as P  # noqa: E402

FAM = os.path.join(C.ROOT, "analysis", "families")
MIN_SHARE = 0.10
LATIN = re.compile(r"[A-Za-z][A-Za-z'\- ]*")


def norm(s):
    return re.sub(r"\s+", " ", s.strip().lower())


def stems_of(fam):
    out = set()
    for s in fam.get("seeds", []):
        s = s.strip().lower()
        if LATIN.fullmatch(s) and len(s) >= 3:
            out.add(s)
    for m in fam["members"]:
        s = m["token"].strip().lower()
        if LATIN.fullmatch(s) and len(s) >= 4:
            out.add(s)
    return out


def matcher(stems):
    if not stems:
        return None
    return re.compile(r"(?<![A-Za-z])(?:" + "|".join(sorted(map(re.escape, stems), key=len, reverse=True)) + ")", re.I)


def main():
    files = []
    for p in sorted(glob.glob(os.path.join(FAM, "*_prefix_postresp_merged.json"))):
        with open(p) as f:
            files.append(json.load(f))
    L = ["# Echo check: readout words that are also in the conversation", "",
         "Written by `scripts/echo_check.py`. Build-split scenario transcripts, commentary dropped, post-response",
         "slots. \"The context has the word\" = the system prompt, the user prompt or the response contains a word",
         "that starts with one of the family's stems (English forms only). Families present in at least 10% of the",
         "scenario transcripts at the position are listed. Cells are `present / transcripts`.", ""]
    js = {}
    for f in files:
        m, lens = f["model"], f["lens"]
        d = P.load(m, lens)
        texts = C.load_transcripts(m)
        trs = d["transcripts"]
        scen = np.array([t["set"] == "scenario" for t in trs])
        lie = d["cls"] == "lie"
        tru = d["cls"] == "truth"
        npt = d["cls"] == "np_truth"
        # stems per family name, pooled over the unit's positions
        by_name = defaultdict(set)
        for fam in f["families"]:
            by_name[norm(fam["name"])] |= stems_of(fam)
        rows = []
        pairs = defaultdict(dict)                       # scenario -> {label: transcript index}
        for i, t in enumerate(trs):
            if t["set"] == "scenario":
                pairs[t["item_id"]][t["label"]] = i
        pairs = [(v["lie"], v["truth"]) for v in pairs.values() if len(v) == 2]
        any_sys = np.zeros(len(trs), bool)
        any_lie_sys = np.zeros(len(trs), bool)
        any_lie_ctx = np.zeros(len(trs), bool)
        has = {}
        for name, stems in by_name.items():
            rx = matcher(stems)
            if rx is None:
                continue
            sys_h = np.array([bool(rx.search(texts[t["tid"]]["system"])) for t in trs])
            usr_h = np.array([bool(rx.search(texts[t["tid"]]["user_prompt"])) for t in trs])
            rsp_h = np.array([bool(rx.search(texts[t["tid"]]["response"])) for t in trs])
            has[name] = (sys_h, usr_h, rsp_h)
        for fam in f["families"]:
            name = norm(fam["name"])
            if name not in has:
                continue
            sys_h, usr_h, rsp_h = has[name]
            any_sys |= sys_h
            if fam["side"] == "lie":
                any_lie_sys |= sys_h
                any_lie_ctx |= sys_h | usr_h | rsp_h
            ids = {x["id"] for x in fam["members"]}
            pm = P.present_mask(d, "prefix", fam["position"], ids)
            n_s = int(scen.sum())
            if (pm & scen).sum() < MIN_SHARE * n_s:
                continue
            ctx = sys_h | usr_h | rsp_h
            c = lambda a, b: [int((a & b).sum()), int(b.sum())]
            pr = [sum(1 for a, b in pairs if pm[a] and pm[b]), sum(1 for a, b in pairs if pm[a] and not pm[b]),
                  sum(1 for a, b in pairs if pm[b] and not pm[a]), sum(1 for a, b in pairs if not pm[a] and not pm[b])]
            rows.append(dict(
                name=name, side=fam["side"], position=fam["position"], stems=sorted(by_name[name]),
                present_lie=c(pm, lie), present_truth=c(pm, tru), present_np=c(pm, npt),
                sys=c(sys_h, scen), user=c(usr_h, scen), resp_lie=c(rsp_h, lie), resp_truth=c(rsp_h, tru),
                with_word=c(pm, scen & ctx), without_word=c(pm, scen & ~ctx),
                lie_with=c(pm, lie & ctx), lie_without=c(pm, lie & ~ctx),
                truth_with=c(pm, tru & ctx), truth_without=c(pm, tru & ~ctx),
                np_ctx=c(sys_h | usr_h | rsp_h, npt), paired=pr))
        summary = dict(n_scenario=int(scen.sum()), n_pairs=len(pairs),
                       system_has_any_family_word=[int((any_sys & scen).sum()), int(scen.sum())],
                       system_has_lie_word=[int((any_lie_sys & scen).sum()), int(scen.sum())],
                       context_has_lie_word=[int((any_lie_ctx & scen).sum()), int(scen.sum())],
                       np_context_has_lie_word=[int((any_lie_ctx & npt).sum()), int(npt.sum())])
        js[f"{m}|{lens}"] = dict(summary=summary, rows=rows)
        fr = lambda v: f"{v[0]}/{v[1]} ({P.pct(*v)})"
        L += [f"## {m}, {'J-lens' if lens == 'J' else 'logit lens'}", "",
              f"Scenario system prompts with a word of any family: {fr(summary['system_has_any_family_word'])}; of any lie-side family: {fr(summary['system_has_lie_word'])}. "
              f"Whole context (system prompt, user prompt, response): {fr(summary['context_has_lie_word'])}. "
              f"No-pressure truths, whole context: {fr(summary['np_context_has_lie_word'])}. "
              f"Scenarios with both a lie and a truth: {summary['n_pairs']}.", ""]
        if rows:
            L += ["| family | side | position | present: lies | present: truths | word in system prompt | in user prompt | in response: lies | in response: truths | present when the context has the word | present when it does not | same scenario: both / lie only / truth only / neither |",
                  "|---|---|---|---|---|---|---|---|---|---|---|---|"]
            for r in sorted(rows, key=lambda r: (P.position_key(r["position"]), -(r["present_lie"][0] + r["present_truth"][0]))):
                L.append(f"| {r['name']} | {r['side']} | {r['position']} | {fr(r['present_lie'])} | {fr(r['present_truth'])} | {fr(r['sys'])} | {fr(r['user'])} | "
                         f"{fr(r['resp_lie'])} | {fr(r['resp_truth'])} | {fr(r['with_word'])} | {fr(r['without_word'])} | {' / '.join(map(str, r['paired']))} |")
        else:
            L.append("No family is present in 10% of the scenario transcripts.")
        L.append("")
    with open(os.path.join(FAM, "ECHO.md"), "w") as f:
        f.write("\n".join(L))
    with open(os.path.join(FAM, "echo.json"), "w") as f:
        json.dump(js, f, ensure_ascii=False)
    # compact console summary
    for key, v in js.items():
        s = v["summary"]
        rows = [r for r in v["rows"] if r["side"] == "lie"]
        tot_w = [sum(r["with_word"][i] for r in rows) for i in (0, 1)]
        tot_wo = [sum(r["without_word"][i] for r in rows) for i in (0, 1)]
        print(f"{key}: pairs {s['n_pairs']}, system prompt has any family word {s['system_has_any_family_word']}, a lie-side word {s['system_has_lie_word']}, context {s['context_has_lie_word']}, "
              f"no-pressure context {s['np_context_has_lie_word']}; lie-side families listed {len(rows)}; "
              f"pooled present with word {tot_w[0]}/{tot_w[1]}, without {tot_wo[0]}/{tot_wo[1]}")


if __name__ == "__main__":
    main()
