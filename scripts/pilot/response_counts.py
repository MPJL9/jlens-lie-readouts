#!/usr/bin/env python3
"""Experiment 2 pilot, step 1: which fixed word lists the J-lens readout holds at the model's own response
tokens, and where (Qwen3.6-27B, J-lens, band 35-58, build split plus the unrelated sets, in-sample).

For every response token of every transcript, a word list is *present* when one of its tokens is in the
top-16 readout at one or more band layers; the number of such band layers is kept as the strength. The lists
are fixed and printed in the output: the ten lie-side families of post-response slot 1, `evade`, `vague`, the
truth-side families (honest, candid, disclose, confess), `refuse`, `knowingly`, `cannot`, `deny`, and the
situation words (the junk survey's kind "deception and the situation", minus every token that belongs to a
slot-1 family). Each response token also gets a type (word, number, punctuation, line break, space) and, for
lies, a place relative to the judge's quoted lie (before, inside, after), found by locating the quote's text
in the joined response tokens. An *echo* flag per transcript and list says whether the response text itself
contains one of the list's words, since the readout can copy the text.

Outputs under analysis/pilot/: marks.pkl (per transcript: token types, places, strengths [tokens, lists],
echo flags, the quote's token span), COUNTS.md (the tables), lists.json (the lists with their tokens).
Run from the project root: python3 scripts/pilot/response_counts.py
"""
from __future__ import annotations

import json
import os
import pickle
import sys
import time
import unicodedata
from collections import defaultdict

import numpy as np

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
import common as C  # noqa: E402
import presence as P  # noqa: E402

M = "qwen3.6-27b"
BAND = C.BANDS[M]
OUT = os.path.join(C.ROOT, "analysis", "pilot")
TEN = ["lie", "fake", "deceive", "falsehood", "fabricate", "conceal", "misinformation", "false", "mislead", "dishonest"]
# The pooled set for the response tokens (user, 2026-10-03): the ten without `false` and `falsehood`, which appear at
# the model's answer word "No" (22% of the tokens "No" carry `false`; no other family is above 2%), so they follow
# the answer and not the situation. Called "the lie-side set"; not to be confused with "the eight" of the newline.
POOL = [n for n in TEN if n not in ("false", "falsehood")]
PRESSURE = ["conceal", "deceive", "dishonest", "lie", "mislead"]     # the pressure set (scripts/pilot/where_words_sit.py)
EXTRA_FAM = ["evade", "vague", "honest", "candid", "disclose", "confess", "refuse"]
BY_TEXT = {  # lists given by token text (stripped, lower-cased), as in family_findings.md Sections 5 and 11
    "knowingly": ["knowingly", "knowing", "明知"],
    "cannot": ["cannot", "unable", "无法", "我不能", "我无法"],
    "deny": ["deny", "denied", "denial", "denies", "denying", "否认", "否定"],
}
TYPES = ["word", "number", "punctuation", "line break", "space"]
PLACES = ["before", "inside", "after", "no quote"]
CLASSES = [("lies", "lie"), ("truths", "truth"), ("no-pressure truths", "np_truth"), ("unrelated", "unrelated")]


def token_type(s):
    if "\n" in s:
        return 3
    t = s.strip()
    if not t:
        return 4
    cats = [unicodedata.category(ch) for ch in t]
    if all(c[0] in "PS" for c in cats):
        return 2
    if all(ch.isdigit() or ch in ".,%-:/" for ch in t) and any(ch.isdigit() for ch in t):
        return 1
    return 0


