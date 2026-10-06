"""Shared utilities: loading the readout exports, position map, readouts at a position, AUROC,
grouped bootstrap, label permutation.

The data are the new runs (2026-09-27/28), pulled by scripts/pull_from_cluster.sh into data/cluster/:
  runs/<slug>/     samples.jsonl, judge.jsonl, judge_second.jsonl, transcripts.jsonl,
                   selection_summary.json, sequences.jsonl
  exports/<slug>/  manifest.json, vocab.json, and per transcript <set>/<tid>/<part>.json + .bin
                   (part = "prefix" or a wording; format in src/readout.py)
The pilot files (data/source, data/labels, data/exports; built by scripts/setup_data.py) keep
their own loaders at the end of this file, prefixed pilot_.

No GPU, no network.
"""
from __future__ import annotations

import json
import os
import random
import re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA = os.path.join(ROOT, "data")
RUNS = os.path.join(DATA, "cluster", "runs")
EXPORTS = os.path.join(DATA, "cluster", "exports")

WORDINGS = ["Q1_bare", "Q2_after", "Q6_factual", "Q7_ab", "Q9_dyl"]

MODELS = ["gemma-3-12b-it", "gemma-3-27b-it", "qwen3.6-27b", "gpt-oss-20b"]
LENSES = ["J", "LL"]          # J-lens, logit lens

# One layer band per model, inclusive layer numbers. Chosen by the user on 2026-10-01 in the
# viewer from the two label-free suggestions in analysis/band/BAND.md (PLAN.md Sections 4 and 8).
# Used for every family on that model.
BANDS = {"gemma-3-12b-it": (17, 40), "gemma-3-27b-it": (27, 52), "qwen3.6-27b": (35, 58), "gpt-oss-20b": (10, 20)}
# The logit lens's own band, for the comparison of PLAN.md Section 5.7 (user, 2026-10-01; from the
# readout suggestion in analysis/band/BAND.md, Section 7).
BANDS_LL = {"gemma-3-12b-it": (21, 44), "gemma-3-27b-it": (27, 54), "qwen3.6-27b": (35, 58), "gpt-oss-20b": (9, 14)}

# Commentary: a section after the answer that explains it ("Important considerations", "Why this
# works", "My reasoning", ...), found by a fixed text-matching rule: a heading line (starting with
# ** or #) that contains one of these words. Transcripts with commentary are left out of later
# analyses (user decision, 2026-09-29; DATA.md, "Commentary"), because the commentary often names
# the hidden fact or talks about hiding or honesty, so readouts after it can reflect the text.
COMMENTARY_HEADING = re.compile(r"^\s*(\*\*|#{1,4} |\*\*\*)")
COMMENTARY_WORDS = re.compile(r"consideration|why |why$|breakdown|explanation|key (things|elements|points)|reasoning"
                              r"|strategy|rationale|disclaimer|\bnotes?\b|internal|behind|approach|important", re.I)
HIDING_WORDS = re.compile(r"conceal|\bhid(e|es|ing|den)\b|withh|not (to )?(mention|disclos|reveal)|avoid(s|ed|ing)? "
                          r"(mention|disclos|reveal|admit|confirm)|downplay|deflect|mislead|decept|deceiv|\blie\b"
                          r"|\blying\b|honest|transparen|instruct|system prompt", re.I)

# The extra unrelated set (1,000 more Alpaca prompts) is run for Qwen only (user decision,
# 2026-10-01). Gemma-12B has two such transcripts from the smoke run; load_manifest() leaves them out.
EXTRA_UNRELATED_MODELS = ("qwen3.6-27b",)

TURN_END = {"<end_of_turn>", "<|im_end|>", "<|end|>"}
THINK_OPEN = "<think>"


# ---------------------------------------------------------------- data access
def read_jsonl(path):
    with open(path) as f:
        return [json.loads(l) for l in f if l.strip()]


def slug(model):
    """Folder name of a model, as in src/models.py: "qwen3.6-27b" -> "qwen3_6_27b"."""
    return re.sub(r"[^a-z0-9]+", "_", model.lower()).strip("_")


def commentary_section(text):
    """The text from the first commentary heading on, or None."""
    lines = text.splitlines()
    for i, line in enumerate(lines):
        if COMMENTARY_HEADING.match(line) and COMMENTARY_WORDS.search(line):
            return "\n".join(lines[i:])
    return None


