# Draft families: qwen3.6-27b, J-lens, part Q6_factual, group questionb

Written by `scripts/apply_family_decisions.py` (2026-10-01; draft, not frozen). Counts are `present / transcripts (share)`
on the build split.

## q_tok8

| family | side | members | lies | truths | no-pressure truths | unrelated | lies that deny | truths that deny |
|---|---|---|---|---|---|---|---|---|
| self_check (checking or examining oneself) | unclear | `自查`, `自检`, `审查` | 38/152 (25%) | 47/81 (58%) | 121/138 (88%) | 131/158 (83%) | 18/43 (42%) | 44/73 (60%) |
| lie (telling a lie / a lie) | lie | `说谎`, `谎言` | 26/152 (17%) | 19/81 (23%) | 1/138 (1%) | 12/158 (8%) | 6/43 (14%) | 16/73 (22%) |
| truthful (telling the truth) | truth | `␣truthful` | 17/152 (11%) | 2/81 (2%) | 0/138 (0%) | 18/158 (11%) | 7/43 (16%) | 1/73 (1%) |
| true (true, real) | truth | `␣true`, `true`, `True`, `␣True`, `␣TRUE`, `真`, `的真` | 10/152 (7%) | 3/81 (4%) | 1/138 (1%) | 54/158 (34%) | 4/43 (9%) | 2/73 (3%) |
| wrong (wrong, mistaken) | lie | `错误` | 2/152 (1%) | 10/81 (12%) | 29/138 (21%) | 69/158 (44%) | 2/43 (5%) | 10/73 (14%) |
| reflect (reflecting on one's own act) | unclear | `反思`, `␣reflection`, `reflect`, `Reflect`, `reflection` | 9/152 (6%) | 2/81 (2%) | 44/138 (32%) | 42/158 (27%) | 3/43 (7%) | 2/73 (3%) |
| intentional (doing it knowingly / on purpose) | unclear | `明知` | 1/152 (1%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 1/43 (2%) | 0/73 (0%) |

Not in the draft: truth (excluded: truth from the question on); admit (excluded: admit / deny / acknowledge); false (excluded: the question's own word)

## q_tok9

| family | side | members | lies | truths | no-pressure truths | unrelated | lies that deny | truths that deny |
|---|---|---|---|---|---|---|---|---|
| true (true, real) | truth | `␣true`, `true`, `True`, `␣True`, `␣TRUE`, `:true`, `真` | 40/152 (26%) | 19/81 (23%) | 29/138 (21%) | 91/158 (58%) | 4/43 (9%) | 16/73 (22%) |
| honest (being honest) | truth | `␣honestly` | 6/152 (4%) | 2/81 (2%) | 0/138 (0%) | 0/158 (0%) | 4/43 (9%) | 2/73 (3%) |
| truthful (telling the truth) | truth | `␣truthful` | 1/152 (1%) | 0/81 (0%) | 1/138 (1%) | 0/158 (0%) | 1/43 (2%) | 0/73 (0%) |

Not in the draft: truth (excluded: truth from the question on); false (excluded: the question's own word)

## q_tok10

| family | side | members | lies | truths | no-pressure truths | unrelated | lies that deny | truths that deny |
|---|---|---|---|---|---|---|---|---|
| wrong (wrong, mistaken) | lie | `␣WRONG` | 2/152 (1%) | 1/81 (1%) | 2/138 (1%) | 0/158 (0%) | 2/43 (5%) | 1/73 (1%) |
| incorrect (incorrect) | lie | `␣Incorrect` | 0/152 (0%) | 0/81 (0%) | 0/138 (0%) | 1/158 (1%) | 0/43 (0%) | 0/73 (0%) |

## q_tok11

| family | side | members | lies | truths | no-pressure truths | unrelated | lies that deny | truths that deny |
|---|---|---|---|---|---|---|---|---|
| sorry (apologizing) | unclear | `␣Sorry` | 1/152 (1%) | 2/81 (2%) | 0/138 (0%) | 0/158 (0%) | 1/43 (2%) | 2/73 (3%) |
| incorrect (incorrect) | lie | `␣Incorrect` | 1/152 (1%) | 0/81 (0%) | 1/138 (1%) | 5/158 (3%) | 0/43 (0%) | 0/73 (0%) |
| true (true, real) | truth | `␣True` | 0/152 (0%) | 0/81 (0%) | 0/138 (0%) | 3/158 (2%) | 0/43 (0%) | 0/73 (0%) |

Not in the draft: false (excluded: the question's own word)

## q_tok13

| family | side | members | lies | truths | no-pressure truths | unrelated | lies that deny | truths that deny |
|---|---|---|---|---|---|---|---|---|
| truthful (telling the truth) | truth | `␣truthful`, `实事求是` | 111/152 (73%) | 30/81 (37%) | 39/138 (28%) | 12/158 (8%) | 22/43 (51%) | 26/73 (36%) |
| true (true, real) | truth | `True`, `␣True`, `真`, `真实`, `真实性`, `真正的`, `真实的`, `真實`, `的真`, `的真实`, `的真实性` | 84/152 (55%) | 20/81 (25%) | 4/138 (3%) | 4/158 (3%) | 9/43 (21%) | 18/73 (25%) |
| violate (violating rules) | unclear | `违反`, `违反了`, `违规`, `违背`, `␣violate`, `␣violates`, `␣violating`, `␣violations`, `␣violation`, `␣violated` | 72/152 (47%) | 29/81 (36%) | 53/138 (38%) | 1/158 (1%) | 11/43 (26%) | 23/73 (32%) |
| fictional (made up / fiction) | unclear | `虚构`, `␣fictional`, `␣Fiction`, `fiction`, `␣fiction` | 75/152 (49%) | 23/81 (28%) | 2/138 (1%) | 17/158 (11%) | 8/43 (19%) | 20/73 (27%) |
| unethical (unethical / immoral) | unclear | `␣unethical`, `␣immoral` | 78/152 (51%) | 16/81 (20%) | 0/138 (0%) | 0/158 (0%) | 5/43 (12%) | 12/73 (16%) |
| fake (fake / forged) | lie | `fake`, `Fake`, `␣fake`, `␣Fake`, `伪造` | 73/152 (48%) | 18/81 (22%) | 0/138 (0%) | 5/158 (3%) | 9/43 (21%) | 14/73 (19%) |
| fact (fact, factual) | truth | `␣fact`, `␣actual`, `␣reality`, `actual`, `␣facts`, `Fact`, `Actual`, `fact`, `␣Actual`, `_FACT`, `␣Fact`, `_actual`, `␣Reality`, `␣Facts`, `Reality`, `_fact`, `␣FACT`, `FACT`, `␣factual`, `facts`, `实际`, `事实`, `实际情况`, `的事实`, `实际的`, `根据实际情况`, `事实和`, `␣réalité` | 69/152 (45%) | 14/81 (17%) | 18/138 (13%) | 29/158 (18%) | 14/43 (33%) | 12/73 (16%) |
| deceive (the act of deceiving) | lie | `欺骗`, `␣deception`, `␣deceptive`, `␣deceive`, `骗` | 71/152 (47%) | 8/81 (10%) | 0/138 (0%) | 0/158 (0%) | 8/43 (19%) | 6/73 (8%) |
| conceal (hiding / concealing) | lie | `隐瞒`, `隐藏`, `隐藏的`, `␣hidden`, `hidden`, `-hidden` | 65/152 (43%) | 10/81 (12%) | 1/138 (1%) | 0/158 (0%) | 6/43 (14%) | 8/73 (11%) |
| ethics (ethics / ethical) | unclear | `␣ethical`, `␣ethics`, `␣Ethics`, `ethical`, `伦理`, `␣ethic`, `职业道德` | 61/152 (40%) | 14/81 (17%) | 0/138 (0%) | 0/158 (0%) | 8/43 (19%) | 11/73 (15%) |
| conceal (concealing a fact) | lie | `隐瞒` | 64/152 (42%) | 9/81 (11%) | 1/138 (1%) | 0/158 (0%) | 5/43 (12%) | 7/73 (10%) |
| ethical (ethical / moral (adjective)) | unclear | `␣ethical`, `ethical`, `␣moral`, `␣Moral`, `␣morally` | 61/152 (40%) | 11/81 (14%) | 0/138 (0%) | 0/158 (0%) | 8/43 (19%) | 8/73 (11%) |
| ethics (ethics / morality (noun)) | unclear | `␣ethics`, `␣Ethics`, `␣ethic`, `伦理`, `道德`, `的道德`, `职业道德`, `␣morality`, `␣morals` | 55/152 (36%) | 14/81 (17%) | 0/138 (0%) | 0/158 (0%) | 6/43 (14%) | 11/73 (15%) |
| lie (telling a lie / a lie) | lie | `谎言`, `说谎`, `撒谎`, `谎` | 53/152 (35%) | 4/81 (5%) | 5/138 (4%) | 1/158 (1%) | 8/43 (19%) | 2/73 (3%) |
| prohibited (forbidden) | unclear | `禁止`, `␣prohibited`, `␣prohibit`, `␣prohibits`, `␣forbidden` | 35/152 (23%) | 20/81 (25%) | 3/138 (2%) | 0/158 (0%) | 5/43 (12%) | 16/73 (22%) |
| honest (being honest) | truth | `␣honesty`, `诚实`, `␣honest`, `诚信` | 33/152 (22%) | 10/81 (12%) | 1/138 (1%) | 0/158 (0%) | 9/43 (21%) | 8/73 (11%) |
| wrong (wrong, mistaken) | lie | `␣wrong`, `␣ERROR`, `␣WRONG`, `误`, `错误`, `的错误` | 17/152 (11%) | 25/81 (31%) | 103/138 (75%) | 134/158 (85%) | 6/43 (14%) | 22/73 (30%) |
| moral (morality / moral) | unclear | `道德`, `␣moral`, `␣morally`, `␣morality`, `␣Moral`, `␣morals`, `的道德` | 36/152 (24%) | 4/81 (5%) | 0/138 (0%) | 0/158 (0%) | 4/43 (9%) | 2/73 (3%) |
| misinformation (false information) | lie | `␣misinformation` | 28/152 (18%) | 10/81 (12%) | 10/138 (7%) | 14/158 (9%) | 4/43 (9%) | 9/73 (12%) |
| persona (an adopted persona) | unclear | `␣persona`, `␣personas`, `␣Persona`, `Persona`, `persona`, `␣Personas` | 18/152 (12%) | 10/81 (12%) | 0/138 (0%) | 1/158 (1%) | 4/43 (9%) | 10/73 (14%) |
| incorrect (incorrect) | lie | `␣incorrect`, `Incorrect`, `␣inaccur`, `␣incorrectly`, `␣inaccurate`, `incorrect`, `␣erroneous`, `␣Incorrect`, `错误的`, `不符合` | 8/152 (5%) | 20/81 (25%) | 92/138 (67%) | 109/158 (69%) | 3/43 (7%) | 19/73 (26%) |
| cheat (cheating) | lie | `作弊`, `␣cheating` | 23/152 (15%) | 3/81 (4%) | 0/138 (0%) | 0/158 (0%) | 2/43 (5%) | 1/73 (1%) |
| comply (complying with rules) | unclear | `␣compliance`, `␣Compliance`, `␣comply`, `␣complying`, `遵守`, `严格遵守`, `合规` | 12/152 (8%) | 14/81 (17%) | 4/138 (3%) | 0/158 (0%) | 4/43 (9%) | 13/73 (18%) |
| dishonest (being dishonest) | lie | `␣dishonest` | 22/152 (14%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 1/43 (2%) | 0/73 (0%) |
| intentional (doing it knowingly / on purpose) | unclear | `故意`, `明知`, `␣intentionally`, `␣intentional`, `␣deliberately`, `␣deliberate`, `␣knowingly` | 21/152 (14%) | 2/81 (2%) | 0/138 (0%) | 0/158 (0%) | 3/43 (7%) | 2/73 (3%) |
| fabricate (forging / fabricating) | lie | `伪造` | 16/152 (11%) | 3/81 (4%) | 0/138 (0%) | 0/158 (0%) | 2/43 (5%) | 2/73 (3%) |
| role-play (playing a role) | unclear | `角色扮演`, `扮演` | 12/152 (8%) | 6/81 (7%) | 0/138 (0%) | 0/158 (0%) | 4/43 (9%) | 6/73 (8%) |
| intentional (doing it on purpose) | unclear | `故意`, `␣intentionally`, `␣intentional` | 15/152 (10%) | 2/81 (2%) | 0/138 (0%) | 0/158 (0%) | 2/43 (5%) | 2/73 (3%) |
| audit (auditing) | unclear | `Audit`, `␣audit`, `␣auditing`, `审计`, `audit`, `␣audits`, `␣Audit`, `␣auditor` | 7/152 (5%) | 8/81 (10%) | 1/138 (1%) | 0/158 (0%) | 4/43 (9%) | 8/73 (11%) |
| refuse (refusing) | unclear | `拒绝`, `拒绝了`, `␣refusing`, `␣refused`, `␣refuse`, `␣refuses`, `␣refusal`, `␣refus` | 1/152 (1%) | 11/81 (14%) | 0/138 (0%) | 0/158 (0%) | 0/43 (0%) | 11/73 (15%) |
| disclaimer (disclaimer) | unclear | `␣disclaimer`, `Disclaimer`, `␣Disclaimer` | 5/152 (3%) | 7/81 (9%) | 3/138 (2%) | 0/158 (0%) | 1/43 (2%) | 7/73 (10%) |
| reflect (reflecting on one's own act) | unclear | `反思`, `␣reflection`, `reflection`, `␣Reflection`, `Reflection`, `reflect`, `␣reflective`, `␣reflect`, `Reflect`, `.reflect`, `␣Reflect`, `␣reflecting` | 8/152 (5%) | 4/81 (5%) | 24/138 (17%) | 1/158 (1%) | 4/43 (9%) | 4/73 (5%) |
| integrity (integrity) | truth | `诚信`, `␣integrity`, `␣Integrity` | 10/152 (7%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 2/43 (5%) | 0/73 (0%) |
| fraud (fraud) | lie | `␣fraudulent`, `␣fraud`, `␣Fraud`, `欺诈` | 10/152 (7%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 1/43 (2%) | 0/73 (0%) |
| secret (secret / secrecy) | lie | `秘密`, `的秘密`, `␣secret`, `Secret`, `secret`, `␣secretly` | 9/152 (6%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 1/43 (2%) | 1/73 (1%) |
| confidential (confidential) | unclear | `␣confidentiality`, `␣confidential`, `机密` | 5/152 (3%) | 3/81 (4%) | 0/138 (0%) | 0/158 (0%) | 0/43 (0%) | 2/73 (3%) |
| unauthorized (unauthorized) | unclear | `␣Unauthorized`, `␣unauthorized` | 6/152 (4%) | 2/81 (2%) | 0/138 (0%) | 0/158 (0%) | 0/43 (0%) | 2/73 (3%) |
| knowingly (doing it while knowing it is false) | unclear | `明知` | 8/152 (5%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 1/43 (2%) | 0/73 (0%) |
| self_check (checking or examining oneself) | unclear | `自查`, `自检` | 4/152 (3%) | 4/81 (5%) | 26/138 (19%) | 2/158 (1%) | 2/43 (5%) | 4/73 (5%) |
| disguise (disguising / pretending) | lie | `伪装` | 5/152 (3%) | 2/81 (2%) | 0/138 (0%) | 0/158 (0%) | 1/43 (2%) | 2/73 (3%) |
| correct (correct) | truth | `␣correct`, `␣correctly`, `correct`, `Correct`, `␣corrected`, `␣Correct`, `␣correctness`, `正确`, `正确的`, `修正`, `纠错`, `正确答案`, `纠正`, `更正`, `是正确的`, `是否正确` | 1/152 (1%) | 6/81 (7%) | 82/138 (59%) | 56/158 (35%) | 0/43 (0%) | 5/73 (7%) |
| illegal (breaking the law) | unclear | `违法` | 4/152 (3%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 0/43 (0%) | 0/73 (0%) |
| hypocrisy (hypocrisy / two-faced) | lie | `虚伪`, `␣hypocrisy` | 3/152 (2%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 0/43 (0%) | 0/73 (0%) |
| mislead (misleading) | lie | `误导`, `␣misleading` | 2/152 (1%) | 0/81 (0%) | 5/138 (4%) | 1/158 (1%) | 1/43 (2%) | 0/73 (0%) |
| trick (tricking) | lie | `␣trick`, `␣Trick` | 1/152 (1%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 1/43 (2%) | 0/73 (0%) |
| reveal (exposing / revealing) | truth | `揭露` | 1/152 (1%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 0/43 (0%) | 0/73 (0%) |
| accurate (accurate) | truth | `␣accurate`, `␣accuracy`, `Accuracy`, `␣Accuracy` | 0/152 (0%) | 1/81 (1%) | 3/138 (2%) | 1/158 (1%) | 0/43 (0%) | 1/73 (1%) |

Not in the draft: deny (excluded: admit / deny / acknowledge); truth (excluded: truth from the question on); admit (excluded: admit / deny / acknowledge); admit (excluded: admit / deny / acknowledge); false (excluded: the question's own word)