def build_lists(vocab):
    """{name: sorted token ids}; slot-1 draft families first, then the text lists, then the situation words."""
    with open(os.path.join(C.ROOT, "analysis", "families", "families_draft.json")) as f:
        ents = json.load(f)["entries"]
    fam = defaultdict(set)
    for e in ents:
        if e["model"] == M and e["lens"] == "J" and e["part"] == "prefix" and e["position"] == "postresp_slot1" and e["status"] == "keep":
            fam[e["name"]] |= {x["id"] for x in e["members"]}
    lists = {n: sorted(fam[n]) for n in TEN + EXTRA_FAM}
    for n, words in BY_TEXT.items():
        w = set(words)
        lists[n] = sorted(i for i, t in enumerate(vocab) if t.strip().lower() in w)
    with open(os.path.join(C.ROOT, "analysis", "junk", "kind_of_token.json")) as f:
        kind = {int(k): v for k, v in json.load(f).items()}
    in_fam = set().union(*fam.values())
    deny = set(lists["deny"])
    lists["situation"] = sorted(t for t, k in kind.items() if k == "deception_situation" and t not in in_fam and t not in deny)
    return lists


def locate_quote(tokens, quote):
    """Token span [a, b) of the quote inside the response tokens, or None. Tries the full quote, then its
    first 40 characters, then its first 15 (emoji byte pieces can break the exact join)."""
    joined = "".join(tokens)
    if not quote:
        return None
    for probe in (quote, quote[:40], quote[:15]):
        k = joined.find(probe)
        if k >= 0:
            break
    else:
        return None
    end = k + len(quote) if probe == quote else min(len(joined), k + len(quote))
    offs, c = [], 0
    for t in tokens:
        offs.append((c, c + len(t)))
        c += len(t)
    inside = [i for i, (a, b) in enumerate(offs) if b > k and a < end]
    return (inside[0], inside[-1] + 1) if inside else None


def main():
    os.makedirs(OUT, exist_ok=True)
    vocab = C.load_vocab(M)
    lists = build_lists(vocab)
    names = list(lists)
    member = np.zeros((len(vocab), len(names)), bool)
    for j, n in enumerate(names):
        member[lists[n], j] = True
    with open(os.path.join(OUT, "lists.json"), "w") as f:
        json.dump({n: [vocab[i] for i in ids] for n, ids in lists.items()}, f, ensure_ascii=False, indent=1)
    texts = {n: {vocab[i].strip().lower() for i in ids if len(vocab[i].strip()) >= 2} for n, ids in lists.items()}

    man = C.load_manifest(M)
    rec = C.load_transcripts(M)
    entries = [e for e in man["transcripts"] if e["split"] == "build" or e["set"] in ("unrelated", "unrelated_extra")]
    layers = man["layers"]
    lidx = [i for i, l in enumerate(layers) if BAND[0] <= l <= BAND[1]]
    marks, t0 = [], time.time()
    for k, e in enumerate(entries):
        h, a = C.read_part(M, e, "prefix")
        item = dict(tokens=h["tokens"], ids=h["ids"], segments=h["segments"])
        pos = C.positions(item)
        n = sum(1 for q in pos if q.startswith("resp_tok"))
        p0 = pos["resp_tok0"]
        toks = h["tokens"][p0:p0 + n]
        block = a["J_ids"][lidx, p0:p0 + n, :]                 # [band layers, n, 16]
        hit = member[block]                                     # [band, n, 16, L]
        strength = hit.any(axis=2).sum(axis=0).astype(np.uint8)  # [n, L]
        r = rec[e["tid"]]
        span = locate_quote(toks, r.get("quote") or "") if e["label"] == "lie" else None
        place = np.full(n, 3, np.uint8)
        if span:
            place[:span[0]] = 0
            place[span[0]:span[1]] = 1
            place[span[1]:] = 2
        low = r["response"].lower()
        echo = np.array([any(w in low for w in texts[nm]) for nm in names], bool)
        cls = e["label"] if e["set"] == "scenario" else ("np_truth" if e["set"] == "nopressure" and e["label"] == "truth" else
                                                           "np_lie" if e["set"] == "nopressure" else "unrelated")
        marks.append(dict(tid=e["tid"], set=e["set"], cls=cls, item_id=e["item_id"], n=n, tokens=toks,
                          types=np.array([token_type(t) for t in toks], np.uint8), place=place, strength=strength,
                          quote_span=span, has_quote=bool(r.get("quote")), echo=echo))
        if (k + 1) % 200 == 0 or k + 1 == len(entries):
            print(f"  {k + 1}/{len(entries)} transcripts ({time.time() - t0:.0f} s)", flush=True)
    with open(os.path.join(OUT, "marks.pkl"), "wb") as f:
        pickle.dump(dict(model=M, band=list(BAND), names=names, lists=lists, types=TYPES, places=PLACES, marks=marks), f, protocol=4)
    write_counts(marks, names, lists, vocab)


