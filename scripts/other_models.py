#!/usr/bin/env python3
"""A first look at the other models and at every self-report wording (user, 2026-10-02).

All four models, J-lens, each model's own layer band. No families are needed: the other models have
draft families at the post-response slots only, so the strength of a position is measured token by
token.

For every position, among the scenario transcripts of the build split:
  gap of a token   the share of lies with the token in the band's readout minus the share of truths
  best gap         the largest gap of any token at the position
  shuffled         the same after shuffling the lie / truth labels (mean of 20 shuffles): what "best
                   gap" looks like when there is nothing to find. It is large when the groups are small.
  strong tokens    tokens with a gap of 30 points or more and a truth rate of 10% or less

Also: how each model answers the self-report question, and whether the Qwen findings repeat when
the same words are counted on the other models (words matched by spelling in each vocabulary).

Reads the presence index (build split and unrelated set only; the held-out split is not read).
Writes analysis/other_models/OTHER_MODELS.md and token_gaps.json. Every number is in-sample.

Usage: python3 scripts/other_models.py
"""
from __future__ import annotations

import json
import os
import sys

import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import common as C  # noqa: E402
import presence as P  # noqa: E402

OUT = os.path.join(C.ROOT, "analysis", "other_models")
QWEN = "qwen3.6-27b"
GAP, CAP, SHUFFLES, MIN_GROUP = 0.30, 0.10, 20, 20
LIE_EXTRA = {"謊", "謊言", "说谎", "মিথ্যা", "거짓", "거짓말", "झूठ", "झूठा", "mentira", "mentiras", "🤥", "ложь", "嘘", "Lüge", "mensonge"}
WORDS = {"knowingly": {"knowingly", "Knowingly", "knowing", "Knowing", "明知"},
         "cannot": {"cannot", "Cannot", "CANNOT"},
         "yes": {"yes", "Yes", "YES"}, "no": {"no", "No", "NO"}}


def tk(s):
    s = s.replace("\n", "\\n").replace("\r", "\\r").replace("|", "\\|").replace("`", "'")
    return "␣" + s[1:] if s.startswith(" ") else s


def matrix(d, part, pos, sel):
    """Tokens x selected transcripts: is the token present. Tokens present in fewer than 3 are left out."""
    idx = np.where(sel)[0]
    remap = -np.ones(len(d["transcripts"]), int)
    remap[idx] = np.arange(len(idx))
    toks, rows = [], []
    for t, (ti, _) in d["present"][part][pos].items():
        r = remap[ti.astype(int)]
        r = r[r >= 0]
        if len(r) >= 3:
            v = np.zeros(len(idx), bool)
            v[r] = True
            toks.append(t)
            rows.append(v)
    return toks, (np.array(rows) if rows else np.zeros((0, len(idx)), bool))


def token_gaps():
    rng = np.random.default_rng(0)
    out = {}
    for m in C.MODELS:
        d = P.load(m, "J")
        v = C.load_vocab(m)
        cls = d["cls"]
        for part in ["prefix"] + C.WORDINGS:
            ans = P.answer(d, part) if part != "prefix" else None
            for pos in P.positions(d, part):
                hv = P.have_mask(d, part, pos)
                for cond in (["all"] if part == "prefix" else ["all", "deny"]):
                    sel = hv & np.isin(cls, ["lie", "truth"])
                    if cond == "deny":
                        sel = sel & (ans == "deny")
                    lab = cls[sel] == "lie"
                    if lab.sum() < MIN_GROUP or (~lab).sum() < MIN_GROUP:
                        continue
                    toks, M = matrix(d, part, pos, sel)
                    if not toks:
                        continue
                    a, b = M[:, lab].mean(1), M[:, ~lab].mean(1)
                    null = []
                    for _ in range(SHUFFLES):
                        pl = rng.permutation(lab)
                        pa, pb = M[:, pl].mean(1), M[:, ~pl].mean(1)
                        null.append((pa - pb).max())
                    o, ot = np.argsort(b - a)[:6], np.argsort(a - b)[:4]
                    out[f"{m}|{part}|{pos}|{cond}"] = dict(
                        model=m, part=part, position=pos, cond=cond, lies=int(lab.sum()), truths=int((~lab).sum()),
                        strong=int(((a - b >= GAP) & (b <= CAP)).sum()), strong_truth=int(((b - a >= GAP) & (a <= CAP)).sum()),
                        best=float((a - b).max()), shuffled=float(np.mean(null)),
                        top=[(v[toks[i]], float(a[i]), float(b[i])) for i in o],
                        top_truth=[(v[toks[i]], float(a[i]), float(b[i])) for i in ot])
    return out


