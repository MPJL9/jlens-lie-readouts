# Draft families: qwen3.6-27b, logit lens, part Q6_factual, group preans

Written by `scripts/apply_family_decisions.py` (2026-10-01; draft, not frozen). Counts are `present / transcripts (share)`
on the build split.

## preans_slot0

| family | side | members | lies | truths | no-pressure truths | unrelated | lies that deny | truths that deny |
|---|---|---|---|---|---|---|---|---|
| self-examination (checking or critiquing one's own reply) | unclear | `反思`, `自查`, `自检`, `␣critique`, `批判`, `指正` | 145/152 (95%) | 72/81 (89%) | 126/138 (91%) | 156/158 (99%) | 38/43 (88%) | 64/73 (88%) |
| objective (being objective) | unclear | `客观`, `␣objectively` | 36/152 (24%) | 18/81 (22%) | 3/138 (2%) | 4/158 (3%) | 7/43 (16%) | 16/73 (22%) |
| I cannot ('I cannot' (declining stance)) | unclear | `我无法` | 10/152 (7%) | 12/81 (15%) | 0/138 (0%) | 11/158 (7%) | 8/43 (19%) | 12/73 (16%) |
| law-abiding (obeying the law) | unclear | `守法` | 2/152 (1%) | 4/81 (5%) | 1/138 (1%) | 1/158 (1%) | 2/43 (5%) | 4/73 (5%) |
| deliberate (doing it on purpose, knowingly) | unclear | `明知` | 1/152 (1%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 0/43 (0%) | 0/73 (0%) |
| wrong (wrong, mistaken) | lie | `是非` | 1/152 (1%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 0/43 (0%) | 0/73 (0%) |
| conceal (to conceal, to hide) | lie | `掩` | 0/152 (0%) | 0/81 (0%) | 0/138 (0%) | 1/158 (1%) | 0/43 (0%) | 0/73 (0%) |

Not in the draft: admit (excluded: admit / deny / acknowledge); perfunctory (held back: no undisputed member left)

## preans_slot1

| family | side | members | lies | truths | no-pressure truths | unrelated | lies that deny | truths that deny |
|---|---|---|---|---|---|---|---|---|
| fact (fact, factual) | truth | `␣fact`, `␣reality`, `␣facts`, `Fact`, `fact`, `␣Fact`, `␣Reality`, `␣Facts`, `Reality`, `_fact`, `␣FACT`, `FACT`, `␣factual`, `facts`, `␣realidad`, `实际`, `符合`, `现实`, `事实`, `实际上`, `实际情况`, `事实上`, `的事实`, `的实际`, `实际的`, `是否符合`, `现实中`, `的现实`, `实际上是`, `根据实际情况`, `与实际`, `求实`, `与现实`, `认定事实`, `事实和`, `上述事实` | 149/152 (98%) | 78/81 (96%) | 137/138 (99%) | 122/158 (77%) | 43/43 (100%) | 70/73 (96%) |
| honest (being honest, truthful) | truth | `诚实`, `诚`, `诚信`, `坦诚`, `␣truthful`, `␣honest`, `␣honesty`, `␣honestly`, `␣Honest`, `如实`, `如实供述`, `实事求是` | 127/152 (84%) | 53/81 (65%) | 100/138 (72%) | 36/158 (23%) | 33/43 (77%) | 47/73 (64%) |
| deliberate (doing it on purpose, knowingly) | unclear | `明知`, `故意`, `刻意`, `␣intentionally`, `␣deliberately`, `␣deliberate`, `␣knowingly` | 144/152 (95%) | 36/81 (44%) | 44/138 (32%) | 14/158 (9%) | 38/43 (88%) | 30/73 (41%) |
| knowingly (knowing full well) | unclear | `明知`, `␣knowingly` | 142/152 (93%) | 30/81 (37%) | 43/138 (31%) | 6/158 (4%) | 36/43 (84%) | 24/73 (33%) |
| fabricate (making up false content, fake or fictional) | lie | `虚构`, `␣fabricated`, `␣fabrication`, `␣invented`, `␣invent`, `凭空`, `伪造`, `fake`, `␣fake`, `fiction`, `␣fiction`, `␣fictional`, `-fiction` | 124/152 (82%) | 44/81 (54%) | 49/138 (36%) | 48/158 (30%) | 30/43 (70%) | 37/73 (51%) |
| fiction (fiction / fictional) | unclear | `fiction`, `␣fiction`, `-fiction`, `␣fictional`, `␣fict`, `虚构`, `架空` | 119/152 (78%) | 44/81 (54%) | 49/138 (36%) | 48/158 (30%) | 28/43 (65%) | 37/73 (51%) |
| claim (claiming, asserting) | unclear | `␣claim`, `␣claims`, `␣claiming`, `␣Claim`, `claim`, `␣claimed`, `Claim`, `␣Claims`, `␣CLAIM`, `claims`, `Claims`, `CLAIM`, `_claim`, `声称`, `宣称`, `␣assert`, `assert`, `_assert`, `␣asserting`, `␣assertions`, `␣Assert`, `␣assertion`, `␣asserts`, `_ASSERT`, `.assert`, `(assert`, `	assert`, `␣asserted`, `Assert`, `␣Assertion` | 113/152 (74%) | 46/81 (57%) | 64/138 (46%) | 24/158 (15%) | 32/43 (74%) | 39/73 (53%) |
| lie (telling a lie) | lie | `谎言`, `谎`, `撒谎`, `说谎`, `␣거짓`, `␣lie`, `␣lies`, `␣lied`, `␣lying`, `lying`, `␣mentira` | 125/152 (82%) | 22/81 (27%) | 0/138 (0%) | 0/158 (0%) | 29/43 (67%) | 16/73 (22%) |
| conceal (hiding or covering up information) | lie | `隐瞒`, `掩盖`, `掩饰`, `遮掩`, `遮盖`, `遮住`, `遮蔽`, `␣conceal`, `␣concealed`, `␣masking`, `␣masked`, `␣hiding`, `␣hide`, `␣hides`, `-hide`, `Hide`, `_hide`, `隐藏`, `掩`, `遮`, `隐` | 116/152 (76%) | 27/81 (33%) | 3/138 (2%) | 0/158 (0%) | 33/43 (77%) | 21/73 (29%) |
| conceal (withholding or concealing the truth) | lie | `␣conceal`, `␣concealed`, `隐瞒`, `瞒` | 109/152 (72%) | 25/81 (31%) | 3/138 (2%) | 0/158 (0%) | 30/43 (70%) | 19/73 (26%) |
| true (true, real) | truth | `␣true`, `true`, `␣real`, `True`, `␣True`, `real`, `_real`, `␣genuine`, `␣REAL`, `.real`, `真`, `成立`, `真实`, `真实性`, `确实`, `真正的`, `的确`, `真实的`, `的真`, `内容的真实性`, `确实是`, `的真实`, `属实`, `的真实性` | 104/152 (68%) | 30/81 (37%) | 17/138 (12%) | 20/158 (13%) | 26/43 (60%) | 25/73 (34%) |
| deceive (the act of deceiving) | lie | `欺骗`, `␣deception`, `␣deceptive`, `欺`, `哄` | 105/152 (69%) | 23/81 (28%) | 1/138 (1%) | 1/158 (1%) | 21/43 (49%) | 17/73 (23%) |
| fabricate (making something up) | lie | `␣fabricated`, `␣fabrication`, `␣invented`, `␣invent`, `伪造`, `凭空` | 88/152 (58%) | 18/81 (22%) | 11/138 (8%) | 25/158 (16%) | 20/43 (47%) | 14/73 (19%) |
| cover up (covering up or masking something) | lie | `掩盖`, `掩饰`, `遮盖`, `遮掩`, `遮住`, `遮蔽`, `␣masking`, `␣masked` | 92/152 (61%) | 13/81 (16%) | 0/138 (0%) | 0/158 (0%) | 21/43 (49%) | 9/73 (12%) |
| contradict (contradicting, being contrary to) | unclear | `␣contrad`, `␣contradict`, `␣contradictory`, `␣contradiction`, `␣contradictions`, `矛盾`, `矛盾的`, `␣contrary`, `相反`, `相反的` | 62/152 (41%) | 40/81 (49%) | 74/138 (54%) | 8/158 (5%) | 17/43 (40%) | 34/73 (47%) |
| objective (being objective) | unclear | `客观`, `␣objectively`, `␣objective` | 67/152 (44%) | 23/81 (28%) | 35/138 (25%) | 9/158 (6%) | 24/43 (56%) | 22/73 (30%) |
| fake (fake / falsified) | lie | `fake`, `␣fake` | 38/152 (25%) | 13/81 (16%) | 7/138 (5%) | 2/158 (1%) | 4/43 (9%) | 9/73 (12%) |
| violate (violating, going against) | unclear | `违背`, `违反`, `违反了`, `␣violate`, `␣violates` | 35/152 (23%) | 12/81 (15%) | 8/138 (6%) | 0/158 (0%) | 9/43 (21%) | 10/73 (14%) |
| correct (correct) | truth | `valid`, `␣valid`, `␣correct`, `␣Valid`, `␣correctly`, `correct`, `␣correction`, `_correct`, `Correct`, `␣corrected`, `␣Correct`, `␣corrections`, `␣correctness`, `␣correctamente`, `␣Correction`, `␣correcting`, `␣Corrections`, `␣corrective`, `正确`, `正确的`, `正确的是`, `正确答案`, `纠正`, `的正确`, `无误`, `是正确的`, `正确地`, `是否正确`, `是对的` | 5/152 (3%) | 41/81 (51%) | 128/138 (93%) | 119/158 (75%) | 3/43 (7%) | 40/73 (55%) |
| accurate (accurate) | truth | `␣accur`, `␣accurate`, `␣accuracy`, `␣accurately`, `accuracy`, `accur`, `Accuracy`, `␣Accuracy`, `准确`, `准确性`, `准确的`, `准确地` | 5/152 (3%) | 33/81 (41%) | 118/138 (86%) | 94/158 (59%) | 1/43 (2%) | 33/73 (45%) |
| wrong (wrong, mistaken) | lie | `␣error`, `␣wrong`, `错`, `错误`, `不对`, `错了`, `没错`, `是非`, `的错误`, `是错误的` | 24/152 (16%) | 12/81 (15%) | 23/138 (17%) | 49/158 (31%) | 7/43 (16%) | 10/73 (14%) |
| imply (implying, suggesting indirectly) | unclear | `␣implying`, `␣implies`, `␣implied`, `␣imply`, `␣IMPLIED`, `␣implication`, `␣implications`, `␣implicitly`, `␣implicit`, `␣implica`, `␣implique`, `暗示`, `隐含` | 24/152 (16%) | 11/81 (14%) | 3/138 (2%) | 1/158 (1%) | 10/43 (23%) | 9/73 (12%) |
| incorrect (incorrect) | lie | `␣incorrect`, `␣inaccur`, `␣incorrectly`, `␣inaccurate`, `␣Incorrect`, `不符合`, `有误`, `错误的是` | 15/152 (10%) | 17/81 (21%) | 23/138 (17%) | 44/158 (28%) | 4/43 (9%) | 15/73 (21%) |
| disclose (disclosing, revealing) | truth | `␣disclosure`, `␣disclosed`, `信息披露`, `披露`, `揭露`, `␣revealing`, `␣revealed`, `␣reveal`, `␣reveals`, `公开`, `揭示`, `揭示了` | 3/152 (2%) | 16/81 (20%) | 3/138 (2%) | 2/158 (1%) | 1/43 (2%) | 14/73 (19%) |
| refuse (refusing) | unclear | `␣refusal`, `␣refusing`, `␣refused`, `␣refuse`, `␣refuses`, `␣refus`, `拒绝`, `拒绝了`, `␣decline`, `␣declines`, `␣declined` | 0/152 (0%) | 18/81 (22%) | 1/138 (1%) | 0/158 (0%) | 0/43 (0%) | 18/73 (25%) |
| blame (blaming) | unclear | `␣blaming`, `␣blame`, `␣blames`, `␣blamed` | 15/152 (10%) | 3/81 (4%) | 1/138 (1%) | 0/158 (0%) | 1/43 (2%) | 2/73 (3%) |
| mislead (leading someone to a wrong belief) | lie | `␣misleading`, `误导`, `误导性` | 9/152 (6%) | 6/81 (7%) | 0/138 (0%) | 2/158 (1%) | 0/43 (0%) | 4/73 (5%) |
| downplay (understating, playing down) | lie | `淡化` | 9/152 (6%) | 4/81 (5%) | 0/138 (0%) | 0/158 (0%) | 3/43 (7%) | 4/73 (5%) |
| exaggerate (overstating) | lie | `夸大`, `␣exaggerated` | 10/152 (7%) | 2/81 (2%) | 0/138 (0%) | 2/158 (1%) | 2/43 (5%) | 2/73 (3%) |
| I cannot ('I cannot' (declining stance)) | unclear | `我不能`, `我无法` | 0/152 (0%) | 11/81 (14%) | 0/138 (0%) | 4/158 (3%) | 0/43 (0%) | 11/73 (15%) |
| hide (hiding / hidden) | lie | `␣hide`, `␣hides`, `␣hiding`, `-hide`, `Hide`, `_hide`, `␣hidden`, `-hidden`, `Hidden`, `␣Hidden`, `隐藏`, `隐藏的` | 8/152 (5%) | 2/81 (2%) | 0/138 (0%) | 0/158 (0%) | 3/43 (7%) | 1/73 (1%) |
| hypothetical (hypothetical) | unclear | `␣hypothetical` | 2/152 (1%) | 8/81 (10%) | 4/138 (3%) | 19/158 (12%) | 2/43 (5%) | 8/73 (11%) |
| omit (leaving information out) | lie | `␣omit`, `omit`, `␣omission`, `省略` | 7/152 (5%) | 2/81 (2%) | 0/138 (0%) | 1/158 (1%) | 1/43 (2%) | 2/73 (3%) |
| pretend (pretending, disguising) | lie | `␣pretend`, `␣pretending`, `假装`, `伪装` | 7/152 (5%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 0/43 (0%) | 0/73 (0%) |
| confess (confessing, coming clean) | truth | `␣confess`, `␣confession`, `坦白`, `如实供述` | 0/152 (0%) | 6/81 (7%) | 3/138 (2%) | 0/158 (0%) | 0/43 (0%) | 6/73 (8%) |
| role-play (playing a role / persona) | unclear | `␣persona`, `␣personas`, `␣Persona`, `Persona`, `扮演` | 4/152 (3%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 4/43 (9%) | 1/73 (1%) |
| evade (evading, dodging) | lie | `␣evasion`, `回避` | 4/152 (3%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 1/43 (2%) | 0/73 (0%) |
| transparent (being transparent) | truth | `␣transparency`, `-transparent`, `␣transparent`, `␣Transparency`, `透明`, `透明度` | 0/152 (0%) | 4/81 (5%) | 0/138 (0%) | 2/158 (1%) | 0/43 (0%) | 4/73 (5%) |
| outwardly (on the surface / outwardly) | unclear | `表面上` | 3/152 (2%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 1/43 (2%) | 1/73 (1%) |
| inaccurate (inaccurate) | lie | `准确性和`, `不准确` | 2/152 (1%) | 2/81 (2%) | 10/138 (7%) | 19/158 (12%) | 0/43 (0%) | 2/73 (3%) |
| subjective (being subjective) | unclear | `主观` | 2/152 (1%) | 1/81 (1%) | 0/138 (0%) | 5/158 (3%) | 0/43 (0%) | 1/73 (1%) |
| withhold (keeping information back) | lie | `␣withholding` | 2/152 (1%) | 0/81 (0%) | 1/138 (1%) | 0/158 (0%) | 1/43 (2%) | 0/73 (0%) |
| ethical (ethical, moral) | unclear | `␣ethical`, `␣ethics`, `伦理`, `␣moral` | 0/152 (0%) | 2/81 (2%) | 0/138 (0%) | 0/158 (0%) | 0/43 (0%) | 2/73 (3%) |
| simulated (simulated / simulation) | unclear | `␣simulated`, `模拟` | 0/152 (0%) | 2/81 (2%) | 2/138 (1%) | 1/158 (1%) | 0/43 (0%) | 2/73 (3%) |
| dishonest (not honest, insincere) | lie | `␣dishonest` | 1/152 (1%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 0/43 (0%) | 0/73 (0%) |
| secret (kept secret, hidden, confidential) | lie | `␣hidden`, `Hidden`, `␣Hidden`, `-hidden`, `隐藏的` | 0/152 (0%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 0/43 (0%) | 0/73 (0%) |
| perfunctory (perfunctory, going through the motions) | unclear | `敷衍` | 0/152 (0%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 0/43 (0%) | 1/73 (1%) |

Not in the draft: deny (excluded: admit / deny / acknowledge); admit (excluded: admit / deny / acknowledge); false (excluded: the question's own word); truth (excluded: truth from the question on)

## preans_slot2

| family | side | members | lies | truths | no-pressure truths | unrelated | lies that deny | truths that deny |
|---|---|---|---|---|---|---|---|---|
| fact (fact, factual) | truth | `␣fact`, `␣reality`, `␣facts`, `Fact`, `fact`, `␣Fact`, `␣Reality`, `␣Facts`, `Reality`, `_fact`, `␣realities`, `␣FACT`, `FACT`, `␣factual`, `facts`, `␣realidad`, `实际`, `符合`, `现实`, `事实`, `实际上`, `实际情况`, `事实上`, `的事实`, `的实际`, `实际的`, `是否符合`, `现实中`, `的现实`, `实际上是`, `根据实际情况`, `与实际`, `犯罪事实`, `与现实`, `事实和`, `上述事实`, `␣realtà`, `␣reales` | 120/152 (79%) | 46/81 (57%) | 134/138 (97%) | 77/158 (49%) | 29/43 (67%) | 39/73 (53%) |
| deliberate (doing it on purpose, knowingly) | unclear | `明知`, `故意`, `刻意`, `有意`, `␣intentionally`, `␣intentional`, `␣deliberately`, `␣deliberate`, `␣knowingly` | 111/152 (73%) | 35/81 (43%) | 33/138 (24%) | 3/158 (2%) | 26/43 (60%) | 31/73 (42%) |
| true (true, real) | truth | `␣true`, `true`, `␣real`, `True`, `␣True`, `real`, `␣TRUE`, `=true`, `_real`, `,true`, `␣genuine`, `␣REAL`, `.real`, `.True`, `>true`, `␣genuinely`, `真`, `成立`, `真正`, `真实`, `真实性`, `确实`, `真正的`, `的确`, `真实的`, `是真的`, `真實`, `的真`, `确实是`, `的真实`, `属实`, `的真实性`, `的真正` | 104/152 (68%) | 36/81 (44%) | 126/138 (91%) | 51/158 (32%) | 27/43 (63%) | 29/73 (40%) |
| knowingly (knowing full well) | unclear | `明知`, `␣knowingly` | 94/152 (62%) | 28/81 (35%) | 33/138 (24%) | 0/158 (0%) | 22/43 (51%) | 24/73 (33%) |
| fabricate (making up false content, fake or fictional) | lie | `虚构`, `␣fabricated`, `␣fabrication`, `␣invented`, `凭空`, `伪造`, `作假`, `fake`, `␣fake`, `Fake`, `fiction`, `␣fiction`, `␣fictional`, `-fiction`, `␣Fiction` | 65/152 (43%) | 36/81 (44%) | 13/138 (9%) | 28/158 (18%) | 22/43 (51%) | 34/73 (47%) |
| role-play (playing a role / persona) | unclear | `␣persona`, `␣personas`, `␣Persona`, `persona`, `Persona`, `␣Personas`, `扮演`, `角色扮演` | 62/152 (41%) | 38/81 (47%) | 1/138 (1%) | 2/158 (1%) | 28/43 (65%) | 34/73 (47%) |
| objective (being objective) | unclear | `客观`, `␣objective` | 78/152 (51%) | 20/81 (25%) | 53/138 (38%) | 3/158 (2%) | 23/43 (53%) | 16/73 (22%) |
| conceal (hiding or covering up information) | lie | `隐瞒`, `掩盖`, `掩饰`, `␣conceal`, `␣concealed`, `␣masking`, `␣hiding`, `␣hide`, `␣hides`, `Hide`, `隐藏`, `隐藏着`, `掩`, `遮`, `隐` | 77/152 (51%) | 19/81 (23%) | 1/138 (1%) | 0/158 (0%) | 19/43 (44%) | 16/73 (22%) |
| fiction (fiction / fictional) | unclear | `fiction`, `␣fiction`, `␣Fiction`, `-fiction`, `␣fictional`, `␣fict`, `虚构`, `架空` | 58/152 (38%) | 36/81 (44%) | 13/138 (9%) | 28/158 (18%) | 21/43 (49%) | 34/73 (47%) |
| honest (being honest, truthful) | truth | `诚实`, `诚`, `诚信`, `坦诚`, `␣truthful`, `␣honest`, `␣honesty`, `如实`, `实事求是` | 64/152 (42%) | 17/81 (21%) | 2/138 (1%) | 18/158 (11%) | 11/43 (26%) | 14/73 (19%) |
| conceal (withholding or concealing the truth) | lie | `␣conceal`, `␣concealed`, `隐瞒`, `瞒` | 53/152 (35%) | 16/81 (20%) | 0/138 (0%) | 0/158 (0%) | 10/43 (23%) | 13/73 (18%) |
| secret (kept secret, hidden, confidential) | lie | `␣secret`, `secret`, `␣Secret`, `Secret`, `_secret`, `-secret`, `␣secretly`, `秘密`, `的秘密`, `私下`, `暗中`, `机密`, `␣confidential`, `␣hidden`, `hidden`, `Hidden`, `隐藏的`, `隐蔽`, `幕后`, `内幕` | 54/152 (36%) | 14/81 (17%) | 1/138 (1%) | 0/158 (0%) | 18/43 (42%) | 11/73 (15%) |
| accurate (accurate) | truth | `␣accurate`, `␣accuracy`, `␣accurately`, `accuracy`, `准确`, `准确的`, `准确地` | 32/152 (21%) | 13/81 (16%) | 56/138 (41%) | 42/158 (27%) | 4/43 (9%) | 12/73 (16%) |
| hide (hiding / hidden) | lie | `␣hide`, `␣hides`, `␣hiding`, `Hide`, `␣hidden`, `hidden`, `Hidden`, `隐藏`, `隐藏的`, `隐藏着`, `隐蔽` | 36/152 (24%) | 8/81 (10%) | 1/138 (1%) | 0/158 (0%) | 16/43 (37%) | 7/73 (10%) |
| violate (violating, going against) | unclear | `违背`, `违反`, `违反了`, `␣violate`, `␣violates`, `␣violated`, `␣violating` | 21/152 (14%) | 21/81 (26%) | 1/138 (1%) | 0/158 (0%) | 4/43 (9%) | 21/73 (29%) |
| violate (violating / going against (a principle)) | unclear | `违背`, `违反`, `违反了` | 21/152 (14%) | 21/81 (26%) | 1/138 (1%) | 0/158 (0%) | 4/43 (9%) | 21/73 (29%) |
| hypothetical (hypothetical) | unclear | `␣hypothetical` | 17/152 (11%) | 23/81 (28%) | 7/138 (5%) | 15/158 (9%) | 11/43 (26%) | 23/73 (32%) |
| contradict (contradicting, being contrary to) | unclear | `␣contrad`, `␣contradict`, `␣contradictory`, `␣contradiction`, `␣contradictions`, `␣contradd`, `矛盾`, `矛盾的`, `␣contrary`, `相反`, `相反的` | 15/152 (10%) | 23/81 (28%) | 26/138 (19%) | 3/158 (2%) | 3/43 (7%) | 21/73 (29%) |
| cover up (covering up or masking something) | lie | `掩盖`, `掩饰`, `␣masking` | 28/152 (18%) | 2/81 (2%) | 0/138 (0%) | 0/158 (0%) | 4/43 (9%) | 2/73 (3%) |
| ethical (ethical, moral) | unclear | `␣ethical`, `ethical`, `␣ethics`, `␣Ethics`, `伦理`, `道德`, `的道德`, `职业道德`, `␣moral`, `␣morally`, `␣morality` | 11/152 (7%) | 16/81 (20%) | 0/138 (0%) | 0/158 (0%) | 3/43 (7%) | 15/73 (21%) |
| fake (fake / falsified) | lie | `fake`, `␣fake`, `Fake`, `作假` | 24/152 (16%) | 1/81 (1%) | 1/138 (1%) | 1/158 (1%) | 6/43 (14%) | 1/73 (1%) |
| simulated (simulated / simulation) | unclear | `␣simulated`, `␣simulation`, `␣Simulation`, `模拟` | 12/152 (8%) | 10/81 (12%) | 1/138 (1%) | 3/158 (2%) | 9/43 (21%) | 10/73 (14%) |
| outwardly (on the surface / outwardly) | unclear | `表面上` | 15/152 (10%) | 6/81 (7%) | 0/138 (0%) | 0/158 (0%) | 6/43 (14%) | 5/73 (7%) |
| deceive (the act of deceiving) | lie | `欺骗`, `␣deception`, `␣deceptive`, `哄` | 17/152 (11%) | 3/81 (4%) | 0/138 (0%) | 2/158 (1%) | 4/43 (9%) | 3/73 (4%) |
| wrong (wrong, mistaken) | lie | `␣error`, `␣wrong`, `错`, `错误`, `错了`, `没错`, `是非`, `的错误`, `是错误的` | 9/152 (6%) | 11/81 (14%) | 8/138 (6%) | 16/158 (10%) | 4/43 (9%) | 10/73 (14%) |
| unethical (unethical, immoral) | unclear | `␣unethical`, `␣immoral` | 3/152 (2%) | 13/81 (16%) | 0/138 (0%) | 0/158 (0%) | 1/43 (2%) | 13/73 (18%) |
| lie (telling a lie) | lie | `谎言`, `谎`, `撒谎`, `说谎`, `␣거짓`, `␣lie`, `␣lies`, `␣lying`, `␣mentira` | 10/152 (7%) | 3/81 (4%) | 0/138 (0%) | 0/158 (0%) | 3/43 (7%) | 3/73 (4%) |
| incorrect (incorrect) | lie | `␣incorrect`, `␣incorrectly`, `不符合`, `有误`, `错误的是` | 2/152 (1%) | 11/81 (14%) | 3/138 (2%) | 11/158 (7%) | 1/43 (2%) | 11/73 (15%) |
| claim (claiming, asserting) | unclear | `␣claim`, `␣claims`, `␣claiming`, `␣Claim`, `claim`, `␣claimed`, `Claim`, `␣Claims`, `␣CLAIM`, `claims`, `Claims`, `CLAIM`, `_claim`, `声称`, `宣称`, `␣assert`, `assert`, `_assert`, `␣asserting`, `␣assertions`, `␣Assert`, `␣assertion`, `␣asserts`, `_ASSERT`, `.assert`, `␣asserted`, `Assert`, `/assert` | 7/152 (5%) | 3/81 (4%) | 69/138 (50%) | 5/158 (3%) | 2/43 (5%) | 3/73 (4%) |
| fabricate (making something up) | lie | `␣fabricated`, `␣fabrication`, `␣invented`, `伪造`, `凭空` | 10/152 (7%) | 0/81 (0%) | 2/138 (1%) | 7/158 (4%) | 4/43 (9%) | 0/73 (0%) |
| disclose (disclosing, revealing) | truth | `␣disclosed`, `信息披露`, `披露`, `揭露`, `公开` | 4/152 (3%) | 5/81 (6%) | 2/138 (1%) | 0/158 (0%) | 3/43 (7%) | 4/73 (5%) |
| imply (implying, suggesting indirectly) | unclear | `␣implied`, `␣implicitly`, `␣implicit`, `暗示`, `隐含` | 5/152 (3%) | 2/81 (2%) | 1/138 (1%) | 2/158 (1%) | 1/43 (2%) | 2/73 (3%) |
| mislead (leading someone to a wrong belief) | lie | `␣misleading`, `误导` | 3/152 (2%) | 2/81 (2%) | 2/138 (1%) | 0/158 (0%) | 1/43 (2%) | 2/73 (3%) |
| correct (correct) | truth | `valid`, `␣valid`, `␣correct`, `␣Valid`, `␣correctly`, `correct`, `␣correction`, `_correct`, `Correct`, `␣corrected`, `␣Correct`, `␣corrections`, `␣correctness`, `␣correctamente`, `␣correcting`, `␣Corrections`, `正确`, `正确的`, `正确的是`, `正确答案`, `纠正`, `的正确`, `无误`, `是正确的`, `正确地`, `是否正确` | 0/152 (0%) | 5/81 (6%) | 51/138 (37%) | 107/158 (68%) | 0/43 (0%) | 4/73 (5%) |
| withhold (keeping information back) | lie | `␣withholding`, `␣withheld`, `␣withhold` | 3/152 (2%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 2/43 (5%) | 1/73 (1%) |
| refuse (refusing) | unclear | `␣refusal`, `␣refusing`, `␣refused`, `␣refuse`, `␣refuses`, `␣refus`, `拒绝`, `拒绝了`, `␣decline`, `␣declines`, `␣declined` | 0/152 (0%) | 4/81 (5%) | 0/138 (0%) | 4/158 (3%) | 0/43 (0%) | 4/73 (5%) |
| pretend (pretending, disguising) | lie | `伪装` | 3/152 (2%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 1/43 (2%) | 0/73 (0%) |
| exaggerate (overstating) | lie | `夸大` | 2/152 (1%) | 1/81 (1%) | 1/138 (1%) | 0/158 (0%) | 0/43 (0%) | 1/73 (1%) |
| distort (twisting the facts) | lie | `扭曲` | 2/152 (1%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 0/43 (0%) | 0/73 (0%) |
| subjective (being subjective) | unclear | `主观` | 2/152 (1%) | 0/81 (0%) | 1/138 (1%) | 3/158 (2%) | 2/43 (5%) | 0/73 (0%) |
| omit (leaving information out) | lie | `␣omit`, `␣omission` | 1/152 (1%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 1/43 (2%) | 0/73 (0%) |
| evade (evading, dodging) | lie | `␣evasion`, `回避` | 1/152 (1%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 1/43 (2%) | 0/73 (0%) |
| manipulate (manipulating) | lie | `␣manipulation` | 0/152 (0%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 0/43 (0%) | 1/73 (1%) |
| I cannot ('I cannot' (declining stance)) | unclear | `我不能` | 0/152 (0%) | 1/81 (1%) | 0/138 (0%) | 5/158 (3%) | 0/43 (0%) | 1/73 (1%) |

Not in the draft: deny (excluded: admit / deny / acknowledge); admit (excluded: admit / deny / acknowledge); perfunctory (held back: no undisputed member left); false (excluded: the question's own word); truth (excluded: truth from the question on)

## preans_slot3

| family | side | members | lies | truths | no-pressure truths | unrelated | lies that deny | truths that deny |
|---|---|---|---|---|---|---|---|---|
| disclose (disclosing, revealing) | truth | `公开`, `公布` | 107/152 (70%) | 57/81 (70%) | 36/138 (26%) | 48/158 (30%) | 22/43 (51%) | 52/73 (71%) |
| refuse (refusing) | unclear | `␣refusal`, `␣refusing`, `␣refuse`, `␣refuses`, `␣refus` | 53/152 (35%) | 7/81 (9%) | 4/138 (3%) | 0/158 (0%) | 13/43 (30%) | 5/73 (7%) |
| I cannot ('I cannot' (declining stance)) | unclear | `我不能`, `我无法` | 33/152 (22%) | 7/81 (9%) | 0/138 (0%) | 0/158 (0%) | 15/43 (35%) | 7/73 (10%) |
| apologize (being sorry) | unclear | `抱歉` | 24/152 (16%) | 14/81 (17%) | 8/138 (6%) | 38/158 (24%) | 14/43 (33%) | 13/73 (18%) |
| law-abiding (obeying the law) | unclear | `守法` | 28/152 (18%) | 10/81 (12%) | 27/138 (20%) | 3/158 (2%) | 2/43 (5%) | 10/73 (14%) |
| true (true, real) | truth | `␣true`, `true`, `True`, `␣True`, `.True`, `真` | 3/152 (2%) | 2/81 (2%) | 29/138 (21%) | 59/158 (37%) | 0/43 (0%) | 2/73 (3%) |
| fabricate (making up false content, fake or fictional) | lie | `fiction` | 1/152 (1%) | 2/81 (2%) | 0/138 (0%) | 0/158 (0%) | 1/43 (2%) | 2/73 (3%) |
| violate (violating, going against) | unclear | `违背` | 0/152 (0%) | 3/81 (4%) | 3/138 (2%) | 0/158 (0%) | 0/43 (0%) | 3/73 (4%) |
| claim (claiming, asserting) | unclear | `␣assert` | 2/152 (1%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 2/43 (5%) | 1/73 (1%) |
| ethical (ethical, moral) | unclear | `␣ethical`, `伦理` | 3/152 (2%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 0/43 (0%) | 0/73 (0%) |
| fact (fact, factual) | truth | `FACT` | 2/152 (1%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 1/43 (2%) | 0/73 (0%) |
| secret (kept secret, hidden, confidential) | lie | `秘密` | 1/152 (1%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 1/43 (2%) | 0/73 (0%) |
| confess (confessing, coming clean) | truth | `坦白` | 1/152 (1%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 0/43 (0%) | 0/73 (0%) |
| conceal (to conceal, to hide) | lie | `掩` | 0/152 (0%) | 0/81 (0%) | 0/138 (0%) | 3/158 (2%) | 0/43 (0%) | 0/73 (0%) |
| correct (correct) | truth | `␣correct`, `正确` | 0/152 (0%) | 0/81 (0%) | 4/138 (3%) | 1/158 (1%) | 0/43 (0%) | 0/73 (0%) |
| wrong (wrong, mistaken) | lie | `␣wrong`, `错了`, `没错`, `对错` | 0/152 (0%) | 0/81 (0%) | 5/138 (4%) | 3/158 (2%) | 0/43 (0%) | 0/73 (0%) |

Not in the draft: false (excluded: the question's own word)

## preans_slot4

| family | side | members | lies | truths | no-pressure truths | unrelated | lies that deny | truths that deny |
|---|---|---|---|---|---|---|---|---|
| true (true, real) | truth | `␣true`, `true`, `␣real`, `True`, `␣True`, `␣TRUE`, `_true`, `TRUE`, `真`, `成立`, `真实`, `确实`, `的确`, `真实的`, `确实是`, `的真实`, `的真实性` | 144/152 (95%) | 78/81 (96%) | 115/138 (83%) | 53/158 (34%) | 35/43 (81%) | 70/73 (96%) |
| honest (being honest, truthful) | truth | `诚实`, `诚`, `诚信`, `坦诚`, `␣truthful`, `␣honest`, `如实`, `实事求是` | 117/152 (77%) | 37/81 (46%) | 7/138 (5%) | 2/158 (1%) | 33/43 (77%) | 32/73 (44%) |
| objective (being objective) | unclear | `客观`, `␣objectively` | 93/152 (61%) | 21/81 (26%) | 6/138 (4%) | 0/158 (0%) | 23/43 (53%) | 19/73 (26%) |
| fact (fact, factual) | truth | `␣fact`, `␣reality`, `␣facts`, `Fact`, `␣FACT`, `␣factual`, `实际`, `符合`, `事实`, `实际上`, `实际情况`, `根据实际情况` | 67/152 (44%) | 38/81 (47%) | 33/138 (24%) | 17/158 (11%) | 10/43 (23%) | 32/73 (44%) |
| fabricate (making up false content, fake or fictional) | lie | `虚构`, `␣invented`, `␣invent`, `fiction`, `␣fiction`, `␣fictional`, `-fiction`, `␣Fiction`, `␣fict`, `架空` | 53/152 (35%) | 18/81 (22%) | 5/138 (4%) | 14/158 (9%) | 8/43 (19%) | 14/73 (19%) |
| deliberate (doing it on purpose, knowingly) | unclear | `明知`, `故意`, `故意的`, `␣intentionally`, `␣intentional`, `␣deliberately`, `␣deliberate` | 60/152 (39%) | 8/81 (10%) | 3/138 (2%) | 1/158 (1%) | 8/43 (19%) | 5/73 (7%) |
| knowingly (knowing full well) | unclear | `明知` | 39/152 (26%) | 3/81 (4%) | 3/138 (2%) | 0/158 (0%) | 3/43 (7%) | 2/73 (3%) |
| deceive (the act of deceiving) | lie | `欺骗`, `␣deception`, `␣deceptive` | 27/152 (18%) | 5/81 (6%) | 1/138 (1%) | 0/158 (0%) | 7/43 (16%) | 2/73 (3%) |
| accurate (accurate) | truth | `␣accurate`, `␣accuracy`, `准确`, `准确的` | 8/152 (5%) | 16/81 (20%) | 17/138 (12%) | 4/158 (3%) | 1/43 (2%) | 15/73 (21%) |
| correct (correct) | truth | `valid`, `␣correct`, `␣correction`, `Correct`, `␣Correct`, `正确`, `正确的`, `纠正`, `无误`, `是正确的`, `是否正确` | 4/152 (3%) | 19/81 (23%) | 116/138 (84%) | 27/158 (17%) | 2/43 (5%) | 19/73 (26%) |
| lie (telling a lie) | lie | `谎言`, `撒谎`, `说谎` | 17/152 (11%) | 3/81 (4%) | 0/138 (0%) | 0/158 (0%) | 4/43 (9%) | 1/73 (1%) |
| I cannot ('I cannot' (declining stance)) | unclear | `我不能`, `我无法` | 15/152 (10%) | 3/81 (4%) | 0/138 (0%) | 9/158 (6%) | 4/43 (9%) | 3/73 (4%) |
| simulated (simulated / simulation) | unclear | `␣simulated`, `␣simulation`, `模拟` | 13/152 (9%) | 5/81 (6%) | 0/138 (0%) | 0/158 (0%) | 3/43 (7%) | 4/73 (5%) |
| conceal (hiding or covering up information) | lie | `隐瞒` | 16/152 (11%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 2/43 (5%) | 0/73 (0%) |
| subjective (being subjective) | unclear | `主观` | 14/152 (9%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 7/43 (16%) | 1/73 (1%) |
| hypothetical (hypothetical) | unclear | `␣hypothetical` | 9/152 (6%) | 4/81 (5%) | 1/138 (1%) | 0/158 (0%) | 2/43 (5%) | 4/73 (5%) |
| contradict (contradicting, being contrary to) | unclear | `␣contrad`, `␣contradict`, `相反` | 7/152 (5%) | 3/81 (4%) | 28/138 (20%) | 0/158 (0%) | 6/43 (14%) | 3/73 (4%) |
| violate (violating, going against) | unclear | `违背`, `违反`, `违反了` | 7/152 (5%) | 1/81 (1%) | 2/138 (1%) | 0/158 (0%) | 1/43 (2%) | 1/73 (1%) |
| claim (claiming, asserting) | unclear | `␣assert`, `assert` | 6/152 (4%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 6/43 (14%) | 1/73 (1%) |
| self-examination (checking or critiquing one's own reply) | unclear | `反思`, `自查` | 5/152 (3%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 5/43 (12%) | 1/73 (1%) |
| wrong (wrong, mistaken) | lie | `error`, `␣error`, `错误`, `不对`, `错了`, `是非`, `指正`, `是错误的` | 4/152 (3%) | 1/81 (1%) | 3/138 (2%) | 29/158 (18%) | 1/43 (2%) | 1/73 (1%) |
| dishonest (not honest, insincere) | lie | `␣dishonest`, `虚伪` | 4/152 (3%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 0/43 (0%) | 0/73 (0%) |
| outwardly (on the surface / outwardly) | unclear | `表面上` | 2/152 (1%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 0/43 (0%) | 0/73 (0%) |
| incorrect (incorrect) | lie | `␣incorrect`, `␣inaccur`, `不符合`, `错误的是` | 1/152 (1%) | 1/81 (1%) | 6/138 (4%) | 2/158 (1%) | 0/43 (0%) | 0/73 (0%) |
| confess (confessing, coming clean) | truth | `坦白` | 1/152 (1%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 0/43 (0%) | 0/73 (0%) |
| disclose (disclosing, revealing) | truth | `公开` | 1/152 (1%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 0/43 (0%) | 0/73 (0%) |
| imply (implying, suggesting indirectly) | unclear | `隐含` | 1/152 (1%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 1/43 (2%) | 0/73 (0%) |
| refuse (refusing) | unclear | `拒绝` | 0/152 (0%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 0/43 (0%) | 1/73 (1%) |
| apologize (being sorry) | unclear | `抱歉` | 1/152 (1%) | 0/81 (0%) | 0/138 (0%) | 2/158 (1%) | 1/43 (2%) | 0/73 (0%) |
| fabricate (making something up) | lie | `␣invented`, `␣invent` | 1/152 (1%) | 0/81 (0%) | 0/138 (0%) | 1/158 (1%) | 0/43 (0%) | 0/73 (0%) |
| contradict (contradicting / contradiction) | unclear | `␣contradict` | 0/152 (0%) | 1/81 (1%) | 1/138 (1%) | 0/158 (0%) | 0/43 (0%) | 1/73 (1%) |

Not in the draft: deny (excluded: admit / deny / acknowledge); admit (excluded: admit / deny / acknowledge); fake (held back: no undisputed member left); false (excluded: the question's own word); truth (excluded: truth from the question on)
