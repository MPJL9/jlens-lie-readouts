# Prompt: readout suggestion for one layer band, logit lens (PLAN.md Section 4.4)

You are given one language model's logit-lens readouts and asked where a **layer band** should
start and end. Frozen on 2026-10-01. The model name is filled in by the caller as `{MODEL}`;
its folder slug is `{SLUG}`. Work only from the files named below; write one file.

## Background

- The logit lens gives, at every layer and every token position of a transcript, a **readout**:
  the 16 vocabulary tokens with the highest scores when the model's own unembedding (final norm
  plus unembedding matrix) is applied to that layer's residual stream directly, with no map.
  Layer numbers count transformer blocks from 0; the last layer's readout is the model's own
  next-token distribution. (The J-lens, which first carries the residual stream to the final
  layer's space with a fitted map, is a separate method with a band of its own; it is not the
  object of this task.)
- A **layer band** is a fixed range of layers. Later analysis asks, at fixed template
  positions, whether words about the model's own act (for example deceiving or being honest)
  appear in the readouts at any layer of the band. One band is used for the whole model.
- The band should
  - **start** where readouts begin to carry words about the conversation (its topic, the
    situation, what the model is doing) rather than copies of the template tokens, punctuation,
    fragments or unrelated words;
  - **end** before readouts become mostly the actual next token (at that point the lens shows
    what the model is about to write, not what it represents).

## Files to read (all under the project root `redo_analysis/`)

1. `analysis/band/readout_stats_LL_{SLUG}.md`: per layer and per position group, three numbers
   over 10 transcripts, logit-lens top 16:
   - `readable`: share of readout tokens that are words of 3 or more letters;
   - `next`: share of positions whose top readout token is the actual next token;
   - `overlap`: mean overlap (Jaccard) between the readouts at neighbouring positions; a high
     value means the readout barely changes from one token to the next.
   The `J_` columns give the same numbers for the J-lens; they are context, not the object of
   the decision.
2. `analysis/band/readouts_LL/{SLUG}/01_*.md` … `10_*.md`: one file per transcript. Each shows the
   conversation (system prompt, user prompt, model response, the self-report question that
   follows) and then, for about a dozen positions, one line per layer with the top-5 logit-lens
   tokens and the top token's probability. Positions: the last user-prompt token, three
   response tokens, every post-response slot (the turn boundary between the response and the
   question: turn end, newline, turn start, `user`, newline; gpt-oss has four such tokens),
   the last pre-answer slot, and the first post-answer slot.

Read the statistics file first, then all ten transcript files. Do not read anything else in
`analysis/`: in particular no `cka_*` file, no `readout_suggestion_*` file and nothing under
`analysis/band/readouts/` (those concern the J-lens; this band is chosen for the logit lens on
its own), and nothing under `data/`. No file you are given carries a lie/truth label; do not try to guess
labels and do not mention any guess.

## What to decide

Propose one band `start–end` (inclusive layer numbers) for `{MODEL}`, and give your reasons with
concrete examples: transcript number, position, layer, the tokens seen. Base the start on the
readouts at template positions and response tokens together. Base the end on the `next` numbers
(response and answer tokens) and on the top-token probabilities in the dumps. Also give one
alternative band (narrower or wider) and say what is gained or lost.

Be concrete about what the readouts at the post-response slots show in each layer region
(template tokens, punctuation, topic words, words about the model's act, the next token), since
those slots are the positions that matter most later.

## Output

Write `analysis/band/readout_suggestion_LL_{SLUG}.md` with these sections, in plain English:

1. **Proposed band**: `start–end`, one sentence each for the start and the end.
2. **Layer regions**: a table with one row per region of consecutive layers that behave
   alike: layers, what the readouts at the post-response slots show, what they show at
   response tokens, the typical `readable` / `next` / `overlap` values.
3. **Evidence**: 6 to 12 bullet points, each with transcript number, position, layer and
   tokens.
4. **Alternative band** and its trade-off.
5. **Caveats**: anything that made the choice uncertain (for example a position group whose
   readouts are template tokens at every layer, or two transcripts that disagree).

Keep the file under 1,500 words. Do not edit any other file.
