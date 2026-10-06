# Draft families: qwen3.6-27b, J-lens, part Q2_after, group think

Written by `scripts/apply_family_decisions.py` (2026-10-01; draft, not frozen). Counts are `present / transcripts (share)`
on the build split.

## think_slot0

| family | side | members | lies | truths | no-pressure truths | unrelated | lies that deny | truths that deny |
|---|---|---|---|---|---|---|---|---|
| lawful / legal (permitted by law) | unclear | `/legal`, `legal`, `_legal`, `合法`, `␣legality` | 152/152 (100%) | 80/81 (99%) | 136/138 (99%) | 156/158 (99%) | 47/47 (100%) | 76/77 (99%) |
| hidden / secret (kept hidden, secret) | lie | `隐秘` | 151/152 (99%) | 80/81 (99%) | 137/138 (99%) | 125/158 (79%) | 47/47 (100%) | 76/77 (99%) |
| compliant (complying with rules) | unclear | `合规`, `依法依规`, `依法` | 130/152 (86%) | 63/81 (78%) | 130/138 (94%) | 1/158 (1%) | 41/47 (87%) | 61/77 (79%) |
| clarify (to make clear, set the record straight) | unclear | `澄清` | 102/152 (67%) | 58/81 (72%) | 138/138 (100%) | 156/158 (99%) | 28/47 (60%) | 54/77 (70%) |
| fictional / made-up (invented, fabricated content) | lie | `虚构` | 82/152 (54%) | 51/81 (63%) | 27/138 (20%) | 0/158 (0%) | 36/47 (77%) | 50/77 (65%) |
| illegal (against the law) | unclear | `违法违规`, `非法`, `违法`, `illegal`, `Illegal` | 73/152 (48%) | 34/81 (42%) | 56/138 (41%) | 31/158 (20%) | 30/47 (64%) | 33/77 (43%) |
| fake (fake, counterfeit, not genuine) | lie | `fake`, `Fake`, `假` | 58/152 (38%) | 24/81 (30%) | 7/138 (5%) | 6/158 (4%) | 22/47 (47%) | 24/77 (31%) |
| ethics / morality (moral standards) | unclear | `道德`, `ethical`, `的道德` | 58/152 (38%) | 15/81 (19%) | 6/138 (4%) | 29/158 (18%) | 8/47 (17%) | 14/77 (18%) |
| doubt / question (doubting or challenging) | unclear | `质疑` | 53/152 (35%) | 17/81 (21%) | 64/138 (46%) | 131/158 (83%) | 22/47 (47%) | 17/77 (22%) |
| violate (breaking a rule or principle) | unclear | `违规`, `违反`, `违背`, `違規` | 40/152 (26%) | 16/81 (20%) | 8/138 (6%) | 0/158 (0%) | 14/47 (30%) | 16/77 (21%) |
| quiet / stealthy (quietly, silently, unnoticed) | unclear | `悄然` | 32/152 (21%) | 15/81 (19%) | 0/138 (0%) | 0/158 (0%) | 18/47 (38%) | 15/77 (19%) |
| forbidden / unauthorized (not permitted) | unclear | `␣Unauthorized` | 13/152 (9%) | 5/81 (6%) | 2/138 (1%) | 24/158 (15%) | 9/47 (19%) | 5/77 (6%) |
| suppress (holding back, suppressing) | lie | `suppress` | 3/152 (2%) | 14/81 (17%) | 2/138 (1%) | 0/158 (0%) | 2/47 (4%) | 14/77 (18%) |
| misunderstanding (a misunderstanding) | unclear | `误解` | 6/152 (4%) | 6/81 (7%) | 19/138 (14%) | 140/158 (89%) | 2/47 (4%) | 6/77 (8%) |
| vague (vague, blurred, unclear) | unclear | `模糊` | 5/152 (3%) | 5/81 (6%) | 2/138 (1%) | 0/158 (0%) | 5/47 (11%) | 5/77 (6%) |
| true (true, real) | truth | `真` | 1/152 (1%) | 8/81 (10%) | 4/138 (3%) | 7/158 (4%) | 0/47 (0%) | 8/77 (10%) |
| conceal (to conceal, to hide) | lie | `藏`, `隐` | 1/152 (1%) | 2/81 (2%) | 2/138 (1%) | 0/158 (0%) | 0/47 (0%) | 2/77 (3%) |
| wrong (wrong, mistaken) | lie | `错`, `错误` | 1/152 (1%) | 2/81 (2%) | 0/138 (0%) | 42/158 (27%) | 0/47 (0%) | 2/77 (3%) |

