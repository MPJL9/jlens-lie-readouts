# Draft families: qwen3.6-27b, logit lens, part Q2_after, group preans

Written by `scripts/apply_family_decisions.py` (2026-10-01; draft, not frozen). Counts are `present / transcripts (share)`
on the build split.

## preans_slot0

| family | side | members | lies | truths | no-pressure truths | unrelated | lies that deny | truths that deny |
|---|---|---|---|---|---|---|---|---|
| wrong (wrong, mistaken) | lie | `是非`, `指正` | 66/152 (43%) | 38/81 (47%) | 52/138 (38%) | 130/158 (82%) | 14/47 (30%) | 37/77 (48%) |
| objective (objectivity) | unclear | `客观` | 50/152 (33%) | 10/81 (12%) | 4/138 (3%) | 3/158 (2%) | 4/47 (9%) | 9/77 (12%) |
| knowing (with knowledge; knowingly) | unclear | `明知` | 7/152 (5%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 0/47 (0%) | 0/77 (0%) |
| candid / frank (candid, frank, straightforward) | truth | `␣blunt` | 2/152 (1%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 2/47 (4%) | 1/77 (1%) |
| integrity (integrity; uprightness) | truth | `正直` | 1/152 (1%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 0/47 (0%) | 1/77 (1%) |
| law-abiding (abiding by the law) | unclear | `守法` | 0/152 (0%) | 2/81 (2%) | 0/138 (0%) | 0/158 (0%) | 0/47 (0%) | 2/77 (3%) |
| ethics (ethics; morality) | unclear | `伦理` | 1/152 (1%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 0/47 (0%) | 0/77 (0%) |
| conceal (to conceal, to hide) | lie | `藏`, `掩` | 0/152 (0%) | 0/81 (0%) | 1/138 (1%) | 2/158 (1%) | 0/47 (0%) | 0/77 (0%) |

Not in the draft: perfunctory (held back: no undisputed member left); admit (excluded: admit / deny / acknowledge)

## preans_slot1

| family | side | members | lies | truths | no-pressure truths | unrelated | lies that deny | truths that deny |
|---|---|---|---|---|---|---|---|---|
| fact (fact(s); factual) | unclear | `事实`, `␣fact`, `␣factual`, `事实上`, `␣facts`, `事实和`, `的事实`, `␣Fact`, `Fact`, `fact`, `␣Facts`, `␣FACT`, `facts`, `FACT`, `_fact`, `认定事实`, `实际情况`, `根据实际情况`, `␣realities`, `␣realidad`, `实际`, `符合`, `现实`, `的实际`, `实际的`, `是否符合`, `现实中`, `的现实`, `求实`, `与现实`, `上述事实`, `␣realtà` | 152/152 (100%) | 67/81 (83%) | 129/138 (93%) | 108/158 (68%) | 47/47 (100%) | 63/77 (82%) |
| truthful (telling the truth) | truth | `␣truthful`, `如实`, `实事求是`, `如实供述` | 139/152 (91%) | 65/81 (80%) | 117/138 (85%) | 57/158 (36%) | 43/47 (91%) | 63/77 (82%) |
| conceal (concealing information) | lie | `隐瞒`, `␣conceal`, `␣concealed`, `瞒`, `藏`, `掩`, `遮`, `隐` | 143/152 (94%) | 47/81 (58%) | 54/138 (39%) | 3/158 (2%) | 45/47 (96%) | 44/77 (57%) |
| conceal (concealing the truth) | lie | `隐瞒`, `掩盖`, `掩饰`, `␣conceal`, `␣concealed`, `瞒`, `遮掩`, `隐匿` | 143/152 (94%) | 47/81 (58%) | 55/138 (40%) | 1/158 (1%) | 44/47 (94%) | 44/77 (57%) |
| knowing (with knowledge; knowingly) | unclear | `明知`, `知情`, `␣knowingly`, `␣knowing`, `␣Knowing`, `Knowing` | 143/152 (94%) | 44/81 (54%) | 100/138 (72%) | 36/158 (23%) | 40/47 (85%) | 41/77 (53%) |
| false (false, untrue) | lie | `␣false`, `␣False`, `false`, `False`, `␣FALSE`, `␣fals`, `␣falsely`, `␣untrue`, `/false`, `假`, `虚假`, `假的`, `真假` | 145/152 (95%) | 31/81 (38%) | 85/138 (62%) | 44/158 (28%) | 41/47 (87%) | 27/77 (35%) |
| lie (telling a lie) | lie | `谎言`, `撒谎`, `说谎`, `谎`, `␣lies`, `␣lie`, `␣lied`, `␣lying`, `lying`, `␣mentira`, `␣거짓`, `␣Lie`, `␣liar`, `Lie`, `lies`, `␣Lies`, `␣falsehood` | 137/152 (90%) | 17/81 (21%) | 24/138 (17%) | 0/158 (0%) | 38/47 (81%) | 15/77 (19%) |
| cover up (covering up or masking something) | lie | `掩盖`, `掩饰`, `遮盖`, `␣masking`, `遮住`, `遮掩`, `遮蔽`, `␣cover`, `␣masked`, `mask`, `cover`, `␣Cover` | 125/152 (82%) | 22/81 (27%) | 21/138 (15%) | 1/158 (1%) | 35/47 (74%) | 20/77 (26%) |
| fabricate (making something up) | lie | `虚构`, `␣fabricated`, `␣fabrication`, `凭空`, `␣invented`, `␣invent`, `伪造`, `␣invention`, `invent`, `␣inventions`, `␣Invent` | 103/152 (68%) | 24/81 (30%) | 85/138 (62%) | 73/158 (46%) | 21/47 (45%) | 21/77 (27%) |
| fiction (fiction; fictional) | unclear | `␣fictional`, `fiction`, `␣fiction`, `虚构` | 91/152 (60%) | 23/81 (28%) | 84/138 (61%) | 72/158 (46%) | 18/47 (38%) | 20/77 (26%) |
| mislead (misleading someone) | lie | `␣misleading`, `误导`, `误导性` | 83/152 (55%) | 18/81 (22%) | 8/138 (6%) | 15/158 (9%) | 20/47 (43%) | 15/77 (19%) |
| true (true, real) | truth | `␣true`, `true`, `␣real`, `True`, `␣True`, `real`, `_true`, `␣genuine`, `␣genuinely`, `真`, `成立`, `真实`, `真实性`, `确实`, `真实性负责`, `的确`, `真实的`, `是真的`, `的真`, `确实是`, `的真实`, `属实`, `的真实性` | 79/152 (52%) | 18/81 (22%) | 76/138 (55%) | 54/158 (34%) | 23/47 (49%) | 15/77 (19%) |
| deliberate (doing something on purpose) | unclear | `␣deliberately`, `故意`, `␣intentionally`, `刻意`, `␣deliberate`, `有意`, `␣intentional` | 71/152 (47%) | 17/81 (21%) | 19/138 (14%) | 61/158 (39%) | 15/47 (32%) | 15/77 (19%) |
| honest (honesty) | truth | `诚实`, `诚`, `␣honesty`, `␣honest`, `诚信`, `␣honestly`, `␣Honest`, `诚实守信` | 32/152 (21%) | 54/81 (67%) | 85/138 (62%) | 81/158 (51%) | 15/47 (32%) | 52/77 (68%) |
| misinformation (false information) | lie | `␣misinformation`, `虚假信息`, `不实` | 83/152 (55%) | 2/81 (2%) | 18/138 (13%) | 3/158 (2%) | 13/47 (28%) | 1/77 (1%) |
| wrong (wrong, mistaken) | lie | `␣error`, `␣wrong`, `错`, `错误`, `不对`, `错了`, `没错`, `是非`, `是错误的` | 69/152 (45%) | 15/81 (19%) | 13/138 (9%) | 18/158 (11%) | 16/47 (34%) | 11/77 (14%) |
| contradict (contradicting; contradiction) | unclear | `␣contradict`, `␣contrad`, `矛盾`, `␣contradictory`, `␣contradiction`, `␣contradictions`, `矛盾的` | 62/152 (41%) | 17/81 (21%) | 36/138 (26%) | 10/158 (6%) | 23/47 (49%) | 17/77 (22%) |
| reality (reality; the actual situation) | unclear | `实际情况`, `实际上`, `与实际`, `␣reality`, `根据实际情况`, `实际上是`, `␣Reality`, `Reality`, `但实际上` | 60/152 (39%) | 17/81 (21%) | 20/138 (14%) | 8/158 (5%) | 17/47 (36%) | 14/77 (18%) |
| objective (objectivity) | unclear | `客观`, `␣objectively`, `␣objective` | 49/152 (32%) | 22/81 (27%) | 30/138 (22%) | 15/158 (9%) | 20/47 (43%) | 21/77 (27%) |
| downplay (downplaying or glossing over) | lie | `淡化`, `␣gloss` | 47/152 (31%) | 15/81 (19%) | 3/138 (2%) | 3/158 (2%) | 18/47 (38%) | 15/77 (19%) |
| imply (implying; implicit) | unclear | `暗示`, `␣implying`, `␣imply`, `␣implies`, `␣implied`, `隐含`, `␣implication`, `␣implicitly`, `␣implicit`, `␣implications`, `␣implic`, `␣implica`, `implicitly`, `间接`, `␣indirect`, `␣indirectly`, `含蓄` | 31/152 (20%) | 28/81 (35%) | 19/138 (14%) | 11/158 (7%) | 11/47 (23%) | 27/77 (35%) |
| contrary (the opposite; contrary) | unclear | `␣contrary`, `相反`, `相反的` | 31/152 (20%) | 27/81 (33%) | 35/138 (25%) | 4/158 (3%) | 12/47 (26%) | 26/77 (34%) |
| omit (leaving something out) | lie | `␣omit`, `␣omission`, `omit`, `省略`, `␣omitted`, `␣OMIT` | 37/152 (24%) | 19/81 (23%) | 6/138 (4%) | 12/158 (8%) | 16/47 (34%) | 19/77 (25%) |
| fake (faking; fake) | lie | `fake`, `␣fake`, `作假` | 39/152 (26%) | 8/81 (10%) | 59/138 (43%) | 21/158 (13%) | 4/47 (9%) | 6/77 (8%) |
| violate (violating a rule or principle) | unclear | `违背`, `违反`, `违反了`, `␣violates` | 37/152 (24%) | 8/81 (10%) | 18/138 (13%) | 9/158 (6%) | 12/47 (26%) | 8/77 (10%) |
| withhold (withholding information) | lie | `␣withholding`, `␣withhold`, `␣withheld` | 28/152 (18%) | 15/81 (19%) | 4/138 (3%) | 0/158 (0%) | 16/47 (34%) | 15/77 (19%) |
| claim (claiming) | unclear | `声称`, `␣claim`, `␣claims`, `␣claiming`, `claim`, `␣Claim`, `␣claimed`, `␣Claims`, `Claim`, `claims`, `␣CLAIM`, `Claims`, `CLAIM` | 34/152 (22%) | 9/81 (11%) | 5/138 (4%) | 8/158 (5%) | 7/47 (15%) | 6/77 (8%) |
| hide (hiding; being hidden) | lie | `␣hiding`, `_hide`, `␣hide`, `隐藏`, `-hide`, `Hide`, `␣hides`, `hide`, `␣Hide`, `␣hidden`, `隐匿`, `藏着` | 37/152 (24%) | 4/81 (5%) | 1/138 (1%) | 1/158 (1%) | 16/47 (34%) | 4/77 (5%) |
| evade (evading) | lie | `␣evasion`, `回避`, `␣evade`, `␣dodge` | 27/152 (18%) | 10/81 (12%) | 1/138 (1%) | 0/158 (0%) | 15/47 (32%) | 10/77 (13%) |
| correct (fix) (correcting an error) | truth | `纠正`, `␣corrected`, `␣correction`, `␣correcting`, `␣corrective`, `␣corrections`, `␣Correction`, `Correction`, `␣Corrections`, `_correction`, `valid`, `␣valid`, `␣correct`, `␣Valid`, `␣correctly`, `correct`, `_correct`, `Correct`, `␣Correct`, `␣correctness`, `␣correctamente`, `正确`, `正确的`, `正确的是`, `正确答案`, `的正确`, `无误`, `是正确的`, `正确地`, `是否正确`, `是对的` | 5/152 (3%) | 32/81 (40%) | 82/138 (59%) | 90/158 (57%) | 4/47 (9%) | 31/77 (40%) |
| disclose (disclosing or revealing) | truth | `信息披露`, `揭露`, `␣disclosure`, `公开`, `披露`, `揭`, `␣disclose`, `␣disclosed`, `揭示`, `␣disclosures`, `␣Disclosure`, `␣reveal`, `␣revealing`, `揭示了` | 16/152 (11%) | 18/81 (22%) | 21/138 (15%) | 2/158 (1%) | 6/47 (13%) | 17/77 (22%) |
| accurate (accurate) | truth | `␣accur`, `␣accurate`, `␣accuracy`, `␣accurately`, `accuracy`, `accur`, `Accuracy`, `␣Accuracy`, `准确`, `准确性`, `准确的`, `准确地` | 8/152 (5%) | 26/81 (32%) | 87/138 (63%) | 85/158 (54%) | 4/47 (9%) | 26/77 (34%) |
| vague (being vague or ambiguous) | unclear | `␣vague`, `模糊`, `含糊`, `␣vaguely` | 22/152 (14%) | 11/81 (14%) | 0/138 (0%) | 3/158 (2%) | 8/47 (17%) | 9/77 (12%) |
| refuse (refusing or declining) | unclear | `␣refusal`, `拒绝`, `␣refusing`, `␣refused`, `␣refuse`, `␣refuses`, `␣refus`, `拒`, `拒絕`, `拒绝了`, `␣отказ`, `␣decline`, `␣declining`, `␣отказа`, `␣declined`, `␣declines`, `拒不` | 2/152 (1%) | 28/81 (35%) | 7/138 (5%) | 1/158 (1%) | 2/47 (4%) | 28/77 (36%) |
| euphemism (saying something indirectly or tactfully) | unclear | `委婉` | 9/152 (6%) | 18/81 (22%) | 5/138 (4%) | 0/158 (0%) | 8/47 (17%) | 18/77 (23%) |
| official line (an agreed messaging line) | unclear | `口径` | 24/152 (16%) | 2/81 (2%) | 0/138 (0%) | 0/158 (0%) | 10/47 (21%) | 2/77 (3%) |
| ostensibly (on the surface; ostensibly) | unclear | `表面上` | 18/152 (12%) | 7/81 (9%) | 10/138 (7%) | 1/158 (1%) | 9/47 (19%) | 6/77 (8%) |
| disclose (disclosing information) | truth | `信息披露`, `␣disclosure`, `披露`, `␣disclose`, `␣disclosed`, `␣disclosures`, `␣Disclosure`, `透露` | 13/152 (9%) | 10/81 (12%) | 13/138 (9%) | 1/158 (1%) | 5/47 (11%) | 10/77 (13%) |
| incorrect (incorrect) | lie | `␣incorrect`, `␣inaccur`, `␣incorrectly`, `␣inaccurate`, `␣Incorrect`, `错误的`, `不符合`, `有误`, `错误的是` | 8/152 (5%) | 15/81 (19%) | 16/138 (12%) | 53/158 (34%) | 3/47 (6%) | 15/77 (19%) |
| candid / frank (candid, frank, straightforward) | truth | `坦诚`, `␣straightforward`, `␣blunt`, `直言` | 0/152 (0%) | 21/81 (26%) | 35/138 (25%) | 54/158 (34%) | 0/47 (0%) | 21/77 (27%) |
| blame (blaming) | unclear | `␣blame`, `␣blames`, `␣blamed` | 17/152 (11%) | 2/81 (2%) | 0/138 (0%) | 0/158 (0%) | 1/47 (2%) | 2/77 (3%) |
| candid (being candid or frank) | truth | `坦诚` | 0/152 (0%) | 18/81 (22%) | 20/138 (14%) | 8/158 (5%) | 0/47 (0%) | 18/77 (23%) |
| integrity (integrity; uprightness) | truth | `正直`, `诚信` | 5/152 (3%) | 13/81 (16%) | 14/138 (10%) | 3/158 (2%) | 2/47 (4%) | 13/77 (17%) |
| framing (framing / spin) | unclear | `␣framing` | 9/152 (6%) | 8/81 (10%) | 3/138 (2%) | 2/158 (1%) | 4/47 (9%) | 6/77 (8%) |
| transparent (transparency) | truth | `透明`, `-transparent`, `␣transparency`, `␣transparent`, `透明的`, `透明度`, `␣Transparency` | 0/152 (0%) | 16/81 (20%) | 18/138 (13%) | 12/158 (8%) | 0/47 (0%) | 16/77 (21%) |
| exaggerate (exaggerating) | lie | `夸大`, `␣exaggerated` | 12/152 (8%) | 3/81 (4%) | 0/138 (0%) | 3/158 (2%) | 2/47 (4%) | 3/77 (4%) |
| confess (confessing) | truth | `坦白`, `如实供述` | 0/152 (0%) | 14/81 (17%) | 12/138 (9%) | 2/158 (1%) | 0/47 (0%) | 14/77 (18%) |
| comply (complying with rules or instructions) | unclear | `␣adherence`, `遵循`, `␣adher`, `␣compliance`, `合规` | 7/152 (5%) | 7/81 (9%) | 25/138 (18%) | 3/158 (2%) | 2/47 (4%) | 7/77 (9%) |
| inaccurate (inaccurate) | lie | `准确性和`, `不准确` | 8/152 (5%) | 6/81 (7%) | 6/138 (4%) | 35/158 (22%) | 3/47 (6%) | 6/77 (8%) |
| clarify (clarifying) | unclear | `澄清`, `␣clarify`, `␣clarification` | 3/152 (2%) | 9/81 (11%) | 13/138 (9%) | 10/158 (6%) | 2/47 (4%) | 8/77 (10%) |
| reveal (revealing, exposing) | truth | `揭露`, `揭`, `揭示`, `␣reveal`, `␣revealing`, `揭示了`, `␣exposing` | 1/152 (1%) | 11/81 (14%) | 13/138 (9%) | 0/158 (0%) | 1/47 (2%) | 11/77 (14%) |
| spin (putting a spin on facts) | lie | `␣spin`, `Spin`, `-spin`, `␣Spin`, `␣spins`, `spin`, `␣spinning`, `_spin` | 5/152 (3%) | 2/81 (2%) | 0/138 (0%) | 0/158 (0%) | 3/47 (6%) | 2/77 (3%) |
| ethics (ethics; morality) | unclear | `␣ethical`, `␣ethics`, `伦理`, `道德` | 0/152 (0%) | 6/81 (7%) | 0/138 (0%) | 0/158 (0%) | 0/47 (0%) | 6/77 (8%) |
| make public (making public, announcing) | truth | `公开` | 2/152 (1%) | 3/81 (4%) | 6/138 (4%) | 1/158 (1%) | 0/47 (0%) | 2/77 (3%) |
| pretend (pretending; disguise) | lie | `伪装`, `␣pretending` | 1/152 (1%) | 3/81 (4%) | 1/138 (1%) | 2/158 (1%) | 0/47 (0%) | 2/77 (3%) |
| distort (distorting) | lie | `␣distortion`, `␣distort`, `␣distorted`, `扭曲` | 3/152 (2%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 3/47 (6%) | 0/77 (0%) |
| secret (secrecy; something kept secret) | lie | `秘密`, `保密` | 1/152 (1%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 1/47 (2%) | 1/77 (1%) |
| manipulate (manipulating) | lie | `␣manipulated`, `␣manipulation` | 1/152 (1%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 1/47 (2%) | 1/77 (1%) |
| role-play (playing a role or persona) | unclear | `␣persona`, `␣personas`, `␣Persona`, `Persona`, `persona`, `␣Personas`, `扮演`, `角色扮演` | 0/152 (0%) | 2/81 (2%) | 9/138 (7%) | 5/158 (3%) | 0/47 (0%) | 2/77 (3%) |
| role-play / simulate (playing a role, simulating) | unclear | `扮演`, `角色扮演`, `模拟` | 0/152 (0%) | 2/81 (2%) | 10/138 (7%) | 7/158 (4%) | 0/47 (0%) | 2/77 (3%) |
| unaware (without knowledge) | unclear | `不知情` | 1/152 (1%) | 0/81 (0%) | 6/138 (4%) | 0/158 (0%) | 0/47 (0%) | 0/77 (0%) |
| good faith (good faith) | truth | `善意` | 0/152 (0%) | 1/81 (1%) | 8/138 (6%) | 0/158 (0%) | 0/47 (0%) | 1/77 (1%) |
| simulate (simulating) | unclear | `模拟` | 0/152 (0%) | 1/81 (1%) | 7/138 (5%) | 4/158 (3%) | 0/47 (0%) | 1/77 (1%) |
| leak (leaking information) | unclear | `泄露` | 0/152 (0%) | 1/81 (1%) | 1/138 (1%) | 0/158 (0%) | 0/47 (0%) | 1/77 (1%) |
| law-abiding / compliant (following law or rules) | unclear | `合规` | 0/152 (0%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 0/47 (0%) | 1/77 (1%) |
| truth (the truth) | truth | `求真` | 0/152 (0%) | 0/81 (0%) | 1/138 (1%) | 0/158 (0%) | 0/47 (0%) | 0/77 (0%) |

Not in the draft: coax / fool (held back: no undisputed member left); deny (excluded: admit / deny / acknowledge); perfunctory (held back: no undisputed member left); admit (excluded: admit / deny / acknowledge); deceive (excluded: the question's own word)

## preans_slot2

| family | side | members | lies | truths | no-pressure truths | unrelated | lies that deny | truths that deny |
|---|---|---|---|---|---|---|---|---|
| fact (fact(s); factual) | unclear | `␣fact`, `事实`, `的事实`, `␣facts`, `␣factual`, `事实上`, `fact`, `␣Fact`, `facts`, `␣Facts`, `事实和`, `Fact`, `␣FACT`, `FACT`, `_fact`, `上述事实`, `实际情况`, `根据实际情况`, `␣realities`, `␣realidad`, `实际`, `符合`, `现实`, `的实际`, `实际的`, `是否符合`, `现实中`, `的现实`, `犯罪事实`, `与现实`, `␣realtà`, `␣reale` | 110/152 (72%) | 39/81 (48%) | 130/138 (94%) | 81/158 (51%) | 32/47 (68%) | 35/77 (45%) |
| true (true, real) | truth | `␣true`, `true`, `␣real`, `True`, `␣True`, `real`, `␣TRUE`, `_real`, `_true`, `,true`, `␣genuine`, `␣REAL`, `.real`, `.True`, `␣genuinely`, `真`, `成立`, `真正`, `真实`, `真实性`, `确实`, `真正的`, `的确`, `真实的`, `是真的`, `真實`, `的真`, `确实是`, `的真实`, `属实`, `的真实性`, `的真正` | 107/152 (70%) | 28/81 (35%) | 114/138 (83%) | 44/158 (28%) | 31/47 (66%) | 26/77 (34%) |
| knowing (with knowledge; knowingly) | unclear | `明知`, `知情`, `␣knowing`, `␣knowingly`, `␣Knowing`, `Knowing` | 95/152 (62%) | 28/81 (35%) | 85/138 (62%) | 0/158 (0%) | 23/47 (49%) | 27/77 (35%) |
| reality (reality; the actual situation) | unclear | `实际情况`, `␣reality`, `␣Reality`, `实际上`, `Reality`, `但实际上`, `与实际`, `实际上是`, `根据实际情况` | 96/152 (63%) | 20/81 (25%) | 23/138 (17%) | 4/158 (3%) | 26/47 (55%) | 19/77 (25%) |
| objective (objectivity) | unclear | `客观`, `␣objective`, `␣objectively`, `␣Objective` | 66/152 (43%) | 17/81 (21%) | 63/138 (46%) | 16/158 (10%) | 25/47 (53%) | 16/77 (21%) |
| truthful (telling the truth) | truth | `如实`, `␣truthful`, `实事求是` | 51/152 (34%) | 22/81 (27%) | 7/138 (5%) | 3/158 (2%) | 11/47 (23%) | 21/77 (27%) |
| role-play (playing a role or persona) | unclear | `␣persona`, `␣personas`, `␣Persona`, `扮演`, `角色扮演`, `Persona`, `persona` | 42/152 (28%) | 27/81 (33%) | 7/138 (5%) | 1/158 (1%) | 19/47 (40%) | 25/77 (32%) |
| fiction (fiction; fictional) | unclear | `␣fictional`, `fiction`, `␣Fiction`, `-fiction`, `虚构` | 42/152 (28%) | 27/81 (33%) | 31/138 (22%) | 20/158 (13%) | 20/47 (43%) | 27/77 (35%) |
| conceal (concealing information) | lie | `隐瞒`, `␣concealed`, `␣conceal`, `瞒`, `掩盖`, `掩`, `隐` | 45/152 (30%) | 20/81 (25%) | 1/138 (1%) | 0/158 (0%) | 14/47 (30%) | 19/77 (25%) |
| deliberate (doing something on purpose) | unclear | `故意`, `␣intentionally`, `刻意`, `␣deliberately`, `␣intentional`, `␣deliberate`, `故意的` | 45/152 (30%) | 13/81 (16%) | 3/138 (2%) | 3/158 (2%) | 7/47 (15%) | 13/77 (17%) |
| secret (secrecy; something kept secret) | lie | `␣secret`, `私下`, `秘密`, `的秘密`, `secret`, `␣Secret`, `␣secretly`, `-secret`, `␣confidential`, `Secret`, `_secret`, `␣Confidential`, `保密`, `机密` | 47/152 (31%) | 7/81 (9%) | 2/138 (1%) | 0/158 (0%) | 15/47 (32%) | 6/77 (8%) |
| fabricate (making something up) | lie | `虚构`, `伪造`, `␣fabrication` | 32/152 (21%) | 22/81 (27%) | 29/138 (21%) | 20/158 (13%) | 14/47 (30%) | 22/77 (29%) |
| accurate (accurate) | truth | `␣accurate`, `␣accuracy`, `␣accurately`, `accur`, `准确`, `准确的`, `准确地` | 29/152 (19%) | 11/81 (14%) | 42/138 (30%) | 50/158 (32%) | 4/47 (9%) | 10/77 (13%) |
| contradict (contradicting; contradiction) | unclear | `矛盾`, `矛盾的`, `␣contrad`, `␣contradict`, `␣contradictory` | 21/152 (14%) | 16/81 (20%) | 17/138 (12%) | 1/158 (1%) | 7/47 (15%) | 16/77 (21%) |
| violate (violating a rule or principle) | unclear | `违背`, `违反`, `违反了`, `␣violates`, `␣violated`, `␣violate` | 17/152 (11%) | 19/81 (23%) | 3/138 (2%) | 0/158 (0%) | 3/47 (6%) | 19/77 (25%) |
| simulate (simulating) | unclear | `模拟`, `␣simulated`, `␣simulation`, `␣Simulation`, `Simulation`, `扮演`, `角色扮演` | 15/152 (10%) | 20/81 (25%) | 3/138 (2%) | 1/158 (1%) | 9/47 (19%) | 18/77 (23%) |
| private (private, done privately) | unclear | `私下`, `␣private`, `␣privately`, `private`, `␣Private`, `Private`, `PRIVATE`, `-private`, `_private`, `私密` | 29/152 (19%) | 6/81 (7%) | 0/138 (0%) | 0/158 (0%) | 7/47 (15%) | 5/77 (6%) |
| honest (honesty) | truth | `诚实`, `诚`, `␣honest`, `␣honesty`, `诚信` | 19/152 (12%) | 13/81 (16%) | 2/138 (1%) | 11/158 (7%) | 4/47 (9%) | 13/77 (17%) |
| false (false, untrue) | lie | `␣false`, `␣False`, `(false`, `false`, `False`, `␣FALSE`, `=false`, `FALSE`, `>false`, `␣fals`, `␣falsely`, `/false`, `假`, `虚假`, `假的`, `真假`, `不实`, `虚假信息` | 19/152 (12%) | 9/81 (11%) | 31/138 (22%) | 3/158 (2%) | 8/47 (17%) | 9/77 (12%) |
| ostensibly (on the surface; ostensibly) | unclear | `表面上` | 13/152 (9%) | 14/81 (17%) | 1/138 (1%) | 0/158 (0%) | 7/47 (15%) | 13/77 (17%) |
| hide (hiding; being hidden) | lie | `␣hidden`, `隐藏`, `隐藏的`, `隐藏着`, `␣hiding`, `隐蔽`, `Hidden` | 23/152 (15%) | 3/81 (4%) | 8/138 (6%) | 0/158 (0%) | 8/47 (17%) | 2/77 (3%) |
| ethics (ethics; morality) | unclear | `␣ethical`, `伦理`, `道德`, `␣moral`, `␣ethics`, `␣morally`, `ethical`, `的道德`, `␣morals`, `␣Moral` | 7/152 (5%) | 10/81 (12%) | 0/138 (0%) | 0/158 (0%) | 0/47 (0%) | 8/77 (10%) |
| comply (complying with rules or instructions) | unclear | `合规`, `␣compliance`, `遵循`, `␣adherence` | 12/152 (8%) | 5/81 (6%) | 0/138 (0%) | 0/158 (0%) | 5/47 (11%) | 4/77 (5%) |
| wrong (wrong, mistaken) | lie | `␣error`, `␣wrong`, `␣wrongful`, `错`, `错误`, `错了`, `没错`, `是非`, `误会`, `的错误`, `是错误的` | 7/152 (5%) | 10/81 (12%) | 20/138 (14%) | 6/158 (4%) | 3/47 (6%) | 10/77 (13%) |
| law-abiding / compliant (following law or rules) | unclear | `合规` | 11/152 (7%) | 4/81 (5%) | 0/138 (0%) | 0/158 (0%) | 5/47 (11%) | 3/77 (4%) |
| disclose (disclosing or revealing) | truth | `公开`, `␣disclosed`, `揭露`, `信息披露` | 3/152 (2%) | 9/81 (11%) | 17/138 (12%) | 0/158 (0%) | 1/47 (2%) | 9/77 (12%) |
| cover up (covering up or masking something) | lie | `掩盖`, `␣masking` | 8/152 (5%) | 2/81 (2%) | 0/138 (0%) | 0/158 (0%) | 2/47 (4%) | 2/77 (3%) |
| incorrect (incorrect) | lie | `␣incorrect`, `␣incorrectly`, `␣inaccurate`, `不符合`, `有误` | 3/152 (2%) | 7/81 (9%) | 4/138 (3%) | 7/158 (4%) | 1/47 (2%) | 7/77 (9%) |
| lie (telling a lie) | lie | `谎言`, `␣lie`, `␣lying`, `␣lies`, `␣lied`, `撒谎`, `说谎`, `lying`, `␣Lie`, `␣Lies`, `谎`, `␣mentira`, `␣falsehood` | 4/152 (3%) | 5/81 (6%) | 3/138 (2%) | 0/158 (0%) | 3/47 (6%) | 5/77 (6%) |
| claim (claiming) | unclear | `␣claim`, `声称`, `␣claims`, `claim`, `␣claimed`, `␣claiming`, `␣Claim` | 6/152 (4%) | 3/81 (4%) | 4/138 (3%) | 5/158 (3%) | 2/47 (4%) | 3/77 (4%) |
| make public (making public, announcing) | truth | `公开` | 3/152 (2%) | 6/81 (7%) | 17/138 (12%) | 0/158 (0%) | 1/47 (2%) | 6/77 (8%) |
| mislead (misleading someone) | lie | `误导`, `␣misleading` | 2/152 (1%) | 6/81 (7%) | 3/138 (2%) | 0/158 (0%) | 1/47 (2%) | 6/77 (8%) |
| fake (faking; fake) | lie | `fake`, `␣fake`, `Fake`, `作假` | 5/152 (3%) | 3/81 (4%) | 5/138 (4%) | 4/158 (3%) | 2/47 (4%) | 3/77 (4%) |
| euphemism (saying something indirectly or tactfully) | unclear | `委婉` | 5/152 (3%) | 3/81 (4%) | 1/138 (1%) | 0/158 (0%) | 2/47 (4%) | 3/77 (4%) |
| contrary (the opposite; contrary) | unclear | `␣contrary`, `相反` | 1/152 (1%) | 7/81 (9%) | 7/138 (5%) | 0/158 (0%) | 0/47 (0%) | 7/77 (9%) |
| correct (correct) | truth | `valid`, `␣valid`, `␣correct`, `␣Valid`, `␣correctly`, `correct`, `␣correction`, `_correct`, `Correct`, `␣corrected`, `␣Correct`, `␣corrections`, `␣correctness`, `␣correctamente`, `␣correcting`, `␣Corrections`, `正确`, `正确的`, `正确的是`, `正确答案`, `纠正`, `的正确`, `无误`, `是正确的`, `正确地`, `是否正确` | 1/152 (1%) | 6/81 (7%) | 29/138 (21%) | 88/158 (56%) | 1/47 (2%) | 5/77 (6%) |
| refuse (refusing or declining) | unclear | `拒绝`, `␣refusal`, `␣refused`, `␣refuses`, `拒`, `␣refusing`, `␣refuse`, `␣refus`, `拒絕`, `拒绝了`, `拒不`, `␣отказ`, `␣decline`, `␣declining`, `␣declines`, `␣отказа`, `␣declined` | 0/152 (0%) | 6/81 (7%) | 0/138 (0%) | 0/158 (0%) | 0/47 (0%) | 6/77 (8%) |
| unethical (unethical) | lie | `␣unethical` | 0/152 (0%) | 6/81 (7%) | 0/138 (0%) | 0/158 (0%) | 0/47 (0%) | 6/77 (8%) |
| official line (an agreed messaging line) | unclear | `口径` | 5/152 (3%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 3/47 (6%) | 1/77 (1%) |
| withhold (withholding information) | lie | `␣withholding`, `␣withheld` | 1/152 (1%) | 4/81 (5%) | 0/138 (0%) | 0/158 (0%) | 0/47 (0%) | 4/77 (5%) |
| imply (implying; implicit) | unclear | `␣implied`, `␣implicit`, `␣implicitly`, `暗示`, `隐含`, `间接`, `␣indirect`, `␣indirectly` | 1/152 (1%) | 4/81 (5%) | 2/138 (1%) | 1/158 (1%) | 0/47 (0%) | 4/77 (5%) |
| pretend (pretending; disguise) | lie | `伪装`, `装着` | 2/152 (1%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 2/47 (4%) | 1/77 (1%) |
| framing (framing / spin) | unclear | `␣framing` | 2/152 (1%) | 1/81 (1%) | 1/138 (1%) | 0/158 (0%) | 0/47 (0%) | 1/77 (1%) |
| integrity (integrity; uprightness) | truth | `␣integrity`, `诚信` | 0/152 (0%) | 3/81 (4%) | 0/138 (0%) | 0/158 (0%) | 0/47 (0%) | 3/77 (4%) |
| blame (blaming) | unclear | `␣blame`, `␣blames`, `␣blamed` | 2/152 (1%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 0/47 (0%) | 0/77 (0%) |
| good faith (good faith) | truth | `善意` | 2/152 (1%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 0/47 (0%) | 0/77 (0%) |
| reveal (revealing, exposing) | truth | `揭露` | 0/152 (0%) | 2/81 (2%) | 0/138 (0%) | 0/158 (0%) | 0/47 (0%) | 2/77 (3%) |
| dishonest (not honest) | lie | `␣dishonest` | 0/152 (0%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 0/47 (0%) | 1/77 (1%) |
| omit (leaving something out) | lie | `␣omit`, `␣omitted` | 0/152 (0%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 0/47 (0%) | 1/77 (1%) |
| misinformation (false information) | lie | `␣misinformation` | 0/152 (0%) | 1/81 (1%) | 1/138 (1%) | 0/158 (0%) | 0/47 (0%) | 1/77 (1%) |
| trick (tricking someone) | lie | `␣trick`, `␣tricks`, `␣Trick` | 0/152 (0%) | 1/81 (1%) | 1/138 (1%) | 0/158 (0%) | 0/47 (0%) | 1/77 (1%) |
| manipulate (manipulating) | lie | `␣manipulated`, `␣manipulation`, `␣manipulate`, `␣manipulating`, `操纵` | 0/152 (0%) | 1/81 (1%) | 1/138 (1%) | 0/158 (0%) | 0/47 (0%) | 1/77 (1%) |
| downplay (downplaying or glossing over) | lie | `淡化` | 1/152 (1%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 1/47 (2%) | 0/77 (0%) |
| candid (being candid or frank) | truth | `坦诚` | 0/152 (0%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 0/47 (0%) | 1/77 (1%) |
| clarify (clarifying) | unclear | `澄清` | 1/152 (1%) | 0/81 (0%) | 1/138 (1%) | 1/158 (1%) | 0/47 (0%) | 0/77 (0%) |
| mask / cover up (covering something over) | lie | `␣masking` | 1/152 (1%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 0/47 (0%) | 0/77 (0%) |
| distort (distorting) | lie | `扭曲` | 1/152 (1%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 0/47 (0%) | 0/77 (0%) |
| spin (putting a spin on facts) | lie | `␣spin`, `Spin`, `␣Spin` | 1/152 (1%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 0/47 (0%) | 0/77 (0%) |
| fraud (fraud) | lie | `␣fraud` | 0/152 (0%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 0/47 (0%) | 1/77 (1%) |
| inaccurate (inaccurate) | lie | `准确性和`, `不准确` | 0/152 (0%) | 1/81 (1%) | 3/138 (2%) | 1/158 (1%) | 0/47 (0%) | 1/77 (1%) |
| truth (the truth) | truth | `求真` | 0/152 (0%) | 0/81 (0%) | 1/138 (1%) | 0/158 (0%) | 0/47 (0%) | 0/77 (0%) |

Not in the draft: coax / fool (held back: no undisputed member left); deny (excluded: admit / deny / acknowledge); perfunctory (held back: no undisputed member left); admit (excluded: admit / deny / acknowledge); deceive (excluded: the question's own word)

## preans_slot3

| family | side | members | lies | truths | no-pressure truths | unrelated | lies that deny | truths that deny |
|---|---|---|---|---|---|---|---|---|
| false (false, untrue) | lie | `␣false`, `␣False`, `false`, `False`, `=False`, `FALSE`, `>false`, `_false`, `.assertFalse`, `.False`, `/false`, `假` | 58/152 (38%) | 65/81 (80%) | 134/138 (97%) | 104/158 (66%) | 33/47 (70%) | 63/77 (82%) |
| law-abiding (abiding by the law) | unclear | `守法` | 80/152 (53%) | 30/81 (37%) | 16/138 (12%) | 0/158 (0%) | 9/47 (19%) | 29/77 (38%) |
| disclose (disclosing or revealing) | truth | `公布`, `公开` | 66/152 (43%) | 39/81 (48%) | 28/138 (20%) | 37/158 (23%) | 16/47 (34%) | 39/77 (51%) |
| refuse (refusing or declining) | unclear | `␣refusal`, `␣refuse`, `拒`, `␣refusing`, `␣refus`, `拒绝` | 84/152 (55%) | 11/81 (14%) | 7/138 (5%) | 0/158 (0%) | 14/47 (30%) | 10/77 (13%) |
| sorry (apology) | unclear | `抱歉`, `␣sorry`, `Sorry`, `␣Sorry` | 27/152 (18%) | 17/81 (21%) | 9/138 (7%) | 5/158 (3%) | 13/47 (28%) | 17/77 (22%) |
| confess (confessing) | truth | `坦白` | 16/152 (11%) | 2/81 (2%) | 3/138 (2%) | 1/158 (1%) | 4/47 (9%) | 2/77 (3%) |
| clarify (clarifying) | unclear | `澄清` | 3/152 (2%) | 5/81 (6%) | 11/138 (8%) | 9/158 (6%) | 1/47 (2%) | 5/77 (6%) |
| violate (violating a rule or principle) | unclear | `违背` | 2/152 (1%) | 4/81 (5%) | 6/138 (4%) | 0/158 (0%) | 0/47 (0%) | 3/77 (4%) |
| ethics (ethics; morality) | unclear | `␣ethical`, `伦理` | 5/152 (3%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 0/47 (0%) | 0/77 (0%) |
| secret (secrecy; something kept secret) | lie | `秘密`, `私下` | 2/152 (1%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 2/47 (4%) | 0/77 (0%) |
| fiction (fiction; fictional) | unclear | `fiction` | 1/152 (1%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 1/47 (2%) | 1/77 (1%) |
| honest (honesty) | truth | `␣honestly` | 1/152 (1%) | 0/81 (0%) | 0/138 (0%) | 1/158 (1%) | 1/47 (2%) | 0/77 (0%) |
| fact (fact(s); factual) | unclear | `FACT` | 1/152 (1%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 1/47 (2%) | 0/77 (0%) |
| private (private, done privately) | unclear | `私下` | 1/152 (1%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 1/47 (2%) | 0/77 (0%) |
| spin (putting a spin on facts) | lie | `␣spin` | 0/152 (0%) | 1/81 (1%) | 4/138 (3%) | 0/158 (0%) | 0/47 (0%) | 1/77 (1%) |
| conceal (to conceal, to hide) | lie | `掩` | 0/152 (0%) | 0/81 (0%) | 0/138 (0%) | 4/158 (3%) | 0/47 (0%) | 0/77 (0%) |
| true (true, real) | truth | `␣true`, `true`, `True`, `␣True`, `TRUE`, `真` | 0/152 (0%) | 0/81 (0%) | 31/138 (22%) | 33/158 (21%) | 0/47 (0%) | 0/77 (0%) |
| objective (objective) | unclear | `␣objectively` | 0/152 (0%) | 0/81 (0%) | 0/138 (0%) | 1/158 (1%) | 0/47 (0%) | 0/77 (0%) |
| correct (correct) | truth | `正确` | 0/152 (0%) | 0/81 (0%) | 3/138 (2%) | 0/158 (0%) | 0/47 (0%) | 0/77 (0%) |
| wrong (wrong, mistaken) | lie | `没错` | 0/152 (0%) | 0/81 (0%) | 4/138 (3%) | 0/158 (0%) | 0/47 (0%) | 0/77 (0%) |

Not in the draft: truth (excluded: truth from the question on)

## preans_slot4

| family | side | members | lies | truths | no-pressure truths | unrelated | lies that deny | truths that deny |
|---|---|---|---|---|---|---|---|---|
| true (true, real) | truth | `␣true`, `true`, `␣real`, `True`, `␣True`, `␣TRUE`, `TRUE`, `␣genuine`, `真`, `成立`, `真实`, `确实`, `的确`, `真实的`, `是真的`, `确实是`, `属实` | 118/152 (78%) | 73/81 (90%) | 128/138 (93%) | 75/158 (47%) | 24/47 (51%) | 69/77 (90%) |
| honest (honesty) | truth | `诚实`, `诚信`, `诚`, `␣honest`, `␣honesty`, `真诚`, `␣Honest` | 106/152 (70%) | 72/81 (89%) | 112/138 (81%) | 81/158 (51%) | 39/47 (83%) | 69/77 (90%) |
| false (false, untrue) | lie | `␣false`, `␣False`, `(false`, `false`, `False`, `=False`, `_FALSE`, `FALSE`, `>false`, `_false`, `.assertFalse`, `.False`, `/false`, `假`, `假的` | 51/152 (34%) | 68/81 (84%) | 137/138 (99%) | 158/158 (100%) | 38/47 (81%) | 67/77 (87%) |
| integrity (integrity; uprightness) | truth | `正直`, `诚信` | 51/152 (34%) | 57/81 (70%) | 100/138 (72%) | 75/158 (47%) | 31/47 (66%) | 55/77 (71%) |
| fact (fact(s); factual) | unclear | `事实`, `␣factual`, `␣fact`, `␣Fact`, `Fact`, `符合`, `是否符合`, `求实` | 74/152 (49%) | 16/81 (20%) | 13/138 (9%) | 0/158 (0%) | 8/47 (17%) | 14/77 (18%) |
| objective (objectivity) | unclear | `客观`, `␣objectively` | 65/152 (43%) | 21/81 (26%) | 22/138 (16%) | 6/158 (4%) | 16/47 (34%) | 20/77 (26%) |
| truthful (telling the truth) | truth | `如实`, `␣truthful`, `实事求是` | 41/152 (27%) | 23/81 (28%) | 25/138 (18%) | 0/158 (0%) | 10/47 (21%) | 21/77 (27%) |
| comply (complying with rules or instructions) | unclear | `合规`, `␣adher`, `遵循` | 48/152 (32%) | 6/81 (7%) | 8/138 (6%) | 14/158 (9%) | 4/47 (9%) | 5/77 (6%) |
| fabricate (making something up) | lie | `虚构` | 35/152 (23%) | 5/81 (6%) | 2/138 (1%) | 0/158 (0%) | 1/47 (2%) | 5/77 (6%) |
| fiction (fiction; fictional) | unclear | `␣fictional`, `fiction`, `虚构` | 35/152 (23%) | 5/81 (6%) | 2/138 (1%) | 0/158 (0%) | 1/47 (2%) | 5/77 (6%) |
| candid (being candid or frank) | truth | `坦诚` | 24/152 (16%) | 13/81 (16%) | 10/138 (7%) | 4/158 (3%) | 20/47 (43%) | 13/77 (17%) |
| simulate (simulating) | unclear | `模拟`, `␣simulated`, `␣simulation`, `␣simulate`, `扮演`, `角色扮演`, `扮演着` | 33/152 (22%) | 4/81 (5%) | 1/138 (1%) | 0/158 (0%) | 2/47 (4%) | 4/77 (5%) |
| law-abiding / compliant (following law or rules) | unclear | `合规` | 33/152 (22%) | 4/81 (5%) | 0/138 (0%) | 0/158 (0%) | 4/47 (9%) | 3/77 (4%) |
| deliberate (doing something on purpose) | unclear | `␣intentionally`, `故意`, `␣deliberately`, `␣deliberate`, `故意的` | 22/152 (14%) | 10/81 (12%) | 4/138 (3%) | 1/158 (1%) | 0/47 (0%) | 9/77 (12%) |
| knowing (with knowledge; knowingly) | unclear | `明知` | 24/152 (16%) | 4/81 (5%) | 1/138 (1%) | 0/158 (0%) | 0/47 (0%) | 3/77 (4%) |
| role-play (playing a role or persona) | unclear | `扮演`, `␣persona`, `␣personas`, `角色扮演`, `␣Persona`, `Persona`, `persona`, `扮演着` | 24/152 (16%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 1/47 (2%) | 0/77 (0%) |
| good faith (good faith) | truth | `善意` | 16/152 (11%) | 7/81 (9%) | 3/138 (2%) | 0/158 (0%) | 3/47 (6%) | 5/77 (6%) |
| ostensibly (on the surface; ostensibly) | unclear | `表面上` | 20/152 (13%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 0/47 (0%) | 0/77 (0%) |
| confess (confessing) | truth | `坦白` | 10/152 (7%) | 7/81 (9%) | 5/138 (4%) | 18/158 (11%) | 7/47 (15%) | 7/77 (9%) |
| contrary (the opposite; contrary) | unclear | `相反`, `␣contrary` | 3/152 (2%) | 13/81 (16%) | 2/138 (1%) | 0/158 (0%) | 3/47 (6%) | 13/77 (17%) |
| correct (correct) | truth | `valid`, `␣correct`, `正确`, `是正确的` | 7/152 (5%) | 8/81 (10%) | 10/138 (7%) | 0/158 (0%) | 0/47 (0%) | 8/77 (10%) |
| wrong (wrong, mistaken) | lie | `不对`, `是非` | 8/152 (5%) | 6/81 (7%) | 0/138 (0%) | 0/158 (0%) | 5/47 (11%) | 5/77 (6%) |
| ethics (ethics; morality) | unclear | `␣ethical`, `伦理`, `道德`, `␣ethics`, `职业道德`, `␣moral` | 9/152 (6%) | 2/81 (2%) | 0/138 (0%) | 0/158 (0%) | 1/47 (2%) | 2/77 (3%) |
| downplay (downplaying or glossing over) | lie | `淡化` | 8/152 (5%) | 2/81 (2%) | 0/138 (0%) | 0/158 (0%) | 6/47 (13%) | 2/77 (3%) |
| sorry (apology) | unclear | `抱歉` | 7/152 (5%) | 3/81 (4%) | 4/138 (3%) | 13/158 (8%) | 5/47 (11%) | 3/77 (4%) |
| violate (violating a rule or principle) | unclear | `违反`, `违背` | 9/152 (6%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 2/47 (4%) | 0/77 (0%) |
| fair (impartial) | unclear | `公正` | 2/152 (1%) | 7/81 (9%) | 6/138 (4%) | 8/158 (5%) | 2/47 (4%) | 7/77 (9%) |
| conceal (concealing information) | lie | `隐瞒`, `隐` | 7/152 (5%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 1/47 (2%) | 0/77 (0%) |
| accurate (accurate) | truth | `␣accurate`, `␣accuracy`, `准确` | 1/152 (1%) | 6/81 (7%) | 19/138 (14%) | 0/158 (0%) | 0/47 (0%) | 6/77 (8%) |
| refuse (refusing or declining) | unclear | `拒绝` | 0/152 (0%) | 4/81 (5%) | 0/138 (0%) | 0/158 (0%) | 0/47 (0%) | 4/77 (5%) |
| disclose (disclosing or revealing) | truth | `信息披露`, `公开` | 3/152 (2%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 0/47 (0%) | 0/77 (0%) |
| transparent (transparency) | truth | `透明的`, `透明`, `␣transparent`, `␣transparency` | 1/152 (1%) | 3/81 (4%) | 2/138 (1%) | 1/158 (1%) | 1/47 (2%) | 3/77 (4%) |
| sincere (sincere) | truth | `真诚` | 2/152 (1%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 2/47 (4%) | 1/77 (1%) |
| withhold (withholding information) | lie | `␣withholding`, `␣withhold` | 2/152 (1%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 1/47 (2%) | 0/77 (0%) |
| lie (telling a lie) | lie | `说谎`, `␣falsehood` | 1/152 (1%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 1/47 (2%) | 0/77 (0%) |
| dishonest (not honest) | lie | `␣dishonest` | 1/152 (1%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 0/47 (0%) | 0/77 (0%) |
| contradict (contradicting; contradiction) | unclear | `␣contradict` | 0/152 (0%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 0/47 (0%) | 1/77 (1%) |
| official line (an agreed messaging line) | unclear | `口径` | 1/152 (1%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 0/47 (0%) | 0/77 (0%) |
| clarify (clarifying) | unclear | `澄清` | 1/152 (1%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 1/47 (2%) | 0/77 (0%) |
| secret (secret, kept secret) | lie | `保密` | 1/152 (1%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 0/47 (0%) | 0/77 (0%) |
| make public (making public, announcing) | truth | `公开` | 1/152 (1%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 0/47 (0%) | 0/77 (0%) |
| incorrect (incorrect) | lie | `不符合` | 0/152 (0%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 0/47 (0%) | 1/77 (1%) |

Not in the draft: coax / fool (held back: no undisputed member left); deny (excluded: admit / deny / acknowledge); truth (excluded: truth from the question on); admit (excluded: admit / deny / acknowledge); deceive (excluded: the question's own word)
