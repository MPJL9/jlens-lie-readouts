#!/usr/bin/env python3
"""Sheets for the survey of readouts that are not about deception (user, 2026-10-02; it replaces
Step A of PLAN.md Section 5A.3).

Qwen3.6-27B, J-lens, band 35-58. Positions agreed with the user: post-response slots 0, 2, 3, and
under Q9_dyl the four think slots and the five post-answer slots. Post-response slot 1 is added to
the counting (not to the reading) as the reference position with useful readouts.

Outputs, under analysis/junk/:
  sample.json        the 50 sampled transcripts (seed 0: 20 lies, 15 truths, 5 no-pressure truths,
                     10 unrelated chats; build split and unrelated set only), split into halves A and B
  sheet_A.md, sheet_B.md
                     what a subagent reads: for each sampled transcript and position, the readout
                     tokens of the early, middle and late third of the band, most frequent first
                     (labels not shown)
  top_tokens.json    for each position, every token with its share of the readout entries (16 per
                     band layer) over all build-split scenario transcripts and unrelated chats, and
                     whether it is in a draft family at that position
  top_tokens.md      the unique tokens that the later assignment step sorts into kinds: at each
                     position the most frequent tokens up to COVER of the entries (at most TOP_N)

Usage: python3 scripts/junk_sheets.py
"""
from __future__ import annotations

import json
import os
import random
import sys
from collections import Counter, defaultdict

import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import common as C  # noqa: E402
import presence as P  # noqa: E402
from frequency_tables import part_positions, prefix_positions  # noqa: E402
from presence_index import read_ids  # noqa: E402

QWEN = "qwen3.6-27b"
OUT = os.path.join(C.ROOT, "analysis", "junk")
WORDING = "Q9_dyl"
READ_POSITIONS = [("prefix", "postresp_slot0"), ("prefix", "postresp_slot2"), ("prefix", "postresp_slot3"),
                  (WORDING, "think_slot0"), (WORDING, "think_slot1"), (WORDING, "think_slot2"), (WORDING, "think_slot3"),
                  (WORDING, "postans_slot0"), (WORDING, "postans_slot1"), (WORDING, "postans_slot2"),
                  (WORDING, "postans_slot3"), (WORDING, "postans_slot4")]
REFERENCE = ("prefix", "postresp_slot1")
TOKEN_AT = {"postresp_slot0": "<|im_end|>", "postresp_slot1": "\\n", "postresp_slot2": "<|im_start|>", "postresp_slot3": "user",
            "think_slot0": "<think>", "think_slot1": "\\n\\n", "think_slot2": "</think>", "think_slot3": "\\n\\n",
            "postans_slot0": "<|im_end|>", "postans_slot1": "\\n", "postans_slot2": "<|im_start|>", "postans_slot3": "user",
            "postans_slot4": "\\n"}
SAMPLE = {"lie": 20, "truth": 15, "np_truth": 5, "unrelated": 10}
THIRDS = [(35, 42), (43, 50), (51, 58)]
PER_THIRD = 12
K = 16
COVER, TOP_N = 0.85, 120


def show(s):
    s = s.replace("\n", "\\n").replace("\t", "\\t").replace("|", "\\|").replace("`", "'")
    if s.startswith(" "):
        s = "␣" + s[1:]
    return s if s.strip() else f"[{s or 'empty'}]"


def sample(d):
    rng = random.Random(0)
    picked = []
    for cls, n in SAMPLE.items():
        idx = [i for i, c in enumerate(d["cls"]) if c == cls and d["transcripts"][i]["set"] != "unrelated_extra"]
        idx = [i for i in idx if d["transcripts"][i]["wordings"].get(WORDING, {}).get("answer_finished", True)]
        picked += [(i, cls) for i in rng.sample(idx, n)]
    halves = {"A": picked[0::2], "B": picked[1::2]}
    return halves


