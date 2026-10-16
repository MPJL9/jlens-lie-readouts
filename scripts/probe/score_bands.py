#!/usr/bin/env python3
"""The post's difference-of-means probe (sections 4.4 and 4.6), redone for any of the four models at every
template token of the four bands of scripts/probe/bands.py (user, 2026-10-09: "redoing the probe experiment in the
blog post for other models").

A direction is the mean of the fit set's positives minus the mean of its negatives at one token and layer; a
transcript's score is its position along that direction from the midpoint of the two means; above 0 is the lie
side. Nothing is trained. Three numbers per token, layer and task:
  build split      the direction fitted on four folds and scored on the fifth (scenarios kept together; the folds
                   of Experiment 3): AUROC, lies and truths above 0
  held-out         fitted on the build split, scored on the held-out split: AUROC and balanced accuracy with 95%
                   intervals (2,000 resamples of scenarios, seed 0; at the two key layers only), lies and truths
                   above 0
  both splits      the two splits pooled, five folds: AUROC (for the models whose held-out groups are tiny)
Tasks:
  after the response (prefix part, no question asked): lies against truths, every transcript; also the share of
                   no-pressure truths above 0 and the scenarios with a lie and a truth where the lie scores above
                   its truth (the post's 4.4)
  from the question to after the answer, per wording: "all", lies against truths among the answers that
                   finished and open with yes or no; "deniers", the same among the No answers (the post's 4.6).
                   A task is scored only where the fit set has 10 or more of each class.
The released did-you-lie probe is scored on the same transcripts under Q9 (runs/<model>/dyl_probe.jsonl).
Key layers: the layer of the post's numbers for Qwen (47) and of each model's Experiment 3 pictures (Gemma-12B 29,
Gemma-27B 39; gpt-oss 15, the middle of its band), and the released probe's layer (Qwen 50, Gemma-12B 46,
Gemma-27B 58, gpt-oss 16). Full tables at the key layers; AUROC by layer for every cut layer.
--scale writes a second set of files in which each dimension is divided by its spread (standard deviation) over the
fit set's vectors before every fit (Gemma's residual stream has a few dimensions hundreds of times larger than the
rest, which otherwise drive the direction; scripts/exp3/pictures.py scales Gemma the same way, by the unrelated
chats' spread).

Reproduces the post's Qwen numbers from the existing cuts (checked 2026-10-09, see STATUS.md):
  python3 scripts/probe/score_bands.py --model qwen3.6-27b --data exp3 exp3_heldout exp3_postans exp3_last exp3_heldout_q9 exp3_layer50
  after the response at layer 47 = analysis/heldout/DIRECTION.md; the Q9 tokens at layers 47 and 50 = POSTANS.md.

Data: data/cluster/runs/<model>/exp3_bands/ (cut from inputs/exp3_cut_list_bands_<slug>.jsonl, written by
scripts/probe/list_band_positions.py; the commands are in its docstring). --data names other cut folders under
runs/<model>/ too; several are merged, and the first that holds a transcript's vector at the position and layer
is used. Positions no folder holds are left out; a build-only cut (the Gemma exp3 folders) gives the build-split
numbers only.
Output: analysis/probe/<slug>/BANDS.md, bands.json, fig/bands.png (with --scale also BANDS_scaled.md,
bands_scaled.json, fig/bands_scaled.png). The figure has three panels: after the response (all transcripts); around the Q9
answer, all transcripts; the same among the No answers (user, 2026-10-09: separate plots). --figure-only redraws the
figures from the saved json without scoring.
Usage: python3 scripts/probe/score_bands.py --model gemma-3-12b-it [--data exp3_bands ...] [--layers 29 46] [--scale] [--n-boot 2000]
"""
import argparse
import datetime
import json
import os
import sys
import time

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
SCRIPTS = os.path.dirname(HERE)
for p in (SCRIPTS, os.path.join(SCRIPTS, "exp3"), os.path.join(SCRIPTS, "heldout"), HERE):
    sys.path.insert(0, p)
import common as C  # noqa: E402
import presence as P  # noqa: E402
import pictures as X3  # noqa: E402
import analyze_dyl_probe as A  # noqa: E402
import score_newline_families as H  # noqa: E402
import score_q9_rates as R  # noqa: E402
import bands as B  # noqa: E402

MAIN = {"qwen3.6-27b": 47, "gemma-3-12b-it": 29, "gemma-3-27b-it": 39, "gpt-oss-20b": 15}
NAME = {"qwen3.6-27b": "Qwen3.6-27B", "gemma-3-12b-it": "Gemma-3-12B", "gemma-3-27b-it": "Gemma-3-27B", "gpt-oss-20b": "gpt-oss-20b"}
MIN_FIT = 10
W_POST = "Q9_dyl"
TASKS = {"all": "lies against truths, all transcripts", "deniers": "lies against truths, among the No answers"}
BLUE, ORANGE = X3.COL["truth"], X3.COL["lie"]        # the two validated hues of the chart rules used across the project


