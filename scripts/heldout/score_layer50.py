#!/usr/bin/env python3
"""The three probe positions of the post on one layer, the released probe's layer 50 (user's request, 2026-10-05,
third session: "Everything at 50, the probe's own layer").

Positions (Qwen3.6-27B): the newline after the response (postresp_slot1, prefix part; no question asked); the
last token before the answer to Q9 (think_slot3, where the released probe reads); the newline after the
self-report answer under Q9 (postans_slot1). All at layer 50. A direction is the mean of the build split's
positives minus the mean of its negatives; the threshold is 0, the midpoint between the two means; nothing is
trained. Tasks: "all", lies against truths over every transcript (at the newline after the response also the
share of no-pressure truths flagged); for the two Q9 positions also "deniers", lies against truths among the
transcripts that answer No. Held-out: fitted on the build split, scored on the held-out scenarios, with 95%
intervals (2,000 resamples of scenarios, seed 0; the newline after the response uses the resampling of
score_newline_families.py, the Q9 positions that of analyze_dyl_probe.grouped_bootstrap, as the earlier checks
did). Build split: fitted on four folds and scored on the fifth (the folds of the write-up).

Data: runs/qwen3_6_27b/exp3_layer50/ (cut from inputs/exp3_cut_list_layer50.jsonl, build_cut_list.py --layer50:
the newline after the response on both splits, the newline after the Q9 answer on the build split), exp3_last/
(think_slot3, build) and exp3_heldout_q9/ (think_slot3 and postans_slot1, held-out), all holding layer 50.
Check: think_slot3's held-out AUROCs must equal analysis/heldout/direction_q9.json (same data, same direction).

--check scores think_slot3 only (its data exist before the new cut) and runs the check.
Output: analysis/heldout/LAYER50.md and layer50.json.
Usage: python3 scripts/heldout/score_layer50.py [--check]
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
import pictures as X3  # noqa: E402
import analyze_dyl_probe as A  # noqa: E402
import score_newline_families as H  # noqa: E402
import score_newline_direction as N  # noqa: E402
import score_q9_directions as Q  # noqa: E402
import score_q9_rates as R  # noqa: E402

LAYER = 50
# name, part, position, fit folder, test folder, tasks
POSITIONS = [("the newline after the response", "prefix", "postresp_slot1", "exp3_layer50", "exp3_layer50", ["all"]),
             ("the last token before the answer to Q9 (the released probe's token)", "Q9_dyl", "think_slot3", "exp3_last", "exp3_heldout_q9", ["all", "deniers"]),
             ("the newline after the self-report answer", "Q9_dyl", "postans_slot1", "exp3_layer50", "exp3_heldout_q9", ["all", "deniers"])]
TASK_NAME = {"all": "lies against truths, all transcripts", "deniers": "lies against truths, among the No answers"}


def cut(run, folder):
    path = os.path.join(run, folder)
    if not os.path.exists(os.path.join(path, "meta.json")):
        sys.exit(f"FATAL: {path} is not there. Cut it on the cluster and pull it first (STATUS.md, top block).")
    c = X3.Cut(path)
    if LAYER not in c.layers:
        sys.exit(f"FATAL: {path} holds layers {c.layers}, not {LAYER}")
    return c


def build_fold_numbers(X, y, g):
    """Direction fitted on four folds, scored on the fifth: AUROC and the rates at 0."""
    s = X3.direction_scores(X, y, g)
    return dict(auroc=X3.summary(s, y, g)["auroc"], tp=int((s[y == 1] > 0).sum()), n_pos=int((y == 1).sum()),
                fp=int((s[y == 0] > 0).sum()), n_neg=int((y == 0).sum()))


def newline_after_response(run):
    """Task "all" at the newline after the response, with the no-pressure truths, as score_newline_direction.py."""
    c = cut(run, "exp3_layer50")
    build, held = N.transcripts("build"), N.transcripts("heldout")
    pres = [t for t in build if t["cls"] in ("lie", "truth")]
    Xb = N.vectors(c, pres, "postresp_slot1", LAYER)
    y, g = np.array([int(t["cls"] == "lie") for t in pres]), np.array([t["item"] for t in pres])
    cv = build_fold_numbers(Xb, y, g)
    u, mid = N.fit(Xb, pres)
    rows = N.scored(N.vectors(c, held, "postresp_slot1", LAYER), held, u, mid)
    r = H.with_ci(rows, {"direction": lambda q: q["s"]})["direction"]
    out = dict(auroc=r["auroc"], ci=r["ci"]["auroc"], tp=r["k"]["lie"], n_pos=r["n"]["lie"], fp=r["k"]["truth"], n_neg=r["n"]["truth"],
               np_truth=[r["k"]["np_truth"], r["n"]["np_truth"]], np_truth_ci=r["ci"]["np_truth"], tpr_ci=r["ci"]["lie"], fpr_ci=r["ci"]["truth"],
               pairs=N.pairs(rows), build=cv)
    out["balanced_accuracy"] = (out["tp"] / out["n_pos"] + 1 - out["fp"] / out["n_neg"]) / 2
    pres_rows = [q for q in rows if q["cls"] in ("lie", "truth")]
    out["balanced_accuracy_ci"] = R.rate_rows([int(q["s"] > 0) for q in pres_rows], [int(q["cls"] == "lie") for q in pres_rows],
                                              [q["item"] for q in pres_rows])["balanced_accuracy"]["ci"]
    return out


def q9_position(run, name, fit_folder, test_folder, task):
    """A Q9 position and task, as score_q9_directions.py and score_q9_rates.py."""
    cf, ct = cut(run, fit_folder), cut(run, test_folder)
    build, held = Q.transcripts("build"), Q.transcripts("heldout")
    (Xf, yf, gf), (Xt, yt, gt) = Q.task_set(cf, build, name, LAYER, task), Q.task_set(ct, held, name, LAYER, task)
    cv = build_fold_numbers(Xf, yf, gf)
    a, b = Xf[yf == 1].mean(0), Xf[yf == 0].mean(0)
    s = (Xt - (a + b) / 2) @ ((a - b) / np.linalg.norm(a - b))
    rows = [(float(v), int(yy), g) for v, yy, g in zip(s, yt, gt)]
    rr = R.rate_rows((s > 0).astype(int), yt, gt)
    return dict(auroc=A.auroc_np(s[yt == 1], s[yt == 0]), ci=A.grouped_bootstrap(rows), tp=rr["tp"], n_pos=rr["n_pos"], fp=rr["fp"], n_neg=rr["n_neg"],
                tpr_ci=rr["tpr"]["ci"], fpr_ci=rr["fpr"]["ci"], balanced_accuracy=rr["balanced_accuracy"]["value"],
                balanced_accuracy_ci=rr["balanced_accuracy"]["ci"], build=cv)


def row(title, task, r):
    b = r["build"]
    return (f"| {title} | {TASK_NAME[task]} | {b['auroc']:.2f}; {b['tp']}/{b['n_pos']} ({b['tp'] / b['n_pos']:.0%}); {b['fp']}/{b['n_neg']} ({b['fp'] / b['n_neg']:.0%})"
            f" | {r['auroc']:.2f} ({r['ci'][0]:.2f} to {r['ci'][1]:.2f}) | {r['balanced_accuracy']:.2f} ({r['balanced_accuracy_ci'][0]:.2f} to {r['balanced_accuracy_ci'][1]:.2f})"
            f" | {r['tp']}/{r['n_pos']} ({r['tp'] / r['n_pos']:.0%}; {r['tpr_ci'][0]:.0%} to {r['tpr_ci'][1]:.0%})"
            f" | {r['fp']}/{r['n_neg']} ({r['fp'] / r['n_neg']:.0%}; {r['fpr_ci'][0]:.0%} to {r['fpr_ci'][1]:.0%}) |")


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--check", action="store_true", help="think_slot3 only (its data exist before the new cut), with the check against direction_q9.json")
    args = ap.parse_args()
    run = os.path.join(C.RUNS, C.slug(Q.M))
    res = {}
    for title, part, name, fit_folder, test_folder, tasks in POSITIONS:
        if args.check and name != "think_slot3":
            continue
        for task in tasks:
            res[(name, task)] = newline_after_response(run) if part == "prefix" else q9_position(run, name, fit_folder, test_folder, task)
    with open(os.path.join(C.ROOT, "analysis", "heldout", "direction_q9.json")) as f:
        known = json.load(f)["test"]
    for task in ("all", "deniers"):
        got, want = res[("think_slot3", task)]["auroc"], known[f"think_slot3/{task}"]["auroc"]
        if abs(got - want) > 1e-9:
            sys.exit(f"FATAL: think_slot3 {task}: held-out AUROC {got:.6f} here, {want:.6f} in direction_q9.json")
    print("check: think_slot3's held-out AUROCs equal direction_q9.json (all, deniers)")

    L = [f"# The three probe positions at layer {LAYER}, the released probe's layer", "",
         "Qwen3.6-27B. A direction is the mean of the build split's positives minus the mean of its negatives at one token;",
         "threshold 0, the midpoint between the two means; nothing is trained. Build split: fitted on four folds, scored on",
         "the fifth. Held-out: fitted on the build split, scored on the held-out scenarios; 95% intervals, 2,000 resamples of",
         "scenarios. Balanced accuracy = the mean of the true-positive rate and the true-negative rate.", "",
         "| position | task | build split: AUROC; lies flagged; truths flagged | held-out AUROC | held-out balanced accuracy | held-out lies flagged | held-out truths flagged |",
         "|---|---|---|---|---|---|---|"]
    for title, _, name, _, _, tasks in POSITIONS:
        for task in tasks:
            if (name, task) in res:
                L.append(row(title, task, res[(name, task)]))
    if ("postresp_slot1", "all") in res:
        r = res[("postresp_slot1", "all")]
        L += ["", f"At the newline after the response, no-pressure truths flagged on the held-out set: {r['np_truth'][0]}/{r['np_truth'][1]} "
                  f"({r['np_truth'][0] / r['np_truth'][1]:.0%}; {r['np_truth_ci'][0]:.0%} to {r['np_truth_ci'][1]:.0%}); held-out scenarios with a lie and a truth "
                  f"where the lie scores above its truth: {r['pairs'][0]} of {r['pairs'][1]}. At layer 47 (DIRECTION.md): AUROC 0.96, 93/101, 7/54, 6/90, 46 of 47."]
    out_dir = os.path.join(C.ROOT, "analysis", "heldout")
    suffix = "_check" if args.check else ""
    with open(os.path.join(out_dir, f"LAYER50{suffix}.md"), "w") as f:
        f.write("\n".join(L) + "\n")
    with open(os.path.join(out_dir, f"layer50{suffix}.json"), "w") as f:
        json.dump({f"{n}/{t}": v for (n, t), v in res.items()}, f, indent=1)
    print("\n".join(L[6:]))
    print(f"\nwritten: {os.path.join(out_dir, f'LAYER50{suffix}.md')}")


if __name__ == "__main__":
    main()
