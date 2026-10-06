# Draft families: qwen3.6-27b, J-lens, part Q7_ab, group questionc

Written by `scripts/apply_family_decisions.py` (2026-10-01; draft, not frozen). Counts are `present / transcripts (share)`
on the build split.

## q_tok16

| family | side | members | lies | truths | no-pressure truths | unrelated | lies that deny | truths that deny |
|---|---|---|---|---|---|---|---|---|
| true (true, real) | truth | `␣true`, `␣True`, `:true` | 0/152 (0%) | 1/81 (1%) | 0/138 (0%) | 14/158 (9%) | 0/79 (0%) | 1/77 (1%) |
| incorrect (incorrect) | lie | `␣Incorrect` | 0/152 (0%) | 0/81 (0%) | 0/138 (0%) | 1/158 (1%) | 0/79 (0%) | 0/77 (0%) |

## q_tok17

| family | side | members | lies | truths | no-pressure truths | unrelated | lies that deny | truths that deny |
|---|---|---|---|---|---|---|---|---|
| true (true, real) | truth | `␣true`, `True`, `␣True` | 116/152 (76%) | 46/81 (57%) | 65/138 (47%) | 158/158 (100%) | 49/79 (62%) | 42/77 (55%) |
| false (false, untrue) | lie | `␣false`, `␣False`, `false`, `False`, `␣falsehood` | 75/152 (49%) | 64/81 (79%) | 108/138 (78%) | 66/158 (42%) | 42/79 (53%) | 60/77 (78%) |
| misinformation (false information) | lie | `␣misinformation` | 51/152 (34%) | 22/81 (27%) | 9/138 (7%) | 10/158 (6%) | 20/79 (25%) | 20/77 (26%) |
| honest (honest) | truth | `␣honesty`, `␣honest` | 24/152 (16%) | 4/81 (5%) | 0/138 (0%) | 0/158 (0%) | 9/79 (11%) | 4/77 (5%) |
| fake (fake, sham) | lie | `␣fake`, `␣Fake`, `fake`, `Fake` | 5/152 (3%) | 4/81 (5%) | 1/138 (1%) | 0/158 (0%) | 1/79 (1%) | 3/77 (4%) |
| unethical (unethical, immoral) | lie | `␣unethical` | 4/152 (3%) | 3/81 (4%) | 0/138 (0%) | 0/158 (0%) | 0/79 (0%) | 3/77 (4%) |

