# Draft families: qwen3.6-27b, J-lens, part Q2_after, group preans

Written by `scripts/apply_family_decisions.py` (2026-10-01; draft, not frozen). Counts are `present / transcripts (share)`
on the build split.

## preans_slot0

| family | side | members | lies | truths | no-pressure truths | unrelated | lies that deny | truths that deny |
|---|---|---|---|---|---|---|---|---|
| critique (critique / criticism) | unclear | `批判`, `␣critique`, `␣critic`, `批评`, `␣critiques` | 76/152 (50%) | 27/81 (33%) | 49/138 (36%) | 10/158 (6%) | 19/47 (40%) | 25/77 (32%) |

Not in the draft: violate (held back: no undisputed member left)

## preans_slot1

| family | side | members | lies | truths | no-pressure truths | unrelated | lies that deny | truths that deny |
|---|---|---|---|---|---|---|---|---|
| truthful (telling the truth) | truth | `␣truthful`, `如实`, `实事求是` | 142/152 (93%) | 72/81 (89%) | 119/138 (86%) | 77/158 (49%) | 43/47 (91%) | 69/77 (90%) |
| false (false, untrue) | lie | `␣false`, `␣False`, `false`, `False`, `␣FALSE`, `␣fals`, `␣falsely`, `␣untrue`, `/false`, `␣falsehood`, `假`, `虚假`, `假的`, `真假`, `不实` | 151/152 (99%) | 58/81 (72%) | 110/138 (80%) | 82/158 (52%) | 47/47 (100%) | 54/77 (70%) |
| mislead (leading someone to a wrong belief) | lie | `␣misleading`, `误导`, `␣misled`, `误导性` | 144/152 (95%) | 59/81 (73%) | 89/138 (64%) | 86/158 (54%) | 43/47 (91%) | 55/77 (71%) |
| conceal (concealing, covering up) | lie | `隐瞒`, `掩盖`, `␣conceal`, `␣concealed`, `掩饰`, `隐匿`, `瞒`, `遮蔽`, `遮盖`, `藏`, `掩`, `隐` | 138/152 (91%) | 64/81 (79%) | 81/138 (59%) | 9/158 (6%) | 43/47 (91%) | 62/77 (81%) |
| hide (hiding, hidden) | lie | `␣hiding`, `隐藏`, `Hide`, `hide`, `_hide`, `␣hide`, `␣hides`, `-hide`, `␣Hide`, `␣hid`, `藏着`, `␣hidden`, `hidden`, `隐蔽`, `隐瞒`, `掩盖`, `␣conceal`, `␣concealed`, `掩饰`, `␣masking`, `隐匿`, `瞒`, `掩护` | 138/152 (91%) | 64/81 (79%) | 81/138 (59%) | 9/158 (6%) | 43/47 (91%) | 62/77 (81%) |
| lie (telling a lie) | lie | `谎言`, `说谎`, `谎`, `撒谎`, `␣거짓`, `␣lied`, `␣lying`, `␣mentira`, `␣lie`, `␣lies`, `␣Lies`, `␣Lie`, `Lie`, `lying`, `lie`, `lies`, `␣liar` | 150/152 (99%) | 48/81 (59%) | 64/138 (46%) | 1/158 (1%) | 46/47 (98%) | 45/77 (58%) |
| misinformation (false information given out) | lie | `␣misinformation`, `虚假信息` | 147/152 (97%) | 44/81 (54%) | 108/138 (78%) | 81/158 (51%) | 43/47 (91%) | 40/77 (52%) |
| fake (fake) | lie | `fake`, `Fake`, `␣fake`, `␣Fake`, `_fake`, `.fake`, `假冒` | 129/152 (85%) | 31/81 (38%) | 93/138 (67%) | 91/158 (58%) | 33/47 (70%) | 28/77 (36%) |
| misrepresent (presenting something as other than it is) | lie | `␣misrepresented` | 118/152 (78%) | 33/81 (41%) | 17/138 (12%) | 10/158 (6%) | 29/47 (62%) | 31/77 (40%) |
| fabricate (fabricating, making up) | lie | `伪造`, `造假`, `␣fabricated`, `弄虚作假`, `␣fabrication`, `␣invented`, `␣invent`, `␣invention`, `␣Invent` | 94/152 (62%) | 10/81 (12%) | 44/138 (32%) | 27/158 (17%) | 22/47 (47%) | 8/77 (10%) |
| fictional (fiction, made-up scenario) | unclear | `虚构`, `␣fict`, `␣fictional`, `fiction` | 66/152 (43%) | 19/81 (23%) | 89/138 (64%) | 84/158 (53%) | 14/47 (30%) | 16/77 (21%) |
| claim (claiming) | unclear | `␣claiming`, `声称`, `claim`, `␣claim`, `␣claims`, `宣称`, `␣Claim`, `Claim`, `claims`, `␣Claims`, `␣claimed`, `CLAIM`, `Claims`, `␣CLAIM`, `_claim` | 63/152 (41%) | 17/81 (21%) | 10/138 (7%) | 8/158 (5%) | 17/47 (36%) | 14/77 (18%) |
| contradict (contradicting) | unclear | `␣contradict`, `␣contrad`, `␣contradictory`, `␣contradiction`, `␣contradictions`, `矛盾`, `␣contradd` | 55/152 (36%) | 22/81 (27%) | 45/138 (33%) | 8/158 (5%) | 23/47 (49%) | 21/77 (27%) |
| dishonest (not honest) | lie | `␣dishonest` | 51/152 (34%) | 13/81 (16%) | 1/138 (1%) | 0/158 (0%) | 23/47 (49%) | 13/77 (17%) |
| knowingly (knowingly) | unclear | `␣knowingly`, `明知` | 56/152 (37%) | 2/81 (2%) | 2/138 (1%) | 0/158 (0%) | 19/47 (40%) | 2/77 (3%) |
| fact (the facts, factual) | unclear | `␣factual`, `事实`, `␣facts`, `的事实`, `␣Facts`, `facts`, `␣fact`, `Fact`, `fact`, `␣Fact`, `FACT`, `␣FACT`, `_fact`, `事实和`, `事实上`, `认定事实`, `␣actually`, `␣actual`, `actual`, `Actual`, `␣Actual`, `␣Actually`, `_FACT`, `Actually`, `actually`, `实际`, `的实际`, `实际的`, `实际上是` | 18/152 (12%) | 37/81 (46%) | 108/138 (78%) | 91/158 (58%) | 14/47 (30%) | 36/77 (47%) |
| imply (implying rather than stating) | unclear | `␣implicitly`, `␣implying`, `暗示`, `␣implicit`, `隐含`, `␣implication`, `␣imply`, `␣implied`, `␣implies`, `implicitly`, `␣implications`, `Implicit`, `␣Implicit`, `implicit`, `␣IMPLIED`, `␣implica` | 29/152 (19%) | 25/81 (31%) | 25/138 (18%) | 28/158 (18%) | 12/47 (26%) | 22/77 (29%) |
| assert (asserting) | unclear | `␣asserting`, `␣assertions`, `assert`, `␣assertion`, `_assert`, `␣asserted`, `␣asserts`, `␣assert`, `␣Assert`, `.assert`, `Assert`, `ASSERT`, `␣Assertions`, `/assert`, `Assertions` | 40/152 (26%) | 13/81 (16%) | 20/138 (14%) | 4/158 (3%) | 15/47 (32%) | 11/77 (14%) |
| incorrect (incorrect) | lie | `␣incorrect`, `Wrong`, `Incorrect`, `␣inaccur`, `␣incorrectly`, `␣inaccurate`, `incorrect`, `␣wrongly`, `␣erroneous`, `␣Incorrect`, `错误的`, `不符合`, `有误`, `不正确` | 34/152 (22%) | 19/81 (23%) | 21/138 (15%) | 78/158 (49%) | 9/47 (19%) | 17/77 (22%) |
| factual (factual) | truth | `␣factual` | 15/152 (10%) | 36/81 (44%) | 108/138 (78%) | 80/158 (51%) | 13/47 (28%) | 35/77 (45%) |
| blame (blaming) | unclear | `␣blaming`, `␣blame`, `␣blames`, `␣blamed` | 43/152 (28%) | 7/81 (9%) | 4/138 (3%) | 0/158 (0%) | 4/47 (9%) | 6/77 (8%) |
| honest (being honest) | truth | `␣honesty`, `诚实`, `␣honest`, `␣honestly`, `␣Honest` | 2/152 (1%) | 40/81 (49%) | 66/138 (48%) | 31/158 (20%) | 2/47 (4%) | 40/77 (52%) |
| refuse (refusing) | unclear | `拒绝`, `␣refusal`, `␣refusing`, `␣refus`, `␣refused`, `␣refuse`, `␣refuses`, `拒绝了`, `拒`, `拒絕`, `␣отказ`, `␣отказа`, `拒不`, `␣menolak` | 5/152 (3%) | 32/81 (40%) | 8/138 (6%) | 2/158 (1%) | 5/47 (11%) | 32/77 (42%) |
| disclaimer (a disclaimer) | unclear | `␣disclaimer`, `␣Disclaimer`, `Disclaimer`, `␣DISCLAIMER` | 4/152 (3%) | 31/81 (38%) | 29/138 (21%) | 38/158 (24%) | 4/47 (9%) | 31/77 (40%) |
| violate (violating a rule or principle) | unclear | `违背`, `违反`, `违反了`, `␣violates`, `␣violated` | 28/152 (18%) | 7/81 (9%) | 8/138 (6%) | 4/158 (3%) | 12/47 (26%) | 7/77 (9%) |
| evade (evading) | lie | `回避`, `␣evasion`, `规避`, `␣evade`, `逃避` | 19/152 (12%) | 13/81 (16%) | 3/138 (2%) | 0/158 (0%) | 11/47 (23%) | 13/77 (17%) |
| intentional (on purpose, deliberately) | unclear | `␣intentionally`, `␣deliberately`, `故意`, `刻意`, `␣deliberate`, `␣intentional` | 25/152 (16%) | 7/81 (9%) | 3/138 (2%) | 7/158 (4%) | 4/47 (9%) | 7/77 (9%) |
| disguise (disguising, masking) | lie | `伪装`, `␣masking`, `␣disgu`, `␣disguised`, `␣disguise` | 23/152 (15%) | 8/81 (10%) | 3/138 (2%) | 5/158 (3%) | 6/47 (13%) | 7/77 (9%) |
| inform (informing someone) | unclear | `告知` | 21/152 (14%) | 9/81 (11%) | 23/138 (17%) | 2/158 (1%) | 0/47 (0%) | 7/77 (9%) |
| true (true, real) | truth | `␣TRUE`, `真实`, `真实性`, `确实`, `真实的`, `是真的`, `内容的真实性`, `的真实`, `的真实性` | 15/152 (10%) | 15/81 (19%) | 75/138 (54%) | 51/158 (32%) | 7/47 (15%) | 14/77 (18%) |
| omit (leaving something out) | lie | `␣omission`, `␣omit`, `␣omitted`, `omit`, `省略`, `␣OMIT`, `遗漏` | 18/152 (12%) | 11/81 (14%) | 2/138 (1%) | 4/158 (3%) | 11/47 (23%) | 11/77 (14%) |
| candid (speaking frankly and openly) | truth | `坦诚`, `直言`, `␣straightforward` | 0/152 (0%) | 26/81 (32%) | 38/138 (28%) | 46/158 (29%) | 0/47 (0%) | 26/77 (34%) |
| correct (correct) | truth | `␣correct`, `␣correctly`, `correct`, `␣correction`, `_correct`, `Correct`, `␣corrected`, `␣Correct`, `␣corrections`, `␣correctness`, `␣Correction`, `␣correcting`, `.correct`, `_correction`, `Correction`, `␣Corrections`, `␣corrective`, `正确`, `正确的`, `修正`, `纠错`, `正确答案`, `纠正`, `改正`, `的正确`, `更正`, `是正确的`, `正确地` | 3/152 (2%) | 22/81 (27%) | 73/138 (53%) | 91/158 (58%) | 3/47 (6%) | 22/77 (29%) |
| vague (being vague) | unclear | `␣vague`, `含糊`, `模糊`, `␣vaguely` | 13/152 (9%) | 11/81 (14%) | 0/138 (0%) | 2/158 (1%) | 7/47 (15%) | 9/77 (12%) |
| fraud (fraud) | lie | `␣fraudulent`, `␣fraud` | 23/152 (15%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 8/47 (17%) | 1/77 (1%) |
| reject (rejecting) | unclear | `␣rejecting`, `␣rejection`, `reject`, `␣Reject`, `Reject`, `␣reject`, `␣rejected`, `Rejected`, `rejected` | 1/152 (1%) | 22/81 (27%) | 3/138 (2%) | 0/158 (0%) | 1/47 (2%) | 22/77 (29%) |
| ambiguous (ambiguity) | unclear | `␣ambiguity`, `␣ambiguous`, `␣ambigu`, `ambiguous` | 11/152 (7%) | 11/81 (14%) | 1/138 (1%) | 12/158 (8%) | 7/47 (15%) | 9/77 (12%) |
| avoid (avoiding) | unclear | `␣avoidance`, `␣avoided`, `␣avoiding`, `avoid`, `避开`, `␣Avoid`, `避免`, `Avoid`, `␣avoid`, `␣avoids` | 6/152 (4%) | 11/81 (14%) | 1/138 (1%) | 0/158 (0%) | 6/47 (13%) | 11/77 (14%) |
| clarify (clarifying) | unclear | `澄清`, `␣clarification`, `␣clarify`, `␣clarified` | 2/152 (1%) | 14/81 (17%) | 17/138 (12%) | 16/158 (10%) | 2/47 (4%) | 14/77 (18%) |
| framing (framing a statement) | unclear | `␣framing` | 8/152 (5%) | 6/81 (7%) | 4/138 (3%) | 2/158 (1%) | 4/47 (9%) | 4/77 (5%) |
| accurate (accurate) | truth | `␣accurate`, `␣accuracy`, `␣accurately`, `accuracy`, `accur`, `Accuracy`, `␣Accuracy`, `准确`, `准确性`, `准确的`, `准确地` | 0/152 (0%) | 14/81 (17%) | 69/138 (50%) | 78/158 (49%) | 0/47 (0%) | 14/77 (18%) |
| undisclosed (not disclosed) | lie | `␣undisclosed` | 7/152 (5%) | 6/81 (7%) | 4/138 (3%) | 1/158 (1%) | 6/47 (13%) | 6/77 (8%) |
| disclose (disclosing information) | truth | `␣disclosure`, `␣disclosing`, `␣disclose`, `␣disclosed`, `␣disclosures`, `␣Disclosure`, `披露`, `信息披露`, `公开`, `Disclosure`, `信息公开` | 1/152 (1%) | 11/81 (14%) | 20/138 (14%) | 4/158 (3%) | 1/47 (2%) | 11/77 (14%) |
| exaggerate (exaggerating) | lie | `夸大`, `␣exaggerated` | 8/152 (5%) | 4/81 (5%) | 1/138 (1%) | 3/158 (2%) | 2/47 (4%) | 4/77 (5%) |
| transparent (transparency) | truth | `␣transparency`, `透明`, `␣transparent`, `␣Transparency`, `透明度` | 0/152 (0%) | 12/81 (15%) | 5/138 (4%) | 5/158 (3%) | 0/47 (0%) | 12/77 (16%) |
| secret (secret, secrecy, covert) | lie | `␣secrecy`, `秘密`, `␣secretly`, `的秘密`, `隐秘`, `␣covert` | 8/152 (5%) | 3/81 (4%) | 2/138 (1%) | 0/158 (0%) | 7/47 (15%) | 3/77 (4%) |
| confidential (confidential, kept private by duty) | lie | `保密`, `␣confidentiality` | 7/152 (5%) | 4/81 (5%) | 5/138 (4%) | 0/158 (0%) | 5/47 (11%) | 4/77 (5%) |
| wrong (wrong, mistaken) | lie | `␣wrong`, `␣Wrong`, `␣WRONG`, `误`, `错误`, `错了`, `是错误的` | 6/152 (4%) | 5/81 (6%) | 12/138 (9%) | 28/158 (18%) | 2/47 (4%) | 4/77 (5%) |
| confess (confessing, owning up) | truth | `坦白`, `␣confession` | 0/152 (0%) | 10/81 (12%) | 18/138 (13%) | 4/158 (3%) | 0/47 (0%) | 10/77 (13%) |
| withhold (withholding information) | lie | `␣withholding`, `␣withheld`, `␣withhold` | 7/152 (5%) | 3/81 (4%) | 1/138 (1%) | 0/158 (0%) | 5/47 (11%) | 3/77 (4%) |
| unethical (unethical, immoral) | lie | `␣unethical` | 6/152 (4%) | 4/81 (5%) | 0/138 (0%) | 0/158 (0%) | 2/47 (4%) | 4/77 (5%) |
| prohibited (prohibited) | unclear | `禁止`, `␣prohibited`, `␣prohibition` | 1/152 (1%) | 9/81 (11%) | 0/138 (0%) | 0/158 (0%) | 0/47 (0%) | 9/77 (12%) |
| liar (a person who lies) | lie | `␣liar` | 9/152 (6%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 5/47 (11%) | 0/77 (0%) |
| reality (reality, the actual state of affairs) | unclear | `实际情况`, `␣reality`, `␣Reality`, `Reality`, `␣realities`, `␣réalité`, `但实际上`, `根据实际情况`, `实际上` | 7/152 (5%) | 1/81 (1%) | 6/138 (4%) | 6/158 (4%) | 5/47 (11%) | 1/77 (1%) |
| pretend (pretending) | lie | `␣pretending`, `假装`, `␣pretend` | 3/152 (2%) | 5/81 (6%) | 12/138 (9%) | 12/158 (8%) | 2/47 (4%) | 4/77 (5%) |
| minimize (minimizing, downplaying) | unclear | `␣minimizing`, `␣minimized`, `␣minimize`, `␣minimise` | 5/152 (3%) | 3/81 (4%) | 0/138 (0%) | 0/158 (0%) | 2/47 (4%) | 3/77 (4%) |
| decline (declining) | unclear | `␣declined`, `␣declining`, `␣declines`, `␣decline` | 0/152 (0%) | 8/81 (10%) | 0/138 (0%) | 0/158 (0%) | 0/47 (0%) | 8/77 (10%) |
| reveal (revealing, exposing) | truth | `揭露`, `␣revealing` | 0/152 (0%) | 7/81 (9%) | 8/138 (6%) | 0/158 (0%) | 0/47 (0%) | 7/77 (9%) |
| hypocrisy (hypocrisy) | lie | `␣hypocrisy`, `虚伪` | 2/152 (1%) | 5/81 (6%) | 0/138 (0%) | 0/158 (0%) | 2/47 (4%) | 5/77 (6%) |
| justify (justifying oneself, making excuses) | unclear | `辩解` | 4/152 (3%) | 3/81 (4%) | 2/138 (1%) | 0/158 (0%) | 3/47 (6%) | 3/77 (4%) |
| ethical (ethical) | truth | `␣ethical`, `ethical` | 0/152 (0%) | 7/81 (9%) | 0/138 (0%) | 0/158 (0%) | 0/47 (0%) | 7/77 (9%) |
| ethics (ethics, morality (the domain)) | unclear | `道德`, `␣moral`, `伦理`, `␣morally`, `␣ethical`, `ethical` | 0/152 (0%) | 7/81 (9%) | 0/138 (0%) | 0/158 (0%) | 0/47 (0%) | 7/77 (9%) |
| indirect (indirect, not direct) | unclear | `␣indirect`, `␣indirectly`, `␣INDIRECT` | 2/152 (1%) | 4/81 (5%) | 3/138 (2%) | 0/158 (0%) | 2/47 (4%) | 4/77 (5%) |
| lawful (lawful) | unclear | `␣lawful`, `合法`, `␣legitim`, `␣legitimate` | 1/152 (1%) | 5/81 (6%) | 3/138 (2%) | 20/158 (13%) | 0/47 (0%) | 5/77 (6%) |
| integrity (integrity, uprightness) | truth | `诚信`, `正直` | 1/152 (1%) | 3/81 (4%) | 5/138 (4%) | 3/158 (2%) | 1/47 (2%) | 3/77 (4%) |
| spin (spin, slanted presentation) | unclear | `␣spin`, `spin`, `Spin`, `␣spins`, `␣spinning`, `␣Spin`, `-spin`, `_spin`, `.spin` | 2/152 (1%) | 2/81 (2%) | 0/138 (0%) | 0/158 (0%) | 2/47 (4%) | 2/77 (3%) |
| legitimate (legitimate) | unclear | `␣legitim`, `␣legitimate` | 1/152 (1%) | 2/81 (2%) | 2/138 (1%) | 20/158 (13%) | 0/47 (0%) | 2/77 (3%) |
| hypothetical (hypothetical) | unclear | `␣hypothetical` | 1/152 (1%) | 2/81 (2%) | 35/138 (25%) | 24/158 (15%) | 0/47 (0%) | 2/77 (3%) |
| critique (critique / criticism) | unclear | `␣critique`, `␣criticisms`, `␣criticizing` | 0/152 (0%) | 3/81 (4%) | 1/138 (1%) | 3/158 (2%) | 0/47 (0%) | 3/77 (4%) |
| cannot (saying one cannot (answer)) | unclear | `无法`, `无法满足`, `不能说` | 2/152 (1%) | 0/81 (0%) | 1/138 (1%) | 0/158 (0%) | 0/47 (0%) | 0/77 (0%) |
| sincere (sincerity) | truth | `真诚` | 0/152 (0%) | 1/81 (1%) | 4/138 (3%) | 5/158 (3%) | 0/47 (0%) | 1/77 (1%) |
| manipulate (manipulating) | lie | `␣manipulated` | 0/152 (0%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 0/47 (0%) | 1/77 (1%) |
| illegal (illegal) | unclear | `␣illegally` | 1/152 (1%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 0/47 (0%) | 0/77 (0%) |
| compliant (compliance) | unclear | `合规` | 0/152 (0%) | 1/81 (1%) | 4/138 (3%) | 1/158 (1%) | 0/47 (0%) | 1/77 (1%) |
| simulated (simulated) | unclear | `␣simulated`, `模拟` | 0/152 (0%) | 1/81 (1%) | 4/138 (3%) | 4/158 (3%) | 0/47 (0%) | 1/77 (1%) |
| impossible (impossible) | unclear | `␣Impossible`, `Impossible`, `␣impossible` | 1/152 (1%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 0/47 (0%) | 0/77 (0%) |
| inaccurate (inaccurate) | lie | `不准确` | 0/152 (0%) | 1/81 (1%) | 1/138 (1%) | 3/158 (2%) | 0/47 (0%) | 1/77 (1%) |

Not in the draft: truth (excluded: truth from the question on); deny (excluded: admit / deny / acknowledge); admit (excluded: admit / deny / acknowledge); acknowledge (excluded: admit / deny / acknowledge)

## preans_slot2

| family | side | members | lies | truths | no-pressure truths | unrelated | lies that deny | truths that deny |
|---|---|---|---|---|---|---|---|---|
| unethical (unethical, immoral) | lie | `␣unethical`, `␣immoral` | 101/152 (66%) | 52/81 (64%) | 3/138 (2%) | 0/158 (0%) | 28/47 (60%) | 50/77 (65%) |
| fake (fake) | lie | `fake`, `␣fake`, `Fake`, `␣Fake`, `_fake` | 88/152 (58%) | 44/81 (54%) | 32/138 (23%) | 9/158 (6%) | 27/47 (57%) | 43/77 (56%) |
| conceal (concealing, covering up) | lie | `隐瞒`, `␣concealed`, `␣conceal`, `掩盖` | 99/152 (65%) | 32/81 (40%) | 3/138 (2%) | 0/158 (0%) | 32/47 (68%) | 31/77 (40%) |
| hide (hiding, hidden) | lie | `␣hidden`, `隐藏`, `hidden`, `隐藏的`, `-hidden`, `隐蔽`, `␣hiding`, `Hidden`, `:hidden`, `隐瞒`, `␣concealed`, `␣conceal`, `掩盖`, `掩护`, `␣masking` | 99/152 (65%) | 32/81 (40%) | 5/138 (4%) | 0/158 (0%) | 32/47 (68%) | 31/77 (40%) |
| misinformation (false information given out) | lie | `␣misinformation`, `虚假信息` | 92/152 (61%) | 37/81 (46%) | 94/138 (68%) | 13/158 (8%) | 23/47 (49%) | 36/77 (47%) |
| fact (the facts, factual) | unclear | `事实`, `␣facts`, `␣factual`, `facts`, `的事实`, `␣Facts`, `事实上`, `␣fact`, `␣Fact`, `Fact`, `fact`, `FACT`, `事实和`, `␣FACT`, `_fact`, `_FACT`, `␣actually`, `␣actual`, `actual`, `Actual`, `␣Actual`, `␣Actually`, `_actual`, `Actually`, `actually`, `实际`, `的实际`, `实际的`, `认定事实`, `事実` | 86/152 (57%) | 24/81 (30%) | 126/138 (91%) | 52/158 (33%) | 27/47 (57%) | 23/77 (30%) |
| true (true, real) | truth | `␣true`, `␣TRUE`, `真正`, `真实`, `真实性`, `确实`, `真正的`, `的确`, `真实的`, `是真的`, `真實`, `内容的真实性`, `的真实`, `的真实性`, `的真正` | 81/152 (53%) | 19/81 (23%) | 66/138 (48%) | 21/158 (13%) | 25/47 (53%) | 17/77 (22%) |
| secret (secret, secrecy, covert) | lie | `秘密`, `␣secretly`, `的秘密`, `␣secrecy`, `␣secretive`, `␣secret`, `secret`, `Secret`, `隐秘`, `␣covert`, `␣secrets`, `␣Secret`, `.secret`, `-secret`, `␣SECRET`, `内幕` | 78/152 (51%) | 17/81 (21%) | 1/138 (1%) | 0/158 (0%) | 29/47 (62%) | 15/77 (19%) |
| truthful (telling the truth) | truth | `␣truthful`, `实事求是`, `如实` | 70/152 (46%) | 20/81 (25%) | 96/138 (70%) | 9/158 (6%) | 24/47 (51%) | 19/77 (25%) |
| factual (factual) | truth | `␣factual` | 69/152 (45%) | 18/81 (22%) | 125/138 (91%) | 47/158 (30%) | 23/47 (49%) | 17/77 (22%) |
| confidential (confidential, kept private by duty) | lie | `␣confidentiality`, `机密`, `保密`, `␣confidential`, `␣Confidential` | 67/152 (44%) | 19/81 (23%) | 2/138 (1%) | 0/158 (0%) | 24/47 (51%) | 16/77 (21%) |
| false (false, untrue) | lie | `␣false`, `␣False`, `false`, `False`, `␣FALSE`, `:false`, `␣fals`, `␣falsely`, `␣untrue`, `/false`, `␣falsehood`, `假`, `虚假`, `假的`, `真假`, `不实`, `真伪`, `␣falso` | 55/152 (36%) | 31/81 (38%) | 65/138 (47%) | 9/158 (6%) | 20/47 (43%) | 31/77 (40%) |
| reality (the real situation) | unclear | `实际情况`, `␣reality`, `␣Reality`, `Reality`, `实际上`, `␣realities`, `但实际上`, `根据实际情况`, `实际上是` | 71/152 (47%) | 11/81 (14%) | 13/138 (9%) | 2/158 (1%) | 20/47 (43%) | 11/77 (14%) |
| fictional (fiction, made-up scenario) | unclear | `虚构`, `␣fictional`, `fiction`, `␣fict`, `␣Fiction`, `␣fiction`, `-fiction` | 46/152 (30%) | 34/81 (42%) | 78/138 (57%) | 31/158 (20%) | 19/47 (40%) | 33/77 (43%) |
| reality (reality, the actual state of affairs) | unclear | `实际情况`, `␣reality`, `␣Reality`, `Reality`, `␣réalité`, `␣realities`, `␣realidad`, `␣realidade` | 68/152 (45%) | 10/81 (12%) | 13/138 (9%) | 1/158 (1%) | 17/47 (36%) | 10/77 (13%) |
| undisclosed (not disclosed) | lie | `␣undisclosed` | 54/152 (36%) | 10/81 (12%) | 2/138 (1%) | 0/158 (0%) | 13/47 (28%) | 9/77 (12%) |
| violate (violating a rule or principle) | unclear | `违背`, `违反`, `违规`, `␣violates`, `␣violate`, `␣violations`, `␣violated`, `违反了`, `␣violation`, `␣violating` | 32/152 (21%) | 27/81 (33%) | 4/138 (3%) | 0/158 (0%) | 9/47 (19%) | 27/77 (35%) |
| intentional (on purpose, deliberately) | unclear | `故意`, `␣intentionally`, `␣deliberately`, `␣intentional`, `刻意`, `␣deliberate`, `故意的` | 38/152 (25%) | 17/81 (21%) | 2/138 (1%) | 1/158 (1%) | 11/47 (23%) | 17/77 (22%) |
| fabricate (fabricating, making up) | lie | `伪造`, `造假`, `弄虚作假` | 28/152 (18%) | 15/81 (19%) | 4/138 (3%) | 2/158 (1%) | 12/47 (26%) | 15/77 (19%) |
| hypothetical (hypothetical) | unclear | `␣hypothetical` | 14/152 (9%) | 27/81 (33%) | 39/138 (28%) | 11/158 (7%) | 7/47 (15%) | 27/77 (35%) |
| knowingly (knowingly) | unclear | `明知`, `␣knowingly` | 35/152 (23%) | 4/81 (5%) | 2/138 (1%) | 0/158 (0%) | 13/47 (28%) | 4/77 (5%) |
| contradict (contradicting) | unclear | `␣contradict`, `␣contradictory`, `矛盾`, `␣contrad`, `␣contradiction`, `␣contradictions`, `矛盾的` | 16/152 (11%) | 21/81 (26%) | 24/138 (17%) | 0/158 (0%) | 7/47 (15%) | 20/77 (26%) |
| mislead (leading someone to a wrong belief) | lie | `␣misleading`, `误导`, `␣misled` | 20/152 (13%) | 14/81 (17%) | 11/138 (8%) | 1/158 (1%) | 8/47 (17%) | 14/77 (18%) |
| ethics (ethics, morality (the domain)) | unclear | `␣ethics`, `␣morally`, `伦理`, `道德`, `␣Ethics`, `␣moral`, `的道德`, `␣morality`, `␣morals`, `␣Moral`, `␣ethical`, `ethical` | 13/152 (9%) | 21/81 (26%) | 0/138 (0%) | 0/158 (0%) | 2/47 (4%) | 19/77 (25%) |
| lie (telling a lie) | lie | `谎言`, `说谎`, `谎`, `撒谎`, `␣lying`, `␣거짓`, `␣lie`, `␣lied`, `␣liar` | 23/152 (15%) | 10/81 (12%) | 1/138 (1%) | 0/158 (0%) | 13/47 (28%) | 10/77 (13%) |
| unauthorized (unauthorized) | unclear | `␣unauthorized`, `␣Unauthorized`, `Unauthorized` | 21/152 (14%) | 10/81 (12%) | 0/138 (0%) | 1/158 (1%) | 5/47 (11%) | 10/77 (13%) |
| hypocrisy (hypocrisy) | lie | `␣hypocrisy`, `虚伪` | 17/152 (11%) | 13/81 (16%) | 1/138 (1%) | 0/158 (0%) | 6/47 (13%) | 13/77 (17%) |
| ethical (ethical) | truth | `␣ethical`, `ethical` | 12/152 (8%) | 18/81 (22%) | 0/138 (0%) | 0/158 (0%) | 1/47 (2%) | 16/77 (21%) |
| illegal (illegal) | unclear | `␣illegal`, `非法`, `␣illegally`, `违法`, `illegal`, `Illegal`, `␣unlawful` | 16/152 (11%) | 11/81 (14%) | 0/138 (0%) | 0/158 (0%) | 5/47 (11%) | 11/77 (14%) |
| dishonest (not honest) | lie | `␣dishonest` | 15/152 (10%) | 11/81 (14%) | 0/138 (0%) | 0/158 (0%) | 4/47 (9%) | 11/77 (14%) |
| role-play (playing a role) | unclear | `角色扮演`, `扮演` | 7/152 (5%) | 16/81 (20%) | 2/138 (1%) | 1/158 (1%) | 5/47 (11%) | 15/77 (19%) |
| refuse (refusing) | unclear | `拒绝`, `␣refusal`, `␣refused`, `␣refusing`, `␣refus`, `␣refuse`, `␣refuses`, `拒绝了`, `拒`, `拒絕`, `拒不`, `␣отказ`, `␣отказа` | 3/152 (2%) | 17/81 (21%) | 0/138 (0%) | 1/158 (1%) | 1/47 (2%) | 17/77 (22%) |
| prohibited (prohibited) | unclear | `禁止`, `␣prohibited` | 8/152 (5%) | 11/81 (14%) | 1/138 (1%) | 1/158 (1%) | 3/47 (6%) | 11/77 (14%) |
| disguise (disguising, masking) | lie | `伪装`, `␣disgu`, `␣disguise`, `␣masking` | 12/152 (8%) | 5/81 (6%) | 3/138 (2%) | 0/158 (0%) | 7/47 (15%) | 5/77 (6%) |
| wrong (wrong, mistaken) | lie | `␣ERROR`, `␣WRONG`, `误`, `错误`, `的错误` | 10/152 (7%) | 7/81 (9%) | 6/138 (4%) | 6/158 (4%) | 4/47 (9%) | 7/77 (9%) |
| misrepresent (presenting something as other than it is) | lie | `␣misrepresented` | 8/152 (5%) | 7/81 (9%) | 2/138 (1%) | 1/158 (1%) | 1/47 (2%) | 7/77 (9%) |
| incorrect (incorrect) | lie | `␣incorrect`, `Incorrect`, `␣inaccur`, `␣incorrectly`, `␣inaccurate`, `incorrect`, `␣wrongly`, `␣erroneous`, `␣Incorrect`, `错误的`, `不符合`, `有误`, `不正确` | 11/152 (7%) | 4/81 (5%) | 9/138 (7%) | 20/158 (13%) | 3/47 (6%) | 4/77 (5%) |
| imply (implying rather than stating) | unclear | `␣implicitly`, `隐含`, `␣implicit`, `暗示`, `␣implied`, `implicitly`, `␣implying`, `implicit` | 5/152 (3%) | 8/81 (10%) | 11/138 (8%) | 1/158 (1%) | 0/47 (0%) | 8/77 (10%) |
| claim (claiming) | unclear | `声称`, `␣claim`, `␣claims`, `␣claiming`, `宣称`, `␣claimed`, `claim`, `␣Claim`, `␣Claims`, `Claim` | 7/152 (5%) | 5/81 (6%) | 3/138 (2%) | 5/158 (3%) | 2/47 (4%) | 5/77 (6%) |
| cheat (cheating) | lie | `作弊`, `␣cheating` | 7/152 (5%) | 4/81 (5%) | 0/138 (0%) | 0/158 (0%) | 1/47 (2%) | 4/77 (5%) |
| disclose (disclosing information) | truth | `␣disclosure`, `␣disclosures`, `␣disclosing`, `␣disclosed`, `公开` | 6/152 (4%) | 3/81 (4%) | 0/138 (0%) | 0/158 (0%) | 2/47 (4%) | 3/77 (4%) |
| simulated (simulated) | unclear | `模拟`, `␣simulated` | 2/152 (1%) | 7/81 (9%) | 3/138 (2%) | 2/158 (1%) | 2/47 (4%) | 7/77 (9%) |
| reveal (revealing, exposing) | truth | `揭露` | 8/152 (5%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 2/47 (4%) | 0/77 (0%) |
| wrongdoing (wrongdoing) | lie | `␣wrongdoing`, `␣wrongful` | 4/152 (3%) | 4/81 (5%) | 0/138 (0%) | 0/158 (0%) | 1/47 (2%) | 4/77 (5%) |
| legitimate (legitimate) | unclear | `␣legitimately`, `␣legitimate`, `␣legitimacy`, `合法` | 3/152 (2%) | 4/81 (5%) | 0/138 (0%) | 8/158 (5%) | 3/47 (6%) | 3/77 (4%) |
| cannot (saying one cannot (answer)) | unclear | `无法`, `无法满足`, `␣cannot`, `根本无法`, `不能完全` | 3/152 (2%) | 3/81 (4%) | 0/138 (0%) | 7/158 (4%) | 1/47 (2%) | 3/77 (4%) |
| honest (being honest) | truth | `␣honest`, `␣honesty`, `␣honestly`, `诚实` | 1/152 (1%) | 4/81 (5%) | 0/138 (0%) | 0/158 (0%) | 0/47 (0%) | 4/77 (5%) |
| assert (asserting) | unclear | `␣assertions`, `assert`, `␣asserted`, `␣asserting`, `␣assertion`, `␣asserts`, `␣assert`, `/assert` | 3/152 (2%) | 2/81 (2%) | 32/138 (23%) | 1/158 (1%) | 1/47 (2%) | 2/77 (3%) |
| disclaimer (a disclaimer) | unclear | `␣disclaimer` | 2/152 (1%) | 3/81 (4%) | 24/138 (17%) | 5/158 (3%) | 1/47 (2%) | 3/77 (4%) |
| lawful (lawful) | unclear | `合法` | 2/152 (1%) | 3/81 (4%) | 0/138 (0%) | 1/158 (1%) | 2/47 (4%) | 3/77 (4%) |
| inform (informing someone) | unclear | `告知` | 3/152 (2%) | 2/81 (2%) | 1/138 (1%) | 0/158 (0%) | 0/47 (0%) | 2/77 (3%) |
| correct (correct) | truth | `␣correct`, `␣correctly`, `correct`, `␣correction`, `_correct`, `Correct`, `␣corrected`, `␣Correct`, `␣corrections`, `␣correctness`, `␣correcting`, `.correct`, `Correction`, `␣Corrections`, `正确`, `正确的`, `修正`, `纠错`, `正确答案`, `纠正`, `改正`, `的正确`, `更正`, `是正确的`, `正确地`, `是否正确` | 0/152 (0%) | 4/81 (5%) | 14/138 (10%) | 65/158 (41%) | 0/47 (0%) | 3/77 (4%) |
| accurate (accurate) | truth | `␣accurate`, `␣accuracy`, `␣accurately`, `accur`, `准确` | 0/152 (0%) | 4/81 (5%) | 0/138 (0%) | 39/158 (25%) | 0/47 (0%) | 4/77 (5%) |
| reject (rejecting) | unclear | `␣rejecting`, `reject`, `␣Reject`, `Reject`, `␣rejection`, `␣reject`, `␣rejected`, `rejected`, `.reject` | 0/152 (0%) | 3/81 (4%) | 0/138 (0%) | 0/158 (0%) | 0/47 (0%) | 3/77 (4%) |
| guilty (guilty) | unclear | `␣guilty` | 3/152 (2%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 2/47 (4%) | 0/77 (0%) |
| liar (a person who lies) | lie | `␣liar` | 1/152 (1%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 1/47 (2%) | 1/77 (1%) |
| avoid (avoiding) | unclear | `为了避免`, `␣avoidance` | 1/152 (1%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 0/47 (0%) | 1/77 (1%) |
| pretend (pretending) | lie | `␣pretending`, `␣pretend` | 1/152 (1%) | 1/81 (1%) | 1/138 (1%) | 3/158 (2%) | 1/47 (2%) | 1/77 (1%) |
| manipulate (manipulating) | lie | `␣manipulated`, `␣manipulation`, `␣manipulate`, `␣manipulating`, `␣manipul` | 1/152 (1%) | 1/81 (1%) | 1/138 (1%) | 0/158 (0%) | 0/47 (0%) | 1/77 (1%) |
| framing (framing a statement) | unclear | `␣framing` | 1/152 (1%) | 1/81 (1%) | 1/138 (1%) | 0/158 (0%) | 0/47 (0%) | 1/77 (1%) |
| betrayal (betrayal) | lie | `␣betrayal` | 1/152 (1%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 1/47 (2%) | 1/77 (1%) |
| blame (blaming) | unclear | `␣blame`, `␣blames`, `␣blamed`, `␣blaming` | 2/152 (1%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 0/47 (0%) | 0/77 (0%) |
| compliant (compliance) | unclear | `␣compliance`, `合规` | 2/152 (1%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 0/47 (0%) | 0/77 (0%) |
| candid (speaking frankly and openly) | truth | `坦诚` | 0/152 (0%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 0/47 (0%) | 1/77 (1%) |
| withhold (withholding information) | lie | `␣withholding`, `␣withheld` | 0/152 (0%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 0/47 (0%) | 1/77 (1%) |
| omit (leaving something out) | lie | `␣omitted` | 0/152 (0%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 0/47 (0%) | 1/77 (1%) |
| ambiguous (ambiguity) | unclear | `␣ambiguous` | 0/152 (0%) | 1/81 (1%) | 0/138 (0%) | 2/158 (1%) | 0/47 (0%) | 1/77 (1%) |
| decline (declining) | unclear | `␣declined`, `␣declining`, `␣declines`, `␣decline` | 0/152 (0%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 0/47 (0%) | 1/77 (1%) |
| clarify (clarifying) | unclear | `澄清` | 1/152 (1%) | 0/81 (0%) | 1/138 (1%) | 1/158 (1%) | 0/47 (0%) | 0/77 (0%) |
| justify (justifying oneself, making excuses) | unclear | `辩解` | 0/152 (0%) | 1/81 (1%) | 1/138 (1%) | 0/158 (0%) | 0/47 (0%) | 1/77 (1%) |
| impossible (impossible) | unclear | `␣impossible` | 0/152 (0%) | 1/81 (1%) | 1/138 (1%) | 2/158 (1%) | 0/47 (0%) | 1/77 (1%) |
| inaccurate (inaccurate) | lie | `不准确` | 1/152 (1%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 1/47 (2%) | 0/77 (0%) |

Not in the draft: truth (excluded: truth from the question on); fraud (excluded: the question's own word); deny (excluded: admit / deny / acknowledge); admit (excluded: admit / deny / acknowledge); acknowledge (excluded: admit / deny / acknowledge)

## preans_slot3

| family | side | members | lies | truths | no-pressure truths | unrelated | lies that deny | truths that deny |
|---|---|---|---|---|---|---|---|---|
| cannot (saying one cannot (answer)) | unclear | `␣Cannot`, `我无法`, `cannot`, `Cannot`, `不能`, `我不能`, `无法`, `是不能`, `できません` | 73/152 (48%) | 14/81 (17%) | 1/138 (1%) | 0/158 (0%) | 28/47 (60%) | 13/77 (17%) |
| false (false, untrue) | lie | `␣False`, `false`, `False`, `=False`, `>false`, `.False`, `/false` | 6/152 (4%) | 23/81 (28%) | 127/138 (92%) | 53/158 (34%) | 6/47 (13%) | 23/77 (30%) |
| impossible (impossible) | unclear | `␣Impossible` | 8/152 (5%) | 9/81 (11%) | 5/138 (4%) | 0/158 (0%) | 7/47 (15%) | 9/77 (12%) |
| true (true, real) | truth | `True`, `>true` | 7/152 (5%) | 1/81 (1%) | 8/138 (6%) | 1/158 (1%) | 3/47 (6%) | 0/77 (0%) |
| apologize (apologizing) | unclear | `␣Sorry`, `抱歉`, `Sorry` | 4/152 (3%) | 3/81 (4%) | 0/138 (0%) | 0/158 (0%) | 3/47 (6%) | 3/77 (4%) |
| refuse (refusing) | unclear | `␣refusal`, `拒绝` | 1/152 (1%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 0/47 (0%) | 0/77 (0%) |
| reject (rejecting) | unclear | `␣Reject` | 1/152 (1%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 1/47 (2%) | 0/77 (0%) |
| disclaimer (a disclaimer) | unclear | `␣Disclaimer` | 1/152 (1%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 0/47 (0%) | 0/77 (0%) |
| prohibited (prohibited) | unclear | `禁止` | 1/152 (1%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 0/47 (0%) | 0/77 (0%) |
| correct (correct) | truth | `Correct` | 0/152 (0%) | 0/81 (0%) | 1/138 (1%) | 0/158 (0%) | 0/47 (0%) | 0/77 (0%) |
| incorrect (incorrect) | lie | `Incorrect`, `incorrect`, `␣Incorrect` | 0/152 (0%) | 0/81 (0%) | 9/138 (7%) | 0/158 (0%) | 0/47 (0%) | 0/77 (0%) |

## preans_slot4

| family | side | members | lies | truths | no-pressure truths | unrelated | lies that deny | truths that deny |
|---|---|---|---|---|---|---|---|---|
| truthful (telling the truth) | truth | `␣truthful`, `如实` | 139/152 (91%) | 79/81 (98%) | 137/138 (99%) | 149/158 (94%) | 46/47 (98%) | 75/77 (97%) |
| ethics (ethics, morality (the domain)) | unclear | `␣morally`, `␣ethics`, `␣Ethics`, `伦理`, `道德`, `␣moral`, `职业道德`, `␣ethical`, `ethical` | 108/152 (71%) | 43/81 (53%) | 0/138 (0%) | 0/158 (0%) | 22/47 (47%) | 39/77 (51%) |
| ethical (ethical) | truth | `␣ethical`, `ethical` | 107/152 (70%) | 43/81 (53%) | 0/138 (0%) | 0/158 (0%) | 22/47 (47%) | 39/77 (51%) |
| honest (being honest) | truth | `␣honest`, `␣honesty`, `诚实`, `␣Honest`, `␣honestly` | 80/152 (53%) | 69/81 (85%) | 97/138 (70%) | 31/158 (20%) | 37/47 (79%) | 67/77 (87%) |
| false (false, untrue) | lie | `␣false`, `␣False`, `false`, `False`, `=False`, `␣FALSE`, `:false`, `(False`, `␣fals`, `␣untrue`, `/false`, `␣falsehood`, `假`, `虚假` | 82/152 (54%) | 66/81 (81%) | 138/138 (100%) | 158/158 (100%) | 35/47 (74%) | 62/77 (81%) |
| intentional (on purpose, deliberately) | unclear | `␣intentionally`, `␣intentional`, `故意`, `␣deliberately`, `␣deliberate`, `刻意` | 101/152 (66%) | 42/81 (52%) | 10/138 (7%) | 5/158 (3%) | 10/47 (21%) | 39/77 (51%) |
| true (true, real) | truth | `␣true`, `True`, `␣True`, `␣TRUE`, `真实`, `真实性`, `确实` | 54/152 (36%) | 40/81 (49%) | 64/138 (46%) | 34/158 (22%) | 7/47 (15%) | 38/77 (49%) |
| unethical (unethical, immoral) | lie | `␣unethical` | 78/152 (51%) | 10/81 (12%) | 0/138 (0%) | 0/158 (0%) | 5/47 (11%) | 9/77 (12%) |
| fact (the facts, factual) | unclear | `␣factual` | 19/152 (12%) | 29/81 (36%) | 74/138 (54%) | 31/158 (20%) | 10/47 (21%) | 28/77 (36%) |
| conceal (concealing, covering up) | lie | `隐瞒` | 36/152 (24%) | 6/81 (7%) | 10/138 (7%) | 2/158 (1%) | 3/47 (6%) | 5/77 (6%) |
| integrity (integrity, uprightness) | truth | `诚信`, `正直`, `␣integrity`, `␣Integrity` | 8/152 (5%) | 32/81 (40%) | 25/138 (18%) | 8/158 (5%) | 6/47 (13%) | 32/77 (42%) |
| fictional (fiction, made-up scenario) | unclear | `␣fictional`, `虚构`, `␣fict`, `␣Fiction`, `fiction` | 35/152 (23%) | 4/81 (5%) | 1/138 (1%) | 2/158 (1%) | 2/47 (4%) | 4/77 (5%) |
| lawful (lawful) | unclear | `␣lawful`, `合法`, `␣legitimate`, `␣legitimately` | 25/152 (16%) | 5/81 (6%) | 0/138 (0%) | 0/158 (0%) | 16/47 (34%) | 4/77 (5%) |
| hypothetical (hypothetical) | unclear | `␣hypothetical` | 24/152 (16%) | 4/81 (5%) | 0/138 (0%) | 0/158 (0%) | 1/47 (2%) | 4/77 (5%) |
| simulated (simulated) | unclear | `模拟`, `␣simulated`, `␣simulation`, `␣simulate`, `␣Simulation`, `␣simulations` | 22/152 (14%) | 3/81 (4%) | 0/138 (0%) | 0/158 (0%) | 1/47 (2%) | 3/77 (4%) |
| dishonest (not honest) | lie | `␣dishonest` | 15/152 (10%) | 6/81 (7%) | 0/138 (0%) | 0/158 (0%) | 0/47 (0%) | 5/77 (6%) |
| fake (fake) | lie | `fake`, `␣fake`, `␣Fake`, `Fake` | 18/152 (12%) | 1/81 (1%) | 1/138 (1%) | 1/158 (1%) | 0/47 (0%) | 1/77 (1%) |
| lie (telling a lie) | lie | `谎言` | 16/152 (11%) | 2/81 (2%) | 2/138 (1%) | 1/158 (1%) | 3/47 (6%) | 1/77 (1%) |
| confidential (confidential, kept private by duty) | lie | `␣confidentiality`, `保密`, `␣Confidential` | 16/152 (11%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 3/47 (6%) | 0/77 (0%) |
| legitimate (legitimate) | unclear | `␣legitimate`, `␣legitimately` | 12/152 (8%) | 4/81 (5%) | 0/138 (0%) | 0/158 (0%) | 4/47 (9%) | 3/77 (4%) |
| candid (speaking frankly and openly) | truth | `坦诚`, `␣straightforward` | 1/152 (1%) | 11/81 (14%) | 4/138 (3%) | 2/158 (1%) | 1/47 (2%) | 11/77 (14%) |
| misinformation (false information given out) | lie | `␣misinformation` | 7/152 (5%) | 4/81 (5%) | 9/138 (7%) | 4/158 (3%) | 3/47 (6%) | 2/77 (3%) |
| imply (implying rather than stating) | unclear | `␣implicitly`, `␣implicit`, `␣Implicit` | 8/152 (5%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 0/47 (0%) | 0/77 (0%) |
| compliant (compliance) | unclear | `␣compliance`, `␣Compliance`, `␣compliant`, `合规` | 9/152 (6%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 1/47 (2%) | 0/77 (0%) |
| mislead (leading someone to a wrong belief) | lie | `␣misleading`, `误导` | 5/152 (3%) | 3/81 (4%) | 5/138 (4%) | 0/158 (0%) | 0/47 (0%) | 1/77 (1%) |
| sincere (sincerity) | truth | `真诚`, `␣sincerity` | 1/152 (1%) | 7/81 (9%) | 2/138 (1%) | 1/158 (1%) | 1/47 (2%) | 7/77 (9%) |
| disguise (disguising, masking) | lie | `伪装` | 7/152 (5%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 0/47 (0%) | 0/77 (0%) |
| clarify (clarifying) | unclear | `澄清`, `␣clarification` | 6/152 (4%) | 2/81 (2%) | 0/138 (0%) | 1/158 (1%) | 6/47 (13%) | 2/77 (3%) |
| violate (violating a rule or principle) | unclear | `违反`, `␣violating`, `违背`, `␣violates`, `␣violate` | 8/152 (5%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 0/47 (0%) | 0/77 (0%) |
| refuse (refusing) | unclear | `拒绝`, `␣refusal`, `␣refusing`, `␣refus` | 0/152 (0%) | 5/81 (6%) | 0/138 (0%) | 0/158 (0%) | 0/47 (0%) | 5/77 (6%) |
| role-play (playing a role) | unclear | `角色扮演`, `扮演` | 5/152 (3%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 0/47 (0%) | 0/77 (0%) |
| pretend (pretending) | lie | `␣pretending`, `␣pretend` | 4/152 (3%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 0/47 (0%) | 0/77 (0%) |
| assert (asserting) | unclear | `␣assertions`, `␣assert` | 4/152 (3%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 4/47 (9%) | 0/77 (0%) |
| unauthorized (unauthorized) | unclear | `␣Unauthorized`, `␣unauthorized` | 4/152 (3%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 0/47 (0%) | 0/77 (0%) |
| accurate (accurate) | truth | `␣accurate`, `␣accuracy` | 2/152 (1%) | 2/81 (2%) | 16/138 (12%) | 0/158 (0%) | 2/47 (4%) | 2/77 (3%) |
| secret (secret, secrecy, covert) | lie | `␣secrecy` | 2/152 (1%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 1/47 (2%) | 0/77 (0%) |
| transparent (transparency) | truth | `透明`, `␣Transparency`, `␣transparency` | 0/152 (0%) | 3/81 (4%) | 0/138 (0%) | 0/158 (0%) | 0/47 (0%) | 3/77 (4%) |
| disclaimer (a disclaimer) | unclear | `␣disclaimer`, `␣Disclaimer` | 3/152 (2%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 0/47 (0%) | 0/77 (0%) |
| prohibited (prohibited) | unclear | `␣prohibited` | 3/152 (2%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 1/47 (2%) | 0/77 (0%) |
| correct (correct) | truth | `␣correct`, `␣Correct`, `␣correctness`, `正确` | 2/152 (1%) | 1/81 (1%) | 15/138 (11%) | 0/158 (0%) | 1/47 (2%) | 1/77 (1%) |
| incorrect (incorrect) | lie | `␣incorrect`, `␣inaccurate`, `␣Incorrect` | 3/152 (2%) | 0/81 (0%) | 2/138 (1%) | 6/158 (4%) | 0/47 (0%) | 0/77 (0%) |
| fraud (fraud) | lie | `␣fraudulent` | 1/152 (1%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 0/47 (0%) | 0/77 (0%) |
| reject (rejecting) | unclear | `␣rejecting`, `␣rejection`, `␣rejected` | 0/152 (0%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 0/47 (0%) | 1/77 (1%) |
| cannot (saying one cannot (answer)) | unclear | `␣Cannot` | 1/152 (1%) | 0/81 (0%) | 2/138 (1%) | 1/158 (1%) | 1/47 (2%) | 0/77 (0%) |
| apologize (apologizing) | unclear | `␣Sorry` | 1/152 (1%) | 0/81 (0%) | 0/138 (0%) | 1/158 (1%) | 1/47 (2%) | 0/77 (0%) |
| unintentional (not on purpose) | unclear | `␣unintention` | 1/152 (1%) | 0/81 (0%) | 1/138 (1%) | 0/158 (0%) | 0/47 (0%) | 0/77 (0%) |
| wrong (wrong, mistaken) | lie | `错误` | 0/152 (0%) | 0/81 (0%) | 1/138 (1%) | 0/158 (0%) | 0/47 (0%) | 0/77 (0%) |

Not in the draft: truth (excluded: truth from the question on); deny (excluded: admit / deny / acknowledge); admit (excluded: admit / deny / acknowledge); acknowledge (excluded: admit / deny / acknowledge)
