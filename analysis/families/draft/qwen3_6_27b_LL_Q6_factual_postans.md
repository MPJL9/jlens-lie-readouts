# Draft families: qwen3.6-27b, logit lens, part Q6_factual, group postans

Written by `scripts/apply_family_decisions.py` (2026-10-01; draft, not frozen). Counts are `present / transcripts (share)`
on the build split.

## postans_slot0

| family | side | members | lies | truths | no-pressure truths | unrelated | lies that deny | truths that deny |
|---|---|---|---|---|---|---|---|---|
| sincere (sincere, earnest) | truth | `诚挚` | 127/152 (84%) | 67/81 (83%) | 101/138 (73%) | 2/158 (1%) | 30/43 (70%) | 62/73 (85%) |
| neutral (neutral) | unclear | `中立` | 44/152 (29%) | 49/81 (60%) | 82/138 (59%) | 118/158 (75%) | 12/43 (28%) | 44/73 (60%) |
| joke (joking) | unclear | `玩笑` | 21/152 (14%) | 22/81 (27%) | 112/138 (81%) | 125/158 (79%) | 12/43 (28%) | 22/73 (30%) |
| responsibility (responsibility, liability) | unclear | `负责任` | 3/152 (2%) | 2/81 (2%) | 0/138 (0%) | 0/158 (0%) | 0/43 (0%) | 2/73 (3%) |
| deceive (the act of deceiving) | lie | `欺` | 3/152 (2%) | 1/81 (1%) | 1/138 (1%) | 21/158 (13%) | 2/43 (5%) | 1/73 (1%) |
| wrong (wrong, mistaken) | lie | `错` | 3/152 (2%) | 1/81 (1%) | 14/138 (10%) | 0/158 (0%) | 3/43 (7%) | 1/73 (1%) |
| hide (hiding, concealing) | lie | `-hide`, `掩` | 1/152 (1%) | 1/81 (1%) | 2/138 (1%) | 0/158 (0%) | 0/43 (0%) | 1/73 (1%) |
| true (true, real) | truth | `real` | 1/152 (1%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 0/43 (0%) | 1/73 (1%) |

Not in the draft: fake (held back: no undisputed member left); doubt (held back: no undisputed member left); fact (excluded: truth from the question on)

## postans_slot1

| family | side | members | lies | truths | no-pressure truths | unrelated | lies that deny | truths that deny |
|---|---|---|---|---|---|---|---|---|
| hide (hiding, concealing) | lie | `隐瞒`, `-hide`, `Hidden`, `藏`, `掩` | 130/152 (86%) | 59/81 (73%) | 32/138 (23%) | 18/158 (11%) | 27/43 (63%) | 53/73 (73%) |
| true (true, real) | truth | `␣true`, `true`, `␣True`, `real`, `真`, `真实`, `真实的`, `成真` | 109/152 (72%) | 18/81 (22%) | 42/138 (30%) | 11/158 (7%) | 5/43 (12%) | 11/73 (15%) |
| fact (fact, factual) | unclear | `␣factual`, `事实`, `␣fact`, `␣facts`, `␣Fact`, `事实上`, `的事实`, `事实和`, `␣reality`, `实际`, `现实`, `实际上`, `的现实`, `求实`, `与现实` | 94/152 (62%) | 23/81 (28%) | 15/138 (11%) | 51/158 (32%) | 8/43 (19%) | 16/73 (22%) |
| accurate (accurate) | truth | `␣accurate`, `␣accuracy`, `␣accurately`, `准确`, `准确的` | 96/152 (63%) | 15/81 (19%) | 59/138 (43%) | 40/158 (25%) | 3/43 (7%) | 8/73 (11%) |
| knowingly (doing it knowingly, on purpose) | unclear | `明知` | 101/152 (66%) | 7/81 (9%) | 0/138 (0%) | 1/158 (1%) | 10/43 (23%) | 2/73 (3%) |
| consistent (consistent with, conforming to) | unclear | `符合`, `是否符合`, `符合要求` | 43/152 (28%) | 52/81 (64%) | 125/138 (91%) | 10/158 (6%) | 33/43 (77%) | 51/73 (70%) |
| truthful (truthful) | truth | `␣truthful`, `如实` | 70/152 (46%) | 12/81 (15%) | 0/138 (0%) | 0/158 (0%) | 1/43 (2%) | 8/73 (11%) |
| honest (honest, candid) | truth | `诚实`, `诚`, `如实`, `坦诚`, `␣honest`, `␣honesty`, `诚信`, `诚恳` | 69/152 (45%) | 10/81 (12%) | 0/138 (0%) | 0/158 (0%) | 6/43 (14%) | 8/73 (11%) |
| wrong (wrong, mistaken) | lie | `error`, `␣error`, `错`, `错误`, `不对`, `是非`, `指正`, `是错误的` | 45/152 (30%) | 32/81 (40%) | 16/138 (12%) | 55/158 (35%) | 25/43 (58%) | 31/73 (42%) |
| correct (correct) | truth | `valid`, `␣valid`, `␣correct`, `␣Valid`, `␣correctly`, `correct`, `␣corrected`, `␣Correct`, `正确`, `正确的`, `正确的是`, `正确答案`, `纠正` | 17/152 (11%) | 28/81 (35%) | 111/138 (80%) | 70/158 (44%) | 9/43 (21%) | 26/73 (36%) |
| violate (violating a rule or principle) | unclear | `违背`, `违反`, `违反了` | 38/152 (25%) | 4/81 (5%) | 0/138 (0%) | 0/158 (0%) | 8/43 (19%) | 1/73 (1%) |
| objective (objective, impartial) | unclear | `客观` | 34/152 (22%) | 8/81 (10%) | 1/138 (1%) | 0/158 (0%) | 13/43 (30%) | 8/73 (11%) |
| legal (lawful, by law) | unclear | `合法`, `依法`, `␣legally`, `合法的` | 21/152 (14%) | 18/81 (22%) | 4/138 (3%) | 0/158 (0%) | 18/43 (42%) | 18/73 (25%) |
| inconsistent (not consistent with) | unclear | `不符合` | 23/152 (15%) | 13/81 (16%) | 0/138 (0%) | 0/158 (0%) | 5/43 (12%) | 12/73 (16%) |
| lie (telling a lie) | lie | `说谎`, `谎言`, `撒谎`, `␣lie`, `␣lying`, `谎`, `lying` | 32/152 (21%) | 3/81 (4%) | 0/138 (0%) | 0/158 (0%) | 12/43 (28%) | 1/73 (1%) |
| lawful (lawful, legal) | unclear | `合法` | 15/152 (10%) | 14/81 (17%) | 4/138 (3%) | 0/158 (0%) | 15/43 (35%) | 14/73 (19%) |
| good_intent (good intentions) | unclear | `好心` | 24/152 (16%) | 2/81 (2%) | 4/138 (3%) | 1/158 (1%) | 1/43 (2%) | 0/73 (0%) |
| compliance (complying with rules) | unclear | `合规`, `遵循` | 14/152 (9%) | 10/81 (12%) | 4/138 (3%) | 0/158 (0%) | 13/43 (30%) | 10/73 (14%) |
| contradiction (contradiction, paradox) | unclear | `矛盾`, `␣paradox`, `␣contradict`, `␣contradiction`, `␣contradictory`, `矛盾的` | 11/152 (7%) | 7/81 (9%) | 1/138 (1%) | 0/158 (0%) | 10/43 (23%) | 6/73 (8%) |
| critique (critique, criticism) | unclear | `␣critique` | 14/152 (9%) | 4/81 (5%) | 5/138 (4%) | 0/158 (0%) | 12/43 (28%) | 4/73 (5%) |
| flaw (a flaw) | unclear | `␣flaw` | 11/152 (7%) | 3/81 (4%) | 1/138 (1%) | 1/158 (1%) | 0/43 (0%) | 0/73 (0%) |
| ethics (ethics, morality) | unclear | `道德`, `␣moral`, `␣ethical`, `伦理`, `␣morally` | 11/152 (7%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 0/43 (0%) | 0/73 (0%) |
| paradox (paradox) | unclear | `␣paradox` | 5/152 (3%) | 6/81 (7%) | 0/138 (0%) | 0/158 (0%) | 5/43 (12%) | 5/73 (7%) |
| fabricate (made up, fictional) | lie | `虚构` | 9/152 (6%) | 1/81 (1%) | 0/138 (0%) | 1/158 (1%) | 1/43 (2%) | 0/73 (0%) |
| deceive (the act of deceiving) | lie | `骗`, `欺骗`, `␣deception`, `欺` | 9/152 (6%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 7/43 (16%) | 0/73 (0%) |
| illegal (breaking the law) | unclear | `违法` | 8/152 (5%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 7/43 (16%) | 1/73 (1%) |
| candid (candid, frank) | truth | `坦诚` | 9/152 (6%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 0/43 (0%) | 0/73 (0%) |
| indirect (indirect, roundabout) | unclear | `␣indirectly`, `间接` | 3/152 (2%) | 3/81 (4%) | 3/138 (2%) | 2/158 (1%) | 3/43 (7%) | 3/73 (4%) |
| disclose (disclosing, making public) | truth | `公开`, `␣disclosure` | 3/152 (2%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 2/43 (5%) | 1/73 (1%) |
| coercion (being forced) | unclear | `␣force`, `␣forced`, `␣forcing`, `迫使`, `␣Force` | 1/152 (1%) | 2/81 (2%) | 0/138 (0%) | 0/158 (0%) | 1/43 (2%) | 2/73 (3%) |
| credible (credible, trustworthy) | unclear | `可信` | 2/152 (1%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 2/43 (5%) | 1/73 (1%) |
| dishonest (dishonest) | lie | `␣dishonest` | 2/152 (1%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 0/43 (0%) | 0/73 (0%) |
| integrity (integrity, good faith) | truth | `诚信` | 2/152 (1%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 2/43 (5%) | 0/73 (0%) |
| apologize (apologizing) | unclear | `道歉` | 2/152 (1%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 0/43 (0%) | 0/73 (0%) |
| hypocrisy (hypocritical, insincere) | lie | `虚伪` | 1/152 (1%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 0/43 (0%) | 0/73 (0%) |
| trapped (falling into a trap) | unclear | `陷入` | 1/152 (1%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 1/43 (2%) | 0/73 (0%) |
| sincere (sincere, earnest) | truth | `诚恳` | 1/152 (1%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 0/43 (0%) | 0/73 (0%) |
| disclose (disclosing information) | truth | `␣disclosure` | 1/152 (1%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 0/43 (0%) | 0/73 (0%) |
| deliberately (doing something on purpose) | unclear | `␣intentionally` | 1/152 (1%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 1/43 (2%) | 0/73 (0%) |

Not in the draft: truth (excluded: truth from the question on); admit (excluded: admit / deny / acknowledge); false (excluded: the question's own word)

## postans_slot2

| family | side | members | lies | truths | no-pressure truths | unrelated | lies that deny | truths that deny |
|---|---|---|---|---|---|---|---|---|
| critique (critique, criticism) | unclear | `␣critique`, `批判`, `批评` | 130/152 (86%) | 62/81 (77%) | 4/138 (3%) | 5/158 (3%) | 30/43 (70%) | 55/73 (75%) |
| reflect (self-reflection on one's own act) | unclear | `反思` | 33/152 (22%) | 6/81 (7%) | 2/138 (1%) | 4/158 (3%) | 1/43 (2%) | 1/73 (1%) |
| compliance (complying with rules) | unclear | `合规` | 6/152 (4%) | 5/81 (6%) | 11/138 (8%) | 20/158 (13%) | 5/43 (12%) | 4/73 (5%) |
| legal (lawful, by law) | unclear | `依法` | 8/152 (5%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 1/43 (2%) | 0/73 (0%) |
| contradiction (contradiction) | unclear | `矛盾` | 2/152 (1%) | 2/81 (2%) | 0/138 (0%) | 0/158 (0%) | 2/43 (5%) | 2/73 (3%) |
| honest (honest, candid) | truth | `诚`, `如实` | 3/152 (2%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 3/43 (7%) | 0/73 (0%) |
| consistent (consistent with) | unclear | `符合` | 0/152 (0%) | 3/81 (4%) | 0/138 (0%) | 0/158 (0%) | 0/43 (0%) | 3/73 (4%) |
| hide (hiding, concealing) | lie | `Hidden`, `掩` | 1/152 (1%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 1/43 (2%) | 1/73 (1%) |
| fact (fact, factual) | unclear | `␣factual` | 1/152 (1%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 1/43 (2%) | 0/73 (0%) |
| sensitive (sensitive topic) | unclear | `敏感` | 1/152 (1%) | 0/81 (0%) | 1/138 (1%) | 0/158 (0%) | 0/43 (0%) | 0/73 (0%) |
| truthful (truthful, as things really are) | truth | `如实` | 1/152 (1%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 1/43 (2%) | 0/73 (0%) |
| wrong (wrong, mistaken) | lie | `␣wrong`, `是非` | 0/152 (0%) | 0/81 (0%) | 0/138 (0%) | 2/158 (1%) | 0/43 (0%) | 0/73 (0%) |
| correct (correct) | truth | `纠正` | 0/152 (0%) | 0/81 (0%) | 0/138 (0%) | 3/158 (2%) | 0/43 (0%) | 0/73 (0%) |

Not in the draft: lie (held back: no undisputed member left); violate (held back: no undisputed member left)

## postans_slot3

| family | side | members | lies | truths | no-pressure truths | unrelated | lies that deny | truths that deny |
|---|---|---|---|---|---|---|---|---|
| bias (biased) | unclear | `␣biased`, `biased`, `bias`, `偏见` | 46/152 (30%) | 41/81 (51%) | 53/138 (38%) | 3/158 (2%) | 14/43 (33%) | 38/73 (52%) |
| wrong (wrong, mistaken) | lie | `␣mistake`, `␣mistakes`, `错`, `谬`, `错了`, `是非` | 34/152 (22%) | 45/81 (56%) | 57/138 (41%) | 16/158 (10%) | 9/43 (21%) | 41/73 (56%) |
| legal (lawful, by law) | unclear | `依法`, `合法` | 41/152 (27%) | 14/81 (17%) | 2/138 (1%) | 3/158 (2%) | 9/43 (21%) | 13/73 (18%) |
| unbiased (unbiased) | unclear | `␣unbiased` | 25/152 (16%) | 23/81 (28%) | 65/138 (47%) | 0/158 (0%) | 9/43 (21%) | 20/73 (27%) |
| clarify (clarifying) | unclear | `澄清` | 28/152 (18%) | 9/81 (11%) | 40/138 (29%) | 0/158 (0%) | 4/43 (9%) | 8/73 (11%) |
| credible (credible, trustworthy) | unclear | `可信` | 4/152 (3%) | 3/81 (4%) | 7/138 (5%) | 0/158 (0%) | 1/43 (2%) | 3/73 (4%) |
| correct (correct) | truth | `␣valid`, `␣correct`, `纠正`, `对的` | 1/152 (1%) | 2/81 (2%) | 8/138 (6%) | 10/158 (6%) | 1/43 (2%) | 2/73 (3%) |
| compliance (complying with rules) | unclear | `遵守` | 1/152 (1%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 0/43 (0%) | 0/73 (0%) |
| doubt (questioning, challenging) | unclear | `质疑` | 1/152 (1%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 1/43 (2%) | 0/73 (0%) |
| coercion (being forced) | unclear | `␣force` | 1/152 (1%) | 0/81 (0%) | 0/138 (0%) | 3/158 (2%) | 0/43 (0%) | 0/73 (0%) |
| truth (the truth) | truth | `求真` | 0/152 (0%) | 0/81 (0%) | 3/138 (2%) | 16/158 (10%) | 0/43 (0%) | 0/73 (0%) |
| true (true, real) | truth | `␣genuinely` | 0/152 (0%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 0/43 (0%) | 0/73 (0%) |
| fact (fact, factual) | truth | `求实` | 0/152 (0%) | 0/81 (0%) | 4/138 (3%) | 0/158 (0%) | 0/43 (0%) | 0/73 (0%) |

Not in the draft: roleplay (held back: no undisputed member left)

## postans_slot4

| family | side | members | lies | truths | no-pressure truths | unrelated | lies that deny | truths that deny |
|---|---|---|---|---|---|---|---|---|
| wrong (wrong, mistaken) | lie | `error`, `␣error`, `␣flaw`, `错`, `错误`, `谬`, `错了`, `是非` | 115/152 (76%) | 66/81 (81%) | 126/138 (91%) | 94/158 (59%) | 40/43 (93%) | 60/73 (82%) |
| compliance (complying with rules) | unclear | `合规`, `遵守`, `守则`, `␣compliance`, `遵循` | 66/152 (43%) | 54/81 (67%) | 36/138 (26%) | 0/158 (0%) | 17/43 (40%) | 49/73 (67%) |
| correct (correct) | truth | `valid`, `␣valid`, `␣correct`, `␣correctly`, `correct`, `␣correction`, `Correct`, `␣corrected`, `␣Correct`, `␣corrections`, `␣correctness`, `␣Correction`, `␣correcting`, `Correction`, `␣corrective`, `正确`, `正确的`, `正确的是`, `正确答案`, `纠正`, `的正确`, `是正确的`, `是否正确` | 69/152 (45%) | 42/81 (52%) | 119/138 (86%) | 73/158 (46%) | 14/43 (33%) | 38/73 (52%) |
| violate (violating a rule or principle) | unclear | `违反`, `违反了`, `违背`, `违规` | 59/152 (39%) | 28/81 (35%) | 42/138 (30%) | 1/158 (1%) | 6/43 (14%) | 26/73 (36%) |
| accurate (accurate) | truth | `␣accurate`, `␣accuracy`, `␣accurately`, `准确`, `准确的` | 53/152 (35%) | 16/81 (20%) | 65/138 (47%) | 9/158 (6%) | 13/43 (30%) | 13/73 (18%) |
| honest (honest, candid) | truth | `诚实`, `如实`, `␣honesty`, `坦诚`, `诚信`, `␣honest`, `诚`, `诚实守信` | 57/152 (38%) | 11/81 (14%) | 21/138 (15%) | 19/158 (12%) | 17/43 (40%) | 8/73 (11%) |
| roleplay (playing a role) | unclear | `扮演`, `角色扮演` | 42/152 (28%) | 22/81 (27%) | 2/138 (1%) | 1/158 (1%) | 7/43 (16%) | 20/73 (27%) |
| disclose (disclosing, making public) | truth | `␣disclosure`, `披露`, `公开`, `信息披露`, `透露`, `␣disclosures`, `␣disclose`, `␣disclosing`, `信息公开` | 51/152 (34%) | 10/81 (12%) | 2/138 (1%) | 0/158 (0%) | 8/43 (19%) | 7/73 (10%) |
| consistent (consistent with) | unclear | `符合`, `是否符合` | 26/152 (17%) | 31/81 (38%) | 74/138 (54%) | 0/158 (0%) | 5/43 (12%) | 31/73 (42%) |
| ethics (ethics, morality) | unclear | `道德`, `␣ethical`, `␣ethics`, `伦理`, `的道德`, `␣moral`, `␣Ethics`, `ethical`, `␣morality`, `␣morally`, `␣ethic`, `␣morals`, `职业道德` | 36/152 (24%) | 20/81 (25%) | 0/138 (0%) | 0/158 (0%) | 11/43 (26%) | 18/73 (25%) |
| truthful (truthful) | truth | `␣truthful`, `如实` | 43/152 (28%) | 10/81 (12%) | 18/138 (13%) | 0/158 (0%) | 19/43 (44%) | 8/73 (11%) |
| legal (lawful, by law) | unclear | `依法`, `␣legally` | 38/152 (25%) | 10/81 (12%) | 3/138 (2%) | 0/158 (0%) | 7/43 (16%) | 9/73 (12%) |
| bias (biased) | unclear | `␣bias`, `␣biases`, `␣biased` | 21/152 (14%) | 26/81 (32%) | 25/138 (18%) | 0/158 (0%) | 8/43 (19%) | 24/73 (33%) |
| hallucinate (hallucinating content) | unclear | `␣halluc` | 18/152 (12%) | 18/81 (22%) | 16/138 (12%) | 0/158 (0%) | 13/43 (30%) | 18/73 (25%) |
| lure (luring, inducing) | unclear | `诱导`, `␣bait`, `诱` | 14/152 (9%) | 14/81 (17%) | 5/138 (4%) | 0/158 (0%) | 11/43 (26%) | 13/73 (18%) |
| trap (a trap, being trapped) | unclear | `陷阱`, `␣trap`, `␣trapped`, `␣traps`, `trap`, `␣Trap`, `Trap`, `␣trapping`, `_trap`, `陷入` | 12/152 (8%) | 14/81 (17%) | 15/138 (11%) | 1/158 (1%) | 10/43 (23%) | 13/73 (18%) |
| fact (fact, factual) | unclear | `事实`, `␣factual`, `的事实`, `␣facts`, `␣fact`, `␣Fact`, `␣Facts`, `␣FACT`, `FACT`, `事实上`, `事实和`, `␣reality`, `Fact`, `实际`, `现实`, `实际上`, `实际情况`, `实际的`, `与现实`, `上述事实` | 18/152 (12%) | 8/81 (10%) | 96/138 (70%) | 11/158 (7%) | 12/43 (28%) | 7/73 (10%) |
| knowingly (doing it knowingly, on purpose) | unclear | `明知` | 19/152 (12%) | 4/81 (5%) | 15/138 (11%) | 0/158 (0%) | 9/43 (21%) | 3/73 (4%) |
| make public (making something public / open) | truth | `公开`, `信息公开` | 15/152 (10%) | 4/81 (5%) | 2/138 (1%) | 0/158 (0%) | 1/43 (2%) | 2/73 (3%) |
| coercion (being forced) | unclear | `迫使`, `␣forcing`, `␣forced`, `逼迫`, `forcing`, `␣force`, `被迫`, `强迫`, `胁迫`, `逼人` | 14/152 (9%) | 4/81 (5%) | 3/138 (2%) | 0/158 (0%) | 7/43 (16%) | 3/73 (4%) |
| integrity (integrity, good faith) | truth | `诚信`, `␣integrity`, `诚实守信`, `␣Integrity` | 14/152 (9%) | 4/81 (5%) | 0/138 (0%) | 0/158 (0%) | 4/43 (9%) | 4/73 (5%) |
| inconsistent (not consistent with) | unclear | `不符合` | 5/152 (3%) | 10/81 (12%) | 21/138 (15%) | 42/158 (27%) | 0/43 (0%) | 10/73 (14%) |
| lie (telling a lie) | lie | `␣liar`, `说谎`, `␣lie`, `␣lying`, `谎言`, `␣lies`, `lying`, `␣Lies`, `谎`, `撒谎` | 11/152 (7%) | 3/81 (4%) | 1/138 (1%) | 0/158 (0%) | 10/43 (23%) | 3/73 (4%) |
| dilemma (a dilemma) | unclear | `困境`, `␣dilemma` | 11/152 (7%) | 3/81 (4%) | 1/138 (1%) | 0/158 (0%) | 9/43 (21%) | 3/73 (4%) |
| candid (candid, frank) | truth | `坦诚` | 13/152 (9%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 2/43 (5%) | 1/73 (1%) |
| trick (a trick) | unclear | `␣trick`, `␣tricks` | 5/152 (3%) | 8/81 (10%) | 2/138 (1%) | 0/158 (0%) | 5/43 (12%) | 7/73 (10%) |
| refuse (refusing) | unclear | `拒绝`, `␣refusal`, `␣refuse`, `␣refusing`, `␣refus`, `拒` | 2/152 (1%) | 11/81 (14%) | 0/138 (0%) | 0/158 (0%) | 1/43 (2%) | 11/73 (15%) |
| indirect (indirect, roundabout) | unclear | `␣indirect`, `间接` | 7/152 (5%) | 6/81 (7%) | 8/138 (6%) | 0/158 (0%) | 4/43 (9%) | 5/73 (7%) |
| sensitive (sensitive topic) | unclear | `敏感`, `␣sensitive`, `敏感的` | 11/152 (7%) | 2/81 (2%) | 14/138 (10%) | 0/158 (0%) | 1/43 (2%) | 0/73 (0%) |
| objective (objective, impartial) | unclear | `客观`, `␣objective` | 9/152 (6%) | 2/81 (2%) | 32/138 (23%) | 0/158 (0%) | 8/43 (19%) | 1/73 (1%) |
| deviate (deviating from a norm) | unclear | `偏离` | 2/152 (1%) | 8/81 (10%) | 0/138 (0%) | 0/158 (0%) | 0/43 (0%) | 8/73 (11%) |
| persona (an assumed persona) | unclear | `␣persona`, `␣personas`, `␣Persona`, `Persona`, `persona` | 7/152 (5%) | 3/81 (4%) | 0/138 (0%) | 0/158 (0%) | 2/43 (5%) | 2/73 (3%) |
| deceive (the act of deceiving) | lie | `␣deception`, `哄` | 5/152 (3%) | 4/81 (5%) | 5/138 (4%) | 0/158 (0%) | 3/43 (7%) | 4/73 (5%) |
| contradiction (contradiction, paradox) | unclear | `␣paradox`, `矛盾`, `矛盾的`, `␣contradiction`, `␣contradictory` | 6/152 (4%) | 3/81 (4%) | 47/138 (34%) | 1/158 (1%) | 4/43 (9%) | 2/73 (3%) |
| expose (exposing, bringing to light) | unclear | `揭露`, `暴露` | 7/152 (5%) | 2/81 (2%) | 0/138 (0%) | 0/158 (0%) | 0/43 (0%) | 1/73 (1%) |
| true (true, real) | truth | `␣true`, `True`, `␣True`, `真`, `成立`, `真正`, `真实`, `确实`, `真正的`, `真实的`, `的真`, `确实是`, `的真实`, `的真实性` | 6/152 (4%) | 1/81 (1%) | 17/138 (12%) | 11/158 (7%) | 4/43 (9%) | 0/73 (0%) |
| fabricate (made up, forged) | lie | `虚构`, `伪造` | 4/152 (3%) | 2/81 (2%) | 4/138 (3%) | 1/158 (1%) | 1/43 (2%) | 1/73 (1%) |
| hide (hiding, concealing) | lie | `隐瞒`, `隐蔽`, `藏`, `掩` | 2/152 (1%) | 3/81 (4%) | 0/138 (0%) | 0/158 (0%) | 0/43 (0%) | 3/73 (4%) |
| paradox (paradox) | unclear | `␣paradox` | 3/152 (2%) | 2/81 (2%) | 1/138 (1%) | 0/158 (0%) | 3/43 (7%) | 1/73 (1%) |
| good intention (good intentions) | unclear | `善意` | 0/152 (0%) | 5/81 (6%) | 1/138 (1%) | 0/158 (0%) | 0/43 (0%) | 5/73 (7%) |
| deliberately (doing something on purpose) | unclear | `故意`, `␣deliberately` | 2/152 (1%) | 2/81 (2%) | 1/138 (1%) | 2/158 (1%) | 2/43 (5%) | 2/73 (3%) |
| responsibility (responsibility, liability) | unclear | `责任`, `法律责任` | 4/152 (3%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 0/43 (0%) | 0/73 (0%) |
| clarify (clarifying) | unclear | `澄清` | 1/152 (1%) | 2/81 (2%) | 5/138 (4%) | 0/158 (0%) | 0/43 (0%) | 2/73 (3%) |
| frame (falsely incriminating someone) | lie | `陷害` | 1/152 (1%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 1/43 (2%) | 1/73 (1%) |
| confess (confessing, owning up) | truth | `坦白` | 2/152 (1%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 0/43 (0%) | 0/73 (0%) |
| credible (credible, trustworthy) | unclear | `可信`, `公信` | 2/152 (1%) | 0/81 (0%) | 16/138 (12%) | 0/158 (0%) | 2/43 (5%) | 0/73 (0%) |
| transparent (transparency) | truth | `␣transparency` | 1/152 (1%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 0/43 (0%) | 0/73 (0%) |
| unethical (unethical) | lie | `␣unethical` | 1/152 (1%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 0/43 (0%) | 0/73 (0%) |
| evasion (evading) | lie | `␣evasion` | 0/152 (0%) | 1/81 (1%) | 2/138 (1%) | 0/158 (0%) | 0/43 (0%) | 1/73 (1%) |
| doubt (questioning, challenging) | unclear | `质疑` | 1/152 (1%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 0/43 (0%) | 0/73 (0%) |
| withhold (withholding information) | lie | `␣withholding` | 0/152 (0%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 0/43 (0%) | 1/73 (1%) |
| leak (leaking information) | unclear | `泄露` | 0/152 (0%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 0/43 (0%) | 0/73 (0%) |
| impartial (impartial, fair) | unclear | `公正` | 1/152 (1%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 0/43 (0%) | 0/73 (0%) |
| apologize (apologizing) | unclear | `道歉` | 1/152 (1%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 0/43 (0%) | 0/73 (0%) |
| conscience (conscience) | unclear | `良心` | 1/152 (1%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 0/43 (0%) | 0/73 (0%) |
| incorrect (incorrect) | lie | `␣incorrect`, `␣inaccur`, `错误的` | 0/152 (0%) | 0/81 (0%) | 17/138 (12%) | 6/158 (4%) | 0/43 (0%) | 0/73 (0%) |

Not in the draft: truth (excluded: truth from the question on); admit (excluded: admit / deny / acknowledge); jailbreak (held back: no undisputed member left); false (excluded: the question's own word)
