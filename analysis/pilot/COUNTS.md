# Experiment 2 pilot, step 1: word lists at the response tokens (Qwen3.6-27B, J-lens, band 35-58)

Written by `scripts/pilot/response_counts.py`. Build split plus the unrelated sets (158 + 545 extra chats,
commentary dropped), in-sample. *present at a token* = one of the list's tokens is in the top 16 at one or
more band layers at that response token. Lists are in `analysis/pilot/lists.json`; the slot-1 families use
the draft lists of that position.

**The lie-side set** = the ten lie-side families without `false` and `falsehood`: lie, fake, deceive, fabricate, conceal, misinformation, mislead, dishonest. Changed by the user on
2026-10-03: `false` and `falsehood` appear at the model's answer word "No", so they follow the answer. Their own rows are kept.

Transcripts: lies 152, truths 81, no-pressure truths 138, unrelated 703. Response tokens: lies 27211, truths 15421, no-pressure truths 14537, unrelated 118699.

## A. Share of transcripts with the list present

Three places: at one or more response tokens; at the last response token; at the newline after the response
(post-response slot 1, from the presence index, for reference). Cells: lies / truths / no-pressure truths / unrelated.

| list | tokens in the list | at any response token | at the last response token | at the newline |
|---|---|---|---|---|
| lie | 17 | 50/152 (33%) / 38/81 (47%) / 13/138 (9%) / 37/703 (5%) | 1/152 (1%) / 1/81 (1%) / 0/138 (0%) / 0/703 (0%) | 127/152 (84%) / 7/81 (9%) / 0/138 (0%) / 0/703 (0%) |
| fake | 9 | 79/152 (52%) / 47/81 (58%) / 30/138 (22%) / 69/703 (10%) | 1/152 (1%) / 1/81 (1%) / 0/138 (0%) / 0/703 (0%) | 117/152 (77%) / 5/81 (6%) / 0/138 (0%) / 1/703 (0%) |
| deceive | 7 | 46/152 (30%) / 43/81 (53%) / 17/138 (12%) / 18/703 (3%) | 1/152 (1%) / 2/81 (2%) / 0/138 (0%) / 0/703 (0%) | 94/152 (62%) / 5/81 (6%) / 0/138 (0%) / 0/703 (0%) |
| falsehood | 1 | 61/152 (40%) / 44/81 (54%) / 37/138 (27%) / 16/703 (2%) | 0/152 (0%) / 0/81 (0%) / 0/138 (0%) / 0/703 (0%) | 89/152 (59%) / 0/81 (0%) / 2/138 (1%) / 0/703 (0%) |
| fabricate | 5 | 41/152 (27%) / 35/81 (43%) / 29/138 (21%) / 55/703 (8%) | 0/152 (0%) / 2/81 (2%) / 0/138 (0%) / 0/703 (0%) | 83/152 (55%) / 1/81 (1%) / 1/138 (1%) / 5/703 (1%) |
| conceal | 3 | 78/152 (51%) / 52/81 (64%) / 12/138 (9%) / 9/703 (1%) | 1/152 (1%) / 5/81 (6%) / 0/138 (0%) / 0/703 (0%) | 109/152 (72%) / 17/81 (21%) / 2/138 (1%) / 0/703 (0%) |
| misinformation | 2 | 101/152 (66%) / 55/81 (68%) / 70/138 (51%) / 49/703 (7%) | 4/152 (3%) / 1/81 (1%) / 2/138 (1%) / 0/703 (0%) | 101/152 (66%) / 7/81 (9%) / 10/138 (7%) / 0/703 (0%) |
| false | 12 | 86/152 (57%) / 55/81 (68%) / 41/138 (30%) / 47/703 (7%) | 3/152 (2%) / 2/81 (2%) / 0/138 (0%) / 0/703 (0%) | 79/152 (52%) / 2/81 (2%) / 1/138 (1%) / 0/703 (0%) |
| mislead | 4 | 82/152 (54%) / 56/81 (69%) / 31/138 (22%) / 31/703 (4%) | 0/152 (0%) / 0/81 (0%) / 1/138 (1%) / 0/703 (0%) | 61/152 (40%) / 6/81 (7%) / 2/138 (1%) / 0/703 (0%) |
| dishonest | 1 | 36/152 (24%) / 42/81 (52%) / 18/138 (13%) / 13/703 (2%) | 0/152 (0%) / 2/81 (2%) / 0/138 (0%) / 0/703 (0%) | 35/152 (23%) / 4/81 (5%) / 0/138 (0%) / 0/703 (0%) |
| evade | 8 | 20/152 (13%) / 25/81 (31%) / 17/138 (12%) / 43/703 (6%) | 0/152 (0%) / 0/81 (0%) / 0/138 (0%) / 0/703 (0%) | 18/152 (12%) / 6/81 (7%) / 0/138 (0%) / 0/703 (0%) |
| vague | 7 | 17/152 (11%) / 5/81 (6%) / 9/138 (7%) / 109/703 (16%) | 0/152 (0%) / 0/81 (0%) / 0/138 (0%) / 0/703 (0%) | 13/152 (9%) / 4/81 (5%) / 0/138 (0%) / 1/703 (0%) |
| honest | 10 | 111/152 (73%) / 70/81 (86%) / 44/138 (32%) / 66/703 (9%) | 3/152 (2%) / 14/81 (17%) / 7/138 (5%) / 0/703 (0%) | 9/152 (6%) / 43/81 (53%) / 40/138 (29%) / 1/703 (0%) |
| candid | 1 | 66/152 (43%) / 60/81 (74%) / 29/138 (21%) / 13/703 (2%) | 0/152 (0%) / 3/81 (4%) / 1/138 (1%) / 0/703 (0%) | 1/152 (1%) / 34/81 (42%) / 19/138 (14%) / 0/703 (0%) |
| disclose | 14 | 64/152 (42%) / 56/81 (69%) / 46/138 (33%) / 58/703 (8%) | 0/152 (0%) / 3/81 (4%) / 2/138 (1%) / 0/703 (0%) | 1/152 (1%) / 26/81 (32%) / 20/138 (14%) / 0/703 (0%) |
| confess | 4 | 24/152 (16%) / 46/81 (57%) / 19/138 (14%) / 6/703 (1%) | 0/152 (0%) / 4/81 (5%) / 1/138 (1%) / 0/703 (0%) | 0/152 (0%) / 24/81 (30%) / 5/138 (4%) / 0/703 (0%) |
| refuse | 13 | 34/152 (22%) / 50/81 (62%) / 21/138 (15%) / 70/703 (10%) | 3/152 (2%) / 1/81 (1%) / 0/138 (0%) / 0/703 (0%) | 26/152 (17%) / 44/81 (54%) / 9/138 (7%) / 2/703 (0%) |
| knowingly | 5 | 90/152 (59%) / 53/81 (65%) / 54/138 (39%) / 123/703 (17%) | 1/152 (1%) / 0/81 (0%) / 2/138 (1%) / 0/703 (0%) | 1/152 (1%) / 1/81 (1%) / 0/138 (0%) / 0/703 (0%) |
| cannot | 11 | 85/152 (56%) / 65/81 (80%) / 81/138 (59%) / 155/703 (22%) | 0/152 (0%) / 0/81 (0%) / 1/138 (1%) / 1/703 (0%) | 0/152 (0%) / 0/81 (0%) / 0/138 (0%) / 0/703 (0%) |
| deny | 10 | 50/152 (33%) / 27/81 (33%) / 30/138 (22%) / 20/703 (3%) | 3/152 (2%) / 0/81 (0%) / 0/138 (0%) / 0/703 (0%) | 72/152 (47%) / 12/81 (15%) / 10/138 (7%) / 0/703 (0%) |
| situation | 48 | 122/152 (80%) / 73/81 (90%) / 88/138 (64%) / 344/703 (49%) | 3/152 (2%) / 4/81 (5%) / 3/138 (2%) / 1/703 (0%) | 13/152 (9%) / 41/81 (51%) / 52/138 (38%) / 14/703 (2%) |
| any of the lie-side set (the ten without false, falsehood) | – | 119/152 (78%) / 67/81 (83%) / 77/138 (56%) / 169/703 (24%) | 5/152 (3%) / 7/81 (9%) / 2/138 (1%) / 0/703 (0%) | 138/152 (91%) / 21/81 (26%) / 12/138 (9%) / 5/703 (1%) |
| any of the pressure set (conceal, deceive, dishonest, lie, mislead) | – | 107/152 (70%) / 65/81 (80%) / 41/138 (30%) / 84/703 (12%) | 1/152 (1%) / 6/81 (7%) / 1/138 (1%) / 0/703 (0%) | 134/152 (88%) / 19/81 (23%) / 4/138 (3%) / 0/703 (0%) |
| any truth-side (honest, candid, disclose, confess) | – | 119/152 (78%) / 73/81 (90%) / 67/138 (49%) / 110/703 (16%) | 3/152 (2%) / 15/81 (19%) / 9/138 (7%) / 0/703 (0%) | 10/152 (7%) / 44/81 (54%) / 46/138 (33%) / 1/703 (0%) |

