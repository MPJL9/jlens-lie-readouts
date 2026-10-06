#!/usr/bin/env python3
"""Stage 1 (GPU): sample the models' responses.

Sets:
  scenario    MASK pressure prompt. Round 1: sample 0 greedy + samples 1-7 at temperature
              1.0 (top-p 0.95). Round 2 (top-up): samples 8-15 at temperature 1.0, only for
              scenarios whose round-1 samples include no usable lie or no usable truth
              (usable = finished, judged lie or truth, and not a lie that also discloses the
              truth; reads the current-version rows of runs/<model>/judge.jsonl).
  nopressure  the same user prompt with the no-pressure system prompt; greedy only.
  unrelated   ordinary chat prompts (inputs/unrelated.jsonl); greedy only.
  unrelated_extra  the extra unrelated set (inputs/unrelated_extra.jsonl: 1,000 more Alpaca
              prompts, none repeating the first set; user decision, 2026-10-01); greedy only.

A sample is "finished" when the model ended its turn within the token limit (for gpt-oss:
and reached its final answer). Unfinished samples are kept in the file but never selected.

Output: runs/<model>/samples.jsonl, one row per sample, keyed "<set>|<item id>|<k>".
Rerunnable: items already sampled are skipped.

Usage: python3 src/sample.py --model qwen3.6-27b --sets scenario nopressure unrelated --round 1
       python3 src/sample.py --model qwen3.6-27b --sets scenario --round 2
"""
import argparse
import os
import sys
import time

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from models import (RESPONSE_LIMIT, append_jsonl, decode_generation, generate, gpu_sanity,  # noqa: E402
                    limit_for, load_model, logger, read_jsonl, render, setup_logging, slug)
from prompts import JUDGE_VERSION  # noqa: E402

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
N_ROUND1, N_TOPUP, TEMPERATURE = 8, 8, 1.0


