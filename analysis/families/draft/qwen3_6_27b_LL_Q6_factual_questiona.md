# Draft families: qwen3.6-27b, logit lens, part Q6_factual, group questiona

Written by `scripts/apply_family_decisions.py` (2026-10-01; draft, not frozen). Counts are `present / transcripts (share)`
on the build split.

## q_tok0

| family | side | members | lies | truths | no-pressure truths | unrelated | lies that deny | truths that deny |
|---|---|---|---|---|---|---|---|---|
| true (true, real) | truth | `真的`, `确实`, `的真` | 64/152 (42%) | 20/81 (25%) | 17/138 (12%) | 4/158 (3%) | 12/43 (28%) | 19/73 (26%) |
| wrong (wrong, mistaken) | lie | `错`, `错了`, `误会` | 2/152 (1%) | 4/81 (5%) | 13/138 (9%) | 3/158 (2%) | 2/43 (5%) | 4/73 (5%) |
| deliberate (doing it on purpose) | unclear | `␣intentionally`, `␣intentional`, `␣deliberate`, `␣deliberately`, `␣knowingly` | 2/152 (1%) | 2/81 (2%) | 0/138 (0%) | 0/158 (0%) | 0/43 (0%) | 2/73 (3%) |
| omit (omitting something) | unclear | `遗漏` | 1/152 (1%) | 2/81 (2%) | 1/138 (1%) | 12/158 (8%) | 0/43 (0%) | 2/73 (3%) |
| knowingly (with knowledge of the truth) | unclear | `␣knowingly` | 1/152 (1%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 0/43 (0%) | 1/73 (1%) |
| comply (complying with or adhering to rules) | unclear | `遵守`, `遵循` | 0/152 (0%) | 2/81 (2%) | 1/138 (1%) | 2/158 (1%) | 0/43 (0%) | 1/73 (1%) |
| lie (telling a lie) | lie | `撒谎` | 1/152 (1%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 0/43 (0%) | 0/73 (0%) |
| truthful (truthful, as things are) | truth | `如实` | 1/152 (1%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 0/43 (0%) | 0/73 (0%) |
| contradict (contradiction) | unclear | `␣contradict` | 1/152 (1%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 1/43 (2%) | 0/73 (0%) |
| secret (secrecy, confidentiality) | lie | `保密` | 0/152 (0%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 0/43 (0%) | 1/73 (1%) |
| fact (fact, factual) | truth | `符合`, `事实` | 1/152 (1%) | 0/81 (0%) | 1/138 (1%) | 0/158 (0%) | 1/43 (2%) | 0/73 (0%) |
| incorrect (incorrect) | lie | `有误` | 0/152 (0%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 0/43 (0%) | 1/73 (1%) |
| correct (correct) | truth | `␣correctly` | 0/152 (0%) | 0/81 (0%) | 0/138 (0%) | 2/158 (1%) | 0/43 (0%) | 0/73 (0%) |
| accurate (accurate) | truth | `␣accurately` | 0/152 (0%) | 0/81 (0%) | 0/138 (0%) | 1/158 (1%) | 0/43 (0%) | 0/73 (0%) |

Not in the draft: admit (excluded: admit / deny / acknowledge); deny (excluded: admit / deny / acknowledge); truth (excluded: truth from the question on); false (excluded: the question's own word)

## q_tok1

| family | side | members | lies | truths | no-pressure truths | unrelated | lies that deny | truths that deny |
|---|---|---|---|---|---|---|---|---|
| honest (being honest) | truth | `诚实`, `诚`, `坦诚`, `诚信`, `如实` | 14/152 (9%) | 4/81 (5%) | 0/138 (0%) | 0/158 (0%) | 1/43 (2%) | 4/73 (5%) |
| integrity (integrity, good faith) | truth | `诚信` | 10/152 (7%) | 3/81 (4%) | 0/138 (0%) | 0/158 (0%) | 1/43 (2%) | 3/73 (4%) |
| wrong (wrong, mistaken) | lie | `␣mistake`, `不对`, `失误` | 4/152 (3%) | 5/81 (6%) | 4/138 (3%) | 0/158 (0%) | 0/43 (0%) | 5/73 (7%) |
| comply (complying with or adhering to rules) | unclear | `合规`, `遵守` | 2/152 (1%) | 2/81 (2%) | 0/138 (0%) | 0/158 (0%) | 1/43 (2%) | 2/73 (3%) |
| secret (secrecy, confidentiality) | lie | `保密` | 3/152 (2%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 1/43 (2%) | 1/73 (1%) |
| knowingly (with knowledge of the truth) | unclear | `明知` | 1/152 (1%) | 2/81 (2%) | 0/138 (0%) | 0/158 (0%) | 0/43 (0%) | 2/73 (3%) |
| refuse (refusing) | unclear | `␣refusal`, `拒绝` | 0/152 (0%) | 3/81 (4%) | 0/138 (0%) | 0/158 (0%) | 0/43 (0%) | 3/73 (4%) |
| lie (telling a lie) | lie | `␣lie`, `lying` | 1/152 (1%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 0/43 (0%) | 1/73 (1%) |
| truthful (truthful, as things are) | truth | `如实` | 1/152 (1%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 0/43 (0%) | 1/73 (1%) |
| fact (fact, factual) | truth | `␣fact`, `␣facts`, `␣Fact`, `␣factual`, `实际情况` | 2/152 (1%) | 0/81 (0%) | 3/138 (2%) | 0/158 (0%) | 0/43 (0%) | 0/73 (0%) |
| objective (objective) | unclear | `客观` | 2/152 (1%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 2/43 (5%) | 0/73 (0%) |
| contradict (contradiction) | unclear | `␣contradict` | 1/152 (1%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 1/43 (2%) | 0/73 (0%) |
| exaggerate (exaggerating) | lie | `␣exaggerated` | 0/152 (0%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 0/43 (0%) | 1/73 (1%) |
| conscience (conscience) | unclear | `良心` | 0/152 (0%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 0/43 (0%) | 1/73 (1%) |
| oversight (negligence, oversight) | unclear | `疏忽` | 0/152 (0%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 0/43 (0%) | 1/73 (1%) |
| conceal (to conceal, to hide) | lie | `藏` | 1/152 (1%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 1/43 (2%) | 0/73 (0%) |
| true (true, real) | truth | `真`, `真正` | 1/152 (1%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 0/43 (0%) | 0/73 (0%) |
| correct (correct) | truth | `␣correction`, `␣corrected`, `␣corrections`, `纠正` | 0/152 (0%) | 0/81 (0%) | 0/138 (0%) | 2/158 (1%) | 0/43 (0%) | 0/73 (0%) |

Not in the draft: admit (excluded: admit / deny / acknowledge); deny (excluded: admit / deny / acknowledge); false (excluded: the question's own word)

## q_tok2

| family | side | members | lies | truths | no-pressure truths | unrelated | lies that deny | truths that deny |
|---|---|---|---|---|---|---|---|---|
| contradict (contradiction) | unclear | `␣contradictory`, `␣contradict`, `矛盾` | 5/152 (3%) | 2/81 (2%) | 0/138 (0%) | 0/158 (0%) | 2/43 (5%) | 2/73 (3%) |
| wrong (wrong, mistaken) | lie | `错误` | 2/152 (1%) | 2/81 (2%) | 0/138 (0%) | 0/158 (0%) | 1/43 (2%) | 2/73 (3%) |
| incorrect (incorrect) | lie | `␣incorrect` | 1/152 (1%) | 1/81 (1%) | 18/138 (13%) | 4/158 (3%) | 1/43 (2%) | 1/73 (1%) |
| fact (fact, factual) | truth | `与现实` | 1/152 (1%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 0/43 (0%) | 1/73 (1%) |
| noncompliant (not conforming) | unclear | `不符合` | 0/152 (0%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 0/43 (0%) | 1/73 (1%) |
| true (true, real) | truth | `确实` | 1/152 (1%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 0/43 (0%) | 0/73 (0%) |

Not in the draft: admit (excluded: admit / deny / acknowledge); deny (excluded: admit / deny / acknowledge)

## q_tok3

| family | side | members | lies | truths | no-pressure truths | unrelated | lies that deny | truths that deny |
|---|---|---|---|---|---|---|---|---|
| accurate (accurate) | truth | `␣accur`, `␣accurate`, `␣accuracy`, `␣accurately`, `accur`, `准确`, `准确的`, `准确地` | 150/152 (99%) | 79/81 (98%) | 138/138 (100%) | 146/158 (92%) | 43/43 (100%) | 71/73 (97%) |
| violate (violating a rule) | unclear | `␣violate`, `违反`, `␣violates`, `违背`, `违规`, `␣violating`, `␣violation`, `␣violations`, `违反了`, `触犯`, `Viol` | 127/152 (84%) | 73/81 (90%) | 111/138 (80%) | 96/158 (61%) | 28/43 (65%) | 65/73 (89%) |
| correct (correct) | truth | `␣correct`, `␣correctly`, `Correct`, `␣Correct`, `正确`, `正确的`, `正确答案`, `纠正`, `正确地`, `是否正确` | 102/152 (67%) | 69/81 (85%) | 137/138 (99%) | 140/158 (89%) | 25/43 (58%) | 62/73 (85%) |
| comply (complying with or adhering to rules) | unclear | `␣adher`, `␣adhere`, `␣comply`, `遵守`, `符合`, `是否符合`, `遵循`, `合规`, `␣adherence`, `␣conform`, `严格遵守`, `␣compliance` | 99/152 (65%) | 61/81 (75%) | 73/138 (53%) | 144/158 (91%) | 16/43 (37%) | 54/73 (74%) |
| inadvertent (doing it unintentionally) | unclear | `␣inadvertently`, `␣accidentally`, `␣unintention` | 87/152 (57%) | 62/81 (77%) | 62/138 (45%) | 6/158 (4%) | 25/43 (58%) | 56/73 (77%) |
| contradict (contradiction) | unclear | `␣contradict`, `␣contrad` | 65/152 (43%) | 28/81 (35%) | 119/138 (86%) | 6/158 (4%) | 25/43 (58%) | 22/73 (30%) |
| perfunctory (a perfunctory, going-through-the-motions reply) | unclear | `敷衍` | 51/152 (34%) | 16/81 (20%) | 7/138 (5%) | 3/158 (2%) | 24/43 (56%) | 14/73 (19%) |
| imply (implying or hinting rather than stating) | unclear | `␣imply`, `␣implicitly`, `暗示`, `␣implies`, `␣implying`, `␣implied`, `隐含` | 31/152 (20%) | 28/81 (35%) | 23/138 (17%) | 0/158 (0%) | 17/43 (40%) | 25/73 (34%) |
| honest (being honest) | truth | `␣honestly`, `诚实`, `诚`, `如实`, `␣truthful` | 25/152 (16%) | 16/81 (20%) | 5/138 (4%) | 0/158 (0%) | 12/43 (28%) | 14/73 (19%) |
| truthful (truthful, as things are) | truth | `如实`, `␣truthful` | 23/152 (15%) | 13/81 (16%) | 5/138 (4%) | 0/158 (0%) | 12/43 (28%) | 11/73 (15%) |
| incorrect (incorrect) | lie | `␣incorrect`, `␣inaccur`, `␣incorrectly`, `␣Incorrect`, `有误` | 10/152 (7%) | 10/81 (12%) | 43/138 (31%) | 22/158 (14%) | 7/43 (16%) | 8/73 (11%) |
| lie (telling a lie) | lie | `撒谎`, `说谎`, `␣lie`, `␣lies`, `谎言` | 17/152 (11%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 9/43 (21%) | 0/73 (0%) |
| noncompliant (not conforming) | unclear | `不符合` | 2/152 (1%) | 10/81 (12%) | 0/138 (0%) | 2/158 (1%) | 1/43 (2%) | 8/73 (11%) |
| wrong (wrong, mistaken) | lie | `␣error`, `错`, `错误`, `错了`, `是错误的` | 3/152 (2%) | 8/81 (10%) | 13/138 (9%) | 10/158 (6%) | 1/43 (2%) | 6/73 (8%) |
| evade (evading) | lie | `回避`, `␣evasion` | 7/152 (5%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 4/43 (9%) | 1/73 (1%) |
| refuse (refusing) | unclear | `拒绝`, `␣refusal`, `拒` | 0/152 (0%) | 7/81 (9%) | 0/138 (0%) | 0/158 (0%) | 0/43 (0%) | 7/73 (10%) |
| deliberate (doing it on purpose) | unclear | `␣intentionally` | 3/152 (2%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 1/43 (2%) | 1/73 (1%) |
| fact (fact, factual) | truth | `␣factual`, `实际上` | 1/152 (1%) | 3/81 (4%) | 11/138 (8%) | 2/158 (1%) | 0/43 (0%) | 2/73 (3%) |
| objective (objective) | unclear | `␣objectively`, `客观` | 2/152 (1%) | 1/81 (1%) | 2/138 (1%) | 0/158 (0%) | 0/43 (0%) | 0/73 (0%) |
| true (true, real) | truth | `内容的真实性`, `的真实性` | 3/152 (2%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 1/43 (2%) | 0/73 (0%) |
| euphemistic (saying something indirectly or euphemistically) | unclear | `委婉` | 2/152 (1%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 0/43 (0%) | 0/73 (0%) |
| hallucinate (hallucination by a model) | unclear | `␣halluc` | 1/152 (1%) | 1/81 (1%) | 7/138 (5%) | 13/158 (8%) | 0/43 (0%) | 1/73 (1%) |
| fabricate (making something up) | lie | `虚构` | 2/152 (1%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 0/43 (0%) | 0/73 (0%) |
| omit (omitting something) | unclear | `␣omit`, `遗漏` | 1/152 (1%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 0/43 (0%) | 0/73 (0%) |
| leak (leaking information) | unclear | `␣leak`, `泄露` | 1/152 (1%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 0/43 (0%) | 0/73 (0%) |
| conceal (hiding or concealing something) | lie | `掩饰` | 1/152 (1%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 0/43 (0%) | 0/73 (0%) |

Not in the draft: admit (excluded: admit / deny / acknowledge); acknowledge (excluded: admit / deny / acknowledge); deny (excluded: admit / deny / acknowledge); false (excluded: the question's own word); truth (excluded: truth from the question on)

## q_tok4

| family | side | members | lies | truths | no-pressure truths | unrelated | lies that deny | truths that deny |
|---|---|---|---|---|---|---|---|---|
| hallucinate (hallucination by a model) | unclear | `␣halluc` | 138/152 (91%) | 64/81 (79%) | 133/138 (96%) | 126/158 (80%) | 36/43 (84%) | 57/73 (78%) |
| fact (fact, factual) | truth | `␣facts`, `␣factual`, `事实` | 81/152 (53%) | 35/81 (43%) | 111/138 (80%) | 10/158 (6%) | 24/43 (56%) | 30/73 (41%) |
| truthful (truthful, as things are) | truth | `␣truthful` | 31/152 (20%) | 13/81 (16%) | 26/138 (19%) | 0/158 (0%) | 8/43 (19%) | 12/73 (16%) |
| lie (telling a lie) | lie | `␣lies`, `说谎`, `谎言`, `␣lie`, `␣lying`, `谎`, `撒谎` | 21/152 (14%) | 4/81 (5%) | 0/138 (0%) | 0/158 (0%) | 8/43 (19%) | 4/73 (5%) |
| accurate (accurate) | truth | `␣accurate`, `准确` | 12/152 (8%) | 8/81 (10%) | 41/138 (30%) | 3/158 (2%) | 1/43 (2%) | 6/73 (8%) |
| comply (complying with or adhering to rules) | unclear | `符合`, `合规` | 8/152 (5%) | 11/81 (14%) | 15/138 (11%) | 15/158 (9%) | 0/43 (0%) | 10/73 (14%) |
| wrong (wrong, mistaken) | lie | `error`, `␣mistakes`, `错`, `错误` | 15/152 (10%) | 3/81 (4%) | 8/138 (6%) | 11/158 (7%) | 1/43 (2%) | 3/73 (4%) |
| mistake (a mistake or error) | unclear | `␣error` | 7/152 (5%) | 5/81 (6%) | 17/138 (12%) | 26/158 (16%) | 3/43 (7%) | 4/73 (5%) |
| objective (objective) | unclear | `␣objectively`, `客观` | 0/152 (0%) | 8/81 (10%) | 13/138 (9%) | 2/158 (1%) | 0/43 (0%) | 8/73 (11%) |
| correct (correct) | truth | `␣valid`, `␣correct` | 3/152 (2%) | 1/81 (1%) | 57/138 (41%) | 36/158 (23%) | 1/43 (2%) | 1/73 (1%) |
| deliberate (doing it on purpose) | unclear | `有意` | 2/152 (1%) | 1/81 (1%) | 2/138 (1%) | 0/158 (0%) | 0/43 (0%) | 1/73 (1%) |
| refuse (refusing) | unclear | `␣refusal`, `拒绝` | 1/152 (1%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 0/43 (0%) | 1/73 (1%) |
| fabricate (making something up) | lie | `␣fabricated` | 2/152 (1%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 1/43 (2%) | 0/73 (0%) |
| misinformation (misinformation) | unclear | `␣misinformation` | 1/152 (1%) | 1/81 (1%) | 3/138 (2%) | 0/158 (0%) | 0/43 (0%) | 0/73 (0%) |
| incorrect (incorrect) | lie | `␣inaccur` | 1/152 (1%) | 1/81 (1%) | 1/138 (1%) | 0/158 (0%) | 0/43 (0%) | 0/73 (0%) |
| violate (violating a rule) | unclear | `违反` | 0/152 (0%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 0/43 (0%) | 1/73 (1%) |
| conceal (hiding or concealing something) | lie | `␣hidden` | 1/152 (1%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 0/43 (0%) | 0/73 (0%) |
| deceive (the act of deceiving) | lie | `␣deception`, `欺骗` | 1/152 (1%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 1/43 (2%) | 0/73 (0%) |
| true (true, real) | truth | `␣true`, `true`, `True`, `␣TRUE`, `真` | 0/152 (0%) | 0/81 (0%) | 6/138 (4%) | 0/158 (0%) | 0/43 (0%) | 0/73 (0%) |

Not in the draft: deny (excluded: admit / deny / acknowledge); false (excluded: the question's own word); truth (excluded: truth from the question on)

## q_tok5

| family | side | members | lies | truths | no-pressure truths | unrelated | lies that deny | truths that deny |
|---|---|---|---|---|---|---|---|---|
| fact (fact, factual) | truth | `␣fact`, `␣reality`, `␣facts`, `Fact`, `fact`, `␣Fact`, `␣Facts`, `_fact`, `␣FACT`, `FACT`, `␣factual`, `facts`, `实际`, `现实`, `事实`, `实际上`, `实际情况`, `事实上`, `的事实`, `的实际`, `实际的`, `实事求是`, `现实中`, `的现实`, `实际上是`, `与实际`, `与现实`, `事实和`, `上述事实` | 139/152 (91%) | 59/81 (73%) | 138/138 (100%) | 98/158 (62%) | 42/43 (98%) | 52/73 (71%) |
| lie (telling a lie) | lie | `␣lie`, `谎言`, `␣lying`, `␣lies`, `谎`, `撒谎`, `说谎`, `␣Lie`, `␣lied`, `␣mentira`, `␣liar`, `lying`, `Lie`, `␣Lies`, `␣거짓`, `lies` | 138/152 (91%) | 54/81 (67%) | 89/138 (64%) | 1/158 (1%) | 37/43 (86%) | 46/73 (63%) |
| hallucinate (hallucination by a model) | unclear | `␣halluc`, `幻觉` | 116/152 (76%) | 66/81 (81%) | 137/138 (99%) | 141/158 (89%) | 30/43 (70%) | 59/73 (81%) |
| honest (being honest) | truth | `诚实`, `诚`, `坦诚`, `␣honesty`, `␣honest`, `␣truthful`, `诚信`, `如实` | 115/152 (76%) | 48/81 (59%) | 123/138 (89%) | 11/158 (7%) | 27/43 (63%) | 41/73 (56%) |
| conceal (hiding or concealing something) | lie | `隐瞒`, `␣hidden`, `掩饰`, `掩盖`, `␣conceal`, `␣concealed`, `隐藏`, `␣masking`, `遮掩`, `␣hiding`, `hidden`, `瞒`, `藏`, `掩`, `遮`, `隐` | 119/152 (78%) | 40/81 (49%) | 105/138 (76%) | 89/158 (56%) | 38/43 (88%) | 34/73 (47%) |
| truthful (truthful, as things are) | truth | `␣truthful`, `如实` | 111/152 (73%) | 44/81 (54%) | 121/138 (88%) | 0/158 (0%) | 27/43 (63%) | 38/73 (52%) |
| violate (violating a rule) | unclear | `违反`, `违背`, `␣violation`, `违反了`, `␣violating`, `违规`, `␣violate`, `␣violations`, `␣violates`, `␣violated`, `违法`, `␣viol` | 96/152 (63%) | 57/81 (70%) | 121/138 (88%) | 6/158 (4%) | 22/43 (51%) | 51/73 (70%) |
| fabricate (making something up) | lie | `␣fabricated`, `虚构`, `␣fabrication`, `伪造` | 122/152 (80%) | 28/81 (35%) | 63/138 (46%) | 7/158 (4%) | 29/43 (67%) | 25/73 (34%) |
| contradict (contradiction) | unclear | `␣contradiction`, `␣contradict`, `矛盾`, `␣contrad`, `␣contradictory`, `␣contradictions`, `矛盾的`, `之间的矛盾`, `␣contradd` | 82/152 (54%) | 53/81 (65%) | 134/138 (97%) | 32/158 (20%) | 24/43 (56%) | 46/73 (63%) |
| comply (complying with or adhering to rules) | unclear | `符合`, `合规`, `是否符合`, `␣compliance`, `遵守`, `␣compliant`, `␣complying`, `␣comply`, `符合要求`, `遵循`, `必须符合`, `严格遵守`, `␣adherence`, `遵照`, `␣adher`, `符合国家` | 63/152 (41%) | 43/81 (53%) | 110/138 (80%) | 25/158 (16%) | 13/43 (30%) | 38/73 (52%) |
| hidden (being hidden (state)) | lie | `␣hidden`, `hidden` | 54/152 (36%) | 33/81 (41%) | 105/138 (76%) | 89/158 (56%) | 18/43 (42%) | 28/73 (38%) |
| fiction (fiction, fictional content) | unclear | `␣fictional`, `fiction`, `␣fiction`, `␣Fiction`, `-fiction`, `虚构` | 67/152 (44%) | 18/81 (22%) | 10/138 (7%) | 8/158 (5%) | 11/43 (26%) | 18/73 (25%) |
| noncompliant (not conforming) | unclear | `不符合` | 46/152 (30%) | 32/81 (40%) | 15/138 (11%) | 17/158 (11%) | 9/43 (21%) | 29/73 (40%) |
| refuse (refusing) | unclear | `␣refusal`, `拒绝`, `␣refus`, `拒`, `␣refused`, `␣refuse`, `␣refusing`, `␣refuses`, `拒绝了`, `拒絕`, `拒不` | 31/152 (20%) | 45/81 (56%) | 59/138 (43%) | 4/158 (3%) | 13/43 (30%) | 45/73 (62%) |
| correct (correct) | truth | `valid`, `␣valid`, `␣correct`, `␣Valid`, `␣correctly`, `correct`, `␣correction`, `Correct`, `␣corrected`, `␣Correct`, `␣corrections`, `␣correctness`, `␣Correction`, `␣correcting`, `Correction`, `正确`, `正确的`, `正确的是`, `正确答案`, `纠正`, `的正确`, `无误`, `是正确的`, `是否正确` | 26/152 (17%) | 39/81 (48%) | 112/138 (81%) | 134/158 (85%) | 12/43 (28%) | 37/73 (51%) |
| deceive (the act of deceiving) | lie | `␣deception`, `欺骗`, `␣deceptive`, `骗`, `␣deceive`, `欺`, `哄` | 60/152 (39%) | 3/81 (4%) | 12/138 (9%) | 0/158 (0%) | 11/43 (26%) | 2/73 (3%) |
| deliberate (doing it on purpose) | unclear | `␣deliberate`, `␣deliberately`, `故意`, `␣intentionally`, `␣intentional`, `明知`, `␣knowingly` | 51/152 (34%) | 11/81 (14%) | 8/138 (6%) | 2/158 (1%) | 12/43 (28%) | 9/73 (12%) |
| integrity (integrity, good faith) | truth | `诚信` | 49/152 (32%) | 8/81 (10%) | 0/138 (0%) | 0/158 (0%) | 9/43 (21%) | 6/73 (8%) |
| imply (implying or hinting rather than stating) | unclear | `暗示`, `隐含`, `␣hint`, `␣implicit`, `␣implicitly`, `␣implied`, `␣imply`, `␣implies`, `␣implying`, `hint`, `␣Hint`, `implicit`, `Hint` | 42/152 (28%) | 14/81 (17%) | 10/138 (7%) | 2/158 (1%) | 11/43 (26%) | 10/73 (14%) |
| ethics (ethics, morality) | unclear | `␣moral`, `␣ethical`, `道德`, `伦理`, `␣morally`, `␣ethics`, `ethical`, `␣Ethics`, `的道德`, `␣morality`, `␣morals`, `␣Moral`, `职业道德` | 23/152 (15%) | 31/81 (38%) | 1/138 (1%) | 0/158 (0%) | 2/43 (5%) | 30/73 (41%) |
| disclose (disclosing or revealing) | truth | `公开`, `␣disclosure`, `透露`, `披露`, `␣disclosing`, `␣disclose`, `暴露`, `␣reveal`, `␣exposing` | 25/152 (16%) | 28/81 (35%) | 7/138 (5%) | 1/158 (1%) | 6/43 (14%) | 25/73 (34%) |
| fake (fake, not genuine) | lie | `fake`, `␣fake`, `Fake` | 40/152 (26%) | 1/81 (1%) | 2/138 (1%) | 2/158 (1%) | 3/43 (7%) | 1/73 (1%) |
| liar (a person who lies) | lie | `␣liar` | 35/152 (23%) | 3/81 (4%) | 0/138 (0%) | 0/158 (0%) | 8/43 (19%) | 1/73 (1%) |
| objective (objective) | unclear | `客观` | 24/152 (16%) | 12/81 (15%) | 38/138 (28%) | 0/158 (0%) | 4/43 (9%) | 11/73 (15%) |
| true (true, real) | truth | `␣true`, `true`, `␣real`, `True`, `␣True`, `␣TRUE`, `␣genuine`, `真`, `真正`, `真实`, `真正的`, `真实的`, `的真`, `确实是`, `的真实`, `的真实性`, `的真正` | 23/152 (15%) | 11/81 (14%) | 102/138 (74%) | 12/158 (8%) | 6/43 (14%) | 9/73 (12%) |
| knowingly (with knowledge of the truth) | unclear | `明知`, `␣knowingly` | 31/152 (20%) | 1/81 (1%) | 6/138 (4%) | 0/158 (0%) | 9/43 (21%) | 1/73 (1%) |
| euphemistic (saying something indirectly or euphemistically) | unclear | `委婉` | 21/152 (14%) | 11/81 (14%) | 1/138 (1%) | 0/158 (0%) | 7/43 (16%) | 8/73 (11%) |
| wrong (wrong, mistaken) | lie | `␣wrong`, `␣flaw`, `错`, `错误`, `不对`, `错了`, `失误`, `是非`, `的错误`, `是错误的` | 19/152 (12%) | 13/81 (16%) | 19/138 (14%) | 85/158 (54%) | 2/43 (5%) | 11/73 (15%) |
| mistake (a mistake or error) | unclear | `␣mistake`, `␣mistakes`, `␣error`, `error` | 8/152 (5%) | 12/81 (15%) | 63/138 (46%) | 129/158 (82%) | 2/43 (5%) | 10/73 (14%) |
| leak (leaking information) | unclear | `泄露` | 9/152 (6%) | 8/81 (10%) | 4/138 (3%) | 0/158 (0%) | 3/43 (7%) | 7/73 (10%) |
| dishonest (being dishonest) | lie | `␣dishonest` | 14/152 (9%) | 2/81 (2%) | 0/138 (0%) | 0/158 (0%) | 2/43 (5%) | 1/73 (1%) |
| role-play (playing a role) | unclear | `扮演`, `角色扮演`, `扮演着` | 4/152 (3%) | 12/81 (15%) | 2/138 (1%) | 1/158 (1%) | 0/43 (0%) | 12/73 (16%) |
| accurate (accurate) | truth | `␣accurate`, `␣accurately`, `准确`, `准确的`, `准确地` | 6/152 (4%) | 10/81 (12%) | 65/138 (47%) | 8/158 (5%) | 3/43 (7%) | 10/73 (14%) |
| mislead (misleading someone) | lie | `␣misleading`, `误导` | 12/152 (8%) | 1/81 (1%) | 1/138 (1%) | 3/158 (2%) | 1/43 (2%) | 1/73 (1%) |
| misinformation (misinformation) | unclear | `␣misinformation` | 12/152 (8%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 1/43 (2%) | 0/73 (0%) |
| simulate (simulating) | unclear | `模拟`, `仿真` | 0/152 (0%) | 11/81 (14%) | 0/138 (0%) | 0/158 (0%) | 0/43 (0%) | 11/73 (15%) |
| vague (being vague) | unclear | `␣vague` | 6/152 (4%) | 2/81 (2%) | 0/138 (0%) | 0/158 (0%) | 0/43 (0%) | 1/73 (1%) |
| apologize (apologizing) | unclear | `␣apology`, `道歉`, `␣apologies` | 4/152 (3%) | 3/81 (4%) | 13/138 (9%) | 8/158 (5%) | 1/43 (2%) | 3/73 (4%) |
| secret (secrecy, confidentiality) | lie | `␣confidentiality`, `␣secret`, `秘密`, `␣covert`, `保密` | 1/152 (1%) | 5/81 (6%) | 1/138 (1%) | 0/158 (0%) | 0/43 (0%) | 4/73 (5%) |
| confess (confessing, coming clean) | truth | `␣confession`, `坦白` | 0/152 (0%) | 5/81 (6%) | 1/138 (1%) | 0/158 (0%) | 0/43 (0%) | 4/73 (5%) |
| incorrect (incorrect) | lie | `␣incorrect`, `␣inaccur`, `␣incorrectly`, `␣inaccurate`, `␣Incorrect`, `错误的`, `有误`, `错误的是` | 2/152 (1%) | 3/81 (4%) | 8/138 (6%) | 24/158 (15%) | 0/43 (0%) | 2/73 (3%) |
| evade (evading) | lie | `回避`, `␣evasion`, `规避`, `␣evade` | 3/152 (2%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 2/43 (5%) | 1/73 (1%) |
| unethical (unethical) | lie | `␣unethical` | 2/152 (1%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 0/43 (0%) | 1/73 (1%) |
| transparent (being transparent) | truth | `␣transparent`, `␣transparency`, `-transparent` | 0/152 (0%) | 3/81 (4%) | 0/138 (0%) | 0/158 (0%) | 0/43 (0%) | 3/73 (4%) |
| omit (omitting something) | unclear | `遗漏`, `␣omission` | 3/152 (2%) | 0/81 (0%) | 2/138 (1%) | 4/158 (3%) | 0/43 (0%) | 0/73 (0%) |
| manipulate (manipulating someone) | lie | `␣manipulation`, `␣manipulate`, `␣manipulated`, `␣manipulating`, `操纵` | 1/152 (1%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 0/43 (0%) | 1/73 (1%) |
| inadvertent (doing it unintentionally) | unclear | `␣inadvertently`, `␣unintention` | 1/152 (1%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 1/43 (2%) | 1/73 (1%) |
| inaccurate (inaccurate) | lie | `不准确` | 2/152 (1%) | 0/81 (0%) | 0/138 (0%) | 3/158 (2%) | 1/43 (2%) | 0/73 (0%) |
| perfunctory (a perfunctory, going-through-the-motions reply) | unclear | `敷衍` | 1/152 (1%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 0/43 (0%) | 0/73 (0%) |
| exaggerate (exaggerating) | lie | `夸大` | 1/152 (1%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 0/43 (0%) | 0/73 (0%) |

Not in the draft: deny (excluded: admit / deny / acknowledge); admit (excluded: admit / deny / acknowledge); acknowledge (excluded: admit / deny / acknowledge); false (excluded: the question's own word); truth (excluded: truth from the question on)

## q_tok6

| family | side | members | lies | truths | no-pressure truths | unrelated | lies that deny | truths that deny |
|---|---|---|---|---|---|---|---|---|
| fact (fact, factual) | truth | `␣fact`, `␣reality`, `␣facts`, `fact`, `␣Fact`, `␣factual`, `事实`, `的事实` | 151/152 (99%) | 68/81 (84%) | 134/138 (97%) | 155/158 (98%) | 43/43 (100%) | 61/73 (84%) |
| fake (fake, not genuine) | lie | `␣fake`, `fake`, `␣Fake`, `Fake` | 121/152 (80%) | 64/81 (79%) | 50/138 (36%) | 18/158 (11%) | 22/43 (51%) | 58/73 (79%) |
| mislead (misleading someone) | lie | `␣misleading`, `误导` | 121/152 (80%) | 33/81 (41%) | 1/138 (1%) | 0/158 (0%) | 27/43 (63%) | 26/73 (36%) |
| honest (honesty, truthfulness, candour) | truth | `␣truthful` | 85/152 (56%) | 8/81 (10%) | 0/138 (0%) | 0/158 (0%) | 17/43 (40%) | 6/73 (8%) |
| true (true, real) | truth | `␣true`, `真`, `真实的` | 65/152 (43%) | 15/81 (19%) | 1/138 (1%) | 2/158 (1%) | 18/43 (42%) | 13/73 (18%) |
| deliberate (doing it on purpose) | unclear | `␣intentionally`, `故意`, `␣deliberately`, `␣deliberate`, `明知`, `␣knowingly` | 65/152 (43%) | 14/81 (17%) | 2/138 (1%) | 0/158 (0%) | 15/43 (35%) | 13/73 (18%) |
| lie (telling a lie) | lie | `谎言`, `说谎`, `撒谎`, `谎`, `lying` | 50/152 (33%) | 4/81 (5%) | 0/138 (0%) | 0/158 (0%) | 15/43 (35%) | 3/73 (4%) |
| knowingly (with knowledge of the truth) | unclear | `明知`, `␣knowingly` | 40/152 (26%) | 10/81 (12%) | 2/138 (1%) | 0/158 (0%) | 14/43 (33%) | 9/73 (12%) |
| incorrect (incorrect) | lie | `␣incorrect`, `␣Incorrect`, `错误的` | 5/152 (3%) | 29/81 (36%) | 131/138 (95%) | 157/158 (99%) | 3/43 (7%) | 28/73 (38%) |
| deceive (the act of deceiving) | lie | `␣deceptive`, `欺骗` | 19/152 (12%) | 4/81 (5%) | 0/138 (0%) | 0/158 (0%) | 1/43 (2%) | 3/73 (4%) |
| wrong (wrong, mistaken) | lie | `␣wrong`, `错误`, `谬` | 2/152 (1%) | 8/81 (10%) | 16/138 (12%) | 52/158 (33%) | 1/43 (2%) | 7/73 (10%) |
| pretext (a false pretext) | lie | `␣pretext` | 4/152 (3%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 0/43 (0%) | 1/73 (1%) |
| fabricate (making something up) | lie | `伪造`, `虚构` | 4/152 (3%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 1/43 (2%) | 0/73 (0%) |
| refuse (refusing) | unclear | `␣refusal` | 1/152 (1%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 1/43 (2%) | 1/73 (1%) |
| fictional (invented, fictional) | unclear | `虚构` | 2/152 (1%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 0/43 (0%) | 0/73 (0%) |
| exaggerate (exaggerating) | lie | `夸大` | 1/152 (1%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 0/43 (0%) | 0/73 (0%) |
| mistake (a mistake or error) | unclear | `␣error` | 0/152 (0%) | 1/81 (1%) | 60/138 (43%) | 135/158 (85%) | 0/43 (0%) | 1/73 (1%) |

Not in the draft: deny (excluded: admit / deny / acknowledge); false (excluded: the question's own word); truth (excluded: truth from the question on)

## q_tok7

| family | side | members | lies | truths | no-pressure truths | unrelated | lies that deny | truths that deny |
|---|---|---|---|---|---|---|---|---|
| fact (fact, factual) | truth | `␣fact`, `␣facts`, `Fact`, `fact`, `␣Fact`, `␣Facts`, `␣FACT`, `␣factual`, `事实`, `事实上`, `的事实`, `事实和`, `上述事实` | 152/152 (100%) | 81/81 (100%) | 138/138 (100%) | 158/158 (100%) | 43/43 (100%) | 73/73 (100%) |
| deliberate (doing it on purpose) | unclear | `故意`, `有意`, `␣intentionally`, `␣deliberately`, `␣deliberate`, `␣intentional`, `故意的`, `␣knowingly`, `明知` | 133/152 (88%) | 44/81 (54%) | 0/138 (0%) | 0/158 (0%) | 35/43 (81%) | 38/73 (52%) |
| true (true, real) | truth | `␣true`, `true`, `成立`, `的真` | 124/152 (82%) | 33/81 (41%) | 33/138 (24%) | 25/158 (16%) | 29/43 (67%) | 26/73 (36%) |
| knowingly (with knowledge of the truth) | unclear | `␣knowingly`, `明知` | 113/152 (74%) | 14/81 (17%) | 0/138 (0%) | 0/158 (0%) | 30/43 (70%) | 11/73 (15%) |
| lie (telling a lie) | lie | `谎`, `谎言`, `␣거짓`, `␣liar` | 65/152 (43%) | 19/81 (23%) | 0/138 (0%) | 1/158 (1%) | 12/43 (28%) | 15/73 (21%) |
| honest (honesty, truthfulness, candour) | truth | `␣truthful` | 14/152 (9%) | 8/81 (10%) | 0/138 (0%) | 0/158 (0%) | 7/43 (16%) | 7/73 (10%) |
| contradict (contradiction) | unclear | `␣contrad`, `␣contradictory` | 8/152 (5%) | 5/81 (6%) | 68/138 (49%) | 0/158 (0%) | 0/43 (0%) | 3/73 (4%) |
| mistake (a mistake or error) | unclear | `␣error` | 2/152 (1%) | 8/81 (10%) | 38/138 (28%) | 43/158 (27%) | 2/43 (5%) | 7/73 (10%) |
| wrong (wrong, mistaken) | lie | `error`, `␣wrong`, `错误`, `谬`, `是错误的` | 1/152 (1%) | 5/81 (6%) | 22/138 (16%) | 27/158 (17%) | 1/43 (2%) | 5/73 (7%) |
| violate (violating a rule) | unclear | `违反`, `违背` | 3/152 (2%) | 1/81 (1%) | 2/138 (1%) | 0/158 (0%) | 0/43 (0%) | 0/73 (0%) |
| inadvertent (doing it unintentionally) | unclear | `无意` | 2/152 (1%) | 0/81 (0%) | 0/138 (0%) | 1/158 (1%) | 2/43 (5%) | 0/73 (0%) |
| liar (a person who lies) | lie | `␣liar` | 1/152 (1%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 1/43 (2%) | 1/73 (1%) |
| deceive (the act of deceiving) | lie | `欺骗` | 1/152 (1%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 0/43 (0%) | 0/73 (0%) |
| incorrect (incorrect) | lie | `␣incorrect`, `错误的`, `错误的是` | 0/152 (0%) | 1/81 (1%) | 21/138 (15%) | 92/158 (58%) | 0/43 (0%) | 1/73 (1%) |
| objective (objective) | unclear | `客观` | 1/152 (1%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 1/43 (2%) | 0/73 (0%) |

Not in the draft: false (excluded: the question's own word); truth (excluded: truth from the question on)