## B. Share of response tokens carrying the list (all tokens of the class pooled)

| list | lies | truths | no-pressure truths | unrelated |
|---|---|---|---|---|
| lie | 0.3% | 2.6% | 0.2% | 0.1% |
| fake | 1.1% | 4.0% | 1.5% | 0.3% |
| deceive | 0.3% | 4.0% | 0.9% | 0.1% |
| falsehood | 1.4% | 2.9% | 1.5% | 0.1% |
| fabricate | 0.6% | 3.3% | 1.8% | 0.2% |
| conceal | 0.5% | 4.0% | 0.3% | 0.0% |
| misinformation | 5.0% | 7.6% | 4.7% | 0.3% |
| false | 2.4% | 4.2% | 2.3% | 0.2% |
| mislead | 2.3% | 4.9% | 2.3% | 0.2% |
| dishonest | 0.3% | 4.1% | 0.9% | 0.0% |
| evade | 0.2% | 0.4% | 0.3% | 0.1% |
| vague | 0.2% | 0.1% | 0.2% | 0.5% |
| honest | 4.3% | 10.7% | 2.4% | 0.5% |
| candid | 1.2% | 4.0% | 1.1% | 0.1% |
| disclose | 1.0% | 4.2% | 2.1% | 0.3% |
| confess | 0.3% | 1.2% | 0.4% | 0.0% |
| refuse | 0.2% | 1.4% | 0.4% | 0.2% |
| knowingly | 1.5% | 2.1% | 1.2% | 0.4% |
| cannot | 1.2% | 2.5% | 3.1% | 0.6% |
| deny | 0.4% | 0.6% | 0.6% | 0.1% |
| situation | 6.4% | 12.7% | 8.2% | 2.9% |
| any of the lie-side set (the ten without false, falsehood) | 6.1% | 11.0% | 6.7% | 1.0% |
| any of the pressure set (conceal, deceive, dishonest, lie, mislead) | 3.0% | 7.8% | 3.0% | 0.4% |
| any truth-side (honest, candid, disclose, confess) | 5.1% | 12.9% | 4.3% | 0.8% |

