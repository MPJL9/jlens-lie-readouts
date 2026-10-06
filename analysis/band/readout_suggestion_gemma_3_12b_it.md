# gemma-3-12b-it: readout-based band suggestion (PLAN.md Section 4.2)

Written from `readout_stats_gemma_3_12b_it.md` and the ten dumps in `readouts/gemma_3_12b_it/`. No `cka_*` file and nothing under `data/` was read. The model has 48 layers (L00–L47).

## 1. Proposed band: 21–43

- **Start at L21.** L21 is the first layer where both the response tokens and the post-response slots switch from punctuation, quote marks and markup to words about the conversation. The `readable` share jumps from 0.32 to 0.59 at response positions and from 0.40 to 0.59 at template positions.
- **End at L43.** L43 is the last layer before the actual next token becomes the majority top token. Response `next` is 0.49 at L43 and 0.57 at L44; answer `next` is 0.52 at L43 and 0.59 at L44. At L44 several post-response slots also collapse to whitespace, brackets or `<end_of_turn>`.

## 2. Layer regions

| Layers | Post-response slots | Response tokens | readable (tmpl / resp) | next (resp / ans) | overlap (tmpl / resp) |
|---|---|---|---|---|---|
| L00–L10 | Fixed junk shared by all transcripts. Slot 0 shows `<end_of_turn>` plus emoji and cuneiform signs. Slot 1 and slot 4 show sub-word fragments (`്‍`, `avour`, `<sup>`, `<i>`). Slot 2 shows `~~`, `––`, `($\`. Slot 3 shows `"—`, `</h3>`. | Single letters (`s`, `e`, `o`), HTML tags, dashes | 0.09–0.24 / 0.05–0.12 | 0.00 / 0.00 | ≤0.01 / 0.02–0.04 |
| L11–L20 | Mostly punctuation (`?"`, `!`, `,`, `**.`). The first generic words appear at slot 3 from L16 (`TikTok`, `chatbot`, `ChatGPT`) and at slot 4 from L18 (`asking`, `Honestly`). | Punctuation and quote marks (`..."`, `.".`, `!".`) | 0.08–0.40 / 0.12–0.32 | ≤0.01 | 0.01–0.05 / 0.04–0.09 |
| L21–L29 | Words about the situation and the model's act appear at slots 1, 2 and 4 (`obfusc`, `confidentiality`, `misleading`, `questioning`, `skepticism`). Slot 3 shows `bertanya`/`meminta` (Indonesian "ask"/"request") and `replying`. In 5 of 10 transcripts slot 2 collapses to low-probability glyphs from L22. | Topic words tied to the passage, often synonyms of what is coming (`unforeseen`, `repentance`, `timeframe`) | 0.59–0.78 / 0.59–0.85 | 0.01–0.15 / 0.02–0.15 | 0.05–0.09 / 0.10–0.16 |
| L30–L43 | Slot 1 and slot 2 keep act or topic words in several transcripts (`reassurance`, `denial`, `evasion`, `discouraging`, `Silence`, `Protect`). Slot 3 turns to `ChatGPT`/`OpenAI`, then `Thank`/`You`/`updated`. Slot 4 turns to `Thank`/`Okay`/`Alright`. The last pre-answer slot shows the answer word (`Yes`/`No`/`You`). | The next token or close synonyms, with top probability often 0.95–1.00 | 0.76–0.86 / 0.83–0.88 | 0.17–0.49 / 0.17–0.52 | 0.03–0.06 / 0.08–0.12 |
| L44–L47 | Whitespace, `[`, `(`, `<end_of_turn>`, `\n`, sentence starters (`Okay`, `That`) | The actual next token (digits, `re`, `.`) | 0.55–0.78 / 0.73–0.84 | 0.57–0.84 / 0.59–0.98 | 0.04–0.06 / 0.07–0.08 |

## 3. Evidence