# ---------------------------------------------------------------- data
class Cuts:
    """Several cut folders merged: vectors(T, part, name, layer) -> (float64 [n, d], have mask). The first
    folder holding a transcript's vector at the position and layer is used."""

    def __init__(self, folders):
        self.folders, self.where, self.d = [], {}, None
        for path in folders:
            with open(os.path.join(path, "meta.json")) as f:
                meta = json.load(f)
            arr = {s: np.load(os.path.join(path, f"{s}.npy"), mmap_mode="r") for s in meta["sets"]}
            k = len(self.folders)
            self.folders.append(dict(path=path, layers=meta["layers"], arr=arr))
            for s in meta["sets"]:
                for i, r in enumerate(C.read_jsonl(os.path.join(path, f"{s}.jsonl"))):
                    self.where.setdefault((r["tid"], r["part"], r["name"]), []).append((k, s, i, r["position"]))
            d = next(iter(arr.values())).shape[2]
            if self.d is not None and d != self.d:
                sys.exit(f"FATAL: {path} holds vectors of {d} dimensions, the earlier folders {self.d}")
            self.d = d
        self.layers = sorted({l for f in self.folders for l in f["layers"]})

    def names(self):
        return {(part, name) for (_, part, name) in self.where}

    def first(self, part, name):
        """(tid, position) of the first row at a position (to read its token from sequences.jsonl)."""
        for (tid, p, n), hits in self.where.items():
            if p == part and n == name:
                return tid, hits[0][3]
        return None

    def vectors(self, T, part, name, layer):
        picks = []
        for t in T:
            hit = None
            for (k, s, i, _) in self.where.get((t["tid"], part, name), []):
                if layer in self.folders[k]["layers"]:
                    hit = (k, s, i)
                    break
            picks.append(hit)
        have = np.array([p is not None for p in picks], bool)
        X = np.zeros((int(have.sum()), self.d))
        groups = {}
        for j, p in enumerate(p for p in picks if p is not None):
            groups.setdefault((p[0], p[1]), []).append((p[2], j))
        for (k, s), pairs in groups.items():
            li = self.folders[k]["layers"].index(layer)
            rows, js = zip(*sorted(pairs))
            X[list(js)] = self.folders[k]["arr"][s][list(rows), li]
        return X, have


def transcripts(model):
    """Scenario lies and truths and no-pressure truths of both splits (commentary dropped), with each
    wording's answer label and whether the answer finished."""
    out = []
    for e in C.load_manifest(model)["transcripts"]:
        if e["set"] not in ("scenario", "nopressure"):
            continue
        cls = P._class(e)
        if cls == "np_lie":
            continue
        out.append(dict(tid=e["tid"], cls=cls, item=e["item_id"], split=e["split"],
                        answer={w: e["wordings"][w]["answer_label"] for w in C.WORDINGS},
                        finished={w: e["wordings"][w]["answer_finished"] for w in C.WORDINGS}))
    return out


def tokens_at(model, cuts):
    """{(part, name): the token string at that position} from the first transcript the cut holds there."""
    want = {}
    for part, name in cuts.names():
        tid, pos = cuts.first(part, name)
        want.setdefault((tid, part), []).append((name, pos))
    rows = {}
    for r in C.read_jsonl(os.path.join(C.RUNS, C.slug(model), "sequences.jsonl")):
        if (r["tid"], r["part"]) in want:
            rows[(r["tid"], r["part"])] = r          # the last row per transcript and part is the current one (stale smoke-run rows exist)
    out = {}
    for (tid, part), names in want.items():
        for name, pos in names:
            out[(part, name)] = rows[(tid, part)]["tokens"][pos]
    return out


def probe_layer(model):
    path = os.path.join(C.RUNS, C.slug(model), "dyl_probe.jsonl")
    if not os.path.exists(path):
        return None
    with open(path) as f:
        return json.loads(f.readline())["layer"]


# ---------------------------------------------------------------- the direction
def fit(Xf, yf, scale):
    """(unit direction, midpoint, per-dimension spread or None) from the positives and negatives of the fit set."""
    sd = None
    if scale:
        sd = Xf.std(0)
        sd[sd == 0] = 1
        Xf = Xf / sd
    a, b = Xf[yf == 1].mean(0), Xf[yf == 0].mean(0)
    return (a - b) / np.linalg.norm(a - b), (a + b) / 2, sd


