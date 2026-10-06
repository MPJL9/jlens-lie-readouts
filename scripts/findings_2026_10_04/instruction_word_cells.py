"""How much of the readout the "instruction" and "constraint" words fill (user's question, 2026-10-04, after
piece 6.3 of pieces_of_blog.md). Qwen, J-lens, build split and unrelated chats (the held-out split is never read).

Until now the count was "transcripts with a list word anywhere in the band's readout". Here every readout cell is
counted. A transcript's readout at one token has 16 cells per layer (the top 16 tokens), so 384 cells over the 24
band layers (35 to 58) and 1,024 over all 64 layers.

  A. At the newline after the self-report question, per wording and class: transcripts with one or more cells,
     cells held by the two lists out of all cells, and band layers with a list word.
  B. Under Q7 at that newline, layer by layer over all 64 layers.
  C. Under Q7, at every token of the self-report round: the share of band cells held by the two lists.
  D. Under Q7 at that newline: the rank of the list words inside the top 16, and the single tokens.

Run from the project root:
python3 scripts/findings_2026_10_04/instruction_word_cells.py > analysis/findings_2026_10_04/instruction_word_cells.md"""
import collections
import os
import re
import sys

import numpy as np

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
import common as C  # noqa: E402
import presence as P  # noqa: E402
from frequency_tables import part_positions  # noqa: E402
from presence_index import keep, read_ids  # noqa: E402

M = "qwen3.6-27b"
SHORT = {"Q1_bare": "Q1", "Q2_after": "Q2", "Q6_factual": "Q6", "Q7_ab": "Q7", "Q9_dyl": "Q9"}
CLASSES = [("lies", "lie"), ("truths", "truth"), ("no-pressure truths", "np_truth"), ("unrelated", "unrelated")]
INSTRUCTION = r"(?i)instruct(ion|ions|ed|ing|s)?|directives?|mandat(e|ed|es)"
CONSTRAINT = r"(?i)constraints?|constrained|restrictions?"
ZH = {"instruction": ("指令", "指示"), "constraint": ("约束", "限制")}
NEWLINE = "preans_slot1"


def cls_of(e):
    if e["set"] == "scenario":
        return e["label"]
    if e["set"] == "nopressure":
        return "np_truth" if e["label"] == "truth" else "np_lie"
    return "unrelated"


