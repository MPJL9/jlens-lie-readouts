"""True-positive and false-positive rates of our two directions under Q9 at the midpoint, on the BUILD SPLIT ONLY
(user's question, 2026-10-05: "why no true-positive rate and false-positive rate?").

The held-out test of these directions (scripts/heldout/score_q9_directions.py, frozen) was fixed as the AUROC
alone, and its output holds no per-transcript scores; this script does not read the held-out split. It repeats the
build-split procedure of that test (the direction fitted on four folds and scored on the fifth, the same folds)
and adds the rates at the fixed threshold 0, the midpoint between the two means, as in 4.4.

Cell: lie against truth among the transcripts whose answer to Q9 is No ("deniers"). Positions: A, the last token
before the answer (layer 50, the released probe's token); B, the newline after the self-report answer (layer 47).
Balanced accuracy = the mean of the true-positive rate and the true-negative rate.

Run from the project root:
python3 scripts/findings_2026_10_04/q9_direction_rates.py > analysis/findings_2026_10_04/q9_direction_rates.md"""
import os
import sys

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, ".."))
sys.path.insert(0, os.path.join(HERE, "..", "exp3"))
sys.path.insert(0, os.path.join(HERE, "..", "heldout"))
import common as C  # noqa: E402
import pictures as X3  # noqa: E402
import score_q9_directions as Q  # noqa: E402  (its functions only; main() is not called, nothing held-out is read)


def main():
    run = os.path.join(C.RUNS, C.slug(Q.M))
    build = Q.transcripts("build")
    print("# Our two directions under Q9: rates at the midpoint, build split only\n")
    print("Qwen3.6-27B, Q9, lie against truth among the transcripts that answer No. The direction is fitted on four folds")
    print("and scored on the fifth (the folds of the write-up); the threshold is 0, the midpoint between the two means.")
    print("Nothing held-out is read. For comparison, the released probe at its shipped threshold on the same transcripts.\n")
    print("| detector | token (layer) | balanced accuracy | true-positive rate | false-positive rate | AUROC |")
    print("|---|---|---|---|---|---|")
    for name, layer, folder, title in Q.POSITIONS:
        X, y, g = Q.task_set(X3.Cut(os.path.join(run, folder)), build, name, layer, "deniers")
        s = X3.direction_scores(X, y, g)
        auroc = X3.summary(s, y, g)["auroc"]
        tp, n_pos = int((s[y == 1] > 0).sum()), int((y == 1).sum())
        fp, n_neg = int((s[y == 0] > 0).sum()), int((y == 0).sum())
        tpr, fpr = tp / n_pos, fp / n_neg
        print(f"| our direction | {title.split('. ', 1)[1]} | {(tpr + 1 - fpr) / 2:.2f} | {tp}/{n_pos} ({tpr:.0%}) | {fp}/{n_neg} ({fpr:.0%}) | {auroc:.2f} |")
    # the released probe on the same cell, build split, at its shipped threshold
    tids = {t["tid"] for t in build}
    info = {e["tid"]: e for e in C.load_manifest(Q.M)["transcripts"]}
    rows = [r for r in C.read_jsonl(os.path.join(run, "dyl_probe.jsonl"))
            if r["wording"] == Q.W and r["tid"] in tids and r["first_token_yes_no"] and r["answer_label"] == "deny"]
    lab = lambda r: info[r["tid"]]
    L = [r for r in rows if Q.P._class(lab(r)) == "lie"]
    T = [r for r in rows if Q.P._class(lab(r)) == "truth"]
    tp, fp = sum(r["flagged"] for r in L), sum(r["flagged"] for r in T)
    tpr, fpr = tp / len(L), fp / len(T)
    auroc = Q.A.auroc_np([r["score"] for r in L], [r["score"] for r in T])
    print(f"| the released probe, at its shipped threshold | the last token before the answer (50) | {(tpr + 1 - fpr) / 2:.2f} | {tp}/{len(L)} ({tpr:.0%}) | {fp}/{len(T)} ({fpr:.0%}) | {auroc:.2f} |")


if __name__ == "__main__":
    main()