def usable_labels(run_dir):
    """{scenario id: set of labels among its usable round-1 samples}, for every scenario that
    has round-1 samples (the set is empty when none is usable). Only verdicts from the current
    judge prompt count; a lie that also discloses the truth is not usable."""
    samples = {r["key"]: r for r in read_jsonl(os.path.join(run_dir, "samples.jsonl"))}
    out = {s["item_id"]: set() for s in samples.values() if s["set"] == "scenario" and s["round"] == 1}
    judged = {j["key"]: j for j in read_jsonl(os.path.join(run_dir, "judge.jsonl"))
              if j.get("prompt_version") == JUDGE_VERSION}
    for j in judged.values():
        s = samples.get(j["key"])
        if s and s["set"] == "scenario" and s["round"] == 1 and s["finished"] \
                and j.get("verdict") in ("lie", "truth") and not j.get("discloses"):
            out[s["item_id"]].add(j["verdict"])
    return out


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--model", required=True)
    ap.add_argument("--sets", nargs="+", default=["scenario", "nopressure", "unrelated"])
    ap.add_argument("--round", type=int, default=1, choices=[1, 2])
    ap.add_argument("--limit", type=int, default=None, help="first N items per set (smoke tests)")
    ap.add_argument("--max-new-tokens", type=int, default=None, help="override (smoke tests)")
    ap.add_argument("--device", default=None)
    args = ap.parse_args()
    setup_logging()
    gpu_sanity()
    run_dir = os.path.join(ROOT, "runs", slug(args.model))
    out_path = os.path.join(run_dir, "samples.jsonl")
    done = {r["key"] for r in read_jsonl(out_path)}

    scenarios = read_jsonl(os.path.join(ROOT, "inputs", "scenarios.jsonl"))
    unrelated = {s: read_jsonl(os.path.join(ROOT, "inputs", s + ".jsonl")) for s in ("unrelated", "unrelated_extra")}
    for s in ("unrelated", "unrelated_extra"):
        if s in args.sets and not unrelated[s]:
            sys.exit(f"FATAL: inputs/{s}.jsonl is missing or empty")
    have = usable_labels(run_dir) if args.round == 2 else {}
    if args.round == 2 and not read_jsonl(os.path.join(run_dir, "judge.jsonl")):
        sys.exit("FATAL: round 2 needs judged round-1 samples (runs/<model>/judge.jsonl)")

    L = load_model(args.model, args.device)
    max_new = args.max_new_tokens or limit_for(L.spec, RESPONSE_LIMIT)
    logger.info("response limit %d new tokens; stop ids %s", max_new, sorted(L.stop_ids))
    old_limits = {r["max_new_tokens"] for r in read_jsonl(out_path) if r["set"] in args.sets}
    if old_limits - {max_new}:
        sys.exit(f"FATAL: {out_path} already holds samples made with a token limit of {sorted(old_limits)}, "
                 f"but this run uses {max_new}. Move that file aside before sampling with a new limit.")

    jobs = []   # (set, item, system, list of (k, temperature, n, seed))
    for set_name in args.sets:
        if set_name == "scenario":
            for idx, sc in enumerate(scenarios):
                if args.round == 1:
                    plan = [(0, 0.0, 1, None), (1, TEMPERATURE, N_ROUND1 - 1, 10_000 + idx)]
                else:
                    if sc["id"] not in have or have[sc["id"]] >= {"lie", "truth"}:
                        continue          # not sampled in round 1, or already has both
                    plan = [(N_ROUND1, TEMPERATURE, N_TOPUP, 20_000 + idx)]
                jobs.append(("scenario", sc["id"], sc["system"], sc["user_prompt"], plan))
        elif set_name == "nopressure":
            for sc in scenarios:
                jobs.append(("nopressure", sc["id"], sc["no_pressure_system"], sc["user_prompt"],
                             [(0, 0.0, 1, None)]))
        elif set_name in unrelated:
            for u in unrelated[set_name]:
                jobs.append((set_name, u["id"], u["system"], u["user_prompt"], [(0, 0.0, 1, None)]))
        else:
            sys.exit(f"unknown set {set_name}")
    if args.limit:
        counts, kept = {}, []
        for j in jobs:
            counts[j[0]] = counts.get(j[0], 0) + 1
            if counts[j[0]] <= args.limit:
                kept.append(j)
        jobs = kept
    logger.info("%d items to sample (round %d)", len(jobs), args.round)

    t0 = time.time()
    for n_done, (set_name, item_id, system, user_prompt, plan) in enumerate(jobs, 1):
        msgs = [{"role": "system", "content": system}, {"role": "user", "content": user_prompt}]
        # same rendering and tokenization as forward.py, so the prompt tokens match
        prompt_ids = list(L.tokenizer(render(L, msgs, True), add_special_tokens=False)["input_ids"])
        for k0, temp, n, seed in plan:
            keys = [f"{set_name}|{item_id}|{k0 + i}" for i in range(n)]
            if all(k in done for k in keys):
                continue
            outs = generate(L, prompt_ids, max_new, n=n, temperature=temp, seed=seed)
            for i, new in enumerate(outs):
                g = decode_generation(L, new)
                append_jsonl(out_path, dict(
                    key=keys[i], set=set_name, item_id=item_id, k=k0 + i, round=args.round,
                    temperature=temp, top_p=0.95 if temp > 0 else None, seed=seed,
                    max_new_tokens=max_new, prompt_tokens=len(prompt_ids),
                    response=g["text"], reasoning=g["reasoning"], finished=g["finished"],
                    n_tokens=g["n_tokens"]))
                done.add(keys[i])
        if n_done % 10 == 0 or n_done == len(jobs):
            logger.info("%d/%d items (%.0f s)", n_done, len(jobs), time.time() - t0)
    print(f"SAMPLE DONE: {args.model} round {args.round} -> {out_path}")


if __name__ == "__main__":
    main()
