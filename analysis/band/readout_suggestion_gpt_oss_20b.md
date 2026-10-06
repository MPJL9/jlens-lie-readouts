# gpt-oss-20b: readout suggestion for the layer band (PLAN.md Section 4.2)

Written from `analysis/band/readout_stats_gpt_oss_20b.md` and the ten dumps in
`analysis/band/readouts/gpt_oss_20b/`. No other file in `analysis/` was read. The model has
24 layers (L00–L23).

## 1. Proposed band: 11–20

- **Start at L11.** From L11, most post-response slots and response tokens carry words
  about the conversation. Examples are `interrogation` at the `<|start|>` slot, `chatbot` and
  `thanking` at the `user` slot, `replying` and `apologized` at the pre-answer slot, and topic
  words such as `stolen`, `conference` and `sidewalk` at response tokens. Before L11 the
  post-response slots show fixed fragments that are the same in every transcript.
- **End at L20.** Up to L20 the top readout token is the actual next token at only 20% of
  response positions and 28% of answer positions. At L21 these shares jump to 40% and 54%,
  and the top-token probability at every template slot rises to 0.89–1.00.

## 2. Layer regions

"Post-response slots" are the four gpt-oss turn-boundary tokens between the response and
the question: `<|end|>` (slot 0), `<|start|>` (slot 1), `user` (slot 2) and `<|message|>`
(slot 3). The pre-answer `assistant` slot is included in this column. Statistic ranges are
readable / next / overlap. T = template positions, R = response positions, A = answer positions.

| Layers | Post-response slots show | Response tokens show | Typical stats |
|---|---|---|---|
| 0–8 | The same fixed fragments in every transcript. Slot 0: `subsequently`, `fourteen`, `(§`, `‘‘`. Slot 1: `ssp`, `ske`, `ibid`, `kong`. Slot 2: code fragments (`":`, `Customizer`, `=create`, `-chat`). Slot 3: dash fragments (`—not`, `—as`, `(§`). Pre-answer: `fourteen`, `twelve`, `chief`. | Function words and punctuation (`the`, `of`, `in`, `.”`, `?”`). | T 0.41–0.62 / 0.00 / 0.01–0.06; R 0.45–0.68 / 0.02–0.05 / 0.05–0.11 |
| 9–10 | Transition. Slot 2 and the pre-answer slot move to `chatbot`, `Reviewer`, `Advisor`, `replying`. Slot 1 is still `kong`, `ibid`, `pett`, `speaker`. Slots 0 and 3 are unchanged. | The first topic words appear: `somewhere`, `stolen` (T1), `advertised`, `servicing`, `sidewalk` (T5), `rumors` (T9). | T 0.44–0.52 / 0.00–0.03 / 0.02–0.03; R 0.72–0.74 / 0.02–0.04 / 0.08 |
| 11–14 | Slot 1: `interrogation`, `interloc`, `inviter`, `interviewer`, `chatbot`. Slot 2: `chatbot`, `thanking`, `replying`, `wanting`. Slot 3: `—not` until L12, then `“Yes`, `“Well`, `replying`, `politely`, `apologized`. Pre-answer: `chatbot`, `replying`, `apologized`. Slot 0: quote-and-newline tokens plus `全文` and `正文` (Chinese for "full text" and "main text"). | Clear topic words: `stolen`, `overnight`, `unauthorized`, `reprim(and)`, `dismissal`, `scheduled`, `inspection`, `safety`, `hiring`, `paycheck`, `streets`. | T 0.46–0.51 / 0.00 / 0.05–0.10; R 0.74–0.86 / 0.02 / 0.10–0.13 |
| 15–18 | Multilingual genre words at very low probability (top probability 0.00–0.03): `点评` (review), `免责声明` (disclaimer), `回复` (reply), `-feedback`, `投诉` (complaint), `댓글` (comment), `sí`. Slot 3 shows `sarcas(tic)`, `thanked`, `“If`, `“What`, and then `sorry`, `Want`, `Reply` at L18. | Topic words continue (`safe`, `safest`, `trustworthy`, `inspirations`, `vibes`, `gameplay`, `timing`, `tweaks`). Short one-word responses fall back to punctuation (`.”\n\n`). | T 0.37–0.47 / 0.00–0.02 / 0.08–0.11; R 0.54–0.65 / 0.01–0.05 / 0.14–0.18 |
| 19–20 | Slot 0: `<|start|>` is top (the actual next token), probability 0.08–0.44. Slot 1: `assistant`, 0.11–0.56. Slot 2: `-feedback`, `回复`, `点赞`. Slot 3: openers of a user reply (`Thanks`, `okay`, `Why`, `Want`, `Continue`). Pre-answer: `<|channel|>`, `回复`, `免责声明` at 0.01–0.03. | The strongest topic words (`inspectors`, `gambling`, `wagering`, `aromas`, `urgently`, `cleared`). Some positions already show the next token (T5 `cleared` 0.96 at L20). | T 0.43–0.51 / 0.26–0.34 / 0.04–0.05; R 0.65–0.67 / 0.10–0.20 / 0.09–0.14; A next 0.14–0.28 |
| 21–23 | Format tokens at probability 0.89–1.00. Slot 0: `<|start|>`. Slot 1: `assistant`. Slot 2: `<|message|>` or `<|channel|>`. Pre-answer: `<|channel|>`. Slot 3: `Thanks`, `What`, `I`. | Mostly the actual next token (`any`, `tract`, `done`, `operating`, `<|return|>`). | T 0.39–0.61 / 0.49–0.51 / 0.04–0.08; R 0.63–0.73 / 0.40–0.89; A 0.54–0.97 |

