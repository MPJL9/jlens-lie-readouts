# Draft families: qwen3.6-27b, J-lens, part Q6_factual, group think

Written by `scripts/apply_family_decisions.py` (2026-10-01; draft, not frozen). Counts are `present / transcripts (share)`
on the build split.

## think_slot0

| family | side | members | lies | truths | no-pressure truths | unrelated | lies that deny | truths that deny |
|---|---|---|---|---|---|---|---|---|
| secret (secretive, kept hidden) | lie | `隐秘` | 151/152 (99%) | 79/81 (98%) | 131/138 (95%) | 88/158 (56%) | 42/43 (98%) | 71/73 (97%) |
| lawful (legal, permitted by law) | unclear | `合法`, `/legal`, `legal`, `_legal`, `␣legality`, `Legal`, `LEGAL` | 151/152 (99%) | 76/81 (94%) | 135/138 (98%) | 96/158 (61%) | 43/43 (100%) | 68/73 (93%) |
| clarify (to clarify, set the record straight) | unclear | `澄清` | 120/152 (79%) | 70/81 (86%) | 135/138 (98%) | 135/158 (85%) | 33/43 (77%) | 64/73 (88%) |
| insinuate (to hint at, imply) | unclear | `暗示`, `隐含` | 122/152 (80%) | 59/81 (73%) | 50/138 (36%) | 18/158 (11%) | 33/43 (77%) | 53/73 (73%) |
| compliant (complying with rules) | unclear | `合规`, `依法依规` | 111/152 (73%) | 54/81 (67%) | 113/138 (82%) | 0/158 (0%) | 34/43 (79%) | 51/73 (70%) |
| illegal (illegal, against the law) | unclear | `违法违规`, `非法`, `违法`, `illegal`, `Illegal` | 76/152 (50%) | 36/81 (44%) | 45/138 (33%) | 19/158 (12%) | 28/43 (65%) | 35/73 (48%) |
| fake (fake, counterfeit) | lie | `fake`, `Fake` | 65/152 (43%) | 32/81 (40%) | 4/138 (3%) | 1/158 (1%) | 23/43 (53%) | 31/73 (42%) |
| fabricate (made up, fabricated) | lie | `虚构` | 55/152 (36%) | 42/81 (52%) | 11/138 (8%) | 0/158 (0%) | 23/43 (53%) | 41/73 (56%) |
| lawful (lawful, legality) | unclear | `合法`, `␣legality` | 35/152 (23%) | 18/81 (22%) | 3/138 (2%) | 0/158 (0%) | 16/43 (37%) | 17/73 (23%) |
| violate (to break a rule) | unclear | `违规`, `违反`, `违反了` | 24/152 (16%) | 12/81 (15%) | 4/138 (3%) | 0/158 (0%) | 13/43 (30%) | 11/73 (15%) |
| ethics (morality, ethical) | unclear | `道德`, `ethical` | 28/152 (18%) | 6/81 (7%) | 0/138 (0%) | 0/158 (0%) | 6/43 (14%) | 5/73 (7%) |
| true (true, real) | truth | `真` | 13/152 (9%) | 20/81 (25%) | 8/138 (6%) | 1/158 (1%) | 5/43 (12%) | 20/73 (27%) |
| stealth (quietly, unnoticed) | unclear | `悄然` | 15/152 (10%) | 9/81 (11%) | 0/138 (0%) | 0/158 (0%) | 12/43 (28%) | 9/73 (12%) |
| suppress (to suppress (information)) | lie | `suppress` | 3/152 (2%) | 12/81 (15%) | 0/138 (0%) | 0/158 (0%) | 3/43 (7%) | 12/73 (16%) |
| unauthorized (not authorized) | unclear | `␣Unauthorized` | 6/152 (4%) | 1/81 (1%) | 1/138 (1%) | 7/158 (4%) | 5/43 (12%) | 0/73 (0%) |
| vague (vague, unclear (evasive vagueness)) | unclear | `模糊` | 2/152 (1%) | 4/81 (5%) | 1/138 (1%) | 0/158 (0%) | 1/43 (2%) | 4/73 (5%) |
| misunderstanding (misunderstanding) | unclear | `误解` | 3/152 (2%) | 3/81 (4%) | 5/138 (4%) | 59/158 (37%) | 1/43 (2%) | 2/73 (3%) |
| hide (to hide, hidden) | lie | `藏`, `隐` | 1/152 (1%) | 2/81 (2%) | 8/138 (6%) | 0/158 (0%) | 0/43 (0%) | 2/73 (3%) |
| wrong (wrong, mistaken) | lie | `错误` | 1/152 (1%) | 2/81 (2%) | 1/138 (1%) | 1/158 (1%) | 0/43 (0%) | 2/73 (3%) |
| spoiler (giving away hidden information) | unclear | `Spoiler` | 1/152 (1%) | 0/81 (0%) | 0/138 (0%) | 6/158 (4%) | 0/43 (0%) | 0/73 (0%) |

