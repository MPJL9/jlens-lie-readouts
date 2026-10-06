"""What the J-lens readout holds at the newline after each turn (Qwen; user's hypothesis, 2026-10-04: the
newline holds a description of the text before it). Three looks, all on the build split and the unrelated
chats (the held-out split is never read); band layers 35 to 58; "present" = in the top 16 at one or more
band layers.

  A. Unrelated chats by kind of request (fixed text rules on the prompt): the tokens most over-represented
     at the newline after the request (pre-response slot 1) and at the newline after the response
     (post-response slot 1).
  B. Calculation words (list printed) at each template token around the response, for maths-like requests
     with and without such a word in the prompt, against the other chats. This separates a copy of the
     prompt's word from a description of the task.
  C. The newline after the self-report question (pre-answer slot 1) and after the self-report answer
     (post-answer slot 1), per wording: yes / no and 是否, and the most common word tokens of the unrelated
     chats with their shares among lies and truths.

Reads the exports directly (about three minutes). Run from the project root:
python3 scripts/findings_2026_10_04/newline_holds.py"""
import collections
import os
import re
import sys

import numpy as np

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
import common as C  # noqa: E402
from frequency_tables import part_positions  # noqa: E402
from presence_index import keep, read_ids  # noqa: E402

M = "qwen3.6-27b"
SHORT = {"Q1_bare": "Q1", "Q2_after": "Q2", "Q6_factual": "Q6", "Q7_ab": "Q7", "Q9_dyl": "Q9"}
PREFIX = ["preresp_slot0", "preresp_slot1", "preresp_slot2", "preresp_slot3", "preresp_slot4", "postresp_slot0", "postresp_slot1", "postresp_slot4"]
MATH = r"(?i)calculat|comput|\bsum\b|product of|area|average|how many|solve|equation|[-+*/=]\s*\d|percent|%|convert|multipl|divide"
KINDS = {      # fixed text rules on the prompt
    "maths": lambda p: bool(re.search(r"\d", p) and re.search(MATH, p)),
    "rewrite": lambda p: bool(re.match(r"(?i)\s*(rewrite|edit|rearrange|transform|paraphrase|rephrase|reword)", p)),
    "classify": lambda p: bool(re.match(r"(?i)\s*(classify|categorize|sort)", p)),
    "summarize": lambda p: bool(re.search(r"(?i)summar", p)),
    "translate": lambda p: bool(re.search(r"(?i)translat", p)),
    "list": lambda p: bool(re.match(r"(?i)\s*(name|list|give|provide|suggest)", p)),
    "write": lambda p: bool(re.match(r"(?i)\s*(write|compose|generate|create|construct|make|come up|brainstorm|design)", p)),
    "code": lambda p: bool(re.search(r"(?i)\b(code|program|function|python|algorithm|sql|javascript)\b", p)),
}
CALC = {"calculate", "calculates", "calculated", "calculating", "calculation", "calculations", "compute", "computation", "computing",
        "arithmetic", "math", "mathematics", "mathematical", "计算", "数学", "算", "算术", "运算"}