## C. Lies: where the lie-side words sit relative to the judge's quoted lie

151 of 152 lies have a quote that was located in the response tokens (1 quotes not located, 0 lies without a quote). Share of tokens carrying any of the lie-side set, by place:

| place | tokens | carrying any of the lie-side set | carrying `lie` | carrying any truth-side |
|---|---|---|---|---|
| before the quote | 7073 | 569/7073 (8%) | 22/7073 (0%) | 661/7073 (9%) |
| inside the quote | 2055 | 184/2055 (9%) | 11/2055 (1%) | 73/2055 (4%) |
| after the quote | 17743 | 866/17743 (5%) | 43/17743 (0%) | 633/17743 (4%) |
| (truths, all tokens) | 15421 | 1704/15421 (11%) | 406/15421 (3%) | 1991/15421 (13%) |

By distance in tokens from the quote (negative = before its start, positive = after its end):

| distance | tokens | carrying any of the lie-side set | carrying `lie` |
|---|---|---|---|
| -1000000 to -51 | 2477 | 219/2477 (9%) | 7/2477 (0%) |
| -50 to -21 | 2429 | 157/2429 (6%) | 10/2429 (0%) |
| -20 to -6 | 1597 | 129/1597 (8%) | 5/1597 (0%) |
| -5 to -1 | 570 | 64/570 (11%) | 0/570 (0%) |
| inside the quote | 2055 | 184/2055 (9%) | 11/2055 (1%) |
| +1 to +5 | 691 | 60/691 (9%) | 1/691 (0%) |
| +6 to +20 | 2054 | 133/2054 (6%) | 3/2054 (0%) |
| +21 to +50 | 3631 | 168/3631 (5%) | 8/3631 (0%) |
| +51 and beyond | 11367 | 505/11367 (4%) | 31/11367 (0%) |

