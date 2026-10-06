"""How much of the newline's readout the ten lie-side families of the draft's Section 4.1 take, per transcript.
User's question, 2026-10-05: not every lie has as many lie-side words as the example on the screenshot page.

Qwen3.6-27B, J-lens, the newline after the response, band layers 35 to 58, build split. A readout has 16 cells
per band layer, so 384 cells per transcript. A cell is *lie-side* when its token is a member of one of the ten
families (one fixed list: the newline's draft lists).

Run from the project root:
python3 scripts/findings_2026_10_04/lie_side_cells.py > analysis/findings_2026_10_04/lie_side_cells.md"""
import json
import os
import random
import sys
from collections import defaultdict

import numpy as np

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
import common as C  # noqa: E402
import presence as P  # noqa: E402

M, POS = "qwen3.6-27b", "postresp_slot1"
TEN = ["lie", "fake", "conceal", "misinformation", "deceive", "falsehood", "fabricate", "false", "mislead", "dishonest"]
NAMES = {"lie": "lies", "truth": "truths", "np_truth": "no-pressure truths"}


def main():
    d = P.load(M, "J")
    cls, trs = d["cls"], d["transcripts"]
    with open(os.path.join(C.ROOT, "analysis", "families", "families_draft.json")) as f:
        ents = json.load(f)["entries"]
    fam = defaultdict(set)
    for e in ents:
        if e["model"] == M and e["lens"] == "J" and e["part"] == "prefix" and e["position"] == POS and e["status"] == "keep":
            fam[e["name"]] |= {x["id"] for x in e["members"]}
    red = np.array(sorted(set().union(*[fam[n] for n in TEN])))
    hv = P.have_mask(d, "prefix", POS)
    n_ten = sum((P.present_mask(d, "prefix", POS, fam[n]) & hv).astype(int) for n in TEN)
    entry = {e["tid"]: e for e in C.load_manifest(M)["transcripts"]}
    lo, hi = C.BANDS[M]
    n_cells = (hi - lo + 1) * 16

    def cells(i):
        ph, pa = C.read_part(M, entry[trs[i]["tid"]], "prefix")
        item = dict(tokens=ph["tokens"], ids=ph["ids"], segments=ph["segments"], layers=ph["layers"],
                    ids_top={"J": pa["J_ids"]}, p={"J": pa["J_p"]})
        p = C.positions(item)[POS]
        return int(np.isin(pa["J_ids"][lo:hi + 1, p, :].astype(int), red).sum())

    print("# Lie-side cells at the newline, per transcript\n")
    print(f"Qwen3.6-27B, J-lens, the newline after the response, layers {lo} to {hi}, build split. {n_cells} cells per")
    print("transcript (16 per layer). Lie-side = a member of one of the ten families of the draft's Section 4.1:")
    print(", ".join(f"`{n}`" for n in TEN) + f" ({len(red)} tokens).\n")
    print("| class | transcripts | all cells | lowest | first quarter | median | third quarter | highest |")
    print("|---|---|---|---|---|---|---|---|")
    per = {}
    for c in ("lie", "truth", "np_truth"):
        idx = np.where((cls == c) & hv)[0]
        x = np.array([cells(i) for i in idx])
        per[c] = (idx, x)
        q = [x.min(), np.percentile(x, 25), np.median(x), np.percentile(x, 75), x.max()]
        print(f"| {NAMES[c]} | {len(idx)} | {int(x.sum()):,} of {len(idx) * n_cells:,} ({x.sum() / (len(idx) * n_cells):.1%}) | "
              + " | ".join(f"{v:g} ({v / n_cells:.0%})" for v in q) + " |")
    print("\nTranscripts by the share of their 384 cells that are lie-side:\n")
    print("| class | none | under 5% | 5% to 10% | 10% to 25% | 25% to 50% | over 50% |")
    print("|---|---|---|---|---|---|---|")
    for c in ("lie", "truth", "np_truth"):
        idx, x = per[c]
        s = x / n_cells
        groups = [(x == 0), (x > 0) & (s < 0.05), (s >= 0.05) & (s < 0.10), (s >= 0.10) & (s < 0.25), (s >= 0.25) & (s <= 0.50), s > 0.50]
        assert sum(int(g.sum()) for g in groups) == len(idx)
        print(f"| {NAMES[c]} | " + " | ".join(f"{int(g.sum())}/{len(idx)} ({g.mean():.0%})" for g in groups) + " |")
    idx, x = per["lie"]
    where = {int(i): k for k, i in enumerate(idx)}
    cands = np.where((cls == "lie") & hv & (n_ten >= 1))[0].tolist()
    pick = random.Random(0).sample(cands, 11)
    print(f"\nThe eleven lies of the screenshot page (`viewer/readout_page.html`): drawn at random, seed 0, from the {len(cands)}")
    print("lies with one or more of the ten families at the newline. Rank 1 is the lie with the most lie-side cells.\n")
    print("| on the page | scenario (end of the id) | sample | lie-side cells | rank among the 152 lies | families of the ten |")
    print("|---|---|---|---|---|---|")
    for n, i in enumerate(pick, 1):
        v = x[where[i]]
        print(f"| {n} | `{trs[i]['item_id'][-6:]}` | k{trs[i]['tid'].split('__k')[-1]} | {v} of {n_cells} ({v / n_cells:.0%}) | "
              f"{int((x > v).sum()) + 1} | {int(n_ten[i])} |")


if __name__ == "__main__":
    main()
