#!/usr/bin/env python3
"""Experiment 3 (heuristic study; PLAN.md Section 7): pictures of the residual stream at template
positions, with one number per picture. Design agreed with the user on 2026-10-03 for Qwen; the
user then asked for the same on Gemma (--model; the positions and the lie families of each model
are set in configure()).

Data: data/cluster/runs/<model>/exp3/ (cut on the cluster by src/cut_positions.py from the list
of scripts/exp3/build_cut_list.py): the residual stream at eight template positions and five band
layers, build split and unrelated chats only. The held-out split is never read.

Classes: lies and truths told under pressure ("pressured transcripts"), truths with no pressure,
unrelated chats. Scenario = the prompt; a scenario has at most one lie and one truth.

Two fits per position, PCA both (the first two principal components are drawn):
  U  fitted on the unrelated chats; every other point is placed on its axes
  P  fitted on the pressured transcripts; every other point is placed on its axes
Positions before the self-report question (postresp_slot1 and two controls) also get
  - a second colouring: how many of the model's lie families the newline readout holds (0, 1, 2
    or more; Qwen: the eight), with the lies that have none (the misses) ringed;
  - a picture along one supervised direction: mean of lies minus mean of truths. Each pressured
    transcript is scored by a direction fitted without its scenario.
Positions after the question pool the five wordings. Each wording's mean (taken on the fit set)
is subtracted first, because the tokens before the position differ by wording. One panel per
wording, on shared axes; marker shape shows whether the model admitted or denied. The raw pooled
fit (no subtraction) is drawn once per position, coloured by wording.
UMAP is drawn as a check for the P fit only (n_neighbors 15, min_dist 0.1, seeds 0 to 2).
More components of the U fit (user, 2026-10-03), at the drawn layer: the lie-minus-truth direction
is fitted within the first k principal components of the unrelated chats, k = 1 to 500 and all
(topk.png, NUMBERS.md Section 6); components 1 to 4 are drawn in consecutive pairs (PC1 against
PC2, PC2 against PC3, PC3 against PC4; <position>_U_more.png).

Numbers (all cross-validated in five folds with scenarios kept together):
  line   AUROC of a straight-line split (linear discriminant) of lies against truths in the two
         drawn dimensions; the line is fitted on the other folds. The axes are fitted without labels.
  dir    AUROC of the lie-minus-truth direction in the full space, fitted on the other folds.
  pairs  among scenarios with both a lie and a truth: how often the lie scores above its truth.
  After the question the same numbers are also given among deniers (line fitted among deniers).
Pictures are drawn at --draw-layer; the numbers are computed at every layer that was cut.

Output: analysis/exp3/ for Qwen, analysis/exp3/<slug>/ for the other models: fig/*.png,
numbers.json, NUMBERS.md.

Usage: python3 scripts/exp3/pictures.py [--model gemma-3-12b-it] [--data DIR] [--out DIR] [--no-umap]
"""
import argparse
import json
import os
import sys
import warnings

import numpy as np

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import common as C  # noqa: E402
import presence as P  # noqa: E402

QWEN = "qwen3.6-27b"
# Qwen: the newline detector's set (family_findings.md Section 9). Gemma: the model's lie-leaning
# families at the same position (Section 12). Word lists: the draft families of post-response slot 1.
EIGHT = ["lie", "fake", "falsehood", "misinformation", "deceive", "fabricate", "false", "mislead"]
MODELS = {
    QWEN: dict(name="Qwen3.6-27B", draw=47, role="assistant", families=EIGHT, fam="the eight families", fam_short="the eight"),
    "gemma-3-12b-it": dict(name="Gemma-3-12B", draw=29, role="model", scale=True, fam="its eight lie-leaning families", fam_short="the eight",
                           families=["lie", "obfuscate", "mislead", "pretend", "evade", "hide", "deflect", "blatant"]),
    "gemma-3-27b-it": dict(name="Gemma-3-27B", draw=39, role="model", scale=True, fam="its three lie-leaning families", fam_short="the three",
                           families=["lie", "lying-face emoji", "secret"]),
}
KS = [1, 2, 3, 5, 10, 20, 50, 100, 200, 500]     # numbers of principal components of the unrelated chats
PAIRS = ((0, 1), (1, 2), (2, 3))                  # the component pairs drawn for the unrelated fit (user, 2026-10-03)
MODEL = CFG = BEFORE = AFTER = None               # set by configure()
SCALE = False     # divide each dimension by its spread in the unrelated chats before every fit (Gemma: a few dimensions
#                   are hundreds of times larger than the rest and otherwise drive every picture; user, 2026-10-03)


def configure(model, scale=None):
    """Set the model: its template positions, its lie families, the layer the pictures are drawn at,
    and whether the dimensions are scaled (scale=None: the model's default)."""
    global MODEL, CFG, BEFORE, AFTER, SCALE
    MODEL, CFG = model, MODELS[model]
    SCALE = CFG.get("scale", False) if scale is None else scale
    BEFORE = {"postresp_slot1": "the newline after the response",
              "postresp_slot0": "control: the turn-end token after the response",
              "preresp_slot4": "control: the newline before the response"}
    AFTER = {"preans_slot1": "the newline after the question"}
    if model.startswith("gemma"):          # Gemma's readout carries a signal at the turn-start token too
        AFTER["preans_slot2"] = "the turn-start token after the question"
    AFTER["preans_slot4"] = f"the newline after `{CFG['role']}`"
    if model == QWEN:                      # only Qwen has a thinking block
        AFTER["think_slot2"] = "`</think>`"
    AFTER["postans_slot1"] = "the first newline after the self-report answer"
    AFTER["postans_slot4"] = "the last newline after the self-report answer"
    return CFG


def out_dir(model):
    base = os.path.join(C.ROOT, "analysis", "exp3")
    return base if model == QWEN else os.path.join(base, C.slug(model))


SHORT = {"Q1_bare": "Q1", "Q2_after": "Q2", "Q6_factual": "Q6", "Q7_ab": "Q7", "Q9_dyl": "Q9"}
CLASS_NAME = {"lie": "lie", "truth": "truth", "np_truth": "no-pressure truth", "unrelated": "unrelated chat"}
FIT_NAME = {"U": "fitted on the unrelated chats", "P": "fitted on the pressured transcripts"}

# colours: the reference palette of the chart rules (first three slots pass the all-pairs check)
SURFACE, INK, INK2, MUTED, GRID = "#fcfcfb", "#0b0b0b", "#52514e", "#898781", "#e1e0d9"
COL = {"lie": "#eb6834", "truth": "#2a78d6", "np_truth": "#1baf7a", "unrelated": "#c3c2b7"}
RAMP = ["#86b6ef", "#2a78d6", "#0d366b"]                     # 0, 1, 2 or more of the eight (one hue)
WCOL = ["#2a78d6", "#eb6834", "#1baf7a", "#eda100", "#e87ba4"]   # wordings, with direct labels
SHAPE = {"deny": "o", "admit": "^", "other": "X"}


