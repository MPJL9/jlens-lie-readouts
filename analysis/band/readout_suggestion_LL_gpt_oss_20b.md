# gpt-oss-20b: suggested logit-lens layer band (PLAN.md Section 4.4)

Based on `readout_stats_LL_gpt_oss_20b.md` and the ten dumps in `readouts_LL/gpt_oss_20b/`.
gpt-oss-20b has 24 layers (L00–L23). Post-response slots here are the four turn-boundary tokens
`<|end|>` (slot0), `<|start|>` (slot1), `user` (slot2) and `<|message|>` (slot3).

## 1. Proposed band: 8–14

- **Start at 8.** From layer 8 on, response tokens read out topic words (for example "alleged",
  "overnight", "suspects", "urgent") and the post-response slots read out words about the chat
  itself ("Chat", "GPT", "conveys", "asked"). Before layer 7 every position shows the same
  unrelated fragments ("fur", "Kiel", "brevet", "bern", "uhu", "vent").
- **End at 14.** At layer 15 the template positions collapse into punctuation and
  `<|endoftext|>`, with `readable` falling from 0.55 to 0.29. From layer 17 the response
  readouts are mostly the actual next token, often at probability 0.9 or higher.

## 2. Layer regions

| layers | post-response slots | response tokens | readable (tmpl / resp) | next (resp / ans) | overlap (tmpl / resp) |
|---|---|---|---|---|---|
| 0–6 | Fixed unrelated fragments, the same in every transcript: slot0 "he, ministries, fur, brevet, Kiel"; slot1 "fur, cab, kn"; slot2 "vent, constr, Bor, 脱"; slot3 "bern, uhu, Pier, sanity" | Unrelated words and fragments ("rod", "pasti", "glimps", "vet", "cad") | 0.71–0.81 / 0.79–0.81 | 0.00 / 0.00–0.01 | 0.01–0.06 / 0.01–0.06 |
| 7–14 | Words about the chat and its turn-taking: "Chat", "GPT", "conveys/conveying", "response", "asked", "wanting", "reply", "posted", "again", "further". At the pre-answer `assistant` slot: "responses", "reply", "answer", "回答" | Topic words from the conversation ("alleged", "overnight", "harmless", "scheduling", "safety", "integrity", "urgently", "subtle, timing, cues, psychological") | 0.55–0.79 / 0.68–0.80 | 0.00–0.05 / 0.00–0.05 | 0.06–0.09 / 0.06–0.15 |
| 15–20 | Punctuation and control tokens: ".", ":", "\n\n", `<|endoftext|>`, `<|reserved_200016|>`. Slot2 adds "asks", "says" at L17–19. Slot3 shows "A", "I", "." and then the question's possible first words ("Thanks", "What", "Why") from L19–20 | Moving to the next token: function words and punctuation, with top probability often 0.9–1.0 from L17 on | 0.07–0.29 / 0.53–0.59 | 0.10–0.54 / 0.11–0.65 | 0.14–0.34 / 0.07–0.17 |
| 21–23 | The actual next template token at probability ≈1.0: `<|start|>`, "assistant", `<|message|>`/`<|channel|>` | The actual next token | 0.20–0.39 / 0.60–0.63 | 0.67–0.89 / 0.81–0.97 | 0.08–0.14 / 0.07 |

The `readable` share does not separate regions 0–6 and 7–14. The fragments "fur", "Kiel" and
"brevet" count as words of three or more letters, so the share stays high in both. The dumps
draw the start boundary. The stats draw the end boundary: template `readable` collapses at
L15, template `overlap` peaks at L16–18, and response `next` climbs from 0.05 at L14 to 0.26 at L17.

## 3. Evidence

- **T01, resp_tok17 ("taking"), L07–L13:** "alleged", "ever", "overnight", "possession",
  "allegedly", "supposedly". At L17 the readout is "any" at 0.96, and it stays the next-token
  set ("any", "anything") at 0.99–1.00 through L22.
- **T09, resp_tok102 ("and"), L10–L14:** "subtle, timing, cues, psychological, tactics,
  avoidance". By L17 the top token is "the" at 0.92.
- **T05, user_prompt_last, L08–L15:** "urgent, urgency, urgently, Urg, quickly" (top
  probability 0.24–0.78). At L16–L20 this falls to "\n", spaces and `<|endoftext|>`.
