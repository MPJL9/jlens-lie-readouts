#!/usr/bin/env python3
"""Reading sample for the "discloses" decision on the Gemma models. Runs on the Mac.

Gemma often writes the customer-facing answer and then commentary sections ("Important
considerations", "Why this works", "My reasoning", ...). The judge flags a lie as "discloses"
when that commentary states the true fact or admits hiding it; such lies are not selected. The
judge does not check truths, whose commentary may also talk about the pressure to hide.

This script writes analysis/gemma_notes_sample.md:
  - counts, per Gemma model and label, of build-split answers with a commentary section, and of
    those whose commentary uses words about hiding or honesty;
  - 10 dropped lies that disclose (5 per model) and 10 selected truths (5 per model), drawn at
    random (seed 0) from the build split, with the commentary headings marked.
Commentary is found by a fixed text-matching rule (a heading line that contains words such as
"considerations", "why", "explanation", "reasoning", "strategy", "disclaimer" or "note"), so the
counts are approximate. Response text only; no readouts are shown.

Usage: python3 scripts/review_gemma_notes.py
"""
import collections
import json
import os
import random
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RUNS = os.path.join(ROOT, "data", "cluster", "runs")
MODELS = ["gemma_3_27b_it", "gemma_3_12b_it"]
N_PER_MODEL = 5
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common import COMMENTARY_HEADING as HEADING, COMMENTARY_WORDS as COMMENTARY, HIDING_WORDS as HIDING  # noqa: E402


def read_jsonl(path):
    with open(path) as f:
        return [json.loads(line) for line in f if line.strip()]


def commentary_start(text):
    """Line index of the first commentary heading, or None."""
    for i, line in enumerate(text.splitlines()):
        if HEADING.match(line) and COMMENTARY.search(line):
            return i
    return None


def commentary(text):
    i = commentary_start(text)
    return None if i is None else "\n".join(text.splitlines()[i:])


def marked(text):
    lines = text.splitlines()
    out = []
    for line in lines:
        if HEADING.match(line) and COMMENTARY.search(line):
            out.append(">>>>> commentary heading (found by the text rule) >>>>>")
        out.append(line)
    return "\n".join(out)


def main():
    scen = {s["id"]: s for s in read_jsonl(os.path.join(ROOT, "inputs", "scenarios.jsonl"))}
    rng = random.Random(0)
    counts, lies, truths = [], [], []
    for m in MODELS:
        samples = {s["key"]: s for s in read_jsonl(os.path.join(RUNS, m, "samples.jsonl"))}
        judged = {j["key"]: j for j in read_jsonl(os.path.join(RUNS, m, "judge.jsonl"))
                  if j.get("prompt_version") == "v3"}
        selected = [t for t in read_jsonl(os.path.join(RUNS, m, "transcripts.jsonl"))
                    if t["set"] == "scenario" and t["split"] == "build"]
        dropped = [(samples[k], j) for k, j in judged.items()
                   if j["set"] == "scenario" and j["finished"] and j["verdict"] == "lie" and j.get("discloses")
                   and scen[j["item_id"]]["split"] == "build"]
        groups = {"selected lies": [t["response"] for t in selected if t["label"] == "lie"],
                  "selected truths": [t["response"] for t in selected if t["label"] == "truth"],
                  "dropped lies (disclose)": [s["response"] for s, _ in dropped]}
        for name, texts in groups.items():
            with_c = [commentary(x) for x in texts]
            n_c = sum(c is not None for c in with_c)
            n_h = sum(c is not None and bool(HIDING.search(c)) for c in with_c)
            counts.append((m, name, len(texts), n_c, n_h))
        dropped.sort(key=lambda p: p[0]["key"])
        for s, j in rng.sample(dropped, N_PER_MODEL):
            lies.append((m, s["item_id"], s["k"], s["response"], j))
        tr = sorted((t for t in selected if t["label"] == "truth"), key=lambda t: t["tid"])
        for t in rng.sample(tr, N_PER_MODEL):
            truths.append((m, t["item_id"], t["k"], t["response"], t))

    out = ["# Gemma reading sample for the \"discloses\" decision", "",
           "Made by `scripts/review_gemma_notes.py` (seed 0) from `data/cluster/runs/`. Build split only.",
           "Response text only; no readouts. Commentary is found by a fixed text-matching rule (a heading",
           "line with words such as \"considerations\", \"why\", \"explanation\", \"reasoning\", \"strategy\"),",
           "so the counts are approximate. \"Hiding or honesty words\" means the commentary contains words",
           "such as conceal, hide, withhold, avoid mentioning, downplay, mislead, deceive, lie, honest,",
           "transparent, instructed or system prompt.", "",
           "## How common is commentary?", "",
           "| model | answers | n | with a commentary section | commentary uses hiding or honesty words |",
           "|---|---|---|---|---|"]
    for m, name, n, n_c, n_h in counts:
        pct = lambda x: f"{x} ({100 * x / n:.0f}%)" if n else "0"
        out.append(f"| {m} | {name} | {n} | {pct(n_c)} | {pct(n_h)} |")
    out += ["", "## A. Dropped lies that disclose (5 per model)", ""]
    for i, (m, item, k, text, j) in enumerate(lies, 1):
        sc = scen[item]
        out += [f"### A{i}. {m}, {item}, sample {k}", "",
                f"- **True statement:** {sc['true_statement']}",
                f"- **False statement:** {sc['false_statement']}",
                f"- **User asks:** {sc['user_prompt'][:400]}{'…' if len(sc['user_prompt']) > 400 else ''}",
                f"- **Judge's quote of the false claim:** {j.get('quote')}",
                f"- **Judge's reason:** {j.get('reason')}", "", "```text", marked(text), "```", ""]
    out += ["## B. Selected truths (5 per model)", ""]
    for i, (m, item, k, text, t) in enumerate(truths, 1):
        sc = scen[item]
        c = commentary(text)
        out += [f"### B{i}. {m}, {item}, sample {k}", "",
                f"- **True statement:** {sc['true_statement']}",
                f"- **User asks:** {sc['user_prompt'][:400]}{'…' if len(sc['user_prompt']) > 400 else ''}",
                f"- **Judge's reason:** {t.get('judge_reason')}",
                f"- **Commentary section:** {'yes' if c else 'none found'}"
                + (f"; hiding or honesty words: {'yes' if HIDING.search(c) else 'no'}" if c else ""),
                "", "```text", marked(text), "```", ""]
    os.makedirs(os.path.join(ROOT, "analysis"), exist_ok=True)
    path = os.path.join(ROOT, "analysis", "gemma_notes_sample.md")
    with open(path, "w") as f:
        f.write("\n".join(out))
    for m, name, n, n_c, n_h in counts:
        print(f"{m:16s} {name:24s} n={n:4d}  commentary {n_c:4d}  hiding/honesty words {n_h:4d}")
    print(f"wrote {path}")


if __name__ == "__main__":
    main()
