"""How often the readout holds 作为 ("as", in the sense "in the role of"), 作为一个 ("as a ..."), `AI` and 人工智能
("artificial intelligence"), by class (user's question, 2026-10-04). Qwen, J-lens, band 35 to 58, build split and
unrelated chats (the held-out split is never read). "Present" = in the top 16 at one or more band layers.

Fixed token lists, printed first; simplified and traditional forms are also counted one by one.
  A. The template tokens around the response: the five before it and the five after it.
  B. The template tokens of the self-report round, per wording.
  C. Inside the response: transcripts with the word at one or more response tokens, and response tokens that carry
     it. For the `AI` and 人工智能 lists the counts are repeated without the responses whose own text says "AI" or
     "artificial intelligence" (whole words), because there the readout can show the word as a guess at the next
     token. The English word "as" is in almost every response, so no such exclusion is possible for 作为.

Run from the project root: python3 scripts/findings_2026_10_04/ai_words.py > analysis/findings_2026_10_04/ai_words.md"""
import collections
import os
import re
import sys

import numpy as np

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
import common as C  # noqa: E402
import presence as P  # noqa: E402
from frequency_tables import part_positions  # noqa: E402
from presence_index import keep, read_ids  # noqa: E402

M = "qwen3.6-27b"
SHORT = {"Q1_bare": "Q1", "Q2_after": "Q2", "Q6_factual": "Q6", "Q7_ab": "Q7", "Q9_dyl": "Q9"}
CLASSES = [("lies", "lie"), ("truths", "truth"), ("no-pressure truths", "np_truth"), ("unrelated", "unrelated")]
LISTS = {                                              # exact tokens after stripping spaces
    "作为 / 作為": ["作为", "作為"],
    "作为一个 and the like": ["作为一个", "作为一名", "作为一种", "作为一款", "作为一家", "作为一项"],
    "AI": ["AI", "_AI", ".AI"],
    "人工智能": ["人工智能", "的人工智能"],
    "any of the four lists": None,
}
SINGLE = ["作为", "作為", "作为一个", "作为一名", "身为", "智能", "artificial"]      # counted one by one, for reference
AI_TEXT = re.compile(r"\bAI\b|artificial intelligence", re.I)
ORDER = {"preresp": 0, "postresp": 1, "preans": 2, "think": 3, "postans": 4}


def cls_of(e):
    if e["set"] == "scenario":
        return e["label"]
    if e["set"] == "nopressure":
        return "np_truth" if e["label"] == "truth" else "np_lie"
    return "unrelated"


def cell(k, n):
    return f"{k}/{n} ({100 * k / n:.0f}%)" if n else "–"


