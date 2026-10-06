#!/usr/bin/env python3
"""Experiment 3, one fit per wording (user, 2026-10-04): the residual stream at a template position
after the self-report question, drawn twice per wording: coloured lie against truth, and coloured
by the self-report answer (denies against admits).

One PCA per wording and position, fitted on that wording's pressured transcripts (lies and truths
told under pressure, build split) and on nothing else; no other class is drawn. Qwen, unscaled, as
in pictures.py. The held-out split is never read.

Numbers (cross-validated in five folds with scenarios kept together, as in pictures.py):
  line  AUROC of a straight-line split in the two drawn dimensions
  dir   AUROC of the direction between the two group means in the full space
for lie against truth (all; among deniers; among admitters) and for admits against denies (all;
among lies; among truths). Transcripts with another answer are drawn in grey and left out of the
admit / deny numbers. A number is left out when a group has fewer than 10 transcripts.

The last token before the self-report answer (think_slot3, where the DYL probe reads) is cut into
its own folder: build_cut_list.py --last, then --data exp3_last here.

Output: analysis/exp3/fig/<position>_by_wording.png (drawn at --draw-layer; another layer than the
model's default adds _L<layer> to the name) and analysis/exp3/by_wording.json (every cut layer).

Usage: python3 scripts/exp3/by_wording.py [--positions preans_slot4 think_slot2] [--draw-layer 47]
       python3 scripts/exp3/by_wording.py --data exp3_last --positions think_slot3 [--draw-layer 50]
"""
import argparse
import json
import os
import sys

import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import common as C  # noqa: E402
import pictures as X3  # noqa: E402

# deny / admit: a pair of the chart rules' palette that is not used for a class elsewhere (validated:
# colour-blind separation 41, normal vision 46; yellow is below 3:1 on the surface, so counts are printed)
ANS_COL = {"deny": "#4a3aa7", "admit": "#eda100", "other": "#c3c2b7"}
ANS_NAME = {"deny": "denies", "admit": "admits", "other": "other answer"}
CLS_COL = {1: X3.COL["lie"], 0: X3.COL["truth"]}
SPLITS = ("lie_all", "lie_deniers", "lie_admitters", "admit_all", "admit_lies", "admit_truths")
EXTRA = {"think_slot3": "the blank line after `</think>`, the last token before the answer"}   # positions outside pictures.py


def auroc(score, Z, y, g, m):
    Z, y, g = Z[m], y[m], g[m]
    return X3.summary(score(Z, y, g), y, g)["auroc"] if X3.enough(y) else None


def numbers(Z, X, lie, ans, g):
    """Per split: line (in the two drawn dimensions Z), dir (in the full space X), n = [positives, negatives].
    Positive = lie for the lie splits, admit for the admit splits."""
    adm, known, every = (ans == "admit").astype(int), ans != "other", np.ones(len(lie), bool)
    masks = dict(lie_all=(lie, every), lie_deniers=(lie, ans == "deny"), lie_admitters=(lie, ans == "admit"),
                 admit_all=(adm, known), admit_lies=(adm, known & (lie == 1)), admit_truths=(adm, known & (lie == 0)))
    return {k: dict(line=auroc(X3.line_scores, Z, y, g, m), dir=auroc(X3.direction_scores, X, y, g, m),
                    n=[int(y[m].sum()), int((1 - y[m]).sum())]) for k, (y, m) in masks.items()}


def position(D, T, name, layer):
    """Per wording: the two drawn coordinates, the labels, the share of variance and the numbers."""
    out = {}
    for w in C.WORDINGS:
        X, have = D.vectors(T, w, name, layer)
        cls = X3.col(T, "cls", have)
        pres = (cls == "lie") | (cls == "truth")
        X, lie, g = X[pres], (cls[pres] == "lie").astype(int), X3.col(T, "group", have)[pres]
        ans = np.array([t["answer"][w] for t in T])[have][pres]
        mu, comp, share = X3.pca(X)
        Z = X3.orient((X - mu) @ comp.T, lie == 1, lie == 0)
        out[w] = dict(Z=Z, lie=lie, ans=ans, share=[float(v) for v in share], num=numbers(Z, X, lie, ans, g))
    return out


def f2(v):
    return "–" if v is None else f"{v:.2f}"


def scatter(ax, Z, colors, rng):
    """One call in a random order, so that neither group is drawn on top of the other."""
    o = rng.permutation(len(Z))
    ax.scatter(Z[o, 0], Z[o, 1], s=30, c=[colors[i] for i in o], edgecolors=X3.SURFACE, linewidths=0.6)


