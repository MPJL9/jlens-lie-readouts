# Prompt: semantic families at template positions (PLAN.md Section 5.3)

Frozen on 2026-10-01. The caller fills in `{MODEL}`, `{SLUG}` (its folder name), `{LENS}` (J =
J-lens, LL = logit lens), `{PART}` (`prefix` for the post-response slots, or a wording such as `Q1_bare`), `{GROUP}`
(a position group), `{POSITIONS}` (the position names in the group), `{QUESTION}` (the wording's
question text, or "none" for the post-response slots), `{REPLICATE}` (1 or 2) and `{OUT}` (the
file to write). Work only from the files named here. Write one file.

## Background

A **readout** is the 16 vocabulary tokens with the highest scores when one layer's residual
stream is read with a lens. A **layer band** is a fixed range of layers; a token is *present* at
a position in a transcript if it is in the readout at one or more layers of the band. The
transcripts are conversations in which a model, given a role and an incentive, answered a
user's question either truthfully or with a lie; after the response comes a self-report question.
You are not told which transcripts are lies. Your job is to find, at each template position,
**semantic families**: lists of readout tokens that share one meaning and could describe the
model's own act (for example deceiving, hiding, being honest, admitting) or its stance toward
it. The families are scored later for whether they separate lies from truths; you do not score
anything and must not try to guess labels.

## Inputs

1. `analysis/freq/{SLUG}_{LENS}_{PART}.md`: one frequency table per position. Rows are tokens
   present at that position in one or more of the build-split transcripts, sorted by `n` (the
   number of transcripts in which the token is present); the layer columns give the count per
   band layer. Read the first 400 rows of each table in `{POSITIONS}` (the whole table if it is
   shorter). The rest is reached through the matcher below.
2. The matcher: `python3 scripts/match_seeds.py --model {MODEL} --lens {LENS} --part {PART}
   --positions <position names> --seeds <seed words>` prints every token at those positions that
   contains a seed as a substring (case-insensitive, leading space ignored, any script), at any
   frequency, with its id, `n` and per-layer counts. Run it from the project root. It over-matches
   on purpose (`lie` also returns `Replies`, `Client`, `Allies`); you accept or reject each hit.
3. Nothing else. Do not open `data/`, `analysis/band/`, `analysis/dyl_*`, `OBSERVATIONS.md`, other
   families files, or the transcripts.

## Rules

1. **One meaning per family.** All members share one short gloss. Each member could replace any
   other in "my response was ___" or "I am ___ing" without changing the meaning. Families are
   fine-grained: *secret* and *lie* are separate families; so are *hide* and *mislead*; so are
   *deceive* and *deceptive* only if you judge the meanings different (normally they are one
   family: the act of deceiving). Merging is done later by the user. **Antonyms never share a
   family**; put them in the paired family (deceive / honest, hide / reveal).
2. **Every variant is included.** Inflections (conceal, concealed, concealing, concealment),
   other languages and scripts (隐瞒, 欺骗, 거짓, झूठ, mentir, Lüge), capitalization and
   leading-space forms are all members. Three steps, in this order:
   - from the tables, name the seed words of each candidate family and their translations;
   - run the matcher with those seeds on the group's positions;
   - accept or reject each hit, and record the rejected ones with a reason only when the reason
     is not obvious (`Replies` for `lie` needs no note; a near-miss does).
3. **Word pieces.** A fragment such as `decept` or `conce` joins a family only if the family's
   words are the only common words that start with it (`decept` → deception, deceptive: yes;
   `conce` → conceal, concern, concept: no). List the rejected fragments under
   `ambiguous_pieces`; they are not scored.
4. **Exclusions.** Do not put these in any family; log each under `exclusions` with the reason:
   - yes / no and A / B, in any language or form (Yes, NO, 是, 否, oui, nein, …);
   - words that answer the user's question in the scenario rather than describe the model's act:
     confirm, deny, agree, admit *as an answer to the user*, and the scenario's own content words
     (products, prices, places, names). Note: *admit* and *deny* can also describe the model's
     act toward the self-report question; if a word is plausible in both readings, keep it in a
     family and add a note `"double_reading": true`;
   - for `{PART}` ≠ `prefix` only: words copied from the self-report question
     `{QUESTION}`, with their inflections and translations (for example *deceptive*, *lie*,
     *false*, *statement*, *previous*, *response*, when they appear in that question). Log
     them; they are excluded at these positions because the question itself puts them there.
5. **Borderline words.** *true, false, wrong, correct, accurate, incorrect, right* and their
   variants are not decided by you: list them under `borderline` with the family they would join
   if accepted. The user decides.
6. **Side.** Give each family a side by meaning: `"lie"` (the word marks deceiving, hiding,
   misleading, denying the truth), `"truth"` (honesty, candour, admitting, disclosing), or
   `"unclear"`. The user decides the unclear ones. Do not use frequency or anything else to set
   the side.
7. **What counts as a candidate.** Words about the model's own act or stance (deceive, conceal,
   mislead, evade, bluff, cover, pretend, fake, honest, truthful, admit, confess, disclose,
   reveal, transparent, sincere …), about secrecy (secret, hidden, confidential …), about
   guilt or moral judgement of the act (unethical, wrong-doing, guilt, shame, sorry …), and about
   the stance of the reply (denial, evasion, refusal …). Not candidates: template tokens,
   punctuation, generic dialogue words (reply, answer, question, chatbot, user), the scenario's
   content, and words with no clear meaning in English or in their own language.

## Output

Write `{OUT}` as JSON with this shape (keep the key names):

```json
{
  "model": "{MODEL}", "lens": "{LENS}", "part": "{PART}", "group": "{GROUP}", "replicate": {REPLICATE},
  "prompt_file": "prompts/family_generation.md", "rows_read_per_table": 400,
  "families": [
    {"position": "postresp_slot2", "name": "deceive", "gloss": "the act of deceiving", "side": "lie",
     "seeds": ["decept", "deceiv", "欺骗"],
     "members": [{"token": " deception", "id": 74492, "n": 20}, {"token": " deceptive", "id": 114557, "n": 12}],
     "notes": ""}
  ],
  "ambiguous_pieces": [{"position": "postresp_slot2", "token": "conce", "id": 0, "reason": "conceal, concern, concept"}],
  "borderline": [{"position": "postresp_slot1", "token": " false", "id": 0, "family_if_accepted": "false / untrue"}],
  "exclusions": [{"position": "postresp_slot2", "token": " deny", "id": 0, "reason": "answers the user's question"}],
  "rejected_matches": [{"position": "postresp_slot1", "token": " Replies", "id": 178835, "seed": "lie", "reason": ""}],
  "positions_without_families": ["postresp_slot0"],
  "notes": ""
}
```

One entry per family per position (the same meaning at two positions is two entries, each with
its own members). Members carry the exact token string from the table (with its leading space),
the id and `n`. Include every accepted hit, whatever its frequency. Give families short names
in English; a family may be a single token. Expect roughly 5 to 25 families per position where
act words exist, and none at positions that hold only template tokens or noise (list those
under `positions_without_families`).

Finish by replying with one line per position: the position name and the family names found.