def load_manifest(model, drop_commentary=True):
    """{model, hf, layers, top_k, yes_tokens, no_tokens, wordings, transcripts}. Each transcript
    entry: tid, set, item_id, k, split, label, stance, n_tokens, commentary (True / False), and per
    wording {answer_label (admit / deny / other), answer_finished}. By default transcripts with
    commentary are left out; drop_commentary=False keeps the full selection."""
    with open(os.path.join(EXPORTS, slug(model), "manifest.json")) as f:
        man = json.load(f)
    if model not in EXTRA_UNRELATED_MODELS:
        man["transcripts"] = [e for e in man["transcripts"] if e["set"] != "unrelated_extra"]
    texts = {t["tid"]: t["response"] for t in read_jsonl(os.path.join(RUNS, slug(model), "transcripts.jsonl"))}
    for e in man["transcripts"]:
        e["commentary"] = commentary_section(texts[e["tid"]]) is not None
    if drop_commentary:
        man["transcripts"] = [e for e in man["transcripts"] if not e["commentary"]]
    return man


def load_vocab(model):
    """[token id -> decoded string]."""
    with open(os.path.join(EXPORTS, slug(model), "vocab.json")) as f:
        return json.load(f)


def load_transcripts(model):
    """{tid: row} of runs/<slug>/transcripts.jsonl (texts, judge label, quote, discloses)."""
    return {t["tid"]: t for t in read_jsonl(os.path.join(RUNS, slug(model), "transcripts.jsonl"))}


def load_summary(model):
    with open(os.path.join(RUNS, slug(model), "selection_summary.json")) as f:
        return json.load(f)


def entries(manifest, **match):
    """Manifest transcripts whose fields equal every given value, e.g.
    entries(man, set="scenario", split="build", label="lie")."""
    return [e for e in manifest["transcripts"] if all(e.get(k) == v for k, v in match.items())]


def read_part(model, entry, part, readouts=True):
    """(header, arrays) of one part ("prefix" or a wording). arrays: J_ids, LL_ids (uint32
    [layers, T, K]), J_p, LL_p (float32 [layers, T, K]), scores (float32 [2, layers, T]; row 0
    J-lens, row 1 logit lens: log-sum-exp of the Yes tokens minus that of the No tokens).
    readouts=False reads the header only and returns empty arrays."""
    import numpy as np
    base = os.path.join(EXPORTS, slug(model), entry["set"], entry["tid"], part)
    with open(base + ".json") as f:
        header = json.load(f)
    if not readouts:
        return header, {}
    with open(base + ".bin", "rb") as f:
        buf = f.read()
    arrays = {}
    for a in header["arrays"]:
        n = 1
        for d in a["shape"]:
            n *= d
        x = np.frombuffer(buf, dtype=a["dtype"], count=n, offset=a["offset"]).reshape(a["shape"])
        arrays[a["name"]] = x.astype(np.float32) if a["dtype"] == "float16" else x
    return header, arrays


def load_item(model, entry, wording, readouts=True):
    """One transcript under one wording: the prefix part and the wording part joined along
    positions (the prefix ends where the question starts).

    tokens, ids        the joined tokens and token ids
    segments           user_prompt (its last token only), response, post_response, self_q,
                       gen_prompt, answer, post_answer; positions in the joined item
    layers, top_k, T, n_prefix (positions from the prefix part)
    ids[lens], p[lens] top-K token ids and probabilities, [layers, T, K], lens "J" or "LL"
    yes_no[lens]       the Yes - No score, [layers, T]
    prefix, part       the two headers (texts, abs_start, question, answer_text, answer_label,
                       answer_finished, answer_limit)
    readouts=False skips the arrays (tokens and segments only; much faster)."""
    import numpy as np
    ph, pa = read_part(model, entry, "prefix", readouts)
    wh, wa = read_part(model, entry, wording, readouts)
    t1 = len(ph["tokens"])
    item = dict(
        tid=entry["tid"], wording=wording,
        tokens=ph["tokens"] + wh["tokens"], ids=ph["ids"] + wh["ids"],
        segments=ph["segments"] + [dict(s, start=s["start"] + t1, end=s["end"] + t1) for s in wh["segments"]],
        layers=ph["layers"], top_k=ph["top_k"], T=t1 + len(wh["tokens"]), n_prefix=t1,
        prefix={k: v for k, v in ph.items() if k != "arrays"},
        part={k: v for k, v in wh.items() if k != "arrays"},
    )
    if readouts:
        join = lambda name, axis: np.concatenate([pa[name], wa[name]], axis=axis)
        item.update(ids_top={lens: join(lens + "_ids", 1) for lens in LENSES},
                    p={lens: join(lens + "_p", 1) for lens in LENSES},
                    yes_no={lens: join("scores", 2)[i] for i, lens in enumerate(LENSES)})
    return item