Not in the draft: deny (excluded: admit / deny / acknowledge); admit (excluded: admit / deny / acknowledge); acknowledge (excluded: admit / deny / acknowledge); truth (excluded: the question's own word)

## q_tok18

| family | side | members | lies | truths | no-pressure truths | unrelated | lies that deny | truths that deny |
|---|---|---|---|---|---|---|---|---|
| false (false, untrue) | lie | `␣False`, `False`, `␣fals`, `/false`, `␣falsehood` | 85/152 (56%) | 65/81 (80%) | 118/138 (86%) | 85/158 (54%) | 42/79 (53%) | 61/77 (79%) |
| unethical (unethical, immoral) | lie | `␣unethical` | 85/152 (56%) | 64/81 (79%) | 95/138 (69%) | 85/158 (54%) | 37/79 (47%) | 61/77 (79%) |
| violate (violating a rule) | unclear | `违反`, `␣violation`, `␣violates`, `违法` | 31/152 (20%) | 44/81 (54%) | 72/138 (52%) | 39/158 (25%) | 10/79 (13%) | 41/77 (53%) |
| incorrect (incorrect) | lie | `␣incorrect`, `incorrect`, `␣Incorrect` | 27/152 (18%) | 40/81 (49%) | 112/138 (81%) | 114/158 (72%) | 12/79 (15%) | 39/77 (51%) |
| wrong (wrong, mistaken) | lie | `␣Wrong`, `␣WRONG`, `错误` | 12/152 (8%) | 33/81 (41%) | 85/138 (62%) | 22/158 (14%) | 8/79 (10%) | 32/77 (42%) |
| accuse (accusing) | unclear | `␣accusations` | 5/152 (3%) | 7/81 (9%) | 13/138 (9%) | 0/158 (0%) | 4/79 (5%) | 6/77 (8%) |
| dishonest (dishonest) | lie | `␣dishonest` | 1/152 (1%) | 3/81 (4%) | 0/138 (0%) | 1/158 (1%) | 0/79 (0%) | 3/77 (4%) |
| fake (fake, sham) | lie | `Fake`, `fake`, `造假` | 0/152 (0%) | 3/81 (4%) | 0/138 (0%) | 1/158 (1%) | 0/79 (0%) | 3/77 (4%) |
| wrongdoing (wrongdoing) | unclear | `␣wrongdoing` | 0/152 (0%) | 3/81 (4%) | 16/138 (12%) | 9/158 (6%) | 0/79 (0%) | 3/77 (4%) |
| correct (correct) | truth | `␣Correct` | 2/152 (1%) | 1/81 (1%) | 2/138 (1%) | 0/158 (0%) | 2/79 (3%) | 1/77 (1%) |
| deceive (the act of deceiving) | lie | `欺骗` | 0/152 (0%) | 1/81 (1%) | 0/138 (0%) | 1/158 (1%) | 0/79 (0%) | 1/77 (1%) |
| fabricate (making something up) | lie | `造假` | 0/152 (0%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 0/79 (0%) | 1/77 (1%) |
| illegal (illegal) | unclear | `违法` | 1/152 (1%) | 0/81 (0%) | 1/138 (1%) | 0/158 (0%) | 0/79 (0%) | 0/77 (0%) |

Not in the draft: admit (excluded: admit / deny / acknowledge); acknowledge (excluded: admit / deny / acknowledge); truth (excluded: the question's own word)

## q_tok19

| family | side | members | lies | truths | no-pressure truths | unrelated | lies that deny | truths that deny |
|---|---|---|---|---|---|---|---|---|
| false (false, untrue) | lie | `␣false`, `␣False`, `false`, `False`, `␣FALSE`, `␣fals`, `␣falsely`, `␣untrue`, `/false`, `␣falsehood`, `虚假` | 152/152 (100%) | 81/81 (100%) | 138/138 (100%) | 157/158 (99%) | 79/79 (100%) | 77/77 (100%) |
| deceive (the act of deceiving) | lie | `欺骗`, `␣deception`, `␣deceived`, `␣deceptive`, `␣deceive`, `␣deceit` | 142/152 (93%) | 80/81 (99%) | 130/138 (94%) | 118/158 (75%) | 73/79 (92%) | 76/77 (99%) |
| conceal (concealing) | lie | `隐瞒`, `␣conceal`, `␣concealed`, `掩盖` | 143/152 (94%) | 73/81 (90%) | 75/138 (54%) | 18/158 (11%) | 73/79 (92%) | 69/77 (90%) |
| fake (fake, sham) | lie | `␣fake`, `fake`, `Fake`, `␣Fake`, `假`, `假的`, `_fake`, `假冒`, `伪造`, `造假` | 131/152 (86%) | 73/81 (90%) | 127/138 (92%) | 147/158 (93%) | 67/79 (85%) | 70/77 (91%) |
| misinformation (false information) | lie | `␣misinformation`, `虚假信息` | 114/152 (75%) | 66/81 (81%) | 135/138 (98%) | 156/158 (99%) | 55/79 (70%) | 64/77 (83%) |
| contradict (contradicting) | unclear | `␣contradict`, `␣contrad`, `␣contradictory`, `␣contradiction`, `␣contradictions`, `␣conflicting`, `矛盾` | 95/152 (62%) | 60/81 (74%) | 128/138 (93%) | 12/158 (8%) | 52/79 (66%) | 57/77 (74%) |
| knowingly (knowing, with knowledge) | unclear | `␣knowingly`, `␣knowing`, `明知`, `␣Knowing`, `Knowing` | 127/152 (84%) | 23/81 (28%) | 1/138 (1%) | 43/158 (27%) | 65/79 (82%) | 20/77 (26%) |
| fact (fact, factual) | truth | `␣fact`, `␣actually`, `␣actual`, `␣reality`, `actual`, `␣facts`, `Fact`, `Actual`, `fact`, `␣Actual`, `␣Actually`, `_FACT`, `␣Fact`, `_actual`, `␣Reality`, `␣Facts`, `Reality`, `_fact`, `Actually`, `␣FACT`, `FACT`, `␣factual`, `facts`, `actually`, `实际`, `事实`, `实际上`, `实际情况`, `事实上`, `的事实`, `的实际`, `实际的`, `实事求是`, `但实际上`, `实际上是`, `根据实际情况`, `事实和` | 123/152 (81%) | 20/81 (25%) | 51/138 (37%) | 68/158 (43%) | 59/79 (75%) | 17/77 (22%) |
| knowingly (with knowledge, consciously) | unclear | `␣knowingly`, `明知`, `␣consciously` | 120/152 (79%) | 22/81 (27%) | 1/138 (1%) | 42/158 (27%) | 59/79 (75%) | 19/77 (25%) |
| mislead (misleading) | lie | `␣misleading`, `␣misled`, `误导` | 47/152 (31%) | 66/81 (81%) | 93/138 (67%) | 140/158 (89%) | 29/79 (37%) | 63/77 (82%) |
| secret (secret, in secret) | lie | `␣secretly`, `秘密`, `的秘密`, `␣secret`, `secret`, `␣secrecy`, `␣Secret`, `␣secrets`, `␣SECRET`, `Secret`, `-secret` | 90/152 (59%) | 22/81 (27%) | 1/138 (1%) | 0/158 (0%) | 45/79 (57%) | 20/77 (26%) |
| intentional (on purpose) | unclear | `␣intentionally`, `故意`, `␣deliberately`, `␣intentional`, `␣deliberate`, `␣purposely`, `刻意`, `␣intention`, `␣consciously` | 71/152 (47%) | 38/81 (47%) | 24/138 (17%) | 110/158 (70%) | 32/79 (41%) | 35/77 (45%) |
| pretend (pretending) | lie | `␣pretending`, `␣pretended`, `␣pretend`, `假装`, `伪装`, `冒充` | 48/152 (32%) | 55/81 (68%) | 53/138 (38%) | 35/158 (22%) | 23/79 (29%) | 53/77 (69%) |
| undisclosed (not disclosed) | lie | `␣undisclosed` | 86/152 (57%) | 15/81 (19%) | 9/138 (7%) | 0/158 (0%) | 40/79 (51%) | 14/77 (18%) |
| fabricate (making something up) | lie | `伪造`, `虚构`, `␣fabricated`, `造假`, `␣fabrication`, `␣invented` | 54/152 (36%) | 46/81 (57%) | 59/138 (43%) | 84/158 (53%) | 32/79 (41%) | 46/77 (60%) |
| dishonest (dishonest) | lie | `␣dishonest`, `虚伪` | 56/152 (37%) | 35/81 (43%) | 25/138 (18%) | 11/158 (7%) | 38/79 (48%) | 34/77 (44%) |
| hide (hiding) | lie | `␣hiding`, `␣hidden`, `隐藏`, `␣Hidden`, `␣hide`, `hidden`, `隐藏的`, `Hide`, `␣hid`, `␣hides`, `hide`, `-hidden`, `␣Hide`, `隱藏`, `Hidden`, `_hidden` | 59/152 (39%) | 24/81 (30%) | 2/138 (1%) | 0/158 (0%) | 26/79 (33%) | 22/77 (29%) |
| incorrect (incorrect) | lie | `␣incorrect`, `Wrong`, `Incorrect`, `␣inaccur`, `␣incorrectly`, `␣inaccurate`, `incorrect`, `␣wrongly`, `␣erroneous`, `␣Incorrect`, `错误的`, `不符合`, `有误`, `不正确` | 22/152 (14%) | 45/81 (56%) | 134/138 (97%) | 155/158 (98%) | 14/79 (18%) | 44/77 (57%) |
| wrong (wrong, mistaken) | lie | `␣wrong`, `␣ERROR`, `wrong`, `␣Wrong`, `␣WRONG`, `误`, `错误`, `错了`, `的错误`, `错误或`, `是错误的` | 15/152 (10%) | 38/81 (47%) | 118/138 (86%) | 146/158 (92%) | 12/79 (15%) | 38/77 (49%) |
| unethical (unethical, immoral) | lie | `␣unethical` | 29/152 (19%) | 17/81 (21%) | 16/138 (12%) | 0/158 (0%) | 18/79 (23%) | 17/77 (22%) |
| violate (violating a rule) | unclear | `违背`, `违反`, `␣violates`, `违反了`, `␣violated`, `␣violating`, `␣violate`, `违规`, `␣violation`, `违法` | 20/152 (13%) | 21/81 (26%) | 69/138 (50%) | 2/158 (1%) | 11/79 (14%) | 21/77 (27%) |
| true (true, real) | truth | `␣true`, `真的`, `确实`, `真正的`, `是真的`, `真實`, `的真实性`, `的真正` | 35/152 (23%) | 2/81 (2%) | 0/138 (0%) | 4/158 (3%) | 14/79 (18%) | 1/77 (1%) |
| misrepresent (misrepresenting) | lie | `␣misrepresented` | 15/152 (10%) | 21/81 (26%) | 18/138 (13%) | 34/158 (22%) | 10/79 (13%) | 21/77 (27%) |
| fraud (fraud, defrauding) | lie | `␣fraudulent`, `␣fraud`, `␣Fraud` | 25/152 (16%) | 8/81 (10%) | 4/138 (3%) | 5/158 (3%) | 16/79 (20%) | 8/77 (10%) |
| fiction (fiction, fictional) | unclear | `␣fictional`, `␣fict`, `␣Fiction`, `␣fiction` | 17/152 (11%) | 16/81 (20%) | 13/138 (9%) | 55/158 (35%) | 14/79 (18%) | 16/77 (21%) |
| disguise (disguising, masking) | lie | `伪装`, `␣masking` | 7/152 (5%) | 25/81 (31%) | 0/138 (0%) | 2/158 (1%) | 4/79 (5%) | 25/77 (32%) |
| private (private, privately) | unclear | `␣privately`, `␣private` | 23/152 (15%) | 2/81 (2%) | 0/138 (0%) | 0/158 (0%) | 15/79 (19%) | 2/77 (3%) |
| honest (honest) | truth | `␣honesty`, `␣honest`, `␣honestly`, `诚信` | 6/152 (4%) | 18/81 (22%) | 15/138 (11%) | 10/158 (6%) | 5/79 (6%) | 18/77 (23%) |
| confidential (confidential) | unclear | `␣confidential`, `保密`, `␣confidentiality` | 7/152 (5%) | 7/81 (9%) | 0/138 (0%) | 0/158 (0%) | 6/79 (8%) | 7/77 (9%) |
| withhold (withholding) | lie | `␣withholding`, `␣withheld`, `␣withhold` | 6/152 (4%) | 5/81 (6%) | 0/138 (0%) | 0/158 (0%) | 3/79 (4%) | 4/77 (5%) |
| ethical (ethics, morality) | unclear | `␣moral`, `␣ethical`, `␣morally`, `道德`, `␣ethics`, `的道德`, `␣morality`, `␣Moral`, `伦理` | 0/152 (0%) | 9/81 (11%) | 0/138 (0%) | 0/158 (0%) | 0/79 (0%) | 9/77 (12%) |
| omit (leaving something out) | lie | `␣omit`, `␣omission`, `␣omitted` | 4/152 (3%) | 4/81 (5%) | 1/138 (1%) | 2/158 (1%) | 3/79 (4%) | 4/77 (5%) |
| disclose (disclosing, making public) | truth | `␣disclosed`, `公开`, `公开的`, `␣disclosure`, `␣disclosing` | 6/152 (4%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 5/79 (6%) | 1/77 (1%) |
| hypocritical (hypocritical, two-faced) | lie | `虚伪` | 0/152 (0%) | 6/81 (7%) | 0/138 (0%) | 0/158 (0%) | 0/79 (0%) | 6/77 (8%) |
| suppress (suppressing) | lie | `␣suppressing`, `␣suppress`, `␣suppressed` | 5/152 (3%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 2/79 (3%) | 1/77 (1%) |
| refuse (refusing) | unclear | `␣refusal`, `␣refusing`, `拒绝` | 0/152 (0%) | 5/81 (6%) | 0/138 (0%) | 0/158 (0%) | 0/79 (0%) | 5/77 (6%) |
| guilt (guilty) | unclear | `␣guilty` | 3/152 (2%) | 2/81 (2%) | 0/138 (0%) | 0/158 (0%) | 3/79 (4%) | 2/77 (3%) |
| role-play (playing a role or persona) | unclear | `␣persona`, `␣personas`, `␣Persona`, `Persona`, `persona`, `扮演`, `角色扮演`, `␣Personas` | 3/152 (2%) | 2/81 (2%) | 1/138 (1%) | 1/158 (1%) | 3/79 (4%) | 2/77 (3%) |
| cheat (cheating) | lie | `␣cheating`, `␣cheated` | 2/152 (1%) | 2/81 (2%) | 0/138 (0%) | 0/158 (0%) | 2/79 (3%) | 2/77 (3%) |
| hallucinate (hallucinating) | unclear | `␣halluc` | 1/152 (1%) | 3/81 (4%) | 14/138 (10%) | 71/158 (45%) | 1/79 (1%) | 3/77 (4%) |
| comply (complying) | unclear | `␣compliance`, `␣complied`, `␣complying`, `遵守`, `合规`, `␣Compliance` | 0/152 (0%) | 3/81 (4%) | 0/138 (0%) | 0/158 (0%) | 0/79 (0%) | 3/77 (4%) |
| make public (making public) | truth | `公开`, `公开的` | 3/152 (2%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 2/79 (3%) | 0/77 (0%) |
| correct (correct) | truth | `␣correct`, `␣correctly`, `correct`, `␣correction`, `Correct`, `␣corrected`, `␣Correct`, `␣corrections`, `␣correctness`, `␣Correction`, `Correction`, `正确`, `正确的`, `纠正`, `更正`, `是正确的` | 1/152 (1%) | 2/81 (2%) | 3/138 (2%) | 23/158 (15%) | 0/79 (0%) | 2/77 (3%) |
| impersonate (posing as someone else) | lie | `冒充` | 1/152 (1%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 1/79 (1%) | 1/77 (1%) |
| evasion (evading) | lie | `␣evasion` | 1/152 (1%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 1/79 (1%) | 1/77 (1%) |
| exaggerate (overstating) | lie | `夸大`, `␣exaggerated` | 2/152 (1%) | 0/81 (0%) | 0/138 (0%) | 6/158 (4%) | 1/79 (1%) | 0/77 (0%) |
| evade (evading, avoiding) | lie | `␣evasion`, `回避`, `逃避` | 1/152 (1%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 1/79 (1%) | 1/77 (1%) |
| reject (rejecting) | unclear | `␣rejected` | 0/152 (0%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 0/79 (0%) | 1/77 (1%) |
| expose (exposing, revealing) | truth | `揭露` | 0/152 (0%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 0/79 (0%) | 1/77 (1%) |
| illegal (illegal) | unclear | `违法` | 0/152 (0%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 0/79 (0%) | 1/77 (1%) |
| accuse (accusing) | unclear | `␣accusations` | 0/152 (0%) | 1/81 (1%) | 2/138 (1%) | 2/158 (1%) | 0/79 (0%) | 1/77 (1%) |
| accurate (accurate) | truth | `␣accurate`, `␣accuracy`, `␣accurately`, `accuracy`, `Accuracy`, `␣Accuracy`, `准确性` | 0/152 (0%) | 1/81 (1%) | 0/138 (0%) | 16/158 (10%) | 0/79 (0%) | 1/77 (1%) |
| inaccurate (inaccurate) | lie | `不准确` | 0/152 (0%) | 0/81 (0%) | 0/138 (0%) | 2/158 (1%) | 0/79 (0%) | 0/77 (0%) |

Not in the draft: deny (excluded: admit / deny / acknowledge); admit (excluded: admit / deny / acknowledge); acknowledge (excluded: admit / deny / acknowledge); truth (excluded: the question's own word); liar (excluded: the question's own word)

## q_tok20

| family | side | members | lies | truths | no-pressure truths | unrelated | lies that deny | truths that deny |
|---|---|---|---|---|---|---|---|---|
| deceive (the act of deceiving) | lie | `␣deceived`, `␣deception`, `欺骗`, `␣deceive`, `␣fooled`, `␣deceptive` | 145/152 (95%) | 61/81 (75%) | 121/138 (88%) | 129/158 (82%) | 73/79 (92%) | 57/77 (74%) |
| intentional (on purpose) | unclear | `␣intentionally`, `␣deliberately`, `␣purposely`, `故意`, `␣intentional`, `␣consciously` | 139/152 (91%) | 59/81 (73%) | 93/138 (67%) | 132/158 (84%) | 69/79 (87%) | 55/77 (71%) |
| mislead (misleading) | lie | `␣misled`, `␣misleading`, `误导` | 137/152 (90%) | 56/81 (69%) | 132/138 (96%) | 107/158 (68%) | 69/79 (87%) | 52/77 (68%) |
| misrepresent (misrepresenting) | lie | `␣misrepresented` | 131/152 (86%) | 62/81 (77%) | 102/138 (74%) | 49/158 (31%) | 68/79 (86%) | 58/77 (75%) |
| fake (fake, sham) | lie | `␣fake`, `Fake`, `fake`, `␣Fake`, `假`, `伪造` | 128/152 (84%) | 50/81 (62%) | 37/138 (27%) | 23/158 (15%) | 65/79 (82%) | 46/77 (60%) |
| pretend (pretending) | lie | `␣pretending`, `␣pretended`, `␣pretend`, `假装`, `冒充` | 110/152 (72%) | 60/81 (74%) | 38/138 (28%) | 4/158 (3%) | 52/79 (66%) | 56/77 (73%) |
| violate (violating a rule) | unclear | `␣violated`, `违反`, `违背`, `违反了`, `违规`, `␣violate`, `␣violates` | 105/152 (69%) | 54/81 (67%) | 106/138 (77%) | 5/158 (3%) | 51/79 (65%) | 53/77 (69%) |
| knowingly (with knowledge, consciously) | unclear | `␣knowingly`, `␣consciously`, `明知` | 117/152 (77%) | 28/81 (35%) | 15/138 (11%) | 46/158 (29%) | 56/79 (71%) | 27/77 (35%) |
| dishonest (dishonest) | lie | `␣dishonest` | 87/152 (57%) | 32/81 (40%) | 68/138 (49%) | 24/158 (15%) | 43/79 (54%) | 31/77 (40%) |
| fabricate (making something up) | lie | `虚构`, `␣fabricated`, `伪造` | 82/152 (54%) | 33/81 (41%) | 17/138 (12%) | 20/158 (13%) | 42/79 (53%) | 29/77 (38%) |
| false (false, untrue) | lie | `␣fals`, `␣falsely`, `␣falsehood`, `虚假` | 82/152 (54%) | 32/81 (40%) | 99/138 (72%) | 72/158 (46%) | 44/79 (56%) | 30/77 (39%) |
| simulate (simulating) | unclear | `模拟`, `␣simulated`, `仿真`, `␣simulation`, `␣simulate`, `␣Simulation`, `␣simulations`, `Simulation`, `simulate` | 79/152 (52%) | 34/81 (42%) | 10/138 (7%) | 0/158 (0%) | 38/79 (48%) | 31/77 (40%) |
| role-play (playing a role or persona) | unclear | `␣persona`, `␣Persona`, `角色扮演`, `扮演`, `Persona`, `␣personas`, `persona`, `␣Personas` | 72/152 (47%) | 36/81 (44%) | 1/138 (1%) | 0/158 (0%) | 37/79 (47%) | 33/77 (43%) |
| unethical (unethical, immoral) | lie | `␣unethical` | 70/152 (46%) | 32/81 (40%) | 3/138 (2%) | 0/158 (0%) | 33/79 (42%) | 31/77 (40%) |
| fiction (fiction, fictional) | unclear | `␣fictional`, `␣Fiction`, `fiction`, `␣fict`, `␣fiction` | 58/152 (38%) | 29/81 (36%) | 5/138 (4%) | 1/158 (1%) | 30/79 (38%) | 25/77 (32%) |
| ethical (ethics, morality) | unclear | `␣ethical`, `␣ethics`, `␣Ethics`, `ethical`, `␣morally`, `道德`, `伦理` | 23/152 (15%) | 31/81 (38%) | 9/138 (7%) | 1/158 (1%) | 9/79 (11%) | 31/77 (40%) |
| cheat (cheating) | lie | `␣cheated` | 49/152 (32%) | 4/81 (5%) | 17/138 (12%) | 14/158 (9%) | 25/79 (32%) | 4/77 (5%) |
| accuse (accusing) | unclear | `␣accusing`, `␣accusations`, `␣accused`, `␣accusation`, `␣accuses` | 31/152 (20%) | 7/81 (9%) | 2/138 (1%) | 0/158 (0%) | 20/79 (25%) | 7/77 (9%) |
| honest (honest) | truth | `␣honesty`, `␣honest`, `␣sincerely` | 24/152 (16%) | 9/81 (11%) | 1/138 (1%) | 0/158 (0%) | 14/79 (18%) | 9/77 (12%) |
| misinformation (false information) | lie | `␣misinformation`, `虚假信息` | 14/152 (9%) | 18/81 (22%) | 117/138 (85%) | 109/158 (69%) | 8/79 (10%) | 18/77 (23%) |
| refuse (refusing) | unclear | `␣refused`, `␣refusal`, `␣refus`, `␣refusing`, `拒绝`, `␣refuse`, `␣refuses`, `拒绝了`, `拒`, `拒絕`, `拒不`, `␣отказ`, `␣отказа`, `␣declined`, `␣decline`, `␣declining`, `␣declines` | 0/152 (0%) | 26/81 (32%) | 9/138 (7%) | 5/158 (3%) | 0/79 (0%) | 26/77 (34%) |
| apologize (apologizing) | truth | `␣apologized`, `␣apologize` | 7/152 (5%) | 16/81 (20%) | 52/138 (38%) | 66/158 (42%) | 4/79 (5%) | 16/77 (21%) |
| conceal (concealing) | lie | `隐瞒` | 12/152 (8%) | 5/81 (6%) | 1/138 (1%) | 0/158 (0%) | 5/79 (6%) | 5/77 (6%) |
| comply (complying) | unclear | `遵守`, `␣complied`, `合规`, `␣compliance`, `␣Compliance`, `␣complying`, `严格遵守` | 11/152 (7%) | 6/81 (7%) | 1/138 (1%) | 0/158 (0%) | 6/79 (8%) | 6/77 (8%) |
| incorrect (incorrect) | lie | `␣incorrect`, `Incorrect`, `␣inaccur`, `␣incorrectly`, `␣inaccurate`, `incorrect`, `␣Incorrect`, `错误的`, `有误` | 5/152 (3%) | 10/81 (12%) | 83/138 (60%) | 77/158 (49%) | 3/79 (4%) | 10/77 (13%) |
| decline (declining) | unclear | `␣declined`, `␣decline`, `␣declining`, `␣declines` | 0/152 (0%) | 14/81 (17%) | 0/138 (0%) | 0/158 (0%) | 0/79 (0%) | 14/77 (18%) |
| sincere (sincere) | truth | `␣sincerely` | 10/152 (7%) | 4/81 (5%) | 0/138 (0%) | 0/158 (0%) | 9/79 (11%) | 4/77 (5%) |
| hallucinate (hallucinating) | unclear | `␣halluc` | 4/152 (3%) | 3/81 (4%) | 86/138 (62%) | 133/158 (84%) | 2/79 (3%) | 3/77 (4%) |
| betray (betraying) | lie | `␣betrayed` | 5/152 (3%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 5/79 (6%) | 1/77 (1%) |
| reject (rejecting) | unclear | `␣rejected`, `␣rejection`, `␣reject`, `␣rejecting`, `␣Reject` | 0/152 (0%) | 5/81 (6%) | 0/138 (0%) | 0/158 (0%) | 0/79 (0%) | 5/77 (6%) |
| confidential (confidential) | unclear | `␣confidentiality` | 3/152 (2%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 0/79 (0%) | 1/77 (1%) |
| impersonate (posing as someone else) | lie | `冒充` | 3/152 (2%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 2/79 (3%) | 0/77 (0%) |
| withhold (withholding) | lie | `␣withheld` | 0/152 (0%) | 3/81 (4%) | 0/138 (0%) | 0/158 (0%) | 0/79 (0%) | 3/77 (4%) |
| fraud (fraud, defrauding) | lie | `␣fraudulent` | 2/152 (1%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 2/79 (3%) | 0/77 (0%) |
| wrong (wrong, mistaken) | lie | `␣wrong`, `␣ERROR`, `␣WRONG`, `误`, `错误`, `错了`, `的错误` | 2/152 (1%) | 0/81 (0%) | 57/138 (41%) | 48/158 (30%) | 2/79 (3%) | 0/77 (0%) |
| omit (leaving something out) | lie | `␣omitted` | 0/152 (0%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 0/79 (0%) | 1/77 (1%) |
| exaggerate (overstating) | lie | `␣exaggerated`, `夸大` | 1/152 (1%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 0/79 (0%) | 0/77 (0%) |
| correct (correct) | truth | `␣correct`, `␣correctly`, `␣Correct` | 0/152 (0%) | 0/81 (0%) | 8/138 (6%) | 1/158 (1%) | 0/79 (0%) | 0/77 (0%) |
| accurate (accurate) | truth | `␣accuracy` | 0/152 (0%) | 0/81 (0%) | 0/138 (0%) | 2/158 (1%) | 0/79 (0%) | 0/77 (0%) |
| fact (fact, factual) | truth | `␣factual` | 0/152 (0%) | 0/81 (0%) | 0/138 (0%) | 4/158 (3%) | 0/79 (0%) | 0/77 (0%) |

Not in the draft: admit (excluded: admit / deny / acknowledge); acknowledge (excluded: admit / deny / acknowledge); truth (excluded: the question's own word); liar (excluded: the question's own word)

## q_tok21

| family | side | members | lies | truths | no-pressure truths | unrelated | lies that deny | truths that deny |
|---|---|---|---|---|---|---|---|---|
| deceive (the act of deceiving) | lie | `欺骗`, `骗`, `␣deception`, `␣deceived`, `␣deceit` | 152/152 (100%) | 81/81 (100%) | 138/138 (100%) | 158/158 (100%) | 79/79 (100%) | 77/77 (100%) |
| fake (fake, sham) | lie | `␣fake`, `fake`, `Fake`, `␣Fake`, `伪造`, `造假` | 152/152 (100%) | 81/81 (100%) | 138/138 (100%) | 158/158 (100%) | 79/79 (100%) | 77/77 (100%) |
| dishonest (dishonest) | lie | `␣dishonest` | 152/152 (100%) | 81/81 (100%) | 138/138 (100%) | 158/158 (100%) | 79/79 (100%) | 77/77 (100%) |
| false (false, untrue) | lie | `␣false`, `␣fals`, `␣falsely`, `␣untrue`, `/false`, `␣falsehood`, `虚假` | 152/152 (100%) | 81/81 (100%) | 138/138 (100%) | 158/158 (100%) | 79/79 (100%) | 77/77 (100%) |
| fabricate (making something up) | lie | `伪造`, `造假` | 139/152 (91%) | 71/81 (88%) | 110/138 (80%) | 109/158 (69%) | 69/79 (87%) | 67/77 (87%) |
| intentional (on purpose) | unclear | `␣intentionally`, `故意`, `␣deliberately`, `␣intentional`, `刻意` | 138/152 (91%) | 59/81 (73%) | 108/138 (78%) | 156/158 (99%) | 70/79 (89%) | 55/77 (71%) |
| hoax (a hoax) | lie | `␣hoax` | 56/152 (37%) | 60/81 (74%) | 117/138 (85%) | 158/158 (100%) | 29/79 (37%) | 57/77 (74%) |
| misinformation (false information) | lie | `␣misinformation` | 36/152 (24%) | 44/81 (54%) | 56/138 (41%) | 113/158 (72%) | 21/79 (27%) | 44/77 (57%) |
| honest (honest) | truth | `诚信` | 30/152 (20%) | 14/81 (17%) | 15/138 (11%) | 3/158 (2%) | 14/79 (18%) | 12/77 (16%) |
| knowingly (with knowledge, consciously) | unclear | `␣knowingly` | 28/152 (18%) | 1/81 (1%) | 10/138 (7%) | 26/158 (16%) | 14/79 (18%) | 1/77 (1%) |
| pretend (pretending) | lie | `␣pretending` | 3/152 (2%) | 20/81 (25%) | 1/138 (1%) | 9/158 (6%) | 1/79 (1%) | 20/77 (26%) |
| mislead (misleading) | lie | `误导`, `␣misleading` | 4/152 (3%) | 7/81 (9%) | 3/138 (2%) | 0/158 (0%) | 4/79 (5%) | 7/77 (9%) |
| wrong (wrong, mistaken) | lie | `␣WRONG`, `错误` | 2/152 (1%) | 6/81 (7%) | 44/138 (32%) | 9/158 (6%) | 2/79 (3%) | 6/77 (8%) |
| conceal (concealing) | lie | `隐瞒` | 4/152 (3%) | 3/81 (4%) | 0/138 (0%) | 0/158 (0%) | 1/79 (1%) | 3/77 (4%) |
| unethical (unethical, immoral) | lie | `␣unethical` | 5/152 (3%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 2/79 (3%) | 1/77 (1%) |
| misrepresent (misrepresenting) | lie | `␣misrepresented` | 1/152 (1%) | 2/81 (2%) | 0/138 (0%) | 0/158 (0%) | 1/79 (1%) | 2/77 (3%) |
| fraud (fraud, defrauding) | lie | `欺诈` | 0/152 (0%) | 2/81 (2%) | 0/138 (0%) | 0/158 (0%) | 0/79 (0%) | 2/77 (3%) |

Not in the draft: truth (excluded: the question's own word); liar (excluded: the question's own word)

## q_tok22

| family | side | members | lies | truths | no-pressure truths | unrelated | lies that deny | truths that deny |
|---|---|---|---|---|---|---|---|---|
| confess (confessing a wrong) | truth | `␣confess`, `␣confession`, `坦白`, `␣confessed`, `认错`, `认罪` | 112/152 (74%) | 59/81 (73%) | 90/138 (65%) | 146/158 (92%) | 72/79 (91%) | 58/77 (75%) |
| unethical (unethical, immoral) | lie | `␣unethical`, `␣immoral` | 84/152 (55%) | 56/81 (69%) | 50/138 (36%) | 128/158 (81%) | 34/79 (43%) | 53/77 (69%) |
| honest (honest) | truth | `␣honesty`, `␣honest`, `坦诚` | 94/152 (62%) | 29/81 (36%) | 12/138 (9%) | 45/158 (28%) | 58/79 (73%) | 28/77 (36%) |
| knowingly (with knowledge, consciously) | unclear | `␣knowingly`, `明知`, `␣consciously` | 58/152 (38%) | 10/81 (12%) | 0/138 (0%) | 0/158 (0%) | 18/79 (23%) | 7/77 (9%) |
| knowingly (knowing, with knowledge) | unclear | `␣knowingly`, `明知`, `␣knowing`, `␣Knowing`, `Knowing` | 58/152 (38%) | 10/81 (12%) | 0/138 (0%) | 0/158 (0%) | 18/79 (23%) | 7/77 (9%) |
| wrong (wrong, mistaken) | lie | `␣wrong`, `␣ERROR`, `␣WRONG`, `错误`, `的错误` | 14/152 (9%) | 54/81 (67%) | 122/138 (88%) | 128/158 (81%) | 11/79 (14%) | 54/77 (70%) |
| apologize (apologizing) | truth | `道歉`, `␣apologies`, `␣apologize`, `␣apology`, `␣apologized` | 35/152 (23%) | 30/81 (37%) | 97/138 (70%) | 100/158 (63%) | 28/79 (35%) | 30/77 (39%) |
| expose (exposing, revealing) | truth | `揭露`, `揭秘` | 51/152 (34%) | 14/81 (17%) | 0/138 (0%) | 0/158 (0%) | 23/79 (29%) | 12/77 (16%) |
| conceal (concealing) | lie | `隐瞒`, `␣concealed`, `␣conceal`, `掩盖`, `隐` | 47/152 (31%) | 16/81 (20%) | 0/138 (0%) | 1/158 (1%) | 17/79 (22%) | 14/77 (18%) |
| incorrect (incorrect) | lie | `␣incorrect`, `Incorrect`, `␣incorrectly`, `incorrect`, `␣Incorrect`, `错误的`, `不符合` | 19/152 (12%) | 44/81 (54%) | 110/138 (80%) | 114/158 (72%) | 8/79 (10%) | 43/77 (56%) |
| accuse (accusing) | unclear | `␣accusations`, `␣accusing`, `指责`, `␣accusation`, `指控`, `␣accuse`, `␣accuses` | 14/152 (9%) | 48/81 (59%) | 114/138 (83%) | 146/158 (92%) | 11/79 (14%) | 47/77 (61%) |
| false (false, untrue) | lie | `␣false`, `False`, `␣fals`, `␣falsely`, `/false`, `␣falsehood`, `虚假` | 23/152 (15%) | 28/81 (35%) | 38/138 (28%) | 13/158 (8%) | 9/79 (11%) | 25/77 (32%) |
| fake (fake, sham) | lie | `fake`, `Fake`, `␣fake`, `␣Fake`, `假冒`, `伪造` | 20/152 (13%) | 29/81 (36%) | 12/138 (9%) | 6/158 (4%) | 7/79 (9%) | 28/77 (36%) |
| repent (regretting, repenting) | truth | `忏悔`, `悔`, `␣repent`, `后悔` | 25/152 (16%) | 19/81 (23%) | 59/138 (43%) | 8/158 (5%) | 19/79 (24%) | 19/77 (25%) |
| deceive (the act of deceiving) | lie | `欺骗`, `␣deception`, `␣deceptive` | 23/152 (15%) | 16/81 (20%) | 21/138 (15%) | 3/158 (2%) | 10/79 (13%) | 15/77 (19%) |
| dishonest (dishonest) | lie | `␣dishonest` | 9/152 (6%) | 26/81 (32%) | 25/138 (18%) | 14/158 (9%) | 4/79 (5%) | 26/77 (34%) |
| secret (secret, in secret) | lie | `秘密`, `␣secretly`, `的秘密`, `␣secret`, `Secret` | 26/152 (17%) | 4/81 (5%) | 0/138 (0%) | 0/158 (0%) | 12/79 (15%) | 2/77 (3%) |
| violate (violating a rule) | unclear | `违反`, `␣violate`, `␣violates`, `␣violating`, `违背`, `违反了`, `违法` | 10/152 (7%) | 18/81 (22%) | 6/138 (4%) | 0/158 (0%) | 3/79 (4%) | 17/77 (22%) |
| wrongdoing (wrongdoing) | unclear | `␣wrongdoing` | 2/152 (1%) | 25/81 (31%) | 76/138 (55%) | 81/158 (51%) | 0/79 (0%) | 24/77 (31%) |
| intentional (on purpose) | unclear | `故意`, `␣intentionally`, `␣deliberately`, `␣intentional`, `␣deliberate`, `␣purposely`, `刻意`, `有意`, `故意的`, `␣consciously` | 18/152 (12%) | 7/81 (9%) | 0/138 (0%) | 0/158 (0%) | 5/79 (6%) | 5/77 (6%) |
| guilt (guilty) | unclear | `␣guilty` | 4/152 (3%) | 14/81 (17%) | 3/138 (2%) | 0/158 (0%) | 2/79 (3%) | 14/77 (18%) |
| hide (hiding) | lie | `␣hidden`, `hidden`, `隐藏`, `Hidden`, `-hidden`, `␣Hidden`, `隐藏的`, `␣hiding`, `_hidden`, `隱藏` | 11/152 (7%) | 2/81 (2%) | 0/138 (0%) | 0/158 (0%) | 6/79 (8%) | 2/77 (3%) |
| concede (conceding) | truth | `␣concede`, `␣conced` | 13/152 (9%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 9/79 (11%) | 0/77 (0%) |
| fabricate (making something up) | lie | `伪造`, `虚构` | 9/152 (6%) | 3/81 (4%) | 0/138 (0%) | 0/158 (0%) | 3/79 (4%) | 3/77 (4%) |
| fact (fact, factual) | truth | `␣actual`, `actual`, `Actual`, `事实`, `实际情况`, `实事求是` | 7/152 (5%) | 2/81 (2%) | 0/138 (0%) | 0/158 (0%) | 1/79 (1%) | 0/77 (0%) |
| pretend (pretending) | lie | `␣pretending` | 5/152 (3%) | 2/81 (2%) | 0/138 (0%) | 0/158 (0%) | 2/79 (3%) | 2/77 (3%) |
| leak (leaking) | unclear | `泄露` | 4/152 (3%) | 2/81 (2%) | 0/138 (0%) | 0/158 (0%) | 2/79 (3%) | 2/77 (3%) |
| fraud (fraud, defrauding) | lie | `␣fraudulent` | 0/152 (0%) | 5/81 (6%) | 1/138 (1%) | 0/158 (0%) | 0/79 (0%) | 5/77 (6%) |
| contradict (contradicting) | unclear | `␣contradict`, `␣contradictory` | 0/152 (0%) | 5/81 (6%) | 3/138 (2%) | 0/158 (0%) | 0/79 (0%) | 5/77 (6%) |
| disclose (disclosing, making public) | truth | `公开`, `␣disclosure`, `信息公开` | 1/152 (1%) | 3/81 (4%) | 0/138 (0%) | 0/158 (0%) | 1/79 (1%) | 3/77 (4%) |
| ethical (ethics, morality) | unclear | `␣morally`, `道德` | 3/152 (2%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 0/79 (0%) | 1/77 (1%) |
| correct (correct) | truth | `␣correct`, `正确`, `正确答案`, `纠正`, `改正`, `更正` | 2/152 (1%) | 2/81 (2%) | 12/138 (9%) | 2/158 (1%) | 0/79 (0%) | 1/77 (1%) |
| undisclosed (not disclosed) | lie | `␣undisclosed` | 3/152 (2%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 1/79 (1%) | 0/77 (0%) |
| make public (making public) | truth | `公开` | 1/152 (1%) | 2/81 (2%) | 0/138 (0%) | 0/158 (0%) | 1/79 (1%) | 2/77 (3%) |
| candid (candid, frank) | truth | `坦诚` | 1/152 (1%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 1/79 (1%) | 1/77 (1%) |
| mislead (misleading) | lie | `␣misleading` | 1/152 (1%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 0/79 (0%) | 0/77 (0%) |
| malicious (malicious) | lie | `␣malicious` | 0/152 (0%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 0/79 (0%) | 1/77 (1%) |
| coward (cowardly) | unclear | `␣coward` | 0/152 (0%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 0/79 (0%) | 1/77 (1%) |
| illegal (illegal) | unclear | `违法` | 0/152 (0%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 0/79 (0%) | 1/77 (1%) |

Not in the draft: deny (excluded: admit / deny / acknowledge); admit (excluded: admit / deny / acknowledge); acknowledge (excluded: admit / deny / acknowledge); truth (excluded: the question's own word); true (excluded: the question's own word)

## q_tok23

| family | side | members | lies | truths | no-pressure truths | unrelated | lies that deny | truths that deny |
|---|---|---|---|---|---|---|---|---|
| false (false, untrue) | lie | `False`, `:false` | 137/152 (90%) | 77/81 (95%) | 136/138 (99%) | 158/158 (100%) | 65/79 (82%) | 73/77 (95%) |