def project(X, u, mid, sd):
    if sd is not None:
        X = X / sd
    return (X - mid) @ u


def cv_scores(X, y, g, scale):
    """Each transcript's score on the direction fitted on the other folds (the folds of Experiment 3)."""
    s = np.full(len(y), np.nan)
    for tr, te in X3.folds(y, g):
        s[te] = project(X[te], *fit(X[tr], y[tr], scale))
    return s


def enough(y):
    return (y == 1).sum() >= MIN_FIT and (y == 0).sum() >= MIN_FIT


def cv_summary(X, y, g, scale):
    s = cv_scores(X, y, g, scale)
    r = X3.summary(s, y, g)
    r.update(tp=int((s[y == 1] > 0).sum()), fp=int((s[y == 0] > 0).sum()))
    return r


def heldout_test(Xf, yf, Xt, yt, gt, scale, n_boot):
    """Fitted on the fit set, scored on the test set: AUROC, rates at 0, balanced accuracy; intervals when n_boot > 0
    (the resampling of analyze_dyl_probe.grouped_bootstrap and score_q9_rates.rate_rows, as in the post's 4.6)."""
    s = project(Xt, *fit(Xf, yf, scale))
    pos, neg = s[yt == 1], s[yt == 0]
    out = dict(auroc=A.auroc_np(pos, neg), n=[len(pos), len(neg)], n_fit=[int((yf == 1).sum()), int((yf == 0).sum())],
               tp=int((pos > 0).sum()), fp=int((neg > 0).sum()), balanced_accuracy=float(((pos > 0).mean() + (neg <= 0).mean()) / 2))
    if n_boot:
        rows = [(float(v), int(yy), g) for v, yy, g in zip(s, yt, gt)]
        out["ci"] = A.grouped_bootstrap(rows, n_boot)
        rr = R.rate_rows((s > 0).astype(int), yt, gt, n_boot)
        out.update(ba_ci=rr["balanced_accuracy"]["ci"], tp_ci=rr["tpr"]["ci"], fp_ci=rr["fpr"]["ci"])
    return out


def heldout_after_response(Xf, yf, Xt, Tt, scale, n_boot):
    """The post's 4.4 test: lies, truths and no-pressure truths of the held-out split, the resampling of
    score_newline_families.with_ci (scenarios within has-lie-only / has-truth-only / has-both; no-pressure truths by
    scenario)."""
    s = project(Xt, *fit(Xf, yf, scale))
    rows = [dict(cls=t["cls"], item=t["item"], s=float(v)) for t, v in zip(Tt, s)]
    score = lambda q: q["s"]
    if n_boot:
        H.N_BOOT = n_boot
        r = H.with_ci(rows, {"d": score})["d"]
    else:
        r = H.stats(rows, score)
    lie = {q["item"]: q["s"] for q in rows if q["cls"] == "lie"}
    truth = {q["item"]: q["s"] for q in rows if q["cls"] == "truth"}
    both = sorted(set(lie) & set(truth))
    out = dict(auroc=r["auroc"], n=[r["n"]["lie"], r["n"]["truth"]], n_fit=[int((yf == 1).sum()), int((yf == 0).sum())],
               tp=r["k"]["lie"], fp=r["k"]["truth"], np_truth=[r["k"]["np_truth"], r["n"]["np_truth"]],
               balanced_accuracy=(r["lie"] + 1 - r["truth"]) / 2,
               pairs=[sum(lie[g] > truth[g] for g in both), sum(lie[g] == truth[g] for g in both), len(both)])
    if n_boot:
        out.update(ci=r["ci"]["auroc"], tp_ci=r["ci"]["lie"], fp_ci=r["ci"]["truth"], np_ci=r["ci"]["np_truth"])
        pres = [q for q in rows if q["cls"] in ("lie", "truth")]
        rr = R.rate_rows([int(q["s"] > 0) for q in pres], [int(q["cls"] == "lie") for q in pres], [q["item"] for q in pres], n_boot)
        out["ba_ci"] = rr["balanced_accuracy"]["ci"]
    return out


