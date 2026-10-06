"""Figure for 3.4: Qwen's chat template as a strip of tokens, every token named, the newline after the response
marked. Three rows: up to the response; the turn boundary after the response and the self-report question; the
boundary before the answer, the empty thinking block, the answer and the boundary after it. Prose segments (the
prompts, the response, the question, the answer) are wider grey boxes; template tokens are white boxes. No title or
caption: the user writes those.

Run from the project root: python3 scripts/findings_2026_10_04/plot_template_strip.py
Output: analysis/post_figures/F_template_strip.png (and .svg)
"""
import os

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402
from matplotlib.patches import FancyBboxPatch  # noqa: E402

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
INK, INK2, GRID, BLUE, PROSE = "#0b0b0b", "#52514e", "#c9c8c1", "#2a78d6", "#efeeea"
# (label, kind): kind "t" = template token, "p" = prose segment, "mark" = the marked newline
ROWS = [
    [("system prompt", "p"), ("user prompt", "p"), ("<|im_end|>", "t"), ("newline", "t"), ("<|im_start|>", "t"), ("assistant", "t"), ("newline", "t"), ("response", "p")],
    [("<|im_end|>", "t"), ("newline", "mark"), ("<|im_start|>", "t"), ("user", "t"), ("newline", "t"), ("self-report question", "p")],
    [("<|im_end|>", "t"), ("newline", "t"), ("<|im_start|>", "t"), ("assistant", "t"), ("newline", "t"), ("<think>", "t"), ("blank line", "t"), ("</think>", "t"),
     ("blank line", "t")],
    [("answer", "p"), ("<|im_end|>", "t"), ("newline", "t"), ("<|im_start|>", "t"), ("user", "t"), ("newline", "t")],
]
FONT = 11   # pt; the post column is about 700 px wide, so the figure is drawn 8 inches wide with large type
def width(label):
    """Box width in data units, from the label's length (11 pt type; one unit is about 0.55 inch)."""
    return 0.17 * len(label) + 0.45


def main():
    gap, h, rowgap = 0.1, 0.7, 1.0
    widths = [sum(width(l) for l, _ in row) + gap * (len(row) - 1) for row in ROWS]
    total_w, total_h = max(widths), len(ROWS) * h + (len(ROWS) - 1) * rowgap
    fig, ax = plt.subplots(figsize=(8, 8 * (total_h + 0.3) / (total_w + 0.2)), dpi=200)
    y, mark = 0, None
    for row in ROWS[::-1]:
        x = 0
        for label, kind in row:
            w = width(label)
            face = BLUE if kind == "mark" else (PROSE if kind == "p" else "white")
            edge = BLUE if kind == "mark" else GRID
            ax.add_patch(FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0,rounding_size=0.08", fc=face, ec=edge, lw=1.2))
            ax.text(x + w / 2, y + h / 2, label, ha="center", va="center", fontsize=FONT,
                    color="white" if kind == "mark" else (INK2 if kind == "p" else INK),
                    style="italic" if kind == "p" else "normal")
            if kind == "mark":
                mark = (x + w / 2, y + h)
            x += w + gap
        y += h + rowgap
    # the marker: the user's phrase from the draft, in the gap above the marked box
    ax.annotate("the newline after the response", xy=mark, xytext=(mark[0], mark[1] + 0.45), ha="left", va="bottom",
                fontsize=FONT, color=BLUE, arrowprops=dict(arrowstyle="-", color=BLUE, lw=1.2))
    ax.set_xlim(-0.1, total_w + 0.1)
    ax.set_ylim(-0.15, total_h + 0.15)
    ax.set_aspect("equal")
    ax.axis("off")
    fig.subplots_adjust(left=0.01, right=0.99, top=0.99, bottom=0.01)
    out = os.path.join(ROOT, "analysis", "post_figures", "F_template_strip")
    fig.savefig(out + ".png", facecolor="white")
    fig.savefig(out + ".svg", facecolor="white")
    print("written:", out + ".png")


if __name__ == "__main__":
    main()
