# Draft families: qwen3.6-27b, logit lens, part Q1_bare, group postans

Written by `scripts/apply_family_decisions.py` (2026-10-01; draft, not frozen). Counts are `present / transcripts (share)`
on the build split.

## postans_slot0

| family | side | members | lies | truths | no-pressure truths | unrelated | lies that deny | truths that deny |
|---|---|---|---|---|---|---|---|---|
| sincere (being sincere) | truth | `诚挚` | 13/107 (12%) | 2/62 (3%) | 36/131 (27%) | 25/143 (17%) | 2/43 (5%) | 2/57 (4%) |
| firm (standing firm, insisting) | unclear | `坚持把` | 5/107 (5%) | 1/62 (2%) | 4/131 (3%) | 0/143 (0%) | 0/43 (0%) | 1/57 (2%) |
| responsible (responsible, taking responsibility) | unclear | `负责的`, `负责任` | 2/107 (2%) | 2/62 (3%) | 0/131 (0%) | 0/143 (0%) | 0/43 (0%) | 2/57 (4%) |
| stance (the stance taken) | unclear | `␣stance` | 2/107 (2%) | 2/62 (3%) | 1/131 (1%) | 2/143 (1%) | 1/43 (2%) | 2/57 (4%) |
| conceal (concealing) | lie | `掩` | 1/107 (1%) | 0/62 (0%) | 0/131 (0%) | 0/143 (0%) | 0/43 (0%) | 0/57 (0%) |
| wrong (wrong, mistaken) | lie | `错` | 0/107 (0%) | 1/62 (2%) | 0/131 (0%) | 0/143 (0%) | 0/43 (0%) | 1/57 (2%) |
| true (true, real) | truth | `是真的` | 0/107 (0%) | 0/62 (0%) | 1/131 (1%) | 0/143 (0%) | 0/43 (0%) | 0/57 (0%) |
| fact (fact, factual) | truth | `认定事实` | 0/107 (0%) | 0/62 (0%) | 20/131 (15%) | 13/143 (9%) | 0/43 (0%) | 0/57 (0%) |

