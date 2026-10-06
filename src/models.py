"""Model registry, loading, chat rendering with segment bookkeeping, and generation.

Used by every GPU stage (sample.py, forward.py, readout.py). The chat template, the stop
tokens and the layer indexing are defined here once.
"""
from __future__ import annotations

import json
import logging
import os
import re
import sys
from dataclasses import dataclass, field

logger = logging.getLogger("redo")

LENS_REPO = "neuronpedia/jacobian-lens"

# harmony = gpt-oss chat format: the model writes a hidden reasoning passage (analysis
# channel) before its final answer (final channel).
MODELS = {
    "gemma-3-12b-it": dict(
        hf="google/gemma-3-12b-it",
        lens_file="gemma-3-12b-it/jlens/Salesforce-wikitext/gemma-3-12b-it_jacobian_lens.pt",
        lens_rev="main", chat_kwargs={}, response_limit=2048),   # Gemma writes long answers
    "gemma-3-27b-it": dict(
        hf="google/gemma-3-27b-it",
        lens_file="gemma-3-27b-it/jlens/Salesforce-wikitext/gemma-3-27b-it_jacobian_lens.pt",
        lens_rev="main", chat_kwargs={}, response_limit=2048),   # Gemma writes long answers
    "qwen3.6-27b": dict(
        hf="Qwen/Qwen3.6-27B",
        lens_file="qwen3.6-27b/jlens/Salesforce-wikitext/Qwen3.6-27B_jacobian_lens_n1000.pt",
        lens_rev="qwen-n1000", chat_kwargs={"enable_thinking": False}),
    "gpt-oss-20b": dict(
        hf="openai/gpt-oss-20b",
        lens_file="gpt-oss-20b/jlens/Salesforce-wikitext/gpt-oss-20b_jacobian_lens.pt",
        lens_rev="main", chat_kwargs={"reasoning_effort": "low"}, harmony=True),
    # small model with a published lens: local smoke tests only
    "qwen3-1.7b": dict(
        hf="Qwen/Qwen3-1.7B",
        lens_file="qwen3-1.7b/jlens/Salesforce-wikitext/Qwen3-1.7B_jacobian_lens.pt",
        lens_rev="main", chat_kwargs={"enable_thinking": False}),
}

# token limits (new tokens). Harmony models spend part of the budget on hidden reasoning.
RESPONSE_LIMIT = {"default": 512, "harmony": 2048}    # a model entry's response_limit overrides this
ANSWER_LIMIT = {"default": 256, "harmony": 1024}   # Q1 answers often explain themselves at length

HARMONY_FINAL = "<|channel|>final<|message|>"


def limit_for(spec, table):
    if table is RESPONSE_LIMIT and spec.get("response_limit"):
        return spec["response_limit"]
    return table["harmony"] if spec.get("harmony") else table["default"]


def slug(name):
    return re.sub(r"[^a-z0-9]+", "_", name.lower()).strip("_")


def setup_logging():
    logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")
    logging.getLogger("transformers").setLevel(logging.WARNING)


def gpu_sanity():
    import torch
    if os.environ.get("SLURM_JOB_ID") and os.environ.get("CUDA_VISIBLE_DEVICES") is not None \
            and not torch.cuda.is_available():
        sys.exit("FATAL: GPU allocated but torch.cuda.is_available() is False")


# ---------------------------------------------------------------- io
def read_jsonl(path):
    if not os.path.exists(path):
        return []
    with open(path) as f:
        return [json.loads(l) for l in f if l.strip()]


def append_jsonl(path, row):
    os.makedirs(os.path.dirname(path) or ".", exist_ok=True)
    with open(path, "a") as f:
        f.write(json.dumps(row, ensure_ascii=False) + "\n")


def write_jsonl(path, rows):
    os.makedirs(os.path.dirname(path) or ".", exist_ok=True)
    with open(path, "w") as f:
        for r in rows:
            f.write(json.dumps(r, ensure_ascii=False) + "\n")


# ---------------------------------------------------------------- loading
@dataclass
class Loaded:
    name: str
    spec: dict
    hf_model: object
    tokenizer: object
    lens_model: object          # jlens.HFLensModel: .layers, .forward, .unembed
    device: object
    n_layers: int = 0
    d_model: int = 0
    stop_ids: set = field(default_factory=set)


def load_model(name, device=None, head_only=False):
    """head_only: keep the model body on the CPU and put only the final norm and the unembedding
    on `device`. That is all the readout uses (it unembeds saved residuals), and it lets a 27B
    model's readout run on a 48 GB card. Same dtype and the same modules, so the logits match."""
    import torch
    import transformers
    import jlens
    spec = MODELS[name]
    if device is None:
        device = "cuda" if torch.cuda.is_available() else ("mps" if torch.backends.mps.is_available() else "cpu")
    dev = torch.device(device)
    dtype = torch.float32 if dev.type == "cpu" else torch.bfloat16   # Gemma overflows in fp16
    logger.info("loading %s on %s (%s)%s", spec["hf"], dev, dtype,
                "; body on the CPU, final norm and unembedding on the device" if head_only else "")
    hf = transformers.AutoModelForCausalLM.from_pretrained(spec["hf"], dtype=dtype, low_cpu_mem_usage=True)
    hf.eval()
    if not head_only:
        hf.to(dev)
    tok = transformers.AutoTokenizer.from_pretrained(spec["hf"])
    if tok.pad_token_id is None:
        tok.pad_token = tok.eos_token
    lm = jlens.from_hf(hf, tok)
    if head_only:
        # jlens' unembed runs lm._final_norm then lm._lm_head on the lm_head's device
        lm._final_norm.to(dev)
        lm._lm_head.to(dev)
        with torch.no_grad():
            lm.unembed(torch.zeros(1, lm.d_model, device=dev))    # fails here, not mid-run
    eos = hf.generation_config.eos_token_id
    stop = set(eos if isinstance(eos, list) else [eos]) | {tok.eos_token_id}
    stop.discard(None)
    return Loaded(name=name, spec=spec, hf_model=hf, tokenizer=tok, lens_model=lm, device=dev,
                  n_layers=lm.n_layers, d_model=lm.d_model, stop_ids=stop)


