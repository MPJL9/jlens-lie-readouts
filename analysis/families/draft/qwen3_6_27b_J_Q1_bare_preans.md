# Draft families: qwen3.6-27b, J-lens, part Q1_bare, group preans

Written by `scripts/apply_family_decisions.py` (2026-10-01; draft, not frozen). Counts are `present / transcripts (share)`
on the build split.

## preans_slot0

| family | side | members | lies | truths | no-pressure truths | unrelated | lies that deny | truths that deny |
|---|---|---|---|---|---|---|---|---|
| critique (criticizing) | unclear | `␣critique`, `批判`, `␣critiques`, `␣critic`, `批评`, `␣critica`, `␣criticism`, `␣crítico`, `␣crítica`, `␣kritik`, `␣críticos` | 132/152 (87%) | 65/81 (80%) | 117/138 (85%) | 19/158 (12%) | 40/53 (75%) | 58/74 (78%) |
| self-reflection (examining oneself) | unclear | `反思`, `自省`, `自查`, `自检`, `自评` | 42/152 (28%) | 27/81 (33%) | 72/138 (52%) | 34/158 (22%) | 9/53 (17%) | 24/74 (32%) |
| accusation (accusing) | unclear | `指控`, `␣accusation`, `␣accusations`, `␣accus`, `␣accusing`, `␣accuse`, `指责`, `␣acus`, `␣acusa` | 8/152 (5%) | 3/81 (4%) | 0/138 (0%) | 0/158 (0%) | 5/53 (9%) | 3/74 (4%) |

Not in the draft: acknowledge (excluded: admit / deny / acknowledge); violate (held back: no undisputed member left); admit (excluded: admit / deny / acknowledge)

## preans_slot1

