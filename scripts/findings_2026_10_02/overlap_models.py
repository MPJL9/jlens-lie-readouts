#!/usr/bin/env python3
"""The fuller overlap study (user, 2026-10-02): for each model, which families carry the lie signal
at the newline after the response, and how much they overlap. On Qwen they are the eight families of
family_findings.md Section 9; this script finds the matching set on every model and repeats the
Section 9 study on each.

All four models, J-lens, each model's own layer band, post-response slot 1, build split only.
Families are the draft families as they are (kept entries of analysis/families/families_draft.json,
entries with the same name at the position pooled). Every number is in-sample.

Definitions
  gap            share of lies with the family minus share of truths, in points
  controls       no-pressure truths and unrelated chats
  strict rule    truths and both controls at most 5%, lies at least 50%   (user's decision, 2026-10-02)
  main rule      truths and both controls at most 10%, lies at least 40%  (user's decision, 2026-10-02)
  lie-leaning    lies at least 15%, truths at most 15%, both controls at most 10%, gap at least 10 points
                 (my choice, for the models where the two rules leave nothing: Gemma's truth groups have 30
                 and 32 transcripts, so 15% is four or five of them)

Outputs, under analysis/overlap/:
  OVERLAP_MODELS.md   the tables
  overlap_models.json the numbers behind them

Usage, from the project root: python3 scripts/findings_2026_10_02/overlap_models.py
"""
from __future__ import annotations

import json
import os
import sys
from collections import defaultdict

import numpy as np

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
import common as C  # noqa: E402
import presence as P  # noqa: E402

OUT = os.path.join(C.ROOT, "analysis", "overlap")
POS = "postresp_slot1"
MODELS = ["qwen3.6-27b", "gemma-3-12b-it", "gemma-3-27b-it", "gpt-oss-20b"]
SHORT = {"qwen3.6-27b": "Qwen", "gemma-3-12b-it": "Gemma-12B", "gemma-3-27b-it": "Gemma-27B", "gpt-oss-20b": "gpt-oss"}
EIGHT = ["lie", "fake", "falsehood", "misinformation", "deceive", "fabricate", "false", "mislead"]
STRICT = dict(cap=0.05, floor=0.50)
MAIN = dict(cap=0.10, floor=0.40)
LEAN = dict(lies=0.15, truths=0.15, controls=0.10, gap=0.10)
GROUPS = [("lies", "lie"), ("truths", "truth"), ("no-pressure truths", "np_truth"), ("unrelated", "unrelated")]


def tk(s):
    s = s.replace("\n", "\\n").replace("|", "\\|").replace("`", "'")
    return "␣" + s[1:] if s.startswith(" ") else s


def pct(a, n):
    return f"{a}/{n} ({100 * a / n:.0f}%)" if n else "–"


def load_families(model):
    """{name: (member ids, member tokens, draft side)} for the kept draft families at POS, pooled by name."""
    with open(os.path.join(C.ROOT, "analysis", "families", "families_draft.json")) as f:
        entries = json.load(f)["entries"]
    fams = {}
    for e in entries:
        if not (e["model"] == model and e["lens"] == "J" and e["part"] == "prefix" and e["position"] == POS and e["status"] == "keep"):
            continue
        ids, toks, side = fams.get(e["name"], (set(), [], e["side"]))
        for x in e["members"]:
            if x["id"] not in ids:
                ids.add(x["id"])
                toks.append(x["token"])
        fams[e["name"]] = (ids, toks, side)
    return fams


def rates(pm, hv, cls):
    r = {}
    for _, c in GROUPS:
        g = hv & (cls == c)
        r[c] = (int((pm & g).sum()), int(g.sum()))
    return r


def share(r, c):
    return r[c][0] / r[c][1] if r[c][1] else 0.0


def rule(r):
    """'strict', 'main' or '' : the strictest of the two rules the family meets."""
    t, n, u = share(r, "truth"), share(r, "np_truth"), share(r, "unrelated")
    lie = share(r, "lie")
    if max(t, n, u) <= STRICT["cap"] and lie >= STRICT["floor"]:
        return "strict"
    if max(t, n, u) <= MAIN["cap"] and lie >= MAIN["floor"]:
        return "main"
    return ""


