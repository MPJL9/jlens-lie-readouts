# One layer band per model: the two suggestions (PLAN.md Section 4)

Written 2026-09-30. The band is chosen before any family is built and is used for every family
on that model. This file gives the two label-free suggestions and what to check in the viewer.
The user's choice goes into `PLAN.md` Section 8.

Terms. A **readout** is the 16 vocabulary tokens with the highest J-lens scores at one layer and
one position. A **layer band** is a fixed range of layers; a token is "present in the band" at a
position if it is in the readout at one or more layers of the band. **CKA** (centered kernel
alignment) is a number between 0 and 1 that says how similar two arrangements of points are,
ignoring rotation and overall scale. Layers count transformer blocks from 0; the last layer's
readout is the model's own next-token distribution.

## 1. Suggestion A: CKA between layers (no activations, no labels)

**Method** (`scripts/band_cka.py`). At layer l the J-lens gives every vocabulary token a
direction in the residual stream: the token's row of the unembedding matrix, scaled by the final
norm's weights, times the lens map of layer l. For a fixed sample of 2,000 word tokens (seed 0;
a token counts as a word if it decodes to 2 or more letters after one optional leading space),
the CKA between two layers measures how similar the arrangements of these 2,000 directions are.
It is computed plain, and again after removing each layer's single strongest direction (the
first principal component), because one direction can dominate the plain score. A second sample
of 2,000 tokens drawn uniformly from the whole vocabulary is run as a check. Layers are then cut
into k = 2 … 6 contiguous blocks with Ward's criterion on 1 − CKA (the cut that keeps dissimilar
layers apart, found exactly). Inputs: the published lens files (local cache; the same files as
on the Hub, checked by hash), the unembedding rows and the final-norm weights saved by
`scripts/fetch_weights.py` in `data/weights/`.

**Reading rule.** The block structure is the suggestion. As a single band, I read off the k = 4
cut (strongest direction removed, word sample) and take the block just before the block that
holds the last layers (where readouts turn into the next token). This rule was fixed after
looking at the four matrices; the user's check in the viewer is what decides.

| model | k = 4 blocks (drop) | biggest adjacent-layer drops (drop) | CKA band by the rule |
|---|---|---|---|
| gemma-3-12b-it (48) | 0–4, 5–16, 17–29, 30–47 | 4/5 0.88, 16/17 0.90, 45/46 0.91, 46/47 0.64; k = 5 splits 30–47 into 30–40, 41–47 | 17–29 |
| gemma-3-27b-it (62) | 0–12, 13–26, 27–52, 53–61 | 52/53 0.81, 58/59 0.76, 60/61 0.87 | 27–52 |
| qwen3.6-27b (64) | 0–7, 8–33, 34–49, 50–63 | 5/6 0.91, 17/18 0.92, 62/63 0.88 (uniform sample: 45/46 0.73, 48/49 0.76) | 34–49 |
| gpt-oss-20b (24) | 0–6, 7–12, 13–20, 21–23 | 19/20 0.86, 20/21 0.81, 21/22 0.80, 22/23 0.63; k = 3 gives 9–19 | 13–20 |

Full tables for every k and both samples: `cka_summary.md`. Figures: `cka_<model>.png` (plain,
strongest direction removed, and the CKA of each layer with the next). Numbers: `cka_<model>.json`.

What the matrices show (observation): neighbouring layers are almost always very similar
(CKA of a layer with the next is above 0.9 nearly everywhere). The change is gradual, with a few
sharper steps. The last one or two layers stand apart in every model: the last layer's map is
the identity, and its CKA with the layer before is 0.6–0.9. Qwen's plain matrix shows one large
change around layers 45–50; the Gemma models change most sharply at 52/53 (27B) and 46/47 (12B).

## 2. Suggestion B: reading the readouts (a subagent, no labels)

