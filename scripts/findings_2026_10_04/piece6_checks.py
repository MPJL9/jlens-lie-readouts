"""Three checks for piece 6 of pieces_of_blog.md (the hypothesis: the newline describes the turn before it).
Qwen, J-lens, band 35 to 58, build split and unrelated chats (the held-out split is never read).
"Present" = in the top 16 at one or more band layers.

  A. The user's observation (2026-10-04): under Q7 the readout holds many "instruction" and "constraint" words.
     Two fixed word lists (printed), counted at every template token after the response and after the question,
     per wording and per class.
  B. Echo of the text at the newline after the response: the `lie` family and the eight families, counted again
     after leaving out the conversations whose text (system prompt, user prompt, response) contains the word,
     matched as whole words on word stems (the rules of scripts/pilot/where_words_sit.py).
  C. Example chats for screenshots: unrelated chats whose newline after the request shows the task word at the
     most band layers, with the words at both newlines and the chat's number in the viewer.

Parts A and B read the presence index; part C reads the exports of about 120 chats.
Run from the project root: python3 scripts/findings_2026_10_04/piece6_checks.py > analysis/findings_2026_10_04/piece6_checks.md"""
import collections
import json
import os
import re
import sys

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, ".."))
sys.path.insert(0, HERE)
import common as C  # noqa: E402
import presence as P  # noqa: E402
from frequency_tables import part_positions  # noqa: E402
from presence_index import read_ids  # noqa: E402
import newline_holds as NH  # noqa: E402

M = "qwen3.6-27b"
SHORT = {"Q1_bare": "Q1", "Q2_after": "Q2", "Q6_factual": "Q6", "Q7_ab": "Q7", "Q9_dyl": "Q9"}
CLASSES = [("lies", "lie"), ("truths", "truth"), ("no-pressure truths", "np_truth"), ("unrelated", "unrelated")]
INSTRUCTION = r"(?i)instruct(ion|ions|ed|ing|s)?|directives?|mandat(e|ed|es)"
CONSTRAINT = r"(?i)constraints?|constrained|restrictions?"
ZH = {"instruction": ("指令", "指示"), "constraint": ("约束", "限制")}
EIGHT = ["lie", "fake", "falsehood", "misinformation", "deceive", "fabricate", "false", "mislead"]
RULES = {"lie": r"\b(lie|lies|lied|lying|liar|liars)\b", "fake": r"\bfak(e|es|ed|ing|ery)\b", "deceive": r"\bdece(iv|pt|it)\w*",
         "falsehood": r"\bfalsehoods?\b", "fabricate": r"\bfabricat\w*", "conceal": r"\bconceal\w*",
         "misinformation": r"\b(mis|dis)inform\w*", "false": r"\b(fals(e|ely|ity|ify|ified|ifying)|untru(e|th|ths))\b",
         "mislead": r"\bmis(lead|leads|leading|led)\b", "dishonest": r"\bdishonest\w*", "honest": r"\bhonest\w*"}
TASK = {"maths": ({"计算", " calculation", " calculate", "数学"}, r"(?i)calculat|comput|arithmetic|\bmath"),
        "classify": ({"分类", "归类", "类别"}, r"(?i)classif|categor"),
        "translate": ({"翻译", "翻译成"}, r"(?i)translat")}


def cell(pm, sel):
    n, k = int(sel.sum()), int((pm & sel).sum())
    return f"{k}/{n} ({100 * k / n:.0f}%)" if n else "–"


