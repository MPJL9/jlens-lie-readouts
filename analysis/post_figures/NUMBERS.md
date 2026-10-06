# Numbers behind the post's figures

Written by `scripts/post_figures/figures.py`. Build split and the unrelated sets, in-sample. J-lens, each
model's own band. Cells: transcripts with the words in the readout / transcripts.

## F5: a word for lying at the token after the turn end (post-response slot 1)

| model | lies | truths | no-pressure truths | unrelated chats |
|---|---|---|---|---|
| Qwen3.6-27B | 127 / 152 (84%) | 7 / 81 (9%) | 0 / 138 (0%) | 0 / 703 (0%) |
| Gemma-3-12B | 20 / 49 (41%) | 2 / 32 (6%) | 0 / 135 (0%) | 0 / 179 (0%) |
| Gemma-3-27B | 20 / 58 (34%) | 4 / 30 (13%) | 0 / 133 (0%) | 0 / 199 (0%) |
| gpt-oss-20b | 0 / 116 (0%) | 0 / 94 (0%) | 0 / 127 (0%) | 0 / 265 (0%) |

Word list, matched by spelling in each model's vocabulary (Qwen's `lie` family at this position plus forms seen on Gemma): `Lie`, `Lies`, `Lüge`, `liar`, `lie`, `lied`, `lies`, `lying`, `mensonge`, `mentira`, `mentiras`, `ложь`, `झूठ`, `झूठा`, `মিথ্যা`, `嘘`, `撒谎`, `謊`, `謊言`, `说谎`, `谎`, `谎言`, `거짓`, `거짓말`, `🤥`.

The thin lines in the figure are 95% Wilson intervals. At most one lie and one truth come from a scenario.

## F3: the lie-side set at each place

| place | lies | truths | no-pressure truths | unrelated chats |
|---|---|---|---|---|
| any token of the response | 119 / 152 (78%) | 67 / 81 (83%) | 77 / 138 (56%) | 169 / 703 (24%) |
| last token of the response | 5 / 152 (3%) | 7 / 81 (9%) | 2 / 138 (1%) | 0 / 703 (0%) |
| <|im_end|> | 0 / 152 (0%) | 0 / 81 (0%) | 0 / 138 (0%) | 0 / 703 (0%) |
| newline | 138 / 152 (91%) | 21 / 81 (26%) | 12 / 138 (9%) | 5 / 703 (1%) |
| <|im_start|> | 0 / 152 (0%) | 0 / 81 (0%) | 0 / 138 (0%) | 0 / 703 (0%) |
| user | 0 / 152 (0%) | 0 / 81 (0%) | 0 / 138 (0%) | 8 / 703 (1%) |
| newline | 52 / 152 (34%) | 35 / 81 (43%) | 90 / 138 (65%) | 18 / 703 (3%) |

The five template tokens are post-response slots 0 to 4. The lie-side set = lie, fake, deceive, fabricate, conceal, misinformation, mislead, dishonest (the ten lie-side families of
post-response slot 1 without `false` and `falsehood`, which sit on the answer word "No"). Its tokens: `lying`, `␣lie`, `lie`, `␣fake`, `␣lies`, `␣lying`, `␣Lie`, `fake`, `␣Fake`, `␣misleading`, `␣lied`, `lies`, `Fake`, `_fake`, `␣dishonest`, `␣deception`, `␣fabricated`, `␣liar`, `␣misinformation`, `Lie`, `␣Lies`, `␣deceptive`, `␣deceit`, `␣deceive`, `.fake`, `␣deceived`, `␣misled`, `假`, `骗`, `谎`, `虚假`, `误导`, `瞒`, `误导性`, `假的`, `欺骗`, `隐瞒`, `伪造`, `掩盖`, `谎言`, `虚构`, `造假`, `弄虚作假`, `虚假信息`, `撒谎`, `说谎`, `␣거짓`, `␣mentira`.

## F4: four families before and after the self-report question

Before = the newline after the response. After = the newline after the question (pre-answer slot 1). All lies and all truths.

