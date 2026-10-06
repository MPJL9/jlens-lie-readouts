#!/usr/bin/env python3
"""PLAN.md Section 4.2: the numbers and the readout dumps behind the readout suggestion for one
layer band per model. No labels are read or written.

Transcripts: 10 per model from the scenario set, build split, chosen by scenario ID: the kept
scenario IDs are sorted, 10 are drawn with seed 0, and for each the transcript with the lowest
sample index k is taken. The Q1_bare wording is used (the prefix is the same under every wording).

Per layer, three numbers, each over three position groups (template positions = the turn
boundaries and the question tokens; response tokens; self-report answer tokens), J-lens top 16:
  readable  share of readout tokens that are words: one optional leading space, then 3+ letters
            of any script (the viewer's rule)
  next      share of positions whose top readout token is the actual next token
  overlap   mean Jaccard overlap between the top-16 sets at a position and the next position
The same numbers are given for the other lens as a comparison (the "LL_" or "J_" columns).

--lens J (default) or LL chooses the lens the dumps and the figure show and the lens whose
columns come first in the .md; the .json always holds both lenses.

Outputs (for --lens LL the names carry "_LL": readout_stats_LL_<slug>.md / .png, readouts_LL/):
  analysis/band/readout_stats_<slug>.json / .md   the numbers per layer
  analysis/band/readout_stats_<slug>.png          the three curves per group
  analysis/band/readouts/<slug>/<n>_<scenario>.md one file per transcript: the conversation
      (system prompt, user prompt, response; no label, stance or quote), then for a fixed set
      of positions one line per layer with the top-5 J-lens tokens and the top token's
      probability. Positions: the last user-prompt token, three response tokens at 25/50/75%
      of the response, every post-response slot, the last pre-answer slot, and the first
      post-answer slot.

Usage: python3 scripts/band_readout_stats.py [--models m1 m2] [--lens J|LL]
"""
from __future__ import annotations

import argparse
import json
import os
import random
import re
import sys

import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import common as C  # noqa: E402

OUT = os.path.join(C.ROOT, "analysis", "band")
READABLE = re.compile(r"^\s?[^\W\d_]{3,}$")
WORDING = "Q1_bare"
N_TRANSCRIPTS = 10
SHOW_TOP = 5
GROUPS = ["template", "response", "answer"]
LENS_NAME = {"J": "J-lens", "LL": "logit lens"}


def suffix(lens):
    return "" if lens == "J" else "_LL"


def choose_transcripts(model, n=N_TRANSCRIPTS, seed=0):
    """n build-split scenario transcripts, chosen by scenario ID (no label read)."""
    man = C.load_manifest(model)
    build = C.entries(man, set="scenario", split="build")
    by_item = {}
    for e in build:
        by_item.setdefault(e["item_id"], []).append(e)
    ids = sorted(by_item)
    chosen = random.Random(seed).sample(ids, n)
    return man, [min(by_item[i], key=lambda e: e["k"]) for i in chosen]


def group_of(name):
    if name.startswith("resp_tok"):
        return "response"
    if name.startswith("ans_tok"):
        return "answer"
    return "template"


def disp(s):
    """Token string for the dumps: newlines and leading spaces made visible."""
    s = s.replace("\n", "\\n").replace("\t", "\\t")
    m = re.match(r"^( +)", s)
    if m:
        s = "␣" * len(m.group(1)) + s[len(m.group(1)):]
    return s


def stats_for(item, vocab, lens):
    """{group: {readable: [per layer], next: [...], overlap: [...], n_positions}}."""
    pos = C.positions(item)
    ids = item["ids_top"][lens]                      # [layers, T, K]
    T, K = item["T"], item["top_k"]
    readable_tok = np.array([bool(READABLE.match(s)) for s in vocab], dtype=bool)
    out = {}
    for g in GROUPS:
        ps = sorted(p for name, p in pos.items() if group_of(name) == g)
        ps = [p for p in ps if p + 1 < T]            # the next token must exist
        if not ps:
            continue
        top = ids[:, ps, :]                          # [layers, n, K]
        readable = readable_tok[top].mean(axis=(1, 2))
        nxt = np.array([item["ids"][p + 1] for p in ps])
        next_share = (top[:, :, 0] == nxt[None, :]).mean(axis=1)
        overlap = []
        for li in range(len(item["layers"])):
            js = []
            for p in ps:
                a, b = set(ids[li, p].tolist()), set(ids[li, p + 1].tolist())
                js.append(len(a & b) / len(a | b))
            overlap.append(float(np.mean(js)))
        out[g] = {"readable": readable.tolist(), "next": next_share.tolist(), "overlap": overlap, "n_positions": len(ps)}
    return out