**Method** (`scripts/band_readout_stats.py`, `prompts/band_readout.md`). Ten build-split
scenario transcripts per model, chosen by scenario ID (seed 0; the transcript with the lowest
sample index per scenario), wording Q1. For every layer, three numbers over template positions
(turn boundaries and question tokens), response tokens and self-report answer tokens:
- **readable**: share of the 16 readout tokens that are words of 3 or more letters (the
  viewer's rule);
- **next**: share of positions whose top readout token is the actual next token;
- **overlap**: how much the readout at a position repeats the readout at the next position.

A Claude Code subagent (model `claude-opus-5-5`, one per model, prompt frozen in
`prompts/band_readout.md`) read the numbers and, per transcript, the readouts at about a dozen
positions (the last prompt token, three response tokens, every post-response slot, the last
pre-answer slot, the first post-answer slot), together with the conversation text. It saw no
label. It proposed a start (readouts begin to carry words about the conversation) and an end
(before readouts become mostly the next token). Its files: `readout_suggestion_<model>.md`;
the numbers: `readout_stats_<model>.md` and `.png`; the dumps it read: `readouts/<model>/`.

| model | proposed | alternative | start reason | end reason |
|---|---|---|---|---|
| gemma-3-12b-it | 21–43 | 23–38 (narrower) | at 21 response tokens and post-response slots switch from punctuation and markup to words (readable 0.32 → 0.59) | at 44 the next token is the top readout at more than half of response and answer positions (0.49 → 0.57) |
| gemma-3-27b-it | 32–52 | 30–56 (wider) | from 32–34 the `<start_of_turn>` and newline slots show situation and act words in most transcripts; below 30 every transcript shows the same junk tokens | next stays under 0.30 through 52, climbs from 55 (0.38) to 0.57 at 58 |
| qwen3.6-27b | 38–56 | 36–58 (wider) | from 38–39 the slots stop showing newlines and special tokens and show words about the conversation | next is 0.26 at 56 for response and answer tokens, 0.30 at 57, 0.50 at 60 |
| gpt-oss-20b | 11–20 | 11–18 (narrower) | from 11 the slots show `interrogation`, `chatbot`, `replying`, and response tokens show topic words; before 11 the slots show the same fixed fragments in every transcript | next is 0.20 (response) and 0.28 (answer) at 20, 0.40 and 0.54 at 21 |

**Caveats the subagents raised** (they matter for Section 5 too):
- The first post-response slot (the turn-end token: `<end_of_turn>`, `<|im_end|>`, `<|end|>`)
  reads out itself at probability near 1 at every layer in all four models. Act words appear
  there, if at all, only at ranks 2–5.
- The `user` slot is generic: the same words in every transcript (`chatbot`, `followup`,
  `Thank`). It reflects the template's role, not the conversation.
- Words about the model's act often appear in other languages first (Chinese, Korean, Hindi,
  Bengali) and in English only at later layers. Qwen: Chinese act words fill layers 39–50 at the
  newline slot, English forms (`lie`, `denial`, `evasion`) mostly 52–58. The `readable` number
  (3 or more letters) misses Chinese words, so it understates the template positions at
  layers 30–49 for Qwen.
- Gemma-12B's `<start_of_turn>` slot carries low-probability glyph junk from 22 to about 43 in
  half of the transcripts, and readable words in the other half.
- One-word responses (`No.`) give no evidence at response tokens; the starts rest on the longer
  responses.

## 3. Where the two suggestions agree and differ (interpretation)

| model | CKA band | readout band | agreement | what to look at in the viewer |
|---|---|---|---|---|
| gemma-3-27b-it | 27–52 | 32–52 | the end agrees exactly (52/53 is the sharpest CKA step); the readout start is 5 layers later, because layers 27–31 still show junk at the slots | layers 27–34: do the post-response slots already carry words? |
| gpt-oss-20b | 13–20 (k = 3: 9–19) | 11–20 | the end agrees; the start differs by 2 layers | layers 9–13 |
| qwen3.6-27b | 34–49 | 38–56 | the start agrees within 4 layers; the ends differ: the CKA sees the directions re-arrange at 49/50 (and 45/46 in the uniform sample), while the next-token share stays low through 56 and the English act words sit at 52–58 | layers 50–58 at the newline slot after the turn end: act words or next-token guesses? |
| gemma-3-12b-it | 17–29 (k = 5: 17–29, 30–40, 41–47) | 21–43 | the readout band straddles the CKA step at 29/30; the CKA's 30–40 block covers the second half of the readout band | layers 17–22 and 29–31: does anything change at the slots across the 29/30 step? |