The first response token carrying `lie`, among the 151 lies with a located quote: before the quote in 18, inside it in 9, after it in 22, never in 102.

Of the 61 lies with any of the lie-side set inside the quote, 15 also carry one at one of the last three response tokens.

## D. By token type: share of tokens carrying any of the lie-side set

| token type | lies | truths | no-pressure truths | unrelated |
|---|---|---|---|---|
| word | 1374/23674 (6%) | 1436/13021 (11%) | 785/11926 (7%) | 847/78635 (1%) |
| number | 26/232 (11%) | 19/289 (7%) | 21/245 (9%) | 51/5000 (1%) |
| punctuation | 245/2780 (9%) | 218/1709 (13%) | 138/1928 (7%) | 267/26575 (1%) |
| line break | 21/459 (5%) | 17/306 (6%) | 14/347 (4%) | 21/5442 (0%) |
| space | 4/66 (6%) | 14/96 (15%) | 10/91 (11%) | 28/3047 (1%) |

## E. The lies the newline misses, against the caught lies

*caught* = one of the eight families at the newline after the response; *missed* = none.

| | missed lies | caught lies |
|---|---|---|
| any of the lie-side set at one or more response tokens | 14/19 (74%) | 105/133 (79%) |
| any of the pressure set at one or more response tokens | 14/19 (74%) | 93/133 (70%) |
| `lie` at one or more response tokens | 5/19 (26%) | 45/133 (34%) |
| any of the lie-side set at one of the last three response tokens | 1/19 (5%) | 17/133 (13%) |
| any truth-side at one or more response tokens | 14/19 (74%) | 105/133 (79%) |
| `refuse` at one or more response tokens | 6/19 (32%) | 28/133 (21%) |
| `evade` or `vague` at one or more response tokens | 5/19 (26%) | 32/133 (24%) |
| share of response tokens carrying any of the lie-side set | 6.2% | 6.1% |

## G. Strength: transcripts with any of the lie-side set at a token held by at least s band layers

Table A counts a word present at one band layer, which over a response of hundreds of tokens gives many chances.
Here s is the number of band layers (of 24) whose top 16 hold one of the lie-side set at that token; the newline is given beside it.

| s | at a response token: lies / truths / np truths / unrelated | at the newline |
|---|---|---|
| 1 | 119/152 (78%) / 67/81 (83%) / 77/138 (56%) / 169/703 (24%) | 138/152 (91%) / 21/81 (26%) / 12/138 (9%) / 5/703 (1%) |
| 2 | 113/152 (74%) / 67/81 (83%) / 69/138 (50%) / 145/703 (21%) | 133/152 (88%) / 18/81 (22%) / 8/138 (6%) / 4/703 (1%) |
| 4 | 108/152 (71%) / 63/81 (78%) / 61/138 (44%) / 108/703 (15%) | 128/152 (84%) / 14/81 (17%) / 6/138 (4%) / 4/703 (1%) |
| 8 | 95/152 (62%) / 60/81 (74%) / 48/138 (35%) / 69/703 (10%) | 121/152 (80%) / 9/81 (11%) / 1/138 (1%) / 2/703 (0%) |
| 12 | 83/152 (55%) / 52/81 (64%) / 35/138 (25%) / 45/703 (6%) | 105/152 (69%) / 6/81 (7%) / 1/138 (1%) / 0/703 (0%) |
| 16 | 62/152 (41%) / 48/81 (59%) / 29/138 (21%) / 30/703 (4%) | 76/152 (50%) / 3/81 (4%) / 0/138 (0%) / 0/703 (0%) |

The same for the pressure set:

