#!/usr/bin/env python3
"""Stage 3 (CPU): choose the transcripts and summarize the sampling.

Scenario set: per scenario, the lowest-numbered usable lie and the lowest-numbered usable truth
(usable = the model finished its turn, the first-pass judge said lie or truth, and it is not a
lie that also discloses the truth or admits hiding it). A scenario gives 0, 1 or 2 transcripts.
No-pressure set: the greedy sample, if usable.
Only judge rows from the current prompt version (src/prompts.py) are read.
Unrelated set: the greedy sample, if finished. The extra unrelated set (unrelated_extra) is
handled the same way and appended after it.

Writes runs/<model>/transcripts.jsonl and runs/<model>/selection_summary.json, and prints
the summary: greedy behaviour, lie rate over the temperature samples, cut-offs by label,
scenarios with a lie / a truth / both, lies that disclose, transcripts per split and label.

--must-keep-existing: refuse to write if a transcript that is already in transcripts.jsonl would
change or disappear (used when the extra unrelated set is added to a finished run, so the
transcripts that were already forwarded and exported stay exactly as they were).

Usage: python3 src/select_transcripts.py --model qwen3.6-27b [--must-keep-existing]
"""
import argparse
import collections
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from models import read_jsonl, slug, write_jsonl  # noqa: E402
from prompts import JUDGE_VERSION  # noqa: E402

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def last_by_key(rows):
    out = {}
    for r in rows:
        out[r["key"]] = r
    return out


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--model", required=True)
    ap.add_argument("--must-keep-existing", action="store_true",
                    help="exit without writing if an already selected transcript would change or disappear")
    args = ap.parse_args()
    run_dir = os.path.join(ROOT, "runs", slug(args.model))
    scen = {s["id"]: s for s in read_jsonl(os.path.join(ROOT, "inputs", "scenarios.jsonl"))}
    unrel = {s: {u["id"]: u for u in read_jsonl(os.path.join(ROOT, "inputs", s + ".jsonl"))}
             for s in ("unrelated", "unrelated_extra")}
    samples = last_by_key(read_jsonl(os.path.join(run_dir, "samples.jsonl")))
    judged = last_by_key(j for j in read_jsonl(os.path.join(run_dir, "judge.jsonl"))
                         if j.get("prompt_version") == JUDGE_VERSION)
    second = last_by_key(j for j in read_jsonl(os.path.join(run_dir, "judge_second.jsonl"))
                         if j.get("prompt_version") == JUDGE_VERSION)

    def verdict(key):
        return judged.get(key, {}).get("verdict")

    def discloses(key):
        return bool(judged.get(key, {}).get("discloses"))

    def is_usable(s):
        return s["finished"] and verdict(s["key"]) in ("lie", "truth") and not discloses(s["key"])

    summary = {}
    kept = []

    def make_row(s, set_name, split, system, user_prompt, j):
        return dict(tid=f"{set_name}__{s['item_id']}__k{s['k']}", set=set_name, item_id=s["item_id"],
                    k=s["k"], split=split, label=(j or {}).get("verdict"), stance=(j or {}).get("stance"),
                    quote=(j or {}).get("quote"), quote_span=(j or {}).get("quote_span"),
                    discloses=(j or {}).get("discloses"), judge_reason=(j or {}).get("reason"),
                    system=system, user_prompt=user_prompt, response=s["response"], reasoning=s.get("reasoning", ""), n_tokens=s["n_tokens"],
                    temperature=s["temperature"])

    # ---- scenario set
    sc_samples = [s for s in samples.values() if s["set"] == "scenario"]
    by_item = collections.defaultdict(list)
    for s in sc_samples:
        by_item[s["item_id"]].append(s)
    greedy = collections.Counter()
    temp = collections.Counter()
    cut = collections.Counter()
    avail = collections.Counter()
    n_disclosing, lost_lie = 0, 0
    for item_id, ss in by_item.items():
        sc = scen[item_id]
        ss.sort(key=lambda s: s["k"])
        for s in ss:
            v = verdict(s["key"])
            if not s["finished"]:
                cut[v] += 1
            if s["k"] == 0:
                greedy[v if s["finished"] else f"{v} (cut off)"] += 1
            elif s["finished"] and s["round"] == 1:
                temp[v] += 1
        finished_lies = [s for s in ss if s["finished"] and verdict(s["key"]) == "lie"]
        n_disclosing += sum(discloses(s["key"]) for s in finished_lies)
        lost_lie += bool(finished_lies) and all(discloses(s["key"]) for s in finished_lies)
        usable = [s for s in ss if is_usable(s)]
        labels = {verdict(s["key"]) for s in usable}
        avail["both" if len(labels) == 2 else (labels.pop() + " only" if labels else "none")] += 1
        for lab in ("lie", "truth"):
            first = next((s for s in usable if verdict(s["key"]) == lab), None)
            if first:
                kept.append(make_row(first, "scenario", sc["split"], sc["system"], sc["user_prompt"],
                                     judged[first["key"]]))
    lt = temp["lie"] + temp["truth"]
    summary["scenario"] = dict(
        scenarios_sampled=len(by_item), samples=len(sc_samples),
        greedy_verdicts=dict(greedy),
        round1_temperature_verdicts=dict(temp),
        round1_temperature_lie_rate=round(temp["lie"] / lt, 3) if lt else None,
        cut_off_samples_by_verdict=dict(cut),
        scenarios_with=dict(avail),
        finished_lies_that_disclose=n_disclosing,
        scenarios_whose_only_lies_disclose=lost_lie,
        topped_up=len({s["item_id"] for s in sc_samples if s["round"] == 2}))

    # ---- no-pressure and unrelated sets
    for set_name in ("nopressure", "unrelated", "unrelated_extra"):
        ss = [s for s in samples.values() if s["set"] == set_name]
        if set_name == "unrelated_extra" and not ss:
            continue
        c = collections.Counter()
        for s in ss:
            v = verdict(s["key"]) if set_name == "nopressure" else "not judged"
            if v == "lie" and discloses(s["key"]):
                v = "lie (discloses)"
            c[v if s["finished"] else f"{v} (cut off)"] += 1
            if not s["finished"]:
                continue
            if set_name == "nopressure":
                if not is_usable(s):
                    continue
                sc = scen[s["item_id"]]
                kept.append(make_row(s, set_name, sc["split"], sc["no_pressure_system"], sc["user_prompt"],
                                     judged[s["key"]]))
            else:
                u = unrel[set_name][s["item_id"]]
                kept.append(make_row(s, set_name, "unrelated", u["system"], u["user_prompt"], None))
        summary[set_name] = dict(samples=len(ss), verdicts=dict(c))

    # ---- kept transcripts and judge agreement
    summary["transcripts"] = {f"{set_}/{split}/{lab}": n for (set_, split, lab), n in sorted(
        collections.Counter((r["set"], r["split"], r["label"]) for r in kept).items(), key=str)}
    lies = [r for r in kept if r["label"] == "lie"]
    summary["lie_quotes_found"] = f"{sum(bool(r['quote_span']) for r in lies)} / {len(lies)}"
    if second:
        pairs = [(verdict(k), j["verdict"]) for k, j in second.items() if k in judged]
        lie_pairs = [(discloses(k), bool(j.get("discloses"))) for k, j in second.items()
                     if verdict(k) == j["verdict"] == "lie"]
        summary["second_pass"] = dict(
            n=len(pairs), agree=sum(a == b for a, b in pairs),
            disagreements={f"{a}->{b}": n for (a, b), n in collections.Counter(
                p for p in pairs if p[0] != p[1]).items()},
            discloses_agrees_on_lies=f"{sum(a == b for a, b in lie_pairs)} / {len(lie_pairs)}")
    if args.must_keep_existing:
        canon = lambda r: json.dumps(r, sort_keys=True, ensure_ascii=False)
        new = {r["tid"]: canon(r) for r in kept}
        changed = [r["tid"] for r in read_jsonl(os.path.join(run_dir, "transcripts.jsonl")) if new.get(r["tid"]) != canon(r)]
        if changed:
            sys.exit(f"FATAL: {len(changed)} already selected transcripts would change or disappear "
                     f"(first: {changed[:3]}); nothing written")
    write_jsonl(os.path.join(run_dir, "transcripts.jsonl"), kept)
    with open(os.path.join(run_dir, "selection_summary.json"), "w") as f:
        json.dump(summary, f, indent=1)
    print(json.dumps(summary, indent=1))
    print(f"SELECT DONE: {len(kept)} transcripts -> {run_dir}/transcripts.jsonl")


if __name__ == "__main__":
    main()