## 3. Evidence

- **T1, postresp_slot1 (`<|start|>`).** L00–L10 show `ssp`, `ske`, `ibid`, `kong` at every
  layer. L11–L12 show `interrogation` and `interrog`. L13–L14 show `interloc`, `inviter`,
  `interviewer` and `chatbot`. L15–L18 show `-chat`, `点评` and `-feedback` at 0.01–0.02. L21
  shows `assistant` at 0.99. The same sequence appears in all ten transcripts.
- **T2, postresp_slot2 (`user`).** L00–L03 show `":`, `"\n` and `":\n` (0.71 at L00). L04–L07
  show `Customizer`, `Autocomplete` and `-chat`. L11–L14 show `chatbot`, `wanting`,
  `thanking` and `replying`. L21 shows `<|message|>` at 0.73.
- **T7, postresp_slot3 (`<|message|>`).** L00–L12 show dash fragments (`—not`, `—a`,
  `—even`). L14 shows `politely`, `apology`, `replying`, `apologized` and `replied`. L20–L22
  show reply openers (`Thank`, `Explain`, `Continue`).
- **T10, postresp_slot3.** L13 shows `replied`, `apologized` and `apology`. L15–L17 show
  `sarcas`. L19–L21 show `Why` at 0.34–0.58. These are the closest words to the model's own
  act that appear at a post-response slot. They all fall inside 11–20.
- **T1, resp_tok17 `taking` (next `tools`).** L00–L08 show `the`, `in` and `on`. L10–L14
  show `stolen`, `outside`, `overnight` and `unauthorized`. L17 shows `unauthorized` and
  `inventory`. L21 shows `any` at 0.94, and `tools` first appears at L22.
- **T3, resp_tok102 `was` (next `operating`).** L00–L12 show `the`, `outside` and
  `officially`. L13–L20 show `safety`, `safe`, `safely` and `trustworthy`. L21–L22 show
  `functioning` and `operating` at 0.49–0.66.
- **T3 and T9, user_prompt_last.** In T3, L07–L14 show `Everyone`, `They'll` and `that'll`.
  L19 shows `honesty` (0.66), `诚信` (integrity) and `Honest`, and `honesty` is still top at
  L21. In T9, L13 shows `unethical` and `illegal`. L17–L20 show `wrongdoing`, `违法`
  (illegal) and `illegal`, and L21–L22 show `cheating`.