# ---------------------------------------------------------------- data
class Cut:
    """The cut residual streams: vectors(T, part, name, layer) -> (float64 [n, d], have mask)."""

    def __init__(self, data_dir):
        with open(os.path.join(data_dir, "meta.json")) as f:
            self.meta = json.load(f)
        self.layers = self.meta["layers"]
        self.arr, self.row = {}, {}
        for s in self.meta["sets"]:
            self.arr[s] = np.load(os.path.join(data_dir, f"{s}.npy"), mmap_mode="r")
            for i, r in enumerate(C.read_jsonl(os.path.join(data_dir, f"{s}.jsonl"))):
                self.row[(r["tid"], r["part"], r["name"])] = (s, i)

    def vectors(self, T, part, name, layer):
        li = self.layers.index(layer)
        where = [self.row.get((t["tid"], part, name)) for t in T]
        have = np.array([w is not None for w in where])
        X = np.zeros((int(have.sum()), self.arr[next(iter(self.arr))].shape[2]))
        at = {s: [] for s in self.arr}
        for k, w in enumerate(w for w in where if w is not None):
            at[w[0]].append((w[1], k))
        for s, pairs in at.items():
            if pairs:
                rows, ks = zip(*sorted(pairs))
                X[list(ks)] = self.arr[s][list(rows), li]
        return X, have


def load_transcripts():
    """Build-split lies, truths and no-pressure truths, and the unrelated chats. count = how many
    of the model's lie families are present in the J-lens readout at post-response slot 1."""
    man = C.load_manifest(MODEL)
    d = P.load(MODEL, "J")
    with open(os.path.join(C.ROOT, "analysis", "families", "families_draft.json")) as f:
        fd = [e for e in json.load(f)["entries"] if e["model"] == MODEL and e["lens"] == "J" and e["status"] == "keep"
              and e["part"] == "prefix" and e["position"] == "postresp_slot1"]
    cnt = np.zeros(len(d["transcripts"]), int)
    for name in CFG["families"]:
        ids = {x["id"] for e in fd if e["name"] == name for x in e["members"]}
        assert ids, f"no draft family {name!r} at post-response slot 1 of {MODEL}"
        cnt += P.present_mask(d, "prefix", "postresp_slot1", ids)
    count = {t["tid"]: int(c) for t, c in zip(d["transcripts"], cnt)}
    T = []
    for e in man["transcripts"]:
        cls = P._class(e)
        if e["split"] == "heldout" or cls == "np_lie":
            continue
        T.append(dict(tid=e["tid"], cls=cls, group=e["item_id"] if cls != "unrelated" else e["tid"], count=count[e["tid"]],
                      answer={w: e["wordings"][w]["answer_label"] for w in C.WORDINGS}))
    return T


def col(T, key, have=None):
    a = np.array([t[key] for t in T])
    return a if have is None else a[have]


# ---------------------------------------------------------------- fits and numbers
def unit_spread(X, U):
    """X with each dimension divided by its spread (standard deviation) in the rows of U (unrelated chats)."""
    sd = U.std(0)
    sd[sd == 0] = 1
    return X / sd


def pca(X, k=2):
    """(mean, components [k, d], share of the variance [k]) of the rows of X."""
    from scipy.linalg import eigh
    mu = X.mean(0)
    Xc = X - mu
    n = len(Xc)
    if n <= Xc.shape[1]:
        w, U = eigh(Xc @ Xc.T, subset_by_index=[n - k, n - 1])
        w, U = w[::-1], U[:, ::-1]
        assert w[-1] > 1e-12 * w[0], f"asked for {k} components, more than the {n} vectors span"
        comp = (Xc.T @ U / np.sqrt(w)).T
    else:
        w, V = eigh(Xc.T @ Xc, subset_by_index=[Xc.shape[1] - k, Xc.shape[1] - 1])
        w, comp = w[::-1], V[:, ::-1].T
    return mu, comp, w / (Xc ** 2).sum()


def orient(Z, lie, truth):
    """Flip each axis so that lies have the larger mean (display only)."""
    for j in range(Z.shape[1]):
        if lie.any() and truth.any() and Z[lie, j].mean() < Z[truth, j].mean():
            Z[:, j] *= -1
    return Z


def folds(y, groups, k=5):
    from sklearn.model_selection import StratifiedGroupKFold
    return StratifiedGroupKFold(n_splits=k, shuffle=True, random_state=0).split(np.zeros(len(y)), y, groups)


def line_scores(Z, y, groups):
    """Held-out score of each point on a straight-line split fitted on the other folds."""
    from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
    s = np.full(len(y), np.nan)
    for tr, te in folds(y, groups):
        s[te] = LinearDiscriminantAnalysis().fit(Z[tr], y[tr]).decision_function(Z[te])
    return s


def direction_scores(X, y, groups):
    """Held-out score on the direction mean(lies) - mean(truths) of the other folds; 0 is the
    midpoint between the two means."""
    s = np.full(len(y), np.nan)
    for tr, te in folds(y, groups):
        a, b = X[tr][y[tr] == 1].mean(0), X[tr][y[tr] == 0].mean(0)
        s[te] = (X[te] - (a + b) / 2) @ ((a - b) / np.linalg.norm(a - b))
    return s


def summary(s, y, groups):
    """AUROC, and among scenarios with both a lie and a truth: [lie above, ties, pairs]."""
    from sklearn.metrics import roc_auc_score
    lie = {g: v for v, yy, g in zip(s, y, groups) if yy == 1}
    truth = {g: v for v, yy, g in zip(s, y, groups) if yy == 0}
    both = sorted(set(lie) & set(truth))
    wins = sum(lie[g] > truth[g] for g in both)
    ties = sum(lie[g] == truth[g] for g in both)
    return dict(auroc=float(roc_auc_score(y, s)), pairs=[int(wins), int(ties), len(both)],
                n=[int((y == 1).sum()), int((y == 0).sum())])


def topk_ks(n_fit):
    """The numbers of components tried for a fit set of n_fit vectors: KS, then all of them if few."""
    most = n_fit - 1
    return [k for k in KS if k < most] + ([most] if most <= 1000 else [])


def topk(Z, y, groups, ks):
    """AUROC of the lie-minus-truth direction (fitted on the other folds) within the first k
    coordinates of Z, for each k."""
    return [summary(direction_scores(Z[:, :k], y, groups), y, groups)["auroc"] for k in ks]


