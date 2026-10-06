#!/usr/bin/env python3
"""A second held-out check (user's request, 2026-10-05): the lie-minus-truth direction of the residual stream at
Qwen's newline after the response, fitted on the build split and scored on the held-out scenarios.

FROZEN BEFORE THE HELD-OUT RESIDUAL STREAMS ARE CUT (nothing below may be changed after the run):
  model           Qwen3.6-27B
  position        post-response slot 1 (the newline right after the turn-end token of the response)
  layer           47 (the layer of every picture and number of Experiment 3 in the write-up)
  vectors         the residual stream as cut by src/cut_positions.py (block output, float16), no scaling
  direction       the mean of the build split's lies minus the mean of its truths (152 and 81 transcripts told
                  under pressure). Nothing is trained: no probe, no SVM, no regularisation.
  score           (x - midpoint of the two means) . unit direction; above 0 is the lie side
  test            held-out lies against held-out truths: AUROC. At the fixed threshold 0: the share of held-out
                  lies, truths and no-pressure truths above it. Among held-out scenarios with a lie and a
                  truth: how often the lie scores above its truth.
  transcripts     the selection with commentary dropped (load_manifest), scenario and no-pressure sets
  intervals       as in the first held-out check (score_newline_families.py): 95%, 2,000 resamples of
                  scenarios with replacement (seed 0), within the groups "has a lie only", "has a truth only",
                  "has both"; no-pressure truths resampled by scenario
  not the test    the same direction procedure at two control positions (the newline before the response, the
                  turn-end token) and at the other four cut layers. They are printed below the result and
                  marked as secondary.

The held-out split was read once before, on 2026-10-04, for the word families at this token (HELDOUT.md).
That look did not touch the residual stream, and the layer, the position and the direction were all set on
the build split on 2026-10-03.

Step 1 recomputes the build-split number of the write-up (the direction fitted on four folds and scored on the
fifth, analysis/exp3/numbers.json) and stops if it differs. Step 2 reads the held-out vectors once.

--rehearse DIR runs every step without reading the held-out split: the build split's scenarios are divided in
two halves (seed 0), the direction is fitted on one half and scored on the other, and the files go to DIR.

Data: data/cluster/runs/qwen3_6_27b/exp3/ (build split, pulled on 2026-10-03) and exp3_heldout/ (cut on the
cluster from inputs/exp3_cut_list_heldout.jsonl; see STATUS.md for the commands).
Output: analysis/heldout/DIRECTION.md and direction.json.
Usage: python3 scripts/heldout/score_newline_direction.py [--rehearse DIR]
"""
import argparse
import json
import os
import sys

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, ".."))
sys.path.insert(0, os.path.join(HERE, "..", "exp3"))
sys.path.insert(0, HERE)
import common as C  # noqa: E402
import presence as P  # noqa: E402
import pictures as X3  # noqa: E402
import score_newline_families as H  # noqa: E402

M, POS, LAYER = "qwen3.6-27b", "postresp_slot1", 47
CONTROLS = {"preresp_slot4": "the newline before the response (the prompt alone)", "postresp_slot0": "the turn-end token after the response"}
NAMES = {"lie": "lies", "truth": "truths", "np_truth": "no-pressure truths"}


def transcripts(split):
    """The selected transcripts of one split: lies and truths told under pressure, and no-pressure truths."""
    out = []
    for e in C.load_manifest(M)["transcripts"]:
        if e["set"] not in ("scenario", "nopressure") or e["split"] != split:
            continue
        cls = P._class(e)
        if cls != "np_lie":
            out.append(dict(tid=e["tid"], cls=cls, item=e["item_id"]))
    return out


def vectors(cut, T, name, layer):
    X, have = cut.vectors(T, "prefix", name, layer)
    if not have.all():
        sys.exit(f"FATAL: {int((~have).sum())} of {len(T)} transcripts have no vector at {name}")
    return X


def fit(X, T):
    """(unit direction, midpoint) from the lies and truths of T."""
    cls = np.array([t["cls"] for t in T])
    a, b = X[cls == "lie"].mean(0), X[cls == "truth"].mean(0)
    return (a - b) / np.linalg.norm(a - b), (a + b) / 2


def scored(X, T, u, mid):
    return [dict(cls=t["cls"], item=t["item"], s=float(v)) for t, v in zip(T, (X - mid) @ u)]


def pairs(rows):
    lie = {r["item"]: r["s"] for r in rows if r["cls"] == "lie"}
    truth = {r["item"]: r["s"] for r in rows if r["cls"] == "truth"}
    both = sorted(set(lie) & set(truth))
    return [sum(lie[g] > truth[g] for g in both), len(both)]


def test(cut_fit, T_fit, cut_test, T_test, name, layer):
    u, mid = fit(vectors(cut_fit, T_fit, name, layer), T_fit)
    rows = scored(vectors(cut_test, T_test, name, layer), T_test, u, mid)
    r = H.with_ci(rows, {"direction": lambda q: q["s"]})["direction"]
    r["pairs"] = pairs(rows)
    return r


