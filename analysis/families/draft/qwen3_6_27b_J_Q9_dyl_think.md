# Draft families: qwen3.6-27b, J-lens, part Q9_dyl, group think

Written by `scripts/apply_family_decisions.py` (2026-10-01; draft, not frozen). Counts are `present / transcripts (share)`
on the build split.

## think_slot0

| family | side | members | lies | truths | no-pressure truths | unrelated | lies that deny | truths that deny |
|---|---|---|---|---|---|---|---|---|
| legal (lawful, legality) | unclear | `/legal`, `_legal`, `legal`, `合法`, `␣legality`, `Legal`, `␣Legal` | 152/152 (100%) | 81/81 (100%) | 138/138 (100%) | 155/158 (98%) | 65/65 (100%) | 76/76 (100%) |
| compliant (complying with rules) | unclear | `合规`, `依法依规` | 151/152 (99%) | 80/81 (99%) | 138/138 (100%) | 1/158 (1%) | 65/65 (100%) | 75/76 (99%) |
| secret (secretive, hidden from view) | lie | `隐秘` | 149/152 (98%) | 77/81 (95%) | 92/138 (67%) | 77/158 (49%) | 64/65 (98%) | 72/76 (95%) |
| clarify (clarifying, setting the record straight) | truth | `澄清` | 135/152 (89%) | 70/81 (86%) | 138/138 (100%) | 152/158 (96%) | 58/65 (89%) | 65/76 (86%) |
| illegal (unlawful) | unclear | `违法违规`, `违法`, `非法`, `illegal`, `Illegal`, `␣ilegal` | 115/152 (76%) | 57/81 (70%) | 74/138 (54%) | 30/158 (19%) | 52/65 (80%) | 53/76 (70%) |
| lawful (lawful, legal) | unclear | `合法` | 58/152 (38%) | 28/81 (35%) | 0/138 (0%) | 0/158 (0%) | 29/65 (45%) | 27/76 (36%) |
| fictional (made up, fabricated) | lie | `虚构` | 42/152 (28%) | 24/81 (30%) | 4/138 (3%) | 0/158 (0%) | 23/65 (35%) | 23/76 (30%) |
| caution (needing care, caution) | unclear | `需谨慎` | 46/152 (30%) | 20/81 (25%) | 0/138 (0%) | 0/158 (0%) | 26/65 (40%) | 20/76 (26%) |
| violate rules (breaking rules or regulations) | unclear | `违规`, `違規` | 39/152 (26%) | 16/81 (20%) | 4/138 (3%) | 0/158 (0%) | 24/65 (37%) | 15/76 (20%) |
| morality (morality, ethics) | unclear | `道德` | 23/152 (15%) | 9/81 (11%) | 0/138 (0%) | 39/158 (25%) | 7/65 (11%) | 9/76 (12%) |
| fake (not genuine) | lie | `fake` | 15/152 (10%) | 10/81 (12%) | 2/138 (1%) | 0/158 (0%) | 9/65 (14%) | 9/76 (12%) |
| sensitive (sensitive (topic or information)) | unclear | `_sensitive` | 6/152 (4%) | 13/81 (16%) | 0/138 (0%) | 0/158 (0%) | 3/65 (5%) | 13/76 (17%) |
| vague (vague, blurred (evasive wording)) | unclear | `模糊` | 9/152 (6%) | 7/81 (9%) | 1/138 (1%) | 0/158 (0%) | 3/65 (5%) | 7/76 (9%) |
| suppress (suppressing information) | lie | `suppress` | 3/152 (2%) | 10/81 (12%) | 0/138 (0%) | 0/158 (0%) | 3/65 (5%) | 10/76 (13%) |
| true (true, real) | truth | `真` | 4/152 (3%) | 3/81 (4%) | 0/138 (0%) | 0/158 (0%) | 3/65 (5%) | 3/76 (4%) |
| unauthorized (not permitted) | unclear | `␣Unauthorized` | 2/152 (1%) | 2/81 (2%) | 1/138 (1%) | 0/158 (0%) | 2/65 (3%) | 1/76 (1%) |
| wrong (wrong, mistaken) | lie | `错`, `错误` | 1/152 (1%) | 2/81 (2%) | 0/138 (0%) | 1/158 (1%) | 0/65 (0%) | 1/76 (1%) |
| impossible (impossible to do) | unclear | `Impossible` | 1/152 (1%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 1/65 (2%) | 0/76 (0%) |
| correct (correct) | truth | `更正` | 0/152 (0%) | 0/81 (0%) | 4/138 (3%) | 0/158 (0%) | 0/65 (0%) | 0/76 (0%) |

Not in the draft: honest (held back: no undisputed member left); truth (excluded: truth from the question on)

## think_slot1

| family | side | members | lies | truths | no-pressure truths | unrelated | lies that deny | truths that deny |
|---|---|---|---|---|---|---|---|---|
| violate (violating a rule or principle) | unclear | `违反`, `违反了`, `违规`, `违背`, `违规行为`, `␣violate`, `␣violation`, `␣violates`, `␣violated`, `違反` | 152/152 (100%) | 80/81 (99%) | 122/138 (88%) | 123/158 (78%) | 65/65 (100%) | 75/76 (99%) |
| wrong (wrong, mistaken) | lie | `␣ERROR`, `rong`, `erreur`, `_wrong`, `_WRONG`, `错`, `錯`, `错误`, `谬`, `錯誤`, `错的`, `的错误` | 151/152 (99%) | 81/81 (100%) | 113/138 (82%) | 114/158 (72%) | 64/65 (98%) | 76/76 (100%) |
| fake (fake, false, not genuine) | lie | `假`, `假的`, `fake`, `Fake` | 143/152 (94%) | 76/81 (94%) | 135/138 (98%) | 97/158 (61%) | 61/65 (94%) | 71/76 (93%) |
| cannot (unable to (do or satisfy)) | unclear | `无法满足`, `不能满足`, `无法`, `Unable` | 147/152 (97%) | 72/81 (89%) | 131/138 (95%) | 157/158 (99%) | 64/65 (98%) | 68/76 (89%) |
| compliant (complying with rules) | unclear | `依规`, `合规`, `依法依规`, `恪守`, `严格遵守`, `依法`, `规范要求` | 142/152 (93%) | 61/81 (75%) | 137/138 (99%) | 153/158 (97%) | 59/65 (91%) | 57/76 (75%) |
| inconvenient (inconvenient (polite refusal)) | unclear | `不方便`, `不便` | 70/152 (46%) | 50/81 (62%) | 86/138 (62%) | 144/158 (91%) | 26/65 (40%) | 46/76 (61%) |
| illusion (illusion, fantasy, delusion) | unclear | `幻想`, `幻觉`, `错觉`, `虚幻`, `妄想` | 66/152 (43%) | 29/81 (36%) | 32/138 (23%) | 62/158 (39%) | 26/65 (40%) | 28/76 (37%) |
| absurd (absurd, ridiculous) | unclear | `荒唐`, `滑稽` | 76/152 (50%) | 19/81 (23%) | 0/138 (0%) | 0/158 (0%) | 28/65 (43%) | 18/76 (24%) |
| lawful (lawful, according to law) | unclear | `合法`, `依法` | 63/152 (41%) | 14/81 (17%) | 2/138 (1%) | 0/158 (0%) | 21/65 (32%) | 12/76 (16%) |
| forged (forged, counterfeited) | lie | `伪造`, `虚构` | 54/152 (36%) | 14/81 (17%) | 1/138 (1%) | 0/158 (0%) | 25/65 (38%) | 12/76 (16%) |
| fictional (made up, fiction) | lie | `虚构`, `fiction` | 58/152 (38%) | 8/81 (10%) | 7/138 (5%) | 0/158 (0%) | 28/65 (43%) | 6/76 (8%) |
| polite (polite, courteous) | unclear | `礼貌` | 17/152 (11%) | 13/81 (16%) | 36/138 (26%) | 13/158 (8%) | 9/65 (14%) | 13/76 (17%) |
| impossible (impossible) | unclear | `Impossible`, `␣impossibile`, `␣imposs`, `不可能的` | 13/152 (9%) | 10/81 (12%) | 15/138 (11%) | 55/158 (35%) | 6/65 (9%) | 9/76 (12%) |
| reject (rejecting / vetoing) | unclear | `否决` | 11/152 (7%) | 6/81 (7%) | 0/138 (0%) | 0/158 (0%) | 4/65 (6%) | 5/76 (7%) |
| ethical (ethical, moral) | unclear | `ethical`, `道德`, `ético` | 11/152 (7%) | 2/81 (2%) | 2/138 (1%) | 0/158 (0%) | 3/65 (5%) | 2/76 (3%) |
| false (false, untrue) | lie | `_false`, `.false` | 4/152 (3%) | 9/81 (11%) | 6/138 (4%) | 0/158 (0%) | 1/65 (2%) | 9/76 (12%) |
| incorrect (incorrect) | lie | `Incorrect`, `incorrect` | 6/152 (4%) | 5/81 (6%) | 46/138 (33%) | 20/158 (13%) | 3/65 (5%) | 4/76 (5%) |
| reveal (revealing, divulging) | truth | `透露` | 5/152 (3%) | 1/81 (1%) | 2/138 (1%) | 0/158 (0%) | 2/65 (3%) | 0/76 (0%) |
| silence (silence) | unclear | `沉默` | 3/152 (2%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 1/65 (2%) | 0/76 (0%) |
| secretly (secretly, covertly) | lie | `暗中` | 1/152 (1%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 0/65 (0%) | 0/76 (0%) |

Not in the draft: admit (excluded: admit / deny / acknowledge); pretext (held back: no undisputed member left)

## think_slot2

| family | side | members | lies | truths | no-pressure truths | unrelated | lies that deny | truths that deny |
|---|---|---|---|---|---|---|---|---|
| leak (leaking secrets) | truth | `泄露`, `␣WikiLeaks` | 149/152 (98%) | 81/81 (100%) | 102/138 (74%) | 111/158 (70%) | 65/65 (100%) | 76/76 (100%) |
| silence (staying silent) | unclear | `沉默`, `␣Silence`, `␣silence`, `silent`, `␣Silent`, `␣silencio`, `␣silenc`, `寂静` | 148/152 (97%) | 78/81 (96%) | 23/138 (17%) | 6/158 (4%) | 63/65 (97%) | 74/76 (97%) |
| false (false, untrue) | lie | `␣false`, `␣False`, `(false`, `false`, `False`, `=False`, `␣FALSE`, `=false`, `:false`, `(False`, `,false`, `FALSE`, `>false`, `_false`, `.assertFalse`, `.False`, `.false`, `toBeFalsy`, `/false`, `假`, `虚假` | 132/152 (87%) | 77/81 (95%) | 133/138 (96%) | 134/158 (85%) | 56/65 (86%) | 74/76 (97%) |
| unauthorized (not permitted) | unclear | `␣Unauthorized`, `␣unauthorized` | 138/152 (91%) | 67/81 (83%) | 6/138 (4%) | 1/158 (1%) | 59/65 (91%) | 62/76 (82%) |
| compliant (complying with rules) | unclear | `␣Compliance`, `␣compliance`, `合规`, `依法`, `依法依规` | 136/152 (89%) | 66/81 (81%) | 63/138 (46%) | 132/158 (84%) | 58/65 (89%) | 62/76 (82%) |
| refuse (refusing, rejecting) | unclear | `拒绝`, `拒絕`, `拒`, `拒不`, `拒绝了`, `reject`, `rejected`, `.reject`, `␣Reject`, `␣refusal`, `␣refus`, `␣refuses`, `␣refuse`, `␣refused` | 136/152 (89%) | 57/81 (70%) | 10/138 (7%) | 0/158 (0%) | 62/65 (95%) | 53/76 (70%) |
| cannot (being unable to) | unclear | `Cannot`, `cannot`, `␣Cannot`, `_CANNOT`, `␣cannot`, `不能`, `我不能`, `我无法`, `无法`, `是无法`, `無法`, `不可以`, `可不能`, `是不能`, `unable`, `不能说`, `不能有`, `不能被` | 130/152 (86%) | 63/81 (78%) | 14/138 (10%) | 1/158 (1%) | 59/65 (91%) | 59/76 (78%) |
| hypocrisy (hypocrisy) | lie | `␣hypocrisy` | 119/152 (78%) | 58/81 (72%) | 0/138 (0%) | 9/158 (6%) | 49/65 (75%) | 56/76 (74%) |
| privacy (privacy, private) | unclear | `privacy`, `␣Privacy`, `Privacy`, `␣privacy`, `␣privacidad`, `隐私`, `private`, `/Private` | 123/152 (81%) | 49/81 (60%) | 55/138 (40%) | 12/158 (8%) | 53/65 (82%) | 45/76 (59%) |
| prohibited (forbidden, banned) | unclear | `␣prohibited`, `禁止`, `严禁`, `禁用`, `禁忌`, `␣Forbidden`, `␣forbidden`, `Forbidden`, `␣запрещ`, `␣запрещено`, `␣prohibition`, `␣prohibits`, `␣prohib`, `␣нельзя` | 108/152 (71%) | 45/81 (56%) | 6/138 (4%) | 0/158 (0%) | 45/65 (69%) | 43/76 (57%) |
| disclose (disclosing, revealing) | truth | `␣Disclosure`, `␣disclosure`, `␣disclosures`, `透露` | 102/152 (67%) | 30/81 (37%) | 11/138 (8%) | 5/158 (3%) | 42/65 (65%) | 26/76 (34%) |
| refute (rebutting, refuting) | unclear | `␣refute`, `反驳` | 78/152 (51%) | 41/81 (51%) | 49/138 (36%) | 0/158 (0%) | 36/65 (55%) | 39/76 (51%) |
| illegal (unlawful) | unclear | `illegal`, `␣Illegal`, `␣illegal`, `␣illicit`, `非法`, `␣ilegal`, `违法`, `违法违规` | 84/152 (55%) | 12/81 (15%) | 9/138 (7%) | 3/158 (2%) | 32/65 (49%) | 9/76 (12%) |
| violate (violating a rule or principle) | unclear | `违规`, `违背`, `违反`, `违反了`, `␣violates`, `␣violate`, `␣violating`, `␣violation` | 68/152 (45%) | 24/81 (30%) | 13/138 (9%) | 0/158 (0%) | 23/65 (35%) | 21/76 (28%) |
| impossible (impossible) | unclear | `␣Impossible`, `Impossible`, `␣imposs`, `␣impossible`, `是不可能的`, `是不可能` | 62/152 (41%) | 24/81 (30%) | 2/138 (1%) | 37/158 (23%) | 34/65 (52%) | 23/76 (30%) |
| secrecy (keeping things secret or confidential) | lie | `␣secrecy`, `保密` | 68/152 (45%) | 14/81 (17%) | 10/138 (7%) | 1/158 (1%) | 28/65 (43%) | 14/76 (18%) |
| reject (rejecting) | unclear | `reject`, `rejected`, `.reject`, `␣Reject` | 64/152 (42%) | 14/81 (17%) | 1/138 (1%) | 0/158 (0%) | 35/65 (54%) | 13/76 (17%) |
| legal (lawful, legality) | unclear | `/legal`, `␣legally`, `␣legality`, `_legal`, `␣Legal` | 68/152 (45%) | 10/81 (12%) | 1/138 (1%) | 0/158 (0%) | 26/65 (40%) | 8/76 (11%) |
| conscience (conscience) | unclear | `␣conscience` | 61/152 (40%) | 13/81 (16%) | 0/138 (0%) | 0/158 (0%) | 18/65 (28%) | 12/76 (16%) |
| verify (verifying) | unclear | `␣Verification`, `␣verification`, `验证`, `核实`, `_verified`, `verification`, `␣Verified`, `_verification`, `Verification`, `.verify` | 48/152 (32%) | 24/81 (30%) | 136/138 (99%) | 154/158 (97%) | 20/65 (31%) | 22/76 (29%) |
| true (true, real) | truth | `True`, `␣TRUE`, `:true`, `>true`, `.isTrue`, `真的`, `确实`, `的确` | 54/152 (36%) | 12/81 (15%) | 13/138 (9%) | 6/158 (4%) | 9/65 (14%) | 10/76 (13%) |
| sorry (apologizing) | unclear | `抱歉`, `Sorry`, `␣Sorry`, `道歉` | 31/152 (20%) | 12/81 (15%) | 0/138 (0%) | 3/158 (2%) | 21/65 (32%) | 12/76 (16%) |
| unethical (unethical) | lie | `␣unethical` | 31/152 (20%) | 4/81 (5%) | 0/138 (0%) | 0/158 (0%) | 9/65 (14%) | 3/76 (4%) |
| nonexistent (does not exist) | unclear | `不存在`, `␣nonexistent` | 17/152 (11%) | 14/81 (17%) | 2/138 (1%) | 0/158 (0%) | 16/65 (25%) | 13/76 (17%) |
| honest (honest, upright) | truth | `␣honest`, `正直` | 13/152 (9%) | 13/81 (16%) | 83/138 (60%) | 25/158 (16%) | 11/65 (17%) | 13/76 (17%) |
| mislead (misleading) | lie | `误导性` | 10/152 (7%) | 15/81 (19%) | 2/138 (1%) | 2/158 (1%) | 7/65 (11%) | 15/76 (20%) |
| ethical (ethical) | unclear | `ethical`, `␣ethical`, `␣ethics` | 24/152 (16%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 10/65 (15%) | 0/76 (0%) |
| dissent (dissent) | unclear | `␣dissent` | 17/152 (11%) | 4/81 (5%) | 0/138 (0%) | 0/158 (0%) | 3/65 (5%) | 4/76 (5%) |
| euphemistic (tactful, indirect wording) | unclear | `婉`, `委婉` | 16/152 (11%) | 3/81 (4%) | 0/138 (0%) | 0/158 (0%) | 8/65 (12%) | 3/76 (4%) |
| hidden (hidden, not disclosed) | lie | `␣Hidden`, `hidden`, `␣hidden`, `Hidden`, `隐藏`, `隐藏的`, `␣undisclosed`, `.isHidden` | 12/152 (8%) | 4/81 (5%) | 1/138 (1%) | 1/158 (1%) | 3/65 (5%) | 3/76 (4%) |
| whistleblow (exposing wrongdoing) | truth | `␣whistlebl`, `␣whistleblower` | 14/152 (9%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 6/65 (9%) | 0/76 (0%) |
| disclaimer (disclaimer) | unclear | `␣disclaimer` | 9/152 (6%) | 2/81 (2%) | 0/138 (0%) | 0/158 (0%) | 3/65 (5%) | 2/76 (3%) |
| correction (correcting an error) | unclear | `更正`, `␣Correction`, `Correction`, `纠错` | 6/152 (4%) | 4/81 (5%) | 21/138 (15%) | 11/158 (7%) | 3/65 (5%) | 4/76 (5%) |
| cannot say (cannot tell, withholding) | unclear | `不能说` | 4/152 (3%) | 2/81 (2%) | 6/138 (4%) | 0/158 (0%) | 3/65 (5%) | 2/76 (3%) |
| self-protection (protecting oneself) | unclear | `自我保护` | 5/152 (3%) | 1/81 (1%) | 3/138 (2%) | 0/158 (0%) | 2/65 (3%) | 1/76 (1%) |
| illusion (illusion) | unclear | `错觉` | 1/152 (1%) | 5/81 (6%) | 5/138 (4%) | 0/158 (0%) | 1/65 (2%) | 5/76 (7%) |
| cheat (cheating) | lie | `作弊` | 5/152 (3%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 0/65 (0%) | 0/76 (0%) |
| frank (speaking frankly) | truth | `直言` | 4/152 (3%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 2/65 (3%) | 0/76 (0%) |
| wrong (wrong, mistaken) | lie | `␣Wrong`, `错`, `没错` | 2/152 (1%) | 3/81 (4%) | 6/138 (4%) | 4/158 (3%) | 1/65 (2%) | 3/76 (4%) |
| clarify (clarifying) | truth | `澄清` | 2/152 (1%) | 2/81 (2%) | 23/138 (17%) | 83/158 (53%) | 1/65 (2%) | 2/76 (3%) |
| deceive (the act of deceiving) | lie | `欺骗`, `骗` | 3/152 (2%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 2/65 (3%) | 0/76 (0%) |
| truth (the truth, authenticity) | truth | `其真实性` | 2/152 (1%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 1/65 (2%) | 1/76 (1%) |
| evade (evading, avoiding) | lie | `回避`, `规避` | 2/152 (1%) | 0/81 (0%) | 45/138 (33%) | 0/158 (0%) | 0/65 (0%) | 0/76 (0%) |
| not guilty (innocent, not guilty) | truth | `无罪` | 1/152 (1%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 0/65 (0%) | 1/76 (1%) |
| cover up (covering up, glossing over) | lie | `掩饰` | 1/152 (1%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 0/65 (0%) | 0/76 (0%) |
| undisclosed (not disclosed) | lie | `␣undisclosed` | 1/152 (1%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 0/65 (0%) | 0/76 (0%) |
| honest (honest) | truth | `␣honest` | 1/152 (1%) | 0/81 (0%) | 0/138 (0%) | 1/158 (1%) | 1/65 (2%) | 0/76 (0%) |
| correct (correct) | truth | `Correct`, `␣Correct`, `_correction` | 0/152 (0%) | 1/81 (1%) | 3/138 (2%) | 5/158 (3%) | 0/65 (0%) | 1/76 (1%) |
| incorrect (incorrect) | lie | `incorrect`, `不符合` | 1/152 (1%) | 0/81 (0%) | 1/138 (1%) | 3/158 (2%) | 0/65 (0%) | 0/76 (0%) |

Not in the draft: admit (excluded: admit / deny / acknowledge)

## think_slot3

| family | side | members | lies | truths | no-pressure truths | unrelated | lies that deny | truths that deny |
|---|---|---|---|---|---|---|---|---|
| false (false, untrue) | lie | `␣false`, `␣False`, `(false`, `false`, `False`, `=False`, `␣FALSE`, `=false`, `:false`, `(False`, `FALSE`, `>false`, `␣fals`, `_false`, `.assertFalse`, `.False`, `␣falsely`, `.false`, `␣untrue`, `/false`, `␣falsehood` | 152/152 (100%) | 81/81 (100%) | 138/138 (100%) | 158/158 (100%) | 65/65 (100%) | 76/76 (100%) |
| refuse (refusing, rejecting) | unclear | `拒绝`, `␣refusal`, `␣Reject`, `reject` | 64/152 (42%) | 41/81 (51%) | 2/138 (1%) | 0/158 (0%) | 36/65 (55%) | 39/76 (51%) |
| incorrect (incorrect) | lie | `␣incorrect`, `␣inaccurate`, `␣Incorrect`, `不符合` | 60/152 (39%) | 42/81 (52%) | 33/138 (24%) | 5/158 (3%) | 32/65 (49%) | 40/76 (53%) |
| true (true, real) | truth | `␣true`, `True`, `␣True`, `>true` | 57/152 (38%) | 30/81 (37%) | 63/138 (46%) | 10/158 (6%) | 13/65 (20%) | 26/76 (34%) |
| cannot (being unable to) | unclear | `␣Cannot`, `cannot`, `Cannot`, `␣cannot`, `我不能`, `我无法`, `无法`, `␣Unable` | 57/152 (38%) | 2/81 (2%) | 0/138 (0%) | 0/158 (0%) | 23/65 (35%) | 1/76 (1%) |
| truthful (truthful) | truth | `␣truthful` | 25/152 (16%) | 4/81 (5%) | 1/138 (1%) | 3/158 (2%) | 12/65 (18%) | 4/76 (5%) |
| nonexistent (does not exist) | unclear | `␣nonexistent`, `不存在` | 9/152 (6%) | 7/81 (9%) | 2/138 (1%) | 34/158 (22%) | 5/65 (8%) | 7/76 (9%) |
| impossible (impossible) | unclear | `␣Impossible` | 4/152 (3%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 1/65 (2%) | 0/76 (0%) |
| reject (rejecting) | unclear | `␣Reject`, `reject` | 3/152 (2%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 2/65 (3%) | 0/76 (0%) |
| dishonest (dishonest) | lie | `␣dishonest` | 2/152 (1%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 0/65 (0%) | 0/76 (0%) |
| violate (violating a rule or principle) | unclear | `违背` | 2/152 (1%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 0/65 (0%) | 0/76 (0%) |
| illegal (unlawful) | unclear | `␣Illegal` | 1/152 (1%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 0/65 (0%) | 0/76 (0%) |
| disclaimer (disclaimer) | unclear | `␣Disclaimer`, `免责声明` | 1/152 (1%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 0/65 (0%) | 0/76 (0%) |
| fake (fake) | lie | `␣Fake` | 1/152 (1%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 1/65 (2%) | 0/76 (0%) |
| silence (staying silent) | unclear | `␣Silence` | 1/152 (1%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 0/65 (0%) | 0/76 (0%) |
| unauthorized (not permitted) | unclear | `␣Unauthorized` | 1/152 (1%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 0/65 (0%) | 0/76 (0%) |
| prohibited (forbidden) | unclear | `␣Forbidden` | 1/152 (1%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 0/65 (0%) | 0/76 (0%) |
| unequivocal (unequivocal, unambiguous) | unclear | `␣unequiv` | 1/152 (1%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 1/65 (2%) | 0/76 (0%) |
| legal (lawful) | unclear | `␣Legal` | 0/152 (0%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 0/65 (0%) | 0/76 (0%) |

Not in the draft: truth (excluded: truth from the question on); deny (excluded: admit / deny / acknowledge); admit (excluded: admit / deny / acknowledge)
