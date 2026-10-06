#!/usr/bin/env python3
"""A first look at outstanding families, before any threshold is set (user, 2026-10-02).

Qwen3.6-27B, J-lens, band 35-58. Families are the draft families as they are (unmerged; kept
entries of analysis/families/families_draft.json, entries with the same name at one position
pooled). For every family at every position:

  before the self-report question   a = share of lies with the family, b = share of truths
  from the question on              a = share of the lies that deny, b = share of the truths that deny
  controls                          the larger of the shares in no-pressure truths and unrelated chats

Outputs, under analysis/outstanding/:
  OUTSTANDING.md             how many cells pass "b and controls at most m, a at least n" for a grid of
                             m and n; the sorted tables
  postresp_slot1.png         one dot per family at post-response slot 1 (x = b, y = a)
  after_question_deniers.png the same among deniers at the template positions after the question
  outstanding.json           every cell

Reads the presence index (build split and unrelated set only; the held-out split is not read).
Every number is in-sample.

Usage: python3 scripts/outstanding_families.py
"""
from __future__ import annotations

import json
import os
import sys
from collections import defaultdict

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402
import numpy as np  # noqa: E402

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import common as C  # noqa: E402
import presence as P  # noqa: E402
from position_map import tokens_at_positions, show  # noqa: E402

QWEN = "qwen3.6-27b"
OUT = os.path.join(C.ROOT, "analysis", "outstanding")
MIN_SHARE = 0.20            # a family is listed where it reaches this share in one or more groups
LIST_GAP = 0.25             # a cell enters the sorted tables when |a - b| is at least this
CONTROL_CAP = 0.15          # dots are coloured by whether the controls stay at or under this
M_GRID, N_GRID = [0.05, 0.10, 0.15, 0.20], [0.30, 0.40, 0.50, 0.60, 0.70]
PANEL_POS = ["preans_slot1", "preans_slot2", "preans_slot4", "think_slot2", "postans_slot1", "postans_slot4"]
POS_TITLE = {"preans_slot1": "pre-answer slot 1\n(newline)", "preans_slot2": "pre-answer slot 2\n(turn start)",
             "preans_slot4": "pre-answer slot 4\n(newline)", "think_slot2": "think slot 2\n(</think>)",
             "postans_slot1": "post-answer slot 1\n(newline)", "postans_slot4": "post-answer slot 4\n(newline)"}
# chart colours: the first two slots of the dataviz reference palette (validated all-pairs, light surface)
SURFACE, INK, MUTED, GRID = "#fcfcfb", "#0b0b0b", "#52514e", "#e4e3df"
BLUE, ORANGE = "#2a78d6", "#eb6834"


def share(mask, sel):
    n = int(sel.sum())
    return int((mask & sel).sum()), n


def rate(t):
    return t[0] / t[1] if t[1] else float("nan")


def cells():
    d = P.load(QWEN, "J")
    cls = d["cls"]
    vocab = C.load_vocab(QWEN)
    with open(os.path.join(C.ROOT, "analysis", "families", "families_draft.json")) as f:
        entries = [e for e in json.load(f)["entries"] if e["model"] == QWEN and e["lens"] == "J" and e["status"] == "keep"]
    kept = defaultdict(lambda: defaultdict(set))
    for e in entries:
        kept[(e["part"], e["position"])][e["name"]] |= {m["id"] for m in e["members"]}
    toks = tokens_at_positions()
    out = []
    for part in ["prefix"] + C.WORDINGS:
        ans = P.answer(d, part) if part != "prefix" else None
        for pos in P.positions(d, part):
            hv = P.have_mask(d, part, pos)
            for name, ids in kept.get((part, pos), {}).items():
                pm = P.present_mask(d, part, pos, ids)
                r = dict(part=part, position=pos, token=toks[part].get(pos, "?"), family=name,
                         members=[P.tok(vocab[i]) for i in sorted(ids)],
                         lie=share(pm, hv & (cls == "lie")), truth=share(pm, hv & (cls == "truth")),
                         np=share(pm, hv & (cls == "np_truth")), un=share(pm, hv & (cls == "unrelated")))
                if part != "prefix":
                    r["lie_deny"] = share(pm, hv & (cls == "lie") & (ans == "deny"))
                    r["truth_deny"] = share(pm, hv & (cls == "truth") & (ans == "deny"))
                    r["a"], r["b"] = rate(r["lie_deny"]), rate(r["truth_deny"])
                else:
                    r["a"], r["b"] = rate(r["lie"]), rate(r["truth"])
                r["control"] = max(rate(r["np"]), rate(r["un"]))
                shares = [rate(r[k]) for k in ("lie", "truth", "np", "un", "lie_deny", "truth_deny") if k in r]
                if max(shares) >= MIN_SHARE:
                    out.append(r)
    return out