def draw(plt, path, name, layer, res):
    from matplotlib.lines import Line2D
    rng = np.random.default_rng(0)
    fig, axes = plt.subplots(2, 5, figsize=(16, 8.9))
    fig.subplots_adjust(left=0.04, right=0.995, top=0.855, bottom=0.07, wspace=0.24, hspace=0.46)
    for j, w in enumerate(C.WORDINGS):
        r, num = res[w], res[w]["num"]
        Z, lie, ans = r["Z"], r["lie"], r["ans"]
        scatter(axes[0, j], Z, [CLS_COL[int(v)] for v in lie], rng)
        scatter(axes[1, j], Z, [ANS_COL[a] for a in ans], rng)
        axes[0, j].set_title(f"{X3.SHORT[w]}   all {f2(num['lie_all']['line'])} · among deniers {f2(num['lie_deniers']['line'])}",
                             loc="left", fontsize=8.5, color=X3.INK2)
        axes[1, j].set_title(f"{X3.SHORT[w]}   all {f2(num['admit_all']['line'])} · among lies {f2(num['admit_lies']['line'])}\n"
                             + " · ".join(f"{ANS_NAME[a]} {int((ans == a).sum())}" for a in ANS_NAME),
                             loc="left", fontsize=8.5, color=X3.INK2, linespacing=1.5)
        lo, hi = Z.min(0), Z.max(0)                       # the same limits in both rows, one unit the same length on both axes
        box = axes[0, j].get_position()
        bw, bh = box.width * fig.get_figwidth(), box.height * fig.get_figheight()
        per_inch = 1.08 * max((hi[0] - lo[0]) / bw, (hi[1] - lo[1]) / bh)
        cx, cy = (lo + hi) / 2
        for ax in axes[:, j]:
            ax.set_xlim(cx - per_inch * bw / 2, cx + per_inch * bw / 2)
            ax.set_ylim(cy - per_inch * bh / 2, cy + per_inch * bh / 2)
            ax.set_xlabel(f"PC1 ({100 * r['share'][0]:.0f}% of the variance)")
            ax.set_ylabel(f"PC2 ({100 * r['share'][1]:.0f}%)", labelpad=2)
    n_lie, n_truth = int(res[C.WORDINGS[0]]["lie"].sum()), int((1 - res[C.WORDINGS[0]]["lie"]).sum())
    rows = (("Coloured lie against truth", [Line2D([], [], ls="", marker="o", ms=6, color=CLS_COL[1], label=f"lie ({n_lie})"),
                                             Line2D([], [], ls="", marker="o", ms=6, color=CLS_COL[0], label=f"truth ({n_truth})")], 0.3),
            ("Coloured by the self-report answer (the same points)",
             [Line2D([], [], ls="", marker="o", ms=6, color=ANS_COL[a], label=ANS_NAME[a]) for a in ANS_NAME], 0.52))
    H = fig.get_figheight()
    for i, (head, handles, up) in enumerate(rows):         # a header and a legend above each row, clear of the panel titles
        y = axes[i, 0].get_position().y1 + up / H
        fig.text(0.012, y, head, ha="left", va="center", fontsize=10, color=X3.INK, fontweight="bold")
        fig.legend(handles=handles, loc="center left", bbox_to_anchor=(0.012 + 0.0062 * len(head) + 0.02, y), ncol=3, fontsize=8.5,
                   handletextpad=0.2, columnspacing=1.4, borderpad=0)
    X3.finish(plt, fig, path,
              f"{dict(X3.AFTER, **EXTRA)[name]} ({name}), layer {layer}: one PCA per wording, fitted on that wording's pressured transcripts "
              f"({n_lie + n_truth} vectors)",
              "Each column is one wording with its own axes. Panel title: AUROC of a straight-line split in the picture (five folds, scenarios kept "
              "together),\nof lies against truths (top) and of admits against denies (bottom), among all and within one group. "
              "Each axis is flipped so that lies have the larger mean.")


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--positions", nargs="+", default=["preans_slot4"])
    ap.add_argument("--draw-layer", type=int, help="default: the model's middle band layer that was cut")
    ap.add_argument("--out", help="default: analysis/exp3")
    ap.add_argument("--data", default="exp3", help="the cut's folder under data/cluster/runs/<model>/ (exp3_last for think_slot3)")
    args = ap.parse_args()
    cfg = X3.configure(X3.QWEN)
    out = args.out or X3.out_dir(X3.QWEN)
    fig_dir = os.path.join(out, "fig")
    os.makedirs(fig_dir, exist_ok=True)
    draw_layer = args.draw_layer or cfg["draw"]
    tag = "" if draw_layer == cfg["draw"] else f"_L{draw_layer}"
    D, T = X3.Cut(os.path.join(C.RUNS, C.slug(X3.QWEN), args.data)), X3.load_transcripts()
    assert draw_layer in D.layers, f"layer {draw_layer} is not in the cut: {D.layers}"
    plt = X3.style()
    path = os.path.join(out, "by_wording.json")
    saved = json.load(open(path)) if os.path.exists(path) else {}
    for name in args.positions:
        assert name in X3.AFTER or name in EXTRA, f"{name} is not a cut position after the question: {list(X3.AFTER) + list(EXTRA)}"
        saved[name] = {}
        for layer in D.layers:
            res = position(D, T, name, layer)
            saved[name][str(layer)] = {w: dict(share=res[w]["share"], **res[w]["num"]) for w in C.WORDINGS}
            if layer == draw_layer:
                draw(plt, os.path.join(fig_dir, f"{name}_by_wording{tag}.png"), name, layer, res)
            for kind in ("line", "dir"):
                print(f"{name} layer {layer} {kind:4s} " + "; ".join(
                    f"{X3.SHORT[w]} " + " ".join(f2(res[w]["num"][k][kind]) for k in SPLITS) for w in C.WORDINGS), flush=True)
    with open(path, "w") as f:
        json.dump(saved, f, indent=1)
    print("columns per wording:", " ".join(SPLITS), "->", out)


if __name__ == "__main__":
    main()
