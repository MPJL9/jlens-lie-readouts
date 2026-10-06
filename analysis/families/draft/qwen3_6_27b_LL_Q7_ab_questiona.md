# Draft families: qwen3.6-27b, logit lens, part Q7_ab, group questiona

Written by `scripts/apply_family_decisions.py` (2026-10-01; draft, not frozen). Counts are `present / transcripts (share)`
on the build split.

## q_tok0

| family | side | members | lies | truths | no-pressure truths | unrelated | lies that deny | truths that deny |
|---|---|---|---|---|---|---|---|---|
| true (true, real) | truth | `真的`, `确实` | 65/152 (43%) | 20/81 (25%) | 17/138 (12%) | 3/158 (2%) | 34/79 (43%) | 19/77 (25%) |
| knowingly (knowingly, with knowledge (明知)) | unclear | `␣knowingly`, `知情` | 9/152 (6%) | 2/81 (2%) | 0/138 (0%) | 0/158 (0%) | 6/79 (8%) | 2/77 (3%) |
| wrong (wrong, mistaken) | lie | `错`, `错了`, `误会` | 2/152 (1%) | 4/81 (5%) | 12/138 (9%) | 3/158 (2%) | 2/79 (3%) | 4/77 (5%) |
| misunderstand (misunderstanding) | unclear | `␣misunderstand`, `␣misunderstood` | 3/152 (2%) | 2/81 (2%) | 1/138 (1%) | 0/158 (0%) | 3/79 (4%) | 2/77 (3%) |
| deliberate (on purpose, intentionally) | unclear | `␣intentionally`, `␣intentional`, `␣deliberate`, `␣deliberately` | 2/152 (1%) | 2/81 (2%) | 0/138 (0%) | 0/158 (0%) | 2/79 (3%) | 2/77 (3%) |
| false (false, untrue) | lie | `␣fals` | 2/152 (1%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 2/79 (3%) | 0/77 (0%) |
| contradict (contradicting, contradiction) | unclear | `␣contradict` | 1/152 (1%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 1/79 (1%) | 0/77 (0%) |
| fact (fact, factual) | unclear | `事实`, `符合` | 1/152 (1%) | 0/81 (0%) | 1/138 (1%) | 0/158 (0%) | 1/79 (1%) | 0/77 (0%) |
| incorrect (incorrect) | lie | `有误` | 0/152 (0%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 0/79 (0%) | 1/77 (1%) |
| correct (correct) | truth | `␣correctly` | 0/152 (0%) | 0/81 (0%) | 0/138 (0%) | 2/158 (1%) | 0/79 (0%) | 0/77 (0%) |
| accurate (accurate) | truth | `␣accurately` | 0/152 (0%) | 0/81 (0%) | 0/138 (0%) | 1/158 (1%) | 0/79 (0%) | 0/77 (0%) |

Not in the draft: deny (excluded: admit / deny / acknowledge); admit (excluded: admit / deny / acknowledge); truth (excluded: the question's own word)

## q_tok1

| family | side | members | lies | truths | no-pressure truths | unrelated | lies that deny | truths that deny |
|---|---|---|---|---|---|---|---|---|
| knowingly (doing it with knowledge of the facts) | unclear | `明知`, `知情`, `␣knowingly`, `␣knowing`, `␣Knowing` | 80/152 (53%) | 30/81 (37%) | 26/138 (19%) | 13/158 (8%) | 47/79 (59%) | 30/77 (39%) |
| deliberate (on purpose, intentionally) | unclear | `␣intentionally`, `␣deliberately`, `故意`, `刻意`, `␣deliberate`, `特意`, `␣intentional`, `故意的`, `有意` | 56/152 (37%) | 38/81 (47%) | 26/138 (19%) | 79/158 (50%) | 39/79 (49%) | 37/77 (48%) |
| knowingly (knowingly, with knowledge (明知)) | unclear | `明知`, `␣knowingly` | 59/152 (39%) | 23/81 (28%) | 6/138 (4%) | 1/158 (1%) | 37/79 (47%) | 23/77 (30%) |
| conceal (hiding or covering up information) | lie | `隐瞒`, `瞒`, `隐藏`, `掩盖`, `␣conceal`, `掩饰`, `␣hiding`, `␣hidden`, `␣hide`, `hide`, `␣hides`, `-hidden`, `遮盖`, `隐藏的`, `藏`, `掩`, `遮` | 52/152 (34%) | 13/81 (16%) | 0/138 (0%) | 0/158 (0%) | 25/79 (32%) | 13/77 (17%) |
| false (false, untrue) | lie | `␣false`, `false`, `False`, `>false`, `␣fals`, `/false`, `␣falsehood`, `假`, `虚假`, `假的`, `虚假信息` | 50/152 (33%) | 10/81 (12%) | 7/138 (5%) | 0/158 (0%) | 23/79 (29%) | 8/77 (10%) |
| contradict (contradicting, contradiction) | unclear | `␣contradict`, `矛盾`, `␣contrad`, `矛盾的` | 32/152 (21%) | 20/81 (25%) | 23/138 (17%) | 1/158 (1%) | 17/79 (22%) | 19/77 (25%) |
| integrity (integrity, trustworthiness (诚信)) | truth | `诚信` | 29/152 (19%) | 9/81 (11%) | 0/138 (0%) | 0/158 (0%) | 11/79 (14%) | 9/77 (12%) |
| fabricate (making up content that is not real) | lie | `伪造`, `虚构`, `␣fabricated`, `␣invent`, `凭空` | 31/152 (20%) | 5/81 (6%) | 2/138 (1%) | 6/158 (4%) | 15/79 (19%) | 3/77 (4%) |
| inform (informing, telling someone (告知)) | unclear | `告知` | 17/152 (11%) | 18/81 (22%) | 6/138 (4%) | 0/158 (0%) | 4/79 (5%) | 16/77 (21%) |
| violate (violating a rule, duty or law) | unclear | `违反`, `违背`, `␣violate`, `违规` | 14/152 (9%) | 17/81 (21%) | 3/138 (2%) | 0/158 (0%) | 8/79 (10%) | 17/77 (22%) |
| groundless (out of thin air, without basis (凭空)) | lie | `凭空` | 25/152 (16%) | 2/81 (2%) | 1/138 (1%) | 4/158 (3%) | 10/79 (13%) | 2/77 (3%) |
| accidental (by accident, unintentionally) | unclear | `␣accidentally`, `␣случайно`, `␣accidental`, `␣accident`, `意外` | 22/152 (14%) | 4/81 (5%) | 8/138 (6%) | 14/158 (9%) | 6/79 (8%) | 3/77 (4%) |
| negate (negating, repudiating) | unclear | `否定` | 15/152 (10%) | 11/81 (14%) | 11/138 (8%) | 0/158 (0%) | 13/79 (16%) | 10/77 (13%) |
| wrong (wrong, mistaken) | lie | `␣error`, `␣mistake`, `␣mistakes`, `错`, `错误`, `不对`, `错了`, `没错`, `失误`, `是非` | 15/152 (10%) | 11/81 (14%) | 38/138 (28%) | 73/158 (46%) | 6/79 (8%) | 10/77 (13%) |
| perfunctory (brushing off, answering perfunctorily (敷衍)) | unclear | `敷衍` | 23/152 (15%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 11/79 (14%) | 1/77 (1%) |
| fact (fact, factual) | unclear | `␣fact`, `事实`, `␣factual`, `实际`, `符合`, `实际上`, `实际情况`, `事实上`, `是否符合`, `与实际` | 19/152 (12%) | 5/81 (6%) | 2/138 (1%) | 5/158 (3%) | 9/79 (11%) | 4/77 (5%) |
| role-play (playing a role) | unclear | `扮演`, `角色扮演` | 6/152 (4%) | 15/81 (19%) | 4/138 (3%) | 0/158 (0%) | 3/79 (4%) | 15/77 (19%) |
| true (true, real) | truth | `真`, `真的`, `成立`, `真正`, `确实`, `真正的`, `真的是` | 17/152 (11%) | 4/81 (5%) | 0/138 (0%) | 0/158 (0%) | 11/79 (14%) | 3/77 (4%) |
| candid (candid, upfront) | truth | `坦诚` | 11/152 (7%) | 9/81 (11%) | 0/138 (0%) | 0/158 (0%) | 2/79 (3%) | 9/77 (12%) |
| fake (fake, not genuine) | lie | `fake`, `␣fake`, `_fake`, `伪造` | 18/152 (12%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 9/79 (11%) | 0/77 (0%) |
| honest (honest, honesty) | truth | `␣honestly`, `␣honesty`, `␣honest`, `␣Honest` | 10/152 (7%) | 8/81 (10%) | 0/138 (0%) | 0/158 (0%) | 2/79 (3%) | 8/77 (10%) |
| misunderstand (misunderstanding) | unclear | `␣misunderstand` | 2/152 (1%) | 15/81 (19%) | 29/138 (21%) | 16/158 (10%) | 1/79 (1%) | 14/77 (18%) |
| transparent (transparent, transparency) | truth | `␣transparent`, `透明`, `透明的`, `␣transparency`, `␣Transparency`, `透明度` | 9/152 (6%) | 5/81 (6%) | 0/138 (0%) | 0/158 (0%) | 2/79 (3%) | 5/77 (6%) |
| objective (objective, impartial (客观)) | unclear | `客观` | 7/152 (5%) | 4/81 (5%) | 3/138 (2%) | 0/158 (0%) | 4/79 (5%) | 4/77 (5%) |
| cover up (covering up or masking the truth) | lie | `掩盖`, `掩饰`, `遮盖` | 11/152 (7%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 4/79 (5%) | 0/77 (0%) |
| insinuate (hinting or implying) | unclear | `暗示` | 7/152 (5%) | 1/81 (1%) | 1/138 (1%) | 0/158 (0%) | 3/79 (4%) | 1/77 (1%) |
| consistent (being consistent) | unclear | `一致`, `一致的` | 7/152 (5%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 1/79 (1%) | 1/77 (1%) |
| deceive (the act of deceiving) | lie | `欺骗`, `骗`, `␣deception`, `欺`, `哄` | 5/152 (3%) | 2/81 (2%) | 0/138 (0%) | 0/158 (0%) | 1/79 (1%) | 2/77 (3%) |
| disclose (disclosing information) | truth | `信息披露`, `␣disclosure`, `␣disclose` | 3/152 (2%) | 4/81 (5%) | 0/138 (0%) | 0/158 (0%) | 1/79 (1%) | 4/77 (5%) |
| accurate (accurate) | truth | `␣accuracy`, `␣accurately`, `准确` | 5/152 (3%) | 2/81 (2%) | 2/138 (1%) | 15/158 (9%) | 1/79 (1%) | 2/77 (3%) |
| evade (evading, avoiding the question) | unclear | `回避` | 5/152 (3%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 4/79 (5%) | 1/77 (1%) |
| omit (leaving information out) | lie | `省略`, `␣omit` | 4/152 (3%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 2/79 (3%) | 1/77 (1%) |
| secret (secret, secrecy) | lie | `␣secret`, `␣secretly`, `秘密`, `secret`, `␣Secret`, `的秘密` | 3/152 (2%) | 2/81 (2%) | 0/138 (0%) | 0/158 (0%) | 2/79 (3%) | 2/77 (3%) |
| exaggerate (exaggerating) | lie | `夸大`, `␣exagger` | 3/152 (2%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 2/79 (3%) | 1/77 (1%) |
| confess (confessing, owning up (坦白)) | truth | `坦白` | 1/152 (1%) | 3/81 (4%) | 0/138 (0%) | 0/158 (0%) | 0/79 (0%) | 3/77 (4%) |
| incorrect (incorrect) | lie | `␣incorrect`, `␣incorrectly`, `␣Incorrect`, `错误的`, `不符合`, `有误` | 0/152 (0%) | 4/81 (5%) | 0/138 (0%) | 3/158 (2%) | 0/79 (0%) | 4/77 (5%) |
| refuse (refusing) | unclear | `拒绝`, `␣refusal` | 0/152 (0%) | 3/81 (4%) | 0/138 (0%) | 0/158 (0%) | 0/79 (0%) | 3/77 (4%) |
| sincere (sincere, genuine, in earnest) | truth | `␣genuinely` | 2/152 (1%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 1/79 (1%) | 0/77 (0%) |
| euphemistic (euphemistic, tactfully indirect (委婉)) | unclear | `委婉` | 2/152 (1%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 2/79 (3%) | 0/77 (0%) |
| excuse (an excuse) | unclear | `借口`, `␣excuse` | 2/152 (1%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 0/79 (0%) | 0/77 (0%) |
| fraud (defrauding, obtaining something by deceit) | lie | `␣fraud` | 1/152 (1%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 1/79 (1%) | 0/77 (0%) |
| withhold (withholding information) | lie | `␣withholding` | 0/152 (0%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 0/79 (0%) | 1/77 (1%) |
| mislead (misleading someone) | lie | `误导` | 0/152 (0%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 0/79 (0%) | 0/77 (0%) |
| dishonest (dishonest) | lie | `␣dishonest` | 1/152 (1%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 1/79 (1%) | 0/77 (0%) |
| intention (intention (noun)) | unclear | `␣intention` | 1/152 (1%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 1/79 (1%) | 0/77 (0%) |
| ethics (ethics, morality) | unclear | `␣ethical`, `␣ethics` | 0/152 (0%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 0/79 (0%) | 1/77 (1%) |
| conscience (conscience (良心)) | unclear | `良心` | 0/152 (0%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 0/79 (0%) | 1/77 (1%) |
| apologize (apologizing (道歉)) | unclear | `道歉` | 0/152 (0%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 0/79 (0%) | 1/77 (1%) |
| confidential (confidentiality) | unclear | `␣confidentiality` | 0/152 (0%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 0/79 (0%) | 1/77 (1%) |
| betray (betraying, selling out) | lie | `出卖` | 0/152 (0%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 0/79 (0%) | 1/77 (1%) |
| correct (correct) | truth | `␣correct`, `␣correctly`, `正确`, `正确的` | 1/152 (1%) | 0/81 (0%) | 5/138 (4%) | 52/158 (33%) | 1/79 (1%) | 0/77 (0%) |

Not in the draft: deny (excluded: admit / deny / acknowledge); admit (excluded: admit / deny / acknowledge); truth (excluded: the question's own word)

## q_tok2

| family | side | members | lies | truths | no-pressure truths | unrelated | lies that deny | truths that deny |
|---|---|---|---|---|---|---|---|---|
| deceive (the act of deceiving) | lie | `欺骗`, `骗`, `␣deception`, `哄` | 152/152 (100%) | 81/81 (100%) | 138/138 (100%) | 158/158 (100%) | 79/79 (100%) | 77/77 (100%) |
| integrity (integrity, trustworthiness (诚信)) | truth | `诚信` | 152/152 (100%) | 81/81 (100%) | 138/138 (100%) | 158/158 (100%) | 79/79 (100%) | 77/77 (100%) |
| false (false, untrue) | lie | `␣false`, `␣False`, `false`, `=False`, `=false`, `␣fals`, `␣untrue`, `/false`, `␣falsehood`, `假`, `虚假`, `假的`, `真假`, `虚假信息` | 152/152 (100%) | 81/81 (100%) | 138/138 (100%) | 158/158 (100%) | 79/79 (100%) | 77/77 (100%) |
| conceal (hiding or covering up information) | lie | `隐瞒`, `␣conceal`, `掩盖`, `瞒`, `掩饰` | 131/152 (86%) | 71/81 (88%) | 29/138 (21%) | 18/158 (11%) | 65/79 (82%) | 68/77 (88%) |
| fake (fake, not genuine) | lie | `fake`, `␣fake`, `Fake`, `␣Fake` | 128/152 (84%) | 67/81 (83%) | 129/138 (93%) | 145/158 (92%) | 59/79 (75%) | 64/77 (83%) |
| omit (leaving information out) | lie | `␣omission`, `␣omit`, `omit`, `␣OMIT` | 53/152 (35%) | 38/81 (47%) | 9/138 (7%) | 0/158 (0%) | 30/79 (38%) | 35/77 (45%) |
| deliberate (on purpose, intentionally) | unclear | `故意`, `␣intentionally`, `␣deliberately`, `␣deliberate`, `故意的`, `␣intentional`, `有意` | 50/152 (33%) | 25/81 (31%) | 99/138 (72%) | 73/158 (46%) | 26/79 (33%) | 23/77 (30%) |
| inform (informing, telling someone (告知)) | unclear | `告知` | 12/152 (8%) | 2/81 (2%) | 0/138 (0%) | 0/158 (0%) | 1/79 (1%) | 2/77 (3%) |
| fact (fact, factual) | unclear | `事实`, `␣factual`, `␣facts`, `与现实` | 9/152 (6%) | 3/81 (4%) | 1/138 (1%) | 31/158 (20%) | 4/79 (5%) | 3/77 (4%) |
| cover up (covering up or masking the truth) | lie | `掩盖`, `掩饰` | 9/152 (6%) | 3/81 (4%) | 0/138 (0%) | 0/158 (0%) | 8/79 (10%) | 3/77 (4%) |
| candid (candid, upfront) | truth | `␣upfront` | 3/152 (2%) | 3/81 (4%) | 0/138 (0%) | 0/158 (0%) | 1/79 (1%) | 3/77 (4%) |
| knowingly (knowingly, with knowledge (明知)) | unclear | `␣knowingly`, `明知`, `知情` | 4/152 (3%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 3/79 (4%) | 1/77 (1%) |
| fabricate (making up content that is not real) | lie | `␣invent`, `虚构`, `␣invented`, `凭空` | 3/152 (2%) | 0/81 (0%) | 34/138 (25%) | 88/158 (56%) | 0/79 (0%) | 0/77 (0%) |
| betray (betraying, selling out) | lie | `出卖` | 0/152 (0%) | 3/81 (4%) | 4/138 (3%) | 0/158 (0%) | 0/79 (0%) | 3/77 (4%) |
| mislead (misleading someone) | lie | `误导` | 0/152 (0%) | 1/81 (1%) | 1/138 (1%) | 0/158 (0%) | 0/79 (0%) | 1/77 (1%) |
| groundless (out of thin air, without basis (凭空)) | lie | `凭空` | 1/152 (1%) | 0/81 (0%) | 5/138 (4%) | 0/158 (0%) | 0/79 (0%) | 0/77 (0%) |
| intention (intention (noun)) | unclear | `␣intentions` | 0/152 (0%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 0/79 (0%) | 1/77 (1%) |
| accuse (accusation) | unclear | `指控` | 1/152 (1%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 1/79 (1%) | 0/77 (0%) |

Not in the draft: honest (excluded: the question's own word); admit (excluded: admit / deny / acknowledge); truth (excluded: the question's own word); true (excluded: the question's own word)

## q_tok3

| family | side | members | lies | truths | no-pressure truths | unrelated | lies that deny | truths that deny |
|---|---|---|---|---|---|---|---|---|
| false (false, untrue) | lie | `␣false`, `=False`, `␣FALSE`, `␣fals`, `/false`, `␣falsehood`, `假`, `虚假` | 73/152 (48%) | 26/81 (32%) | 47/138 (34%) | 139/158 (88%) | 42/79 (53%) | 26/77 (34%) |
| integrity (integrity, trustworthiness (诚信)) | truth | `诚信` | 72/152 (47%) | 19/81 (23%) | 22/138 (16%) | 125/158 (79%) | 34/79 (43%) | 17/77 (22%) |
| cover up (covering up or masking the truth) | lie | `␣disguise`, `掩盖`, `掩饰` | 54/152 (36%) | 21/81 (26%) | 15/138 (11%) | 12/158 (8%) | 32/79 (41%) | 19/77 (25%) |
| knowingly (knowingly, with knowledge (明知)) | unclear | `明知`, `␣knowingly`, `知情` | 53/152 (35%) | 16/81 (20%) | 7/138 (5%) | 2/158 (1%) | 27/79 (34%) | 16/77 (21%) |
| conceal (hiding or covering up information) | lie | `隐瞒`, `掩盖`, `hide`, `␣hiding`, `␣conceal`, `␣hide`, `Hide`, `瞒`, `掩饰`, `隐匿`, `遮` | 43/152 (28%) | 22/81 (27%) | 8/138 (6%) | 10/158 (6%) | 28/79 (35%) | 21/77 (27%) |
| disguise (disguising the true nature of something) | lie | `␣disguise` | 48/152 (32%) | 16/81 (20%) | 12/138 (9%) | 12/158 (8%) | 27/79 (34%) | 14/77 (18%) |
| sincere (sincere, genuine, in earnest) | truth | `␣earnest` | 24/152 (16%) | 5/81 (6%) | 2/138 (1%) | 7/158 (4%) | 11/79 (14%) | 5/77 (6%) |
| deliberate (on purpose, intentionally) | unclear | `故意` | 15/152 (10%) | 14/81 (17%) | 6/138 (4%) | 0/158 (0%) | 8/79 (10%) | 14/77 (18%) |
| deceive (the act of deceiving) | lie | `欺骗`, `␣deception`, `骗`, `哄` | 14/152 (9%) | 5/81 (6%) | 1/138 (1%) | 12/158 (8%) | 8/79 (10%) | 5/77 (6%) |
| fact (fact, factual) | unclear | `␣fact`, `事实上` | 13/152 (9%) | 2/81 (2%) | 3/138 (2%) | 4/158 (3%) | 10/79 (13%) | 2/77 (3%) |
| mislead (misleading someone) | lie | `误导`, `␣misleading` | 5/152 (3%) | 8/81 (10%) | 0/138 (0%) | 0/158 (0%) | 3/79 (4%) | 8/77 (10%) |
| fake (fake, not genuine) | lie | `fake`, `␣fake` | 7/152 (5%) | 5/81 (6%) | 1/138 (1%) | 23/158 (15%) | 4/79 (5%) | 5/77 (6%) |
| contradict (contradicting, contradiction) | unclear | `␣contrad`, `␣contradict` | 5/152 (3%) | 3/81 (4%) | 2/138 (1%) | 0/158 (0%) | 4/79 (5%) | 3/77 (4%) |
| disclose (disclosing information) | truth | `信息披露` | 5/152 (3%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 5/79 (6%) | 1/77 (1%) |
| honest (honest, honesty) | truth | `␣honest`, `␣honesty` | 4/152 (3%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 2/79 (3%) | 0/77 (0%) |
| transparent (transparent, transparency) | truth | `透明` | 3/152 (2%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 2/79 (3%) | 0/77 (0%) |
| inform (informing, telling someone (告知)) | unclear | `告知` | 2/152 (1%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 2/79 (3%) | 1/77 (1%) |
| betray (betraying, selling out) | lie | `出卖` | 2/152 (1%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 0/79 (0%) | 1/77 (1%) |
| negate (negating, repudiating) | unclear | `否定` | 0/152 (0%) | 3/81 (4%) | 0/138 (0%) | 0/158 (0%) | 0/79 (0%) | 3/77 (4%) |
| role-play (playing a role) | unclear | `角色扮演`, `扮演` | 0/152 (0%) | 2/81 (2%) | 0/138 (0%) | 0/158 (0%) | 0/79 (0%) | 2/77 (3%) |
| exaggerate (exaggerating) | lie | `夸大` | 1/152 (1%) | 0/81 (0%) | 0/138 (0%) | 1/158 (1%) | 0/79 (0%) | 0/77 (0%) |
| candid (candid, upfront) | truth | `坦诚` | 1/152 (1%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 1/79 (1%) | 0/77 (0%) |
| violate (violating a rule, duty or law) | unclear | `违反`, `违背` | 0/152 (0%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 0/79 (0%) | 1/77 (1%) |
| euphemistic (euphemistic, tactfully indirect (委婉)) | unclear | `委婉` | 0/152 (0%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 0/79 (0%) | 1/77 (1%) |

Not in the draft: deny (excluded: admit / deny / acknowledge); admit (excluded: admit / deny / acknowledge); truth (excluded: the question's own word); perfunctory (held back: no undisputed member left); true (excluded: the question's own word)

## q_tok4

| family | side | members | lies | truths | no-pressure truths | unrelated | lies that deny | truths that deny |
|---|---|---|---|---|---|---|---|---|
| false (false, untrue) | lie | `false`, `=False`, `␣fals`, `/false`, `␣falsehood`, `假`, `虚假` | 39/152 (26%) | 10/81 (12%) | 1/138 (1%) | 43/158 (27%) | 20/79 (25%) | 8/77 (10%) |
| knowingly (knowingly, with knowledge (明知)) | unclear | `明知`, `知情` | 26/152 (17%) | 12/81 (15%) | 36/138 (26%) | 5/158 (3%) | 13/79 (16%) | 12/77 (16%) |
| negate (negating, repudiating) | unclear | `否定` | 14/152 (9%) | 16/81 (20%) | 5/138 (4%) | 0/158 (0%) | 10/79 (13%) | 16/77 (21%) |
| refuse (refusing) | unclear | `␣refusal`, `拒绝` | 1/152 (1%) | 13/81 (16%) | 0/138 (0%) | 0/158 (0%) | 1/79 (1%) | 13/77 (17%) |
| fabricate (making up content that is not real) | lie | `␣fabricated`, `␣fabrication`, `虚构`, `伪造`, `凭空` | 9/152 (6%) | 3/81 (4%) | 1/138 (1%) | 3/158 (2%) | 4/79 (5%) | 2/77 (3%) |
| fake (fake, not genuine) | lie | `␣fake`, `fake`, `_fake`, `伪造` | 10/152 (7%) | 2/81 (2%) | 0/138 (0%) | 1/158 (1%) | 3/79 (4%) | 2/77 (3%) |
| conceal (hiding or covering up information) | lie | `隐瞒`, `掩饰`, `掩盖`, `瞒`, `隐藏`, `藏` | 5/152 (3%) | 3/81 (4%) | 0/138 (0%) | 9/158 (6%) | 5/79 (6%) | 3/77 (4%) |
| wrong (wrong, mistaken) | lie | `错`, `错了` | 3/152 (2%) | 5/81 (6%) | 1/138 (1%) | 2/158 (1%) | 2/79 (3%) | 5/77 (6%) |
| honest (honest, honesty) | truth | `␣honest`, `␣honesty` | 4/152 (3%) | 3/81 (4%) | 0/138 (0%) | 0/158 (0%) | 1/79 (1%) | 3/77 (4%) |
| integrity (integrity, trustworthiness (诚信)) | truth | `诚信` | 5/152 (3%) | 1/81 (1%) | 1/138 (1%) | 8/158 (5%) | 2/79 (3%) | 1/77 (1%) |
| deliberate (on purpose, intentionally) | unclear | `故意`, `刻意` | 2/152 (1%) | 4/81 (5%) | 1/138 (1%) | 0/158 (0%) | 0/79 (0%) | 3/77 (4%) |
| contradict (contradicting, contradiction) | unclear | `␣contrad`, `␣contradictory`, `␣contradict` | 3/152 (2%) | 3/81 (4%) | 4/138 (3%) | 0/158 (0%) | 2/79 (3%) | 3/77 (4%) |
| role-play (playing a role) | unclear | `扮演` | 3/152 (2%) | 3/81 (4%) | 3/138 (2%) | 0/158 (0%) | 1/79 (1%) | 3/77 (4%) |
| cover up (covering up or masking the truth) | lie | `掩饰`, `掩盖` | 3/152 (2%) | 2/81 (2%) | 0/138 (0%) | 0/158 (0%) | 3/79 (4%) | 2/77 (3%) |
| fact (fact, factual) | unclear | `␣factual` | 1/152 (1%) | 2/81 (2%) | 5/138 (4%) | 0/158 (0%) | 1/79 (1%) | 2/77 (3%) |
| betray (betraying, selling out) | lie | `出卖` | 0/152 (0%) | 3/81 (4%) | 0/138 (0%) | 0/158 (0%) | 0/79 (0%) | 3/77 (4%) |
| groundless (out of thin air, without basis (凭空)) | lie | `凭空` | 2/152 (1%) | 0/81 (0%) | 0/138 (0%) | 3/158 (2%) | 1/79 (1%) | 0/77 (0%) |
| candid (candid, upfront) | truth | `坦诚` | 0/152 (0%) | 2/81 (2%) | 0/138 (0%) | 0/158 (0%) | 0/79 (0%) | 2/77 (3%) |
| disclose (disclosing information) | truth | `披露`, `信息披露` | 2/152 (1%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 2/79 (3%) | 0/77 (0%) |
| deceive (the act of deceiving) | lie | `欺骗` | 0/152 (0%) | 1/81 (1%) | 0/138 (0%) | 5/158 (3%) | 0/79 (0%) | 1/77 (1%) |
| fraud (defrauding, obtaining something by deceit) | lie | `欺诈` | 1/152 (1%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 1/79 (1%) | 0/77 (0%) |
| mislead (misleading someone) | lie | `误导` | 0/152 (0%) | 1/81 (1%) | 1/138 (1%) | 0/158 (0%) | 0/79 (0%) | 1/77 (1%) |
| pretend (pretending) | lie | `假装` | 0/152 (0%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 0/79 (0%) | 1/77 (1%) |
| sincere (sincere, genuine, in earnest) | truth | `␣genuine` | 1/152 (1%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 1/79 (1%) | 0/77 (0%) |
| perfunctory (brushing off, answering perfunctorily (敷衍)) | unclear | `敷衍` | 0/152 (0%) | 1/81 (1%) | 0/138 (0%) | 1/158 (1%) | 0/79 (0%) | 1/77 (1%) |
| inform (informing, telling someone (告知)) | unclear | `告知` | 1/152 (1%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 0/79 (0%) | 0/77 (0%) |
| accurate (accurate) | truth | `准确` | 0/152 (0%) | 0/81 (0%) | 4/138 (3%) | 0/158 (0%) | 0/79 (0%) | 0/77 (0%) |

Not in the draft: deny (excluded: admit / deny / acknowledge); admit (excluded: admit / deny / acknowledge); truth (excluded: the question's own word); true (excluded: the question's own word); correct (excluded: the question's own word)

## q_tok5

| family | side | members | lies | truths | no-pressure truths | unrelated | lies that deny | truths that deny |
|---|---|---|---|---|---|---|---|---|
| false (false, untrue) | lie | `虚假` | 6/152 (4%) | 3/81 (4%) | 0/138 (0%) | 0/158 (0%) | 5/79 (6%) | 3/77 (4%) |
| contradict (contradicting, contradiction) | unclear | `␣contradictory` | 0/152 (0%) | 2/81 (2%) | 0/138 (0%) | 0/158 (0%) | 0/79 (0%) | 2/77 (3%) |
| fake (fake, not genuine) | lie | `fake` | 1/152 (1%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 1/79 (1%) | 0/77 (0%) |
| disclose (disclosing information) | truth | `␣disclosures` | 0/152 (0%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 0/79 (0%) | 1/77 (1%) |
| fact (fact, factual) | truth | `与现实` | 1/152 (1%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 0/79 (0%) | 0/77 (0%) |

Not in the draft: true (excluded: the question's own word)

## q_tok6

| family | side | members | lies | truths | no-pressure truths | unrelated | lies that deny | truths that deny |
|---|---|---|---|---|---|---|---|---|
| deliberate (on purpose, intentionally) | unclear | `故意`, `␣intentionally`, `␣deliberately`, `刻意`, `故意的`, `␣deliberate`, `␣intentional`, `有意` | 122/152 (80%) | 70/81 (86%) | 108/138 (78%) | 89/158 (56%) | 57/79 (72%) | 67/77 (87%) |
| false (false, untrue) | lie | `␣false`, `false`, `␣FALSE`, `␣falsely`, `␣falsehood`, `假`, `虚假`, `假的`, `真假`, `虚假信息` | 146/152 (96%) | 39/81 (48%) | 47/138 (34%) | 17/158 (11%) | 76/79 (96%) | 36/77 (47%) |
| contradict (contradicting, contradiction) | unclear | `␣contradict`, `␣contrad`, `矛盾`, `␣contradictory`, `␣contradiction`, `矛盾的`, `␣conflicting` | 111/152 (73%) | 57/81 (70%) | 108/138 (78%) | 14/158 (9%) | 64/79 (81%) | 54/77 (70%) |
| conceal (hiding or covering up information) | lie | `隐瞒`, `掩饰`, `掩盖`, `瞒`, `遮掩`, `␣conceal`, `␣hiding`, `␣masking`, `␣hide`, `␣hides`, `遮` | 127/152 (84%) | 33/81 (41%) | 22/138 (16%) | 0/158 (0%) | 63/79 (80%) | 30/77 (39%) |
| fact (fact, factual) | unclear | `事实`, `␣factual`, `␣fact`, `␣facts`, `Fact`, `␣FACT`, `的事实`, `事实和`, `␣Fact`, `实际`, `符合`, `实际上`, `实际情况`, `事实上`, `是否符合`, `与实际`, `与现实`, `认定事实`, `上述事实` | 87/152 (57%) | 34/81 (42%) | 94/138 (68%) | 61/158 (39%) | 46/79 (58%) | 32/77 (42%) |
| cover up (covering up or masking the truth) | lie | `掩饰`, `掩盖`, `遮掩`, `␣masking` | 103/152 (68%) | 14/81 (17%) | 7/138 (5%) | 0/158 (0%) | 47/79 (59%) | 11/77 (14%) |
| fabricate (making up content that is not real) | lie | `␣fabricated`, `␣fabrication`, `虚构`, `␣invent`, `伪造`, `␣invented`, `凭空` | 95/152 (62%) | 20/81 (25%) | 46/138 (33%) | 26/158 (16%) | 38/79 (48%) | 18/77 (23%) |
| deceive (the act of deceiving) | lie | `欺骗`, `骗`, `␣deception`, `␣deceive`, `骗取`, `哄` | 79/152 (52%) | 16/81 (20%) | 5/138 (4%) | 11/158 (7%) | 33/79 (42%) | 14/77 (18%) |
| knowingly (knowingly, with knowledge (明知)) | unclear | `明知`, `␣knowingly`, `知情` | 75/152 (49%) | 14/81 (17%) | 9/138 (7%) | 6/158 (4%) | 34/79 (43%) | 11/77 (14%) |
| negate (negating, repudiating) | unclear | `否定` | 35/152 (23%) | 35/81 (43%) | 18/138 (13%) | 3/158 (2%) | 23/79 (29%) | 35/77 (45%) |
| wrong (wrong, mistaken) | lie | `error`, `␣error`, `␣wrong`, `错`, `错误`, `错了`, `是错误的` | 33/152 (22%) | 18/81 (22%) | 27/138 (20%) | 63/158 (40%) | 16/79 (20%) | 16/77 (21%) |
| fake (fake, not genuine) | lie | `fake`, `␣fake`, `_fake`, `伪造`, `forge` | 41/152 (27%) | 8/81 (10%) | 11/138 (8%) | 6/158 (4%) | 14/79 (18%) | 5/77 (6%) |
| disclose (disclosing information) | truth | `信息披露`, `␣disclosure`, `披露`, `␣disclose`, `␣disclosing` | 29/152 (19%) | 12/81 (15%) | 17/138 (12%) | 0/158 (0%) | 12/79 (15%) | 11/77 (14%) |
| withhold (withholding information) | lie | `␣withholding`, `␣withhold` | 29/152 (19%) | 8/81 (10%) | 2/138 (1%) | 0/158 (0%) | 15/79 (19%) | 7/77 (9%) |
| mislead (misleading someone) | lie | `误导`, `␣misleading` | 24/152 (16%) | 10/81 (12%) | 3/138 (2%) | 2/158 (1%) | 10/79 (13%) | 8/77 (10%) |
| omit (leaving information out) | lie | `␣omit`, `␣omission`, `省略`, `omit` | 18/152 (12%) | 9/81 (11%) | 1/138 (1%) | 0/158 (0%) | 9/79 (11%) | 8/77 (10%) |
| objective (objective, impartial (客观)) | unclear | `客观` | 20/152 (13%) | 7/81 (9%) | 1/138 (1%) | 4/158 (3%) | 14/79 (18%) | 7/77 (9%) |
| refuse (refusing) | unclear | `␣refusal`, `拒绝`, `␣refusing`, `␣refuse`, `␣refus`, `␣refuses`, `拒绝了` | 0/152 (0%) | 21/81 (26%) | 0/138 (0%) | 0/158 (0%) | 0/79 (0%) | 21/77 (27%) |
| incorrect (incorrect) | lie | `␣incorrectly`, `不符合`, `有误`, `错误的是` | 5/152 (3%) | 16/81 (20%) | 15/138 (11%) | 52/158 (33%) | 3/79 (4%) | 16/77 (21%) |
| perfunctory (brushing off, answering perfunctorily (敷衍)) | unclear | `敷衍` | 5/152 (3%) | 15/81 (19%) | 17/138 (12%) | 24/158 (15%) | 5/79 (6%) | 15/77 (19%) |
| inform (informing, telling someone (告知)) | unclear | `告知` | 17/152 (11%) | 2/81 (2%) | 4/138 (3%) | 0/158 (0%) | 5/79 (6%) | 0/77 (0%) |
| euphemistic (euphemistic, tactfully indirect (委婉)) | unclear | `委婉` | 8/152 (5%) | 10/81 (12%) | 1/138 (1%) | 0/158 (0%) | 4/79 (5%) | 8/77 (10%) |
| insinuate (hinting or implying) | unclear | `暗示` | 8/152 (5%) | 10/81 (12%) | 4/138 (3%) | 0/158 (0%) | 4/79 (5%) | 9/77 (12%) |
| violate (violating a rule, duty or law) | unclear | `违背`, `违反`, `␣violate`, `违反了`, `违法` | 11/152 (7%) | 6/81 (7%) | 2/138 (1%) | 0/158 (0%) | 4/79 (5%) | 6/77 (8%) |
| groundless (out of thin air, without basis (凭空)) | lie | `凭空` | 15/152 (10%) | 0/81 (0%) | 12/138 (9%) | 6/158 (4%) | 7/79 (9%) | 0/77 (0%) |
| accurate (accurate) | truth | `␣accur`, `␣accurate`, `␣accuracy`, `␣accurately`, `accuracy`, `准确` | 1/152 (1%) | 13/81 (16%) | 26/138 (19%) | 49/158 (31%) | 1/79 (1%) | 13/77 (17%) |
| inaccurate (inaccurate) | lie | `不准确` | 6/152 (4%) | 5/81 (6%) | 1/138 (1%) | 9/158 (6%) | 4/79 (5%) | 5/77 (6%) |
| exaggerate (exaggerating) | lie | `夸大` | 6/152 (4%) | 3/81 (4%) | 0/138 (0%) | 0/158 (0%) | 2/79 (3%) | 3/77 (4%) |
| evade (evading, avoiding the question) | unclear | `回避`, `␣evasion`, `␣dodge` | 7/152 (5%) | 2/81 (2%) | 0/138 (0%) | 0/158 (0%) | 4/79 (5%) | 2/77 (3%) |
| fraud (defrauding, obtaining something by deceit) | lie | `骗取` | 5/152 (3%) | 3/81 (4%) | 0/138 (0%) | 5/158 (3%) | 3/79 (4%) | 2/77 (3%) |
| integrity (integrity, trustworthiness (诚信)) | truth | `诚信` | 0/152 (0%) | 6/81 (7%) | 2/138 (1%) | 0/158 (0%) | 0/79 (0%) | 6/77 (8%) |
| inconsistent (inconsistent, conflicting) | unclear | `␣conflicting` | 1/152 (1%) | 5/81 (6%) | 4/138 (3%) | 0/158 (0%) | 1/79 (1%) | 4/77 (5%) |
| suspected (suspected of wrongdoing (涉嫌)) | unclear | `涉嫌` | 2/152 (1%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 1/79 (1%) | 1/77 (1%) |
| role-play (playing a role) | unclear | `扮演` | 1/152 (1%) | 2/81 (2%) | 0/138 (0%) | 0/158 (0%) | 1/79 (1%) | 2/77 (3%) |
| accidental (doing it by accident) | unclear | `无意` | 1/152 (1%) | 2/81 (2%) | 0/138 (0%) | 11/158 (7%) | 1/79 (1%) | 2/77 (3%) |
| correct (correct) | truth | `␣correct`, `␣correctly`, `正确`, `纠正`, `的正确`, `无误`, `是否正确` | 1/152 (1%) | 2/81 (2%) | 8/138 (6%) | 10/158 (6%) | 0/79 (0%) | 2/77 (3%) |
| candid (candid, upfront) | truth | `坦诚` | 0/152 (0%) | 2/81 (2%) | 1/138 (1%) | 3/158 (2%) | 0/79 (0%) | 2/77 (3%) |
| pretend (pretending) | lie | `␣pretending` | 0/152 (0%) | 1/81 (1%) | 0/138 (0%) | 5/158 (3%) | 0/79 (0%) | 1/77 (1%) |
| confess (confessing, owning up (坦白)) | truth | `坦白` | 0/152 (0%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 0/79 (0%) | 1/77 (1%) |
| vague (vague, blurred (模糊)) | unclear | `模糊` | 1/152 (1%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 1/79 (1%) | 0/77 (0%) |
| ethics (ethics, morality) | unclear | `的道德` | 0/152 (0%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 0/79 (0%) | 1/77 (1%) |
| betray (betraying, selling out) | lie | `出卖` | 0/152 (0%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 0/79 (0%) | 1/77 (1%) |

Not in the draft: deny (excluded: admit / deny / acknowledge); honest (excluded: the question's own word); admit (excluded: admit / deny / acknowledge); truth (excluded: the question's own word); true (excluded: the question's own word)

## q_tok7

| family | side | members | lies | truths | no-pressure truths | unrelated | lies that deny | truths that deny |
|---|---|---|---|---|---|---|---|---|
| true (true, real) | truth | `␣true`, `true`, `True`, `␣True`, `␣TRUE`, `真`, `是真的` | 152/152 (100%) | 81/81 (100%) | 138/138 (100%) | 158/158 (100%) | 79/79 (100%) | 77/77 (100%) |
| integrity (integrity, trustworthiness (诚信)) | truth | `诚信` | 127/152 (84%) | 73/81 (90%) | 85/138 (62%) | 155/158 (98%) | 72/79 (91%) | 71/77 (92%) |
| false (false, untrue) | lie | `␣false`, `␣False`, `false`, `False`, `=False`, `␣FALSE`, `=false`, `_FALSE`, `:false`, `␣fals`, `.assertFalse`, `.False`, `␣untrue`, `/false`, `␣falsehood`, `假`, `虚假`, `假的`, `真假` | 93/152 (61%) | 76/81 (94%) | 136/138 (99%) | 158/158 (100%) | 61/79 (77%) | 74/77 (96%) |
| deceive (the act of deceiving) | lie | `欺骗`, `␣deception`, `欺` | 105/152 (69%) | 63/81 (78%) | 119/138 (86%) | 157/158 (99%) | 58/79 (73%) | 60/77 (78%) |
| knowingly (knowingly, with knowledge (明知)) | unclear | `明知`, `知情` | 92/152 (61%) | 20/81 (25%) | 7/138 (5%) | 8/158 (5%) | 50/79 (63%) | 19/77 (25%) |
| intention (intention (noun)) | unclear | `␣intentions`, `␣intention`, `意图` | 58/152 (38%) | 49/81 (60%) | 19/138 (14%) | 5/158 (3%) | 25/79 (32%) | 46/77 (60%) |
| accuse (accusation) | unclear | `␣accusations`, `␣accusation`, `␣accused`, `指控`, `␣accuse`, `涉嫌` | 42/152 (28%) | 38/81 (47%) | 56/138 (41%) | 3/158 (2%) | 32/79 (41%) | 37/77 (48%) |
| deliberate (on purpose, intentionally) | unclear | `故意的`, `故意`, `␣intentionally`, `␣deliberate`, `␣intentional` | 28/152 (18%) | 36/81 (44%) | 38/138 (28%) | 143/158 (91%) | 16/79 (20%) | 36/77 (47%) |
| fact (fact, factual) | unclear | `事实`, `␣fact`, `与现实` | 45/152 (30%) | 16/81 (20%) | 39/138 (28%) | 59/158 (37%) | 29/79 (37%) | 15/77 (19%) |
| dishonest (dishonest) | lie | `␣dishonest` | 41/152 (27%) | 15/81 (19%) | 37/138 (27%) | 142/158 (90%) | 17/79 (22%) | 14/77 (18%) |
| faithful (faithful, true to the facts (忠实)) | truth | `忠实` | 16/152 (11%) | 15/81 (19%) | 51/138 (37%) | 0/158 (0%) | 8/79 (10%) | 15/77 (19%) |
| contradict (contradicting, contradiction) | unclear | `␣contradictory`, `矛盾`, `␣contrad`, `␣contradiction`, `␣contradict`, `␣contradictions`, `␣conflicting`, `␣inconsistency`, `不一致`, `␣inconsistent`, `␣inconsistencies` | 2/152 (1%) | 22/81 (27%) | 17/138 (12%) | 0/158 (0%) | 2/79 (3%) | 22/77 (29%) |
| candid (candid, upfront) | truth | `坦诚` | 18/152 (12%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 5/79 (6%) | 1/77 (1%) |
| inconsistent (inconsistent, conflicting) | unclear | `␣inconsistency`, `␣conflicting`, `不一致`, `␣inconsistent`, `␣inconsistencies` | 0/152 (0%) | 9/81 (11%) | 1/138 (1%) | 0/158 (0%) | 0/79 (0%) | 9/77 (12%) |
| violate (violating a rule, duty or law) | unclear | `违反`, `违反了` | 3/152 (2%) | 5/81 (6%) | 5/138 (4%) | 1/158 (1%) | 1/79 (1%) | 4/77 (5%) |
| transparent (transparent, transparency) | truth | `透明`, `␣transparency` | 5/152 (3%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 1/79 (1%) | 0/77 (0%) |
| fake (fake, not genuine) | lie | `␣fake` | 2/152 (1%) | 2/81 (2%) | 1/138 (1%) | 5/158 (3%) | 2/79 (3%) | 2/77 (3%) |
| confess (confessing, owning up (坦白)) | truth | `坦白` | 4/152 (3%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 1/79 (1%) | 0/77 (0%) |
| suspected (suspected of wrongdoing (涉嫌)) | unclear | `涉嫌` | 2/152 (1%) | 2/81 (2%) | 0/138 (0%) | 0/158 (0%) | 2/79 (3%) | 2/77 (3%) |
| conceal (hiding or covering up information) | lie | `隐瞒` | 1/152 (1%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 1/79 (1%) | 1/77 (1%) |
| betray (betraying, selling out) | lie | `出卖` | 1/152 (1%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 1/79 (1%) | 0/77 (0%) |
| accurate (accurate) | truth | `␣accuracy` | 0/152 (0%) | 0/81 (0%) | 0/138 (0%) | 7/158 (4%) | 0/79 (0%) | 0/77 (0%) |

Not in the draft: deny (excluded: admit / deny / acknowledge); honest (excluded: the question's own word); admit (excluded: admit / deny / acknowledge); truth (excluded: the question's own word)
