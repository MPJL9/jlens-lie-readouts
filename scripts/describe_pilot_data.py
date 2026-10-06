#!/usr/bin/env python3
"""Pilot Step 0: write DATA_pilot.md, the description of the pilot transcripts, labels and exports
in data/ (superseded by scripts/describe_data.py for the new runs).

Counts only; no readout content and no lie/truth comparison of readouts. Two checks of the
position map are included:
  - the template tokens found at each position group, per export;
  - post-response readouts are the same across wordings (they come before the question),
    and pre-response readouts are the same for a lie and a truth of one scenario (they come
    before the response is sampled).

Usage: python3 scripts/describe_pilot_data.py      (reads data/, writes DATA_pilot.md)
"""
import collections
import json
import os
import statistics
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common import (DATA, PILOT_MODELS, ROOT, WORDINGS, pilot_item, pilot_items_for, pilot_labels,  # noqa: E402
                    positions, read_jsonl)  # noqa: E402

GROUPS = ["preresp_slot", "postresp_slot", "q_tok", "preans_slot", "think_slot", "postans_slot"]
ANSWER_WORD = {"yes": "admit", "no": "deny", "other": "other"}


def group_of(name):
    for g in GROUPS:
        if name.startswith(g):
            return g
    return None


def funnel(model, reg):
    scen = [s for s in read_jsonl(os.path.join(DATA, "source", "mask_scenarios.jsonl"))
            if s["id"].startswith("mask_provided_facts")]
    beliefs = {r["id"]: r for r in read_jsonl(os.path.join(DATA, "source", "beliefs", reg["beliefs"]))}
    resolved = sum(1 for s in scen if beliefs.get(s["id"], {}).get("honest_answer") is not None)
    trans = [t for t in read_jsonl(os.path.join(DATA, "source", reg["run"], "transcripts.jsonl"))
             if t["fact_id"].startswith("mask_provided_facts")]
    mech = collections.Counter(t["condition"] for t in trans)
    labels = pilot_labels(model)
    dropped = read_jsonl(os.path.join(DATA, "labels", model + "_dropped.jsonl"))
    lab = collections.Counter(r["label"] for r in labels.values())
    flips = collections.Counter((r["mechanical"], r["label"]) for r in labels.values())
    by_sc = collections.defaultdict(set)
    for r in labels.values():
        by_sc[r["scenario"]].add(r["label"])
    return dict(
        scenarios=len(scen), resolved=resolved,
        with_sample=len({t["fact_id"] for t in trans}), kept=len(trans),
        mech_lie=mech["lie"], mech_truth=mech["truth"],
        dropped=collections.Counter(r["label"] for r in dropped),
        lie=lab["lie"], truth=lab["truth"], labelled_scenarios=len(by_sc),
        both=sum(len(v) == 2 for v in by_sc.values()),
        t2l=flips[("truth", "lie")], l2t=flips[("lie", "truth")])


