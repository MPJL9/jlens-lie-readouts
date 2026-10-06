#!/usr/bin/env python3
"""Experiment 2 pilot, step 2: a page showing ten transcripts token by token, each response token marked with
the word lists its readout holds (from analysis/pilot/marks.pkl), with the template tokens before and after
the response as their own marks, and a click showing the layer-by-rank readout.

The ten (seed 0): three same-scenario pairs (a lie and a truth from one prompt, both with 60 to 300 response
tokens), one of the 19 lies the newline misses, one caught lie whose quoted lie starts in the first fifth of
the response, one no-pressure truth, one unrelated chat (60 to 300 tokens each). Added on 2026-10-03 at the
user's request: ten lies and ten truths drawn at random (same seed) among the transcripts with a lie-side word
at one or more response tokens held by eight or more band layers (40 to 400 response tokens). That draw used
all ten lie-side families and is kept as drawn; the page's red marks use the lie-side set (the ten without
`false` and `falsehood`, which get their own colour).

To keep thirty transcripts under the page size limit, readout token ids are written as indices into the
page's own vocabulary list, three characters each in a 64-letter alphabet, and probabilities as two.

Writes viewer/response_readouts.html from viewer/response_readouts_template.html (data embedded) and, with
--artifact PATH, the same page without the document wrapper. Run from the project root after
scripts/pilot/response_counts.py: python3 scripts/pilot/pilot_page.py [--artifact PATH]
"""
from __future__ import annotations

import argparse
import json
import os
import pickle
import random
import re
import sys
from collections import defaultdict

import numpy as np

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
import common as C  # noqa: E402
import presence as P  # noqa: E402

M = "qwen3.6-27b"
SEED = 0
LO, HI = 60, 300
VIEWER = os.path.join(C.ROOT, "viewer")
TEMPLATE = os.path.join(VIEWER, "response_readouts_template.html")
OUT_HTML = os.path.join(VIEWER, "response_readouts.html")
EIGHT = ["lie", "fake", "falsehood", "misinformation", "deceive", "fabricate", "false", "mislead"]
N_EXTRA, STRONG, XLO, XHI = 10, 8, 40, 400
TEN = ["lie", "fake", "deceive", "falsehood", "fabricate", "conceal", "misinformation", "false", "mislead", "dishonest"]
POOL = [n for n in TEN if n not in ("false", "falsehood")]     # the lie-side set of the response study (user, 2026-10-03)
# page categories, in the order of priority for a token's colour
CATS = [("ten", POOL), ("truth", ["honest"]), ("fal", ["false", "falsehood"]), ("evade", ["evade", "vague"]),
        ("refuse", ["candid", "disclose", "confess", "refuse"]), ("know", ["knowingly", "cannot"]), ("deny", ["deny"]), ("sit", ["situation"])]
ALPHA = np.array(list("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789-_"))
SLOTS = [f"preresp_slot{k}" for k in range(5)] + [f"postresp_slot{k}" for k in range(5)]


