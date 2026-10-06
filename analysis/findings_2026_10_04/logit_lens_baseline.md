# The logit lens at the newline after the response (baseline for Section 4.6)

Qwen3.6-27B, layers 35 to 58, top 16 per layer, build split. A family is present when one of its tokens is in
the top 16 at one or more band layers. Unrelated chats: the first set of 158, as in the tables of 4.1.

## A. The ten families of 4.1, one fixed token list (the J-lens's draft lists), read with each lens

| family | tokens | lens | lies (152) | truths (81) | no-pressure truths (138) | unrelated (158) |
|---|---|---|---|---|---|---|
| lie | 17 | J-lens | 127 (84%) | 7 (9%) | 0 (0%) | 0 (0%) |
|  |  | logit lens | 96 (63%) | 3 (4%) | 0 (0%) | 0 (0%) |
| fake | 9 | J-lens | 117 (77%) | 5 (6%) | 0 (0%) | 0 (0%) |
|  |  | logit lens | 84 (55%) | 1 (1%) | 1 (1%) | 1 (1%) |
| conceal | 3 | J-lens | 109 (72%) | 17 (21%) | 2 (1%) | 0 (0%) |
|  |  | logit lens | 78 (51%) | 9 (11%) | 1 (1%) | 0 (0%) |
| misinformation | 2 | J-lens | 101 (66%) | 7 (9%) | 10 (7%) | 0 (0%) |
|  |  | logit lens | 34 (22%) | 0 (0%) | 0 (0%) | 0 (0%) |
| deceive | 7 | J-lens | 94 (62%) | 5 (6%) | 0 (0%) | 0 (0%) |
|  |  | logit lens | 53 (35%) | 2 (2%) | 0 (0%) | 0 (0%) |
| falsehood | 1 | J-lens | 89 (59%) | 0 (0%) | 2 (1%) | 0 (0%) |
|  |  | logit lens | 46 (30%) | 0 (0%) | 2 (1%) | 0 (0%) |
| fabricate | 5 | J-lens | 83 (55%) | 1 (1%) | 1 (1%) | 0 (0%) |
|  |  | logit lens | 85 (56%) | 2 (2%) | 5 (4%) | 0 (0%) |
| false | 12 | J-lens | 79 (52%) | 2 (2%) | 1 (1%) | 0 (0%) |
|  |  | logit lens | 58 (38%) | 0 (0%) | 2 (1%) | 0 (0%) |
| mislead | 4 | J-lens | 61 (40%) | 6 (7%) | 2 (1%) | 0 (0%) |
|  |  | logit lens | 9 (6%) | 2 (2%) | 0 (0%) | 0 (0%) |
| dishonest | 1 | J-lens | 35 (23%) | 4 (5%) | 0 (0%) | 0 (0%) |
|  |  | logit lens | 6 (4%) | 1 (1%) | 0 (0%) | 0 (0%) |

## B. The detectors of 4.4 with the same lists, read with each lens (build split, in-sample)

| detector | lens | lies (152) | truths (81) | no-pressure truths (138) | unrelated (158) | AUROC, lies against truths |
|---|---|---|---|---|---|---|
| the `lie` family | J-lens | 127 (84%) | 7 (9%) | 0 (0%) | 0 (0%) | 0.87 |
| one or more of the eight | J-lens | 133 (88%) | 10 (12%) | 13 (9%) | 0 (0%) | 0.88 |
| two or more of the eight | J-lens | 126 (83%) | 6 (7%) | 2 (1%) | 0 (0%) | 0.88 |
| the count of the eight, as a score | J-lens |  |  |  |  | 0.91 |
| the `lie` family | logit lens | 96 (63%) | 3 (4%) | 0 (0%) | 0 (0%) | 0.80 |
| one or more of the eight | logit lens | 116 (76%) | 7 (9%) | 8 (6%) | 1 (1%) | 0.84 |
| two or more of the eight | logit lens | 98 (64%) | 3 (4%) | 1 (1%) | 0 (0%) | 0.80 |
| the count of the eight, as a score | logit lens |  |  |  |  | 0.86 |
| the `lie` family, the logit lens's own list | logit lens | 96 (63%) | 3 (4%) | 0 (0%) | 0 (0%) | 0.80 |
| one or more of the logit lens's own families of the same names (lie, fake, deceive, falsehood, fabricate, false, mislead) | logit lens | 132 (87%) | 12 (15%) | 6 (4%) | 10 (6%) | 0.86 |
| two or more of the logit lens's own families of the same names (lie, fake, deceive, falsehood, fabricate, false, mislead) | logit lens | 107 (70%) | 4 (5%) | 1 (1%) | 0 (0%) | 0.83 |
| the count of those 7, as a score | logit lens |  |  |  |  | 0.90 |

