"""Does role play explain where the "as an AI" words are in the readout? (User's question, 2026-10-04.)
Qwen, J-lens, band 35 to 58, presence index (build split and unrelated chats; the held-out split is never read).

In the unrelated chats the system prompt is "You are a helpful assistant." In the no-pressure chats it is "You are a
helpful assistant. The following fact is true: ...", with the scenario's own user message. In the pressured chats
the system prompt gives a role. By a fixed text rule on the pressured system prompt the scenarios are sorted into
  says AI        the prompt has "AI", "artificial intelligence", "chatbot", "language model", "virtual assistant" or "bot"
  other role     none of these and not the word "assistant" (a public relations representative, a receptionist, ...)
  assistant only "assistant" without any of the AI words (shown in the counts, left out of the tables)
If playing a role that is not an AI is what removes the "as an AI" words, the pressured chats whose prompt says AI
should keep them, and the no-pressure chats (no role in the system prompt) should look like the unrelated chats.

Word lists (exact tokens after stripping spaces): AI words = AI, _AI, .AI, 人工智能, 的人工智能; 作为一个 ("as a", general);
作为一名 ("as a", used for a member of a profession); 作为 / 作為 (the plain word). Every wording, every template token
from the response's end on. Rows where no group reaches 15% are left out.

Run from the project root:
python3 scripts/findings_2026_10_04/ai_words_by_role.py > analysis/findings_2026_10_04/ai_words_by_role.md"""
import os
import re
import sys

import numpy as np

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
import common as C  # noqa: E402
import presence as P  # noqa: E402

M = "qwen3.6-27b"
SHORT = {"prefix": "before the question", "Q1_bare": "Q1", "Q2_after": "Q2", "Q6_factual": "Q6", "Q7_ab": "Q7", "Q9_dyl": "Q9"}
AI_RULE = re.compile(r"\bAI\b|artificial intelligence|chatbot|language model|virtual assistant|\bbot\b", re.I)
ASSISTANT = re.compile(r"\bassistant\b", re.I)
LISTS = {"AI words": ["AI", "_AI", ".AI", "人工智能", "的人工智能"], "作为一个": ["作为一个"], "作为一名": ["作为一名"], "作为 / 作為": ["作为", "作為"]}
TOKEN = {"postresp_slot0": "turn end", "postresp_slot1": "newline", "postresp_slot2": "`<|im_start|>`", "postresp_slot3": "`user`", "postresp_slot4": "newline",
         "preans_slot0": "turn end", "preans_slot1": "newline", "preans_slot2": "`<|im_start|>`", "preans_slot3": "`assistant`", "preans_slot4": "newline",
         "think_slot0": "`<think>`", "think_slot1": "blank line", "think_slot2": "`</think>`", "think_slot3": "blank line",
         "postans_slot0": "turn end", "postans_slot1": "newline", "postans_slot2": "`<|im_start|>`", "postans_slot3": "`user`", "postans_slot4": "newline"}


def cell(pm, sel):
    n, k = int(sel.sum()), int((pm & sel).sum())
    return f"{k}/{n} ({100 * k / n:.0f}%)" if n else "–"


def main():
    d, vocab = P.load(M, "J"), C.load_vocab(M)
    cls = d["cls"]
    system = {r["id"]: r["system"] for r in C.read_jsonl(os.path.join(C.ROOT, "inputs", "scenarios.jsonl"))}
    kind = []
    for t in d["transcripts"]:
        s = system.get(t["item_id"])
        kind.append("" if s is None else "says AI" if AI_RULE.search(s) else "assistant only" if ASSISTANT.search(s) else "other role")
    kind = np.array(kind)
    press = np.isin(cls, ["lie", "truth"])
    groups = [("pressured, prompt says AI", press & (kind == "says AI")), ("pressured, other role", press & (kind == "other role")),
              ("no-pressure, scenario says AI", (cls == "np_truth") & (kind == "says AI")), ("no-pressure, other role", (cls == "np_truth") & (kind == "other role")),
              ("unrelated", cls == "unrelated")]
    fine = [("lies, says AI", (cls == "lie") & (kind == "says AI")), ("lies, other role", (cls == "lie") & (kind == "other role")),
            ("truths, says AI", (cls == "truth") & (kind == "says AI")), ("truths, other role", (cls == "truth") & (kind == "other role"))]
    stripped = [t.strip() for t in vocab]
    ids = {k: [i for i, s in enumerate(stripped) if s in v] for k, v in LISTS.items()}

    print("# The \"as an AI\" words by the role the prompt gives\n")
    print("Written by `scripts/findings_2026_10_04/ai_words_by_role.py`. Qwen, J-lens, band 35 to 58, build split and unrelated chats, in-sample. "
          "Cells: transcripts with the word in the band's readout at the token / transcripts.\n")
    for k, v in ids.items():
        print(f"- `{k}`: " + ", ".join(repr(vocab[i]) for i in v))
    print("\nTranscripts: " + "; ".join(f"{n} {int(m.sum())}" for n, m in groups + fine)
          + f"; pressured with \"assistant\" only (left out) {int((press & (kind == 'assistant only')).sum())}.")
    for k in ids:
        for title, grp in ((f"`{k}`", groups), (f"`{k}`, lies and truths apart", fine)):
            print(f"\n## {title}\n")
            print("| wording | position | token | " + " | ".join(n for n, _ in grp) + " |")
            print("|---|---|---|" + "---|" * len(grp))
            for part in ["prefix"] + C.WORDINGS:
                for pos in P.positions(d, part):
                    if pos.startswith("q_tok"):
                        continue
                    pm, have = P.present_mask(d, part, pos, ids[k]), P.have_mask(d, part, pos)
                    sh = [(pm & have & m).sum() / max(1, (have & m).sum()) for _, m in groups]
                    if max(sh) < 0.15:
                        continue
                    print(f"| {SHORT[part]} | {pos} | {TOKEN[pos]} | " + " | ".join(cell(pm, have & m) for _, m in grp) + " |")


if __name__ == "__main__":
    main()