- **T09, user_prompt_last, L13–L14:** "illegal, legality, outlaw, prohibited, violating". This
  is the conversation's topic (card counting) at the last user token. At L15 the readout becomes "?, …".
- **T01, postresp_slot2 (`user`), L09–L14:** "asked, wanting, reply, posted, requested". At
  L15–L17 it is ":" and "." (":" at 0.96 at L17). At L21–L23 it is `<|message|>`/`<|channel|>`, the next token.
- **T02, postresp_slot0 (`<|end|>`), L08–L12:** "conveys, conveying, response, Chat, please".
  At L16 it is `<|endoftext|>` at 0.73. At L21–L23 it is `<|start|>`, the actual next token, at 0.86–1.00.
- **All ten, postresp_slot1 (`<|start|>`), L09–L12:** "ieb, kn, GPT, tur, clar" in nearly
  identical order. At L19–L20 it is "assistant", and at L21–L23 "assistant, comment, analysis"
  at 1.00. This slot carries the chat format and nothing specific to the conversation.
- **All ten, preans_slot2 (`assistant`), L10–L14:** "responses, reply, answer, 回答,
  formulated". At L21 every transcript gives `<|channel|>` at 1.00.
- **T08, resp_tok1 (final "."), L12–L14:** "intentionally", "detected", "unavoidable",
  "albeit". These are among the few act-related words in any dump, and they sit inside the
  band. At L16 the readout is `<|endoftext|>`, and from L21 it is `<|return|>` at 0.88–1.00.
- **T03, user_prompt_last, L13–L14:** "strength, honesty, requested, insisting, honest". The
  user had asked for "an honest answer". At L15–L17 the readout is "…", spaces and "\n".

## 4. Alternative band: 10–14

Dropping layers 8–9 removes the layers where the post-response slots still mix chat words
with leftover fragments ("Kiel", "Pier", "rede", "pinned", "vela"). Every layer in 10–14
shows conversation or chat-role words at most positions, so a hit in the narrow band is
easier to trust. The cost is the early topic words at response tokens. Examples are "ever"
and "alleged" in T01 at L08–L09, "ordinary, normally, suspects" in T09 at L08–L09, and
"urgent/urgency" in T05 at L08–L09. A five-layer band also gives fewer chances to catch a
word that shows up in only one layer.

I did not prefer a wider band such as 8–16 because layers 15–16 add almost only punctuation
and `<|endoftext|>` at the post-response slots. At L16, slot0 already reaches
`<|endoftext|>` at 0.73–0.99 in every transcript.

## 5. Caveats

- **No act words at the post-response slots.** At no layer do these slots read out words
  about deceiving or honesty. In layers 7–14 they show words about the chat format ("Chat",
  "conveys", "asked", "reply", "responses"), not about what the model did. The band is chosen
  so that such words could appear, but these ten dumps do not show them there.
- **The slots are template-driven.** Slot0 and slot1 readouts are nearly the same in all
  ten transcripts at every layer. Little of the conversation reaches them. Slot3
  (`<|message|>`) shows fragments in 7–14 ("wanting", "further", "give", "-e", "ery"), then
  the question's possible first words from about L19 ("Thanks", "What", "Why", "Ok"). Those
  late words anticipate the next token rather than carry content.
- **Short responses repeat positions.** In T06, T07, T08 and T10 the response is one or two
  tokens ("No", "No.", "Yes."). The 25/50/75% response positions are the same token shown two
  or three times, so these transcripts add little response-token evidence. For these short
  responses the "No"/"Yes" readouts at L09–L14 are spaces, "!", "regards", "sorry", "yes".
- **The start is a judgement call.** Topic words appear at L07 in some places (T01 "alleged",
  T02 resp_tok110 "ready, comfortable", T05 resp_tok51 "traffic") and only at L10–L13 in
  others (T03 resp_tok51 "safety" at L12–L13). Layer 8 is a midpoint, not a sharp edge.
- **`next` is not zero inside the band at every position.** A few response positions lock
  onto the next token early: T02 resp_tok73 already has "only" at 0.55 at L14, and T05
  resp_tok77 has "unless" at 0.73 at L14. Averaged over positions, response `next` is still
  only 0.05 at L14.