def leaning(r):
    lie, t = share(r, "lie"), share(r, "truth")
    return (lie >= LEAN["lies"] and t <= LEAN["truths"] and max(share(r, "np_truth"), share(r, "unrelated")) <= LEAN["controls"]
            and lie - t >= LEAN["gap"])


def count_table(masks, names, hv, cls, title):
    """Rows 'at least k of the families present' for the four classes."""
    cnt = sum(masks[n].astype(int) for n in names) if names else np.zeros(len(cls), int)
    L = [title, "", "| at least | " + " | ".join(g for g, _ in GROUPS) + " |", "|---|" + "---|" * len(GROUPS)]
    rows = {}
    for k in range(1, len(names) + 1):
        cells = []
        for _, c in GROUPS:
            g = hv & (cls == c)
            cells.append(pct(int(((cnt >= k) & g).sum()), int(g.sum())))
            rows.setdefault(k, {})[c] = [int(((cnt >= k) & g).sum()), int(g.sum())]
        L.append(f"| {k} | " + " | ".join(cells) + " |")
    return L, cnt, rows


def overlap_study(model, d, fams, names, label):
    """The Section 9 study on one set of families. Returns markdown lines and a dict of numbers."""
    cls, hv, scn = d["cls"], P.have_mask(d, "prefix", POS), d["scenario"]
    masks = {n: P.present_mask(d, "prefix", POS, fams[n][0]) & hv for n in names}
    lies, truths = hv & (cls == "lie"), hv & (cls == "truth")
    out = {"families": names}
    L = [f"### {SHORT[model]}: {label} ({len(names)} families" + (": " + ", ".join(names) if names else "") + ")", ""]
    if not names:
        L += ["No family in this set.", ""]
        return L, out
    tab, cnt, rows = count_table(masks, names, hv, cls, "Number of these families present, per transcript:")
    L += tab
    out["at_least"] = rows
    # greedy order: which family adds the most lies not yet caught
    left, order, pool = lies.copy(), [], list(names)
    while pool:
        best = max(pool, key=lambda n: (masks[n] & left).sum())
        order.append((best, int((masks[best] & left).sum())))
        left &= ~masks[best]
        pool.remove(best)
    out["greedy"] = order
    out["lies_with_none"] = int(((cnt == 0) & lies).sum())
    out["truth_counts"] = sorted(cnt[(cnt >= 1) & truths].tolist())
    L += ["", f"- Greedy order (each family with the lies it adds that no earlier family caught): "
          + ", ".join(f"{n} +{k}" for n, k in order) + f". Lies with none of the set: {out['lies_with_none']}/{int(lies.sum())}.",
          f"- Truths with one or more of the set: {len(out['truth_counts'])}/{int(truths.sum())}; how many families each has: "
          + (", ".join(map(str, out["truth_counts"])) or "–") + "."]
    both = sorted(set(scn[lies]) & set(scn[truths]))
    inb = np.isin(scn, both)
    pairs = {}
    for k in (1, 2):
        pairs[k] = [int(((cnt >= k) & lies & inb).sum()), int((lies & inb).sum()), int(((cnt >= k) & truths & inb).sum()), int((truths & inb).sum())]
    out["same_scenario"] = {"scenarios": len(both), "at_least": pairs}
    L.append(f"- Scenarios with both a lie and a truth: {len(both)}. In them, one or more families: lies {pairs[1][0]}/{pairs[1][1]}, "
             f"truths {pairs[1][2]}/{pairs[1][3]}; two or more: lies {pairs[2][0]}/{pairs[2][1]}, truths {pairs[2][2]}/{pairs[2][3]}.")
    if len(names) >= 2:
        L += ["", "Share of the lies with the row family that also have the column family:", "",
              "| A \\ B | " + " | ".join(names) + " |", "|---|" + "---|" * len(names)]
        pw = {}
        for a in names:
            cells = []
            for b in names:
                if a == b:
                    cells.append("–")
                else:
                    na = int((masks[a] & lies).sum())
                    v = (masks[a] & masks[b] & lies).sum() / na if na else 0.0
                    cells.append(f"{100 * v:.0f}%")
                    pw[f"{a}|{b}"] = float(v)
            L.append(f"| {a} ({int((masks[a] & lies).sum())}) | " + " | ".join(cells) + " |")
        out["pairwise"] = pw
    L.append("")
    return L, out


