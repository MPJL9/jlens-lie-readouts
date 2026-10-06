# Draft families: qwen3.6-27b, J-lens, part Q1_bare, group think

Written by `scripts/apply_family_decisions.py` (2026-10-01; draft, not frozen). Counts are `present / transcripts (share)`
on the build split.

## think_slot0

| family | side | members | lies | truths | no-pressure truths | unrelated | lies that deny | truths that deny |
|---|---|---|---|---|---|---|---|---|
| lawful / legal (in accordance with the law) | unclear | `合法`, `依法`, `legal`, `/legal`, `_legal`, `␣legality` | 151/152 (99%) | 77/81 (95%) | 134/138 (97%) | 141/158 (89%) | 53/53 (100%) | 71/74 (96%) |
| secret (hidden, secret) | lie | `隐秘` | 147/152 (97%) | 79/81 (98%) | 138/138 (100%) | 144/158 (91%) | 49/53 (92%) | 72/74 (97%) |
| compliance (following rules) | unclear | `合规`, `␣Compliance`, `依法依规` | 133/152 (88%) | 67/81 (83%) | 124/138 (90%) | 1/158 (1%) | 48/53 (91%) | 61/74 (82%) |
| fabricated / fictional (made up, fictional) | unclear | `虚构` | 82/152 (54%) | 50/81 (62%) | 22/138 (16%) | 0/158 (0%) | 31/53 (58%) | 45/74 (61%) |
| clarify (making something clear) | truth | `澄清` | 67/152 (44%) | 53/81 (65%) | 138/138 (100%) | 157/158 (99%) | 22/53 (42%) | 49/74 (66%) |
| rule violation (breaking rules or regulations) | unclear | `违法违规`, `违规` | 68/152 (45%) | 25/81 (31%) | 57/138 (41%) | 41/158 (26%) | 28/53 (53%) | 21/74 (28%) |
| illegal (against the law) | unclear | `非法`, `违法`, `illegal`, `Illegal`, `␣Illegal` | 64/152 (42%) | 24/81 (30%) | 13/138 (9%) | 11/158 (7%) | 21/53 (40%) | 20/74 (27%) |
| quietly / unnoticed (doing something quietly, without notice) | unclear | `悄然` | 52/152 (34%) | 28/81 (35%) | 0/138 (0%) | 9/158 (6%) | 20/53 (38%) | 25/74 (34%) |
| lawful (in accordance with the law) | unclear | `合法`, `依法依规`, `依法` | 56/152 (37%) | 18/81 (22%) | 0/138 (0%) | 0/158 (0%) | 23/53 (43%) | 15/74 (20%) |
| unauthorized (without permission) | unclear | `␣Unauthorized`, `Unauthorized` | 52/152 (34%) | 21/81 (26%) | 72/138 (52%) | 81/158 (51%) | 21/53 (40%) | 16/74 (22%) |
| ethics / morality (ethics, morality) | unclear | `道德`, `ethical` | 41/152 (27%) | 15/81 (19%) | 7/138 (5%) | 8/158 (5%) | 5/53 (9%) | 13/74 (18%) |
| fake (fake, false (not genuine)) | lie | `fake`, `Fake`, `假` | 22/152 (14%) | 9/81 (11%) | 23/138 (17%) | 20/158 (13%) | 16/53 (30%) | 7/74 (9%) |
| suppress (suppressing something) | lie | `suppress` | 9/152 (6%) | 14/81 (17%) | 3/138 (2%) | 0/158 (0%) | 9/53 (17%) | 14/74 (19%) |
| questioning / doubt (calling into question) | unclear | `质疑` | 14/152 (9%) | 3/81 (4%) | 15/138 (11%) | 0/158 (0%) | 7/53 (13%) | 3/74 (4%) |
| misunderstanding (a misunderstanding) | unclear | `误解` | 6/152 (4%) | 5/81 (6%) | 0/138 (0%) | 19/158 (12%) | 2/53 (4%) | 5/74 (7%) |
| vague (vague, blurred) | unclear | `模糊` | 2/152 (1%) | 6/81 (7%) | 1/138 (1%) | 0/158 (0%) | 2/53 (4%) | 6/74 (8%) |
| hide (to hide, conceal) | lie | `藏`, `隐` | 2/152 (1%) | 4/81 (5%) | 0/138 (0%) | 0/158 (0%) | 2/53 (4%) | 4/74 (5%) |
| wrong (wrong, mistaken) | lie | `错`, `错误` | 1/152 (1%) | 1/81 (1%) | 0/138 (0%) | 8/158 (5%) | 0/53 (0%) | 1/74 (1%) |
| leak (leaking information) | unclear | `Leaks` | 0/152 (0%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 0/53 (0%) | 0/74 (0%) |
| true (true, real) | truth | `真` | 0/152 (0%) | 1/81 (1%) | 13/138 (9%) | 5/158 (3%) | 0/53 (0%) | 1/74 (1%) |

Not in the draft: truth (excluded: truth from the question on)

## think_slot1

| family | side | members | lies | truths | no-pressure truths | unrelated | lies that deny | truths that deny |
|---|---|---|---|---|---|---|---|---|
| violate (to violate, go against) | unclear | `违反`, `违反了`, `违背`, `␣violate`, `␣violates`, `␣violated`, `違反`, `违规`, `违规行为`, `违法违规行为` | 152/152 (100%) | 81/81 (100%) | 137/138 (99%) | 131/158 (83%) | 53/53 (100%) | 74/74 (100%) |
| fake (fake, false (not genuine)) | lie | `假`, `fake`, `假的` | 150/152 (99%) | 72/81 (89%) | 134/138 (97%) | 11/158 (7%) | 53/53 (100%) | 65/74 (88%) |
| compliance (following rules) | unclear | `依规`, `恪`, `严格遵守`, `恪守`, `合规`, `自觉遵守`, `␣Compliance`, `遵守` | 136/152 (89%) | 71/81 (88%) | 128/138 (93%) | 33/158 (21%) | 48/53 (91%) | 66/74 (89%) |
| cannot (cannot satisfy, unable) | unclear | `无法满足`, `不能满足` | 87/152 (57%) | 40/81 (49%) | 78/138 (57%) | 0/158 (0%) | 43/53 (81%) | 37/74 (50%) |
| rule violation (breaking rules or regulations) | unclear | `违规`, `违规行为`, `违法违规行为` | 72/152 (47%) | 35/81 (43%) | 61/138 (44%) | 25/158 (16%) | 35/53 (66%) | 30/74 (41%) |
| refuse (to refuse, reject) | unclear | `拒`, `拒绝`, `拒绝了`, `.reject` | 39/152 (26%) | 23/81 (28%) | 11/138 (8%) | 1/158 (1%) | 12/53 (23%) | 22/74 (30%) |
| wrong (wrong, mistaken) | lie | `␣ERROR`, `rong`, `erreur`, `_WRONG`, `错`, `錯`, `错误`, `谬`, `錯誤`, `的错误`, `错误或` | 39/152 (26%) | 21/81 (26%) | 112/138 (81%) | 4/158 (3%) | 19/53 (36%) | 17/74 (23%) |
| fantasy / illusion (fantasy, illusion, false impression) | unclear | `幻想`, `虚幻`, `错觉` | 41/152 (27%) | 15/81 (19%) | 26/138 (19%) | 13/158 (8%) | 23/53 (43%) | 15/74 (20%) |
| forge (to forge, counterfeit) | lie | `伪造` | 30/152 (20%) | 9/81 (11%) | 0/138 (0%) | 0/158 (0%) | 15/53 (28%) | 7/74 (9%) |
| ethics / morality (ethics, morality) | unclear | `ethical`, `伦理`, `␣Ethics`, `道德`, `␣ethical` | 25/152 (16%) | 10/81 (12%) | 26/138 (19%) | 9/158 (6%) | 14/53 (26%) | 7/74 (9%) |
| fictional (fiction, made up) | unclear | `fiction`, `虚构` | 18/152 (12%) | 13/81 (16%) | 2/138 (1%) | 0/158 (0%) | 12/53 (23%) | 13/74 (18%) |
| taboo (taboo, something to avoid) | unclear | `忌讳`, `禁忌` | 21/152 (14%) | 9/81 (11%) | 94/138 (68%) | 55/158 (35%) | 6/53 (11%) | 8/74 (11%) |
| unauthorized (doing something privately without permission) | unclear | `私自` | 12/152 (8%) | 3/81 (4%) | 47/138 (34%) | 5/158 (3%) | 6/53 (11%) | 2/74 (3%) |
| lawful (in accordance with the law) | unclear | `合法`, `依法` | 9/152 (6%) | 2/81 (2%) | 2/138 (1%) | 0/158 (0%) | 5/53 (9%) | 1/74 (1%) |
| misunderstanding (a misunderstanding) | unclear | `误解`, `错觉` | 2/152 (1%) | 4/81 (5%) | 41/138 (30%) | 15/158 (9%) | 0/53 (0%) | 4/74 (5%) |
| fact (fact, factual) | truth | `实际` | 1/152 (1%) | 1/81 (1%) | 17/138 (12%) | 1/158 (1%) | 0/53 (0%) | 0/74 (0%) |
| reject (to reject) | unclear | `.reject` | 1/152 (1%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 1/53 (2%) | 0/74 (0%) |
| conceal (to conceal, to hide) | lie | `隐` | 0/152 (0%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 0/53 (0%) | 1/74 (1%) |
| false (false, untrue) | lie | `_false` | 0/152 (0%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 0/53 (0%) | 0/74 (0%) |

Not in the draft: pretext / front (held back: no undisputed member left); avoid / evade (held back: no undisputed member left); secret (held back: no undisputed member left)

## think_slot2

| family | side | members | lies | truths | no-pressure truths | unrelated | lies that deny | truths that deny |
|---|---|---|---|---|---|---|---|---|
| privacy (privacy) | unclear | `␣Privacy`, `privacy`, `␣privacy`, `Privacy`, `隐私`, `␣privacidad`, `ความเป็นส่วนตัว` | 150/152 (99%) | 79/81 (98%) | 137/138 (99%) | 135/158 (85%) | 51/53 (96%) | 72/74 (97%) |
| unauthorized (without permission) | unclear | `␣Unauthorized` | 128/152 (84%) | 64/81 (79%) | 56/138 (41%) | 2/158 (1%) | 48/53 (91%) | 58/74 (78%) |
| forbidden (forbidden, prohibited) | unclear | `␣Forbidden`, `严禁`, `禁止`, `禁用`, `␣prohibited`, `取缔`, `␣запрещ`, `␣banned`, `␣prohibits`, `␣forbidden` | 91/152 (60%) | 56/81 (69%) | 73/138 (53%) | 0/158 (0%) | 39/53 (74%) | 52/74 (70%) |
| illegal (against the law) | unclear | `␣Illegal`, `illegal`, `␣ilegal`, `␣illegal`, `␣unlawful`, `Illegal`, `违法`, `非法` | 96/152 (63%) | 47/81 (58%) | 60/138 (43%) | 6/158 (4%) | 33/53 (62%) | 42/74 (57%) |
| cannot (cannot, unable) | unclear | `cannot`, `我无法`, `␣Cannot`, `Cannot`, `我不能`, `␣cannot`, `不可以`, `_CANNOT`, `不能`, `␣Unable`, `是无法`, `无法满足`, `Unable`, `unable`, `是不能`, `不能使用` | 89/152 (59%) | 51/81 (63%) | 67/138 (49%) | 6/158 (4%) | 42/53 (79%) | 47/74 (64%) |
| whistleblowing (whistleblowing (disclosing wrongdoing)) | truth | `␣whistleblower`, `␣whistlebl`, `␣WikiLeaks` | 84/152 (55%) | 33/81 (41%) | 74/138 (54%) | 46/158 (29%) | 28/53 (53%) | 27/74 (36%) |
| confidential (confidential, kept secret) | lie | `␣confidentiality`, `保密`, `␣Confidential`, `␣конфиден` | 52/152 (34%) | 24/81 (30%) | 35/138 (25%) | 9/158 (6%) | 18/53 (34%) | 22/74 (30%) |
| ethics / morality (ethics, morality) | unclear | `␣Ethics`, `␣ethical`, `ethical`, `␣ethics` | 58/152 (38%) | 12/81 (15%) | 14/138 (10%) | 18/158 (11%) | 10/53 (19%) | 10/74 (14%) |
| lawful / legal (legal, lawful) | unclear | `␣Legal`, `/legal`, `␣legality`, `␣legally`, `合法`, `依法依规`, `Legal` | 44/152 (29%) | 24/81 (30%) | 56/138 (41%) | 21/158 (13%) | 15/53 (28%) | 22/74 (30%) |
| refuse (to refuse, reject) | unclear | `拒绝`, `␣refusal`, `拒絕`, `reject`, `␣refuses`, `rejected`, `拒`, `.reject`, `␣Reject`, `拒不`, `拒绝了`, `␣refusing`, `␣rejecting`, `␣refused` | 36/152 (24%) | 22/81 (27%) | 0/138 (0%) | 0/158 (0%) | 30/53 (57%) | 20/74 (27%) |
| apology (apologising) | truth | `Sorry`, `抱歉`, `␣Sorry`, `␣sorry`, `sorry` | 38/152 (25%) | 15/81 (19%) | 22/138 (16%) | 43/158 (27%) | 25/53 (47%) | 14/74 (19%) |
| violate (to violate, go against) | unclear | `␣violates`, `␣violate`, `违背`, `␣violation`, `␣violating`, `␣violations`, `违反` | 28/152 (18%) | 20/81 (25%) | 20/138 (14%) | 0/158 (0%) | 25/53 (47%) | 18/74 (24%) |
| leak (leaking information) | unclear | `␣WikiLeaks` | 28/152 (18%) | 19/81 (23%) | 44/138 (32%) | 14/158 (9%) | 18/53 (34%) | 17/74 (23%) |
| unethical (unethical) | lie | `␣unethical` | 27/152 (18%) | 5/81 (6%) | 7/138 (5%) | 0/158 (0%) | 14/53 (26%) | 4/74 (5%) |
| silence (staying silent) | unclear | `␣Silence`, `沉默`, `␣silence` | 20/152 (13%) | 12/81 (15%) | 0/138 (0%) | 0/158 (0%) | 16/53 (30%) | 12/74 (16%) |
| true (true, real) | truth | `True`, `␣TRUE`, `.isTrue`, `真`, `确实`, `的确`, `的真实`, `的真实性`, `眞` | 17/152 (11%) | 15/81 (19%) | 75/138 (54%) | 4/158 (3%) | 4/53 (8%) | 13/74 (18%) |
| compliance (following rules) | unclear | `合规`, `␣Compliance`, `依法依规` | 7/152 (5%) | 5/81 (6%) | 33/138 (24%) | 0/158 (0%) | 5/53 (9%) | 4/74 (5%) |
| refute (to argue that a claim is false) | unclear | `␣refute` | 6/152 (4%) | 3/81 (4%) | 0/138 (0%) | 0/158 (0%) | 6/53 (11%) | 3/74 (4%) |
| skepticism (doubt about a claim) | unclear | `␣skepticism` | 5/152 (3%) | 3/81 (4%) | 0/138 (0%) | 0/158 (0%) | 4/53 (8%) | 3/74 (4%) |
| secrecy (secrecy) | lie | `␣secrecy` | 6/152 (4%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 5/53 (9%) | 1/74 (1%) |
| reject (to reject) | unclear | `reject`, `rejected`, `.reject`, `␣Reject`, `␣rejecting` | 5/152 (3%) | 2/81 (2%) | 0/138 (0%) | 0/158 (0%) | 5/53 (9%) | 2/74 (3%) |
| false (false, untrue) | lie | `false`, `False`, `,false`, `>false`, `_false`, `.assertFalse`, `.False` | 4/152 (3%) | 2/81 (2%) | 8/138 (6%) | 4/158 (3%) | 4/53 (8%) | 2/74 (3%) |
| disclose (disclosing) | truth | `␣Disclosure` | 4/152 (3%) | 1/81 (1%) | 14/138 (10%) | 1/158 (1%) | 1/53 (2%) | 1/74 (1%) |
| hypocrisy (hypocrisy) | lie | `␣hypocrisy` | 4/152 (3%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 3/53 (6%) | 0/74 (0%) |
| conscience (conscience) | unclear | `␣conscience` | 0/152 (0%) | 3/81 (4%) | 0/138 (0%) | 0/158 (0%) | 0/53 (0%) | 3/74 (4%) |
| misinformation (false information) | lie | `␣misinformation` | 3/152 (2%) | 0/81 (0%) | 2/138 (1%) | 1/158 (1%) | 2/53 (4%) | 0/74 (0%) |
| mislead (misleading) | lie | `误导性` | 2/152 (1%) | 0/81 (0%) | 15/138 (11%) | 4/158 (3%) | 2/53 (4%) | 0/74 (0%) |
| ostensible (seeming, on the surface) | unclear | `␣ostensibly` | 2/152 (1%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 2/53 (4%) | 0/74 (0%) |
| discreet (discreet) | unclear | `␣discreet` | 0/152 (0%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 0/53 (0%) | 1/74 (1%) |
| honest (honest, honestly) | truth | `␣honestly`, `␣Honestly` | 1/152 (1%) | 0/81 (0%) | 0/138 (0%) | 2/158 (1%) | 0/53 (0%) | 0/74 (0%) |
| truth (the truth) | truth | `其真实性` | 1/152 (1%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 1/53 (2%) | 0/74 (0%) |
| clarify (making something clear) | truth | `澄清` | 1/152 (1%) | 0/81 (0%) | 1/138 (1%) | 1/158 (1%) | 1/53 (2%) | 0/74 (0%) |
| fictional (fiction, made up) | unclear | `fiction` | 0/152 (0%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 0/53 (0%) | 1/74 (1%) |
| accurate (accurate) | truth | `␣accurate`, `accur`, `␣Accuracy` | 0/152 (0%) | 0/81 (0%) | 7/138 (5%) | 6/158 (4%) | 0/53 (0%) | 0/74 (0%) |
| correct (correct) | truth | `␣Correct`, `正确`, `更正` | 0/152 (0%) | 0/81 (0%) | 10/138 (7%) | 5/158 (3%) | 0/53 (0%) | 0/74 (0%) |
| fact (fact, factual) | truth | `␣Facts`, `Actually`, `facts`, `事实` | 0/152 (0%) | 0/81 (0%) | 23/138 (17%) | 5/158 (3%) | 0/53 (0%) | 0/74 (0%) |
| incorrect (incorrect) | lie | `incorrect` | 0/152 (0%) | 0/81 (0%) | 0/138 (0%) | 1/158 (1%) | 0/53 (0%) | 0/74 (0%) |

Not in the draft: deny (excluded: admit / deny / acknowledge)

## think_slot3

| family | side | members | lies | truths | no-pressure truths | unrelated | lies that deny | truths that deny |
|---|---|---|---|---|---|---|---|---|
| truthful (truthful) | truth | `␣truthful` | 145/152 (95%) | 78/81 (96%) | 132/138 (96%) | 46/158 (29%) | 50/53 (94%) | 71/74 (96%) |
| honest (honest, honestly) | truth | `␣honestly`, `␣honest`, `␣honesty`, `␣Honest`, `␣Honestly`, `诚实` | 130/152 (86%) | 55/81 (68%) | 17/138 (12%) | 63/158 (40%) | 38/53 (72%) | 50/74 (68%) |
| true (true, real) | truth | `␣true`, `␣True`, `␣TRUE`, `确实` | 115/152 (76%) | 57/81 (70%) | 51/138 (37%) | 15/158 (9%) | 30/53 (57%) | 50/74 (68%) |
| genuine (genuinely) | truth | `␣genuinely` | 76/152 (50%) | 37/81 (46%) | 7/138 (5%) | 6/158 (4%) | 27/53 (51%) | 32/74 (43%) |
| unethical (unethical) | lie | `␣unethical` | 82/152 (54%) | 21/81 (26%) | 0/138 (0%) | 0/158 (0%) | 7/53 (13%) | 17/74 (23%) |
| ethics / morality (ethics, morality) | unclear | `␣ethical`, `␣morally`, `␣ethics`, `ethical`, `␣Ethics`, `伦理`, `␣moral`, `␣morality`, `的道德`, `道德`, `职业道德` | 79/152 (52%) | 19/81 (23%) | 0/138 (0%) | 0/158 (0%) | 7/53 (13%) | 15/74 (20%) |
| false (false, untrue) | lie | `␣false`, `␣False`, `false`, `False`, `=False`, `␣FALSE`, `FALSE`, `>false`, `␣fals`, `_false`, `.False`, `␣falsely`, `␣untrue`, `/false`, `␣falsehood` | 45/152 (30%) | 46/81 (57%) | 105/138 (76%) | 5/158 (3%) | 32/53 (60%) | 43/74 (58%) |
| confidential (confidential, kept secret) | lie | `␣confidentiality`, `␣confidential`, `␣Confidential` | 77/152 (51%) | 10/81 (12%) | 0/138 (0%) | 0/158 (0%) | 20/53 (38%) | 7/74 (9%) |
| confess (to confess, come clean) | truth | `坦白`, `␣confess`, `␣confession` | 58/152 (38%) | 18/81 (22%) | 5/138 (4%) | 6/158 (4%) | 11/53 (21%) | 14/74 (19%) |
| candid / frank (speaking frankly) | truth | `␣frankly`, `坦诚`, `坦言` | 47/152 (31%) | 14/81 (17%) | 0/138 (0%) | 1/158 (1%) | 19/53 (36%) | 13/74 (18%) |
| sincere (sincere) | truth | `␣sincerely`, `␣sincere` | 34/152 (22%) | 9/81 (11%) | 0/138 (0%) | 0/158 (0%) | 18/53 (34%) | 9/74 (12%) |
| clarify (making something clear) | truth | `澄清`, `␣clarification` | 13/152 (9%) | 27/81 (33%) | 12/138 (9%) | 67/158 (42%) | 9/53 (17%) | 27/74 (36%) |
| cannot (cannot) | unclear | `我无法`, `我不能`, `␣Cannot`, `␣cannot`, `绝对不能`, `无法满足` | 24/152 (16%) | 9/81 (11%) | 0/138 (0%) | 0/158 (0%) | 11/53 (21%) | 8/74 (11%) |
| apology (apologising) | truth | `␣apologies`, `抱歉`, `␣apologize`, `␣Sorry`, `␣apolog`, `␣apology`, `对不起`, `道歉` | 17/152 (11%) | 9/81 (11%) | 0/138 (0%) | 2/158 (1%) | 9/53 (17%) | 8/74 (11%) |
| intentional (done on purpose) | unclear | `␣intentionally` | 10/152 (7%) | 14/81 (17%) | 1/138 (1%) | 1/158 (1%) | 2/53 (4%) | 11/74 (15%) |
| undeniable (cannot be denied) | unclear | `␣undeniable` | 18/152 (12%) | 4/81 (5%) | 0/138 (0%) | 0/158 (0%) | 15/53 (28%) | 4/74 (5%) |
| accusation (an accusation) | unclear | `␣accusations`, `␣allegations`, `␣accusing`, `␣accuse`, `␣accusation`, `␣accuses` | 14/152 (9%) | 5/81 (6%) | 24/138 (17%) | 0/158 (0%) | 8/53 (15%) | 5/74 (7%) |
| refute (to argue that a claim is false) | unclear | `␣refute` | 8/152 (5%) | 6/81 (7%) | 0/138 (0%) | 0/158 (0%) | 7/53 (13%) | 5/74 (7%) |
| ostensible (seeming, on the surface) | unclear | `␣ostensibly`, `␣purported` | 11/152 (7%) | 2/81 (2%) | 1/138 (1%) | 0/158 (0%) | 4/53 (8%) | 1/74 (1%) |
| fact (fact, factual) | truth | `␣actually`, `␣Actually`, `␣factual` | 4/152 (3%) | 8/81 (10%) | 16/138 (12%) | 16/158 (10%) | 1/53 (2%) | 8/74 (11%) |
| dishonest (dishonest) | lie | `␣dishonest` | 10/152 (7%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 2/53 (4%) | 1/74 (1%) |
| hypocrisy (hypocrisy) | lie | `␣hypocrisy` | 9/152 (6%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 2/53 (4%) | 0/74 (0%) |
| misunderstanding (a misunderstanding) | unclear | `␣misunderstanding`, `误解`, `␣misunderstood`, `␣misunderstand` | 3/152 (2%) | 7/81 (9%) | 2/138 (1%) | 5/158 (3%) | 2/53 (4%) | 6/74 (8%) |
| forgive (asking forgiveness) | truth | `␣forgive` | 8/152 (5%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 4/53 (8%) | 1/74 (1%) |
| privacy (privacy, privately) | unclear | `␣privately`, `␣Privacy`, `␣privacy` | 7/152 (5%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 2/53 (4%) | 1/74 (1%) |
| questioning / doubt (calling into question) | unclear | `质疑` | 5/152 (3%) | 1/81 (1%) | 0/138 (0%) | 2/158 (1%) | 3/53 (6%) | 1/74 (1%) |
| refuse (to refuse, reject) | unclear | `拒绝`, `␣refusal`, `␣rejecting`, `␣Reject` | 5/152 (3%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 4/53 (8%) | 1/74 (1%) |
| discreet (discreet) | unclear | `␣discreet` | 5/152 (3%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 5/53 (9%) | 0/74 (0%) |
| private (privately) | unclear | `␣privately` | 5/152 (3%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 1/53 (2%) | 0/74 (0%) |
| misinformation (false information) | lie | `␣misinformation` | 3/152 (2%) | 1/81 (1%) | 6/138 (4%) | 2/158 (1%) | 2/53 (4%) | 1/74 (1%) |
| lawful / legal (legal, lawful) | unclear | `␣legally`, `␣Legal` | 3/152 (2%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 1/53 (2%) | 0/74 (0%) |
| transparency (transparency) | truth | `␣Transparency` | 2/152 (1%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 1/53 (2%) | 1/74 (1%) |
| secret (hidden, secret) | lie | `␣secretly`, `秘密`, `隐秘`, `␣secrecy` | 3/152 (2%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 1/53 (2%) | 0/74 (0%) |
| conceal (to conceal) | lie | `␣concealed`, `隐瞒` | 2/152 (1%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 0/53 (0%) | 0/74 (0%) |
| mislead (misleading) | lie | `␣misleading` | 1/152 (1%) | 1/81 (1%) | 1/138 (1%) | 0/158 (0%) | 1/53 (2%) | 1/74 (1%) |
| unauthorized (without permission) | unclear | `␣unauthorized`, `␣Unauthorized` | 1/152 (1%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 0/53 (0%) | 0/74 (0%) |
| reject (to reject) | unclear | `␣rejecting`, `␣Reject` | 1/152 (1%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 1/53 (2%) | 1/74 (1%) |
| incorrect (incorrect) | lie | `␣incorrect`, `␣inaccur`, `␣incorrectly`, `␣inaccurate`, `incorrect`, `␣Incorrect`, `不符合` | 1/152 (1%) | 1/81 (1%) | 7/138 (5%) | 4/158 (3%) | 1/53 (2%) | 1/74 (1%) |
| fake (fake) | lie | `␣fake`, `␣Fake` | 1/152 (1%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 0/53 (0%) | 0/74 (0%) |
| silence (staying silent) | unclear | `␣silence`, `␣Silence`, `␣Silent` | 1/152 (1%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 1/53 (2%) | 0/74 (0%) |
| illegal (against the law) | unclear | `␣Illegal`, `Illegal` | 0/152 (0%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 0/53 (0%) | 0/74 (0%) |
| wrong (wrong, mistaken) | lie | `没错` | 0/152 (0%) | 0/81 (0%) | 0/138 (0%) | 1/158 (1%) | 0/53 (0%) | 0/74 (0%) |

Not in the draft: truth (excluded: truth from the question on); admit / acknowledge (excluded: admit / deny / acknowledge); deny (excluded: admit / deny / acknowledge)
