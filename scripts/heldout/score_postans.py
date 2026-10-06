#!/usr/bin/env python3
"""Does the newline after the self-report answer matter, or does any token near the answer do? (User's question,
2026-10-05, third session.)

Qwen3.6-27B, wording Q9. Seven tokens: the last token before the answer (think_slot3, where the released probe
reads), the answer token itself (ans_tok0: Yes / No), and the five tokens of the turn boundary appended after the
answer (postans_slot0 `<|im_end|>`, slot1 `\\n`, slot2 `<|im_start|>`, slot3 `user`, slot4 `\\n`). Layers 47 and
50. At each token and layer, a direction (the mean of the build split's positives minus the mean of its negatives;
threshold 0, the midpoint; nothing trained) for two tasks: "all", lies against truths over every transcript, and
"deniers", lies against truths among the transcripts that answer No. Build split: fitted on four folds, scored on
the fifth. Held-out: fitted on the build split, scored on the held-out scenarios, 95% intervals (2,000 resamples of
scenarios, seed 0, as in the earlier checks). Transcripts: scenario set, answers that finished and open with yes or
no (score_q9_directions.transcripts).

Checks: think_slot3 at layer 50 must reproduce analysis/heldout/direction_q9.json, and postans_slot1 at layer 50
must reproduce analysis/heldout/layer50.json (same tokens, cut again from the same cache).

Data: runs/qwen3_6_27b/exp3_postans/ (cut from inputs/exp3_cut_list_postans.jsonl, build_cut_list.py --postans).
Output: analysis/heldout/POSTANS.md and postans.json.
Usage: python3 scripts/heldout/score_postans.py
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
import analyze_dyl_probe as A  # noqa: E402
import score_q9_directions as Q  # noqa: E402
import score_q9_rates as R  # noqa: E402

LAYERS = [50, 47]
TOKENS = [("think_slot3", "the last token before the answer (the released probe's token)"),
          ("ans_tok0", "the answer token (Yes / No)"),
          ("postans_slot0", "`<|im_end|>` after the answer"),
          ("postans_slot1", "the newline after it"),
          ("postans_slot2", "`<|im_start|>`"),
          ("postans_slot3", "`user`"),
          ("postans_slot4", "the newline after `user`")]
TASKS = {"all": "all transcripts", "deniers": "among the No answers"}


def one(cut, build, held, name, layer, task):
    (Xf, yf, gf), (Xt, yt, gt) = Q.task_set(cut, build, name, layer, task), Q.task_set(cut, held, name, layer, task)
    s_cv = X3.direction_scores(Xf, yf, gf)
    cv = dict(auroc=X3.summary(s_cv, yf, gf)["auroc"], tp=int((s_cv[yf == 1] > 0).sum()), n_pos=int(yf.sum()),
              fp=int((s_cv[yf == 0] > 0).sum()), n_neg=int((1 - yf).sum()))
    a, b = Xf[yf == 1].mean(0), Xf[yf == 0].mean(0)
    s = (Xt - (a + b) / 2) @ ((a - b) / np.linalg.norm(a - b))
    rows = [(float(v), int(yy), g) for v, yy, g in zip(s, yt, gt)]
    rr = R.rate_rows((s > 0).astype(int), yt, gt)
    return dict(auroc=A.auroc_np(s[yt == 1], s[yt == 0]), ci=A.grouped_bootstrap(rows), tp=rr["tp"], n_pos=rr["n_pos"], fp=rr["fp"], n_neg=rr["n_neg"],
                balanced_accuracy=rr["balanced_accuracy"]["value"], ba_ci=rr["balanced_accuracy"]["ci"], build=cv)


def main():
    run = os.path.join(C.RUNS, C.slug(Q.M))
    path = os.path.join(run, "exp3_postans")
    if not os.path.exists(os.path.join(path, "meta.json")):
        sys.exit(f"FATAL: {path} is not there. Cut it on the cluster and pull it first (STATUS.md, top block).")
    cut = X3.Cut(path)
    for layer in LAYERS:
        if layer not in cut.layers:
            sys.exit(f"FATAL: {path} holds layers {cut.layers}, not {layer}")
    build, held = Q.transcripts("build"), Q.transcripts("heldout")
    res = {}
    for layer in LAYERS:
        for name, _ in TOKENS:
            for task in TASKS:
                res[(layer, name, task)] = one(cut, build, held, name, layer, task)

    # checks against the earlier runs
    with open(os.path.join(C.ROOT, "analysis", "heldout", "direction_q9.json")) as f:
        q9 = json.load(f)["test"]
    with open(os.path.join(C.ROOT, "analysis", "heldout", "layer50.json")) as f:
        l50 = json.load(f)
    for name, src in (("think_slot3", {t: q9[f"think_slot3/{t}"]["auroc"] for t in TASKS}), ("postans_slot1", {t: l50[f"postans_slot1/{t}"]["auroc"] for t in TASKS})):
        for task in TASKS:
            got, want = res[(50, name, task)]["auroc"], src[task]
            if abs(got - want) > 1e-9:
                sys.exit(f"FATAL: {name} layer 50 {task}: held-out AUROC {got:.6f} here, {want:.6f} in the earlier run")
    print("checks: think_slot3 and postans_slot1 at layer 50 reproduce direction_q9.json and layer50.json")

    L = ["# Tokens around the self-report answer: does the newline matter?", "",
         "Qwen3.6-27B, wording Q9. A direction is the mean of the build split's positives minus the mean of its negatives at one",
         "token and layer; threshold 0, the midpoint; nothing is trained. Build split: fitted on four folds, scored on the fifth.",
         "Held-out: fitted on the build split, scored on the held-out scenarios; 95% intervals, 2,000 resamples of scenarios.",
         "Tasks: lies against truths over all transcripts (held-out 101 / 54), and among the No answers (46 / 52).", ""]
    for layer in LAYERS:
        L += [f"## Layer {layer}", "",
              "| token | task | build split: AUROC; lies flagged; truths flagged | held-out AUROC | held-out balanced accuracy | held-out lies flagged | held-out truths flagged |",
              "|---|---|---|---|---|---|---|"]
        for name, title in TOKENS:
            for task, tname in TASKS.items():
                r, b = res[(layer, name, task)], res[(layer, name, task)]["build"]
                L.append(f"| {title} | {tname} | {b['auroc']:.2f}; {b['tp']}/{b['n_pos']} ({b['tp'] / b['n_pos']:.0%}); {b['fp']}/{b['n_neg']} ({b['fp'] / b['n_neg']:.0%})"
                         f" | {r['auroc']:.2f} ({r['ci'][0]:.2f} to {r['ci'][1]:.2f}) | {r['balanced_accuracy']:.2f} ({r['ba_ci'][0]:.2f} to {r['ba_ci'][1]:.2f})"
                         f" | {r['tp']}/{r['n_pos']} ({r['tp'] / r['n_pos']:.0%}) | {r['fp']}/{r['n_neg']} ({r['fp'] / r['n_neg']:.0%}) |")
        L.append("")
    out_dir = os.path.join(C.ROOT, "analysis", "heldout")
    with open(os.path.join(out_dir, "POSTANS.md"), "w") as f:
        f.write("\n".join(L))
    with open(os.path.join(out_dir, "postans.json"), "w") as f:
        json.dump({f"{l}/{n}/{t}": v for (l, n, t), v in res.items()}, f, indent=1)
    print("\n".join(L[6:]))
    print(f"written: {os.path.join(out_dir, 'POSTANS.md')}")


if __name__ == "__main__":
    main()
