# qwen3.6-27b: readout suggestion for the layer band (PLAN.md Section 4.2)

Written from `analysis/band/readout_stats_qwen3_6_27b.md` and the ten dumps in
`analysis/band/readouts/qwen3_6_27b/`. The model has 64 layers (L00–L63). "Slot1" to "slot4"
are the post-response positions: `\n` after the turn end, `<|im_start|>`, `user`, and the `\n`
before the question. "Preans" is the last `\n` before the answer. Many readout words are
Chinese; their meaning is given in brackets.

## 1. Proposed band

**38–56**

- **Start (L38):** this is the first layer where the post-response slots and the pre-answer slot
  stop showing newlines, underscores and special tokens and start showing words about the
  conversation (questioning, threats, lying, honesty); response tokens also switch to topic
  words here.
- **End (L56):** this is the last layer where the actual next token is still a minority. At L56
  `next` is 0.26 for response tokens, 0.26 for answer tokens and 0.12 for template positions.
  From L57 on it climbs steadily to 0.78 / 0.99 at L63, and response-token dumps often show the
  next token as the top readout with probability above 0.9.

## 2. Layer regions

| Layers | Post-response slots | Response tokens | Template readable / next / overlap | Response readable / next / overlap |
|---|---|---|---|---|
| 0–10 | Punctuation, the same unrelated junk tokens in every transcript (`Shemale`, `milfs` at L03), `但不限于` [including but not limited to] at slot2, runs of spaces and newlines | Punctuation and fragments | 0.02–0.43 / 0.00 / 0.03–0.22 | 0.01–0.57 / ≤0.03 / 0.04–0.37 |
| 11–29 | `\n\n`, `____`, `<|im_end|>`; `\n\n` often has probability near 1.00 (L18–L28) | Filler words (`stuff`, `folks`, `truly`), copies of the current token (`anniversary`, `happy`), and a few weak topic words at low probability | 0.02–0.30 / ≤0.03 / 0.04–0.41 | 0.28–0.68 / 0.01–0.03 / 0.03–0.20 |
| 30–37 | Fullwidth question marks, `…**`, Chinese function words `的` `中` `在` [of, in, at]; slot4 starts showing `询问` [ask] at L35–L37 | Topic words firm up (`prestigious`, `kids`, `routine`) | 0.03–0.11 / 0.00 / 0.20–0.30 | 0.37–0.70 / 0.02–0.04 / 0.14–0.17 |
| 38–49 | Words about the situation and the model's act: slot1 shows lying, denial, evasion, concealment; slot2 and slot3 show `回答` `回复` `对话` [answer, reply, conversation]; slot4 shows the user's behaviour (questioning, threats, suspicion); preans shows `ethical`, `truthful`, `intentionally` | Clear topic words (`safety`, `vacation`, `scheduled`, `toys`, `procedures`) | 0.20–0.39 / 0.00–0.02 / 0.10–0.15 | 0.70–0.84 / 0.03–0.07 / 0.17–0.20 |
| 50–56 | Slot1 still shows act words, now often in English (`denial`, `lie`, `evasion`, `falsehood`); slot3 is taken over by `<|im_end|>` and `<think>` at 0.88–1.00; slot2 turns to `user` / `assistant`; slot4 turns to the person being addressed (`customer`, `employee`, `General`); preans turns to `yes` / `否` [no] | Topic words sharpen toward the next word | 0.38–0.58 / 0.03–0.12 / 0.06–0.10 | 0.64–0.72 / 0.07–0.26 / 0.17–0.20 |
| 57–63 | Slot1 and slot3 collapse to `<|im_start|>`, `<|im_end|>` or the user's name at 0.9–1.00; slot4 shows the addressee or the next word | Mostly the actual next token | 0.38–0.62 / 0.08–0.65 / 0.07–0.09 | 0.68–0.77 / 0.30–0.78 / 0.10–0.16 |

## 3. Evidence

- **Transcript 8, slot1, L39–L48:** `谎言 · 说谎 · 欺骗 · 隐瞒` [lie, lying, deceive, conceal],
  top probability 0.22–0.84. At L55–L58 the English form appears: `␣lie · 谎言 · ␣lies · ␣lied`.
  At L59–L63 the slot collapses to `<|im_end|>` / `<|im_start|>` (0.93–1.00).
- **Transcript 9, slot1, L42–L54:** `隐瞒 · 回避 · 否认 · ␣misleading · ␣evasion` [conceal,
  evade, deny]; L53 `回避 · ␣evasion · 避 · 避开 · ␣evade` (0.87). At L60 it becomes
  `<|endoftext|> · <|im_end|> · <|im_start|>` (0.85).
- **Transcript 10, slot1, L40–L58:** `说谎 · 谎言 · ␣fals · 撒谎` [lying, lie, lie], then
  `␣falsehood` (L47–L54) and `␣denial · ␣lied` (L55–L58). At L61–L63 it becomes `<|im_start|>` (0.96–1.00).
- **Transcript 1, slot1, L39–L58:** `否认 · 谎言 · 说谎 · fake` [deny, lie, lying] from L39, then
  `␣denial · ␣denying · ␣deny` at L52–L58 (0.58–0.82). Slot1 at L00–L38 shows only `\n\n`,
  `____` and `<|im_end|>`.
