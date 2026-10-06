#!/usr/bin/env python3
"""Experiment 3: two checks behind the write-up (family_findings.md Section 14), at one layer, for one model.

1. The pre-response control. A scenario's lie and truth share the prompt, so their vectors at the
   newline before the response should be the same. Counts the identical pairs and measures how far
   the others differ.
2. The newline after the response: the J-lens family count against the residual direction. The
   count = how many of the model's lie families the readout holds (Qwen: the eight); the direction = mean of lies minus mean
   of truths, each transcript scored by a direction fitted without its scenario (0 = midpoint).

Writes CHECKS.md next to the model's numbers (analysis/exp3/ for Qwen).
Usage: python3 scripts/exp3/checks.py [--model gemma-3-12b-it] [--layer N]
"""
import argparse
import os
import sys

import numpy as np

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import common as C  # noqa: E402
from exp3 import pictures as X3  # noqa: E402


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--model", default=X3.QWEN, choices=list(X3.MODELS))
    ap.add_argument("--layer", type=int, help="default: the layer the pictures are drawn at")
    args = ap.parse_args()
    cfg = X3.configure(args.model)
    args.layer = args.layer or cfg["draw"]
    from scipy.stats import spearmanr
    from sklearn.metrics import roc_auc_score
    D, T = X3.Cut(os.path.join(C.RUNS, C.slug(X3.MODEL), "exp3")), X3.load_transcripts()
    cls, grp, cnt = X3.col(T, "cls"), X3.col(T, "group"), X3.col(T, "count")
    pres = (cls == "lie") | (cls == "truth")
    y, g, c = (cls[pres] == "lie").astype(int), grp[pres], cnt[pres]
    lie, truth = y == 1, y == 0
    L = [f"# Experiment 3: checks ({cfg['name']}, layer {args.layer}, build split, in-sample)", "",
         "Written by `scripts/exp3/checks.py`.", ""]

    X, _ = D.vectors(T, "prefix", "preresp_slot4", args.layer)
    both = sorted(set(grp[cls == "lie"]) & set(grp[cls == "truth"]))
    rel = []
    for s in both:
        i, j = np.where((grp == s) & (cls == "lie"))[0][0], np.where((grp == s) & (cls == "truth"))[0][0]
        rel.append(np.linalg.norm(X[i] - X[j]) / np.linalg.norm(X[i]))
    rel = np.array(rel)
    far = [np.linalg.norm(X[i] - X[j]) / np.linalg.norm(X[i])
           for i, j in zip(np.where(cls == "lie")[0][:60], np.where(cls == "truth")[0][:60])]
    L += ["## 1. The pre-response control: a scenario's lie and truth", "",
          f"- Pairs (scenarios with both a lie and a truth): {len(both)}. Identical vectors: {int((rel == 0).sum())}."]
    if (rel > 0).any():
        L += [f"- The other {int((rel > 0).sum())} pairs differ by {100 * np.median(rel[rel > 0]):.1f}% of the vector's length (median; "
              f"largest {100 * rel.max():.1f}%). A lie and a truth from different scenarios differ by {100 * np.median(far):.0f}% (median of 60).",
              "- So the pairs that are not exact ties differ by rounding in the forward pass, and their order in the pair counts is noise.", ""]
    else:
        L += [f"- Every pair is identical. A lie and a truth from different scenarios differ by {100 * np.median(far):.0f}% (median of 60).", ""]

    X, _ = D.vectors(T, "prefix", "postresp_slot1", args.layer)
    if X3.SCALE:
        X = X3.unit_spread(X, X[cls == "unrelated"])
    s = X3.direction_scores(X[pres], y, g)
    a, b = X[cls == "lie"].mean(0), X[cls == "truth"].mean(0)
    full = (X - (a + b) / 2) @ ((a - b) / np.linalg.norm(a - b))       # for the classes outside the fit
    n = lambda m: int(m.sum())  # noqa: E731
    L += ["## 2. The newline after the response: family count against the residual direction", ""]
    if X3.SCALE:
        L += ["Each dimension is divided by its spread in the unrelated chats first, as in the pictures.", ""]
    L += [
          "| score | AUROC, lies against truths |", "|---|---|",
          f"| number of {cfg['fam']} in the readout | {roc_auc_score(y, c):.2f} |",
          f"| residual direction (lie minus truth, fitted without the scenario) | {roc_auc_score(y, s):.2f} |", "",
          "| | lies | truths |", "|---|---|---|",
          f"| one or more of {cfg['fam_short']} | {n(lie & (c >= 1))} / {n(lie)} | {n(truth & (c >= 1))} / {n(truth)} |",
          f"| on the lie side of the direction | {n(lie & (s > 0))} / {n(lie)} | {n(truth & (s > 0))} / {n(truth)} |",
          f"| both | {n(lie & (c >= 1) & (s > 0))} / {n(lie)} | {n(truth & (c >= 1) & (s > 0))} / {n(truth)} |",
          f"| either | {n(lie & ((c >= 1) | (s > 0)))} / {n(lie)} | {n(truth & ((c >= 1) | (s > 0)))} / {n(truth)} |", "",
          f"- Lies with none of {cfg['fam_short']} (the misses): {n(lie & (c == 0) & (s > 0))} of {n(lie & (c == 0))} are on the lie side of the direction.",
          f"- Truths with one or more of {cfg['fam_short']}: {n(truth & (c >= 1) & (s > 0))} of {n(truth & (c >= 1))} are on the lie side. "
          f"Truths with none: {n(truth & (c == 0) & (s > 0))} of {n(truth & (c == 0))}.",
          f"- Spearman correlation between the count and the direction score: {spearmanr(c, s)[0]:.2f} among all pressured transcripts, "
          f"{spearmanr(c[lie], s[lie])[0]:.2f} among lies, {spearmanr(c[truth], s[truth])[0]:.2f} among truths.",
          f"- With the direction fitted on all pressured transcripts, on the lie side: {n(full[cls == 'np_truth'] > 0)} of {n(cls == 'np_truth')} "
          f"no-pressure truths, {n(full[cls == 'unrelated'] > 0)} of {n(cls == 'unrelated')} unrelated chats.", ""]
    mu, comp, share = X3.pca(X[pres])
    pc1 = roc_auc_score(y, (X[pres] - mu) @ comp[0])
    L += ["Where each group sits on the direction (score; 0 = midpoint between the two means):", "",
          "| group | transcripts | median | quartiles |", "|---|---|---|---|"]
    for lab, m in ((f"lies with two or more of {cfg['fam_short']}", lie & (c >= 2)), ("lies with one", lie & (c == 1)),
                   ("lies with none (the misses)", lie & (c == 0)), ("truths with one or more", truth & (c >= 1)),
                   ("truths with none", truth & (c == 0))):
        L.append(f"| {lab} | {n(m)} | {np.median(s[m]):.1f} | {np.percentile(s[m], 25):.1f} to {np.percentile(s[m], 75):.1f} |")
    L += ["", f"- The first principal component of the pressured transcripts alone, with nothing fitted on labels: AUROC {max(pc1, 1 - pc1):.2f} "
              f"({100 * share[0]:.0f}% of the variance).", ""]
    path = os.path.join(X3.out_dir(X3.MODEL), "CHECKS.md")
    with open(path, "w") as f:
        f.write("\n".join(L))
    print("\n".join(L))


if __name__ == "__main__":
    main()
