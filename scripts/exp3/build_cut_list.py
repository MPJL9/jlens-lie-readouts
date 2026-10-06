#!/usr/bin/env python3
"""Experiment 3, step 1 (Mac): list the template positions whose residual streams are cut on the
cluster.

One model per run. Transcripts: the build split of the scenario and no-pressure sets, and the
unrelated sets the model has; transcripts with commentary are left out (common.load_manifest). The
held-out split is listed only with --heldout.

Positions on Qwen (user, 2026-10-03):
  prefix part   preresp_slot4   the newline after `assistant`, right before the response (control:
                                a scenario's lie and truth share the same prompt up to here)
                postresp_slot0  the turn-end token after the response (control: empty readout)
                postresp_slot1  the newline after it
  each wording  preans_slot1    the newline after the question
                preans_slot4    the newline after `assistant`
                think_slot2     `</think>`
                postans_slot1, postans_slot4   the two newlines after the self-report answer
                                (only when the answer finished)
On Gemma (user, 2026-10-03: "the same thing for gemma"): the same positions with Gemma's tokens
(`<end_of_turn>`, `model`), without `</think>` (Gemma has no thinking block) and with preans_slot2,
the turn-start token after the question, where Gemma's readout carries a signal
(family_findings.md Section 8).

--last (user, 2026-10-04; Qwen only): list one position per wording and nothing else, the last
token before the self-report answer, where the DYL probe reads: think_slot3, the blank line after
`</think>`. On Gemma that token is preans_slot4, already in the list above. The list goes to
inputs/exp3_cut_list_last.jsonl and is cut into its own folder (OUT=exp3_last in slurm/exp3_cut.sh),
because the cut job skips a set that is already cut.

--heldout (user, 2026-10-05; Qwen only): list the held-out split of the scenario and no-pressure sets and
nothing else, at the three positions of the prefix part (no self-report wording). It is for one test fixed in
advance: the lie-minus-truth direction of the build split at the newline after the response, scored on the
held-out transcripts (scripts/heldout/score_newline_direction.py). The list goes to
inputs/exp3_cut_list_heldout.jsonl and is cut into its own folder (OUT=exp3_heldout in slurm/exp3_cut.sh).
Building the list reads the token positions of the held-out transcripts, not their labels or readouts.

--heldout-q9 (user, 2026-10-05; Qwen only): list the held-out split of the scenario set under the wording Q9
and nothing else, at two positions: think_slot3, the last token before the self-report answer (where the
released probe reads), and postans_slot1, the newline after the answer (when the answer finished). It is for
the test fixed in scripts/heldout/score_q9_directions.py. The list goes to
inputs/exp3_cut_list_heldout_q9.jsonl and is cut into OUT=exp3_heldout_q9.

--layer50 (user, 2026-10-05, third session; Qwen only): the positions needed to put the three probe positions of the
post on one layer, the released probe's layer 50: postresp_slot1, the newline after the response, on BOTH splits
of the scenario and no-pressure sets; and postans_slot1, the newline after the self-report answer under Q9 (when
the answer finished), on the build split only (the held-out split has it at layer 50 in exp3_heldout_q9 already;
think_slot3 is at layer 50 on both splits already: exp3_last and exp3_heldout_q9). The list goes to
inputs/exp3_cut_list_layer50.jsonl and is cut with LAYERS="50" into OUT=exp3_layer50. Scored by
scripts/heldout/score_layer50.py.

--postans (user, 2026-10-05, third session; Qwen only): does the newline after the self-report answer matter, or
does any token after the answer do? Under Q9, both splits, scenario set, finished answers: think_slot3 (the last
token before the answer), ans_tok0 (the answer token itself, Yes / No / yes / no, not checked against a fixed
token), and the five tokens of the turn boundary appended after the answer: postans_slot0 `<|im_end|>`, slot1
`\\n`, slot2 `<|im_start|>`, slot3 `user`, slot4 `\\n`. The list goes to inputs/exp3_cut_list_postans.jsonl and is
cut with LAYERS="47 50" into OUT=exp3_postans. Scored by scripts/heldout/score_postans.py.

Output: inputs/exp3_cut_list.jsonl for Qwen, inputs/exp3_cut_list_<slug>.jsonl for the other
models; one row per transcript x part: tid, set, part, names, positions (absolute token
positions), ids (the token id expected at each position; the cluster job checks them against the
cache). inputs/ is pushed by scripts/push_to_cluster.sh.

Usage: python3 scripts/exp3/build_cut_list.py [--model gemma-3-12b-it] [--last | --heldout | --heldout-q9 | --layer50]
"""
import argparse
import collections
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import common as C  # noqa: E402