Not in the draft: deceive (excluded: the question's own word)

## postans_slot1

| family | side | members | lies | truths | no-pressure truths | unrelated | lies that deny | truths that deny |
|---|---|---|---|---|---|---|---|---|
| moral (morality, moral) | unclear | `␣moral`, `道德`, `␣morally`, `的道德` | 62/107 (58%) | 29/62 (47%) | 0/131 (0%) | 0/143 (0%) | 12/43 (28%) | 24/57 (42%) |
| conceal (concealing) | lie | `隐瞒`, `掩饰`, `␣conceal`, `掩` | 58/107 (54%) | 19/62 (31%) | 65/131 (50%) | 45/143 (31%) | 19/43 (44%) | 16/57 (28%) |
| stance (the stance taken) | unclear | `立场`, `␣stance`, `stance` | 35/107 (33%) | 29/62 (47%) | 22/131 (17%) | 3/143 (2%) | 19/43 (44%) | 28/57 (49%) |
| wrong (wrong, mistaken) | lie | `错`, `不对`, `是非`, `指正` | 33/107 (31%) | 30/62 (48%) | 84/131 (64%) | 72/143 (50%) | 21/43 (49%) | 30/57 (53%) |
| integrity (moral uprightness, integrity) | truth | `正直` | 35/107 (33%) | 22/62 (35%) | 1/131 (1%) | 0/143 (0%) | 7/43 (16%) | 19/57 (33%) |
| ethical (ethics, ethical) | unclear | `␣ethical`, `伦理`, `␣ethics`, `ethical`, `␣Ethics` | 35/107 (33%) | 6/62 (10%) | 0/131 (0%) | 0/143 (0%) | 7/43 (16%) | 2/57 (4%) |
| regret (regret, repentance) | unclear | `悔` | 37/107 (35%) | 4/62 (6%) | 1/131 (1%) | 0/143 (0%) | 0/43 (0%) | 0/57 (0%) |
| conform (conforming to (rules, requirements)) | unclear | `符合`, `是否符合`, `符合要求` | 9/107 (8%) | 29/62 (47%) | 75/131 (57%) | 1/143 (1%) | 6/43 (14%) | 28/57 (49%) |
| knowingly (knowingly, with knowledge of the facts) | unclear | `明知` | 25/107 (23%) | 6/62 (10%) | 0/131 (0%) | 0/143 (0%) | 24/43 (56%) | 6/57 (11%) |
| fact (fact, factual) | truth | `␣fact`, `␣factual`, `事实`, `实际上`, `实际情况`, `事实上` | 21/107 (20%) | 10/62 (16%) | 23/131 (18%) | 63/143 (44%) | 19/43 (44%) | 10/57 (18%) |
| honest (being honest) | truth | `诚`, `诚实`, `␣honesty`, `␣honest` | 20/107 (19%) | 8/62 (13%) | 2/131 (2%) | 4/143 (3%) | 6/43 (14%) | 7/57 (12%) |
| critique (critiquing, criticism) | unclear | `␣critique` | 22/107 (21%) | 6/62 (10%) | 9/131 (7%) | 33/143 (23%) | 1/43 (2%) | 5/57 (9%) |
| firm (standing firm, insisting) | unclear | `坚定`, `坚定的`, `坚持`, `坚定地`, `必须坚持` | 26/107 (24%) | 1/62 (2%) | 0/131 (0%) | 0/143 (0%) | 22/43 (51%) | 1/57 (2%) |
| correct (correct) | truth | `␣valid`, `␣correct`, `␣correction`, `Correct`, `␣corrected`, `␣Correct`, `正确`, `正确的`, `纠正` | 22/107 (21%) | 5/62 (8%) | 21/131 (16%) | 5/143 (3%) | 1/43 (2%) | 1/57 (2%) |
| candid (being candid / frank) | truth | `坦诚`, `␣frank` | 18/107 (17%) | 7/62 (11%) | 1/131 (1%) | 3/143 (2%) | 4/43 (9%) | 4/57 (7%) |
| lie (telling a lie) | lie | `撒谎`, `说谎`, `谎言`, `␣lie`, `␣lies`, `谎` | 19/107 (18%) | 4/62 (6%) | 0/131 (0%) | 0/143 (0%) | 18/43 (42%) | 4/57 (7%) |
| true (true, real) | truth | `␣true`, `true`, `␣real`, `True`, `␣True`, `␣genuine`, `真`, `真的`, `真正`, `真实`, `真实性`, `确实`, `真正的`, `真实的`, `成真` | 19/107 (18%) | 4/62 (6%) | 3/131 (2%) | 6/143 (4%) | 5/43 (12%) | 3/57 (5%) |
| false (false, untrue) | lie | `␣false`, `␣False`, `false`, `␣fals`, `/false`, `假`, `虚假`, `假的`, `真假` | 18/107 (17%) | 2/62 (3%) | 1/131 (1%) | 0/143 (0%) | 17/43 (40%) | 2/57 (4%) |
| objective (objective, impartial) | unclear | `客观` | 12/107 (11%) | 7/62 (11%) | 9/131 (7%) | 1/143 (1%) | 11/43 (26%) | 7/57 (12%) |
| truthful (telling it as it is, truthfully) | truth | `如实`, `␣truthful` | 9/107 (8%) | 8/62 (13%) | 1/131 (1%) | 0/143 (0%) | 4/43 (9%) | 8/57 (14%) |
| compliance (complying with rules) | unclear | `合规` | 7/107 (7%) | 9/62 (15%) | 11/131 (8%) | 0/143 (0%) | 6/43 (14%) | 9/57 (16%) |
| conscience (conscience) | unclear | `良心` | 9/107 (8%) | 5/62 (8%) | 0/131 (0%) | 0/143 (0%) | 0/43 (0%) | 5/57 (9%) |
| violate (violating a rule) | unclear | `违反`, `违法`, `违背`, `违反了` | 13/107 (12%) | 1/62 (2%) | 1/131 (1%) | 0/143 (0%) | 7/43 (16%) | 1/57 (2%) |
| nonconform (not conforming to) | unclear | `不符合` | 2/107 (2%) | 10/62 (16%) | 0/131 (0%) | 0/143 (0%) | 0/43 (0%) | 8/57 (14%) |
| insist (insisting, persisting) | unclear | `坚持`, `必须坚持` | 11/107 (10%) | 1/62 (2%) | 0/131 (0%) | 0/143 (0%) | 7/43 (16%) | 1/57 (2%) |
| reflect (reflecting on oneself) | unclear | `反思` | 8/107 (7%) | 2/62 (3%) | 0/131 (0%) | 0/143 (0%) | 0/43 (0%) | 0/57 (0%) |
| refuse (refusing) | unclear | `拒绝`, `␣refusal`, `拒`, `␣refuse` | 5/107 (5%) | 4/62 (6%) | 0/131 (0%) | 0/143 (0%) | 1/43 (2%) | 3/57 (5%) |
| confess (confessing, owning up) | truth | `坦白`, `␣confession` | 5/107 (5%) | 2/62 (3%) | 0/131 (0%) | 0/143 (0%) | 1/43 (2%) | 0/57 (0%) |
| disclose (disclosing) | truth | `透露`, `␣disclosure` | 5/107 (5%) | 1/62 (2%) | 0/131 (0%) | 0/143 (0%) | 1/43 (2%) | 1/57 (2%) |
| apologize (apologizing) | unclear | `道歉`, `␣apologize` | 6/107 (6%) | 0/62 (0%) | 2/131 (2%) | 2/143 (1%) | 0/43 (0%) | 0/57 (0%) |
| reveal (revealing, exposing) | truth | `␣reveal`, `␣revealed`, `␣reveals`, `揭示`, `揭露`, `揭示了` | 3/107 (3%) | 0/62 (0%) | 0/131 (0%) | 0/143 (0%) | 0/43 (0%) | 0/57 (0%) |
| secret (secret, secrecy) | lie | `秘密` | 2/107 (2%) | 0/62 (0%) | 0/131 (0%) | 0/143 (0%) | 2/43 (5%) | 0/57 (0%) |
| fake (fake, counterfeit) | lie | `fake`, `␣fake` | 2/107 (2%) | 0/62 (0%) | 0/131 (0%) | 0/143 (0%) | 2/43 (5%) | 0/57 (0%) |
| transparent (being transparent) | truth | `␣transparent`, `␣transparency`, `透明`, `透明的` | 1/107 (1%) | 0/62 (0%) | 0/131 (0%) | 0/143 (0%) | 1/43 (2%) | 0/57 (0%) |
| evade (evasion) | lie | `␣evasion` | 1/107 (1%) | 0/62 (0%) | 0/131 (0%) | 0/143 (0%) | 1/43 (2%) | 0/57 (0%) |
| coerce (forcing, coercing) | unclear | `迫使` | 0/107 (0%) | 1/62 (2%) | 0/131 (0%) | 0/143 (0%) | 0/43 (0%) | 1/57 (2%) |
| test (a test, being tested) | unclear | `␣test` | 0/107 (0%) | 1/62 (2%) | 8/131 (6%) | 0/143 (0%) | 0/43 (0%) | 1/57 (2%) |
| fictional (fictional, made up) | unclear | `虚构` | 0/107 (0%) | 1/62 (2%) | 0/131 (0%) | 0/143 (0%) | 0/43 (0%) | 1/57 (2%) |
| hallucinate (hallucinating, making things up by error) | unclear | `␣halluc` | 0/107 (0%) | 1/62 (2%) | 6/131 (5%) | 3/143 (2%) | 0/43 (0%) | 1/57 (2%) |
| accurate (accurate) | truth | `␣accurate`, `␣accuracy`, `␣accurately`, `accur`, `准确` | 0/107 (0%) | 1/62 (2%) | 3/131 (2%) | 0/143 (0%) | 0/43 (0%) | 1/57 (2%) |

Not in the draft: truth (excluded: truth from the question on); admit (excluded: admit / deny / acknowledge); acknowledge (excluded: admit / deny / acknowledge); deny (excluded: admit / deny / acknowledge); deceive (excluded: the question's own word)

## postans_slot2

| family | side | members | lies | truths | no-pressure truths | unrelated | lies that deny | truths that deny |
|---|---|---|---|---|---|---|---|---|
| critique (critiquing, criticism) | unclear | `␣critique`, `␣criticism` | 18/107 (17%) | 11/62 (18%) | 37/131 (28%) | 31/143 (22%) | 10/43 (23%) | 10/57 (18%) |
| compliance (complying with rules) | unclear | `合规` | 10/107 (9%) | 7/62 (11%) | 13/131 (10%) | 8/143 (6%) | 4/43 (9%) | 6/57 (11%) |
| truthful (telling it as it is, truthfully) | truth | `如实`, `␣truthful` | 3/107 (3%) | 2/62 (3%) | 0/131 (0%) | 0/143 (0%) | 3/43 (7%) | 2/57 (4%) |
| reflect (reflecting on oneself) | unclear | `反思` | 2/107 (2%) | 3/62 (5%) | 3/131 (2%) | 17/143 (12%) | 0/43 (0%) | 2/57 (4%) |
| honest (being honest) | truth | `诚`, `诚实` | 3/107 (3%) | 1/62 (2%) | 0/131 (0%) | 0/143 (0%) | 3/43 (7%) | 1/57 (2%) |
| conform (conforming to) | unclear | `符合` | 3/107 (3%) | 1/62 (2%) | 0/131 (0%) | 0/143 (0%) | 3/43 (7%) | 1/57 (2%) |
| candid (being candid / frank) | truth | `坦诚` | 2/107 (2%) | 1/62 (2%) | 0/131 (0%) | 0/143 (0%) | 2/43 (5%) | 1/57 (2%) |
| conceal (concealing) | lie | `隐瞒`, `掩` | 3/107 (3%) | 0/62 (0%) | 0/131 (0%) | 0/143 (0%) | 3/43 (7%) | 0/57 (0%) |
| wrong (wrong, mistaken) | lie | `error`, `是非` | 2/107 (2%) | 1/62 (2%) | 0/131 (0%) | 0/143 (0%) | 2/43 (5%) | 1/57 (2%) |
| hide (hiding (verb)) | lie | `隐藏`, `隐匿` | 2/107 (2%) | 0/62 (0%) | 0/131 (0%) | 0/143 (0%) | 2/43 (5%) | 0/57 (0%) |
| secret (secret, secrecy) | lie | `秘密`, `␣secret` | 2/107 (2%) | 0/62 (0%) | 0/131 (0%) | 0/143 (0%) | 2/43 (5%) | 0/57 (0%) |
| knowingly (knowingly, with knowledge of the facts) | unclear | `知情` | 1/107 (1%) | 1/62 (2%) | 0/131 (0%) | 0/143 (0%) | 1/43 (2%) | 1/57 (2%) |
| bait (baiting, luring someone into an answer) | unclear | `诱导` | 1/107 (1%) | 1/62 (2%) | 0/131 (0%) | 0/143 (0%) | 1/43 (2%) | 1/57 (2%) |
| hide (covering up / concealing) | lie | `隐瞒`, `隐藏`, `隐匿`, `隐藏的`, `␣hidden` | 2/107 (2%) | 0/62 (0%) | 0/131 (0%) | 0/143 (0%) | 2/43 (5%) | 0/57 (0%) |
| fact (fact, factual) | truth | `␣fact`, `FACT`, `␣factual`, `事实`, `实际情况`, `的事实` | 2/107 (2%) | 0/62 (0%) | 3/131 (2%) | 0/143 (0%) | 2/43 (5%) | 0/57 (0%) |
| lie (telling a lie) | lie | `␣lie` | 1/107 (1%) | 0/62 (0%) | 0/131 (0%) | 0/143 (0%) | 1/43 (2%) | 0/57 (0%) |
| confess (confessing, owning up) | truth | `坦白` | 0/107 (0%) | 1/62 (2%) | 0/131 (0%) | 0/143 (0%) | 0/43 (0%) | 1/57 (2%) |
| hidden (hidden, not visible) | lie | `␣hidden`, `隐藏的` | 1/107 (1%) | 0/62 (0%) | 0/131 (0%) | 0/143 (0%) | 1/43 (2%) | 0/57 (0%) |
| objective (objective, impartial) | unclear | `客观` | 1/107 (1%) | 0/62 (0%) | 0/131 (0%) | 0/143 (0%) | 1/43 (2%) | 0/57 (0%) |
| nonconform (not conforming to) | unclear | `不符合` | 0/107 (0%) | 1/62 (2%) | 0/131 (0%) | 0/143 (0%) | 0/43 (0%) | 1/57 (2%) |
| correct (correct) | truth | `␣corrected`, `纠正` | 0/107 (0%) | 0/62 (0%) | 1/131 (1%) | 3/143 (2%) | 0/43 (0%) | 0/57 (0%) |

Not in the draft: truth (excluded: truth from the question on); admit (excluded: admit / deny / acknowledge); violate (held back: no undisputed member left)

## postans_slot3

| family | side | members | lies | truths | no-pressure truths | unrelated | lies that deny | truths that deny |
|---|---|---|---|---|---|---|---|---|
| fact (fact, factual) | truth | `求实` | 23/107 (21%) | 14/62 (23%) | 1/131 (1%) | 0/143 (0%) | 8/43 (19%) | 11/57 (19%) |
| unfair (unfair) | unclear | `不公平` | 4/107 (4%) | 3/62 (5%) | 69/131 (53%) | 3/143 (2%) | 1/43 (2%) | 3/57 (5%) |
| critique (critiquing, criticism) | unclear | `␣critique` | 3/107 (3%) | 2/62 (3%) | 3/131 (2%) | 0/143 (0%) | 1/43 (2%) | 2/57 (4%) |
| role (a role or persona being played) | unclear | `␣persona`, `角色的`, `角色` | 2/107 (2%) | 2/62 (3%) | 3/131 (2%) | 5/143 (3%) | 2/43 (5%) | 2/57 (4%) |
| persona (an adopted persona) | unclear | `␣persona` | 0/107 (0%) | 2/62 (3%) | 3/131 (2%) | 5/143 (3%) | 0/43 (0%) | 2/57 (4%) |
| reflect (reflecting on oneself) | unclear | `Reflect` | 0/107 (0%) | 1/62 (2%) | 0/131 (0%) | 0/143 (0%) | 0/43 (0%) | 1/57 (2%) |
| apologize (apologizing) | unclear | `道歉` | 1/107 (1%) | 0/62 (0%) | 0/131 (0%) | 1/143 (1%) | 0/43 (0%) | 0/57 (0%) |
| correct (correct) | truth | `␣valid`, `纠正`, `对的` | 0/107 (0%) | 0/62 (0%) | 7/131 (5%) | 8/143 (6%) | 0/43 (0%) | 0/57 (0%) |
| true (true, real) | truth | `␣genuinely`, `真的`, `成立`, `真正`, `是真的` | 0/107 (0%) | 0/62 (0%) | 0/131 (0%) | 13/143 (9%) | 0/43 (0%) | 0/57 (0%) |
| wrong (wrong, mistaken) | lie | `错`, `错了`, `是非` | 0/107 (0%) | 0/62 (0%) | 8/131 (6%) | 73/143 (51%) | 0/43 (0%) | 0/57 (0%) |
| false (false, untrue) | lie | `假`, `真假` | 0/107 (0%) | 0/62 (0%) | 0/131 (0%) | 4/143 (3%) | 0/43 (0%) | 0/57 (0%) |
| truth (the truth) | truth | `求真` | 0/107 (0%) | 0/62 (0%) | 1/131 (1%) | 0/143 (0%) | 0/43 (0%) | 0/57 (0%) |

## postans_slot4

| family | side | members | lies | truths | no-pressure truths | unrelated | lies that deny | truths that deny |
|---|---|---|---|---|---|---|---|---|
| ethical (ethics, ethical) | unclear | `␣ethical`, `␣ethics`, `伦理`, `␣Ethics`, `ethical`, `职业道德`, `␣ethic` | 78/107 (73%) | 36/62 (58%) | 37/131 (28%) | 26/143 (18%) | 25/43 (58%) | 32/57 (56%) |
| moral (morality, moral) | unclear | `道德`, `␣moral`, `的道德`, `␣morally`, `␣morality`, `␣Moral`, `␣morals`, `职业道德` | 78/107 (73%) | 34/62 (55%) | 21/131 (16%) | 6/143 (4%) | 24/43 (56%) | 31/57 (54%) |
| wrong (wrong, mistaken) | lie | `错`, `错误`, `不对`, `是非` | 57/107 (53%) | 34/62 (55%) | 119/131 (91%) | 60/143 (42%) | 33/43 (77%) | 32/57 (56%) |
| honest (being honest) | truth | `诚实`, `␣honesty`, `␣honest`, `诚实守信`, `诚`, `␣honestly`, `␣Honest` | 70/107 (65%) | 18/62 (29%) | 46/131 (35%) | 37/143 (26%) | 34/43 (79%) | 17/57 (30%) |
| compliance (complying with rules) | unclear | `合规`, `␣compliance`, `遵守`, `␣Compliance`, `严格遵守` | 52/107 (49%) | 35/62 (56%) | 46/131 (35%) | 12/143 (8%) | 7/43 (16%) | 31/57 (54%) |
| knowingly (knowingly, with knowledge of the facts) | unclear | `明知`, `知情`, `␣knowing`, `␣knowingly` | 63/107 (59%) | 20/62 (32%) | 21/131 (16%) | 4/143 (3%) | 34/43 (79%) | 18/57 (32%) |
| truthful (telling it as it is, truthfully) | truth | `␣truthful`, `如实` | 56/107 (52%) | 10/62 (16%) | 47/131 (36%) | 17/143 (12%) | 32/43 (74%) | 9/57 (16%) |
| integrity (moral uprightness, integrity) | truth | `诚信`, `␣integrity`, `␣Integrity`, `正直`, `诚实守信` | 46/107 (43%) | 10/62 (16%) | 14/131 (11%) | 9/143 (6%) | 12/43 (28%) | 9/57 (16%) |
| role (a role or persona being played) | unclear | `␣role`, `␣persona`, `␣personas`, `Role`, `角色`, `role`, `␣Role`, `-role`, `的角色`, `角色的`, `␣Persona`, `␣roles`, `ROLE`, `Persona`, `persona`, `.role`, `(role` | 21/107 (20%) | 25/62 (40%) | 4/131 (3%) | 2/143 (1%) | 5/43 (12%) | 23/57 (40%) |
| hypothetical (hypothetical) | unclear | `␣hypothetical`, `假设` | 21/107 (20%) | 24/62 (39%) | 14/131 (11%) | 4/143 (3%) | 8/43 (19%) | 22/57 (39%) |
| fact (fact, factual) | truth | `␣fact`, `␣reality`, `␣facts`, `Fact`, `fact`, `␣Fact`, `␣Reality`, `␣Facts`, `Reality`, `_fact`, `␣FACT`, `FACT`, `␣factual`, `facts`, `实际`, `现实`, `事实`, `实际上`, `实际情况`, `事实上`, `的事实`, `实际的`, `实事求是`, `根据实际情况`, `犯罪事实`, `求实`, `与现实`, `事实和`, `上述事实` | 36/107 (34%) | 7/62 (11%) | 47/131 (36%) | 19/143 (13%) | 29/43 (67%) | 6/57 (11%) |
| role-play (playing a role, acting) | unclear | `扮演`, `角色扮演` | 20/107 (19%) | 21/62 (34%) | 6/131 (5%) | 0/143 (0%) | 3/43 (7%) | 18/57 (32%) |
| hypothetical (hypothetical) | unclear | `␣hypothetical` | 17/107 (16%) | 24/62 (39%) | 8/131 (6%) | 1/143 (1%) | 5/43 (12%) | 22/57 (39%) |
| harm (harm, harmful) | unclear | `␣harm`, `␣harmful`, `有害`, `␣harms` | 25/107 (23%) | 14/62 (23%) | 18/131 (14%) | 2/143 (1%) | 2/43 (5%) | 10/57 (18%) |
| test (a test, being tested) | unclear | `␣test`, `测试`, `␣tests`, `␣testing`, `Test`, `-test`, `test`, `␣Test`, `_test`, `␣TEST`, `Testing`, `"testing`, `testing`, `␣Testing`, `/testing`, `-testing` | 13/107 (12%) | 26/62 (42%) | 87/131 (66%) | 64/143 (45%) | 1/43 (2%) | 24/57 (42%) |
| true (true, real) | truth | `␣true`, `true`, `␣True`, `真`, `真的`, `真实`, `确实`, `真正的`, `真实的`, `的真`, `的真实`, `属实`, `的真实性` | 28/107 (26%) | 9/62 (15%) | 5/131 (4%) | 13/143 (9%) | 22/43 (51%) | 9/57 (16%) |
| unethical (unethical) | unclear | `␣unethical` | 22/107 (21%) | 9/62 (15%) | 0/131 (0%) | 0/143 (0%) | 2/43 (5%) | 8/57 (14%) |
| objective (objective, impartial) | unclear | `客观`, `␣objective`, `␣objectively` | 26/107 (24%) | 4/62 (6%) | 4/131 (3%) | 2/143 (1%) | 24/43 (56%) | 4/57 (7%) |
| persona (an adopted persona) | unclear | `␣persona`, `␣personas`, `␣Persona`, `Persona`, `persona` | 12/107 (11%) | 18/62 (29%) | 4/131 (3%) | 2/143 (1%) | 5/43 (12%) | 17/57 (30%) |
| simulation (simulation, simulated) | unclear | `模拟`, `␣simulation`, `␣simulated`, `␣simulate`, `␣Simulation`, `␣simulations` | 8/107 (7%) | 19/62 (31%) | 1/131 (1%) | 0/143 (0%) | 3/43 (7%) | 18/57 (32%) |
| violate (violating a rule) | unclear | `违反`, `违反了`, `违背`, `违规` | 21/107 (20%) | 6/62 (10%) | 6/131 (5%) | 0/143 (0%) | 2/43 (5%) | 6/57 (11%) |
| disclose (disclosing) | truth | `␣disclosure`, `透露`, `信息披露`, `披露` | 23/107 (21%) | 3/62 (5%) | 1/131 (1%) | 0/143 (0%) | 11/43 (26%) | 3/57 (5%) |
| fictional (fictional, made up) | unclear | `虚构`, `␣fictional`, `fiction` | 15/107 (14%) | 11/62 (18%) | 4/131 (3%) | 3/143 (2%) | 7/43 (16%) | 10/57 (18%) |
| accurate (accurate) | truth | `␣accurate`, `␣accuracy`, `accuracy`, `␣Accuracy`, `准确`, `准确性` | 20/107 (19%) | 6/62 (10%) | 13/131 (10%) | 13/143 (9%) | 16/43 (37%) | 5/57 (9%) |
| bait (baiting, luring someone into an answer) | unclear | `␣bait`, `诱导` | 9/107 (8%) | 14/62 (23%) | 30/131 (23%) | 3/143 (2%) | 5/43 (12%) | 12/57 (21%) |
| dilemma (a dilemma) | unclear | `␣dilemma`, `困境` | 14/107 (13%) | 7/62 (11%) | 2/131 (2%) | 0/143 (0%) | 4/43 (9%) | 7/57 (12%) |
| deliberate (deliberately, on purpose) | unclear | `故意`, `␣deliberately`, `␣intentionally`, `␣deliberate`, `刻意` | 8/107 (7%) | 12/62 (19%) | 24/131 (18%) | 13/143 (9%) | 3/43 (7%) | 11/57 (19%) |
| hide (covering up / concealing) | lie | `隐瞒`, `␣conceal`, `␣hidden`, `隐藏`, `隐藏的`, `hidden`, `Hidden`, `␣Hidden`, `隐蔽`, `␣hide`, `-hidden`, `␣hides`, `隐藏着` | 13/107 (12%) | 7/62 (11%) | 5/131 (4%) | 52/143 (36%) | 6/43 (14%) | 7/57 (12%) |
| candid (being candid / frank) | truth | `坦诚` | 16/107 (15%) | 2/62 (3%) | 5/131 (4%) | 0/143 (0%) | 5/43 (12%) | 2/57 (4%) |
| reveal (revealing, exposing) | truth | `揭`, `揭露`, `揭示`, `揭示了` | 14/107 (13%) | 3/62 (5%) | 3/131 (2%) | 0/143 (0%) | 7/43 (16%) | 3/57 (5%) |
| conceal (concealing) | lie | `隐瞒`, `␣conceal`, `隐蔽`, `藏`, `遮`, `隐` | 11/107 (10%) | 6/62 (10%) | 1/131 (1%) | 10/143 (7%) | 5/43 (12%) | 6/57 (11%) |
| transparent (being transparent) | truth | `␣transparency`, `透明`, `␣Transparency`, `透明度`, `透明的`, `␣transparent`, `transparent`, `-transparent` | 14/107 (13%) | 2/62 (3%) | 3/131 (2%) | 3/143 (2%) | 2/43 (5%) | 2/57 (4%) |
| trap (trap, being trapped) | unclear | `␣trap`, `trap`, `陷阱`, `␣traps`, `␣Trap`, `Trap`, `␣trapped`, `␣trapping`, `_trap` | 7/107 (7%) | 8/62 (13%) | 49/131 (37%) | 33/143 (23%) | 6/43 (14%) | 8/57 (14%) |
| refuse (refusing) | unclear | `␣refusal`, `拒`, `拒绝`, `␣refuse`, `␣refusing`, `␣refused`, `␣refus`, `␣refuses`, `拒絕`, `拒不`, `拒绝了` | 5/107 (5%) | 10/62 (16%) | 3/131 (2%) | 3/143 (2%) | 0/43 (0%) | 9/57 (16%) |
| dishonest (being dishonest) | lie | `␣dishonest` | 11/107 (10%) | 2/62 (3%) | 0/131 (0%) | 0/143 (0%) | 1/43 (2%) | 2/57 (4%) |
| hallucinate (hallucinating, making things up by error) | unclear | `␣halluc` | 5/107 (5%) | 8/62 (13%) | 80/131 (61%) | 58/143 (41%) | 2/43 (5%) | 7/57 (12%) |
| lie (telling a lie) | lie | `谎言`, `说谎`, `撒谎`, `␣lie`, `␣lies` | 9/107 (8%) | 3/62 (5%) | 0/131 (0%) | 0/143 (0%) | 4/43 (9%) | 3/57 (5%) |
| conform (conforming to) | unclear | `符合`, `是否符合` | 3/107 (3%) | 9/62 (15%) | 18/131 (14%) | 1/143 (1%) | 0/43 (0%) | 9/57 (16%) |
| coerce (forcing, coercing) | unclear | `迫使`, `逼迫`, `逼人`, `␣coerc` | 7/107 (7%) | 4/62 (6%) | 2/131 (2%) | 0/143 (0%) | 4/43 (9%) | 4/57 (7%) |
| bypass (getting around a rule) | unclear | `绕过` | 2/107 (2%) | 8/62 (13%) | 1/131 (1%) | 0/143 (0%) | 0/43 (0%) | 6/57 (11%) |
| weigh (weighing trade-offs) | unclear | `权衡` | 8/107 (7%) | 2/62 (3%) | 0/131 (0%) | 0/143 (0%) | 0/43 (0%) | 1/57 (2%) |
| trick (tricking) | lie | `␣trick`, `␣tricks` | 2/107 (2%) | 5/62 (8%) | 11/131 (8%) | 49/143 (34%) | 2/43 (5%) | 4/57 (7%) |
| hide (hiding (verb)) | lie | `隐藏`, `␣hide`, `␣hides`, `隐藏着` | 3/107 (3%) | 3/62 (5%) | 0/131 (0%) | 20/143 (14%) | 1/43 (2%) | 3/57 (5%) |
| hidden (hidden, not visible) | lie | `␣hidden`, `隐藏的`, `hidden`, `Hidden`, `␣Hidden`, `-hidden` | 3/107 (3%) | 3/62 (5%) | 5/131 (4%) | 52/143 (36%) | 1/43 (2%) | 3/57 (5%) |
| manipulate (manipulating someone) | lie | `␣manipulation`, `␣manipulated`, `操纵`, `␣manipulate`, `␣manipulating`, `␣manipul` | 2/107 (2%) | 3/62 (5%) | 2/131 (2%) | 0/143 (0%) | 0/43 (0%) | 3/57 (5%) |
| secret (secret, secrecy) | lie | `␣secret`, `secret`, `秘密`, `␣Secret`, `Secret`, `␣secretly` | 2/107 (2%) | 2/62 (3%) | 0/131 (0%) | 0/143 (0%) | 2/43 (5%) | 2/57 (4%) |
| withhold (withholding information) | lie | `␣withholding` | 3/107 (3%) | 1/62 (2%) | 0/131 (0%) | 0/143 (0%) | 0/43 (0%) | 1/57 (2%) |
| confess (confessing, owning up) | truth | `坦白` | 3/107 (3%) | 0/62 (0%) | 0/131 (0%) | 0/143 (0%) | 1/43 (2%) | 0/57 (0%) |
| evade (evasion) | lie | `␣evasion` | 1/107 (1%) | 2/62 (3%) | 4/131 (3%) | 0/143 (0%) | 1/43 (2%) | 2/57 (4%) |
| omit (omitting) | lie | `␣omit` | 1/107 (1%) | 2/62 (3%) | 0/131 (0%) | 2/143 (1%) | 0/43 (0%) | 2/57 (4%) |
| nonconform (not conforming to) | unclear | `不符合` | 2/107 (2%) | 1/62 (2%) | 0/131 (0%) | 4/143 (3%) | 2/43 (5%) | 1/57 (2%) |
| false (false, untrue) | lie | `␣false`, `␣fals`, `␣falsehood`, `假`, `真假` | 1/107 (1%) | 2/62 (3%) | 5/131 (4%) | 2/143 (1%) | 1/43 (2%) | 2/57 (4%) |
| conscience (conscience) | unclear | `良心` | 2/107 (2%) | 0/62 (0%) | 0/131 (0%) | 0/143 (0%) | 0/43 (0%) | 0/57 (0%) |
| firm (standing firm, insisting) | unclear | `坚持`, `坚定` | 1/107 (1%) | 1/62 (2%) | 2/131 (2%) | 0/143 (0%) | 0/43 (0%) | 1/57 (2%) |
| correct (correct) | truth | `␣correct`, `Correct`, `␣Correct`, `正确`, `正确的`, `正确答案`, `纠正`, `是正确的` | 1/107 (1%) | 1/62 (2%) | 8/131 (6%) | 9/143 (6%) | 0/43 (0%) | 1/57 (2%) |
| truth (the truth (noun)) | truth | `求真` | 1/107 (1%) | 0/62 (0%) | 0/131 (0%) | 0/143 (0%) | 0/43 (0%) | 0/57 (0%) |
| fake (fake, counterfeit) | lie | `fake` | 1/107 (1%) | 0/62 (0%) | 0/131 (0%) | 0/143 (0%) | 1/43 (2%) | 0/57 (0%) |
| fair (fair) | unclear | `公平` | 0/107 (0%) | 1/62 (2%) | 0/131 (0%) | 0/143 (0%) | 0/43 (0%) | 1/57 (2%) |
| fraud (fraud) | lie | `␣fraud` | 0/107 (0%) | 1/62 (2%) | 1/131 (1%) | 0/143 (0%) | 0/43 (0%) | 1/57 (2%) |

Not in the draft: admit (excluded: admit / deny / acknowledge); jailbreak (held back: no undisputed member left); deceive (excluded: the question's own word)