Recommendation (mine, to be confirmed or changed by the user): take the readout bands
(gemma-3-27b-it 32–52, gpt-oss-20b 11–20, qwen3.6-27b 38–56, gemma-3-12b-it 21–43). They are
built on the criterion the later analysis needs (words present, next token not yet dominant),
and the CKA agrees on the ends for the two models where it has a sharp step there. The two open
points are Qwen's end (49 or 56) and Gemma-12B's start (17 or 21).

## 4. How to check in the viewer

`python3 scripts/serve_viewer.py`, then open `/viewer/`. Labels are hidden by default. Type the
band as `lo-hi` in the "band" box (or add `band=38-56` to the address bar): the band's layers are
shaded in the readout table and drawn on the heatmap. The heatmap can show "top J-lens token =
actual next token" and "share of top-16 that are words of 3 or more letters" per layer and
position. The ten transcripts each subagent read are listed at the end of
`readout_stats_<model>.md`; any other transcript is as good for the check.

## 5. Files

| file | what |
|---|---|
| `scripts/fetch_weights.py` | saves the sampled unembedding rows and the final-norm weights to `data/weights/` |
| `scripts/band_cka.py` | CKA matrices, blocks, figures; `cka_<model>.json/.png`, `cka_summary.md` |
| `scripts/band_readout_stats.py` | the three numbers per layer and the dumps; `readout_stats_<model>.json/.md/.png`, `readouts/<model>/` |
| `prompts/band_readout.md` | the frozen subagent prompt |
| `readout_suggestion_<model>.md` | the four subagent reports (`claude-opus-5-5`, 2026-09-30) |

## 6. Decision (user, 2026-10-01)

Chosen in the viewer from the two suggestions above:

| model | band | compared with the suggestions |
|---|---|---|
| gemma-3-12b-it | 17–40 | the CKA start (17) and the end of the CKA's 30–40 block; inside the readout band's end (43) |
| gemma-3-27b-it | 27–52 | the CKA band; 5 layers earlier than the readout start |
| qwen3.6-27b | 35–58 | the readout alternative's end (58); start between the CKA (34) and the readout (38) |
| gpt-oss-20b | 10–20 | the readout band, one layer earlier at the start |

Note for the write-up: for Qwen3.6-27B, Agam Bhatia, Camila Blank and Neel Nanda (Alignment
Forum, 2026-07-20) used about layers 20–62 as the workspace layers. Our band 35–58 sits inside
that range.

The values are in `BANDS` in `scripts/common.py`; every later script reads them from there.

## 7. Logit-lens band (PLAN.md Section 4.4; added 2026-10-01)

For the comparison in `PLAN.md` Section 5.7 the logit lens gets a band of its own. The **logit
lens** applies the model's own unembedding (final norm plus unembedding matrix) to a layer's
residual stream directly, with no map. Because the unembedding is the same at every layer, the
token directions are identical across layers and the CKA of Section 1 would be 1 everywhere, so
only the readout suggestion applies.

**Method.** Same 10 transcripts per model, same three numbers and dumps, now from the logit-lens
readouts (`scripts/band_readout_stats.py --lens LL`; files `readout_stats_LL_<model>.md/.png`,
`readouts_LL/<model>/`). A separate frozen prompt, `prompts/band_readout_LL.md`, with the same
criteria; one `claude-opus-5-5` subagent per model, which saw no J-lens suggestion, no J-lens
dump and no label. Reports: `readout_suggestion_LL_<model>.md`.