QWEN = "qwen3.6-27b"
POSTANS = {"postans_slot1": "\n", "postans_slot4": "\n"}
LAST = {QWEN: {"think_slot3": "\n\n"}}       # the last token before the self-report answer (--last)


def wanted(model):
    """(prefix positions, wording positions): {position name: the token expected there}."""
    if model == QWEN:
        return ({"preresp_slot4": "\n", "postresp_slot0": "<|im_end|>", "postresp_slot1": "\n"},
                {"preans_slot1": "\n", "preans_slot4": "\n", "think_slot2": "</think>"})
    if model.startswith("gemma"):
        return ({"preresp_slot4": "\n", "postresp_slot0": "<end_of_turn>", "postresp_slot1": "\n"},
                {"preans_slot1": "\n", "preans_slot2": "<start_of_turn>", "preans_slot4": "\n"})
    sys.exit(f"FATAL: no position list for {model}")


def list_path(model, last=False, heldout=False, heldout_q9=False, layer50=False, postans=False):
    name = ("exp3_cut_list" + ("_last" if last else "") + ("_heldout" if heldout else "") + ("_heldout_q9" if heldout_q9 else "")
            + ("_layer50" if layer50 else "") + ("_postans" if postans else "") + ("" if model == QWEN else f"_{C.slug(model)}") + ".jsonl")
    return os.path.join(C.ROOT, "inputs", name)


POSTANS_ALL = {"think_slot3": "\n\n", "ans_tok0": None, "postans_slot0": "<|im_end|>", "postans_slot1": "\n",
               "postans_slot2": "<|im_start|>", "postans_slot3": "user", "postans_slot4": "\n"}


def postans_rows(man, rows):
    """--postans: under Q9, both splits, scenario set, finished answers: the token before the answer, the answer
    token, and the five turn-boundary tokens after it. Returns (list rows, transcripts per split, vectors per split
    and position)."""
    out, n_tr, n_vec = [], collections.Counter(), collections.Counter()
    for e in man["transcripts"]:
        if e["set"] != "scenario" or not e["wordings"]["Q9_dyl"]["answer_finished"]:
            continue
        n_tr[e["split"]] += 1
        r = rows[(e["tid"], "Q9_dyl")]
        slots = C.positions(dict(tokens=r["tokens"], segments=r["segments"]))
        for name, token in POSTANS_ALL.items():
            if name not in slots:
                sys.exit(f"FATAL: {e['tid']} Q9_dyl has no {name}")
            if token is not None and r["tokens"][slots[name]] != token:
                sys.exit(f"FATAL: {e['tid']} Q9_dyl {name} is {r['tokens'][slots[name]]!r}, expected {token!r}")
        names = list(POSTANS_ALL)
        out.append(dict(tid=e["tid"], set=e["set"], part="Q9_dyl", names=names,
                        positions=[slots[k] for k in names], ids=[r["ids"][slots[k]] for k in names]))
        for k in names:
            n_vec[(e["split"], k)] += 1
    return out, n_tr, n_vec