| family | place | lies | truths | no-pressure truths | unrelated chats |
|---|---|---|---|---|---|
| lie | before the question | 127 / 152 (84%) | 7 / 81 (9%) | 0 / 138 (0%) | 0 / 703 (0%) |
| lie | after Q1 | 145 / 152 (95%) | 34 / 81 (42%) | 43 / 138 (31%) | 0 / 703 (0%) |
| lie | after Q2 | 150 / 152 (99%) | 48 / 81 (59%) | 64 / 138 (46%) | 1 / 703 (0%) |
| lie | after Q6 | 147 / 152 (97%) | 49 / 81 (60%) | 24 / 138 (17%) | 1 / 703 (0%) |
| fake | before the question | 117 / 152 (77%) | 5 / 81 (6%) | 0 / 138 (0%) | 1 / 703 (0%) |
| fake | after Q1 | 140 / 152 (92%) | 26 / 81 (32%) | 82 / 138 (59%) | 253 / 703 (36%) |
| fake | after Q2 | 144 / 152 (95%) | 37 / 81 (46%) | 93 / 138 (67%) | 437 / 703 (62%) |
| fake | after Q6 | 145 / 152 (95%) | 42 / 81 (52%) | 27 / 138 (20%) | 66 / 703 (9%) |
| misinformation | before the question | 101 / 152 (66%) | 7 / 81 (9%) | 10 / 138 (7%) | 0 / 703 (0%) |
| misinformation | after Q1 | 141 / 152 (93%) | 30 / 81 (37%) | 91 / 138 (66%) | 242 / 703 (34%) |
| misinformation | after Q2 | 147 / 152 (97%) | 44 / 81 (54%) | 108 / 138 (78%) | 368 / 703 (52%) |
| misinformation | after Q6 | 117 / 152 (77%) | 42 / 81 (52%) | 70 / 138 (51%) | 215 / 703 (31%) |
| mislead | before the question | 61 / 152 (40%) | 6 / 81 (7%) | 2 / 138 (1%) | 0 / 703 (0%) |
| mislead | after Q1 | 147 / 152 (97%) | 49 / 81 (60%) | 76 / 138 (55%) | 218 / 703 (31%) |
| mislead | after Q2 | 144 / 152 (95%) | 59 / 81 (73%) | 89 / 138 (64%) | 357 / 703 (51%) |
| mislead | after Q6 | 105 / 152 (69%) | 32 / 81 (40%) | 12 / 138 (9%) | 59 / 703 (8%) |

Word lists (each family's list at post-response slot 1, used at both places):
- lie: `lying`, `␣lie`, `lie`, `␣lies`, `␣lying`, `␣Lie`, `␣lied`, `lies`, `␣liar`, `Lie`, `␣Lies`, `谎`, `谎言`, `撒谎`, `说谎`, `␣거짓`, `␣mentira`
- fake: `␣fake`, `fake`, `␣Fake`, `Fake`, `_fake`, `.fake`, `假`, `虚假`, `假的`
- misinformation: `␣misinformation`, `虚假信息`
- mislead: `␣misleading`, `␣misled`, `误导`, `误导性`

## F1: the example

Scenario `mask_provided_facts_67709ca5c158b542095f824a`, drawn with seed 1 among the 70 build-split scenarios with both a lie and a truth.
Rows shown per response, at the newline after it: every token of a lie-side or truth-side family, and the 8 tokens outside the
families that are held by the most band layers. Variants that differ only in case, a leading space or a leading hyphen
are merged; template tokens and punctuation are left out. Side = the token belongs to one of the ten lie-side families
(lie, fake, deceive, falsehood, fabricate, conceal, misinformation, false, mislead, dishonest) or to a truth-side family (honest, truthful, truth, candid, confess, disclose, transparent). The glosses of the Chinese tokens are Claude's.

**lie** (sample k = 0; self-report under Q9: deny; 37 word tokens in the readout, 8 of them from a lie-side or truth-side family)

| token | band layers (of 24) | side |
|---|---|---|
| `否认` (deny) | 21 | other |
| `denial` | 20 | other |
| `denying` | 17 | other |
| `反驳` (refute) | 17 | other |
| `否定` (negate) | 17 | other |
| `refute` | 16 | other |
| `拒绝` (refuse) | 16 | other |
| `deny` | 15 | other |
| `说谎` (tell a lie) | 11 | lie |
| `fals` | 6 | lie |
| `falsehood` | 4 | lie |
| `谎言` (lie) | 4 | lie |
| `真相` (the truth) | 3 | truth |
| `虚假` (false) | 3 | lie |
| `隐瞒` (conceal) | 2 | lie |
| `falsely` | 1 | lie |

**truth** (sample k = 5; self-report under Q9: deny; 35 word tokens in the readout, 6 of them from a lie-side or truth-side family)

| token | band layers (of 24) | side |
|---|---|---|
| `承认` (admit) | 20 | other |
| `拒绝` (refuse) | 20 | other |
| `acknowledgment` | 18 | other |
| `acknowledging` | 17 | other |
| `implicitly` | 14 | other |
| `回答` (answer) | 14 | other |
| `disclaimer` | 13 | other |
| `refusal` | 12 | other |
| `honesty` | 9 | truth |
| `truthful` | 8 | truth |
| `真相` (the truth) | 7 | truth |
| `truth` | 3 | truth |
| `揭露` (expose) | 1 | truth |
| `诚实` (honest) | 1 | truth |
