"""The template-token bands around the response and the self-report answer, shared by
scripts/probe/list_band_positions.py (the cut list for the cluster) and scripts/probe/score_bands.py (the
numbers). Written 2026-10-09 for the user's request: redo the post's difference-of-means probe (sections 4.4
and 4.6) on the other models, at every template token of these bands.

Four bands, named by what sits before and after them (position names as in common.positions):
  after_response   the template tokens between the response and the self-report question (prefix part, the
                   same for every wording): postresp_slot0, 1, ...  Qwen and Gemma: turn end, newline, turn
                   start, `user`, newline. gpt-oss: `<|end|>`, `<|start|>`, `user`, `<|message|>`.
  before_answer    the template tokens between the self-report question and the answer, per wording:
                   preans_slot0, 1, ... (Qwen also think_slot0 to 3, its empty thinking block; gpt-oss also
                   analysis_slot0 to 2, the header the model writes before its hidden reasoning, and
                   final_slot0 to 5, the header it writes before its visible answer; the hidden reasoning
                   between the two headers is text and is not a position).
  answer           the answer token itself, Yes or No: ans_tok0. On gpt-oss it is the token after the final
                   channel's `<|message|>`, not the first token of the answer segment (that is `<|channel|>`).
  after_answer     the template tokens after the answer, per wording: postans_slot0, 1, ...
Position names outside these (the pre-response controls, the question tokens, the response tokens) are in no
band and are left alone by the scoring script.
"""
from __future__ import annotations

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import common as C  # noqa: E402

BANDS = ["after_response", "before_answer", "answer", "after_answer"]
TITLE = {"after_response": "after the response (before the self-report question)",
         "before_answer": "between the self-report question and the answer",
         "answer": "the self-report answer token",
         "after_answer": "after the self-report answer"}
# name prefix -> (band, order within the band)
PREFIXES = [("postresp_slot", "after_response", 0), ("preans_slot", "before_answer", 0), ("think_slot", "before_answer", 1),
            ("analysis_slot", "before_answer", 2), ("final_slot", "before_answer", 3), ("ans_tok0", "answer", 0),
            ("postans_slot", "after_answer", 0)]
GPT_OSS = "gpt-oss-20b"
ANALYSIS = ["<|channel|>", "analysis", "<|message|>"]                                       # gpt-oss, before the hidden reasoning
FINAL = ["<|end|>", "<|start|>", "assistant", "<|channel|>", "final", "<|message|>"]        # gpt-oss, before the visible answer


def band(name):
    """The band of a position name, or None."""
    for prefix, b, _ in PREFIXES:
        if name.startswith(prefix):
            return b
    return None


def order_key(name):
    """Sort key: band, then the order within the band, then the slot number."""
    for i, (prefix, b, k) in enumerate(PREFIXES):
        if name.startswith(prefix):
            digits = "".join(ch for ch in name[len(prefix):] if ch.isdigit())
            return (BANDS.index(b), k, int(digits) if digits else 0)
    return (9, 0, 0)


def _slots(pos, prefix):
    return sorted(((k, p) for k, p in pos.items() if k.startswith(prefix)), key=lambda kp: order_key(kp[0]))


def prefix_positions(tokens, segments):
    """[(name, index)] of the after_response band of a prefix part."""
    pos = C.positions(dict(tokens=tokens, segments=segments))
    return _slots(pos, "postresp_slot")


def wording_positions(model, tokens, segments):
    """[(name, index)] of the before_answer, answer and after_answer bands of one wording part, in order; or
    (None, reason) when the answer token cannot be placed."""
    pos = C.positions(dict(tokens=tokens, segments=segments))
    out = _slots(pos, "preans_slot") + _slots(pos, "think_slot")
    if model == GPT_OSS:
        a = next((s for s in segments if s["name"] == "answer"), None)
        if a is None:
            return None, "no answer segment"
        if tokens[a["start"]:a["start"] + len(ANALYSIS)] != ANALYSIS:
            return None, "the answer does not open with the analysis header"
        out += [(f"analysis_slot{k}", a["start"] + k) for k in range(len(ANALYSIS))]
        i = next((j for j in range(a["end"] - len(FINAL) - 1, a["start"] - 1, -1) if tokens[j:j + len(FINAL)] == FINAL), None)
        if i is None:
            return None, "no final-channel header followed by an answer token"
        out += [(f"final_slot{k}", i + k) for k in range(len(FINAL))]
        out.append(("ans_tok0", i + len(FINAL)))
    else:
        if "ans_tok0" not in pos:
            return None, "no answer token"
        out.append(("ans_tok0", pos["ans_tok0"]))
    return out + _slots(pos, "postans_slot"), None


def label(name, token, plain=False):
    """A short label for a position: the token in plain words or in backticks, and the position name."""
    if name == "ans_tok0":
        return "the answer token (Yes / No)"
    t = {"\n": "newline", "\n\n": "blank line"}.get(token)
    if t is None:
        t = token if plain else "`" + token.replace("|", "\\|") + "`"
    return f"{t} ({name})"
