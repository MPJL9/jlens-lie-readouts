#!/usr/bin/env python3
"""PLAN.md Section 4.1: the CKA suggestion for one layer band per model. No activations, no labels.

At layer l the J-lens gives token t the direction d_t(l) = J_l^T (g * U[t]) in the residual
stream: U[t] is the token's row of the unembedding matrix, g the final norm's scale (the norm's
per-position RMS factor does not change directions and is left out), J_l the lens map (the
identity at the last layer). For a fixed sample of tokens S, X_l = (U[S] * g) J_l is the
[n_tokens, d_model] arrangement of directions at layer l. Linear CKA (centered kernel
alignment) between X_l and X_m says how similar the two arrangements are, ignoring rotations
and overall scale. It is also computed after removing each layer's single strongest direction
(the first principal component of X_l), because one direction can dominate the plain score.

Token sample (seed 0, fixed): 2,000 "word" tokens, whose decoded text after one leading space is
2+ ASCII letters; and, as a check, 2,000 tokens drawn uniformly from the whole vocabulary.

Blocks: layers are cut into k contiguous blocks (k = 2..6) with Ward's criterion on 1 - CKA (the
cut that keeps dissimilar layers apart; exact search). The adjacent-layer CKA profile is reported
too. The band suggestion is drawn from these in analysis/band/BAND.md.

Inputs (all local): the lens files in the HF cache (read by path, no download), the cached weight shard
that holds the unembedding, and data/weights/<slug>_final_norm.npy (fetched once by
scripts/fetch_weights.py). Outputs: analysis/band/cka_<slug>.json, cka_<slug>.png, and
analysis/band/cka_summary.md.

Usage: python3 scripts/band_cka.py [--models m1 m2] [--n 2000]
"""
from __future__ import annotations

import argparse
import glob
import json
import os
import random
import re
import sys
import time

import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import common as C  # noqa: E402

OUT = os.path.join(C.ROOT, "analysis", "band")
WEIGHTS = os.path.join(C.DATA, "weights")
WORD = re.compile(r"^ ?[A-Za-z]{2,}$")


# ---------------------------------------------------------------- inputs
def lens_maps(model):
    """{layer: J_l as float32 numpy [d, d]} from the local HF cache (memory-mapped, no download)."""
    import torch
    sys.path.insert(0, os.path.join(C.ROOT, "src"))
    from models import LENS_REPO, MODELS  # noqa: E402
    spec = MODELS[model]
    repo = os.path.expanduser("~/.cache/huggingface/hub/models--" + LENS_REPO.replace("/", "--"))
    # the cached snapshot may be an older commit than the revision's current one; the files were
    # checked to be identical (same sha256 as the Hub's) on 2026-09-30
    paths = glob.glob(os.path.join(repo, "snapshots", "*", spec["lens_file"]))
    if not paths:
        sys.exit(f"FATAL: {spec['lens_file']} is not in the HF cache")
    ck = torch.load(paths[0], map_location="cpu", mmap=True, weights_only=False)
    return ck["J"], ck["d_model"]


def unembed_rows(model, ids):
    """Rows `ids` of the unembedding matrix (float32 [len(ids), d]) from data/weights/ (written
    by scripts/fetch_weights.py)."""
    z = np.load(os.path.join(WEIGHTS, C.slug(model) + "_unembed_rows.npz"))
    have = {int(i): k for k, i in enumerate(z["ids"])}
    return z["rows"][[have[int(i)] for i in ids]].astype(np.float32)


def final_scale(model):
    """g: the final norm's scale as used on the residual (Gemma stores w with output = x * (1 + w))."""
    g = np.load(os.path.join(WEIGHTS, C.slug(model) + "_final_norm.npy")).astype(np.float32)
    return 1.0 + g if model.startswith("gemma") else g


def token_samples(model, n, seed=0):
    """(word sample ids, uniform sample ids). Tokens that decode to "" (padding rows) are skipped."""
    vocab = C.load_vocab(model)
    ok = [i for i, s in enumerate(vocab) if s != ""]
    words = [i for i in ok if WORD.match(vocab[i])]
    rng = random.Random(seed)
    return sorted(rng.sample(words, n)), sorted(rng.sample(ok, n))