- **Pre-answer slot `assistant` (all transcripts, T5 as the example).** L00–L02 show
  `fourteen`, `twelve` and `chief`. L09–L14 show `chatbot`, `replying`, `replied` and
  `apologized`, with probability rising to 0.36. L15–L20 show `回复` and `免责声明` at
  0.01–0.08. L21 shows `<|channel|>` at 0.97.
- **postresp_slot0 `<|end|>` (all transcripts).** L00–L06 show `subsequently`, `fourteen`
  and `(§`. L07–L14 show `’\n\n`, `×\n\n`, `全文` and `正文`. L15–L18 show `点评`, `免责声明`
  and `sí` at 0.00–0.01. L19–L20 show `<|start|>` at 0.08–0.44. L21–L23 show `<|start|>` at
  0.96–1.00.
- **T6, T7 and T10, one-word response `No`.** L02–L10 show punctuation (`?”`, `.”`, `,`).
  L11–L13 show `regrets`, `surprises` and `spoiler`, and T10 also shows `misinformation` and
  `apology`. L19–L20 show `<|return|>`. L21 shows `<|return|>` or `.` at 0.77–0.92.

## 4. Alternative band: 11–18

This band drops L19–L20.

- **Gained:** no layer in the band has a noticeable next-token share. At template positions
  `next` is at most 0.02, and at response positions it is at most 0.05. At L19–L20 slot 0
  already shows the actual next token `<|start|>`. Slot 3 already shows guesses at the user's
  next message (`Thanks`, `Why`), which are next-token guesses even though the actual next
  token `Was` never appears.
- **Lost:** L19–L20 carry the strongest topic words of the whole stack. Examples are
  `honesty` (T3), `wrongdoing` and `违法` (T9), `Immediate` and `Threat` (T1), and `Quickly`
  and `urgency` (T5) at the last user-prompt token. The same two layers hold `inspectors`,
  `gambling` and `wagering` at response tokens. Without them, the post-response slots in the
  band contribute only L11–L14 of clearly readable words, because L15–L18 are low-probability
  genre words.

A wider start (L09 or L10) would add `chatbot` and `replying` at slot 2 and the pre-answer
slot. It would also add early topic words at response tokens. Slots 0, 1 and 3 still show
the fixed fragments there, so the gain is small.

## 5. Caveats

- **Slot 0 (`<|end|>`) never carries conversation words.** From L00 to L18 it shows
  punctuation, document-format tokens (`全文`, `正文`, `™\n\n`) or low-probability genre
  words. From L19 on it is the actual next token. Any hits at this slot in the band will be
  rare.
- **Slot 3 (`<|message|>`) changes meaning inside the band.** L11–L17 show words about
  replying (`replying`, `politely`, `apologized`, `sarcas`). L18–L20 show openers of the
  user's next message, which are next-token guesses.
- **The readouts at post-response slots are nearly identical across the ten transcripts.**
  The same tokens appear at the same layers regardless of topic. At these slots the band
  mostly captures the template's role in the conversation (reply, chatbot, feedback), not the
  transcript content.
- **The L15–L18 dip.** `readable` falls to 0.37–0.47 at template positions, 0.54–0.65 at
  response positions and 0.47–0.63 at answer positions (from 0.73–0.86 at L11–L14). The top-token probabilities at template slots are
  0.00–0.03. These layers are inside the band but add mostly multilingual genre words.
- **Some response positions reach the next token before L21.** T5 `street` already shows
  `cleared` at 0.96 at L20, and T2 `’re` shows `finished` at 0.63. The end at L20 therefore
  admits a few next-token readouts. Averaged over all positions, the `next` share is still
  only 0.20.
- **One-word responses (T6, T7, T8, T10) give no topic signal at response tokens.** Their
  single response token shows punctuation at most layers, so the start is based on the
  longer responses (T1–T5, T9).