def sheet(d, man, vocab, half, items):
    by_tid = {e["tid"]: e for e in man["transcripts"]}
    layers = man["layers"]
    L = [f"# Readout sheet {half}: {len(items)} transcripts, {len(READ_POSITIONS)} positions each", "",
         "Qwen3.6-27B, J-lens. For each position: the tokens in the readout (the 16 most likely tokens per layer) in",
         "three groups of band layers, most frequent first, each with the number of layers of that group (out of 8)",
         f"in which it appears. At most {PER_THIRD} tokens per group. `␣` is a leading space; `\\n` is a newline.", ""]
    for n, (ti, _) in enumerate(items, 1):
        t = d["transcripts"][ti]
        e = by_tid[t["tid"]]
        L.append(f"## Transcript {half}{n:02d}")
        L.append("")
        cache = {}
        for part, pos in READ_POSITIONS:
            if part not in cache:
                header, ids = read_ids(QWEN, e, part)
                cache[part] = (prefix_positions(header) if part == "prefix" else part_positions(header), ids["J"])
            pmap, arr = cache[part]
            if pos not in pmap:
                continue
            L.append(f"**{pos}** (the token here is `{TOKEN_AT[pos]}`)")
            for lo, hi in THIRDS:
                li = [i for i, layer in enumerate(layers) if lo <= layer <= hi]
                cnt = Counter()
                for i in li:
                    cnt.update(set(int(x) for x in arr[i, pmap[pos]]))
                top = cnt.most_common(PER_THIRD)
                L.append(f"- layers {lo}-{hi}: " + "  ".join(f"`{show(vocab[tok])}`×{c}" for tok, c in top))
            L.append("")
    with open(os.path.join(OUT, f"sheet_{half}.md"), "w") as f:
        f.write("\n".join(L) + "\n")


def token_shares(d, part, pos, sel):
    """{token id: share of the readout entries of the selected transcripts}."""
    hv = P.have_mask(d, part, pos) & sel
    n = int(hv.sum()) * len(d["band_layers"]) * K
    out = {}
    for t, (idx, cnt) in d["present"][part][pos].items():
        s = int(cnt[hv[idx.astype(int)]].sum())
        if s:
            out[t] = s / n
    return out


def main():
    os.makedirs(OUT, exist_ok=True)
    d = P.load(QWEN, "J")
    man = C.load_manifest(QWEN)
    vocab = C.load_vocab(QWEN)
    halves = sample(d)
    with open(os.path.join(OUT, "sample.json"), "w") as f:
        json.dump({h: [dict(tid=d["transcripts"][i]["tid"], cls=c) for i, c in items] for h, items in halves.items()}, f, indent=1)
    for half, items in halves.items():
        sheet(d, man, vocab, half, items)

    with open(os.path.join(C.ROOT, "analysis", "families", "families_draft.json")) as f:
        entries = [e for e in json.load(f)["entries"] if e["model"] == QWEN and e["lens"] == "J"]
    fam = defaultdict(set)
    for e in entries:
        fam[(e["part"], e["position"])] |= {m["id"] for m in e["members"]} | {m["id"] for m in e.get("removed", [])}
    cls = d["cls"]
    groups = {"scenario": np.isin(cls, ["lie", "truth"]), "unrelated": cls == "unrelated"}
    top, unique = {}, {}
    for part, pos in READ_POSITIONS + [REFERENCE]:
        sh = {g: token_shares(d, part, pos, sel) for g, sel in groups.items()}
        pooled = token_shares(d, part, pos, groups["scenario"] | groups["unrelated"])
        rows = [dict(id=t, token=vocab[t], share=s, scenario=sh["scenario"].get(t, 0.0), unrelated=sh["unrelated"].get(t, 0.0),
                     family=t in fam[(part, pos)]) for t, s in sorted(pooled.items(), key=lambda x: -x[1])]
        top[pos] = rows
        cum = 0.0
        for r in rows[:TOP_N]:
            unique.setdefault(r["id"], dict(id=r["id"], token=r["token"], positions=[]))["positions"].append(pos)
            cum += r["share"]
            if cum >= COVER:
                break
    with open(os.path.join(OUT, "top_tokens.json"), "w") as f:
        json.dump(top, f, ensure_ascii=False)
    L = ["# Tokens to sort into kinds", "",
         f"At each position, the most frequent readout tokens up to {100 * COVER:.0f}% of the readout entries (at most {TOP_N}).",
         "One line per unique token: its id, the token, and the positions where it is among those.", ""]
    for u in sorted(unique.values(), key=lambda u: (-len(u["positions"]), u["id"])):
        L.append(f"{u['id']}\t`{show(u['token'])}`\t{', '.join(u['positions'])}")
    with open(os.path.join(OUT, "top_tokens.md"), "w") as f:
        f.write("\n".join(L) + "\n")
    print(f"written: {OUT}; unique tokens to sort: {len(unique)}")
    for part, pos in READ_POSITIONS + [REFERENCE]:
        rows = top[pos]
        cum = np.cumsum([r["share"] for r in rows])
        n85 = int(np.searchsorted(cum, COVER)) + 1
        print(f"  {pos:15} distinct tokens {len(rows):5}  tokens to reach {100 * COVER:.0f}%: {n85:4}  covered by the top {TOP_N}: {100 * cum[min(TOP_N, len(cum)) - 1]:.0f}%"
              f"  family words: {100 * sum(r['share'] for r in rows if r['family']):.0f}%")


if __name__ == "__main__":
    main()