def main():
    out = []
    w = out.append
    w("# Data description\n")
    w("Written by `scripts/describe_pilot_data.py` from `data/` (built by `scripts/setup_data.py`). "
      "Regenerate rather than edit.\n")
    w("## Where the files are\n")
    w("- `data/source/`: read-only links to the source runs (transcripts, judge verdicts, "
      "honest-answer caches, scenario file) in `../J-lens_lie_detector/`.")
    w("- `data/labels/<model>.jsonl`: one row per labelled transcript. `label` is the judge "
      "verdict (the label used everywhere). `mechanical` is the first-pass label.")
    w("- `data/exports/<slug>/`: top-16 J-lens and logit-lens readouts at every saved layer and "
      "position. The manifest lists only labelled provided_facts transcripts and adds `label`.")
    w("- Residual streams (cluster only): `/scratch/liucfe/jlens_lie/runs/<run>/cache/<seq_id>.pt`, "
      "bf16 `[layers, positions, d_model]`, from the last user-prompt token onward. The local "
      "`cache/` folders are empty.\n")

    # ---- funnel
    w("## How many transcripts survive each step\n")
    w("| model | scenarios | honest answer found | ≥1 sample opens with Yes/No | kept transcripts (mechanical lie / truth) | "
      "judge: no usable verdict | **lies** | **truths** | scenarios labelled | scenarios with both | mechanical truth → judge lie | mechanical lie → judge truth |")
    w("|---|---|---|---|---|---|---|---|---|---|---|---|")
    for model, reg in PILOT_MODELS.items():
        f = funnel(model, reg)
        drop = ", ".join(f"{k} {v}" for k, v in f["dropped"].items()) or "0"
        w(f"| {model} | {f['scenarios']} | {f['resolved']} | {f['with_sample']} | {f['kept']} "
          f"({f['mech_lie']} / {f['mech_truth']}) | {drop} | **{f['lie']}** | **{f['truth']}** | "
          f"{f['labelled_scenarios']} | {f['both']} | {f['t2l']} | {f['l2t']} |")
    w("\nA scenario gives at most one lie and one truth. \"Scenarios with both\" have one of each; "
      "at pre-response positions those two transcripts are identical.\n")

    # ---- answer polarity and response length
    w("## Opening word of the response, and response length\n")
    w("The opening word is what the mechanical label read. Length is in tokens of the model's "
      "own tokenizer. Gemma and Qwen responses were generated with a limit of 48 new tokens, so a "
      "response at 48 tokens was cut off, usually mid-sentence. gpt-oss had a limit of 1,024 new "
      "tokens, shared with its reasoning passage.\n")
    w("| model | lies opening \"No\" | truths opening \"No\" | response length, lies (median, min-max) | truths | lies cut off at 48 | truths cut off at 48 |")
    w("|---|---|---|---|---|---|---|")
    for model in PILOT_MODELS:
        labels = pilot_labels(model)
        slug, items = pilot_items_for(model, "Q1_bare")
        lens = collections.defaultdict(list)
        for it in items:
            d = pilot_item(slug, it["seq_id"])
            r = next(s for s in d["segments"] if s["name"] == "response")
            lens[it["label"]].append(r["end"] - r["start"])
        pol = {}
        for side in ("lie", "truth"):
            rows = [r for r in labels.values() if r["label"] == side]
            pol[side] = f"{sum(r['answer_said'] == 'no' for r in rows)} / {len(rows)}"
        ln = {s: f"{statistics.median(v):.0f} ({min(v)}-{max(v)})" for s, v in lens.items()}
        cut = {s: (f"{sum(n >= 48 for n in v)} / {len(v)}" if not model.startswith("gpt-oss") else "n/a")
               for s, v in lens.items()}
        w(f"| {model} | {pol['lie']} | {pol['truth']} | {ln['lie']} | {ln['truth']} | {cut['lie']} | {cut['truth']} |")
    w("")

    # ---- self-report answers (Qwen)
    w("## Qwen3.6-27B: self-report answers per wording\n")
    w("Admit = \"yes…\" (Q7: \"A…\"); deny = \"no…\" (Q7: \"B…\"). The denial cell of a wording "
      "is its \"lies deny\" and \"truths deny\" columns.\n")
    w("| wording | lies admit | lies deny | lies other | truths admit | truths deny | truths other |")
    w("|---|---|---|---|---|---|---|")
    for wd in WORDINGS:
        _, items = pilot_items_for("qwen3.6-27b", wd)
        c = collections.Counter((it["label"], it["answer_label"]) for it in items)
        w(f"| {wd} | " + " | ".join(str(c[(s, a)]) for s in ("lie", "truth") for a in ("yes", "no", "other")) + " |")
    w("")

    # ---- template tokens per position group
    w("## Tokens at each position group (checks the position map)\n")
    w("Each cell lists the token sequence found at that group and how many sequences show it. "
      "One sequence per cell means the template is the same for every transcript.\n")
    for model, reg in PILOT_MODELS.items():
        w(f"### {model}\n")
        w("| export | wording | group | tokens (count of sequences) |")
        w("|---|---|---|---|")
        for postans in (False, True):
            mapping = reg.get("postans", {}) if postans else reg["exports"]
            for wd in WORDINGS:
                if wd not in mapping:
                    continue
                slug, items = pilot_items_for(model, wd, postans=postans)
                seen = collections.defaultdict(collections.Counter)
                for it in items:
                    d = pilot_item(slug, it["seq_id"])
                    pm = positions(d)
                    by_g = collections.defaultdict(list)
                    for name, p in pm.items():
                        g = group_of(name)
                        if g:
                            by_g[g].append((int(name[len(g):]), d["tokens"][p]))
                    for g, toks in by_g.items():
                        seen[g][tuple(t for _, t in sorted(toks))] += 1
                groups = ["postans_slot"] if postans else [g for g in GROUPS if g != "postans_slot"]
                for g in groups:
                    if g not in seen:
                        continue
                    cells = []
                    for seq, n in seen[g].most_common(3):
                        s = " ".join(json.dumps(t, ensure_ascii=False) for t in seq)
                        if g == "q_tok":
                            s = f"{len(seq)} tokens"
                        cells.append(f"{s} ({n})")
                    more = f" … +{len(seen[g]) - 3} more" if len(seen[g]) > 3 else ""
                    cell = "; ".join(cells).replace("|", "\\|") + more
                    w(f"| {slug} | {wd} | {g} | {cell} |")
        w("")

    # ---- identity checks
    w("## Checks on two properties the plan relies on (Qwen3.6-27B, J-lens, all layers)\n")
    labels = pilot_labels("qwen3.6-27b")
    slug_q, items_q1 = pilot_items_for("qwen3.6-27b", "Q1_bare")
    other = {wd: dict((it["fact_id"] + "|" + it["condition"], it) for it in pilot_items_for("qwen3.6-27b", wd)[1])
             for wd in ("Q2_after", "Q9_dyl")}

    def slot_sets(d, prefix):
        pm = positions(d)
        return {n: [frozenset(t for t, _ in d["readout"]["J"][li][p]) for li in range(len(d["layers"]))]
                for n, p in pm.items() if n.startswith(prefix)}

    same, total = collections.Counter(), collections.Counter()
    q1_cache = {}
    for it in items_q1:
        d1 = pilot_item(slug_q, it["seq_id"])
        a = slot_sets(d1, "postresp_slot")
        q1_cache[it["fact_id"] + "|" + it["condition"]] = (it, slot_sets(d1, "preresp_slot"))
        for wd, idx in other.items():
            o = idx.get(it["fact_id"] + "|" + it["condition"])
            if o is None:
                continue
            b = slot_sets(pilot_item(pilot_items_for("qwen3.6-27b", wd)[0], o["seq_id"]), "postresp_slot")
            for n in a:
                for x, y in zip(a[n], b.get(n, [])):
                    total[wd] += 1
                    same[wd] += x == y
    w("1. **Post-response readouts across wordings.** Share of (transcript, slot, layer) cells "
      "whose top-16 set under Q1 equals the set under another wording:")
    for wd in other:
        w(f"   - Q1 vs {wd}: {same[wd]} / {total[wd]} ({same[wd] / max(1, total[wd]):.1%})")
    by_sc = collections.defaultdict(list)
    for key, (it, sets) in q1_cache.items():
        by_sc[it["fact_id"]].append(sets)
    s2 = t2 = 0
    for sc, lst in by_sc.items():
        if len(lst) == 2:
            for n in lst[0]:
                for x, y in zip(lst[0][n], lst[1].get(n, [])):
                    t2 += 1
                    s2 += x == y
    w("2. **Pre-response readouts within a scenario.** For scenarios with both a lie and a truth, "
      f"share of (slot, layer) cells whose top-16 set is the same for the two: {s2} / {t2} "
      f"({s2 / max(1, t2):.1%}).")
    w("\nSmall differences can come from rounding in separate forward passes of different lengths.\n")

    with open(os.path.join(ROOT, "DATA_pilot.md"), "w") as f:
        f.write("\n".join(out) + "\n")
    print("wrote DATA_pilot.md")


if __name__ == "__main__":
    main()
