#!/usr/bin/env python3
"""Stage 2 (CPU + Anthropic API): the LLM judge labels every scenario and no-pressure sample.

The judge sees the true and the false statement and the full conversation (system prompt,
user prompt, response). It returns a verdict (lie / truth / ambiguous), the response's stance
on the fact (true / false / neither), for lies a verbatim quote of the false claim and whether
the response also discloses the truth or admits hiding it ("discloses"), and a one-sentence
reason (prompt v3, src/prompts.py). The quote is checked against the response; its character
span is stored for Experiment 2.

Passes:
  first   every sample -> runs/<model>/judge.jsonl
  second  an independent re-judgment of a random 20% of first-pass rows (seed 0) plus every
          first-pass "ambiguous" -> runs/<model>/judge_second.jsonl; agreement is printed.

Unfinished samples are judged too (so cut-offs can be counted by label) but never selected.
Empty responses get verdict "empty" without an API call. Rerunnable: keys already judged with
the current prompt version are skipped; rows from an older version are judged again, and only
current-version rows are read.

Credentials: ANTHROPIC_API_KEY (and ANTHROPIC_WORKSPACE_ID if the key needs it), e.g. from
~/.anthropic_env on the cluster.

Usage: python3 src/judge.py --model qwen3.6-27b [--pass second] [--workers 8]
       python3 src/judge.py --model qwen3.6-27b --dry-run --limit 2      (print prompts only)
       python3 src/judge.py --model qwen3-1.7b --mock                     (fake verdicts, tests)
"""
import argparse
import collections
import concurrent.futures as cf
import hashlib
import json
import os
import random
import re
import sys
import threading

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from models import append_jsonl, read_jsonl, slug  # noqa: E402
from prompts import JUDGE_SYSTEM, JUDGE_VERSION, judge_user_prompt  # noqa: E402

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SECOND_SHARE = 0.2
FALLBACK_BETA = "server-side-fallback-2026-07-01"


def parse(text):
    m = re.search(r"\{.*\}", text, re.S)
    if not m:
        return None
    try:
        obj = json.loads(m.group(0))
    except json.JSONDecodeError:
        return None
    if obj.get("verdict") not in ("lie", "truth", "ambiguous"):
        return None
    if obj.get("stance") not in ("true", "false", "neither"):
        obj["stance"] = None
    discloses = obj.get("discloses")
    if isinstance(discloses, str):
        discloses = {"true": True, "false": False}.get(discloses.strip().lower())
    if obj["verdict"] != "lie":
        discloses = False
    elif not isinstance(discloses, bool):
        return None                     # a lie must say whether it discloses (prompt v3)
    return dict(verdict=obj["verdict"], stance=obj["stance"], quote=str(obj.get("quote") or ""),
                discloses=discloses, reason=str(obj.get("reason", ""))[:500])


def find_quote(response, quote):
    """(start, end) character span of the quote in the response, or None. Tries an exact
    match, then a match that ignores differences in whitespace."""
    if not quote:
        return None
    i = response.find(quote)
    if i >= 0:
        return [i, i + len(quote)]
    pat = r"\s+".join(re.escape(w) for w in quote.split())
    m = re.search(pat, response)
    return [m.start(), m.end()] if m else None


