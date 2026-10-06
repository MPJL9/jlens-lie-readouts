# Draft families: qwen3.6-27b, logit lens, part Q2_after, group questionb

Written by `scripts/apply_family_decisions.py` (2026-10-01; draft, not frozen). Counts are `present / transcripts (share)`
on the build split.

## q_tok8

| family | side | members | lies | truths | no-pressure truths | unrelated | lies that deny | truths that deny |
|---|---|---|---|---|---|---|---|---|
| false (false, untrue) | lie | `␣false`, `␣False`, `false`, `False`, `.assertFalse`, `.FALSE` | 103/152 (68%) | 57/81 (70%) | 126/138 (91%) | 158/158 (100%) | 23/47 (49%) | 55/77 (71%) |
| true (true, real) | truth | `␣true`, `true`, `␣True` | 28/152 (18%) | 16/81 (20%) | 36/138 (26%) | 75/158 (47%) | 1/47 (2%) | 15/77 (19%) |
| candid (speaking frankly, being upfront) | truth | `␣upfront` | 24/152 (16%) | 8/81 (10%) | 49/138 (36%) | 73/158 (46%) | 8/47 (17%) | 6/77 (8%) |
| refuse (refusing to answer or comply) | unclear | `␣refusal` | 1/152 (1%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 0/47 (0%) | 0/77 (0%) |

## q_tok9

| family | side | members | lies | truths | no-pressure truths | unrelated | lies that deny | truths that deny |
|---|---|---|---|---|---|---|---|---|
| false (false, untrue) | lie | `␣false`, `␣False`, `false`, `=False`, `(False`, `.assertFalse`, `.false`, `/false` | 152/152 (100%) | 80/81 (99%) | 138/138 (100%) | 158/158 (100%) | 47/47 (100%) | 76/77 (99%) |
| true (true, real) | truth | `true`, `True`, `␣True`, `TRUE`, `成立` | 123/152 (81%) | 70/81 (86%) | 126/138 (91%) | 158/158 (100%) | 24/47 (51%) | 66/77 (86%) |
| candid (speaking frankly, being upfront) | truth | `␣upfront`, `␣straightforward` | 86/152 (57%) | 31/81 (38%) | 82/138 (59%) | 138/158 (87%) | 17/47 (36%) | 28/77 (36%) |
| neutral (taking no side) | unclear | `中立` | 3/152 (2%) | 31/81 (38%) | 0/138 (0%) | 0/158 (0%) | 1/47 (2%) | 31/77 (40%) |
| silent (staying silent, not speaking) | unclear | `不语` | 15/152 (10%) | 1/81 (1%) | 2/138 (1%) | 1/158 (1%) | 0/47 (0%) | 0/77 (0%) |
| kidding (joking, not being serious) | unclear | `␣kidding` | 5/152 (3%) | 2/81 (2%) | 1/138 (1%) | 0/158 (0%) | 4/47 (9%) | 2/77 (3%) |

Not in the draft: deny (excluded: admit / deny / acknowledge)

## q_tok10

| family | side | members | lies | truths | no-pressure truths | unrelated | lies that deny | truths that deny |
|---|---|---|---|---|---|---|---|---|
| honest (being honest) | truth | `诚实`, `␣honesty`, `␣honest`, `␣honestly`, `␣Honest`, `诚实守信`, `诚` | 139/152 (91%) | 66/81 (81%) | 113/138 (82%) | 89/158 (56%) | 42/47 (89%) | 64/77 (83%) |
| objective (objective, unbiased) | unclear | `客观`, `␣objectively`, `␣objective` | 128/152 (84%) | 50/81 (62%) | 93/138 (67%) | 89/158 (56%) | 33/47 (70%) | 46/77 (60%) |
| truthful (telling it as it is) | truth | `␣truthful`, `如实`, `实事求是` | 114/152 (75%) | 57/81 (70%) | 114/138 (83%) | 108/158 (68%) | 32/47 (68%) | 54/77 (70%) |
| violate (violating a rule or principle) | unclear | `违反`, `违背`, `违反了`, `␣violate`, `␣violating`, `␣violates`, `␣violations`, `␣violation`, `␣violated`, `违法`, `违规`, `违反上述` | 126/152 (83%) | 44/81 (54%) | 73/138 (53%) | 3/158 (2%) | 24/47 (51%) | 40/77 (52%) |
| deliberate (doing on purpose) | unclear | `␣intentionally`, `␣intentional`, `␣deliberately`, `␣deliberate`, `故意`, `故意的`, `刻意`, `有意`, `␣sengaja`, `␣purposely`, `明知`, `␣knowingly`, `␣knowing` | 119/152 (78%) | 26/81 (32%) | 107/138 (78%) | 36/158 (23%) | 23/47 (49%) | 23/77 (30%) |
| fact (facts, what actually is) | truth | `␣fact`, `␣facts`, `Fact`, `fact`, `␣Fact`, `␣factual`, `␣Facts`, `␣FACT`, `facts`, `FACT`, `事实`, `的事实`, `事实上`, `事实和`, `实际情况`, `␣reality`, `␣Reality`, `Reality`, `␣realities`, `实际`, `符合`, `现实`, `实际上`, `实际的`, `是否符合`, `现实中`, `的现实`, `根据实际情况`, `求实`, `与现实` | 105/152 (69%) | 38/81 (47%) | 86/138 (62%) | 53/158 (34%) | 24/47 (51%) | 34/77 (44%) |
| knowingly (acting with knowledge) | unclear | `明知`, `␣knowingly`, `␣knowing` | 115/152 (76%) | 22/81 (27%) | 107/138 (78%) | 35/158 (22%) | 22/47 (47%) | 19/77 (25%) |
| moral (morality, moral) | unclear | `␣moral`, `␣morally`, `␣morality`, `␣Moral`, `␣morals`, `道德`, `的道德`, `职业道德`, `␣ethical`, `␣ethics`, `伦理`, `ethical`, `␣Ethics`, `␣ethic` | 105/152 (69%) | 25/81 (31%) | 0/138 (0%) | 0/158 (0%) | 24/47 (51%) | 23/77 (30%) |
| hide (hiding) | lie | `隐藏`, `␣hiding`, `␣hide`, `hide`, `Hide`, `␣hidden`, `-hidden`, `␣Hidden`, `隐瞒`, `␣conceal`, `掩盖`, `掩饰`, `␣concealed`, `遮掩` | 101/152 (66%) | 23/81 (28%) | 74/138 (54%) | 0/158 (0%) | 24/47 (51%) | 20/77 (26%) |
| not conform (not conforming to) | unclear | `不符合` | 82/152 (54%) | 39/81 (48%) | 39/138 (28%) | 21/158 (13%) | 12/47 (26%) | 36/77 (47%) |
| ethics (ethics, ethical) | unclear | `␣ethical`, `ethical`, `␣ethics`, `␣Ethics`, `␣ethic`, `伦理` | 96/152 (63%) | 24/81 (30%) | 0/138 (0%) | 0/158 (0%) | 23/47 (49%) | 22/77 (29%) |
| conceal (concealing) | lie | `隐瞒`, `␣conceal`, `␣concealed`, `瞒`, `掩`, `遮`, `隐` | 97/152 (64%) | 22/81 (27%) | 71/138 (51%) | 2/158 (1%) | 23/47 (49%) | 19/77 (25%) |
| truth (the truth) | truth | `真实`, `真实的`, `的真实`, `的真实性`, `真实性`, `真實`, `求真` | 90/152 (59%) | 22/81 (27%) | 80/138 (58%) | 29/158 (18%) | 23/47 (49%) | 20/77 (26%) |
| comply (complying, adhering to rules) | unclear | `遵守`, `严格遵守`, `合规`, `␣compliance`, `␣Compliance`, `␣complying`, `␣comply`, `␣compliant`, `␣adherence`, `␣adher`, `␣adhere`, `遵循`, `遵照` | 52/152 (34%) | 54/81 (67%) | 59/138 (43%) | 0/158 (0%) | 14/47 (30%) | 52/77 (68%) |
| lie (telling a lie) | lie | `␣lie`, `␣lied`, `␣lies`, `␣Lie`, `lies`, `Lie`, `␣Lies`, `␣lying`, `lying`, `说谎`, `谎言`, `撒谎`, `谎`, `␣mentira` | 90/152 (59%) | 15/81 (19%) | 17/138 (12%) | 2/158 (1%) | 22/47 (47%) | 13/77 (17%) |
| fabricate (making something up) | lie | `虚构`, `␣fabrication`, `␣fabricated`, `伪造` | 79/152 (52%) | 23/81 (28%) | 67/138 (49%) | 42/158 (27%) | 13/47 (28%) | 21/77 (27%) |
| fiction (fiction, fictional) | unclear | `fiction`, `␣fictional`, `␣Fiction`, `␣fiction`, `-fiction`, `虚构` | 79/152 (52%) | 23/81 (28%) | 68/138 (49%) | 42/158 (27%) | 13/47 (28%) | 21/77 (27%) |
| true (true, real) | truth | `␣true`, `true`, `␣real`, `True`, `␣True`, `real`, `␣TRUE`, `␣genuine`, `.True`, `␣genuinely`, `确实`, `真正的`, `是真的`, `的真` | 67/152 (44%) | 21/81 (26%) | 78/138 (57%) | 44/158 (28%) | 24/47 (51%) | 20/77 (26%) |
| persona (an adopted persona) | unclear | `␣persona`, `␣personas`, `Persona`, `␣Persona`, `persona`, `␣personagem`, `扮演`, `␣backstory`, `角色扮演` | 58/152 (38%) | 29/81 (36%) | 33/138 (24%) | 4/158 (3%) | 12/47 (26%) | 27/77 (35%) |
| integrity (integrity, uprightness) | truth | `诚信`, `正直`, `␣integrity`, `␣Integrity` | 61/152 (40%) | 25/81 (31%) | 33/138 (24%) | 23/158 (15%) | 19/47 (40%) | 25/77 (32%) |
| role-play (playing a role) | unclear | `扮演`, `角色扮演` | 43/152 (28%) | 27/81 (33%) | 33/138 (24%) | 3/158 (2%) | 8/47 (17%) | 25/77 (32%) |
| wrong (wrong, mistaken) | lie | `error`, `␣error`, `错`, `错误`, `错了`, `是非`, `指正`, `是错误的` | 41/152 (27%) | 27/81 (33%) | 35/138 (25%) | 64/158 (41%) | 14/47 (30%) | 25/77 (32%) |
| withhold (withholding information) | lie | `␣withholding`, `␣withhold`, `␣withheld` | 44/152 (29%) | 14/81 (17%) | 19/138 (14%) | 2/158 (1%) | 5/47 (11%) | 12/77 (16%) |
| fulfill (fulfilling a duty or request) | unclear | `␣fulfill`, `␣fulfillment`, `␣fulfilled`, `␣fulfilling`, `履行`, `履行职责` | 37/152 (24%) | 15/81 (19%) | 8/138 (6%) | 12/158 (8%) | 6/47 (13%) | 14/77 (18%) |
| euphemistic (speaking tactfully, indirectly) | unclear | `委婉` | 36/152 (24%) | 15/81 (19%) | 14/138 (10%) | 5/158 (3%) | 6/47 (13%) | 15/77 (19%) |
| false (false, untrue) | lie | `␣false`, `␣False`, `false`, `␣FALSE`, `␣fals`, `.assertFalse`, `.False`, `.FALSE`, `/false`, `␣falsehood`, `假`, `虚假`, `假的`, `真假`, `虚假信息` | 39/152 (26%) | 12/81 (15%) | 76/138 (55%) | 123/158 (78%) | 13/47 (28%) | 12/77 (16%) |
| cover up (covering up, masking) | lie | `掩盖`, `掩饰`, `遮掩`, `␣masking` | 44/152 (29%) | 6/81 (7%) | 7/138 (5%) | 0/158 (0%) | 7/47 (15%) | 3/77 (4%) |
| candid (speaking frankly, being upfront) | truth | `坦诚`, `直言`, `␣straightforward` | 21/152 (14%) | 25/81 (31%) | 62/138 (45%) | 75/158 (47%) | 15/47 (32%) | 25/77 (32%) |
| candid (frank, candid) | truth | `坦诚` | 21/152 (14%) | 23/81 (28%) | 48/138 (35%) | 16/158 (10%) | 15/47 (32%) | 23/77 (30%) |
| evade (evading) | lie | `evas`, `␣evasion`, `回避` | 27/152 (18%) | 10/81 (12%) | 4/138 (3%) | 0/158 (0%) | 8/47 (17%) | 8/77 (10%) |
| refuse (refusing) | unclear | `拒绝`, `拒绝了`, `␣refusal`, `␣refusing`, `␣refuse`, `␣refused`, `␣refuses`, `␣refus` | 5/152 (3%) | 28/81 (35%) | 2/138 (1%) | 3/158 (2%) | 3/47 (6%) | 28/77 (36%) |
| faithful (faithful to the facts) | truth | `忠实` | 24/152 (16%) | 6/81 (7%) | 24/138 (17%) | 2/158 (1%) | 2/47 (4%) | 6/77 (8%) |
| unethical (unethical) | lie | `␣unethical` | 29/152 (19%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 1/47 (2%) | 1/77 (1%) |
| contradict (contradicting) | unclear | `␣contrad`, `␣contradict`, `␣contradictory`, `␣contradiction` | 15/152 (10%) | 11/81 (14%) | 20/138 (14%) | 0/158 (0%) | 3/47 (6%) | 11/77 (14%) |
| disclose (disclosing information) | truth | `信息披露`, `披露`, `␣disclosure`, `␣disclosures`, `␣Disclosure`, `␣disclose`, `␣disclosed`, `␣disclosing`, `透露` | 14/152 (9%) | 11/81 (14%) | 25/138 (18%) | 0/158 (0%) | 2/47 (4%) | 10/77 (13%) |
| reveal (revealing, exposing) | truth | `揭示了`, `揭示`, `␣reveal`, `reveal`, `␣revealing`, `揭露`, `揭` | 13/152 (9%) | 12/81 (15%) | 3/138 (2%) | 0/158 (0%) | 5/47 (11%) | 12/77 (16%) |
| accurate (accurate) | truth | `␣accur`, `␣accurate`, `␣accuracy`, `␣accurately`, `accuracy`, `accur`, `Accuracy`, `␣Accuracy`, `准确`, `准确性`, `准确的` | 15/152 (10%) | 8/81 (10%) | 56/138 (41%) | 61/158 (39%) | 8/47 (17%) | 8/77 (10%) |
| correct (correct) | truth | `␣correct`, `␣correctly`, `correct`, `␣correction`, `Correct`, `␣corrected`, `␣Correct`, `␣corrections`, `␣correctness`, `␣Correction`, `␣correcting`, `Correction`, `␣Corrections`, `正确`, `正确的`, `正确的是`, `正确答案`, `纠正`, `无误`, `是正确的` | 1/152 (1%) | 21/81 (26%) | 98/138 (71%) | 63/158 (40%) | 1/47 (2%) | 21/77 (27%) |
| transparent (transparency) | truth | `␣transparency`, `␣Transparency`, `-transparent`, `␣transparent`, `transparent`, `␣Transparent`, `透明`, `透明度`, `透明的` | 3/152 (2%) | 16/81 (20%) | 51/138 (37%) | 1/158 (1%) | 3/47 (6%) | 16/77 (21%) |
| fake (fake) | lie | `fake` | 17/152 (11%) | 1/81 (1%) | 9/138 (7%) | 3/158 (2%) | 2/47 (4%) | 0/77 (0%) |
| conscience (conscience) | unclear | `良心` | 16/152 (11%) | 2/81 (2%) | 0/138 (0%) | 0/158 (0%) | 3/47 (6%) | 2/77 (3%) |
| manipulate (manipulating) | lie | `␣manip`, `␣manipulation`, `␣manipulating` | 9/152 (6%) | 6/81 (7%) | 1/138 (1%) | 0/158 (0%) | 0/47 (0%) | 4/77 (5%) |
| dishonest (being dishonest) | lie | `␣dishonest` | 9/152 (6%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 0/47 (0%) | 0/77 (0%) |
| omit (leaving something out) | lie | `␣omit`, `omit`, `␣omission` | 6/152 (4%) | 3/81 (4%) | 1/138 (1%) | 0/158 (0%) | 2/47 (4%) | 2/77 (3%) |
| confess (confessing, coming clean) | truth | `坦白` | 3/152 (2%) | 5/81 (6%) | 4/138 (3%) | 2/158 (1%) | 2/47 (4%) | 5/77 (6%) |
| deviate (deviating from) | unclear | `偏离`, `背离` | 3/152 (2%) | 5/81 (6%) | 1/138 (1%) | 0/158 (0%) | 2/47 (4%) | 4/77 (5%) |
| mislead (misleading) | lie | `␣misleading`, `误导` | 5/152 (3%) | 2/81 (2%) | 23/138 (17%) | 8/158 (5%) | 0/47 (0%) | 1/77 (1%) |
| secret (secrecy, doing in secret) | lie | `␣secretly`, `␣secret`, `秘密`, `的秘密`, `暗中`, `␣covert` | 4/152 (3%) | 2/81 (2%) | 0/138 (0%) | 0/158 (0%) | 0/47 (0%) | 2/77 (3%) |
| silent (staying silent) | unclear | `沉默`, `␣silence` | 5/152 (3%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 4/47 (9%) | 1/77 (1%) |
| pretend (pretending) | lie | `␣pretending` | 4/152 (3%) | 0/81 (0%) | 1/138 (1%) | 2/158 (1%) | 2/47 (4%) | 0/77 (0%) |
| neutral (taking no side) | unclear | `中立` | 1/152 (1%) | 3/81 (4%) | 0/138 (0%) | 1/158 (1%) | 0/47 (0%) | 3/77 (4%) |
| avoid (avoiding) | unclear | `␣avoid`, `␣avoiding`, `␣avoided`, `avoid`, `␣avoidance` | 0/152 (0%) | 2/81 (2%) | 0/138 (0%) | 0/158 (0%) | 0/47 (0%) | 2/77 (3%) |
| unfulfilled (failing to fulfil) | unclear | `未履行` | 1/152 (1%) | 1/81 (1%) | 0/138 (0%) | 2/158 (1%) | 1/47 (2%) | 1/77 (1%) |
| fraud (fraud) | lie | `␣fraud` | 1/152 (1%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 0/47 (0%) | 0/77 (0%) |
| exaggerate (exaggerating) | lie | `夸大` | 1/152 (1%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 0/47 (0%) | 0/77 (0%) |
| impersonate (pretending to be someone) | lie | `冒充` | 1/152 (1%) | 0/81 (0%) | 4/138 (3%) | 0/158 (0%) | 0/47 (0%) | 0/77 (0%) |
| incorrect (incorrect) | lie | `␣incorrect`, `␣inaccur`, `␣Incorrect`, `错误的`, `有误` | 0/152 (0%) | 0/81 (0%) | 2/138 (1%) | 8/158 (5%) | 0/47 (0%) | 0/77 (0%) |
| inaccurate (inaccurate) | lie | `准确性和` | 0/152 (0%) | 0/81 (0%) | 16/138 (12%) | 0/158 (0%) | 0/47 (0%) | 0/77 (0%) |

Not in the draft: deny (excluded: admit / deny / acknowledge); admit (excluded: admit / deny / acknowledge); acknowledge (excluded: admit / deny / acknowledge); deceive (excluded: the question's own word)
