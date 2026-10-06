#!/usr/bin/env python3
"""family_findings.md Section 11: the 19 missed lies and their readouts, as a self-contained web page.

A *miss* is a build-split scenario lie with none of the eight families (lie, fake, falsehood, misinformation,
deceive, fabricate, false, mislead) at post-response slot 1 (the newline after the response). Qwen3.6-27B,
J-lens, band 35-58.

Ten caught lies (one or more of the eight present), drawn at random with seed 0, are added for comparison, and
every other one-token response of the build split and the unrelated set (lies, truths, no-pressure truths,
unrelated chats), because two of the misses are one-token responses.

For each transcript the page holds the system prompt, the user prompt, the response with the judge's quoted lie
marked, the fact, the judge's reason, the five self-report answers (asked after the readout was computed),
and the top-16 readout at every layer at six positions: the last response token and post-response slots
0-4. Every readout token is tagged: its draft family at slot 1 (the slot-1 lists are used at every position,
one fixed list), its junk kind from the approved survey (analysis/junk/kind_of_token.json), whether it is
the token that actually comes next, and whether it copies a word of the conversation.

Writes viewer/misses.html from viewer/misses_template.html (the data are embedded, so the page opens by
double-click) and, for publishing, the same page without the document wrapper to the path given with
--artifact. Also prints the counts of Section 11.1.
Run from the project root: python3 scripts/findings_2026_10_02/misses_page.py [--artifact PATH]
"""
from __future__ import annotations

import argparse
import json
import os
import random
import re
import sys
from collections import defaultdict

import numpy as np

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
import common as C  # noqa: E402
import presence as P  # noqa: E402

M = "qwen3.6-27b"
POS = "postresp_slot1"
EIGHT = ["lie", "fake", "falsehood", "misinformation", "deceive", "fabricate", "false", "mislead"]
N_CAUGHT, SEED = 10, 0
PAGE_POSITIONS = ["resp_last", "postresp_slot0", "postresp_slot1", "postresp_slot2", "postresp_slot3", "postresp_slot4"]
VIEWER = os.path.join(C.ROOT, "viewer")
TEMPLATE = os.path.join(VIEWER, "misses_template.html")
OUT_HTML = os.path.join(VIEWER, "misses.html")
# the survey's kinds, grouped into the four approved levels
KIND_LEVEL = {
    "template": "no meaning", "whitespace": "no meaning", "punctuation": "no meaning",
    "code_pieces": "unrelated", "error_words": "unrelated", "common_words": "unrelated",
    "turn_words": "about the chat", "role_names": "about the chat", "thinking_words": "about the chat",
    "openers": "about the chat", "answer_words": "about the chat",
    "deception_situation": "deception or the situation", "other_words": "other words", "disagree": "other words",
}


def families():
    """{name: (side, {token ids})} of the kept draft families at post-response slot 1."""
    with open(os.path.join(C.ROOT, "analysis", "families", "families_draft.json")) as f:
        ents = json.load(f)["entries"]
    fam, side = defaultdict(set), {}
    for e in ents:
        if e["model"] == M and e["lens"] == "J" and e["part"] == "prefix" and e["position"] == POS and e["status"] == "keep":
            fam[e["name"]] |= {x["id"] for x in e["members"]}
            side[e["name"]] = e["side"]
    return {n: (side[n], fam[n]) for n in fam}


