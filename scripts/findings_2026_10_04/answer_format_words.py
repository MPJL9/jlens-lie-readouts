"""The user's finding, rechecked on 2026-10-04: after the self-report question, `yes`, 是, 是的 and 是否 are in
the readout whatever the model then answers. All four models, J-lens, each model's band, presence index
(build split and unrelated chats only; the held-out split is never read).

Each word is counted on its own (English and Chinese are never pooled); the member tokens are printed first.
For every wording and every position from the first question token to the last token before the answer:
the share of transcripts with the word in the band's readout, among the pressured transcripts that then
admit, among those that then deny, and among the unrelated chats. Positions where no word reaches 20% in
any group are left out. The post-response slots (before any question exists) are printed as a control.

Run from the project root: python3 scripts/findings_2026_10_04/answer_format_words.py [--models ...]"""
import argparse
import os
import sys

import numpy as np

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
import common as C  # noqa: E402
import presence as P  # noqa: E402

SHORT = {"Q1_bare": "Q1", "Q2_after": "Q2", "Q6_factual": "Q6", "Q7_ab": "Q7", "Q9_dyl": "Q9"}
WORDS = {"yes": lambda t: t.strip().lower() == "yes", "no": lambda t: t.strip().lower() == "no",
         "是": lambda t: t.strip() == "是", "是的": lambda t: t.strip() == "是的", "是否": lambda t: t.strip() == "是否",
         "否": lambda t: t.strip() == "否"}


def token_at(model, d, part, pos):
    """The text token at a position, read from one transcript's header."""
    for ti in d["have"][part][pos][:1]:
        t = d["transcripts"][ti]
        h, _ = C.read_part(model, dict(set=t["set"], tid=t["tid"]), part, readouts=False)
        item = {"tokens": h["tokens"], "segments": h["segments"]}
        return P.tok(h["tokens"][C.positions(item)[pos]])
    return "?"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--models", nargs="+", default=C.MODELS)
    ap.add_argument("--floor", type=float, default=0.2)
    args = ap.parse_args()
    for m in args.models:
        d, vocab = P.load(m, "J"), C.load_vocab(m)
        G = {k: [i for i, t in enumerate(vocab) if f(t)] for k, f in WORDS.items()}
        scen, unrel = np.isin(d["cls"], ["lie", "truth"]), d["cls"] == "unrelated"
        print(f"\n\n## {m} (band {d['band'][0]} to {d['band'][1]}; {int(scen.sum())} pressured transcripts, {int(unrel.sum())} unrelated chats)\n")
        for k, v in G.items():
            print(f"- `{k}`: " + ", ".join(repr(vocab[i]) for i in v))
        print("\nControl, before any question (post-response slots; pressured | unrelated):")
        for pos in P.positions(d, "prefix"):
            have = P.have_mask(d, "prefix", pos)
            cells = []
            for k in G:
                pm = P.present_mask(d, "prefix", pos, G[k])
                cells.append(f"{k} {int((pm & have & scen).sum())}/{int((have & scen).sum())} | {int((pm & have & unrel).sum())}/{int((have & unrel).sum())}")
            print(f"- {pos} ({token_at(m, d, 'prefix', pos)}): " + "; ".join(cells))
        for w in C.WORDINGS:
            ans = P.answer(d, w)
            a, dn = scen & (ans == "admit"), scen & (ans == "deny")
            print(f"\n**{SHORT[w]}** ({int(a.sum())} admit, {int(dn.sum())} deny; each cell: admit | deny | unrelated)\n")
            print("| position | token | " + " | ".join(f"`{k}`" for k in G) + " |")
            print("|" + "---|" * (2 + len(G)))
            for pos in P.positions(d, w):
                if pos.startswith("postans"):
                    continue
                have = P.have_mask(d, w, pos)
                row, top = [], 0.0
                for k in G:
                    pm = P.present_mask(d, w, pos, G[k])
                    sh = []
                    for sel in (a, dn, unrel):
                        n, c = int((have & sel).sum()), int((pm & have & sel).sum())
                        sh.append(f"{c}/{n} ({100 * c / n:.0f}%)" if n else "–")
                        top = max(top, c / n if n else 0)
                    row.append(" \\| ".join(sh))
                if top >= args.floor:
                    print(f"| {pos} | {token_at(m, d, w, pos)} | " + " | ".join(row) + " |")


if __name__ == "__main__":
    main()
