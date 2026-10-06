# qwen3.6-27b: suggested logit-lens layer band (PLAN.md Section 4.4)

Sources: `analysis/band/readout_stats_LL_qwen3_6_27b.md` and the ten files in
`analysis/band/readouts_LL/qwen3_6_27b/`. The model has 64 layers (L00–L63). "next" means the
share of positions whose top readout token is the token the model actually writes next.
"overlap" means how much the top-16 readout set stays the same from one position to the next.

## 1. Proposed band: 35–58

- **Start (L35):** this is the first layer where the slot right after the response (the
  newline after the turn-end token, `postresp_slot1`) shows words about the model's own act in
  most transcripts. At L34 the same slot still shows fragments such as `承 · 可是 · pa`.
  `readable` also jumps here: from 0.27 to 0.35 at template positions and from 0.24 to 0.38 at
  response tokens.
- **End (L58):** this is the last layer where fewer than 40% of response and answer positions
  read out the actual next token (`next` = 0.39 / 0.38). From L60 on, `next` passes 0.5, and
  the post-response slots switch to the next template token (`<|im_start|>`, `<|im_end|>`).

## 2. Layer regions

| layers | post-response slots | response tokens | readable (tmpl / resp) | next (tmpl / resp / ans) | overlap (tmpl / resp) |
|---|---|---|---|---|---|
| 0–18 | Spaces and punctuation (`␣ · . · , · ␣(`). The readout is nearly the same at every position. | Same punctuation set | 0.00–0.06 / 0.00–0.08 | 0.00–0.07 / 0.01–0.04 / 0.01–0.06 | 0.79→0.24 / 0.76→0.26 |
| 19–34 | Fragments and single letters (`hood · S · A · M · T · 承 · zen`). Slot 1 often shows the generic word `回答` ("answer"). | Mostly punctuation, plus a few low-probability topic words (`␣health`, `␣standards`, `␣focus`) | 0.12–0.27 / 0.11–0.24 | 0.00 / 0.05–0.09 / 0.06–0.12 | 0.05–0.17 / 0.13–0.26 |
| 35–47 | Slot 1: words about the act, mostly in Chinese (`否认` deny, `撒谎`/`谎言` lie, `假的`/`虚假` false, `隐瞒` conceal, `回避` evade, `诚实`/`如实` honest). Slot 4: words about the situation (`威胁` threat, `追问` press, `␣suspicious`, `要求` demand). Slots 2–3: generic dialogue words (`␣response · 对话 · ␣questions · 继续`). | Topic words for the conversation (`␣priority · ␣paramount`, `积木` blocks, `培养` cultivate, `␣standards`), rarely the next token | 0.35–0.40 / 0.38–0.51 | 0.00 / 0.08–0.16 / 0.11–0.19 | 0.04–0.05 / 0.08–0.12 |
| 48–58 | The same act words, now often in English and with higher top probability (`␣denial` 0.74, `␣lie` 0.66, `␣evasion`, `␣honest` 0.70). Slot 4 shows English situation words (`␣customer`, `␣threat`, `␣persistence`, `␣guest`, `␣General`). | Topic words converge on the next token whenever the continuation is predictable (`␣matters` 0.85, `␣cross` 0.94, `␣every` 0.95) | 0.41–0.65 / 0.56–0.78 | 0.00–0.11 / 0.17–0.39 / 0.19–0.38 | 0.03–0.06 / 0.10–0.16 |
| 59–63 | Slot 1 becomes `<|im_start|>`, the actual next token (L60–62). Slot 3 becomes `<|im_end|>` at p ≈ 1.0, plus the addressee's name. Slot 0 becomes `\n` at p ≈ 1.0 (L62). | Mostly the next token | 0.38–0.65 / 0.68–0.78 | 0.13–0.65 / 0.46–0.78 / 0.45–0.99 | 0.05–0.09 / 0.11–0.14 |

## 3. Evidence

- **T1, postresp_slot1:** at L34 the readout is `可是 · 上述 · 承 · 直接 · **`, which carries no
  meaning. At L38 it is `坚定 · 上述 · 回答 · 否认 · ␣denial`, and at L39 `否认 · ␣denial · 回答 ·
  坚定 · 谎言`. From L52 to L58 the top token is `␣denial` or `否认`, peaking at p 0.74 at L56. At L62
  `<|im_start|>` takes over with p 1.00.
- **T4, postresp_slot1:** L34 is `承 · 可是 · 上述 · pa · 刚`. L35 is `解释 · 上述 · 哄 · 安抚 ·
  听起来` ("explain, coax, appease"). At L55 the readout is `␣lie · ␣lies · 口径`. From L57 on,
  `<|im_start|>` and `<think>` lead. This is the clearest example of the jump at L35.
- **T8, postresp_slot1:** L39–40 read `谎言 · 撒谎 · 说谎` (lie, lying). From L55 to L58,
  `␣lie · ␣lies · ␣lying` is top with p 0.58–0.66. The readout becomes `<|endoftext|> ·
  <|im_start|>` at L62.