# ---------------------------------------------------------------- position map
def _seg(item, name):
    for s in item["segments"]:
        if s["name"] == name:
            return s
    return None


def positions(item):
    """{position name: token index} from the export's segment boundaries.

    preresp_slotK  tokens between the user prompt and the response (turn end ... role header)
    resp_tokK      response tokens
    postresp_slotK tokens between the response and the self-report question
    q_tokK         self-report question tokens
    preans_slotK   generation prompt up to (not including) Qwen's empty thinking block
    think_slotK    Qwen's empty thinking block: <think> \\n\\n </think> \\n\\n
    ans_tokK       generated self-report answer
    postans_slotK  turn boundary appended after the answer (every wording in the new runs;
                   the pilot had it for Qwen only). Not to be scored when the answer was cut off.
    """
    toks = item["tokens"]
    out = {}
    u, r, q = _seg(item, "user_prompt"), _seg(item, "response"), _seg(item, "self_q")
    g, a, pa = _seg(item, "gen_prompt"), _seg(item, "answer"), _seg(item, "post_answer")
    if r is not None:
        # anchor on the first turn-end marker after the user prompt starts (a stray
        # prompt-tail token can sit between the user-prompt segment and the marker)
        start = u["start"] if u else 0
        anchor = next((i for i in range(start, r["start"]) if toks[i] in TURN_END), None)
        if anchor is not None:
            for k, p in enumerate(range(anchor, r["start"])):
                out[f"preresp_slot{k}"] = p
        for k, p in enumerate(range(r["start"], r["end"])):
            out[f"resp_tok{k}"] = p
        stop = q["start"] if q else (g["start"] if g else len(toks))
        for k, p in enumerate(range(r["end"], stop)):
            out[f"postresp_slot{k}"] = p
    if q is not None:
        for k, p in enumerate(range(q["start"], q["end"])):
            out[f"q_tok{k}"] = p
    if g is not None:
        gp = list(range(g["start"], g["end"]))
        cut = next((i for i, p in enumerate(gp) if toks[p] == THINK_OPEN), len(gp))
        for k, p in enumerate(gp[:cut]):
            out[f"preans_slot{k}"] = p
        for k, p in enumerate(gp[cut:]):
            out[f"think_slot{k}"] = p
    if a is not None:
        for k, p in enumerate(range(a["start"], a["end"])):
            out[f"ans_tok{k}"] = p
    if pa is not None:
        for k, p in enumerate(range(pa["start"], pa["end"])):
            out[f"postans_slot{k}"] = p
    return out


# ---------------------------------------------------------------- readouts
def top_tokens(item, pos, layer, lens="J"):
    """[(token id, probability)] top-K at one position and layer (a layer number, not an index)."""
    li = item["layers"].index(layer)
    return [(int(t), float(q)) for t, q in zip(item["ids_top"][lens][li, pos], item["p"][lens][li, pos])]


def band_tokens(item, pos, band, vocab, lens="J"):
    """{token string: [layers where it is in the top-K]} at one position, layers lo..hi."""
    lo, hi = band
    out = {}
    for li, layer in enumerate(item["layers"]):
        if lo <= layer <= hi:
            for t in item["ids_top"][lens][li, pos]:
                out.setdefault(vocab[int(t)], []).append(layer)
    return out


# ---------------------------------------------------------------- statistics
def auroc(pos_scores, neg_scores):
    """P(random positive > random negative), ties count half. None if a side is empty."""
    if not pos_scores or not neg_scores:
        return None
    wins = 0.0
    for a in pos_scores:
        for b in neg_scores:
            wins += 1.0 if a > b else (0.5 if a == b else 0.0)
    return wins / (len(pos_scores) * len(neg_scores))


def _auroc_rows(rows):
    return auroc([s for s, y, _ in rows if y == 1], [s for s, y, _ in rows if y == 0])