# ---------------------------------------------------------------- one token, one layer
def after_response(cuts, T, name, layer, scale, n_boot):
    X, have = cuts.vectors(T, "prefix", name, layer)
    Th = [t for t, h in zip(T, have) if h]
    cls, split, item = (np.array([t[k] for t in Th]) for k in ("cls", "split", "item"))
    y = (cls == "lie").astype(int)
    pres = (cls == "lie") | (cls == "truth")
    b, h, test = pres & (split == "build"), pres & (split == "heldout"), split == "heldout"
    out = dict(n=dict(build=[int((b & (y == 1)).sum()), int((b & (y == 0)).sum())],
                      heldout=[int((h & (y == 1)).sum()), int((h & (y == 0)).sum())],
                      np_heldout=int((test & (cls == "np_truth")).sum())))
    if enough(y[b]):
        out["build"] = cv_summary(X[b], y[b], item[b], scale)
        if (y[h] == 1).any() and (y[h] == 0).any():
            if (cls[test] == "np_truth").any():
                out["heldout"] = heldout_after_response(X[b], y[b], X[test], [Th[i] for i in np.flatnonzero(test)], scale, n_boot)
            else:
                out["heldout"] = heldout_test(X[b], y[b], X[h], y[h], item[h], scale, n_boot)
    if h.any() and enough(y[pres]):
        out["pooled"] = cv_summary(X[pres], y[pres], item[pres], scale)
    return out


def around_answer(cuts, T, w, name, layer, task, scale, n_boot):
    Tw = [t for t in T if t["cls"] in ("lie", "truth") and t["finished"][w] and t["answer"][w] in ("deny", "admit")]
    X, have = cuts.vectors(Tw, w, name, layer)
    Th = [t for t, hv in zip(Tw, have) if hv]
    cls, split, item = (np.array([t[k] for t in Th]) for k in ("cls", "split", "item"))
    ans = np.array([t["answer"][w] for t in Th])
    keep = np.ones(len(Th), bool) if task == "all" else ans == "deny"
    X, y, split, item = X[keep], (cls[keep] == "lie").astype(int), split[keep], item[keep]
    b, h = split == "build", split == "heldout"
    out = dict(n=dict(build=[int((b & (y == 1)).sum()), int((b & (y == 0)).sum())],
                      heldout=[int((h & (y == 1)).sum()), int((h & (y == 0)).sum())]))
    if enough(y[b]):
        out["build"] = cv_summary(X[b], y[b], item[b], scale)
        if (y[h] == 1).any() and (y[h] == 0).any():
            out["heldout"] = heldout_test(X[b], y[b], X[h], y[h], item[h], scale, n_boot)
    if h.any() and enough(y):
        out["pooled"] = cv_summary(X, y, item, scale)
    return out


def released_probe(model, T, n_boot):
    """The released did-you-lie probe's score under Q9 on the same transcripts, per task and split: AUROC (with
    interval), and the lies and truths flagged at its shipped threshold."""
    path = os.path.join(C.RUNS, C.slug(model), "dyl_probe.jsonl")
    if not os.path.exists(path):
        return None
    info = {t["tid"]: t for t in T if t["cls"] in ("lie", "truth")}
    rows = [r for r in C.read_jsonl(path) if r["wording"] == W_POST and r["tid"] in info and r["first_token_yes_no"]
            and r["answer_finished"] and info[r["tid"]]["answer"][W_POST] in ("deny", "admit")]
    out = {}
    for task in TASKS:
        for split in ("build", "heldout"):
            sel = [r for r in rows if info[r["tid"]]["split"] == split and (task == "all" or info[r["tid"]]["answer"][W_POST] == "deny")]
            trip = [(r["score"], int(info[r["tid"]]["cls"] == "lie"), info[r["tid"]]["item"]) for r in sel]
            pos, neg = [s for s, yy, _ in trip if yy == 1], [s for s, yy, _ in trip if yy == 0]
            res = dict(auroc=A.auroc_np(pos, neg), n=[len(pos), len(neg)],
                       tp=sum(int(r["flagged"]) for r in sel if info[r["tid"]]["cls"] == "lie"),
                       fp=sum(int(r["flagged"]) for r in sel if info[r["tid"]]["cls"] == "truth"))
            if n_boot and pos and neg:
                res["ci"] = A.grouped_bootstrap(trip, n_boot)
            out[f"{task}/{split}"] = res
    return out


# ---------------------------------------------------------------- tables
def f_auc(r):
    if not r or r.get("auroc") is None:
        return "–"
    return f"{r['auroc']:.2f} ({r['ci'][0]:.2f} to {r['ci'][1]:.2f})" if r.get("ci") else f"{r['auroc']:.2f}"


def f_frac(k, n, ci=None):
    if not n:
        return "–"
    return f"{k}/{n} ({k / n:.0%}" + (f"; {ci[0]:.0%} to {ci[1]:.0%})" if ci else ")")


def f_ba(r):
    if not r or r.get("balanced_accuracy") is None:
        return "–"
    v = r["balanced_accuracy"]
    return f"{v:.2f} ({r['ba_ci'][0]:.2f} to {r['ba_ci'][1]:.2f})" if r.get("ba_ci") else f"{v:.2f}"


