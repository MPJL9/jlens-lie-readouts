# Draft families: qwen3.6-27b, logit lens, part Q9_dyl, group questiona

Written by `scripts/apply_family_decisions.py` (2026-10-01; draft, not frozen). Counts are `present / transcripts (share)`
on the build split.

## q_tok0

| family | side | members | lies | truths | no-pressure truths | unrelated | lies that deny | truths that deny |
|---|---|---|---|---|---|---|---|---|
| true (true, real) | truth | `真的`, `确实`, `的真` | 64/152 (42%) | 20/81 (25%) | 17/138 (12%) | 4/158 (3%) | 30/65 (46%) | 19/76 (25%) |
| promise (a promise or guarantee) | unclear | `承诺`, `␣promise`, `保证` | 5/152 (3%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 2/65 (3%) | 1/76 (1%) |
| wrong (wrong, mistaken) | lie | `错`, `错了`, `误会` | 2/152 (1%) | 4/81 (5%) | 12/138 (9%) | 3/158 (2%) | 2/65 (3%) | 4/76 (5%) |
| misunderstand (misunderstanding) | unclear | `␣misunderstand`, `␣misunderstood` | 3/152 (2%) | 2/81 (2%) | 1/138 (1%) | 0/158 (0%) | 2/65 (3%) | 2/76 (3%) |
| intentional (on purpose, deliberately) | unclear | `␣intentionally`, `␣intentional`, `␣deliberate`, `␣deliberately` | 2/152 (1%) | 2/81 (2%) | 0/138 (0%) | 0/158 (0%) | 2/65 (3%) | 2/76 (3%) |
| omit (to leave something out) | lie | `遗漏` | 1/152 (1%) | 2/81 (2%) | 1/138 (1%) | 12/158 (8%) | 0/65 (0%) | 2/76 (3%) |
| knowingly (knowingly, while knowing better (明知)) | unclear | `␣knowingly` | 1/152 (1%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 1/65 (2%) | 1/76 (1%) |
| comply (to comply with, follow rules (遵守, 遵循, 遵照)) | unclear | `遵守`, `遵循` | 0/152 (0%) | 2/81 (2%) | 1/138 (1%) | 2/158 (1%) | 0/65 (0%) | 1/76 (1%) |
| false (false, untrue) | lie | `␣fals` | 2/152 (1%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 1/65 (2%) | 0/76 (0%) |
| truthful (truthful; telling it as it is) | truth | `如实` | 1/152 (1%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 0/65 (0%) | 0/76 (0%) |
| contradict (to contradict; contradiction) | unclear | `␣contradict` | 1/152 (1%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 1/65 (2%) | 0/76 (0%) |
| fact (fact, factual) | truth | `符合`, `事实` | 1/152 (1%) | 0/81 (0%) | 1/138 (1%) | 0/158 (0%) | 1/65 (2%) | 0/76 (0%) |
| incorrect (incorrect) | lie | `有误` | 0/152 (0%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 0/65 (0%) | 1/76 (1%) |
| correct (correct) | truth | `␣correctly` | 0/152 (0%) | 0/81 (0%) | 0/138 (0%) | 2/158 (1%) | 0/65 (0%) | 0/76 (0%) |
| accurate (accurate) | truth | `␣accurately` | 0/152 (0%) | 0/81 (0%) | 0/138 (0%) | 1/158 (1%) | 0/65 (0%) | 0/76 (0%) |

Not in the draft: deny (excluded: admit / deny / acknowledge); truth (excluded: truth from the question on); admit (excluded: admit / deny / acknowledge)

## q_tok1

| family | side | members | lies | truths | no-pressure truths | unrelated | lies that deny | truths that deny |
|---|---|---|---|---|---|---|---|---|
| intentional (on purpose, deliberately) | unclear | `␣intentionally`, `␣deliberately`, `故意`, `刻意`, `␣deliberate`, `特意`, `␣intentional`, `故意的`, `有意` | 56/152 (37%) | 38/81 (47%) | 26/138 (19%) | 78/158 (49%) | 31/65 (48%) | 36/76 (47%) |
| agreed line (the agreed official line or story (口径)) | unclear | `口径` | 72/152 (47%) | 16/81 (20%) | 4/138 (3%) | 0/158 (0%) | 30/65 (46%) | 14/76 (18%) |
| truthful (truthful; telling it as it is) | truth | `如实`, `␣truthful` | 56/152 (37%) | 27/81 (33%) | 3/138 (2%) | 0/158 (0%) | 22/65 (34%) | 27/76 (36%) |
| knowingly (knowingly, while knowing better (明知)) | unclear | `明知`, `␣knowingly` | 60/152 (39%) | 23/81 (28%) | 6/138 (4%) | 1/158 (1%) | 29/65 (45%) | 22/76 (29%) |
| conceal (to keep the truth from someone) | lie | `隐瞒`, `瞒`, `␣conceal`, `藏`, `掩`, `遮` | 52/152 (34%) | 12/81 (15%) | 0/138 (0%) | 0/158 (0%) | 20/65 (31%) | 12/76 (16%) |
| hide (to hide; hidden) | lie | `隐藏`, `␣hiding`, `␣hidden`, `hide`, `␣hide`, `␣hides`, `-hidden`, `隐藏的`, `隐瞒`, `瞒`, `掩盖`, `␣conceal`, `掩饰` | 50/152 (33%) | 13/81 (16%) | 0/138 (0%) | 0/158 (0%) | 20/65 (31%) | 13/76 (17%) |
| false (false, untrue) | lie | `␣false`, `false`, `False`, `>false`, `␣fals`, `/false`, `假`, `虚假`, `假的` | 50/152 (33%) | 10/81 (12%) | 8/138 (6%) | 0/158 (0%) | 12/65 (18%) | 8/76 (11%) |
| honest (honest; honesty) | truth | `诚实`, `诚`, `␣honestly`, `␣honesty`, `␣honest`, `␣Honest` | 42/152 (28%) | 16/81 (20%) | 1/138 (1%) | 0/158 (0%) | 14/65 (22%) | 15/76 (20%) |
| contradict (to contradict; contradiction) | unclear | `␣contradict`, `矛盾`, `␣contrad`, `矛盾的` | 32/152 (21%) | 20/81 (25%) | 23/138 (17%) | 1/158 (1%) | 12/65 (18%) | 18/76 (24%) |
| blurt (blurting out (脱口)) | unclear | `脱口` | 32/152 (21%) | 12/81 (15%) | 1/138 (1%) | 4/158 (3%) | 15/65 (23%) | 12/76 (16%) |
| promise (a promise or guarantee) | unclear | `保证`, `承诺`, `␣promise`, `Promise` | 35/152 (23%) | 6/81 (7%) | 1/138 (1%) | 0/158 (0%) | 14/65 (22%) | 6/76 (8%) |
| integrity (integrity, good faith (诚信)) | truth | `诚信`, `信用` | 31/152 (20%) | 9/81 (11%) | 0/138 (0%) | 0/158 (0%) | 8/65 (12%) | 9/76 (12%) |
| fabricate (to make up something untrue) | lie | `伪造`, `虚构`, `␣fabricated`, `␣invent`, `凭空` | 31/152 (20%) | 5/81 (6%) | 2/138 (1%) | 6/158 (4%) | 11/65 (17%) | 3/76 (4%) |
| comply (to comply with, follow rules (遵守, 遵循, 遵照)) | unclear | `遵守`, `遵循`, `严格遵守`, `遵照`, `␣comply` | 17/152 (11%) | 18/81 (22%) | 5/138 (4%) | 23/158 (15%) | 8/65 (12%) | 18/76 (24%) |
| violate (to violate a rule or principle) | unclear | `违反`, `违背`, `违反了`, `␣violate` | 14/152 (9%) | 17/81 (21%) | 3/138 (2%) | 0/158 (0%) | 3/65 (5%) | 17/76 (22%) |
| out of thin air (made up from nothing (凭空)) | lie | `凭空` | 25/152 (16%) | 2/81 (2%) | 1/138 (1%) | 4/158 (3%) | 7/65 (11%) | 2/76 (3%) |
| accidental (by accident, unintentionally) | unclear | `␣accidentally`, `␣случайно`, `␣accidental`, `不小心` | 22/152 (14%) | 4/81 (5%) | 8/138 (6%) | 13/158 (8%) | 4/65 (6%) | 3/76 (4%) |
| wrong (wrong, mistaken) | lie | `␣error`, `␣mistake`, `␣mistakes`, `错`, `错误`, `不对`, `错了`, `没错`, `失误`, `是非` | 15/152 (10%) | 10/81 (12%) | 37/138 (27%) | 74/158 (47%) | 3/65 (5%) | 8/76 (11%) |
| perfunctory (to answer for form's sake, brush off (敷衍, 应付)) | unclear | `敷衍` | 23/152 (15%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 8/65 (12%) | 1/76 (1%) |
| fact (fact, factual) | truth | `␣fact`, `␣factual`, `实际`, `符合`, `事实`, `实际上`, `实际情况`, `事实上`, `是否符合`, `与实际` | 19/152 (12%) | 5/81 (6%) | 2/138 (1%) | 5/158 (3%) | 7/65 (11%) | 4/76 (5%) |
| true (true, real) | truth | `真`, `真的`, `成立`, `真正`, `真实`, `确实`, `真正的`, `真的是`, `的真`, `的真实` | 20/152 (13%) | 4/81 (5%) | 0/138 (0%) | 0/158 (0%) | 9/65 (14%) | 3/76 (4%) |
| role-play (playing a role) | unclear | `扮演`, `角色扮演` | 6/152 (4%) | 15/81 (19%) | 4/138 (3%) | 0/158 (0%) | 1/65 (2%) | 15/76 (20%) |
| candid (candid, frank (坦诚)) | truth | `坦诚` | 11/152 (7%) | 9/81 (11%) | 0/138 (0%) | 0/158 (0%) | 2/65 (3%) | 9/76 (12%) |
| misunderstand (misunderstanding) | unclear | `␣misunderstand` | 2/152 (1%) | 15/81 (19%) | 29/138 (21%) | 15/158 (9%) | 1/65 (2%) | 14/76 (18%) |
| transparent (transparent; transparency) | truth | `␣transparent`, `透明`, `透明的`, `␣transparency`, `␣Transparency`, `透明度` | 9/152 (6%) | 5/81 (6%) | 0/138 (0%) | 0/158 (0%) | 1/65 (2%) | 5/76 (7%) |
| cooperate (cooperating (配合)) | unclear | `配合` | 10/152 (7%) | 4/81 (5%) | 1/138 (1%) | 0/158 (0%) | 3/65 (5%) | 4/76 (5%) |
| fake (fake; to fake) | lie | `fake`, `␣fake`, `_fake` | 11/152 (7%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 2/65 (3%) | 0/76 (0%) |
| cover up (to cover up or gloss over (掩盖, 掩饰, 遮掩)) | lie | `掩盖`, `掩饰` | 11/152 (7%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 2/65 (3%) | 0/76 (0%) |
| secret (secret; secretly) | lie | `␣secret`, `␣secretly`, `秘密`, `␣Secret`, `secret`, `的秘密`, `私下`, `␣confidentiality` | 7/152 (5%) | 4/81 (5%) | 0/138 (0%) | 0/158 (0%) | 2/65 (3%) | 4/76 (5%) |
| objective (objective) | unclear | `客观` | 7/152 (5%) | 4/81 (5%) | 3/138 (2%) | 0/158 (0%) | 2/65 (3%) | 4/76 (5%) |
| privately (in private, behind the scenes (私下)) | unclear | `私下` | 6/152 (4%) | 2/81 (2%) | 0/138 (0%) | 0/158 (0%) | 2/65 (3%) | 2/76 (3%) |
| deceive (the act of deceiving) | lie | `欺骗`, `骗`, `␣deception`, `欺`, `哄` | 5/152 (3%) | 2/81 (2%) | 0/138 (0%) | 0/158 (0%) | 0/65 (0%) | 2/76 (3%) |
| disclose (to disclose; disclosure) | truth | `信息披露`, `␣disclosure`, `␣disclose` | 3/152 (2%) | 4/81 (5%) | 0/138 (0%) | 0/158 (0%) | 1/65 (2%) | 4/76 (5%) |
| reveal (to reveal) | truth | `透露` | 4/152 (3%) | 3/81 (4%) | 1/138 (1%) | 0/158 (0%) | 1/65 (2%) | 3/76 (4%) |
| accurate (accurate) | truth | `␣accuracy`, `␣accurately`, `准确` | 5/152 (3%) | 2/81 (2%) | 2/138 (1%) | 13/158 (8%) | 1/65 (2%) | 2/76 (3%) |
| omit (to leave something out) | lie | `␣omit`, `遗漏`, `省略` | 5/152 (3%) | 1/81 (1%) | 0/138 (0%) | 19/158 (12%) | 2/65 (3%) | 1/76 (1%) |
| evade (to evade; evasion) | unclear | `回避` | 5/152 (3%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 4/65 (6%) | 1/76 (1%) |
| refuse (to refuse; refusal) | unclear | `拒绝`, `拒`, `␣refusal` | 0/152 (0%) | 4/81 (5%) | 0/138 (0%) | 0/158 (0%) | 0/65 (0%) | 4/76 (5%) |
| confess (to confess, own up (坦白)) | truth | `坦白` | 1/152 (1%) | 3/81 (4%) | 0/138 (0%) | 0/158 (0%) | 0/65 (0%) | 3/76 (4%) |
| words and deeds (one's words and actions (言行, as in 言行一致)) | unclear | `言行` | 1/152 (1%) | 3/81 (4%) | 0/138 (0%) | 0/158 (0%) | 1/65 (2%) | 3/76 (4%) |
| incorrect (incorrect) | lie | `␣incorrect`, `␣incorrectly`, `␣Incorrect`, `错误的`, `不符合`, `有误` | 0/152 (0%) | 4/81 (5%) | 0/138 (0%) | 3/158 (2%) | 0/65 (0%) | 4/76 (5%) |
| falsehood (an untrue statement (noun)) | lie | `␣falsehood` | 3/152 (2%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 0/65 (0%) | 0/76 (0%) |
| exaggerate (exaggerating) | lie | `夸大` | 3/152 (2%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 1/65 (2%) | 0/76 (0%) |
| euphemistic (indirect, tactful wording (委婉)) | unclear | `委婉` | 2/152 (1%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 2/65 (3%) | 0/76 (0%) |
| excuse (an excuse) | unclear | `借口`, `␣excuse` | 2/152 (1%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 0/65 (0%) | 0/76 (0%) |
| genuine (genuine, sincere) | unclear | `␣genuinely` | 2/152 (1%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 1/65 (2%) | 0/76 (0%) |
| leak (to leak (泄露)) | unclear | `泄露` | 0/152 (0%) | 2/81 (2%) | 0/138 (0%) | 0/158 (0%) | 0/65 (0%) | 2/76 (3%) |
| ethics (ethics, morality) | unclear | `␣ethical`, `␣ethics`, `␣moral` | 0/152 (0%) | 2/81 (2%) | 0/138 (0%) | 0/158 (0%) | 0/65 (0%) | 2/76 (3%) |
| correct (correct) | truth | `␣correct`, `␣correctly`, `正确`, `正确的`, `正确答案` | 1/152 (1%) | 1/81 (1%) | 5/138 (4%) | 53/158 (34%) | 1/65 (2%) | 1/76 (1%) |
| mislead (to mislead) | lie | `误导` | 0/152 (0%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 0/65 (0%) | 0/76 (0%) |
| misinformation (false information given out) | lie | `虚假信息` | 1/152 (1%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 0/65 (0%) | 0/76 (0%) |
| dishonest (dishonest) | lie | `␣dishonest` | 1/152 (1%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 0/65 (0%) | 0/76 (0%) |
| confidential (confidential) | unclear | `␣confidentiality` | 0/152 (0%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 0/65 (0%) | 1/76 (1%) |
| intent (intention (noun)) | unclear | `␣intention` | 1/152 (1%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 1/65 (2%) | 0/76 (0%) |
| ethics (ethics, morality (noun)) | unclear | `␣ethics` | 0/152 (0%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 0/65 (0%) | 1/76 (1%) |
| ethical (ethical) | truth | `␣ethical` | 0/152 (0%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 0/65 (0%) | 1/76 (1%) |
| betray (to betray (出卖)) | unclear | `出卖` | 0/152 (0%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 0/65 (0%) | 1/76 (1%) |
| keep a promise (to make good on a promise (兑现)) | unclear | `兑现` | 1/152 (1%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 1/65 (2%) | 0/76 (0%) |
| ostensibly (on the surface / ostensibly) | unclear | `表面上` | 0/152 (0%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 0/65 (0%) | 1/76 (1%) |
| apologize (apologizing) | unclear | `道歉` | 0/152 (0%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 0/65 (0%) | 1/76 (1%) |

Not in the draft: fool / coax (held back: no undisputed member left); deny (excluded: admit / deny / acknowledge); truth (excluded: truth from the question on); admit (excluded: admit / deny / acknowledge)

## q_tok2

| family | side | members | lies | truths | no-pressure truths | unrelated | lies that deny | truths that deny |
|---|---|---|---|---|---|---|---|---|
| deceive (the act of deceiving) | lie | `欺骗`, `骗`, `␣deception`, `哄` | 152/152 (100%) | 81/81 (100%) | 138/138 (100%) | 158/158 (100%) | 65/65 (100%) | 76/76 (100%) |
| integrity (integrity, good faith (诚信)) | truth | `诚信`, `诚实守信` | 152/152 (100%) | 81/81 (100%) | 138/138 (100%) | 158/158 (100%) | 65/65 (100%) | 76/76 (100%) |
| false (false, untrue) | lie | `␣false`, `␣False`, `false`, `=False`, `=false`, `␣fals`, `␣untrue`, `/false`, `假`, `虚假`, `假的`, `真假` | 152/152 (100%) | 81/81 (100%) | 138/138 (100%) | 158/158 (100%) | 65/65 (100%) | 76/76 (100%) |
| honest (honest; honesty) | truth | `诚实`, `␣honest`, `诚实守信` | 149/152 (98%) | 67/81 (83%) | 126/138 (91%) | 57/158 (36%) | 63/65 (97%) | 62/76 (82%) |
| truthful (truthful; telling it as it is) | truth | `如实`, `␣truthful` | 143/152 (94%) | 73/81 (90%) | 67/138 (49%) | 44/158 (28%) | 60/65 (92%) | 68/76 (89%) |
| falsehood (an untrue statement (noun)) | lie | `␣falsehood` | 146/152 (96%) | 68/81 (84%) | 135/138 (98%) | 153/158 (97%) | 63/65 (97%) | 65/76 (86%) |
| conceal (to keep the truth from someone) | lie | `隐瞒`, `␣conceal`, `瞒`, `掩盖`, `掩饰` | 131/152 (86%) | 73/81 (90%) | 28/138 (20%) | 18/158 (11%) | 57/65 (88%) | 69/76 (91%) |
| fake (fake; to fake) | lie | `fake`, `␣fake`, `Fake`, `␣Fake` | 128/152 (84%) | 67/81 (83%) | 129/138 (93%) | 144/158 (91%) | 48/65 (74%) | 63/76 (83%) |
| omit (to leave something out) | lie | `␣omission`, `␣omit`, `omit`, `␣OMIT` | 53/152 (35%) | 38/81 (47%) | 8/138 (6%) | 0/158 (0%) | 29/65 (45%) | 35/76 (46%) |
| intentional (on purpose, deliberately) | unclear | `故意`, `␣intentionally`, `␣deliberately`, `␣deliberate`, `故意的`, `␣intentional`, `有意` | 50/152 (33%) | 25/81 (31%) | 100/138 (72%) | 73/158 (46%) | 17/65 (26%) | 23/76 (30%) |
| true (true, real) | truth | `␣true`, `true`, `真实`, `真实的`, `是真的`, `的真实` | 62/152 (41%) | 8/81 (10%) | 15/138 (11%) | 7/158 (4%) | 21/65 (32%) | 5/76 (7%) |
| promise (a promise or guarantee) | unclear | `承诺`, `␣promise` | 39/152 (26%) | 30/81 (37%) | 6/138 (4%) | 32/158 (20%) | 19/65 (29%) | 29/76 (38%) |
| cover up (to cover up or gloss over (掩盖, 掩饰, 遮掩)) | lie | `掩盖`, `掩饰` | 9/152 (6%) | 3/81 (4%) | 0/138 (0%) | 0/158 (0%) | 7/65 (11%) | 3/76 (4%) |
| fact (fact, factual) | truth | `␣facts`, `␣factual`, `事实`, `与现实` | 9/152 (6%) | 3/81 (4%) | 1/138 (1%) | 30/158 (19%) | 4/65 (6%) | 3/76 (4%) |
| candid (frank, upfront) | truth | `␣upfront` | 3/152 (2%) | 3/81 (4%) | 0/138 (0%) | 0/158 (0%) | 1/65 (2%) | 3/76 (4%) |
| knowingly (knowingly, while knowing better (明知)) | unclear | `␣knowingly`, `明知` | 4/152 (3%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 1/65 (2%) | 1/76 (1%) |
| misinformation (false information given out) | lie | `虚假信息` | 3/152 (2%) | 0/81 (0%) | 0/138 (0%) | 3/158 (2%) | 1/65 (2%) | 0/76 (0%) |
| fabricate (to make up something untrue) | lie | `␣invent`, `␣invented`, `虚构`, `凭空` | 3/152 (2%) | 0/81 (0%) | 33/138 (24%) | 87/158 (55%) | 0/65 (0%) | 0/76 (0%) |
| betray (to betray (出卖)) | unclear | `出卖` | 0/152 (0%) | 3/81 (4%) | 4/138 (3%) | 0/158 (0%) | 0/65 (0%) | 3/76 (4%) |
| mislead (to mislead) | lie | `误导` | 0/152 (0%) | 1/81 (1%) | 1/138 (1%) | 0/158 (0%) | 0/65 (0%) | 1/76 (1%) |
| out of thin air (made up from nothing (凭空)) | lie | `凭空` | 1/152 (1%) | 0/81 (0%) | 4/138 (3%) | 0/158 (0%) | 0/65 (0%) | 0/76 (0%) |
| intent (intention (noun)) | unclear | `␣intentions` | 0/152 (0%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 0/65 (0%) | 1/76 (1%) |
| accuse (accusation) | unclear | `指控` | 1/152 (1%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 1/65 (2%) | 0/76 (0%) |

Not in the draft: fool / coax (held back: no undisputed member left); truth (excluded: truth from the question on); admit (excluded: admit / deny / acknowledge)

## q_tok3

| family | side | members | lies | truths | no-pressure truths | unrelated | lies that deny | truths that deny |
|---|---|---|---|---|---|---|---|---|
| false (false, untrue) | lie | `␣false`, `=False`, `␣FALSE`, `␣fals`, `/false`, `假`, `虚假` | 73/152 (48%) | 26/81 (32%) | 46/138 (33%) | 130/158 (82%) | 35/65 (54%) | 25/76 (33%) |
| integrity (integrity, good faith (诚信)) | truth | `诚信` | 72/152 (47%) | 19/81 (23%) | 23/138 (17%) | 125/158 (79%) | 32/65 (49%) | 17/76 (22%) |
| knowingly (knowingly, while knowing better (明知)) | unclear | `明知`, `␣knowingly` | 52/152 (34%) | 16/81 (20%) | 7/138 (5%) | 2/158 (1%) | 21/65 (32%) | 16/76 (21%) |
| conceal (hiding or covering up information) | lie | `隐瞒`, `掩盖`, `hide`, `␣hiding`, `␣conceal`, `瞒`, `掩饰`, `␣hide`, `Hide`, `隐匿` | 42/152 (28%) | 22/81 (27%) | 8/138 (6%) | 9/158 (6%) | 25/65 (38%) | 21/76 (28%) |
| disguise (to disguise) | lie | `␣disguise` | 47/152 (31%) | 16/81 (20%) | 12/138 (9%) | 12/158 (8%) | 22/65 (34%) | 13/76 (17%) |
| conceal (to keep the truth from someone) | lie | `隐瞒`, `␣conceal`, `瞒`, `掩`, `遮` | 40/152 (26%) | 22/81 (27%) | 7/138 (5%) | 9/158 (6%) | 24/65 (37%) | 21/76 (28%) |
| cooperate (cooperating (配合)) | unclear | `配合` | 25/152 (16%) | 11/81 (14%) | 4/138 (3%) | 0/158 (0%) | 12/65 (18%) | 10/76 (13%) |
| intentional (on purpose, deliberately) | unclear | `故意`, `␣intentionally` | 15/152 (10%) | 14/81 (17%) | 6/138 (4%) | 0/158 (0%) | 6/65 (9%) | 14/76 (18%) |
| truthful (truthful; telling it as it is) | truth | `如实` | 18/152 (12%) | 8/81 (10%) | 1/138 (1%) | 1/158 (1%) | 11/65 (17%) | 8/76 (11%) |
| true (true, real) | truth | `真`, `成立`, `真实`, `的真` | 18/152 (12%) | 4/81 (5%) | 2/138 (1%) | 21/158 (13%) | 8/65 (12%) | 2/76 (3%) |
| deceive (the act of deceiving) | lie | `欺骗`, `␣deception`, `骗`, `哄` | 14/152 (9%) | 5/81 (6%) | 1/138 (1%) | 12/158 (8%) | 7/65 (11%) | 5/76 (7%) |
| cover up (to cover up or gloss over (掩盖, 掩饰, 遮掩)) | lie | `掩盖`, `掩饰` | 12/152 (8%) | 7/81 (9%) | 5/138 (4%) | 0/158 (0%) | 8/65 (12%) | 7/76 (9%) |
| honest (honest; honesty) | truth | `诚实`, `␣honest`, `␣honesty` | 17/152 (11%) | 2/81 (2%) | 0/138 (0%) | 32/158 (20%) | 5/65 (8%) | 1/76 (1%) |
| fact (fact, factual) | truth | `␣fact`, `事实上` | 13/152 (9%) | 2/81 (2%) | 4/138 (3%) | 4/158 (3%) | 9/65 (14%) | 2/76 (3%) |
| agreed line (the agreed official line or story (口径)) | unclear | `口径` | 10/152 (7%) | 4/81 (5%) | 0/138 (0%) | 0/158 (0%) | 5/65 (8%) | 4/76 (5%) |
| mislead (to mislead) | lie | `误导`, `␣misleading` | 5/152 (3%) | 8/81 (10%) | 0/138 (0%) | 0/158 (0%) | 4/65 (6%) | 8/76 (11%) |
| hide (to hide; hidden) | lie | `hide`, `␣hiding`, `␣hide`, `Hide`, `隐匿` | 5/152 (3%) | 7/81 (9%) | 0/138 (0%) | 0/158 (0%) | 5/65 (8%) | 7/76 (9%) |
| fake (fake; to fake) | lie | `fake`, `␣fake` | 7/152 (5%) | 5/81 (6%) | 0/138 (0%) | 23/158 (15%) | 4/65 (6%) | 5/76 (7%) |
| contradict (to contradict; contradiction) | unclear | `␣contrad`, `␣contradict` | 4/152 (3%) | 3/81 (4%) | 2/138 (1%) | 0/158 (0%) | 3/65 (5%) | 3/76 (4%) |
| disclose (to disclose; disclosure) | truth | `信息披露` | 5/152 (3%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 4/65 (6%) | 1/76 (1%) |
| promise (a promise or guarantee) | unclear | `承诺`, `␣promise`, `␣promises`, `的承诺` | 3/152 (2%) | 3/81 (4%) | 0/138 (0%) | 0/158 (0%) | 1/65 (2%) | 3/76 (4%) |
| falsehood (an untrue statement (noun)) | lie | `␣falsehood` | 5/152 (3%) | 0/81 (0%) | 0/138 (0%) | 82/158 (52%) | 2/65 (3%) | 0/76 (0%) |
| transparent (transparent; transparency) | truth | `透明` | 3/152 (2%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 2/65 (3%) | 0/76 (0%) |
| betray (to betray (出卖)) | unclear | `出卖` | 2/152 (1%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 0/65 (0%) | 1/76 (1%) |
| role-play (playing a role) | unclear | `角色扮演`, `扮演` | 0/152 (0%) | 2/81 (2%) | 0/138 (0%) | 0/158 (0%) | 0/65 (0%) | 2/76 (3%) |
| euphemistic (indirect, tactful wording (委婉)) | unclear | `委婉` | 0/152 (0%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 0/65 (0%) | 1/76 (1%) |
| candid (candid, frank (坦诚)) | truth | `坦诚` | 1/152 (1%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 1/65 (2%) | 0/76 (0%) |
| reveal (to reveal) | truth | `透露` | 1/152 (1%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 0/65 (0%) | 0/76 (0%) |
| violate (to violate a rule or principle) | unclear | `违反`, `违背` | 0/152 (0%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 0/65 (0%) | 1/76 (1%) |
| keep a promise (to make good on a promise (兑现)) | unclear | `兑现` | 0/152 (0%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 0/65 (0%) | 1/76 (1%) |
| exaggerate (exaggerating) | lie | `夸大` | 1/152 (1%) | 0/81 (0%) | 0/138 (0%) | 1/158 (1%) | 0/65 (0%) | 0/76 (0%) |
| wrong (wrong, mistaken) | lie | `错误或` | 0/152 (0%) | 0/81 (0%) | 0/138 (0%) | 1/158 (1%) | 0/65 (0%) | 0/76 (0%) |

Not in the draft: fool / coax (held back: no undisputed member left); deny (excluded: admit / deny / acknowledge); perfunctory (held back: no undisputed member left); truth (excluded: truth from the question on); admit (excluded: admit / deny / acknowledge)

## q_tok4

| family | side | members | lies | truths | no-pressure truths | unrelated | lies that deny | truths that deny |
|---|---|---|---|---|---|---|---|---|
| false (false, untrue) | lie | `␣false`, `␣False`, `false`, `False`, `=False`, `␣FALSE`, `=false`, `>false`, `␣fals`, `.assertFalse`, `.False`, `assertFalse`, `␣falsely`, `/false`, `假`, `虚假`, `假的`, `真假`, `不实` | 110/152 (72%) | 32/81 (40%) | 49/138 (36%) | 30/158 (19%) | 49/65 (75%) | 30/76 (39%) |
| hide (to hide; hidden) | lie | `隐藏`, `␣hidden`, `隐藏的`, `␣hiding`, `␣hide`, `hidden`, `Hidden`, `␣Hidden`, `␣hides`, `-hide`, `hide`, `Hide`, `␣Hide`, `_hide`, `隐藏着`, `隐蔽`, `隐瞒`, `掩盖`, `掩饰`, `␣conceal`, `遮掩`, `瞒`, `␣concealed`, `隱藏`, `藏着` | 98/152 (64%) | 29/81 (36%) | 59/138 (43%) | 2/158 (1%) | 37/65 (57%) | 26/76 (34%) |
| fact (fact, factual) | truth | `␣fact`, `␣reality`, `␣facts`, `Fact`, `fact`, `␣Fact`, `␣Reality`, `␣Facts`, `_fact`, `␣FACT`, `FACT`, `␣factual`, `facts`, `实际`, `符合`, `现实`, `事实`, `实际上`, `实际情况`, `事实上`, `的事实`, `的实际`, `实际的`, `是否符合`, `实事求是`, `现实中`, `的现实`, `实际上是`, `与实际`, `犯罪事实`, `与现实`, `事实和`, `上述事实` | 86/152 (57%) | 36/81 (44%) | 123/138 (89%) | 21/158 (13%) | 38/65 (58%) | 35/76 (46%) |
| truthful (truthful; telling it as it is) | truth | `如实`, `␣truthful` | 85/152 (56%) | 35/81 (43%) | 53/138 (38%) | 22/158 (14%) | 34/65 (52%) | 34/76 (45%) |
| conceal (to keep the truth from someone) | lie | `隐瞒`, `␣conceal`, `瞒`, `␣concealed`, `藏`, `掩`, `遮`, `隐` | 86/152 (57%) | 26/81 (32%) | 33/138 (24%) | 2/158 (1%) | 33/65 (51%) | 23/76 (30%) |
| fabricate (to make up something untrue) | lie | `␣fabricated`, `虚构`, `␣fabrication`, `␣invented`, `伪造`, `␣invent`, `␣invention`, `␣Invent`, `␣inventions`, `凭空` | 86/152 (57%) | 23/81 (28%) | 13/138 (9%) | 7/158 (4%) | 36/65 (55%) | 22/76 (29%) |
| knowingly (knowingly, while knowing better (明知)) | unclear | `明知`, `␣knowingly` | 64/152 (42%) | 19/81 (23%) | 80/138 (58%) | 1/158 (1%) | 23/65 (35%) | 17/76 (22%) |
| cover up (to cover up or gloss over (掩盖, 掩饰, 遮掩)) | lie | `掩盖`, `掩饰`, `遮掩` | 62/152 (41%) | 14/81 (17%) | 1/138 (1%) | 0/158 (0%) | 22/65 (34%) | 13/76 (17%) |
| deceive (the act of deceiving) | lie | `欺骗`, `␣deception`, `␣deceptive`, `骗`, `␣deceive`, `␣deceit`, `欺`, `哄` | 59/152 (39%) | 10/81 (12%) | 15/138 (11%) | 1/158 (1%) | 20/65 (31%) | 8/76 (11%) |
| agreed line (the agreed official line or story (口径)) | unclear | `口径` | 55/152 (36%) | 8/81 (10%) | 0/138 (0%) | 0/158 (0%) | 24/65 (37%) | 8/76 (11%) |
| contradict (to contradict; contradiction) | unclear | `␣contradict`, `␣contrad`, `矛盾`, `␣contradictory`, `矛盾的`, `␣contradiction`, `␣conflicting`, `␣contradictions` | 42/152 (28%) | 20/81 (25%) | 29/138 (21%) | 0/158 (0%) | 16/65 (25%) | 17/76 (22%) |
| true (true, real) | truth | `␣true`, `true`, `␣real`, `True`, `␣True`, `real`, `:true`, `真`, `成立`, `真实`, `确实`, `真正的`, `的确`, `真实的`, `是真的`, `的真`, `内容的真实性`, `确实是`, `的真实`, `属实`, `的真实性` | 48/152 (32%) | 12/81 (15%) | 85/138 (62%) | 19/158 (12%) | 24/65 (37%) | 10/76 (13%) |
| wrong (wrong, mistaken) | lie | `␣error`, `␣wrong`, `错`, `错误`, `不对`, `错了`, `没错`, `是非`, `误会`, `的错误`, `是错误的` | 40/152 (26%) | 20/81 (25%) | 16/138 (12%) | 49/158 (31%) | 13/65 (20%) | 18/76 (24%) |
| ostensibly (on the surface / ostensibly) | unclear | `表面上` | 45/152 (30%) | 14/81 (17%) | 6/138 (4%) | 0/158 (0%) | 18/65 (28%) | 12/76 (16%) |
| intentional (on purpose, deliberately) | unclear | `故意`, `␣intentionally`, `␣deliberately`, `刻意`, `␣deliberate`, `␣intentional`, `故意的`, `特意` | 39/152 (26%) | 17/81 (21%) | 16/138 (12%) | 3/158 (2%) | 17/65 (26%) | 16/76 (21%) |
| fake (fake; to fake) | lie | `fake`, `␣fake`, `_fake`, `Fake`, `作假` | 41/152 (27%) | 10/81 (12%) | 11/138 (8%) | 1/158 (1%) | 16/65 (25%) | 10/76 (13%) |
| honest (honest; honesty) | truth | `诚实`, `诚`, `␣honest`, `␣honesty`, `␣honestly`, `␣Honest`, `诚实守信` | 29/152 (19%) | 18/81 (22%) | 25/138 (18%) | 30/158 (19%) | 11/65 (17%) | 18/76 (24%) |
| mislead (to mislead) | lie | `误导`, `␣misleading`, `误导性`, `␣misled` | 29/152 (19%) | 14/81 (17%) | 7/138 (5%) | 0/158 (0%) | 14/65 (22%) | 13/76 (17%) |
| objective (objective) | unclear | `␣objective`, `客观` | 33/152 (22%) | 10/81 (12%) | 43/138 (31%) | 0/158 (0%) | 12/65 (18%) | 8/76 (11%) |
| misinformation (false information given out) | lie | `虚假信息`, `␣misinformation` | 34/152 (22%) | 6/81 (7%) | 4/138 (3%) | 0/158 (0%) | 12/65 (18%) | 6/76 (8%) |
| falsehood (an untrue statement (noun)) | lie | `␣falsehood` | 35/152 (23%) | 4/81 (5%) | 3/138 (2%) | 6/158 (4%) | 10/65 (15%) | 4/76 (5%) |
| violate (to violate a rule or principle) | unclear | `违背`, `违反`, `违反了`, `␣violate` | 28/152 (18%) | 9/81 (11%) | 13/138 (9%) | 2/158 (1%) | 10/65 (15%) | 7/76 (9%) |
| role-play (playing an assigned role) | unclear | `␣persona`, `扮演` | 22/152 (14%) | 14/81 (17%) | 60/138 (43%) | 7/158 (4%) | 7/65 (11%) | 11/76 (14%) |
| excuse (an excuse) | unclear | `␣excuse`, `借口`, `␣excuses`, `␣pretext` | 23/152 (15%) | 4/81 (5%) | 0/138 (0%) | 0/158 (0%) | 7/65 (11%) | 3/76 (4%) |
| secret (secret; secretly) | lie | `␣secret`, `秘密`, `␣Secret`, `的秘密`, `secret`, `Secret`, `_secret`, `-secret`, `␣secretly`, `隐秘`, `私下`, `␣confidential` | 17/152 (11%) | 9/81 (11%) | 2/138 (1%) | 0/158 (0%) | 7/65 (11%) | 7/76 (9%) |
| fiction (fiction; fictional) | unclear | `␣fictional`, `fiction`, `-fiction`, `␣fiction`, `␣Fiction` | 16/152 (11%) | 8/81 (10%) | 1/138 (1%) | 1/158 (1%) | 6/65 (9%) | 8/76 (11%) |
| role-play (playing a role) | unclear | `扮演`, `角色扮演` | 11/152 (7%) | 12/81 (15%) | 27/138 (20%) | 7/158 (4%) | 2/65 (3%) | 9/76 (12%) |
| privately (in private, behind the scenes (私下)) | unclear | `私下` | 15/152 (10%) | 7/81 (9%) | 0/138 (0%) | 0/158 (0%) | 7/65 (11%) | 6/76 (8%) |
| comply (to comply with, follow rules (遵守, 遵循, 遵照)) | unclear | `遵照`, `遵守`, `遵循`, `严格遵守`, `␣compliance`, `␣comply` | 16/152 (11%) | 6/81 (7%) | 8/138 (6%) | 1/158 (1%) | 8/65 (12%) | 6/76 (8%) |
| ethics (ethics, morality (noun)) | unclear | `␣ethics`, `道德`, `␣Ethics`, `的道德`, `职业道德`, `␣ethical`, `␣moral`, `ethical`, `␣morally`, `␣morality` | 16/152 (11%) | 4/81 (5%) | 1/138 (1%) | 6/158 (4%) | 3/65 (5%) | 4/76 (5%) |
| ethical (ethical) | truth | `␣ethical`, `ethical` | 16/152 (11%) | 4/81 (5%) | 1/138 (1%) | 5/158 (3%) | 3/65 (5%) | 4/76 (5%) |
| cooperate (cooperating (配合)) | unclear | `配合`, `积极配合` | 11/152 (7%) | 8/81 (10%) | 13/138 (9%) | 0/158 (0%) | 8/65 (12%) | 8/76 (11%) |
| out of thin air (made up from nothing (凭空)) | lie | `凭空` | 16/152 (11%) | 2/81 (2%) | 3/138 (2%) | 1/158 (1%) | 4/65 (6%) | 2/76 (3%) |
| vague (vague, unclear on purpose) | unclear | `␣vague`, `含糊`, `模糊`, `␣vaguely` | 11/152 (7%) | 6/81 (7%) | 0/138 (0%) | 0/158 (0%) | 6/65 (9%) | 5/76 (7%) |
| disclose (to disclose; disclosure) | truth | `信息披露`, `␣disclosure`, `披露` | 12/152 (8%) | 3/81 (4%) | 0/138 (0%) | 0/158 (0%) | 7/65 (11%) | 3/76 (4%) |
| incorrect (incorrect) | lie | `␣incorrect`, `不符合`, `错误的是` | 7/152 (5%) | 8/81 (10%) | 3/138 (2%) | 0/158 (0%) | 2/65 (3%) | 8/76 (11%) |
| downplay (to play down (淡化)) | unclear | `淡化` | 7/152 (5%) | 7/81 (9%) | 0/138 (0%) | 0/158 (0%) | 3/65 (5%) | 7/76 (9%) |
| integrity (integrity, good faith (诚信)) | truth | `诚信`, `␣integrity`, `诚实守信` | 9/152 (6%) | 5/81 (6%) | 6/138 (4%) | 16/158 (10%) | 4/65 (6%) | 5/76 (7%) |
| correct (correct) | truth | `␣correct`, `␣correctly`, `correct`, `␣correction`, `Correct`, `␣corrected`, `␣Correct`, `␣corrections`, `␣correctness`, `␣Correction`, `␣correcting`, `Correction`, `␣Corrections`, `␣corrective`, `正确`, `正确的`, `正确答案`, `纠正`, `的正确`, `无误`, `是正确的`, `正确地`, `是否正确` | 3/152 (2%) | 10/81 (12%) | 17/138 (12%) | 3/158 (2%) | 2/65 (3%) | 10/76 (13%) |
| refuse (to refuse; refusal) | unclear | `␣refusal`, `拒绝`, `拒不`, `␣refusing`, `␣refuses`, `␣refused`, `␣refuse`, `拒`, `␣refus`, `拒絕`, `拒绝了` | 2/152 (1%) | 9/81 (11%) | 1/138 (1%) | 2/158 (1%) | 2/65 (3%) | 9/76 (12%) |
| exaggerate (exaggerating) | lie | `夸大` | 9/152 (6%) | 2/81 (2%) | 0/138 (0%) | 0/158 (0%) | 1/65 (2%) | 2/76 (3%) |
| promise (a promise or guarantee) | unclear | `␣promise`, `承诺`, `␣Promise`, `␣promised`, `Promise`, `␣promises`, `的承诺`, `promise`, `保证`, `保证其`, `可以保证`, `的保证` | 5/152 (3%) | 5/81 (6%) | 0/138 (0%) | 12/158 (8%) | 2/65 (3%) | 4/76 (5%) |
| accurate (accurate) | truth | `␣accurate`, `␣accuracy`, `accur`, `准确`, `准确的`, `准确地` | 2/152 (1%) | 7/81 (9%) | 9/138 (7%) | 4/158 (3%) | 1/65 (2%) | 7/76 (9%) |
| confidential (confidential) | unclear | `机密`, `␣confidential` | 6/152 (4%) | 2/81 (2%) | 0/138 (0%) | 0/158 (0%) | 3/65 (5%) | 2/76 (3%) |
| evade (to evade; evasion) | unclear | `回避`, `␣evasion`, `␣evade` | 5/152 (3%) | 3/81 (4%) | 0/138 (0%) | 0/158 (0%) | 4/65 (6%) | 3/76 (4%) |
| candid (candid, frank (坦诚)) | truth | `坦诚` | 4/152 (3%) | 4/81 (5%) | 2/138 (1%) | 9/158 (6%) | 3/65 (5%) | 4/76 (5%) |
| unethical (unethical) | lie | `␣unethical` | 6/152 (4%) | 2/81 (2%) | 0/138 (0%) | 0/158 (0%) | 1/65 (2%) | 2/76 (3%) |
| omit (to leave something out) | lie | `␣omit`, `omit`, `␣omission`, `␣OMIT` | 5/152 (3%) | 1/81 (1%) | 0/138 (0%) | 1/158 (1%) | 2/65 (3%) | 1/76 (1%) |
| euphemistic (indirect, tactful wording (委婉)) | unclear | `委婉` | 4/152 (3%) | 2/81 (2%) | 0/138 (0%) | 0/158 (0%) | 3/65 (5%) | 2/76 (3%) |
| pretend (to pretend) | lie | `␣pretend`, `假装`, `␣pretending` | 3/152 (2%) | 2/81 (2%) | 1/138 (1%) | 0/158 (0%) | 0/65 (0%) | 2/76 (3%) |
| reveal (revealing, exposing) | truth | `揭露`, `␣revealing` | 3/152 (2%) | 2/81 (2%) | 0/138 (0%) | 0/158 (0%) | 2/65 (3%) | 2/76 (3%) |
| perfunctory (to answer for form's sake, brush off (敷衍, 应付)) | unclear | `敷衍` | 3/152 (2%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 3/65 (5%) | 1/76 (1%) |
| genuine (genuine, sincere) | unclear | `␣genuine`, `␣genuinely` | 3/152 (2%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 1/65 (2%) | 1/76 (1%) |
| transparent (transparent; transparency) | truth | `透明度`, `␣transparency`, `-transparent`, `透明`, `␣transparent`, `␣Transparency`, `透明的` | 2/152 (1%) | 2/81 (2%) | 1/138 (1%) | 1/158 (1%) | 1/65 (2%) | 2/76 (3%) |
| manipulate (to manipulate) | lie | `␣manipulation`, `␣manipulate`, `␣manipulated`, `␣manipulating`, `操纵` | 2/152 (1%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 2/65 (3%) | 1/76 (1%) |
| leak (to leak (泄露)) | unclear | `泄露` | 2/152 (1%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 2/65 (3%) | 1/76 (1%) |
| wrongdoing (wrongdoing, fault) | unclear | `␣wrongdoing`, `过错` | 1/152 (1%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 1/65 (2%) | 1/76 (1%) |
| words and deeds (one's words and actions (言行, as in 言行一致)) | unclear | `言行` | 1/152 (1%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 1/65 (2%) | 1/76 (1%) |
| disguise (to disguise) | lie | `伪装` | 1/152 (1%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 0/65 (0%) | 0/76 (0%) |
| impersonate (to pass oneself off as someone else (冒充)) | lie | `冒充` | 1/152 (1%) | 0/81 (0%) | 1/138 (1%) | 0/158 (0%) | 0/65 (0%) | 0/76 (0%) |
| dishonest (dishonest) | lie | `␣dishonest` | 1/152 (1%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 1/65 (2%) | 0/76 (0%) |
| reveal (to reveal) | truth | `␣revealing`, `透露` | 0/152 (0%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 0/65 (0%) | 1/76 (1%) |
| accidental (by accident, unintentionally) | unclear | `␣accidental` | 1/152 (1%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 0/65 (0%) | 0/76 (0%) |
| accuse (accusation) | unclear | `␣accusations`, `指控` | 1/152 (1%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 1/65 (2%) | 0/76 (0%) |
| keep a promise (to make good on a promise (兑现)) | unclear | `兑现` | 1/152 (1%) | 0/81 (0%) | 0/138 (0%) | 2/158 (1%) | 1/65 (2%) | 0/76 (0%) |
| inaccurate (inaccurate) | lie | `准确性和`, `不准确` | 0/152 (0%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 0/65 (0%) | 1/76 (1%) |
| truth (the truth (noun)) | truth | `求真` | 0/152 (0%) | 0/81 (0%) | 1/138 (1%) | 0/158 (0%) | 0/65 (0%) | 0/76 (0%) |

Not in the draft: fool / coax (held back: no undisputed member left); deny (excluded: admit / deny / acknowledge); admit (excluded: admit / deny / acknowledge)

## q_tok5

| family | side | members | lies | truths | no-pressure truths | unrelated | lies that deny | truths that deny |
|---|---|---|---|---|---|---|---|---|
| fact (fact, factual) | truth | `与现实` | 5/152 (3%) | 1/81 (1%) | 0/138 (0%) | 1/158 (1%) | 1/65 (2%) | 1/76 (1%) |
| fake (fake; to fake) | lie | `fake` | 4/152 (3%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 1/65 (2%) | 0/76 (0%) |
| conceal (to keep the truth from someone) | lie | `瞒`, `隐` | 1/152 (1%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 0/65 (0%) | 0/76 (0%) |
| integrity (integrity, good faith (诚信)) | truth | `␣integrity`, `诚信` | 1/152 (1%) | 1/81 (1%) | 1/138 (1%) | 0/158 (0%) | 0/65 (0%) | 1/76 (1%) |
| promise (a promise or guarantee) | unclear | `的承诺` | 0/152 (0%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 0/65 (0%) | 1/76 (1%) |
| false (false, untrue) | lie | `虚假` | 1/152 (1%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 1/65 (2%) | 0/76 (0%) |

## q_tok6

| family | side | members | lies | truths | no-pressure truths | unrelated | lies that deny | truths that deny |
|---|---|---|---|---|---|---|---|---|
| false (false, untrue) | lie | `␣false`, `false`, `假`, `虚假`, `假的` | 123/152 (81%) | 39/81 (48%) | 31/138 (22%) | 4/158 (3%) | 55/65 (85%) | 36/76 (47%) |
| intentional (on purpose, deliberately) | unclear | `故意`, `␣intentionally`, `␣deliberately`, `␣intentional`, `故意的`, `刻意`, `特意` | 65/152 (43%) | 41/81 (51%) | 27/138 (20%) | 4/158 (3%) | 24/65 (37%) | 36/76 (47%) |
| contradict (to contradict; contradiction) | unclear | `␣contradict`, `␣contrad`, `␣contradictory`, `矛盾`, `␣contradiction`, `␣conflicting`, `矛盾的` | 52/152 (34%) | 27/81 (33%) | 34/138 (25%) | 0/158 (0%) | 27/65 (42%) | 25/76 (33%) |
| conceal (hiding or covering up information) | lie | `隐瞒`, `掩饰`, `掩盖`, `瞒`, `藏着` | 54/152 (36%) | 10/81 (12%) | 3/138 (2%) | 0/158 (0%) | 28/65 (43%) | 9/76 (12%) |
| conceal (to keep the truth from someone) | lie | `隐瞒`, `瞒` | 44/152 (29%) | 7/81 (9%) | 3/138 (2%) | 0/158 (0%) | 22/65 (34%) | 6/76 (8%) |
| cover up (to cover up or gloss over (掩盖, 掩饰, 遮掩)) | lie | `掩饰`, `掩盖` | 38/152 (25%) | 7/81 (9%) | 0/138 (0%) | 0/158 (0%) | 21/65 (32%) | 6/76 (8%) |
| fact (fact, factual) | truth | `␣factual`, `与现实`, `上述事实` | 24/152 (16%) | 17/81 (21%) | 13/138 (9%) | 8/158 (5%) | 14/65 (22%) | 17/76 (22%) |
| misinformation (false information given out) | lie | `虚假信息` | 37/152 (24%) | 2/81 (2%) | 0/138 (0%) | 0/158 (0%) | 15/65 (23%) | 2/76 (3%) |
| promise (a promise or guarantee) | unclear | `的保证` | 28/152 (18%) | 5/81 (6%) | 25/138 (18%) | 0/158 (0%) | 11/65 (17%) | 5/76 (7%) |
| deceive (the act of deceiving) | lie | `骗`, `欺骗` | 10/152 (7%) | 7/81 (9%) | 0/138 (0%) | 0/158 (0%) | 6/65 (9%) | 7/76 (9%) |
| fabricate (to make up something untrue) | lie | `虚构`, `伪造`, `␣fabricated`, `␣fabrication`, `␣invent`, `凭空` | 13/152 (9%) | 2/81 (2%) | 4/138 (3%) | 0/158 (0%) | 2/65 (3%) | 2/76 (3%) |
| refuse (to refuse; refusal) | unclear | `␣refusal`, `拒绝`, `␣refusing`, `拒`, `␣refuses`, `␣refused`, `␣refuse`, `␣refus` | 1/152 (1%) | 10/81 (12%) | 0/138 (0%) | 0/158 (0%) | 1/65 (2%) | 10/76 (13%) |
| truthful (truthful; telling it as it is) | truth | `␣truthful`, `如实` | 4/152 (3%) | 6/81 (7%) | 3/138 (2%) | 0/158 (0%) | 2/65 (3%) | 6/76 (8%) |
| pretend (to pretend) | lie | `假装`, `␣pretending` | 5/152 (3%) | 2/81 (2%) | 3/138 (2%) | 0/158 (0%) | 2/65 (3%) | 2/76 (3%) |
| out of thin air (made up from nothing (凭空)) | lie | `凭空` | 6/152 (4%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 0/65 (0%) | 0/76 (0%) |
| euphemistic (indirect, tactful wording (委婉)) | unclear | `委婉` | 1/152 (1%) | 5/81 (6%) | 0/138 (0%) | 0/158 (0%) | 0/65 (0%) | 5/76 (7%) |
| fake (fake; to fake) | lie | `␣fake`, `fake` | 4/152 (3%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 1/65 (2%) | 1/76 (1%) |
| honest (honest; honesty) | truth | `诚实`, `␣honesty` | 0/152 (0%) | 4/81 (5%) | 2/138 (1%) | 0/158 (0%) | 0/65 (0%) | 4/76 (5%) |
| blurt (blurting out (脱口)) | unclear | `脱口` | 1/152 (1%) | 2/81 (2%) | 2/138 (1%) | 0/158 (0%) | 1/65 (2%) | 2/76 (3%) |
| incorrect (incorrect) | lie | `不符合` | 1/152 (1%) | 2/81 (2%) | 0/138 (0%) | 0/158 (0%) | 1/65 (2%) | 2/76 (3%) |
| true (true, real) | truth | `内容的真实性`, `的真实性` | 0/152 (0%) | 3/81 (4%) | 3/138 (2%) | 0/158 (0%) | 0/65 (0%) | 3/76 (4%) |
| apologize (to apologize) | unclear | `␣apolog` | 0/152 (0%) | 2/81 (2%) | 9/138 (7%) | 0/158 (0%) | 0/65 (0%) | 2/76 (3%) |
| role-play (playing a role) | unclear | `扮演` | 0/152 (0%) | 2/81 (2%) | 1/138 (1%) | 0/158 (0%) | 0/65 (0%) | 2/76 (3%) |
| falsehood (an untrue statement (noun)) | lie | `␣falsehood` | 2/152 (1%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 1/65 (2%) | 0/76 (0%) |
| wrong (wrong, mistaken) | lie | `错`, `是错误的` | 0/152 (0%) | 2/81 (2%) | 0/138 (0%) | 0/158 (0%) | 0/65 (0%) | 1/76 (1%) |
| accurate (accurate) | truth | `准确` | 0/152 (0%) | 2/81 (2%) | 0/138 (0%) | 0/158 (0%) | 0/65 (0%) | 2/76 (3%) |
| mislead (to mislead) | lie | `误导` | 0/152 (0%) | 1/81 (1%) | 1/138 (1%) | 0/158 (0%) | 0/65 (0%) | 0/76 (0%) |
| perfunctory (to answer for form's sake, brush off (敷衍, 应付)) | unclear | `敷衍` | 1/152 (1%) | 0/81 (0%) | 2/138 (1%) | 1/158 (1%) | 1/65 (2%) | 0/76 (0%) |
| knowingly (knowingly, while knowing better (明知)) | unclear | `明知` | 1/152 (1%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 0/65 (0%) | 0/76 (0%) |
| accidental (by accident, unintentionally) | unclear | `␣unintention` | 0/152 (0%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 0/65 (0%) | 1/76 (1%) |
| violate (to violate a rule or principle) | unclear | `违背` | 0/152 (0%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 0/65 (0%) | 1/76 (1%) |
| ethics (ethics, morality (noun)) | unclear | `道德`, `的道德`, `␣moral` | 0/152 (0%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 0/65 (0%) | 1/76 (1%) |
| apologize (apologizing) | unclear | `道歉` | 0/152 (0%) | 1/81 (1%) | 10/138 (7%) | 0/158 (0%) | 0/65 (0%) | 1/76 (1%) |
| correct (correct) | truth | `纠正` | 0/152 (0%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 0/65 (0%) | 1/76 (1%) |
| objective (objective) | unclear | `客观` | 0/152 (0%) | 0/81 (0%) | 1/138 (1%) | 0/158 (0%) | 0/65 (0%) | 0/76 (0%) |

Not in the draft: deny (excluded: admit / deny / acknowledge); truth (excluded: truth from the question on); admit (excluded: admit / deny / acknowledge)

## q_tok7

| family | side | members | lies | truths | no-pressure truths | unrelated | lies that deny | truths that deny |
|---|---|---|---|---|---|---|---|---|
| true (true, real) | truth | `␣true`, `true`, `True`, `␣True`, `TRUE`, `真`, `真实`, `真实的`, `是真的`, `的真`, `的真实性` | 151/152 (99%) | 80/81 (99%) | 134/138 (97%) | 158/158 (100%) | 64/65 (98%) | 75/76 (99%) |
| fact (fact, factual) | truth | `␣facts`, `␣factual`, `事实`, `事实上`, `与现实` | 134/152 (88%) | 51/81 (63%) | 118/138 (86%) | 155/158 (98%) | 57/65 (88%) | 47/76 (62%) |
| intentional (on purpose, deliberately) | unclear | `␣intentionally`, `故意`, `故意的`, `␣intentional`, `␣deliberately` | 113/152 (74%) | 58/81 (72%) | 70/138 (51%) | 155/158 (98%) | 52/65 (80%) | 56/76 (74%) |
| honest (honest; honesty) | truth | `诚实`, `␣honesty`, `␣honest`, `诚`, `诚实守信` | 139/152 (91%) | 26/81 (32%) | 5/138 (4%) | 2/158 (1%) | 58/65 (89%) | 22/76 (29%) |
| truthful (truthful; telling it as it is) | truth | `␣truthful` | 114/152 (75%) | 16/81 (20%) | 2/138 (1%) | 40/158 (25%) | 46/65 (71%) | 13/76 (17%) |
| integrity (integrity, good faith, credibility) | truth | `诚信`, `信用` | 87/152 (57%) | 40/81 (49%) | 24/138 (17%) | 24/158 (15%) | 42/65 (65%) | 38/76 (50%) |
| integrity (integrity, good faith (诚信)) | truth | `诚信`, `诚实守信` | 84/152 (55%) | 38/81 (47%) | 24/138 (17%) | 24/158 (15%) | 41/65 (63%) | 36/76 (47%) |
| words and deeds (one's words and actions (言行, as in 言行一致)) | unclear | `言行` | 44/152 (29%) | 52/81 (64%) | 76/138 (55%) | 62/158 (39%) | 31/65 (48%) | 50/76 (66%) |
| false (false, untrue) | lie | `␣false`, `␣False`, `false`, `=False`, `␣fals`, `␣untrue`, `/false`, `假`, `虚假`, `假的` | 49/152 (32%) | 41/81 (51%) | 70/138 (51%) | 135/158 (85%) | 30/65 (46%) | 39/76 (51%) |
| keep a promise (to make good on a promise (兑现)) | unclear | `兑现` | 57/152 (38%) | 26/81 (32%) | 40/138 (29%) | 56/158 (35%) | 29/65 (45%) | 23/76 (30%) |
| contradict (to contradict; contradiction) | unclear | `␣contradictory`, `␣contradiction`, `␣contradict`, `␣conflicting`, `␣contrad`, `矛盾`, `␣contradictions`, `␣inconsistent`, `␣inconsistencies`, `␣inconsistency` | 12/152 (8%) | 32/81 (40%) | 13/138 (9%) | 0/158 (0%) | 10/65 (15%) | 32/76 (42%) |
| knowingly (knowingly, while knowing better (明知)) | unclear | `明知` | 40/152 (26%) | 3/81 (4%) | 3/138 (2%) | 6/158 (4%) | 21/65 (32%) | 3/76 (4%) |
| intent (intention (noun)) | unclear | `␣intentions`, `意图` | 23/152 (15%) | 19/81 (23%) | 1/138 (1%) | 0/158 (0%) | 11/65 (17%) | 19/76 (25%) |
| deceive (the act of deceiving) | lie | `欺骗` | 16/152 (11%) | 17/81 (21%) | 4/138 (3%) | 50/158 (32%) | 12/65 (18%) | 17/76 (22%) |
| accuse (accusation) | unclear | `指控` | 10/152 (7%) | 8/81 (10%) | 20/138 (14%) | 1/158 (1%) | 3/65 (5%) | 8/76 (11%) |
| violate (to violate a rule or principle) | unclear | `违反`, `违反了` | 4/152 (3%) | 8/81 (10%) | 3/138 (2%) | 0/158 (0%) | 2/65 (3%) | 7/76 (9%) |
| fake (fake; to fake) | lie | `␣fake` | 2/152 (1%) | 5/81 (6%) | 0/138 (0%) | 21/158 (13%) | 2/65 (3%) | 5/76 (7%) |
| inconsistent (inconsistent) | unclear | `␣inconsistent`, `␣inconsistencies`, `␣inconsistency` | 1/152 (1%) | 5/81 (6%) | 2/138 (1%) | 0/158 (0%) | 0/65 (0%) | 5/76 (7%) |
| conceal (to keep the truth from someone) | lie | `隐瞒` | 1/152 (1%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 1/65 (2%) | 0/76 (0%) |
| hypocritical (hypocritical, false-faced (虚伪)) | lie | `虚伪` | 1/152 (1%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 1/65 (2%) | 0/76 (0%) |
| comply (to comply with, follow rules (遵守, 遵循, 遵照)) | unclear | `遵守` | 0/152 (0%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 0/65 (0%) | 1/76 (1%) |
| betray (to betray (出卖)) | unclear | `出卖` | 1/152 (1%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 1/65 (2%) | 0/76 (0%) |
| falsehood (an untrue statement (noun)) | lie | `␣falsehood` | 1/152 (1%) | 0/81 (0%) | 0/138 (0%) | 5/158 (3%) | 1/65 (2%) | 0/76 (0%) |

Not in the draft: deny (excluded: admit / deny / acknowledge); truth (excluded: truth from the question on)