# ---------------------------------------------------------------- CKA
def centered_gram(X):
    X = X - X.mean(0, keepdims=True)
    return X @ X.T


def drop_top_direction(X):
    """Remove the first principal component of X (rows are token directions)."""
    Xc = X - X.mean(0, keepdims=True)
    # top right-singular vector via the small n x n problem
    _, _, vt = np.linalg.svd(Xc, full_matrices=False)
    v = vt[0]
    return Xc - np.outer(Xc @ v, v)


def cka_matrix(grams):
    """Linear CKA between every pair of layers from their centered Gram matrices."""
    n = len(grams)
    flat = np.stack([g.reshape(-1) for g in grams]).astype(np.float64)
    hsic = flat @ flat.T
    norm = np.sqrt(np.diag(hsic))
    return hsic / np.outer(norm, norm)


# ---------------------------------------------------------------- blocks
def best_blocks(M, k):
    """Cut layers 0..L-1 into k contiguous blocks. A block's cost is the sum of (1 - CKA) over
    its layer pairs divided by its size (Ward's criterion, with 1 - CKA as the squared
    distance); the cut with the lowest total cost is found exactly by dynamic programming.
    Returns block boundaries [(lo, hi), ...] as layer indices."""
    L = len(M)
    D = 1.0 - M
    cum = np.zeros((L + 1, L + 1))
    cum[1:, 1:] = D.cumsum(0).cumsum(1)

    def cost(a, b):               # layers a..b inclusive
        n = b - a + 1
        s = cum[b + 1, b + 1] - cum[a, b + 1] - cum[b + 1, a] + cum[a, a]   # both orders of each pair
        return s / (2 * n)

    best = np.full((k + 1, L + 1), np.inf)
    arg = np.zeros((k + 1, L + 1), int)
    best[0, 0] = 0.0
    for j in range(1, k + 1):
        for end in range(j, L + 1):
            for start in range(j - 1, end):
                v = best[j - 1, start] + cost(start, end - 1)
                if v < best[j, end]:
                    best[j, end], arg[j, end] = v, start
    blocks, end = [], L
    for j in range(k, 0, -1):
        start = arg[j, end]
        blocks.append((start, end - 1))
        end = start
    return blocks[::-1]


# ---------------------------------------------------------------- plot
def plot(model, layers, cka, cka_drop, adj, blocks, path):
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    fig, axes = plt.subplots(1, 3, figsize=(15.5, 4.6), gridspec_kw=dict(width_ratios=[1, 1, 1.1], wspace=0.35))
    for ax, M, title in [(axes[0], cka, "CKA between layers"), (axes[1], cka_drop, "strongest direction removed")]:
        im = ax.imshow(M, vmin=0, vmax=1, cmap="Blues", origin="lower")
        ax.set_title(title, fontsize=10)
        ax.set_xlabel("layer")
        ax.set_ylabel("layer")
        for lo, hi in blocks:
            ax.add_patch(plt.Rectangle((lo - 0.5, lo - 0.5), hi - lo + 1, hi - lo + 1, fill=False, ec="#eb6834", lw=1.5))
    fig.colorbar(im, ax=axes[:2], fraction=0.025, pad=0.03)
    fig.suptitle(f"{model}: linear CKA of the J-lens token directions (word sample; boxes = 4 blocks)", fontsize=10, y=1.0)
    ax = axes[2]
    ax.plot(layers[:-1], adj["plain"], color="#2a78d6", lw=2, marker="o", ms=4, label="plain")
    ax.plot(layers[:-1], adj["drop"], color="#eb6834", lw=2, marker="o", ms=4, label="strongest direction removed")
    for sp in ("top", "right"):
        ax.spines[sp].set_visible(False)
    ax.set_ylim(0, 1.02)
    ax.set_xlabel("layer l (CKA of l with l + 1)")
    ax.set_ylabel("CKA")
    ax.set_title("adjacent layers", fontsize=10)
    ax.grid(alpha=0.25, lw=0.5)
    ax.legend(fontsize=8, loc="lower left")
    fig.savefig(path, dpi=130, bbox_inches="tight")
    plt.close(fig)


