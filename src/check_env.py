#!/usr/bin/env python3
"""Check that the cluster environment can run the pipeline. Prints one PASS / FAIL line per check.

Checks: Python packages; the GPU (when the job has one); Hugging Face access to each model and
lens (metadata only, nothing large is downloaded); the input files; that the output folders are
writable; and the Anthropic API key, with one tiny call in the judge's exact request shape.

Usage (normally through slurm/check_env.sh): python3 src/check_env.py [--no-api]
"""
import argparse
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
results = []


def check(name, fn):
    try:
        detail = fn()
        results.append(True)
        print(f"PASS  {name}" + (f": {detail}" if detail else ""), flush=True)
    except Exception as e:           # report and keep going
        results.append(False)
        print(f"FAIL  {name}: {type(e).__name__}: {str(e)[:300]}", flush=True)


def packages():
    import numpy, torch, transformers, jlens, anthropic, huggingface_hub  # noqa: F401
    return (f"torch {torch.__version__} (CUDA build {torch.version.cuda}), transformers {transformers.__version__}, "
            f"anthropic {anthropic.__version__}, huggingface_hub {huggingface_hub.__version__}")


def gpu():
    import torch
    if not os.environ.get("CUDA_VISIBLE_DEVICES"):
        return "no GPU requested for this job (skipped)"
    if not torch.cuda.is_available():
        raise RuntimeError("a GPU was allocated but torch cannot see it")
    p = torch.cuda.get_device_properties(0)
    return f"{p.name}, {p.total_memory / 2**30:.0f} GiB"


def hf_token():
    from huggingface_hub import get_token
    if not get_token():
        raise RuntimeError(f"no Hugging Face token under HF_HOME={os.environ.get('HF_HOME')} (Gemma is gated)")
    return f"token found (HF_HOME={os.environ.get('HF_HOME')})"


def model_access(name, spec):
    def fn():
        from huggingface_hub import get_hf_file_metadata, hf_hub_url
        get_hf_file_metadata(hf_hub_url(spec["hf"], "config.json"))
        get_hf_file_metadata(hf_hub_url("neuronpedia/jacobian-lens", spec["lens_file"], revision=spec["lens_rev"]))
        return f"{spec['hf']} and its lens are reachable"
    return fn


def inputs():
    n_s = sum(1 for _ in open(os.path.join(ROOT, "inputs", "scenarios.jsonl")))
    n_u = sum(1 for _ in open(os.path.join(ROOT, "inputs", "unrelated.jsonl")))
    if n_s != 274 or n_u == 0:
        raise RuntimeError(f"{n_s} scenarios (expected 274), {n_u} unrelated prompts")
    return f"{n_s} scenarios, {n_u} unrelated prompts"


def writable():
    for d in ("runs", "exports", os.path.join("slurm", "logs")):
        path = os.path.join(ROOT, d)
        os.makedirs(path, exist_ok=True)
        probe = os.path.join(path, ".write_test")
        open(probe, "w").close()
        os.remove(probe)
    return "runs/, exports/, slurm/logs/"


def api(no_fallback):
    def fn():
        key = os.environ.get("ANTHROPIC_API_KEY", "")
        if not key:
            raise RuntimeError("ANTHROPIC_API_KEY is not set (is ~/.anthropic_env there and sourced?)")
        import anthropic
        ws = os.environ.get("ANTHROPIC_WORKSPACE_ID")
        client = anthropic.Anthropic(default_headers={"anthropic-workspace-id": ws} if ws else None)
        kw = dict(model="claude-opus-5", max_tokens=300, output_config={"effort": "low"},
                  messages=[{"role": "user", "content": "Reply with the single word OK."}])
        if not no_fallback:     # the same request shape src/judge.py uses
            kw.update(extra_headers={"anthropic-beta": "server-side-fallback-2026-07-01"},
                      extra_body={"fallbacks": "default"})
        resp = client.messages.create(**kw)
        text = "".join(b.text for b in resp.content if getattr(b, "type", "") == "text").strip()
        return f"key works (length {len(key)}); served by {resp.model}; reply {text[:20]!r}"
    return fn


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--no-api", action="store_true", help="skip the API call")
    ap.add_argument("--no-fallback", action="store_true", help="test the API call without the fallback option")
    args = ap.parse_args()
    from models import MODELS
    check("python packages", packages)
    check("GPU", gpu)
    check("Hugging Face token", hf_token)
    for name in ("gemma-3-12b-it", "gemma-3-27b-it", "qwen3.6-27b", "gpt-oss-20b"):
        check(f"model + lens {name}", model_access(name, MODELS[name]))
    check("input files", inputs)
    check("output folders writable", writable)
    if not args.no_api:
        check("Anthropic API" + (" (no fallback)" if args.no_fallback else ""), api(args.no_fallback))
    ok = all(results)
    print(("ALL CHECKS PASSED" if ok else f"{results.count(False)} CHECK(S) FAILED"), flush=True)
    sys.exit(0 if ok else 1)


if __name__ == "__main__":
    main()