- **T7, postresp_slot1:** L43 reads `回答 · 措 · ␣refusal · ␣evasion · 委婉`. From L52 to L59,
  `␣evasion · 回避 · 绕` lead. At L60 `<|im_start|>` is top.
- **T6, postresp_slot1:** L45–53 read `虚假 · 虚构 · 假的` (false, fabricated). L55 reads `谎言 ·
  ␣lie · ␣lies · 说谎 · ␣falsehood`. From L60 on, `<|im_start|>` and `</think>` lead.
- **T2, postresp_slot1:** L38–47 read `如实 · 诚实 · 直` (truthfully, honest, direct). L54 reads
  `诚实 · ␣honest · ␣honesty` with p 0.70. At L61 `<|im_start|>` takes over with p 0.96.
- **T5 and T4, postresp_slot4** (the newline before the question's first word, "Was"): T5 shows
  `威胁 · ␣threat · ␣threats` at L37–53, with `␣blackmail` added at L40–41. T4 shows `␣suspicious · ␣probing` at L36
  and `␣persistence · ␣persistent` at L54–60. These are words about the user's behaviour. The
  actual next token, `Was`, never appears at any layer.
- **T5, postresp_slot3 (`user`) and slot2 (`<|im_start|>`):** slot 3 shows `hood · , · : · S`
  from L18 to L29. Slot 2 shows `A · S · T · M` from L26 to L29. These are template-like
  fragments throughout the 19–34 region.
- **Response tokens, end of band:** at T6 resp_tok47 (`␣or`), `␣cross` (the actual next token)
  is top at L55 with p 0.94. At T7 resp_tok94, `␣every` is top at L56 with p 0.95. At T1
  resp_tok72, L50–55 show `␣priority · 是最重要的 · ␣paramount`, and then `␣matters` (the next
  token) leads from L56 at p 0.85.
- **Response tokens before the band:** T1 resp_tok72 shows `␣health` at L20–25 with p ≤ 0.01.
  T2 user_prompt_last shows `␣focus` at L19–21. These topic words are real but rare and weak.
  The template slots show nothing comparable before L35.
- **T3, postresp_slot0 (`<|im_end|>`):** from L34 to L61 the readout is `承 · ъ · 典 · upy ·
  ossi`, which is junk. At L62 it becomes `\n` with p 0.98.

## 4. Alternative band: 38–56

This narrower band starts where act words appear at slot 1 in nearly every transcript: T1
`否认`, T2 `诚实`, T6 `假的`, T8 `谎言`, T9 `隐瞒` at L38–39. It ends where `next` is still at
or below 0.31 for both response and answer tokens.

- **Gained:** five fewer layers (19 instead of 24), so fewer chances for a stray word to match
  by accident. The end also sits further from the next-token takeover.
- **Lost:** the first sightings at L35–37 (T4 `安抚 · 哄`, T10 `撒谎 · 否认` at L36, T8
  `假的 · 撒谎` at L36–37). Also lost are the late English peaks at L57–58 (T8 `␣lie` 0.58–0.66,
  T1 `␣denial` 0.60/0.56, T9 `␣evasion` 0.38/0.35). Those layers are where the English
  act words are strongest.

## 5. Caveats

- **Slot 0 (`<|im_end|>`) and postans_slot0 carry nothing usable at any layer.** Their readouts
  are junk subword pieces (`典 · fox · upy · 新加坡 · .cleanup`) until L62, which reads `\n`.
- **Slots 2 and 3 (`<|im_start|>`, `user`) never show act words.** In the band they show generic
  dialogue words (`␣response · 对话 · ␣questions · 继续` "continue"). At L54 and L58, slot 2
  collapses back to punctuation (`␣ · ␣( · - · . · ,`) in 7 of 10 transcripts. T2, T5 and T10
  show `用户 · ␣user` there instead. The same collapse
  appears once at T2 slot 4, L58.
- **Language of the act words.** From L35 to about L50, act words appear mostly as Chinese
  tokens. English forms (`␣denial`, `␣lie`, `␣evasion`) lead mainly from L50 to L58. If the
  later matching uses only English word lists, the start that matters in practice is closer to
  L50.
- **preans_slot4 reads out the coming answer.** From about L38–43 to L61 it shows `是的 · ␣yes`
  or `否 · No`, and sometimes `␣honesty` (T6), `␣ethical` (T8) or `␣deception` (T3, L57–60).
  Words found here may reflect the answer the model is about to give, not its representation
  of the earlier act.
- **The end is a soft boundary.** `next` rises steadily: 0.31 at L56, 0.39 at L58, 0.46 at L59,
  0.53 at L60. Choosing 58 instead of 59 is a judgement call. L59 adds little: its slot-1 act
  words also appear at L58, and slot 3 is already `<|im_end|>` at p ≈ 1.0.
- **Three responses are a single word** (T2 and T10 "No.", T5 "Yes."). Their "response"
  positions are just `No`/`Yes` and `.`, and the `.` reads out `<|im_end|>` at p 1.00 from
  L59. These short responses pull the response `next` share upward at late layers.
