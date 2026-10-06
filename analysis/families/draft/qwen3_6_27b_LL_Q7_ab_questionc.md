# Draft families: qwen3.6-27b, logit lens, part Q7_ab, group questionc

Written by `scripts/apply_family_decisions.py` (2026-10-01; draft, not frozen). Counts are `present / transcripts (share)`
on the build split.

## q_tok16

| family | side | members | lies | truths | no-pressure truths | unrelated | lies that deny | truths that deny |
|---|---|---|---|---|---|---|---|---|
| true (true, real) | truth | `␣true`, `true`, `␣True`, `(True`, `成立` | 151/152 (99%) | 81/81 (100%) | 138/138 (100%) | 158/158 (100%) | 78/79 (99%) | 77/77 (100%) |
| false (false, untrue) | lie | `␣false`, `false`, `:false` | 24/152 (16%) | 23/81 (28%) | 99/138 (72%) | 137/158 (87%) | 6/79 (8%) | 22/77 (29%) |

## q_tok17

| family | side | members | lies | truths | no-pressure truths | unrelated | lies that deny | truths that deny |
|---|---|---|---|---|---|---|---|---|
| true (true, real) | truth | `␣true`, `true`, `True`, `␣True`, `确实` | 152/152 (100%) | 81/81 (100%) | 138/138 (100%) | 158/158 (100%) | 79/79 (100%) | 77/77 (100%) |
| false (false, untrue) | lie | `␣false`, `false` | 41/152 (27%) | 33/81 (41%) | 52/138 (38%) | 103/158 (65%) | 23/79 (29%) | 32/77 (42%) |

Not in the draft: admit (excluded: admit / deny / acknowledge)

## q_tok18