def lengths(X, *masks):
    """Per mask: [mean length of its vectors, spread = standard deviation / mean]."""
    out = []
    for m in masks:
        n = np.linalg.norm(X[m], axis=1)
        out.append([float(n.mean()), float(n.std() / n.mean())])
    return out


def enough(y, k=10):
    return (y == 1).sum() >= k and (y == 0).sum() >= k


def umap_embed(X, seed):
    import umap
    with warnings.catch_warnings():
        warnings.simplefilter("ignore")
        return umap.UMAP(n_neighbors=15, min_dist=0.1, random_state=seed).fit_transform(X)


# ---------------------------------------------------------------- drawing
def style():
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    plt.rcParams.update({
        "font.family": ["Helvetica Neue", "Arial", "DejaVu Sans"], "font.size": 9, "figure.facecolor": SURFACE,
        "axes.facecolor": SURFACE, "axes.edgecolor": "#c3c2b7", "axes.linewidth": 0.6, "axes.labelcolor": INK2,
        "axes.grid": True, "grid.color": GRID, "grid.linewidth": 0.5, "axes.axisbelow": True,
        "xtick.color": MUTED, "ytick.color": MUTED, "xtick.labelsize": 8, "ytick.labelsize": 8,
        "axes.spines.top": False, "axes.spines.right": False, "savefig.facecolor": SURFACE, "legend.frameon": False})
    return plt


def dots(ax, Z, color, marker="o", big=True, **kw):
    if big:      # a surface-coloured ring keeps overlapping markers apart
        ax.scatter(Z[:, 0], Z[:, 1], s=30, c=color, marker=marker, edgecolors=SURFACE, linewidths=0.6, **kw)
    else:
        ax.scatter(Z[:, 0], Z[:, 1], s=7, c=color, marker=marker, linewidths=0, alpha=0.7, **kw)


def panel_class(ax, Z, cls, answer=None):
    """Colour = class. With answer: marker shape of lies and truths = the self-report answer."""
    for c in ("unrelated", "np_truth"):
        dots(ax, Z[cls == c], COL[c], big=False)
    for c in ("truth", "lie"):
        if answer is None:
            dots(ax, Z[cls == c], COL[c])
        else:
            for a, mk in SHAPE.items():
                dots(ax, Z[(cls == c) & (answer == a)], COL[c], marker=mk)


def panel_count(ax, Z, cls, cnt):
    """Lies (circles) and truths (triangles) coloured by the number of the model's lie families;
    the lies with none are ringed, the truths with one or more are boxed."""
    for c in ("unrelated", "np_truth"):
        dots(ax, Z[cls == c], "#e1e0d9", big=False)
    for c, mk in (("truth", "^"), ("lie", "o")):
        for k in (2, 1, 0):
            m = (cls == c) & (np.minimum(cnt, 2) == k)
            dots(ax, Z[m], RAMP[k], marker=mk)
    miss = (cls == "lie") & (cnt == 0)
    ax.scatter(Z[miss, 0], Z[miss, 1], s=95, facecolors="none", edgecolors=INK, linewidths=0.9)
    flag = (cls == "truth") & (cnt >= 1)             # truths whose readout holds a lie family (user, 2026-10-03)
    ax.scatter(Z[flag, 0], Z[flag, 1], s=130, marker="s", facecolors="none", edgecolors=INK, linewidths=0.9)


def handles_class(plt, cls=None, shapes=False):
    from matplotlib.lines import Line2D
    h = [Line2D([], [], ls="", marker="o", ms=6 if c in ("lie", "truth") else 3.5, color=COL[c],
                label=CLASS_NAME[c] + ("" if cls is None else f" ({int((cls == c).sum())})")) for c in ("lie", "truth", "np_truth", "unrelated")]
    if shapes:
        h += [Line2D([], [], ls="", marker=mk, ms=6, color=MUTED, label={"deny": "denies", "admit": "admits", "other": "other answer"}[a])
              for a, mk in SHAPE.items()]
    return h


def handles_count(plt, cls, cnt):
    from matplotlib.lines import Line2D
    n = lambda c, k: int(((cls == c) & (np.minimum(cnt, 2) == k)).sum())
    lab = [f"none of {CFG['fam_short']}", "one", "two or more"]
    h = [Line2D([], [], ls="", marker="s", ms=6, color=RAMP[k], label=f"{lab[k]} (lies {n('lie', k)}, truths {n('truth', k)})")
         for k in range(3)]
    h += [Line2D([], [], ls="", marker="o", ms=6, color=MUTED, label="lie"),
          Line2D([], [], ls="", marker="^", ms=6, color=MUTED, label="truth"),
          Line2D([], [], ls="", marker="o", ms=9, markerfacecolor="none", color=INK, label=f"missed lie (none of {CFG['fam_short']})"),
          Line2D([], [], ls="", marker="s", ms=9, markerfacecolor="none", color=INK, label=f"flagged truth (one or more of {CFG['fam_short']})")]
    return h


def equal_limits(fig, axes, Zs):
    """The same limits in every panel, with one unit the same length on both axes."""
    Z = np.concatenate(Zs)
    lo, hi = Z.min(0), Z.max(0)
    box = axes[0].get_position()
    w, h = box.width * fig.get_figwidth(), box.height * fig.get_figheight()
    per_inch = 1.08 * max((hi[0] - lo[0]) / w, (hi[1] - lo[1]) / h)
    cx, cy = (lo + hi) / 2
    for ax in axes:
        ax.set_xlim(cx - per_inch * w / 2, cx + per_inch * w / 2)
        ax.set_ylim(cy - per_inch * h / 2, cy + per_inch * h / 2)
    for ax in axes[1:]:
        ax.tick_params(labelleft=False)


def finish(plt, fig, path, title, sub):
    h = fig.get_figheight()                  # title and subtitle at fixed distances from the top, whatever the height
    fig.text(0.012, 1 - 0.09 / h, title, ha="left", va="top", fontsize=11, color=INK, fontweight="bold")
    fig.text(0.012, 1 - 0.37 / h, sub, ha="left", va="top", fontsize=8.5, color=INK2, linespacing=1.5)
    fig.savefig(path, dpi=150)
    plt.close(fig)


def fmt(r):
    w, t, n = r["pairs"]
    tie = f", {t} ties" if t else ""
    return f"AUROC {r['auroc']:.2f}; the lie is above its truth in {w} of {n} pairs{tie}"