| family | side | members | lies | truths | no-pressure truths | unrelated | lies that deny | truths that deny |
|---|---|---|---|---|---|---|---|---|
| truthful (telling the truth) | truth | `␣truthful`, `如实`, `实事求是`, `如实供述` | 142/152 (93%) | 68/81 (84%) | 122/138 (88%) | 65/158 (41%) | 50/53 (94%) | 62/74 (84%) |
| false (false, untrue) | lie | `␣false`, `␣False`, `false`, `False`, `␣FALSE`, `␣fals`, `␣falsely`, `␣untrue`, `/false`, `␣falsehood`, `假`, `虚假`, `假的`, `真假`, `不实`, `真伪` | 149/152 (98%) | 49/81 (60%) | 96/138 (70%) | 44/158 (28%) | 50/53 (94%) | 43/74 (58%) |
| mislead (leading someone to a wrong belief) | lie | `␣misleading`, `误导`, `␣misled`, `误导性` | 147/152 (97%) | 49/81 (60%) | 76/138 (55%) | 49/158 (31%) | 50/53 (94%) | 43/74 (58%) |
| conceal / hide (keeping information hidden) | lie | `隐瞒`, `掩盖`, `␣conceal`, `␣masking`, `␣hiding`, `␣concealed`, `Hide`, `_hide`, `隐藏`, `hide`, `␣hide`, `␣hid`, `␣hides`, `-hide`, `掩饰`, `掩护`, `遮盖`, `遮蔽`, `瞒`, `隐匿`, `隐` | 141/152 (93%) | 54/81 (67%) | 86/138 (62%) | 6/158 (4%) | 47/53 (89%) | 49/74 (66%) |
| lie (telling a lie) | lie | `谎言`, `说谎`, `谎`, `撒谎`, `␣거짓`, `␣lied`, `␣mentira`, `␣lying`, `␣lie`, `␣liar`, `␣lies`, `␣Lies`, `␣Lie`, `lies` | 145/152 (95%) | 34/81 (42%) | 43/138 (31%) | 0/158 (0%) | 46/53 (87%) | 30/74 (41%) |
| misinformation (false information) | lie | `␣misinformation`, `虚假信息` | 141/152 (93%) | 30/81 (37%) | 91/138 (66%) | 47/158 (30%) | 44/53 (83%) | 25/74 (34%) |
| fake (fake, not genuine) | lie | `fake`, `Fake`, `␣fake`, `␣Fake`, `_fake`, `.fake`, `假冒` | 121/152 (80%) | 24/81 (30%) | 80/138 (58%) | 52/158 (33%) | 35/53 (66%) | 20/74 (27%) |
| misrepresent (giving a distorted account) | lie | `␣misrepresented` | 101/152 (66%) | 22/81 (27%) | 14/138 (10%) | 9/158 (6%) | 26/53 (49%) | 20/74 (27%) |
| misrepresent (misrepresent, distort) | lie | `␣misrepresented`, `␣distortion`, `␣distort` | 101/152 (66%) | 22/81 (27%) | 14/138 (10%) | 9/158 (6%) | 26/53 (49%) | 20/74 (27%) |
| fabricate (making something up) | lie | `伪造`, `虚构`, `造假`, `␣fabricated`, `弄虚作假`, `␣fabrication` | 94/152 (62%) | 19/81 (23%) | 76/138 (55%) | 56/158 (35%) | 29/53 (55%) | 16/74 (22%) |
| contradict (contradicting) | unclear | `␣contradict`, `␣contrad`, `␣contradictory`, `␣contradiction`, `␣contradictions`, `矛盾`, `矛盾的`, `␣contradd` | 56/152 (37%) | 26/81 (32%) | 43/138 (31%) | 8/158 (5%) | 25/53 (47%) | 23/74 (31%) |
| imply (implying, implicit) | unclear | `␣implicitly`, `␣implying`, `暗示`, `␣implicit`, `␣implied`, `隐含`, `␣imply`, `␣implication`, `␣implies`, `implicitly`, `␣IMPLIED`, `␣implications`, `implicit`, `Implicit`, `␣Implicit`, `␣implica` | 47/152 (31%) | 29/81 (36%) | 39/138 (28%) | 17/158 (11%) | 15/53 (28%) | 26/74 (35%) |
| intentional (doing it on purpose) | unclear | `␣intentionally`, `␣deliberately`, `故意`, `刻意`, `␣deliberate`, `␣knowingly`, `明知` | 59/152 (39%) | 7/81 (9%) | 5/138 (4%) | 3/158 (2%) | 19/53 (36%) | 4/74 (5%) |
| facts (the facts, what actually happened) | unclear | `␣factual`, `事实`, `␣facts`, `的事实`, `Fact`, `␣Facts`, `␣fact`, `␣Fact`, `facts`, `实际情况`, `fact`, `事实上`, `_fact`, `␣FACT`, `FACT`, `根据实际情况`, `事实和` | 28/152 (18%) | 32/81 (40%) | 108/138 (78%) | 78/158 (49%) | 15/53 (28%) | 31/74 (42%) |
| knowingly (knowing it, aware) | unclear | `␣knowingly`, `明知` | 57/152 (38%) | 1/81 (1%) | 3/138 (2%) | 0/158 (0%) | 19/53 (36%) | 0/74 (0%) |
| disclaimer (disclaimer) | unclear | `␣disclaimer`, `␣Disclaimer`, `Disclaimer`, `␣DISCLAIMER` | 12/152 (8%) | 42/81 (52%) | 37/138 (27%) | 34/158 (22%) | 9/53 (17%) | 42/74 (57%) |
| dishonest (not honest) | lie | `␣dishonest` | 41/152 (27%) | 2/81 (2%) | 0/138 (0%) | 0/158 (0%) | 17/53 (32%) | 1/74 (1%) |
| refuse (refusing) | unclear | `拒绝`, `␣refusal`, `␣refusing`, `␣refused`, `␣refuse`, `拒`, `␣refus`, `␣refuses`, `拒絕`, `拒绝了`, `␣отказ`, `␣отказа`, `拒不`, `␣menolak`, `␣declined`, `␣decline`, `␣declining`, `␣declines` | 10/152 (7%) | 33/81 (41%) | 13/138 (9%) | 4/158 (3%) | 7/53 (13%) | 33/74 (45%) |
| blame (blaming) | unclear | `␣blaming`, `␣blame`, `␣blames`, `␣blamed` | 37/152 (24%) | 5/81 (6%) | 0/138 (0%) | 0/158 (0%) | 10/53 (19%) | 3/74 (4%) |
| incorrect (incorrect) | lie | `␣incorrect`, `Incorrect`, `␣inaccur`, `␣incorrectly`, `␣inaccurate`, `incorrect`, `␣wrongly`, `␣erroneous`, `␣Incorrect`, `错误的`, `不符合`, `有误`, `不正确` | 26/152 (17%) | 16/81 (20%) | 23/138 (17%) | 62/158 (39%) | 11/53 (21%) | 13/74 (18%) |
| evade (evading) | lie | `回避`, `␣evasion`, `规避`, `␣evade`, `逃避`, `避开`, `␣dodge`, `␣deflect` | 22/152 (14%) | 19/81 (23%) | 4/138 (3%) | 0/158 (0%) | 10/53 (19%) | 19/74 (26%) |
| honest (honest) | truth | `␣honesty`, `诚实`, `␣honest`, `␣honestly`, `␣Honest` | 2/152 (1%) | 38/81 (47%) | 84/138 (61%) | 26/158 (16%) | 2/53 (4%) | 37/74 (50%) |
| ambiguous (ambiguous) | unclear | `␣ambiguous`, `␣ambiguity`, `␣ambigu`, `ambiguous`, `␣vague`, `含糊`, `模糊`, `␣vaguely` | 20/152 (13%) | 16/81 (20%) | 1/138 (1%) | 12/158 (8%) | 10/53 (19%) | 13/74 (18%) |
| violate (violating a rule or principle) | unclear | `违背`, `违反`, `␣violate`, `违反了`, `␣violation`, `␣violated`, `␣violating`, `␣violates`, `违规` | 25/152 (16%) | 6/81 (7%) | 10/138 (7%) | 2/158 (1%) | 8/53 (15%) | 5/74 (7%) |
| omit (leaving something out) | lie | `␣omit`, `␣omission`, `␣omitted`, `省略`, `omit`, `␣OMIT` | 19/152 (12%) | 9/81 (11%) | 2/138 (1%) | 1/158 (1%) | 6/53 (11%) | 9/74 (12%) |
| candid (candid, frank) | truth | `坦诚`, `直言`, `␣straightforward` | 0/152 (0%) | 28/81 (35%) | 60/138 (43%) | 67/158 (42%) | 0/53 (0%) | 27/74 (36%) |
| correct (correct) | truth | `␣correct`, `␣correctly`, `correct`, `␣correction`, `_correct`, `Correct`, `␣corrected`, `␣Correct`, `␣corrections`, `␣correctness`, `␣Correction`, `␣correcting`, `.correct`, `_correction`, `Correction`, `␣Corrections`, `␣corrective`, `正确`, `正确的`, `修正`, `纠错`, `正确答案`, `纠正`, `改正`, `的正确`, `更正`, `是正确的`, `正确地`, `是否正确` | 4/152 (3%) | 23/81 (28%) | 78/138 (57%) | 86/158 (54%) | 3/53 (6%) | 23/74 (31%) |
| reject (rejecting) | unclear | `␣rejecting`, `␣rejection`, `reject`, `␣reject`, `␣Reject`, `Reject`, `␣rejected`, `Rejected`, `rejected` | 2/152 (1%) | 23/81 (28%) | 4/138 (3%) | 0/158 (0%) | 2/53 (4%) | 23/74 (31%) |
| vague (vague) | unclear | `␣vague`, `含糊`, `模糊`, `␣vaguely` | 15/152 (10%) | 10/81 (12%) | 0/138 (0%) | 4/158 (3%) | 7/53 (13%) | 7/74 (9%) |
| true (true, real) | truth | `true`, `真实`, `真实性`, `确实`, `真实的`, `是真的`, `内容的真实性`, `的真实`, `的真实性` | 13/152 (9%) | 10/81 (12%) | 69/138 (50%) | 45/158 (28%) | 3/53 (6%) | 10/74 (14%) |
| clarify (clarifying) | unclear | `澄清`, `␣clarification`, `␣clarify`, `␣clarified` | 4/152 (3%) | 17/81 (21%) | 17/138 (12%) | 15/158 (9%) | 3/53 (6%) | 16/74 (22%) |
| technically (technically (hedge)) | unclear | `␣technically`, `技术上` | 10/152 (7%) | 7/81 (9%) | 1/138 (1%) | 3/158 (2%) | 6/53 (11%) | 7/74 (9%) |
| forbidden (forbidden, prohibited) | unclear | `禁止`, `␣prohibited` | 0/152 (0%) | 17/81 (21%) | 3/138 (2%) | 0/158 (0%) | 0/53 (0%) | 17/74 (23%) |
| fraud (fraud) | lie | `␣fraudulent`, `␣fraud` | 16/152 (11%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 6/53 (11%) | 0/74 (0%) |
| avoid (avoiding) | unclear | `␣avoidance`, `␣avoiding`, `␣avoided`, `避开`, `avoid`, `␣avoid`, `␣avoids`, `避免`, `␣Avoid`, `Avoid`, `避免了` | 8/152 (5%) | 8/81 (10%) | 0/138 (0%) | 0/158 (0%) | 5/53 (9%) | 8/74 (11%) |
| fiction (fiction, fictional) | unclear | `␣fictional`, `␣fict`, `fiction`, `␣Fiction` | 8/152 (5%) | 6/81 (7%) | 49/138 (36%) | 41/158 (26%) | 2/53 (4%) | 5/74 (7%) |
| transparent (transparent) | truth | `透明`, `␣transparency`, `␣Transparency`, `透明度`, `␣transparent` | 0/152 (0%) | 13/81 (16%) | 15/138 (11%) | 5/158 (3%) | 0/53 (0%) | 12/74 (16%) |
| secret (secret, secrecy) | lie | `␣secrecy`, `秘密`, `␣secretive`, `␣undisclosed` | 6/152 (4%) | 7/81 (9%) | 8/138 (6%) | 1/158 (1%) | 4/53 (8%) | 6/74 (8%) |
| wrong (wrong, mistaken) | lie | `␣WRONG`, `误`, `错误`, `错了`, `没错`, `是错误的` | 8/152 (5%) | 5/81 (6%) | 8/138 (6%) | 21/158 (13%) | 4/53 (8%) | 4/74 (5%) |
| undisclosed (not disclosed) | lie | `␣undisclosed` | 5/152 (3%) | 7/81 (9%) | 7/138 (5%) | 1/158 (1%) | 3/53 (6%) | 6/74 (8%) |
| confess (confessing, coming clean) | truth | `坦白`, `␣confess`, `␣confession` | 0/152 (0%) | 12/81 (15%) | 17/138 (12%) | 4/158 (3%) | 0/53 (0%) | 11/74 (15%) |
| disclose (disclosing) | truth | `␣disclosure`, `␣disclosing`, `␣disclosed`, `␣disclose`, `␣disclosures`, `␣Disclosure`, `披露`, `信息披露`, `揭露`, `␣revealing` | 1/152 (1%) | 11/81 (14%) | 25/138 (18%) | 2/158 (1%) | 1/53 (2%) | 10/74 (14%) |
| justify (justifying oneself, making excuses) | unclear | `辩解` | 8/152 (5%) | 3/81 (4%) | 2/138 (1%) | 0/158 (0%) | 4/53 (8%) | 3/74 (4%) |
| decline (declining (to do something)) | unclear | `␣declined`, `␣decline`, `␣declining`, `␣declines` | 0/152 (0%) | 10/81 (12%) | 0/138 (0%) | 0/158 (0%) | 0/53 (0%) | 10/74 (14%) |
| pretend / disguise (putting on a false appearance) | lie | `伪装`, `␣pretending`, `␣disguised`, `␣disguise`, `假装` | 7/152 (5%) | 2/81 (2%) | 11/138 (8%) | 6/158 (4%) | 1/53 (2%) | 2/74 (3%) |
| accurate (accurate) | truth | `␣accurate`, `␣accuracy`, `␣accurately`, `accuracy`, `accur`, `_accuracy`, `Accuracy`, `␣Accuracy`, `准确`, `准确性`, `准确的`, `准确地` | 0/152 (0%) | 9/81 (11%) | 74/138 (54%) | 70/158 (44%) | 0/53 (0%) | 9/74 (12%) |
| withhold (withholding information) | lie | `␣withholding`, `␣withheld`, `␣withhold` | 6/152 (4%) | 2/81 (2%) | 1/138 (1%) | 0/158 (0%) | 5/53 (9%) | 2/74 (3%) |
| exaggerate (overstating) | lie | `夸大`, `␣exaggerated`, `␣exagger` | 6/152 (4%) | 2/81 (2%) | 1/138 (1%) | 4/158 (3%) | 1/53 (2%) | 2/74 (3%) |
| comply (complying with rules) | unclear | `合规`, `␣complying`, `␣compliance`, `␣Compliance`, `␣compliant` | 2/152 (1%) | 6/81 (7%) | 11/138 (8%) | 3/158 (2%) | 1/53 (2%) | 6/74 (8%) |
| debunk (exposing a falsehood) | unclear | `␣debunk` | 2/152 (1%) | 5/81 (6%) | 7/138 (5%) | 4/158 (3%) | 2/53 (4%) | 5/74 (7%) |
| unethical (unethical) | unclear | `␣unethical` | 6/152 (4%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 1/53 (2%) | 1/74 (1%) |
| downplay (understating) | lie | `淡化` | 4/152 (3%) | 3/81 (4%) | 0/138 (0%) | 0/158 (0%) | 2/53 (4%) | 3/74 (4%) |
| confidential (confidential, kept private) | unclear | `␣confidentiality`, `保密` | 2/152 (1%) | 5/81 (6%) | 11/138 (8%) | 1/158 (1%) | 2/53 (4%) | 5/74 (7%) |
| fact (fact, factual) | truth | `␣actually`, `␣actual`, `␣reality`, `actual`, `Actual`, `␣Actual`, `␣Actually`, `_FACT`, `␣Reality`, `Reality`, `Actually`, `actually`, `实际`, `实际上`, `实际的`, `但实际上`, `实际上是` | 3/152 (2%) | 4/81 (5%) | 4/138 (3%) | 20/158 (13%) | 1/53 (2%) | 3/74 (4%) |
| reveal / expose (revealing, exposing) | truth | `揭露`, `␣revealing` | 0/152 (0%) | 6/81 (7%) | 6/138 (4%) | 0/158 (0%) | 0/53 (0%) | 5/74 (7%) |
| accusation (accusing) | unclear | `␣accusations`, `指控`, `␣alleging`, `␣allegations` | 5/152 (3%) | 1/81 (1%) | 2/138 (1%) | 0/158 (0%) | 3/53 (6%) | 1/74 (1%) |
| ethical (ethical) | unclear | `␣ethical` | 0/152 (0%) | 5/81 (6%) | 0/138 (0%) | 0/158 (0%) | 0/53 (0%) | 5/74 (7%) |
| lawful / legitimate (lawful, legitimate) | unclear | `合法`, `␣lawful`, `␣legitimate`, `␣legitimately`, `␣legitim` | 2/152 (1%) | 3/81 (4%) | 3/138 (2%) | 28/158 (18%) | 1/53 (2%) | 3/74 (4%) |
| moral (moral, morality) | unclear | `␣moral`, `道德`, `␣ethical` | 0/152 (0%) | 5/81 (6%) | 0/138 (0%) | 0/158 (0%) | 0/53 (0%) | 5/74 (7%) |
| misunderstanding (misunderstanding) | unclear | `误解`, `␣misunderstanding` | 3/152 (2%) | 2/81 (2%) | 4/138 (3%) | 19/158 (12%) | 1/53 (2%) | 1/74 (1%) |
| integrity (integrity) | truth | `诚信` | 1/152 (1%) | 3/81 (4%) | 8/138 (6%) | 0/158 (0%) | 0/53 (0%) | 3/74 (4%) |
| sincere (sincere) | truth | `真诚` | 0/152 (0%) | 2/81 (2%) | 4/138 (3%) | 4/158 (3%) | 0/53 (0%) | 2/74 (3%) |
| hypocrisy (hypocrisy) | lie | `␣hypocrisy`, `虚伪` | 1/152 (1%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 0/53 (0%) | 1/74 (1%) |
| genuine (genuine, sincerely meant) | truth | `␣genuinely` | 1/152 (1%) | 1/81 (1%) | 3/138 (2%) | 51/158 (32%) | 1/53 (2%) | 1/74 (1%) |
| illegal (illegal) | unclear | `␣illegal`, `违法` | 1/152 (1%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 1/53 (2%) | 0/74 (0%) |
| critique (criticizing) | unclear | `␣criticisms` | 0/152 (0%) | 1/81 (1%) | 0/138 (0%) | 2/158 (1%) | 0/53 (0%) | 1/74 (1%) |
| cheat (cheating) | lie | `作弊` | 1/152 (1%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 0/53 (0%) | 0/74 (0%) |
| apology (apologize, sorry) | unclear | `道歉` | 0/152 (0%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 0/53 (0%) | 1/74 (1%) |
| truth (the truth) | truth | `其真实性` | 0/152 (0%) | 0/81 (0%) | 0/138 (0%) | 1/158 (1%) | 0/53 (0%) | 0/74 (0%) |
| inaccurate (inaccurate) | lie | `不准确` | 0/152 (0%) | 0/81 (0%) | 0/138 (0%) | 4/158 (3%) | 0/53 (0%) | 0/74 (0%) |

Not in the draft: deny (excluded: admit / deny / acknowledge); admit (excluded: admit / deny / acknowledge); acknowledge (excluded: admit / deny / acknowledge)

## preans_slot2

| family | side | members | lies | truths | no-pressure truths | unrelated | lies that deny | truths that deny |
|---|---|---|---|---|---|---|---|---|
| unethical (unethical) | unclear | `␣unethical`, `␣immoral` | 118/152 (78%) | 62/81 (77%) | 5/138 (4%) | 0/158 (0%) | 39/53 (74%) | 56/74 (76%) |
| conceal / hide (keeping information hidden) | lie | `隐瞒`, `␣hidden`, `隐藏`, `hidden`, `␣concealed`, `␣conceal`, `隐藏的`, `-hidden`, `Hidden`, `␣Hidden`, `␣hiding`, `掩盖`, `隐藏着`, `藏着`, `隐` | 100/152 (66%) | 32/81 (40%) | 3/138 (2%) | 0/158 (0%) | 34/53 (64%) | 30/74 (41%) |
| misinformation (false information) | lie | `␣misinformation`, `虚假信息` | 89/152 (59%) | 38/81 (47%) | 100/138 (72%) | 18/158 (11%) | 25/53 (47%) | 37/74 (50%) |
| fake (fake, not genuine) | lie | `fake`, `␣fake`, `Fake`, `␣Fake`, `_fake` | 77/152 (51%) | 45/81 (56%) | 34/138 (25%) | 10/158 (6%) | 25/53 (47%) | 43/74 (58%) |
| secret (secret, secrecy) | lie | `秘密`, `␣secretly`, `的秘密`, `␣secrecy`, `␣secretive`, `␣secret`, `secret`, `Secret`, `-secret`, `␣secrets`, `内幕`, `␣Secret`, `.secret`, `␣SECRET`, `_secret`, `SECRET`, `␣undisclosed`, `␣clandest`, `␣covert`, `隐秘`, `隐蔽`, `商业秘密` | 90/152 (59%) | 21/81 (26%) | 2/138 (1%) | 0/158 (0%) | 30/53 (57%) | 17/74 (23%) |
| confidential (confidential, kept private) | unclear | `␣confidentiality`, `保密`, `␣confidential`, `机密`, `␣Confidential` | 81/152 (53%) | 25/81 (31%) | 4/138 (3%) | 1/158 (1%) | 30/53 (57%) | 20/74 (27%) |
| facts (the facts, what actually happened) | unclear | `事实`, `␣facts`, `实际情况`, `␣factual`, `的事实`, `facts`, `␣Facts`, `事实上`, `␣fact`, `fact`, `␣Fact`, `Fact`, `␣FACT`, `FACT`, `根据实际情况`, `事实和`, `_fact` | 81/152 (53%) | 19/81 (23%) | 127/138 (92%) | 35/158 (22%) | 22/53 (42%) | 17/74 (23%) |
| fabricate (making something up) | lie | `虚构`, `伪造`, `造假`, `弄虚作假` | 52/152 (34%) | 41/81 (51%) | 85/138 (62%) | 26/158 (16%) | 17/53 (32%) | 39/74 (53%) |
| truthful (telling the truth) | truth | `␣truthful`, `实事求是`, `如实` | 69/152 (45%) | 21/81 (26%) | 101/138 (73%) | 4/158 (3%) | 17/53 (32%) | 20/74 (27%) |
| true (true, real) | truth | `␣true`, `␣TRUE`, `真正`, `真实`, `真实性`, `确实`, `真正的`, `的确`, `真实的`, `是真的`, `真實`, `内容的真实性`, `的真实`, `的真实性`, `的真正` | 77/152 (51%) | 12/81 (15%) | 62/138 (45%) | 14/158 (9%) | 19/53 (36%) | 11/74 (15%) |
| false (false, untrue) | lie | `␣false`, `␣False`, `false`, `False`, `␣FALSE`, `␣fals`, `␣falsely`, `␣untrue`, `/false`, `␣falsehood`, `假`, `虚假`, `假的`, `真假`, `真伪` | 54/152 (36%) | 35/81 (43%) | 67/138 (49%) | 9/158 (6%) | 13/53 (25%) | 34/74 (46%) |
| intentional (doing it on purpose) | unclear | `故意`, `␣intentionally`, `␣deliberately`, `␣intentional`, `刻意`, `␣deliberate`, `故意的`, `明知`, `␣knowingly` | 63/152 (41%) | 20/81 (25%) | 0/138 (0%) | 1/158 (1%) | 17/53 (32%) | 20/74 (27%) |
| violate (violating a rule or principle) | unclear | `违背`, `违反`, `违规`, `␣violate`, `␣violates`, `␣violations`, `␣violated`, `␣violating`, `违反了`, `␣violation` | 43/152 (28%) | 30/81 (37%) | 2/138 (1%) | 0/158 (0%) | 9/53 (17%) | 28/74 (38%) |
| fact (fact, factual) | truth | `␣actually`, `␣actual`, `␣reality`, `actual`, `Actual`, `␣Actual`, `␣Actually`, `_FACT`, `_actual`, `␣Reality`, `Reality`, `Actually`, `actually`, `实际`, `实际上`, `的实际`, `实际的`, `但实际上`, `实际上是`, `认定事实`, `␣réalité` | 58/152 (38%) | 6/81 (7%) | 11/138 (8%) | 15/158 (9%) | 13/53 (25%) | 5/74 (7%) |
| moral (moral, morality) | unclear | `␣morally`, `道德`, `␣moral`, `的道德`, `␣morality`, `␣Moral`, `␣morals`, `␣ethical`, `␣ethics`, `ethical`, `伦理`, `␣Ethics`, `职业道德`, `␣ethic` | 34/152 (22%) | 25/81 (31%) | 2/138 (1%) | 1/158 (1%) | 11/53 (21%) | 21/74 (28%) |
| ethical (ethical) | unclear | `␣ethical`, `ethical` | 32/152 (21%) | 24/81 (30%) | 2/138 (1%) | 1/158 (1%) | 10/53 (19%) | 20/74 (27%) |
| whistleblower (whistleblower) | unclear | `␣whistleblower`, `␣whistlebl` | 43/152 (28%) | 11/81 (14%) | 2/138 (1%) | 0/158 (0%) | 11/53 (21%) | 10/74 (14%) |
| undisclosed (not disclosed) | lie | `␣undisclosed` | 46/152 (30%) | 7/81 (9%) | 1/138 (1%) | 0/158 (0%) | 16/53 (30%) | 6/74 (8%) |
| fiction (fiction, fictional) | unclear | `␣fictional`, `fiction`, `␣fict`, `␣Fiction`, `␣fiction`, `-fiction` | 21/152 (14%) | 30/81 (37%) | 52/138 (38%) | 21/158 (13%) | 10/53 (19%) | 28/74 (38%) |
| hypocrisy (hypocrisy) | lie | `␣hypocrisy` | 30/152 (20%) | 18/81 (22%) | 1/138 (1%) | 0/158 (0%) | 7/53 (13%) | 18/74 (24%) |
| lie (telling a lie) | lie | `谎言`, `说谎`, `撒谎`, `␣liar`, `谎`, `␣lie`, `␣lies`, `␣lying`, `␣Lie`, `␣lied`, `␣거짓`, `␣mentira`, `lying`, `lie`, `Lie`, `␣Lies` | 34/152 (22%) | 14/81 (17%) | 0/138 (0%) | 0/158 (0%) | 7/53 (13%) | 14/74 (19%) |
| knowingly (knowing it, aware) | unclear | `明知`, `␣knowingly` | 38/152 (25%) | 5/81 (6%) | 0/138 (0%) | 0/158 (0%) | 10/53 (19%) | 5/74 (7%) |
| contradict (contradicting) | unclear | `␣contradict`, `␣contradictory`, `矛盾`, `␣contrad`, `␣contradiction`, `␣contradictions`, `矛盾的` | 15/152 (10%) | 25/81 (31%) | 21/138 (15%) | 0/158 (0%) | 4/53 (8%) | 24/74 (32%) |
| ethics (ethics as a topic) | unclear | `␣ethics`, `伦理`, `␣Ethics`, `职业道德`, `␣ethic` | 21/152 (14%) | 18/81 (22%) | 2/138 (1%) | 1/158 (1%) | 6/53 (11%) | 15/74 (20%) |
| unauthorized (unauthorized) | unclear | `␣unauthorized`, `␣Unauthorized`, `Unauthorized` | 26/152 (17%) | 9/81 (11%) | 0/138 (0%) | 1/158 (1%) | 9/53 (17%) | 8/74 (11%) |
| dishonest (not honest) | lie | `␣dishonest` | 21/152 (14%) | 13/81 (16%) | 0/138 (0%) | 0/158 (0%) | 3/53 (6%) | 13/74 (18%) |
| illegal (illegal) | unclear | `␣illegal`, `非法`, `␣illegally`, `违法`, `illegal`, `Illegal`, `␣Illegal`, `␣unlawful` | 15/152 (10%) | 14/81 (17%) | 0/138 (0%) | 0/158 (0%) | 6/53 (11%) | 12/74 (16%) |
| accusation (accusing) | unclear | `␣accusations`, `␣accusation`, `指控`, `␣allegations`, `␣allegation` | 18/152 (12%) | 8/81 (10%) | 3/138 (2%) | 0/158 (0%) | 5/53 (9%) | 8/74 (11%) |
| pretend / disguise (putting on a false appearance) | lie | `伪装`, `␣disguised`, `␣disguise`, `␣pretending` | 19/152 (12%) | 6/81 (7%) | 4/138 (3%) | 1/158 (1%) | 5/53 (9%) | 5/74 (7%) |
| mislead (leading someone to a wrong belief) | lie | `␣misleading`, `误导`, `␣misled`, `误导性` | 10/152 (7%) | 11/81 (14%) | 9/138 (7%) | 3/158 (2%) | 2/53 (4%) | 11/74 (15%) |
| forbidden (forbidden, prohibited) | unclear | `禁止`, `␣prohibited`, `␣forbidden`, `␣forbid` | 9/152 (6%) | 12/81 (15%) | 2/138 (1%) | 0/158 (0%) | 5/53 (9%) | 11/74 (15%) |
| fraud (fraud) | lie | `␣fraudulent`, `␣fraud`, `␣Fraud` | 10/152 (7%) | 8/81 (10%) | 1/138 (1%) | 0/158 (0%) | 2/53 (4%) | 8/74 (11%) |
| wrong (wrong, mistaken) | lie | `␣WRONG`, `误`, `错误` | 8/152 (5%) | 9/81 (11%) | 2/138 (1%) | 3/158 (2%) | 2/53 (4%) | 8/74 (11%) |
| refuse (refusing) | unclear | `拒绝`, `␣refusal`, `␣refused`, `␣refusing`, `␣refus`, `␣refuses`, `拒`, `␣refuse`, `拒絕`, `拒绝了` | 0/152 (0%) | 16/81 (20%) | 1/138 (1%) | 0/158 (0%) | 0/53 (0%) | 16/74 (22%) |
| immoral (immoral) | unclear | `␣immoral` | 8/152 (5%) | 7/81 (9%) | 0/138 (0%) | 0/158 (0%) | 3/53 (6%) | 6/74 (8%) |
| covert (covert, clandestine) | lie | `␣clandest`, `␣covert` | 13/152 (9%) | 2/81 (2%) | 0/138 (0%) | 0/158 (0%) | 10/53 (19%) | 2/74 (3%) |
| disclose (disclosing) | truth | `␣disclosure`, `␣disclosures`, `␣disclose`, `␣disclosed`, `␣Disclosure`, `␣disclosing`, `揭露` | 12/152 (8%) | 3/81 (4%) | 0/138 (0%) | 0/158 (0%) | 3/53 (6%) | 3/74 (4%) |
| cheat (cheating) | lie | `作弊`, `␣cheating` | 7/152 (5%) | 6/81 (7%) | 0/138 (0%) | 0/158 (0%) | 1/53 (2%) | 6/74 (8%) |
| genuine (genuine, sincerely meant) | truth | `␣genuinely`, `␣genuine`, `␣Genuine` | 11/152 (7%) | 2/81 (2%) | 0/138 (0%) | 5/158 (3%) | 2/53 (4%) | 2/74 (3%) |
| imply (implying, implicit) | unclear | `隐含`, `␣implicitly`, `␣implicit`, `implicit`, `␣implied`, `␣implies`, `␣imply`, `␣implying`, `暗示` | 5/152 (3%) | 7/81 (9%) | 2/138 (1%) | 1/158 (1%) | 1/53 (2%) | 7/74 (9%) |
| privacy (privacy) | unclear | `隐私`, `␣privacy`, `privacy`, `␣Privacy`, `Privacy` | 7/152 (5%) | 4/81 (5%) | 1/138 (1%) | 1/158 (1%) | 6/53 (11%) | 3/74 (4%) |
| misrepresent (giving a distorted account) | lie | `␣misrepresented` | 4/152 (3%) | 6/81 (7%) | 2/138 (1%) | 1/158 (1%) | 2/53 (4%) | 6/74 (8%) |
| reveal / expose (revealing, exposing) | truth | `揭露` | 9/152 (6%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 0/53 (0%) | 1/74 (1%) |
| honest (honest) | truth | `␣honesty`, `诚实`, `␣honestly`, `␣honest`, `␣Honest` | 4/152 (3%) | 5/81 (6%) | 1/138 (1%) | 0/158 (0%) | 0/53 (0%) | 5/74 (7%) |
| strategic (strategic, calculated) | unclear | `␣strategy`, `␣Strategy`, `␣strategies`, `␣strategically` | 5/152 (3%) | 4/81 (5%) | 0/138 (0%) | 0/158 (0%) | 3/53 (6%) | 4/74 (5%) |
| comply (complying with rules) | unclear | `␣compliance`, `合规`, `␣Compliance` | 6/152 (4%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 2/53 (4%) | 1/74 (1%) |
| incorrect (incorrect) | lie | `␣incorrect`, `Incorrect`, `␣inaccur`, `␣incorrectly`, `␣inaccurate`, `incorrect`, `␣erroneous`, `␣Incorrect`, `错误的`, `不符合`, `有误` | 2/152 (1%) | 5/81 (6%) | 10/138 (7%) | 12/158 (8%) | 1/53 (2%) | 5/74 (7%) |
| disclaimer (disclaimer) | unclear | `␣disclaimer` | 4/152 (3%) | 2/81 (2%) | 36/138 (26%) | 3/158 (2%) | 3/53 (6%) | 2/74 (3%) |
| wrongdoing (wrongdoing) | unclear | `␣wrongdoing`, `␣wrongful` | 3/152 (2%) | 2/81 (2%) | 0/138 (0%) | 0/158 (0%) | 1/53 (2%) | 2/74 (3%) |
| integrity (integrity) | truth | `␣integrity`, `诚信`, `␣Integrity` | 2/152 (1%) | 3/81 (4%) | 1/138 (1%) | 0/158 (0%) | 2/53 (4%) | 3/74 (4%) |
| lawful / legitimate (lawful, legitimate) | unclear | `合法`, `␣legitimately`, `␣legitimate`, `␣lawful` | 4/152 (3%) | 1/81 (1%) | 0/138 (0%) | 1/158 (1%) | 2/53 (4%) | 1/74 (1%) |
| correct (correct) | truth | `␣correct`, `␣correctly`, `correct`, `␣correction`, `_correct`, `Correct`, `␣corrected`, `␣Correct`, `␣corrections`, `␣correctness`, `␣Correction`, `␣correcting`, `.correct`, `Correction`, `␣Corrections`, `␣corrective`, `正确`, `正确的`, `修正`, `纠错`, `正确答案`, `纠正`, `改正`, `的正确`, `更正`, `是正确的`, `正确地`, `是否正确` | 1/152 (1%) | 4/81 (5%) | 28/138 (20%) | 36/158 (23%) | 0/53 (0%) | 3/74 (4%) |
| responsible (responsible, accountable) | unclear | `␣responsible`, `␣Responsible`, `␣Responsibility`, `␣responsibly`, `␣Responsable`, `␣accountability`, `␣responsibility` | 3/152 (2%) | 1/81 (1%) | 0/138 (0%) | 1/158 (1%) | 3/53 (6%) | 1/74 (1%) |
| bias (biased) | unclear | `␣biased`, `␣biases`, `␣bias`, `biased`, `Bias`, `␣Bias`, `偏见`, `_bias`, `bias` | 2/152 (1%) | 1/81 (1%) | 1/138 (1%) | 0/158 (0%) | 1/53 (2%) | 1/74 (1%) |
| avoid (avoiding) | unclear | `避免`, `␣avoidance`, `为了避免`, `以避免`, `␣avoiding`, `Avoid` | 1/152 (1%) | 2/81 (2%) | 0/138 (0%) | 0/158 (0%) | 1/53 (2%) | 2/74 (3%) |
| withhold (withholding information) | lie | `␣withholding`, `␣withheld` | 2/152 (1%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 2/53 (4%) | 1/74 (1%) |
| accountability (accountability) | unclear | `␣accountability` | 2/152 (1%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 2/53 (4%) | 0/74 (0%) |
| manipulate (manipulating someone) | lie | `␣manipulated`, `␣manipulation`, `␣manipulate`, `␣manipulating`, `操纵`, `␣manipul` | 1/152 (1%) | 1/81 (1%) | 1/138 (1%) | 0/158 (0%) | 1/53 (2%) | 1/74 (1%) |
| debunk (exposing a falsehood) | unclear | `␣debunk` | 1/152 (1%) | 1/81 (1%) | 1/138 (1%) | 3/158 (2%) | 0/53 (0%) | 1/74 (1%) |
| candid (candid, frank) | truth | `坦诚` | 0/152 (0%) | 2/81 (2%) | 0/138 (0%) | 0/158 (0%) | 0/53 (0%) | 2/74 (3%) |
| blame (blaming) | unclear | `␣blame`, `␣blaming` | 1/152 (1%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 1/53 (2%) | 1/74 (1%) |
| betray (betray) | unclear | `␣betrayal`, `␣betray` | 1/152 (1%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 1/53 (2%) | 1/74 (1%) |
| irresponsible (irresponsible) | unclear | `␣irresponsible` | 2/152 (1%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 2/53 (4%) | 0/74 (0%) |
| accurate (accurate) | truth | `␣accurate`, `␣accuracy`, `␣accurately`, `accuracy`, `accur`, `Accuracy`, `␣Accuracy`, `准确`, `准确性`, `准确的` | 0/152 (0%) | 2/81 (2%) | 1/138 (1%) | 16/158 (10%) | 0/53 (0%) | 2/74 (3%) |
| trick (tricking someone) | lie | `␣trick`, `␣tricks`, `␣Trick` | 0/152 (0%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 0/53 (0%) | 1/74 (1%) |
| guilt (guilt) | unclear | `␣guilty`, `␣guilt` | 1/152 (1%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 0/53 (0%) | 0/74 (0%) |
| reject (rejecting) | unclear | `␣rejected`, `Reject`, `rejected` | 0/152 (0%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 0/53 (0%) | 1/74 (1%) |
| omit (leaving something out) | lie | `␣omission` | 1/152 (1%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 1/53 (2%) | 0/74 (0%) |
| evade (evading) | lie | `逃避` | 0/152 (0%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 0/53 (0%) | 1/74 (1%) |
| technically (technically (hedge)) | unclear | `␣technically` | 1/152 (1%) | 0/81 (0%) | 0/138 (0%) | 1/158 (1%) | 0/53 (0%) | 0/74 (0%) |
| unintentional (not on purpose) | unclear | `␣unintention` | 0/152 (0%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 0/53 (0%) | 1/74 (1%) |
| mistake (mistake) | unclear | `␣mistake`, `␣mistakes`, `失误` | 0/152 (0%) | 1/81 (1%) | 0/138 (0%) | 1/158 (1%) | 0/53 (0%) | 1/74 (1%) |
| misunderstanding (misunderstanding) | unclear | `误解` | 0/152 (0%) | 1/81 (1%) | 1/138 (1%) | 2/158 (1%) | 0/53 (0%) | 1/74 (1%) |

Not in the draft: truth (excluded: truth from the question on); admit (excluded: admit / deny / acknowledge); acknowledge (excluded: admit / deny / acknowledge); deny (excluded: admit / deny / acknowledge)

## preans_slot3

| family | side | members | lies | truths | no-pressure truths | unrelated | lies that deny | truths that deny |
|---|---|---|---|---|---|---|---|---|
| honest (honest) | truth | `␣honestly`, `␣Honestly`, `␣Honest`, `␣honesty`, `␣honest`, `诚实`, `Honestly` | 28/152 (18%) | 9/81 (11%) | 0/138 (0%) | 17/158 (11%) | 8/53 (15%) | 7/74 (9%) |
| apologize (apologizing) | unclear | `␣apologize`, `␣apologies`, `抱歉`, `␣sorry`, `␣Sorry`, `Sorry`, `␣apology`, `sorry` | 24/152 (16%) | 6/81 (7%) | 0/138 (0%) | 3/158 (2%) | 8/53 (15%) | 5/74 (7%) |
| confess (confessing, coming clean) | truth | `坦白` | 12/152 (8%) | 6/81 (7%) | 0/138 (0%) | 1/158 (1%) | 3/53 (6%) | 5/74 (7%) |
| false (false, untrue) | lie | `␣False`, `false`, `False`, `=False`, `>false` | 4/152 (3%) | 4/81 (5%) | 13/138 (9%) | 0/158 (0%) | 4/53 (8%) | 4/74 (5%) |
| disclaimer (disclaimer) | unclear | `␣disclaimer`, `Disclaimer`, `␣Disclaimer` | 7/152 (5%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 0/53 (0%) | 0/74 (0%) |
| clarify (clarifying) | unclear | `澄清` | 1/152 (1%) | 4/81 (5%) | 0/138 (0%) | 0/158 (0%) | 1/53 (2%) | 4/74 (5%) |
| ethics (ethics as a topic) | unclear | `伦理`, `␣Ethics`, `␣ethical` | 4/152 (3%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 0/53 (0%) | 0/74 (0%) |
| confidential (confidential, kept private) | unclear | `␣confidentiality` | 2/152 (1%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 1/53 (2%) | 0/74 (0%) |
| accountability (accountability) | unclear | `␣Accountability` | 1/152 (1%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 0/53 (0%) | 1/74 (1%) |
| true (true, real) | truth | `>true`, `的确` | 1/152 (1%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 1/53 (2%) | 1/74 (1%) |
| ethical (ethical) | unclear | `␣ethical` | 1/152 (1%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 0/53 (0%) | 0/74 (0%) |
| candid (candid, frank) | truth | `␣frankly` | 1/152 (1%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 1/53 (2%) | 0/74 (0%) |
| unethical (unethical) | unclear | `␣unethical` | 1/152 (1%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 0/53 (0%) | 0/74 (0%) |
| refuse (refusing) | unclear | `拒绝` | 1/152 (1%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 0/53 (0%) | 0/74 (0%) |
| technically (technically (hedge)) | unclear | `␣technically` | 1/152 (1%) | 0/81 (0%) | 0/138 (0%) | 5/158 (3%) | 1/53 (2%) | 0/74 (0%) |
| incorrect (incorrect) | lie | `␣Incorrect` | 0/152 (0%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 0/53 (0%) | 1/74 (1%) |
| wrong (wrong, mistaken) | lie | `没错` | 0/152 (0%) | 1/81 (1%) | 2/138 (1%) | 0/158 (0%) | 0/53 (0%) | 1/74 (1%) |
| fact (fact, factual) | truth | `␣Actually` | 0/152 (0%) | 0/81 (0%) | 0/138 (0%) | 1/158 (1%) | 0/53 (0%) | 0/74 (0%) |

Not in the draft: admit (excluded: admit / deny / acknowledge); acknowledge (excluded: admit / deny / acknowledge); deny (excluded: admit / deny / acknowledge)

## preans_slot4

| family | side | members | lies | truths | no-pressure truths | unrelated | lies that deny | truths that deny |
|---|---|---|---|---|---|---|---|---|
| truthful (telling the truth) | truth | `␣truthful`, `如实`, `实事求是` | 133/152 (88%) | 80/81 (99%) | 138/138 (100%) | 157/158 (99%) | 52/53 (98%) | 74/74 (100%) |
| honest (honest) | truth | `␣honesty`, `␣honest`, `␣honestly`, `诚实`, `␣Honest`, `␣Honestly`, `诚实守信` | 132/152 (87%) | 78/81 (96%) | 134/138 (97%) | 156/158 (99%) | 51/53 (96%) | 73/74 (99%) |
| moral (moral, morality) | unclear | `␣morally`, `␣moral`, `道德`, `的道德`, `␣morality`, `␣Moral`, `␣ethical`, `␣ethics`, `ethical`, `␣Ethics`, `伦理`, `职业道德` | 109/152 (72%) | 47/81 (58%) | 2/138 (1%) | 1/158 (1%) | 20/53 (38%) | 41/74 (55%) |
| ethical (ethical) | unclear | `␣ethical`, `ethical` | 107/152 (70%) | 47/81 (58%) | 2/138 (1%) | 1/158 (1%) | 19/53 (36%) | 41/74 (55%) |
| intentional (doing it on purpose) | unclear | `␣intentionally`, `␣intentional`, `␣deliberately`, `故意`, `␣deliberate`, `␣knowingly`, `明知` | 67/152 (44%) | 64/81 (79%) | 80/138 (58%) | 102/158 (65%) | 16/53 (30%) | 58/74 (78%) |
| true (true, real) | truth | `␣true`, `␣True`, `␣TRUE`, `>true`, `真实`, `真实性`, `确实`, `真实的`, `的真实`, `的真实性` | 67/152 (44%) | 46/81 (57%) | 107/138 (78%) | 80/158 (51%) | 12/53 (23%) | 42/74 (57%) |
| unethical (unethical) | unclear | `␣unethical`, `␣immoral` | 92/152 (61%) | 19/81 (23%) | 1/138 (1%) | 0/158 (0%) | 10/53 (19%) | 14/74 (19%) |
| ethics (ethics as a topic) | unclear | `␣ethics`, `␣Ethics`, `伦理`, `职业道德` | 79/152 (52%) | 12/81 (15%) | 0/138 (0%) | 0/158 (0%) | 9/53 (17%) | 10/74 (14%) |
| confidential (confidential, kept private) | unclear | `␣confidentiality`, `␣confidential`, `保密`, `␣Confidential`, `机密` | 74/152 (49%) | 8/81 (10%) | 1/138 (1%) | 0/158 (0%) | 22/53 (42%) | 5/74 (7%) |
| integrity (integrity) | truth | `诚信`, `␣integrity`, `␣Integrity`, `正直` | 35/152 (23%) | 44/81 (54%) | 37/138 (27%) | 43/158 (27%) | 13/53 (25%) | 42/74 (57%) |
| candid (candid, frank) | truth | `坦诚`, `␣straightforward`, `␣frankly` | 28/152 (18%) | 50/81 (62%) | 38/138 (28%) | 43/158 (27%) | 13/53 (25%) | 47/74 (64%) |
| facts (the facts, what actually happened) | unclear | `␣factual`, `事实`, `␣facts` | 24/152 (16%) | 42/81 (52%) | 135/138 (98%) | 136/158 (86%) | 14/53 (26%) | 42/74 (57%) |
| genuine (genuine, sincerely meant) | truth | `␣genuinely`, `␣genuine` | 21/152 (14%) | 39/81 (48%) | 18/138 (13%) | 95/158 (60%) | 13/53 (25%) | 39/74 (53%) |
| conceal / hide (keeping information hidden) | lie | `隐瞒`, `␣conceal`, `隐藏` | 46/152 (30%) | 12/81 (15%) | 9/138 (7%) | 2/158 (1%) | 9/53 (17%) | 9/74 (12%) |
| lawful / legitimate (lawful, legitimate) | unclear | `␣legitimate`, `␣lawful`, `合法`, `␣legitimately` | 43/152 (28%) | 12/81 (15%) | 0/138 (0%) | 0/158 (0%) | 28/53 (53%) | 11/74 (15%) |
| clarify (clarifying) | unclear | `␣clarification`, `澄清`, `␣clarify` | 28/152 (18%) | 25/81 (31%) | 7/138 (5%) | 36/158 (23%) | 18/53 (34%) | 24/74 (32%) |
| transparent (transparent) | truth | `␣transparency`, `␣Transparency`, `透明`, `透明度`, `␣transparent`, `-transparent`, `透明的`, `␣Transparent`, `transparent`, `␣transparencia`, `Transparent` | 21/152 (14%) | 31/81 (38%) | 10/138 (7%) | 5/158 (3%) | 13/53 (25%) | 29/74 (39%) |
| dishonest (not honest) | lie | `␣dishonest` | 44/152 (29%) | 6/81 (7%) | 0/138 (0%) | 0/158 (0%) | 6/53 (11%) | 4/74 (5%) |
| false (false, untrue) | lie | `␣false`, `␣False`, `false`, `False`, `␣FALSE`, `␣fals`, `␣untrue`, `/false`, `␣falsehood`, `假`, `虚假`, `不实` | 31/152 (20%) | 17/81 (21%) | 65/138 (47%) | 72/158 (46%) | 23/53 (43%) | 16/74 (22%) |
| misinformation (false information) | lie | `␣misinformation` | 38/152 (25%) | 7/81 (9%) | 36/138 (26%) | 109/158 (69%) | 12/53 (23%) | 4/74 (5%) |
| sincere (sincere) | truth | `真诚`, `␣sincerely`, `␣sincerity`, `␣sincere` | 16/152 (11%) | 27/81 (33%) | 8/138 (6%) | 13/158 (8%) | 10/53 (19%) | 27/74 (36%) |
| comply (complying with rules) | unclear | `␣compliance`, `␣Compliance`, `合规`, `␣compliant` | 37/152 (24%) | 4/81 (5%) | 1/138 (1%) | 0/158 (0%) | 10/53 (19%) | 2/74 (3%) |
| violate (violating a rule or principle) | unclear | `违背`, `违反`, `␣violating`, `␣violate`, `␣violates`, `违规`, `␣violations`, `␣violated`, `␣violation`, `违反了` | 37/152 (24%) | 4/81 (5%) | 1/138 (1%) | 0/158 (0%) | 0/53 (0%) | 3/74 (4%) |
| responsible (responsible, accountable) | unclear | `␣responsibly` | 32/152 (21%) | 8/81 (10%) | 1/138 (1%) | 0/158 (0%) | 10/53 (19%) | 8/74 (11%) |
| mislead (leading someone to a wrong belief) | lie | `␣misleading`, `误导` | 17/152 (11%) | 6/81 (7%) | 15/138 (11%) | 41/158 (26%) | 5/53 (9%) | 4/74 (5%) |
| immoral (immoral) | unclear | `␣immoral` | 19/152 (12%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 0/53 (0%) | 0/74 (0%) |
| strategic (strategic, calculated) | unclear | `␣strategically`, `␣strategic`, `␣strategy`, `␣strategies`, `␣Strategy`, `␣Strategic` | 13/152 (9%) | 4/81 (5%) | 0/138 (0%) | 0/158 (0%) | 6/53 (11%) | 2/74 (3%) |
| confess (confessing, coming clean) | truth | `坦白` | 9/152 (6%) | 7/81 (9%) | 1/138 (1%) | 4/158 (3%) | 2/53 (4%) | 5/74 (7%) |
| lie (telling a lie) | lie | `谎言`, `说谎`, `撒谎` | 13/152 (9%) | 2/81 (2%) | 0/138 (0%) | 0/158 (0%) | 5/53 (9%) | 0/74 (0%) |
| secret (secret, secrecy) | lie | `␣secrecy`, `秘密`, `␣secretive`, `␣secretly`, `␣secret`, `␣Secret`, `Secret`, `的秘密`, `␣undisclosed`, `␣clandest`, `隐蔽` | 11/152 (7%) | 2/81 (2%) | 0/138 (0%) | 0/158 (0%) | 3/53 (6%) | 0/74 (0%) |
| refuse (refusing) | unclear | `拒绝`, `␣refusal`, `␣refus`, `␣refusing`, `␣refused` | 0/152 (0%) | 12/81 (15%) | 0/138 (0%) | 0/158 (0%) | 0/53 (0%) | 12/74 (16%) |
| technically (technically (hedge)) | unclear | `␣technically` | 9/152 (6%) | 2/81 (2%) | 0/138 (0%) | 14/158 (9%) | 3/53 (6%) | 2/74 (3%) |
| accusation (accusing) | unclear | `␣accusations`, `指控`, `␣allegations` | 9/152 (6%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 7/53 (13%) | 1/74 (1%) |
| fabricate (making something up) | lie | `虚构`, `弄虚作假` | 8/152 (5%) | 0/81 (0%) | 1/138 (1%) | 13/158 (8%) | 0/53 (0%) | 0/74 (0%) |
| disclaimer (disclaimer) | unclear | `␣disclaimer`, `␣Disclaimer` | 3/152 (2%) | 5/81 (6%) | 3/138 (2%) | 3/158 (2%) | 1/53 (2%) | 4/74 (5%) |
| correct (correct) | truth | `␣correct`, `␣correctly`, `correct`, `␣Correct`, `␣correctness`, `正确`, `正确的`, `是正确的` | 3/152 (2%) | 5/81 (6%) | 63/138 (46%) | 7/158 (4%) | 3/53 (6%) | 5/74 (7%) |
| accurate (accurate) | truth | `␣accurate`, `␣accuracy`, `␣accurately`, `accur`, `␣Accuracy`, `准确` | 3/152 (2%) | 5/81 (6%) | 82/138 (59%) | 53/158 (34%) | 3/53 (6%) | 5/74 (7%) |
| fraud (fraud) | lie | `␣fraudulent`, `␣Fraud` | 7/152 (5%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 1/53 (2%) | 0/74 (0%) |
| fiction (fiction, fictional) | unclear | `␣fictional`, `␣Fiction`, `fiction`, `␣fict` | 7/152 (5%) | 0/81 (0%) | 1/138 (1%) | 9/158 (6%) | 0/53 (0%) | 0/74 (0%) |
| forbidden (forbidden, prohibited) | unclear | `␣prohibited` | 5/152 (3%) | 2/81 (2%) | 0/138 (0%) | 0/158 (0%) | 0/53 (0%) | 1/74 (1%) |
| pretend / disguise (putting on a false appearance) | lie | `伪装` | 4/152 (3%) | 2/81 (2%) | 0/138 (0%) | 0/158 (0%) | 1/53 (2%) | 1/74 (1%) |
| privacy (privacy) | unclear | `␣privacy`, `␣Privacy`, `privacy`, `隐私` | 5/152 (3%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 2/53 (4%) | 0/74 (0%) |
| misunderstanding (misunderstanding) | unclear | `␣misunderstanding`, `␣misunderstand`, `␣misunderstood`, `误解` | 3/152 (2%) | 3/81 (4%) | 0/138 (0%) | 13/158 (8%) | 3/53 (6%) | 3/74 (4%) |
| disclose (disclosing) | truth | `␣disclosure` | 3/152 (2%) | 2/81 (2%) | 1/138 (1%) | 0/158 (0%) | 0/53 (0%) | 2/74 (3%) |
| fake (fake, not genuine) | lie | `fake`, `␣fake` | 5/152 (3%) | 0/81 (0%) | 1/138 (1%) | 9/158 (6%) | 0/53 (0%) | 0/74 (0%) |
| illegal (illegal) | unclear | `␣illegal` | 4/152 (3%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 0/53 (0%) | 0/74 (0%) |
| reject (rejecting) | unclear | `␣rejecting`, `␣Reject` | 0/152 (0%) | 4/81 (5%) | 0/138 (0%) | 0/158 (0%) | 0/53 (0%) | 4/74 (5%) |
| knowingly (knowing it, aware) | unclear | `␣knowingly`, `明知` | 4/152 (3%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 0/53 (0%) | 0/74 (0%) |
| unauthorized (unauthorized) | unclear | `␣unauthorized`, `␣Unauthorized` | 4/152 (3%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 0/53 (0%) | 0/74 (0%) |
| apologize (apologizing) | unclear | `␣apologize`, `␣apologies`, `␣sorry`, `␣Sorry`, `抱歉` | 2/152 (1%) | 1/81 (1%) | 1/138 (1%) | 9/158 (6%) | 1/53 (2%) | 1/74 (1%) |
| incorrect (incorrect) | lie | `␣incorrect`, `Incorrect`, `␣inaccur`, `␣incorrectly`, `␣inaccurate`, `incorrect`, `␣erroneous`, `␣Incorrect`, `不符合` | 2/152 (1%) | 1/81 (1%) | 7/138 (5%) | 29/158 (18%) | 0/53 (0%) | 1/74 (1%) |
| undisclosed (not disclosed) | lie | `␣undisclosed` | 1/152 (1%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 1/53 (2%) | 0/74 (0%) |
| trust (trust, trustworthy) | unclear | `␣trustworthy`, `信任` | 2/152 (1%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 1/53 (2%) | 0/74 (0%) |
| wrong (wrong, mistaken) | lie | `␣WRONG`, `误`, `错误`, `没错` | 1/152 (1%) | 1/81 (1%) | 1/138 (1%) | 4/158 (3%) | 0/53 (0%) | 0/74 (0%) |
| avoid (avoiding) | unclear | `␣Avoid`, `避免` | 0/152 (0%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 0/53 (0%) | 1/74 (1%) |
| contradict (contradicting) | unclear | `␣contradict` | 0/152 (0%) | 1/81 (1%) | 2/138 (1%) | 0/158 (0%) | 0/53 (0%) | 1/74 (1%) |
| imply (implying, implicit) | unclear | `␣implicitly` | 1/152 (1%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 0/53 (0%) | 0/74 (0%) |
| hypocrisy (hypocrisy) | lie | `␣hypocrisy` | 1/152 (1%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 0/53 (0%) | 0/74 (0%) |
| misrepresent (giving a distorted account) | lie | `␣misrepresented` | 1/152 (1%) | 0/81 (0%) | 1/138 (1%) | 0/158 (0%) | 0/53 (0%) | 0/74 (0%) |
| covert (covert, clandestine) | lie | `␣clandest` | 1/152 (1%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 0/53 (0%) | 0/74 (0%) |
| self-reflection (examining oneself) | unclear | `反思` | 1/152 (1%) | 0/81 (0%) | 0/138 (0%) | 1/158 (1%) | 0/53 (0%) | 0/74 (0%) |
| fact (fact, factual) | truth | `␣actually`, `␣Facts` | 0/152 (0%) | 0/81 (0%) | 0/138 (0%) | 2/158 (1%) | 0/53 (0%) | 0/74 (0%) |

Not in the draft: truth (excluded: truth from the question on); admit (excluded: admit / deny / acknowledge); deny (excluded: admit / deny / acknowledge); acknowledge (excluded: admit / deny / acknowledge)