def write_counts(marks, names, lists, vocab):
    J = {n: j for j, n in enumerate(names)}
    ten = [J[n] for n in POOL]
    truth_side = [J[n] for n in ("honest", "candid", "disclose", "confess")]
    by = {c: [m for m in marks if m["cls"] == c] for _, c in CLASSES}
    # the newline after the response, for reference
    d = P.load(M, "J")
    hv = P.have_mask(d, "prefix", "postresp_slot1")
    tid_idx = {t["tid"]: i for i, t in enumerate(d["transcripts"])}

    def slot1(n, ms):
        m = P.present_mask(d, "prefix", "postresp_slot1", lists[n]) & hv
        ids = [tid_idx[x["tid"]] for x in ms if x["tid"] in tid_idx]
        return int(m[ids].sum()), len(ids)

    def pct(a, b):
        return f"{a}/{b} ({100 * a / b:.0f}%)" if b else "–"

    def any_tok(m, js):
        return (m["strength"][:, js] > 0).any(axis=1)          # [n] bool: any of the lists present at the token

    L = [f"# Experiment 2 pilot, step 1: word lists at the response tokens (Qwen3.6-27B, J-lens, band {BAND[0]}-{BAND[1]})", "",
         "Written by `scripts/pilot/response_counts.py`. Build split plus the unrelated sets (158 + 545 extra chats,",
         "commentary dropped), in-sample. *present at a token* = one of the list's tokens is in the top 16 at one or",
         "more band layers at that response token. Lists are in `analysis/pilot/lists.json`; the slot-1 families use",
         "the draft lists of that position.", "",
         "**The lie-side set** = the ten lie-side families without `false` and `falsehood`: " + ", ".join(POOL) + ". Changed by the user on",
         "2026-10-03: `false` and `falsehood` appear at the model's answer word \"No\", so they follow the answer. Their own rows are kept.", "",
         f"Transcripts: " + ", ".join(f"{lab} {len(by[c])}" for lab, c in CLASSES) + ". Response tokens: " +
         ", ".join(f"{lab} {sum(m['n'] for m in by[c])}" for lab, c in CLASSES) + ".", ""]

    # ---- A. transcripts with the list at one or more response tokens, at the last token, at the newline
    L += ["## A. Share of transcripts with the list present", "",
          "Three places: at one or more response tokens; at the last response token; at the newline after the response",
          "(post-response slot 1, from the presence index, for reference). Cells: lies / truths / no-pressure truths / unrelated.", "",
          "| list | tokens in the list | at any response token | at the last response token | at the newline |", "|---|---|---|---|---|"]
    press = [J[n] for n in PRESSURE]
    members = {"any of the lie-side set (the ten without false, falsehood)": POOL, "any of the pressure set (conceal, deceive, dishonest, lie, mislead)": PRESSURE,
               "any truth-side (honest, candid, disclose, confess)": ["honest", "candid", "disclose", "confess"]}
    rows = [(n, [J[n]]) for n in names] + [(k, [J[x] for x in v]) for k, v in members.items()]
    for n, js in rows:
        anyr = " / ".join(pct(sum(1 for m in by[c] if any_tok(m, js).any()), len(by[c])) for _, c in CLASSES)
        last = " / ".join(pct(sum(1 for m in by[c] if m["n"] and any_tok(m, js)[-1]), len(by[c])) for _, c in CLASSES)
        if n in lists:
            nl = " / ".join(pct(*slot1(n, by[c])) for _, c in CLASSES)
            ntok = len(lists[n])
        else:
            masks = {c: np.zeros(len(by[c]), bool) for _, c in CLASSES}
            for nm in members[n]:
                m = P.present_mask(d, "prefix", "postresp_slot1", lists[nm]) & hv
                for _, c in CLASSES:
                    ids = [tid_idx[x["tid"]] for x in by[c]]
                    masks[c] |= m[ids]
            nl = " / ".join(pct(int(masks[c].sum()), len(by[c])) for _, c in CLASSES)
            ntok = "–"
        L.append(f"| {n} | {ntok} | {anyr} | {last} | {nl} |")
    L.append("")

    # ---- B. share of response tokens carrying the list
    L += ["## B. Share of response tokens carrying the list (all tokens of the class pooled)", "",
          "| list | lies | truths | no-pressure truths | unrelated |", "|---|---|---|---|---|"]
    for n, js in rows:
        cells = []
        for _, c in CLASSES:
            tot = sum(m["n"] for m in by[c])
            k = sum(int(any_tok(m, js).sum()) for m in by[c])
            cells.append(f"{100 * k / tot:.1f}%" if tot else "–")
        L.append(f"| {n} | " + " | ".join(cells) + " |")
    L.append("")

    # ---- C. lies: by place relative to the quoted lie, and by distance
    lies = by["lie"]
    withq = [m for m in lies if m["quote_span"]]
    L += ["## C. Lies: where the lie-side words sit relative to the judge's quoted lie", "",
          f"{len(withq)} of {len(lies)} lies have a quote that was located in the response tokens "
          f"({sum(1 for m in lies if m['has_quote'] and not m['quote_span'])} quotes not located, "
          f"{sum(1 for m in lies if not m['has_quote'])} lies without a quote). Share of tokens carrying any of the lie-side set, by place:", "",
          "| place | tokens | carrying any of the lie-side set | carrying `lie` | carrying any truth-side |", "|---|---|---|---|---|"]
    for pi, pl in enumerate(PLACES[:3]):
        tot = sum(int((m["place"] == pi).sum()) for m in withq)
        a = sum(int((any_tok(m, ten) & (m["place"] == pi)).sum()) for m in withq)
        b = sum(int((any_tok(m, [J["lie"]]) & (m["place"] == pi)).sum()) for m in withq)
        t = sum(int((any_tok(m, truth_side) & (m["place"] == pi)).sum()) for m in withq)
        L.append(f"| {pl} the quote | {tot} | {pct(a, tot)} | {pct(b, tot)} | {pct(t, tot)} |")
    tot = sum(m["n"] for m in by["truth"])
    L.append(f"| (truths, all tokens) | {tot} | {pct(sum(int(any_tok(m, ten).sum()) for m in by['truth']), tot)} | "
             f"{pct(sum(int(any_tok(m, [J['lie']]).sum()) for m in by['truth']), tot)} | {pct(sum(int(any_tok(m, truth_side).sum()) for m in by['truth']), tot)} |")
    L += ["", "By distance in tokens from the quote (negative = before its start, positive = after its end):", "",
          "| distance | tokens | carrying any of the lie-side set | carrying `lie` |", "|---|---|---|---|"]
    bins = [(-10 ** 6, -50), (-50, -20), (-20, -5), (-5, 0), ("inside", None), (1, 5), (6, 20), (21, 50), (51, 10 ** 6)]
    for lo, hi in bins:
        tot = a = b = 0
        for m in withq:
            s, e = m["quote_span"]
            idx = np.arange(m["n"])
            if lo == "inside":
                sel = (idx >= s) & (idx < e)
            elif hi <= 0:
                dist = idx - s
                sel = (idx < s) & (dist >= lo) & (dist < hi)
            else:
                dist = idx - e + 1
                sel = (idx >= e) & (dist >= lo) & (dist <= hi)
            tot += int(sel.sum())
            a += int((any_tok(m, ten) & sel).sum())
            b += int((any_tok(m, [J["lie"]]) & sel).sum())
        label = "inside the quote" if lo == "inside" else (f"{lo} to {hi - 1}" if hi <= 0 else f"+{lo} to +{hi}" if hi < 10 ** 6 else f"+{lo} and beyond")
        L.append(f"| {label} | {tot} | {pct(a, tot)} | {pct(b, tot)} |")
    L.append("")
    # first token with `lie`, relative to the quote start
    first = []
    for m in withq:
        w = np.where(any_tok(m, [J["lie"]]))[0]
        first.append(int(w[0]) - m["quote_span"][0] if len(w) else None)
    never = sum(1 for x in first if x is None)
    before = sum(1 for x in first if x is not None and x < 0)
    inside = sum(1 for x, m in zip(first, withq) if x is not None and 0 <= x < m["quote_span"][1] - m["quote_span"][0])
    after = len(withq) - never - before - inside
    L += [f"The first response token carrying `lie`, among the {len(withq)} lies with a located quote: before the quote in {before}, "
          f"inside it in {inside}, after it in {after}, never in {never}.", ""]
    # persistence: the last tokens, and the newline, for lies whose quote carries the words
    carry = [m for m in withq if (any_tok(m, ten) & (m["place"] == 1)).any()]
    last3 = sum(1 for m in carry if any_tok(m, ten)[-3:].any())
    L += [f"Of the {len(carry)} lies with any of the lie-side set inside the quote, {last3} also carry one at one of the last three response tokens.", ""]

    # ---- D. by token type
    L += ["## D. By token type: share of tokens carrying any of the lie-side set", "",
          "| token type | lies | truths | no-pressure truths | unrelated |", "|---|---|---|---|---|"]
    for ti, tn in enumerate(TYPES):
        cells = []
        for _, c in CLASSES:
            tot = sum(int((m["types"] == ti).sum()) for m in by[c])
            a = sum(int((any_tok(m, ten) & (m["types"] == ti)).sum()) for m in by[c])
            cells.append(pct(a, tot))
        L.append(f"| {tn} | " + " | ".join(cells) + " |")
    L.append("")

    # ---- E. the 19 misses and the caught lies
    m1 = P.present_mask(d, "prefix", "postresp_slot1", sorted(set().union(*[set(lists[n]) for n in ["lie", "fake", "falsehood", "misinformation", "deceive", "fabricate", "false", "mislead"]]))) & hv
    miss = [m for m in lies if not m1[tid_idx[m["tid"]]]]
    caught = [m for m in lies if m1[tid_idx[m["tid"]]]]
    L += ["## E. The lies the newline misses, against the caught lies", "",
          "*caught* = one of the eight families at the newline after the response; *missed* = none.", "",
          "| | missed lies | caught lies |", "|---|---|---|"]
    for lab, js in [("any of the lie-side set at one or more response tokens", ten), ("any of the pressure set at one or more response tokens", press),
                    ("`lie` at one or more response tokens", [J["lie"]]),
                    ("any of the lie-side set at one of the last three response tokens", ten), ("any truth-side at one or more response tokens", truth_side),
                    ("`refuse` at one or more response tokens", [J["refuse"]]), ("`evade` or `vague` at one or more response tokens", [J["evade"], J["vague"]])]:
        if "last three" in lab:
            f = lambda ms: sum(1 for m in ms if any_tok(m, js)[-3:].any())  # noqa: E731
        else:
            f = lambda ms: sum(1 for m in ms if any_tok(m, js).any())  # noqa: E731
        L.append(f"| {lab} | {pct(f(miss), len(miss))} | {pct(f(caught), len(caught))} |")
    L.append("| share of response tokens carrying any of the lie-side set | " + " | ".join(
        f"{100 * sum(int(any_tok(m, ten).sum()) for m in g) / max(1, sum(m['n'] for m in g)):.1f}%" for g in (miss, caught)) + " |")
    L.append("")

    # ---- G. strength: a lenient "one band layer" over hundreds of tokens gives many chances
    def slot1_strength(tid, ids):
        i, best = tid_idx[tid], 0
        tab = d["present"]["prefix"]["postresp_slot1"]
        for t in ids:
            h = tab.get(t)
            if h is not None:
                w = np.where(h[0] == i)[0]
                if len(w):
                    best = max(best, int(h[1][w[0]]))
        return best
    ten_ids = sorted(set().union(*[set(lists[n]) for n in POOL]))
    L += ["## G. Strength: transcripts with any of the lie-side set at a token held by at least s band layers", "",
          "Table A counts a word present at one band layer, which over a response of hundreds of tokens gives many chances.",
          "Here s is the number of band layers (of 24) whose top 16 hold one of the lie-side set at that token; the newline is given beside it.", "",
          "| s | at a response token: lies / truths / np truths / unrelated | at the newline |", "|---|---|---|"]
    for s_ in (1, 2, 4, 8, 12, 16):
        a = " / ".join(pct(sum(1 for m in by[c] if m["n"] and (m["strength"][:, ten].max(axis=1) >= s_).any()), len(by[c])) for _, c in CLASSES)
        b = " / ".join(pct(sum(1 for m in by[c] if slot1_strength(m["tid"], ten_ids) >= s_), len(by[c])) for _, c in CLASSES)
        L.append(f"| {s_} | {a} | {b} |")
    press_ids = sorted(set().union(*[set(lists[n]) for n in PRESSURE]))
    L += ["", "The same for the pressure set:", "", "| s | at a response token: lies / truths / np truths / unrelated | at the newline |", "|---|---|---|"]
    for s_ in (1, 2, 4, 8, 12, 16):
        a = " / ".join(pct(sum(1 for m in by[c] if m["n"] and (m["strength"][:, press].max(axis=1) >= s_).any()), len(by[c])) for _, c in CLASSES)
        b = " / ".join(pct(sum(1 for m in by[c] if slot1_strength(m["tid"], press_ids) >= s_), len(by[c])) for _, c in CLASSES)
        L.append(f"| {s_} | {a} | {b} |")
    L += ["", "Response tokens with any of the lie-side set held by 8 or more band layers, per 100 tokens: " +
          ", ".join(f"{lab} {100 * sum(int((m['strength'][:, ten].max(axis=1) >= 8).sum()) for m in by[c]) / max(1, sum(m['n'] for m in by[c])):.1f}" for lab, c in CLASSES) + ".", ""]

    # ---- F. echo
    L += ["## F. Echo: transcripts whose response text contains a word of the list", "",
          "The readout can copy the text, so Table A is repeated without these transcripts.", "",
          "| list | text contains a list word: lies / truths / np truths / unrelated | at any response token, echo transcripts left out |", "|---|---|---|"]
    for n in names:
        j = J[n]
        e = " / ".join(f"{sum(1 for m in by[c] if m['echo'][j])}/{len(by[c])}" for _, c in CLASSES)
        a = " / ".join(pct(sum(1 for m in by[c] if not m["echo"][j] and any_tok(m, [j]).any()), sum(1 for m in by[c] if not m["echo"][j])) for _, c in CLASSES)
        L.append(f"| {n} | {e} | {a} |")
    L.append("")

    # ---- the lists
    L += ["## The lists", ""]
    for n in names:
        L.append(f"- **{n}** ({len(lists[n])}): " + ", ".join(f"`{P.tok(vocab[i])}`" for i in lists[n]))
    L.append("")
    with open(os.path.join(OUT, "COUNTS.md"), "w") as f:
        f.write("\n".join(L) + "\n")
    print(f"written: {OUT}/COUNTS.md, marks.pkl, lists.json")


if __name__ == "__main__":
    main()