def fmt(t):
    return f"{t[0]}/{t[1]} ({100 * rate(t):.0f}%)" if t[1] else "–"


def place_labels(ax, pts, fontsize):
    """Label the given (x, y, text) points. Each label takes the free spot nearest to its dot: right or
    left of it, moved up or down in steps until it overlaps no other label, no dot and stays inside."""
    h = 0.036 * fontsize / 8
    cw = 0.0135 * fontsize / 8
    pad = 0.022
    boxes = [(x - 0.014, x + 0.014, y - 0.014, y + 0.014) for x, y, _ in pts]

    def free(b):
        return all(b[1] < o[0] or b[0] > o[1] or b[3] < o[2] or b[2] > o[3] for o in boxes)

    for x, y, text in sorted(pts, key=lambda p: (-p[1], p[0])):
        w = cw * len(text)
        best = None
        for k in range(0, 14):
            for dy in ((0,) if k == 0 else (k * h, -k * h)):
                for right in (True, False):
                    lx = x + pad if right else x - pad - w
                    b = (lx, lx + w, y + dy - h / 2, y + dy + h / 2)
                    if b[0] >= -0.02 and b[1] <= 1.03 and b[2] >= -0.02 and b[3] <= 1.03 and free(b):
                        best = (right, dy, b)
                        break
                if best:
                    break
            if best:
                break
        if best is None:
            continue
        right, dy, b = best
        boxes.append(b)
        ax.annotate(text, (x, y), xytext=(x + pad if right else x - pad, y + dy), fontsize=fontsize, color=INK,
                    ha="left" if right else "right", va="center",
                    arrowprops=dict(arrowstyle="-", color=MUTED, lw=0.4, shrinkA=0, shrinkB=2) if dy else None)


def style(ax):
    ax.set_facecolor(SURFACE)
    ax.set_xlim(-0.03, 1.03)
    ax.set_ylim(-0.03, 1.03)
    ax.set_aspect("equal")
    ax.plot([0, 1], [0, 1], color=GRID, lw=1, zorder=1)
    ax.set_xticks([0, 0.5, 1], ["0%", "50%", "100%"])
    ax.set_yticks([0, 0.5, 1], ["0%", "50%", "100%"])
    ax.tick_params(colors=MUTED, labelsize=7, length=0)
    ax.grid(color=GRID, lw=0.6)
    ax.set_axisbelow(True)
    for s in ax.spines.values():
        s.set_visible(False)


def dots(ax, rows, size):
    for colour, sel in ((BLUE, lambda r: r["control"] <= CONTROL_CAP), (ORANGE, lambda r: r["control"] > CONTROL_CAP)):
        xs = [r["b"] for r in rows if sel(r)]
        ys = [r["a"] for r in rows if sel(r)]
        ax.scatter(xs, ys, s=size, color=colour, edgecolor=SURFACE, linewidth=1.2, zorder=3)