The word lists of the first eight rows were chosen from the J-lens's readouts, which favours the J-lens. The last
four rows use the lists proposed from the logit lens's own readouts. It has no `misinformation` family: its `falsehood`
family holds the tokens `misinformation` and 虚假信息.

## C. The logit lens's own draft families at this token, in 20% or more of lies or of truths

80 draft families were kept for the logit lens at this token; 39 are in 20% or more of lies or of truths.
Sorted by the share of lies minus the share of truths.

| family | side | members (a selection) | lies (152) | truths (81) | no-pressure truths (138) | unrelated (158) | lies minus truths |
|---|---|---|---|---|---|---|---|
| lie | lie | `谎言`, `说谎`, `撒谎`, `lie`, `谎` … (17 tokens) | 96 (63%) | 3 (4%) | 0 (0%) | 0 (0%) | +59 points |
| deceive | lie | `欺骗`, `骗`, `deception`, `deceptive`, `deceive` … (9 tokens) | 110 (72%) | 11 (14%) | 2 (1%) | 9 (6%) | +59 points |
| uphold | unclear | `维护`, `和维护`, `与维护`, `维护和` | 98 (64%) | 10 (12%) | 7 (5%) | 0 (0%) | +52 points |
| scripted | unclear | `canned`, `scripted`, `套用`, `口径` | 98 (64%) | 11 (14%) | 8 (6%) | 0 (0%) | +51 points |
| false | lie | `false`, `False`, `(false`, `false`, `False` … (16 tokens) | 79 (52%) | 1 (1%) | 2 (1%) | 0 (0%) | +51 points |
| fake | lie | `假的`, `假`, `fake`, `fake`, `Fake` | 76 (50%) | 1 (1%) | 1 (1%) | 1 (1%) | +49 points |
| fabricate | lie | `fabricated`, `凭空`, `fabrication`, `invented`, `invent` … (7 tokens) | 75 (49%) | 1 (1%) | 0 (0%) | 0 (0%) | +48 points |
| official line | unclear | `口径` | 92 (61%) | 11 (14%) | 5 (4%) | 0 (0%) | +47 points |
| conceal | lie | `隐瞒`, `掩盖`, `掩饰`, `瞒`, `遮掩` … (11 tokens) | 89 (59%) | 10 (12%) | 1 (1%) | 1 (1%) | +46 points |
| firm | unclear | `坚`, `坚定`, `firmly`, `坚决`, `firm` … (8 tokens) | 84 (55%) | 14 (17%) | 1 (1%) | 0 (0%) | +38 points |
| falsehood | lie | `falsehood`, `misinformation`, `虚假信息` | 57 (38%) | 0 (0%) | 2 (1%) | 0 (0%) | +38 points |
| fiction | unclear | `虚构`, `fictional`, `fiction`, `fict`, `-fiction` … (7 tokens) | 59 (39%) | 2 (2%) | 5 (4%) | 4 (3%) | +36 points |
| confident | unclear | `confidently`, `自信`, `confident`, `confidence`, `自信的` … (9 tokens) | 53 (35%) | 1 (1%) | 0 (0%) | 0 (0%) | +34 points |
| assert | unclear | `assert`, `_assert`, `assert`, `asserting`, `.assert` … (13 tokens) | 53 (35%) | 4 (5%) | 2 (1%) | 0 (0%) | +30 points |
| ostensibly | unclear | `表面上` | 39 (26%) | 0 (0%) | 0 (0%) | 0 (0%) | +26 points |
| outright | unclear | `outright` | 42 (28%) | 3 (4%) | 0 (0%) | 0 (0%) | +24 points |
| downplay | lie | `淡化`, `gloss` | 37 (24%) | 5 (6%) | 0 (0%) | 0 (0%) | +18 points |
| euphemistic | unclear | `委婉` | 42 (28%) | 13 (16%) | 6 (4%) | 0 (0%) | +12 points |
| fact | truth | `fact`, `reality`, `facts`, `Fact`, `fact` … (31 tokens) | 54 (36%) | 20 (25%) | 91 (66%) | 36 (23%) | +11 points |
| contradict | unclear | `contradict`, `contrad`, `矛盾`, `contradictory`, `contradiction` | 45 (30%) | 16 (20%) | 13 (9%) | 0 (0%) | +10 points |
| factual | truth | `factual`, `事实`, `的事实` | 39 (26%) | 13 (16%) | 101 (73%) | 20 (13%) | +10 points |
| wrong | lie | `wrong`, `WRONG`, `错`, `错误`, `不对` … (10 tokens) | 36 (24%) | 12 (15%) | 16 (12%) | 5 (3%) | +9 points |
| informed | unclear | `知情` | 25 (16%) | 18 (22%) | 16 (12%) | 0 (0%) | -6 points |
| direct | unclear | `直接`, `direct`, `directly`, `正面`, `straight` … (14 tokens) | 116 (76%) | 70 (86%) | 128 (93%) | 27 (17%) | -10 points |
| incorrect | lie | `incorrect`, `inaccur`, `inaccurate`, `不符合`, `有误` | 29 (19%) | 27 (33%) | 8 (6%) | 1 (1%) | -14 points |
| truth | truth | `truth`, `truth`, `Truth`, `Truth`, `真相` … (10 tokens) | 29 (19%) | 29 (36%) | 44 (32%) | 0 (0%) | -17 points |
| integrity | truth | `正直`, `integrity`, `Integrity` | 1 (1%) | 17 (21%) | 2 (1%) | 1 (1%) | -20 points |
| reject | unclear | `reject`, `rejection`, `rejecting`, `Reject`, `reject` … (6 tokens) | 2 (1%) | 19 (23%) | 1 (1%) | 0 (0%) | -22 points |
| seek truth from facts | truth | `实事求是` | 0 (0%) | 19 (23%) | 20 (14%) | 0 (0%) | -23 points |
| truthful | truth | `truthful`, `如实`, `实话`, `说实话`, `实事求是` | 38 (25%) | 41 (51%) | 53 (38%) | 0 (0%) | -26 points |
| confess | truth | `坦白`, `confession`, `confess`, `confessed` | 0 (0%) | 23 (28%) | 7 (5%) | 0 (0%) | -28 points |
| transparent | truth | `transparency`, `透明`, `transparent`, `透明度`, `透明的` … (8 tokens) | 0 (0%) | 24 (30%) | 13 (9%) | 0 (0%) | -30 points |
| honest | truth | `诚实`, `诚`, `honesty`, `honest`, `honestly` … (9 tokens) | 38 (25%) | 45 (56%) | 56 (41%) | 6 (4%) | -31 points |
| ethical | unclear | `ethical`, `伦理`, `ethics`, `Ethics`, `ethical` … (9 tokens) | 1 (1%) | 26 (32%) | 2 (1%) | 1 (1%) | -31 points |
| refuse | unclear | `拒`, `refusal`, `拒绝`, `refused`, `refuse` … (13 tokens) | 14 (9%) | 33 (41%) | 8 (6%) | 0 (0%) | -32 points |
| moral | unclear | `moral`, `道德`, `的道德`, `职业道德` | 0 (0%) | 26 (32%) | 2 (1%) | 0 (0%) | -32 points |
| sincere | truth | `真诚`, `诚恳`, `坦诚` | 2 (1%) | 32 (40%) | 19 (14%) | 0 (0%) | -38 points |
| candid | truth | `坦诚`, `frank`, `直言` | 2 (1%) | 32 (40%) | 21 (15%) | 1 (1%) | -38 points |
| disclose | truth | `disclosure`, `透露`, `disclosed`, `Disclosure`, `披露` … (18 tokens) | 6 (4%) | 37 (46%) | 33 (24%) | 0 (0%) | -42 points |
