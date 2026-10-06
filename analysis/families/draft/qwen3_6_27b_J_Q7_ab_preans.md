# Draft families: qwen3.6-27b, J-lens, part Q7_ab, group preans

Written by `scripts/apply_family_decisions.py` (2026-10-01; draft, not frozen). Counts are `present / transcripts (share)`
on the build split.

## preans_slot0

| family | side | members | lies | truths | no-pressure truths | unrelated | lies that deny | truths that deny |
|---|---|---|---|---|---|---|---|---|

Not in the draft: violate (held back: no undisputed member left)

## preans_slot1

| family | side | members | lies | truths | no-pressure truths | unrelated | lies that deny | truths that deny |
|---|---|---|---|---|---|---|---|---|
| fake (fake, counterfeit) | lie | `fake`, `Fake`, `␣fake`, `假`, `␣Fake`, `假冒`, `_fake`, `假的`, `伪造`, `虚假`, `造假`, `弄虚作假` | 128/152 (84%) | 58/81 (72%) | 119/138 (86%) | 147/158 (93%) | 64/79 (81%) | 55/77 (71%) |
| hide (to hide; hidden) | lie | `␣hidden`, `隐藏`, `隐藏的`, `hidden`, `Hidden`, `␣Hidden`, `-hidden`, `隠`, `隐蔽`, `_hidden`, `隐瞒`, `隱藏`, `␣concealed`, `␣conceal`, `␣hiding`, `.hidden`, `隐匿` | 128/152 (84%) | 51/81 (63%) | 87/138 (63%) | 3/158 (2%) | 64/79 (81%) | 47/77 (61%) |
| fictional (fictional, made up) | unclear | `虚构`, `␣fictional`, `fiction`, `␣Fiction`, `␣fiction`, `-fiction`, `␣fict` | 118/152 (78%) | 53/81 (65%) | 114/138 (83%) | 143/158 (91%) | 56/79 (71%) | 50/77 (65%) |
| conceal (to conceal, cover up) | lie | `隐瞒`, `␣concealed`, `␣conceal`, `隐匿`, `隐` | 121/152 (80%) | 48/81 (59%) | 54/138 (39%) | 3/158 (2%) | 60/79 (76%) | 44/77 (57%) |
| unethical (unethical, immoral) | unclear | `␣unethical`, `␣immoral` | 99/152 (65%) | 54/81 (67%) | 6/138 (4%) | 55/158 (35%) | 49/79 (62%) | 52/77 (68%) |
| secret (secret, secretly, secrecy) | lie | `秘密`, `␣secretly`, `␣secret`, `的秘密`, `secret`, `Secret`, `␣secretive`, `暗中`, `.secret`, `隐秘`, `␣Secret`, `-secret`, `_secret`, `␣secrets`, `␣SECRET`, `␣covert`, `␣clandest`, `␣secrecy` | 110/152 (72%) | 35/81 (43%) | 21/138 (15%) | 0/158 (0%) | 52/79 (66%) | 31/77 (40%) |
| confidential (confidential, kept confidential) | lie | `机密`, `␣confidentiality`, `保密`, `␣confidential`, `␣Confidential` | 80/152 (53%) | 33/81 (41%) | 5/138 (4%) | 0/158 (0%) | 35/79 (44%) | 30/77 (39%) |
| intentional (intentional, deliberate) | unclear | `故意`, `␣intentionally`, `␣deliberately`, `␣intentional`, `␣deliberate`, `故意的` | 70/152 (46%) | 38/81 (47%) | 23/138 (17%) | 81/158 (51%) | 30/79 (38%) | 35/77 (45%) |
| violate (to violate (rules, instructions)) | unclear | `违背`, `违反`, `违规`, `␣violates`, `␣violate`, `␣violating`, `违反了`, `␣violated`, `␣violation`, `␣violations` | 47/152 (31%) | 52/81 (64%) | 53/138 (38%) | 2/158 (1%) | 26/79 (33%) | 52/77 (68%) |
| facts (the actual facts / real situation) | unclear | `事实`, `␣facts`, `␣factual`, `实际情况`, `␣Facts`, `facts`, `的事实`, `␣Fact`, `事实上`, `根据实际情况`, `Fact`, `␣fact`, `fact`, `FACT`, `事实和`, `␣FACT`, `_fact` | 83/152 (55%) | 14/81 (17%) | 82/138 (59%) | 130/158 (82%) | 46/79 (58%) | 11/77 (14%) |
| contradict (to contradict; contradictory) | unclear | `␣contradict`, `␣contradictory`, `矛盾`, `␣contradiction`, `␣conflicting`, `␣contradictions`, `矛盾的`, `␣contrad` | 52/152 (34%) | 42/81 (52%) | 104/138 (75%) | 14/158 (9%) | 34/79 (43%) | 41/77 (53%) |
| deceive (the act of deceiving) | lie | `欺骗`, `␣deception`, `␣deceptive`, `␣deceive`, `骗`, `欺` | 63/152 (41%) | 30/81 (37%) | 61/138 (44%) | 27/158 (17%) | 30/79 (38%) | 27/77 (35%) |
| fabricate (to fabricate or falsify) | lie | `伪造`, `造假`, `弄虚作假` | 50/152 (33%) | 28/81 (35%) | 25/138 (18%) | 6/158 (4%) | 26/79 (33%) | 26/77 (34%) |
| misinformation (misinformation) | lie | `␣misinformation`, `虚假信息` | 56/152 (37%) | 22/81 (27%) | 114/138 (83%) | 102/158 (65%) | 26/79 (33%) | 21/77 (27%) |
| knowingly (with knowledge (e.g. of the truth)) | unclear | `明知`, `␣knowingly`, `␣knowing`, `␣Knowing`, `Knowing` | 59/152 (39%) | 14/81 (17%) | 0/138 (0%) | 7/158 (4%) | 35/79 (44%) | 12/77 (16%) |
| knowingly (knowingly) | unclear | `明知`, `␣knowingly` | 59/152 (39%) | 13/81 (16%) | 0/138 (0%) | 7/158 (4%) | 35/79 (44%) | 11/77 (14%) |
| ethics (ethics, morality, ethical) | unclear | `␣ethical`, `ethical`, `␣ethics`, `伦理`, `道德`, `␣morally`, `␣Ethics`, `␣moral`, `的道德`, `␣morality`, `␣Moral`, `职业道德`, `␣ethic`, `␣morals` | 37/152 (24%) | 18/81 (22%) | 4/138 (3%) | 51/158 (32%) | 16/79 (20%) | 17/77 (22%) |
| pretend (to pretend) | lie | `假装`, `␣pretend`, `␣pretending`, `␣pretended`, `伪装`, `␣disguised` | 30/152 (20%) | 21/81 (26%) | 13/138 (9%) | 4/158 (3%) | 13/79 (16%) | 21/77 (27%) |
| fact (fact, factual) | truth | `␣actually`, `␣actual`, `␣reality`, `actual`, `Actual`, `␣Actual`, `␣Actually`, `_actual`, `␣Reality`, `Reality`, `Actually`, `actually`, `实际`, `实际上`, `的实际`, `实际的`, `实事求是`, `但实际上`, `␣réalité` | 43/152 (28%) | 7/81 (9%) | 2/138 (1%) | 25/158 (16%) | 30/79 (38%) | 5/77 (6%) |
| disguise (to disguise) | lie | `伪装`, `␣disguised` | 30/152 (20%) | 19/81 (23%) | 13/138 (9%) | 0/158 (0%) | 13/79 (16%) | 19/77 (25%) |
| cheat (to cheat) | lie | `作弊`, `␣cheating` | 31/152 (20%) | 10/81 (12%) | 3/138 (2%) | 0/158 (0%) | 17/79 (22%) | 10/77 (13%) |
| hypocrisy (hypocrisy) | lie | `␣hypocrisy`, `虚伪` | 22/152 (14%) | 12/81 (15%) | 1/138 (1%) | 0/158 (0%) | 15/79 (19%) | 12/77 (16%) |
| false (false, untrue) | lie | `␣false`, `␣False`, `false`, `False`, `␣FALSE`, `␣fals`, `␣falsely`, `␣untrue`, `/false` | 18/152 (12%) | 15/81 (19%) | 63/138 (46%) | 125/158 (79%) | 9/79 (11%) | 13/77 (17%) |
| dishonest (dishonest) | lie | `␣dishonest` | 18/152 (12%) | 7/81 (9%) | 0/138 (0%) | 13/158 (8%) | 9/79 (11%) | 6/77 (8%) |
| falsehood (an untrue statement) | lie | `␣falsehood` | 19/152 (12%) | 5/81 (6%) | 41/138 (30%) | 126/158 (80%) | 15/79 (19%) | 5/77 (6%) |
| refuse (to refuse; refusal) | unclear | `拒绝`, `␣refusal`, `␣refused`, `␣refusing`, `␣refus`, `拒绝了`, `拒`, `␣refuse`, `␣refuses`, `拒絕`, `拒不` | 4/152 (3%) | 18/81 (22%) | 1/138 (1%) | 1/158 (1%) | 3/79 (4%) | 18/77 (23%) |
| true (true, real) | truth | `␣true`, `真正`, `确实`, `真正的`, `是真的`, `真實`, `的真实性`, `的真正` | 17/152 (11%) | 4/81 (5%) | 1/138 (1%) | 11/158 (7%) | 15/79 (19%) | 3/77 (4%) |
| disclaimer (a hedging statement) | unclear | `␣disclaimer`, `␣Disclaimer` | 8/152 (5%) | 9/81 (11%) | 111/138 (80%) | 23/158 (15%) | 5/79 (6%) | 9/77 (12%) |
| undisclosed (not disclosed) | lie | `␣undisclosed` | 12/152 (8%) | 4/81 (5%) | 2/138 (1%) | 0/158 (0%) | 8/79 (10%) | 3/77 (4%) |
| illegal (illegal) | unclear | `␣illegal`, `非法`, `违法`, `␣illegally`, `Illegal`, `illegal` | 6/152 (4%) | 9/81 (11%) | 0/138 (0%) | 0/158 (0%) | 5/79 (6%) | 9/77 (12%) |
| incorrect (incorrect) | lie | `␣incorrect`, `Incorrect`, `␣incorrectly`, `␣inaccurate`, `incorrect`, `␣Incorrect`, `错误的`, `不符合` | 5/152 (3%) | 10/81 (12%) | 8/138 (6%) | 16/158 (10%) | 3/79 (4%) | 10/77 (13%) |
| honest (honest, honesty) | truth | `␣honesty`, `␣honest` | 7/152 (5%) | 3/81 (4%) | 13/138 (9%) | 74/158 (47%) | 5/79 (6%) | 3/77 (4%) |
| reject (to reject) | unclear | `reject`, `␣rejecting`, `␣rejection`, `␣Reject`, `Reject`, `␣reject`, `␣rejected`, `rejected`, `Rejected`, `.reject` | 1/152 (1%) | 8/81 (10%) | 0/138 (0%) | 0/158 (0%) | 1/79 (1%) | 8/77 (10%) |
| trap (a trap) | unclear | `陷阱`, `␣trap`, `␣traps`, `␣Trap`, `trap`, `Trap`, `␣trapping`, `␣trapped`, `_trap` | 3/152 (2%) | 5/81 (6%) | 10/138 (7%) | 2/158 (1%) | 3/79 (4%) | 5/77 (6%) |
| wrong (wrong, mistaken) | lie | `␣WRONG`, `错误` | 3/152 (2%) | 5/81 (6%) | 6/138 (4%) | 8/158 (5%) | 2/79 (3%) | 5/77 (6%) |
| mislead (to mislead) | lie | `误导`, `␣misleading` | 3/152 (2%) | 4/81 (5%) | 16/138 (12%) | 2/158 (1%) | 2/79 (3%) | 4/77 (5%) |
| fraud (fraud, swindling) | lie | `␣fraudulent`, `欺诈`, `␣fraud` | 4/152 (3%) | 2/81 (2%) | 1/138 (1%) | 1/158 (1%) | 2/79 (3%) | 2/77 (3%) |
| sabotage (to sabotage) | unclear | `␣sabotage` | 3/152 (2%) | 2/81 (2%) | 1/138 (1%) | 0/158 (0%) | 1/79 (1%) | 2/77 (3%) |
| correct (correct) | truth | `␣correct`, `␣correctly`, `correct`, `Correct`, `␣Correct`, `␣correctness`, `正确`, `正确的`, `正确答案`, `纠正`, `的正确`, `是正确的` | 1/152 (1%) | 4/81 (5%) | 2/138 (1%) | 10/158 (6%) | 0/79 (0%) | 4/77 (5%) |
| trick (to trick) | lie | `␣trick`, `␣Trick`, `␣tricks` | 1/152 (1%) | 3/81 (4%) | 8/138 (6%) | 3/158 (2%) | 1/79 (1%) | 3/77 (4%) |
| integrity (integrity) | truth | `␣integrity`, `␣Integrity`, `诚信` | 3/152 (2%) | 0/81 (0%) | 2/138 (1%) | 12/158 (8%) | 3/79 (4%) | 0/77 (0%) |
| withhold (to withhold) | lie | `␣withheld`, `␣withholding`, `␣withhold` | 1/152 (1%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 1/79 (1%) | 1/77 (1%) |
| manipulate (to manipulate) | lie | `␣manipulation`, `␣manipulate`, `␣manipulated` | 1/152 (1%) | 1/81 (1%) | 2/138 (1%) | 0/158 (0%) | 0/79 (0%) | 1/77 (1%) |
| evade (to evade or avoid) | lie | `回避`, `␣evasion` | 1/152 (1%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 1/79 (1%) | 1/77 (1%) |
| cannot (cannot, unable (refusal to answer)) | unclear | `无法`, `根本无法` | 2/152 (1%) | 0/81 (0%) | 0/138 (0%) | 15/158 (9%) | 2/79 (3%) | 0/77 (0%) |
| loyalty (loyalty) | unclear | `忠诚`, `忠诚度` | 2/152 (1%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 1/79 (1%) | 0/77 (0%) |
| omit (to omit; omission) | lie | `␣omit`, `␣omitted`, `␣OMIT`, `omit`, `␣omission` | 0/152 (0%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 0/79 (0%) | 1/77 (1%) |
| disclose (to disclose) | truth | `公开` | 1/152 (1%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 1/79 (1%) | 0/77 (0%) |
| reveal (to reveal or expose) | truth | `揭秘` | 1/152 (1%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 0/79 (0%) | 0/77 (0%) |
| betray (to betray) | unclear | `␣betrayal` | 1/152 (1%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 1/79 (1%) | 0/77 (0%) |
| silence (silence, staying silent) | unclear | `␣silence` | 0/152 (0%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 0/79 (0%) | 1/77 (1%) |
| privacy (private matters) | unclear | `隐私` | 1/152 (1%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 0/79 (0%) | 0/77 (0%) |
| crime (crime) | unclear | `␣crimes`, `␣criminal` | 1/152 (1%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 1/79 (1%) | 0/77 (0%) |
| accurate (accurate) | truth | `␣accurate`, `␣accuracy`, `␣accurately`, `accuracy`, `Accuracy`, `␣Accuracy` | 0/152 (0%) | 1/81 (1%) | 1/138 (1%) | 8/158 (5%) | 0/79 (0%) | 1/77 (1%) |

Not in the draft: admit (excluded: admit / deny / acknowledge); acknowledge (excluded: admit / deny / acknowledge); deny (excluded: admit / deny / acknowledge); liar (excluded: the question's own word); truth (the truth) (excluded: the question's own word)

## preans_slot2

| family | side | members | lies | truths | no-pressure truths | unrelated | lies that deny | truths that deny |
|---|---|---|---|---|---|---|---|---|
| fake (fake, counterfeit) | lie | `fake`, `␣fake`, `Fake`, `假`, `␣Fake`, `假的`, `_fake`, `␣counterfeit` | 100/152 (66%) | 50/81 (62%) | 36/138 (26%) | 15/158 (9%) | 49/79 (62%) | 49/77 (64%) |
| fake / forge (made to look real but not real) | lie | `fake`, `␣fake`, `Fake`, `伪造`, `虚假`, `␣Fake`, `假的`, `弄虚作假`, `造假`, `_fake`, `␣fabricated` | 100/152 (66%) | 50/81 (62%) | 36/138 (26%) | 14/158 (9%) | 49/79 (62%) | 49/77 (64%) |
| hide (to hide; hidden) | lie | `隐藏`, `␣hidden`, `hidden`, `-hidden`, `隐藏的`, `Hidden`, `隐蔽`, `hide`, `␣hide`, `Hide`, `␣hides`, `␣Hide`, `␣Hidden`, `_hide`, `-hide`, `隐瞒`, `␣conceal`, `␣hiding`, `␣concealed`, `瞒`, `:hidden`, `.isHidden`, `藏着` | 95/152 (62%) | 39/81 (48%) | 4/138 (3%) | 0/158 (0%) | 45/79 (57%) | 36/77 (47%) |
| conceal (to conceal, cover up) | lie | `隐瞒`, `␣conceal`, `掩盖`, `␣concealed`, `瞒`, `掩饰`, `隐` | 96/152 (63%) | 36/81 (44%) | 0/138 (0%) | 0/158 (0%) | 45/79 (57%) | 33/77 (43%) |
| unethical (unethical, immoral) | unclear | `␣unethical`, `␣immoral` | 78/152 (51%) | 49/81 (60%) | 1/138 (1%) | 0/158 (0%) | 41/79 (52%) | 48/77 (62%) |
| secret (secret, secretly, secrecy) | lie | `秘密`, `␣secretly`, `的秘密`, `␣secretive`, `␣secret`, `secret`, `Secret`, `隐秘`, `␣secrets`, `␣clandest`, `-secret`, `␣Secret`, `.secret`, `␣SECRET`, `_secret`, `暗中`, `␣covert`, `(secret`, `SECRET`, `␣secrecy`, `␣비밀` | 73/152 (48%) | 32/81 (40%) | 0/138 (0%) | 0/158 (0%) | 38/79 (48%) | 29/77 (38%) |
| misinformation (misinformation) | lie | `␣misinformation`, `虚假信息` | 73/152 (48%) | 30/81 (37%) | 59/138 (43%) | 8/158 (5%) | 33/79 (42%) | 28/77 (36%) |
| confidential (confidential, kept confidential) | lie | `保密`, `␣confidentiality`, `机密`, `␣confidential`, `␣Confidential` | 69/152 (45%) | 33/81 (41%) | 2/138 (1%) | 1/158 (1%) | 36/79 (46%) | 30/77 (39%) |
| fictional (fictional, made up) | unclear | `虚构`, `␣fictional`, `fiction`, `␣Fiction`, `␣fiction`, `␣fict` | 48/152 (32%) | 37/81 (46%) | 113/138 (82%) | 40/158 (25%) | 21/79 (27%) | 37/77 (48%) |
| facts (the actual facts / real situation) | unclear | `事实`, `␣facts`, `实际情况`, `␣factual`, `facts`, `的事实`, `␣Facts`, `事实上`, `␣fact`, `fact`, `Fact`, `根据实际情况`, `␣Fact`, `FACT`, `␣FACT` | 60/152 (39%) | 19/81 (23%) | 129/138 (93%) | 43/158 (27%) | 27/79 (34%) | 17/77 (22%) |
| violate (to violate (rules, instructions)) | unclear | `违背`, `违反`, `违规`, `␣violates`, `␣violate`, `␣violating`, `␣violated`, `␣violation`, `␣violations`, `违反了` | 33/152 (22%) | 29/81 (36%) | 3/138 (2%) | 1/158 (1%) | 18/79 (23%) | 28/77 (36%) |
| deceive (the act of deceiving) | lie | `欺骗`, `␣deception`, `␣deceptive`, `␣deceive`, `骗`, `␣deceived`, `骗取`, `骗子`, `␣deceit`, `欺` | 43/152 (28%) | 13/81 (16%) | 2/138 (1%) | 0/158 (0%) | 17/79 (22%) | 13/77 (17%) |
| false (false, untrue) | lie | `␣false`, `␣False`, `false`, `False`, `␣FALSE`, `FALSE`, `␣fals`, `␣falsely`, `␣untrue`, `/false`, `不实`, `真伪` | 37/152 (24%) | 14/81 (17%) | 8/138 (6%) | 1/158 (1%) | 16/79 (20%) | 14/77 (18%) |
| mislead (to mislead) | lie | `误导`, `␣misleading`, `␣misled`, `误导性` | 34/152 (22%) | 14/81 (17%) | 6/138 (4%) | 2/158 (1%) | 14/79 (18%) | 14/77 (18%) |
| pretend (to pretend) | lie | `␣pretending`, `假装`, `␣pretend`, `␣pretended`, `伪装`, `␣disguise`, `␣disguised` | 31/152 (20%) | 16/81 (20%) | 3/138 (2%) | 2/158 (1%) | 12/79 (15%) | 16/77 (21%) |
| fabricate (to fabricate or falsify) | lie | `伪造`, `弄虚作假`, `造假`, `␣fabricated` | 30/152 (20%) | 16/81 (20%) | 6/138 (4%) | 1/158 (1%) | 12/79 (15%) | 16/77 (21%) |
| intentional (intentional, deliberate) | unclear | `故意`, `␣intentionally`, `␣deliberately`, `␣intentional`, `␣deliberate` | 27/152 (18%) | 16/81 (20%) | 1/138 (1%) | 0/158 (0%) | 10/79 (13%) | 16/77 (21%) |
| disguise (to disguise) | lie | `伪装`, `␣disguise`, `␣disguised` | 30/152 (20%) | 10/81 (12%) | 2/138 (1%) | 0/158 (0%) | 12/79 (15%) | 10/77 (13%) |
| fact (fact, factual) | truth | `␣actually`, `␣actual`, `␣reality`, `actual`, `Actual`, `␣Actual`, `␣Actually`, `_FACT`, `_actual`, `␣Reality`, `Reality`, `_fact`, `Actually`, `actually`, `实际`, `实际上`, `的实际`, `实际的`, `实事求是`, `但实际上`, `实际上是`, `认定事实`, `事实和`, `␣réalité` | 34/152 (22%) | 5/81 (6%) | 93/138 (67%) | 14/158 (9%) | 14/79 (18%) | 5/77 (6%) |
| undisclosed (not disclosed) | lie | `␣undisclosed` | 27/152 (18%) | 8/81 (10%) | 0/138 (0%) | 0/158 (0%) | 12/79 (15%) | 6/77 (8%) |
| contradict (to contradict; contradictory) | unclear | `矛盾`, `␣contradictory`, `␣contradict`, `␣conflicting`, `␣contradiction`, `␣contradictions`, `矛盾的`, `␣contrad` | 13/152 (9%) | 22/81 (27%) | 7/138 (5%) | 0/158 (0%) | 7/79 (9%) | 21/77 (27%) |
| knowingly (with knowledge (e.g. of the truth)) | unclear | `明知`, `␣knowing`, `␣knowingly`, `␣Knowing`, `Knowing` | 26/152 (17%) | 8/81 (10%) | 1/138 (1%) | 0/158 (0%) | 13/79 (16%) | 7/77 (9%) |
| knowingly (knowingly) | unclear | `明知`, `␣knowingly` | 22/152 (14%) | 8/81 (10%) | 0/138 (0%) | 0/158 (0%) | 13/79 (16%) | 7/77 (9%) |
| true (true, real) | truth | `␣true`, `true`, `True`, `␣TRUE`, `:true`, `TRUE`, `>true`, `.isTrue`, `真的`, `真正`, `确实`, `真正的`, `的确`, `是真的`, `真實`, `的真实性`, `的真正` | 24/152 (16%) | 5/81 (6%) | 66/138 (48%) | 10/158 (6%) | 10/79 (13%) | 4/77 (5%) |
| hypocrisy (hypocrisy) | lie | `␣hypocrisy` | 15/152 (10%) | 12/81 (15%) | 0/138 (0%) | 0/158 (0%) | 10/79 (13%) | 12/77 (16%) |
| falsehood (an untrue statement) | lie | `␣falsehood` | 18/152 (12%) | 5/81 (6%) | 27/138 (20%) | 0/158 (0%) | 7/79 (9%) | 5/77 (6%) |
| ethics (ethics, morality, ethical) | unclear | `␣ethical`, `ethical`, `␣ethics`, `␣morally`, `伦理`, `道德`, `␣Ethics`, `␣moral`, `的道德` | 11/152 (7%) | 11/81 (14%) | 0/138 (0%) | 0/158 (0%) | 1/79 (1%) | 10/77 (13%) |
| sabotage (to sabotage) | unclear | `␣sabotage` | 13/152 (9%) | 8/81 (10%) | 1/138 (1%) | 0/158 (0%) | 7/79 (9%) | 8/77 (10%) |
| wrong (wrong, mistaken) | lie | `␣wrong`, `␣ERROR`, `wrong`, `␣WRONG`, `误`, `错误`, `的错误`, `是错误的` | 11/152 (7%) | 8/81 (10%) | 5/138 (4%) | 4/158 (3%) | 6/79 (8%) | 7/77 (9%) |
| misrepresent (to misrepresent) | lie | `␣misrepresented` | 15/152 (10%) | 3/81 (4%) | 0/138 (0%) | 0/158 (0%) | 7/79 (9%) | 3/77 (4%) |
| dishonest (dishonest) | lie | `␣dishonest` | 12/152 (8%) | 5/81 (6%) | 0/138 (0%) | 0/158 (0%) | 5/79 (6%) | 5/77 (6%) |
| fraud / scam (deceiving for gain) | lie | `␣fraudulent`, `␣fraud`, `欺诈`, `骗局`, `骗取`, `␣scams`, `␣Fraud`, `诈骗`, `骗子`, `␣scam`, `␣hoax` | 11/152 (7%) | 6/81 (7%) | 1/138 (1%) | 0/158 (0%) | 6/79 (8%) | 6/77 (8%) |
| illegal (illegal) | unclear | `␣illegal`, `非法`, `␣illegally`, `违法`, `illegal`, `违法行为`, `Illegal`, `␣Illegal`, `违法违规` | 8/152 (5%) | 8/81 (10%) | 0/138 (0%) | 0/158 (0%) | 3/79 (4%) | 8/77 (10%) |
| fraud (fraud, swindling) | lie | `␣fraudulent`, `␣fraud`, `欺诈`, `␣Fraud`, `诈骗` | 9/152 (6%) | 6/81 (7%) | 1/138 (1%) | 0/158 (0%) | 5/79 (6%) | 6/77 (8%) |
| cover up (covering over a fact) | lie | `掩盖`, `掩饰`, `掩护` | 12/152 (8%) | 3/81 (4%) | 0/138 (0%) | 0/158 (0%) | 2/79 (3%) | 3/77 (4%) |
| privacy (private matters) | unclear | `隐私`, `␣privacy`, `privacy`, `␣Privacy` | 9/152 (6%) | 6/81 (7%) | 0/138 (0%) | 0/158 (0%) | 5/79 (6%) | 5/77 (6%) |
| refuse (to refuse; refusal) | unclear | `拒绝`, `␣refusal`, `␣refused`, `␣refus`, `␣refusing`, `␣refuses` | 5/152 (3%) | 9/81 (11%) | 0/138 (0%) | 0/158 (0%) | 2/79 (3%) | 9/77 (12%) |
| disclose (to disclose) | truth | `␣disclosure`, `␣disclosed`, `␣disclosing`, `披露`, `信息披露`, `公开`, `␣disclose`, `␣Disclosure`, `信息公开`, `揭露`, `揭示` | 9/152 (6%) | 4/81 (5%) | 0/138 (0%) | 0/158 (0%) | 5/79 (6%) | 4/77 (5%) |
| propaganda (propaganda) | lie | `␣propaganda` | 11/152 (7%) | 2/81 (2%) | 0/138 (0%) | 0/158 (0%) | 6/79 (8%) | 2/77 (3%) |
| incorrect (incorrect) | lie | `␣incorrect`, `Incorrect`, `␣inaccur`, `␣incorrectly`, `␣inaccurate`, `incorrect`, `␣wrongly`, `␣erroneous`, `␣Incorrect`, `错误的`, `有误`, `不正确` | 9/152 (6%) | 3/81 (4%) | 5/138 (4%) | 16/158 (10%) | 4/79 (5%) | 3/77 (4%) |
| cheat (to cheat) | lie | `作弊`, `␣cheating` | 5/152 (3%) | 3/81 (4%) | 0/138 (0%) | 0/158 (0%) | 1/79 (1%) | 3/77 (4%) |
| manipulate (to manipulate) | lie | `␣manipulation`, `␣manipulated`, `␣manipulate`, `␣manipulating` | 4/152 (3%) | 3/81 (4%) | 1/138 (1%) | 0/158 (0%) | 2/79 (3%) | 3/77 (4%) |
| wrongdoing (wrongdoing) | unclear | `␣wrongdoing`, `␣wrongful` | 5/152 (3%) | 2/81 (2%) | 0/138 (0%) | 0/158 (0%) | 3/79 (4%) | 2/77 (3%) |
| reveal (to reveal or expose) | truth | `揭露` | 5/152 (3%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 2/79 (3%) | 1/77 (1%) |
| cannot (cannot, unable (refusal to answer)) | unclear | `无法`, `根本无法`, `cannot`, `␣Cannot`, `Cannot`, `␣cannot`, `无法满足`, `不能`, `是不能`, `绝对不能`, `绝不能`, `都不能`, `我们不能`, `你不能`, `又不能`, `而不能`, `不能说`, `不能让` | 4/152 (3%) | 1/81 (1%) | 0/138 (0%) | 7/158 (4%) | 1/79 (1%) | 1/77 (1%) |
| scam (a scam or hoax) | lie | `␣scams`, `骗局`, `␣scam`, `␣hoax` | 3/152 (2%) | 1/81 (1%) | 1/138 (1%) | 0/158 (0%) | 2/79 (3%) | 1/77 (1%) |
| omit (to omit; omission) | lie | `␣omit`, `␣omission`, `␣omitted`, `omit` | 1/152 (1%) | 2/81 (2%) | 0/138 (0%) | 0/158 (0%) | 0/79 (0%) | 2/77 (3%) |
| honest (honest, honesty) | truth | `␣honesty`, `␣honest`, `␣honestly`, `坦诚` | 2/152 (1%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 0/79 (0%) | 1/77 (1%) |
| confess (to confess) | truth | `␣confess`, `␣confessed`, `␣confession`, `坦白` | 2/152 (1%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 1/79 (1%) | 1/77 (1%) |
| disclaimer (a hedging statement) | unclear | `␣disclaimer` | 1/152 (1%) | 2/81 (2%) | 16/138 (12%) | 3/158 (2%) | 1/79 (1%) | 2/77 (3%) |
| crime (crime) | unclear | `犯罪事实`, `␣crimes`, `crime`, `犯罪` | 3/152 (2%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 1/79 (1%) | 0/77 (0%) |
| loyalty (loyalty) | unclear | `忠诚`, `忠诚度` | 1/152 (1%) | 2/81 (2%) | 0/138 (0%) | 0/158 (0%) | 1/79 (1%) | 2/77 (3%) |
| correct (correct) | truth | `␣correct`, `␣correctly`, `correct`, `␣correction`, `_correct`, `Correct`, `␣corrected`, `␣Correct`, `␣corrections`, `␣correctness`, `␣Correction`, `␣correcting`, `.correct`, `Correction`, `␣Corrections`, `正确`, `正确的`, `修正`, `纠错`, `正确答案`, `纠正`, `改正`, `的正确`, `更正`, `是正确的`, `正确地`, `是否正确` | 0/152 (0%) | 3/81 (4%) | 27/138 (20%) | 75/158 (47%) | 0/79 (0%) | 2/77 (3%) |
| betray (to betray) | unclear | `␣betray`, `背叛` | 1/152 (1%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 1/79 (1%) | 1/77 (1%) |
| pretext (a false pretext) | lie | `␣pretext` | 1/152 (1%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 0/79 (0%) | 0/77 (0%) |
| evade (to evade or avoid) | lie | `回避` | 1/152 (1%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 0/79 (0%) | 0/77 (0%) |
| candid (candid, frank) | truth | `坦诚` | 0/152 (0%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 0/79 (0%) | 1/77 (1%) |
| integrity (integrity) | truth | `␣integrity`, `␣Integrity` | 1/152 (1%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 1/79 (1%) | 0/77 (0%) |
| transparency (transparency) | truth | `␣transparency` | 0/152 (0%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 0/79 (0%) | 1/77 (1%) |
| reject (to reject) | unclear | `␣rejection` | 0/152 (0%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 0/79 (0%) | 1/77 (1%) |
| unintentional (unintentional) | unclear | `␣unintention` | 1/152 (1%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 0/79 (0%) | 0/77 (0%) |
| distort (twisting the facts) | lie | `␣distorted`, `␣distort` | 1/152 (1%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 1/79 (1%) | 0/77 (0%) |
| exaggerate (overstating) | lie | `夸大` | 1/152 (1%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 1/79 (1%) | 0/77 (0%) |
| clarify (making something clear / correcting a misunderstanding) | unclear | `澄清` | 0/152 (0%) | 1/81 (1%) | 1/138 (1%) | 0/158 (0%) | 0/79 (0%) | 1/77 (1%) |
| accurate (accurate) | truth | `␣accurate`, `␣accuracy`, `␣accurately`, `accur`, `准确`, `准确的`, `准确地` | 0/152 (0%) | 1/81 (1%) | 0/138 (0%) | 41/158 (26%) | 0/79 (0%) | 1/77 (1%) |

Not in the draft: admit (excluded: admit / deny / acknowledge); acknowledge (excluded: admit / deny / acknowledge); deny (excluded: admit / deny / acknowledge); liar (excluded: the question's own word); tell the truth (excluded: the question's own word); truth (the truth) (excluded: the question's own word)

## preans_slot3

| family | side | members | lies | truths | no-pressure truths | unrelated | lies that deny | truths that deny |
|---|---|---|---|---|---|---|---|---|
| cannot (cannot, unable (refusal to answer)) | unclear | `cannot`, `␣Cannot`, `Cannot`, `无法`, `我无法`, `不能`, `我不能`, `␣cannot`, `不能被`, `是不能`, `Unable`, `␣Unable`, `是无法`, `不能用`, `不能使用` | 119/152 (78%) | 38/81 (47%) | 0/138 (0%) | 1/158 (1%) | 62/79 (78%) | 37/77 (48%) |
| apology (sorry, apologize) | unclear | `抱歉`, `Sorry`, `␣Sorry`, `sorry`, `␣apologize`, `␣sorry` | 35/152 (23%) | 3/81 (4%) | 0/138 (0%) | 0/158 (0%) | 17/79 (22%) | 3/77 (4%) |
| disclaimer (a hedging statement) | unclear | `␣Disclaimer`, `␣DISCLAIMER` | 7/152 (5%) | 0/81 (0%) | 6/138 (4%) | 0/158 (0%) | 2/79 (3%) | 0/77 (0%) |
| ethics (ethics, morality, ethical) | unclear | `␣Moral`, `␣Ethics`, `道德` | 2/152 (1%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 0/79 (0%) | 0/77 (0%) |
| false (false, untrue) | lie | `false`, `False`, `FALSE`, `>false` | 1/152 (1%) | 1/81 (1%) | 53/138 (38%) | 11/158 (7%) | 1/79 (1%) | 1/77 (1%) |
| refuse (to refuse; refusal) | unclear | `拒绝`, `拒` | 1/152 (1%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 0/79 (0%) | 0/77 (0%) |
| contradict (to contradict; contradictory) | unclear | `矛盾` | 0/152 (0%) | 1/81 (1%) | 7/138 (5%) | 0/158 (0%) | 0/79 (0%) | 1/77 (1%) |
| fact (fact, factual) | truth | `Actually` | 0/152 (0%) | 0/81 (0%) | 0/138 (0%) | 1/158 (1%) | 0/79 (0%) | 0/77 (0%) |
| correct (correct) | truth | `正确答案` | 0/152 (0%) | 0/81 (0%) | 0/138 (0%) | 2/158 (1%) | 0/79 (0%) | 0/77 (0%) |

## preans_slot4

| family | side | members | lies | truths | no-pressure truths | unrelated | lies that deny | truths that deny |
|---|---|---|---|---|---|---|---|---|
| false (false, untrue) | lie | `␣false`, `␣False`, `false`, `False`, `␣FALSE`, `␣fals` | 132/152 (87%) | 48/81 (59%) | 67/138 (49%) | 11/158 (7%) | 68/79 (86%) | 44/77 (57%) |
| hide (to hide; hidden) | lie | `␣Hidden`, `hidden`, `␣hidden`, `隐藏`, `隐蔽`, `隠`, `隐瞒`, `␣concealed` | 105/152 (69%) | 9/81 (11%) | 0/138 (0%) | 0/158 (0%) | 38/79 (48%) | 6/77 (8%) |
| true (true, real) | truth | `␣true`, `True`, `␣True`, `␣TRUE`, `确实` | 57/152 (38%) | 48/81 (59%) | 31/138 (22%) | 8/158 (5%) | 17/79 (22%) | 46/77 (60%) |
| conceal (to conceal, cover up) | lie | `隐瞒`, `␣concealed`, `隐` | 89/152 (59%) | 9/81 (11%) | 0/138 (0%) | 0/158 (0%) | 34/79 (43%) | 6/77 (8%) |
| cannot (cannot, unable (refusal to answer)) | unclear | `␣Cannot`, `cannot`, `Cannot`, `␣cannot`, `␣Unable`, `无法`, `我无法`, `我不能`, `是无法` | 76/152 (50%) | 2/81 (2%) | 1/138 (1%) | 1/158 (1%) | 33/79 (42%) | 2/77 (3%) |
| correct (correct) | truth | `␣correct`, `Correct`, `␣Correct`, `正确`, `正确答案` | 6/152 (4%) | 47/81 (58%) | 92/138 (67%) | 12/158 (8%) | 6/79 (8%) | 47/77 (61%) |
| honest (honest, honesty) | truth | `␣Honest`, `␣honest`, `␣honesty` | 13/152 (9%) | 18/81 (22%) | 1/138 (1%) | 0/158 (0%) | 12/79 (15%) | 18/77 (23%) |
| falsehood (an untrue statement) | lie | `␣falsehood` | 28/152 (18%) | 3/81 (4%) | 1/138 (1%) | 0/158 (0%) | 14/79 (18%) | 3/77 (4%) |
| fake (fake, counterfeit) | lie | `␣Fake`, `fake`, `Fake`, `虚假` | 23/152 (15%) | 4/81 (5%) | 1/138 (1%) | 4/158 (3%) | 16/79 (20%) | 4/77 (5%) |
| secret (secret, secretly, secrecy) | lie | `秘密`, `␣Secret`, `␣secretly`, `的秘密`, `␣clandest`, `␣secrecy` | 19/152 (12%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 9/79 (11%) | 0/77 (0%) |
| undisclosed (not disclosed) | lie | `␣undisclosed` | 17/152 (11%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 9/79 (11%) | 0/77 (0%) |
| deceive (the act of deceiving) | lie | `欺骗` | 9/152 (6%) | 3/81 (4%) | 0/138 (0%) | 0/158 (0%) | 2/79 (3%) | 2/77 (3%) |
| confidential (confidential, kept confidential) | lie | `保密`, `␣confidentiality`, `␣Confidential` | 11/152 (7%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 7/79 (9%) | 0/77 (0%) |
| incorrect (incorrect) | lie | `␣incorrect`, `incorrect`, `␣Incorrect`, `不符合` | 4/152 (3%) | 7/81 (9%) | 14/138 (10%) | 5/158 (3%) | 3/79 (4%) | 7/77 (9%) |
| wrong (wrong, mistaken) | lie | `␣ERROR`, `␣Wrong`, `错误` | 4/152 (3%) | 6/81 (7%) | 14/138 (10%) | 1/158 (1%) | 4/79 (5%) | 6/77 (8%) |
| dishonest (dishonest) | lie | `␣dishonest` | 8/152 (5%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 2/79 (3%) | 1/77 (1%) |
| unethical (unethical, immoral) | unclear | `␣unethical` | 8/152 (5%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 2/79 (3%) | 1/77 (1%) |
| disguise (to disguise) | lie | `伪装` | 7/152 (5%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 3/79 (4%) | 0/77 (0%) |
| fictional (fictional, made up) | unclear | `虚构` | 3/152 (2%) | 0/81 (0%) | 1/138 (1%) | 0/158 (0%) | 1/79 (1%) | 0/77 (0%) |
| apology (sorry, apologize) | unclear | `␣Sorry`, `Sorry`, `抱歉` | 3/152 (2%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 2/79 (3%) | 0/77 (0%) |
| intentional (intentional, deliberate) | unclear | `␣intentionally`, `故意` | 3/152 (2%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 0/79 (0%) | 0/77 (0%) |
| violate (to violate (rules, instructions)) | unclear | `违反`, `违背` | 2/152 (1%) | 1/81 (1%) | 2/138 (1%) | 0/158 (0%) | 1/79 (1%) | 1/77 (1%) |
| disclaimer (a hedging statement) | unclear | `␣Disclaimer` | 3/152 (2%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 1/79 (1%) | 0/77 (0%) |
| refuse (to refuse; refusal) | unclear | `拒绝` | 2/152 (1%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 2/79 (3%) | 0/77 (0%) |
| silence (silence, staying silent) | unclear | `␣Silent`, `␣Silence` | 2/152 (1%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 2/79 (3%) | 0/77 (0%) |
| cheat (to cheat) | lie | `作弊` | 1/152 (1%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 0/79 (0%) | 0/77 (0%) |
| integrity (integrity) | truth | `␣Integrity` | 1/152 (1%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 1/79 (1%) | 0/77 (0%) |
| ethics (ethics, morality, ethical) | unclear | `␣ethical` | 0/152 (0%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 0/79 (0%) | 1/77 (1%) |
| clarify (making something clear / correcting a misunderstanding) | unclear | `澄清` | 1/152 (1%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 1/79 (1%) | 0/77 (0%) |
| fact (fact, factual) | truth | `␣Actually`, `Actually`, `actually` | 0/152 (0%) | 0/81 (0%) | 0/138 (0%) | 2/158 (1%) | 0/79 (0%) | 0/77 (0%) |

Not in the draft: admit (excluded: admit / deny / acknowledge); acknowledge (excluded: admit / deny / acknowledge); deny (excluded: admit / deny / acknowledge); truth (the truth) (excluded: the question's own word)
