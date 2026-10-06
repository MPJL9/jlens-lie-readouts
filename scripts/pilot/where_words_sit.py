#!/usr/bin/env python3
"""Experiment 2 pilot, step 3: where in the response the situation words of the readout sit (Qwen3.6-27B, J-lens,
band 35-58, build split plus the unrelated sets, in-sample). Reads analysis/pilot/marks.pkl.

Tracked readout words: the lie-side set, which is the ten lie-side families of post-response slot 1 without
`false` and `falsehood` (user, 2026-10-03: those two appear when the model answers "No"; Section 0.1 of the
output counts it), pooled and each, and `honest` (user, 2026-10-03: a situation-revealing word; `refuse` and
the other truth-side words are left out because they describe the response). The rows of `false` and
`falsehood` are still shown on their own. A token *carries* a list when one of the list's tokens is in its top-16 readout at
one or more band layers.

Excluded (user, 2026-10-03): every response whose own text contains a lie-side word or an honest word, matched
as whole words on word stems ("to be honest", "lying", "misled", "fabrication"), because the readout then shows
the word as a guess at the next token. Responses that write "false" stay left out although `false` is no longer
pooled: the Chinese members of `fake` and `misinformation` (假, 虚假, 虚假信息) mean "false".

Each response token gets three labels:
  kind       a mark type (sentence end, comma, colon or semicolon, quote or bracket, dash, markdown mark, other
             mark, line break, space) or, for tokens with a letter or digit, the word class of the word the token
             belongs to (noun, name, verb, auxiliary, adjective, adverb, negation, pronoun, determiner,
             preposition, conjunction, number, other word), from NLTK's English tagger run sentence by sentence
  piece      for word tokens: first piece (or the whole word), or a later piece of a split word
  position   paragraph start, sentence start, last word of a sentence, elsewhere
and, for lies, a place: before, at or after the deception sentence (the judge's quote widened to the full
sentences that contain it).

Outputs under analysis/pilot/: WHERE.md (the tables, all with counts), labels.pkl (per transcript: the labels,
the exclusion and the matched words), LABEL_CHECK.md (200 tokens with their labels, for checking the tagger).
Run from the project root: python3 scripts/pilot/where_words_sit.py
"""
from __future__ import annotations

import os
import pickle
import re
import sys
from collections import Counter, defaultdict

import nltk
import numpy as np

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
import common as C  # noqa: E402

M = "qwen3.6-27b"
OUT = os.path.join(C.ROOT, "analysis", "pilot")
TEN = ["lie", "fake", "deceive", "falsehood", "fabricate", "conceal", "misinformation", "false", "mislead", "dishonest"]
# the pooled set (user, 2026-10-03): the ten without `false` and `falsehood`, which follow the answer word "No"
POOL = [n for n in TEN if n not in ("false", "falsehood")]
PNAME = "lie-side set"
# the pressure set (2026-10-03): the lie-side families that are in the pressured transcripts, lies and truths alike, and
# much less in the no-pressure truths (WHERE.md Section 0); `misinformation`, `fabricate` and `fake` are left out
PRESSURE = ["conceal", "deceive", "dishonest", "lie", "mislead"]
PRNAME = "pressure set"
POOLED = [PNAME, PRNAME, "honest"]
TITLE = {PNAME: "The lie-side set", PRNAME: "The pressure set", "honest": "`honest`"}
MIN_PART = 5            # a part (before / at / after) counts only with this many tokens
N_BOOT, SEED = 2000, 0
CLASSES = [("lies", "lie"), ("truths", "truth"), ("no-pressure truths", "np_truth"), ("unrelated", "unrelated")]