def main():
    os.makedirs(OUT, exist_ok=True)
    data = {m: P.load(m, "J") for m in MODELS}
    fams = {m: load_families(m) for m in MODELS}
    vocab = {m: C.load_vocab(m) for m in MODELS}
    result = {"position": POS, "lens": "J", "strict_rule": STRICT, "main_rule": MAIN, "lie_leaning": LEAN, "models": {}}
    L = ["# Which families carry the lie signal, on each model, and how they overlap", "",
         f"Written by `scripts/findings_2026_10_02/overlap_models.py`. J-lens, post-response slot 1 (the newline after the "
         "response), build split only; every number is in-sample. Bands: "
         + ", ".join(f"{SHORT[m]} {C.BANDS[m][0]}-{C.BANDS[m][1]}" for m in MODELS) + ".", "",
         "Families are the draft families as they are (kept entries, pooled by name at this position). Each model has its",
         "own draft families, so a name such as `lie` has a different token list on each model; Section 3 counts one fixed",
         "list on every model instead.", "",
         "- *gap* = share of lies with the family minus share of truths, in points.",
         f"- *strict rule* = truths and both controls at most {100 * STRICT['cap']:.0f}%, lies at least {100 * STRICT['floor']:.0f}%; "
         f"*main rule* = at most {100 * MAIN['cap']:.0f}% and at least {100 * MAIN['floor']:.0f}% (the user's decision of 2026-10-02).",
         f"- *lie-leaning* = lies at least {100 * LEAN['lies']:.0f}%, truths at most {100 * LEAN['truths']:.0f}%, both controls at most "
         f"{100 * LEAN['controls']:.0f}%, gap at least {100 * LEAN['gap']:.0f} points. This looser bar is my choice: on Gemma the two rules "
         "keep one family or none, and the truth groups are 30 and 32 transcripts, so 15% is four or five of them.", "",
         "## 1. Every lie-leaning family, per model", "",
         "All kept families whose gap is positive, sorted by gap. Families with a gap of 5 points or less are folded into one line.", ""]
    sets = {}
    for m in MODELS:
        d, cls = data[m], data[m]["cls"]
        hv = P.have_mask(d, "prefix", POS)
        rows = []
        for name, (ids, toks, side) in fams[m].items():
            r = rates(P.present_mask(d, "prefix", POS, ids), hv, cls)
            gap = share(r, "lie") - share(r, "truth")
            rows.append(dict(name=name, side=side, tokens=toks, rates=r, gap=gap, rule=rule(r), leaning=leaning(r)))
        rows.sort(key=lambda x: -x["gap"])
        pos_rows = [x for x in rows if x["gap"] > 0]
        big = [x for x in pos_rows if x["gap"] > 0.05]
        small = [x for x in pos_rows if x["gap"] <= 0.05]
        sets[m] = dict(strict=[x["name"] for x in rows if x["rule"] == "strict"],
                       main=[x["name"] for x in rows if x["rule"] in ("strict", "main")],
                       leaning=[x["name"] for x in rows if x["leaning"]])
        n = {c: int((hv & (cls == c)).sum()) for _, c in GROUPS}
        L += [f"### {SHORT[m]} ({len(fams[m])} kept families; lies / truths / no-pressure truths / unrelated = "
              f"{n['lie']} / {n['truth']} / {n['np_truth']} / {n['unrelated']})", "",
              "| family | draft side | members | lies | truths | no-pressure truths | unrelated | gap | rule met | lie-leaning |",
              "|---|---|---|---|---|---|---|---|---|---|"]
        for x in big:
            r = x["rates"]
            L.append(f"| {x['name']} | {x['side']} | " + ", ".join(f"`{tk(t)}`" for t in x["tokens"]) + " | "
                     + " | ".join(pct(*r[c]) for _, c in GROUPS) + f" | +{100 * x['gap']:.0f} | {x['rule'] or '–'} | {'yes' if x['leaning'] else '–'} |")
        if small:
            L.append("| " + ", ".join(f"{x['name']} (+{100 * x['gap']:.0f})" for x in small) + " | | gap of 5 points or less | | | | | | | |")
        if not pos_rows:
            L.append("| (no kept family has a positive gap" + (": " + ", ".join(f"{x['name']} ({x['side']}; {100 * share(x['rates'], 'lie'):.0f}% / {100 * share(x['rates'], 'truth'):.0f}%)" for x in rows) if rows else "") + ") | | | | | | | | | |")
        if m == "gpt-oss-20b":
            L += ["", "Note: gpt-oss's turn boundary is made of different tokens. Qwen and Gemma have `turn end, newline, turn start,",
                  "user, newline`, and the signal sits at the first newline; gpt-oss has `<|end|>, <|start|>, user, <|message|>` with no",
                  "newline, so its post-response slot 1 is `<|start|>`."]
        neg_lie = [x for x in rows if x["gap"] <= 0 and x["side"] == "lie"]
        if neg_lie:
            L += ["", "Draft lie-side families that are not more frequent after lies: "
                  + ", ".join(f"{x['name']} ({100 * share(x['rates'], 'lie'):.0f}% / {100 * share(x['rates'], 'truth'):.0f}%)" for x in neg_lie) + "."]
        L.append("")
        result["models"][m] = dict(n=n, families=[dict(name=x["name"], side=x["side"], tokens=x["tokens"], gap=x["gap"], rule=x["rule"],
                                                      leaning=x["leaning"], rates=x["rates"]) for x in rows], sets=sets[m])

    L += ["## 2. The overlap study on each model's signal set", "",
          "The study of `family_findings.md` Section 9, repeated. Sets: the families that meet the strict rule, those that meet",
          "the main rule (the strict ones included), and the lie-leaning families.", "",
          "| model | strict rule | main rule | lie-leaning |", "|---|---|---|---|"]
    for m in MODELS:
        s = sets[m]
        L.append(f"| {SHORT[m]} | {', '.join(s['strict']) or 'none'} ({len(s['strict'])}) | {', '.join(s['main']) or 'none'} ({len(s['main'])}) | "
                 f"{', '.join(s['leaning']) or 'none'} ({len(s['leaning'])})"
                 + (" — no newline in its turn boundary; slot 1 is `<\\|start\\|>`" if m == "gpt-oss-20b" else "") + " |")
    L.append("")
    for m in MODELS:
        result["models"][m]["overlap"] = {}
        done = set()
        for key, label in (("main", "main rule"), ("leaning", "lie-leaning")):
            names = sets[m][key]
            sig = tuple(names)
            if sig in done:
                L += [f"### {SHORT[m]}: {label} — the same set as above", ""]
                continue
            done.add(sig)
            lines, out = overlap_study(m, data[m], fams[m], names, label)
            L += lines
            result["models"][m]["overlap"][key] = out

    # Section 3: one fixed list per family name, counted on every model
    L += ["## 3. The same families on every model, with one fixed token list each", "",
          "For each family name, the list is the union of the tokens that the drafts of all four models give it at this",
          "position; tokens are matched by spelling (leading space ignored) in each model's vocabulary. The list is shown so",
          "that the rows can be checked. Cells: lies / truths, in percent; `–` = no token of the list is in the model's",
          "vocabulary.", ""]
    names_union = []
    for m in MODELS:
        for x in result["models"][m]["families"]:
            if x["name"] in sets[m]["leaning"] and x["name"] not in names_union:
                names_union.append(x["name"])
    for extra in ("conceal", "hide", "dishonest", "excuse"):
        if extra not in names_union:
            names_union.append(extra)
    fixed = {}
    for name in names_union:
        words = set()
        for m in MODELS:
            if name in fams[m]:
                words |= {t.strip() for t in fams[m][name][1]}
        fixed[name] = sorted(words)
    L += ["| family | fixed list | " + " | ".join(SHORT[m] for m in MODELS) + " |", "|---|---|" + "---|" * len(MODELS)]
    result["fixed_lists"] = {}
    for name in names_union:
        cells = []
        rec = {"list": fixed[name], "models": {}}
        for m in MODELS:
            d, cls = data[m], data[m]["cls"]
            hv = P.have_mask(d, "prefix", POS)
            ids = [i for i, t in enumerate(vocab[m]) if t.strip() in set(fixed[name])]
            if not ids:
                cells.append("–")
                continue
            r = rates(P.present_mask(d, "prefix", POS, ids), hv, cls)
            rec["models"][m] = r
            cells.append(f"{100 * share(r, 'lie'):.0f} / {100 * share(r, 'truth'):.0f}"
                         + (f" (controls {100 * max(share(r, 'np_truth'), share(r, 'unrelated')):.0f})" if max(share(r, 'np_truth'), share(r, 'unrelated')) >= 0.05 else ""))
        result["fixed_lists"][name] = rec
        L.append(f"| {name} | " + ", ".join(f"`{tk(t)}`" for t in fixed[name]) + " | " + " | ".join(cells) + " |")
    L += ["", "A union list is wider than any one model's own list, so a cell can differ from Section 1: Qwen's `false` reads 61",
          "here against 52 there because Gemma-12B's draft puts `falsehood` in its `false` family; Gemma-12B's `evade` reads 27",
          "against 20 because Qwen's draft puts `deflect` and `dodge` in its `evade` family."]
    # Qwen's eight as one count on every model
    L += ["", "Qwen's eight families, each with its fixed list above, counted on every model:", "",
          "| model | one or more | two or more | three or more |", "|---|---|---|---|"]
    result["eight_on_models"] = {}
    for m in MODELS:
        d, cls = data[m], data[m]["cls"]
        hv = P.have_mask(d, "prefix", POS)
        masks = {}
        for name in EIGHT:
            ids = [i for i, t in enumerate(vocab[m]) if t.strip() in set(fixed[name])]
            masks[name] = P.present_mask(d, "prefix", POS, ids) & hv
        cnt = sum(masks[n].astype(int) for n in EIGHT)
        cells, rec = [], {}
        for k in (1, 2, 3):
            parts = []
            for _, c in GROUPS:
                g = hv & (cls == c)
                parts.append(f"{100 * ((cnt >= k) & g).sum() / g.sum():.0f}")
                rec.setdefault(k, {})[c] = [int(((cnt >= k) & g).sum()), int(g.sum())]
            cells.append(" / ".join(parts))
        result["eight_on_models"][m] = rec
        L.append(f"| {SHORT[m]} | " + " | ".join(cells) + " |")
    L += ["", "Cells: lies / truths / no-pressure truths / unrelated, in percent.", ""]

    # Section 4: the other post-response slots, in one line per model
    L += ["## 4. The other post-response slots", "",
          "Number of kept families that meet the main rule (in brackets: the strict rule) at each post-response slot, per model.", "",
          "| model | " + " | ".join(f"slot {k}" for k in range(5)) + " |", "|---|---|---|---|---|---|"]
    with open(os.path.join(C.ROOT, "analysis", "families", "families_draft.json")) as f:
        entries = json.load(f)["entries"]
    result["other_slots"] = {}
    for m in MODELS:
        d, cls = data[m], data[m]["cls"]
        cells = []
        for k in range(5):
            pos = f"postresp_slot{k}"
            if pos not in P.positions(d, "prefix"):
                cells.append("–")
                continue
            hv = P.have_mask(d, "prefix", pos)
            pooled = defaultdict(set)
            for e in entries:
                if e["model"] == m and e["lens"] == "J" and e["part"] == "prefix" and e["position"] == pos and e["status"] == "keep":
                    pooled[e["name"]] |= {x["id"] for x in e["members"]}
            t1, t2, names2 = 0, 0, []
            for name, ids in pooled.items():
                t = rule(rates(P.present_mask(d, "prefix", pos, ids), hv, cls))
                t1 += t == "strict"
                t2 += t in ("strict", "main")
                if t:
                    names2.append(name)
            cells.append(f"{t2} ({t1})" + (": " + ", ".join(names2) if names2 and k != 1 else ""))
            result["other_slots"][f"{m}|{pos}"] = dict(main=t2, strict=t1, names=names2, kept=len(pooled))
        L.append(f"| {SHORT[m]} | " + " | ".join(cells) + " |")
    L.append("")

    with open(os.path.join(OUT, "OVERLAP_MODELS.md"), "w") as f:
        f.write("\n".join(L) + "\n")
    with open(os.path.join(OUT, "overlap_models.json"), "w") as f:
        json.dump(result, f, ensure_ascii=False, indent=1)
    print(f"written: {os.path.join(OUT, 'OVERLAP_MODELS.md')}")


if __name__ == "__main__":
    main()
