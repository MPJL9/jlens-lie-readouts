# Draft families: qwen3.6-27b, logit lens, part Q7_ab, group postans

Written by `scripts/apply_family_decisions.py` (2026-10-01; draft, not frozen). Counts are `present / transcripts (share)`
on the build split.

## postans_slot0

| family | side | members | lies | truths | no-pressure truths | unrelated | lies that deny | truths that deny |
|---|---|---|---|---|---|---|---|---|
| sincere (sincere, earnest) | truth | `诚挚` | 151/152 (99%) | 80/81 (99%) | 121/138 (88%) | 31/158 (20%) | 79/79 (100%) | 76/77 (99%) |
| solemn (solemnly, in earnest) | unclear | `郑重` | 142/152 (93%) | 74/81 (91%) | 137/138 (99%) | 158/158 (100%) | 70/79 (89%) | 70/77 (91%) |
| reveal (reveal, uncover, expose) | truth | `揭` | 59/152 (39%) | 25/81 (31%) | 0/138 (0%) | 0/158 (0%) | 32/79 (41%) | 25/77 (32%) |
| deceive (the act of deceiving) | lie | `欺` | 18/152 (12%) | 30/81 (37%) | 80/138 (58%) | 42/158 (27%) | 16/79 (20%) | 30/77 (39%) |
| true (true, real) | truth | `␣real`, `real` | 12/152 (8%) | 13/81 (16%) | 0/138 (0%) | 0/158 (0%) | 2/79 (3%) | 11/77 (14%) |
| neutral (neutral stance) | unclear | `中立` | 7/152 (5%) | 16/81 (20%) | 97/138 (70%) | 59/158 (37%) | 5/79 (6%) | 16/77 (21%) |
| conceal (to conceal, to hide) | lie | `藏` | 0/152 (0%) | 0/81 (0%) | 1/138 (1%) | 0/158 (0%) | 0/79 (0%) | 0/77 (0%) |
| wrong (wrong, mistaken) | lie | `错` | 0/152 (0%) | 0/81 (0%) | 8/138 (6%) | 0/158 (0%) | 0/79 (0%) | 0/77 (0%) |