# whole-word rules on word stems, used to exclude responses whose text contains the words
RULES = {
    "lie": r"\b(lie|lies|lied|lying|liar|liars)\b",
    "fake": r"\bfak(e|es|ed|ing|ery)\b",
    "deceive": r"\bdece(iv|pt|it)\w*",
    "falsehood": r"\bfalsehoods?\b",
    "fabricate": r"\bfabricat\w*",
    "conceal": r"\bconceal\w*",
    "misinformation": r"\b(mis|dis)inform\w*",
    "false": r"\b(fals(e|ely|ity|ify|ified|ifying)|untru(e|th|ths))\b",
    "mislead": r"\bmis(lead|leads|leading|led)\b",
    "dishonest": r"\bdishonest\w*",
    "honest": r"\bhonest\w*",
}
RX = {k: re.compile(v, re.I) for k, v in RULES.items()}

MARKS = ["sentence end", "comma", "colon or semicolon", "quote or bracket", "dash", "markdown mark", "other mark", "line break", "space"]
WORDS = ["noun", "name", "verb", "auxiliary", "adjective", "adverb", "negation", "pronoun", "determiner", "preposition", "conjunction",
         "number", "other word"]
KINDS = WORDS + MARKS
POSITIONS = ["paragraph start", "sentence start", "last word of a sentence", "elsewhere"]
NEG = {"not", "n't", "never", "no", "none", "nor", "neither", "cannot", "nothing", "nobody"}
AUX = {"is", "are", "was", "were", "be", "been", "being", "am", "'s", "'re", "'m", "have", "has", "had", "'ve", "'d", "do", "does", "did",
       "ca", "wo", "'ll"}
ABBR = {"mr", "mrs", "ms", "dr", "vs", "etc", "e.g", "i.e", "st", "inc", "ltd", "co", "jr", "sr", "prof", "u.s", "u.k", "a.m", "p.m"}
WORD_RE = re.compile(r"n't|'(?:s|re|ve|ll|d|m)\b|[A-Za-z]+(?=n't)|\w+|[^\w\s]")
GROUPS = [("content words (noun, name, verb, adjective, adverb)", {"noun", "name", "verb", "adjective", "adverb"}),
          ("function words (auxiliary, pronoun, determiner, preposition, conjunction, negation, number, other)",
           {"auxiliary", "pronoun", "determiner", "preposition", "conjunction", "negation", "number", "other word"}),
          ("sentence end", {"sentence end"}), ("comma", {"comma"}),
          ("other marks, line breaks, spaces", {"colon or semicolon", "quote or bracket", "dash", "markdown mark", "other mark", "line break", "space"})]


def sentence_spans(text):
    """Character spans of sentences: a sentence ends at . ! ? followed by blank space or the end (after closing
    quotes, brackets or markdown stars), or at a line break. Abbreviations, initials and list numbers do not end one."""
    spans, start, i, n = [], 0, 0, len(text)
    while start < n and text[start].isspace():
        start += 1
    i = start
    while i < n:
        ch = text[i]
        if ch == "\n":
            if i > start:
                spans.append((start, i))
            j = i
            while j < n and text[j].isspace():
                j += 1
            start = i = j
            continue
        if ch in ".!?":
            j = i + 1
            while j < n and text[j] in ".!?":
                j += 1
            k = j
            while k < n and text[k] in "\"'”’)]*_":
                k += 1
            if k >= n or text[k].isspace():
                w = re.search(r"([A-Za-z][A-Za-z.]*|\d+)$", text[start:i])
                prev = w.group(0) if w else ""
                abbr = ch == "." and j == i + 1 and (prev.lower() in ABBR or (len(prev) == 1 and prev.isupper()))
                listnum = ch == "." and prev.isdigit() and text[start:i].strip() == prev
                if not (abbr or listnum):
                    spans.append((start, k))
                    j2 = k
                    while j2 < n and text[j2].isspace() and text[j2] != "\n":
                        j2 += 1
                    start = i = j2
                    continue
            i = j
            continue
        i += 1
    if start < n and text[start:].strip():
        spans.append((start, n))
    return spans