- **Transcript 7, slot1, L40–L49:** `回答 · 回避 · 拒绝 · ␣refusal` [answer, evade, refuse];
  `␣evasion` appears at L53–L59. This matches a response that declined to confirm or deny.
- **Transcript 4, slot4, L36–L57:** `␣suspicious · ␣questioning · 质疑 · 追问` [question, press
  further] (0.28–0.92). From L58 on it becomes `␣persistence`. At L00–L35 the slot shows
  junk, underscores and question marks.
- **Transcript 5, slot4, L40–L54:** `威胁 · ␣blackmail · ␣threats · ␣threatening` [threat]
  (0.36–0.70). At L55–L56 it becomes `␣employee · 员工` [employee]. This names the user's role,
  not the act.
- **Transcript 6, preans, L38–L44:** `␣intentionally · ␣intentional · ␣deliberately · ␣ethical`.
  At L51–L52 `欺骗` [deceive] enters the top 5. L54–L59 shows `␣honesty · 诚实 ·
  ␣technically` (0.32–0.87). At L61–L63 it becomes `<think>` (0.93–1.00), the actual next token.
- **Transcript 1, resp_tok72 (`-being`, next `␣matters`):** L36–L47 shows `␣safety · ␣health ·
  ␣priorities`. At L56–L61 the readout is `␣matters · ␣comes` at 0.61–0.98, so the next token
  has taken over.
- **Transcript 3, resp_tok284 (`␣But`, next `␣if`):** the readout is `␣if` at 0.92 by L52 and
  at 0.99–1.00 from L54. This is the earliest next-token takeover in the dumps. It is also why
  the end should not go much past L56.
- **Transcript 8, resp_tok25 (`␣with`, next `␣his`):** L28–L37 shows `␣kids · ␣toys ·
  ␣children` (0.56–0.93), which is early topic content. The stats back this: response `readable`
  jumps from 0.48 at L35 to 0.64 at L36 and 0.73 at L38.

## 4. Alternative band

**36–58 (wider).**

- **Gained:**
  - It captures the earliest topic words at slot4. Examples: `␣suspicious` in transcript 4 at
    L36, and `询问` / `质疑` [ask, question] in transcripts 3 and 7 at L35–L37.
  - It keeps two more layers of English act words at slot1. Examples: `␣lie · ␣lied` in
    transcript 8 at L58, `␣denial` in transcripts 1 and 10 at L57–L58, and `␣evasion · ␣evade`
    in transcript 9 at L57–L58.
- **Lost:**
  - At L57–L58 `next` rises to 0.30–0.35 for both response and answer tokens.
  - Preans is already `yes` / `否` [no], which is close to the answer itself.
  - Slot4 is mostly the addressee's name or role (`General` 0.91–0.97, `guest` 0.42–0.54).
  - L36–L37 adds mostly question marks and `<|im_end|>` at slot1 to slot3.

A narrower band such as 40–52 would keep `next` at or below 0.12 at response tokens. However,
it would drop most English act words, which appear at L52–L58.

## 5. Caveats

- **Two slots carry nothing at any layer.** The post-answer slot and postresp slot0 (both
  `<|im_end|>`) are template tokens at every layer in all ten transcripts. The post-answer slot
  is `<|endoftext|> · <|im_end|> · <|file_sep|>` at 1.00 from about L30 to L53, then unrelated
  Chinese characters. Postresp slot0 is `<|im_end|>` at 0.9–1.00 from L14 to L61. The only
  exceptions are `解读 · interpret` [interpret] at L58–L59 in transcripts 1 and 6.
- **The language changes with depth.** At slot1, Chinese act words (`谎言`, `说谎`, `否认`,
  `隐瞒`) dominate L39–L50. English forms (`lie`, `denial`, `evasion`, `falsehood`) mostly
  appear at L52–L58. If later matching uses English words only, the effective start is nearer
  L47–L52 than L38.
- **The template `readable` numbers understate content in L30–L49.** `readable` counts only
  words of 3 or more letters, so Chinese words do not count. Template `readable` stays at
  0.03–0.39 through L30–L49 even where the dumps clearly show topic and act words.
- **The onset at slot1 differs by transcript.** Transcripts 1, 8 and 10 start at L39.
  Transcripts 4, 5 and 6 start at L42–L43.
- **Transcripts 4 and 6 lose slot1 early.** Their slot1 act words (`fake`, `虚假` [false])
  give way to special tokens at L49–L54, well before L56.
- **The model's own act and the user's behaviour share the same layers.** Slot4 consistently
  reflects the user's behaviour (questions, threats, suspicion), not the model's act. Slot2 and
  slot3 mostly show generic `answer` / `reply` / `conversation` words. Words about the model's
  act concentrate at slot1 and preans.
- **Short responses have no content at response tokens.** Transcripts 2, 5 and 10 have one-word
  responses (`No.` / `Yes.`). Their response tokens show only newlines and `<|im_end|>` at all
  layers, so they give no evidence for the start.