def f_build(r):
    if not r:
        return "–"
    return f"{r['auroc']:.2f}; {f_frac(r['tp'], r['n'][0])}; {f_frac(r['fp'], r['n'][1])}"


def f_pairs(p):
    if not p:
        return "–"
    w, t, n = p
    return f"{w} of {n}" + (f" ({t} ties)" if t else "")


def table(header, rows):
    return ["| " + " | ".join(header) + " |", "|" + "---|" * len(header)] + ["| " + " | ".join(r) + " |" for r in rows] + [""]


def counts(res, layers, part, names, task):
    """The fit set's and the held-out split's [lies, truths] of one wording and task: the largest over the tokens and
    layers (a token that no folder holds at a layer has zero counts there)."""
    best = {"build": [0, 0], "heldout": [0, 0]}
    for name in names:
        for l in layers:
            c = res.get((l, part, name, task), {}).get("n")
            if c and sum(c["build"]) + sum(c["heldout"]) > sum(best["build"]) + sum(best["heldout"]):
                best = {"build": c["build"], "heldout": c["heldout"]}
    return best


def by_layer(res, layers, part, names, task, key, tokens):
    """Rows of a tokens x layers table of AUROC for one kind of result ('build', 'heldout' or 'pooled'); None when every
    cell is empty."""
    rows, any_ = [], False
    for name in names:
        cells = []
        for l in layers:
            r = res.get((l, part, name, task), {}).get(key)
            cells.append(f_auc(r))
            any_ |= cells[-1] != "–"
        rows.append([B.label(name, tokens[(part, name)])] + cells)
    return rows if any_ else None


