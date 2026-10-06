#!/usr/bin/env python3
"""Experiment 3, data step (CPU): cut the cached residual streams at the listed template positions.
No model, no GPU.

Reads inputs/exp3_cut_list.jsonl (built on the Mac by scripts/exp3/build_cut_list.py; one row
per transcript x part: tid, set, part, names, positions (absolute), ids (the token id expected at
each position)) and, per row, runs/<slug>/cache/<tid>/template_<part>.pt if it exists (the extra
unrelated set: {acts [layers, n, d] bf16, positions, ids}), else <part>.pt (whole sequences:
{acts [layers, T, d] bf16, start, ids}). The template file is tried first because the extra
unrelated set also has a Q9_dyl.pt that holds one position only (the DYL probe's). acts[l] is
block l's output. The token id at every position is checked against the list; a mismatch is fatal.

Writes, per set, runs/<slug>/exp3/<set>.npy ([n vectors, n layers, d], layers in the order of
--layers) and <set>.jsonl (one row per vector, same order: tid, part, name, position), and
runs/<slug>/exp3/meta.json (layers, counts, the largest absolute value, rows whose cache file is
missing). Rerunnable: a set whose two files exist is skipped. --out names another folder than
exp3 under runs/<slug>/ (a second list, such as the one of build_cut_list.py --last, needs its own).

--dtype float16 (default) halves the files but holds values up to about 65,000 only; the job
stops if a value is larger. Gemma's residual stream has larger values: use --dtype float32.

Usage: python3 src/cut_positions.py --model qwen3.6-27b --layers 35 41 47 53 58 [--dtype float32] [--out exp3_last] [--root .]
"""
import argparse
import json
import os
import sys
import time

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from models import logger, read_jsonl, setup_logging, slug  # noqa: E402

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def load(path):
    """The saved dict, memory-mapped where torch allows it (only the pages that are read load)."""
    import torch
    try:
        return torch.load(path, map_location="cpu", mmap=True)
    except (TypeError, RuntimeError, ValueError):
        return torch.load(path, map_location="cpu")


def cut(cache_dir, row, layers, dtype):
    """float32 [len(positions), len(layers), d] for one list row, or None if no cache file."""
    import torch
    tdir = os.path.join(cache_dir, row["tid"])
    template = os.path.join(tdir, f"template_{row['part']}.pt")
    whole = os.path.join(tdir, f"{row['part']}.pt")
    if os.path.exists(template):
        blob = load(template)
        where = {p: i for i, p in enumerate(blob["positions"])}
        missing = [p for p in row["positions"] if p not in where]
        if missing:
            sys.exit(f"FATAL: {template} lacks positions {missing}")
        idx = [where[p] for p in row["positions"]]
        ids = [int(blob["ids"][i]) for i in idx]
    elif os.path.exists(whole):
        blob = load(whole)
        idx = [p - blob["start"] for p in row["positions"]]
        if min(idx) < 0 or max(idx) >= blob["acts"].shape[1]:
            sys.exit(f"FATAL: {whole} holds positions {blob['start']}..{blob['start'] + blob['acts'].shape[1] - 1}, "
                     f"asked {row['positions']}")
        ids = [int(blob["ids"][p]) for p in row["positions"]]
    else:
        return None
    if ids != row["ids"]:
        sys.exit(f"FATAL: {row['tid']} {row['part']}: tokens {ids} at {row['positions']}, the list expects {row['ids']}")
    x = torch.stack([blob["acts"][l][idx] for l in layers], dim=1).to(torch.float32)   # [n, layers, d]
    if not torch.isfinite(x).all():
        sys.exit(f"FATAL: {row['tid']} {row['part']}: values not finite")
    if dtype == "float16" and x.abs().max() > 65000:
        sys.exit(f"FATAL: {row['tid']} {row['part']}: largest value {x.abs().max().item():.0f} does not fit float16; rerun with --dtype float32")
    return x.numpy()


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--model", required=True)
    ap.add_argument("--layers", type=int, nargs="+", required=True)
    ap.add_argument("--list", default="inputs/exp3_cut_list.jsonl")
    ap.add_argument("--dtype", choices=["float16", "float32"], default="float16")
    ap.add_argument("--out", default="exp3", help="output folder under runs/<model>/ (a second list needs its own folder)")
    ap.add_argument("--root", default=ROOT)
    args = ap.parse_args()
    setup_logging()
    import numpy as np

    run_dir = os.path.join(args.root, "runs", slug(args.model))
    cache_dir = os.path.join(run_dir, "cache")
    out_dir = os.path.join(run_dir, args.out)
    os.makedirs(out_dir, exist_ok=True)
    rows = read_jsonl(os.path.join(args.root, args.list))
    sets = list(dict.fromkeys(r["set"] for r in rows))
    meta_path = os.path.join(out_dir, "meta.json")
    meta = json.load(open(meta_path)) if os.path.exists(meta_path) else {}
    meta.update(model=args.model, layers=args.layers)
    meta.setdefault("sets", {})

    t0 = time.time()
    for s in sets:
        npy, idx_path = os.path.join(out_dir, f"{s}.npy"), os.path.join(out_dir, f"{s}.jsonl")
        if os.path.exists(npy) and os.path.exists(idx_path):
            logger.info("%s: already cut, skipped", s)
            continue
        todo = [r for r in rows if r["set"] == s]
        X, index, missing, n, top = None, [], [], 0, 0.0
        for k, r in enumerate(todo, 1):
            x = cut(cache_dir, r, args.layers, args.dtype)
            if x is None:
                missing.append([r["tid"], r["part"]])
            else:
                if X is None:
                    X = np.zeros((sum(len(q["positions"]) for q in todo), len(args.layers), x.shape[2]), args.dtype)
                X[n:n + len(x)] = x
                top = max(top, float(abs(x).max()))
                n += len(x)
                index += [dict(tid=r["tid"], part=r["part"], name=name, position=p)
                          for name, p in zip(r["names"], r["positions"])]
            if k % 500 == 0 or k == len(todo):
                logger.info("%s: %d/%d parts (%.0f s)", s, k, len(todo), time.time() - t0)
        if X is None:
            sys.exit(f"FATAL: no cache file found for set {s} under {cache_dir}")
        np.save(npy + ".tmp.npy", X[:n])
        os.replace(npy + ".tmp.npy", npy)
        with open(idx_path + ".tmp", "w") as f:
            for row in index:
                f.write(json.dumps(row) + "\n")
        os.replace(idx_path + ".tmp", idx_path)
        meta["sets"][s] = dict(vectors=n, parts=len(todo), missing=missing, largest_value=top, dtype=args.dtype)
        with open(meta_path, "w") as f:
            json.dump(meta, f)
        logger.info("%s: %d vectors (%s, largest value %.0f), %d parts with no cache file -> %s", s, n, args.dtype, top, len(missing), npy)
    n_missing = sum(len(v["missing"]) for v in meta["sets"].values())
    print(f"CUT DONE: {args.model} layers {args.layers} -> {out_dir}; parts with no cache file: {n_missing}")


if __name__ == "__main__":
    main()
