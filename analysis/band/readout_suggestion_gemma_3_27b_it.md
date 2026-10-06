# gemma-3-27b-it: readout suggestion for the layer band (PLAN.md Section 4.2)

Written from `readout_stats_gemma_3_27b_it.md` and the ten transcript dumps in
`readouts/gemma_3_27b_it/`. The model has 62 layers (L0–L61). "Slot0–slot4" are the five
post-response template tokens: `<end_of_turn>`, `\n`, `<start_of_turn>`, `user`, `\n`.
In the statistics, `readable` is the share of readout tokens that are words of 3 or more letters.
`next` is the share of positions whose top readout token is the actual next token.
`overlap` measures how much the readout stays the same from one position to the next.

## 1. Proposed band: 32–52

- **Start (L32):** from about L32–34, the `<start_of_turn>` and `\n` slots show words about the situation and the model's act in most transcripts, such as unethical, dishonesty, truth, secret, avoiding and denial. Below L30 these slots show the same junk tokens in every transcript.
- **End (L52):** at L52, `next` is still under 0.30 (0.27 for response tokens, 0.29 for answer tokens). From L55 it climbs past 0.38 and reaches 0.57 at L58. Several slot-2 readouts also switch from act words to names and topic nouns around L53–55.

## 2. Layer regions

