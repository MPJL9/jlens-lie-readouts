# gemma-3-12b-it: logit-lens layer band suggestion (PLAN.md Section 4.4)

Sources: `readout_stats_LL_gemma_3_12b_it.md` and the ten dumps in `readouts_LL/gemma_3_12b_it/`.
The model has 48 layers (L0–L47). "Slot0" to "slot4" are the post-response slots: `<end_of_turn>`, `\n`, `<start_of_turn>`, `user`, `\n`.

## 1. Proposed band: 21–40

- **Start (L21):** this is the first layer where the post-response slots and the response tokens regularly show words about the conversation and the model's act. Examples are "hypocrisy", "Protect", "Avoiding", "Truth" and "motivations". Below L21 the readouts are template-token fragments, foreign function words, or the word "question" in other languages.
- **End (L40):** this is the last layer before two things happen at L41–42. First, the response and answer `next` share passes 0.5 (response 0.47 at L40, 0.52 at L42; answer 0.49 at L40, 0.51 at L41). Second, slot0 and slot1 switch to `<end_of_turn>`, newline and space tokens.

## 2. Layer regions

| Layers | Post-response slots | Response tokens | readable (tmpl / resp) | next (tmpl / resp / ans) | overlap (tmpl / resp) |
|---|---|---|---|---|---|
| 0–13 | Fixed fragments with top probability near 1.00. Slot0 shows `er · ر · з · ت`, slot1 `in · is · ak`, slot2 `U · D · K` then `I · K`, slot3 `ת · sthe · IAMS · ዬ`, slot4 `in · m · ak`. | Subword fragments and scripts unrelated to the text, then `␣and · ␣in · ␣is`. | 0.16–0.24 / 0.41–0.53 | 0.00 / 0.00–0.04 / 0.00–0.04 | 0.01–0.06 / 0.01–0.09 |
| 14–20 | Top probability about 0.00. Slot0 still shows `er · ر`. Slot3 shows the word "question" in other languages (`ถาม · pergunta · pytanie · 質問`). Slot4 shows first-person words in other languages (`私は · ഞാൻ · minha`). Slots 1 and 2 show foreign function words and `Ombudsman`. | Function words (`and · in · is · are`) and foreign tokens. Topic words appear only rarely. | 0.25–0.41 / 0.36–0.46 | 0.00 / 0.04–0.05 | 0.04–0.08 / 0.08–0.12 |
| 21–26 | Transition region. Slot0 changes from `er` to `\n · Reply · Note · Your`. Slot1 shows `Honestly · Acknowled · Reply · Continue · hypocrisy · Invite`. Slot2 shows the first act words: `wouldn · Protect · 🤫 · Sadly · Unfortunately · loyalty · refusal · deny`. Slots 3 and 4 show `That · I · What · Okay`. | Topic words related to, but not equal to, the next token (`expediency · adaptability`, `motivations · intentions`, `accountability · forgiveness`). | 0.52–0.78 / 0.53–0.84 | 0.00–0.10 / 0.05–0.20 / 0.05–0.20 | 0.04–0.11 / 0.07–0.11 |
| 27–40 | Content region. Slot0's top token is `\n` (the actual next token); ranks 2–5 hold `your · hiding · hide · embedding · CEO`. Slot1 holds act or topic words (`denial · evas · dodging`, `reassuring · misleading · vague`, `investor`, `Disclaimer`). Slot2 holds act or topic words (`denying · refusal`, `company · our`, `silence · loyalty · job`, `protecting · withholding`) in half the transcripts. Slot3 shows `ChatGPT · Thank · What`. Slot4 shows `Thank · Okay · That` with probability 0.8–0.98. | The next word plus close synonyms. The top-token probability often exceeds 0.9 from about L30–35. | 0.78–0.83 / 0.84–0.88 | 0.05–0.21 / 0.24–0.47 / 0.25–0.49 | 0.04–0.13 / 0.08–0.13 |
| 41–47 | Template tokens: `<end_of_turn> · \n · ␣ · ( · [`, digits, HTML tags. Act words fade out by L43–45 (except in transcript 10). | The actual next token, with probability near 1.0 by L46–47. | 0.82 → 0.55 / 0.87 → 0.73 | 0.13–0.29 / 0.49–0.84 / 0.51–0.98 | 0.04–0.08 / 0.07–0.09 |

## 3. Evidence

