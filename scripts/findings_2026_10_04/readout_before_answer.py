"""What the J-lens readout holds at the last token before the self-report answer (Qwen: think slot 3, the
blank line after `</think>`), per wording: how much of it is the same whatever the model then answers, how
much changes with the answer, and how the constant part changes with the wording (user, 2026-10-04).

Scenario transcripts of the build split (lies and truths together) that then admit or deny; the unrelated
chats (both sets) are counted next to them. The held-out split is never read. A transcript's readout is the
top-16 tokens at each of the band's layers (35 to 58: 24 x 16 cells).
  constant token          in the readout of 90% or more of the admitters and of 90% or more of the deniers
  answer-following token  its share among admitters and its share among deniers differ by 50 points or more
Reads the exports directly (about two minutes). Run from the project root:
python3 scripts/findings_2026_10_04/readout_before_answer.py [--position think_slot3]"""
import argparse
import collections
import os
import sys

import numpy as np

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
import common as C  # noqa: E402
from frequency_tables import part_positions  # noqa: E402
from presence_index import keep, read_ids  # noqa: E402

M = "qwen3.6-27b"
SHORT = {"Q1_bare": "Q1", "Q2_after": "Q2", "Q6_factual": "Q6", "Q7_ab": "Q7", "Q9_dyl": "Q9"}


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--position", default="think_slot3")
    pos = ap.parse_args().position
    man, vocab = C.load_manifest(M), C.load_vocab(M)
    layers, (lo, hi) = man["layers"], C.BANDS[M]
    lidx = [i for i, l in enumerate(layers) if lo <= l <= hi]
    ents = [e for e in man["transcripts"] if keep(e) and e["set"] in ("scenario", "unrelated", "unrelated_extra")]
    assert not any(e["split"] == "heldout" for e in ents if e["set"] == "scenario")
    cells = len(lidx) * 16
    show = lambda toks: " ".join(repr(vocab[t]) for t in sorted(toks, key=lambda t: vocab[t]))
    const = {}
    for w in C.WORDINGS:
        blocks = {"admit": [], "deny": [], "unrelated": []}
        for e in ents:
            g = "unrelated" if e["set"] != "scenario" else e["wordings"][w]["answer_label"]
            if g in blocks:
                h, ids = read_ids(M, e, w)
                blocks[g].append(np.asarray(ids["J"][lidx, part_positions(h)[pos]]))      # [band layers, 16]
        n = {g: len(b) for g, b in blocks.items()}
        pres = {g: collections.Counter(t for b in bs for t in set(b.ravel().tolist())) for g, bs in blocks.items()}
        top1 = {g: collections.Counter(t for b in bs for t in b[:, 0].tolist()) for g, bs in blocks.items()}
        share = lambda g, t: pres[g][t] / n[g]
        toks = set(pres["admit"]) | set(pres["deny"])
        const[w] = {t for t in toks if share("admit", t) >= 0.9 and share("deny", t) >= 0.9}
        follow = {t for t in toks if abs(share("admit", t) - share("deny", t)) >= 0.5}
        both = blocks["admit"] + blocks["deny"]
        distinct = np.mean([len(set(b.ravel().tolist())) for b in both])
        in_const = np.mean([len(set(b.ravel().tolist()) & const[w]) for b in both])
        in_follow = np.mean([len(set(b.ravel().tolist()) & follow) for b in both])
        cell_const = np.mean([np.isin(b, list(const[w])).mean() for b in both])
        cell_follow = np.mean([np.isin(b, list(follow)).mean() for b in both]) if follow else 0.0
        print(f"\n=== {SHORT[w]} at {pos}: {n['admit']} admit, {n['deny']} deny, {n['unrelated']} unrelated chats")
        print(f"  distinct tokens per transcript {distinct:.0f}; constant {in_const:.0f}; answer-following {in_follow:.1f}")
        print(f"  share of the {cells} readout cells: constant tokens {100 * cell_const:.0f}%, answer-following tokens {100 * cell_follow:.1f}%")
        print("  top-ranked token, share of transcript x layer cells (admit | deny | unrelated):")
        for t, _ in (top1["admit"] + top1["deny"]).most_common(6):
            print(f"    {vocab[t]!r:16}" + " | ".join(f"{100 * top1[g][t] / (n[g] * len(lidx)):3.0f}%" for g in blocks))
        print("  answer-following tokens (admit | deny | unrelated):")
        for t in sorted(follow, key=lambda t: share("admit", t) - share("deny", t)):
            print(f"    {vocab[t]!r:16}" + " | ".join(f"{pres[g][t]}/{n[g]} ({100 * share(g, t):.0f}%)" for g in blocks))
        print("  constant tokens:", show(const[w]))
    yn = const["Q2_after"] & const["Q6_factual"] & const["Q9_dyl"]
    print("\nconstant tokens shared between wordings:")
    for a in C.WORDINGS:
        print(f"  {SHORT[a]} ({len(const[a])}): " + "  ".join(f"{SHORT[b]} {len(const[a] & const[b])}" for b in C.WORDINGS if b != a))
    print("constant under Q2, Q6 and Q9 but not under Q7:", show(yn - const["Q7_ab"]))
    print("constant under Q7 but under none of Q2, Q6, Q9:", show(const["Q7_ab"] - (const["Q2_after"] | const["Q6_factual"] | const["Q9_dyl"])))
    print("constant under all five wordings:", show(set.intersection(*const.values())))


if __name__ == "__main__":
    main()