Not in the draft: fake (held back: no undisputed member left); fact (excluded: the question's own word)

## postans_slot1

| family | side | members | lies | truths | no-pressure truths | unrelated | lies that deny | truths that deny |
|---|---|---|---|---|---|---|---|---|
| fact (fact, factual) | truth | `␣factual`, `符合`, `事实`, `实际上`, `是否符合` | 121/152 (80%) | 74/81 (91%) | 136/138 (99%) | 106/158 (67%) | 73/79 (92%) | 72/77 (94%) |
| true (true, real) | truth | `␣true`, `true`, `True`, `␣True`, `real`, `␣genuine`, `真`, `确实`, `的确`, `成真` | 126/152 (83%) | 30/81 (37%) | 111/138 (80%) | 36/158 (23%) | 54/79 (68%) | 26/77 (34%) |
| conceal (hide, cover up) | lie | `-hide`, `藏`, `掩` | 105/152 (69%) | 48/81 (59%) | 10/138 (7%) | 10/158 (6%) | 38/79 (48%) | 44/77 (57%) |
| lawful (lawful, legal) | unclear | `合法`, `合法的` | 68/152 (45%) | 32/81 (40%) | 8/138 (6%) | 0/158 (0%) | 68/79 (86%) | 32/77 (42%) |
| comply (compliance with rules) | unclear | `合规`, `遵守` | 47/152 (31%) | 46/81 (57%) | 39/138 (28%) | 2/158 (1%) | 46/79 (58%) | 46/77 (60%) |
| upright (integrity, uprightness) | truth | `正直`, `诚信` | 35/152 (23%) | 48/81 (59%) | 11/138 (8%) | 1/158 (1%) | 13/79 (16%) | 48/77 (62%) |
| objective (objective, impartial) | unclear | `客观` | 56/152 (37%) | 22/81 (27%) | 8/138 (6%) | 9/158 (6%) | 26/79 (33%) | 22/77 (29%) |
| correct (correct) | truth | `valid`, `␣valid`, `␣correct`, `␣Valid`, `正确`, `正确的`, `纠正` | 24/152 (16%) | 39/81 (48%) | 76/138 (55%) | 5/158 (3%) | 19/79 (24%) | 39/77 (51%) |
| incorrect (incorrect) | lie | `不符合` | 42/152 (28%) | 9/81 (11%) | 0/138 (0%) | 0/158 (0%) | 7/79 (9%) | 7/77 (9%) |
| knowingly (acting with knowledge) | unclear | `明知` | 37/152 (24%) | 2/81 (2%) | 0/138 (0%) | 0/158 (0%) | 0/79 (0%) | 0/77 (0%) |
| ethics (ethics, morality) | unclear | `道德`, `␣moral`, `␣ethical`, `伦理` | 39/152 (26%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 1/79 (1%) | 0/77 (0%) |
| accurate (accurate) | truth | `␣accurate`, `␣accuracy`, `␣accurately`, `准确` | 20/152 (13%) | 18/81 (22%) | 41/138 (30%) | 7/158 (4%) | 3/79 (4%) | 17/77 (22%) |
| candid (candid, frank) | truth | `坦诚` | 35/152 (23%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 0/79 (0%) | 0/77 (0%) |
| honest (honest, honesty) | truth | `␣honesty`, `␣honest`, `诚信` | 35/152 (23%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 0/79 (0%) | 0/77 (0%) |
| critique (critique, criticism) | unclear | `␣critique` | 24/152 (16%) | 5/81 (6%) | 2/138 (1%) | 0/158 (0%) | 18/79 (23%) | 5/77 (6%) |
| false (false, untrue) | lie | `␣false`, `false`, `假`, `虚假`, `假的`, `真假` | 18/152 (12%) | 2/81 (2%) | 0/138 (0%) | 1/158 (1%) | 18/79 (23%) | 2/77 (3%) |
| ethical (ethics, ethical) | unclear | `␣ethical`, `伦理` | 13/152 (9%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 0/79 (0%) | 0/77 (0%) |
| apologize (apologize) | unclear | `道歉` | 11/152 (7%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 0/79 (0%) | 0/77 (0%) |
| private (private, not public) | unclear | `␣private` | 9/152 (6%) | 2/81 (2%) | 0/138 (0%) | 0/158 (0%) | 2/79 (3%) | 1/77 (1%) |
| violate (break a rule or law) | unclear | `违反`, `违法` | 7/152 (5%) | 3/81 (4%) | 0/138 (0%) | 0/158 (0%) | 2/79 (3%) | 2/77 (3%) |
| confess (confess, own up) | truth | `坦白`, `␣confession` | 9/152 (6%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 0/79 (0%) | 0/77 (0%) |
| deceive (deceive, cheat) | lie | `骗` | 8/152 (5%) | 1/81 (1%) | 1/138 (1%) | 2/158 (1%) | 8/79 (10%) | 1/77 (1%) |
| shame (shame, guilt) | unclear | `愧` | 7/152 (5%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 0/79 (0%) | 0/77 (0%) |
| faithful (faithful to the facts) | truth | `忠实` | 4/152 (3%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 2/79 (3%) | 0/77 (0%) |
| conscience (conscience) | unclear | `良心` | 4/152 (3%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 0/79 (0%) | 0/77 (0%) |
| right and wrong (right and wrong (moral judgement)) | unclear | `是非` | 2/152 (1%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 1/79 (1%) | 1/77 (1%) |
| regret (regret, repent) | unclear | `悔` | 3/152 (2%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 0/79 (0%) | 0/77 (0%) |
| wrong (wrong, mistaken) | lie | `␣wrong`, `不对` | 3/152 (2%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 3/79 (4%) | 0/77 (0%) |
| dishonest (not honest) | lie | `␣dishonest` | 1/152 (1%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 0/79 (0%) | 0/77 (0%) |
| disclose (disclose) | truth | `␣disclosure` | 1/152 (1%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 0/79 (0%) | 0/77 (0%) |

Not in the draft: admit (excluded: admit / deny / acknowledge); fib (held back: no undisputed member left); coerce (held back: no undisputed member left); truth (excluded: the question's own word)

## postans_slot2

| family | side | members | lies | truths | no-pressure truths | unrelated | lies that deny | truths that deny |
|---|---|---|---|---|---|---|---|---|
| critique (critique, criticism) | unclear | `␣critique`, `␣critical`, `批判`, `critical`, `␣Critical`, `␣critically`, `批评`, `Critical`, `␣criticism`, `␣critic`, `␣critiques` | 141/152 (93%) | 75/81 (93%) | 43/138 (31%) | 26/158 (16%) | 73/79 (92%) | 71/77 (92%) |
| reflect (self-reflection) | unclear | `反思` | 14/152 (9%) | 5/81 (6%) | 0/138 (0%) | 9/158 (6%) | 6/79 (8%) | 4/77 (5%) |
| comply (compliance with rules) | unclear | `合规` | 7/152 (5%) | 3/81 (4%) | 1/138 (1%) | 81/158 (51%) | 1/79 (1%) | 2/77 (3%) |
| correct (correct) | truth | `纠正` | 2/152 (1%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 0/79 (0%) | 0/77 (0%) |
| conceal (to conceal, to hide) | lie | `掩` | 0/152 (0%) | 0/81 (0%) | 1/138 (1%) | 0/158 (0%) | 0/79 (0%) | 0/77 (0%) |

## postans_slot3

| family | side | members | lies | truths | no-pressure truths | unrelated | lies that deny | truths that deny |
|---|---|---|---|---|---|---|---|---|
| critique (critique, criticism) | unclear | `批评`, `␣critically`, `␣critique`, `␣criticism`, `_critical`, `␣critical`, `Critical`, `␣critic`, `批判`, `␣Critical`, `␣criticisms`, `␣critica`, `critical`, `␣criticize`, `批評` | 32/152 (21%) | 17/81 (21%) | 9/138 (7%) | 0/158 (0%) | 6/79 (8%) | 15/77 (19%) |
| bias (biased, bias) | unclear | `␣biased`, `biased`, `bias` | 27/152 (18%) | 12/81 (15%) | 75/138 (54%) | 1/158 (1%) | 21/79 (27%) | 11/77 (14%) |
| unbiased (free of bias) | unclear | `␣unbiased` | 11/152 (7%) | 13/81 (16%) | 72/138 (52%) | 0/158 (0%) | 9/79 (11%) | 13/77 (17%) |
| suspected (suspected of wrongdoing) | unclear | `涉嫌` | 12/152 (8%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 11/79 (14%) | 1/77 (1%) |
| apologize (apologize) | unclear | `道歉`, `␣apology` | 7/152 (5%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 2/79 (3%) | 1/77 (1%) |
| violate (break a rule or law) | unclear | `违规` | 3/152 (2%) | 2/81 (2%) | 5/138 (4%) | 0/158 (0%) | 3/79 (4%) | 2/77 (3%) |
| harm (harm) | unclear | `␣harm` | 5/152 (3%) | 0/81 (0%) | 7/138 (5%) | 0/158 (0%) | 2/79 (3%) | 0/77 (0%) |
| wrong (wrong, mistaken) | lie | `␣mistake`, `␣flaw`, `错`, `谬`, `错了`, `是非` | 1/152 (1%) | 4/81 (5%) | 11/138 (8%) | 11/158 (7%) | 1/79 (1%) | 4/77 (5%) |
| reveal (reveal, uncover, expose) | truth | `揭` | 2/152 (1%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 2/79 (3%) | 1/77 (1%) |
| unfair (unfair) | unclear | `不公平` | 1/152 (1%) | 2/81 (2%) | 13/138 (9%) | 0/158 (0%) | 1/79 (1%) | 2/77 (3%) |
| fact (fact, factual) | truth | `求实` | 0/152 (0%) | 2/81 (2%) | 47/138 (34%) | 0/158 (0%) | 0/79 (0%) | 2/77 (3%) |
| comply (compliance with rules) | unclear | `遵守` | 1/152 (1%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 1/79 (1%) | 0/77 (0%) |
| sly (cunning, sly) | lie | `狡` | 1/152 (1%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 1/79 (1%) | 0/77 (0%) |
| conceal (to conceal, to hide) | lie | `掩` | 0/152 (0%) | 0/81 (0%) | 1/138 (1%) | 0/158 (0%) | 0/79 (0%) | 0/77 (0%) |
| correct (correct) | truth | `␣corrections`, `_correction`, `纠正`, `对的` | 0/152 (0%) | 0/81 (0%) | 3/138 (2%) | 9/158 (6%) | 0/79 (0%) | 0/77 (0%) |
| truth (the truth) | truth | `求真` | 0/152 (0%) | 0/81 (0%) | 1/138 (1%) | 0/158 (0%) | 0/79 (0%) | 0/77 (0%) |

## postans_slot4

| family | side | members | lies | truths | no-pressure truths | unrelated | lies that deny | truths that deny |
|---|---|---|---|---|---|---|---|---|
| right and wrong (right and wrong (moral judgement)) | unclear | `是非` | 132/152 (87%) | 74/81 (91%) | 131/138 (95%) | 139/158 (88%) | 75/79 (95%) | 71/77 (92%) |
| comply (compliance with rules) | unclear | `合规`, `␣compliance`, `遵守`, `␣Compliance`, `␣compliant`, `严格遵守` | 127/152 (84%) | 71/81 (88%) | 30/138 (22%) | 1/158 (1%) | 62/79 (78%) | 67/77 (87%) |
| ethics (ethics, morality) | unclear | `道德`, `␣ethical`, `␣ethics`, `伦理`, `的道德`, `␣moral`, `␣Ethics`, `ethical`, `␣morality`, `职业道德`, `␣morally`, `␣Moral`, `␣morals`, `␣ethic` | 116/152 (76%) | 43/81 (53%) | 1/138 (1%) | 0/158 (0%) | 54/79 (68%) | 41/77 (53%) |
| ethical (ethics, ethical) | unclear | `␣ethical`, `␣ethics`, `伦理`, `␣Ethics`, `ethical`, `␣ethic` | 105/152 (69%) | 41/81 (51%) | 1/138 (1%) | 0/158 (0%) | 47/79 (59%) | 39/77 (51%) |
| honest (honest, honesty) | truth | `␣honesty`, `␣honest`, `␣honestly`, `␣Honest`, `誠`, `诚信` | 88/152 (58%) | 20/81 (25%) | 3/138 (2%) | 0/158 (0%) | 35/79 (44%) | 20/77 (26%) |
| integrity (integrity, good faith) | truth | `␣integrity`, `诚信`, `␣Integrity`, `正直` | 77/152 (51%) | 18/81 (22%) | 1/138 (1%) | 0/158 (0%) | 28/79 (35%) | 18/77 (23%) |
| violate (break a rule or law) | unclear | `违反`, `违背`, `违规`, `违反了`, `␣violate`, `违法` | 71/152 (47%) | 17/81 (21%) | 39/138 (28%) | 1/158 (1%) | 18/79 (23%) | 15/77 (19%) |
| knowingly (acting with knowledge) | unclear | `明知`, `␣knowingly` | 62/152 (41%) | 22/81 (27%) | 38/138 (28%) | 0/158 (0%) | 40/79 (51%) | 20/77 (26%) |
| accurate (accurate) | truth | `␣accurate`, `␣accuracy`, `␣accurately`, `␣Accuracy`, `准确` | 65/152 (43%) | 19/81 (23%) | 14/138 (10%) | 2/158 (1%) | 33/79 (42%) | 18/77 (23%) |
| disclose (disclose, make public) | truth | `␣disclosure`, `公开`, `披露`, `␣disclosures`, `信息披露`, `透露` | 68/152 (45%) | 14/81 (17%) | 19/138 (14%) | 0/158 (0%) | 28/79 (35%) | 12/77 (16%) |
| integrity (integrity) | truth | `␣integrity`, `␣Integrity` | 58/152 (38%) | 14/81 (17%) | 1/138 (1%) | 0/158 (0%) | 22/79 (28%) | 14/77 (18%) |
| fact (fact, factual) | truth | `␣fact`, `␣reality`, `␣facts`, `Fact`, `fact`, `␣Fact`, `␣Reality`, `␣Facts`, `Reality`, `_fact`, `␣FACT`, `FACT`, `␣factual`, `facts`, `实际`, `符合`, `现实`, `事实`, `实际上`, `实际情况`, `事实上`, `的事实`, `是否符合`, `现实中`, `与现实`, `事实和` | 51/152 (34%) | 16/81 (20%) | 85/138 (62%) | 1/158 (1%) | 27/79 (34%) | 15/77 (19%) |
| hallucinate (produce false content unintentionally) | unclear | `␣halluc` | 45/152 (30%) | 17/81 (21%) | 19/138 (14%) | 1/158 (1%) | 29/79 (37%) | 17/77 (22%) |
| lure (bait, lure, induce) | unclear | `诱导`, `␣bait`, `诱`, `␣lure`, `诱惑`, `引诱` | 27/152 (18%) | 34/81 (42%) | 4/138 (3%) | 0/158 (0%) | 25/79 (32%) | 33/77 (43%) |
| coerce (force, coerce) | unclear | `迫使`, `␣forcing`, `␣forced`, `逼迫`, `forcing`, `被迫`, `强制`, `forced`, `强迫`, `␣Forced`, `胁迫`, `␣coerc`, `␣coercion`, `压迫`, `逼人`, `force`, `倒逼`, `forcer`, `被逼`, `FORCE` | 37/152 (24%) | 21/81 (26%) | 4/138 (3%) | 0/158 (0%) | 26/79 (33%) | 21/77 (27%) |
| trap (trap, trick question) | unclear | `陷阱`, `trap`, `␣trap`, `␣traps`, `Trap`, `␣Trap`, `␣trapped`, `␣trapping`, `_trap` | 21/152 (14%) | 31/81 (38%) | 8/138 (6%) | 0/158 (0%) | 18/79 (23%) | 31/77 (40%) |
| induce (induce, lead someone into) | unclear | `诱导` | 23/152 (15%) | 29/81 (36%) | 4/138 (3%) | 0/158 (0%) | 21/79 (27%) | 28/77 (36%) |
| deceive (the act of deceiving) | lie | `␣deception`, `欺骗`, `␣deceptive`, `骗`, `␣deceit`, `␣deceive`, `欺`, `哄` | 33/152 (22%) | 12/81 (15%) | 13/138 (9%) | 1/158 (1%) | 10/79 (13%) | 10/77 (13%) |
| role-play (playing a role) | unclear | `扮演`, `角色扮演` | 23/152 (15%) | 10/81 (12%) | 0/138 (0%) | 0/158 (0%) | 8/79 (10%) | 10/77 (13%) |
| bias (biased, bias) | unclear | `␣bias`, `␣biased` | 8/152 (5%) | 21/81 (26%) | 9/138 (7%) | 2/158 (1%) | 7/79 (9%) | 21/77 (27%) |
| dishonest (not honest) | lie | `␣dishonest` | 24/152 (16%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 1/79 (1%) | 0/77 (0%) |
| candid (candid, frank) | truth | `坦诚` | 23/152 (15%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 6/79 (8%) | 0/77 (0%) |
| correct (correct) | truth | `␣valid`, `␣correct`, `␣correctly`, `correct`, `Correct`, `␣Correct`, `正确`, `正确的`, `正确的是`, `纠正`, `是否正确` | 14/152 (9%) | 9/81 (11%) | 48/138 (35%) | 4/158 (3%) | 6/79 (8%) | 9/77 (12%) |
| unethical (not ethical) | unclear | `␣unethical` | 14/152 (9%) | 5/81 (6%) | 0/138 (0%) | 0/158 (0%) | 5/79 (6%) | 5/77 (6%) |
| harmful (harm, harmful) | unclear | `有害`, `␣harm`, `␣harmful` | 13/152 (9%) | 4/81 (5%) | 1/138 (1%) | 15/158 (9%) | 2/79 (3%) | 4/77 (5%) |
| deliberate (on purpose) | unclear | `故意`, `␣deliberately`, `␣deliberate`, `␣intentionally`, `刻意` | 8/152 (5%) | 8/81 (10%) | 3/138 (2%) | 6/158 (4%) | 5/79 (6%) | 7/77 (9%) |
| conceal (hide, cover up, hidden) | lie | `隐瞒`, `隐蔽`, `␣conceal`, `␣hidden`, `藏` | 9/152 (6%) | 6/81 (7%) | 2/138 (1%) | 0/158 (0%) | 2/79 (3%) | 5/77 (6%) |
| pressure (pressure) | unclear | `压力`, `␣pressure`, `␣pressures`, `␣Pressure`, `pressure`, `Pressure`, `␣pressured` | 11/152 (7%) | 4/81 (5%) | 0/138 (0%) | 0/158 (0%) | 6/79 (8%) | 4/77 (5%) |
| objective (objective, impartial) | unclear | `客观`, `␣objective`, `␣objectively` | 13/152 (9%) | 1/81 (1%) | 41/138 (30%) | 0/158 (0%) | 11/79 (14%) | 1/77 (1%) |
| trick (a trick) | unclear | `␣trick`, `␣tricks`, `␣Trick`, `套路` | 6/152 (4%) | 8/81 (10%) | 1/138 (1%) | 0/158 (0%) | 6/79 (8%) | 8/77 (10%) |
| reveal (reveal, uncover, expose) | truth | `揭`, `透露`, `揭露`, `暴露`, `揭示了`, `揭示`, `␣reveal` | 10/152 (7%) | 2/81 (2%) | 1/138 (1%) | 0/158 (0%) | 2/79 (3%) | 1/77 (1%) |
| intentional (deliberately) | unclear | `故意` | 4/152 (3%) | 6/81 (7%) | 3/138 (2%) | 6/158 (4%) | 3/79 (4%) | 6/77 (8%) |
| seek truth from facts (being realistic, true to the facts) | truth | `实事求是`, `求实` | 6/152 (4%) | 4/81 (5%) | 0/138 (0%) | 0/158 (0%) | 4/79 (5%) | 4/77 (5%) |
| incorrect (incorrect) | lie | `␣incorrect`, `不符合` | 7/152 (5%) | 3/81 (4%) | 8/138 (6%) | 0/158 (0%) | 5/79 (6%) | 3/77 (4%) |
| false (false, untrue) | lie | `␣fals`, `␣falsehood`, `虚假`, `真假` | 7/152 (5%) | 2/81 (2%) | 25/138 (18%) | 0/158 (0%) | 1/79 (1%) | 2/77 (3%) |
| confess (confess, own up) | truth | `坦白`, `␣confession`, `␣confess` | 7/152 (5%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 0/79 (0%) | 0/77 (0%) |
| transparent (transparency) | truth | `␣transparency`, `␣transparent`, `透明`, `透明的`, `透明度` | 5/152 (3%) | 2/81 (2%) | 0/138 (0%) | 0/158 (0%) | 0/79 (0%) | 2/77 (3%) |
| hidden (hidden, covert) | lie | `隐蔽`, `␣hidden` | 1/152 (1%) | 5/81 (6%) | 1/138 (1%) | 0/158 (0%) | 1/79 (1%) | 5/77 (6%) |
| true (true, real) | truth | `␣true`, `True`, `␣True`, `真`, `成立`, `确实`, `真正的` | 5/152 (3%) | 1/81 (1%) | 24/138 (17%) | 0/158 (0%) | 4/79 (5%) | 1/77 (1%) |
| fabricate (fabricate, make up, falsify) | lie | `虚构`, `␣fabricated`, `␣fabrication`, `造假`, `伪造` | 4/152 (3%) | 1/81 (1%) | 8/138 (6%) | 0/158 (0%) | 1/79 (1%) | 1/77 (1%) |
| manipulate (manipulate) | lie | `␣manipulation`, `␣manipulated`, `操纵`, `␣manipulating` | 1/152 (1%) | 3/81 (4%) | 0/138 (0%) | 0/158 (0%) | 1/79 (1%) | 3/77 (4%) |
| evasion (evade, avoid answering) | lie | `␣evasion` | 2/152 (1%) | 2/81 (2%) | 1/138 (1%) | 0/158 (0%) | 1/79 (1%) | 2/77 (3%) |
| fraud (fraud) | lie | `␣fraud`, `␣fraudulent`, `欺诈` | 4/152 (3%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 0/79 (0%) | 0/77 (0%) |
| conscience (conscience) | unclear | `良心` | 4/152 (3%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 0/79 (0%) | 0/77 (0%) |
| wrong (wrong, mistaken) | lie | `错`, `错了` | 2/152 (1%) | 2/81 (2%) | 7/138 (5%) | 0/158 (0%) | 0/79 (0%) | 2/77 (3%) |
| lawful (lawful, legal) | unclear | `合法` | 0/152 (0%) | 2/81 (2%) | 0/138 (0%) | 0/158 (0%) | 0/79 (0%) | 1/77 (1%) |
| upright (upright, of integrity) | truth | `正直` | 2/152 (1%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 1/79 (1%) | 0/77 (0%) |
| refusal (refusal) | unclear | `␣refusal` | 2/152 (1%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 1/79 (1%) | 0/77 (0%) |
| fair (fair, just) | unclear | `公平`, `公正` | 0/152 (0%) | 2/81 (2%) | 0/138 (0%) | 0/158 (0%) | 0/79 (0%) | 2/77 (3%) |
| fraud (fraud, swindle) | lie | `欺诈` | 1/152 (1%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 0/79 (0%) | 0/77 (0%) |
| mislead (mislead) | lie | `误导` | 0/152 (0%) | 1/81 (1%) | 1/138 (1%) | 0/158 (0%) | 0/79 (0%) | 0/77 (0%) |
| faithful (faithful to the facts) | truth | `忠实` | 1/152 (1%) | 0/81 (0%) | 1/138 (1%) | 0/158 (0%) | 0/79 (0%) | 0/77 (0%) |
| sly (cunning, sly) | lie | `狡` | 0/152 (0%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 0/79 (0%) | 1/77 (1%) |

Not in the draft: admit (excluded: admit / deny / acknowledge); fib (held back: no undisputed member left); coax (held back: no undisputed member left); deny (excluded: admit / deny / acknowledge); truth (excluded: the question's own word)
