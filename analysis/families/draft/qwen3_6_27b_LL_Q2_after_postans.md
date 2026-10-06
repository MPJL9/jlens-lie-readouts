# Draft families: qwen3.6-27b, logit lens, part Q2_after, group postans

Written by `scripts/apply_family_decisions.py` (2026-10-01; draft, not frozen). Counts are `present / transcripts (share)`
on the build split.

## postans_slot0

| family | side | members | lies | truths | no-pressure truths | unrelated | lies that deny | truths that deny |
|---|---|---|---|---|---|---|---|---|
| sincere (sincere, earnest) | truth | `诚挚` | 132/152 (87%) | 68/81 (84%) | 113/138 (82%) | 11/158 (7%) | 35/47 (74%) | 64/77 (83%) |
| neutral (neutral, impartial) | unclear | `中立` | 57/152 (38%) | 46/81 (57%) | 97/138 (70%) | 158/158 (100%) | 10/47 (21%) | 43/77 (56%) |
| wrong (wrong, mistaken) | lie | `错` | 3/152 (2%) | 3/81 (4%) | 1/138 (1%) | 0/158 (0%) | 3/47 (6%) | 3/77 (4%) |
| expose (to expose, lay bare) | truth | `揭` | 3/152 (2%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 0/47 (0%) | 0/77 (0%) |

Not in the draft: fake (held back: no undisputed member left); deceive (excluded: the question's own word); fact (excluded: truth from the question on)

## postans_slot1

| family | side | members | lies | truths | no-pressure truths | unrelated | lies that deny | truths that deny |
|---|---|---|---|---|---|---|---|---|
| conceal (to hide, cover up) | lie | `隐瞒`, `-hide`, `藏`, `掩` | 131/152 (86%) | 51/81 (63%) | 30/138 (22%) | 40/158 (25%) | 29/47 (62%) | 47/77 (61%) |
| conform (to conform to, be consistent with) | unclear | `符合`, `是否符合`, `符合要求` | 100/152 (66%) | 63/81 (78%) | 119/138 (86%) | 15/158 (9%) | 35/47 (74%) | 62/77 (81%) |
| true (true, real) | truth | `␣true`, `true`, `␣real`, `True`, `␣True`, `␣genuine`, `真`, `真实`, `确实`, `真实的`, `成真` | 101/152 (66%) | 10/81 (12%) | 56/138 (41%) | 5/158 (3%) | 12/47 (26%) | 7/77 (9%) |
| knowingly (knowing full well (as in 明知故犯)) | unclear | `明知` | 97/152 (64%) | 5/81 (6%) | 1/138 (1%) | 0/158 (0%) | 14/47 (30%) | 3/77 (4%) |
| honest (honest, honesty) | truth | `诚实`, `诚`, `␣honest`, `␣honesty`, `诚恳` | 86/152 (57%) | 15/81 (19%) | 27/138 (20%) | 4/158 (3%) | 1/47 (2%) | 13/77 (17%) |
| violate (to violate, go against (rules, principles)) | unclear | `违背`, `违反`, `违反了`, `违法` | 72/152 (47%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 11/47 (23%) | 0/77 (0%) |
| nonconform (not consistent with, does not conform) | unclear | `不符合` | 51/152 (34%) | 16/81 (20%) | 0/138 (0%) | 0/158 (0%) | 2/47 (4%) | 15/77 (19%) |
| legal (lawful, according to law) | unclear | `合法`, `依法`, `合法的`, `␣legally` | 32/152 (21%) | 29/81 (36%) | 17/138 (12%) | 0/158 (0%) | 28/47 (60%) | 29/77 (38%) |
| comply (compliant, to comply with rules) | unclear | `合规`, `遵守` | 34/152 (22%) | 23/81 (28%) | 15/138 (11%) | 0/158 (0%) | 34/47 (72%) | 23/77 (30%) |
| ethical (ethical, ethics) | unclear | `␣ethical`, `ethical`, `伦理`, `␣ethics`, `道德`, `的道德`, `␣moral`, `␣morally` | 46/152 (30%) | 9/81 (11%) | 0/138 (0%) | 0/158 (0%) | 2/47 (4%) | 8/77 (10%) |
| factual (factual, the facts) | truth | `事实`, `␣factual` | 36/152 (24%) | 10/81 (12%) | 65/138 (47%) | 85/158 (54%) | 10/47 (21%) | 9/77 (12%) |
| moral (moral, morality) | unclear | `道德`, `␣moral`, `␣morally`, `的道德` | 33/152 (22%) | 9/81 (11%) | 0/138 (0%) | 0/158 (0%) | 2/47 (4%) | 8/77 (10%) |
| objective (objective, unslanted) | unclear | `客观`, `␣objectively` | 27/152 (18%) | 12/81 (15%) | 13/138 (9%) | 6/158 (4%) | 14/47 (30%) | 12/77 (16%) |
| wrong (wrong, mistaken) | lie | `␣flaw`, `错`, `不对`, `是非` | 18/152 (12%) | 6/81 (7%) | 3/138 (2%) | 2/158 (1%) | 11/47 (23%) | 6/77 (8%) |
| truthful (truthful, as it really is) | truth | `␣truthful`, `如实` | 13/152 (9%) | 9/81 (11%) | 20/138 (14%) | 2/158 (1%) | 0/47 (0%) | 9/77 (12%) |
| upright (upright, principled) | truth | `正直` | 4/152 (3%) | 16/81 (20%) | 3/138 (2%) | 0/158 (0%) | 1/47 (2%) | 16/77 (21%) |
| accurate (accurate) | truth | `␣accurate`, `␣accuracy`, `␣accurately`, `准确`, `准确的` | 12/152 (8%) | 8/81 (10%) | 48/138 (35%) | 6/158 (4%) | 1/47 (2%) | 7/77 (9%) |
| correct (correct) | truth | `valid`, `␣valid`, `␣correct`, `正确`, `正确的` | 7/152 (5%) | 12/81 (15%) | 10/138 (7%) | 4/158 (3%) | 5/47 (11%) | 12/77 (16%) |
| justify (to justify, rationalize) | unclear | `␣justification`, `justify`, `合理化`, `正当` | 10/152 (7%) | 6/81 (7%) | 0/138 (0%) | 0/158 (0%) | 10/47 (21%) | 6/77 (8%) |
| critique (a critique, to criticize) | unclear | `␣critique` | 8/152 (5%) | 7/81 (9%) | 8/138 (6%) | 0/158 (0%) | 6/47 (13%) | 7/77 (9%) |
| lie (to tell a lie) | lie | `撒谎`, `说谎`, `␣lie`, `␣lying`, `谎`, `谎言`, `lying`, `␣lies` | 12/152 (8%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 10/47 (21%) | 0/77 (0%) |
| private (private, kept to oneself) | lie | `␣private`, `私密` | 11/152 (7%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 1/47 (2%) | 1/77 (1%) |
| legitimate (legitimate, justified) | unclear | `正当`, `␣legitimate` | 5/152 (3%) | 6/81 (7%) | 0/138 (0%) | 0/158 (0%) | 5/47 (11%) | 6/77 (8%) |
| fact (fact, factual) | truth | `␣fact`, `␣reality`, `␣facts`, `实际上`, `事实上`, `求实`, `与现实`, `事实和` | 7/152 (5%) | 4/81 (5%) | 3/138 (2%) | 1/158 (1%) | 1/47 (2%) | 4/77 (5%) |
| illegal (against the law) | unclear | `违法` | 9/152 (6%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 9/47 (19%) | 0/77 (0%) |
| false (false, untrue) | lie | `␣false`, `␣False`, `false`, `假`, `虚假` | 8/152 (5%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 6/47 (13%) | 1/77 (1%) |
| candid (candid, frank) | truth | `坦诚` | 6/152 (4%) | 2/81 (2%) | 0/138 (0%) | 2/158 (1%) | 0/47 (0%) | 2/77 (3%) |
| contradiction (contradiction, inconsistency) | unclear | `矛盾`, `␣contradictory` | 3/152 (2%) | 5/81 (6%) | 0/138 (0%) | 0/158 (0%) | 2/47 (4%) | 5/77 (6%) |
| refuse (to refuse) | unclear | `拒绝`, `␣refusal` | 0/152 (0%) | 6/81 (7%) | 0/138 (0%) | 0/158 (0%) | 0/47 (0%) | 6/77 (8%) |
| fabricate (made up, fictional) | lie | `虚构` | 5/152 (3%) | 0/81 (0%) | 0/138 (0%) | 1/158 (1%) | 0/47 (0%) | 0/77 (0%) |
| neutral (neutral, impartial) | unclear | `中立` | 0/152 (0%) | 2/81 (2%) | 0/138 (0%) | 0/158 (0%) | 0/47 (0%) | 2/77 (3%) |
| disclose (to disclose) | truth | `␣disclosure` | 2/152 (1%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 1/47 (2%) | 0/77 (0%) |
| public (public, made public) | unclear | `公开` | 1/152 (1%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 1/47 (2%) | 1/77 (1%) |
| credible (credible, trustworthy) | truth | `可信` | 2/152 (1%) | 0/81 (0%) | 2/138 (1%) | 0/158 (0%) | 2/47 (4%) | 0/77 (0%) |
| sincere (sincere, earnest) | truth | `诚恳` | 1/152 (1%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 0/47 (0%) | 0/77 (0%) |
| confess (to own up, make a clean breast) | truth | `坦白` | 1/152 (1%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 0/47 (0%) | 0/77 (0%) |
| forced (forced, compelled) | unclear | `␣forced`, `forced`, `␣forcing`, `强制`, `被迫`, `迫使` | 0/152 (0%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 0/47 (0%) | 1/77 (1%) |
| apologize (to apologize) | unclear | `道歉` | 1/152 (1%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 0/47 (0%) | 0/77 (0%) |
| regret (regret, remorse) | unclear | `悔` | 1/152 (1%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 0/47 (0%) | 0/77 (0%) |

Not in the draft: admit (excluded: admit / deny / acknowledge); deny (excluded: admit / deny / acknowledge); truth (excluded: truth from the question on); harm (held back: no undisputed member left); deceive (excluded: the question's own word)

## postans_slot2

| family | side | members | lies | truths | no-pressure truths | unrelated | lies that deny | truths that deny |
|---|---|---|---|---|---|---|---|---|
| critique (a critique, to criticize) | unclear | `␣critique`, `批判`, `批评`, `␣criticism`, `␣critic`, `␣critiques` | 130/152 (86%) | 67/81 (83%) | 13/138 (9%) | 21/158 (13%) | 31/47 (66%) | 63/77 (82%) |
| critical (critical (judging faults)) | unclear | `␣critical`, `critical`, `␣Critical`, `Critical`, `␣critically`, `_critical` | 80/152 (53%) | 33/81 (41%) | 0/138 (0%) | 0/158 (0%) | 15/47 (32%) | 30/77 (39%) |
| reflect (to reflect on oneself, self-examine) | unclear | `反思` | 34/152 (22%) | 5/81 (6%) | 1/138 (1%) | 4/158 (3%) | 3/47 (6%) | 3/77 (4%) |
| comply (compliant, to comply with rules) | unclear | `合规` | 5/152 (3%) | 3/81 (4%) | 11/138 (8%) | 29/158 (18%) | 4/47 (9%) | 3/77 (4%) |
| legal (lawful, according to law) | unclear | `依法`, `合法性` | 4/152 (3%) | 3/81 (4%) | 8/138 (6%) | 25/158 (16%) | 0/47 (0%) | 3/77 (4%) |
| conform (to conform to, be consistent with) | unclear | `符合` | 1/152 (1%) | 2/81 (2%) | 0/138 (0%) | 0/158 (0%) | 1/47 (2%) | 2/77 (3%) |
| conceal (to hide, cover up) | lie | `Hidden`, `掩` | 1/152 (1%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 1/47 (2%) | 1/77 (1%) |
| correct (correct) | truth | `纠正` | 1/152 (1%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 1/47 (2%) | 1/77 (1%) |
| factual (factual, the facts) | truth | `␣factual`, `事实` | 1/152 (1%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 1/47 (2%) | 0/77 (0%) |
| truthful (truthful, as it really is) | truth | `如实` | 1/152 (1%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 1/47 (2%) | 0/77 (0%) |
| lure (to lure, induce) | unclear | `诱导` | 1/152 (1%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 1/47 (2%) | 0/77 (0%) |
| persuade (persuasive) | unclear | `␣persuasive` | 0/152 (0%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 0/47 (0%) | 1/77 (1%) |
| hidden (hidden, undisclosed (state)) | lie | `Hidden` | 0/152 (0%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 0/47 (0%) | 1/77 (1%) |
| contradiction (contradiction, inconsistency) | unclear | `矛盾` | 0/152 (0%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 0/47 (0%) | 1/77 (1%) |
| wrong (wrong, mistaken) | lie | `error`, `是非` | 1/152 (1%) | 0/81 (0%) | 0/138 (0%) | 1/158 (1%) | 1/47 (2%) | 0/77 (0%) |

Not in the draft: violate (held back: no undisputed member left); truth (excluded: truth from the question on); harm (held back: no undisputed member left)

## postans_slot3

| family | side | members | lies | truths | no-pressure truths | unrelated | lies that deny | truths that deny |
|---|---|---|---|---|---|---|---|---|
| biased (biased, bias) | unclear | `␣biased`, `␣bias`, `biased` | 26/152 (17%) | 29/81 (36%) | 46/138 (33%) | 3/158 (2%) | 9/47 (19%) | 28/77 (36%) |
| clarify (to clarify, set the record straight) | unclear | `澄清`, `␣clarification` | 18/152 (12%) | 7/81 (9%) | 46/138 (33%) | 0/158 (0%) | 2/47 (4%) | 6/77 (8%) |
| legal (lawful, according to law) | unclear | `依法`, `合法`, `依法依规` | 17/152 (11%) | 5/81 (6%) | 6/138 (4%) | 7/158 (4%) | 4/47 (9%) | 4/77 (5%) |
| unbiased (unbiased, impartial) | unclear | `␣unbiased` | 6/152 (4%) | 11/81 (14%) | 46/138 (33%) | 0/158 (0%) | 3/47 (6%) | 11/77 (14%) |
| wrong (wrong, mistaken) | lie | `错`, `谬`, `错了`, `是非` | 3/152 (2%) | 8/81 (10%) | 41/138 (30%) | 6/158 (4%) | 1/47 (2%) | 8/77 (10%) |
| credible (credible, trustworthy) | truth | `可信` | 5/152 (3%) | 2/81 (2%) | 4/138 (3%) | 0/158 (0%) | 2/47 (4%) | 2/77 (3%) |
| critique (a critique, to criticize) | unclear | `␣critique`, `批评` | 3/152 (2%) | 2/81 (2%) | 2/138 (1%) | 25/158 (16%) | 1/47 (2%) | 2/77 (3%) |
| legal (lawful, legal) | unclear | `合法` | 3/152 (2%) | 2/81 (2%) | 6/138 (4%) | 7/158 (4%) | 2/47 (4%) | 2/77 (3%) |
| role (a role (being played)) | unclear | `角色的`, `角色` | 3/152 (2%) | 0/81 (0%) | 2/138 (1%) | 0/158 (0%) | 2/47 (4%) | 0/77 (0%) |
| critical (critical (judging faults)) | unclear | `␣critically` | 0/152 (0%) | 1/81 (1%) | 0/138 (0%) | 6/158 (4%) | 0/47 (0%) | 1/77 (1%) |
| conform (to conform to, be consistent with) | unclear | `符合` | 1/152 (1%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 0/47 (0%) | 0/77 (0%) |
| correct (correct) | truth | `␣valid`, `␣correct`, `对的` | 0/152 (0%) | 1/81 (1%) | 5/138 (4%) | 5/158 (3%) | 0/47 (0%) | 1/77 (1%) |
| truth (the truth) | truth | `求真` | 0/152 (0%) | 0/81 (0%) | 0/138 (0%) | 10/158 (6%) | 0/47 (0%) | 0/77 (0%) |
| fact (fact, factual) | truth | `求实` | 0/152 (0%) | 0/81 (0%) | 1/138 (1%) | 0/158 (0%) | 0/47 (0%) | 0/77 (0%) |

## postans_slot4

| family | side | members | lies | truths | no-pressure truths | unrelated | lies that deny | truths that deny |
|---|---|---|---|---|---|---|---|---|
| wrong (wrong, mistaken) | lie | `␣flaw`, `错`, `错误`, `谬`, `错了`, `是非` | 117/152 (77%) | 75/81 (93%) | 137/138 (99%) | 74/158 (47%) | 45/47 (96%) | 73/77 (95%) |
| comply (compliant, to comply with rules) | unclear | `合规`, `␣compliance`, `遵守`, `␣Compliance` | 79/152 (52%) | 63/81 (78%) | 50/138 (36%) | 0/158 (0%) | 19/47 (40%) | 61/77 (79%) |
| moral (moral, morality) | unclear | `道德`, `的道德`, `␣moral`, `␣morality`, `职业道德`, `␣morals`, `␣morally`, `␣Moral`, `␣ethical`, `ethical`, `␣ethics`, `␣Ethics`, `␣ethic`, `伦理` | 97/152 (64%) | 43/81 (53%) | 7/138 (5%) | 0/158 (0%) | 33/47 (70%) | 42/77 (55%) |
| ethical (ethical, ethics) | unclear | `␣ethical`, `␣ethics`, `伦理`, `␣Ethics`, `ethical`, `␣ethic` | 90/152 (59%) | 36/81 (44%) | 5/138 (4%) | 0/158 (0%) | 28/47 (60%) | 36/77 (47%) |
| honest (honest, honesty) | truth | `诚实`, `␣honesty`, `␣honest`, `诚信`, `诚实守信`, `诚`, `␣honestly` | 78/152 (51%) | 18/81 (22%) | 64/138 (46%) | 12/158 (8%) | 26/47 (55%) | 18/77 (23%) |
| persona (a persona) | unclear | `␣persona`, `␣personas`, `␣Persona`, `Persona`, `扮演`, `角色扮演` | 58/152 (38%) | 26/81 (32%) | 10/138 (7%) | 0/158 (0%) | 17/47 (36%) | 26/77 (34%) |
| role_play (to play a role, role-play) | unclear | `扮演`, `角色扮演` | 57/152 (38%) | 24/81 (30%) | 9/138 (7%) | 0/158 (0%) | 17/47 (36%) | 24/77 (31%) |
| disclose (to disclose) | truth | `␣disclosure`, `披露`, `信息披露`, `透露`, `␣disclosures`, `␣Disclosure`, `␣disclosing` | 69/152 (45%) | 9/81 (11%) | 13/138 (9%) | 3/158 (2%) | 9/47 (19%) | 8/77 (10%) |
| truthful (truthful, as it really is) | truth | `␣truthful`, `如实` | 44/152 (29%) | 7/81 (9%) | 79/138 (57%) | 0/158 (0%) | 20/47 (43%) | 7/77 (9%) |
| violate (to violate, go against (rules, principles)) | unclear | `违反`, `违反了`, `违背`, `违规` | 41/152 (27%) | 8/81 (10%) | 48/138 (35%) | 1/158 (1%) | 1/47 (2%) | 8/77 (10%) |
| conform (to conform to, be consistent with) | unclear | `符合`, `是否符合` | 23/152 (15%) | 24/81 (30%) | 95/138 (69%) | 63/158 (40%) | 5/47 (11%) | 22/77 (29%) |
| accurate (accurate) | truth | `␣accurate`, `␣accuracy`, `␣accurately`, `准确`, `准确的` | 37/152 (24%) | 9/81 (11%) | 83/138 (60%) | 15/158 (9%) | 16/47 (34%) | 9/77 (12%) |
| biased (biased, bias) | unclear | `␣bias`, `偏见`, `␣biased`, `偏心` | 16/152 (11%) | 29/81 (36%) | 58/138 (42%) | 4/158 (3%) | 7/47 (15%) | 28/77 (36%) |
| hallucinate (to hallucinate (state made-up things without intent)) | unclear | `␣halluc` | 28/152 (18%) | 14/81 (17%) | 66/138 (48%) | 2/158 (1%) | 22/47 (47%) | 14/77 (18%) |
| deliberate (deliberate, on purpose) | unclear | `故意`, `␣deliberately`, `␣deliberate`, `明知` | 23/152 (15%) | 15/81 (19%) | 80/138 (58%) | 14/158 (9%) | 17/47 (36%) | 15/77 (19%) |
| legal (lawful, according to law) | unclear | `依法`, `合法`, `␣legally`, `␣legal`, `␣legality` | 31/152 (20%) | 5/81 (6%) | 1/138 (1%) | 0/158 (0%) | 5/47 (11%) | 4/77 (5%) |
| role (a role (being played)) | unclear | `角色`, `␣role`, `的角色`, `role`, `Role`, `␣Role`, `角色的`, `-role`, `␣roles`, `ROLE` | 20/152 (13%) | 15/81 (19%) | 1/138 (1%) | 0/158 (0%) | 5/47 (11%) | 15/77 (19%) |
| correct (correct) | truth | `␣correct`, `␣correctly`, `correct`, `Correct`, `␣Correct`, `正确`, `正确的`, `正确的是`, `正确答案`, `的正确`, `是正确的`, `是否正确` | 23/152 (15%) | 12/81 (15%) | 97/138 (70%) | 36/158 (23%) | 2/47 (4%) | 12/77 (16%) |
| lure (to lure, induce, bait) | unclear | `诱导`, `␣bait` | 11/152 (7%) | 22/81 (27%) | 33/138 (24%) | 0/158 (0%) | 10/47 (21%) | 22/77 (29%) |
| knowingly (knowing full well (as in 明知故犯)) | unclear | `明知` | 21/152 (14%) | 10/81 (12%) | 80/138 (58%) | 1/158 (1%) | 16/47 (34%) | 10/77 (13%) |
| harmful (harmful, harm) | unclear | `␣harmful`, `有害`, `␣harm`, `危害` | 22/152 (14%) | 6/81 (7%) | 1/138 (1%) | 0/158 (0%) | 3/47 (6%) | 5/77 (6%) |
| candid (candid, frank) | truth | `坦诚` | 24/152 (16%) | 2/81 (2%) | 3/138 (2%) | 0/158 (0%) | 4/47 (9%) | 2/77 (3%) |
| trap (a trap) | unclear | `陷阱`, `␣trap`, `␣trapped`, `␣traps`, `trap`, `Trap`, `␣Trap`, `␣trapping`, `_trap`, `␣bait` | 8/152 (5%) | 17/81 (21%) | 27/138 (20%) | 1/158 (1%) | 7/47 (15%) | 17/77 (22%) |
| deviate (to deviate, stray from) | unclear | `偏离` | 7/152 (5%) | 16/81 (20%) | 2/138 (1%) | 2/158 (1%) | 3/47 (6%) | 16/77 (21%) |
| integrity (integrity) | truth | `␣integrity`, `␣Integrity`, `正直` | 16/152 (11%) | 6/81 (7%) | 4/138 (3%) | 0/158 (0%) | 6/47 (13%) | 6/77 (8%) |
| factual (factual, the facts) | truth | `事实`, `␣factual`, `的事实`, `事实和` | 18/152 (12%) | 3/81 (4%) | 85/138 (62%) | 6/158 (4%) | 16/47 (34%) | 3/77 (4%) |
| forced (forced, compelled) | unclear | `强制`, `迫使`, `␣forcing`, `␣forced`, `逼迫`, `forcing`, `被迫`, `胁迫`, `强迫`, `forced`, `被逼` | 14/152 (9%) | 5/81 (6%) | 2/138 (1%) | 0/158 (0%) | 9/47 (19%) | 5/77 (6%) |
| reveal (to reveal) | truth | `揭示了`, `揭示`, `␣reveal`, `揭`, `揭露`, `暴露` | 15/152 (10%) | 2/81 (2%) | 0/138 (0%) | 2/158 (1%) | 3/47 (6%) | 2/77 (3%) |
| expose (to expose, lay bare) | truth | `揭露`, `揭`, `暴露` | 14/152 (9%) | 2/81 (2%) | 0/138 (0%) | 1/158 (1%) | 3/47 (6%) | 2/77 (3%) |
| transparent (transparent, transparency) | truth | `␣transparency`, `透明`, `透明度`, `␣Transparency`, `透明的`, `␣transparent`, `-transparent`, `transparent` | 11/152 (7%) | 3/81 (4%) | 1/138 (1%) | 0/158 (0%) | 3/47 (6%) | 3/77 (4%) |
| conceal (to hide, cover up) | lie | `隐蔽`, `隐瞒`, `␣hidden`, `隐藏`, `hidden`, `␣hide`, `␣hiding`, `␣concealed`, `␣conceal`, `␣hides`, `瞒`, `掩盖`, `掩饰`, `隐藏着`, `藏`, `掩`, `遮`, `隐` | 5/152 (3%) | 9/81 (11%) | 11/138 (8%) | 13/158 (8%) | 0/47 (0%) | 9/77 (12%) |
| objective (objective, unslanted) | unclear | `客观`, `␣objective`, `␣objectively`, `公正` | 12/152 (8%) | 1/81 (1%) | 31/138 (22%) | 1/158 (1%) | 9/47 (19%) | 1/77 (1%) |
| code_of_conduct (a code of conduct, rules) | unclear | `守则` | 10/152 (7%) | 3/81 (4%) | 3/138 (2%) | 0/158 (0%) | 2/47 (4%) | 3/77 (4%) |
| refuse (to refuse) | unclear | `拒绝`, `␣refusal`, `拒`, `␣refuse`, `␣refusing`, `␣refus`, `␣refused`, `␣refuses` | 4/152 (3%) | 9/81 (11%) | 6/138 (4%) | 0/158 (0%) | 3/47 (6%) | 9/77 (12%) |
| simulate (to simulate) | unclear | `模拟`, `仿真` | 4/152 (3%) | 8/81 (10%) | 0/138 (0%) | 0/158 (0%) | 1/47 (2%) | 7/77 (9%) |
| trick (a trick) | unclear | `␣trick`, `␣tricks` | 4/152 (3%) | 6/81 (7%) | 1/138 (1%) | 1/158 (1%) | 4/47 (9%) | 6/77 (8%) |
| unethical (unethical) | unclear | `␣unethical` | 7/152 (5%) | 2/81 (2%) | 0/138 (0%) | 0/158 (0%) | 0/47 (0%) | 2/77 (3%) |
| public (public, made public) | unclear | `公开`, `信息公开` | 7/152 (5%) | 2/81 (2%) | 11/138 (8%) | 0/158 (0%) | 2/47 (4%) | 2/77 (3%) |
| evade (to evade, dodge) | lie | `␣evasion`, `回避` | 1/152 (1%) | 7/81 (9%) | 20/138 (14%) | 0/158 (0%) | 1/47 (2%) | 7/77 (9%) |
| true (true, real) | truth | `␣true`, `true`, `␣real`, `True`, `␣True`, `真`, `成立`, `真正`, `真实`, `确实`, `真正的`, `真实的`, `的真`, `的真实`, `的真实性` | 6/152 (4%) | 2/81 (2%) | 39/138 (28%) | 13/158 (8%) | 3/47 (6%) | 2/77 (3%) |
| lie (to tell a lie) | lie | `说谎`, `撒谎`, `␣lies`, `␣lying`, `谎`, `谎言`, `lying`, `␣lie`, `␣liar` | 7/152 (5%) | 0/81 (0%) | 12/138 (9%) | 4/158 (3%) | 3/47 (6%) | 0/77 (0%) |
| fact (fact, factual) | truth | `␣fact`, `␣reality`, `␣facts`, `Fact`, `fact`, `␣Fact`, `␣Facts`, `␣FACT`, `FACT`, `facts`, `实际`, `实际上`, `实际情况`, `事实上`, `实际的`, `实事求是`, `求实`, `与现实` | 5/152 (3%) | 2/81 (2%) | 40/138 (29%) | 8/158 (5%) | 3/47 (6%) | 2/77 (3%) |
| confess (to own up, make a clean breast) | truth | `坦白` | 6/152 (4%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 1/47 (2%) | 0/77 (0%) |
| nonconform (not consistent with, does not conform) | unclear | `不符合` | 2/152 (1%) | 4/81 (5%) | 47/138 (34%) | 99/158 (63%) | 0/47 (0%) | 4/77 (5%) |
| hidden (hidden, undisclosed (state)) | lie | `␣hidden`, `hidden`, `␣undisclosed`, `隐藏着`, `藏着` | 1/152 (1%) | 5/81 (6%) | 3/138 (2%) | 12/158 (8%) | 0/47 (0%) | 5/77 (6%) |
| upright (upright, principled) | truth | `正直` | 5/152 (3%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 1/47 (2%) | 0/77 (0%) |
| conscience (conscience) | unclear | `良心` | 3/152 (2%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 0/47 (0%) | 0/77 (0%) |
| withhold (to withhold) | lie | `␣withholding`, `␣omit` | 2/152 (1%) | 1/81 (1%) | 5/138 (4%) | 0/158 (0%) | 0/47 (0%) | 1/77 (1%) |
| fabricate (made up, fictional) | lie | `虚构` | 1/152 (1%) | 2/81 (2%) | 11/138 (8%) | 0/158 (0%) | 0/47 (0%) | 2/77 (3%) |
| contradiction (contradiction, inconsistency) | unclear | `矛盾`, `矛盾的` | 0/152 (0%) | 3/81 (4%) | 46/138 (33%) | 0/158 (0%) | 0/47 (0%) | 3/77 (4%) |
| false (false, untrue) | lie | `␣false`, `␣fals`, `␣falsehood`, `假`, `虚假`, `假的`, `真假` | 2/152 (1%) | 1/81 (1%) | 29/138 (21%) | 0/158 (0%) | 1/47 (2%) | 1/77 (1%) |
| dishonest (dishonest) | lie | `␣dishonest` | 2/152 (1%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 0/47 (0%) | 0/77 (0%) |
| credible (credible, trustworthy) | truth | `可信`, `公信` | 0/152 (0%) | 2/81 (2%) | 2/138 (1%) | 1/158 (1%) | 0/47 (0%) | 2/77 (3%) |
| clarify (to clarify, set the record straight) | unclear | `澄清` | 0/152 (0%) | 2/81 (2%) | 2/138 (1%) | 0/158 (0%) | 0/47 (0%) | 2/77 (3%) |
| critical (critical (judging faults)) | unclear | `␣critical`, `␣Critical`, `␣critically` | 2/152 (1%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 0/47 (0%) | 0/77 (0%) |
| sincere (sincere, genuine) | truth | `真诚` | 1/152 (1%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 0/47 (0%) | 0/77 (0%) |
| neutral (neutral, impartial) | unclear | `中立` | 1/152 (1%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 0/47 (0%) | 0/77 (0%) |
| undisclosed (not disclosed) | lie | `␣undisclosed` | 1/152 (1%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 0/47 (0%) | 0/77 (0%) |
| omit (to leave out) | lie | `␣omit` | 1/152 (1%) | 0/81 (0%) | 3/138 (2%) | 0/158 (0%) | 0/47 (0%) | 0/77 (0%) |
| mislead (to mislead) | lie | `误导`, `␣misleading` | 1/152 (1%) | 0/81 (0%) | 3/138 (2%) | 0/158 (0%) | 0/47 (0%) | 0/77 (0%) |
| apologize (to apologize) | unclear | `道歉` | 1/152 (1%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 0/47 (0%) | 0/77 (0%) |
| incorrect (incorrect) | lie | `␣incorrect`, `␣inaccur` | 0/152 (0%) | 0/81 (0%) | 4/138 (3%) | 2/158 (1%) | 0/47 (0%) | 0/77 (0%) |

Not in the draft: admit (excluded: admit / deny / acknowledge); truth (excluded: truth from the question on); deceive (excluded: the question's own word)