| Layers | Post-response slots | Response tokens | readable (template / response) | next (response) | overlap (template / response) |
|---|---|---|---|---|---|
| 0–10 | The same junk tokens in every transcript: slot0 `—“ ⸨ ⓪`, slot1 `</i> ς ের`, slot2 `～～ ℝ $$\`, slot3 `</blockquote> --*/` (probability near 1.0) | Punctuation variants of the current token (`,.. ,,,, ,...`) | 0.05–0.11 / 0.05–0.13 | 0.00 | 0.01–0.02 / 0.01–0.04 |
| 11–24 | Still identical junk: braille blanks, `阅读全文` ("read full text"), `</h6>`, `''' }}^{\`, code-comment tokens. From L16, slot3 shows `chatbot` at ranks 3–5 | Punctuation copies, then filler from ~L17 (really, pretty, big, kids) | 0.05–0.28 / 0.10–0.36 | 0.00–0.01 | 0.01–0.04 / 0.03–0.07 |
| 25–31 | Transition. Slot0's top token becomes its own token `<end_of_turn>` (p≈1.0). Slot1 shows `<eos> </blockquote> ៕`. Slot2 shows `!!!! ?!?!` and emoji (😂 🤔 ⚠️ 🤫). Slot3 shows 질문/답변/ответить ("question/answer/to reply") at p 0.01–0.15. Slot4 shows asking/wondering/replying | Filler (really, indeed), then the first topic words (mistake, criticizing, confidentiality) | 0.25–0.46 / 0.41–0.62 | 0.01–0.04 | 0.03–0.09 / 0.08–0.13 |
| 32–47 | Slot2 and slot1 carry topic words and words about the model's act (see Evidence). Slot3 shows reply/question words, then analysing, replying, 扮演 ("play a role") and continue words. Slot4 shows 我现在 ("I now"), Seems, Interesting, Explain. Slot0 keeps `<end_of_turn>` on top; ranks 2–5 show ChatGPT, chatbot, 🤖, Disclaimer, ⚠️, 🤫 | Topic words tied to the content (misunderstanding, jealousy, directives, ambiguity, compliance) | 0.45–0.73 / 0.63–0.81 | 0.02–0.16 | 0.04–0.10 / 0.13–0.17 |
| 48–54 | In all 10 transcripts, slot3 becomes `followup/follow` (p 0.4–1.0) and slot4 becomes okay/thank/wonderful. Slot2 keeps act words in some transcripts and switches to names or topic nouns in others (Ralph, management, podcast, customer). The pre-answer slot shows the actual answer (Yes/No) at p 0.8–1.0 | Topic words, with the actual next token rising to the top | 0.75–0.79 / 0.84–0.88 | 0.18–0.31 | 0.03–0.04 / 0.11–0.13 |
| 55–61 | Slot2 decays to names, then fragments (`s`, `t`, `re`) at L60–61. Slot3 becomes `\n`. The pre-answer slot shows the answer token | Mostly the actual next token | 0.52–0.83 / 0.69–0.88 | 0.38–0.97 | 0.03–0.05 / 0.08–0.10 |

## 3. Evidence

- **T8, postresp_slot2 (`<start_of_turn>`):** L30 `⚠️ · unethical`. From L34 to L57, `unethical` is the top token at p 0.88–1.00, with dishonesty (L37–49) and wrongdoing (L40–41). L60 shows `withholding`.
- **T7, postresp_slot2:** L32 `🫤 · 😬 · 🤐 · 🤥 · unethical`. From L37 to L53, `unethical · dishonesty · ethical` appear at p ≥ 0.81. L58 shows `dilemma`.
- **T3, postresp_slot2:** from L33 to L47 the readouts are 真相 / सच्चाई ("truth"), 秘密 ("secret"), betrayal and 거짓 ("lie"). From L48 to L53 they are 거짓 · झूठ ("lie") · deceit · deception. From L55 they are `museum`.
- **T4, postresp_slot2:** Avoiding / 避免 ("avoid") from L35 to L44. Redirection / subtly / steering from L46 to L53. Upholding / deflect at L54–55.
- **T10, postresp_slot1 (`\n`):** L34 `মিথ্যা ("lie", Bengali) · denials · 거짓 · झूठ · denial`. Denial/denials from L40 to L46, confidently from L48 to L55, firm at L56–57. In slot2, 🤫 / 🤐 / خفیہ ("secret") / 秘密 run from L33 to L38. After that come 内部 ("internal", L39–47) and management (L48 onward).
- **T8, postresp_slot1:** denial / denials / denying from L38 to L57, at p ≥ 0.95 from L49 to L57.
- **T6, postresp_slot1:** at L30–34, `Avoiding · এড়িয়ে ("avoid") · 避免 · умолча ("keep silent")` appear at ranks 1–5. From L42, generic answer words (回答, پاسخ) take over.
- **Below L25, all ten transcripts give the same junk.** Slot3 is `</blockquote>` at p ≈ 1.00 from L10 to L22. Slot2 is `$$\ · ''' · }}^{\` from L11 to L22. Slot1 is `</i> · </blockquote> · 阅读全文` from L10 to L23.
- **Response-token start:** in T5 resp_tok52 (`a`, next token `total`), L17–30 show big / kids / really / kinda. L31 shows `mistake` at p 1.00, and mistake/misunderstanding lasts to L57; `total` wins at L61. In T3 resp_tok300 (`focused`), criticizing / accusations appear from L30 to L54, and the next token `on` takes over at L55.
- **Next-token takeover:** in T8 resp_tok28 (`any`), the next token `elaboration` is on top from L45 at p 0.77–1.00. At preans_slot4, the answer token is on top at p ≥ 0.9 from L47 in T2, T6 and T8, and from L46 in T1.
- **Slot2 without act words:** T9 shows strategy (戦略, 전략) at L32–38 and `Ralph / CEO` at L50–59. T1 shows followup / explanation. T2 shows remediation / corrective at L39–60, at p up to 1.00.

## 4. Alternative band: 30–56 (wider)

- **Gained:**
  - The first act words at L30–31: T8 `unethical` at L30 and T6 `Avoiding` at L30–31.
  - The tail of the act words at L53–57: T7 and T8 `unethical`, T8 `denial` and T3 `deceit`.
- **Lost:**
  - At L55–56, response `next` is 0.38–0.42 and answer `next` is 0.41–0.47, so nearly half of those readouts are simply the next token.
  - The pre-answer slot is the Yes/No answer itself.
  - L30–31 add mostly `!!!!`, `?!?!` and emoji at slot2, which makes it harder to show that a hit comes from content.
- **Narrower option (34–48):** this avoids both edges and still contains the core of every act-word run above. It loses T8's L30–33 and T10's L33 `🤫`.

## 5. Caveats

- **postresp_slot0 is a copy at every layer in the band.** Its top token is its own token, `<end_of_turn>`, at p ≈ 1.00 from L26 to L61 in all ten transcripts. Content words appear only at ranks 2–5 (ChatGPT, chatbot, Disclaimer, ⚠️, 🤫, warning). Any band will read this slot only through the lower ranks of the top 16.
- **postresp_slot3 (`user`) is generic.** It shows question/answer words at very low probability (0.01–0.15) from L24 to L38, then reply and role-play words, then `followup` in all ten transcripts from L48 to L58. It barely differs between transcripts.
- **Transcripts disagree at slot2.** Six transcripts (T3, T4, T5, T7, T8, T10) show words about the model's act. Four (T1, T2, T6, T9) show next steps, customers or names instead.
- **Many act words first appear in other languages.** Examples are 거짓, झूठ and মিথ্যা ("lie"), and 避免 ("avoid"). The English forms often come later: in T3, `deceit / deception` appears only at L48–54. A fixed text-matching rule that uses English words only would push the useful start later. It would also make the L48–52 end region matter more.
- **`next` is an average.** Predictable tokens resolve early (T6 `deciding` is on top at p 1.00 from L38), so no single end layer is free of next-token readouts.
- **The sample is small and narrow.** It covers 10 transcripts, all from the provided-facts scenario family with the same question wording.