def main():
    man, vocab = C.load_manifest(M), C.load_vocab(M)
    layers, (lo, hi) = man["layers"], C.BANDS[M]
    band = [i for i, l in enumerate(layers) if lo <= l <= hi]
    ents = [e for e in man["transcripts"] if keep(e)]
    assert not any(e["split"] == "heldout" for e in ents if not e["set"].startswith("unrelated"))
    cls = np.array([cls_of(e) for e in ents])
    texts = C.load_transcripts(M)
    stripped = [t.strip() for t in vocab]
    masks = {k: np.array([s in v for s in stripped]) for k, v in LISTS.items() if v}
    masks["any of the four lists"] = np.any(list(masks.values()), axis=0)
    single = {k: np.array([(s.lower() if k == "artificial" else s) == k for s in stripped]) for k in SINGLE}
    allm = {**masks, **{"single: " + k: v for k, v in single.items()}}

    hit = collections.defaultdict(lambda: collections.defaultdict(lambda: np.zeros(len(ents), bool)))   # hit[(part, pos)][list]
    have = collections.defaultdict(lambda: np.zeros(len(ents), bool))
    tok_at = {}
    resp = {k: dict(any=np.zeros(len(ents), bool), car=np.zeros(len(ents), int)) for k in allm}
    ntok, echo = np.zeros(len(ents), int), np.zeros(len(ents), bool)
    for i, e in enumerate(ents):
        echo[i] = bool(AI_TEXT.search(texts[e["tid"]]["response"]))
        for part in ["prefix"] + C.WORDINGS:
            h, ids = read_ids(M, e, part)
            pp = part_positions(h)
            rt = [p for n, p in pp.items() if n.startswith("resp_tok")]
            if part == "prefix" and rt:
                block = np.asarray(ids["J"][band][:, rt])                       # [24, response tokens, 16]
                ntok[i] = len(rt)
                for k, m in allm.items():
                    c = m[block].any((0, 2))
                    resp[k]["any"][i], resp[k]["car"][i] = c.any(), int(c.sum())
            for n, p in pp.items():
                if n.startswith(("resp_tok", "q_tok", "ans_tok")) or (n.startswith("postans") and not h.get("answer_finished", True)):
                    continue
                key = (part, n)
                have[key][i] = True
                tok_at.setdefault(key, h["tokens"][p])
                block = np.asarray(ids["J"][band, p])
                for k, m in allm.items():
                    if m[block].any():
                        hit[key][k][i] = True

    print("# 作为, 作为一个, AI and 人工智能 in the readouts, by class\n")
    print("Written by `scripts/findings_2026_10_04/ai_words.py`. Qwen, J-lens, band 35 to 58, build split and unrelated chats, in-sample. "
          "Cells: transcripts with the word in the band's readout at the token / transcripts.\n")
    for k, v in LISTS.items():
        if v:
            print(f"- `{k}`: " + ", ".join(repr(vocab[t]) for t in np.flatnonzero(masks[k])))
    print("- Left out of the 作为 lists because they mean something else: 不作为, 可以作为, 可作为, 而作为, 担当作为, 不能作为, 主动作为, 作为中国, 作为国内.")
    print("- `ai`, ` ai`, ` Ai`, `Ai` are left out of `AI`: they are also pieces of other words.")
    print("- Counted one by one in Section D: " + ", ".join(f"{k} ({', '.join(repr(vocab[t]) for t in np.flatnonzero(m))})" for k, m in single.items()))

    def table(keys, title, floor):
        print(f"\n## {title}\n")
        for k in masks:
            rows = []
            for key in keys:
                cells, top = [], 0.0
                for _, c in CLASSES:
                    sel = have[key] & (cls == c)
                    n, kk = int(sel.sum()), int((hit[key][k] & sel).sum())
                    cells.append(cell(kk, n))
                    top = max(top, kk / n if n else 0)
                if top >= floor:
                    rows.append(f"| {(SHORT[key[0]] + ' ') if key[0] != 'prefix' else ''}{key[1]} | `{P.tok(tok_at[key])}` | " + " | ".join(cells) + " |")
            print(f"**`{k}`**" + ("" if rows else f": under {100 * floor:.0f}% in every class at every one of these tokens.") + "\n")
            if rows:
                print("| position | token | " + " | ".join(n for n, _ in CLASSES) + " |")
                print("|---|---|---|---|---|---|")
                print("\n".join(rows) + "\n")

    pos_key = lambda key: (ORDER[key[1].split("_")[0]], int(re.sub(r"\D", "", key[1]) or 0))
    pre = sorted([k for k in have if k[0] == "prefix"], key=pos_key)
    table(pre, "A. The template tokens around the response (every row is shown)", 0.0)
    for w in C.WORDINGS:
        table(sorted([k for k in have if k[0] == w], key=pos_key), f"B. After the self-report question, {SHORT[w]} (rows where a class reaches 10%)", 0.10)

    print("\n## C. Inside the response\n")
    print("Transcripts with the word at one or more response tokens, then response tokens that carry it / response tokens.\n")
    print("| list | responses | " + " | ".join(n for n, _ in CLASSES) + " |")
    print("|---|---|---|---|---|---|")
    for k in masks:
        for lab, keepm in (("all", np.ones(len(ents), bool)), ("text without \"AI\"", ~echo)):
            if lab != "all" and k.startswith("作为"):
                continue
            row = []
            for _, c in CLASSES:
                sel = (cls == c) & keepm
                row.append(f"{cell(int(resp[k]['any'][sel].sum()), int(sel.sum()))}; {int(resp[k]['car'][sel].sum()):,}/{int(ntok[sel].sum()):,} ({100 * resp[k]['car'][sel].sum() / max(1, ntok[sel].sum()):.2f}%)")
            print(f"| `{k}` | {lab} | " + " | ".join(row) + " |")
    print("\nResponses whose own text says \"AI\" or \"artificial intelligence\": " + "; ".join(f"{n} {int((echo & (cls == c)).sum())}/{int((cls == c).sum())}" for n, c in CLASSES) + ".")

    print("\n## D. Single tokens, at the positions of Section A and inside the response\n")
    print("| token | place | " + " | ".join(n for n, _ in CLASSES) + " |")
    print("|---|---|---|---|---|---|")
    for k in single:
        kk = "single: " + k
        for key in pre:
            cells = [(int((hit[key][kk] & have[key] & (cls == c)).sum()), int((have[key] & (cls == c)).sum())) for _, c in CLASSES]
            if max(a / b for a, b in cells) >= 0.05:
                print(f"| {k} | {key[1]} (`{P.tok(tok_at[key])}`) | " + " | ".join(cell(a, b) for a, b in cells) + " |")
        print(f"| {k} | at one or more response tokens | " + " | ".join(cell(int(resp[kk]['any'][cls == c].sum()), int((cls == c).sum())) for _, c in CLASSES) + " |")


if __name__ == "__main__":
    main()