| s | at a response token: lies / truths / np truths / unrelated | at the newline |
|---|---|---|
| 1 | 107/152 (70%) / 65/81 (80%) / 41/138 (30%) / 84/703 (12%) | 134/152 (88%) / 19/81 (23%) / 4/138 (3%) / 0/703 (0%) |
| 2 | 104/152 (68%) / 64/81 (79%) / 34/138 (25%) / 72/703 (10%) | 127/152 (84%) / 16/81 (20%) / 3/138 (2%) / 0/703 (0%) |
| 4 | 95/152 (62%) / 60/81 (74%) / 29/138 (21%) / 46/703 (7%) | 123/152 (81%) / 13/81 (16%) / 2/138 (1%) / 0/703 (0%) |
| 8 | 84/152 (55%) / 55/81 (68%) / 24/138 (17%) / 32/703 (5%) | 117/152 (77%) / 9/81 (11%) / 0/138 (0%) / 0/703 (0%) |
| 12 | 63/152 (41%) / 48/81 (59%) / 23/138 (17%) / 19/703 (3%) | 102/152 (67%) / 6/81 (7%) / 0/138 (0%) / 0/703 (0%) |
| 16 | 40/152 (26%) / 44/81 (54%) / 18/138 (13%) / 15/703 (2%) | 73/152 (48%) / 3/81 (4%) / 0/138 (0%) / 0/703 (0%) |

Response tokens with any of the lie-side set held by 8 or more band layers, per 100 tokens: lies 3.6, truths 6.7, no-pressure truths 3.5, unrelated 0.4.

## F. Echo: transcripts whose response text contains a word of the list

The readout can copy the text, so Table A is repeated without these transcripts.

| list | text contains a list word: lies / truths / np truths / unrelated | at any response token, echo transcripts left out |
|---|---|---|
| lie | 20/152 / 23/81 / 15/138 / 74/703 | 44/132 (33%) / 25/58 (43%) / 12/123 (10%) / 24/629 (4%) |
| fake | 0/152 / 0/81 / 0/138 / 0/703 | 79/152 (52%) / 47/81 (58%) / 30/138 (22%) / 69/703 (10%) |
| deceive | 0/152 / 7/81 / 1/138 / 0/703 | 46/152 (30%) / 36/74 (49%) / 16/137 (12%) / 18/703 (3%) |
| falsehood | 0/152 / 0/81 / 0/138 / 0/703 | 61/152 (40%) / 44/81 (54%) / 37/138 (27%) / 16/703 (2%) |
| fabricate | 1/152 / 0/81 / 0/138 / 0/703 | 40/151 (26%) / 35/81 (43%) / 29/138 (21%) / 55/703 (8%) |
| conceal | 0/152 / 0/81 / 0/138 / 0/703 | 78/152 (51%) / 52/81 (64%) / 12/138 (9%) / 9/703 (1%) |
| misinformation | 5/152 / 3/81 / 2/138 / 3/703 | 96/147 (65%) / 52/78 (67%) / 68/136 (50%) / 46/700 (7%) |
| false | 14/152 / 16/81 / 4/138 / 1/703 | 72/138 (52%) / 39/65 (60%) / 37/134 (28%) / 46/702 (7%) |
| mislead | 5/152 / 7/81 / 4/138 / 0/703 | 77/147 (52%) / 49/74 (66%) / 27/134 (20%) / 31/703 (4%) |
| dishonest | 1/152 / 1/81 / 1/138 / 0/703 | 35/151 (23%) / 41/80 (51%) / 17/137 (12%) / 13/703 (2%) |
| evade | 0/152 / 2/81 / 1/138 / 0/703 | 20/152 (13%) / 23/79 (29%) / 16/137 (12%) / 43/703 (6%) |
| vague | 0/152 / 1/81 / 0/138 / 5/703 | 17/152 (11%) / 4/80 (5%) / 9/138 (7%) / 104/698 (15%) |
| honest | 4/152 / 21/81 / 5/138 / 4/703 | 107/148 (72%) / 49/60 (82%) / 39/133 (29%) / 62/699 (9%) |
| candid | 0/152 / 0/81 / 0/138 / 0/703 | 66/152 (43%) / 60/81 (74%) / 29/138 (21%) / 13/703 (2%) |
| disclose | 3/152 / 4/81 / 3/138 / 1/703 | 61/149 (41%) / 52/77 (68%) / 43/135 (32%) / 57/702 (8%) |
| confess | 0/152 / 0/81 / 0/138 / 0/703 | 24/152 (16%) / 46/81 (57%) / 19/138 (14%) / 6/703 (1%) |
| refuse | 0/152 / 0/81 / 0/138 / 3/703 | 34/152 (22%) / 50/81 (62%) / 21/138 (15%) / 67/700 (10%) |
| knowingly | 4/152 / 1/81 / 1/138 / 2/703 | 86/148 (58%) / 52/80 (65%) / 53/137 (39%) / 121/701 (17%) |
| cannot | 18/152 / 42/81 / 30/138 / 19/703 | 67/134 (50%) / 23/39 (59%) / 51/108 (47%) / 136/684 (20%) |
| deny | 2/152 / 4/81 / 0/138 / 1/703 | 48/150 (32%) / 23/77 (30%) / 30/138 (22%) / 19/702 (3%) |
| situation | 31/152 / 22/81 / 16/138 / 51/703 | 91/121 (75%) / 51/59 (86%) / 72/122 (59%) / 294/652 (45%) |