def layer50_rows(man, rows):
    """--layer50: the newline after the response on both splits (scenario and no-pressure sets); the newline after
    the Q9 answer on the build split (scenario set, finished answers). Returns (list rows, transcripts per set and
    split, vectors per set and position)."""
    out, n_tr, n_vec = [], collections.Counter(), collections.Counter()
    for e in man["transcripts"]:
        if e["set"] not in ("scenario", "nopressure"):
            continue
        n_tr[f"{e['set']}/{e['split']}"] += 1
        todo = [("prefix", {"postresp_slot1": "\n"})]
        if e["split"] == "build" and e["set"] == "scenario" and e["wordings"]["Q9_dyl"]["answer_finished"]:
            todo.append(("Q9_dyl", {"postans_slot1": "\n"}))
        for part, want in todo:
            r = rows[(e["tid"], part)]
            slots = C.positions(dict(tokens=r["tokens"], segments=r["segments"]))
            for name, token in want.items():
                if r["tokens"][slots[name]] != token:
                    sys.exit(f"FATAL: {e['tid']} {part} {name} is {r['tokens'][slots[name]]!r}, expected {token!r}")
            names = list(want)
            out.append(dict(tid=e["tid"], set=e["set"], part=part, names=names,
                            positions=[slots[k] for k in names], ids=[r["ids"][slots[k]] for k in names]))
            for k in names:
                n_vec[(f"{e['set']}/{e['split']}", k)] += 1
    return out, n_tr, n_vec


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--model", default=QWEN)
    ap.add_argument("--last", action="store_true", help="only the last token before the self-report answer (Qwen: think_slot3)")
    ap.add_argument("--heldout", action="store_true", help="only the held-out split, prefix part only (Qwen; one test fixed in advance)")
    ap.add_argument("--heldout-q9", action="store_true", help="only the held-out scenario transcripts under Q9, two positions (Qwen; one test fixed in advance)")
    ap.add_argument("--layer50", action="store_true", help="the newline after the response on both splits and the newline after the Q9 answer on the build split (Qwen; cut at layer 50)")
    ap.add_argument("--postans", action="store_true", help="under Q9, both splits: the token before the answer, the answer token and the five tokens after it (Qwen)")
    args = ap.parse_args()
    MODEL = args.model
    special = [args.last, args.heldout, args.heldout_q9, args.layer50, args.postans]
    if sum(special) > 1 or (MODEL != QWEN and any(special[1:])):
        sys.exit("FATAL: --last, --heldout, --heldout-q9, --layer50 and --postans are one at a time, and all but --last are for Qwen")
    if args.layer50 or args.postans:
        man = C.load_manifest(MODEL)
        rows = {}
        for r in C.read_jsonl(os.path.join(C.RUNS, C.slug(MODEL), "sequences.jsonl")):
            rows[(r["tid"], r["part"])] = r
        out, n_tr, n_vec = layer50_rows(man, rows) if args.layer50 else postans_rows(man, rows)
        path = list_path(MODEL, layer50=args.layer50, postans=args.postans)
        with open(path, "w") as f:
            for row in out:
                f.write(json.dumps(row) + "\n")
        print(f"{len(out)} rows, {sum(n_vec.values())} vectors -> {path}")
        print("transcripts per set/split:", dict(n_tr))
        for name in (("postresp_slot1", "postans_slot1") if args.layer50 else tuple(POSTANS_ALL)):
            print(f"  {name:15s}", {s: n_vec[(s, name)] for s in n_tr if n_vec[(s, name)]})
        return
    if args.last and MODEL not in LAST:
        sys.exit(f"FATAL: --last is for {list(LAST)}; on {MODEL} the last token before the answer is already in the main list")
    PREFIX, WORDING = ({}, LAST[MODEL]) if args.last else wanted(MODEL)
    POST = {} if args.last else POSTANS
    if args.heldout:
        WORDING, POST = {}, {}
    if args.heldout_q9:
        PREFIX, WORDING, POST = {}, dict(LAST[QWEN]), {"postans_slot1": "\n"}
    held = args.heldout or args.heldout_q9
    parts = ["Q9_dyl"] if args.heldout_q9 else ([] if args.last else ["prefix"]) + ([] if args.heldout else C.WORDINGS)
    man = C.load_manifest(MODEL)
    rows = {}
    for r in C.read_jsonl(os.path.join(C.RUNS, C.slug(MODEL), "sequences.jsonl")):
        rows[(r["tid"], r["part"])] = r          # the last row per transcript and part is the current one
    out, n_vec, n_tr = [], collections.Counter(), collections.Counter()
    for e in man["transcripts"]:
        if (e["split"] == "heldout") != held or (args.heldout_q9 and e["set"] != "scenario"):
            continue
        n_tr[e["set"]] += 1
        for part in parts:
            r = rows[(e["tid"], part)]
            slots = C.positions(dict(tokens=r["tokens"], segments=r["segments"]))
            want = dict(PREFIX) if part == "prefix" else dict(WORDING)
            if part != "prefix" and e["wordings"][part]["answer_finished"]:
                want.update(POST)
            for name, token in want.items():
                if r["tokens"][slots[name]] != token:
                    sys.exit(f"FATAL: {e['tid']} {part} {name} is {r['tokens'][slots[name]]!r}, expected {token!r}")
            names = list(want)
            out.append(dict(tid=e["tid"], set=e["set"], part=part, names=names,
                            positions=[slots[k] for k in names], ids=[r["ids"][slots[k]] for k in names]))
            for k in names:
                n_vec[(e["set"], k)] += 1
    path = list_path(MODEL, args.last, args.heldout, args.heldout_q9)
    with open(path, "w") as f:
        for row in out:
            f.write(json.dumps(row) + "\n")
    print(f"{len(out)} rows, {sum(n_vec.values())} vectors -> {path}")
    print("transcripts per set:", dict(n_tr))
    for name in list(PREFIX) + list(WORDING) + list(POST):
        print(f"  {name:15s}", {s: n_vec[(s, name)] for s in n_tr})


if __name__ == "__main__":
    main()