def legend(fig, y):
    handles = [plt.Line2D([], [], marker="o", ls="", color=BLUE, markeredgecolor=SURFACE, markersize=7,
                          label=f"present in at most {100 * CONTROL_CAP:.0f}% of no-pressure truths and of unrelated chats"),
               plt.Line2D([], [], marker="o", ls="", color=ORANGE, markeredgecolor=SURFACE, markersize=7,
                          label="present in more of them (the family does not need a lie, or even the scenario)")]
    fig.legend(handles=handles, loc="upper left", bbox_to_anchor=(0.02, y), frameon=False, fontsize=8, labelcolor=INK)


def figure_postresp(rows):
    rows = [r for r in rows if r["part"] == "prefix" and r["position"] == "postresp_slot1"]
    fig, ax = plt.subplots(figsize=(7.2, 7.6), facecolor=SURFACE)
    style(ax)
    dots(ax, rows, 60)
    place_labels(ax, [(r["b"], r["a"], r["family"]) for r in rows], 8)
    ax.set_xlabel("share of truths with the family", color=MUTED, fontsize=9)
    ax.set_ylabel("share of lies with the family", color=MUTED, fontsize=9)
    fig.suptitle("Families at post-response slot 1 (the newline after the response)", x=0.02, ha="left", fontsize=11, color=INK)
    fig.text(0.02, 0.945, "Qwen3.6-27B, J-lens, build split: 152 lies, 81 truths. One dot per draft family.", fontsize=8, color=MUTED)
    legend(fig, 0.935)
    fig.subplots_adjust(top=0.84, left=0.11, right=0.97, bottom=0.08)
    fig.savefig(os.path.join(OUT, "postresp_slot1.png"), dpi=170, facecolor=SURFACE)
    plt.close(fig)


def figure_after(rows):
    fig, axes = plt.subplots(len(C.WORDINGS), len(PANEL_POS), figsize=(17, 15.2), facecolor=SURFACE)
    for i, w in enumerate(C.WORDINGS):
        for j, pos in enumerate(PANEL_POS):
            ax = axes[i][j]
            style(ax)
            sub = [r for r in rows if r["part"] == w and r["position"] == pos]
            dots(ax, sub, 34)
            far = sorted([r for r in sub if abs(r["a"] - r["b"]) >= LIST_GAP], key=lambda r: -abs(r["a"] - r["b"]))[:7]
            place_labels(ax, [(r["b"], r["a"], r["family"]) for r in far], 6.5)
            if i == 0:
                ax.set_title(POS_TITLE[pos], fontsize=9, color=INK)
            if j == 0:
                ax.set_ylabel(f"{w.split('_')[0]}\nlies that deny", color=MUTED, fontsize=9)
            if i == len(C.WORDINGS) - 1:
                ax.set_xlabel("truths that deny", color=MUTED, fontsize=9)
    fig.suptitle("Families after the self-report question, among the transcripts that deny", x=0.02, ha="left", fontsize=13, color=INK)
    fig.text(0.02, 0.962, "Qwen3.6-27B, J-lens, build split. One dot per draft family. Labels: the families farthest from the diagonal "
             f"(a gap of {100 * LIST_GAP:.0f} points or more, at most seven per panel).", fontsize=9, color=MUTED)
    legend(fig, 0.957)
    fig.subplots_adjust(top=0.895, left=0.05, right=0.99, bottom=0.04, wspace=0.16, hspace=0.12)
    fig.savefig(os.path.join(OUT, "after_question_deniers.png"), dpi=140, facecolor=SURFACE)
    plt.close(fig)


def grid_table(rows, title):
    L = [title, "", "| the rate after truths and both controls at most | " + " | ".join(f"lies at least {100 * n:.0f}%" for n in N_GRID) + " |",
         "|---|" + "---|" * len(N_GRID)]
    for m in M_GRID:
        L.append(f"| {100 * m:.0f}% | " + " | ".join(str(sum(1 for r in rows if r["b"] <= m and r["control"] <= m and r["a"] >= n)) for n in N_GRID) + " |")
    return L + [""]


