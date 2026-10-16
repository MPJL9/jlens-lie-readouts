"""Figure for 5.1 (1): the difference-of-means direction's held-out AUROC at the five template tokens after the
response (layer 47, lies against truths, all transcripts), one dot with its 95% interval per token, in token order,
with the AUROC printed above each dot. Same style as scripts/findings_2026_10_04/plot_postans_tokens.py (the 4.6
figure). Numbers from analysis/probe/qwen3_6_27b/bands.json (scripts/probe/score_bands.py on the exp3_bands cut).
No title or caption: the user writes those.

Run from the project root: python3 scripts/probe/plot_postresp_tokens.py
Output: analysis/post_figures/F_tokens_after_response.png (and .svg)
"""
import json
import os

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
LAYER, TASK = 47, "all"
TOKENS = [("postresp_slot0", "<|im_end|>"),
          ("postresp_slot1", "first newline after the response"),
          ("postresp_slot2", "<|im_start|>"),
          ("postresp_slot3", "user"),
          ("postresp_slot4", "second newline after the response")]
INK, INK2, GRID, BLUE = "#0b0b0b", "#52514e", "#e1e0d9", "#2a78d6"


def main():
    with open(os.path.join(ROOT, "analysis", "probe", "qwen3_6_27b", "bands.json")) as f:
        res = json.load(f)["results"]
    rows = [(label, res[f"{LAYER}/prefix/{name}/{TASK}"]["heldout"]) for name, label in TOKENS]
    fig, ax = plt.subplots(figsize=(7.2, 3.0), dpi=200)
    y = list(range(len(rows)))[::-1]                      # first token at the top
    for yy, (_, r) in zip(y, rows):
        ax.plot(r["ci"], [yy, yy], color=BLUE, lw=2, solid_capstyle="butt", zorder=2)
        ax.plot(r["auroc"], yy, "o", color=BLUE, ms=8, zorder=3)
        ax.annotate(f"{r['auroc']:.2f}", (r["auroc"], yy), xytext=(0, 7), textcoords="offset points",
                    ha="center", va="bottom", fontsize=8.5, color=INK, zorder=4)
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
    ax.set_ylim(-0.6, len(rows) - 0.3)
    fig.tight_layout()
    out = os.path.join(ROOT, "analysis", "post_figures", "F_tokens_after_response")
    os.makedirs(os.path.dirname(out), exist_ok=True)
    fig.savefig(out + ".png", facecolor="white")
    fig.savefig(out + ".svg", facecolor="white")
    print("written:", out + ".png")
    for label, r in rows:
        print(f"  {label}: {r['auroc']:.2f} ({r['ci'][0]:.2f} to {r['ci'][1]:.2f})")


if __name__ == "__main__":
    main()
