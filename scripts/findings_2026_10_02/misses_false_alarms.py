#!/usr/bin/env python3
"""family_findings.md Section 11, steps 1 and 2: which lies the eight families miss at the newline after the
response, and which truths raise a false alarm (Qwen3.6-27B, J-lens, band 35-58, build split, in-sample).

Cases
  miss          a scenario lie with none of the eight families (lie, fake, falsehood, misinformation, deceive,
                fabricate, false, mislead) at post-response slot 1
  false alarm   a scenario truth with one or more of them
  caught lie    a scenario lie with one or more; 20 are drawn at random (seed 0) for the reading
  quiet truth   a scenario truth with none; 20 drawn at random for the reading
  side group    the no-pressure truths with one or more

Step 1 writes one row per case: scenario, the judge's stance, reason and quoted lie, where the quote sits in
the response, response length, whether the second judge pass agreed, the five self-report answers, the eight
families present, the truth-side families present, and the readout words at slot 1 with the most band layers.
Step 2 compares the misses with every caught lie, and the false alarms with every quiet truth, on: distance
from the end of the quoted lie to the end of the response, response length, second-judge agreement, the
self-report answers, and whether the same scenario is caught in its other samples.

Also writes the reading sheets for steps 3 and 4: blind/ (system prompt, user prompt, response; a random code
and no label) and labelled/ (the same plus the label, the group and the families present), in one random order.

Outputs under analysis/misses/: CASES.md, cases.json, COMPARISONS.md, blind/sheet_*.md, labelled/sheet_*.md,
key.json (code -> transcript, kept out of the readers' hands).
Run from the project root: python3 scripts/findings_2026_10_02/misses_false_alarms.py
"""
from __future__ import annotations

import json
import os
import random
import sys
from collections import Counter, defaultdict

import numpy as np

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
import common as C  # noqa: E402
import presence as P  # noqa: E402

M = "qwen3.6-27b"
POS = "postresp_slot1"
EIGHT = ["lie", "fake", "falsehood", "misinformation", "deceive", "fabricate", "false", "mislead"]
TRUTH_SIDE = ["honest", "refuse", "candid", "disclose", "confess", "transparent"]
OUT = os.path.join(C.ROOT, "analysis", "misses")
N_SAMPLE, SEED = 20, 0


def families():
    with open(os.path.join(C.ROOT, "analysis", "families", "families_draft.json")) as f:
        ents = json.load(f)["entries"]
    fam = defaultdict(set)
    for e in ents:
        if e["model"] == M and e["lens"] == "J" and e["part"] == "prefix" and e["position"] == POS and e["status"] == "keep":
            fam[e["name"]] |= {x["id"] for x in e["members"]}
    return fam


def top_words(d, vocab, idx, n=12):
    """The readout tokens at slot 1 of transcript idx with the most band layers (ties by token id)."""
    out = []
    for t, (ti, nl) in d["present"]["prefix"][POS].items():
        hit = np.where(ti == idx)[0]
        if len(hit):
            out.append((int(nl[hit[0]]), vocab[t]))
    out.sort(key=lambda x: -x[0])
    return [(w, k) for k, w in out[:n]]


