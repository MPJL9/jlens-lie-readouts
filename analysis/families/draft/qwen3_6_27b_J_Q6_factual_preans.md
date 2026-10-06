# Draft families: qwen3.6-27b, J-lens, part Q6_factual, group preans

Written by `scripts/apply_family_decisions.py` (2026-10-01; draft, not frozen). Counts are `present / transcripts (share)`
on the build split.

## preans_slot0

| family | side | members | lies | truths | no-pressure truths | unrelated | lies that deny | truths that deny |
|---|---|---|---|---|---|---|---|---|
| critique (criticism) | unclear | `批判`, `␣critique` | 31/152 (20%) | 21/81 (26%) | 50/138 (36%) | 8/158 (5%) | 5/43 (12%) | 17/73 (23%) |
| challenge (challenging, questioning the validity) | unclear | `质疑`, `质问` | 0/152 (0%) | 2/81 (2%) | 2/138 (1%) | 2/158 (1%) | 0/43 (0%) | 2/73 (3%) |

## preans_slot1

| family | side | members | lies | truths | no-pressure truths | unrelated | lies that deny | truths that deny |
|---|---|---|---|---|---|---|---|---|
| honest (honest, truthful) | truth | `␣truthful`, `␣honesty`, `诚实`, `实事求是`, `如实`, `␣honest`, `␣honestly`, `␣Honest`, `如实供述`, `坦诚` | 133/152 (88%) | 67/81 (83%) | 118/138 (86%) | 28/158 (18%) | 37/43 (86%) | 62/73 (85%) |
| lie (telling a lie) | lie | `谎言`, `谎`, `说谎`, `撒谎`, `␣lied`, `␣lie`, `␣lying`, `␣lies`, `␣liar`, `␣mentira` | 147/152 (97%) | 49/81 (60%) | 24/138 (17%) | 0/158 (0%) | 41/43 (95%) | 42/73 (58%) |
| claim (claiming, asserting) | unclear | `␣claiming`, `␣claim`, `claim`, `␣claims`, `Claim`, `␣Claim`, `␣Claims`, `Claims`, `claims`, `␣claimed`, `claimed`, `␣CLAIM`, `CLAIM`, `_claim`, `␣asserting`, `␣assertions`, `assert`, `␣assertion`, `␣assert`, `␣asserted`, `␣asserts`, `␣Assert`, `Assert`, `␣Assertion`, `␣Assertions`, `Assertion`, `Assertions`, `声称`, `宣称` | 124/152 (82%) | 53/81 (65%) | 81/138 (59%) | 37/158 (23%) | 33/43 (77%) | 46/73 (63%) |
| fake (fake, counterfeit) | lie | `fake`, `Fake`, `␣fake`, `␣Fake`, `_fake`, `.fake` | 123/152 (81%) | 34/81 (42%) | 17/138 (12%) | 14/158 (9%) | 27/43 (63%) | 27/73 (37%) |
| deceive (the act of deceiving) | lie | `欺骗`, `␣deception`, `␣deceptive`, `骗` | 126/152 (83%) | 28/81 (35%) | 1/138 (1%) | 0/158 (0%) | 31/43 (72%) | 21/73 (29%) |
| conceal (hiding or withholding something) | lie | `隐瞒`, `␣conceal`, `␣hiding`, `␣concealed`, `隐藏`, `hide`, `␣hidden`, `hidden`, `-hidden`, `Hidden`, `␣Hidden`, `隐藏的` | 106/152 (70%) | 38/81 (47%) | 3/138 (2%) | 0/158 (0%) | 31/43 (72%) | 31/73 (42%) |
| conceal (the act of hiding or concealing) | lie | `隐瞒`, `掩盖`, `掩饰`, `␣conceal`, `␣concealed`, `␣hiding`, `hide`, `隐藏`, `␣masking` | 106/152 (70%) | 38/81 (47%) | 3/138 (2%) | 0/158 (0%) | 31/43 (72%) | 31/73 (42%) |
| fiction (fictional, made up) | unclear | `虚构`, `␣fict`, `␣fictional`, `fiction`, `␣fiction`, `␣Fiction`, `-fiction` | 97/152 (64%) | 42/81 (52%) | 54/138 (39%) | 53/158 (34%) | 22/43 (51%) | 35/73 (48%) |
| mislead (misleading) | lie | `␣misleading`, `误导`, `误导性` | 105/152 (69%) | 32/81 (40%) | 12/138 (9%) | 10/158 (6%) | 25/43 (58%) | 26/73 (36%) |
| fabricate (fabricating / forging) | lie | `伪造`, `造假`, `␣fabricated`, `␣fabrication`, `弄虚作假` | 105/152 (69%) | 15/81 (19%) | 3/138 (2%) | 6/158 (4%) | 24/43 (56%) | 11/73 (15%) |
| fact (fact, factual) | truth | `␣fact`, `␣actually`, `␣actual`, `␣reality`, `actual`, `␣facts`, `Fact`, `Actual`, `fact`, `_FACT`, `␣Fact`, `␣Reality`, `␣Facts`, `Reality`, `_fact`, `␣FACT`, `FACT`, `␣factual`, `facts`, `actually`, `实际`, `事实`, `实际上`, `实际情况`, `事实上`, `的事实`, `的实际`, `实际的`, `但实际上`, `根据实际情况`, `认定事实`, `事实和`, `␣réalité`, `事実` | 43/152 (28%) | 59/81 (73%) | 129/138 (93%) | 114/158 (72%) | 19/43 (44%) | 57/73 (78%) |
| contradict (contradiction) | unclear | `␣contradict`, `␣contrad`, `␣contradictory`, `␣contradiction`, `␣contradictions`, `矛盾` | 54/152 (36%) | 26/81 (32%) | 64/138 (46%) | 0/158 (0%) | 15/43 (35%) | 23/73 (32%) |
| incorrect (incorrect) | lie | `␣incorrect`, `Incorrect`, `␣inaccur`, `␣incorrectly`, `␣inaccurate`, `incorrect`, `␣wrongly`, `␣erroneous`, `␣Incorrect`, `错误的`, `不符合`, `有误`, `不正确` | 40/152 (26%) | 35/81 (43%) | 101/138 (73%) | 104/158 (66%) | 14/43 (33%) | 34/73 (47%) |
| misrepresent (misrepresenting) | lie | `␣misrepresented` | 54/152 (36%) | 16/81 (20%) | 2/138 (1%) | 5/158 (3%) | 8/43 (19%) | 13/73 (18%) |
| true (true, real) | truth | `␣true`, `␣TRUE`, `真实`, `确实`, `的确`, `真实的`, `是真的`, `真實`, `的真实` | 28/152 (18%) | 23/81 (28%) | 20/138 (14%) | 10/158 (6%) | 8/43 (19%) | 22/73 (30%) |
| dishonest (dishonest) | lie | `␣dishonest` | 40/152 (26%) | 6/81 (7%) | 0/138 (0%) | 0/158 (0%) | 15/43 (35%) | 4/73 (5%) |
| blame (blaming) | unclear | `␣blaming`, `␣blame`, `␣blamed`, `␣blames`, `指责` | 40/152 (26%) | 6/81 (7%) | 12/138 (9%) | 0/158 (0%) | 3/43 (7%) | 5/73 (7%) |
| correct (correct) | truth | `␣correct`, `␣correctly`, `correct`, `␣correction`, `_correct`, `Correct`, `␣corrected`, `␣Correct`, `␣corrections`, `␣correctness`, `␣Correction`, `␣correcting`, `.correct`, `_correction`, `Correction`, `␣Corrections`, `␣corrective`, `正确`, `正确的`, `修正`, `正确答案`, `纠正`, `改正`, `的正确`, `更正`, `是正确的`, `正确地`, `是否正确` | 1/152 (1%) | 32/81 (40%) | 118/138 (86%) | 102/158 (65%) | 0/43 (0%) | 31/73 (42%) |
| wrong (wrong, mistaken) | lie | `␣wrong`, `␣ERROR`, `␣Wrong`, `␣WRONG`, `误`, `错误`, `错了`, `的错误`, `是错误的` | 23/152 (15%) | 10/81 (12%) | 20/138 (14%) | 51/158 (32%) | 10/43 (23%) | 8/73 (11%) |
| truth (the truth (as told or hidden)) | truth | `真实性`, `的真实性`, `内容的真实性` | 10/152 (7%) | 21/81 (26%) | 36/138 (26%) | 21/158 (13%) | 4/43 (9%) | 21/73 (29%) |
| knowingly (with knowledge, knowingly) | unclear | `␣knowingly`, `明知`, `␣knowing`, `␣Knowing`, `Knowing` | 25/152 (16%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 10/43 (23%) | 1/73 (1%) |
| knowingly (with knowledge, knowingly) | unclear | `␣knowingly`, `明知` | 25/152 (16%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 10/43 (23%) | 1/73 (1%) |
| allege (alleging, purported) | unclear | `␣alleging`, `␣allegation`, `␣allegations`, `␣purported` | 21/152 (14%) | 4/81 (5%) | 3/138 (2%) | 2/158 (1%) | 5/43 (12%) | 4/73 (5%) |
| violate (violating a rule) | unclear | `违背`, `违反`, `违反了`, `␣violates` | 16/152 (11%) | 8/81 (10%) | 4/138 (3%) | 0/158 (0%) | 4/43 (9%) | 6/73 (8%) |
| fraud (fraud, swindling) | lie | `␣fraudulent`, `弄虚作假` | 22/152 (14%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 9/43 (21%) | 1/73 (1%) |
| pretend (pretending, feigning, disguise) | lie | `␣pretending`, `伪装`, `假装` | 20/152 (13%) | 3/81 (4%) | 0/138 (0%) | 0/158 (0%) | 3/43 (7%) | 1/73 (1%) |
| negate (negating, saying it is not so) | unclear | `否定` | 17/152 (11%) | 6/81 (7%) | 4/138 (3%) | 0/158 (0%) | 8/43 (19%) | 6/73 (8%) |
| disclaimer (disclaimer) | unclear | `␣disclaimer`, `␣Disclaimer`, `Disclaimer`, `␣DISCLAIMER`, `免责声明` | 1/152 (1%) | 21/81 (26%) | 9/138 (7%) | 21/158 (13%) | 1/43 (2%) | 21/73 (29%) |
| cover up (covering up / glossing over) | lie | `掩盖`, `掩饰` | 18/152 (12%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 3/43 (7%) | 1/73 (1%) |
| refuse (refusing) | unclear | `拒绝`, `␣refusal`, `␣refusing`, `␣refus`, `␣refused`, `拒`, `␣refuse`, `␣refuses`, `拒絕`, `拒绝了` | 0/152 (0%) | 18/81 (22%) | 1/138 (1%) | 0/158 (0%) | 0/43 (0%) | 18/73 (25%) |
| accurate (accurate) | truth | `␣accurate`, `␣accuracy`, `␣accurately`, `accuracy`, `accur`, `Accuracy`, `␣Accuracy`, `准确`, `准确性`, `准确的`, `准确地` | 0/152 (0%) | 17/81 (21%) | 84/138 (61%) | 84/158 (53%) | 0/43 (0%) | 17/73 (23%) |
| clarify (clarifying) | unclear | `澄清`, `␣clarification`, `␣clarify`, `␣clarified` | 2/152 (1%) | 9/81 (11%) | 9/138 (7%) | 5/158 (3%) | 2/43 (5%) | 9/73 (12%) |
| deliberate (on purpose) | unclear | `␣intentionally`, `␣deliberately`, `故意` | 7/152 (5%) | 2/81 (2%) | 0/138 (0%) | 1/158 (1%) | 2/43 (5%) | 2/73 (3%) |
| clarify (clarifying) | unclear | `澄清` | 2/152 (1%) | 7/81 (9%) | 9/138 (7%) | 2/158 (1%) | 2/43 (5%) | 7/73 (10%) |
| cannot (being unable / declining to answer) | unclear | `我无法`, `我不能`, `␣Cannot`, `␣cannot`, `cannot`, `Cannot`, `Unable`, `␣Unable`, `不能说`, `无法`, `无法满足`, `而无法` | 1/152 (1%) | 7/81 (9%) | 0/138 (0%) | 2/158 (1%) | 0/43 (0%) | 7/73 (10%) |
| candid (candid, frank) | truth | `坦诚` | 0/152 (0%) | 7/81 (9%) | 2/138 (1%) | 3/158 (2%) | 0/43 (0%) | 7/73 (10%) |
| secret (secret, secrecy) | lie | `秘密`, `的秘密`, `␣secret`, `␣secretly`, `␣secrecy`, `隐秘` | 4/152 (3%) | 2/81 (2%) | 0/138 (0%) | 0/158 (0%) | 3/43 (7%) | 1/73 (1%) |
| reveal (revealing) | truth | `␣revealed`, `␣reveal`, `␣revealing`, `揭露` | 0/152 (0%) | 5/81 (6%) | 0/138 (0%) | 0/158 (0%) | 0/43 (0%) | 5/73 (7%) |
| confess (confessing) | truth | `坦白`, `␣confess`, `␣confession` | 0/152 (0%) | 5/81 (6%) | 2/138 (1%) | 3/158 (2%) | 0/43 (0%) | 5/73 (7%) |
| disclose (disclosing, making known) | truth | `␣disclosure`, `␣Disclosure`, `␣disclosed`, `␣disclosing`, `␣disclose`, `␣disclosures`, `披露`, `公开` | 0/152 (0%) | 4/81 (5%) | 2/138 (1%) | 2/158 (1%) | 0/43 (0%) | 4/73 (5%) |
| ethics (ethics, morality) | unclear | `␣ethical`, `ethical`, `␣ethics`, `伦理` | 0/152 (0%) | 4/81 (5%) | 0/138 (0%) | 0/158 (0%) | 0/43 (0%) | 4/73 (5%) |
| transparent (transparency) | truth | `␣transparency`, `␣Transparency`, `透明` | 0/152 (0%) | 3/81 (4%) | 0/138 (0%) | 1/158 (1%) | 0/43 (0%) | 3/73 (4%) |
| unethical (morally wrong) | unclear | `␣unethical` | 3/152 (2%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 1/43 (2%) | 0/73 (0%) |
| evade (evading) | lie | `回避` | 2/152 (1%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 0/43 (0%) | 0/73 (0%) |
| reject (rejecting) | unclear | `␣rejecting`, `␣rejected`, `␣rejection`, `rejected` | 0/152 (0%) | 2/81 (2%) | 1/138 (1%) | 0/158 (0%) | 0/43 (0%) | 2/73 (3%) |
| confidential (confidential, kept private by duty) | unclear | `␣confidentiality`, `保密` | 0/152 (0%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 0/43 (0%) | 1/73 (1%) |
| undisclosed (not disclosed) | lie | `␣undisclosed` | 1/152 (1%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 1/43 (2%) | 0/73 (0%) |
| prohibited (prohibited, forbidden) | unclear | `禁止` | 0/152 (0%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 0/43 (0%) | 1/73 (1%) |
| unauthorized (unauthorized) | unclear | `␣unauthorized` | 0/152 (0%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 0/43 (0%) | 1/73 (1%) |
| inaccurate (inaccurate) | lie | `不准确` | 1/152 (1%) | 0/81 (0%) | 0/138 (0%) | 9/158 (6%) | 0/43 (0%) | 0/73 (0%) |

Not in the draft: misinformation (excluded: the question's own word); deny (excluded: admit / deny / acknowledge); admit (excluded: admit / deny / acknowledge); acknowledge (excluded: admit / deny / acknowledge); false (excluded: the question's own word)

## preans_slot2

| family | side | members | lies | truths | no-pressure truths | unrelated | lies that deny | truths that deny |
|---|---|---|---|---|---|---|---|---|
| fake (fake, counterfeit) | lie | `fake`, `Fake`, `␣fake`, `␣Fake`, `_fake` | 119/152 (78%) | 55/81 (68%) | 14/138 (10%) | 7/158 (4%) | 33/43 (77%) | 49/73 (67%) |
| conceal (hiding or withholding something) | lie | `隐瞒`, `␣hidden`, `隐藏`, `hidden`, `隐藏的`, `-hidden`, `␣concealed`, `␣Hidden`, `␣conceal`, `Hidden`, `␣hiding`, `隐蔽`, `瞒`, `hide` | 108/152 (71%) | 31/81 (38%) | 0/138 (0%) | 0/158 (0%) | 29/43 (67%) | 25/73 (34%) |
| conceal (the act of hiding or concealing) | lie | `隐瞒`, `掩盖`, `␣conceal`, `␣concealed`, `␣hiding`, `hide`, `隐藏`, `␣masking` | 108/152 (71%) | 31/81 (38%) | 0/138 (0%) | 0/158 (0%) | 29/43 (67%) | 25/73 (34%) |
| unethical (morally wrong) | unclear | `␣unethical`, `␣immoral` | 89/152 (59%) | 45/81 (56%) | 0/138 (0%) | 0/158 (0%) | 26/43 (60%) | 41/73 (56%) |
| fact (fact, factual) | truth | `␣fact`, `␣actually`, `␣actual`, `␣reality`, `actual`, `␣facts`, `Fact`, `Actual`, `fact`, `␣Actual`, `␣Actually`, `␣Fact`, `_actual`, `␣Reality`, `␣Facts`, `Reality`, `_fact`, `Actually`, `␣FACT`, `FACT`, `␣factual`, `facts`, `actually`, `实际`, `事实`, `实际上`, `实际情况`, `事实上`, `的事实`, `的实际`, `实际的`, `但实际上`, `实际上是`, `根据实际情况`, `认定事实`, `事实和`, `␣réalité` | 92/152 (61%) | 33/81 (41%) | 133/138 (96%) | 43/158 (27%) | 23/43 (53%) | 28/73 (38%) |
| fiction (fictional, made up) | unclear | `虚构`, `␣fictional`, `fiction`, `␣Fiction`, `␣fict`, `␣fiction`, `-fiction` | 79/152 (52%) | 44/81 (54%) | 62/138 (45%) | 36/158 (23%) | 22/43 (51%) | 41/73 (56%) |
| secret (secret, secrecy) | lie | `秘密`, `的秘密`, `␣secretly`, `␣secrecy`, `␣secret`, `secret`, `␣secretive`, `Secret`, `␣secrets`, `␣Secret`, `␣covert`, `隐秘`, `-secret`, `.secret`, `_secret` | 90/152 (59%) | 22/81 (27%) | 0/138 (0%) | 0/158 (0%) | 28/43 (65%) | 17/73 (23%) |
| true (true, real) | truth | `␣true`, `␣TRUE`, `真正`, `真实`, `确实`, `真正的`, `的确`, `真实的`, `是真的`, `真實`, `的真实`, `的真正` | 88/152 (58%) | 23/81 (28%) | 57/138 (41%) | 19/158 (12%) | 20/43 (47%) | 19/73 (26%) |
| honest (honest, truthful) | truth | `␣truthful`, `实事求是`, `␣honesty`, `诚实`, `如实` | 84/152 (55%) | 23/81 (28%) | 107/138 (78%) | 4/158 (3%) | 19/43 (44%) | 20/73 (27%) |
| confidential (confidential, kept private by duty) | unclear | `机密`, `␣confidentiality`, `保密`, `␣confidential`, `␣Confidential` | 67/152 (44%) | 20/81 (25%) | 0/138 (0%) | 0/158 (0%) | 25/43 (58%) | 15/73 (21%) |
| deceive (the act of deceiving) | lie | `欺骗`, `␣deception`, `␣deceptive`, `␣deceive`, `骗`, `骗子`, `骗局` | 58/152 (38%) | 17/81 (21%) | 0/138 (0%) | 0/158 (0%) | 11/43 (26%) | 16/73 (22%) |
| fabricate (fabricating / forging) | lie | `伪造`, `造假`, `␣fabricated`, `␣fabrication`, `弄虚作假` | 50/152 (33%) | 16/81 (20%) | 1/138 (1%) | 0/158 (0%) | 12/43 (28%) | 16/73 (22%) |
| lie (telling a lie) | lie | `谎言`, `说谎`, `谎`, `撒谎`, `␣mentira`, `␣lied`, `␣lying` | 51/152 (34%) | 10/81 (12%) | 0/138 (0%) | 0/158 (0%) | 11/43 (26%) | 9/73 (12%) |
| truth (the truth (as told or hidden)) | truth | `真实性`, `的真实性`, `其真实性` | 46/152 (30%) | 11/81 (14%) | 71/138 (51%) | 8/158 (5%) | 12/43 (28%) | 9/73 (12%) |
| violate (violating a rule) | unclear | `违背`, `违反`, `违规`, `␣violate`, `␣violates`, `违反了`, `␣violated`, `␣violating`, `␣violations` | 29/152 (19%) | 27/81 (33%) | 1/138 (1%) | 0/158 (0%) | 9/43 (21%) | 27/73 (37%) |
| pretend (pretending, feigning, disguise) | lie | `伪装`, `␣pretend`, `␣pretending`, `假装` | 40/152 (26%) | 9/81 (11%) | 2/138 (1%) | 1/158 (1%) | 12/43 (28%) | 8/73 (11%) |
| undisclosed (not disclosed) | lie | `␣undisclosed` | 35/152 (23%) | 9/81 (11%) | 0/138 (0%) | 0/158 (0%) | 11/43 (26%) | 6/73 (8%) |
| dishonest (dishonest) | lie | `␣dishonest` | 31/152 (20%) | 11/81 (14%) | 0/138 (0%) | 0/158 (0%) | 7/43 (16%) | 10/73 (14%) |
| ethics (ethics, morality) | unclear | `␣ethical`, `␣ethics`, `ethical`, `␣morally`, `道德`, `伦理`, `␣Ethics`, `的道德`, `␣moral`, `␣Moral`, `␣morality`, `职业道德`, `␣ethic`, `␣morals` | 17/152 (11%) | 21/81 (26%) | 0/138 (0%) | 0/158 (0%) | 6/43 (14%) | 20/73 (27%) |
| deliberate (on purpose) | unclear | `故意`, `␣intentionally`, `␣deliberately`, `␣intentional`, `␣deliberate`, `故意的`, `␣purposely` | 26/152 (17%) | 11/81 (14%) | 0/138 (0%) | 0/158 (0%) | 6/43 (14%) | 11/73 (15%) |
| mislead (misleading) | lie | `␣misleading`, `误导`, `误导性` | 24/152 (16%) | 8/81 (10%) | 2/138 (1%) | 1/158 (1%) | 3/43 (7%) | 8/73 (11%) |
| contradict (contradiction) | unclear | `␣contradict`, `␣contradictory`, `矛盾`, `␣contrad`, `␣contradiction`, `␣contradictions`, `矛盾的` | 13/152 (9%) | 19/81 (23%) | 17/138 (12%) | 1/158 (1%) | 5/43 (12%) | 18/73 (25%) |
| fraud (fraud, swindling) | lie | `␣fraudulent`, `弄虚作假`, `␣fraud`, `欺诈`, `骗局`, `骗子` | 22/152 (14%) | 9/81 (11%) | 0/138 (0%) | 0/158 (0%) | 2/43 (5%) | 9/73 (12%) |
| hidden (being hidden) | lie | `hidden`, `␣hidden`, `Hidden`, `␣Hidden`, `-hidden`, `隐藏的` | 27/152 (18%) | 4/81 (5%) | 0/138 (0%) | 0/158 (0%) | 11/43 (26%) | 3/73 (4%) |
| hypocrisy (hypocrisy) | lie | `␣hypocrisy`, `虚伪` | 18/152 (12%) | 12/81 (15%) | 0/138 (0%) | 0/158 (0%) | 6/43 (14%) | 11/73 (15%) |
| knowingly (with knowledge, knowingly) | unclear | `明知`, `␣knowing`, `␣knowingly`, `␣Knowing`, `Knowing` | 24/152 (16%) | 5/81 (6%) | 0/138 (0%) | 0/158 (0%) | 7/43 (16%) | 4/73 (5%) |
| knowingly (with knowledge, knowingly) | unclear | `␣knowingly`, `明知` | 22/152 (14%) | 5/81 (6%) | 0/138 (0%) | 0/158 (0%) | 7/43 (16%) | 4/73 (5%) |
| prohibited (prohibited, forbidden) | unclear | `禁止`, `␣prohibited`, `严禁`, `␣forbidden`, `␣forbid`, `Forbidden` | 9/152 (6%) | 17/81 (21%) | 0/138 (0%) | 3/158 (2%) | 6/43 (14%) | 17/73 (23%) |
| whistleblow (whistleblowing) | truth | `␣whistleblower`, `␣whistlebl` | 23/152 (15%) | 3/81 (4%) | 0/138 (0%) | 0/158 (0%) | 6/43 (14%) | 3/73 (4%) |
| illegal (illegal) | unclear | `非法`, `␣illegal`, `违法`, `illegal`, `Illegal`, `␣illegally`, `违法行为` | 12/152 (8%) | 12/81 (15%) | 0/138 (0%) | 0/158 (0%) | 5/43 (12%) | 12/73 (16%) |
| allege (alleging, purported) | unclear | `␣alleged`, `␣allegedly`, `␣allegation`, `␣allegations`, `␣purported` | 16/152 (11%) | 8/81 (10%) | 3/138 (2%) | 2/158 (1%) | 2/43 (5%) | 7/73 (10%) |
| cheat (cheating) | lie | `作弊` | 16/152 (11%) | 3/81 (4%) | 0/138 (0%) | 0/158 (0%) | 4/43 (9%) | 3/73 (4%) |
| unauthorized (unauthorized) | unclear | `␣unauthorized`, `␣Unauthorized` | 15/152 (10%) | 4/81 (5%) | 0/138 (0%) | 0/158 (0%) | 4/43 (9%) | 4/73 (5%) |
| wrong (wrong, mistaken) | lie | `␣ERROR`, `wrong`, `␣WRONG`, `误`, `错误`, `没错`, `的错误`, `是错误的` | 10/152 (7%) | 8/81 (10%) | 3/138 (2%) | 7/158 (4%) | 0/43 (0%) | 7/73 (10%) |
| refuse (refusing) | unclear | `拒绝`, `␣refusal`, `␣refusing`, `␣refused`, `␣refus`, `␣refuses`, `␣refuse`, `拒`, `拒絕`, `拒绝了`, `拒不` | 3/152 (2%) | 11/81 (14%) | 0/138 (0%) | 4/158 (3%) | 1/43 (2%) | 11/73 (15%) |
| misrepresent (misrepresenting) | lie | `␣misrepresented` | 4/152 (3%) | 6/81 (7%) | 1/138 (1%) | 0/158 (0%) | 0/43 (0%) | 6/73 (8%) |
| claim (claiming, asserting) | unclear | `␣claiming`, `␣claim`, `claim`, `␣claims`, `Claim`, `␣Claim`, `␣Claims`, `Claims`, `claims`, `␣claimed`, `␣CLAIM`, `CLAIM`, `_claim`, `␣asserting`, `␣assertions`, `assert`, `␣assertion`, `␣assert`, `␣asserted`, `␣asserts`, `␣Assert`, `Assert`, `声称`, `宣称` | 6/152 (4%) | 4/81 (5%) | 61/138 (44%) | 7/158 (4%) | 1/43 (2%) | 4/73 (5%) |
| incorrect (incorrect) | lie | `␣incorrect`, `Incorrect`, `␣inaccur`, `␣incorrectly`, `␣inaccurate`, `incorrect`, `␣wrongly`, `␣erroneous`, `␣Incorrect`, `错误的`, `不符合`, `不正确` | 5/152 (3%) | 4/81 (5%) | 6/138 (4%) | 31/158 (20%) | 0/43 (0%) | 3/73 (4%) |
| reveal (revealing, exposing) | truth | `揭露` | 7/152 (5%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 0/43 (0%) | 0/73 (0%) |
| disclaimer (disclaimer) | unclear | `␣disclaimer` | 2/152 (1%) | 5/81 (6%) | 8/138 (6%) | 7/158 (4%) | 1/43 (2%) | 5/73 (7%) |
| reject (rejecting) | unclear | `␣rejecting`, `␣rejected`, `␣rejection`, `rejected`, `reject`, `Rejected`, `␣reject`, `Reject`, `否决` | 1/152 (1%) | 4/81 (5%) | 0/138 (0%) | 0/158 (0%) | 0/43 (0%) | 4/73 (5%) |
| manipulate (manipulation) | lie | `␣manipulation`, `␣manipulated` | 3/152 (2%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 1/43 (2%) | 1/73 (1%) |
| wrongdoing (wrongdoing) | unclear | `␣wrongdoing` | 1/152 (1%) | 3/81 (4%) | 0/138 (0%) | 0/158 (0%) | 0/43 (0%) | 3/73 (4%) |
| cover up (covering up / glossing over) | lie | `掩盖` | 3/152 (2%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 1/43 (2%) | 0/73 (0%) |
| disclose (disclosing, making known) | truth | `␣disclosure`, `␣disclosed`, `␣disclosures`, `公开` | 2/152 (1%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 1/43 (2%) | 0/73 (0%) |
| negate (negating, saying it is not so) | unclear | `否定` | 3/152 (2%) | 0/81 (0%) | 1/138 (1%) | 3/158 (2%) | 0/43 (0%) | 0/73 (0%) |
| correct (correct) | truth | `␣correct`, `␣correctly`, `correct`, `␣correction`, `_correct`, `Correct`, `␣corrected`, `␣Correct`, `␣corrections`, `␣correctness`, `␣Correction`, `␣correcting`, `.correct`, `Correction`, `␣Corrections`, `正确`, `正确的`, `修正`, `纠错`, `正确答案`, `纠正`, `改正`, `的正确`, `更正`, `是正确的`, `正确地`, `是否正确`, `正确认识` | 0/152 (0%) | 3/81 (4%) | 29/138 (21%) | 65/158 (41%) | 0/43 (0%) | 2/73 (3%) |
| cannot (being unable / declining to answer) | unclear | `无法`, `无法满足`, `都无法`, `根本无法` | 2/152 (1%) | 0/81 (0%) | 0/138 (0%) | 6/158 (4%) | 0/43 (0%) | 0/73 (0%) |
| blame (blaming) | unclear | `␣blaming` | 1/152 (1%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 0/43 (0%) | 1/73 (1%) |
| evade (evading) | lie | `␣evade`, `␣evasion`, `回避` | 1/152 (1%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 1/43 (2%) | 0/73 (0%) |
| refute (refuting) | unclear | `␣refute` | 1/152 (1%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 0/43 (0%) | 0/73 (0%) |
| confess (confessing) | truth | `␣confess`, `␣confessed` | 1/152 (1%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 1/43 (2%) | 0/73 (0%) |
| clarify (clarifying) | unclear | `澄清` | 1/152 (1%) | 0/81 (0%) | 1/138 (1%) | 2/158 (1%) | 0/43 (0%) | 0/73 (0%) |
| accurate (accurate) | truth | `␣accurate`, `␣accuracy`, `␣accurately`, `accur` | 0/152 (0%) | 0/81 (0%) | 0/138 (0%) | 19/158 (12%) | 0/43 (0%) | 0/73 (0%) |

Not in the draft: misinformation (excluded: the question's own word); deny (excluded: admit / deny / acknowledge); admit (excluded: admit / deny / acknowledge); acknowledge (excluded: admit / deny / acknowledge); false (excluded: the question's own word)

## preans_slot3

| family | side | members | lies | truths | no-pressure truths | unrelated | lies that deny | truths that deny |
|---|---|---|---|---|---|---|---|---|
| cannot (being unable / declining to answer) | unclear | `␣Cannot`, `我无法`, `cannot`, `不能`, `Cannot`, `我不能`, `无法`, `是不能`, `できません` | 66/152 (43%) | 14/81 (17%) | 0/138 (0%) | 0/158 (0%) | 22/43 (51%) | 12/73 (16%) |
| true (true, real) | truth | `true`, `True`, `>true` | 13/152 (9%) | 1/81 (1%) | 48/138 (35%) | 1/158 (1%) | 2/43 (5%) | 0/73 (0%) |
| refuse (refusing) | unclear | `拒绝` | 4/152 (3%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 0/43 (0%) | 0/73 (0%) |
| incorrect (incorrect) | lie | `Incorrect`, `␣Incorrect` | 0/152 (0%) | 4/81 (5%) | 18/138 (13%) | 4/158 (3%) | 0/43 (0%) | 4/73 (5%) |
| apology (apologising) | unclear | `抱歉`, `␣Sorry` | 2/152 (1%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 2/43 (5%) | 1/73 (1%) |
| contradict (contradiction) | unclear | `矛盾` | 1/152 (1%) | 0/81 (0%) | 7/138 (5%) | 0/158 (0%) | 0/43 (0%) | 0/73 (0%) |
| correct (correct) | truth | `Correct`, `正确` | 0/152 (0%) | 0/81 (0%) | 5/138 (4%) | 0/158 (0%) | 0/43 (0%) | 0/73 (0%) |
| wrong (wrong, mistaken) | lie | `␣Wrong`, `错误` | 0/152 (0%) | 0/81 (0%) | 1/138 (1%) | 0/158 (0%) | 0/43 (0%) | 0/73 (0%) |

Not in the draft: false (excluded: the question's own word)

## preans_slot4

| family | side | members | lies | truths | no-pressure truths | unrelated | lies that deny | truths that deny |
|---|---|---|---|---|---|---|---|---|
| honest (honest, truthful) | truth | `␣truthful`, `␣honest`, `␣honesty`, `诚实`, `␣Honest`, `如实` | 147/152 (97%) | 79/81 (98%) | 112/138 (81%) | 35/158 (22%) | 42/43 (98%) | 72/73 (99%) |
| true (true, real) | truth | `␣true`, `true`, `True`, `␣True`, `␣TRUE`, `真实`, `确实`, `真实的`, `的真实` | 101/152 (66%) | 44/81 (54%) | 60/138 (43%) | 15/158 (9%) | 8/43 (19%) | 40/73 (55%) |
| fact (fact, factual) | truth | `␣reality`, `␣facts`, `␣Reality`, `␣Facts`, `␣factual`, `facts`, `事实` | 57/152 (38%) | 50/81 (62%) | 46/138 (33%) | 43/158 (27%) | 11/43 (26%) | 47/73 (64%) |
| lie (telling a lie) | lie | `谎言`, `说谎`, `撒谎` | 80/152 (53%) | 13/81 (16%) | 0/138 (0%) | 0/158 (0%) | 17/43 (40%) | 9/73 (12%) |
| incorrect (incorrect) | lie | `␣incorrect`, `Incorrect`, `␣inaccur`, `␣incorrectly`, `␣inaccurate`, `incorrect`, `␣erroneous`, `␣Incorrect`, `错误的`, `不符合`, `有误` | 27/152 (18%) | 40/81 (49%) | 93/138 (67%) | 146/158 (92%) | 7/43 (16%) | 37/73 (51%) |
| correct (correct) | truth | `␣correct`, `␣correctly`, `correct`, `␣correction`, `Correct`, `␣corrected`, `␣Correct`, `␣correctness`, `␣correcting`, `正确`, `正确的`, `修正`, `纠正`, `更正`, `是正确的`, `是否正确` | 9/152 (6%) | 47/81 (58%) | 134/138 (97%) | 127/158 (80%) | 4/43 (9%) | 46/73 (63%) |
| fake (fake, counterfeit) | lie | `fake`, `␣Fake`, `␣fake`, `Fake` | 39/152 (26%) | 12/81 (15%) | 0/138 (0%) | 4/158 (3%) | 8/43 (19%) | 9/73 (12%) |
| fiction (fictional, made up) | unclear | `虚构`, `␣fictional`, `␣Fiction`, `␣fict`, `fiction`, `␣fiction` | 31/152 (20%) | 11/81 (14%) | 1/138 (1%) | 14/158 (9%) | 7/43 (16%) | 9/73 (12%) |
| deceive (the act of deceiving) | lie | `欺骗`, `␣deception`, `␣deceptive` | 31/152 (20%) | 6/81 (7%) | 0/138 (0%) | 0/158 (0%) | 7/43 (16%) | 2/73 (3%) |
| conceal (hiding or withholding something) | lie | `隐瞒`, `␣Hidden` | 30/152 (20%) | 7/81 (9%) | 0/138 (0%) | 0/158 (0%) | 8/43 (19%) | 2/73 (3%) |
| misinformation (false information) | lie | `␣misinformation` | 19/152 (12%) | 17/81 (21%) | 3/138 (2%) | 17/158 (11%) | 7/43 (16%) | 13/73 (18%) |
| wrong (wrong, mistaken) | lie | `␣ERROR`, `␣Wrong`, `误`, `错误`, `的错误` | 6/152 (4%) | 17/81 (21%) | 49/138 (36%) | 129/158 (82%) | 1/43 (2%) | 14/73 (19%) |
| truth (the truth (as told or hidden)) | truth | `真实性`, `的真实性` | 12/152 (8%) | 6/81 (7%) | 2/138 (1%) | 0/158 (0%) | 0/43 (0%) | 6/73 (8%) |
| deliberate (on purpose) | unclear | `␣intentionally`, `␣intentional`, `␣deliberately`, `故意`, `␣deliberate`, `故意的`, `␣purposely` | 16/152 (11%) | 2/81 (2%) | 0/138 (0%) | 0/158 (0%) | 3/43 (7%) | 1/73 (1%) |
| accurate (accurate) | truth | `␣accurate`, `␣accuracy`, `␣accurately`, `accur`, `␣Accuracy` | 1/152 (1%) | 12/81 (15%) | 10/138 (7%) | 15/158 (9%) | 1/43 (2%) | 12/73 (16%) |
| mislead (misleading) | lie | `␣misleading` | 6/152 (4%) | 6/81 (7%) | 1/138 (1%) | 0/158 (0%) | 1/43 (2%) | 3/73 (4%) |
| negate (negating, saying it is not so) | unclear | `否定` | 10/152 (7%) | 2/81 (2%) | 0/138 (0%) | 0/158 (0%) | 10/43 (23%) | 2/73 (3%) |
| claim (claiming, asserting) | unclear | `␣assertions`, `␣assertion` | 9/152 (6%) | 2/81 (2%) | 0/138 (0%) | 1/158 (1%) | 9/43 (21%) | 2/73 (3%) |
| cannot (being unable / declining to answer) | unclear | `␣Cannot` | 6/152 (4%) | 2/81 (2%) | 0/138 (0%) | 5/158 (3%) | 2/43 (5%) | 1/73 (1%) |
| dishonest (dishonest) | lie | `␣dishonest` | 6/152 (4%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 0/43 (0%) | 1/73 (1%) |
| unethical (morally wrong) | unclear | `␣unethical` | 5/152 (3%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 0/43 (0%) | 0/73 (0%) |
| pretend (pretending, feigning, disguise) | lie | `伪装` | 2/152 (1%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 0/43 (0%) | 0/73 (0%) |
| ethics (ethics, morality) | unclear | `␣ethical` | 3/152 (2%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 0/43 (0%) | 0/73 (0%) |
| confidential (confidential, kept private by duty) | unclear | `␣confidentiality`, `保密` | 1/152 (1%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 0/43 (0%) | 0/73 (0%) |
| clarify (clarifying) | unclear | `澄清` | 2/152 (1%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 2/43 (5%) | 0/73 (0%) |
| apology (apologising) | unclear | `␣Sorry` | 2/152 (1%) | 0/81 (0%) | 0/138 (0%) | 1/158 (1%) | 2/43 (5%) | 0/73 (0%) |
| fraud (fraud, swindling) | lie | `␣fraudulent` | 1/152 (1%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 0/43 (0%) | 0/73 (0%) |
| fabricate (fabricating / forging) | lie | `伪造` | 1/152 (1%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 0/43 (0%) | 0/73 (0%) |
| refute (refuting) | unclear | `␣refute` | 1/152 (1%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 1/43 (2%) | 0/73 (0%) |
| refuse (refusing) | unclear | `拒绝` | 0/152 (0%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 0/43 (0%) | 1/73 (1%) |
| reject (rejecting) | unclear | `␣Reject` | 1/152 (1%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 1/43 (2%) | 0/73 (0%) |
| knowingly (with knowledge, knowingly) | unclear | `␣knowingly` | 1/152 (1%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 0/43 (0%) | 0/73 (0%) |
| violate (violating a rule) | unclear | `违背` | 1/152 (1%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 0/43 (0%) | 0/73 (0%) |
| unauthorized (unauthorized) | unclear | `␣unauthorized` | 1/152 (1%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 0/43 (0%) | 0/73 (0%) |
| disclaimer (disclaimer) | unclear | `␣disclaimer` | 0/152 (0%) | 1/81 (1%) | 0/138 (0%) | 1/158 (1%) | 0/43 (0%) | 1/73 (1%) |
| hidden (being hidden) | lie | `␣Hidden` | 1/152 (1%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 1/43 (2%) | 0/73 (0%) |

Not in the draft: deny (excluded: admit / deny / acknowledge); admit (excluded: admit / deny / acknowledge); acknowledge (excluded: admit / deny / acknowledge); false (excluded: the question's own word)