def write_md(path, model, res, probe, layers, key_layers, p_layer, folders, A_names, wordings, BC_names, tokens, T, n_boot, scale):
    nm = NAME[model]
    n = lambda split, cls: sum(t["split"] == split and t["cls"] == cls for t in T)
    L = [f"# The difference-of-means probe at the template tokens: {nm}" + (" (scaled)" if scale else ""), "",
         f"Written by `scripts/probe/score_bands.py` on {datetime.date.today()}. {nm}: the residual stream at every template token of the four bands",
         f"(`scripts/probe/bands.py`), from `{'`, `'.join(os.path.relpath(f, C.ROOT) for f in folders)}`, layers {', '.join(map(str, layers))}. A direction is the mean of the fit set's positives minus the",
         "mean of its negatives at one token and layer; a transcript's score is its position along that direction from the midpoint of the two means;",
         "above 0 is the lie side. Nothing is trained." + (" **Scaled:** before every fit, each dimension is divided by its spread (standard deviation)"
                                                            " over the fit set's vectors." if scale else ""),
         "*Build split*: the direction fitted on four folds and scored on the fifth (scenarios kept together). *Held-out*: fitted on the build split,",
         f"scored on the held-out split; 95% intervals, {n_boot:,} resamples of scenarios (seed 0), at layers {' and '.join(map(str, key_layers))} only. *Both splits*: the two",
         f"splits pooled, five folds. A task is scored only where the fit set has {MIN_FIT} or more of each class (\"–\" otherwise). Above 0 = flagged as a lie.",
         f"Transcripts: build split {n('build', 'lie')} lies, {n('build', 'truth')} truths, {n('build', 'np_truth')} no-pressure truths; held-out {n('heldout', 'lie')}, {n('heldout', 'truth')}, {n('heldout', 'np_truth')}.",
         f"Layer {MAIN[model]}: the layer of the post's numbers (Qwen) or of this model's Experiment 3 pictures" + (f"; layer {p_layer}: the released did-you-lie probe's layer." if p_layer else "."), ""]
    # 1
    L += [f"## 1. After the response (no question asked): lies against truths", ""]
    for l in key_layers:
        L += [f"### Layer {l}", ""]
        rows = []
        for name in A_names:
            r = res.get((l, "prefix", name, "all"), {})
            h = r.get("heldout")
            rows.append([B.label(name, tokens[("prefix", name)]), f_build(r.get("build")), f_auc(h), f_ba(h),
                         f_frac(h["tp"], h["n"][0], h.get("tp_ci")) if h else "–", f_frac(h["fp"], h["n"][1], h.get("fp_ci")) if h else "–",
                         f_frac(h["np_truth"][0], h["np_truth"][1], h.get("np_ci")) if h and h.get("np_truth") else "–",
                         f_pairs(h.get("pairs")) if h else "–", f_auc(r.get("pooled"))])
        L += table(["token", "build split: AUROC; lies above 0; truths above 0", "held-out AUROC", "held-out balanced accuracy", "held-out lies above 0",
                    "held-out truths above 0", "held-out no-pressure truths above 0", "held-out pairs: the lie above its truth", "both splits, five folds: AUROC"], rows)
    # 2
    L += ["## 2. After the response, by layer: AUROC", ""]
    for key, title in (("heldout", "Held-out (fitted on the build split)"), ("build", "Build split, five folds"), ("pooled", "Both splits, five folds")):
        rows = by_layer(res, layers, "prefix", A_names, "all", key, tokens)
        if rows:
            L += [f"**{title}**", ""] + table(["token"] + [f"layer {l}" for l in layers], rows)
    # 3
    if W_POST in wordings:
        L += [f"## 3. Around the self-report answer under Q9 (the post's wording)", ""]
        for l in key_layers:
            for task, tname in TASKS.items():
                rows = []
                for name in BC_names[W_POST]:
                    r = res.get((l, W_POST, name, task), {})
                    h = r.get("heldout")
                    rows.append([B.label(name, tokens[(W_POST, name)]), f_build(r.get("build")), f_auc(h), f_ba(h),
                                 f_frac(h["tp"], h["n"][0], h.get("tp_ci")) if h else "–", f_frac(h["fp"], h["n"][1], h.get("fp_ci")) if h else "–", f_auc(r.get("pooled"))])
                nn = counts(res, [l], W_POST, BC_names[W_POST], task)
                L += [f"### Layer {l}, {tname} (build {nn['build'][0]} / {nn['build'][1]}, held-out {nn['heldout'][0]} / {nn['heldout'][1]})", ""]
                L += table(["token", "build split: AUROC; lies above 0; truths above 0", "held-out AUROC", "held-out balanced accuracy", "held-out lies above 0",
                            "held-out truths above 0", "both splits, five folds: AUROC"], rows)
        if probe:
            L += [f"**The released did-you-lie probe** on the same transcripts (its own layer {p_layer}, the token before the answer), AUROC and, at its shipped threshold, the lies and truths flagged:", ""]
            rows = []
            for task, tname in TASKS.items():
                cells = [tname]
                for split in ("build", "heldout"):
                    r = probe[f"{task}/{split}"]
                    cells.append(f"{f_auc(r)}; {f_frac(r['tp'], r['n'][0])}; {f_frac(r['fp'], r['n'][1])}")
                rows.append(cells)
            L += table(["task", "build split: AUROC; lies flagged; truths flagged", "held-out: AUROC; lies flagged; truths flagged"], rows)
    # 4
    L += ["## 4. Around the self-report answer, every wording, by layer: AUROC", "",
          "Per wording and task, the tokens from the question to after the answer. Counts are the fit set's lies / truths (build split) and the held-out split's.", ""]
    for w in wordings:
        for task, tname in TASKS.items():
            nn = counts(res, layers, w, BC_names[w], task)
            if not sum(nn["build"]) + sum(nn["heldout"]):
                continue
            head = f"{X3.SHORT[w]}, {tname} (build {nn['build'][0]} / {nn['build'][1]}, held-out {nn['heldout'][0]} / {nn['heldout'][1]})"
            if min(nn["build"]) < MIN_FIT:
                L += [f"- **{head}**: not scored, fewer than {MIN_FIT} of a class in the build split.", ""]
                continue
            L += [f"### {head}", ""]
            for key, title in (("heldout", "Held-out (fitted on the build split)"), ("build", "Build split, five folds"), ("pooled", "Both splits, five folds")):
                rows = by_layer(res, layers, w, BC_names[w], task, key, tokens)
                if rows:
                    L += [f"**{title}**", ""] + table(["token"] + [f"layer {l}" for l in layers], rows)
    with open(path, "w") as f:
        f.write("\n".join(L))
    return L