- **Transcript 2, slot2, L26–39:** `refusal · deny · denying · denied · denial · discourage · discouraging`. By L43 it shows `␣ · ␣( · implying`, and L47 shows `<end_of_turn>`.
- **Transcript 10, slot1:** L27–35 shows `refusal · denial · denials · denying · deny`. L36–40 shows `dodging · evas · evasion · dodge`. L41–45 shows `deflection · dodge · non`. L46–47 shows `<end_of_turn> · Avoid`. This is the only transcript where act words at a slot clearly continue past L40.
- **Transcript 7, slot1, L26–42:** `reassurance · reassuring · reassure`. `misleading` appears at L30–34 and `vague` at L38–39. By L45 the readout is `␣ · 1 · A · 2 · 0`.
- **Transcript 6, slot2:** L21 shows `wouldn · doesn · 🤫 · Protect · Avoiding`. L29–43 shows `loyalty · consequences · silence · job · career`. Slot1 at L19–22 contains `거짓` (Korean for "lie"), `नहीं` and `hypocrisy`.
- **Transcript 9, slot2:** L22 shows `🤫 · Truth · Honestly · truthfully`. L33–41 shows `protecting · protect · withholding · preserving`. From L44 on it shows `␣ · \n · (`.
- **Transcripts 1, 4 and 7, slot0, L35–40:** the top token is `\n` (the actual next token), with `hiding · hide` at ranks 2–4. In transcript 1, `hiding` stays at rank 2–3 through L45, behind `\n` and `<end_of_turn>`.
- **All ten transcripts, L0–13:** slot0 shows `er · ر · з · ت` with probability 1.00 at L0–10, and slot3 shows `ת · sthe · IAMS · ዬ · 誦`. These readouts are identical across transcripts, so they carry no conversation content.
- **Transcripts 4 and 9, response tokens, onset of topic words:** in transcript 4, resp_tok52 (`prioritize`) shows `prioritization · expediency · efficiencies · adaptability` at L21–23 and `speed` (the next token) only from L32. In transcript 9, resp_tok25 (`his`) shows `motivations · demeanor · intentions · ambitions` at L21–24, then `intentions · plans · departure` at L29–47.
- **Transcripts 1 and 3, response tokens commit early:** in transcript 1, resp_tok7 (`was` → `indeed`) has `indeed` on top from L26, at probability 0.97 at L30 and about 1.00 at L33–47. In transcript 3, resp_tok129 has `reflect` at probability 0.96 from L34. So some response positions show only the next token well before L40.
- **Transcripts 4 and 8, response tokens switch late:** in transcript 4, resp_tok78 (`was` → `not`) shows `unforeseen · unexpected · regrettable` at L26–44 and `not` only from L45. In transcript 8, resp_tok195 shows `purchase · sale · selling` at L35–43, then `0 · 3 · 1 · 2` at probability 1.00 from L44. Transcript 8's resp_tok292 shows `purchase · take · today` up to L43, then `ve · re · ll` from L44. Layers 41–44 still carry topic words at some positions, so ending earlier would lose them.

## 4. Alternative band: 21–44

- **Gain:** a wider band keeps the late slot readouts. These are transcript 10 slot1 `deflection · dodge · non` (L41–45), transcript 7 slot1 `reassuring · Min` (L41–44), transcript 6 slot2 `silence · loyalty` (L41–43), transcript 5 slot1 `investor` (L41–44) and transcript 9 slot2 `protect` (L41–42). It also keeps the topic words at response tokens before the late switch (transcript 8, L41–43).
- **Loss:** at L41–44 the readouts are mostly the actual next token (response `next` 0.49–0.61, answer 0.51–0.64). Slot0 and slot1 are topped by `<end_of_turn>`. Slot4 starts predicting the user's next words (`Detective`, `Amanda` at L41–44). Words found only in these layers more likely reflect what the model is about to write than what it represents.

## 5. Caveats

- **Slot0 is template-dominated at every layer.** From L23 on, its top token is `\n`, which is also the actual next token. Act or topic words (`hiding`, `embedding`, `CEO`) appear only at ranks 2–5. A top-16 check will find them, but slot0 is a weak position.
- **Slot2 is generic in half the transcripts.** In transcripts 1, 3, 5, 8 and 10, slot2 shows the same set (`perplexing · manera · ба · pleasurable · solace`) at L21–41, whatever the conversation. Transcript 8 shows the same set at slot1. Only the other transcripts carry content at slot2.
- **Slots 3 and 4 show generic replies, not act words.** Inside the band they show `ChatGPT · Thank · What · Okay · That` in all ten transcripts. These words look like a predicted user reply rather than content about the conversation or the model's act.
- **Some act words are in other languages.** In the transition (L19–22), act-related words appear in other languages: `거짓` ("lie"), `नहीं` and `לא` ("not"). A fixed English word list would miss them.
- **The template `next` numbers do not help set the end.** They stay at or below 0.29 at all layers, because late slot readouts converge to `<end_of_turn>` rather than to the actual next token. The end therefore rests on the response and answer `next` numbers and on the dumps.
- **Response positions disagree on timing.** Some commit to the next token by L30 (transcripts 1, 3 and 9); others keep topic words until L43–44 (transcripts 4 and 8). No single end layer fits both groups, so L40 is a compromise.
- **The dumps show only the top 5 tokens**, while the statistics use the top 16. Words at ranks 6–16 inside the band are not visible here.