| family | side | members | lies | truths | no-pressure truths | unrelated | lies that deny | truths that deny |
|---|---|---|---|---|---|---|---|---|
| violate (violating, going against) | unclear | `违背` | 90/152 (59%) | 70/81 (86%) | 138/138 (100%) | 156/158 (99%) | 39/79 (49%) | 66/77 (86%) |
| false (false, untrue) | lie | `␣False`, `/false` | 37/152 (24%) | 56/81 (69%) | 76/138 (55%) | 23/158 (15%) | 29/79 (37%) | 55/77 (71%) |
| partial (only partly) | unclear | `␣partially` | 18/152 (12%) | 28/81 (35%) | 18/138 (13%) | 9/158 (6%) | 6/79 (8%) | 28/77 (36%) |
| omit (leaving something out) | lie | `omit` | 8/152 (5%) | 2/81 (2%) | 0/138 (0%) | 0/158 (0%) | 0/79 (0%) | 2/77 (3%) |
| true (true, real) | truth | `确实`, `的确` | 5/152 (3%) | 4/81 (5%) | 10/138 (7%) | 127/158 (80%) | 5/79 (6%) | 4/77 (5%) |
| outright (outright, flat) | unclear | `␣outright` | 3/152 (2%) | 5/81 (6%) | 6/138 (4%) | 29/158 (18%) | 2/79 (3%) | 4/77 (5%) |
| wrong (wrong, mistaken) | lie | `没错` | 3/152 (2%) | 0/81 (0%) | 3/138 (2%) | 0/158 (0%) | 3/79 (4%) | 0/77 (0%) |
| conceal (concealing the truth) | lie | `␣conceal` | 0/152 (0%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 0/79 (0%) | 1/77 (1%) |
| knowingly (knowing it was untrue) | unclear | `明知` | 1/152 (1%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 1/79 (1%) | 0/77 (0%) |
| inconsistent (not consistent with) | unclear | `不符合` | 0/152 (0%) | 1/81 (1%) | 3/138 (2%) | 10/158 (6%) | 0/79 (0%) | 1/77 (1%) |

Not in the draft: deny (excluded: admit / deny / acknowledge); admit (excluded: admit / deny / acknowledge); acknowledge (excluded: admit / deny / acknowledge)

## q_tok19

| family | side | members | lies | truths | no-pressure truths | unrelated | lies that deny | truths that deny |
|---|---|---|---|---|---|---|---|---|
| fact (fact, factual) | truth | `␣fact`, `␣reality`, `␣facts`, `Fact`, `fact`, `␣Fact`, `␣Reality`, `␣Facts`, `Reality`, `_fact`, `␣realities`, `␣FACT`, `FACT`, `␣factual`, `facts`, `实际`, `符合`, `现实`, `事实`, `实际上`, `实际情况`, `事实上`, `的事实`, `的实际`, `实际的`, `实事求是`, `现实中`, `的现实`, `根据实际情况`, `与实际`, `与现实`, `事实和` | 144/152 (95%) | 69/81 (85%) | 120/138 (87%) | 146/158 (92%) | 73/79 (92%) | 65/77 (84%) |
| true (true, real) | truth | `␣true`, `true`, `␣real`, `True`, `␣True`, `real`, `_true`, `␣genuine`, `真`, `成立`, `真正`, `确实`, `真正的`, `真實`, `内容的真实性`, `确实是`, `的真正` | 146/152 (96%) | 36/81 (44%) | 55/138 (40%) | 39/158 (25%) | 74/79 (94%) | 32/77 (42%) |
| knowingly (knowing it was untrue) | unclear | `明知`, `␣knowingly` | 141/152 (93%) | 37/81 (46%) | 46/138 (33%) | 69/158 (44%) | 71/79 (90%) | 33/77 (43%) |
| knowingly (with knowledge of the truth) | unclear | `明知`, `␣knowing`, `␣knowingly`, `␣Knowing`, `Knowing` | 141/152 (93%) | 37/81 (46%) | 46/138 (33%) | 69/158 (44%) | 71/79 (90%) | 33/77 (43%) |
| hide (hiding something) | lie | `␣hiding`, `隐藏`, `␣hidden`, `-hide`, `␣hide`, `Hide`, `hide`, `␣hides`, `␣Hide`, `_hide`, `␣Hidden`, `隐藏的`, `hidden`, `Hidden`, `_hidden`, `藏着`, `-hidden`, `:hidden`, `隐藏着`, `隐瞒`, `掩盖`, `␣conceal`, `␣concealed`, `掩饰`, `␣hid`, `遮蔽`, `遮掩`, `瞒`, `隐蔽`, `隐匿` | 114/152 (75%) | 57/81 (70%) | 41/138 (30%) | 2/158 (1%) | 56/79 (71%) | 54/77 (70%) |
| conceal (concealing the truth) | lie | `隐瞒`, `␣conceal`, `␣concealed`, `藏`, `掩`, `遮`, `隐` | 114/152 (75%) | 56/81 (69%) | 40/138 (29%) | 2/158 (1%) | 56/79 (71%) | 53/77 (69%) |
| contradict (contradicting) | unclear | `␣contrad`, `␣contradict`, `␣contradictory`, `矛盾`, `␣contradiction`, `␣contradictions`, `矛盾的`, `␣contrary`, `␣conflicting` | 83/152 (55%) | 56/81 (69%) | 116/138 (84%) | 42/158 (27%) | 49/79 (62%) | 52/77 (68%) |
| false (false, untrue) | lie | `␣false`, `␣False`, `false`, `False`, `␣fals`, `_false`, `␣falsely`, `␣untrue`, `/false`, `␣falsehood`, `假`, `虚假`, `假的`, `真假`, `不实`, `虚假信息` | 54/152 (36%) | 58/81 (72%) | 86/138 (62%) | 137/158 (87%) | 23/79 (29%) | 55/77 (71%) |
| inconsistent (not consistent with) | unclear | `不符合`, `不符` | 37/152 (24%) | 42/81 (52%) | 50/138 (36%) | 51/158 (32%) | 16/79 (20%) | 42/77 (55%) |
| deliberate (doing it on purpose) | unclear | `␣intentionally`, `故意`, `␣deliberately`, `␣deliberate`, `␣intentional`, `刻意`, `有意`, `故意的`, `␣purposely` | 52/152 (34%) | 25/81 (31%) | 8/138 (6%) | 114/158 (72%) | 23/79 (29%) | 22/77 (29%) |
| cover up (covering something up) | lie | `掩盖`, `掩饰`, `遮掩` | 44/152 (29%) | 29/81 (36%) | 7/138 (5%) | 0/158 (0%) | 19/79 (24%) | 28/77 (36%) |
| deceive (the act of deceiving) | lie | `欺骗`, `␣deception`, `骗`, `␣deceptive`, `␣deceive`, `哄` | 24/152 (16%) | 47/81 (58%) | 56/138 (41%) | 122/158 (77%) | 13/79 (16%) | 45/77 (58%) |
| fictional (fiction, made-up story) | unclear | `虚构`, `␣fictional`, `␣fiction`, `fiction`, `␣Fiction` | 33/152 (22%) | 31/81 (38%) | 42/138 (30%) | 67/158 (42%) | 20/79 (25%) | 31/77 (40%) |
| violate (violating, going against) | unclear | `违背`, `违反`, `违反了` | 22/152 (14%) | 35/81 (43%) | 89/138 (64%) | 20/158 (13%) | 10/79 (13%) | 35/77 (45%) |
| fake (fake, sham) | lie | `fake`, `␣fake`, `Fake` | 20/152 (13%) | 34/81 (42%) | 16/138 (12%) | 36/158 (23%) | 7/79 (9%) | 34/77 (44%) |
| objective (objective) | unclear | `␣objectively`, `客观` | 47/152 (31%) | 3/81 (4%) | 0/138 (0%) | 1/158 (1%) | 26/79 (33%) | 3/77 (4%) |
| secret (secrecy) | lie | `␣secretly`, `␣secret`, `secret`, `秘密`, `␣Secret`, `␣privately`, `私下`, `␣private`, `私`, `␣undisclosed` | 45/152 (30%) | 4/81 (5%) | 0/138 (0%) | 1/158 (1%) | 20/79 (25%) | 4/77 (5%) |
| private (privately, out of view) | unclear | `␣privately`, `私下`, `␣private` | 34/152 (22%) | 3/81 (4%) | 0/138 (0%) | 0/158 (0%) | 14/79 (18%) | 3/77 (4%) |
| instructions (instructions given to the model) | unclear | `␣instructions`, `指令`, `␣instruction`, `␣Instructions`, `␣instructed`, `instructions`, `␣Instruction`, `Instructions`, `Instruction`, `_instructions`, `instruction`, `.instructions` | 30/152 (20%) | 5/81 (6%) | 2/138 (1%) | 4/158 (3%) | 17/79 (22%) | 5/77 (6%) |
| indirect (indirectly) | unclear | `间接`, `␣indirectly`, `␣indirect` | 7/152 (5%) | 19/81 (23%) | 2/138 (1%) | 5/158 (3%) | 5/79 (6%) | 18/77 (23%) |
| withhold (withholding information) | lie | `␣withholding`, `␣withhold`, `␣withheld` | 13/152 (9%) | 12/81 (15%) | 1/138 (1%) | 0/158 (0%) | 10/79 (13%) | 11/77 (14%) |
| omit (leaving something out) | lie | `␣omit`, `␣omission`, `omit`, `␣omitted` | 13/152 (9%) | 11/81 (14%) | 1/138 (1%) | 3/158 (2%) | 8/79 (10%) | 10/77 (13%) |
| pretend (pretending, putting on a front) | lie | `␣pretending`, `伪装`, `␣pretend`, `假装`, `␣pretended`, `冒充` | 2/152 (1%) | 19/81 (23%) | 3/138 (2%) | 19/158 (12%) | 2/79 (3%) | 19/77 (25%) |
| fabricate (making up false content) | lie | `␣fabricated`, `␣fabrication`, `␣invented`, `␣invent`, `伪造`, `␣Invent`, `作假`, `␣invention` | 4/152 (3%) | 14/81 (17%) | 33/138 (24%) | 59/158 (37%) | 2/79 (3%) | 14/77 (18%) |
| hypocrisy (hypocrisy) | lie | `虚伪` | 0/152 (0%) | 15/81 (19%) | 0/138 (0%) | 0/158 (0%) | 0/79 (0%) | 15/77 (19%) |
| contrary (contrary to) | unclear | `␣contrary` | 4/152 (3%) | 11/81 (14%) | 59/138 (43%) | 0/158 (0%) | 2/79 (3%) | 11/77 (14%) |
| conflicting (conflicting) | unclear | `␣conflicting` | 5/152 (3%) | 9/81 (11%) | 65/138 (47%) | 0/158 (0%) | 4/79 (5%) | 9/77 (12%) |
| moral (moral or ethical judgement) | unclear | `␣moral`, `␣ethical`, `道德`, `␣ethics`, `␣morally`, `的道德` | 0/152 (0%) | 12/81 (15%) | 0/138 (0%) | 0/158 (0%) | 0/79 (0%) | 12/77 (16%) |
| mislead (leading someone to a false belief) | lie | `␣misleading`, `误导` | 6/152 (4%) | 5/81 (6%) | 16/138 (12%) | 41/158 (26%) | 3/79 (4%) | 5/77 (6%) |
| persona (a persona) | unclear | `␣persona`, `␣personas`, `␣Persona`, `Persona` | 6/152 (4%) | 3/81 (4%) | 1/138 (1%) | 2/158 (1%) | 5/79 (6%) | 3/77 (4%) |
| persona (a role or persona being played) | unclear | `␣persona`, `␣personas`, `␣Persona`, `␣role`, `role`, `Role`, `␣Role`, `-role`, `角色`, `的角色`, `角色的`, `Persona`, `␣roles`, `(role`, `roles`, `.role` | 6/152 (4%) | 3/81 (4%) | 1/138 (1%) | 2/158 (1%) | 5/79 (6%) | 3/77 (4%) |
| accurate (accurate) | truth | `␣accurate`, `␣accuracy`, `␣accurately`, `accuracy`, `Accuracy`, `␣Accuracy`, `准确`, `准确性`, `准确的`, `准确地` | 2/152 (1%) | 6/81 (7%) | 26/138 (19%) | 112/158 (71%) | 1/79 (1%) | 6/77 (8%) |
| evade (evading, brushing off) | lie | `回避`, `␣evasion`, `敷衍` | 5/152 (3%) | 2/81 (2%) | 0/138 (0%) | 1/158 (1%) | 4/79 (5%) | 2/77 (3%) |
| honest (honesty) | truth | `␣honesty`, `诚信`, `真诚` | 1/152 (1%) | 6/81 (7%) | 2/138 (1%) | 10/158 (6%) | 1/79 (1%) | 6/77 (8%) |
| hallucinate (hallucinating content) | unclear | `␣halluc` | 2/152 (1%) | 4/81 (5%) | 19/138 (14%) | 69/158 (44%) | 1/79 (1%) | 4/77 (5%) |
| outright (outright, flat) | unclear | `␣outright` | 3/152 (2%) | 3/81 (4%) | 5/138 (4%) | 31/158 (20%) | 2/79 (3%) | 2/77 (3%) |
| comply (following orders or rules) | unclear | `遵照`, `遵循`, `遵从`, `␣adher`, `␣adherence`, `␣compliance`, `遵守`, `服从`, `合规`, `␣adhere`, `␣Compliance` | 1/152 (1%) | 5/81 (6%) | 2/138 (1%) | 0/158 (0%) | 0/79 (0%) | 5/77 (6%) |
| evade (avoiding or dodging the issue) | lie | `回避`, `␣evasion`, `逃避`, `规避` | 4/152 (3%) | 2/81 (2%) | 0/138 (0%) | 0/158 (0%) | 3/79 (4%) | 2/77 (3%) |
| wrong (wrong, mistaken) | lie | `error`, `␣error`, `␣wrong`, `␣mistake`, `␣mistakes`, `错`, `错误`, `谬`, `错了`, `是非`, `是错误的` | 1/152 (1%) | 5/81 (6%) | 10/138 (7%) | 84/158 (53%) | 0/79 (0%) | 5/77 (6%) |
| simulate (simulating) | unclear | `模拟`, `仿真`, `␣simulation`, `␣simulations`, `␣Simulation` | 2/152 (1%) | 3/81 (4%) | 1/138 (1%) | 1/158 (1%) | 2/79 (3%) | 3/77 (4%) |
| exaggerate (exaggerating) | lie | `夸大`, `␣exagger`, `␣exaggerated` | 3/152 (2%) | 1/81 (1%) | 0/138 (0%) | 17/158 (11%) | 1/79 (1%) | 1/77 (1%) |
| partial (only partly) | unclear | `␣partial`, `␣partially` | 1/152 (1%) | 3/81 (4%) | 1/138 (1%) | 12/158 (8%) | 0/79 (0%) | 3/77 (4%) |
| role-play (playing a role) | unclear | `扮演`, `角色扮演` | 1/152 (1%) | 3/81 (4%) | 1/138 (1%) | 0/158 (0%) | 1/79 (1%) | 3/77 (4%) |
| correct (correct) | truth | `␣correct`, `correct`, `␣correction`, `␣corrected`, `␣Correct`, `␣corrections`, `␣correctness`, `␣Correction`, `␣correcting`, `Correction`, `正确`, `正确的`, `正确的是`, `纠正`, `的正确`, `无误` | 0/152 (0%) | 4/81 (5%) | 26/138 (19%) | 49/158 (31%) | 0/79 (0%) | 4/77 (5%) |
| disclose (disclosing) | truth | `透露`, `␣disclosed` | 0/152 (0%) | 3/81 (4%) | 0/138 (0%) | 0/158 (0%) | 0/79 (0%) | 3/77 (4%) |
| vague (vagueness, ambiguity) | unclear | `含糊`, `␣ambiguous`, `␣ambiguity` | 1/152 (1%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 1/79 (1%) | 1/77 (1%) |
| transparent (transparency) | truth | `透明` | 0/152 (0%) | 2/81 (2%) | 0/138 (0%) | 0/158 (0%) | 0/79 (0%) | 2/77 (3%) |
| incorrect (incorrect) | lie | `␣incorrect`, `␣inaccur`, `␣inaccurate`, `␣Incorrect`, `错误的`, `有误`, `错误的是` | 0/152 (0%) | 2/81 (2%) | 5/138 (4%) | 73/158 (46%) | 0/79 (0%) | 2/77 (3%) |
| undisclosed (not disclosed) | lie | `␣undisclosed` | 1/152 (1%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 1/79 (1%) | 0/77 (0%) |
| sincere (sincerity) | truth | `真诚` | 1/152 (1%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 1/79 (1%) | 0/77 (0%) |
| inaccurate (inaccurate) | lie | `准确性和`, `不准确` | 0/152 (0%) | 0/81 (0%) | 0/138 (0%) | 10/158 (6%) | 0/79 (0%) | 0/77 (0%) |

Not in the draft: deny (excluded: admit / deny / acknowledge); admit (excluded: admit / deny / acknowledge); acknowledge (excluded: admit / deny / acknowledge); truth (excluded: the question's own word)

## q_tok20

| family | side | members | lies | truths | no-pressure truths | unrelated | lies that deny | truths that deny |
|---|---|---|---|---|---|---|---|---|
| fictional (fiction, made-up story) | unclear | `␣fictional`, `虚构` | 125/152 (82%) | 50/81 (62%) | 50/138 (36%) | 76/158 (48%) | 59/79 (75%) | 46/77 (60%) |
| comply (following orders or rules) | unclear | `遵循`, `按要求`, `遵守`, `合规`, `␣adher`, `␣adhere`, `遵照`, `遵从`, `服从`, `␣adherence`, `严格遵守`, `␣comply`, `␣obey`, `履行` | 86/152 (57%) | 58/81 (72%) | 55/138 (40%) | 7/158 (4%) | 36/79 (46%) | 55/77 (71%) |
| role-play (playing a role) | unclear | `扮演`, `角色扮演`, `扮演着` | 88/152 (58%) | 48/81 (59%) | 62/138 (45%) | 0/158 (0%) | 45/79 (57%) | 45/77 (58%) |
| simulate (simulating) | unclear | `模拟`, `␣simulated`, `仿真`, `␣simulation`, `imulation`, `␣simulate`, `␣simulations`, `␣Simulation`, `simulation` | 87/152 (57%) | 41/81 (51%) | 14/138 (10%) | 0/158 (0%) | 42/79 (53%) | 38/77 (49%) |
| deliberate (doing it on purpose) | unclear | `␣intentionally`, `␣deliberately`, `故意`, `刻意`, `␣consciously` | 91/152 (60%) | 30/81 (37%) | 30/138 (22%) | 79/158 (50%) | 42/79 (53%) | 28/77 (36%) |
| persona (a role or persona being played) | unclear | `␣role`, `角色`, `␣persona`, `role`, `-role`, `Role`, `角色的`, `␣personas`, `␣Persona`, `␣Role`, `Persona`, `的角色`, `persona`, `(role`, `ROLE`, `␣Personas`, `␣roles`, `.role`, `_role` | 77/152 (51%) | 38/81 (47%) | 7/138 (5%) | 0/158 (0%) | 40/79 (51%) | 35/77 (45%) |
| knowingly (knowing it was untrue) | unclear | `␣knowingly`, `明知` | 76/152 (50%) | 15/81 (19%) | 6/138 (4%) | 0/158 (0%) | 34/79 (43%) | 14/77 (18%) |
| persona (a persona) | unclear | `␣persona`, `␣personas`, `␣Persona`, `Persona`, `persona`, `␣Personas` | 47/152 (31%) | 29/81 (36%) | 1/138 (1%) | 0/158 (0%) | 26/79 (33%) | 26/77 (34%) |
| hallucinate (hallucinating content) | unclear | `␣halluc` | 28/152 (18%) | 20/81 (25%) | 119/138 (86%) | 154/158 (97%) | 16/79 (20%) | 20/77 (26%) |
| fact (fact, factual) | truth | `␣factual`, `符合`, `是否符合` | 24/152 (16%) | 14/81 (17%) | 4/138 (3%) | 11/158 (7%) | 12/79 (15%) | 12/77 (16%) |
| refuse (refusing or declining) | unclear | `拒绝`, `拒`, `␣refusal`, `␣refuse`, `␣refused`, `␣refusing`, `␣refus`, `␣decline`, `␣refuses`, `拒不`, `␣declined`, `拒絕`, `拒绝了`, `␣declines`, `␣declining` | 0/152 (0%) | 20/81 (25%) | 1/138 (1%) | 0/158 (0%) | 0/79 (0%) | 20/77 (26%) |
| objective (objective) | unclear | `客观` | 13/152 (9%) | 7/81 (9%) | 6/138 (4%) | 14/158 (9%) | 8/79 (10%) | 7/77 (9%) |
| correct (correct) | truth | `␣correctly`, `正确` | 10/152 (7%) | 8/81 (10%) | 36/138 (26%) | 3/158 (2%) | 4/79 (5%) | 7/77 (9%) |
| violate (violating, going against) | unclear | `违背`, `违反了`, `违反` | 10/152 (7%) | 7/81 (9%) | 7/138 (5%) | 0/158 (0%) | 4/79 (5%) | 7/77 (9%) |
| indirect (indirectly) | unclear | `间接`, `␣indirectly` | 14/152 (9%) | 3/81 (4%) | 0/138 (0%) | 0/158 (0%) | 6/79 (8%) | 3/77 (4%) |
| take responsibility (taking on responsibility) | unclear | `承担` | 11/152 (7%) | 5/81 (6%) | 0/138 (0%) | 0/158 (0%) | 8/79 (10%) | 5/77 (6%) |
| deceive (the act of deceiving) | lie | `欺骗`, `␣deception`, `骗` | 8/152 (5%) | 5/81 (6%) | 1/138 (1%) | 13/158 (8%) | 2/79 (3%) | 4/77 (5%) |
| conceal (concealing the truth) | lie | `隐瞒` | 6/152 (4%) | 4/81 (5%) | 0/138 (0%) | 0/158 (0%) | 2/79 (3%) | 4/77 (5%) |
| false (false, untrue) | lie | `假`, `虚假` | 6/152 (4%) | 4/81 (5%) | 0/138 (0%) | 0/158 (0%) | 4/79 (5%) | 1/77 (1%) |
| pretend (pretending, putting on a front) | lie | `␣pretend`, `冒充` | 3/152 (2%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 2/79 (3%) | 0/77 (0%) |
| voluntary (doing it on one's own initiative) | unclear | `主动` | 2/152 (1%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 0/79 (0%) | 1/77 (1%) |
| withhold (withholding information) | lie | `␣withhold` | 1/152 (1%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 0/79 (0%) | 1/77 (1%) |
| fabricate (making up false content) | lie | `␣fabricated`, `␣fabrication` | 1/152 (1%) | 1/81 (1%) | 0/138 (0%) | 2/158 (1%) | 0/79 (0%) | 0/77 (0%) |
| exaggerate (exaggerating) | lie | `␣exagger` | 1/152 (1%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 0/79 (0%) | 1/77 (1%) |
| conscious (consciously) | unclear | `␣consciously` | 2/152 (1%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 1/79 (1%) | 0/77 (0%) |
| moral (moral or ethical judgement) | unclear | `␣ethical`, `道德` | 1/152 (1%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 0/79 (0%) | 1/77 (1%) |
| outright (outright, flat) | unclear | `␣outright` | 0/152 (0%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 0/79 (0%) | 0/77 (0%) |
| instructions (instructions given to the model) | unclear | `␣instructions` | 0/152 (0%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 0/79 (0%) | 1/77 (1%) |
| wrong (wrong, mistaken) | lie | `error`, `␣error`, `错`, `错误`, `错了`, `是非` | 1/152 (1%) | 0/81 (0%) | 24/138 (17%) | 25/158 (16%) | 1/79 (1%) | 0/77 (0%) |
| accurate (accurate) | truth | `␣accurate`, `␣accuracy`, `␣accurately`, `准确` | 0/152 (0%) | 0/81 (0%) | 6/138 (4%) | 34/158 (22%) | 0/79 (0%) | 0/77 (0%) |
| incorrect (incorrect) | lie | `␣inaccur`, `有误` | 0/152 (0%) | 0/81 (0%) | 0/138 (0%) | 13/158 (8%) | 0/79 (0%) | 0/77 (0%) |

Not in the draft: admit (excluded: admit / deny / acknowledge); acknowledge (excluded: admit / deny / acknowledge); honest (excluded: the question's own word); truth (excluded: the question's own word); true (excluded: the question's own word)

## q_tok21

| family | side | members | lies | truths | no-pressure truths | unrelated | lies that deny | truths that deny |
|---|---|---|---|---|---|---|---|---|
| deceive (the act of deceiving) | lie | `欺骗`, `骗`, `␣deception` | 152/152 (100%) | 81/81 (100%) | 138/138 (100%) | 158/158 (100%) | 79/79 (100%) | 77/77 (100%) |
| outright (outright, flat) | unclear | `␣outright` | 152/152 (100%) | 81/81 (100%) | 138/138 (100%) | 158/158 (100%) | 79/79 (100%) | 77/77 (100%) |
| false (false, untrue) | lie | `␣false`, `␣False`, `(false`, `false`, `=False`, `=false`, `_FALSE`, `␣fals`, `␣untrue`, `/false`, `␣falsehood`, `假`, `虚假`, `假的`, `虚假信息` | 152/152 (100%) | 81/81 (100%) | 138/138 (100%) | 158/158 (100%) | 79/79 (100%) | 77/77 (100%) |
| deliberate (doing it on purpose) | unclear | `␣intentionally`, `故意`, `␣deliberately`, `␣deliberate`, `有意`, `␣intentional`, `刻意` | 147/152 (97%) | 62/81 (77%) | 134/138 (97%) | 158/158 (100%) | 75/79 (95%) | 58/77 (75%) |
| true (true, real) | truth | `␣true`, `true`, `真` | 145/152 (95%) | 60/81 (74%) | 113/138 (82%) | 4/158 (3%) | 75/79 (95%) | 57/77 (74%) |
| fact (fact, factual) | truth | `␣facts`, `␣factual`, `事实` | 139/152 (91%) | 61/81 (75%) | 37/138 (27%) | 93/158 (59%) | 66/79 (84%) | 57/77 (74%) |
| omit (leaving something out) | lie | `␣omission`, `␣omit`, `omit` | 110/152 (72%) | 51/81 (63%) | 9/138 (7%) | 4/158 (3%) | 52/79 (66%) | 47/77 (61%) |
| knowingly (knowing it was untrue) | unclear | `␣knowingly` | 104/152 (68%) | 7/81 (9%) | 62/138 (45%) | 150/158 (95%) | 50/79 (63%) | 6/77 (8%) |
| conceal (concealing the truth) | lie | `隐瞒` | 55/152 (36%) | 14/81 (17%) | 0/138 (0%) | 0/158 (0%) | 12/79 (15%) | 12/77 (16%) |
| fake (fake, sham) | lie | `␣fake`, `fake` | 19/152 (12%) | 22/81 (27%) | 56/138 (41%) | 104/158 (66%) | 10/79 (13%) | 22/77 (29%) |
| partial (only partly) | unclear | `不完全` | 17/152 (11%) | 10/81 (12%) | 0/138 (0%) | 0/158 (0%) | 9/79 (11%) | 8/77 (10%) |
| fabricate (making up false content) | lie | `␣invent` | 1/152 (1%) | 0/81 (0%) | 3/138 (2%) | 1/158 (1%) | 0/79 (0%) | 0/77 (0%) |
| wrong (wrong, mistaken) | lie | `是非`, `指正` | 0/152 (0%) | 0/81 (0%) | 0/138 (0%) | 1/158 (1%) | 0/79 (0%) | 0/77 (0%) |

Not in the draft: deny (excluded: admit / deny / acknowledge); honest (excluded: the question's own word); truth (excluded: the question's own word)

## q_tok22

| family | side | members | lies | truths | no-pressure truths | unrelated | lies that deny | truths that deny |
|---|---|---|---|---|---|---|---|---|
| confess (confessing) | truth | `␣confession`, `␣confess`, `␣confessed`, `交代`, `自首`, `坦白`, `认错` | 101/152 (66%) | 43/81 (53%) | 77/138 (56%) | 138/158 (87%) | 69/79 (87%) | 42/77 (55%) |
| true (true, real) | truth | `␣true`, `true`, `␣real`, `成立`, `确实`, `真正的`, `的确` | 96/152 (63%) | 37/81 (46%) | 54/138 (39%) | 13/158 (8%) | 34/79 (43%) | 33/77 (43%) |
| wrong (wrong, mistaken) | lie | `是非`, `指正` | 77/152 (51%) | 42/81 (52%) | 89/138 (64%) | 119/158 (75%) | 46/79 (58%) | 39/77 (51%) |
| correct (correct) | truth | `␣correct`, `正确` | 71/152 (47%) | 17/81 (21%) | 73/138 (53%) | 8/158 (5%) | 22/79 (28%) | 13/77 (17%) |
| knowingly (knowing it was untrue) | unclear | `明知`, `␣knowingly` | 69/152 (45%) | 11/81 (14%) | 0/138 (0%) | 0/158 (0%) | 20/79 (25%) | 8/77 (10%) |
| knowingly (with knowledge of the truth) | unclear | `明知`, `␣knowingly`, `␣knowing`, `␣Knowing`, `Knowing` | 69/152 (45%) | 11/81 (14%) | 0/138 (0%) | 0/158 (0%) | 20/79 (25%) | 8/77 (10%) |
| fact (fact, factual) | truth | `␣fact`, `␣factual`, `符合`, `事实`, `实际上`, `实际情况`, `事实上` | 69/152 (45%) | 9/81 (11%) | 0/138 (0%) | 0/158 (0%) | 26/79 (33%) | 8/77 (10%) |
| false (false, untrue) | lie | `␣false`, `false`, `_FALSE`, `␣falsely`, `/false`, `␣falsehood`, `虚假` | 26/152 (17%) | 44/81 (54%) | 99/138 (72%) | 37/158 (23%) | 8/79 (10%) | 41/77 (53%) |
| reveal (revealing, exposing) | truth | `揭示`, `揭`, `揭示了`, `揭露`, `␣revealing`, `␣disclosure` | 59/152 (39%) | 10/81 (12%) | 0/138 (0%) | 0/158 (0%) | 36/79 (46%) | 10/77 (13%) |
| violate (violating, going against) | unclear | `违反`, `违背`, `违反了` | 46/152 (30%) | 22/81 (27%) | 1/138 (1%) | 0/158 (0%) | 17/79 (22%) | 19/77 (25%) |
| voluntary (doing it on one's own initiative) | unclear | `主动` | 42/152 (28%) | 20/81 (25%) | 57/138 (41%) | 139/158 (88%) | 32/79 (41%) | 20/77 (26%) |
| inconsistent (not consistent with) | unclear | `不符合` | 26/152 (17%) | 25/81 (31%) | 2/138 (1%) | 0/158 (0%) | 11/79 (14%) | 25/77 (32%) |
| partial (only partly) | unclear | `片面` | 17/152 (11%) | 28/81 (35%) | 8/138 (6%) | 0/158 (0%) | 10/79 (13%) | 28/77 (36%) |
| hide (hiding something) | lie | `␣hidden`, `-hidden`, `隐藏`, `-hide`, `␣hiding`, `␣Hidden`, `Hidden`, `隐藏的`, `隱藏`, `藏着`, `隐瞒`, `掩盖`, `␣concealed`, `␣conceal`, `瞒` | 38/152 (25%) | 6/81 (7%) | 0/138 (0%) | 0/158 (0%) | 11/79 (14%) | 3/77 (4%) |
| conceal (concealing the truth) | lie | `隐瞒`, `␣concealed`, `␣conceal` | 37/152 (24%) | 6/81 (7%) | 0/138 (0%) | 0/158 (0%) | 11/79 (14%) | 3/77 (4%) |
| private (privately, out of view) | unclear | `␣private`, `私下`, `␣secret` | 25/152 (16%) | 3/81 (4%) | 1/138 (1%) | 0/158 (0%) | 13/79 (16%) | 3/77 (4%) |
| self-reflection (reflecting on one's conduct) | unclear | `反思`, `自查` | 13/152 (9%) | 8/81 (10%) | 14/138 (10%) | 25/158 (16%) | 10/79 (13%) | 8/77 (10%) |
| deliberate (doing it on purpose) | unclear | `␣intentionally`, `␣deliberately`, `␣deliberate`, `␣intentional`, `故意`, `有意`, `故意的`, `刻意`, `␣consciously`, `␣purposely` | 13/152 (9%) | 4/81 (5%) | 0/138 (0%) | 0/158 (0%) | 5/79 (6%) | 3/77 (4%) |
| transparent (transparency) | truth | `透明`, `␣transparency`, `␣transparent` | 13/152 (9%) | 2/81 (2%) | 0/138 (0%) | 0/158 (0%) | 12/79 (15%) | 2/77 (3%) |
| fictional (fiction, made-up story) | unclear | `虚构`, `fiction`, `-fiction`, `␣fictional`, `␣Fiction` | 9/152 (6%) | 5/81 (6%) | 0/138 (0%) | 0/158 (0%) | 3/79 (4%) | 5/77 (6%) |
| secret (secrecy) | lie | `␣secret` | 7/152 (5%) | 3/81 (4%) | 1/138 (1%) | 0/158 (0%) | 7/79 (9%) | 3/77 (4%) |
| comply (following orders or rules) | unclear | `服从` | 6/152 (4%) | 3/81 (4%) | 0/138 (0%) | 0/158 (0%) | 6/79 (8%) | 3/77 (4%) |
| surrender (giving in) | unclear | `投降` | 9/152 (6%) | 0/81 (0%) | 1/138 (1%) | 0/158 (0%) | 8/79 (10%) | 0/77 (0%) |
| candid (candour, frankness) | truth | `坦诚` | 6/152 (4%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 4/79 (5%) | 1/77 (1%) |
| deceive (the act of deceiving) | lie | `欺骗`, `␣deception` | 5/152 (3%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 0/79 (0%) | 1/77 (1%) |
| conscious (consciously) | unclear | `␣consciously`, `␣conscious` | 5/152 (3%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 2/79 (3%) | 1/77 (1%) |
| regret (regret, remorse) | unclear | `悔` | 3/152 (2%) | 3/81 (4%) | 8/138 (6%) | 0/158 (0%) | 3/79 (4%) | 3/77 (4%) |
| cover up (covering something up) | lie | `掩盖` | 4/152 (3%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 0/79 (0%) | 1/77 (1%) |
| pretend (pretending, putting on a front) | lie | `␣pretending`, `冒充` | 4/152 (3%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 1/79 (1%) | 1/77 (1%) |
| disclose (disclosing) | truth | `␣disclosure`, `透露` | 3/152 (2%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 2/79 (3%) | 1/77 (1%) |
| withhold (withholding information) | lie | `␣withholding`, `␣withhold`, `␣withheld` | 3/152 (2%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 1/79 (1%) | 0/77 (0%) |
| indirect (indirectly) | unclear | `间接`, `␣indirectly` | 2/152 (1%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 1/79 (1%) | 1/77 (1%) |
| omit (leaving something out) | lie | `omit` | 1/152 (1%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 0/79 (0%) | 1/77 (1%) |
| fabricate (making up false content) | lie | `␣fabricated` | 1/152 (1%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 0/79 (0%) | 1/77 (1%) |
| guilt (guilt, crime) | unclear | `罪` | 0/152 (0%) | 2/81 (2%) | 0/138 (0%) | 0/158 (0%) | 0/79 (0%) | 2/77 (3%) |
| outright (outright, flat) | unclear | `␣outright` | 1/152 (1%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 1/79 (1%) | 0/77 (0%) |
| simulate (simulating) | unclear | `模拟` | 1/152 (1%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 1/79 (1%) | 0/77 (0%) |
| apologize (apologizing) | unclear | `道歉` | 1/152 (1%) | 0/81 (0%) | 1/138 (1%) | 1/158 (1%) | 1/79 (1%) | 0/77 (0%) |

Not in the draft: deny (excluded: admit / deny / acknowledge); admit (excluded: admit / deny / acknowledge); acknowledge (excluded: admit / deny / acknowledge); honest (excluded: the question's own word); truth (excluded: the question's own word)

## q_tok23

| family | side | members | lies | truths | no-pressure truths | unrelated | lies that deny | truths that deny |
|---|---|---|---|---|---|---|---|---|
| false (false, untrue) | lie | `␣false`, `␣False`, `:false`, `.assertFalse`, `.False` | 126/152 (83%) | 73/81 (90%) | 132/138 (96%) | 158/158 (100%) | 58/79 (73%) | 69/77 (90%) |
| true (true, real) | truth | `true`, `真` | 73/152 (48%) | 35/81 (43%) | 27/138 (20%) | 71/158 (45%) | 30/79 (38%) | 32/77 (42%) |
| outright (outright, flat) | unclear | `␣outright` | 0/152 (0%) | 1/81 (1%) | 0/138 (0%) | 2/158 (1%) | 0/79 (0%) | 1/77 (1%) |

Not in the draft: correct (excluded: the question's own word)