def main():
    man, vocab = C.load_manifest(M), C.load_vocab(M)
    layers, (lo, hi) = man["layers"], C.BANDS[M]
    band = np.array([lo <= l <= hi for l in layers])
    ents = [e for e in man["transcripts"] if keep(e)]
    assert not any(e["split"] == "heldout" for e in ents if not e["set"].startswith("unrelated"))
    cls = np.array([cls_of(e) for e in ents])
    lists = {"instruction": np.array([bool(re.fullmatch(INSTRUCTION, t.strip())) or t.strip() in ZH["instruction"] for t in vocab]),
             "constraint": np.array([bool(re.fullmatch(CONSTRAINT, t.strip())) or t.strip() in ZH["constraint"] for t in vocab])}
    lists["either list"] = lists["instruction"] | lists["constraint"]

    # hits[w][name] : [transcripts, 64 layers, 16] bool at the newline; prof[name] : {position: [transcripts] band cells} under Q7
    hits = {w: {k: np.zeros((len(ents), len(layers), 16), bool) for k in lists} for w in C.WORDINGS}
    prof = collections.defaultdict(lambda: np.full(len(ents), np.nan))
    tokens_at, tok_cells = {}, collections.Counter()
    for i, e in enumerate(ents):
        for w in C.WORDINGS:
            h, ids = read_ids(M, e, w)
            pp = part_positions(h)
            block = np.asarray(ids["J"][:, pp[NEWLINE]])                 # [64 layers, 16]
            for k, mask in lists.items():
                hits[w][k][i] = mask[block]
            if w == "Q7_ab":
                if cls[i] in ("lie", "truth"):
                    for t in block[band][lists["either list"][block[band]]].tolist():
                        tok_cells[t] += 1
                for name, p in pp.items():
                    if name.startswith("ans_tok") or (name.startswith("postans") and not h.get("answer_finished", True)):
                        continue
                    prof[name][i] = lists["either list"][np.asarray(ids["J"][band, p])].sum()
                    tokens_at.setdefault(name, h["tokens"][p])

    print("# How much of the readout the instruction and constraint words fill\n")
    print("Written by `scripts/findings_2026_10_04/instruction_word_cells.py`. Qwen, J-lens, build split and unrelated chats, in-sample. "
          "A readout has 16 cells per layer: 384 over the band (layers 35 to 58), 1,024 over all 64 layers.\n")
    for k in ("instruction", "constraint"):
        print(f"- `{k}` ({int(lists[k].sum())} tokens): " + ", ".join(repr(vocab[t]) for t in np.flatnonzero(lists[k])))

    print("\n## A. At the newline after the self-report question, per wording\n")
    print("Each cell: transcripts with one or more list cells in the band / transcripts; then the list's cells out of all band cells of "
          "the class (transcripts x 384), with the share; then the mean number of band layers (of 24) that hold a list word.\n")
    for k in lists:
        print(f"**`{k}`**\n")
        print("| wording | " + " | ".join(n for n, _ in CLASSES) + " |")
        print("|---|---|---|---|---|")
        for w in C.WORDINGS:
            row = []
            for _, c in CLASSES:
                x = hits[w][k][cls == c][:, band]                          # [n, 24, 16]
                n, cells = len(x), int(x.sum())
                row.append(f"{int(x.any((1, 2)).sum())}/{n}; {cells:,}/{n * 384:,} ({100 * cells / (n * 384):.1f}%); {x.any(2).sum(1).mean():.1f} layers")
            print(f"| {SHORT[w]} | " + " | ".join(row) + " |")
        print()
    print("The same over all 64 layers (cells out of transcripts x 1,024), `either list`:\n")
    print("| wording | " + " | ".join(n for n, _ in CLASSES) + " |")
    print("|---|---|---|---|---|")
    for w in C.WORDINGS:
        row = []
        for _, c in CLASSES:
            x = hits[w]["either list"][cls == c]
            row.append(f"{int(x.any((1, 2)).sum())}/{len(x)}; {int(x.sum()):,}/{len(x) * 1024:,} ({100 * x.sum() / (len(x) * 1024):.1f}%)")
        print(f"| {SHORT[w]} | " + " | ".join(row) + " |")

    print("\n## B. Under Q7 at that newline, layer by layer (`either list`)\n")
    print("Share of transcripts with a list word in the layer's top 16, and in brackets the mean number of the 16 cells the lists hold "
          "(over all transcripts of the class). Layers where no class reaches 2% are left out. The band is layers 35 to 58.\n")
    print("| layer | " + " | ".join(n for n, _ in CLASSES) + " |")
    print("|---|---|---|---|---|")
    x = hits["Q7_ab"]["either list"]
    for li, l in enumerate(layers):
        sh = [x[cls == c][:, li].any(1).mean() for _, c in CLASSES]
        if max(sh) < 0.02:
            continue
        print(f"| {l}{'' if band[li] else ' (outside the band)'} | " + " | ".join(f"{100 * s:.0f}% ({x[cls == c][:, li].sum(1).mean():.1f})" for s, (_, c) in zip(sh, CLASSES)) + " |")

    print("\n## C. Under Q7, at every token of the self-report round (`either list`)\n")
    print("Share of the band's cells held by the two lists, and in brackets the transcripts with one or more such cells. Tokens where no "
          "class reaches 0.5% of cells are left out. The answer's own tokens are not counted.\n")
    print("| position | token | " + " | ".join(n for n, _ in CLASSES) + " |")
    print("|---|---|---|---|---|---|")
    for name in sorted(prof, key=P.position_key):
        v, row, top = prof[name], [], 0.0
        for _, c in CLASSES:
            y = v[(cls == c) & ~np.isnan(v)]
            share = y.sum() / (len(y) * 384) if len(y) else 0.0
            top = max(top, share)
            row.append(f"{100 * share:.1f}% ({int((y > 0).sum())}/{len(y)})")
        if top >= 0.005:
            print(f"| {name} | `{P.tok(tokens_at[name])}` | " + " | ".join(row) + " |")

    print("\n## D. Under Q7 at that newline: ranks and single tokens (band layers)\n")
    x = hits["Q7_ab"]["either list"][:, band]
    print("Where in the top 16 the list words sit (rank 1 is the token the lens rates highest). Cells of the lists by rank group, per class:\n")
    print("| class | all list cells | rank 1 | ranks 2 to 4 | ranks 5 to 8 | ranks 9 to 16 | transcripts where a list word is rank 1 at one or more band layers |")
    print("|---|---|---|---|---|---|---|")
    for n, c in CLASSES:
        y = x[cls == c]
        tot = int(y.sum())
        g = [int(y[:, :, a:b].sum()) for a, b in ((0, 1), (1, 4), (4, 8), (8, 16))]
        print(f"| {n} | {tot:,} | " + " | ".join(f"{v:,} ({100 * v / max(1, tot):.0f}%)" for v in g) + f" | {int(y[:, :, 0].any(1).sum())}/{len(y)} |")
    scen = int(np.isin(cls, ["lie", "truth"]).sum())
    print(f"\nThe single tokens, pressured transcripts (lies and truths, {scen}): band cells held, and the mean per transcript:\n")
    for t, n in tok_cells.most_common(20):
        print(f"- `{P.tok(vocab[t])}`: {n:,} cells ({n / scen:.1f} per transcript)")


if __name__ == "__main__":
    main()