def word_class(word, tag):
    w = word.lower()
    if w in NEG:
        return "negation"
    if tag == "MD" or (tag.startswith("VB") and w in AUX) or w in ("'ll", "ca", "wo"):
        return "auxiliary"
    if tag in ("NN", "NNS"):
        return "noun"
    if tag in ("NNP", "NNPS"):
        return "name"
    if tag.startswith("VB"):
        return "verb"
    if tag.startswith("JJ"):
        return "adjective"
    if tag.startswith("RB") or tag == "WRB":
        return "adverb"
    if tag in ("PRP", "PRP$", "WP", "WP$", "EX"):
        return "pronoun"
    if tag in ("DT", "PDT", "WDT"):
        return "determiner"
    if tag in ("IN", "TO"):
        return "preposition"
    if tag == "CC":
        return "conjunction"
    if tag == "CD":
        return "number"
    return "other word"


def mark_type(tok, ch):
    if "\n" in tok:
        return "line break"
    if not tok.strip():
        return "space"
    if ch in ".!?…":
        return "sentence end"
    if ch in ",，":
        return "comma"
    if ch in ":;":
        return "colon or semicolon"
    if ch in "\"'“”‘’()[]{}«»":
        return "quote or bracket"
    if ch in "-–—":
        return "dash"
    if ch in "*#`_|>~":
        return "markdown mark"
    return "other mark"


def label(tokens, quote_span):
    """Per token: kind, later piece (bool), position, sentence id, and the place relative to the deception sentence."""
    text = "".join(tokens)
    offs, c = [], 0
    for t in tokens:
        offs.append((c, c + len(t)))
        c += len(t)
    norm = text.replace("’", "'").replace("‘", "'")
    sents = sentence_spans(text)
    words = []                                   # (word, start, end, class)
    for s0, s1 in sents:
        ws = [(m.group(0), s0 + m.start(), s0 + m.end()) for m in WORD_RE.finditer(norm[s0:s1])]
        if ws:
            tags = nltk.pos_tag([w for w, _, _ in ws])
            words += [(w, a, b, word_class(w, tg)) for (w, a, b), (_, tg) in zip(ws, tags)]
    wstart = np.array([a for _, a, _, _ in words] or [0])
    sstart = np.array([a for a, _ in sents] or [0])
    n = len(tokens)
    kind, later, sent = [], np.zeros(n, bool), np.full(n, -1)
    for i, (tok, (a, b)) in enumerate(zip(tokens, offs)):
        al = next((a + k for k, ch in enumerate(tok) if ch.isalnum()), None)
        anchor = al if al is not None else next((a + k for k, ch in enumerate(tok) if not ch.isspace()), a)
        if sents:
            si = int(np.searchsorted(sstart, anchor, side="right")) - 1
            if si >= 0 and sents[si][0] <= anchor < sents[si][1]:
                sent[i] = si
        if al is None:
            kind.append(mark_type(tok, text[anchor] if anchor < len(text) else " "))
            continue
        wi = int(np.searchsorted(wstart, al, side="right")) - 1
        if words and wi >= 0 and words[wi][1] <= al < words[wi][2]:
            kind.append(words[wi][3])
            later[i] = words[wi][1] < al and words[wi][1] < a        # the word began in an earlier token
        else:
            kind.append("other word")
    # position in the sentence
    pos = ["elsewhere"] * n
    is_word = [k in WORDS for k in kind]
    for si in range(len(sents)):
        idx = np.where(sent == si)[0]
        if not len(idx):
            continue
        first = int(idx[0])
        para = sents[si][0] == 0 or "\n" in text[max(0, sents[si][0] - 3):sents[si][0]] or first == 0
        pos[first] = "paragraph start" if para else "sentence start"
        wl = [int(j) for j in idx if is_word[j]]
        if wl and wl[-1] != first:
            pos[wl[-1]] = "last word of a sentence"
    # place relative to the deception sentence
    place = np.full(n, 3, np.uint8)               # 0 before, 1 at, 2 after, 3 no quote
    dspan = None
    if quote_span:
        qa, qb = offs[quote_span[0]][0], offs[quote_span[1] - 1][1]
        over = [s for s in sents if s[1] > qa and s[0] < qb]
        s0, s1 = (min(s[0] for s in over), max(s[1] for s in over)) if over else (qa, qb)
        anch = np.array([next((a + k for k, ch in enumerate(t) if not ch.isspace()), a) for t, (a, _) in zip(tokens, offs)])
        place = np.where(anch < s0, 0, np.where(anch < s1, 1, 2)).astype(np.uint8)
        at = np.where(place == 1)[0]
        dspan = (int(at[0]), int(at[-1]) + 1) if len(at) else None
    return dict(kind=kind, later=later, pos=pos, sent=sent, place=place, dspan=dspan)


