"""Reading the presence index (analysis/presence/, written by scripts/presence_index.py).

A *token set* is a set of vocabulary ids. It is present in a transcript at a position if one or
more of its tokens is in the top-16 readout at one or more layers of the band. Everything here
counts transcripts; the index holds the build split and the unrelated set only (never the
held-out split).
"""
from __future__ import annotations

import os
import pickle
import sys

import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import common as C  # noqa: E402

DIR = os.path.join(C.ROOT, "analysis", "presence")
_cache = {}

# transcript classes: scenario lies, scenario truths, no-pressure truths, unrelated
CLASSES = ["lie", "truth", "np_truth", "unrelated"]


def load(model, lens):
    key = (model, lens)
    if key not in _cache:
        with open(os.path.join(DIR, f"{C.slug(model)}_{lens}.pkl"), "rb") as f:
            d = pickle.load(f)
        trs = d["transcripts"]
        cls = np.array([_class(t) for t in trs])
        d["cls"] = cls
        d["scenario"] = np.array([t["item_id"] for t in trs])
        _cache[key] = d
    return _cache[key]


def _class(t):
    if t["set"] == "scenario":
        return t["label"]                       # lie / truth
    if t["set"] == "nopressure":
        return "np_truth" if t["label"] == "truth" else "np_lie"
    return "unrelated"


def position_key(name):
    order = {"postresp": 0, "q": 1, "preans": 2, "think": 3, "postans": 4}
    return (order.get(name.split("_")[0], 9), int("".join(ch for ch in name if ch.isdigit()) or 0))


def positions(d, part):
    return sorted(d["present"].get(part, {}), key=position_key)


def present_mask(d, part, position, ids):
    """Boolean array over the index's transcripts: the token set is present at the position."""
    m = np.zeros(len(d["transcripts"]), bool)
    tab = d["present"].get(part, {}).get(position, {})
    for t in ids:
        hit = tab.get(t)
        if hit is not None:
            m[hit[0]] = True
    return m


def have_mask(d, part, position):
    """Boolean array: the transcript has this position (and its answer finished, for post-answer slots)."""
    m = np.zeros(len(d["transcripts"]), bool)
    m[np.asarray(d["have"].get(part, {}).get(position, []), int)] = True
    return m


def answer(d, wording):
    """Array of the self-report answer label (admit / deny / other / '') under one wording."""
    return np.array([t["wordings"].get(wording, {}).get("answer_label", "") for t in d["transcripts"]])


def counts(d, part, position, ids):
    """{class: (present, transcripts with the position)} for the four classes."""
    pm, hm = present_mask(d, part, position, ids), have_mask(d, part, position)
    return {c: (int((pm & hm & (d["cls"] == c)).sum()), int((hm & (d["cls"] == c)).sum())) for c in CLASSES}


def tok(s):
    s = s.replace("\n", "\\n").replace("|", "\\|")
    return "␣" + s[1:] if s.startswith(" ") else s


def frac(a, b):
    return f"{a}/{b}"


def pct(a, b):
    return "–" if not b else f"{100 * a / b:.0f}%"
