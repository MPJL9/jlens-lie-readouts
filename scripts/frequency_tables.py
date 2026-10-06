#!/usr/bin/env python3
"""PLAN.md Section 5.2: frequency tables of readout tokens at the template positions. No labels.

For each model, lens (J-lens with BANDS, logit lens with BANDS_LL), wording (where the position
depends on it) and position, every token that is in the top-16 readout at one or more layers of
the band, with
  n        the number of transcripts in which it is present (lies and truths pooled)
  layers   the number of transcripts in which it is present at each layer of the band
Population: the scenario transcripts of the build split (commentary transcripts dropped). Positions
(Section 5.1): post-response slots (all models; one value per transcript, from the prefix part);
for Qwen also the question tokens, pre-answer slots, think slots and post-answer slots, per
wording (post-answer slots only from transcripts whose answer finished).

Outputs, under analysis/freq/:
  <slug>_<lens>.json              {wording_or_"prefix": {position: {token_id: {s, n, layers: {layer: n}}}}}
  <slug>_<lens>_<wording>.md      one markdown table per position (the file a subagent reads)
  index.md                        sizes

Usage: python3 scripts/frequency_tables.py [--models ...] [--lenses J LL]
"""
from __future__ import annotations

import argparse
import json
import os
import sys
import time
from collections import defaultdict

import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import common as C  # noqa: E402

OUT = os.path.join(C.ROOT, "analysis", "freq")
QWEN = "qwen3.6-27b"


def part_positions(header):
    """Position names inside one wording part (positions relative to the part), from its segments."""
    item = {"tokens": header["tokens"], "segments": header["segments"]}
    return C.positions(item)


def prefix_positions(header):
    item = {"tokens": header["tokens"], "segments": header["segments"]}
    return {k: v for k, v in C.positions(item).items() if k.startswith("postresp_slot")}


def present_sets(arr_ids, layer_idx, pos):
    """{token id: [layer indices where present]} at one position over the band's layer indices."""
    out = defaultdict(list)
    for li in layer_idx:
        for t in np.unique(arr_ids[li, pos]):
            out[int(t)].append(li)
    return out


def tally(model, lens, band, entries):
    """{part: {position: {tid_token: {"n": int, "layers": {layer: int}}}}} over entries."""
    layers = C.load_manifest(model, drop_commentary=False)["layers"]
    layer_idx = [i for i, l in enumerate(layers) if band[0] <= l <= band[1]]
    counts = defaultdict(lambda: defaultdict(lambda: defaultdict(lambda: {"n": 0, "layers": defaultdict(int)})))
    n_tr = defaultdict(lambda: defaultdict(int))
    parts = ["prefix"] + (C.WORDINGS if model == QWEN else [])
    t0 = time.time()
    for k, e in enumerate(entries, 1):
        for part in parts:
            header, arrays = C.read_part(model, e, part)
            ids = arrays[lens + "_ids"]
            pos_map = prefix_positions(header) if part == "prefix" else part_positions(header)
            finished = header.get("answer_finished", True)
            for name, p in pos_map.items():
                if name.startswith(("ans_tok", "preresp_slot")):
                    continue
                if name.startswith("postans_slot") and not finished:
                    continue
                n_tr[part][name] += 1
                for t, lis in present_sets(ids, layer_idx, p).items():
                    c = counts[part][name][t]
                    c["n"] += 1
                    for li in lis:
                        c["layers"][layers[li]] += 1
        if k % 50 == 0 or k == len(entries):
            print(f"  {model} {lens}: {k}/{len(entries)} transcripts ({time.time() - t0:.0f} s)", flush=True)
    return counts, n_tr, [layers[i] for i in layer_idx]


def disp(s):
    s = s.replace("\n", "\\n").replace("\t", "\\t").replace("|", "\\|")
    if s.startswith(" "):
        s = "␣" + s[1:]
    return s


def write(model, lens, band, counts, n_tr, band_layers, vocab):
    s = C.slug(model)
    js = {}
    sizes = []
    for part, positions in counts.items():
        js[part] = {}
        lines = [f"# {model}, {'J-lens' if lens == 'J' else 'logit lens'}, band {band[0]}-{band[1]}, "
                 f"{'post-response slots (shared by all wordings)' if part == 'prefix' else 'wording ' + part}", "",
                 "Frequency tables (PLAN.md Section 5.2), scenario transcripts of the build split, lies and truths",
                 "pooled; no labels. One table per position. `n` = transcripts in which the token is in the",
                 f"top-16 readout at one or more band layers; the layer columns (L{band_layers[0]} … L{band_layers[-1]}) give",
                 "the number of transcripts per layer. Tokens are shown with `␣` for a leading space and `\\n` for",
                 "a newline; the `id` is the vocabulary index. Rows are sorted by n, then by id.", ""]
        order = sorted(positions, key=lambda nm: (nm.split("_")[0], int("".join(ch for ch in nm if ch.isdigit()) or 0)))
        for name in order:
            toks = positions[name]
            js[part][name] = {str(t): {"s": vocab[t], "n": c["n"], "layers": {str(l): v for l, v in sorted(c["layers"].items())}}
                              for t, c in toks.items()}
            rows = sorted(toks.items(), key=lambda kv: (-kv[1]["n"], kv[0]))
            lines += [f"## {name} ({n_tr[part][name]} transcripts, {len(rows)} distinct tokens)", "",
                      "| token | id | n | " + " ".join(f"L{l}" for l in band_layers) + " |", "|---|---|---|---|"]
            for t, c in rows:
                per = " ".join(str(c["layers"].get(l, 0)) for l in band_layers)
                lines.append(f"| `{disp(vocab[t])}` | {t} | {c['n']} | {per} |")
            lines.append("")
            sizes.append((part, name, n_tr[part][name], len(rows)))
        path = os.path.join(OUT, f"{s}_{lens}_{part}.md")
        with open(path, "w") as f:
            f.write("\n".join(lines))
    with open(os.path.join(OUT, f"{s}_{lens}.json"), "w") as f:
        json.dump({"model": model, "lens": lens, "band": list(band), "band_layers": band_layers,
                   "n_transcripts": {p: dict(v) for p, v in n_tr.items()}, "tables": js}, f)
    return sizes


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--models", nargs="+", default=C.MODELS)
    ap.add_argument("--lenses", nargs="+", default=C.LENSES)
    args = ap.parse_args()
    os.makedirs(OUT, exist_ok=True)
    index = ["# Frequency tables (PLAN.md Section 5.2)", "", "Written by `scripts/frequency_tables.py`. Build-split scenario",
             "transcripts, commentary dropped, lies and truths pooled.", "",
             "| model | lens | band | part | position | transcripts | distinct tokens |", "|---|---|---|---|---|---|---|"]
    for m in args.models:
        man = C.load_manifest(m)
        entries = C.entries(man, set="scenario", split="build")
        vocab = C.load_vocab(m)
        for lens in args.lenses:
            band = (C.BANDS if lens == "J" else C.BANDS_LL)[m]
            counts, n_tr, band_layers = tally(m, lens, band, entries)
            for part, name, n, k in write(m, lens, band, counts, n_tr, band_layers, vocab):
                index.append(f"| {m} | {lens} | {band[0]}-{band[1]} | {part} | {name} | {n} | {k} |")
    with open(os.path.join(OUT, "index.md"), "w") as f:
        f.write("\n".join(index) + "\n")


if __name__ == "__main__":
    main()