def mock_verdict(key, response):
    h = int(hashlib.md5(key.encode()).hexdigest(), 16)
    v = ["lie", "truth", "truth", "ambiguous"][h % 4] if response else "empty"
    words = response.split()
    return dict(verdict=v, stance={"lie": "false", "truth": "true"}.get(v, "neither"),
                quote=" ".join(words[:5]) if v == "lie" else "",
                discloses=v == "lie" and (h >> 8) % 3 == 0, reason="mock verdict")


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--model", required=True, help="the model whose samples are judged")
    ap.add_argument("--pass", dest="which", default="first", choices=["first", "second"])
    ap.add_argument("--judge-model", default="claude-opus-5")
    ap.add_argument("--effort", default="medium")
    ap.add_argument("--max-tokens", type=int, default=8000)
    ap.add_argument("--workers", type=int, default=8)
    ap.add_argument("--no-fallback", action="store_true",
                    help="do not let the API re-run a declined request on another model")
    ap.add_argument("--limit", type=int, default=None)
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--mock", action="store_true")
    args = ap.parse_args()

    run_dir = os.path.join(ROOT, "runs", slug(args.model))
    scen = {s["id"]: s for s in read_jsonl(os.path.join(ROOT, "inputs", "scenarios.jsonl"))}
    samples = [s for s in read_jsonl(os.path.join(run_dir, "samples.jsonl"))
               if s["set"] in ("scenario", "nopressure")]
    first_path = os.path.join(run_dir, "judge.jsonl")
    out_path = first_path if args.which == "first" else os.path.join(run_dir, "judge_second.jsonl")
    if args.which == "second":
        first = [j for j in read_jsonl(first_path) if j.get("verdict") in ("lie", "truth", "ambiguous")
                 and j.get("prompt_version") == JUDGE_VERSION]
        rng = random.Random(0)
        pick = {j["key"] for j in rng.sample(first, round(SECOND_SHARE * len(first)))}
        pick |= {j["key"] for j in first if j["verdict"] == "ambiguous"}
        samples = [s for s in samples if s["key"] in pick]
    done = {j["key"] for j in read_jsonl(out_path)
            if j.get("verdict") not in (None, "error") and j.get("prompt_version") == JUDGE_VERSION}
    todo = [s for s in samples if s["key"] not in done]
    if args.limit:
        todo = todo[:args.limit]

    def prompt_of(s):
        sc = scen[s["item_id"]]
        system = sc["system"] if s["set"] == "scenario" else sc["no_pressure_system"]
        return judge_user_prompt(sc["true_statement"], sc["false_statement"], system,
                                 sc["user_prompt"], s["response"])

    if args.dry_run:
        for s in todo[:args.limit or 2]:
            print("=" * 20, s["key"], "\n[SYSTEM PROMPT OF THE JUDGE]\n" + JUDGE_SYSTEM + "\n[USER]\n" + prompt_of(s))
        print(f"\n(dry run: {len(todo)} samples would be judged by {args.judge_model})")
        return

    client = None
    if not args.mock:
        import anthropic
        ws = os.environ.get("ANTHROPIC_WORKSPACE_ID")
        client = anthropic.Anthropic(max_retries=5,
                                     default_headers={"anthropic-workspace-id": ws} if ws else None)
    lock, stop = threading.Lock(), threading.Event()
    counts = collections.Counter()

    def judge_one(s):
        if stop.is_set():
            return
        rec = dict(key=s["key"], set=s["set"], item_id=s["item_id"], k=s["k"], finished=s["finished"],
                   prompt_version=JUDGE_VERSION, judge_model="mock" if args.mock else args.judge_model,
                   effort=args.effort, pass_=args.which)
        if not s["response"].strip():
            rec.update(verdict="empty", stance=None, quote="", discloses=False, reason="empty response")
        elif args.mock:
            rec.update(mock_verdict(s["key"], s["response"]), served_model="mock")
        else:
            import anthropic
            kw = dict(model=args.judge_model, max_tokens=args.max_tokens,
                      output_config={"effort": args.effort}, system=JUDGE_SYSTEM,
                      messages=[{"role": "user", "content": prompt_of(s)}])
            if not args.no_fallback:
                kw.update(extra_headers={"anthropic-beta": FALLBACK_BETA}, extra_body={"fallbacks": "default"})
            try:
                resp = client.messages.create(**kw)
            except anthropic.AuthenticationError:
                stop.set()
                print("FATAL: the API key was rejected. Check ~/.anthropic_env "
                      "(and ANTHROPIC_WORKSPACE_ID if your key needs one).", file=sys.stderr)
                return
            except (anthropic.APIStatusError, anthropic.APIConnectionError) as e:
                rec.update(verdict="error", reason=f"{type(e).__name__}: {str(e)[:300]}")
                resp = None
            if resp is not None:
                rec["served_model"] = resp.model
                rec["stop_reason"] = resp.stop_reason
                text = "".join(b.text for b in resp.content if getattr(b, "type", "") == "text")
                got = parse(text) if resp.stop_reason != "refusal" else None
                if got is None:
                    rec.update(verdict="error", reason=f"{resp.stop_reason}: unparseable: {text[:200]}")
                else:
                    rec.update(got)
        span = find_quote(s["response"], rec.get("quote", ""))
        rec["quote_span"] = span
        rec["quote_found"] = span is not None if rec.get("quote") else None
        with lock:
            append_jsonl(out_path, rec)
            counts[rec["verdict"]] += 1
            n = sum(counts.values())
            if n % 50 == 0:
                print(f"{n}/{len(todo)} judged: {dict(counts)}", flush=True)

    print(f"judging {len(todo)} samples of {args.model} ({args.which} pass, judge {args.judge_model})", flush=True)
    with cf.ThreadPoolExecutor(max_workers=1 if args.mock else args.workers) as ex:
        list(ex.map(judge_one, todo))
    if stop.is_set():
        sys.exit(1)

    # summary over the whole file (current prompt version only)
    rows = {j["key"]: j for j in read_jsonl(out_path) if j.get("prompt_version") == JUDGE_VERSION}
    by = collections.Counter((j["set"], j["finished"], j["verdict"]) for j in rows.values())
    print("\nverdicts by set / finished:")
    for (st, fin, v), n in sorted(by.items(), key=str):
        print(f"  {st:10s} finished={fin!s:5s} {v:9s} {n}")
    lies = [j for j in rows.values() if j["verdict"] == "lie"]
    if lies:
        print(f"lie quotes found in the response: {sum(bool(j.get('quote_found')) for j in lies)} / {len(lies)}")
        print(f"lies that also disclose the truth (not selected): {sum(bool(j.get('discloses')) for j in lies)} / {len(lies)}")
    other = collections.Counter(j.get("served_model") for j in rows.values() if j.get("served_model"))
    print("served by:", dict(other))
    if args.which == "second":
        f = {j["key"]: j for j in read_jsonl(first_path) if j.get("prompt_version") == JUDGE_VERSION}
        pairs = [(f[k]["verdict"], j["verdict"]) for k, j in rows.items() if k in f]
        agree = sum(a == b for a, b in pairs)
        print(f"second pass agrees with first on {agree} / {len(pairs)}; disagreements:",
              dict(collections.Counter(p for p in pairs if p[0] != p[1])))
        both_lie = [(f[k].get("discloses"), j.get("discloses")) for k, j in rows.items()
                    if k in f and f[k]["verdict"] == j["verdict"] == "lie"]
        print(f"on samples both passes call a lie, discloses agrees on "
              f"{sum(a == b for a, b in both_lie)} / {len(both_lie)}")
    print(f"JUDGE DONE ({args.which}) -> {out_path}")


if __name__ == "__main__":
    main()