def row_line(r, after):
    mem = ", ".join(f"`{m}`" for m in r["members"][:6]) + (f" … (+{len(r['members']) - 6})" if len(r["members"]) > 6 else "")
    cols = [r["family"], mem, fmt(r["lie"]), fmt(r["truth"])]
    if after:
        cols = [r["part"].split("_")[0], f"{r['position']} ({show(r['token'])})"] + cols + [fmt(r["lie_deny"]), fmt(r["truth_deny"])]
    cols += [fmt(r["np"]), fmt(r["un"]), f"{100 * (r['a'] - r['b']):+.0f}"]
    return "| " + " | ".join(cols) + " |"


def main():
    os.makedirs(OUT, exist_ok=True)
    rows = cells()
    with open(os.path.join(OUT, "outstanding.json"), "w") as f:
        json.dump(rows, f, ensure_ascii=False, indent=1)
    figure_postresp(rows)
    figure_after(rows)
    before = [r for r in rows if r["part"] == "prefix"]
    slot1 = sorted([r for r in before if r["position"] == "postresp_slot1"], key=lambda r: r["b"] - r["a"])
    after = [r for r in rows if r["part"] != "prefix"]
    template = [r for r in after if not r["position"].startswith("q_tok")]
    L = ["# Outstanding families: a first look (Qwen3.6-27B, J-lens, band 35-58)", "",
         "Written by `scripts/outstanding_families.py`. Build split only; every number is in-sample. Families are the",
         "draft families as they are (unmerged). No threshold is set here; the tables are for choosing one.", "",
         "- *gap* = the rate after lies minus the rate after truths, in points. From the question on, both rates",
         "  are taken among the transcripts whose self-report answer is a denial.",
         "- *controls* = no-pressure truths and unrelated chats.", "",
         "## 1. Post-response slot 1 (the newline after the response)", "",
         "![families at post-response slot 1](postresp_slot1.png)", ""]
    L += grid_table(slot1, "Number of families that pass, for each pair of thresholds:")
    L += ["| family | members | lies | truths | no-pressure truths | unrelated | gap |", "|---|---|---|---|---|---|---|"]
    L += [row_line(r, False) for r in slot1]
    L += ["", "## 2. After the self-report question, among the transcripts that deny", "",
          "![families after the question, among deniers](after_question_deniers.png)", ""]
    L += grid_table(template, "Number of (position, family) cells that pass, template positions of all five wordings "
                              f"({len(template)} cells):")
    L += grid_table([r for r in after if r["position"].startswith("q_tok")],
                    f"The same for the question's own tokens ({len(after) - len(template)} cells):")
    hdr = ["| wording | position (token) | family | members | lies | truths | lies that deny | truths that deny | no-pressure truths | unrelated | gap |",
           "|---|---|---|---|---|---|---|---|---|---|---|"]
    lie_side = sorted([r for r in after if r["a"] - r["b"] >= LIST_GAP], key=lambda r: r["b"] - r["a"])
    truth_side = sorted([r for r in after if r["b"] - r["a"] >= LIST_GAP], key=lambda r: r["a"] - r["b"])
    L += [f"### 2.1 More frequent after lies: gap of {100 * LIST_GAP:.0f} points or more ({len(lie_side)} cells)", ""] + hdr
    L += [row_line(r, True) for r in lie_side]
    L += ["", f"### 2.2 More frequent after truths: gap of {100 * LIST_GAP:.0f} points or more ({len(truth_side)} cells)", ""] + hdr
    L += [row_line(r, True) for r in truth_side]
    with open(os.path.join(OUT, "OUTSTANDING.md"), "w") as f:
        f.write("\n".join(L) + "\n")
    print(f"written: {OUT} ({len(rows)} cells; {len(lie_side)} lie-side and {len(truth_side)} truth-side rows after the question)")


if __name__ == "__main__":
    main()
