#!/usr/bin/env python3
"""Step 0: write DATA.md, the description of the new runs' transcripts, labels and exports in
data/cluster/ (pulled by scripts/pull_from_cluster.sh).

Counts only; no readout content and no lie/truth comparison of readouts. Two checks are included:
  - the template tokens found at each position group, per model and wording (checks the
    position map);
  - pre-response readouts are the same for a lie and a truth of one scenario (they come before
    the response is sampled, so only rounding in separate forward passes can differ).

Usage: python3 scripts/describe_data.py      (reads data/cluster/, writes DATA.md)
"""
import collections
import os
import statistics
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common import (HIDING_WORDS, MODELS, ROOT, RUNS, commentary_section, entries, load_item,  # noqa: E402
                    load_manifest, load_summary,
                    positions, read_jsonl, read_part, slug)

GROUPS = ["preresp_slot", "postresp_slot", "q_tok", "preans_slot", "think_slot", "postans_slot"]
SPLITS = ["build", "heldout"]


def group_of(name):
    for g in GROUPS:
        if name.startswith(g):
            return g
    return None


def med_range(xs):
    return f"{statistics.median(xs):.0f} ({min(xs)}-{max(xs)})" if xs else "—"


def judge_errors(model):
    """Distinct samples whose latest current-version first-pass verdict is an error, by kind."""
    latest = {}
    for j in read_jsonl(os.path.join(RUNS, slug(model), "judge.jsonl")):
        if j.get("prompt_version") == "v3":
            latest[j["key"]] = j
    kinds = collections.Counter()
    for j in latest.values():
        if j["verdict"] == "error":
            kinds["refusal" if j.get("reason", "").startswith("refusal") else "other"] += 1
    return kinds


def response_limit(model):
    return sorted({s["max_new_tokens"] for s in read_jsonl(os.path.join(RUNS, slug(model), "samples.jsonl"))})