def choose(marks, names):
    rng = random.Random(SEED)
    by_tid = {m["tid"]: m for m in marks}
    ok = lambda m: LO <= m["n"] <= HI  # noqa: E731
    scen = defaultdict(dict)
    for m in marks:
        if m["set"] == "scenario":
            scen[m["item_id"]][m["cls"]] = m
    pairs = [(s["lie"], s["truth"]) for s in scen.values() if "lie" in s and "truth" in s and ok(s["lie"]) and ok(s["truth"])]
    pairs.sort(key=lambda p: p[0]["tid"])
    chosen = []
    for lie, truth in rng.sample(pairs, 3):
        chosen += [(lie, "pair lie"), (truth, "pair truth")]
    # the newline's misses and caught lies, from the presence index
    d = P.load(M, "J")
    hv = P.have_mask(d, "prefix", "postresp_slot1")
    with open(os.path.join(C.ROOT, "analysis", "families", "families_draft.json")) as f:
        ents = json.load(f)["entries"]
    fam = defaultdict(set)
    for e in ents:
        if e["model"] == M and e["lens"] == "J" and e["part"] == "prefix" and e["position"] == "postresp_slot1" and e["status"] == "keep":
            fam[e["name"]] |= {x["id"] for x in e["members"]}
    cnt = sum(P.present_mask(d, "prefix", "postresp_slot1", fam[n]).astype(int) & hv for n in EIGHT)
    tid_of = {t["tid"]: i for i, t in enumerate(d["transcripts"])}
    lies = [m for m in marks if m["cls"] == "lie" and ok(m)]
    taken = {m["tid"] for m, _ in chosen}
    misses = sorted([m for m in lies if cnt[tid_of[m["tid"]]] == 0 and m["tid"] not in taken], key=lambda m: m["tid"])
    chosen.append((rng.choice(misses), "missed lie"))
    taken = {m["tid"] for m, _ in chosen}
    early = sorted([m for m in lies if cnt[tid_of[m["tid"]]] >= 1 and m["quote_span"] and m["quote_span"][0] <= 0.2 * m["n"]
                    and m["n"] >= 100 and m["tid"] not in taken], key=lambda m: m["tid"])
    chosen.append((rng.choice(early), "caught lie, early quote"))
    npt = sorted([m for m in marks if m["cls"] == "np_truth" and ok(m)], key=lambda m: m["tid"])
    chosen.append((rng.choice(npt), "no-pressure truth"))
    unr = sorted([m for m in marks if m["cls"] == "unrelated" and m["set"] == "unrelated" and ok(m)], key=lambda m: m["tid"])
    chosen.append((rng.choice(unr), "unrelated chat"))
    chosen = [(m, role, "pilot") for m, role in chosen]
    taken = {m["tid"] for m, _, _ in chosen}
    ten = [names.index(x) for x in TEN]
    for cls, role, group in (("lie", "lie with lie-side words", "lies"), ("truth", "truth with lie-side words", "truths")):
        pool = sorted([m for m in marks if m["cls"] == cls and XLO <= m["n"] <= XHI and m["tid"] not in taken
                       and (m["strength"][:, ten].max(axis=1) >= STRONG).any()], key=lambda m: m["tid"])
        chosen += [(m, role, group) for m in rng.sample(pool, N_EXTRA)]
    eight_at_newline = {m["tid"]: [n for n in EIGHT if P.present_mask(d, "prefix", "postresp_slot1", fam[n])[tid_of[m["tid"]]]] for m, _, _ in chosen}
    return chosen, eight_at_newline, {n: sorted(v) for n, v in fam.items()}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--artifact")
    args = ap.parse_args()
    with open(os.path.join(C.ROOT, "analysis", "pilot", "marks.pkl"), "rb") as f:
        mk = pickle.load(f)
    names, lists, band = mk["names"], mk["lists"], mk["band"]
    with open(os.path.join(C.ROOT, "analysis", "pilot", "labels.pkl"), "rb") as f:   # from scripts/pilot/where_words_sit.py
        lb = pickle.load(f)
    KINDS, POSITIONS, labels = lb["kinds"], lb["positions"], lb["labels"]
    chosen, eight_nl, fam = choose(mk["marks"], names)
    vocab = C.load_vocab(M)
    man = C.load_manifest(M)
    entry = {e["tid"]: e for e in man["transcripts"]}
    rec = C.load_transcripts(M)
    lidx = list(range(band[0], band[1] + 1))
    raw = []
    used = set()
    for m, role, group in chosen:
        e = entry[m["tid"]]
        h, a = C.read_part(M, e, "prefix")
        pos = C.positions(dict(tokens=h["tokens"], ids=h["ids"], segments=h["segments"]))
        p0 = pos["resp_tok0"]
        ids = np.transpose(a["J_ids"][lidx, p0:p0 + m["n"], :].astype(np.int64), (1, 0, 2)).reshape(-1)   # token-major
        used |= set(np.unique(ids).tolist())
        slots = {}
        for sname in SLOTS:
            if sname in pos:
                p = pos[sname]
                sid = a["J_ids"][:, p, :].astype(np.int64).reshape(-1)
                used |= set(np.unique(sid).tolist())
                slots[sname] = (h["tokens"][p], sid, a["J_p"][:, p, :].reshape(-1))
        raw.append((ids, slots))
    vlist = sorted(used)
    index = np.full(len(vocab), -1, np.int64)
    index[vlist] = np.arange(len(vlist))
    assert len(vlist) < 64 ** 3

    def enc3(x):
        x = index[x]
        return "".join(np.stack([ALPHA[x >> 12], ALPHA[(x >> 6) & 63], ALPHA[x & 63]], axis=1).reshape(-1).tolist())

    def enc2(pr):
        q = np.clip(np.rint(np.asarray(pr, np.float64) * 4095), 0, 4095).astype(np.int64)
        return "".join(np.stack([ALPHA[q >> 6], ALPHA[q & 63]], axis=1).reshape(-1).tolist())

    out = []
    pool = [names.index(x) for x in POOL]
    for n, ((m, role, group), (ids, slots)) in enumerate(zip(chosen, raw), 1):
        e = entry[m["tid"]]
        bits = (m["strength"] > 0).astype(np.int64)
        code = (bits * (1 << np.arange(len(names)))).sum(axis=1).tolist()
        r = rec[m["tid"]]
        out.append(dict(
            n=n, role=role, group=group, cls=m["cls"], tid=m["tid"], scenario=m["item_id"], label=e["label"], stance=r.get("stance"),
            judge_reason=r.get("judge_reason", ""), quote=r.get("quote", ""), quote_span=m["quote_span"], n_tokens=m["n"],
            system=r.get("system") or "", user_prompt=r.get("user_prompt") or "", response=r["response"],
            tokens=m["tokens"], types=m["types"].tolist(), code=code, strength=m["strength"].max(axis=1).tolist(),
            strength_ten=m["strength"][:, pool].max(axis=1).tolist(),
            cs=np.stack([m["strength"][:, [names.index(x) for x in ls]].max(axis=1) for _, ls in CATS], axis=1).tolist(),
            resp_ids=enc3(ids), slots={k: dict(token=tok, ids=enc3(sid), p=enc2(pr)) for k, (tok, sid, pr) in slots.items()},
            eight_at_newline=eight_nl[m["tid"]],
            kind=[KINDS.index(k) for k in labels[m["tid"]]["kind"]], pos=[POSITIONS.index(k) for k in labels[m["tid"]]["pos"]],
            later=labels[m["tid"]]["later"].astype(int).tolist(), place=labels[m["tid"]]["place"].tolist(),
            dspan=labels[m["tid"]]["dspan"], excluded=labels[m["tid"]]["excluded"], matched=labels[m["tid"]]["matched"],
        ))
    with open(os.path.join(C.ROOT, "analysis", "junk", "kind_of_token.json")) as f:
        kinds = {str(int(index[int(k)])): v for k, v in json.load(f).items() if int(k) in used}
    data = dict(model=M, band=band, names=names, slots=SLOTS, seed=SEED, strong=STRONG, kind_names=KINDS, pos_names=POSITIONS,
                cats=[[c, ls] for c, ls in CATS],
                lists={n: [int(index[i]) for i in v if index[i] >= 0] for n, v in lists.items()},
                vocab=[vocab[i] for i in vlist], kinds=kinds, transcripts=out)
    js = json.dumps(data, ensure_ascii=False, separators=(",", ":")).replace("</", "<\\/").replace("�", "\\ufffd")
    with open(TEMPLATE) as f:
        html = f.read()
    assert "/*__DATA__*/" in html
    full = html.replace("/*__DATA__*/", js)
    with open(OUT_HTML, "w") as f:
        f.write(full)
    for t in out:
        print(t["n"], t["group"], t["role"], t["scenario"][-6:], t["n_tokens"], "tokens;", sum(1 for x in t["strength_ten"] if x >= 1), "with a lie-side word,", sum(1 for x in t["strength_ten"] if x >= STRONG), "strong")
    print(f"written: {OUT_HTML} ({len(full) / 1e6:.1f} MB)")
    if args.artifact:
        head, rest = full.split("</head>", 1)
        head = re.sub(r"^.*?<head>", "", head, count=1, flags=re.S)
        head = re.sub(r"<meta [^>]*>\s*", "", head)
        rest = rest.replace("<body>", "", 1)
        rest = rest[: rest.rfind("</body>")]
        with open(args.artifact, "w") as f:
            f.write((head + rest).strip() + "\n")
        print(f"written: {args.artifact}")


if __name__ == "__main__":
    main()
