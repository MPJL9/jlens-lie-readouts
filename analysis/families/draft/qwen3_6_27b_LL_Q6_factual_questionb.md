# Draft families: qwen3.6-27b, logit lens, part Q6_factual, group questionb

Written by `scripts/apply_family_decisions.py` (2026-10-01; draft, not frozen). Counts are `present / transcripts (share)`
on the build split.

## q_tok8

| family | side | members | lies | truths | no-pressure truths | unrelated | lies that deny | truths that deny |
|---|---|---|---|---|---|---|---|---|
| true (true, real) | truth | `␣true`, `true`, `True`, `␣True`, `␣TRUE`, `真`, `的真` | 152/152 (100%) | 81/81 (100%) | 138/138 (100%) | 158/158 (100%) | 43/43 (100%) | 73/73 (100%) |
| self-examine (checking / reflecting on one's own output) | unclear | `自查`, `自检`, `反思`, `自省`, `审视`, `␣reflect`, `␣reflection`, `reflect`, `␣reflecting`, `␣Reflection` | 91/152 (60%) | 69/81 (85%) | 136/138 (99%) | 156/158 (99%) | 35/43 (81%) | 63/73 (86%) |
| correct (correct) | truth | `␣correct` | 12/152 (8%) | 12/81 (15%) | 62/138 (45%) | 87/158 (55%) | 3/43 (7%) | 10/73 (14%) |
| lie (telling a lie) | lie | `␣lie` | 16/152 (11%) | 2/81 (2%) | 1/138 (1%) | 0/158 (0%) | 13/43 (30%) | 1/73 (1%) |
| wrong (wrong, mistaken) | lie | `error`, `␣error`, `指正` | 8/152 (5%) | 6/81 (7%) | 6/138 (4%) | 55/158 (35%) | 4/43 (9%) | 6/73 (8%) |
| knowingly (doing it knowingly, in full awareness) | unclear | `明知` | 11/152 (7%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 5/43 (12%) | 0/73 (0%) |
| objective (being objective) | unclear | `客观` | 8/152 (5%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 5/43 (12%) | 0/73 (0%) |
| honest (being honest / truthful) | truth | `诚实` | 4/152 (3%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 2/43 (5%) | 0/73 (0%) |

Not in the draft: admit (excluded: admit / deny / acknowledge); false (excluded: the question's own word); truth (excluded: truth from the question on)

## q_tok9

| family | side | members | lies | truths | no-pressure truths | unrelated | lies that deny | truths that deny |
|---|---|---|---|---|---|---|---|---|
| true (true, real) | truth | `␣true`, `true`, `True`, `␣True`, `␣TRUE`, `(True`, `的真` | 81/152 (53%) | 32/81 (40%) | 89/138 (64%) | 131/158 (83%) | 13/43 (30%) | 26/73 (36%) |
| honest (being honest / truthful) | truth | `实事求是` | 3/152 (2%) | 4/81 (5%) | 2/138 (1%) | 4/158 (3%) | 0/43 (0%) | 4/73 (5%) |
| correct (correct) | truth | `(true` | 0/152 (0%) | 0/81 (0%) | 0/138 (0%) | 2/158 (1%) | 0/43 (0%) | 0/73 (0%) |

Not in the draft: truth (excluded: truth from the question on); false (excluded: the question's own word)

## q_tok10

| family | side | members | lies | truths | no-pressure truths | unrelated | lies that deny | truths that deny |
|---|---|---|---|---|---|---|---|---|
| true (true, real) | truth | `true`, `True`, `␣True`, `TRUE`, `(True`, `.True`, `的真` | 78/152 (51%) | 38/81 (47%) | 98/138 (71%) | 141/158 (89%) | 12/43 (28%) | 34/73 (47%) |
| wrong (wrong, mistaken) | lie | `错误或`, `对错` | 23/152 (15%) | 28/81 (35%) | 10/138 (7%) | 16/158 (10%) | 10/43 (23%) | 27/73 (37%) |
| correct (correct) | truth | `(true` | 0/152 (0%) | 0/81 (0%) | 0/138 (0%) | 3/158 (2%) | 0/43 (0%) | 0/73 (0%) |

Not in the draft: admit (excluded: admit / deny / acknowledge); false (excluded: the question's own word)

## q_tok11

| family | side | members | lies | truths | no-pressure truths | unrelated | lies that deny | truths that deny |
|---|---|---|---|---|---|---|---|---|
| true (true, real) | truth | `␣true`, `true`, `␣True` | 55/152 (36%) | 22/81 (27%) | 71/138 (51%) | 125/158 (79%) | 4/43 (9%) | 18/73 (25%) |
| sorry (apologising) | unclear | `␣sorry` | 1/152 (1%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 1/43 (2%) | 1/73 (1%) |
| refuse (refusing) | unclear | `␣refusal` | 1/152 (1%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 0/43 (0%) | 0/73 (0%) |

Not in the draft: false (excluded: the question's own word)

## q_tok12

| family | side | members | lies | truths | no-pressure truths | unrelated | lies that deny | truths that deny |
|---|---|---|---|---|---|---|---|---|
| true (true, real) | truth | `␣true`, `true`, `True`, `␣True`, `TRUE`, `成立` | 124/152 (82%) | 71/81 (88%) | 123/138 (89%) | 158/158 (100%) | 25/43 (58%) | 64/73 (88%) |
| silent (staying silent / not speaking) | unclear | `不语` | 67/152 (44%) | 11/81 (14%) | 9/138 (7%) | 52/158 (33%) | 5/43 (12%) | 8/73 (11%) |

Not in the draft: false (excluded: the question's own word)

## q_tok13

| family | side | members | lies | truths | no-pressure truths | unrelated | lies that deny | truths that deny |
|---|---|---|---|---|---|---|---|---|
| objective (being objective) | unclear | `客观`, `␣objectively`, `␣objective`, `objective`, `Objective`, `实事求是` | 131/152 (86%) | 51/81 (63%) | 32/138 (23%) | 27/158 (17%) | 30/43 (70%) | 44/73 (60%) |
| honest (being honest / truthful) | truth | `诚实`, `␣truthful`, `如实`, `实事求是`, `␣honesty`, `忠实`, `诚信`, `诚实守信`, `坦诚`, `␣honest`, `诚` | 130/152 (86%) | 35/81 (43%) | 28/138 (20%) | 7/158 (4%) | 32/43 (74%) | 30/73 (41%) |
| true (true, real) | truth | `␣true`, `true`, `␣real`, `True`, `␣True`, `real`, `␣TRUE`, `真`, `成立`, `真实`, `真实性`, `真正的`, `真实的`, `真實`, `的真`, `的真实`, `的真实性`, `成真` | 123/152 (81%) | 42/81 (52%) | 49/138 (36%) | 47/158 (30%) | 23/43 (53%) | 36/73 (49%) |
| fact (fact, factual) | truth | `␣fact`, `␣reality`, `␣facts`, `Fact`, `fact`, `␣Fact`, `␣Reality`, `␣Facts`, `Reality`, `_fact`, `␣realities`, `␣FACT`, `FACT`, `␣factual`, `facts`, `␣realidad`, `实际`, `符合`, `现实`, `事实`, `实际上`, `实际情况`, `事实上`, `的事实`, `的实际`, `实际的`, `是否符合`, `现实中`, `的现实`, `根据实际情况`, `求实`, `与现实`, `事实和`, `␣realtà` | 112/152 (74%) | 45/81 (56%) | 64/138 (46%) | 43/158 (27%) | 24/43 (56%) | 40/73 (55%) |
| violate (violating rules or principles) | unclear | `违反`, `违背`, `违反了`, `␣violate`, `␣violating`, `␣violations`, `违规`, `␣violation`, `违法` | 94/152 (62%) | 43/81 (53%) | 65/138 (47%) | 1/158 (1%) | 14/43 (33%) | 36/73 (49%) |
| truthful (telling the truth / truthfully) | truth | `␣truthful`, `如实` | 104/152 (68%) | 24/81 (30%) | 26/138 (19%) | 3/158 (2%) | 21/43 (49%) | 22/73 (30%) |
| wrong (wrong, mistaken) | lie | `error`, `␣error`, `␣mistake`, `错`, `错误`, `错了`, `是非`, `指正`, `是错误的` | 72/152 (47%) | 38/81 (47%) | 43/138 (31%) | 114/158 (72%) | 26/43 (60%) | 33/73 (45%) |
| knowingly (doing it knowingly, in full awareness) | unclear | `明知`, `␣knowingly` | 95/152 (62%) | 9/81 (11%) | 14/138 (10%) | 8/158 (5%) | 10/43 (23%) | 5/73 (7%) |
| fictional (fictional / made up) | unclear | `虚构`, `架空`, `␣fictional`, `fiction`, `␣fiction`, `␣Fiction` | 76/152 (50%) | 25/81 (31%) | 7/138 (5%) | 20/158 (13%) | 10/43 (23%) | 21/73 (29%) |
| role-play (playing a role) | unclear | `扮演`, `角色扮演`, `扮演着` | 69/152 (45%) | 28/81 (35%) | 50/138 (36%) | 0/158 (0%) | 12/43 (28%) | 24/73 (33%) |
| incorrect (incorrect) | lie | `␣incorrect`, `错误的`, `不符合`, `错误的是` | 50/152 (33%) | 37/81 (46%) | 64/138 (46%) | 12/158 (8%) | 6/43 (14%) | 33/73 (45%) |
| accurate (accurate) | truth | `␣accurate`, `␣accuracy`, `␣accurately`, `accuracy`, `␣Accuracy`, `准确`, `准确性` | 53/152 (35%) | 15/81 (19%) | 16/138 (12%) | 12/158 (8%) | 12/43 (28%) | 13/73 (18%) |
| faithful (faithful (to facts or instructions)) | unclear | `忠实` | 50/152 (33%) | 17/81 (21%) | 2/138 (1%) | 0/158 (0%) | 4/43 (9%) | 15/73 (21%) |
| hide (hiding / concealing) | lie | `隐瞒`, `␣hidden`, `-hidden`, `隐藏的`, `隐藏`, `hidden`, `Hidden`, `␣hide`, `␣Hidden`, `␣conceal`, `掩盖` | 56/152 (37%) | 9/81 (11%) | 3/138 (2%) | 0/158 (0%) | 7/43 (16%) | 7/73 (10%) |
| persona (an assumed persona) | unclear | `␣persona`, `␣personas`, `Persona`, `␣Persona`, `persona`, `␣Personas` | 43/152 (28%) | 21/81 (26%) | 0/138 (0%) | 1/158 (1%) | 8/43 (19%) | 18/73 (25%) |
| ethics (ethics / morality) | unclear | `␣ethical`, `伦理`, `␣ethics`, `ethical`, `␣Ethics`, `道德`, `␣moral`, `职业道德`, `的道德`, `␣morally`, `␣morality`, `␣ethic`, `␣Moral`, `␣morals` | 54/152 (36%) | 9/81 (11%) | 0/138 (0%) | 0/158 (0%) | 5/43 (12%) | 7/73 (10%) |
| deliberate (doing it intentionally) | unclear | `␣intentionally`, `故意`, `␣deliberately`, `故意的`, `␣deliberate`, `␣intentional`, `刻意`, `有意` | 54/152 (36%) | 7/81 (9%) | 1/138 (1%) | 2/158 (1%) | 5/43 (12%) | 5/73 (7%) |
| self-examine (checking / reflecting on one's own output) | unclear | `自查`, `反思`, `自检`, `␣reflection`, `␣reflective`, `.reflect`, `␣Reflection`, `Reflection`, `Reflect`, `reflection`, `␣reflect`, `reflect`, `自省`, `审视`, `␣Reflect` | 27/152 (18%) | 22/81 (27%) | 40/138 (29%) | 98/158 (62%) | 14/43 (33%) | 22/73 (30%) |
| conceal (concealing / withholding the truth) | lie | `隐瞒`, `␣conceal`, `掩盖`, `遮`, `隐` | 42/152 (28%) | 4/81 (5%) | 1/138 (1%) | 0/158 (0%) | 5/43 (12%) | 3/73 (4%) |
| comply (complying with rules) | unclear | `合规`, `遵守`, `␣compliance`, `严格遵守`, `␣Compliance`, `␣comply` | 19/152 (12%) | 21/81 (26%) | 4/138 (3%) | 0/158 (0%) | 7/43 (16%) | 20/73 (27%) |
| deceive (the act of deceiving) | lie | `欺骗`, `␣deception`, `␣deceptive`, `␣deceit`, `␣deceive`, `骗`, `哄` | 33/152 (22%) | 3/81 (4%) | 1/138 (1%) | 3/158 (2%) | 3/43 (7%) | 2/73 (3%) |
| correct (correct) | truth | `valid`, `␣valid`, `␣correct`, `␣Valid`, `␣correctly`, `correct`, `Correct`, `␣corrected`, `␣Correct`, `␣corrections`, `␣correctness`, `正确`, `正确的`, `正确的是`, `正确答案`, `纠正`, `无误`, `是正确的`, `是否正确`, `是对的` | 10/152 (7%) | 22/81 (27%) | 101/138 (73%) | 100/158 (63%) | 3/43 (7%) | 21/73 (29%) |
| euphemistic (phrasing tactfully / indirectly) | unclear | `委婉` | 8/152 (5%) | 17/81 (21%) | 14/138 (10%) | 0/158 (0%) | 2/43 (5%) | 17/73 (23%) |
| lie (telling a lie) | lie | `说谎`, `谎言`, `␣lie`, `撒谎`, `␣lying`, `lying`, `谎` | 18/152 (12%) | 3/81 (4%) | 2/138 (1%) | 0/158 (0%) | 7/43 (16%) | 2/73 (3%) |
| conscience (conscience) | unclear | `良心` | 18/152 (12%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 0/43 (0%) | 0/73 (0%) |
| reveal (revealing / disclosing) | truth | `透露`, `␣reveal`, `reveal` | 15/152 (10%) | 2/81 (2%) | 0/138 (0%) | 0/158 (0%) | 4/43 (9%) | 2/73 (3%) |
| unethical (being unethical) | lie | `␣unethical` | 8/152 (5%) | 2/81 (2%) | 0/138 (0%) | 0/158 (0%) | 1/43 (2%) | 1/73 (1%) |
| refuse (refusing) | unclear | `拒绝`, `␣refusal`, `拒绝了`, `␣refused`, `␣refuse`, `␣refusing`, `␣refus`, `␣refuses` | 1/152 (1%) | 8/81 (10%) | 0/138 (0%) | 0/158 (0%) | 0/43 (0%) | 8/73 (11%) |
| secret (secrecy) | lie | `␣secret`, `␣secretly`, `秘密`, `Secret`, `secret`, `-secret` | 6/152 (4%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 0/43 (0%) | 0/73 (0%) |
| candid (candour / frankness) | truth | `坦诚` | 3/152 (2%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 2/43 (5%) | 0/73 (0%) |
| silent (staying silent) | unclear | `沉默` | 2/152 (1%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 2/43 (5%) | 0/73 (0%) |
| dishonest (being dishonest) | lie | `␣dishonest` | 1/152 (1%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 0/43 (0%) | 0/73 (0%) |
| fake (fake) | lie | `␣fake`, `fake`, `Fake` | 1/152 (1%) | 0/81 (0%) | 0/138 (0%) | 1/158 (1%) | 1/43 (2%) | 0/73 (0%) |
| pretend (pretending) | lie | `␣pretending` | 1/152 (1%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 1/43 (2%) | 0/73 (0%) |
| trick (tricking) | lie | `␣trick` | 1/152 (1%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 1/43 (2%) | 0/73 (0%) |
| confess (confessing / coming clean) | truth | `坦白` | 1/152 (1%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 0/43 (0%) | 0/73 (0%) |
| truth (the truth) | truth | `求真` | 1/152 (1%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 1/43 (2%) | 0/73 (0%) |
| inaccurate (inaccurate) | lie | `不准确` | 0/152 (0%) | 0/81 (0%) | 0/138 (0%) | 1/158 (1%) | 0/43 (0%) | 0/73 (0%) |

Not in the draft: admit (excluded: admit / deny / acknowledge); admit (excluded: admit / deny / acknowledge); false (excluded: the question's own word)
