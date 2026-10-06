#!/usr/bin/env python3
"""Rates at the midpoint for the two directions under Q9, on the held-out scenarios (user's request, 2026-10-05,
third session: "compute the numbers").

The directions are those of score_q9_directions.py (imported for its functions; that script is kept as it ran):
the mean of the build split's positives minus the mean of its negatives, task "deniers" (lies against truths among
the transcripts whose answer to Q9 is No), at position A (think_slot3, the last token before the answer, layer 50,
the released probe's token) and position B (postans_slot1, the newline after the self-report answer, layer 47).
That run declared the AUROC. This script scores the same held-out vectors on the same fixed directions and adds,
at the fixed threshold 0 (the midpoint between the two means, as in 4.4): the true-positive rate, the
false-positive rate and the balanced accuracy, with 95% intervals (2,000 resamples of scenarios, seed 0, within
the groups of analyze_dyl_probe.grouped_bootstrap). Nothing is fitted or chosen on the held-out split.

Step 1 recomputes each direction's held-out AUROC and stops if it differs from analysis/heldout/direction_q9.json.
For comparison, the released probe at its shipped threshold on the same held-out transcripts (from dyl_probe.jsonl).

Output: analysis/heldout/DIRECTION_Q9_RATES.md and direction_q9_rates.json.
Usage: python3 scripts/heldout/score_q9_rates.py
"""
import json
import os
import sys

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, ".."))
sys.path.insert(0, os.path.join(HERE, "..", "exp3"))
sys.path.insert(0, HERE)
import common as C  # noqa: E402
import pictures as X3  # noqa: E402
import score_q9_directions as Q  # noqa: E402

TASK = "deniers"


def rate_rows(flags, ys, groups, n_boot=2000, seed=0):
    """Balanced accuracy, true-positive rate and false-positive rate with 95% intervals, scenarios resampled."""
    by_sc = {}
    for f, y, g in zip(flags, ys, groups):
        by_sc.setdefault(g, []).append((int(f), int(y)))
    strata = {"lie": [], "truth": [], "both": []}
    for g, rs in by_sc.items():
        kinds = {y for _, y in rs}
        strata["both" if len(kinds) == 2 else ("lie" if 1 in kinds else "truth")].append(g)

    def stats(fs, ys_):
        fs, ys_ = np.asarray(fs), np.asarray(ys_)
        tpr, fpr = fs[ys_ == 1].mean(), fs[ys_ == 0].mean()
        return (tpr + 1 - fpr) / 2, tpr, fpr

    rng = np.random.default_rng(seed)
    draws = []
    for _ in range(n_boot):
        fs, ys_ = [], []
        for scs in strata.values():
            for g in (rng.choice(scs, size=len(scs), replace=True) if scs else []):
                for f, y in by_sc[g]:
                    fs.append(f)
                    ys_.append(y)
        if 1 in ys_ and 0 in ys_:
            draws.append(stats(fs, ys_))
    draws = np.array(draws)
    point = stats(flags, ys)
    out = {}
    for i, k in enumerate(("balanced_accuracy", "tpr", "fpr")):
        out[k] = dict(value=float(point[i]), ci=[float(np.percentile(draws[:, i], 2.5)), float(np.percentile(draws[:, i], 97.5))])
    out["tp"], out["n_pos"] = int(sum(f for f, y in zip(flags, ys) if y == 1)), int(sum(ys))
    out["fp"], out["n_neg"] = int(sum(f for f, y in zip(flags, ys) if y == 0)), int(len(ys) - sum(ys))
    return out


def fmt(r):
    b, t, f = r["balanced_accuracy"], r["tpr"], r["fpr"]
    return (f"{b['value']:.2f} ({b['ci'][0]:.2f} to {b['ci'][1]:.2f}) | {r['tp']}/{r['n_pos']} ({t['value']:.0%}; {t['ci'][0]:.0%} to {t['ci'][1]:.0%})"
            f" | {r['fp']}/{r['n_neg']} ({f['value']:.0%}; {f['ci'][0]:.0%} to {f['ci'][1]:.0%})")