# ---------------------------------------------------------------- main
def run(model, n):
    t0 = time.time()
    J, d = lens_maps(model)
    layers = C.load_manifest(model, drop_commentary=False)["layers"]
    final = layers[-1]
    g = final_scale(model)
    word_ids, unif_ids = token_samples(model, n)
    result = {"model": model, "d_model": d, "layers": layers, "n_tokens": n, "seed": 0,
              "word_sample_ids": word_ids, "uniform_sample_ids": unif_ids, "samples": {}}
    for name, ids in [("word", word_ids), ("uniform", unif_ids)]:
        Ug = unembed_rows(model, ids) * g[None, :]
        grams, grams_drop = [], []
        for l in layers:
            X = Ug if l == final else Ug @ J[l].float().numpy()
            grams.append(centered_gram(X))
            grams_drop.append(centered_gram(drop_top_direction(X)))
        cka = cka_matrix(grams)
        cka_drop = cka_matrix(grams_drop)
        adj = {"plain": [float(cka[i, i + 1]) for i in range(len(layers) - 1)],
               "drop": [float(cka_drop[i, i + 1]) for i in range(len(layers) - 1)]}
        blocks = {str(k): {"plain": [[layers[a], layers[b]] for a, b in best_blocks(cka, k)],
                           "drop": [[layers[a], layers[b]] for a, b in best_blocks(cka_drop, k)]}
                  for k in range(2, 7)}
        result["samples"][name] = {"cka": np.round(cka, 4).tolist(), "cka_drop": np.round(cka_drop, 4).tolist(),
                                   "adjacent": adj, "blocks": blocks}
        print(f"{model} [{name}] done in {time.time() - t0:.0f}s", flush=True)
    with open(os.path.join(OUT, f"cka_{C.slug(model)}.json"), "w") as f:
        json.dump(result, f)
    return result


def summary(results):
    lines = ["# CKA between layers of the J-lens directions (PLAN.md Section 4.1)", "",
             "Written by `scripts/band_cka.py`. Per model: the cut of the layers into k = 2..6 contiguous blocks",
             "(Ward's criterion on 1 - CKA), on the word-token sample (2,000 tokens, seed 0) and, as a check,",
             "the uniform sample. \"plain\" is the CKA of the raw directions; \"drop\" removes each layer's",
             "strongest direction first. Figures: `cka_<model>.png` (word sample; boxes = k = 4 blocks, drop).", ""]
    for r in results:
        layers = r["layers"]
        lines += [f"## {r['model']} ({len(layers)} layers, d = {r['d_model']})", ""]
        for name in ["word", "uniform"]:
            s = r["samples"][name]
            lines += [f"**{name} sample**", "", "| k | plain | drop |", "|---|---|---|"]
            for k in range(2, 7):
                fmt = lambda bl: ", ".join(f"{a}-{b}" for a, b in bl)
                lines.append(f"| {k} | {fmt(s['blocks'][str(k)]['plain'])} | {fmt(s['blocks'][str(k)]['drop'])} |")
            adj = s["adjacent"]
            low = sorted(range(len(adj["drop"])), key=lambda i: adj["drop"][i])[:5]
            lines += ["", "Lowest adjacent-layer CKA (drop): " +
                      ", ".join(f"{layers[i]}-{layers[i] + 1}: {adj['drop'][i]:.2f}" for i in sorted(low)), ""]
    with open(os.path.join(OUT, "cka_summary.md"), "w") as f:
        f.write("\n".join(lines))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--models", nargs="+", default=C.MODELS)
    ap.add_argument("--n", type=int, default=2000)
    args = ap.parse_args()
    os.makedirs(OUT, exist_ok=True)
    results = []
    for m in args.models:
        path = os.path.join(OUT, f"cka_{C.slug(m)}.json")
        if os.path.exists(path):
            with open(path) as f:
                results.append(json.load(f))
            print(f"{m}: using existing {path}")
        else:
            results.append(run(m, args.n))
    for r in results:
        s = r["samples"]["word"]
        blocks = [(r["layers"].index(a), r["layers"].index(b)) for a, b in s["blocks"]["4"]["drop"]]
        plot(r["model"], r["layers"], np.array(s["cka"]), np.array(s["cka_drop"]), s["adjacent"], blocks,
             os.path.join(OUT, f"cka_{C.slug(r['model'])}.png"))
    summary(results)


if __name__ == "__main__":
    main()