def draw_before(plt, path, Z, cls, cnt, title, sub, xlabel, ylabel):
    fig, axes = plt.subplots(1, 2, figsize=(11.5, 6.2))
    panel_class(axes[0], Z, cls)
    panel_count(axes[1], Z, cls, cnt)
    axes[0].set_title("coloured by class", loc="left", fontsize=9, color=INK2)
    axes[1].set_title(f"coloured by the number of {CFG['fam']} in the newline readout", loc="left", fontsize=9, color=INK2)
    for ax in axes:
        ax.set_xlabel(xlabel)
    axes[0].set_ylabel(ylabel)
    axes[0].legend(handles=handles_class(plt, cls), loc="upper left", bbox_to_anchor=(0, -0.1), ncol=2, fontsize=8)
    axes[1].legend(handles=handles_count(plt, cls, cnt), loc="upper left", bbox_to_anchor=(0, -0.1), ncol=2, fontsize=8)
    fig.subplots_adjust(left=0.06, right=0.99, top=0.84, bottom=0.21, wspace=0.05)
    equal_limits(fig, axes, [Z])
    finish(plt, fig, path, title, sub)


def draw_after(plt, path, Zw, clsw, answ, notes, title, sub, xlabel, ylabel):
    fig, axes = plt.subplots(1, 5, figsize=(16, 4.6))
    for ax, w in zip(axes, C.WORDINGS):
        panel_class(ax, Zw[w], clsw[w], answ[w])
        ax.set_title(f"{SHORT[w]}   {notes[w]}", loc="left", fontsize=8.5, color=INK2)
        ax.set_xlabel(xlabel)
    axes[0].set_ylabel(ylabel)
    fig.legend(handles=handles_class(plt, shapes=True), loc="lower center", ncol=7, fontsize=8)
    fig.subplots_adjust(left=0.045, right=0.995, top=0.8, bottom=0.2, wspace=0.04)
    equal_limits(fig, axes, [Zw[w] for w in C.WORDINGS])
    finish(plt, fig, path, title, sub)


def draw_raw(plt, path, Z, wording, title, sub, xlabel, ylabel):
    fig, ax = plt.subplots(figsize=(6.4, 5.6))
    for k, w in enumerate(C.WORDINGS):
        m = wording == w
        dots(ax, Z[m], WCOL[k])
        ax.annotate(SHORT[w], Z[m].mean(0), fontsize=10, color=INK, fontweight="bold", ha="center", va="center",
                    bbox=dict(boxstyle="round,pad=0.2", fc=SURFACE, ec=WCOL[k], lw=1.2))
    ax.set_aspect("equal", adjustable="datalim")
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    from matplotlib.lines import Line2D      # the groups can overlap and hide each other's label
    ax.legend(handles=[Line2D([], [], ls="", marker="o", ms=6, color=WCOL[k], label=SHORT[w]) for k, w in enumerate(C.WORDINGS)],
              loc="upper left", bbox_to_anchor=(1.0, 1.0), fontsize=8)
    fig.subplots_adjust(left=0.11, right=0.9, top=0.84, bottom=0.1)
    finish(plt, fig, path, title, sub)


def draw_more(plt, path, Z, cls, pres, y, g, share, title, sub):
    """Components 1 to 4 of the unrelated fit in consecutive pairs, coloured by class."""
    fig, axes = plt.subplots(1, 3, figsize=(16, 6.2))
    for ax, (a, b) in zip(axes, PAIRS):
        Zp = Z[:, [a, b]]
        panel_class(ax, Zp, cls)
        auc = summary(line_scores(Zp[pres], y, g), y, g)["auroc"]
        ax.set_title(f"PC{a + 1} against PC{b + 1}   line AUROC {auc:.2f}", loc="left", fontsize=9, color=INK2)
        ax.set_xlabel(f"PC{a + 1} ({100 * share[a]:.0f}% of the unrelated chats' variance)")
        ax.set_ylabel(f"PC{b + 1} ({100 * share[b]:.0f}%)")
    fig.legend(handles=handles_class(plt, cls), loc="lower center", ncol=4, fontsize=8)
    fig.subplots_adjust(left=0.045, right=0.99, top=0.84, bottom=0.17, wspace=0.16)
    for ax, (a, b) in zip(axes, PAIRS):
        equal_limits(fig, [ax], [Z[:, [a, b]]])
    finish(plt, fig, path, title, sub)


def draw_more_after(plt, path, Zw, clsw, answ, aucs, share, title, sub):
    """The same pairs after the question: one row per pair, one column per wording; marker shape =
    the self-report answer. Each row has its own limits, shared by the five wordings."""
    fig, axes = plt.subplots(len(PAIRS), 5, figsize=(16, 4.1 * len(PAIRS) + 1.4))
    fig.subplots_adjust(left=0.045, right=0.995, top=1 - 1.1 / fig.get_figheight(), bottom=1.0 / fig.get_figheight(), wspace=0.04, hspace=0.3)
    for row, (a, b) in zip(axes, PAIRS):
        for ax, w in zip(row, C.WORDINGS):
            panel_class(ax, Zw[w][:, [a, b]], clsw[w], answ[w])
            ax.set_title(f"{SHORT[w]}   PC{a + 1} against PC{b + 1}   line AUROC {aucs[w][(a, b)]:.2f}", loc="left", fontsize=8.5, color=INK2)
            ax.set_xlabel(f"PC{a + 1} ({100 * share[a]:.0f}% of the unrelated chats' variance)")
        row[0].set_ylabel(f"PC{b + 1} ({100 * share[b]:.0f}%)")
        equal_limits(fig, list(row), [Zw[w][:, [a, b]] for w in C.WORDINGS])
    fig.legend(handles=handles_class(plt, shapes=True), loc="lower center", ncol=7, fontsize=8)
    finish(plt, fig, path, title, sub)


