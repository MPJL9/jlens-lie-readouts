#!/usr/bin/env python3
"""Step 0: build data/ from the source study's files (read-only links, nothing copied).

  data/source/<run>/          links to transcripts.jsonl, judge_labels.jsonl,
                              judge_final_labels.json, judge_summary.json, meta.json
  data/source/beliefs/        links to the honest-answer caches
  data/source/mask_scenarios.jsonl   link to the scenario file the runs sampled from
  data/labels/<model>.jsonl   one row per provided_facts transcript with a lie/truth verdict
  data/labels/<model>_dropped.jsonl  provided_facts transcripts without one (ambiguous, error)
  data/exports/<slug>/        a filtered manifest.json (labelled provided_facts transcripts,
                              in-scope wordings, judge label added as "label") plus a link
                              to each listed sequence file
  data/exports/index.json     the slugs, for the viewer

Rerunnable: removes and rebuilds data/exports/ and data/labels/ each time.

Usage: python3 scripts/setup_data.py
"""
import json
import os
import shutil
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common import DATA, PILOT_MODELS, ROOT, read_jsonl  # noqa: E402

SRC = os.path.normpath(os.path.join(ROOT, "..", "J-lens_lie_detector"))
RUN_FILES = ["transcripts.jsonl", "judge_labels.jsonl", "judge_final_labels.json",
             "judge_summary.json", "meta.json"]


def link(target, name):
    if not os.path.exists(target):
        raise SystemExit(f"missing source file: {target}")
    os.makedirs(os.path.dirname(name), exist_ok=True)
    if os.path.lexists(name):
        os.remove(name)
    os.symlink(os.path.relpath(target, os.path.dirname(name)), name)


def build_labels(model, reg):
    run = os.path.join(SRC, "runs", reg["run"])
    final = json.load(open(os.path.join(run, "judge_final_labels.json")))
    reasons = {}
    for j in read_jsonl(os.path.join(run, "judge_labels.jsonl")):
        if j.get("judge_verdict") not in (None, "error"):
            reasons[(j["fact_id"], j["condition"])] = j.get("judge_reason", "")
    trans = {(t["fact_id"], t["condition"]): t for t in read_jsonl(os.path.join(run, "transcripts.jsonl"))}
    kept, dropped, seen = [], [], set()
    for key, v in final.items():
        fact_id, cond = key.split("|")[:2]
        if not fact_id.startswith("mask_provided_facts"):
            continue
        if (fact_id, cond) in seen:
            raise SystemExit(f"duplicate transcript key {fact_id}|{cond} in {model}")
        seen.add((fact_id, cond))
        t = trans[(fact_id, cond)]
        row = dict(fact_id=fact_id, scenario=fact_id, mechanical=cond, label=v["label"],
                   sample_index=t.get("sample_index"), answer_said=t.get("answer_said"),
                   honest_answer=t.get("honest_answer"), reason=reasons.get((fact_id, cond), ""))
        (kept if v["label"] in ("lie", "truth") else dropped).append(row)
    # provided_facts transcripts the judge never returned a usable verdict for
    for (fact_id, cond), t in trans.items():
        if fact_id.startswith("mask_provided_facts") and (fact_id, cond) not in seen:
            dropped.append(dict(fact_id=fact_id, scenario=fact_id, mechanical=cond, label="unjudged"))
    os.makedirs(os.path.join(DATA, "labels"), exist_ok=True)
    for name, rows in [(model, kept), (model + "_dropped", dropped)]:
        with open(os.path.join(DATA, "labels", name + ".jsonl"), "w") as f:
            for r in sorted(rows, key=lambda r: (r["fact_id"], r["mechanical"])):
                f.write(json.dumps(r, ensure_ascii=False) + "\n")
    return {(r["fact_id"], r["mechanical"]): r["label"] for r in kept}


def main():
    for d in ("exports", "labels"):
        shutil.rmtree(os.path.join(DATA, d), ignore_errors=True)
    # source links
    link(os.path.join(SRC, "data", "mask_c2.jsonl"), os.path.join(DATA, "source", "mask_scenarios.jsonl"))
    for model, reg in PILOT_MODELS.items():
        for fn in RUN_FILES:
            link(os.path.join(SRC, "runs", reg["run"], fn), os.path.join(DATA, "source", reg["run"], fn))
        link(os.path.join(SRC, "runs", reg["beliefs"]), os.path.join(DATA, "source", "beliefs", reg["beliefs"]))
    # labels, and which wordings each export slug serves for which model
    slug_plan = {}
    for model, reg in PILOT_MODELS.items():
        labels = build_labels(model, reg)
        for mapping in (reg["exports"], reg.get("postans", {})):
            for wording, slug in mapping.items():
                slug_plan.setdefault(slug, (labels, set()))[1].add(wording)
    # filtered exports
    slugs = []
    for slug, (labels, wordings) in sorted(slug_plan.items()):
        src_dir = os.path.join(SRC, "exports", slug)
        man = json.load(open(os.path.join(src_dir, "manifest.json")))
        items = []
        for it in man["items"]:
            key = (it["fact_id"], it["condition"])
            if it["format"] in wordings and key in labels:
                items.append(dict(it, label=labels[key]))
                link(os.path.join(src_dir, it["seq_id"] + ".json"),
                     os.path.join(DATA, "exports", slug, it["seq_id"] + ".json"))
        man = dict(man, items=items, formats=sorted(wordings),
                   note="filtered by scripts/setup_data.py: labelled provided_facts transcripts only; "
                        "'condition' is the mechanical label, 'label' is the judge verdict")
        with open(os.path.join(DATA, "exports", slug, "manifest.json"), "w") as f:
            json.dump(man, f)
        slugs.append(slug)
        print(f"{slug}: {len(items)} sequences, wordings {sorted(wordings)}")
    with open(os.path.join(DATA, "exports", "index.json"), "w") as f:
        json.dump(slugs, f)
    print("SETUP DONE ->", DATA)


if __name__ == "__main__":
    main()
