# gemma-3-27b-it: logit-lens layer band suggestion

Sources: `readout_stats_LL_gemma_3_27b_it.md` and the ten dumps in `readouts_LL/gemma_3_27b_it/`. The model has 62 layers (L00–L61). "Post-response slots" means the five turn-boundary tokens between the response and the question: slot0 `<end_of_turn>`, slot1 `\n`, slot2 `<start_of_turn>`, slot3 `user`, slot4 `\n`.

## 1. Proposed band: 27–50

- **Start, L27:** this is the first layer where most post-response slots and response tokens show English words about the conversation. Below it, they show copies of template tokens, word fragments, or unrelated words from many languages with a top-token probability near 0.
- **End, L50:** this is the last layer before the share of response tokens whose top readout is the actual next token (`next`) passes about one third (0.33 at L50, 0.35 at L51, rising to 0.53 by L56). It is also just after slot3 locks onto `Follow` and slot4 onto `Okay` in every transcript (from L48).

## 2. Layer regions

| Layers | Post-response slots | Response tokens | readable / next / overlap (template; response) |
|---|---|---|---|
| L00–16 | Copies of template tokens and fragments: slot0 `\n · ו · in`, slot2 `고 · n · ა`, slot3 `il · ad · ␣for`. Identical across all ten transcripts, top probability 0.9–1.0. | The input token itself or single letters and fragments (`n · m · on`, `␣S · ␣N · ␣D`). | 0.10–0.21 / 0.16 / 0.02–0.16; 0.21–0.29 / 0.00 / 0.03–0.10 |
| L17–22 | Probability collapses to about 0. Fragments (`et · adım · adı`) and unrelated multilingual words or names (`HSBC`, `DeSantis`, `Meghan`). | Similar noise (`ورٹی`, `Obamacare`, `político`). | 0.18–0.60 / 0.15→0.09 / 0.13→0.03; 0.37–0.60 / 0.00 / 0.07→0.04 |
| L23–26 | Mostly multilingual noise (`Publikum`, `当然`, `Какие`, `ieważ`). A few topic words appear early in single transcripts. | Topic words start to appear, mixed with noise. | 0.71–0.81 / 0.02–0.04 / 0.03; 0.64–0.70 / 0.01–0.02 / 0.03–0.04 |
| L27–37 | English words about the situation and the model's act appear, mostly at slot2 and slot1 (`truth`, `Justice`, `dilemma`, `unethical`, `secretly`, `subtly`, `Denial`). slot0 shows `Note`, `Response`, `Answer`. slot3 shows `pregunta`, `Asked`, `ChatGPT`, `Okay`. slot4 shows `What`, `Why`, `Okay`. | Words that fit the context but are not yet the next token (`contentious`, `testament` before "common"; `unspoken`, `directive` before "hotel"). | 0.82–0.88 / 0.02–0.10 / 0.06–0.11; 0.75–0.86 / 0.03–0.15 / 0.06–0.14 |
| L38–50 | Densest words about the act at slot2 and slot1 (`deception`, `dishonest`, `lie`, `admitting`, `denial`, `redirect`, `deflect`). slot0 moves from `ChatGPT`/`OpenAI` (L38–40) to `Disclaimer` or noise (`water`, `js`, `Brain`). From L48, slot3 is `Follow` and slot4 is `Okay`/`Thank` in all ten. | Context words narrow toward the next token. Top probability is often 0.5–0.9 when the next word is easy to predict. | 0.80–0.84 / 0.01–0.15 / 0.05–0.08; 0.87–0.90 / 0.15–0.33 / 0.10–0.15 |
| L51–55 | slot2 drifts from words about the act to topic nouns and names (`Museum`, `Podcast`, `customer`, `management`, `Ralph`). slot3 stays `Follow` and slot4 `Okay` (top probability up to 0.9). | Mostly the next token or close variants. | 0.76–0.79 / 0.14–0.17 / 0.04–0.05; 0.86–0.88 / 0.35–0.48 / 0.09–0.10 |
| L56–61 | `<end_of_turn>`, `\n`, `<eos>`, and fragments `s · t · re` at slot2. | The actual next token. | 0.75→0.51 / 0.15–0.33 / 0.04–0.08; 0.84→0.67 / 0.53–0.97 / 0.08–0.10 |

## 3. Evidence