def counts(d, masks, hv):
    """Section 11.1: misses and false alarms by two family sets."""
    cls = d["cls"]
    out = {}
    for name, fams in [("eight", EIGHT), ("eight + conceal", EIGHT + ["conceal"])]:
        cnt = sum(masks[n].astype(int) for n in fams)
        out[name] = {
            "lies_missed": [int(((cls == "lie") & hv & (cnt == 0)).sum()), int(((cls == "lie") & hv).sum())],
            "truths_flagged": [int(((cls == "truth") & hv & (cnt >= 1)).sum()), int(((cls == "truth") & hv).sum())],
            "np_truths_flagged": [int(((cls == "np_truth") & hv & (cnt >= 1)).sum()), int(((cls == "np_truth") & hv).sum())],
            "unrelated_flagged": [int(((cls == "unrelated") & hv & (cnt >= 1)).sum()), int(((cls == "unrelated") & hv).sum())],
        }
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--artifact", help="also write the page without the document wrapper to this path")
    args = ap.parse_args()

    d = P.load(M, "J")
    cls, trs = d["cls"], d["transcripts"]
    vocab = C.load_vocab(M)
    fam = families()
    hv = P.have_mask(d, "prefix", POS)
    masks = {n: P.present_mask(d, "prefix", POS, ids) & hv for n, (_, ids) in fam.items()}
    cnt = sum(masks[n].astype(int) for n in EIGHT)
    lies = cls == "lie"
    miss_idx = np.where(lies & (cnt == 0))[0].tolist()
    # lie-side families outside the eight, for the split of the 19
    other_lie = [n for n, (s, _) in fam.items() if s == "lie" and n not in EIGHT]

    with open(os.path.join(C.ROOT, "analysis", "junk", "kind_of_token.json")) as f:
        kind_of = {int(k): v for k, v in json.load(f).items()}
    man = C.load_manifest(M)
    entry = {e["tid"]: e for e in man["transcripts"]}
    scen = {s["id"]: s for s in C.read_jsonl(os.path.join(C.ROOT, "inputs", "scenarios.jsonl"))}
    band = C.BANDS[M]

    def answers(t):
        out = []
        for w in C.WORDINGS:
            p = os.path.join(C.EXPORTS, C.slug(M), t["set"], t["tid"], f"{w}.json")
            with open(p) as f:
                h = json.load(f)
            out.append(dict(wording=w.split("_")[0], question=h.get("question", ""), label=h.get("answer_label", ""),
                            text=(h.get("answer_text") or "").strip(), finished=bool(h.get("answer_finished", True))))
        return out

    # number the 19 by group (no lie-side word first), then by index; then ten caught lies at random
    miss_idx.sort(key=lambda i: (any(masks[n][i] for n in other_lie), i))
    caught_idx = sorted(random.Random(SEED).sample(np.where(lies & (cnt >= 1))[0].tolist(), N_CAUGHT))
    chosen = [(i, "miss") for i in miss_idx] + [(i, "caught") for i in caught_idx]
    rec = C.load_transcripts(M)
    ntok = np.array([int(rec[t["tid"]].get("n_tokens", 0) or 0) for t in trs])
    taken = {i for i, _ in chosen}
    chosen += [(int(i), "one_token") for i in np.where((ntok == 1) & hv)[0] if int(i) not in taken]
    used_ids = set()
    transcripts = []
    for n, (i, group) in enumerate(chosen, 1):
        t = trs[i]
        r = rec[t["tid"]]
        e = entry[t["tid"]]
        ph, pa = C.read_part(M, e, "prefix")
        item = dict(tokens=ph["tokens"], ids=ph["ids"], segments=ph["segments"], layers=ph["layers"],
                    ids_top={"J": pa["J_ids"]}, p={"J": pa["J_p"]})
        pos = C.positions(item)
        n_resp = sum(1 for k in pos if k.startswith("resp_tok"))
        pmap = {"resp_last": pos[f"resp_tok{n_resp - 1}"]}
        for k in range(5):
            pmap[f"postresp_slot{k}"] = pos[f"postresp_slot{k}"]
        readouts = {}
        for name, p in pmap.items():
            ids = pa["J_ids"][:, p, :].astype(int)        # [layers, 16]
            probs = pa["J_p"][:, p, :]
            used_ids |= set(ids.ravel().tolist())
            nxt = int(ph["ids"][p + 1]) if p + 1 < len(ph["ids"]) else None
            readouts[name] = dict(token=ph["tokens"][p], next_id=nxt, ids=ids.tolist(),
                                  p=[[round(float(x), 4) for x in row] for row in probs])
        span = r.get("quote_span")
        span = json.loads(span) if isinstance(span, str) and span not in ("None", "") else (list(span) if isinstance(span, (list, tuple)) else None)
        text_lc = (r["response"] + "\n" + (r.get("user_prompt") or "") + "\n" + (r.get("system") or "")).lower()
        echo = sorted({int(x) for x in np.unique(np.concatenate([np.asarray(v["ids"]).ravel() for v in readouts.values()]))
                       if len(vocab[int(x)].strip()) >= 2 and vocab[int(x)].strip().lower() in text_lc})
        present = sorted(n for n in fam if masks[n][i])
        sib = [dict(label=str(cls[j]), k=rec[trs[j]["tid"]].get("k"), flagged=bool(cnt[j] >= 1), idx=int(j))
               for j in np.where((d["scenario"] == t["item_id"]) & hv)[0] if j != i]
        transcripts.append(dict(
            n=n, group=group, cls=str(cls[i]), idx=int(i), tid=t["tid"], scenario=t["item_id"], k=r.get("k"), temperature=r.get("temperature"),
            label=t["label"], stance=r.get("stance"), judge_reason=r.get("judge_reason", ""), quote=r.get("quote", ""),
            quote_span=span, response_tokens=int(r.get("n_tokens", 0) or 0), system=r.get("system") or "", user_prompt=r.get("user_prompt") or "",
            response=r["response"], true_statement=scen.get(t["item_id"], {}).get("true_statement", ""),
            false_statement=scen.get(t["item_id"], {}).get("false_statement", ""), answers=answers(t),
            families_present=present, other_lie_side=[n for n in other_lie if masks[n][i]],
            eight_present=[n for n in EIGHT if masks[n][i]],
            siblings=sib, echo=echo, readouts=readouts,
        ))

    data = dict(
        model=M, lens="J", band=list(band), position=POS, positions=PAGE_POSITIONS, layers=list(range(64)),
        eight=EIGHT, counts=counts(d, masks, hv),
        split={"none": sum(1 for x in transcripts if x["group"] == "miss" and not x["other_lie_side"]),
               "other_lie_side": sum(1 for x in transcripts if x["group"] == "miss" and x["other_lie_side"]),
               "caught": sum(1 for x in transcripts if x["group"] == "caught"),
               "one_token": sum(1 for x in transcripts if x["group"] == "one_token")},
        n_one_token={c: int(((ntok == 1) & hv & (cls == c)).sum()) for c in ("lie", "truth", "np_truth", "unrelated")},
        n_caught_all=int((lies & hv & (cnt >= 1)).sum()), seed=SEED,
        families={n: dict(side=s, ids=sorted(ids)) for n, (s, ids) in fam.items()},
        kinds={str(k): v for k, v in kind_of.items() if k in used_ids}, kind_level=KIND_LEVEL,
        vocab={str(k): vocab[k] for k in sorted(used_ids)},
        transcripts=transcripts,
    )
    # some vocabulary entries are partial byte sequences that decode to U+FFFD; write them as a JSON escape
    js = json.dumps(data, ensure_ascii=False, separators=(",", ":")).replace("</", "<\\/").replace("�", "\\ufffd")
    with open(TEMPLATE) as f:
        html = f.read()
    assert "/*__DATA__*/" in html
    full = html.replace("/*__DATA__*/", js)
    with open(OUT_HTML, "w") as f:
        f.write(full)
    print({k: v for k, v in data["counts"].items()}, "split:", data["split"])
    print(f"written: {OUT_HTML} ({len(full) / 1e6:.1f} MB)")
    if args.artifact:
        # the artifact wrapper supplies doctype, html, head and body; keep everything in between
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