- **T1, resp_tok21 (`-` before `compliance`).** L20 reads `!". .". !”.`. L21 reads `assurances · confidentiality · understanding · compliance`. The switch from punctuation to topic words happens in one layer.
- **T2 resp_tok30, T3 resp_tok387, T5 resp_tok429.** All three show the same L20→L21 step. The readouts go from `..."` to `requests · availability · bookings` (T2), `students · teaching · expertise` (T3) and `rehabilitation` (T5).
- **T6, postresp_slot1 (`\n`).** L19 reads `<eos> · 🤫`. L20–L22 read `謊 · 谎 · মিথ্যা` (the word "lie" in Chinese and Bengali), then `obfusc · concealment`. L23 reads `obfusc · confidentialité · pretending` at probability 1.00. These are act words, and they sit at the very start of the band.
- **T7, postresp_slot1.** L23–L25 read `obfusc · misleading · contradicting`. L32–L43 read `reassuring · reassurance · misleading · vague · minimization`. The act words persist through the whole band and fade at L45–L47 (`<end_of_turn>`, `</body>`).
- **T10, postresp_slot1.** L29–L35 read `denials · denial · denying`. L36–L43 read `evas · dodging · evasion · deflection`. At L44 the readout is `dodge · dod`, and at L46–L47 it is `<end_of_turn>`. The act words run to L43, which supports ending there rather than earlier.
- **T2, postresp_slot2 (`<start_of_turn>`).** L24–L43 read `discouraging · denying · unwillingness · unavailability`, with probability 0.90–1.00 from L31 to L40. At L44 the readout drops to `( · discouraging` at 0.28. At L46 it becomes `<end_of_turn>`.
- **T6 and T9, postresp_slot2.** T6 shows `Silence · silencio · Compliance` at L34–L43 and `loyalty` at L40–L44; at L45 it becomes `<end_of_turn> · .`. T9 shows `Avoiding` at L28–L37 and `Protect · protecting · safeguarding` at L33–L43; at L44 it becomes `<eos> · ( · ##`.
- **T8, resp_tok195 (`2` before `0`).** L35–L43 read `purchasing · buying · selling · sale`. At L44 the top token is `0`, the actual next token, at probability 1.00. The same happens at resp_tok97: `Hyundai · recall · fail` at L27–L40, then digits from L41–L44. The switch to the next token lands right at the proposed end.
- **T4, resp_tok26 (`alignment`).** The readout is `of`, the actual next token, from L29 onward at probability 0.99–1.00. So some response positions become next-token readouts long before L43. The `next` curve rises gradually rather than jumping at one layer.
- **T3 and T4, user_prompt_last.** L27–L33 are mostly newline tokens (`\n\n\n`). Topic or answer words then appear from L34 (`Nope`, `Honestly`, `No`). Not every template position has topic words across the whole band.

## 4. Alternative band: 23–38

- **Gained.** `readable` is at least 0.73 (template) and 0.83 (response) in every layer. Response `next` stays at or below 0.36 and answer `next` at or below 0.39. This band drops the two transition layers L21–L22. In 5 of 10 transcripts slot 2 falls to near-zero-probability tokens at L22 (`$ · . · even`, probability 0.03–0.07). The band also stops before the answer word fills the last pre-answer slot at high probability (L39–L43 in T5, T7 and T9).
- **Lost.** The early act words at L20–L22 are gone: T6 slot 1 (`謊`, `obfusc`), T7 slot 2 (`secrecy`, `obfusc`) and T2 slot 2 (`sneaky`). The late act words at L39–L43 are also gone: T10 slot 1 (`evasion`, `deflection`), T2 slot 2 (`discouraging`), T6 slot 2 (`Silence`) and T9 slot 2 (`Protect`). The wider band catches more act-word occurrences. It pays for that with more next-token contamination near its end.

## 5. Caveats

- **Slot 0 (`<end_of_turn>`) copies itself.** The top token is `<end_of_turn>` at probability about 1.00 at every layer in all ten transcripts. Only the lower-ranked tokens change: `hiding`/`隐藏` (T1, T7), `Embedding` (T5, T9, T10), HTML closers. This slot will rarely show an act word as its top token.
- **Slot 2 (`<start_of_turn>`) splits into two groups.** In T1, T3, T5, T8 and T10 it holds low-probability glyph junk (`ስቃሴ`, `╿`, `جذاب`, `Ошибка`) from L22 to about L43. In T2, T4, T6, T7 and T9 it holds clear topic or act words over the same layers. The band choice does not fix this. The position simply carries nothing readable in half the transcripts.
- **Slot 3 (`user`) is generic.** In all ten transcripts it reads `chatbot`/`bertanya` (L19–L29), then `ChatGPT`/`OpenAI` (L30–L37), then `Thank`/`You`/`updated`. It looks like a fixed template response, not a readout of this conversation.
- **Slot 4 and the last pre-answer slot drift toward the next turn.** From about L32, slot 4 shows how a reply would open (`Thank`, `Okay`, `Alright`). From L41 it shows the addressee's name (`Detective` in T4, `Amanda` in T10). The last pre-answer slot shows the answer word itself from about L34. Both positions behave more like next-token readouts than the post-response slots do, even well inside the band.
- **The start is soft.** At slot 2, situation words already appear at L18–L20 (`paranoia`, `backstory`, `sneaky`, `lawyers`), and T6 slot 1 shows `謊` at L20. Response tokens, however, are still punctuation at L20 in every dump. A start at L20 is defensible if the template positions are weighted more heavily.
- **Some response positions never carry topic words.** Examples are T5 resp_tok286 (dashes and periods at all layers), T6 resp_tok0 and resp_tok1 (a one-word reply), and T1 resp_tok14 (a bare space before a digit, with unrelated words such as `Agriculture`). These positions pull the response `readable` averages down but do not change the layer where the switch happens.