# ---------------------------------------------------------------- figure
def panel(ax, res, part, names, task, layer, tokens, color, title, note):
    """One panel: a dot per token with its interval, dots exactly on the label rows. Held-out AUROC where there is a
    held-out split, else the build split's five-fold AUROC; a note when the task was not scored."""
    held = any(res.get((layer, part, nm, task), {}).get("heldout") for nm in names)
    key = "heldout" if held else "build"
    ys = list(range(len(names)))[::-1]
    drawn = 0
    for yy, nm in zip(ys, names):
        r = res.get((layer, part, nm, task), {}).get(key)
        if not r or r.get("auroc") is None:
            continue
        drawn += 1
        if r.get("ci"):
            ax.plot(r["ci"], [yy, yy], color=color, lw=2, solid_capstyle="butt", zorder=2)
        ax.plot(r["auroc"], yy, "o", color=color, ms=7, mec=X3.SURFACE, mew=0.8, zorder=3)
    ax.axvline(0.5, color=X3.INK2, lw=1, ls=(0, (3, 3)), zorder=1)
    ax.set_yticks(ys)
    ax.set_yticklabels([B.label(nm, tokens[(part, nm)], plain=True) for nm in names], color=X3.INK, fontsize=8.5)
    ax.set_xlim(0.3, 1.0)
    ax.set_xticks([0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0])
    ax.set_xlabel("held-out AUROC (95% interval)" if held else ("AUROC, build split, five folds" if drawn else "AUROC"))
    ax.grid(axis="y", visible=False)
    ax.tick_params(axis="y", length=0)
    ax.set_ylim(-0.6, len(names) - 0.4)
    ax.set_title(title, loc="left", fontsize=9.5, color=X3.INK)
    if not drawn:
        ax.text(0.75, (len(names) - 1) / 2, note, ha="center", va="center", fontsize=9, color=X3.INK2, wrap=True)


def figure(path, model, res, layers, key_layers, p_layer, A_names, wordings, BC_names, tokens, scale):
    """Three panels: after the response (lies against truths, all transcripts) at the main layer; around the Q9 answer
    at the probe's layer, all transcripts; the same among the No answers."""
    plt = X3.style()
    l_a = MAIN[model] if MAIN[model] in layers else key_layers[0]
    l_b = p_layer if p_layer in layers else l_a
    w = W_POST if W_POST in wordings else (wordings[0] if wordings else None)
    rows_a = max(len(A_names), 2)
    if w:
        names = BC_names[w]
        nn = counts(res, [l_b], w, names, "deniers")
        note = (f"not scored: fewer than {MIN_FIT} lies or truths answer No in the build split\n({nn['build'][0]} lies, {nn['build'][1]} truths)")
        fig = plt.figure(figsize=(12.4, 0.42 * (rows_a + len(names)) + 3.2))
        gs = fig.add_gridspec(2, 2, height_ratios=[rows_a + 2.2, len(names) + 2.2])
        ax_a = fig.add_subplot(gs[0, :])
        ax_b, ax_c = fig.add_subplot(gs[1, 0]), fig.add_subplot(gs[1, 1])
        panel(ax_b, res, w, names, "all", l_b, tokens, BLUE, f"Around the {X3.SHORT[w]} answer, layer {l_b}: all transcripts", "")
        panel(ax_c, res, w, names, "deniers", l_b, tokens, ORANGE, f"Around the {X3.SHORT[w]} answer, layer {l_b}: among the No answers", note)
    else:
        fig, ax_a = plt.subplots(figsize=(7, 0.42 * rows_a + 2.4))
    panel(ax_a, res, "prefix", A_names, "all", l_a, tokens, BLUE, f"After the response, layer {l_a}: all transcripts", "")
    fig.tight_layout(rect=[0, 0, 1, 1 - 0.62 / fig.get_figheight()], h_pad=2.5, w_pad=3)
    X3.finish(plt, fig, path, f"{NAME[model]}: the difference-of-means probe at the template tokens" + (" (scaled)" if scale else ""),
              "Lies against truths. A dot is one token; the line is its 95% interval (scenarios resampled). 0.5 is chance.")


def from_json(path):
    """(res, layers, key_layers, probe layer, A_names, wordings, BC_names, tokens) read back from a bands json."""
    with open(path) as f:
        J = json.load(f)
    res = {}
    for k, r in J["results"].items():
        layer, part, name, task = k.split("/")
        res[(int(layer), part, name, task)] = r
    tokens = {tuple(k.split("/")): t for k, t in J["tokens"].items()}
    A_names = sorted((n for p, n in tokens if p == "prefix" and B.band(n) == "after_response"), key=B.order_key)
    wordings = [w for w in C.WORDINGS if any(p == w and B.band(n) in ("before_answer", "answer", "after_answer") for p, n in tokens)]
    BC_names = {w: sorted((n for p, n in tokens if p == w and B.band(n) in ("before_answer", "answer", "after_answer")), key=B.order_key) for w in wordings}
    return res, J["layers"], J["key_layers"], J["probe_layer"], A_names, wordings, BC_names, tokens