def dump_positions(item):
    """[(label, position)] shown in the transcript dump."""
    pos = C.positions(item)
    show = []
    u = next(s for s in item["segments"] if s["name"] == "user_prompt")
    show.append(("user_prompt_last", u["end"] - 1))
    resp = sorted(p for n, p in pos.items() if n.startswith("resp_tok"))
    for frac in (0.25, 0.5, 0.75):
        p = resp[min(len(resp) - 1, int(frac * len(resp)))]
        show.append((f"resp_tok{resp.index(p)} ({int(frac * 100)}% of the response)", p))
    for name in sorted((n for n in pos if n.startswith("postresp_slot")), key=lambda n: pos[n]):
        show.append((name, pos[name]))
    pre = sorted((n for n in pos if n.startswith("preans_slot")), key=lambda n: pos[n])
    if pre:
        show.append((pre[-1], pos[pre[-1]]))
    if "postans_slot0" in pos:
        show.append(("postans_slot0", pos["postans_slot0"]))
    return show


def write_dump(model, n, entry, item, vocab, path, lens="J"):
    name = LENS_NAME[lens]
    lines = [f"# {model}: transcript {n} of {N_TRANSCRIPTS} for the band check ({name})", "",
             f"Scenario `{entry['item_id']}`, sample k = {entry['k']}, wording {WORDING}. No label is shown.", "",
             "## Conversation", "", "**System prompt**", "", "```", item["prefix"]["system"].strip(), "```", "",
             "**User prompt**", "", "```", item["prefix"]["user_prompt"].strip(), "```", "",
             "**Model response**", "", "```", item["prefix"]["response"].strip(), "```", "",
             f"**Self-report question** ({WORDING})", "", "```", item["part"]["question"].strip(), "```", "",
             f"## {name} readouts", "",
             f"One block per position. Each line: layer | top-5 {name} tokens (most probable first) | probability of the top token.",
             "`␣` marks a leading space; `\\n` a newline. The **actual next token** is given for each position.", ""]
    for label, p in dump_positions(item):
        nxt = disp(item["tokens"][p + 1]) if p + 1 < item["T"] else "(end)"
        lines += [f"### {label}: token `{disp(item['tokens'][p])}` (position {p}); actual next token `{nxt}`", "", "```"]
        for li, layer in enumerate(item["layers"]):
            toks = [disp(vocab[int(t)]) for t in item["ids_top"][lens][li, p, :SHOW_TOP]]
            p1 = float(item["p"][lens][li, p, 0])
            lines.append(f"L{layer:02d} | {' · '.join(toks)} | {p1:.2f}")
        lines += ["```", ""]
    with open(path, "w") as f:
        f.write("\n".join(lines))


def plot(model, layers, stats, path, lens="J"):
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    colors = {"template": "#2a78d6", "response": "#eb6834", "answer": "#1baf7a"}
    fig, axes = plt.subplots(1, 3, figsize=(15, 4), sharex=True)
    for ax, key, title in zip(axes, ["readable", "next", "overlap"],
                              ["share of readout tokens that are words (3+ letters)",
                               "share of positions whose top token is the next token",
                               "overlap of readouts at neighbouring positions"]):
        for g in GROUPS:
            if g in stats[lens]:
                ax.plot(layers, stats[lens][g][key], color=colors[g], lw=2, marker="o", ms=4, label=f"{g} (n = {stats[lens][g]['n_positions']})")
        ax.set_title(title, fontsize=9)
        ax.set_xlabel("layer")
        ax.set_ylim(0, 1.02)
        ax.grid(alpha=0.25, lw=0.5)
        for sp in ("top", "right"):
            ax.spines[sp].set_visible(False)
    axes[0].legend(fontsize=8, loc="upper left")
    fig.suptitle(f"{model}: {LENS_NAME[lens]} readout statistics over {N_TRANSCRIPTS} transcripts", fontsize=10)
    fig.savefig(path, dpi=130, bbox_inches="tight")
    plt.close(fig)