def part_a(d, vocab):
    cls = d["cls"]
    G = {"instruction": [i for i, t in enumerate(vocab) if re.fullmatch(INSTRUCTION, t.strip()) or t.strip() in ZH["instruction"]],
         "constraint": [i for i, t in enumerate(vocab) if re.fullmatch(CONSTRAINT, t.strip()) or t.strip() in ZH["constraint"]]}
    print("## A. Instruction and constraint words, by position, wording and class\n")
    for g, ids in G.items():
        print(f"- `{g}` ({len(ids)} tokens): " + ", ".join(repr(vocab[i]) for i in ids))
    for g, ids in G.items():
        print(f"\n**`{g}`** (positions where no class reaches 5% are left out)\n")
        print("| position | wording | " + " | ".join(n for n, _ in CLASSES) + " |")
        print("|---|---|---|---|---|---|")
        rows = [("prefix", pos, "before the question") for pos in P.positions(d, "prefix")]
        rows += [(w, pos, SHORT[w]) for pos in P.positions(d, "Q1_bare") if not pos.startswith("q_tok") for w in C.WORDINGS]
        for part, pos, lab in rows:
            pm, have = P.present_mask(d, part, pos, ids), P.have_mask(d, part, pos)
            if max(((pm & have & (cls == c)).sum() / max(1, (have & (cls == c)).sum())) for _, c in CLASSES) < 0.05:
                continue
            print(f"| {pos} | {lab} | " + " | ".join(cell(pm, have & (cls == c)) for _, c in CLASSES) + " |")
    ans = P.answer(d, "Q7_ab")
    print("\nUnder Q7 at the newline after the question, by the answer that follows (lies | truths):")
    for g, ids in G.items():
        pm = P.present_mask(d, "Q7_ab", "preans_slot1", ids)
        print(f"- `{g}`: before a denial {cell(pm, (cls == 'lie') & (ans == 'deny'))} | {cell(pm, (cls == 'truth') & (ans == 'deny'))}; "
              f"before an admission {cell(pm, (cls == 'lie') & (ans == 'admit'))} | {cell(pm, (cls == 'truth') & (ans == 'admit'))}")
    tr = C.load_transcripts(M)
    rx = re.compile(r"(?i)\b(instruct\w*|directive\w*|mandat\w*|constrain\w*|restrict\w*)")
    print("\nConversations whose own text (system prompt, user prompt, response) contains one of these words, and the `instruction` list "
          "at the newline after Q7 with and without it:")
    pm = P.present_mask(d, "Q7_ab", "preans_slot1", G["instruction"])
    intext = np.array([bool(rx.search(" ".join((tr[t["tid"]].get("system") or "", tr[t["tid"]]["user_prompt"], tr[t["tid"]]["response"])))) for t in d["transcripts"]])
    for name, c in CLASSES:
        print(f"- {name}: text has a word {int((intext & (cls == c)).sum())}/{int((cls == c).sum())}; present when it has {cell(pm, (cls == c) & intext)}; when it has not {cell(pm, (cls == c) & ~intext)}")


def part_b(d, vocab):
    cls, trs = d["cls"], d["transcripts"]
    tr = C.load_transcripts(M)
    fd = json.load(open(os.path.join(C.ROOT, "analysis", "families", "families_draft.json")))["entries"]
    ents = [e for e in fd if e["model"] == M and e["lens"] == "J" and e["position"] == "postresp_slot1" and e["status"] != "dropped"]
    fam = lambda name: sorted({m["id"] for e in ents if e["name"] == name for m in e["members"]})
    ctx = [(tr[t["tid"]]["response"], " ".join((tr[t["tid"]].get("system") or "", tr[t["tid"]]["user_prompt"], tr[t["tid"]]["response"]))) for t in trs]
    lie_pm = P.present_mask(d, "prefix", "postresp_slot1", fam("lie"))
    any8 = np.zeros(len(trs), bool)
    for n in EIGHT:
        any8 |= P.present_mask(d, "prefix", "postresp_slot1", fam(n))
    print("\n\n## B. Is the lie word at the newline a copy of the text?\n")
    print("`lie` family: " + ", ".join(repr(vocab[i]) for i in fam("lie")))
    for name, rx in (("a form of the word `lie`", re.compile(RULES["lie"], re.I)),
                     ("a word of any lie-side family", re.compile("|".join(v for k, v in RULES.items() if k != "honest"), re.I))):
        inresp = np.array([bool(rx.search(r)) for r, _ in ctx])
        inctx = np.array([bool(rx.search(c)) for _, c in ctx])
        print(f"\n**Text rule: {name}**\n")
        print("| class | response has it | conversation has it | `lie` family, conversation without it | with it | one or more of the eight, without it | with it |")
        print("|---|---|---|---|---|---|---|")
        for cname, c in CLASSES[:3]:
            sel = cls == c
            print(f"| {cname} | {int((inresp & sel).sum())}/{int(sel.sum())} | {int((inctx & sel).sum())}/{int(sel.sum())} | {cell(lie_pm, sel & ~inctx)} | "
                  f"{cell(lie_pm, sel & inctx)} | {cell(any8, sel & ~inctx)} | {cell(any8, sel & inctx)} |")
    rx = re.compile(RULES["honest"], re.I)
    inresp = np.array([bool(rx.search(r)) for r, _ in ctx])
    pm = P.present_mask(d, "prefix", "postresp_slot1", fam("honest"))
    print("\n`honest` family at the newline, by whether the response writes a form of \"honest\":")
    for cname, c in CLASSES[:3]:
        print(f"- {cname}: response writes it {int((inresp & (cls == c)).sum())}/{int((cls == c).sum())}; family present when it does {cell(pm, (cls == c) & inresp)}; when it does not {cell(pm, (cls == c) & ~inresp)}")


