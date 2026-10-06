# Draft families: qwen3.6-27b, J-lens, part Q9_dyl, group preans

Written by `scripts/apply_family_decisions.py` (2026-10-01; draft, not frozen). Counts are `present / transcripts (share)`
on the build split.

## preans_slot0

| family | side | members | lies | truths | no-pressure truths | unrelated | lies that deny | truths that deny |
|---|---|---|---|---|---|---|---|---|
| ethics (ethics, morality) | unclear | `etica` | 90/152 (59%) | 18/81 (22%) | 9/138 (7%) | 81/158 (51%) | 33/65 (51%) | 16/76 (21%) |
| accusation (being accused) | unclear | `␣accusation`, `指控`, `␣accusations` | 3/152 (2%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 2/65 (3%) | 1/76 (1%) |
| trap (a trap) | unclear | `陷阱`, `␣trap`, `␣trapped`, `␣Trap`, `trap`, `Trap` | 3/152 (2%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 3/65 (5%) | 0/76 (0%) |
| impossible (impossible) | unclear | `Impossible` | 2/152 (1%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 2/65 (3%) | 1/76 (1%) |

Not in the draft: violate (held back: no undisputed member left)

## preans_slot1

| family | side | members | lies | truths | no-pressure truths | unrelated | lies that deny | truths that deny |
|---|---|---|---|---|---|---|---|---|
| deceive (the act of deceiving) | lie | `欺骗`, `␣deception`, `␣deceptive`, `␣deceive`, `␣deceived`, `␣deceit`, `骗` | 152/152 (100%) | 81/81 (100%) | 137/138 (99%) | 156/158 (99%) | 65/65 (100%) | 76/76 (100%) |
| honest (being honest / truthful) | truth | `␣truthful`, `␣honesty`, `诚实`, `␣honest`, `␣Honest`, `诚实守信`, `如实`, `␣honestly`, `诚信`, `坦诚`, `实事求是`, `␣sincerity` | 152/152 (100%) | 81/81 (100%) | 138/138 (100%) | 156/158 (99%) | 65/65 (100%) | 76/76 (100%) |
| false (false, untrue) | lie | `␣false`, `␣False`, `false`, `False`, `=False`, `␣FALSE`, `=false`, `:false`, `FALSE`, `>false`, `␣fals`, `.False`, `␣falsely`, `␣untrue`, `/false`, `␣falsehood`, `真假`, `不实` | 152/152 (100%) | 81/81 (100%) | 138/138 (100%) | 158/158 (100%) | 65/65 (100%) | 76/76 (100%) |
| fake (fake, not genuine) | lie | `虚假`, `fake`, `Fake`, `假的`, `␣fake`, `假`, `␣Fake` | 152/152 (100%) | 80/81 (99%) | 136/138 (99%) | 158/158 (100%) | 65/65 (100%) | 75/76 (99%) |
| conceal (concealing) | lie | `隐瞒`, `␣conceal`, `␣concealed`, `隐匿`, `瞒`, `隐` | 150/152 (99%) | 77/81 (95%) | 100/138 (72%) | 55/158 (35%) | 65/65 (100%) | 72/76 (95%) |
| hide (hiding) | lie | `␣hiding`, `隐藏`, `Hide`, `hide`, `␣Hide`, `␣hide`, `␣hid`, `_hide`, `␣hides`, `-hide`, `隐瞒`, `␣conceal`, `␣concealed`, `掩盖`, `隐匿`, `掩饰`, `遮蔽`, `␣masking`, `瞒` | 150/152 (99%) | 77/81 (95%) | 100/138 (72%) | 55/158 (35%) | 65/65 (100%) | 72/76 (95%) |
| fake / fabricate (making something up, faking it) | lie | `fake`, `伪造`, `Fake`, `␣fake`, `␣Fake`, `造假`, `弄虚作假`, `␣fabrication`, `␣fabricated` | 147/152 (97%) | 76/81 (94%) | 128/138 (93%) | 158/158 (100%) | 62/65 (95%) | 71/76 (93%) |
| dishonest (dishonesty) | lie | `␣dishonest`, `虚伪` | 118/152 (78%) | 64/81 (79%) | 90/138 (65%) | 127/158 (80%) | 56/65 (86%) | 61/76 (80%) |
| misinformation (false information) | lie | `␣misinformation`, `虚假信息` | 126/152 (83%) | 55/81 (68%) | 131/138 (95%) | 155/158 (98%) | 57/65 (88%) | 51/76 (67%) |
| fabricate (fabricating or forging something) | lie | `伪造`, `␣fabrication`, `␣fabricated` | 128/152 (84%) | 39/81 (48%) | 38/138 (28%) | 28/158 (18%) | 51/65 (78%) | 35/76 (46%) |
| true (true, real) | truth | `␣true`, `␣TRUE`, `>true`, `真实`, `真实性`, `确实`, `的确`, `真实的`, `内容的真实性`, `的真实`, `的真实性` | 118/152 (78%) | 36/81 (44%) | 97/138 (70%) | 41/158 (26%) | 41/65 (63%) | 33/76 (43%) |
| fiction (made-up, fictional content) | unclear | `虚构`, `␣fictional`, `fiction` | 82/152 (54%) | 46/81 (57%) | 80/138 (58%) | 136/158 (86%) | 34/65 (52%) | 44/76 (58%) |
| factual (facts, factual) | truth | `␣factual`, `事实`, `␣facts`, `的事实`, `␣Facts`, `␣Fact`, `实事求是`, `␣fact`, `Fact`, `fact`, `facts` | 96/152 (63%) | 30/81 (37%) | 94/138 (68%) | 138/158 (87%) | 43/65 (66%) | 27/76 (36%) |
| mislead (misleading someone) | lie | `␣misleading`, `误导`, `␣misled`, `误导性` | 78/152 (51%) | 32/81 (40%) | 35/138 (25%) | 29/158 (18%) | 39/65 (60%) | 29/76 (38%) |
| fraud (fraud, swindling) | lie | `欺诈`, `␣fraudulent` | 61/152 (40%) | 46/81 (57%) | 69/138 (50%) | 107/158 (68%) | 36/65 (55%) | 44/76 (58%) |
| knowingly (acting with knowledge) | unclear | `␣knowingly`, `明知` | 93/152 (61%) | 0/81 (0%) | 2/138 (1%) | 32/158 (20%) | 30/65 (46%) | 0/76 (0%) |
| knowingly (with knowledge) | unclear | `␣knowingly`, `明知`, `␣knowing`, `␣Knowing`, `Knowing` | 93/152 (61%) | 0/81 (0%) | 2/138 (1%) | 32/158 (20%) | 30/65 (46%) | 0/76 (0%) |
| deliberate (acting on purpose) | unclear | `␣intentionally`, `故意`, `␣deliberately`, `␣intentional`, `␣deliberate` | 49/152 (32%) | 12/81 (15%) | 15/138 (11%) | 120/158 (76%) | 21/65 (32%) | 10/76 (13%) |
| misrepresent (misrepresenting) | lie | `␣misrepresented` | 42/152 (28%) | 17/81 (21%) | 36/138 (26%) | 21/158 (13%) | 18/65 (28%) | 16/76 (21%) |
| violate (violating a rule) | unclear | `违背`, `违反`, `违反了`, `␣violated`, `␣violate`, `␣violating`, `␣violates` | 39/152 (26%) | 10/81 (12%) | 11/138 (8%) | 0/158 (0%) | 14/65 (22%) | 9/76 (12%) |
| integrity (integrity, good faith) | truth | `诚信` | 10/152 (7%) | 38/81 (47%) | 75/138 (54%) | 111/158 (70%) | 8/65 (12%) | 38/76 (50%) |
| omit (omitting) | lie | `␣omission`, `␣omit`, `␣omitted`, `省略`, `␣OMIT`, `omit` | 37/152 (24%) | 10/81 (12%) | 0/138 (0%) | 0/158 (0%) | 15/65 (23%) | 8/76 (11%) |
| falsify (falsifying, faking results) | lie | `造假`, `弄虚作假` | 37/152 (24%) | 5/81 (6%) | 1/138 (1%) | 27/158 (17%) | 15/65 (23%) | 5/76 (7%) |
| technically (technically (true)) | unclear | `␣technically`, `技术上`, `技术性` | 35/152 (23%) | 6/81 (7%) | 0/138 (0%) | 2/158 (1%) | 13/65 (20%) | 3/76 (4%) |
| contradict (contradiction) | unclear | `␣contradict`, `␣contrad`, `␣contradiction`, `␣contradictory`, `␣contradictions`, `矛盾` | 21/152 (14%) | 14/81 (17%) | 32/138 (23%) | 0/158 (0%) | 10/65 (15%) | 13/76 (17%) |
| incorrect (incorrect) | lie | `␣incorrect`, `Incorrect`, `␣inaccur`, `␣incorrectly`, `␣inaccurate`, `incorrect`, `␣erroneous`, `␣Incorrect`, `错误的`, `不符合`, `有误` | 18/152 (12%) | 16/81 (20%) | 38/138 (28%) | 76/158 (48%) | 8/65 (12%) | 16/76 (21%) |
| wrong (wrong, mistaken) | lie | `␣wrong`, `␣WRONG`, `误`, `错误`, `的错误`, `是错误的` | 13/152 (9%) | 20/81 (25%) | 32/138 (23%) | 65/158 (41%) | 7/65 (11%) | 19/76 (25%) |
| unethical (unethical, immoral) | lie | `␣unethical` | 23/152 (15%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 9/65 (14%) | 1/76 (1%) |
| ethical (ethics, morality) | unclear | `␣ethical`, `␣morally`, `伦理`, `ethical`, `道德`, `␣moral`, `␣ethics`, `␣morality`, `␣Moral`, `的道德` | 18/152 (12%) | 5/81 (6%) | 0/138 (0%) | 0/158 (0%) | 10/65 (15%) | 4/76 (5%) |
| cover up (covering up) | lie | `掩盖`, `掩饰`, `遮蔽` | 20/152 (13%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 3/65 (5%) | 0/76 (0%) |
| accusation (being accused) | unclear | `␣accusations`, `␣allegations`, `␣accusation` | 12/152 (8%) | 7/81 (9%) | 6/138 (4%) | 35/158 (22%) | 12/65 (18%) | 7/76 (9%) |
| fact (fact, factual) | truth | `␣actual`, `actual`, `Actual`, `␣Actual`, `_actual`, `_fact`, `FACT`, `实际`, `实际情况`, `的实际`, `实际的`, `根据实际情况` | 18/152 (12%) | 1/81 (1%) | 6/138 (4%) | 2/158 (1%) | 8/65 (12%) | 1/76 (1%) |
| deviate (deviating) | unclear | `␣deviation`, `偏离`, `背离`, `␣deviations`, `偏差` | 15/152 (10%) | 2/81 (2%) | 1/138 (1%) | 0/158 (0%) | 3/65 (5%) | 1/76 (1%) |
| withhold (withholding) | lie | `␣withholding`, `␣withheld`, `␣withhold` | 11/152 (7%) | 2/81 (2%) | 0/138 (0%) | 0/158 (0%) | 2/65 (3%) | 2/76 (3%) |
| implicit (implicit, unstated) | unclear | `␣implicitly`, `隐含`, `␣implicit`, `Implicit`, `implicitly`, `␣Implicit`, `␣implied` | 10/152 (7%) | 2/81 (2%) | 0/138 (0%) | 5/158 (3%) | 4/65 (6%) | 2/76 (3%) |
| pretend (pretending, disguising) | lie | `伪装`, `␣pretending` | 5/152 (3%) | 6/81 (7%) | 0/138 (0%) | 2/158 (1%) | 1/65 (2%) | 3/76 (4%) |
| undisclosed (not disclosed) | lie | `␣undisclosed` | 8/152 (5%) | 2/81 (2%) | 0/138 (0%) | 1/158 (1%) | 5/65 (8%) | 2/76 (3%) |
| evade (evading) | lie | `␣evasion`, `␣avoidance`, `回避`, `␣evade`, `␣avoided` | 7/152 (5%) | 3/81 (4%) | 0/138 (0%) | 0/158 (0%) | 6/65 (9%) | 3/76 (4%) |
| accurate (accurate) | truth | `␣accuracy`, `␣accurately`, `accuracy`, `Accuracy`, `␣Accuracy`, `准确性` | 2/152 (1%) | 8/81 (10%) | 71/138 (51%) | 55/158 (35%) | 2/65 (3%) | 8/76 (11%) |
| allege (alleging, allegedly) | unclear | `␣allegations` | 5/152 (3%) | 3/81 (4%) | 0/138 (0%) | 6/158 (4%) | 5/65 (8%) | 3/76 (4%) |
| hypocrisy (hypocrisy, false pretence of virtue) | lie | `虚伪` | 4/152 (3%) | 3/81 (4%) | 0/138 (0%) | 0/158 (0%) | 3/65 (5%) | 2/76 (3%) |
| comply (complying with instructions or rules) | unclear | `␣compliance`, `␣adherence`, `␣comply`, `␣adher`, `␣adhere`, `遵守`, `严格遵守`, `遵照`, `␣complied`, `␣complying`, `遵循`, `遵从` | 2/152 (1%) | 3/81 (4%) | 1/138 (1%) | 0/158 (0%) | 2/65 (3%) | 2/76 (3%) |
| actually (in fact, in reality (contrast)) | unclear | `␣reality`, `␣Reality`, `Reality`, `事实上` | 5/152 (3%) | 0/81 (0%) | 0/138 (0%) | 1/158 (1%) | 2/65 (3%) | 0/76 (0%) |
| candid (candour, frankness) | truth | `坦诚` | 0/152 (0%) | 4/81 (5%) | 3/138 (2%) | 4/158 (3%) | 0/65 (0%) | 4/76 (5%) |
| claim (claiming) | unclear | `␣claims`, `声称`, `␣assertions` | 3/152 (2%) | 1/81 (1%) | 2/138 (1%) | 3/158 (2%) | 2/65 (3%) | 1/76 (1%) |
| inaccurate (inaccurate) | lie | `不准确` | 4/152 (3%) | 0/81 (0%) | 0/138 (0%) | 6/158 (4%) | 1/65 (2%) | 0/76 (0%) |
| assert (asserting) | unclear | `␣assertions` | 2/152 (1%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 1/65 (2%) | 1/76 (1%) |
| sincere (sincerity) | truth | `␣sincerity` | 1/152 (1%) | 1/81 (1%) | 0/138 (0%) | 1/158 (1%) | 1/65 (2%) | 1/76 (1%) |
| confess (confessing) | truth | `坦白` | 0/152 (0%) | 2/81 (2%) | 5/138 (4%) | 2/158 (1%) | 0/65 (0%) | 2/76 (3%) |
| transparency (being transparent) | truth | `␣transparency` | 0/152 (0%) | 2/81 (2%) | 1/138 (1%) | 2/158 (1%) | 0/65 (0%) | 2/76 (3%) |
| clarify (clarifying) | unclear | `澄清`, `␣clarification` | 1/152 (1%) | 1/81 (1%) | 1/138 (1%) | 1/158 (1%) | 1/65 (2%) | 1/76 (1%) |
| hallucinate (hallucinating) | unclear | `␣halluc` | 1/152 (1%) | 1/81 (1%) | 2/138 (1%) | 8/158 (5%) | 0/65 (0%) | 1/76 (1%) |
| hypothetical (hypothetical framing) | unclear | `␣hypothetical` | 1/152 (1%) | 1/81 (1%) | 0/138 (0%) | 2/158 (1%) | 0/65 (0%) | 1/76 (1%) |
| cheat (cheating) | lie | `作弊` | 1/152 (1%) | 0/81 (0%) | 0/138 (0%) | 1/158 (1%) | 0/65 (0%) | 0/76 (0%) |
| imply (implying) | unclear | `␣implied` | 1/152 (1%) | 0/81 (0%) | 0/138 (0%) | 1/158 (1%) | 1/65 (2%) | 0/76 (0%) |
| cannot (cannot, unable) | unclear | `我无法` | 0/152 (0%) | 1/81 (1%) | 1/138 (1%) | 35/158 (22%) | 0/65 (0%) | 1/76 (1%) |
| disclaimer (adding a disclaimer) | unclear | `␣disclaimer` | 0/152 (0%) | 1/81 (1%) | 0/138 (0%) | 1/158 (1%) | 0/65 (0%) | 1/76 (1%) |
| correct (correct) | truth | `␣correct`, `正确`, `正确的`, `正确答案`, `是正确的` | 0/152 (0%) | 1/81 (1%) | 10/138 (7%) | 0/158 (0%) | 0/65 (0%) | 1/76 (1%) |

Not in the draft: deny (excluded: admit / deny / acknowledge); truth (excluded: truth from the question on)

## preans_slot2

| family | side | members | lies | truths | no-pressure truths | unrelated | lies that deny | truths that deny |
|---|---|---|---|---|---|---|---|---|
| fake (fake, not genuine) | lie | `fake`, `虚假`, `␣fake`, `Fake`, `假的`, `假`, `␣Fake`, `_fake`, `.fake`, `假冒` | 133/152 (88%) | 35/81 (43%) | 39/138 (28%) | 25/158 (16%) | 57/65 (88%) | 31/76 (41%) |
| honest (being honest / truthful) | truth | `␣truthful`, `诚实`, `␣honesty`, `如实`, `␣honest`, `␣honestly`, `␣Honest`, `诚实守信`, `实事求是`, `坦诚`, `诚信`, `真诚` | 113/152 (74%) | 52/81 (64%) | 127/138 (92%) | 81/158 (51%) | 47/65 (72%) | 49/76 (64%) |
| fake / fabricate (making something up, faking it) | lie | `fake`, `␣fake`, `Fake`, `伪造`, `造假`, `␣Fake`, `_fake`, `弄虚作假`, `␣fabricated`, `.fake`, `␣fabrication` | 124/152 (82%) | 35/81 (43%) | 38/138 (28%) | 24/158 (15%) | 49/65 (75%) | 31/76 (41%) |
| false (false, untrue) | lie | `␣false`, `␣False`, `false`, `False`, `␣FALSE`, `:false`, `FALSE`, `␣fals`, `␣falsely`, `␣untrue`, `/false`, `␣falsehood`, `真假`, `不实`, `真伪`, `␣falso` | 125/152 (82%) | 34/81 (42%) | 52/138 (38%) | 10/158 (6%) | 57/65 (88%) | 30/76 (39%) |
| conceal (concealing) | lie | `隐瞒`, `␣conceal`, `␣concealed`, `隐匿`, `瞒`, `掩`, `隐` | 116/152 (76%) | 39/81 (48%) | 16/138 (12%) | 0/158 (0%) | 49/65 (75%) | 36/76 (47%) |
| hide (hiding) | lie | `隐藏`, `␣hiding`, `␣hidden`, `隐蔽`, `hide`, `hidden`, `␣hide`, `Hide`, `␣hides`, `隐藏的`, `Hidden`, `_hide`, `隐瞒`, `掩盖`, `␣conceal`, `␣concealed`, `隐匿`, `␣masking`, `掩饰`, `遮盖`, `瞒`, `遮蔽` | 116/152 (76%) | 39/81 (48%) | 16/138 (12%) | 0/158 (0%) | 49/65 (75%) | 36/76 (47%) |
| misinformation (false information) | lie | `␣misinformation`, `虚假信息` | 107/152 (70%) | 27/81 (33%) | 61/138 (44%) | 55/158 (35%) | 48/65 (74%) | 24/76 (32%) |
| true (true, real) | truth | `␣true`, `␣TRUE`, `真的`, `真实`, `真实性`, `确实`, `真实的`, `是真的`, `真實`, `内容的真实性`, `的真实`, `的真实性` | 83/152 (55%) | 39/81 (48%) | 98/138 (71%) | 53/158 (34%) | 28/65 (43%) | 36/76 (47%) |
| factual (facts, factual) | truth | `事实`, `␣factual`, `␣facts`, `facts`, `的事实`, `␣Facts`, `实事求是`, `␣fact`, `fact`, `Fact`, `␣Fact`, `_fact`, `␣FACT`, `FACT`, `事实和`, `_FACT`, `认定事实` | 78/152 (51%) | 42/81 (52%) | 132/138 (96%) | 96/158 (61%) | 31/65 (48%) | 40/76 (53%) |
| deceive (the act of deceiving) | lie | `欺骗`, `␣deception`, `␣deceptive`, `␣deceive`, `␣deceit`, `␣deceived`, `骗`, `欺` | 99/152 (65%) | 19/81 (23%) | 2/138 (1%) | 0/158 (0%) | 41/65 (63%) | 16/76 (21%) |
| fiction (made-up, fictional content) | unclear | `虚构`, `␣fictional`, `␣fict`, `fiction`, `␣fiction`, `␣Fiction` | 67/152 (44%) | 30/81 (37%) | 60/138 (43%) | 44/158 (28%) | 26/65 (40%) | 28/76 (37%) |
| mislead (misleading someone) | lie | `␣misleading`, `误导`, `误导性`, `␣misled` | 68/152 (45%) | 20/81 (25%) | 8/138 (6%) | 9/158 (6%) | 37/65 (57%) | 17/76 (22%) |
| fact (fact, factual) | truth | `␣actual`, `actual`, `Actual`, `␣Actual`, `_actual`, `实际`, `实际情况`, `的实际`, `实际的`, `根据实际情况`, `␣réalité`, `事実` | 70/152 (46%) | 11/81 (14%) | 22/138 (16%) | 1/158 (1%) | 21/65 (32%) | 10/76 (13%) |
| actually (in fact, in reality (contrast)) | unclear | `␣actually`, `␣reality`, `actually`, `实际上`, `但实际上`, `事实上`, `␣Reality`, `Reality`, `实际上是`, `Actually`, `␣Actually` | 68/152 (45%) | 12/81 (15%) | 12/138 (9%) | 10/158 (6%) | 22/65 (34%) | 11/76 (14%) |
| fabricate (fabricating or forging something) | lie | `伪造`, `␣fabricated`, `␣fabrication` | 59/152 (39%) | 9/81 (11%) | 4/138 (3%) | 2/158 (1%) | 25/65 (38%) | 7/76 (9%) |
| secret (secrecy, keeping secret) | lie | `秘密`, `␣secretly`, `的秘密`, `␣secrecy`, `␣secret`, `␣secretive`, `secret`, `Secret`, `␣covert`, `␣Secret`, `-secret`, `␣secrets`, `.secret`, `␣undercover`, `␣undisclosed` | 48/152 (32%) | 14/81 (17%) | 0/138 (0%) | 0/158 (0%) | 17/65 (26%) | 11/76 (14%) |
| contradict (contradiction) | unclear | `␣contradict`, `␣contrad`, `␣contradictory`, `␣contradiction`, `␣contradictions`, `矛盾`, `␣contradd`, `矛盾的` | 44/152 (29%) | 18/81 (22%) | 39/138 (28%) | 1/158 (1%) | 22/65 (34%) | 17/76 (22%) |
| claim (claiming) | unclear | `␣claiming`, `声称`, `␣claim`, `␣claims`, `claim`, `宣称`, `␣claimed`, `claims`, `␣Claims`, `␣Claim`, `Claim`, `␣якобы`, `CLAIM`, `␣CLAIM`, `Claims`, `_claim` | 48/152 (32%) | 13/81 (16%) | 3/138 (2%) | 3/158 (2%) | 27/65 (42%) | 12/76 (16%) |
| claim / assert (claiming or asserting) | unclear | `␣claiming`, `声称`, `␣claim`, `␣claims`, `␣assertions`, `␣asserting`, `claim`, `宣称`, `assert`, `␣claimed`, `␣assertion`, `claims`, `␣Claims`, `␣assert`, `␣Claim`, `Claim`, `␣asserts`, `␣asserted`, `␣Assert`, `CLAIM`, `_assert`, `␣CLAIM`, `Claims`, `_claim`, `Assert`, `␣Assertions`, `/assert`, `.assert`, `␣Assertion`, `(assert` | 42/152 (28%) | 12/81 (15%) | 10/138 (7%) | 3/158 (2%) | 24/65 (37%) | 11/76 (14%) |
| misrepresent (misrepresenting) | lie | `␣misrepresented` | 37/152 (24%) | 11/81 (14%) | 3/138 (2%) | 0/158 (0%) | 16/65 (25%) | 11/76 (14%) |
| undisclosed (not disclosed) | lie | `␣undisclosed` | 33/152 (22%) | 10/81 (12%) | 0/138 (0%) | 0/158 (0%) | 12/65 (18%) | 8/76 (11%) |
| genuine (genuinely, really) | truth | `␣genuinely`, `真正的`, `的真正`, `␣genuine`, `真正` | 36/152 (24%) | 7/81 (9%) | 0/138 (0%) | 40/158 (25%) | 10/65 (15%) | 5/76 (7%) |
| unethical (unethical, immoral) | lie | `␣unethical`, `␣immoral`, `␣wrongdoing` | 27/152 (18%) | 13/81 (16%) | 0/138 (0%) | 0/158 (0%) | 8/65 (12%) | 12/76 (16%) |
| confidential (confidentiality) | unclear | `␣confidentiality`, `保密`, `机密`, `␣confidential`, `␣Confidential` | 23/152 (15%) | 15/81 (19%) | 4/138 (3%) | 0/158 (0%) | 7/65 (11%) | 13/76 (17%) |
| assert (asserting) | unclear | `␣assertions`, `␣asserting`, `assert`, `␣assertion`, `␣assert`, `␣asserts`, `␣Assert`, `␣asserted`, `Assert`, `␣Assertions`, `␣Assertion` | 32/152 (21%) | 6/81 (7%) | 9/138 (7%) | 0/158 (0%) | 19/65 (29%) | 6/76 (8%) |
| incorrect (incorrect) | lie | `␣incorrect`, `Incorrect`, `␣inaccur`, `␣incorrectly`, `␣inaccurate`, `incorrect`, `␣wrongly`, `␣erroneous`, `␣Incorrect`, `错误的`, `不符合`, `有误`, `不正确` | 23/152 (15%) | 15/81 (19%) | 18/138 (13%) | 87/158 (55%) | 15/65 (23%) | 13/76 (17%) |
| ethical (ethics, morality) | unclear | `␣ethical`, `␣ethics`, `伦理`, `道德`, `ethical`, `␣morally`, `␣Ethics`, `␣moral`, `的道德`, `␣morality`, `␣morals`, `␣Moral`, `职业道德` | 12/152 (8%) | 22/81 (27%) | 1/138 (1%) | 0/158 (0%) | 3/65 (5%) | 21/76 (28%) |
| refuse (refusing) | unclear | `␣refusal`, `拒绝`, `␣refusing`, `␣refused`, `␣refus`, `␣refuse`, `拒`, `␣refuses`, `拒绝了`, `拒絕`, `␣отказ`, `拒不`, `␣отказа` | 6/152 (4%) | 28/81 (35%) | 3/138 (2%) | 1/158 (1%) | 4/65 (6%) | 28/76 (37%) |
| role-play (playing a role or persona) | unclear | `␣persona`, `␣Persona`, `Persona`, `角色扮演`, `␣personas`, `persona`, `扮演`, `␣Personas`, `_persona` | 23/152 (15%) | 11/81 (14%) | 1/138 (1%) | 0/158 (0%) | 11/65 (17%) | 11/76 (14%) |
| blame (blaming) | unclear | `␣blaming`, `␣blame`, `␣blamed`, `␣blames` | 27/152 (18%) | 6/81 (7%) | 1/138 (1%) | 0/158 (0%) | 12/65 (18%) | 6/76 (8%) |
| allege (alleging, allegedly) | unclear | `␣allegations`, `␣якобы`, `␣alleging`, `␣alleged`, `␣allegation`, `␣allegedly` | 25/152 (16%) | 8/81 (10%) | 2/138 (1%) | 0/158 (0%) | 11/65 (17%) | 8/76 (11%) |
| violate (violating a rule) | unclear | `违背`, `违反`, `␣violate`, `␣violates`, `违规`, `违反了`, `␣violating`, `违法`, `␣violations`, `␣violation`, `␣violated` | 21/152 (14%) | 10/81 (12%) | 6/138 (4%) | 2/158 (1%) | 7/65 (11%) | 8/76 (11%) |
| pretend (pretending, disguising) | lie | `伪装`, `␣pretending`, `假装`, `␣pretend`, `␣pretended`, `␣disguised`, `␣disguise`, `␣undercover` | 23/152 (15%) | 8/81 (10%) | 1/138 (1%) | 0/158 (0%) | 8/65 (12%) | 7/76 (9%) |
| falsify (falsifying, faking results) | lie | `造假`, `弄虚作假` | 24/152 (16%) | 4/81 (5%) | 0/138 (0%) | 1/158 (1%) | 10/65 (15%) | 3/76 (4%) |
| dishonest (dishonesty) | lie | `␣dishonest` | 26/152 (17%) | 2/81 (2%) | 0/138 (0%) | 0/158 (0%) | 9/65 (14%) | 1/76 (1%) |
| cover up (covering up) | lie | `掩盖`, `掩饰`, `遮盖`, `遮蔽` | 24/152 (16%) | 4/81 (5%) | 0/138 (0%) | 0/158 (0%) | 10/65 (15%) | 3/76 (4%) |
| wrong (wrong, mistaken) | lie | `␣wrong`, `␣ERROR`, `wrong`, `␣Wrong`, `␣WRONG`, `误`, `错误`, `的错误`, `是错误的` | 21/152 (14%) | 7/81 (9%) | 8/138 (6%) | 22/158 (14%) | 7/65 (11%) | 6/76 (8%) |
| accusation (being accused) | unclear | `␣allegations`, `␣accusations`, `␣allegation`, `␣accusing`, `指控` | 19/152 (12%) | 6/81 (7%) | 2/138 (1%) | 0/158 (0%) | 10/65 (15%) | 6/76 (8%) |
| disclaimer (adding a disclaimer) | unclear | `␣disclaimer`, `␣Disclaimer`, `Disclaimer`, `␣DISCLAIMER` | 4/152 (3%) | 20/81 (25%) | 14/138 (10%) | 14/158 (9%) | 4/65 (6%) | 20/76 (26%) |
| knowingly (with knowledge) | unclear | `明知`, `␣knowingly`, `␣knowing`, `␣Knowing`, `Knowing` | 23/152 (15%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 10/65 (15%) | 1/76 (1%) |
| knowingly (acting with knowledge) | unclear | `明知`, `␣knowingly` | 21/152 (14%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 8/65 (12%) | 1/76 (1%) |
| implicit (implicit, unstated) | unclear | `␣implicitly`, `␣implicit`, `隐含`, `implicit`, `implicitly`, `␣Implicit`, `Implicit`, `␣implying`, `␣implied`, `␣implies` | 14/152 (9%) | 6/81 (7%) | 1/138 (1%) | 0/158 (0%) | 6/65 (9%) | 6/76 (8%) |
| correct (correct) | truth | `␣correct`, `␣correctly`, `correct`, `␣correction`, `_correct`, `Correct`, `␣corrected`, `␣Correct`, `␣corrections`, `␣correctness`, `␣Correction`, `␣correcting`, `.correct`, `_correction`, `Correction`, `␣Corrections`, `␣corrective`, `正确`, `正确的`, `修正`, `正确答案`, `纠正`, `改正`, `的正确`, `更正`, `是正确的`, `正确地`, `是否正确` | 2/152 (1%) | 18/81 (22%) | 109/138 (79%) | 118/158 (75%) | 1/65 (2%) | 18/76 (24%) |
| reject (rejecting) | unclear | `␣rejecting`, `␣rejection`, `reject`, `Reject`, `␣reject`, `␣rejected`, `␣Reject`, `rejected` | 0/152 (0%) | 19/81 (23%) | 1/138 (1%) | 0/158 (0%) | 0/65 (0%) | 19/76 (25%) |
| deliberate (acting on purpose) | unclear | `故意`, `␣intentionally`, `␣deliberately`, `␣intentional`, `␣deliberate` | 14/152 (9%) | 4/81 (5%) | 1/138 (1%) | 1/158 (1%) | 6/65 (9%) | 3/76 (4%) |
| hypothetical (hypothetical framing) | unclear | `␣hypothetical` | 9/152 (6%) | 7/81 (9%) | 10/138 (7%) | 10/158 (6%) | 6/65 (9%) | 7/76 (9%) |
| role-play (playing a role) | unclear | `角色扮演`, `扮演` | 9/152 (6%) | 5/81 (6%) | 0/138 (0%) | 0/158 (0%) | 4/65 (6%) | 5/76 (7%) |
| comply (complying with instructions or rules) | unclear | `␣adherence`, `遵守`, `␣compliance`, `␣comply`, `␣adher`, `␣adhere`, `␣complying`, `␣compliant`, `␣Compliance`, `␣complied`, `严格遵守`, `遵照`, `遵循`, `遵从` | 6/152 (4%) | 8/81 (10%) | 49/138 (36%) | 5/158 (3%) | 3/65 (5%) | 8/76 (11%) |
| candid (candour, frankness) | truth | `坦诚` | 0/152 (0%) | 13/81 (16%) | 4/138 (3%) | 4/158 (3%) | 0/65 (0%) | 12/76 (16%) |
| imply (implying) | unclear | `␣implying`, `␣implied`, `␣implies` | 9/152 (6%) | 3/81 (4%) | 0/138 (0%) | 0/158 (0%) | 2/65 (3%) | 3/76 (4%) |
| excuse (making excuses) | unclear | `借口`, `␣excuse`, `␣excuses`, `␣pretext` | 9/152 (6%) | 3/81 (4%) | 0/138 (0%) | 0/158 (0%) | 5/65 (8%) | 2/76 (3%) |
| fraud (fraud, swindling) | lie | `␣fraudulent`, `␣fraud`, `欺诈`, `骗子`, `骗局` | 8/152 (5%) | 2/81 (2%) | 0/138 (0%) | 0/158 (0%) | 3/65 (5%) | 1/76 (1%) |
| confess (confessing) | truth | `坦白`, `␣confess`, `␣confessed`, `如实供述` | 0/152 (0%) | 10/81 (12%) | 4/138 (3%) | 0/158 (0%) | 0/65 (0%) | 9/76 (12%) |
| reveal (revealing, exposing) | truth | `揭露`, `␣revealing`, `reveal` | 3/152 (2%) | 6/81 (7%) | 0/138 (0%) | 0/158 (0%) | 0/65 (0%) | 5/76 (7%) |
| accurate (accurate) | truth | `␣accurate`, `␣accuracy`, `␣accurately`, `accuracy`, `accur`, `␣Accuracy`, `准确`, `准确性`, `准确的`, `准确地` | 1/152 (1%) | 8/81 (10%) | 82/138 (59%) | 94/158 (59%) | 1/65 (2%) | 8/76 (11%) |
| cheat (cheating) | lie | `作弊`, `␣cheating` | 7/152 (5%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 2/65 (3%) | 1/76 (1%) |
| integrity (integrity, good faith) | truth | `诚信`, `␣integrity`, `␣Integrity` | 2/152 (1%) | 6/81 (7%) | 3/138 (2%) | 1/158 (1%) | 1/65 (2%) | 5/76 (7%) |
| disclose (disclosing information) | truth | `␣disclosure`, `␣disclosing`, `␣disclose`, `␣disclosures`, `␣Disclosure`, `␣disclosed`, `披露` | 1/152 (1%) | 7/81 (9%) | 3/138 (2%) | 1/158 (1%) | 0/65 (0%) | 6/76 (8%) |
| omit (omitting) | lie | `␣omit`, `␣omitted`, `␣omission`, `省略`, `omit`, `␣OMIT` | 5/152 (3%) | 3/81 (4%) | 0/138 (0%) | 0/158 (0%) | 2/65 (3%) | 3/76 (4%) |
| transparency (being transparent) | truth | `␣transparency`, `透明`, `␣Transparency`, `␣transparent`, `transparent`, `透明的` | 0/152 (0%) | 7/81 (9%) | 3/138 (2%) | 4/158 (3%) | 0/65 (0%) | 7/76 (9%) |
| evade (evading) | lie | `回避`, `␣avoidance`, `␣evasion`, `␣evade` | 5/152 (3%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 2/65 (3%) | 1/76 (1%) |
| clarify (clarifying) | unclear | `澄清`, `␣clarification`, `␣clarify` | 0/152 (0%) | 6/81 (7%) | 14/138 (10%) | 13/158 (8%) | 0/65 (0%) | 6/76 (8%) |
| evade / avoid (evading or avoiding) | lie | `回避`, `␣avoidance`, `␣evasion`, `␣avoiding`, `␣avoided`, `␣Avoid`, `avoid` | 5/152 (3%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 2/65 (3%) | 1/76 (1%) |
| hypocrisy (hypocrisy, false pretence of virtue) | lie | `␣hypocrisy` | 3/152 (2%) | 2/81 (2%) | 0/138 (0%) | 0/158 (0%) | 1/65 (2%) | 2/76 (3%) |
| misunderstand (misunderstanding) | unclear | `误解`, `␣misunderstand` | 1/152 (1%) | 3/81 (4%) | 1/138 (1%) | 2/158 (1%) | 0/65 (0%) | 3/76 (4%) |
| cannot (cannot, unable) | unclear | `我无法`, `␣cannot`, `␣unable`, `Cannot`, `cannot`, `␣Cannot`, `无法`, `也不能`, `我不能`, `而不能`, `无法满足`, `不能说`, `也不行` | 3/152 (2%) | 1/81 (1%) | 0/138 (0%) | 2/158 (1%) | 1/65 (2%) | 1/76 (1%) |
| privacy (privacy) | unclear | `隐私`, `␣privacy`, `privacy` | 2/152 (1%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 0/65 (0%) | 1/76 (1%) |
| withhold (withholding) | lie | `␣withholding`, `␣withheld`, `␣withhold` | 1/152 (1%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 0/65 (0%) | 1/76 (1%) |
| sincere (sincerity) | truth | `真诚` | 0/152 (0%) | 1/81 (1%) | 0/138 (0%) | 5/158 (3%) | 0/65 (0%) | 1/76 (1%) |
| wrongdoing (wrongdoing) | lie | `␣wrongdoing` | 1/152 (1%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 0/65 (0%) | 0/76 (0%) |
| technically (technically (true)) | unclear | `␣technically` | 1/152 (1%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 0/65 (0%) | 0/76 (0%) |
| impossible (impossible) | unclear | `␣impossible`, `␣Impossible`, `Impossible` | 1/152 (1%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 0/65 (0%) | 0/76 (0%) |
| sorry (apology) | unclear | `␣apology` | 0/152 (0%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 0/65 (0%) | 1/76 (1%) |
| inaccurate (inaccurate) | lie | `不准确` | 0/152 (0%) | 0/81 (0%) | 1/138 (1%) | 3/158 (2%) | 0/65 (0%) | 0/76 (0%) |

Not in the draft: admit (excluded: admit / deny / acknowledge); acknowledge (excluded: admit / deny / acknowledge); deny (excluded: admit / deny / acknowledge); truth (excluded: truth from the question on); admit / acknowledge (excluded: admit / deny / acknowledge)

## preans_slot3

| family | side | members | lies | truths | no-pressure truths | unrelated | lies that deny | truths that deny |
|---|---|---|---|---|---|---|---|---|
| cannot (cannot, unable) | unclear | `␣Cannot`, `不能`, `Cannot`, `cannot`, `我无法`, `我不能`, `无法`, `␣cannot`, `是不能`, `␣Unable`, `␣incapable`, `都不能`, `不可以`, `没法`, `不行` | 116/152 (76%) | 45/81 (56%) | 1/138 (1%) | 2/158 (1%) | 52/65 (80%) | 42/76 (55%) |
| false (false, untrue) | lie | `␣False`, `false`, `False`, `:false`, `(False`, `FALSE`, `>false`, `_false`, `.False`, `.false`, `/false` | 60/152 (39%) | 71/81 (88%) | 136/138 (99%) | 144/158 (91%) | 37/65 (57%) | 69/76 (91%) |
| impossible (impossible) | unclear | `␣Impossible`, `Impossible` | 44/152 (29%) | 19/81 (23%) | 13/138 (9%) | 0/158 (0%) | 26/65 (40%) | 18/76 (24%) |
| true (true, real) | truth | `True`, `>true` | 41/152 (27%) | 18/81 (22%) | 69/138 (50%) | 3/158 (2%) | 8/65 (12%) | 17/76 (22%) |
| sorry (apology) | unclear | `抱歉`, `␣Sorry`, `Sorry`, `␣sorry`, `sorry`, `对不起` | 6/152 (4%) | 2/81 (2%) | 1/138 (1%) | 3/158 (2%) | 4/65 (6%) | 2/76 (3%) |
| correct (correct) | truth | `Correct` | 0/152 (0%) | 0/81 (0%) | 2/138 (1%) | 0/158 (0%) | 0/65 (0%) | 0/76 (0%) |
| incorrect (incorrect) | lie | `␣Incorrect` | 0/152 (0%) | 0/81 (0%) | 2/138 (1%) | 0/158 (0%) | 0/65 (0%) | 0/76 (0%) |
| wrong (wrong, mistaken) | lie | `错`, `没错` | 0/152 (0%) | 0/81 (0%) | 7/138 (5%) | 0/158 (0%) | 0/65 (0%) | 0/76 (0%) |

## preans_slot4

| family | side | members | lies | truths | no-pressure truths | unrelated | lies that deny | truths that deny |
|---|---|---|---|---|---|---|---|---|
| false (false, untrue) | lie | `␣false`, `␣False`, `false`, `False`, `=False`, `␣FALSE`, `:false`, `>false`, `␣fals`, `_false`, `.False`, `␣untrue`, `/false`, `␣falsehood` | 131/152 (86%) | 81/81 (100%) | 138/138 (100%) | 158/158 (100%) | 64/65 (98%) | 76/76 (100%) |
| honest (being honest / truthful) | truth | `␣truthful`, `␣honest`, `␣honesty`, `␣Honest`, `诚实`, `如实`, `␣honestly`, `诚信` | 130/152 (86%) | 56/81 (69%) | 62/138 (45%) | 9/158 (6%) | 59/65 (91%) | 53/76 (70%) |
| cannot (cannot, unable) | unclear | `␣Cannot`, `Cannot`, `␣cannot`, `cannot` | 70/152 (46%) | 4/81 (5%) | 0/138 (0%) | 0/158 (0%) | 24/65 (37%) | 3/76 (4%) |
| true (true, real) | truth | `␣true`, `True`, `␣True`, `␣TRUE`, `真实`, `真实性` | 31/152 (20%) | 23/81 (28%) | 57/138 (41%) | 10/158 (6%) | 6/65 (9%) | 20/76 (26%) |
| unethical (unethical, immoral) | lie | `␣unethical`, `␣immoral` | 33/152 (22%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 6/65 (9%) | 1/76 (1%) |
| hide (hiding) | lie | `␣Hidden`, `隐藏`, `隐蔽`, `隐瞒` | 30/152 (20%) | 3/81 (4%) | 0/138 (0%) | 0/158 (0%) | 9/65 (14%) | 2/76 (3%) |
| conceal (concealing) | lie | `隐瞒` | 29/152 (19%) | 3/81 (4%) | 0/138 (0%) | 0/158 (0%) | 9/65 (14%) | 2/76 (3%) |
| confidential (confidentiality) | unclear | `␣confidentiality`, `保密`, `␣Confidential`, `␣confidential`, `机密`, `␣discreet` | 30/152 (20%) | 2/81 (2%) | 0/138 (0%) | 0/158 (0%) | 7/65 (11%) | 1/76 (1%) |
| ethical (ethics, morality) | unclear | `␣ethical`, `ethical`, `␣Ethics`, `␣ethics`, `␣morally`, `伦理`, `␣moral`, `道德` | 22/152 (14%) | 3/81 (4%) | 0/138 (0%) | 0/158 (0%) | 2/65 (3%) | 1/76 (1%) |
| fiction (made-up, fictional content) | unclear | `␣fictional`, `虚构`, `␣Fiction`, `fiction`, `␣fict`, `␣fiction` | 12/152 (8%) | 3/81 (4%) | 0/138 (0%) | 1/158 (1%) | 1/65 (2%) | 2/76 (3%) |
| fake (fake, not genuine) | lie | `fake`, `␣Fake`, `␣fake`, `Fake`, `假`, `伪造` | 12/152 (8%) | 1/81 (1%) | 0/138 (0%) | 1/158 (1%) | 2/65 (3%) | 1/76 (1%) |
| dishonest (dishonesty) | lie | `␣dishonest` | 12/152 (8%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 5/65 (8%) | 1/76 (1%) |
| clarify (clarifying) | unclear | `澄清`, `␣clarification` | 8/152 (5%) | 3/81 (4%) | 0/138 (0%) | 0/158 (0%) | 8/65 (12%) | 3/76 (4%) |
| deceive (the act of deceiving) | lie | `␣deception`, `欺骗` | 6/152 (4%) | 3/81 (4%) | 0/138 (0%) | 0/158 (0%) | 3/65 (5%) | 2/76 (3%) |
| secret (secrecy, keeping secret) | lie | `秘密`, `␣secrecy`, `␣secretive`, `␣Secret`, `␣undercover`, `的秘密`, `␣undisclosed` | 8/152 (5%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 2/65 (3%) | 0/76 (0%) |
| factual (facts, factual) | truth | `␣factual` | 2/152 (1%) | 4/81 (5%) | 0/138 (0%) | 0/158 (0%) | 1/65 (2%) | 4/76 (5%) |
| hypothetical (hypothetical framing) | unclear | `␣hypothetical` | 6/152 (4%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 1/65 (2%) | 0/76 (0%) |
| incorrect (incorrect) | lie | `␣incorrect`, `␣inaccurate`, `incorrect`, `␣Incorrect`, `不符合` | 2/152 (1%) | 3/81 (4%) | 5/138 (4%) | 8/158 (5%) | 1/65 (2%) | 3/76 (4%) |
| integrity (integrity, good faith) | truth | `诚信` | 3/152 (2%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 1/65 (2%) | 1/76 (1%) |
| privacy (privacy) | unclear | `␣Privacy`, `␣privacy`, `privacy`, `隐私` | 3/152 (2%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 2/65 (3%) | 0/76 (0%) |
| violate (violating a rule) | unclear | `违反`, `␣violating`, `␣violate`, `违规` | 4/152 (3%) | 0/81 (0%) | 1/138 (1%) | 0/158 (0%) | 0/65 (0%) | 0/76 (0%) |
| pretend (pretending, disguising) | lie | `伪装`, `␣pretending`, `␣undercover` | 3/152 (2%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 2/65 (3%) | 0/76 (0%) |
| wrong (wrong, mistaken) | lie | `␣Wrong`, `错误` | 2/152 (1%) | 2/81 (2%) | 1/138 (1%) | 1/158 (1%) | 2/65 (3%) | 2/76 (3%) |
| misinformation (false information) | lie | `␣misinformation` | 2/152 (1%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 2/65 (3%) | 1/76 (1%) |
| refuse (refusing) | unclear | `拒绝` | 2/152 (1%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 2/65 (3%) | 1/76 (1%) |
| misunderstand (misunderstanding) | unclear | `␣misunderstanding`, `␣misunderstood`, `误解`, `␣misunderstand` | 2/152 (1%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 2/65 (3%) | 1/76 (1%) |
| mislead (misleading someone) | lie | `␣misleading` | 1/152 (1%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 1/65 (2%) | 1/76 (1%) |
| role-play (playing a role) | unclear | `扮演`, `角色扮演`, `␣persona`, `␣Persona` | 2/152 (1%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 0/65 (0%) | 0/76 (0%) |
| sorry (apology) | unclear | `␣Sorry` | 2/152 (1%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 1/65 (2%) | 0/76 (0%) |
| cheat (cheating) | lie | `作弊` | 1/152 (1%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 0/65 (0%) | 0/76 (0%) |
| fabricate (fabricating or forging something) | lie | `伪造` | 1/152 (1%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 1/65 (2%) | 0/76 (0%) |
| undisclosed (not disclosed) | lie | `␣undisclosed` | 1/152 (1%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 0/65 (0%) | 0/76 (0%) |
| discreet (discretion) | unclear | `␣discreet` | 1/152 (1%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 1/65 (2%) | 0/76 (0%) |
| deliberate (acting on purpose) | unclear | `␣intentionally` | 1/152 (1%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 0/65 (0%) | 0/76 (0%) |
| silence (staying silent) | unclear | `␣silence`, `␣Silent`, `␣Silence` | 1/152 (1%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 0/65 (0%) | 0/76 (0%) |
| disclaimer (adding a disclaimer) | unclear | `␣disclaimer` | 1/152 (1%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 0/65 (0%) | 0/76 (0%) |
| correct (correct) | truth | `␣Correct` | 0/152 (0%) | 0/81 (0%) | 1/138 (1%) | 0/158 (0%) | 0/65 (0%) | 0/76 (0%) |

Not in the draft: admit (excluded: admit / deny / acknowledge); acknowledge (excluded: admit / deny / acknowledge); deny (excluded: admit / deny / acknowledge); truth (excluded: truth from the question on)