def main():
    man, vocab = C.load_manifest(M), C.load_vocab(M)
    layers, (lo, hi) = man["layers"], C.BANDS[M]
    lidx = [i for i, l in enumerate(layers) if lo <= l <= hi]
    ents = [e for e in man["transcripts"] if keep(e) and e["set"] in ("scenario", "unrelated", "unrelated_extra")]
    assert not any(e["split"] == "heldout" for e in ents if e["set"] == "scenario")
    prompts = {r["id"]: r["user_prompt"] for f in ("unrelated.jsonl", "unrelated_extra.jsonl") for r in C.read_jsonl(os.path.join(C.ROOT, "inputs", f))}
    rows = []
    for e in ents:
        h, ids = read_ids(M, e, "prefix")
        pp = part_positions(h)
        r = dict(cls="unrelated" if e["set"] != "scenario" else e["label"], item=e["item_id"],
                 pos={("prefix", k): set(np.asarray(ids["J"][lidx, pp[k]]).ravel().tolist()) for k in PREFIX})
        for w in C.WORDINGS:
            h, ids = read_ids(M, e, w)
            pp = part_positions(h)
            r["pos"][(w, "preans_slot1")] = set(np.asarray(ids["J"][lidx, pp["preans_slot1"]]).ravel().tolist())
            if e["wordings"][w]["answer_finished"]:
                r["pos"][(w, "postans_slot1")] = set(np.asarray(ids["J"][lidx, pp["postans_slot1"]]).ravel().tolist())
        rows.append(r)
    un = [r for r in rows if r["cls"] == "unrelated"]
    P = [prompts[r["item"]] for r in un]

    print(f"A. {len(un)} unrelated chats by kind of request: token, chats of the kind with it, share of the other chats")
    for pos in ("preresp_slot1", "postresp_slot1"):
        print(f"  {pos}")
        for kind, rule in KINDS.items():
            m = np.array([rule(p) for p in P])
            c1 = collections.Counter(t for r, mm in zip(un, m) if mm for t in r["pos"][("prefix", pos)])
            c0 = collections.Counter(t for r, mm in zip(un, m) if not mm for t in r["pos"][("prefix", pos)])
            n1, n0 = int(m.sum()), int((~m).sum())
            top = sorted(c1, key=lambda t: c1[t] / n1 - c0[t] / n0, reverse=True)[:7]
            print(f"    {kind:9s} (n={n1}): " + "; ".join(f"{vocab[t]!r} {c1[t]}/{n1} vs {100 * c0[t] / n0:.0f}%" for t in top))

    calc = {i for i, t in enumerate(vocab) if t.strip().lower() in CALC or t.strip() in CALC}
    print("\nB. calculation words:", " ".join(repr(vocab[i]) for i in sorted(calc)))
    maths = np.array([KINDS["maths"](p) for p in P])
    word = np.array([bool(re.search(r"(?i)calculat|comput|arithmetic|\bmath", p)) for p in P])
    print("   position: maths-like with such a word in the prompt | maths-like without | other chats")
    for pos in PREFIX:
        pres = np.array([bool(r["pos"][("prefix", pos)] & calc) for r in un])
        print(f"   {pos:15s} " + " | ".join(f"{int(pres[m].sum())}/{int(m.sum())} ({100 * pres[m].mean():.0f}%)" for m in (maths & word, maths & ~word, ~maths)))

    yn = {i for i, t in enumerate(vocab) if t.strip().lower() in ("yes", "no")}
    sf = {i for i, t in enumerate(vocab) if t.strip() in ("是否", "是不是")}
    wordy = lambda t: bool(re.search(r"[A-Za-z]{2,}|[一-鿿]", vocab[t])) and not vocab[t].startswith("<")
    print("\nC. after the self-report question and after the self-report answer (unrelated | lies | truths, in %)")
    for w in C.WORDINGS:
        for pos in ("preans_slot1", "postans_slot1"):
            g = {c: [r["pos"][(w, pos)] for r in rows if r["cls"] == c and (w, pos) in r["pos"]] for c in ("unrelated", "lie", "truth")}
            cnt = {c: collections.Counter(t for s in v for t in s) for c, v in g.items()}
            sh = lambda ids: " | ".join(f"{100 * np.mean([bool(s & ids) for s in g[c]]):.0f}" for c in g)
            top = [t for t, _ in cnt["unrelated"].most_common(400) if wordy(t)][:12]
            print(f"  {SHORT[w]} {pos} (n {' | '.join(str(len(v)) for v in g.values())}): yes / no {sh(yn)}; 是否 {sh(sf)}")
            print("     " + "; ".join(f"{vocab[t]!r} " + "|".join(f"{100 * cnt[c][t] / len(g[c]):.0f}" for c in g) for t in top))


if __name__ == "__main__":
    main()