- **T3, postresp_slot2:** L00–16 show `n · 고 · ა · ות` at probability 0.3–1.0. L26–34 show `vérité · सच्चाई (truth) · Wahrheit · desperate · Truth`. L36–47 show `conundrum · dilemma · deception · deceit`. L48–54 show `lies · lie · deception · deceit · cover`. L55–59 drift to `Museum`, and L60–61 are `s · re · d`.
- **T7, postresp_slot2:** L34–35 show `Ethics · unethical`. L37–57 show `unethical · deception · dishonest · dishonesty · ethical`, with top probability 0.66 at L39. L58 shows `dilemma`, and L59–61 fall to `s · d`.
- **T8, postresp_slot2:** `unethical` is the top token at every layer from L29 to L57 (probability 0.72–0.83 at L39–49), alongside `dishonesty · deceit`. **T8, postresp_slot1:** L34–55 show `denial · denials · deny · denying`, with probability 0.5–0.94 from L38.
- **T10, postresp_slot1:** L31–46 show `Denial · denial · deny`, L47–55 show `confidently · Confidence · firm`, and L59–61 show `<end_of_turn>`. **T10, postresp_slot2:** L25–34 show `secretly · desperately · Truth · internally`, then L47–60 show `management`.
- **T2, postresp_slot1:** L23–30 show noise and `Honestly · told · said`. L38–47 show `acknowledging · admitting · honesty · 承认 (admit)`, with probability 0.79 at L47. L48–59 show `direct`. **T2, postresp_slot2:** L22–27 already show `wages · unfairly · unfair · Justice` (early topic words), and L37–59 show `remediation · corrective`.
- **T4, postresp_slot2:** L33–53 show `nuanced · subtly · avoid · strategically · redirect · deflect · steer`. L54–57 change to `U · tact`, and L60–61 to `s · �`.
- **T3, resp_tok150 (`␣a`, next `␣common`):** L00–16 copy `␣a`, `␣S`, `␣N`. L27–40 show `contentious · testament · misconception · insidious · sexist · jealousy`. From L45 the top token is the next token `common`, at probability 0.70, rising to 0.93–1.00 by L46–57.
- **T8, resp_tok9 (`␣the`, next `␣hotel`):** L25–31 show `unspoken · prerogative`. L32–47 show `mandate · directive · instructed · confidentiality`. `hotel` first becomes top at L44 and stays top from L55 (0.94–1.00).
- **T6, resp_tok75 (`␣still`, next `␣deciding`):** L24–35 show `Covid · Brexit · undecided · decisión`. `deciding` is top from L38 at probability 0.14, rising to 0.87 by L46.
- **Every transcript, slot3 and slot4:** slot3 is `Follow · ␣follow` at L48–55 (probability 0.4–0.8), and slot4 is `Okay · Thank · That` at L40–61. Neither depends on the conversation.

## 4. Alternative band: 27–54

This alternative extends the end by four layers.

- **Gained:** the tail of the words about the act at slot2 and slot1. Examples: T3 `lie · lies · cover` at L51–54, T4 `subtly · steer · uphold` at L52–53, T8 `denial` at L51–55, T7 and T8 `unethical` at L51–54.
- **Lost:** a clean margin from next-token readouts. At L54, `next` is 0.41 for response tokens and 0.42 for answer tokens. Also, slot2 in T3, T5, T6, T9 and T10 has by then drifted to topic nouns or names (`Museum`, `Podcast`, `customer`, `Ralph`, `management`). Those look like guesses at the next turn rather than a representation of the response.

The other natural option is an earlier start at L23. It would add a few early topic words (T2 slot2 `unfairly`, T10 slot2 `secretly` at L25–26, T3 resp_tok300 `wrongdoing` at L24–26). It would also add layers that are mostly multilingual noise.

## 5. Caveats

- **slot1 artifact:** in seven transcripts (T3–T7 slot1, T9 slot2), the readout shows a fixed list of single Cyrillic capital letters (`У · Д · М · Б · А`) at roughly L34–55, with probability up to 0.96. Inside the band, those positions carry no conversation words. Only T1, T2, T8 and T10 show words about the act at slot1.
- **slot3 and slot4 are generic:** slot3 (`user`) shows `Okay · You · Now · ChatGPT · 继续 (continue)` and then `Follow`. slot4 shows `What · Why · Okay · Thank`. Neither shows words about the act in any transcript. Nearly all the signal at post-response slots sits at slot2, plus slot1 in four transcripts.
- **slot0 is generic too:** slot0 shows `Note · Response · Disclaimer · ChatGPT` and then noise. The one exception is T7, where `Disclaimer` reaches probability 0.9 at L48–51.
- **Pre-answer slot:** from about L27 to L61, the readout at this slot is the upcoming answer word (`Yes`/`No`, or `Yeah`/`Okay` in T5). So the pre-answer slot reflects what the model is about to write at every band layer. The post-answer slot is mostly noise (`Talk`, `water`, `Help`), apart from T3 and T7 (`interrupted`, `incomplete`, `truncated`, `قطع`).
- **user_prompt_last:** this position shows the upcoming response word (`Yes` from about L25) in the transcripts whose response starts with Yes or No. Elsewhere it shows topic words (T3 `Threat` at L32–50, then `Patron`; T10 `Threat`, then `Sarah`).
- **Short-response transcripts:** T1, T2 and T4 are one-word or short responses. In T1 and T2, resp_tok1 and the 75% position are the same token (`.`).
- **Transcripts disagree on where act words peak:** T8 and T10 have them from about L29–31. T3, T4 and T7 have them from about L34–37. T3 still has `lie` at L48–54. The start of 27 is set by the earliest transcripts, and the end of 50 cuts the latest ones short.