| model | proposed | alternative | start reason | end reason | J-lens band (user's choice) |
|---|---|---|---|---|---|
| gemma-3-12b-it | 21–40 | 21–44 (wider) | from 21 the post-response slots show words about the conversation and the act (`hypocrisy`, `Avoiding`, `Truth`); below 21 fragments and foreign function words | at 41–42 the next-token share passes 0.5 (response 0.49 → 0.52, answer 0.51 → 0.56) and the first two slots switch to `<end_of_turn>`, newline and space tokens | 17–40 |
| gemma-3-27b-it | 27–50 | 27–54 (wider) | below 27 copies of template tokens, fragments, unrelated words in many languages; at 27 English words about the conversation appear at the slots and response tokens | next-token share 0.33 at 50 (response), 0.41 at 54, 0.53 at 56 | 27–52 |
| qwen3.6-27b | 35–58 | 38–56 (narrower) | at 35 the newline slot after the turn end starts showing act words (`否认`/`denial`, `撒谎`/`谎言` lie, `回避`/`evasion`, `诚实` honest); readable jumps 0.27 → 0.35 (template), 0.24 → 0.38 (response) | last layer with next-token share under 0.40 (0.39 response, 0.38 answer); above 0.5 from 60 | 35–58 |
| gpt-oss-20b | 8–14 | 10–14 (narrower) | below 7 every position shows the same unrelated fragments; from 8 response tokens show topic words and the slots show words about the chat (`Chat`, `asked`, `reply`) | at 15 the template readable share drops 0.55 → 0.29 and readouts become punctuation; from 17 response readouts are mostly the next token (0.26 at 17, 0.33 at 18) | 10–20 |

**Caveats the subagents raised.**
- gpt-oss-20b: at no layer do the post-response slots show words about deceiving or honesty in
  the logit lens; the few act-related words (`intentionally`, `honesty`) sit at response or
  prompt tokens in layers 12–14. The logit lens also commits to the next token earlier than the
  J-lens in this model (0.26 at 17 against 0.03), which is why its band ends 6 layers earlier.
- gemma-3-27b-it: almost all the usable signal sits at the `<start_of_turn>` slot (and the first
  newline slot in four transcripts); in seven transcripts one of these two slots shows a fixed
  list of single Cyrillic capital letters at about layers 34–55.
- gemma-3-12b-it: at the turn-end slot the top token from 23 on is the newline, which is also
  the actual next token; act words there sit at ranks 2–5. Response positions disagree on when
  they commit to the next token (some by 30, others not until 43–44); 40 is a compromise.
- qwen3.6-27b: as with the J-lens, the act words at the newline slot are mostly Chinese from 35
  to about 50 and English later; the `<|im_end|>` slot and the post-answer slot show junk at
  every layer.

**Observation.** For three models the logit-lens suggestion lands on or next to the J-lens band
the user chose (12B: 21–40 vs 17–40; 27B: 27–50 vs 27–52; Qwen: 35–58, the same). gpt-oss is the
exception (8–14 vs 10–20). The subagents could not see the J-lens choice.

What to check in the viewer: choose "top logit-lens token = actual next token" or "share of
top-16 that are words (logit lens)" in the heatmap menu; the readout table shows both lenses
side by side, and the band box shades the same layers in both columns.

## 8. Decision on the logit-lens band (user, 2026-10-01)

| model | logit-lens band | compared with the suggestion | J-lens band |
|---|---|---|---|
| gemma-3-12b-it | 21–44 | the wider alternative | 17–40 |
| gemma-3-27b-it | 27–54 | the wider alternative | 27–52 |
| qwen3.6-27b | 35–58 | the proposal | 35–58 |
| gpt-oss-20b | 9–14 | one layer later than the proposal's start (8), one earlier than the alternative's (10) | 10–20 |

The values are `BANDS_LL` in `scripts/common.py`.
