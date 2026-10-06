#!/usr/bin/env python3
"""A page for screenshots of single transcripts with their J-lens readouts (Qwen3.6-27B, build split).

The page has one drop-down to choose a transcript, then the transcript (fact, judge, system prompt, user
prompt, response, self-report answers) and the top-16 readout at every layer at six positions: the last
response token and post-response slots 0-4. It opens at slot 1, the newline after the response.

Every readout token gets one of four colours:
  red     a member of one of the ten lie-side families of the draft's Section 4.1 (TEN below);
  orange  a member of any other draft family kept at slot 1 (the other 15 lie-side families, truth side or
          side unclear), or a token of the survey's kind "deception or the situation"
          (analysis/junk/kind_of_token.json);
  gray    a token of the survey's levels "no meaning" or "unrelated";
  plain   everything else.
The slot-1 family lists are used at every position (one fixed list).

English translations of the non-English tokens come from viewer/readout_page_glossary.json. They were
written by Claude and are not checked by a speaker. --missing lists the tokens that still have none.

Which transcripts: --pick SUFFIX:CLASS (the end of the scenario id and lie, truth or np_truth; repeatable),
or, with no --pick, --random N lies drawn with --seed among the lies that have one or more of the ten
families at the newline in the band (138 of the 152 lies).

Writes viewer/readout_page.html from viewer/readout_page_template.html (the data are embedded, so the page
opens by double-click) and, for publishing, the same page without the document wrapper to --artifact.
Run from the project root: python3 scripts/findings_2026_10_04/readout_page.py [--pick ...] [--artifact PATH]
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
# the ten families of the draft's Section 4.1, in the order of its table
TEN = ["lie", "fake", "conceal", "misinformation", "deceive", "falsehood", "fabricate", "false", "mislead", "dishonest"]
PAGE_POSITIONS = ["resp_last", "postresp_slot0", "postresp_slot1", "postresp_slot2", "postresp_slot3", "postresp_slot4"]
VIEWER = os.path.join(C.ROOT, "viewer")
TEMPLATE = os.path.join(VIEWER, "readout_page_template.html")
GLOSSARY = os.path.join(VIEWER, "readout_page_glossary.json")
OUT_HTML = os.path.join(VIEWER, "readout_page.html")
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


def needs_translation(tok):
    """True when the token has a letter outside plain English spelling (Chinese, Korean, accented, ...)."""
    return any(ord(ch) > 127 and ch.isalpha() for ch in tok) and "�" not in tok


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--pick", action="append", default=[], metavar="SUFFIX:CLASS",
                    help="a transcript, by the end of its scenario id and its class (lie, truth, np_truth)")
    ap.add_argument("--random", type=int, default=1, help="with no --pick: how many lies to draw")
    ap.add_argument("--seed", type=int, default=0)
    ap.add_argument("--missing", help="write the non-English tokens that have no translation yet to this path")
    ap.add_argument("--artifact", help="also write the page without the document wrapper to this path")
    args = ap.parse_args()

    d = P.load(M, "J")
    cls, trs = d["cls"], d["transcripts"]
    vocab = C.load_vocab(M)
    fam = families()
    hv = P.have_mask(d, "prefix", POS)
    masks = {n: P.present_mask(d, "prefix", POS, ids) & hv for n, (_, ids) in fam.items()}
    n_ten = sum(masks[n].astype(int) for n in TEN)

    if args.pick:
        chosen = []
        for spec in args.pick:
            suffix, _, want = spec.partition(":")
            hits = [i for i, t in enumerate(trs) if t["item_id"].endswith(suffix) and hv[i] and (not want or cls[i] == want)]
            assert hits, f"no transcript for {spec!r}"
            if len(hits) > 1:
                print(f"{spec}: {len(hits)} transcripts match, all are added:", [(str(cls[i]), trs[i]["tid"]) for i in hits])
            chosen += hits
        how = "picked by hand"
    else:
        cands = np.where((cls == "lie") & hv & (n_ten >= 1))[0].tolist()
        chosen = random.Random(args.seed).sample(cands, args.random)
        how = f"{args.random} drawn at random (seed {args.seed}) from the {len(cands)} lies with one or more of the ten families at the newline"
    print("transcripts:", how)

    with open(os.path.join(C.ROOT, "analysis", "junk", "kind_of_token.json")) as f:
        kind_of = {int(k): v for k, v in json.load(f).items()}
    with open(GLOSSARY) as f:
        glossary = {k: v for k, v in json.load(f).items() if not k.startswith("_")}
    man = C.load_manifest(M)
    entry = {e["tid"]: e for e in man["transcripts"]}
    scen = {s["id"]: s for s in C.read_jsonl(os.path.join(C.ROOT, "inputs", "scenarios.jsonl"))}
    rec = C.load_transcripts(M)
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

    used_ids, band_layers = set(), defaultdict(int)
    transcripts = []
    for n, i in enumerate(chosen, 1):
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
            for layer in range(band[0], band[1] + 1):
                for x in set(ids[layer].tolist()):
                    band_layers[x] += 1
            readouts[name] = dict(token=ph["tokens"][p], ids=ids.tolist(),
                                  p=[[round(float(x), 4) for x in row] for row in probs])
        span = r.get("quote_span")
        span = json.loads(span) if isinstance(span, str) and span not in ("None", "") else (list(span) if isinstance(span, (list, tuple)) else None)
        present = sorted(n2 for n2 in fam if masks[n2][i])
        print(f"  {n}. {cls[i]} {t['item_id']} k{r.get('k')} ({t['tid']}), {r.get('n_tokens')} response tokens; "
              f"of the ten families at the newline: {[x for x in TEN if x in present]}")
        transcripts.append(dict(
            n=n, cls=str(cls[i]), idx=int(i), tid=t["tid"], scenario=t["item_id"], k=r.get("k"), temperature=r.get("temperature"),
            label=t["label"], judge_reason=r.get("judge_reason", ""), quote=r.get("quote", ""), quote_span=span,
            response_tokens=int(r.get("n_tokens", 0) or 0), system=r.get("system") or "", user_prompt=r.get("user_prompt") or "",
            response=r["response"], true_statement=scen.get(t["item_id"], {}).get("true_statement", ""),
            false_statement=scen.get(t["item_id"], {}).get("false_statement", ""), answers=answers(t),
            families_present=present, readouts=readouts,
        ))

    # an empty entry in the glossary marks a word piece: it is known and gets no translation
    gloss = {k: glossary[vocab[k].strip()] for k in sorted(used_ids) if glossary.get(vocab[k].strip())}
    need = [k for k in used_ids if needs_translation(vocab[k].strip())]
    missing = sorted((k for k in need if vocab[k].strip() not in glossary), key=lambda k: (-band_layers[k], vocab[k]))
    print(f"non-English tokens on the page: {len(need)}; translated: {sum(1 for k in need if k in gloss)}; "
          f"marked as word pieces: {sum(1 for k in need if glossary.get(vocab[k].strip()) == '')}; "
          f"without a translation: {len(missing)} ({sum(1 for k in missing if band_layers[k])} of them in the band)")
    if args.missing:
        with open(args.missing, "w") as f:
            for k in missing:
                f.write(f"{band_layers[k]}\t{vocab[k].strip()}\n")
        print(f"written: {args.missing}")

    data = dict(
        model=M, lens="J", band=list(band), position=POS, positions=PAGE_POSITIONS, layers=list(range(64)),
        red=TEN, families={n: dict(side=s, ids=sorted(ids)) for n, (s, ids) in fam.items()},
        kinds={str(k): v for k, v in kind_of.items() if k in used_ids}, kind_level=KIND_LEVEL,
        vocab={str(k): vocab[k] for k in sorted(used_ids)}, gloss={str(k): v for k, v in gloss.items()},
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
    print(f"written: {OUT_HTML} ({len(full) / 1e6:.2f} MB)")
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