def main():
    lines = []
    w = lines.append
    mans = {m: load_manifest(m, drop_commentary=False) for m in MODELS}   # the full selection
    sums = {m: load_summary(m) for m in MODELS}

    w("# Data description\n")
    w("Written by `scripts/describe_data.py` from `data/cluster/` (pulled by `scripts/pull_from_cluster.sh`). "
      "Regenerate rather than edit. The pilot's description is in `DATA_pilot.md`. How the data were made: "
      "`PLAN.md` Section 2.\n")

    w("## Where the files are\n")
    w("- `data/cluster/runs/<model>/`: `samples.jsonl` (every sampled response), `judge.jsonl` and "
      "`judge_second.jsonl` (verdicts; only rows with `prompt_version` v3 count), `transcripts.jsonl` (the "
      "selected transcripts with texts, label, quote and `discloses`), `selection_summary.json`, "
      "`sequences.jsonl` (token ids and segments of every forward-pass part).")
    w("- `data/cluster/exports/<model>/`: `manifest.json` (the transcripts, labels and self-report answers), "
      "`vocab.json`, and per transcript `<set>/<tid>/<part>.json` + `.bin`: top-16 J-lens and logit-lens token "
      "ids and probabilities and the Yes - No score, at every layer and every exported position. Part `prefix` "
      "runs from the last user-prompt token to the end of the post-response boundary; each wording part runs "
      "from the question's first token to the end of the post-answer boundary. `scripts/common.py` "
      "(`load_item`) joins the prefix and a wording.")
    w("- Residual streams (cluster only): `/scratch/liucfe/jlens_redo/runs/<model>/cache/<tid>/<part>.pt`, bf16 "
      "`[layers, positions, d_model]`; whole sequences for Qwen3.6-27B, from the last user-prompt token for the "
      "other models.\n")

    w("## Sampling and selection\n")
    w("Scenario set: 8 samples per scenario (sample 0 greedy), plus 8 more for scenarios without a usable lie or "
      "truth. Usable = finished within the token limit, judged lie or truth, and not a lie that also discloses "
      "the truth. A scenario gives at most one lie and one truth (the lowest-numbered usable ones).\n")
    w("| model | response limit (tokens) | scenarios topped up | greedy sample: lie / truth / ambiguous | "
      "round-1 lie rate (temperature samples) | cut off: lies / truths | finished lies that disclose | "
      "scenarios whose only lies disclose |")
    w("|---|---|---|---|---|---|---|---|")
    for m in MODELS:
        sc = sums[m]["scenario"]
        g, cut = sc["greedy_verdicts"], sc["cut_off_samples_by_verdict"]
        w(f"| {m} | {', '.join(map(str, response_limit(m)))} | {sc['topped_up']} | {g.get('lie', 0)} / "
          f"{g.get('truth', 0)} / {g.get('ambiguous', 0)} | {sc['round1_temperature_lie_rate']} | "
          f"{cut.get('lie', 0)} / {cut.get('truth', 0)} | {sc['finished_lies_that_disclose']} | "
          f"{sc['scenarios_whose_only_lies_disclose']} |")
    w("")
    w("| model | scenarios with a lie and a truth | lie only | truth only | none |")
    w("|---|---|---|---|---|")
    for m in MODELS:
        a = sums[m]["scenario"]["scenarios_with"]
        w(f"| {m} | {a.get('both', 0)} | {a.get('lie only', 0)} | {a.get('truth only', 0)} | {a.get('none', 0)} |")
    w("")

    w("## Selected transcripts\n")
    w("Build = 164 scenarios for building families; held-out = 110 scenarios, scored once with frozen families. "
      "The no-pressure set is each scenario's greedy answer with the fact stated plainly and no reason to lie; "
      "the unrelated set is the greedy answer to 300 filtered Alpaca prompts (not judged; cut-off answers "
      "dropped).\n")
    w("| model | scenario build lie / truth | scenario held-out lie / truth | no-pressure truth / lie | unrelated |")
    w("|---|---|---|---|---|")
    for m in MODELS:
        c = collections.Counter((e["set"], e["split"], e["label"]) for e in mans[m]["transcripts"])
        w(f"| {m} | **{c['scenario', 'build', 'lie']}** / **{c['scenario', 'build', 'truth']}** | "
          f"{c['scenario', 'heldout', 'lie']} / {c['scenario', 'heldout', 'truth']} | "
          f"{c['nopressure', 'build', 'truth'] + c['nopressure', 'heldout', 'truth']} / "
          f"{c['nopressure', 'build', 'lie'] + c['nopressure', 'heldout', 'lie']} | "
          f"{c['unrelated', 'unrelated', None]} |")
    w("")

    w("## Commentary: transcripts left out of later analyses\n")
    w("**Problem.** Some responses add a section after the answer that explains it (\"Important considerations\", "
      "\"Why this works\", \"My reasoning\", \"Disclaimer\"). This commentary often names the hidden fact or talks "
      "about hiding, misleading or honesty, so words about deception or honesty can appear in a transcript's own "
      "text, and readouts after the response can reflect that text rather than the model's state. The judge's "
      "\"discloses\" flag removed lies whose commentary admits the truth, but truths are not checked, so in the "
      "Gemma models the selected truths carried such commentary about twice as often as the selected lies. "
      "Gemma writes most of it: its chat format has no system turn, so the scenario's instructions arrive as the "
      "user's own words, and Gemma often reports back on how it followed them. The pilot showed little of it "
      "because its responses were cut at 48 tokens.\n")
    w("**Decision (user, 2026-09-29):** every transcript with commentary is left out of later analyses, in all "
      "models and all sets. `load_manifest()` in `scripts/common.py` drops them by default "
      "(`drop_commentary=False` keeps the full selection); the counts in the other sections of this file are "
      "for the full selection.\n")
    w("**Rule.** A fixed text-matching rule: a heading line (starting with `**` or `#`) that contains a word such "
      "as considerations, why, breakdown, explanation, key things, reasoning, strategy, rationale, disclaimer, "
      "note, internal, approach or important (`COMMENTARY_WORDS` in `scripts/common.py`). It is approximate: it "
      "misses commentary without a heading, such as Gemma's openings that think aloud (\"Okay, deep breaths...\"), "
      "and it can catch an ordinary bold heading inside an answer. \"Hiding or honesty words\" = conceal, hide, "
      "withhold, avoid mentioning, downplay, deflect, mislead, deceive, lie, honest, transparent, instructed, "
      "system prompt (`HIDING_WORDS`). Reading sample: `analysis/gemma_notes_sample.md`.\n")
    w("| model | set / label | selected | with commentary | …with hiding or honesty words | kept |")
    w("|---|---|---|---|---|---|")
    for m in MODELS:
        texts = {t["tid"]: t["response"] for t in read_jsonl(os.path.join(RUNS, slug(m), "transcripts.jsonl"))}
        for st, lab in (("scenario", "lie"), ("scenario", "truth"), ("nopressure", "truth"), ("nopressure", "lie"),
                        ("unrelated", None)):
            es = entries(mans[m], set=st, label=lab)
            if not es:
                continue
            cs = [commentary_section(texts[e["tid"]]) for e in es]
            n_c = sum(c is not None for c in cs)
            n_h = sum(c is not None and bool(HIDING_WORDS.search(c)) for c in cs)
            pct = lambda k: f"{k} ({100 * k / len(es):.0f}%)"
            w(f"| {m} | {st} / {lab or '—'} | {len(es)} | {pct(n_c)} | {pct(n_h)} | **{len(es) - n_c}** |")
    w("")
    w("| model | kept: scenario build lie / truth | held-out lie / truth | scenarios with both a lie and a truth |")
    w("|---|---|---|---|")
    for m in MODELS:
        kept = [e for e in mans[m]["transcripts"] if e["set"] == "scenario" and not e["commentary"]]
        c = collections.Counter((e["split"], e["label"]) for e in kept)
        by = collections.defaultdict(set)
        for e in kept:
            by[e["item_id"]].add(e["label"])
        w(f"| {m} | {c['build', 'lie']} / {c['build', 'truth']} | {c['heldout', 'lie']} / {c['heldout', 'truth']} | "
          f"{sum(len(v) == 2 for v in by.values())} |")
    w("")

    w("## The judge\n")
    w("Claude Opus 5, effort medium, prompt v3. The second pass re-judges a random 20% of samples plus every "
      "ambiguous one. \"Refused\" = samples the judge declined to rate on every try; they are never selected.\n")
    w("| model | second pass agrees | disagreements | \"discloses\" agrees (both passes say lie) | refused | other errors |")
    w("|---|---|---|---|---|---|")
    for m in MODELS:
        sp = sums[m].get("second_pass", {})
        dis = ", ".join(f"{k} {v}" for k, v in sorted(sp.get("disagreements", {}).items(), key=lambda kv: -kv[1]))
        err = judge_errors(m)
        w(f"| {m} | {sp.get('agree')} / {sp.get('n')} | {dis or '—'} | {sp.get('discloses_agrees_on_lies', '—')} | "
          f"{err['refusal']} | {err['other']} |")
    w("")

    w("## Response length\n")
    w("Tokens of the model's own tokenizer, selected transcripts; median (min-max).\n")
    w("| model | scenario lies | scenario truths | no-pressure truths | unrelated |")
    w("|---|---|---|---|---|")
    for m in MODELS:
        n = collections.defaultdict(list)
        for e in mans[m]["transcripts"]:
            n[(e["set"], e["label"])].append(e["n_tokens"])
        w(f"| {m} | {med_range(n['scenario', 'lie'])} | {med_range(n['scenario', 'truth'])} | "
          f"{med_range(n['nopressure', 'truth'])} | {med_range(n['unrelated', None])} |")
    w("")

    w("## Self-report answers, scenario set\n")
    w("Admit = \"yes…\" (Q7: \"A…\"); deny = \"no…\" (Q7: \"B…\"); other = neither opening. \"Cut off\" = the "
      "answer reached its token limit; its post-answer positions are not to be scored.\n")
    for m in MODELS:
        man = mans[m]
        sc = entries(man, set="scenario")
        first = sc[0]
        limit = read_part(m, first, man["wordings"][0], readouts=False)[0].get("answer_limit")
        w(f"### {m} (answer limit {limit} tokens)\n")
        w("| wording | lies admit | lies deny | lies other | truths admit | truths deny | truths other | cut off |")
        w("|---|---|---|---|---|---|---|---|")
        for wd in man["wordings"]:
            c = collections.Counter((e["label"], e["wordings"][wd]["answer_label"]) for e in sc)
            cut = sum(not e["wordings"][wd]["answer_finished"] for e in sc)
            w(f"| {wd} | {c['lie', 'admit']} | {c['lie', 'deny']} | {c['lie', 'other']} | {c['truth', 'admit']} | "
              f"{c['truth', 'deny']} | {c['truth', 'other']} | {cut} / {len(sc)} |")
        w("")

    w("## Tokens at each position group (checks the position map)\n")
    w("Each cell lists the token sequence found at that group and how many transcripts show it (all sets). One "
      "sequence per cell means the template is the same for every transcript. The prefix is one forward pass "
      "shared by all wordings, so pre- and post-response readouts are identical across wordings by "
      "construction.\n")
    for m in MODELS:
        man = mans[m]
        w(f"### {m}\n")
        w("| wording | group | tokens (count of transcripts) |")
        w("|---|---|---|")
        for wd in man["wordings"]:
            seqs = collections.defaultdict(collections.Counter)
            for e in man["transcripts"]:
                it = load_item(m, e, wd, readouts=False)
                by = collections.defaultdict(list)
                for name, p in positions(it).items():
                    g = group_of(name)
                    if g:
                        by[g].append((int(name[len(g):]), it["tokens"][p]))
                for g, toks in by.items():
                    toks = [t for _, t in sorted(toks)]
                    key = f"{len(toks)} tokens" if g == "q_tok" else " ".join(
                        '"' + t.replace("\n", "\\n").replace("|", "\\|") + '"' for t in toks)
                    seqs[g][key] += 1
            for g in GROUPS:
                if g in seqs:
                    w(f"| {wd} | {g} | " + "; ".join(f"{k} ({n})" for k, n in seqs[g].most_common()) + " |")
        w("")

    w("## Check: pre-response readouts within a scenario (J-lens)\n")
    w("For scenarios with both a selected lie and a selected truth, the two transcripts share every token up to "
      "the response, so their pre-response readouts can differ only through rounding in separate forward passes "
      "of different lengths. Per (pre-response slot, layer) cell: is the top token the same, is the whole top-16 "
      "set the same, and how many of the 16 tokens are shared. Layers are split into thirds.\n")
    w("| model | pairs | identical tokens before the response | top token same (early / middle / late) | "
      "identical top-16 set | mean tokens shared of 16 |")
    w("|---|---|---|---|---|---|")
    for m in MODELS:
        by_item = collections.defaultdict(dict)
        for e in entries(mans[m], set="scenario"):
            by_item[e["item_id"]][e["label"]] = e
        pairs = same_ids = 0
        top1, exact, shared, total = (collections.Counter() for _ in range(4))
        for pair in by_item.values():
            if len(pair) < 2:
                continue
            pairs += 1
            got = {}
            for lab, e in pair.items():
                h, a = read_part(m, e, "prefix")
                pos = sorted(p for name, p in positions({"tokens": h["tokens"], "segments": h["segments"]}).items()
                             if name.startswith("preresp_slot"))
                r0 = next(sg["start"] for sg in h["segments"] if sg["name"] == "response")
                got[lab] = (pos, a["J_ids"], h["ids"][:r0], h["abs_start"])
            (pl, al, il, sl), (pt, at, it_, st) = got["lie"], got["truth"]
            same_ids += il == it_ and sl == st
            n_layers = al.shape[0]
            for p_l, p_t in zip(pl, pt):
                for li in range(n_layers):
                    third = min(2, 3 * li // n_layers)
                    x, y = al[li, p_l].tolist(), at[li, p_t].tolist()
                    top1[third] += x[0] == y[0]
                    exact[third] += set(x) == set(y)
                    shared[third] += len(set(x) & set(y))
                    total[third] += 1
        pct = lambda c: " / ".join(f"{c[t] / max(1, total[t]):.1%}" for t in range(3))
        w(f"| {m} | {pairs} | {same_ids} | {pct(top1)} | {pct(exact)} | "
          + " / ".join(f"{shared[t] / max(1, total[t]):.1f}" for t in range(3)) + " |")
    w("")
    w("A top-16 set that differs usually differs in one low-probability token. gpt-oss-20b drifts most, and more "
      "in later layers; a plausible cause is that it is a mixture-of-experts model, where rounding can change "
      "which experts a token is sent to. Presence tests on the top-16 lists carry this much noise.\n")

    with open(os.path.join(ROOT, "DATA.md"), "w") as f:
        f.write("\n".join(lines))
    print("wrote DATA.md")


if __name__ == "__main__":
    main()