def frac(pm, s):
    n = int(s.sum())
    return f"{int((pm & s).sum())}/{n} ({100 * (pm & s).sum() / n:.0f}%)" if n else "–"


def main():
    os.makedirs(OUT, exist_ok=True)
    gaps = token_gaps()
    with open(os.path.join(OUT, "token_gaps.json"), "w") as f:
        json.dump(gaps, f, ensure_ascii=False)
    L = ["# Other models and every self-report wording: a first look (J-lens)", "",
         "Written by `scripts/other_models.py`. Build split only; every number is in-sample. Bands: "
         + ", ".join(f"{m} {C.BANDS[m][0]}-{C.BANDS[m][1]}" for m in C.MODELS) + ".", "",
         "## 1. How each model answers the self-report question", "",
         "Cells are `admit / deny / other`.", "",
         "| model | wording | lies | truths | no-pressure truths | unrelated |", "|---|---|---|---|---|---|"]
    data = {m: P.load(m, "J") for m in C.MODELS}
    for m in C.MODELS:
        d = data[m]
        cls = d["cls"]
        for w in C.WORDINGS:
            ans = P.answer(d, w)
            cell = lambda c: " / ".join(str(int(((cls == c) & (ans == a)).sum())) for a in ("admit", "deny", "other"))  # noqa: E731
            L.append(f"| {m} | {w.split('_')[0]} | {cell('lie')} | {cell('truth')} | {cell('np_truth')} | {cell('unrelated')} |")

    def toks(r, key="top", n=5):
        return ", ".join(f"`{tk(t)}` {100 * a:.0f}/{100 * b:.0f}" for t, a, b in r[key][:n])

    L += ["", "## 2. Post-response slots (before the question)", "",
          "Tokens are shown as `token share of lies/share of truths` in percent.", "",
          "| model | position | lies / truths | best gap | shuffled | strong tokens | tokens with the largest gap |", "|---|---|---|---|---|---|---|"]
    for m in C.MODELS:
        for pos in P.positions(data[m], "prefix"):
            r = gaps.get(f"{m}|prefix|{pos}|all")
            if r:
                L.append(f"| {m} | {pos} | {r['lies']} / {r['truths']} | {100 * r['best']:.0f} | {100 * r['shuffled']:.0f} | {r['strong']} | {toks(r)} |")
    L += ["", "## 3. Template positions after the question", "",
          "Each cell: best gap, the shuffled value in brackets, and one `*` per strong token (at most three). All",
          "scenario transcripts of the build split (lies against truths, whatever the answer).", ""]
    for m in C.MODELS:
        d = data[m]
        poss = [p for p in P.positions(d, "Q9_dyl") if not p.startswith("q_tok")]
        L += [f"**{m}** (lies / truths: {int((d['cls'] == 'lie').sum())} / {int((d['cls'] == 'truth').sum())})", "",
              "| position | " + " | ".join(w.split("_")[0] for w in C.WORDINGS) + " |", "|---|" + "---|" * len(C.WORDINGS)]
        for pos in poss:
            cells = []
            for w in C.WORDINGS:
                r = gaps.get(f"{m}|{w}|{pos}|all")
                cells.append(f"{100 * r['best']:.0f} ({100 * r['shuffled']:.0f}) {'*' * min(3, r['strong'])}" if r else "–")
            L.append(f"| {pos} | " + " | ".join(cells) + " |")
        L.append("")
    L += ["## 4. The strongest positions after the question, per model", "",
          "The twelve positions with the largest best gap above the shuffled value. Question tokens included.", ""]
    for m in C.MODELS:
        for cond, title in (("all", "all scenario transcripts"), ("deny", "among the transcripts that deny")):
            rows = sorted([r for r in gaps.values() if r["model"] == m and r["part"] != "prefix" and r["cond"] == cond],
                          key=lambda r: r["shuffled"] - r["best"])[:12]
            if not rows:
                continue
            L += [f"**{m}, {title}**", "", "| wording | position | lies / truths | best gap | shuffled | strong tokens | more after lies | more after truths |",
                  "|---|---|---|---|---|---|---|---|"]
            for r in rows:
                L.append(f"| {r['part'].split('_')[0]} | {r['position']} | {r['lies']} / {r['truths']} | {100 * r['best']:.0f} | {100 * r['shuffled']:.0f} | "
                         f"{r['strong']} | {toks(r)} | {toks(r, 'top_truth', 3)} |")
            L.append("")

    with open(os.path.join(C.ROOT, "analysis", "families", "families_draft.json")) as f:
        fd = json.load(f)["entries"]
    qv = C.load_vocab(QWEN)
    lie = set(LIE_EXTRA)
    for e in fd:
        if (e["model"] == QWEN and e["lens"] == "J" and e["part"] == "prefix" and e["position"] == "postresp_slot1"
                and e["status"] == "keep" and e["name"] == "lie"):
            lie |= {qv[x["id"]].strip() for x in e["members"]}
    words = dict(WORDS)
    words["lie words"] = lie
    L += ["## 5. The same words on every model", "",
          "Words are matched by spelling in each model's vocabulary. `lie words` = Qwen's `lie` family at post-response",
          "slot 1 plus forms seen on Gemma (" + ", ".join(sorted(LIE_EXTRA)) + ").", "",
          "| words | model | wording | position | lies | truths | no-pressure truths | unrelated | lies that deny | truths that deny |",
          "|---|---|---|---|---|---|---|---|---|---|"]
    for name in ("lie words", "knowingly", "cannot"):
        for m in C.MODELS:
            d = data[m]
            v = C.load_vocab(m)
            cls = d["cls"]
            ids = [i for i, t in enumerate(v) if t.strip() in words[name]]
            for part in ["prefix"] + C.WORDINGS:
                for pos in P.positions(d, part):
                    if pos.startswith("q_tok"):
                        continue
                    hv = P.have_mask(d, part, pos)
                    pm = P.present_mask(d, part, pos, ids)
                    a = (pm & hv & (cls == "lie")).sum() / max(1, (hv & (cls == "lie")).sum())
                    b = (pm & hv & (cls == "truth")).sum() / max(1, (hv & (cls == "truth")).sum())
                    if not (abs(a - b) >= 0.20 or (part == "prefix" and pos == "postresp_slot1")):
                        continue
                    deny = ["", ""]
                    if part != "prefix":
                        ans = P.answer(d, part)
                        deny = [frac(pm, hv & (cls == "lie") & (ans == "deny")), frac(pm, hv & (cls == "truth") & (ans == "deny"))]
                    L.append(f"| {name} | {m} | {'–' if part == 'prefix' else part.split('_')[0]} | {pos} | {frac(pm, hv & (cls == 'lie'))} | "
                             f"{frac(pm, hv & (cls == 'truth'))} | {frac(pm, hv & (cls == 'np_truth'))} | {frac(pm, hv & (cls == 'unrelated'))} | {deny[0]} | {deny[1]} |")
    L += ["", "Rows shown: post-response slot 1, and every template position where the lie and truth rates differ by 20",
          "points or more.", "",
          "## 6. `yes` and `no` before the answer, by the answer", "",
          "Scenario transcripts. The position is the last template token before the answer starts.", "",
          "| model | wording | position | yes: admit | yes: deny | no: admit | no: deny |", "|---|---|---|---|---|---|---|"]
    for m in C.MODELS:
        d = data[m]
        v = C.load_vocab(m)
        cls = d["cls"]
        scen = np.isin(cls, ["lie", "truth"])
        y = [i for i, t in enumerate(v) if t.strip() in WORDS["yes"]]
        n = [i for i, t in enumerate(v) if t.strip() in WORDS["no"]]
        for w in ("Q2_after", "Q6_factual", "Q9_dyl"):
            last = [p for p in P.positions(d, w) if p.startswith(("preans", "think"))][-1]
            ans = P.answer(d, w)
            hv = P.have_mask(d, w, last)
            py, pn = P.present_mask(d, w, last, y), P.present_mask(d, w, last, n)
            adm, den = hv & scen & (ans == "admit"), hv & scen & (ans == "deny")
            L.append(f"| {m} | {w.split('_')[0]} | {last} | {frac(py, adm)} | {frac(py, den)} | {frac(pn, adm)} | {frac(pn, den)} |")
    with open(os.path.join(OUT, "OTHER_MODELS.md"), "w") as f:
        f.write("\n".join(L) + "\n")
    print(f"written: {os.path.join(OUT, 'OTHER_MODELS.md')}")


if __name__ == "__main__":
    main()
