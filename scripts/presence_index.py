#!/usr/bin/env python3
"""Presence index: for each model and lens, which transcripts have which readout token present
in the layer band at each template position. Every labelled count in the family work is read
from this index (scripts/family_checks.py, scripts/apply_family_decisions.py), so the readout
files are scanned once.

Present = the token is in the top-16 readout at one or more layers of the band (BANDS for the
J-lens, BANDS_LL for the logit lens), as in scripts/frequency_tables.py.

Transcripts: the build split only (scenario and no-pressure sets) plus the unrelated set;
commentary transcripts dropped. The held-out split is never read here: it is kept for the one
scoring of the frozen families (PLAN.md Section 5.5).

Positions: post-response slots from the prefix part; the question tokens, pre-answer slots, think
slots (Qwen only has them) and post-answer slots of every wording (post-answer slots only when the
answer finished). Until 2026-10-02 the wording parts were indexed for Qwen only.

Output: analysis/presence/<slug>_<lens>.pkl, a dict
  model, lens, band, band_layers
  transcripts   list of dict(tid, set, split, label, item_id, stance, wordings)
  have          {part: {position: sorted list of transcript indices that have the position}}
  present       {part: {position: {token id: (transcript indices uint16, number of band layers uint8)}}}

Usage: python3 scripts/presence_index.py [--models ...] [--lenses J LL]
"""
from __future__ import annotations

import argparse
import json
import os
import pickle
import sys
import time
from collections import defaultdict

import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import common as C  # noqa: E402
from frequency_tables import part_positions, prefix_positions  # noqa: E402

OUT = os.path.join(C.ROOT, "analysis", "presence")
QWEN = "qwen3.6-27b"


def read_ids(model, entry, part):
    """(header, {lens: uint32 [layers, T, K]}) without reading the probability arrays."""
    base = os.path.join(C.EXPORTS, C.slug(model), entry["set"], entry["tid"], part)
    with open(base + ".json") as f:
        header = json.load(f)
    out = {}
    for a in header["arrays"]:
        if a["name"] in ("J_ids", "LL_ids"):
            out[a["name"][:-4]] = np.memmap(base + ".bin", dtype=a["dtype"], mode="r", offset=a["offset"], shape=tuple(a["shape"]))
    return header, out


def keep(e):
    if e["set"].startswith("unrelated"):          # the first unrelated set and the extra one
        return True
    return e["split"] == "build"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--models", nargs="+", default=C.MODELS)
    ap.add_argument("--lenses", nargs="+", default=C.LENSES)
    args = ap.parse_args()
    os.makedirs(OUT, exist_ok=True)
    for model in args.models:
        man = C.load_manifest(model)
        entries = [e for e in man["transcripts"] if keep(e)]
        assert not any(e["split"] == "heldout" for e in entries)
        layers = man["layers"]
        parts = ["prefix"] + C.WORDINGS          # every model has the five wording parts (all models since 2026-10-02)
        bands = {lens: (C.BANDS if lens == "J" else C.BANDS_LL)[model] for lens in args.lenses}
        lidx = {lens: [i for i, l in enumerate(layers) if b[0] <= l <= b[1]] for lens, b in bands.items()}
        acc = {lens: defaultdict(lambda: defaultdict(lambda: defaultdict(lambda: ([], [])))) for lens in args.lenses}
        have = defaultdict(lambda: defaultdict(list))
        t0 = time.time()
        for ti, e in enumerate(entries):
            for part in parts:
                if not os.path.exists(os.path.join(C.EXPORTS, C.slug(model), e["set"], e["tid"], part + ".json")):
                    continue          # the released data hold the wording parts for Qwen only (2026-10-06)
                header, ids = read_ids(model, e, part)
                pos_map = prefix_positions(header) if part == "prefix" else part_positions(header)
                finished = header.get("answer_finished", True)
                for name, p in pos_map.items():
                    if name.startswith(("ans_tok", "preresp_slot", "resp_tok")):
                        continue
                    if name.startswith("postans_slot") and not finished:
                        continue
                    have[part][name].append(ti)
                    for lens in args.lenses:
                        block = np.asarray(ids[lens][lidx[lens], p])          # [band layers, K]
                        toks, counts = np.unique(block, return_counts=True)    # a token is in a layer's top-K once
                        tab = acc[lens][part][name]
                        for t, c in zip(toks.tolist(), counts.tolist()):
                            a, b = tab[t]
                            a.append(ti)
                            b.append(c)
            if (ti + 1) % 100 == 0 or ti + 1 == len(entries):
                print(f"  {model}: {ti + 1}/{len(entries)} transcripts ({time.time() - t0:.0f} s)", flush=True)
        trs = [dict(tid=e["tid"], set=e["set"], split=e["split"], label=e["label"], item_id=e["item_id"],
                    stance=e.get("stance"), wordings=e.get("wordings", {})) for e in entries]
        for lens in args.lenses:
            present = {part: {name: {t: (np.asarray(a, np.uint16), np.asarray(b, np.uint8)) for t, (a, b) in tab.items()}
                              for name, tab in pos.items()} for part, pos in acc[lens].items()}
            out = dict(model=model, lens=lens, band=list(bands[lens]), band_layers=[layers[i] for i in lidx[lens]],
                       transcripts=trs, have={p: dict(v) for p, v in have.items()}, present=present)
            path = os.path.join(OUT, f"{C.slug(model)}_{lens}.pkl")
            with open(path, "wb") as f:
                pickle.dump(out, f, protocol=4)
            print(f"written: {path} ({os.path.getsize(path) / 1e6:.0f} MB)", flush=True)


if __name__ == "__main__":
    main()