def boot_ci(x, rng):
    x = np.asarray(x, float)
    if len(x) < 2:
        return (np.nan, np.nan)
    m = x[rng.integers(0, len(x), (N_BOOT, len(x)))].mean(axis=1)
    return tuple(np.percentile(m, [2.5, 97.5]))


def main():
    with open(os.path.join(OUT, "marks.pkl"), "rb") as f:
        mk = pickle.load(f)
    names, lists = mk["names"], mk["lists"]
    J = {n: j for j, n in enumerate(names)}
    ten = [J[n] for n in POOL]
    vocab = C.load_vocab(M)
    cjk = [vocab[i] for n in TEN + ["honest"] for i in lists[n] if any(ord(ch) > 0x2E7F for ch in vocab[i])]
    rec = C.load_transcripts(M)
    rng = np.random.default_rng(SEED)

    labels, kept, excl = {}, defaultdict(list), defaultdict(list)
    matched = Counter()
    for m in mk["marks"]:
        txt = rec[m["tid"]]["response"]
        hits = [w.group(0).lower() for rx in RX.values() for w in rx.finditer(txt)] + [t for t in cjk if t in txt]
        lab = label(m["tokens"], m["quote_span"])
        lab.update(excluded=bool(hits), matched=sorted(set(hits)))
        labels[m["tid"]] = lab
        (excl if hits else kept)[m["cls"]].append(m)
        matched.update(set(hits))
    with open(os.path.join(OUT, "labels.pkl"), "wb") as f:
        pickle.dump(dict(kinds=KINDS, positions=POSITIONS, labels=labels), f, protocol=4)

    carry = {PNAME: lambda m: (m["strength"][:, ten] > 0).any(axis=1), "honest": lambda m: m["strength"][:, J["honest"]] > 0}
    for n in TEN:
        carry[n] = (lambda j: (lambda m: m["strength"][:, j] > 0))(J[n])
    press = [J[n] for n in PRESSURE]
    carry[PRNAME] = lambda m: (m["strength"][:, press] > 0).any(axis=1)
    strong = lambda m: (m["strength"][:, ten] >= 8).any(axis=1)  # noqa: E731
    strong_pr = lambda m: (m["strength"][:, press] >= 8).any(axis=1)  # noqa: E731

    def pct(k, n):
        return f"{k}/{n} ({100 * k / n:.1f}%)" if n else "–"

    L = ["# Where the situation words of the readout sit inside the response (Qwen3.6-27B, J-lens, band 35-58)", "",
         "Written by `scripts/pilot/where_words_sit.py`. Build split plus the unrelated sets, in-sample. A token *carries* a list",
         "when one of the list's tokens is in its top-16 readout at one or more band layers. **The lie-side set** = the ten lie-side",
         "families without `false` and `falsehood` (" + ", ".join(POOL) + "; lists in `analysis/pilot/lists.json`), pooled. `honest` is",
         "counted on its own. **The pressure set** = " + ", ".join(PRESSURE) + ": the families of the lie-side set that are in the",
         "pressured transcripts and much less in the no-pressure truths (the table below). Cells are `carrying / tokens (rate)`.", "",
         "## 0. Responses left out", "",
         "A response is left out when its own text contains a lie-side word or an honest word (whole words, on word stems).", "",
         "| class | transcripts | left out | kept | response tokens kept |", "|---|---|---|---|---|"]
    for labc, c in CLASSES:
        a, b = len(kept[c]), len(excl[c])
        L.append(f"| {labc} | {a + b} | {b} | {a} | {sum(m['n'] for m in kept[c])} |")
    L += ["", "Matched words (number of responses): " + ", ".join(f"{w} {k}" for w, k in matched.most_common()) + ".", ""]

    # 0.1 why false and falsehood are not pooled: they sit on the answer word "No"
    scen = [m for c in ("lie", "truth", "np_truth") for m in kept[c]]
    sets = [("the word No", {"no"}), ("the word Yes", {"yes"}), ("not, n't", {"not", "n't"}), ("never, cannot, none, nor, neither, nothing", {"never", "cannot", "none", "nor", "neither", "nothing"})]
    L += ["## 0.1 Why `false` and `falsehood` are not pooled", "",
          "Kept lies, truths and no-pressure truths together. Cells: tokens carrying the family / tokens of that word (rate).", "",
          "| response token | tokens | " + " | ".join(TEN + ["honest"]) + " |", "|---|---|" + "---|" * 11]
    for labw, ws in sets:
        sel = [(m, i) for m in scen for i, t in enumerate(m["tokens"]) if t.strip().lower() in ws]
        L.append(f"| {labw} | {len(sel)} | " + " | ".join(
            f"{sum(1 for m, i in sel if m['strength'][i, J[n]] > 0)} ({100 * sum(1 for m, i in sel if m['strength'][i, J[n]] > 0) / max(1, len(sel)):.1f}%)" for n in TEN + ["honest"]) + " |")
    tot = sum(m["n"] for m in scen)
    L.append(f"| all tokens | {tot} | " + " | ".join(f"{sum(int((m['strength'][:, J[n]] > 0).sum()) for m in scen)} ({100 * sum(int((m['strength'][:, J[n]] > 0).sum()) for m in scen) / tot:.1f}%)" for n in TEN + ["honest"]) + " |")
    L.append("")

    L += ["Kept transcripts with one or more carrying tokens, and the overall rate:", "",
          "| list | lies | truths | no-pressure truths | unrelated |", "|---|---|---|---|---|"]
    for lname in POOLED + TEN:
        cells = []
        for _, c in CLASSES:
            ms = kept[c]
            tr = sum(1 for m in ms if carry[lname](m).any())
            k, n = sum(int(carry[lname](m).sum()) for m in ms), sum(m["n"] for m in ms)
            cells.append(f"{tr}/{len(ms)} transcripts; {pct(k, n)} of tokens")
        L.append(f"| {lname} | " + " | ".join(cells) + " |")
    L.append("")

    # ---------- 1. by kind of token
    def kind_table(lname, fn, title):
        out = [f"### {title}", "",
               "*rate* = carrying tokens of the kind / tokens of the kind. *times the overall rate* = that rate divided by the class's",
               "overall rate (above 1: the words favour this kind). *per transcript* = among transcripts with one or more carrying",
               "tokens, the kind's share of the carrying tokens minus its share of all tokens, in points, averaged over transcripts,",
               "with a 95% interval from resampling transcripts.", ""]
        for labc, c in CLASSES[:3]:
            ms = kept[c]
            tot_n = sum(m["n"] for m in ms)
            tot_k = sum(int(fn(m).sum()) for m in ms)
            base = tot_k / tot_n if tot_n else 0
            out += [f"**{labc}** ({len(ms)} transcripts, {tot_n} tokens, {tot_k} carrying, overall rate {100 * base:.1f}%)", "",
                    "| kind of token | carrying / tokens (rate) | times the overall rate | share of all tokens | share of carrying tokens | per transcript, points |",
                    "|---|---|---|---|---|---|"]
            kinds_of = {m["tid"]: np.array(labels[m["tid"]]["kind"]) for m in ms}
            for kd in KINDS:
                n = sum(int((kinds_of[m["tid"]] == kd).sum()) for m in ms)
                k = sum(int((fn(m) & (kinds_of[m["tid"]] == kd)).sum()) for m in ms)
                diffs = []
                for m in ms:
                    cm = fn(m)
                    if cm.any():
                        km = kinds_of[m["tid"]] == kd
                        diffs.append(100 * (cm & km).sum() / cm.sum() - 100 * km.sum() / m["n"])
                lo, hi = boot_ci(diffs, rng)
                lift = f"{(k / n) / base:.2f}" if n and base else "–"
                out.append(f"| {kd} | {pct(k, n)} | {lift} | {100 * n / tot_n:.1f}% | {100 * k / tot_k:.1f}% | "
                           f"{np.mean(diffs):+.1f} ({lo:+.1f} to {hi:+.1f}) |" if tot_k and diffs else f"| {kd} | {pct(k, n)} | {lift} | {100 * n / max(1, tot_n):.1f}% | – | – |")
            out.append("")
        return out

    L += ["## 1. By kind of token", ""]
    L += kind_table(PNAME, carry[PNAME], "1.1 The lie-side set")
    L += kind_table(PRNAME, carry[PRNAME], "1.2 The pressure set (conceal, deceive, dishonest, lie, mislead)")
    L += kind_table("honest", carry["honest"], "1.3 `honest`")
    L += kind_table("strong", strong, "1.4 The lie-side set, held by eight or more band layers")
    L += kind_table("strong_pr", strong_pr, "1.5 The pressure set, held by eight or more band layers")

    # per family, rates only
    L += ["### 1.6 Each family: rate by kind of token (carrying / tokens, in percent), lies and truths", ""]
    for labc, c in CLASSES[:2]:
        ms = kept[c]
        kinds_of = {m["tid"]: np.array(labels[m["tid"]]["kind"]) for m in ms}
        L += [f"**{labc}**", "", "| kind of token | tokens | " + " | ".join(TEN + ["honest"]) + " |", "|---|---|" + "---|" * 11]
        for kd in KINDS:
            n = sum(int((kinds_of[m["tid"]] == kd).sum()) for m in ms)
            cells = [f"{100 * sum(int((carry[f](m) & (kinds_of[m['tid']] == kd)).sum()) for m in ms) / n:.1f}" if n else "–" for f in TEN + ["honest"]]
            L.append(f"| {kd} | {n} | " + " | ".join(cells) + " |")
        n = sum(m["n"] for m in ms)
        L.append("| all tokens | " + str(n) + " | " + " | ".join(f"{100 * sum(int(carry[f](m).sum()) for m in ms) / n:.1f}" for f in TEN + ["honest"]) + " |")
        L.append("")

    # pieces and position in the sentence
    wide = " | ".join(f"{labc}: {ln}" for labc, _ in CLASSES[:3] for ln in POOLED)
    L += ["### 1.7 Pieces of split words, and position in the sentence", "", "| | " + wide + " |", "|---|" + "---|" * 9]

    def row(name, sel):
        cells = []
        for _, c in CLASSES[:3]:
            for lname in POOLED:
                n = sum(int(sel(m).sum()) for m in kept[c])
                k = sum(int((carry[lname](m) & sel(m)).sum()) for m in kept[c])
                cells.append(pct(k, n))
        return f"| {name} | " + " | ".join(cells) + " |"

    isw = lambda m: np.array([k in WORDS for k in labels[m["tid"]]["kind"]])  # noqa: E731
    L.append(row("word tokens: first piece or whole word", lambda m: isw(m) & ~labels[m["tid"]]["later"]))
    L.append(row("word tokens: later piece of a split word", lambda m: isw(m) & labels[m["tid"]]["later"]))
    for p in POSITIONS:
        L.append(row(p, (lambda p_: (lambda m: np.array(labels[m["tid"]]["pos"]) == p_))(p)))
    L.append(row("the last response token", lambda m: np.arange(m["n"]) == m["n"] - 1))
    L.append("")

    # ---------- 2. before, at, after the deception sentence
    lies = [m for m in kept["lie"] if labels[m["tid"]]["dspan"]]
    L += ["## 2. Lies: before, at and after the deception sentence", "",
          f"The deception sentence is the judge's quote widened to the full sentences that contain it. {len(lies)} kept lies have one "
          f"({len(kept['lie']) - len(lies)} without a located quote).", ""]
    parts = ["before", "at", "after"]
    have = Counter()
    for m in lies:
        pl = labels[m["tid"]]["place"]
        have[tuple(p for i, p in enumerate(parts) if (pl == i).sum() >= MIN_PART)] += 1
    L += [f"Which parts a lie has (a part needs {MIN_PART} tokens or more): " + "; ".join(f"{' + '.join(k) or 'none'}: {v}" for k, v in have.most_common()) + ".", ""]
    for li_, lname in enumerate(POOLED, 1):
        fn = carry[lname]
        L += [f"### 2.{li_} {TITLE[lname]}", "",
              "Pooled counts:", "", "| place | lies with the part | carrying / tokens (rate) | mean of the per-lie rates |", "|---|---|---|---|"]
        rates = {}
        for i, p in enumerate(parts):
            sub = [m for m in lies if (labels[m["tid"]]["place"] == i).sum() >= MIN_PART]
            n = sum(int((labels[m["tid"]]["place"] == i).sum()) for m in sub)
            k = sum(int((fn(m) & (labels[m["tid"]]["place"] == i)).sum()) for m in sub)
            for m in sub:
                sel = labels[m["tid"]]["place"] == i
                rates[(m["tid"], p)] = (fn(m) & sel).sum() / sel.sum()
            L.append(f"| {p} | {len(sub)} | {pct(k, n)} | {100 * np.mean([rates[(m['tid'], p)] for m in sub]):.1f}% |")
        L += ["", "Within the same lie (only lies that have both parts):", "",
              "| comparison | lies | mean difference of the rates, points (95% interval) | higher / equal / lower |", "|---|---|---|---|"]
        for a, b in (("at", "before"), ("after", "at"), ("after", "before")):
            dif = [100 * (rates[(m["tid"], a)] - rates[(m["tid"], b)]) for m in lies if (m["tid"], a) in rates and (m["tid"], b) in rates]
            lo, hi = boot_ci(dif, rng)
            L.append(f"| {a} minus {b} | {len(dif)} | {np.mean(dif):+.1f} ({lo:+.1f} to {hi:+.1f}) | "
                     f"{sum(1 for x in dif if x > 0)} / {sum(1 for x in dif if x == 0)} / {sum(1 for x in dif if x < 0)} |")
        L += ["", "By distance in tokens from the deception sentence:", "",
              "| distance | lies reaching it | carrying / tokens (rate) |", "|---|---|---|"]
        for lo_, hi_ in [(-30, -25), (-25, -20), (-20, -15), (-15, -10), (-10, -5), (-5, 0)]:
            n = k = reach = 0
            for m in lies:
                s, _ = labels[m["tid"]]["dspan"]
                idx = np.arange(m["n"])
                sel = (idx - s >= lo_) & (idx - s < hi_) & (idx < s)
                if sel.any():
                    reach += 1
                n += int(sel.sum())
                k += int((fn(m) & sel).sum())
            L.append(f"| {lo_} to {hi_ - 1} before its start | {reach} | {pct(k, n)} |")
        n = sum(int((labels[m["tid"]]["place"] == 1).sum()) for m in lies)
        k = sum(int((fn(m) & (labels[m["tid"]]["place"] == 1)).sum()) for m in lies)
        L.append(f"| inside the deception sentence | {len(lies)} | {pct(k, n)} |")
        for lo_, hi_ in [(0, 5), (5, 10), (10, 15), (15, 20), (20, 25), (25, 30), (30, 60), (60, 10 ** 6)]:
            n = k = reach = 0
            for m in lies:
                _, e = labels[m["tid"]]["dspan"]
                idx = np.arange(m["n"])
                sel = (idx - e >= lo_) & (idx - e < hi_)
                if sel.any():
                    reach += 1
                n += int(sel.sum())
                k += int((fn(m) & sel).sum())
            L.append(f"| +{lo_ + 1} to {'+' + str(hi_) if hi_ < 10 ** 6 else 'the end'} after its end | {reach} | {pct(k, n)} |")
        L.append("")

    # ---------- 3. tenths of the response
    L += ["## 3. By tenths of the response (no quote needed; responses of 20 tokens or more)", "",
          "| tenth | " + wide + " |", "|---|" + "---|" * 9]
    for dcl in range(10):
        cells = []
        for _, c in CLASSES[:3]:
            for lname in POOLED:
                n = k = 0
                for m in kept[c]:
                    if m["n"] < 20:
                        continue
                    sel = (np.arange(m["n"]) * 10 // m["n"]) == dcl
                    n += int(sel.sum())
                    k += int((carry[lname](m) & sel).sum())
                cells.append(pct(k, n))
        L.append(f"| {dcl + 1} | " + " | ".join(cells) + " |")
    L.append("")

    # ---------- 4. kind crossed with place (lies)
    L += ["## 4. Lies: kind of token crossed with place", ""]
    for lname in (PNAME, PRNAME):
        L += [f"**{TITLE[lname]}**", "", "| kind of token | before | at | after |", "|---|---|---|---|"]
        for gname, gset in GROUPS:
            cells = []
            for i in range(3):
                n = k = 0
                for m in lies:
                    sel = (labels[m["tid"]]["place"] == i) & np.array([kd in gset for kd in labels[m["tid"]]["kind"]])
                    n += int(sel.sum())
                    k += int((carry[lname](m) & sel).sum())
                cells.append(pct(k, n))
            L.append(f"| {gname} | " + " | ".join(cells) + " |")
        L.append("")
    with open(os.path.join(OUT, "WHERE.md"), "w") as f:
        f.write("\n".join(L) + "\n")

    # ---------- the label check: 200 tokens from the first kept lie and truth of 100+ tokens
    C_ = ["# Label check: 200 response tokens with their labels", "",
          "Written by `scripts/pilot/where_words_sit.py`. The first 100 tokens of one kept lie and one kept truth.", ""]
    for c in ("lie", "truth"):
        m = next(x for x in kept[c] if x["n"] >= 100)
        lab = labels[m["tid"]]
        C_ += [f"## {c}: {m['tid']}", "", "| # | token | kind | piece | position | place |", "|---|---|---|---|---|---|"]
        for i in range(100):
            tok = m["tokens"][i].replace("\n", "⏎").replace(" ", "␣").replace("|", "\\|")
            C_.append(f"| {i + 1} | `{tok}` | {lab['kind'][i]} | {'later piece' if lab['later'][i] else ''} | {lab['pos'][i] if lab['pos'][i] != 'elsewhere' else ''} | "
                      f"{['before', 'at', 'after', ''][lab['place'][i]]} |")
        C_.append("")
    with open(os.path.join(OUT, "LABEL_CHECK.md"), "w") as f:
        f.write("\n".join(C_) + "\n")
    print({c: (len(kept[c]), len(excl[c])) for _, c in CLASSES})
    print(f"written: {OUT}/WHERE.md, labels.pkl, LABEL_CHECK.md")


if __name__ == "__main__":
    main()
