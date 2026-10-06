"""Figure for 4.6: the direction's held-out AUROC at the seven tokens around the self-report answer (layer 50,
lies against truths among the transcripts where the model denies), one dot with its 95% interval per token, in
token order. Numbers from analysis/heldout/postans.json (scripts/heldout/score_postans.py). No title or caption:
the user writes those.

Run from the project root: python3 scripts/findings_2026_10_04/plot_postans_tokens.py
Output: analysis/post_figures/F_tokens_after_answer.png (and .svg)
"""
import json
import os

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
LAYER, TASK = 50, "deniers"
TOKENS = [("think_slot3", "newline before the answer (the DYL probe's position)"),
          ("ans_tok0", "self-report answer (Yes / No)"),
          ("postans_slot0", "<|im_end|>"),
          ("postans_slot1", "first newline after the answer"),
          ("postans_slot2", "<|im_start|>"),
          ("postans_slot3", "user"),
          ("postans_slot4", "second newline after the answer")]
INK, INK2, GRID, BLUE = "#0b0b0b", "#52514e", "#e1e0d9", "#2a78d6"


def main():
    with open(os.path.join(ROOT, "analysis", "heldout", "postans.json")) as f:
        res = json.load(f)
    rows = [(label, res[f"{LAYER}/{name}/{TASK}"]) for name, label in TOKENS]
    fig, ax = plt.subplots(figsize=(7.2, 3.4), dpi=200)
    y = list(range(len(rows)))[::-1]                      # first token at the top
    for yy, (_, r) in zip(y, rows):
        ax.plot(r["ci"], [yy, yy], color=BLUE, lw=2, solid_capstyle="butt", zorder=2)
        ax.plot(r["auroc"], yy, "o", color=BLUE, ms=8, zorder=3)
    ax.axvline(0.5, color=INK2, lw=1, ls=(0, (3, 3)), zorder=1)
    ax.set_yticks(y)
    ax.set_yticklabels([label for label, _ in rows], color=INK, fontsize=9.5)
    ax.set_xlim(0.45, 1.0)
    ax.set_xticks([0.5, 0.6, 0.7, 0.8, 0.9, 1.0])
    ax.set_xlabel("AUROC", color=INK, fontsize=10)
    ax.tick_params(axis="x", colors=INK2, labelsize=9)
    ax.tick_params(axis="y", length=0)
    ax.grid(axis="x", color=GRID, lw=0.8, zorder=0)
    for side in ("top", "right", "left"):
        ax.spines[side].set_visible(False)
    ax.spines["bottom"].set_color(GRID)
    ax.set_ylim(-0.6, len(rows) - 0.4)
    fig.tight_layout()
    out = os.path.join(ROOT, "analysis", "post_figures", "F_tokens_after_answer")
    os.makedirs(os.path.dirname(out), exist_ok=True)
    fig.savefig(out + ".png", facecolor="white")
    fig.savefig(out + ".svg", facecolor="white")
    print("written:", out + ".png")


if __name__ == "__main__":
    main()
