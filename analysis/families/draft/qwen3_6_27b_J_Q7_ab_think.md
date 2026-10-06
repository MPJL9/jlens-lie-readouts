# Draft families: qwen3.6-27b, J-lens, part Q7_ab, group think

Written by `scripts/apply_family_decisions.py` (2026-10-01; draft, not frozen). Counts are `present / transcripts (share)`
on the build split.

## think_slot0

| family | side | members | lies | truths | no-pressure truths | unrelated | lies that deny | truths that deny |
|---|---|---|---|---|---|---|---|---|
| legal (legal, lawful) | unclear | `/legal`, `_legal`, `legal`, `合法`, `␣legality`, `Legal`, `␣Legal`, `␣legal`, `守法`, `依法`, `依法依规` | 152/152 (100%) | 81/81 (100%) | 137/138 (99%) | 158/158 (100%) | 79/79 (100%) | 77/77 (100%) |
| secret (secrecy, a secret) | lie | `隐秘`, `秘密` | 150/152 (99%) | 80/81 (99%) | 98/138 (71%) | 140/158 (89%) | 77/79 (97%) | 76/77 (99%) |
| implicit (implicit, unstated) | unclear | `隐含` | 152/152 (100%) | 78/81 (96%) | 116/138 (84%) | 87/158 (55%) | 79/79 (100%) | 74/77 (96%) |
| compliance (compliance) | unclear | `合规` | 142/152 (93%) | 68/81 (84%) | 121/138 (88%) | 52/158 (33%) | 77/79 (97%) | 66/77 (86%) |
| clarify (clarifying, setting the record straight) | unclear | `澄清` | 96/152 (63%) | 64/81 (79%) | 138/138 (100%) | 121/158 (77%) | 42/79 (53%) | 60/77 (78%) |
| illegal (illegal) | unclear | `违法违规`, `非法`, `违法`, `illegal`, `Illegal`, `违纪违法` | 102/152 (67%) | 51/81 (63%) | 63/138 (46%) | 54/158 (34%) | 60/79 (76%) | 50/77 (65%) |
| doubt (doubting or challenging (the claim)) | unclear | `质疑`, `疑`, `置疑`, `疑似` | 81/152 (53%) | 36/81 (44%) | 116/138 (84%) | 146/158 (92%) | 42/79 (53%) | 34/77 (44%) |
| fiction (fiction, fabricated story) | lie | `虚构` | 80/152 (53%) | 33/81 (41%) | 10/138 (7%) | 0/158 (0%) | 49/79 (62%) | 33/77 (43%) |
| hint (hinting, insinuating) | unclear | `暗示` | 81/152 (53%) | 26/81 (32%) | 68/138 (49%) | 88/158 (56%) | 44/79 (56%) | 25/77 (32%) |
| suppress (suppressing) | lie | `suppress` | 56/152 (37%) | 35/81 (43%) | 2/138 (1%) | 0/158 (0%) | 40/79 (51%) | 35/77 (45%) |
| hide (hiding something) | lie | `藏`, `隐` | 59/152 (39%) | 18/81 (22%) | 0/138 (0%) | 0/158 (0%) | 20/79 (25%) | 15/77 (19%) |
| fake (fake, forged) | lie | `fake`, `.fake`, `假` | 16/152 (11%) | 9/81 (11%) | 3/138 (2%) | 0/158 (0%) | 10/79 (13%) | 9/77 (12%) |
| violate (violating a rule) | unclear | `违规` | 9/152 (6%) | 5/81 (6%) | 1/138 (1%) | 4/158 (3%) | 6/79 (8%) | 5/77 (6%) |
| vague (vagueness, ambiguity) | unclear | `模糊` | 4/152 (3%) | 5/81 (6%) | 49/138 (36%) | 0/158 (0%) | 2/79 (3%) | 5/77 (6%) |
| caught (being caught) | unclear | `Caught` | 5/152 (3%) | 3/81 (4%) | 2/138 (1%) | 5/158 (3%) | 1/79 (1%) | 3/77 (4%) |
| unauthorized (without permission) | unclear | `␣Unauthorized` | 1/152 (1%) | 1/81 (1%) | 0/138 (0%) | 6/158 (4%) | 1/79 (1%) | 1/77 (1%) |
| wrong (wrong, mistaken) | lie | `错误` | 1/152 (1%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 1/79 (1%) | 1/77 (1%) |
| correct (correct) | truth | `_correction`, `更正` | 0/152 (0%) | 0/81 (0%) | 3/138 (2%) | 1/158 (1%) | 0/79 (0%) | 0/77 (0%) |

Not in the draft: honest (held back: no undisputed member left); honest speech (excluded: the question's own word); truth (excluded: the question's own word); true (excluded: the question's own word)

## think_slot1

| family | side | members | lies | truths | no-pressure truths | unrelated | lies that deny | truths that deny |
|---|---|---|---|---|---|---|---|---|
| fake (fake, forged) | lie | `假的`, `伪造`, `fake`, `假`, `pseudo` | 152/152 (100%) | 81/81 (100%) | 138/138 (100%) | 124/158 (78%) | 79/79 (100%) | 77/77 (100%) |
| mock (mock, imitation) | unclear | `_mock`, `/mock`, `␣MOCK`, `mock`, `(Mock` | 152/152 (100%) | 81/81 (100%) | 134/138 (97%) | 7/158 (4%) | 79/79 (100%) | 77/77 (100%) |
| wrong (wrong, mistaken) | lie | `␣ERROR`, `rong`, `erreur`, `_wrong`, `_WRONG`, `错`, `錯`, `错误`, `谬`, `錯誤`, `的错误` | 150/152 (99%) | 80/81 (99%) | 126/138 (91%) | 132/158 (84%) | 78/79 (99%) | 76/77 (99%) |
| illusion (fantasy, illusion, delusion) | unclear | `幻想`, `虚幻`, `妄想`, `错觉` | 137/152 (90%) | 50/81 (62%) | 0/138 (0%) | 1/158 (1%) | 73/79 (92%) | 46/77 (60%) |
| cannot comply (unable to satisfy the request (refusal stance)) | unclear | `无法满足` | 124/152 (82%) | 50/81 (62%) | 116/138 (84%) | 93/158 (59%) | 63/79 (80%) | 46/77 (60%) |
| violate (violating a rule) | unclear | `违反`, `违反了`, `违规`, `违背` | 107/152 (70%) | 42/81 (52%) | 31/138 (22%) | 55/158 (35%) | 57/79 (72%) | 41/77 (53%) |
| inconvenient (not convenient (to say)) | unclear | `不方便` | 85/152 (56%) | 48/81 (59%) | 59/138 (43%) | 36/158 (23%) | 36/79 (46%) | 44/77 (57%) |
| clever (cleverly, artfully) | unclear | `巧妙地`, `巧妙` | 68/152 (45%) | 41/81 (51%) | 85/138 (62%) | 100/158 (63%) | 35/79 (44%) | 38/77 (49%) |
| resignation (helpless resignation about the act) | unclear | `无奈` | 55/152 (36%) | 12/81 (15%) | 0/138 (0%) | 1/158 (1%) | 21/79 (27%) | 11/77 (14%) |
| objective (objective, impartial) | truth | `客观` | 29/152 (19%) | 28/81 (35%) | 55/138 (40%) | 46/158 (29%) | 15/79 (19%) | 26/77 (34%) |
| lawful (legal, in line with the law) | unclear | `依法`, `合法`, `依规` | 43/152 (28%) | 11/81 (14%) | 6/138 (4%) | 5/158 (3%) | 26/79 (33%) | 10/77 (13%) |
| fiction (fiction, fabricated story) | lie | `fiction`, `虚构` | 34/152 (22%) | 10/81 (12%) | 5/138 (4%) | 0/158 (0%) | 24/79 (30%) | 8/77 (10%) |
| forge (forging, falsifying) | lie | `伪造` | 21/152 (14%) | 8/81 (10%) | 0/138 (0%) | 0/158 (0%) | 15/79 (19%) | 7/77 (9%) |
| implicit (implicit, unstated) | unclear | `隐含` | 20/152 (13%) | 8/81 (10%) | 0/138 (0%) | 0/158 (0%) | 10/79 (13%) | 6/77 (8%) |
| legal (legal, lawful) | unclear | `合法` | 11/152 (7%) | 3/81 (4%) | 0/138 (0%) | 0/158 (0%) | 9/79 (11%) | 3/77 (4%) |
| conceal (to conceal, to hide) | lie | `隐` | 7/152 (5%) | 7/81 (9%) | 0/138 (0%) | 0/158 (0%) | 4/79 (5%) | 6/77 (8%) |
| reveal (revealing, divulging) | truth | `透露` | 1/152 (1%) | 2/81 (2%) | 0/138 (0%) | 0/158 (0%) | 1/79 (1%) | 0/77 (0%) |
| misunderstanding (misunderstanding) | unclear | `误解` | 1/152 (1%) | 1/81 (1%) | 1/138 (1%) | 7/158 (4%) | 1/79 (1%) | 1/77 (1%) |
| incorrect (incorrect) | lie | `Incorrect`, `incorrect` | 2/152 (1%) | 0/81 (0%) | 0/138 (0%) | 8/158 (5%) | 2/79 (3%) | 0/77 (0%) |
| fact (fact, factual) | truth | `实际` | 1/152 (1%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 0/79 (0%) | 1/77 (1%) |
| oops (oops (noticing a slip)) | unclear | `Oops` | 1/152 (1%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 1/79 (1%) | 0/77 (0%) |
| accurate (accurate) | truth | `_accuracy` | 1/152 (1%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 1/79 (1%) | 0/77 (0%) |

Not in the draft: honest speech (excluded: the question's own word)

## think_slot2

| family | side | members | lies | truths | no-pressure truths | unrelated | lies that deny | truths that deny |
|---|---|---|---|---|---|---|---|---|
| silence (silence, staying silent) | unclear | `沉默`, `␣Silence`, `␣Silent`, `␣silence`, `silent` | 147/152 (97%) | 78/81 (96%) | 60/138 (43%) | 24/158 (15%) | 76/79 (96%) | 74/77 (96%) |
| privacy (privacy) | unclear | `␣Privacy`, `privacy`, `隐私`, `Privacy`, `␣privacidad`, `␣privacy`, `private` | 145/152 (95%) | 77/81 (95%) | 51/138 (37%) | 48/158 (30%) | 77/79 (97%) | 73/77 (95%) |
| compliance (compliance) | unclear | `␣Compliance`, `合规`, `␣compliance` | 146/152 (96%) | 76/81 (94%) | 119/138 (86%) | 143/158 (91%) | 74/79 (94%) | 72/77 (94%) |
| forbidden (forbidden, prohibited) | unclear | `␣Forbidden`, `␣prohibited`, `禁忌`, `严禁`, `禁止`, `Forbidden` | 127/152 (84%) | 67/81 (83%) | 22/138 (16%) | 1/158 (1%) | 62/79 (78%) | 64/77 (83%) |
| disclose (disclosing) | truth | `␣Disclosure` | 118/152 (78%) | 57/81 (70%) | 11/138 (8%) | 4/158 (3%) | 58/79 (73%) | 55/77 (71%) |
| leak (leaking information) | unclear | `␣WikiLeaks`, `␣Leakage` | 99/152 (65%) | 49/81 (60%) | 19/138 (14%) | 1/158 (1%) | 62/79 (78%) | 48/77 (62%) |
| conscience (conscience) | unclear | `␣conscience` | 109/152 (72%) | 31/81 (38%) | 0/138 (0%) | 0/158 (0%) | 52/79 (66%) | 30/77 (39%) |
| mislead (misleading) | lie | `误导性` | 85/152 (56%) | 53/81 (65%) | 20/138 (14%) | 27/158 (17%) | 43/79 (54%) | 50/77 (65%) |
| violate (violating a rule) | unclear | `违背`, `违规`, `␣violates`, `␣violate`, `␣violating`, `␣violation`, `违反` | 102/152 (67%) | 34/81 (42%) | 67/138 (49%) | 9/158 (6%) | 45/79 (57%) | 31/77 (40%) |
| unauthorized (without permission) | unclear | `␣Unauthorized` | 79/152 (52%) | 45/81 (56%) | 6/138 (4%) | 0/158 (0%) | 46/79 (58%) | 44/77 (57%) |
| hide (hiding, keeping out of sight) | lie | `␣Hidden`, `hidden`, `隐藏`, `隐藏的`, `隐匿`, `_hide`, `隐` | 83/152 (55%) | 39/81 (48%) | 1/138 (1%) | 9/158 (6%) | 33/79 (42%) | 38/77 (49%) |
| integrity (integrity, uprightness) | truth | `␣Integrity`, `正直` | 59/152 (39%) | 49/81 (60%) | 7/138 (5%) | 11/158 (7%) | 36/79 (46%) | 48/77 (62%) |
| ethics (ethics, morality) | unclear | `␣Ethics`, `道德`, `ethical`, `␣ethical`, `␣ethics`, `伦理`, `␣Moral` | 74/152 (49%) | 14/81 (17%) | 1/138 (1%) | 0/158 (0%) | 37/79 (47%) | 12/77 (16%) |
| implicit (implicit, unstated) | unclear | `␣Implicit`, `隐含`, `implicit` | 60/152 (39%) | 20/81 (25%) | 1/138 (1%) | 0/158 (0%) | 24/79 (30%) | 16/77 (21%) |
| refuse (refusing) | unclear | `拒绝`, `␣refusal`, `拒`, `␣refus`, `拒絕`, `reject`, `␣Reject`, `rejected` | 35/152 (23%) | 21/81 (26%) | 31/138 (22%) | 0/158 (0%) | 28/79 (35%) | 21/77 (27%) |
| secret (kept secret, confidential) | lie | `保密`, `机密`, `SECRET` | 35/152 (23%) | 13/81 (16%) | 0/138 (0%) | 0/158 (0%) | 18/79 (23%) | 11/77 (14%) |
| confidential (keeping confidential) | lie | `保密` | 32/152 (21%) | 12/81 (15%) | 0/138 (0%) | 0/158 (0%) | 16/79 (20%) | 10/77 (13%) |
| decline (choosing not to) | unclear | `选择不` | 20/152 (13%) | 24/81 (30%) | 45/138 (33%) | 44/158 (28%) | 11/79 (14%) | 23/77 (30%) |
| explicit (explicit, stated openly) | unclear | `␣Explicit`, `explicit` | 37/152 (24%) | 5/81 (6%) | 2/138 (1%) | 0/158 (0%) | 15/79 (19%) | 5/77 (6%) |
| coward (cowardice) | unclear | `␣coward` | 26/152 (17%) | 12/81 (15%) | 0/138 (0%) | 0/158 (0%) | 12/79 (15%) | 10/77 (13%) |
| hypocrisy (hypocrisy) | lie | `␣hypocrisy` | 26/152 (17%) | 7/81 (9%) | 0/138 (0%) | 0/158 (0%) | 17/79 (22%) | 7/77 (9%) |
| taboo (taboo) | unclear | `禁忌` | 24/152 (16%) | 8/81 (10%) | 0/138 (0%) | 0/158 (0%) | 7/79 (9%) | 6/77 (8%) |
| anonymous (anonymity) | unclear | `␣Anonymous`, `␣anonymity`, `␣anonymously` | 21/152 (14%) | 10/81 (12%) | 0/138 (0%) | 0/158 (0%) | 10/79 (13%) | 9/77 (12%) |
| illegal (illegal) | unclear | `illegal`, `␣Illegal`, `␣illegal`, `违法` | 24/152 (16%) | 3/81 (4%) | 2/138 (1%) | 0/158 (0%) | 14/79 (18%) | 3/77 (4%) |
| legal (legal, lawful) | unclear | `␣Legal`, `依法` | 15/152 (10%) | 4/81 (5%) | 1/138 (1%) | 0/158 (0%) | 9/79 (11%) | 4/77 (5%) |
| reject (rejecting) | unclear | `reject`, `␣Reject`, `rejected` | 12/152 (8%) | 6/81 (7%) | 0/138 (0%) | 0/158 (0%) | 11/79 (14%) | 6/77 (8%) |
| false (false, untrue) | lie | `␣FALSE`, `>false`, `_false`, `.assertFalse`, `.False` | 7/152 (5%) | 11/81 (14%) | 1/138 (1%) | 2/158 (1%) | 4/79 (5%) | 11/77 (14%) |
| unethical (unethical) | lie | `␣unethical` | 14/152 (9%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 8/79 (10%) | 1/77 (1%) |
| clarify (clarifying, setting the record straight) | unclear | `澄清` | 5/152 (3%) | 8/81 (10%) | 119/138 (86%) | 126/158 (80%) | 1/79 (1%) | 7/77 (9%) |
| sorry (apology) | unclear | `抱歉`, `Sorry`, `␣Sorry` | 10/152 (7%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 7/79 (9%) | 1/77 (1%) |
| incorrect (incorrect) | lie | `incorrect` | 2/152 (1%) | 6/81 (7%) | 11/138 (8%) | 16/158 (10%) | 1/79 (1%) | 6/77 (8%) |
| self-protection (protecting oneself) | unclear | `自我保护` | 3/152 (2%) | 3/81 (4%) | 4/138 (3%) | 2/158 (1%) | 3/79 (4%) | 3/77 (4%) |
| cheat (cheating) | lie | `作弊` | 2/152 (1%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 1/79 (1%) | 1/77 (1%) |
| fact (fact, factual) | truth | `actual`, `实际`, `的实际` | 1/152 (1%) | 2/81 (2%) | 0/138 (0%) | 0/158 (0%) | 1/79 (1%) | 2/77 (3%) |
| correct (correct) | truth | `␣Correct`, `␣Correction`, `_correction`, `Correction`, `正确`, `纠错`, `纠正`, `更正` | 2/152 (1%) | 1/81 (1%) | 22/138 (16%) | 44/158 (28%) | 2/79 (3%) | 1/77 (1%) |
| deceive (the act of deceiving) | lie | `欺骗` | 1/152 (1%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 0/79 (0%) | 1/77 (1%) |
| fraud (fraud, swindling) | lie | `欺诈` | 1/152 (1%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 1/79 (1%) | 1/77 (1%) |
| true (true, real) | truth | `真的` | 1/152 (1%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 1/79 (1%) | 1/77 (1%) |
| cover up (covering up, glossing over) | lie | `掩饰` | 1/152 (1%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 1/79 (1%) | 0/77 (0%) |
| secret (secrecy, a secret) | lie | `SECRET` | 1/152 (1%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 0/79 (0%) | 0/77 (0%) |
| disclaimer (a disclaimer) | unclear | `␣disclaimer` | 1/152 (1%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 1/79 (1%) | 0/77 (0%) |
| evil (evil) | lie | `␣Evil` | 1/152 (1%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 1/79 (1%) | 0/77 (0%) |
| wrong (wrong, mistaken) | lie | `错`, `错觉` | 0/152 (0%) | 1/81 (1%) | 0/138 (0%) | 17/158 (11%) | 0/79 (0%) | 1/77 (1%) |

Not in the draft: admit (excluded: admit / deny / acknowledge); truth (excluded: the question's own word)

## think_slot3

| family | side | members | lies | truths | no-pressure truths | unrelated | lies that deny | truths that deny |
|---|---|---|---|---|---|---|---|---|
| false (false, untrue) | lie | `␣false`, `␣False`, `false`, `False`, `␣FALSE`, `:false`, `>false`, `␣falsely`, `␣falsehood`, `假` | 110/152 (72%) | 78/81 (96%) | 132/138 (96%) | 56/158 (35%) | 76/79 (96%) | 74/77 (96%) |
| wrong (wrong, mistaken) | lie | `␣ERROR`, `wrong`, `␣Wrong`, `误`, `错误` | 37/152 (24%) | 37/81 (46%) | 27/138 (20%) | 14/158 (9%) | 36/79 (46%) | 37/77 (48%) |
| incorrect (incorrect) | lie | `␣incorrect`, `incorrect`, `␣Incorrect`, `不符合` | 19/152 (12%) | 36/81 (44%) | 10/138 (7%) | 9/158 (6%) | 18/79 (23%) | 36/77 (47%) |
| disclaimer (a disclaimer) | unclear | `␣DISCLAIMER`, `␣Disclaimer` | 17/152 (11%) | 2/81 (2%) | 1/138 (1%) | 0/158 (0%) | 15/79 (19%) | 2/77 (3%) |
| misunderstanding (misunderstanding) | unclear | `误解`, `␣misunderstood` | 2/152 (1%) | 12/81 (15%) | 11/138 (8%) | 30/158 (19%) | 2/79 (3%) | 12/77 (16%) |
| decline (choosing not to) | unclear | `选择不` | 7/152 (5%) | 6/81 (7%) | 0/138 (0%) | 0/158 (0%) | 5/79 (6%) | 6/77 (8%) |
| refuse (refusing) | unclear | `拒绝`, `␣Reject` | 3/152 (2%) | 4/81 (5%) | 0/138 (0%) | 0/158 (0%) | 3/79 (4%) | 4/77 (5%) |
| sorry (apology) | unclear | `␣Sorry`, `抱歉`, `Sorry`, `对不起`, `␣Oops` | 4/152 (3%) | 2/81 (2%) | 0/138 (0%) | 0/158 (0%) | 3/79 (4%) | 2/77 (3%) |
| reject (rejecting) | unclear | `␣Reject` | 1/152 (1%) | 4/81 (5%) | 0/138 (0%) | 0/158 (0%) | 1/79 (1%) | 4/77 (5%) |
| illegal (illegal) | unclear | `␣Illegal` | 4/152 (3%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 4/79 (5%) | 1/77 (1%) |
| coward (cowardice) | unclear | `␣coward` | 3/152 (2%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 3/79 (4%) | 1/77 (1%) |
| hide (hiding, keeping out of sight) | lie | `␣Hidden` | 2/152 (1%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 2/79 (3%) | 0/77 (0%) |
| silence (silence, staying silent) | unclear | `␣Silent`, `␣Silence` | 2/152 (1%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 2/79 (3%) | 0/77 (0%) |
| anonymous (anonymity) | unclear | `␣Anonymous` | 2/152 (1%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 2/79 (3%) | 0/77 (0%) |
| unauthorized (without permission) | unclear | `␣Unauthorized` | 1/152 (1%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 0/79 (0%) | 1/77 (1%) |
| secret (secrecy, a secret) | lie | `␣Secret` | 1/152 (1%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 1/79 (1%) | 0/77 (0%) |
| dishonest (dishonesty) | lie | `␣dishonest` | 1/152 (1%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 1/79 (1%) | 0/77 (0%) |
| violate (violating a rule) | unclear | `违反`, `违反了`, `违背`, `␣violates` | 0/152 (0%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 0/79 (0%) | 1/77 (1%) |
| legal (legal, lawful) | unclear | `␣Legal` | 0/152 (0%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 0/79 (0%) | 1/77 (1%) |
| true (true, real) | truth | `␣true` | 1/152 (1%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 1/79 (1%) | 0/77 (0%) |
| fact (fact, factual) | truth | `␣Actually`, `Actually`, `actually`, `实际上`, `根据实际情况` | 0/152 (0%) | 0/81 (0%) | 1/138 (1%) | 1/158 (1%) | 0/79 (0%) | 0/77 (0%) |

Not in the draft: truth (excluded: the question's own word)
