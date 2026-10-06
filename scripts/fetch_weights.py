#!/usr/bin/env python3
"""Save the small pieces of model weights that scripts/band_cka.py needs, into data/weights/:

  <slug>_final_norm.npy     the final norm's scale vector (float32 [d])
  <slug>_unembed_rows.npz   ids (the sampled token ids) and rows (float32 [n, d]) of the
                            unembedding matrix, for the token samples of band_cka.token_samples

The unembedding rows come from the weight shard already in the local HF cache (Gemma ties the
unembedding to the embedding). The final norm's vector sits in a shard that is not cached, so
it is read with one HTTP range request per model (a few KB, needs the HF token in
~/.cache/huggingface/token for the gated Gemma repos); gpt-oss's is local.

Usage: python3 scripts/fetch_weights.py [--models m1 m2] [--n 2000]
"""
from __future__ import annotations

import argparse
import glob
import json
import os
import struct
import sys
import urllib.request

import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import common as C  # noqa: E402
from band_cka import WEIGHTS, token_samples  # noqa: E402

HUB = os.path.expanduser("~/.cache/huggingface/hub")

# (HF repo, unembedding tensor name, final norm tensor name)
TENSORS = {
    "gemma-3-12b-it": ("google/gemma-3-12b-it", "language_model.model.embed_tokens.weight", "language_model.model.norm.weight"),
    "gemma-3-27b-it": ("google/gemma-3-27b-it", "language_model.model.embed_tokens.weight", "language_model.model.norm.weight"),
    "qwen3.6-27b": ("Qwen/Qwen3.6-27B", "lm_head.weight", "model.language_model.norm.weight"),
    "gpt-oss-20b": ("openai/gpt-oss-20b", "lm_head.weight", "model.norm.weight"),
}


def snapshot(repo):
    return glob.glob(os.path.join(HUB, "models--" + repo.replace("/", "--"), "snapshots", "*"))[0]


def shard_of(repo, name):
    with open(os.path.join(snapshot(repo), "model.safetensors.index.json")) as f:
        return json.load(f)["weight_map"][name]


def bf16_to_f32(raw):
    u16 = np.frombuffer(raw, dtype=np.uint16).astype(np.uint32) << 16
    return u16.view(np.float32)


def fetch_tensor(repo, shard, name):
    """One tensor of a Hub safetensors shard by range requests (header, then the bytes)."""
    tok = open(os.path.expanduser("~/.cache/huggingface/token")).read().strip()
    url = f"https://huggingface.co/{repo}/resolve/main/{shard}"

    def get(lo, hi):
        req = urllib.request.Request(url, headers={"Authorization": f"Bearer {tok}", "Range": f"bytes={lo}-{hi}"})
        with urllib.request.urlopen(req, timeout=120) as r:
            return r.read()

    n = struct.unpack("<Q", get(0, 7))[0]
    meta = json.loads(get(8, 8 + n - 1))[name]
    assert meta["dtype"] == "BF16", meta
    a, b = meta["data_offsets"]
    return bf16_to_f32(get(8 + n + a, 8 + n + b - 1)).reshape(meta["shape"])


def local_tensor_rows(repo, name, ids):
    from safetensors import safe_open
    path = os.path.join(snapshot(repo), shard_of(repo, name))
    if not os.path.exists(path):
        sys.exit(f"FATAL: {path} is not cached; download that shard first")
    with safe_open(path, framework="pt") as f:
        sl = f.get_slice(name)
        rows = [sl[i:i + 1].float().numpy()[0] for i in ids]
    return np.stack(rows)


def local_tensor(repo, name):
    from safetensors import safe_open
    path = os.path.join(snapshot(repo), shard_of(repo, name))
    with safe_open(path, framework="pt") as f:
        return f.get_tensor(name).float().numpy()


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--models", nargs="+", default=C.MODELS)
    ap.add_argument("--n", type=int, default=2000)
    args = ap.parse_args()
    os.makedirs(WEIGHTS, exist_ok=True)
    for m in args.models:
        repo, unembed, norm = TENSORS[m]
        s = C.slug(m)
        npath = os.path.join(WEIGHTS, s + "_final_norm.npy")
        if not os.path.exists(npath):
            shard = shard_of(repo, norm)
            local = os.path.exists(os.path.join(snapshot(repo), shard))
            g = local_tensor(repo, norm) if local else fetch_tensor(repo, shard, norm)
            np.save(npath, g.astype(np.float32))
            print(f"{m}: final norm {g.shape} ({'local' if local else 'fetched'}), mean {g.mean():.3f}")
        rpath = os.path.join(WEIGHTS, s + "_unembed_rows.npz")
        if not os.path.exists(rpath):
            word, unif = token_samples(m, args.n)
            ids = sorted(set(word) | set(unif))
            rows = local_tensor_rows(repo, unembed, ids)
            np.savez(rpath, ids=np.array(ids, dtype=np.int64), rows=rows.astype(np.float32))
            print(f"{m}: {len(ids)} unembedding rows {rows.shape}, row norm mean {np.linalg.norm(rows, axis=1).mean():.3f}")


if __name__ == "__main__":
    main()