Not in the draft: honest speech (excluded: truth from the question on); honest (held back: no undisputed member left); truth (excluded: truth from the question on); false (excluded: the question's own word)

## think_slot1

| family | side | members | lies | truths | no-pressure truths | unrelated | lies that deny | truths that deny |
|---|---|---|---|---|---|---|---|---|
| violate (to break a rule, go against) | unclear | `违反`, `违反了`, `违规`, `違反`, `违背`, `违规行为` | 149/152 (98%) | 77/81 (95%) | 109/138 (79%) | 95/158 (60%) | 41/43 (95%) | 69/73 (95%) |
| cannot comply (unable to satisfy the request) | unclear | `无法满足` | 93/152 (61%) | 55/81 (68%) | 129/138 (93%) | 129/158 (82%) | 35/43 (81%) | 48/73 (66%) |
| wrong (wrong, mistaken) | lie | `␣ERROR`, `erreur`, `_wrong`, `_WRONG`, `错`, `錯`, `错误`, `谬`, `錯誤`, `的错误` | 96/152 (63%) | 52/81 (64%) | 27/138 (20%) | 2/158 (1%) | 32/43 (74%) | 48/73 (66%) |
| rule-abiding (strictly adhering to rules) | unclear | `恪守`, `恪`, `依规`, `合规` | 80/152 (53%) | 35/81 (43%) | 39/138 (28%) | 19/158 (12%) | 25/43 (58%) | 32/73 (44%) |
| illusion (illusory, fantasy, not real) | unclear | `幻想`, `虚幻`, `错觉`, `妄想` | 43/152 (28%) | 26/81 (32%) | 1/138 (1%) | 0/158 (0%) | 23/43 (53%) | 25/73 (34%) |
| fake (fake, pseudo, counterfeit) | lie | `pseudo`, `fake` | 36/152 (24%) | 17/81 (21%) | 10/138 (7%) | 0/158 (0%) | 7/43 (16%) | 14/73 (19%) |
| reject (to reject, veto) | unclear | `否决`, `拒绝` | 33/152 (22%) | 18/81 (22%) | 11/138 (8%) | 0/158 (0%) | 11/43 (26%) | 15/73 (21%) |
| fabricate (made up, fabricated, forged, fictional) | lie | `fiction`, `虚构`, `伪造` | 22/152 (14%) | 7/81 (9%) | 10/138 (7%) | 0/158 (0%) | 13/43 (30%) | 6/73 (8%) |
| delusion (delusion, absurd fancy) | unclear | `妄想`, `妄` | 14/152 (9%) | 6/81 (7%) | 0/138 (0%) | 0/158 (0%) | 10/43 (23%) | 5/73 (7%) |
| lawful (lawful) | unclear | `合法` | 14/152 (9%) | 3/81 (4%) | 0/138 (0%) | 0/158 (0%) | 9/43 (21%) | 2/73 (3%) |
| incorrect (incorrect) | lie | `incorrect` | 8/152 (5%) | 5/81 (6%) | 3/138 (2%) | 0/158 (0%) | 3/43 (7%) | 5/73 (7%) |
| compliant (complying with rules) | unclear | `合规` | 3/152 (2%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 2/43 (5%) | 0/73 (0%) |
| reveal (to reveal, let slip) | truth | `透露` | 1/152 (1%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 0/43 (0%) | 0/73 (0%) |
| secretly (secretly, covertly) | lie | `暗中` | 1/152 (1%) | 0/81 (0%) | 6/138 (4%) | 11/158 (7%) | 0/43 (0%) | 0/73 (0%) |
| ethics (morality) | unclear | `道德` | 1/152 (1%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 0/43 (0%) | 0/73 (0%) |
| refuse (to refuse) | unclear | `拒绝` | 1/152 (1%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 1/43 (2%) | 0/73 (0%) |
| fact (fact, factual) | truth | `实际` | 1/152 (1%) | 0/81 (0%) | 1/138 (1%) | 0/158 (0%) | 0/43 (0%) | 0/73 (0%) |

Not in the draft: honest speech (excluded: truth from the question on); false (excluded: the question's own word)

## think_slot2

| family | side | members | lies | truths | no-pressure truths | unrelated | lies that deny | truths that deny |
|---|---|---|---|---|---|---|---|---|
| privacy (privacy, private) | unclear | `privacy`, `␣Privacy`, `Privacy`, `隐私`, `␣privacidad`, `␣privacy`, `ความเป็นส่วนตัว`, `/Private`, `private`, `.Private` | 151/152 (99%) | 80/81 (99%) | 138/138 (100%) | 158/158 (100%) | 42/43 (98%) | 72/73 (99%) |
| silence (silence, staying silent) | unclear | `沉默`, `␣Silence`, `␣Silent`, `silent`, `␣silence`, `寂静`, `␣Quiet`, `␣silencio`, `␣silenzio` | 151/152 (99%) | 79/81 (98%) | 73/138 (53%) | 12/158 (8%) | 42/43 (98%) | 72/73 (99%) |
| unauthorized (not authorized) | unclear | `␣Unauthorized` | 144/152 (95%) | 72/81 (89%) | 19/138 (14%) | 0/158 (0%) | 36/43 (84%) | 64/73 (88%) |
| leak (to leak secret information) | unclear | `␣WikiLeaks`, `泄露`, `␣Leakage` | 134/152 (88%) | 69/81 (85%) | 50/138 (36%) | 3/158 (2%) | 37/43 (86%) | 62/73 (85%) |
| disclose (disclosure, to reveal) | truth | `␣Disclosure`, `透露` | 119/152 (78%) | 54/81 (67%) | 88/138 (64%) | 69/158 (44%) | 25/43 (58%) | 47/73 (64%) |
| mislead (misleading) | lie | `误导性` | 104/152 (68%) | 58/81 (72%) | 10/138 (7%) | 5/158 (3%) | 21/43 (49%) | 53/73 (73%) |
| verify (verification, verified) | unclear | `␣Verification`, `_verified`, `␣Verified`, `核实`, `_verification`, `验证`, `␣verification`, `verification`, `.verify` | 100/152 (66%) | 59/81 (73%) | 124/138 (90%) | 152/158 (96%) | 23/43 (53%) | 54/73 (74%) |
| forbidden (forbidden, prohibited, taboo) | unclear | `␣Forbidden`, `严禁`, `禁止`, `␣prohibited`, `禁忌`, `禁用` | 104/152 (68%) | 43/81 (53%) | 4/138 (3%) | 0/158 (0%) | 21/43 (49%) | 38/73 (52%) |
| compliant (compliance) | unclear | `␣Compliance`, `合规` | 106/152 (70%) | 41/81 (51%) | 9/138 (7%) | 2/158 (1%) | 26/43 (60%) | 38/73 (52%) |
| confidential (kept confidential, secrecy) | lie | `保密`, `␣конфиден`, `␣Confidential`, `␣confidentiality` | 97/152 (64%) | 47/81 (58%) | 107/138 (78%) | 13/158 (8%) | 22/43 (51%) | 44/73 (60%) |
| true (true, real) | truth | `true`, `True`, `␣TRUE`, `.assertTrue`, `:true`, `TRUE`, `>true`, `.isTrue`, `真的`, `确实`, `的确`, `眞` | 99/152 (65%) | 44/81 (54%) | 44/138 (32%) | 119/158 (75%) | 13/43 (30%) | 37/73 (51%) |
| violate (to break a rule) | unclear | `违背`, `␣violates`, `␣violate`, `违反`, `␣violazione`, `␣violating`, `␣violation`, `违规`, `违反了`, `␣violations` | 100/152 (66%) | 29/81 (36%) | 1/138 (1%) | 0/158 (0%) | 22/43 (51%) | 26/73 (36%) |
| illegal (illegal) | unclear | `␣Illegal`, `illegal`, `␣ilegal`, `␣illegal`, `非法`, `违法` | 57/152 (38%) | 9/81 (11%) | 1/138 (1%) | 0/158 (0%) | 16/43 (37%) | 7/73 (10%) |
| ethics (ethics, ethical) | unclear | `␣Ethics`, `␣ethical`, `ethical`, `伦理` | 58/152 (38%) | 7/81 (9%) | 2/138 (1%) | 0/158 (0%) | 7/43 (16%) | 5/73 (7%) |
| spoiler (giving away hidden information) | unclear | `Spoiler` | 51/152 (34%) | 12/81 (15%) | 0/138 (0%) | 0/158 (0%) | 7/43 (16%) | 8/73 (11%) |
| hide (to hide, hidden) | lie | `␣Hidden`, `_hide`, `hidden`, `隐` | 35/152 (23%) | 17/81 (21%) | 6/138 (4%) | 0/158 (0%) | 8/43 (19%) | 13/73 (18%) |
| reject (to reject) | unclear | `reject`, `␣Reject`, `rejected`, `.reject`, `拒绝`, `␣refusal` | 34/152 (22%) | 14/81 (17%) | 0/138 (0%) | 0/158 (0%) | 24/43 (56%) | 13/73 (18%) |
| refuse (to refuse) | unclear | `拒绝`, `␣refusal`, `拒不`, `拒`, `拒絕` | 33/152 (22%) | 14/81 (17%) | 0/138 (0%) | 0/158 (0%) | 24/43 (56%) | 13/73 (18%) |
| opaque (not transparent) | lie | `opaque` | 25/152 (16%) | 15/81 (19%) | 64/138 (46%) | 6/158 (4%) | 5/43 (12%) | 12/73 (16%) |
| refute (to refute, rebut) | unclear | `␣refute`, `反驳` | 23/152 (15%) | 15/81 (19%) | 3/138 (2%) | 0/158 (0%) | 12/43 (28%) | 15/73 (21%) |
| integrity (integrity) | truth | `␣Integrity`, `正直` | 15/152 (10%) | 10/81 (12%) | 19/138 (14%) | 3/158 (2%) | 7/43 (16%) | 9/73 (12%) |
| encryption (encryption) | unclear | `␣Encryption`, `encryption` | 13/152 (9%) | 5/81 (6%) | 3/138 (2%) | 0/158 (0%) | 1/43 (2%) | 5/73 (7%) |
| genuine (genuine, authentic) | truth | `␣Genuine`, `其真实性` | 12/152 (8%) | 5/81 (6%) | 0/138 (0%) | 0/158 (0%) | 3/43 (7%) | 4/73 (5%) |
| implicit (implied, not stated) | unclear | `␣Implicit`, `隐含` | 10/152 (7%) | 7/81 (9%) | 0/138 (0%) | 0/158 (0%) | 1/43 (2%) | 5/73 (7%) |
| conscience (conscience) | unclear | `␣conscience` | 6/152 (4%) | 5/81 (6%) | 0/138 (0%) | 1/158 (1%) | 1/43 (2%) | 4/73 (5%) |
| unethical (unethical) | lie | `␣unethical` | 9/152 (6%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 3/43 (7%) | 0/73 (0%) |
| correct (correct) | truth | `␣Correct`, `␣Correction`, `正确`, `纠错`, `纠正`, `更正`, `是正确的` | 6/152 (4%) | 3/81 (4%) | 16/138 (12%) | 109/158 (69%) | 0/43 (0%) | 2/73 (3%) |
| hypocrisy (hypocrisy) | lie | `␣hypocrisy` | 7/152 (5%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 3/43 (7%) | 0/73 (0%) |
| ostensibly (seemingly, as a pretence) | lie | `␣ostensibly` | 5/152 (3%) | 2/81 (2%) | 0/138 (0%) | 0/158 (0%) | 3/43 (7%) | 2/73 (3%) |
| apology (apologizing, sorry) | unclear | `抱歉`, `Sorry`, `道歉` | 3/152 (2%) | 2/81 (2%) | 0/138 (0%) | 1/158 (1%) | 1/43 (2%) | 2/73 (3%) |
| suppress (to suppress (information)) | lie | `.Suppress`, `suppress` | 1/152 (1%) | 3/81 (4%) | 0/138 (0%) | 0/158 (0%) | 0/43 (0%) | 3/73 (4%) |
| clarify (to clarify, set the record straight) | unclear | `澄清` | 1/152 (1%) | 2/81 (2%) | 12/138 (9%) | 20/158 (13%) | 1/43 (2%) | 2/73 (3%) |
| sorry (apology) | unclear | `Sorry` | 2/152 (1%) | 0/81 (0%) | 0/138 (0%) | 1/158 (1%) | 1/43 (2%) | 0/73 (0%) |
| lawful (legal, permitted by law) | unclear | `␣Legal`, `/legal` | 1/152 (1%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 0/43 (0%) | 0/73 (0%) |
| cover up (to cover up, gloss over) | lie | `掩饰` | 1/152 (1%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 1/43 (2%) | 0/73 (0%) |
| evade (to evade, avoid) | lie | `回避` | 1/152 (1%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 1/43 (2%) | 0/73 (0%) |
| wrong (wrong, mistaken) | lie | `␣Wrong`, `错觉` | 0/152 (0%) | 0/81 (0%) | 2/138 (1%) | 3/158 (2%) | 0/43 (0%) | 0/73 (0%) |
| incorrect (incorrect) | lie | `incorrect`, `␣Incorrect` | 0/152 (0%) | 0/81 (0%) | 0/138 (0%) | 46/158 (29%) | 0/43 (0%) | 0/73 (0%) |
| fact (fact, factual) | truth | `根据实际情况` | 0/152 (0%) | 0/81 (0%) | 1/138 (1%) | 0/158 (0%) | 0/43 (0%) | 0/73 (0%) |

Not in the draft: deny (excluded: admit / deny / acknowledge); admit (excluded: admit / deny / acknowledge); truth (excluded: truth from the question on); false (excluded: the question's own word)

## think_slot3

| family | side | members | lies | truths | no-pressure truths | unrelated | lies that deny | truths that deny |
|---|---|---|---|---|---|---|---|---|
| true (true, real) | truth | `␣true`, `True`, `␣True`, `␣TRUE`, `>true` | 128/152 (84%) | 74/81 (91%) | 126/138 (91%) | 96/158 (61%) | 21/43 (49%) | 66/73 (90%) |
| incorrect (incorrect) | lie | `␣incorrect`, `Incorrect`, `␣incorrectly`, `incorrect`, `␣Incorrect`, `不符合` | 25/152 (16%) | 16/81 (20%) | 15/138 (11%) | 22/158 (14%) | 3/43 (7%) | 12/73 (16%) |
| refuse (to refuse) | unclear | `拒绝`, `␣refusal`, `␣Reject`, `否决` | 13/152 (9%) | 5/81 (6%) | 1/138 (1%) | 0/158 (0%) | 13/43 (30%) | 4/73 (5%) |
| truthful (truthful, honest) | truth | `␣truthful` | 8/152 (5%) | 3/81 (4%) | 1/138 (1%) | 0/158 (0%) | 3/43 (7%) | 3/73 (4%) |
| reject (to reject, veto) | unclear | `␣Reject`, `否决` | 4/152 (3%) | 3/81 (4%) | 0/138 (0%) | 0/158 (0%) | 4/43 (9%) | 2/73 (3%) |
| violate (to break a rule) | unclear | `违反`, `违背` | 2/152 (1%) | 1/81 (1%) | 3/138 (2%) | 0/158 (0%) | 0/43 (0%) | 1/73 (1%) |
| wrong (wrong, mistaken) | lie | `␣Wrong` | 0/152 (0%) | 3/81 (4%) | 0/138 (0%) | 0/158 (0%) | 0/43 (0%) | 2/73 (3%) |
| dishonest (dishonest) | lie | `␣dishonest` | 2/152 (1%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 1/43 (2%) | 0/73 (0%) |
| refute (to refute, rebut) | unclear | `␣refute` | 1/152 (1%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 0/43 (0%) | 1/73 (1%) |
| hide (hidden) | lie | `␣Hidden` | 2/152 (1%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 0/43 (0%) | 0/73 (0%) |
| fake (fake) | lie | `␣Fake` | 1/152 (1%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 0/43 (0%) | 0/73 (0%) |
| silence (silence, staying silent) | unclear | `␣Silent`, `␣Silence` | 1/152 (1%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 0/43 (0%) | 0/73 (0%) |
| illegal (illegal) | unclear | `␣Illegal` | 0/152 (0%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 0/43 (0%) | 0/73 (0%) |
| forbidden (forbidden) | unclear | `␣Forbidden` | 0/152 (0%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 0/43 (0%) | 0/73 (0%) |
| unauthorized (not authorized) | unclear | `␣Unauthorized` | 0/152 (0%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 0/43 (0%) | 0/73 (0%) |
| lawful (legal) | unclear | `␣Legal` | 0/152 (0%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 0/43 (0%) | 0/73 (0%) |

Not in the draft: deny (excluded: admit / deny / acknowledge); truth (excluded: truth from the question on); false (excluded: the question's own word)