## The lists

- **lie** (17): `lying`, `␣lie`, `lie`, `␣lies`, `␣lying`, `␣Lie`, `␣lied`, `lies`, `␣liar`, `Lie`, `␣Lies`, `谎`, `谎言`, `撒谎`, `说谎`, `␣거짓`, `␣mentira`
- **fake** (9): `␣fake`, `fake`, `␣Fake`, `Fake`, `_fake`, `.fake`, `假`, `虚假`, `假的`
- **deceive** (7): `␣deception`, `␣deceptive`, `␣deceit`, `␣deceive`, `␣deceived`, `骗`, `欺骗`
- **falsehood** (1): `␣falsehood`
- **fabricate** (5): `␣fabricated`, `伪造`, `虚构`, `造假`, `弄虚作假`
- **conceal** (3): `瞒`, `隐瞒`, `掩盖`
- **misinformation** (2): `␣misinformation`, `虚假信息`
- **false** (12): `␣false`, `␣False`, `false`, `False`, `␣FALSE`, `FALSE`, `>false`, `␣fals`, `␣falsely`, `␣untrue`, `/false`, `真假`
- **mislead** (4): `␣misleading`, `␣misled`, `误导`, `误导性`
- **dishonest** (1): `␣dishonest`
- **evade** (8): `␣dodge`, `␣evade`, `␣evasion`, `␣deflect`, `逃避`, `避开`, `回避`, `规避`
- **vague** (7): `␣vague`, `␣ambiguous`, `␣ambigu`, `␣ambiguity`, `␣vaguely`, `ambiguous`, `含糊`
- **honest** (10): `␣honest`, `␣honestly`, `␣honesty`, `␣Honest`, `诚信`, `真诚`, `诚实`, `正直`, `诚实守信`, `坦诚`
- **candid** (1): `坦诚`
- **disclose** (14): `␣disclosure`, `␣revealing`, `␣disclose`, `␣disclosed`, `␣disclosures`, `␣Disclosure`, `Disclosure`, `␣disclosing`, `公开`, `披露`, `信息公开`, `信息披露`, `揭露`, `公开的`
- **confess** (4): `␣confess`, `␣confession`, `␣confessed`, `坦白`
- **refuse** (13): `␣refused`, `␣refuse`, `␣refusing`, `␣refuses`, `␣refusal`, `拒`, `拒绝`, `拒絕`, `拒不`, `拒绝了`, `␣отказ`, `␣отказа`, `␣refus`
- **knowingly** (5): `␣knowing`, `␣Knowing`, `␣knowingly`, `Knowing`, `明知`
- **cannot** (11): `␣cannot`, `␣unable`, `Unable`, `Cannot`, `cannot`, `␣Cannot`, `␣Unable`, `unable`, `无法`, `我不能`, `我无法`
- **deny** (10): `␣denied`, `␣deny`, `␣denial`, `␣denying`, `␣denies`, `Denied`, `␣Denied`, `deny`, `否认`, `否定`
- **situation** (48): `legal`, `␣prompt`, `␣instructions`, `Constraints`, `␣trick`, `␣moral`, `␣constraints`, `␣Privacy`, `␣constraint`, `␣trap`, `␣prohibited`, `␣Instructions`, `␣Constraint`, `␣morality`, `privacy`, `/legal`, `␣prompts`, `␣morally`, `␣Compliance`, `␣Prompt`, `_constraints`, `instructions`, `␣Unauthorized`, `constraints`, `␣Silence`, `␣hypocrisy`, `onestly`, `_legal`, `␣Constraints`, `␣Moral`, `␣loophole`, `_persona`, `法`, `伪`, `违规`, `测试`, `违法违规`, `依规`, `承认`, `指令`, `约束`, `沉默`, `合规`, `陷阱`, `职业道德`, `伪装`, `隐秘`, `规范要求`