def draw_topk(plt, path, res):
    """One small panel per position: AUROC of the lie-minus-truth direction within the first k
    principal components of the unrelated chats, against k. A grey line marks the full space."""
    from matplotlib.lines import Line2D
    from matplotlib.ticker import ScalarFormatter
    dl = str(res["draw_layer"])
    panels = [(n, d, res["before"][n][dl]) for n, d in BEFORE.items()] + [(n, d, res["after"][n][dl]) for n, d in AFTER.items()]
    cols = 4
    rows = -(-len(panels) // cols)
    fig, axes = plt.subplots(rows, cols, figsize=(16, 3.5 * rows + 1.3), sharey=True)
    two = False
    for ax, (name, desc, r) in zip(axes.ravel(), panels):
        t = r["topk"]
        if name in BEFORE:
            series, full = [(t["auroc"], COL["truth"])], r["D"]["auroc"]
        else:
            mean = lambda key: [float(np.mean(v)) for v in zip(*[t[w][key] for w in C.WORDINGS if t[w][key]])]
            series, full = [(mean("all"), COL["truth"])], float(np.mean([t[w]["full"]["all"] for w in C.WORDINGS]))
            if any(t[w]["deniers"] for w in C.WORDINGS):
                series.append((mean("deniers"), COL["lie"]))
                two = True
        ax.axhline(full, color="#c3c2b7", lw=1.2)
        ax.axhline(0.5, color=GRID, lw=0.8)
        top = max(vals[-1] for vals, _ in series)
        for vals, colour in series:
            ax.plot(t["ks"], vals, color=colour, lw=2, marker="o", ms=4.5, markeredgecolor=SURFACE, markeredgewidth=0.8)
            va = "center" if len(series) == 1 else ("bottom" if vals[-1] == top else "top")    # two end labels: one above, one below
            ax.annotate(f"{vals[-1]:.2f}", (t["ks"][-1], vals[-1]), xytext=(5, 0), textcoords="offset points", fontsize=8, color=INK2, va=va)
        ax.set_xscale("log")
        ax.set_xticks([k for k in (1, 2, 5, 10, 20, 50, 100, 200, 500) if k <= t["ks"][-1]])
        ax.get_xaxis().set_major_formatter(ScalarFormatter())
        ax.minorticks_off()
        ax.set_xlim(0.8, t["ks"][-1] * 1.9)
        ax.set_ylim(0.4, 1.0)
        ax.set_title(desc.replace("`", "") + f"\nfull space {full:.2f}", loc="left", fontsize=8.5, color=INK2)
    for ax in axes.ravel()[len(panels):]:
        ax.set_visible(False)
    for ax in axes[-1]:
        ax.set_xlabel("number of principal components of the unrelated chats")
    for ax in axes[:, 0]:
        ax.set_ylabel("AUROC, lies against truths")
    h = [Line2D([], [], color=COL["truth"], lw=2, marker="o", ms=4.5, label="all lies and truths (after the question: mean of the wordings)")]
    if two:
        h.append(Line2D([], [], color=COL["lie"], lw=2, marker="o", ms=4.5, label="among deniers (mean of the wordings that have enough)"))
    h.append(Line2D([], [], color="#c3c2b7", lw=1.2, label="the same direction in the full space"))
    fig.legend(handles=h, loc="lower center", ncol=3, fontsize=8)
    fig.subplots_adjust(left=0.05, right=0.985, top=1 - 1.0 / (3.5 * rows + 1.3), bottom=0.9 / (3.5 * rows + 1.3) + 0.04, wspace=0.08, hspace=0.42)
    finish(plt, fig, path, f"{CFG['name']}, layer {dl}: how many principal components of the unrelated chats separate lies from truths",
           "The lie-minus-truth direction is fitted within the first k components (on other scenarios than the one scored). "
           "The last point uses the most components tried.")


# ---------------------------------------------------------------- one position
def before_position(D, T, name, layer, draw, fig_dir, use_umap, n_boot):
    X, have = D.vectors(T, "prefix", name, layer)
    cls, grp, cnt = col(T, "cls", have), col(T, "group", have), col(T, "count", have)
    if SCALE:
        X = unit_spread(X, X[cls == "unrelated"])
    pres = (cls == "lie") | (cls == "truth")
    y, g = (cls[pres] == "lie").astype(int), grp[pres]
    out = {"length": lengths(X, pres, cls == "unrelated")}
    for fit, mask in (("U", cls == "unrelated"), ("P", pres)):
        mu, comp, share = pca(X[mask])
        Z = orient((X - mu) @ comp.T, cls == "lie", cls == "truth")
        s = line_scores(Z[pres], y, g)
        out[fit] = dict(summary(s, y, g), share=[float(v) for v in share])
        if draw:
            if n_boot:
                out[fit]["ci"] = C.grouped_bootstrap_ci(list(zip(s.tolist(), y.tolist(), g.tolist())), n_boot)
            draw_before(draw, os.path.join(fig_dir, f"{name}_{fit}.png"), Z, cls, cnt,
                        f"{BEFORE[name]} ({name}), layer {layer}: PCA {FIT_NAME[fit]} ({int(mask.sum())})",
                        f"Straight-line split of lies against truths in this picture: {fmt(out[fit])}.",
                        f"PC1 ({100 * share[0]:.0f}% of the fit set's variance)", f"PC2 ({100 * share[1]:.0f}%)")
    if draw:                                               # more components of the unrelated fit
        unrel = cls == "unrelated"
        ks = topk_ks(int(unrel.sum()))
        mu, comp, share = pca(X[unrel], ks[-1])
        Zk = (X - mu) @ comp.T
        out["topk"] = dict(ks=ks, auroc=topk(Zk[pres], y, g, ks), share=[float(share[:k].sum()) for k in ks])
        draw_more(draw, os.path.join(fig_dir, f"{name}_U_more.png"), orient(Zk[:, :4].copy(), cls == "lie", cls == "truth"), cls, pres, y, g, share,
                  f"{BEFORE[name]} ({name}), layer {layer}: components 1 to 4 of the unrelated chats ({int(unrel.sum())})",
                  "Each panel has its own straight-line split of lies against truths. The first 4 components hold "
                  f"{100 * share[:4].sum():.0f}% of the unrelated chats' variance.")
    s = direction_scores(X[pres], y, g)
    lie_p, miss_p = cls[pres] == "lie", (cls[pres] == "lie") & (cnt[pres] == 0)
    out["D"] = dict(summary(s, y, g),
                    misses_truth_side=[int((s[miss_p] < 0).sum()), int(miss_p.sum())],
                    caught_truth_side=[int((s[lie_p & ~miss_p] < 0).sum()), int((lie_p & ~miss_p).sum())],
                    truths_lie_side=[int((s[~lie_p] > 0).sum()), int((~lie_p).sum())])
    if draw:
        if n_boot:
            out["D"]["ci"] = C.grouped_bootstrap_ci(list(zip(s.tolist(), y.tolist(), g.tolist())), n_boot)
        a, b = X[cls == "lie"].mean(0), X[cls == "truth"].mean(0)
        d = (a - b) / np.linalg.norm(a - b)
        x_all = (X - (a + b) / 2) @ d
        x_all[pres] = s                                    # pressured points: the held-out score
        R = X - np.outer((X - (a + b) / 2) @ d, d)
        mu, comp, share = pca(R[pres], 1)
        Z = np.column_stack([x_all, (R - mu) @ comp[0]])
        m, c, t = out["D"]["misses_truth_side"], out["D"]["caught_truth_side"], out["D"]["truths_lie_side"]
        draw_before(draw, os.path.join(fig_dir, f"{name}_direction.png"), Z, cls, cnt,
                    f"{BEFORE[name]} ({name}), layer {layer}: the lie-minus-truth direction",
                    f"Full space, direction fitted without the transcript's scenario: {fmt(out['D'])}.\n"
                    f"Left of 0 (the truth side): {m[0]} of {m[1]} missed lies, {c[0]} of {c[1]} other lies; right of 0: {t[0]} of {t[1]} truths.",
                    "score on the direction mean(lies) - mean(truths); 0 = midpoint", "PC1 of what is left (pressured fit)")
        if use_umap:
            aur = []
            for seed in range(3):
                E = umap_embed(X[pres], seed)
                aur.append(summary(line_scores(E, y, g), y, g)["auroc"])
                if seed == 0:
                    draw_before(draw, os.path.join(fig_dir, f"{name}_umap.png"), orient(E, y == 1, y == 0), cls[pres], cnt[pres],
                                f"{BEFORE[name]} ({name}), layer {layer}: UMAP of the pressured transcripts (check)", "", "UMAP 1", "UMAP 2")
            out["umap"] = aur
    return out


def after_position(D, T, name, layer, draw, fig_dir, use_umap):
    Xw, clsw, grpw, answ = {}, {}, {}, {}
    for w in C.WORDINGS:
        Xw[w], have = D.vectors(T, w, name, layer)
        clsw[w], grpw[w] = col(T, "cls", have), col(T, "group", have)
        answ[w] = np.array([t["answer"][w] for t in T])[have]
    if SCALE:                                             # one scale per position: the spread within each wording's unrelated chats
        U = np.concatenate([Xw[w][clsw[w] == "unrelated"] - Xw[w][clsw[w] == "unrelated"].mean(0) for w in C.WORDINGS])
        Xw = {w: unit_spread(Xw[w], U) for w in C.WORDINGS}
    pres = {w: (clsw[w] == "lie") | (clsw[w] == "truth") for w in C.WORDINGS}
    out = {"length": {w: lengths(Xw[w], pres[w], clsw[w] == "unrelated") for w in C.WORDINGS}}
    for fit in ("U", "P"):
        fitm = {w: (clsw[w] == "unrelated") if fit == "U" else pres[w] for w in C.WORDINGS}
        cen = {w: Xw[w] - Xw[w][fitm[w]].mean(0) for w in C.WORDINGS}       # each wording's mean on the fit set
        mu, comp, share = pca(np.concatenate([cen[w][fitm[w]] for w in C.WORDINGS]))
        Zw = {w: (cen[w] - mu) @ comp.T for w in C.WORDINGS}
        for j in range(2):                                                # one orientation for all wordings
            if np.concatenate([Zw[w][clsw[w] == "lie", j] for w in C.WORDINGS]).mean() < \
                    np.concatenate([Zw[w][clsw[w] == "truth", j] for w in C.WORDINGS]).mean():
                for w in C.WORDINGS:
                    Zw[w][:, j] *= -1
        out[fit], notes = {"share": [float(v) for v in share]}, {}
        for w in C.WORDINGS:
            Z, y, g, a = Zw[w][pres[w]], (clsw[w][pres[w]] == "lie").astype(int), grpw[w][pres[w]], answ[w][pres[w]]
            r = {"all": summary(line_scores(Z, y, g), y, g)}
            den = a == "deny"
            r["deniers"] = summary(line_scores(Z[den], y[den], g[den]), y[den], g[den]) if enough(y[den]) else None
            out[fit][w] = r
            notes[w] = f"all {r['all']['auroc']:.2f}" + (
                f" · deniers {r['deniers']['auroc']:.2f} ({r['deniers']['n'][0]} lies, {r['deniers']['n'][1]} truths)" if r["deniers"] else "")
        if draw:
            n_fit = sum(int(fitm[w].sum()) for w in C.WORDINGS)
            draw_after(draw, os.path.join(fig_dir, f"{name}_{fit}.png"), Zw, clsw, answ, notes,
                       f"{AFTER[name]} ({name}), layer {layer}: PCA {FIT_NAME[fit]}, five wordings pooled ({n_fit} vectors)",
                       "Each wording's mean on the fit set is subtracted before the fit. One panel per wording, shared axes. "
                       "Panel title: AUROC of a straight-line split of lies against truths, among all and among deniers.",
                       f"PC1 ({100 * share[0]:.0f}% of the fit set's variance)", f"PC2 ({100 * share[1]:.0f}%)")
    if draw:                                               # more components of the unrelated fit
        unrel = {w: clsw[w] == "unrelated" for w in C.WORDINGS}
        cen = {w: Xw[w] - Xw[w][unrel[w]].mean(0) for w in C.WORDINGS}
        F = np.concatenate([cen[w][unrel[w]] for w in C.WORDINGS])
        ks = topk_ks(len(F) - len(C.WORDINGS) + 1)        # one mean subtracted per wording: F spans len(F) - 5 dimensions
        mu, comp, share = pca(F, ks[-1])
        out["topk"] = dict(ks=ks, share=[float(share[:k].sum()) for k in ks])
        for w in C.WORDINGS:
            y, g, den = (clsw[w][pres[w]] == "lie").astype(int), grpw[w][pres[w]], answ[w][pres[w]] == "deny"
            Zk, Xp = (cen[w][pres[w]] - mu) @ comp.T, Xw[w][pres[w]]
            ok = enough(y[den])
            out["topk"][w] = dict(
                all=topk(Zk, y, g, ks), deniers=topk(Zk[den], y[den], g[den], ks) if ok else None,
                full=dict(all=summary(direction_scores(Xp, y, g), y, g)["auroc"],
                          deniers=summary(direction_scores(Xp[den], y[den], g[den]), y[den], g[den])["auroc"] if ok else None))
        Z4 = {w: (cen[w] - mu) @ comp[:4].T for w in C.WORDINGS}
        for j in range(4):                                                # one orientation for all wordings
            if np.concatenate([Z4[w][clsw[w] == "lie", j] for w in C.WORDINGS]).mean() < \
                    np.concatenate([Z4[w][clsw[w] == "truth", j] for w in C.WORDINGS]).mean():
                for w in C.WORDINGS:
                    Z4[w][:, j] *= -1
        aucs = {w: {pair: summary(line_scores(Z4[w][pres[w]][:, list(pair)], (clsw[w][pres[w]] == "lie").astype(int), grpw[w][pres[w]]),
                                  (clsw[w][pres[w]] == "lie").astype(int), grpw[w][pres[w]])["auroc"] for pair in PAIRS} for w in C.WORDINGS}
        draw_more_after(draw, os.path.join(fig_dir, f"{name}_U_more.png"), Z4, clsw, answ, aucs, share,
                        f"{AFTER[name]} ({name}), layer {layer}: components 1 to 4 of the unrelated chats, five wordings pooled ({len(F)} vectors)",
                        "Each wording's mean on the unrelated chats is subtracted before the fit. One row per pair of components, one column per wording. "
                        f"The first 4 components hold {100 * share[:4].sum():.0f}% of the unrelated chats' variance.")
    if draw:
        Xp = np.concatenate([Xw[w][pres[w]] for w in C.WORDINGS])
        word = np.concatenate([np.full(int(pres[w].sum()), w) for w in C.WORDINGS])
        mu, comp, share = pca(Xp)
        draw_raw(draw, os.path.join(fig_dir, f"{name}_raw.png"), (Xp - mu) @ comp.T, word,
                 f"{AFTER[name]} ({name}), layer {layer}: raw pooled fit", "Pressured transcripts, no mean subtracted, coloured by wording.",
                 f"PC1 ({100 * share[0]:.0f}% of the variance)", f"PC2 ({100 * share[1]:.0f}%)")
        out["raw_share"] = [float(v) for v in share]
        if use_umap:
            cen = np.concatenate([Xw[w][pres[w]] - Xw[w][pres[w]].mean(0) for w in C.WORDINGS])
            out["umap"] = {w: {"all": [], "deniers": []} for w in C.WORDINGS}
            for seed in range(3):
                E = umap_embed(cen, seed)
                Ew, notes = {}, {}
                for w in C.WORDINGS:
                    Ew[w] = E[word == w]
                    y, g, a = (clsw[w][pres[w]] == "lie").astype(int), grpw[w][pres[w]], answ[w][pres[w]]
                    den = a == "deny"
                    out["umap"][w]["all"].append(summary(line_scores(Ew[w], y, g), y, g)["auroc"])
                    if enough(y[den]):
                        out["umap"][w]["deniers"].append(summary(line_scores(Ew[w][den], y[den], g[den]), y[den], g[den])["auroc"])
                    notes[w] = f"all {out['umap'][w]['all'][-1]:.2f}"
                if seed == 0:
                    draw_after(draw, os.path.join(fig_dir, f"{name}_umap.png"), Ew, {w: clsw[w][pres[w]] for w in C.WORDINGS},
                               {w: answ[w][pres[w]] for w in C.WORDINGS}, notes,
                               f"{AFTER[name]} ({name}), layer {layer}: UMAP of the pressured transcripts, five wordings pooled (check)",
                               "Each wording's mean is subtracted before the fit. Panel title: AUROC of a straight-line split, seed 0.",
                               "UMAP 1", "UMAP 2")
    return out


# ---------------------------------------------------------------- tables
def write_tables(res, path):
    layers, dl = res["layers"], str(res["draw_layer"])
    f2 = lambda v: "–" if v is None else f"{v:.2f}"
    ci = lambda r: f" ({r['ci'][0]:.2f} to {r['ci'][1]:.2f})" if r.get("ci") else ""
    pr = lambda r: f"{r['pairs'][0]} of {r['pairs'][2]}" + (f" ({r['pairs'][1]} ties)" if r["pairs"][1] else "")
    L = [f"# Experiment 3: numbers behind the pictures ({CFG['name']}, build split, in-sample)", "",
         "Written by `scripts/exp3/pictures.py`. Every number is cross-validated in five folds with scenarios kept together.",
         "*line* = AUROC of a straight-line split of lies against truths in the two drawn dimensions. *direction* = AUROC of the",
         "lie-minus-truth direction in the full space. *pairs* = scenarios with both a lie and a truth in which the lie scores above",
         "its truth. 0.50 is chance. Transcripts: " + ", ".join(f"{v} {k}s" for k, v in res["counts"].items()) + ".", ""]
    if res.get("scale"):
        L += ["**Scaled.** Before every fit, each dimension of the residual stream is divided by its spread (standard deviation) in the",
              "unrelated chats at the same position and layer (after the question: the spread within each wording). The lengths in",
              "Section 5 are those of the scaled vectors.", ""]
    L += [f"## 1. Before the question, layer {dl}", "",
         "| position | measure | AUROC (95% interval over scenarios) | pairs |", "|---|---|---|---|"]
    meas = [("U", "line, fit on unrelated chats"), ("P", "line, fit on pressured transcripts"), ("D", "direction, full space")]
    for name in BEFORE:
        for k, lab in meas:
            r = res["before"][name][dl][k]
            L.append(f"| {BEFORE[name]} | {lab} | {r['auroc']:.2f}{ci(r)} | {pr(r)} |")
    L += ["", "Along the direction (0 = midpoint between the two means of the other folds):", "",
          "| position | missed lies on the truth side | other lies on the truth side | truths on the lie side |", "|---|---|---|---|"]
    for name in BEFORE:
        r = res["before"][name][dl]["D"]
        L.append(f"| {BEFORE[name]} | " + " | ".join(f"{r[k][0]} / {r[k][1]}" for k in ("misses_truth_side", "caught_truth_side", "truths_lie_side")) + " |")
    L += ["", "## 2. Before the question, by layer", "", "| position | measure | " + " | ".join(f"layer {l}" for l in layers) + " |",
          "|---|---|" + "---|" * len(layers)]
    for name in BEFORE:
        for k, lab in meas:
            L.append(f"| {BEFORE[name]} | {lab} | " + " | ".join(f2(res["before"][name][str(l)][k]["auroc"]) for l in layers) + " |")
    if any("umap" in res["before"][n][dl] for n in BEFORE):
        L += ["", "UMAP of the pressured transcripts (check; line AUROC for seeds 0, 1, 2): " +
              "; ".join(f"{BEFORE[n]}: " + ", ".join(f2(v) for v in res["before"][n][dl]["umap"]) for n in BEFORE if "umap" in res["before"][n][dl]) + "."]
    L += ["", f"## 3. After the question, layer {dl}", "",
          "Lies / truths in brackets. *deniers* = transcripts that answer No; the line is fitted among deniers.", ""]
    for name in AFTER:
        L += [f"**{AFTER[name]}** (`{name}`)", "",
              "| wording | unrelated fit: all | unrelated fit: deniers | pressured fit: all | pressured fit: deniers | UMAP check: all (three seeds) |",
              "|---|---|---|---|---|---|"]
        for w in C.WORDINGS:
            cells = []
            for fit in ("U", "P"):
                r = res["after"][name][dl][fit][w]
                cells.append(f"{r['all']['auroc']:.2f} ({r['all']['n'][0]} / {r['all']['n'][1]})")
                cells.append("–" if r["deniers"] is None else f"{r['deniers']['auroc']:.2f} ({r['deniers']['n'][0]} / {r['deniers']['n'][1]})")
            u = res["after"][name][dl].get("umap")
            cells.append(", ".join(f2(v) for v in u[w]["all"]) if u else "–")
            L.append(f"| {SHORT[w]} | " + " | ".join(cells) + " |")
        L.append("")
    L += ["## 4. After the question, by layer (line AUROC; all, then deniers)", ""]
    for name in AFTER:
        L += [f"**{AFTER[name]}** (`{name}`)", "", "| wording | fit | " + " | ".join(f"layer {l}" for l in layers) + " |",
              "|---|---|" + "---|" * len(layers)]
        for w in C.WORDINGS:
            for fit, lab in (("U", "unrelated"), ("P", "pressured")):
                row = []
                for l in layers:
                    r = res["after"][name][str(l)][fit][w]
                    row.append(f"{r['all']['auroc']:.2f}, {f2(r['deniers']['auroc'] if r['deniers'] else None)}")
                L.append(f"| {SHORT[w]} | {lab} | " + " | ".join(row) + " |")
        L.append("")
    L += [f"## 5. Vector lengths, layer {dl}", "",
          "Mean length of the residual vectors and its spread (standard deviation / mean). A small spread means that a fit on",
          "vectors scaled to length 1 (the cosine view) would show nearly the same picture as the PCA drawn here. After the",
          "question: the mean over the five wordings.", "",
          "| position | pressured: mean length | pressured: spread | unrelated: mean length | unrelated: spread |", "|---|---|---|---|---|"]
    for name in BEFORE:
        (a, b), (c, d) = res["before"][name][dl]["length"]
        L.append(f"| {BEFORE[name]} | {a:.0f} | {100 * b:.1f}% | {c:.0f} | {100 * d:.1f}% |")
    for name in AFTER:
        v = np.mean([np.ravel(res["after"][name][dl]["length"][w]) for w in C.WORDINGS], axis=0)
        L.append(f"| {AFTER[name]} | {v[0]:.0f} | {100 * v[1]:.1f}% | {v[2]:.0f} | {100 * v[3]:.1f}% |")
    L += ["", f"## 6. Lies against truths within the first k principal components of the unrelated chats, layer {dl}", "",
          "AUROC of the lie-minus-truth direction fitted within the first k components (on other scenarios than the one scored).",
          "*full space* = the same direction with no restriction. After the question: the mean over the wordings; *deniers* over the",
          "wordings with 10 or more lying and 10 or more truthful deniers. The last k is all components when there are 1,000 or fewer.", ""]
    allk = sorted({k for n in BEFORE for k in res["before"][n][dl]["topk"]["ks"]} | {k for n in AFTER for k in res["after"][n][dl]["topk"]["ks"]})
    L += ["| position | " + " | ".join(f"k = {k}" for k in allk) + " | full space |", "|---|" + "---|" * (len(allk) + 1)]
    cell = lambda t, vals: " | ".join(f2(dict(zip(t["ks"], vals)).get(k)) for k in allk)
    for name in BEFORE:
        t = res["before"][name][dl]["topk"]
        L.append(f"| {BEFORE[name]} | {cell(t, t['auroc'])} | {res['before'][name][dl]['D']['auroc']:.2f} |")
    for name in AFTER:
        t = res["after"][name][dl]["topk"]
        for key, lab in (("all", ""), ("deniers", ", deniers")):
            ws = [w for w in C.WORDINGS if t[w][key]]
            if ws:
                mean = [float(np.mean(v)) for v in zip(*[t[w][key] for w in ws])]
                L.append(f"| {AFTER[name]}{lab} | {cell(t, mean)} | {np.mean([t[w]['full'][key] for w in ws]):.2f} |")
    L += ["", "Share of the unrelated chats' variance held by the first k components:", "",
          "| position | " + " | ".join(f"k = {k}" for k in allk) + " |", "|---|" + "---|" * len(allk)]
    for name, desc, r in [(n, d, res["before"][n][dl]) for n, d in BEFORE.items()] + [(n, d, res["after"][n][dl]) for n, d in AFTER.items()]:
        t = r["topk"]
        L.append(f"| {desc} | " + " | ".join("–" if k not in t["ks"] else f"{100 * dict(zip(t['ks'], t['share']))[k]:.0f}%" for k in allk) + " |")
    L.append("")
    with open(path, "w") as f:
        f.write("\n".join(L))


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--model", default=QWEN, choices=list(MODELS))
    ap.add_argument("--data", help="default: data/cluster/runs/<model>/exp3")
    ap.add_argument("--out", help="default: analysis/exp3 (Qwen) or analysis/exp3/<model>")
    ap.add_argument("--draw-layer", type=int, help="default: the model's middle band layer that was cut")
    ap.add_argument("--no-umap", action="store_true")
    ap.add_argument("--boot", type=int, default=1000, help="bootstrap resamples for the intervals at the drawn layer (0 = none)")
    ap.add_argument("--scale", choices=["on", "off"], help="divide each dimension by its spread in the unrelated chats "
                    "(default: on for Gemma, off for Qwen)")
    args = ap.parse_args()
    configure(args.model, None if args.scale is None else args.scale == "on")
    args.data = args.data or os.path.join(C.RUNS, C.slug(MODEL), "exp3")
    args.out = args.out or out_dir(MODEL)
    args.draw_layer = args.draw_layer or CFG["draw"]
    fig_dir = os.path.join(args.out, "fig")
    os.makedirs(fig_dir, exist_ok=True)
    D, T = Cut(args.data), load_transcripts()
    plt = style()
    cls = col(T, "cls")
    counts = {CLASS_NAME[c]: int((cls == c).sum()) for c in CLASS_NAME}
    misses = int(((cls == "lie") & (col(T, "count") == 0)).sum())
    print(MODEL, "transcripts:", counts, f"| lies with none of {CFG['fam_short']}:", misses, "| layers:", D.layers, "| drawn:", args.draw_layer,
          "| scaled:", SCALE)
    res = dict(model=MODEL, name=CFG["name"], families=CFG["families"], layers=D.layers, draw_layer=args.draw_layer, counts=counts,
               misses=misses, before={}, after={})
    if SCALE:
        res["scale"] = True
    for name in BEFORE:
        res["before"][name] = {}
        for layer in D.layers:
            draw = plt if layer == args.draw_layer else None
            res["before"][name][str(layer)] = r = before_position(D, T, name, layer, draw, fig_dir, not args.no_umap, args.boot)
            print(f"{name} layer {layer}: line U {r['U']['auroc']:.2f}, line P {r['P']['auroc']:.2f}, direction {r['D']['auroc']:.2f}", flush=True)
    for name in AFTER:
        res["after"][name] = {}
        for layer in D.layers:
            draw = plt if layer == args.draw_layer else None
            res["after"][name][str(layer)] = r = after_position(D, T, name, layer, draw, fig_dir, not args.no_umap)
            print(f"{name} layer {layer}: " + "; ".join(
                f"{SHORT[w]} U {r['U'][w]['all']['auroc']:.2f} P {r['P'][w]['all']['auroc']:.2f}" for w in C.WORDINGS), flush=True)
    draw_topk(plt, os.path.join(fig_dir, "topk.png"), res)
    with open(os.path.join(args.out, "numbers.json"), "w") as f:
        json.dump(res, f, indent=1)
    write_tables(res, os.path.join(args.out, "NUMBERS.md"))
    print("->", args.out)


if __name__ == "__main__":
    main()