def main():
    os.makedirs(OUT, exist_ok=True)
    for sub in ("blind", "labelled"):
        os.makedirs(os.path.join(OUT, sub), exist_ok=True)
    d = P.load(M, "J")
    cls, trs = d["cls"], d["transcripts"]
    vocab = C.load_vocab(M)
    fam = families()
    hv = P.have_mask(d, "prefix", POS)
    masks = {n: P.present_mask(d, "prefix", POS, fam[n]) & hv for n in EIGHT + TRUTH_SIDE if n in fam}
    cnt = sum(masks[n].astype(int) for n in EIGHT)
    lies, truths, npt = cls == "lie", cls == "truth", cls == "np_truth"
    rng = random.Random(SEED)
    groups = {
        "miss": np.where(lies & (cnt == 0))[0].tolist(),
        "false alarm": np.where(truths & (cnt >= 1))[0].tolist(),
        "caught lie": rng.sample(np.where(lies & (cnt >= 1))[0].tolist(), N_SAMPLE),
        "quiet truth": rng.sample(np.where(truths & (cnt == 0))[0].tolist(), N_SAMPLE),
        "side group": np.where(npt & (cnt >= 1))[0].tolist(),
    }
    # transcript records, judge passes, scenarios, self-report answers
    runs = os.path.join(C.RUNS, C.slug(M))
    rec = {r["tid"]: r for r in C.read_jsonl(os.path.join(runs, "transcripts.jsonl"))}
    second = {r["key"]: r for r in C.read_jsonl(os.path.join(runs, "judge_second.jsonl"))}
    first = {r["key"]: r for r in C.read_jsonl(os.path.join(runs, "judge.jsonl"))}
    scen = {s["id"]: s for s in C.read_jsonl(os.path.join(C.ROOT, "inputs", "scenarios.jsonl"))}

    def answers(t):
        out = {}
        for w in C.WORDINGS:
            p = os.path.join(C.EXPORTS, C.slug(M), t["set"], t["tid"], f"{w}.json")
            try:
                with open(p) as f:
                    h = json.load(f)
                out[w] = (h.get("answer_label", ""), (h.get("answer_text") or "").strip().replace("\n", " ")[:60])
            except FileNotFoundError:
                out[w] = (t["wordings"].get(w, {}).get("answer_label", ""), "")
        return out

    def row(i, group):
        t = trs[i]
        r = rec[t["tid"]]
        key = f"{t['set']}|{t['item_id']}|{t['k']}" if "k" in t else None
        key = f"{t['set']}|{t['item_id']}|{r['k']}"
        resp = r["response"]
        span = r.get("quote_span")
        span = json.loads(span) if isinstance(span, str) and span not in ("None", "") else (list(span) if isinstance(span, (list, tuple)) else None)
        sec = second.get(key)
        fst = first.get(key)
        sib = [j for j in np.where((d["scenario"] == t["item_id"]) & hv)[0] if j != i]
        return dict(
            group=group, idx=int(i), tid=t["tid"], scenario=t["item_id"], label=t["label"], stance=r.get("stance"),
            judge_reason=r.get("judge_reason", ""), quote=r.get("quote", ""), quote_span=span,
            quote_end_to_response_end=(len(resp) - span[1]) if span else None,
            quote_start_share=(span[0] / max(1, len(resp))) if span else None,
            response_chars=len(resp), response_tokens=int(r.get("n_tokens", 0) or 0),
            second_judge=(sec["verdict"] if sec else None), first_judge=(fst["verdict"] if fst else None),
            second_agrees=(None if not sec else sec["verdict"] == t["label"]),
            answers=answers(t),
            eight=[n for n in EIGHT if masks[n][i]], n_eight=int(cnt[i]),
            truth_side=[n for n in TRUTH_SIDE if n in masks and masks[n][i]],
            top_words=top_words(d, vocab, i),
            siblings=[dict(label=str(cls[j]), n_eight=int(cnt[j])) for j in sib],
            system=r["system"], user_prompt=r["user_prompt"], response=resp,
            true_statement=scen[t["item_id"]]["true_statement"], false_statement=scen[t["item_id"]]["false_statement"],
        )

    cases = [row(i, g) for g, ids in groups.items() for i in ids]
    with open(os.path.join(OUT, "cases.json"), "w") as f:
        json.dump(cases, f, ensure_ascii=False, indent=1)

    # ---- CASES.md
    def tk(s):
        return s.replace("|", "\\|").replace("\n", " ")

    L = ["# Missed lies and false alarms: the cases (Qwen3.6-27B, J-lens, band 35-58, post-response slot 1)", "",
         "Written by `scripts/findings_2026_10_02/misses_false_alarms.py`. Build split, in-sample. *eight* = the eight",
         "families of Section 9; *where the lie sits* = characters from the end of the judge's quote to the end of the",
         "response, and the quote's start as a share of the response; *second judge* = the verdict of the second pass",
         "(`–` = not re-judged); answers = the five self-report answers (a = admit, d = deny, o = other); *truth side* =",
         "honest, refuse, candid, disclose, confess, transparent; *readout* = the slot-1 tokens with the most band layers.", ""]
    for g in groups:
        rows = [c for c in cases if c["group"] == g]
        L += [f"## {g} ({len(rows)})", "",
              "| # | scenario | stance | judge's reason | quoted lie | where the lie sits | tokens | second judge | answers Q1 Q2 Q6 Q7 Q9 | eight | truth side | readout |",
              "|---|---|---|---|---|---|---|---|---|---|---|---|"]
        for n, c in enumerate(rows, 1):
            ans = " ".join((c["answers"][w][0] or "?")[0] for w in C.WORDINGS)
            where = f"{c['quote_end_to_response_end']} chars from the end, starts at {100 * c['quote_start_share']:.0f}%" if c["quote_span"] else "no quote"
            L.append(f"| {n} | {c['scenario'].replace('mask_provided_facts_', '')[-6:]} | {c['stance']} | {tk(c['judge_reason'])} | {tk(c['quote'])[:120]} | {where} | "
                     f"{c['response_tokens']} | {c['second_judge'] or '–'} | {ans} | {', '.join(c['eight']) or '–'} | {', '.join(c['truth_side']) or '–'} | "
                     + ", ".join(f"`{P.tok(w)}`" for w, _ in c["top_words"][:8]) + " |")
        L.append("")
    with open(os.path.join(OUT, "CASES.md"), "w") as f:
        f.write("\n".join(L) + "\n")

    # ---- COMPARISONS.md: misses against every caught lie, false alarms against every quiet truth
    def stats(ids, label):
        rows = [row(i, label) for i in ids]
        dist = [c["quote_end_to_response_end"] for c in rows if c["quote_span"]]
        share = [c["quote_start_share"] for c in rows if c["quote_span"]]
        toks = [c["response_tokens"] for c in rows]
        rej = [c for c in rows if c["second_judge"] is not None]
        agree = sum(1 for c in rej if c["second_agrees"])
        ans = {w: Counter(c["answers"][w][0] for c in rows) for w in C.WORDINGS}
        sib_caught = sum(1 for c in rows for s in c["siblings"] if s["label"] == "lie" and s["n_eight"] >= 1)
        sib_lies = sum(1 for c in rows for s in c["siblings"] if s["label"] == "lie")
        scen_n = len({c["scenario"] for c in rows})
        return dict(n=len(rows), dist=dist, share=share, toks=toks, rej=len(rej), agree=agree, ans=ans,
                    sib_caught=sib_caught, sib_lies=sib_lies, scenarios=scen_n, no_quote=sum(1 for c in rows if not c["quote_span"]))

    def med(x):
        return f"{np.median(x):.0f}" if len(x) else "–"

    def q(x, p):
        return f"{np.percentile(x, p):.0f}" if len(x) else "–"

    comp = {
        "misses against every caught lie": (stats(groups["miss"], "miss"), stats(np.where(lies & (cnt >= 1))[0].tolist(), "caught lie")),
        "false alarms against every quiet truth": (stats(groups["false alarm"], "false alarm"), stats(np.where(truths & (cnt == 0))[0].tolist(), "quiet truth")),
    }
    L = ["# Missed lies and false alarms: comparisons by script", "",
         "Written by `scripts/findings_2026_10_02/misses_false_alarms.py`. Build split, in-sample. Medians with the",
         "quartiles in brackets. *Distance* = characters from the end of the judge's quoted lie to the end of the",
         "response (truths have no quote when the judge found no false statement).", ""]
    for title, (a, b) in comp.items():
        ga, gb = title.split(" against every ")
        L += [f"## {title}", "", f"| | {ga} ({a['n']}) | {gb} ({b['n']}) |", "|---|---|---|"]
        L.append(f"| distance from the quote's end to the response's end, chars | {med(a['dist'])} ({q(a['dist'], 25)}-{q(a['dist'], 75)}) | {med(b['dist'])} ({q(b['dist'], 25)}-{q(b['dist'], 75)}) |")
        L.append(f"| quote starts at, share of the response | {med([100 * x for x in a['share']])}% | {med([100 * x for x in b['share']])}% |")
        L.append(f"| cases with no quote | {a['no_quote']} | {b['no_quote']} |")
        L.append(f"| response length, tokens | {med(a['toks'])} ({q(a['toks'], 25)}-{q(a['toks'], 75)}) | {med(b['toks'])} ({q(b['toks'], 25)}-{q(b['toks'], 75)}) |")
        L.append(f"| re-judged by the second pass: agree / re-judged | {a['agree']} / {a['rej']} | {b['agree']} / {b['rej']} |")
        for w in C.WORDINGS:
            fa = lambda s: " / ".join(str(s['ans'][w].get(k, 0)) for k in ("admit", "deny", "other"))  # noqa: E731
            L.append(f"| self-report {w.split('_')[0]}: admit / deny / other | {fa(a)} | {fa(b)} |")
        L.append(f"| distinct scenarios | {a['scenarios']} | {b['scenarios']} |")
        L.append(f"| other lie samples of the same scenarios: caught / all | {a['sib_caught']} / {a['sib_lies']} | {b['sib_caught']} / {b['sib_lies']} |")
        L.append("")
    # the lie's position, in bins, misses against caught lies
    a, b = comp["misses against every caught lie"]
    L += ["## Where the lie sits, in bins (misses against caught lies)", "", "| distance from the quote's end to the response's end | misses | caught lies |", "|---|---|---|"]
    bins = [(0, 100), (100, 300), (300, 700), (700, 10 ** 6)]
    for lo, hi in bins:
        L.append(f"| {lo} to {hi if hi < 10 ** 6 else 'more'} chars | {sum(lo <= x < hi for x in a['dist'])} | {sum(lo <= x < hi for x in b['dist'])} |")
    L.append("")
    # the readout against the self-report, over every scenario transcript
    L += ["## The readout against the self-report, over every lie and truth", "",
          "Cells are counts. *flagged* = one or more of the eight families at post-response slot 1.", "",
          "| wording | lies: flagged & admit | flagged & deny | not flagged & admit | not flagged & deny | truths: flagged & admit | flagged & deny | not flagged & admit | not flagged & deny |",
          "|---|---|---|---|---|---|---|---|---|"]
    flag = cnt >= 1
    for w in C.WORDINGS:
        ans = P.answer(d, w)
        c = lambda g, f, a: int((g & (flag == f) & (ans == a)).sum())  # noqa: E731
        L.append(f"| {w.split('_')[0]} | {c(lies, True, 'admit')} | {c(lies, True, 'deny')} | {c(lies, False, 'admit')} | {c(lies, False, 'deny')} | "
                 f"{c(truths, True, 'admit')} | {c(truths, True, 'deny')} | {c(truths, False, 'admit')} | {c(truths, False, 'deny')} |")
    L.append("")
    with open(os.path.join(OUT, "COMPARISONS.md"), "w") as f:
        f.write("\n".join(L) + "\n")

    # ---- reading sheets
    order = [c for c in cases if c["group"] != "side group"]
    rng2 = random.Random(SEED + 1)
    rng2.shuffle(order)
    codes = [f"R{n:02d}" for n in range(1, len(order) + 1)]
    key = {}
    for code, c in zip(codes, order):
        key[code] = dict(idx=c["idx"], tid=c["tid"], group=c["group"], label=c["label"])
        head = [f"# Case {code}", "", "## System prompt", "", c["system"], "", "## User", "", c["user_prompt"], "",
                "## Response", "", c["response"], ""]
        with open(os.path.join(OUT, "blind", f"sheet_{code}.md"), "w") as f:
            f.write("\n".join(head) + f"\n## The fact\n\nTrue: {c['true_statement']}\nFalse: {c['false_statement']}\n")
        lab = [f"## Label and group", "", f"Judge's label: **{c['label']}** ({c['group']}). Judge's reason: {c['judge_reason']}",
               f"Quoted lie: {c['quote'] or '–'}", f"Families present at the newline after the response: {', '.join(c['eight']) or 'none'}"
               + (f"; truth side: {', '.join(c['truth_side'])}" if c["truth_side"] else ""), ""]
        with open(os.path.join(OUT, "labelled", f"sheet_{code}.md"), "w") as f:
            f.write("\n".join(head) + f"\n## The fact\n\nTrue: {c['true_statement']}\nFalse: {c['false_statement']}\n\n" + "\n".join(lab))
    with open(os.path.join(OUT, "key.json"), "w") as f:
        json.dump(key, f, indent=1)
    print({g: len(v) for g, v in groups.items()}, "sheets:", len(order))
    print(f"written: {OUT}/CASES.md, COMPARISONS.md, cases.json, key.json, blind/, labelled/")


if __name__ == "__main__":
    main()