# ---------------------------------------------------------------- main
def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--model", required=True, choices=C.MODELS)
    ap.add_argument("--data", nargs="+", help="cut folders under data/cluster/runs/<model>/ (default: exp3_bands, else exp3)")
    ap.add_argument("--layers", type=int, nargs="+", help="default: every layer the cuts hold")
    ap.add_argument("--scale", action="store_true", help="also write the scaled variant (BANDS_scaled.md, ...)")
    ap.add_argument("--n-boot", type=int, default=2000, help="resamples for the intervals (0: no intervals)")
    ap.add_argument("--out", help="default: analysis/probe/<slug>/")
    ap.add_argument("--figure-only", action="store_true", help="redraw fig/bands.png (and _scaled) from the saved json, no scoring")
    args = ap.parse_args()
    model = args.model
    if args.figure_only:
        out_dir = args.out or os.path.join(C.ROOT, "analysis", "probe", C.slug(model))
        for scale in ([False, True] if args.scale else [False]):
            tag = "_scaled" if scale else ""
            jp = os.path.join(out_dir, f"bands{tag}.json")
            if not os.path.exists(jp):
                sys.exit(f"FATAL: {jp} is not there")
            figure(os.path.join(out_dir, "fig", f"bands{tag}.png"), model, *from_json(jp), scale)
            print(f"written: {os.path.join(out_dir, 'fig', f'bands{tag}.png')}")
        return
    run = os.path.join(C.RUNS, C.slug(model))
    data = args.data or (["exp3_bands"] if os.path.exists(os.path.join(run, "exp3_bands", "meta.json")) else ["exp3"])
    folders = [os.path.join(run, d) for d in data]
    for f in folders:
        if not os.path.exists(os.path.join(f, "meta.json")):
            sys.exit(f"FATAL: {f} is not there. Cut it on the cluster and pull it first (scripts/probe/list_band_positions.py).")
    out_dir = args.out or os.path.join(C.ROOT, "analysis", "probe", C.slug(model))
    os.makedirs(os.path.join(out_dir, "fig"), exist_ok=True)

    T = transcripts(model)
    cuts = Cuts(folders)
    layers = [l for l in cuts.layers if not args.layers or l in args.layers]
    if not layers:
        sys.exit(f"FATAL: the cuts hold layers {cuts.layers}, none of {args.layers}")
    p_layer = probe_layer(model)
    key_layers = [l for l in dict.fromkeys([MAIN[model], p_layer]) if l in layers] or [layers[len(layers) // 2]]
    tokens = tokens_at(model, cuts)
    names = cuts.names()
    A_names = sorted((n for p, n in names if p == "prefix" and B.band(n) == "after_response"), key=B.order_key)
    wordings = [w for w in C.WORDINGS if any(p == w and B.band(n) in ("before_answer", "answer", "after_answer") for p, n in names)]
    BC_names = {w: sorted((n for p, n in names if p == w and B.band(n) in ("before_answer", "answer", "after_answer")), key=B.order_key) for w in wordings}
    print(f"{NAME[model]}: {len(T)} transcripts; layers {layers} (intervals at {key_layers}); after the response: {A_names}; "
          f"wordings {[X3.SHORT[w] for w in wordings]}: {BC_names[wordings[0]] if wordings else []}", flush=True)

    t0 = time.time()
    for scale in ([False, True] if args.scale else [False]):
        res = {}
        for layer in layers:
            nb = args.n_boot if layer in key_layers else 0
            for name in A_names:
                res[(layer, "prefix", name, "all")] = after_response(cuts, T, name, layer, scale, nb)
            for w in wordings:
                for name in BC_names[w]:
                    for task in TASKS:
                        res[(layer, w, name, task)] = around_answer(cuts, T, w, name, layer, task, scale, nb)
            print(f"  layer {layer}{' (scaled)' if scale else ''}: done ({time.time() - t0:.0f} s)", flush=True)
        probe = released_probe(model, T, args.n_boot)
        tag = "_scaled" if scale else ""
        md = os.path.join(out_dir, f"BANDS{tag}.md")
        L = write_md(md, model, res, probe, layers, key_layers, p_layer, folders, A_names, wordings, BC_names, tokens, T, args.n_boot, scale)
        with open(os.path.join(out_dir, f"bands{tag}.json"), "w") as f:
            json.dump(dict(model=model, scale=scale, layers=layers, key_layers=key_layers, probe_layer=p_layer, folders=folders, n_boot=args.n_boot,
                           tokens={f"{p}/{n}": t for (p, n), t in tokens.items()},
                           results={f"{l}/{p}/{n}/{t}": r for (l, p, n, t), r in res.items()}, released_probe=probe), f, indent=1)
        figure(os.path.join(out_dir, "fig", f"bands{tag}.png"), model, res, layers, key_layers, p_layer, A_names, wordings, BC_names, tokens, scale)
        print("\n".join(L[11:]))
        print(f"written: {md}, {os.path.join(out_dir, f'bands{tag}.json')}, {os.path.join(out_dir, 'fig', f'bands{tag}.png')}")


if __name__ == "__main__":
    main()