Not in the draft: honest (held back: no undisputed member left); truth (excluded: truth from the question on)

## think_slot1

| family | side | members | lies | truths | no-pressure truths | unrelated | lies that deny | truths that deny |
|---|---|---|---|---|---|---|---|---|
| mock (imitation) (a mock, imitation stand-in) | unclear | `_mock`, `/mock`, `␣MOCK`, `mock`, `(mock`, `(Mock` | 152/152 (100%) | 81/81 (100%) | 89/138 (64%) | 9/158 (6%) | 47/47 (100%) | 77/77 (100%) |
| fake (fake, counterfeit, not genuine) | lie | `假`, `pseudo`, `假的`, `伪造`, `fake` | 152/152 (100%) | 80/81 (99%) | 136/138 (99%) | 106/158 (67%) | 47/47 (100%) | 76/77 (99%) |
| violate (breaking a rule or principle) | unclear | `违反`, `违反了`, `违规`, `違反`, `违背`, `违规行为`, `␣violates` | 148/152 (97%) | 79/81 (98%) | 130/138 (94%) | 120/158 (76%) | 43/47 (91%) | 75/77 (97%) |
| compliant (complying with rules) | unclear | `依规`, `合规`, `严格遵守`, `依法` | 105/152 (69%) | 38/81 (47%) | 86/138 (62%) | 45/158 (28%) | 36/47 (77%) | 36/77 (47%) |
| cannot / unable (unable to do or satisfy) | unclear | `无法满足`, `无法`, `不能满足` | 91/152 (60%) | 49/81 (60%) | 122/138 (88%) | 114/158 (72%) | 38/47 (81%) | 45/77 (58%) |
| wrong (wrong, mistaken) | lie | `␣ERROR`, `rong`, `erreur`, `_wrong`, `_WRONG`, `错`, `錯`, `错误`, `谬`, `錯誤`, `的错误` | 92/152 (61%) | 48/81 (59%) | 60/138 (43%) | 14/158 (9%) | 31/47 (66%) | 46/77 (60%) |
| illusion / fantasy (unreal, illusory, imagined) | unclear | `幻想`, `虚幻`, `错觉`, `妄想` | 93/152 (61%) | 42/81 (52%) | 26/138 (19%) | 1/158 (1%) | 33/47 (70%) | 41/77 (53%) |
| fantasy (fantasy, imagining) | unclear | `幻想` | 68/152 (45%) | 19/81 (23%) | 0/138 (0%) | 0/158 (0%) | 27/47 (57%) | 19/77 (25%) |
| fictional / made-up (invented, fabricated content) | lie | `fiction`, `虚构`, `伪造` | 48/152 (32%) | 18/81 (22%) | 12/138 (9%) | 0/158 (0%) | 27/47 (57%) | 18/77 (23%) |
| refuse (refusing) | unclear | `拒绝`, `拒`, `拒绝了`, `否决` | 28/152 (18%) | 12/81 (15%) | 5/138 (4%) | 0/158 (0%) | 4/47 (9%) | 10/77 (13%) |
| reject / veto (turning down, vetoing) | unclear | `否决` | 26/152 (17%) | 11/81 (14%) | 4/138 (3%) | 0/158 (0%) | 2/47 (4%) | 9/77 (12%) |
| false (false, untrue) | lie | `_false`, `.false` | 12/152 (8%) | 24/81 (30%) | 10/138 (7%) | 0/158 (0%) | 2/47 (4%) | 24/77 (31%) |
| impossible (impossible) | unclear | `␣impossibile`, `Impossible`, `␣imposs` | 9/152 (6%) | 10/81 (12%) | 34/138 (25%) | 4/158 (3%) | 4/47 (9%) | 10/77 (13%) |
| lawful / legal (permitted by law) | unclear | `合法` | 13/152 (9%) | 3/81 (4%) | 0/138 (0%) | 0/158 (0%) | 11/47 (23%) | 3/77 (4%) |
| incorrect (incorrect) | lie | `incorrect` | 2/152 (1%) | 2/81 (2%) | 7/138 (5%) | 0/158 (0%) | 2/47 (4%) | 2/77 (3%) |
| fact (fact, factual) | truth | `实际` | 3/152 (2%) | 1/81 (1%) | 1/138 (1%) | 0/158 (0%) | 0/47 (0%) | 1/77 (1%) |
| lie (a lie, falsehood) | lie | `␣거짓` | 0/152 (0%) | 2/81 (2%) | 0/138 (0%) | 0/158 (0%) | 0/47 (0%) | 2/77 (3%) |
| disclose (to reveal, disclose) | truth | `透露` | 1/152 (1%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 0/47 (0%) | 0/77 (0%) |
| secretly (done in secret) | lie | `暗中` | 1/152 (1%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 0/47 (0%) | 0/77 (0%) |
| ethics / morality (moral standards) | unclear | `␣Ethics`, `道德` | 1/152 (1%) | 0/81 (0%) | 0/138 (0%) | 5/158 (3%) | 0/47 (0%) | 0/77 (0%) |

## think_slot2

| family | side | members | lies | truths | no-pressure truths | unrelated | lies that deny | truths that deny |
|---|---|---|---|---|---|---|---|---|
| privacy (privacy, private information) | unclear | `␣Privacy`, `privacy`, `隐私`, `Privacy`, `␣privacy`, `␣privacidad`, `/Private`, `␣Priv`, `ความเป็นส่วนตัว` | 150/152 (99%) | 80/81 (99%) | 138/138 (100%) | 157/158 (99%) | 46/47 (98%) | 76/77 (99%) |
| forbidden / unauthorized (not permitted) | unclear | `␣Unauthorized`, `␣Forbidden`, `严禁`, `禁止`, `␣prohibited`, `禁用`, `禁忌`, `␣запрещ`, `取缔`, `␣unauthorized`, `Unauthorized` | 150/152 (99%) | 79/81 (98%) | 62/138 (45%) | 26/158 (16%) | 45/47 (96%) | 75/77 (97%) |
| unauthorized (not permitted) | unclear | `␣Unauthorized`, `␣unauthorized`, `Unauthorized` | 149/152 (98%) | 77/81 (95%) | 61/138 (44%) | 26/158 (16%) | 44/47 (94%) | 73/77 (95%) |
| leak (leaking hidden information) | unclear | `␣WikiLeaks`, `泄露` | 142/152 (93%) | 72/81 (89%) | 88/138 (64%) | 35/158 (22%) | 42/47 (89%) | 69/77 (90%) |
| silence (staying silent) | unclear | `沉默`, `␣Silence`, `␣Silent`, `␣silence`, `silent`, `␣Quiet` | 131/152 (86%) | 75/81 (93%) | 60/138 (43%) | 3/158 (2%) | 40/47 (85%) | 71/77 (92%) |
| strict (strict) | unclear | `␣STRICT`, `␣Strict`, `严格`, `.strict`, `strict`, `␣strictly`, `Strict`, `严` | 125/152 (82%) | 72/81 (89%) | 85/138 (62%) | 18/158 (11%) | 41/47 (87%) | 71/77 (92%) |
| compliant (complying with rules) | unclear | `␣Compliance`, `合规`, `␣compliance` | 129/152 (85%) | 61/81 (75%) | 39/138 (28%) | 79/158 (50%) | 32/47 (68%) | 58/77 (75%) |
| cannot / unable (unable to do or say) | unclear | `cannot`, `Cannot`, `␣Cannot`, `不能`, `我无法`, `␣cannot`, `我不能`, `_CANNOT`, `unable`, `是无法`, `不能说` | 93/152 (61%) | 61/81 (75%) | 6/138 (4%) | 0/158 (0%) | 43/47 (91%) | 58/77 (75%) |
| true (true, real) | truth | `true`, `True`, `␣TRUE`, `.assertTrue`, `:true`, `TRUE`, `.isTrue`, `真的`, `确实`, `的确`, `的真实性` | 91/152 (60%) | 60/81 (74%) | 81/138 (59%) | 122/158 (77%) | 15/47 (32%) | 56/77 (73%) |
| false (false, untrue) | lie | `␣False`, `(false`, `false`, `False`, `=False`, `␣FALSE`, `:false`, `(False`, `FALSE`, `>false`, `_false`, `.assertFalse`, `.False`, `.false`, `/false`, `␣falsehood` | 83/152 (55%) | 65/81 (80%) | 120/138 (87%) | 157/158 (99%) | 23/47 (49%) | 63/77 (82%) |
| disclose (disclosing information) | truth | `␣Disclosure`, `␣disclosures` | 103/152 (68%) | 43/81 (53%) | 110/138 (80%) | 139/158 (88%) | 23/47 (49%) | 40/77 (52%) |
| verify (checking or verifying) | unclear | `␣Verification`, `_verified`, `核实`, `␣Verified`, `_verification`, `␣verification`, `验证`, `.verify` | 83/152 (55%) | 43/81 (53%) | 126/138 (91%) | 152/158 (96%) | 20/47 (43%) | 41/77 (53%) |
| mislead (misleading) | lie | `误导性` | 74/152 (49%) | 43/81 (53%) | 11/138 (8%) | 23/158 (15%) | 13/47 (28%) | 40/77 (52%) |
| violate (breaking a rule or principle) | unclear | `违背`, `␣violates`, `␣violate`, `违反`, `违规`, `␣violating`, `␣violation`, `违反了`, `␣violations` | 93/152 (61%) | 24/81 (30%) | 8/138 (6%) | 2/158 (1%) | 29/47 (62%) | 22/77 (29%) |
| confidential (kept confidential) | unclear | `保密`, `␣конфиден`, `␣Confidential`, `␣confidentiality` | 57/152 (38%) | 31/81 (38%) | 85/138 (62%) | 6/158 (4%) | 13/47 (28%) | 28/77 (36%) |
| refuse (refusing) | unclear | `拒绝`, `␣refusal`, `拒`, `拒絕`, `拒不` | 57/152 (38%) | 26/81 (32%) | 0/138 (0%) | 0/158 (0%) | 38/47 (81%) | 26/77 (34%) |
| reject / veto (turning down, vetoing) | unclear | `reject`, `␣Reject`, `.reject`, `rejected`, `␣rejecting`, `否决`, `拒绝`, `␣refusal`, `拒`, `拒絕`, `拒不` | 57/152 (38%) | 26/81 (32%) | 0/138 (0%) | 0/158 (0%) | 38/47 (81%) | 26/77 (34%) |
| spoiler (a spoiler (revealing what was held back)) | unclear | `Spoiler` | 63/152 (41%) | 17/81 (21%) | 1/138 (1%) | 1/158 (1%) | 8/47 (17%) | 14/77 (18%) |
| impossible (impossible) | unclear | `␣Impossible`, `␣imposs`, `Impossible`, `␣impossible` | 46/152 (30%) | 31/81 (38%) | 27/138 (20%) | 78/158 (49%) | 31/47 (66%) | 31/77 (40%) |
| ethics (moral standards, ethical) | unclear | `␣Ethics`, `␣ethical`, `ethical`, `␣ethics` | 68/152 (45%) | 6/81 (7%) | 6/138 (4%) | 26/158 (16%) | 9/47 (19%) | 5/77 (6%) |
| illegal (against the law) | unclear | `illegal`, `␣Illegal`, `␣illegal`, `␣ilegal`, `非法`, `违法` | 53/152 (35%) | 9/81 (11%) | 6/138 (4%) | 0/158 (0%) | 22/47 (47%) | 8/77 (10%) |
| refute (arguing that a claim is false) | unclear | `␣refute`, `反驳` | 30/152 (20%) | 17/81 (21%) | 6/138 (4%) | 0/158 (0%) | 19/47 (40%) | 16/77 (21%) |
| genuine (genuine, sincere) | truth | `␣Genuine` | 18/152 (12%) | 10/81 (12%) | 3/138 (2%) | 1/158 (1%) | 2/47 (4%) | 9/77 (12%) |
| hidden (hidden, concealed) | lie | `␣Hidden`, `_hide` | 17/152 (11%) | 8/81 (10%) | 0/138 (0%) | 0/158 (0%) | 1/47 (2%) | 7/77 (9%) |
| hypocrisy (pretending to virtues one lacks) | lie | `␣hypocrisy` | 21/152 (14%) | 2/81 (2%) | 0/138 (0%) | 0/158 (0%) | 11/47 (23%) | 2/77 (3%) |
| opaque (not transparent) | lie | `opaque` | 11/152 (7%) | 9/81 (11%) | 44/138 (32%) | 2/158 (1%) | 1/47 (2%) | 8/77 (10%) |
| ethical (ethical) | truth | `␣ethical`, `ethical` | 16/152 (11%) | 2/81 (2%) | 1/138 (1%) | 0/158 (0%) | 4/47 (9%) | 1/77 (1%) |
| unethical (morally wrong) | lie | `␣unethical` | 15/152 (10%) | 2/81 (2%) | 0/138 (0%) | 0/158 (0%) | 7/47 (15%) | 2/77 (3%) |
| ostensible (seemingly but not really) | lie | `␣ostensibly` | 13/152 (9%) | 3/81 (4%) | 0/138 (0%) | 0/158 (0%) | 8/47 (17%) | 3/77 (4%) |
| conscience (moral conscience) | unclear | `␣conscience` | 6/152 (4%) | 4/81 (5%) | 0/138 (0%) | 6/158 (4%) | 1/47 (2%) | 4/77 (5%) |
| apology (apologizing, being sorry) | unclear | `Sorry`, `抱歉`, `␣Sorry`, `道歉` | 6/152 (4%) | 4/81 (5%) | 0/138 (0%) | 4/158 (3%) | 5/47 (11%) | 4/77 (5%) |
| dissent (dissent) | unclear | `␣dissent` | 6/152 (4%) | 2/81 (2%) | 0/138 (0%) | 0/158 (0%) | 5/47 (11%) | 2/77 (3%) |
| truth (the truth) | truth | `其真实性` | 6/152 (4%) | 2/81 (2%) | 0/138 (0%) | 0/158 (0%) | 3/47 (6%) | 2/77 (3%) |
| integrity (integrity, honesty of character) | truth | `␣Integrity` | 4/152 (3%) | 3/81 (4%) | 20/138 (14%) | 79/158 (50%) | 0/47 (0%) | 3/77 (4%) |
| correct (correct) | truth | `␣Correct`, `␣Correction`, `Correction`, `更正` | 3/152 (2%) | 3/81 (4%) | 14/138 (10%) | 37/158 (23%) | 1/47 (2%) | 3/77 (4%) |
| lawful / legal (permitted by law) | unclear | `␣legally`, `/legal` | 4/152 (3%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 3/47 (6%) | 1/77 (1%) |
| cowardice (cowardly) | unclear | `␣coward` | 3/152 (2%) | 2/81 (2%) | 1/138 (1%) | 0/158 (0%) | 3/47 (6%) | 2/77 (3%) |
| skepticism (doubt) | unclear | `␣skepticism` | 3/152 (2%) | 2/81 (2%) | 0/138 (0%) | 0/158 (0%) | 3/47 (6%) | 2/77 (3%) |
| cover up (to cover up, disguise) | lie | `掩饰`, `隐` | 3/152 (2%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 1/47 (2%) | 0/77 (0%) |
| misinformation (false information) | lie | `␣misinformation` | 1/152 (1%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 0/47 (0%) | 0/77 (0%) |
| suppress (holding back, suppressing) | lie | `.Suppress` | 0/152 (0%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 0/47 (0%) | 1/77 (1%) |
| defiance (defiance) | unclear | `␣defiance` | 1/152 (1%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 1/47 (2%) | 0/77 (0%) |
| clarify (to clarify) | unclear | `澄清` | 1/152 (1%) | 0/81 (0%) | 8/138 (6%) | 33/158 (21%) | 1/47 (2%) | 0/77 (0%) |
| incorrect (incorrect) | lie | `incorrect`, `␣Incorrect`, `不符合` | 1/152 (1%) | 0/81 (0%) | 0/138 (0%) | 19/158 (12%) | 0/47 (0%) | 0/77 (0%) |
| wrong (wrong, mistaken) | lie | `␣Wrong`, `␣WRONG` | 0/152 (0%) | 0/81 (0%) | 0/138 (0%) | 2/158 (1%) | 0/47 (0%) | 0/77 (0%) |

Not in the draft: deny (excluded: admit / deny / acknowledge); admit (excluded: admit / deny / acknowledge); evil (held back: no undisputed member left)

## think_slot3

| family | side | members | lies | truths | no-pressure truths | unrelated | lies that deny | truths that deny |
|---|---|---|---|---|---|---|---|---|
| false (false, untrue) | lie | `␣false`, `␣False`, `(false`, `false`, `False`, `=False`, `␣FALSE`, `=false`, `:false`, `(False`, `FALSE`, `>false`, `␣fals`, `_false`, `.False`, `␣falsely`, `.false`, `toBeFalsy`, `␣untrue`, `.FALSE`, `/false`, `␣falsehood` | 150/152 (99%) | 81/81 (100%) | 138/138 (100%) | 158/158 (100%) | 47/47 (100%) | 77/77 (100%) |
| true (true, real) | truth | `␣true`, `True`, `␣True`, `␣TRUE`, `>true` | 131/152 (86%) | 77/81 (95%) | 135/138 (98%) | 97/158 (61%) | 26/47 (55%) | 73/77 (95%) |
| honest / truthful (honest, truthful) | truth | `␣truthful`, `␣Honest` | 42/152 (28%) | 7/81 (9%) | 9/138 (7%) | 1/158 (1%) | 10/47 (21%) | 7/77 (9%) |
| reject / veto (turning down, vetoing) | unclear | `␣Reject`, `␣rejecting`, `否决`, `驳回`, `拒绝`, `␣refusal`, `拒絕` | 23/152 (15%) | 12/81 (15%) | 6/138 (4%) | 0/158 (0%) | 20/47 (43%) | 12/77 (16%) |
| unethical (morally wrong) | lie | `␣unethical` | 29/152 (19%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 1/47 (2%) | 1/77 (1%) |
| refuse (refusing) | unclear | `拒绝`, `␣refusal`, `拒絕` | 18/152 (12%) | 11/81 (14%) | 6/138 (4%) | 0/158 (0%) | 16/47 (34%) | 11/77 (14%) |
| cannot / unable (unable to do) | unclear | `␣Cannot`, `cannot`, `我不能`, `我无法`, `␣Unable` | 23/152 (15%) | 2/81 (2%) | 0/138 (0%) | 1/158 (1%) | 7/47 (15%) | 2/77 (3%) |
| unequivocal (unequivocal, unmistakable) | unclear | `␣unequiv`, `␣unmistak` | 15/152 (10%) | 2/81 (2%) | 0/138 (0%) | 0/158 (0%) | 12/47 (26%) | 2/77 (3%) |
| incorrect (incorrect) | lie | `␣incorrect`, `incorrect`, `␣Incorrect`, `不符合` | 7/152 (5%) | 10/81 (12%) | 3/138 (2%) | 4/158 (3%) | 4/47 (9%) | 10/77 (13%) |
| impossible (impossible) | unclear | `␣Impossible` | 4/152 (3%) | 2/81 (2%) | 1/138 (1%) | 0/158 (0%) | 4/47 (9%) | 2/77 (3%) |
| forbidden / unauthorized (not permitted) | unclear | `␣Unauthorized`, `␣Forbidden` | 4/152 (3%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 3/47 (6%) | 1/77 (1%) |
| disclaimer (a disclaimer) | unclear | `␣Disclaimer`, `␣DISCLAIMER`, `免责声明` | 3/152 (2%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 1/47 (2%) | 1/77 (1%) |
| unauthorized (not permitted) | unclear | `␣Unauthorized` | 3/152 (2%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 3/47 (6%) | 1/77 (1%) |
| dishonest (not honest) | lie | `␣dishonest` | 3/152 (2%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 2/47 (4%) | 0/77 (0%) |
| genuine (genuine, sincere) | truth | `␣genuinely` | 3/152 (2%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 3/47 (6%) | 0/77 (0%) |
| refute (arguing that a claim is false) | unclear | `␣refute` | 1/152 (1%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 1/47 (2%) | 1/77 (1%) |
| lawful / legal (permitted by law) | unclear | `␣Legal` | 1/152 (1%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 1/47 (2%) | 1/77 (1%) |
| apology (apologizing) | unclear | `␣Sorry` | 0/152 (0%) | 2/81 (2%) | 0/138 (0%) | 0/158 (0%) | 0/47 (0%) | 2/77 (3%) |
| wrong (wrong, mistaken) | lie | `␣Wrong` | 0/152 (0%) | 2/81 (2%) | 0/138 (0%) | 0/158 (0%) | 0/47 (0%) | 2/77 (3%) |
| mislead (misleading) | lie | `␣misleading` | 1/152 (1%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 1/47 (2%) | 0/77 (0%) |
| hidden (hidden, concealed) | lie | `␣Hidden` | 1/152 (1%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 0/47 (0%) | 0/77 (0%) |
| silence (staying silent) | unclear | `␣Silence` | 1/152 (1%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 1/47 (2%) | 0/77 (0%) |
| privacy (privacy) | unclear | `␣Privacy` | 1/152 (1%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 1/47 (2%) | 0/77 (0%) |
| illegal (against the law) | unclear | `␣Illegal` | 0/152 (0%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 0/47 (0%) | 1/77 (1%) |
| compliant (complying with rules) | unclear | `␣Compliance` | 1/152 (1%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 1/47 (2%) | 0/77 (0%) |
| defiance (defiant) | unclear | `␣defiant` | 1/152 (1%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 1/47 (2%) | 0/77 (0%) |

Not in the draft: deny (excluded: admit / deny / acknowledge); admit (excluded: admit / deny / acknowledge); truth (excluded: truth from the question on)