def main():
    run = os.path.join(C.RUNS, C.slug(Q.M))
    hdir = os.path.join(run, "exp3_heldout_q9")
    held = X3.Cut(hdir)
    build, test = Q.transcripts("build"), Q.transcripts("heldout")
    with open(os.path.join(C.ROOT, "analysis", "heldout", "direction_q9.json")) as f:
        known = json.load(f)
    res = {}
    for name, layer, folder, title in Q.POSITIONS:
        fit = Q.task_set(X3.Cut(os.path.join(run, folder)), build, name, layer, TASK)
        tst = Q.task_set(held, test, name, layer, TASK)
        (Xf, yf, _), (Xt, yt, gt) = fit, tst
        a, b = Xf[yf == 1].mean(0), Xf[yf == 0].mean(0)
        s = (Xt - (a + b) / 2) @ ((a - b) / np.linalg.norm(a - b))
        auroc = Q.A.auroc_np(s[yt == 1], s[yt == 0])
        want = known["test"][f"{name}/{TASK}"]
        if abs(auroc - want["auroc"]) > 1e-9 or [int((yt == 1).sum()), int((yt == 0).sum())] != want["n"]:
            sys.exit(f"FATAL: {name}: AUROC {auroc:.6f} here, {want['auroc']:.6f} in direction_q9.json")
        print(f"step 1: {name} layer {layer}: held-out AUROC {auroc:.3f}, equal to direction_q9.json")
        r = rate_rows((s > 0).astype(int), yt, gt)
        r.update(auroc=auroc, ci=want["ci"], title=title, layer=layer)
        res[name] = r

    # the released probe at its shipped threshold on the same held-out transcripts
    tids = {t["tid"] for t in test}
    info = {e["tid"]: e for e in C.load_manifest(Q.M)["transcripts"]}
    flags, ys, gs, scores = [], [], [], []
    for r in C.read_jsonl(os.path.join(run, "dyl_probe.jsonl")):
        if r["wording"] != Q.W or r["tid"] not in tids or not r["first_token_yes_no"]:
            continue
        e = info[r["tid"]]
        y = Q.label(dict(cls=Q.P._class(e), ans=e["wordings"][Q.W]["answer_label"]), TASK)
        if y is not None:
            flags.append(int(r["flagged"])), ys.append(y), gs.append(e["item_id"]), scores.append(r["score"])
    probe = rate_rows(flags, ys, gs)
    probe["auroc"] = Q.A.auroc_np([s for s, y in zip(scores, ys) if y == 1], [s for s, y in zip(scores, ys) if y == 0])
    probe["ci"] = known["probe"][TASK]["ci"]

    L = ["# Directions under Q9 on the held-out scenarios: rates at the midpoint", "",
         "Qwen3.6-27B, wording Q9, lies against truths among the transcripts whose answer is No. The directions are those of",
         "`scripts/heldout/score_q9_directions.py` (fitted on the build split; that run declared the AUROC, reproduced here",
         "in step 1). Threshold: 0, the midpoint between the two means, fixed by the fit. Intervals: 95%, 2,000 resamples of",
         "scenarios. The released probe is at its shipped threshold on the same transcripts. Nothing is fitted or chosen here.", "",
         "| detector | token (layer) | balanced accuracy | true-positive rate | false-positive rate | AUROC |", "|---|---|---|---|---|---|"]
    a = lambda r: f"{r['auroc']:.2f} ({r['ci'][0]:.2f} to {r['ci'][1]:.2f})"
    L.append(f"| the released probe, at its shipped threshold | the last token before the answer (50) | {fmt(probe)} | {a(probe)} |")
    for name, _, _, _ in Q.POSITIONS:
        r = res[name]
        L.append(f"| our direction | {r['title'].split('. ', 1)[1]} | {fmt(r)} | {a(r)} |")
    out_dir = os.path.join(C.ROOT, "analysis", "heldout")
    with open(os.path.join(out_dir, "DIRECTION_Q9_RATES.md"), "w") as f:
        f.write("\n".join(L) + "\n")
    with open(os.path.join(out_dir, "direction_q9_rates.json"), "w") as f:
        json.dump(dict(model=Q.M, wording=Q.W, task=TASK, directions=res, probe=probe), f, indent=1)
    print("\n".join(L[7:]))
    print(f"\nwritten: {os.path.join(out_dir, 'DIRECTION_Q9_RATES.md')}")


if __name__ == "__main__":
    main()