def run(model, lens="J"):
    man, chosen = choose_transcripts(model)
    vocab = C.load_vocab(model)
    layers = man["layers"]
    per_lens = {l: {g: {"readable": [], "next": [], "overlap": [], "n_positions": 0} for g in GROUPS} for l in C.LENSES}
    dump_dir = os.path.join(OUT, "readouts" + suffix(lens), C.slug(model))
    os.makedirs(dump_dir, exist_ok=True)
    for n, e in enumerate(chosen, 1):
        item = C.load_item(model, e, WORDING)
        for l in C.LENSES:
            for g, s in stats_for(item, vocab, l).items():
                acc = per_lens[l][g]
                for key in ("readable", "next", "overlap"):
                    acc[key].append((np.array(s[key]), s["n_positions"]))
                acc["n_positions"] += s["n_positions"]
        write_dump(model, n, e, item, vocab, os.path.join(dump_dir, f"{n:02d}_{e['item_id'].replace('mask_provided_facts_', '')}.md"), lens)
        print(f"{model}: transcript {n} ({e['item_id']}) T = {item['T']}", flush=True)
    stats = {}
    for l in C.LENSES:
        stats[l] = {}
        for g in GROUPS:
            acc = per_lens[l][g]
            if acc["n_positions"] == 0:
                continue
            stats[l][g] = {"n_positions": acc["n_positions"]}
            for key in ("readable", "next", "overlap"):
                stats[l][g][key] = (sum(v * n for v, n in acc[key]) / acc["n_positions"]).round(4).tolist()
    result = {"model": model, "layers": layers, "wording": WORDING, "seed": 0,
              "transcripts": [{"tid": e["tid"], "item_id": e["item_id"], "k": e["k"]} for e in chosen],
              "stats": stats}
    with open(os.path.join(OUT, f"readout_stats_{C.slug(model)}.json"), "w") as f:
        json.dump(result, f)
    write_md(result, os.path.join(OUT, f"readout_stats{suffix(lens)}_{C.slug(model)}.md"), lens)
    plot(model, layers, stats, os.path.join(OUT, f"readout_stats{suffix(lens)}_{C.slug(model)}.png"), lens)
    return result


def write_md(r, path, lens="J"):
    s = r["stats"]
    other = "LL" if lens == "J" else "J"
    name, oname = LENS_NAME[lens], LENS_NAME[other]
    lines = [f"# {r['model']}: {name} readout statistics per layer (PLAN.md Section 4.2)", "",
             f"Written by `scripts/band_readout_stats.py`. {N_TRANSCRIPTS} build-split scenario transcripts chosen by",
             f"scenario ID (seed 0), wording {r['wording']}. No labels were read.", "",
             f"Columns ({name}, top 16): readable = share of readout tokens that are words of 3+ letters; next =",
             "share of positions whose top token is the actual next token; overlap = mean Jaccard overlap of",
             f"the top-16 sets at neighbouring positions. {other}_ columns: the same for the {oname}.",
             "Groups: template = turn boundaries and question tokens; response = response tokens; answer =",
             "self-report answer tokens. Positions per group: " +
             ", ".join(f"{g} {s[lens][g]['n_positions']}" for g in GROUPS if g in s[lens]) + ".", ""]
    for g in GROUPS:
        if g not in s[lens]:
            continue
        lines += [f"## {g} positions", "", f"| layer | readable | next | overlap | {other}_readable | {other}_next | {other}_overlap |", "|---|---|---|---|---|---|---|"]
        for i, layer in enumerate(r["layers"]):
            a, b = s[lens][g], s[other][g]
            lines.append(f"| {layer} | {a['readable'][i]:.2f} | {a['next'][i]:.2f} | {a['overlap'][i]:.2f} | "
                         f"{b['readable'][i]:.2f} | {b['next'][i]:.2f} | {b['overlap'][i]:.2f} |")
        lines.append("")
    lines += ["## Transcripts", ""] + [f"- {t['tid']}" for t in r["transcripts"]]
    with open(path, "w") as f:
        f.write("\n".join(lines) + "\n")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--models", nargs="+", default=C.MODELS)
    ap.add_argument("--lens", choices=C.LENSES, default="J")
    args = ap.parse_args()
    os.makedirs(OUT, exist_ok=True)
    for m in args.models:
        run(m, args.lens)


if __name__ == "__main__":
    main()