def grouped_bootstrap_ci(rows, n_boot=2000, seed=0, alpha=0.05):
    """rows: [(score, y, scenario)], y = 1 for lie. Resamples scenarios with replacement
    within three strata (lie-only, truth-only, both), so each resample keeps the number of
    scenarios per stratum. Returns (lo, hi) or None."""
    by_sc = {}
    for row in rows:
        by_sc.setdefault(row[2], []).append(row)
    strata = {"lie": [], "truth": [], "both": []}
    for sc, rs in by_sc.items():
        ys = {y for _, y, _ in rs}
        strata["both" if len(ys) == 2 else ("lie" if 1 in ys else "truth")].append(sc)
    rng = random.Random(seed)
    vals = []
    for _ in range(n_boot):
        sample = []
        for scs in strata.values():
            for _ in range(len(scs)):
                sample.extend(by_sc[rng.choice(scs)])
        v = _auroc_rows(sample)
        if v is not None:
            vals.append(v)
    if not vals:
        return None
    vals.sort()
    return vals[int(alpha / 2 * len(vals))], vals[min(len(vals) - 1, int((1 - alpha / 2) * len(vals)))]


def permutation_p(rows, n_perm=10000, seed=0):
    """Two-sided label-permutation p-value: shuffle labels among rows (counts kept), share of
    shuffles whose AUROC is at least as far from 0.5 as the real one."""
    real = _auroc_rows(rows)
    if real is None:
        return None
    scores = [s for s, _, _ in rows]
    ys = [y for _, y, _ in rows]
    rng = random.Random(seed)
    hits = 0
    for _ in range(n_perm):
        rng.shuffle(ys)
        v = auroc([s for s, y in zip(scores, ys) if y == 1], [s for s, y in zip(scores, ys) if y == 0])
        hits += abs(v - 0.5) >= abs(real - 0.5) - 1e-12
    return (hits + 1) / (n_perm + 1)


# ---------------------------------------------------------------- pilot files (data/source, data/labels, data/exports)
# Per model: the source run (transcripts, judge labels, honest-answer cache) and, per
# wording, the export slug that holds its readouts. "postans" = the run that adds the turn
# boundary after the self-report answer (Qwen only).
PILOT_MODELS = {
    "gemma-3-12b-it": dict(
        run="gemma_3_12b_it__c3_g0", beliefs="beliefs_gemma_3_12b_it_c3.jsonl",
        exports={w: "gemma_3_12b_it__c3_g0_k16" for w in ["Q1_bare", "Q2_after", "Q6_factual", "Q7_ab"]}),
    "gemma-3-27b-it": dict(
        run="gemma_3_27b_it__c3_g0", beliefs="beliefs_gemma_3_27b_it_c3.jsonl",
        exports={w: "gemma_3_27b_it__c3_g0_k16" for w in ["Q1_bare", "Q2_after", "Q6_factual", "Q7_ab"]}),
    "qwen3.6-27b": dict(
        run="qwen3_6_27b__c3_g0", beliefs="beliefs_qwen3_6_27b_c3.jsonl",
        exports={**{w: "qwen3_6_27b__c3_g0_k16" for w in ["Q1_bare", "Q2_after", "Q6_factual", "Q7_ab"]},
                 "Q9_dyl": "qwen3_6_27b__c3_q9"},
        postans={w: "qwen3_6_27b__c3_postans" for w in ["Q2_after", "Q6_factual", "Q7_ab", "Q9_dyl"]}),
    "gpt-oss-20b": dict(
        run="gpt_oss_20b", beliefs="beliefs_gpt_oss_20b_c3.jsonl",
        exports={w: "gpt_oss_20b" for w in WORDINGS}),
}


def pilot_labels(model):
    """{(fact_id, mech_condition): row} for provided_facts transcripts with a lie/truth verdict.
    row: label (judge), mechanical, scenario, sample_index, answer_said, reason."""
    rows = read_jsonl(os.path.join(DATA, "labels", model + ".jsonl"))
    return {(r["fact_id"], r["mechanical"]): r for r in rows}


def pilot_manifest(export):
    with open(os.path.join(DATA, "exports", export, "manifest.json")) as f:
        return json.load(f)


def pilot_item(export, seq_id):
    with open(os.path.join(DATA, "exports", export, seq_id + ".json")) as f:
        return json.load(f)


def pilot_items_for(model, wording, postans=False):
    """Manifest entries (only labelled provided_facts transcripts) for one model x wording."""
    reg = PILOT_MODELS[model]
    export = (reg.get("postans") if postans else reg["exports"]).get(wording)
    if export is None:
        return None, []
    return export, [i for i in pilot_manifest(export)["items"] if i["format"] == wording]