def part_c(vocab):
    man = C.load_manifest(M)
    layers, (lo, hi) = man["layers"], C.BANDS[M]
    lidx = [i for i, l in enumerate(layers) if lo <= l <= hi]
    raw = json.load(open(os.path.join(C.EXPORTS, C.slug(M), "manifest.json")))
    num, n = {}, 0                      # the viewer numbers chats in the manifest's order, one entry per wording
    for t in raw["transcripts"]:
        for w in raw["wordings"]:
            if t["wordings"].get(w):
                num.setdefault(t["tid"], n)
                n += 1
    prompts = {r["id"]: r["user_prompt"] for f in ("unrelated.jsonl", "unrelated_extra.jsonl") for r in C.read_jsonl(os.path.join(C.ROOT, "inputs", f))}
    tr = C.load_transcripts(M)
    wordy = lambda t: bool(re.search(r"[A-Za-z]{2,}|[一-鿿]", vocab[t])) and not vocab[t].startswith("<")
    print("\n\n## C. Example chats: the task word at the newline after the request\n")
    print("Band layers (of 24) with a task word at the newline after the request and at the newline after the response; the words held at the most layers.\n")
    for kind, (ws, rx) in TASK.items():
        wid = {i for i, t in enumerate(vocab) if t in ws}
        rows = []
        for e in man["transcripts"]:
            if not e["set"].startswith("unrelated") or not NH.KINDS[kind](prompts[e["item_id"]]):
                continue
            h, ids = read_ids(M, e, "prefix")
            pp = part_positions(h)
            got = {}
            for pos in ("preresp_slot1", "postresp_slot1"):
                blk = np.asarray(ids["J"][lidx, pp[pos]])
                cnt = collections.Counter(t for row in blk for t in set(row.tolist()))
                got[pos] = (sum(bool(set(row.tolist()) & wid) for row in blk), [(vocab[t], c) for t, c in cnt.most_common(80) if wordy(t)][:10])
            rows.append((got["preresp_slot1"][0], e, got, bool(re.search(rx, prompts[e["item_id"]])), len(h["tokens"])))
        rows.sort(key=lambda r: (-r[0], r[4]))
        print(f"**{kind}** ({len(rows)} chats; task words {', '.join(sorted(ws))})\n")
        for k, e, got, inprompt, ntok in rows[:3] + [r for r in rows[3:] if not r[3]][:2]:
            p = prompts[e["item_id"]].replace("\n", " / ")
            print(f"- `{e['tid']}` (viewer number {num.get(e['tid'])}; {ntok} tokens; task word in the prompt: {'yes' if inprompt else 'no'})")
            print(f"  - request: {p[:200]}")
            print(f"  - response: {tr[e['tid']]['response'][:120].replace(chr(10), ' / ')}")
            for pos, lab in (("preresp_slot1", "after the request"), ("postresp_slot1", "after the response")):
                print(f"  - newline {lab}: task word at {got[pos][0]} layers; " + ", ".join(f"{P.tok(w)} ({c})" for w, c in got[pos][1]))
        print()


def main():
    d, vocab = P.load(M, "J"), C.load_vocab(M)
    print("# Checks for piece 6 (written by scripts/findings_2026_10_04/piece6_checks.py; Qwen, J-lens, band 35 to 58, build split, in-sample)\n")
    part_a(d, vocab)
    part_b(d, vocab)
    part_c(vocab)


if __name__ == "__main__":
    main()