def load_lens(name):
    import jlens
    spec = MODELS[name]
    return jlens.JacobianLens.from_pretrained(LENS_REPO, filename=spec["lens_file"], revision=spec["lens_rev"])


# ---------------------------------------------------------------- chat rendering
def render(L, messages, add_generation_prompt):
    return L.tokenizer.apply_chat_template(messages, tokenize=False,
                                           add_generation_prompt=add_generation_prompt,
                                           **L.spec["chat_kwargs"])


def encode_marked(L, messages, names, add_generation_prompt):
    """Render messages, tokenize, and return (ids, segments).

    names[i] is the segment name for messages[i] (None = not recorded). Each message's
    content is found in the rendered text left to right (templates may trim content). A
    final segment `gen_prompt` covers everything after the last named message."""
    text = render(L, messages, add_generation_prompt)
    enc = L.tokenizer(text, add_special_tokens=False, return_offsets_mapping=True)
    ids, offs = list(enc["input_ids"]), [tuple(o) for o in enc["offset_mapping"]]
    segments, cursor = [], 0
    for msg, name in zip(messages, names):
        c = msg["content"].strip()
        cs = text.find(c, cursor)
        if cs < 0:
            raise ValueError(f"could not locate {name or msg['role']!r} in the rendered chat")
        ce = cs + len(c)
        if name is not None:
            idx = [i for i, (a, b) in enumerate(offs) if b > cs and a < ce and b > a]
            segments.append({"name": name, "start": idx[0], "end": idx[-1] + 1})
        cursor = ce
    if segments:
        segments.append({"name": "gen_prompt", "start": segments[-1]["end"], "end": len(ids)})
    return ids, segments


def seg(segments, name):
    for s in segments:
        if s["name"] == name:
            return s
    return None


# ---------------------------------------------------------------- generation
def split_harmony(L, new_ids):
    """(final answer text, hidden reasoning text) from a harmony generation."""
    raw = L.tokenizer.decode(new_ids, skip_special_tokens=False)
    reasoning = ""
    m = re.search(r"<\|channel\|>analysis<\|message\|>(.*?)(<\|end\|>|$)", raw, re.S)
    if m:
        reasoning = m.group(1).strip()
    if HARMONY_FINAL not in raw:
        return "", reasoning
    final = raw.rsplit(HARMONY_FINAL, 1)[1]
    for stop in ("<|return|>", "<|end|>", "<|endoftext|>", "<|start|>"):
        final = final.split(stop, 1)[0]
    return final.strip(), reasoning


def cut_at_stop(L, new_ids):
    """(ids before the first stop token, whether a stop token was emitted)."""
    for i, t in enumerate(new_ids):
        if t in L.stop_ids:
            return new_ids[:i], True
    return new_ids, False


def decode_generation(L, new_ids):
    """dict(text, reasoning, finished, n_tokens) for one generated continuation."""
    body, stopped = cut_at_stop(L, new_ids)
    if L.spec.get("harmony"):
        text, reasoning = split_harmony(L, body)
        finished = stopped and HARMONY_FINAL in L.tokenizer.decode(body, skip_special_tokens=False)
    else:
        text, reasoning = L.tokenizer.decode(body, skip_special_tokens=True).strip(), ""
        finished = stopped
    return dict(text=text, reasoning=reasoning, finished=bool(finished), n_tokens=len(body), ids=body)


def generate(L, prompt_ids, max_new_tokens, n=1, temperature=0.0, seed=None):
    """n continuations of prompt_ids. temperature 0 = greedy (n must be 1).
    Returns a list of raw new-token id lists (stop tokens and padding included)."""
    import torch
    inp = torch.tensor([prompt_ids], device=L.device)
    if temperature <= 0:
        assert n == 1
        kw = dict(do_sample=False)
    else:
        kw = dict(do_sample=True, temperature=temperature, top_p=0.95, num_return_sequences=n)
    if seed is not None:
        torch.manual_seed(seed)
    with torch.no_grad():
        out = L.hf_model.generate(input_ids=inp, attention_mask=torch.ones_like(inp),
                                  max_new_tokens=max_new_tokens,
                                  pad_token_id=L.tokenizer.pad_token_id, **kw)
    return [row[len(prompt_ids):].tolist() for row in out]


# ---------------------------------------------------------------- self-report answers
def classify_answer(text, style="yesno"):
    """admit / deny / other from the opening characters of a self-report answer.
    style 'ab' (Q7): A = admits lying, B = denies."""
    t = text.strip().lstrip("*#` \n\"'(").lower()
    if style == "ab":
        return "admit" if t.startswith("a") else ("deny" if t.startswith("b") else "other")
    return "admit" if t.startswith("yes") else ("deny" if t.startswith("no") else "other")
