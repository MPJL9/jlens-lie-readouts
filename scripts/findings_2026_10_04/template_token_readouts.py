"""What the band's readout holds at each template token after the response: the tokens present in the most
pressured transcripts, with their counts in the four classes. J-lens, each model's band, presence index (build
split and unrelated chats only; the held-out split is never read). "Present" = in the top 16 at one or more band
layers. For piece 5 of pieces_of_blog.md (the neighbouring tokens on Qwen; what gpt-oss's tokens hold).

Run from the project root:
python3 scripts/findings_2026_10_04/template_token_readouts.py > analysis/findings_2026_10_04/template_token_readouts.md"""
import argparse
import os
import sys

import numpy as np

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
import common as C  # noqa: E402
import presence as P  # noqa: E402

NAMES = {"lie": "lies", "truth": "truths", "np_truth": "no-pressure truths", "unrelated": "unrelated"}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--models", nargs="+", default=["qwen3.6-27b", "gemma-3-12b-it", "gemma-3-27b-it", "gpt-oss-20b"])
    ap.add_argument("--top", type=int, default=20)
    args = ap.parse_args()
    print("# The most frequent readout tokens at the template tokens after the response\n")
    print("Written by `scripts/findings_2026_10_04/template_token_readouts.py`. J-lens, each model's band, build split, in-sample. "
          "Sorted by the share of pressured transcripts (lies and truths); cells are transcripts with the token / transcripts.\n")
    for m in args.models:
        d, vocab = P.load(m, "J"), C.load_vocab(m)
        cls, N = d["cls"], len(d["cls"])
        scen = np.isin(cls, ["lie", "truth"])
        print(f"\n## {m} (band {d['band'][0]} to {d['band'][1]})\n")
        for pos in P.positions(d, "prefix"):
            tab, have = d["present"]["prefix"][pos], P.have_mask(d, "prefix", pos)
            rows = []
            for t, (idx, _) in tab.items():
                hit = np.zeros(N, bool)
                hit[idx] = True
                rows.append((int((hit & have & scen).sum()), t, hit))
            rows.sort(key=lambda r: -r[0])
            gap = max(rows, key=lambda r: (r[2] & have & (cls == "lie")).sum() / max(1, (have & (cls == "lie")).sum())
                      - (r[2] & have & (cls == "truth")).sum() / max(1, (have & (cls == "truth")).sum()))
            print(f"**{pos}** ({len(tab)} distinct tokens in the band's readouts)\n")
            print("| token | " + " | ".join(NAMES[c] for c in P.CLASSES) + " |")
            print("|---|---|---|---|---|")
            def cells(hit):
                out = []
                for c in P.CLASSES:
                    n, k = int((have & (cls == c)).sum()), int((hit & have & (cls == c)).sum())
                    out.append(f"{k}/{n} ({100 * k / n:.0f}%)")
                return " | ".join(out)
            for _, t, hit in rows[:args.top]:
                print(f"| `{P.tok(vocab[t])}` | {cells(hit)} |")
            print(f"\nThe token with the largest lie-minus-truth gap here: `{P.tok(vocab[gap[1]])}`: {cells(gap[2])}\n")


if __name__ == "__main__":
    main()