def pct(r, k):
    return f"{r['k'][k]}/{r['n'][k]} ({r[k]:.0%}; {r['ci'][k][0]:.0%} to {r['ci'][k][1]:.0%})"


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--rehearse", metavar="DIR", help="no held-out read: fit on half of the build scenarios, score the other half, write to DIR")
    args = ap.parse_args()
    run = os.path.join(C.RUNS, C.slug(M))
    cut_build = X3.Cut(os.path.join(run, "exp3"))
    build = transcripts("build")

    # step 1: the build-split number of the write-up, recomputed
    pres = [t for t in build if t["cls"] in ("lie", "truth")]
    Xb = vectors(cut_build, pres, POS, LAYER)
    y = np.array([int(t["cls"] == "lie") for t in pres])
    g = np.array([t["item"] for t in pres])
    cv = X3.summary(X3.direction_scores(Xb, y, g), y, g)
    with open(os.path.join(C.ROOT, "analysis", "exp3", "numbers.json")) as f:
        known = json.load(f)["before"][POS][str(LAYER)]["D"]["auroc"]
    if abs(cv["auroc"] - known) > 1e-9:
        sys.exit(f"FATAL: the build-split number is {cv['auroc']:.6f} here and {known:.6f} in analysis/exp3/numbers.json")
    print(f"step 1: build split, direction fitted on four folds and scored on the fifth: AUROC {cv['auroc']:.3f} "
          f"({cv['n'][0]} lies, {cv['n'][1]} truths), equal to the write-up")

    # step 2: the test
    if args.rehearse:
        items = sorted({t["item"] for t in build})
        half = set(np.random.default_rng(0).permutation(items)[: len(items) // 2].tolist())
        T_fit = [t for t in build if t["item"] in half and t["cls"] in ("lie", "truth")]
        T_test = [t for t in build if t["item"] not in half]
        cut_test, out_dir, what = cut_build, args.rehearse, "REHEARSAL on the build split (half of the scenarios fit, the other half scored)"
    else:
        hdir = os.path.join(run, "exp3_heldout")
        if not os.path.exists(os.path.join(hdir, "meta.json")):
            sys.exit(f"FATAL: {hdir} is not there. Cut it on the cluster and pull it first (STATUS.md).")
        cut_test = X3.Cut(hdir)
        if cut_test.layers != cut_build.layers:
            sys.exit(f"FATAL: the held-out cut has layers {cut_test.layers}, the build cut {cut_build.layers}")
        T_fit, T_test = pres, transcripts("heldout")
        out_dir, what = os.path.join(C.ROOT, "analysis", "heldout"), "held-out scenarios"
    os.makedirs(out_dir, exist_ok=True)
    n_fit = {c: sum(t["cls"] == c for t in T_fit) for c in ("lie", "truth")}
    main_r = test(cut_build, T_fit, cut_test, T_test, POS, LAYER)
    second = {"controls": {name: test(cut_build, T_fit, cut_test, T_test, name, LAYER) for name in CONTROLS},
              "layers": {str(l): test(cut_build, T_fit, cut_test, T_test, POS, l) for l in cut_build.layers if l != LAYER}}

    a = lambda r: f"{r['auroc']:.2f} ({r['ci']['auroc'][0]:.2f} to {r['ci']['auroc'][1]:.2f})"
    L = [f"# The lie-minus-truth direction at the newline after the response, scored on the {what}", "",
         f"Qwen3.6-27B, the residual stream at the newline after the response, layer {LAYER}. The direction is the mean of the",
         f"lies minus the mean of the truths of the fit set ({n_fit['lie']} lies, {n_fit['truth']} truths); nothing is trained. A transcript's",
         "score is its position along that direction, measured from the midpoint of the two means; above 0 is the lie side.",
         "Intervals: 95%, 2,000 resamples of scenarios. Everything was fixed before the run (the top of",
         "`scripts/heldout/score_newline_direction.py`).", "",
         "## The test", "",
         "| quantity | value (95% interval) |", "|---|---|",
         f"| AUROC, lies against truths | {a(main_r)} |",
         f"| lies above the threshold 0 | {pct(main_r, 'lie')} |",
         f"| truths above it | {pct(main_r, 'truth')} |",
         f"| no-pressure truths above it | {pct(main_r, 'np_truth')} |",
         f"| scenarios with a lie and a truth: the lie scores above its truth | {main_r['pairs'][0]} of {main_r['pairs'][1]} |", "",
         f"For comparison, on the build split with the direction fitted on four folds and scored on the fifth: AUROC {cv['auroc']:.2f}",
         f"({cv['n'][0]} lies, {cv['n'][1]} truths); the lie is above its truth in {cv['pairs'][0]} of {cv['pairs'][2]} pairs.", "",
         "## Not the test: the same procedure at the control positions and the other layers", "",
         "| position | layer | AUROC, lies against truths (95% interval) | lies above 0 | truths above 0 |", "|---|---|---|---|---|"]
    for name, label in CONTROLS.items():
        r = second["controls"][name]
        L.append(f"| {label} | {LAYER} | {a(r)} | {pct(r, 'lie')} | {pct(r, 'truth')} |")
    for l, r in second["layers"].items():
        L.append(f"| the newline after the response | {l} | {a(r)} | {pct(r, 'lie')} | {pct(r, 'truth')} |")
    with open(os.path.join(out_dir, "DIRECTION.md"), "w") as f:
        f.write("\n".join(L) + "\n")
    with open(os.path.join(out_dir, "direction.json"), "w") as f:
        json.dump(dict(what=what, model=M, position=POS, layer=LAYER, n_fit=n_fit, build_cross_validated=cv, test=main_r, secondary=second), f, indent=1)
    print("\n".join(L[8:]))
    print(f"\nwritten: {os.path.join(out_dir, 'DIRECTION.md')}")


if __name__ == "__main__":
    main()
