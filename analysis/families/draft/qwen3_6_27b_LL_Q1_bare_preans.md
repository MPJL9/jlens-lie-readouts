# Draft families: qwen3.6-27b, logit lens, part Q1_bare, group preans

Written by `scripts/apply_family_decisions.py` (2026-10-01; draft, not frozen). Counts are `present / transcripts (share)`
on the build split.

## preans_slot0

| family | side | members | lies | truths | no-pressure truths | unrelated | lies that deny | truths that deny |
|---|---|---|---|---|---|---|---|---|
| critique (critique, criticism) | unclear | `␣critique`, `指正`, `批判`, `␣critiques`, `批评`, `␣criticism` | 145/152 (95%) | 77/81 (95%) | 137/138 (99%) | 158/158 (100%) | 47/53 (89%) | 70/74 (95%) |
| self-reflection (self-examination, reflection) | unclear | `反思`, `自查`, `自省`, `自检`, `审视`, `␣reflection`, `␣reflective` | 100/152 (66%) | 51/81 (63%) | 76/138 (55%) | 141/158 (89%) | 22/53 (42%) | 45/74 (61%) |
| objective (objective) | unclear | `客观` | 22/152 (14%) | 11/81 (14%) | 1/138 (1%) | 5/158 (3%) | 4/53 (8%) | 10/74 (14%) |
| negate (negate, negative) | unclear | `否定` | 11/152 (7%) | 9/81 (11%) | 3/138 (2%) | 0/158 (0%) | 11/53 (21%) | 9/74 (12%) |
| ethics (ethics, morality) | unclear | `伦理` | 16/152 (11%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 0/53 (0%) | 0/74 (0%) |
| knowingly (knowingly, knowing full well) | unclear | `明知` | 15/152 (10%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 3/53 (6%) | 0/74 (0%) |
| true (true, real) | truth | `true`, `确实`, `是真的`, `确实是` | 11/152 (7%) | 3/81 (4%) | 0/138 (0%) | 1/158 (1%) | 0/53 (0%) | 2/74 (3%) |
| candid (candid, frank, speaking openly) | truth | `坦诚`, `直言` | 5/152 (3%) | 4/81 (5%) | 0/138 (0%) | 3/158 (2%) | 2/53 (4%) | 2/74 (3%) |
| accuse (accuse, accusation) | unclear | `指控`, `␣accus`, `␣accusation`, `␣accusations` | 5/152 (3%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 3/53 (6%) | 1/74 (1%) |
| honest (honest, truthful) | truth | `诚` | 5/152 (3%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 0/53 (0%) | 0/74 (0%) |
| integrity (integrity, uprightness) | truth | `正直` | 3/152 (2%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 0/53 (0%) | 0/74 (0%) |
| clarify (clarify) | unclear | `␣clarification` | 0/152 (0%) | 1/81 (1%) | 0/138 (0%) | 1/158 (1%) | 0/53 (0%) | 1/74 (1%) |

Not in the draft: truth (excluded: truth from the question on); admit (excluded: admit / deny / acknowledge); acknowledge (excluded: admit / deny / acknowledge)

## preans_slot1

| family | side | members | lies | truths | no-pressure truths | unrelated | lies that deny | truths that deny |
|---|---|---|---|---|---|---|---|---|
| fact (fact; factual) | truth | `事实`, `␣fact`, `␣factual`, `事实上`, `实际情况`, `␣facts`, `事实和`, `的事实`, `Fact`, `␣Fact`, `fact`, `␣FACT`, `␣Facts`, `facts`, `FACT`, `_fact`, `␣reality`, `␣Reality`, `Reality`, `␣realidad`, `实际`, `符合`, `现实`, `实际上`, `实际的`, `是否符合`, `现实中`, `的现实`, `实际上是`, `根据实际情况`, `与实际`, `求实`, `与现实`, `认定事实`, `上述事实` | 152/152 (100%) | 66/81 (81%) | 131/138 (95%) | 93/158 (59%) | 53/53 (100%) | 59/74 (80%) |
| honest (honest, truthful) | truth | `␣truthful`, `如实`, `诚`, `诚实`, `␣honesty`, `␣honest`, `实事求是`, `诚信`, `␣honestly`, `␣Honest` | 142/152 (93%) | 65/81 (80%) | 124/138 (90%) | 94/158 (59%) | 46/53 (87%) | 58/74 (78%) |
| truthful (truthful; truthfully) | truth | `␣truthful`, `如实` | 135/152 (89%) | 62/81 (77%) | 118/138 (86%) | 29/158 (18%) | 44/53 (83%) | 57/74 (77%) |
| knowingly (knowing; knowingly) | unclear | `明知`, `知情`, `␣knowingly`, `␣knowing`, `␣Knowing`, `Knowing` | 141/152 (93%) | 39/81 (48%) | 94/138 (68%) | 13/158 (8%) | 47/53 (89%) | 33/74 (45%) |
| conceal (conceal) | lie | `隐瞒`, `␣conceal`, `␣concealed`, `瞒`, `藏`, `掩`, `遮`, `隐` | 138/152 (91%) | 33/81 (41%) | 45/138 (33%) | 1/158 (1%) | 45/53 (85%) | 29/74 (39%) |
| knowingly (knowingly, knowing full well) | unclear | `明知`, `␣knowingly` | 139/152 (91%) | 31/81 (38%) | 90/138 (65%) | 13/158 (8%) | 45/53 (85%) | 26/74 (35%) |
| false (false, untrue) | lie | `␣false`, `␣False`, `false`, `False`, `␣fals`, `␣falsely`, `␣untrue`, `/false`, `␣falsehood`, `假`, `虚假`, `假的`, `真假` | 143/152 (94%) | 26/81 (32%) | 78/138 (57%) | 34/158 (22%) | 47/53 (89%) | 20/74 (27%) |
| cover up (cover up, disguise a fault) | lie | `掩盖`, `掩饰`, `遮盖`, `␣masking`, `遮住`, `遮掩`, `遮蔽`, `␣masked` | 116/152 (76%) | 17/81 (21%) | 15/138 (11%) | 1/158 (1%) | 37/53 (70%) | 13/74 (18%) |
| lie (a lie, to lie) | lie | `谎言`, `撒谎`, `说谎`, `谎`, `␣lies`, `␣lie`, `␣lied`, `␣lying`, `lying`, `␣mentira`, `␣거짓`, `␣Lies`, `␣Lie`, `lies`, `␣liar` | 123/152 (81%) | 9/81 (11%) | 3/138 (2%) | 0/158 (0%) | 38/53 (72%) | 6/74 (8%) |
| deliberate (deliberately, intentionally) | unclear | `故意`, `␣deliberately`, `␣intentionally`, `刻意`, `␣deliberate`, `␣intentional` | 92/152 (61%) | 19/81 (23%) | 19/138 (14%) | 15/158 (9%) | 29/53 (55%) | 16/74 (22%) |
| fabricate (fabricate, invent, make up) | lie | `虚构`, `␣fabricated`, `␣fabrication`, `凭空`, `␣invented`, `␣invent`, `伪造`, `␣invention`, `作假` | 88/152 (58%) | 19/81 (23%) | 72/138 (52%) | 43/158 (27%) | 22/53 (42%) | 16/74 (22%) |
| objective (objective) | unclear | `␣objective`, `␣objectively`, `客观` | 62/152 (41%) | 20/81 (25%) | 33/138 (24%) | 11/158 (7%) | 27/53 (51%) | 19/74 (26%) |
| mislead (mislead) | lie | `␣misleading`, `误导`, `误导性`, `␣misled` | 69/152 (45%) | 10/81 (12%) | 3/138 (2%) | 2/158 (1%) | 10/53 (19%) | 6/74 (8%) |
| real / genuine (real, genuine, true to reality) | truth | `真实`, `真实的`, `的真实`, `的真实性` | 59/152 (39%) | 17/81 (21%) | 66/138 (48%) | 28/158 (18%) | 20/53 (38%) | 14/74 (19%) |
| gloss over (gloss over) | lie | `␣gloss`, `淡化` | 59/152 (39%) | 14/81 (17%) | 4/138 (3%) | 2/158 (1%) | 18/53 (34%) | 13/74 (18%) |
| contradict (contradict, contradiction) | unclear | `␣contradict`, `␣contrad`, `矛盾`, `␣contradiction`, `␣contradictory`, `␣contradictions`, `␣contradd`, `矛盾的` | 55/152 (36%) | 18/81 (22%) | 29/138 (21%) | 8/158 (5%) | 21/53 (40%) | 15/74 (20%) |
| true (true, real) | truth | `␣true`, `true`, `␣real`, `True`, `␣True`, `real`, `_true`, `␣genuine`, `.real`, `␣genuinely`, `真`, `成立`, `真实性`, `确实`, `真正的`, `是真的`, `的真`, `确实是`, `属实` | 59/152 (39%) | 11/81 (14%) | 16/138 (12%) | 43/158 (27%) | 29/53 (55%) | 10/74 (14%) |
| omit (omit, leave out) | lie | `␣omit`, `␣omission`, `omit`, `省略`, `␣omitted`, `␣OMIT` | 45/152 (30%) | 15/81 (19%) | 7/138 (5%) | 5/158 (3%) | 17/53 (32%) | 14/74 (19%) |
| downplay (downplay) | lie | `淡化` | 47/152 (31%) | 12/81 (15%) | 1/138 (1%) | 0/158 (0%) | 15/53 (28%) | 12/74 (16%) |
| negate (negate, negative) | unclear | `否定` | 39/152 (26%) | 19/81 (23%) | 16/138 (12%) | 1/158 (1%) | 14/53 (26%) | 18/74 (24%) |
| misinformation (false information) | lie | `␣misinformation`, `虚假信息` | 49/152 (32%) | 2/81 (2%) | 7/138 (5%) | 1/158 (1%) | 10/53 (19%) | 1/74 (1%) |
| withhold (withhold information) | lie | `␣withholding`, `␣withhold`, `␣withheld` | 34/152 (22%) | 14/81 (17%) | 1/138 (1%) | 1/158 (1%) | 18/53 (34%) | 13/74 (18%) |
| wrong (wrong, mistaken) | lie | `␣error`, `␣wrong`, `错`, `错误`, `不对`, `错了`, `没错`, `是非`, `误会`, `是错误的`, `对错` | 32/152 (21%) | 16/81 (20%) | 10/138 (7%) | 15/158 (9%) | 10/53 (19%) | 12/74 (16%) |
| superficially (on the surface, seemingly) | unclear | `表面上`, `看似` | 34/152 (22%) | 13/81 (16%) | 44/138 (32%) | 36/158 (23%) | 17/53 (32%) | 10/74 (14%) |
| evade (evade, dodge) | lie | `回避`, `␣evasion`, `␣dodge`, `规避`, `␣evade`, `逃避` | 35/152 (23%) | 11/81 (14%) | 2/138 (1%) | 0/158 (0%) | 16/53 (30%) | 10/74 (14%) |
| fake (fake) | lie | `fake`, `␣fake`, `作假` | 39/152 (26%) | 5/81 (6%) | 41/138 (30%) | 9/158 (6%) | 8/53 (15%) | 3/74 (4%) |
| violate (violate, go against (a principle)) | unclear | `违背`, `违反`, `违反了` | 37/152 (24%) | 6/81 (7%) | 15/138 (11%) | 3/158 (2%) | 10/53 (19%) | 5/74 (7%) |
| imply (imply, implicit) | unclear | `暗示`, `␣implying`, `␣imply`, `␣implied`, `隐含`, `␣implies`, `␣implicitly`, `␣implication`, `␣implicit`, `␣implic`, `␣implications`, `␣implica`, `␣implique` | 29/152 (19%) | 14/81 (17%) | 6/138 (4%) | 4/158 (3%) | 6/53 (11%) | 11/74 (15%) |
| correct (correct) | truth | `valid`, `␣valid`, `␣correct`, `␣Valid`, `␣correctly`, `correct`, `␣correction`, `_correct`, `Correct`, `␣corrected`, `␣Correct`, `␣corrections`, `␣correctness`, `␣Correction`, `␣correcting`, `_correction`, `Correction`, `␣Corrections`, `␣corrective`, `正确`, `正确的`, `正确的是`, `正确答案`, `纠正`, `的正确`, `无误`, `是正确的`, `正确地`, `是否正确`, `是对的` | 5/152 (3%) | 34/81 (42%) | 78/138 (57%) | 85/158 (54%) | 3/53 (6%) | 33/74 (45%) |
| vague (vague, ambiguous) | unclear | `␣vague`, `模糊`, `含糊`, `␣vaguely`, `␣ambiguity`, `␣ambiguous`, `ambiguous` | 25/152 (16%) | 13/81 (16%) | 0/138 (0%) | 6/158 (4%) | 7/53 (13%) | 10/74 (14%) |
| agreed line (the agreed or official line of a story) | unclear | `口径` | 32/152 (21%) | 3/81 (4%) | 5/138 (4%) | 0/158 (0%) | 12/53 (23%) | 2/74 (3%) |
| accurate (accurate) | truth | `␣accur`, `␣accurate`, `␣accuracy`, `␣accurately`, `accuracy`, `accur`, `Accuracy`, `␣Accuracy`, `准确`, `准确性`, `准确的`, `准确地` | 9/152 (6%) | 23/81 (28%) | 88/138 (64%) | 76/158 (48%) | 5/53 (9%) | 23/74 (31%) |
| technically (technically (true)) | unclear | `␣technically` | 22/152 (14%) | 9/81 (11%) | 1/138 (1%) | 3/158 (2%) | 14/53 (26%) | 9/74 (12%) |
| refuse (refuse) | unclear | `␣refusal`, `拒绝`, `␣refused`, `␣refuse`, `␣refusing`, `␣refuses`, `␣refus`, `拒`, `␣отказ`, `拒絕`, `拒绝了`, `␣отказа`, `拒不`, `␣decline`, `␣declining`, `␣declined`, `␣declines` | 4/152 (3%) | 27/81 (33%) | 9/138 (7%) | 2/158 (1%) | 4/53 (8%) | 27/74 (36%) |
| fictional (fictional) | unclear | `␣fictional`, `fiction`, `␣fiction`, `-fiction` | 18/152 (12%) | 8/81 (10%) | 45/138 (33%) | 25/158 (16%) | 6/53 (11%) | 6/74 (8%) |
| euphemistic (euphemistic, indirect wording) | unclear | `委婉` | 7/152 (5%) | 16/81 (20%) | 5/138 (4%) | 0/158 (0%) | 3/53 (6%) | 15/74 (20%) |
| integrity (integrity, uprightness) | truth | `正直`, `诚信` | 12/152 (8%) | 10/81 (12%) | 21/138 (15%) | 2/158 (1%) | 2/53 (4%) | 9/74 (12%) |
| candid (candid, frank, speaking openly) | truth | `坦诚`, `坦白` | 0/152 (0%) | 19/81 (23%) | 24/138 (17%) | 8/158 (5%) | 0/53 (0%) | 18/74 (24%) |
| incorrect (incorrect) | lie | `␣incorrect`, `␣inaccur`, `␣incorrectly`, `␣inaccurate`, `␣Incorrect`, `不符合`, `有误`, `错误的是` | 5/152 (3%) | 14/81 (17%) | 13/138 (9%) | 35/158 (22%) | 3/53 (6%) | 12/74 (16%) |
| disclose (disclose, reveal) | truth | `信息披露`, `␣disclosure`, `␣disclosing`, `披露`, `␣revealing`, `␣disclose`, `␣disclosed`, `␣Disclosure`, `透露`, `␣reveal` | 8/152 (5%) | 10/81 (12%) | 13/138 (9%) | 2/158 (1%) | 2/53 (4%) | 9/74 (12%) |
| decline (decline (to answer)) | unclear | `␣decline`, `␣declining`, `␣declined`, `␣declines` | 0/152 (0%) | 18/81 (22%) | 1/138 (1%) | 0/158 (0%) | 0/53 (0%) | 18/74 (24%) |
| blame (blaming) | unclear | `␣blaming`, `␣blame`, `␣blames`, `␣blamed` | 17/152 (11%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 5/53 (9%) | 0/74 (0%) |
| candid / frank (speaking candidly or frankly) | truth | `坦诚`, `直言` | 0/152 (0%) | 16/81 (20%) | 26/138 (19%) | 8/158 (5%) | 0/53 (0%) | 15/74 (20%) |
| clarify (clarify) | unclear | `澄清`, `␣clarification`, `␣clarify`, `␣clarified` | 4/152 (3%) | 11/81 (14%) | 14/138 (10%) | 12/158 (8%) | 2/53 (4%) | 10/74 (14%) |
| hide (hide, hidden) | lie | `␣hiding`, `Hide`, `_hide`, `-hide`, `␣hide`, `hide`, `␣hides`, `隐藏`, `␣Hide`, `隐匿` | 15/152 (10%) | 0/81 (0%) | 0/138 (0%) | 1/158 (1%) | 6/53 (11%) | 0/74 (0%) |
| transparent (transparent, open) | truth | `透明`, `␣transparency`, `-transparent`, `␣transparent`, `␣Transparency`, `透明的`, `透明度` | 0/152 (0%) | 13/81 (16%) | 22/138 (16%) | 7/158 (4%) | 0/53 (0%) | 12/74 (16%) |
| inaccurate (inaccurate) | lie | `准确性和`, `不准确` | 6/152 (4%) | 4/81 (5%) | 7/138 (5%) | 25/158 (16%) | 2/53 (4%) | 4/74 (5%) |
| ethics (ethics, morality) | unclear | `␣ethical`, `␣ethics`, `伦理`, `道德` | 0/152 (0%) | 5/81 (6%) | 0/138 (0%) | 0/158 (0%) | 0/53 (0%) | 5/74 (7%) |
| reveal (revealing) | truth | `␣revealing`, `␣reveal` | 0/152 (0%) | 2/81 (2%) | 3/138 (2%) | 1/158 (1%) | 0/53 (0%) | 1/74 (1%) |
| confess (confess) | truth | `交代` | 0/152 (0%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 0/53 (0%) | 1/74 (1%) |
| manipulate (manipulate) | lie | `␣manipulation`, `␣manipulated` | 0/152 (0%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 0/53 (0%) | 1/74 (1%) |
| good faith (good intention) | unclear | `善意` | 0/152 (0%) | 1/81 (1%) | 7/138 (5%) | 1/158 (1%) | 0/53 (0%) | 1/74 (1%) |
| moral (moral; morally) | unclear | `道德` | 0/152 (0%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 0/53 (0%) | 1/74 (1%) |

Not in the draft: truth (excluded: truth from the question on); admit (excluded: admit / deny / acknowledge); acknowledge (excluded: admit / deny / acknowledge); deny (excluded: admit / deny / acknowledge); perfunctory (held back: no undisputed member left); tell the truth (excluded: truth from the question on); deceive (excluded: the question's own word)

## preans_slot2

| family | side | members | lies | truths | no-pressure truths | unrelated | lies that deny | truths that deny |
|---|---|---|---|---|---|---|---|---|
| fact (fact; factual) | truth | `␣fact`, `事实`, `实际情况`, `␣facts`, `的事实`, `事实上`, `␣factual`, `facts`, `fact`, `␣Fact`, `␣Facts`, `事实和`, `Fact`, `␣FACT`, `FACT`, `_fact`, `上述事实`, `事實`, `␣reality`, `␣Reality`, `Reality`, `␣realities`, `␣realidad`, `实际`, `符合`, `现实`, `实际上`, `的实际`, `实际的`, `是否符合`, `现实中`, `的现实`, `实际上是`, `根据实际情况`, `与实际`, `犯罪事实`, `与现实`, `␣realtà` | 111/152 (73%) | 39/81 (48%) | 130/138 (94%) | 68/158 (43%) | 36/53 (68%) | 35/74 (47%) |
| honest (honest, truthful) | truth | `如实`, `诚实`, `诚`, `␣truthful`, `␣honest`, `␣honesty`, `实事求是`, `诚信`, `诚实守信` | 88/152 (58%) | 31/81 (38%) | 17/138 (12%) | 11/158 (7%) | 24/53 (45%) | 29/74 (39%) |
| knowingly (knowing; knowingly) | unclear | `明知`, `知情`, `␣knowing`, `␣Knowing`, `␣knowingly`, `Knowing` | 88/152 (58%) | 21/81 (26%) | 74/138 (54%) | 1/158 (1%) | 27/53 (51%) | 21/74 (28%) |
| knowingly (knowingly, knowing full well) | unclear | `明知`, `␣knowingly` | 86/152 (57%) | 21/81 (26%) | 74/138 (54%) | 1/158 (1%) | 26/53 (49%) | 21/74 (28%) |
| true (true, real) | truth | `␣true`, `true`, `␣real`, `True`, `␣True`, `real`, `_TRUE`, `_real`, `,true`, `␣genuine`, `␣REAL`, `.real`, `␣genuinely`, `真`, `成立`, `真正`, `确实`, `真正的`, `的确`, `是真的`, `的真`, `确实是`, `属实`, `的真正` | 92/152 (61%) | 15/81 (19%) | 115/138 (83%) | 24/158 (15%) | 27/53 (51%) | 13/74 (18%) |
| real / genuine (real, genuine, true to reality) | truth | `的真实`, `真实`, `真实的`, `的真实性`, `真实性`, `真實` | 90/152 (59%) | 16/81 (20%) | 76/138 (55%) | 12/158 (8%) | 25/53 (47%) | 15/74 (20%) |
| truthful (truthful; truthfully) | truth | `如实`, `␣truthful` | 75/152 (49%) | 25/81 (31%) | 14/138 (10%) | 1/158 (1%) | 23/53 (43%) | 24/74 (32%) |
| objective (objective) | unclear | `␣objective`, `␣objectively`, `客观` | 63/152 (41%) | 8/81 (10%) | 62/138 (45%) | 8/158 (5%) | 22/53 (42%) | 7/74 (9%) |
| deliberate (deliberately, intentionally) | unclear | `故意`, `␣intentionally`, `刻意`, `␣deliberately`, `␣deliberate`, `␣intentional`, `故意的` | 50/152 (33%) | 13/81 (16%) | 0/138 (0%) | 2/158 (1%) | 11/53 (21%) | 13/74 (18%) |
| conceal (conceal) | lie | `隐瞒`, `␣concealed`, `␣conceal`, `瞒`, `藏`, `掩`, `遮`, `隐` | 47/152 (31%) | 15/81 (19%) | 1/138 (1%) | 0/158 (0%) | 19/53 (36%) | 15/74 (20%) |
| honest (honest; honesty) | truth | `诚实`, `诚`, `␣honest`, `␣honesty` | 40/152 (26%) | 17/81 (21%) | 6/138 (4%) | 10/158 (6%) | 8/53 (15%) | 16/74 (22%) |
| fictional (fictional) | unclear | `␣fictional`, `fiction`, `␣Fiction`, `-fiction` | 19/152 (12%) | 26/81 (32%) | 9/138 (7%) | 11/158 (7%) | 6/53 (11%) | 24/74 (32%) |
| accurate (accurate) | truth | `␣accur`, `␣accurate`, `␣accuracy`, `␣accurately`, `accuracy`, `accur`, `␣Accuracy`, `准确`, `准确性`, `准确的`, `准确地` | 32/152 (21%) | 11/81 (14%) | 54/138 (39%) | 35/158 (22%) | 10/53 (19%) | 10/74 (14%) |
| fabricate (fabricate, invent, make up) | lie | `虚构`, `伪造`, `凭空` | 22/152 (14%) | 18/81 (22%) | 19/138 (14%) | 14/158 (9%) | 8/53 (15%) | 17/74 (23%) |
| contradict (contradict, contradiction) | unclear | `矛盾`, `矛盾的`, `␣contradict`, `␣contrad`, `␣contradictory` | 13/152 (9%) | 27/81 (33%) | 15/138 (11%) | 0/158 (0%) | 2/53 (4%) | 27/74 (36%) |
| secret (secret, secretly) | lie | `␣secret`, `秘密`, `␣Secret`, `secret`, `的秘密`, `␣secretly`, `-secret`, `Secret`, `_secret`, `.secret`, `␣secrets`, `␣secretive`, `商业秘密` | 35/152 (23%) | 4/81 (5%) | 2/138 (1%) | 0/158 (0%) | 15/53 (28%) | 4/74 (5%) |
| hide (hide, hidden) | lie | `隐藏`, `␣hidden`, `隐藏的`, `␣hiding`, `隐藏着`, `隐蔽`, `␣hide`, `藏着` | 31/152 (20%) | 5/81 (6%) | 12/138 (9%) | 0/158 (0%) | 15/53 (28%) | 5/74 (7%) |
| violate (violate, go against (a principle)) | unclear | `违背`, `违反`, `违反了` | 17/152 (11%) | 19/81 (23%) | 3/138 (2%) | 0/158 (0%) | 5/53 (9%) | 18/74 (24%) |
| ethics (ethics, morality) | unclear | `␣ethical`, `伦理`, `␣ethics`, `道德`, `␣moral`, `␣Ethics`, `ethical`, `的道德`, `␣morally`, `职业道德`, `␣morals`, `␣Moral` | 18/152 (12%) | 16/81 (20%) | 1/138 (1%) | 0/158 (0%) | 5/53 (9%) | 14/74 (19%) |
| superficially (on the surface, seemingly) | unclear | `表面上`, `看似` | 16/152 (11%) | 17/81 (21%) | 2/138 (1%) | 2/158 (1%) | 6/53 (11%) | 16/74 (22%) |
| privately (privately, in private) | unclear | `私下`, `␣privately` | 23/152 (15%) | 3/81 (4%) | 0/138 (0%) | 0/158 (0%) | 8/53 (15%) | 3/74 (4%) |
| wrong (wrong, mistaken) | lie | `␣wrong`, `␣mistake`, `␣mistakes`, `␣flaw`, `错`, `错误`, `没错`, `失误`, `是非`, `误会`, `的错误`, `是错误的` | 12/152 (8%) | 11/81 (14%) | 25/138 (18%) | 3/158 (2%) | 6/53 (11%) | 9/74 (12%) |
| false (false, untrue) | lie | `␣false`, `␣False`, `false`, `False`, `␣fals`, `.False`, `␣falsely`, `/false`, `␣falsehood`, `假`, `虚假`, `假的`, `真假`, `不实` | 12/152 (8%) | 9/81 (11%) | 23/138 (17%) | 2/158 (1%) | 4/53 (8%) | 9/74 (12%) |
| loyalty (loyalty) | unclear | `␣loyalty`, `忠诚`, `␣loyal`, `忠诚度` | 15/152 (10%) | 5/81 (6%) | 0/138 (0%) | 0/158 (0%) | 7/53 (13%) | 5/74 (7%) |
| confess (confess) | truth | `交代` | 9/152 (6%) | 10/81 (12%) | 10/138 (7%) | 0/158 (0%) | 3/53 (6%) | 8/74 (11%) |
| cover up (cover up, disguise a fault) | lie | `掩盖`, `掩饰`, `伪装` | 12/152 (8%) | 4/81 (5%) | 1/138 (1%) | 0/158 (0%) | 4/53 (8%) | 4/74 (5%) |
| moral (moral; morally) | unclear | `道德`, `␣moral`, `␣morally`, `的道德`, `␣morals`, `␣Moral` | 8/152 (5%) | 8/81 (10%) | 1/138 (1%) | 0/158 (0%) | 2/53 (4%) | 7/74 (9%) |
| incorrect (incorrect) | lie | `␣incorrect`, `␣inaccurate`, `错误的`, `不符合`, `有误` | 1/152 (1%) | 10/81 (12%) | 2/138 (1%) | 11/158 (7%) | 0/53 (0%) | 10/74 (14%) |
| lie (a lie, to lie) | lie | `␣lie`, `谎言`, `撒谎`, `说谎`, `␣lies`, `␣lying`, `谎`, `␣lied`, `lying`, `␣Lie`, `Lie`, `␣mentira`, `␣Lies`, `␣거짓`, `␣liar` | 5/152 (3%) | 5/81 (6%) | 1/138 (1%) | 0/158 (0%) | 2/53 (4%) | 5/74 (7%) |
| good faith (good intention) | unclear | `善意` | 8/152 (5%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 1/53 (2%) | 0/74 (0%) |
| confidential (confidential) | lie | `机密`, `␣confidential`, `␣confidentiality`, `␣Confidential` | 5/152 (3%) | 3/81 (4%) | 0/138 (0%) | 0/158 (0%) | 4/53 (8%) | 3/74 (4%) |
| withhold (withhold information) | lie | `␣withholding`, `␣withheld` | 4/152 (3%) | 2/81 (2%) | 0/138 (0%) | 0/158 (0%) | 3/53 (6%) | 2/74 (3%) |
| fake (fake) | lie | `fake`, `␣fake` | 4/152 (3%) | 2/81 (2%) | 2/138 (1%) | 2/158 (1%) | 1/53 (2%) | 2/74 (3%) |
| unethical (unethical) | lie | `␣unethical` | 1/152 (1%) | 5/81 (6%) | 0/138 (0%) | 0/158 (0%) | 0/53 (0%) | 5/74 (7%) |
| mislead (mislead) | lie | `误导`, `␣misleading` | 1/152 (1%) | 4/81 (5%) | 1/138 (1%) | 0/158 (0%) | 0/53 (0%) | 4/74 (5%) |
| euphemistic (euphemistic, indirect wording) | unclear | `委婉` | 3/152 (2%) | 2/81 (2%) | 0/138 (0%) | 0/158 (0%) | 1/53 (2%) | 2/74 (3%) |
| disclose (disclose, reveal) | truth | `␣disclosure`, `信息披露`, `␣disclosed`, `␣revealing` | 3/152 (2%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 3/53 (6%) | 1/74 (1%) |
| misinformation (false information) | lie | `␣misinformation`, `虚假信息` | 0/152 (0%) | 4/81 (5%) | 1/138 (1%) | 0/158 (0%) | 0/53 (0%) | 4/74 (5%) |
| imply (imply, implicit) | unclear | `隐含`, `␣implied`, `␣implies`, `␣implication`, `␣implicit` | 3/152 (2%) | 1/81 (1%) | 2/138 (1%) | 2/158 (1%) | 2/53 (4%) | 1/74 (1%) |
| candid (candid, frank, speaking openly) | truth | `坦诚` | 1/152 (1%) | 2/81 (2%) | 0/138 (0%) | 0/158 (0%) | 0/53 (0%) | 2/74 (3%) |
| disguise (disguise, pretend) | lie | `伪装` | 2/152 (1%) | 1/81 (1%) | 1/138 (1%) | 0/158 (0%) | 1/53 (2%) | 1/74 (1%) |
| technically (technically (true)) | unclear | `␣technically` | 2/152 (1%) | 1/81 (1%) | 0/138 (0%) | 2/158 (1%) | 1/53 (2%) | 1/74 (1%) |
| integrity (integrity; uprightness) | truth | `诚信`, `␣integrity`, `诚实守信` | 0/152 (0%) | 3/81 (4%) | 1/138 (1%) | 0/158 (0%) | 0/53 (0%) | 3/74 (4%) |
| agreed line (the agreed or official line of a story) | unclear | `口径` | 1/152 (1%) | 2/81 (2%) | 0/138 (0%) | 0/158 (0%) | 0/53 (0%) | 2/74 (3%) |
| correct (correct) | truth | `valid`, `␣valid`, `␣correct`, `␣Valid`, `␣correctly`, `correct`, `␣correction`, `Correct`, `␣corrected`, `␣Correct`, `␣corrections`, `␣correctness`, `␣correctamente`, `␣Correction`, `␣correcting`, `␣Corrections`, `␣corrective`, `正确`, `正确的`, `正确答案`, `纠正`, `的正确`, `无误`, `是正确的`, `正确地`, `是否正确` | 0/152 (0%) | 3/81 (4%) | 29/138 (21%) | 61/158 (39%) | 0/53 (0%) | 2/74 (3%) |
| omit (omit, leave out) | lie | `␣omit`, `␣omission` | 1/152 (1%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 1/53 (2%) | 1/74 (1%) |
| evade (evade, dodge) | lie | `回避`, `规避` | 1/152 (1%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 0/53 (0%) | 1/74 (1%) |
| sincere (sincere) | truth | `诚恳` | 0/152 (0%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 0/53 (0%) | 1/74 (1%) |
| transparent (transparent, open) | truth | `␣transparency` | 1/152 (1%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 0/53 (0%) | 0/74 (0%) |
| integrity (integrity, uprightness) | truth | `␣integrity` | 0/152 (0%) | 1/81 (1%) | 1/138 (1%) | 0/158 (0%) | 0/53 (0%) | 1/74 (1%) |
| undisclosed (not disclosed) | lie | `␣undisclosed` | 1/152 (1%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 1/53 (2%) | 0/74 (0%) |
| manipulate (manipulate) | lie | `␣manipulation`, `␣manipulate`, `␣manipulating`, `操纵` | 0/152 (0%) | 1/81 (1%) | 1/138 (1%) | 0/158 (0%) | 0/53 (0%) | 1/74 (1%) |
| trick (trick) | lie | `␣trick`, `␣tricks` | 0/152 (0%) | 1/81 (1%) | 1/138 (1%) | 0/158 (0%) | 0/53 (0%) | 1/74 (1%) |
| negate (negate, negative) | unclear | `否定` | 0/152 (0%) | 1/81 (1%) | 1/138 (1%) | 0/158 (0%) | 0/53 (0%) | 1/74 (1%) |
| decline (decline (to answer)) | unclear | `␣declined` | 0/152 (0%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 0/53 (0%) | 1/74 (1%) |
| refuse (refuse) | unclear | `␣refusal`, `␣refused`, `␣refuse`, `␣refusing`, `␣refuses`, `␣refus`, `拒绝`, `拒`, `拒絕`, `拒绝了`, `␣declined` | 0/152 (0%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 0/53 (0%) | 1/74 (1%) |
| reveal (revealing) | truth | `␣revealing` | 1/152 (1%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 1/53 (2%) | 0/74 (0%) |
| truth (the truth (noun)) | truth | `求真` | 0/152 (0%) | 0/81 (0%) | 1/138 (1%) | 0/158 (0%) | 0/53 (0%) | 0/74 (0%) |
| inaccurate (inaccurate) | lie | `准确性和`, `不准确` | 0/152 (0%) | 0/81 (0%) | 3/138 (2%) | 2/158 (1%) | 0/53 (0%) | 0/74 (0%) |

Not in the draft: admit (excluded: admit / deny / acknowledge); acknowledge (excluded: admit / deny / acknowledge); deny (excluded: admit / deny / acknowledge); perfunctory (held back: no undisputed member left); tell the truth (excluded: truth from the question on); deceive (excluded: the question's own word)

## preans_slot3

| family | side | members | lies | truths | no-pressure truths | unrelated | lies that deny | truths that deny |
|---|---|---|---|---|---|---|---|---|
| candid (candid, frank, speaking openly) | truth | `坦白`, `坦诚`, `␣candid`, `␣frankly` | 135/152 (89%) | 70/81 (86%) | 92/138 (67%) | 121/158 (77%) | 37/53 (70%) | 64/74 (86%) |
| confess (confess) | truth | `␣confession`, `坦白` | 135/152 (89%) | 70/81 (86%) | 92/138 (67%) | 121/158 (77%) | 37/53 (70%) | 64/74 (86%) |
| clarify (clarify) | unclear | `澄清`, `␣clarification` | 123/152 (81%) | 72/81 (89%) | 94/138 (68%) | 125/158 (79%) | 36/53 (68%) | 66/74 (89%) |
| honest (honest, truthful) | truth | `诚`, `␣honestly`, `␣honest`, `诚实`, `␣honesty`, `誠` | 93/152 (61%) | 33/81 (41%) | 27/138 (20%) | 96/158 (61%) | 21/53 (40%) | 30/74 (41%) |
| apologize (apologize, sorry) | unclear | `抱歉`, `␣apologize`, `对不起`, `␣apologies`, `␣sorry`, `␣apology`, `Sorry`, `␣Sorry` | 79/152 (52%) | 36/81 (44%) | 19/138 (14%) | 22/158 (14%) | 18/53 (34%) | 32/74 (43%) |
| sincere (sincere) | truth | `真诚`, `␣sincerely`, `誠に` | 37/152 (24%) | 27/81 (33%) | 3/138 (2%) | 0/158 (0%) | 10/53 (19%) | 26/74 (35%) |
| wrong (wrong, mistaken) | lie | `错了`, `没错`, `是非` | 27/152 (18%) | 29/81 (36%) | 95/138 (69%) | 82/158 (52%) | 4/53 (8%) | 29/74 (39%) |
| true (true, real) | truth | `␣true`, `true`, `True`, `␣True`, `␣TRUE`, `TRUE`, `真`, `确实`, `的确`, `确实是` | 27/152 (18%) | 13/81 (16%) | 118/138 (86%) | 17/158 (11%) | 4/53 (8%) | 11/74 (15%) |
| ethics (ethics, morality) | unclear | `伦理`, `␣ethical` | 24/152 (16%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 1/53 (2%) | 0/74 (0%) |
| false (false, untrue) | lie | `␣false`, `␣False`, `False`, `=False`, `␣FALSE`, `FALSE`, `>false`, `_false`, `/false`, `假` | 8/152 (5%) | 11/81 (14%) | 78/138 (57%) | 17/158 (11%) | 7/53 (13%) | 11/74 (15%) |
| objective (objective) | unclear | `␣objectively`, `客观` | 6/152 (4%) | 12/81 (15%) | 3/138 (2%) | 38/158 (24%) | 2/53 (4%) | 11/74 (15%) |
| technically (technically (true)) | unclear | `␣technically` | 5/152 (3%) | 3/81 (4%) | 0/138 (0%) | 28/158 (18%) | 4/53 (8%) | 3/74 (4%) |
| cover up (cover up, disguise a fault) | lie | `掩` | 6/152 (4%) | 0/81 (0%) | 1/138 (1%) | 2/158 (1%) | 1/53 (2%) | 0/74 (0%) |
| self-reflection (self-examination, reflection) | unclear | `反思` | 2/152 (1%) | 3/81 (4%) | 0/138 (0%) | 0/158 (0%) | 0/53 (0%) | 2/74 (3%) |
| negate (negate, negative) | unclear | `否定` | 2/152 (1%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 2/53 (4%) | 1/74 (1%) |
| ashamed (ashamed) | unclear | `愧` | 3/152 (2%) | 0/81 (0%) | 4/138 (3%) | 0/158 (0%) | 1/53 (2%) | 0/74 (0%) |
| privately (privately, in private) | unclear | `私下` | 1/152 (1%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 1/53 (2%) | 0/74 (0%) |
| refuse (refuse) | unclear | `␣refusal`, `␣refuse` | 1/152 (1%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 0/53 (0%) | 0/74 (0%) |

Not in the draft: truth (excluded: truth from the question on); admit (excluded: admit / deny / acknowledge)

## preans_slot4

| family | side | members | lies | truths | no-pressure truths | unrelated | lies that deny | truths that deny |
|---|---|---|---|---|---|---|---|---|
| honest (honest, truthful) | truth | `诚`, `诚实`, `诚信`, `如实`, `␣honest`, `␣honesty`, `␣truthful`, `␣honestly`, `␣Honest`, `诚实守信`, `实事求是` | 144/152 (95%) | 76/81 (94%) | 138/138 (100%) | 155/158 (98%) | 50/53 (94%) | 70/74 (95%) |
| honest (honest; honesty) | truth | `诚`, `诚实`, `␣honest`, `␣honesty`, `␣honestly`, `誠`, `␣Honest` | 131/152 (86%) | 71/81 (88%) | 133/138 (96%) | 145/158 (92%) | 44/53 (83%) | 65/74 (88%) |
| true (true, real) | truth | `␣true`, `true`, `␣real`, `True`, `␣True`, `real`, `␣TRUE`, `TRUE`, `␣genuine`, `真`, `确实`, `真正的`, `的确`, `是真的`, `确实是` | 117/152 (77%) | 54/81 (67%) | 104/138 (75%) | 48/158 (30%) | 31/53 (58%) | 47/74 (64%) |
| candid (candid, frank, speaking openly) | truth | `坦白`, `坦诚` | 113/152 (74%) | 53/81 (65%) | 91/138 (66%) | 127/158 (80%) | 38/53 (72%) | 49/74 (66%) |
| truthful (truthful; truthfully) | truth | `如实`, `␣truthful` | 105/152 (69%) | 43/81 (53%) | 122/138 (88%) | 98/158 (62%) | 27/53 (51%) | 39/74 (53%) |
| integrity (integrity, uprightness) | truth | `正直`, `␣integrity`, `诚信`, `诚实守信` | 82/152 (54%) | 63/81 (78%) | 121/138 (88%) | 124/158 (78%) | 33/53 (62%) | 60/74 (81%) |
| candid / frank (speaking candidly or frankly) | truth | `坦诚` | 88/152 (58%) | 44/81 (54%) | 71/138 (51%) | 61/158 (39%) | 33/53 (62%) | 41/74 (55%) |
| fact (fact; factual) | truth | `事实`, `␣factual`, `␣fact`, `␣facts`, `␣Fact`, `Fact`, `␣FACT`, `符合`, `实际上`, `是否符合`, `根据实际情况`, `求实`, `与现实` | 77/152 (51%) | 39/81 (48%) | 104/138 (75%) | 89/158 (56%) | 12/53 (23%) | 34/74 (46%) |
| objective (objective) | unclear | `␣objective`, `␣objectively`, `客观` | 77/152 (51%) | 36/81 (44%) | 98/138 (71%) | 55/158 (35%) | 27/53 (51%) | 34/74 (46%) |
| ethics (ethics, morality) | unclear | `␣ethical`, `伦理`, `道德`, `␣ethics`, `␣morally`, `␣moral`, `职业道德`, `的道德`, `␣Ethics`, `ethical` | 70/152 (46%) | 13/81 (16%) | 0/138 (0%) | 0/158 (0%) | 6/53 (11%) | 11/74 (15%) |
| transparent (transparent, open) | truth | `␣transparency`, `透明`, `透明的`, `␣transparent`, `透明度`, `␣Transparency`, `-transparent`, `transparent`, `␣Transparent`, `␣transparencia` | 32/152 (21%) | 31/81 (38%) | 41/138 (30%) | 20/158 (13%) | 19/53 (36%) | 28/74 (38%) |
| negate (negate, negative) | unclear | `否定` | 37/152 (24%) | 24/81 (30%) | 9/138 (7%) | 6/158 (4%) | 30/53 (57%) | 24/74 (32%) |
| violate (violate, go against (a principle)) | unclear | `违反`, `违背`, `违反了` | 55/152 (36%) | 4/81 (5%) | 1/138 (1%) | 0/158 (0%) | 3/53 (6%) | 2/74 (3%) |
| false (false, untrue) | lie | `␣false`, `␣False`, `(false`, `false`, `False`, `=False`, `FALSE`, `␣fals`, `_false`, `.False`, `/false`, `␣falsehood`, `虚假`, `假的` | 32/152 (21%) | 26/81 (32%) | 119/138 (86%) | 73/158 (46%) | 25/53 (47%) | 25/74 (34%) |
| moral (moral; morally) | unclear | `道德`, `␣morally`, `␣moral`, `的道德` | 37/152 (24%) | 6/81 (7%) | 0/138 (0%) | 0/158 (0%) | 2/53 (4%) | 5/74 (7%) |
| conceal (conceal) | lie | `隐瞒`, `␣conceal`, `掩`, `隐` | 35/152 (23%) | 5/81 (6%) | 0/138 (0%) | 0/158 (0%) | 8/53 (15%) | 3/74 (4%) |
| real / genuine (real, genuine, true to reality) | truth | `真实`, `真实的` | 17/152 (11%) | 16/81 (20%) | 14/138 (10%) | 3/158 (2%) | 0/53 (0%) | 16/74 (22%) |
| accurate (accurate) | truth | `␣accurate`, `␣accuracy`, `␣accurately`, `准确`, `准确性`, `准确的` | 7/152 (5%) | 26/81 (32%) | 127/138 (92%) | 66/158 (42%) | 3/53 (6%) | 25/74 (34%) |
| apologize (apologize, sorry) | unclear | `抱歉`, `␣apologize`, `对不起`, `␣apologies`, `␣sorry` | 21/152 (14%) | 11/81 (14%) | 6/138 (4%) | 14/158 (9%) | 10/53 (19%) | 11/74 (15%) |
| deliberate (deliberately, intentionally) | unclear | `␣intentionally`, `故意`, `␣deliberately`, `␣deliberate`, `␣intentional` | 11/152 (7%) | 19/81 (23%) | 9/138 (7%) | 34/158 (22%) | 1/53 (2%) | 19/74 (26%) |
| good faith (good intention) | unclear | `善意` | 20/152 (13%) | 5/81 (6%) | 1/138 (1%) | 0/158 (0%) | 10/53 (19%) | 4/74 (5%) |
| wrong (wrong, mistaken) | lie | `不对`, `错了`, `没错`, `是非`, `误会`, `是错误的` | 17/152 (11%) | 7/81 (9%) | 5/138 (4%) | 6/158 (4%) | 6/53 (11%) | 5/74 (7%) |
| knowingly (knowingly, knowing full well) | unclear | `明知` | 19/152 (12%) | 2/81 (2%) | 5/138 (4%) | 6/158 (4%) | 1/53 (2%) | 0/74 (0%) |
| sincere (sincere) | truth | `␣sincerely`, `真诚` | 13/152 (9%) | 6/81 (7%) | 1/138 (1%) | 3/158 (2%) | 7/53 (13%) | 6/74 (8%) |
| clarify (clarify) | unclear | `澄清`, `␣clarify` | 14/152 (9%) | 3/81 (4%) | 2/138 (1%) | 4/158 (3%) | 10/53 (19%) | 3/74 (4%) |
| incorrect (incorrect) | lie | `不符合`, `有误` | 10/152 (7%) | 6/81 (7%) | 0/138 (0%) | 2/158 (1%) | 0/53 (0%) | 6/74 (8%) |
| fabricate (fabricate, invent, make up) | lie | `虚构` | 12/152 (8%) | 3/81 (4%) | 2/138 (1%) | 9/158 (6%) | 0/53 (0%) | 3/74 (4%) |
| technically (technically (true)) | unclear | `␣technically` | 11/152 (7%) | 4/81 (5%) | 0/138 (0%) | 13/158 (8%) | 3/53 (6%) | 3/74 (4%) |
| superficially (on the surface, seemingly) | unclear | `表面上`, `看似` | 11/152 (7%) | 4/81 (5%) | 1/138 (1%) | 1/158 (1%) | 2/53 (4%) | 3/74 (4%) |
| downplay (downplay) | lie | `淡化` | 10/152 (7%) | 4/81 (5%) | 0/138 (0%) | 0/158 (0%) | 5/53 (9%) | 3/74 (4%) |
| loyalty (loyalty) | unclear | `忠诚`, `␣loyalty` | 11/152 (7%) | 2/81 (2%) | 1/138 (1%) | 0/158 (0%) | 7/53 (13%) | 2/74 (3%) |
| refuse (refuse) | unclear | `拒绝`, `␣refusal`, `␣refuse`, `␣refusing`, `␣refuses`, `␣refus` | 0/152 (0%) | 11/81 (14%) | 0/138 (0%) | 0/158 (0%) | 0/53 (0%) | 11/74 (15%) |
| correct (correct) | truth | `valid`, `␣correct`, `正确`, `纠正`, `无误`, `是正确的`, `是否正确` | 5/152 (3%) | 6/81 (7%) | 35/138 (25%) | 0/158 (0%) | 4/53 (8%) | 6/74 (8%) |
| disclose (disclose, reveal) | truth | `信息披露` | 5/152 (3%) | 5/81 (6%) | 1/138 (1%) | 0/158 (0%) | 0/53 (0%) | 4/74 (5%) |
| agreed line (the agreed or official line of a story) | unclear | `口径` | 9/152 (6%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 3/53 (6%) | 0/74 (0%) |
| withhold (withhold information) | lie | `␣withholding`, `␣withhold` | 8/152 (5%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 4/53 (8%) | 0/74 (0%) |
| self-reflection (self-examination, reflection) | unclear | `反思`, `自查`, `␣reflection`, `␣reflect`, `␣reflecting`, `Reflect` | 6/152 (4%) | 0/81 (0%) | 0/138 (0%) | 2/158 (1%) | 1/53 (2%) | 0/74 (0%) |
| fictional (fictional) | unclear | `␣fictional` | 5/152 (3%) | 0/81 (0%) | 1/138 (1%) | 3/158 (2%) | 0/53 (0%) | 0/74 (0%) |
| lie (a lie, to lie) | lie | `撒谎`, `说谎`, `谎言` | 4/152 (3%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 1/53 (2%) | 0/74 (0%) |
| ashamed (ashamed) | unclear | `愧` | 4/152 (3%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 1/53 (2%) | 0/74 (0%) |
| dishonest (dishonest) | lie | `␣dishonest` | 2/152 (1%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 0/53 (0%) | 0/74 (0%) |
| mislead (mislead) | lie | `␣misleading` | 2/152 (1%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 2/53 (4%) | 0/74 (0%) |
| evade (evade, dodge) | lie | `␣evasion` | 2/152 (1%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 2/53 (4%) | 0/74 (0%) |
| unethical (unethical) | lie | `␣unethical` | 2/152 (1%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 0/53 (0%) | 0/74 (0%) |
| privately (privately, in private) | unclear | `私下` | 2/152 (1%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 0/53 (0%) | 0/74 (0%) |
| inaccurate (inaccurate) | lie | `准确性和`, `不准确` | 2/152 (1%) | 0/81 (0%) | 3/138 (2%) | 12/158 (8%) | 0/53 (0%) | 0/74 (0%) |
| omit (omit, leave out) | lie | `␣omit` | 1/152 (1%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 0/53 (0%) | 0/74 (0%) |
| secret (secret, secretly) | lie | `秘密` | 1/152 (1%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 0/53 (0%) | 0/74 (0%) |

Not in the draft: truth (excluded: truth from the question on); admit (excluded: admit / deny / acknowledge); acknowledge (excluded: admit / deny / acknowledge); cover up (held back: no undisputed member left); deny (excluded: admit / deny / acknowledge); perfunctory (held back: no undisputed member left); tell the truth (excluded: truth from the question on)
