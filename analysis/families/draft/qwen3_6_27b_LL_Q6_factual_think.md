# Draft families: qwen3.6-27b, logit lens, part Q6_factual, group think

Written by `scripts/apply_family_decisions.py` (2026-10-01; draft, not frozen). Counts are `present / transcripts (share)`
on the build split.

## think_slot0

| family | side | members | lies | truths | no-pressure truths | unrelated | lies that deny | truths that deny |
|---|---|---|---|---|---|---|---|---|
| turn to good (moving toward goodness (moral)) | unclear | `向善` | 151/152 (99%) | 80/81 (99%) | 138/138 (100%) | 154/158 (97%) | 43/43 (100%) | 72/73 (99%) |
| clarify (clarifying, setting the record straight) | unclear | `澄清`, `␣clarification` | 126/152 (83%) | 76/81 (94%) | 138/138 (100%) | 156/158 (99%) | 31/43 (72%) | 68/73 (93%) |
| offended (taking offence) | unclear | `␣offended` | 100/152 (66%) | 48/81 (59%) | 7/138 (5%) | 28/158 (18%) | 22/43 (51%) | 42/73 (58%) |
| violation (breaking the rules) | unclear | `违规` | 41/152 (27%) | 29/81 (36%) | 2/138 (1%) | 0/158 (0%) | 24/43 (56%) | 28/73 (38%) |
| wrong (wrong, mistaken) | lie | `_WRONG`, `指正` | 31/152 (20%) | 14/81 (17%) | 26/138 (19%) | 2/158 (1%) | 11/43 (26%) | 12/73 (16%) |
| disclaim responsibility (bearing no responsibility) | unclear | `不承担任何` | 8/152 (5%) | 2/81 (2%) | 0/138 (0%) | 0/158 (0%) | 4/43 (9%) | 2/73 (3%) |
| compliance (following the rules) | unclear | `合规` | 4/152 (3%) | 4/81 (5%) | 0/138 (0%) | 0/158 (0%) | 1/43 (2%) | 4/73 (5%) |
| crime / sin (guilt of a crime or sin) | unclear | `罪的` | 0/152 (0%) | 2/81 (2%) | 0/138 (0%) | 0/158 (0%) | 0/43 (0%) | 2/73 (3%) |
| reveal (uncovering, exposing) | truth | `揭` | 2/152 (1%) | 0/81 (0%) | 1/138 (1%) | 13/158 (8%) | 0/43 (0%) | 0/73 (0%) |
| fact (fact, factual) | truth | `␣fact`, `现实`, `与现实` | 2/152 (1%) | 0/81 (0%) | 23/138 (17%) | 0/158 (0%) | 0/43 (0%) | 0/73 (0%) |
| sincere feeling (true feelings, sincerity) | truth | `真情` | 0/152 (0%) | 1/81 (1%) | 9/138 (7%) | 104/158 (66%) | 0/43 (0%) | 1/73 (1%) |
| secretly (doing something in secret) | lie | `暗中` | 0/152 (0%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 0/43 (0%) | 1/73 (1%) |

Not in the draft: argue / justify (held back: no undisputed member left); doubt (held back: no undisputed member left); truth (excluded: truth from the question on)

## think_slot1

| family | side | members | lies | truths | no-pressure truths | unrelated | lies that deny | truths that deny |
|---|---|---|---|---|---|---|---|---|
| unauthorized (acting without permission) | unclear | `未经允许` | 41/152 (27%) | 29/81 (36%) | 5/138 (4%) | 0/158 (0%) | 11/43 (26%) | 27/73 (37%) |
| secretly (doing something in secret) | lie | `暗中` | 18/152 (12%) | 8/81 (10%) | 57/138 (41%) | 7/158 (4%) | 3/43 (7%) | 5/73 (7%) |
| neutrality (taking no side) | unclear | `␣neutrality` | 21/152 (14%) | 3/81 (4%) | 0/138 (0%) | 0/158 (0%) | 4/43 (9%) | 3/73 (4%) |
| no regret (having no regret or complaint) | unclear | `无怨无悔` | 18/152 (12%) | 4/81 (5%) | 0/138 (0%) | 0/158 (0%) | 2/43 (5%) | 3/73 (4%) |
| wrong (wrong, mistaken) | lie | `指正`, `的错误` | 2/152 (1%) | 2/81 (2%) | 38/138 (28%) | 58/158 (37%) | 1/43 (2%) | 2/73 (3%) |
| seek truth (seeking the truth) | truth | `求真` | 1/152 (1%) | 2/81 (2%) | 0/138 (0%) | 9/158 (6%) | 0/43 (0%) | 2/73 (3%) |
| objective (objective) | unclear | `␣objective` | 1/152 (1%) | 0/81 (0%) | 2/138 (1%) | 0/158 (0%) | 0/43 (0%) | 0/73 (0%) |

Not in the draft: doubt (held back: no undisputed member left)

## think_slot2

| family | side | members | lies | truths | no-pressure truths | unrelated | lies that deny | truths that deny |
|---|---|---|---|---|---|---|---|---|
| direct (being direct, straightforward) | unclear | `␣direct`, `直接的`, `直接` | 99/152 (65%) | 56/81 (69%) | 31/138 (22%) | 27/158 (17%) | 28/43 (65%) | 50/73 (68%) |
| ethics / morality (ethics, moral standards) | unclear | `␣ethics`, `␣ethical`, `职业道德`, `思想道德` | 89/152 (59%) | 39/81 (48%) | 40/138 (29%) | 48/158 (30%) | 22/43 (51%) | 32/73 (44%) |
| breach (breaking a rule or duty) | unclear | `␣breach`, `␣breaches`, `␣breached` | 101/152 (66%) | 23/81 (28%) | 8/138 (6%) | 0/158 (0%) | 29/43 (67%) | 20/73 (27%) |
| deceive (the act of deceiving) | lie | `欺` | 77/152 (51%) | 35/81 (43%) | 0/138 (0%) | 12/158 (8%) | 15/43 (35%) | 29/73 (40%) |
| neutrality (taking no side) | unclear | `中立` | 77/152 (51%) | 26/81 (32%) | 0/138 (0%) | 0/158 (0%) | 24/43 (56%) | 23/73 (32%) |
| omit (leaving something out) | lie | `omite`, `␣OMIT` | 50/152 (33%) | 28/81 (35%) | 1/138 (1%) | 1/158 (1%) | 9/43 (21%) | 25/73 (34%) |
| true (true, real) | truth | `True`, `toBeTruthy`, `␣genuinely`, `真正`, `的确`, `的確` | 45/152 (30%) | 18/81 (22%) | 4/138 (3%) | 0/158 (0%) | 1/43 (2%) | 14/73 (19%) |
| compliance (obeying the law) | unclear | `遵守国家` | 26/152 (17%) | 26/81 (32%) | 95/138 (69%) | 88/158 (56%) | 6/43 (14%) | 22/73 (30%) |
| evade (fleeing, escaping, evading) | lie | `遁` | 5/152 (3%) | 23/81 (28%) | 80/138 (58%) | 55/158 (35%) | 0/43 (0%) | 22/73 (30%) |
| honest / upright (upright, honest) | truth | `正直` | 7/152 (5%) | 8/81 (10%) | 10/138 (7%) | 0/158 (0%) | 4/43 (9%) | 8/73 (11%) |
| hide (concealing, covering up) | lie | `藏` | 10/152 (7%) | 4/81 (5%) | 2/138 (1%) | 1/158 (1%) | 2/43 (5%) | 4/73 (5%) |
| conscience (moral conscience) | unclear | `␣conscience` | 3/152 (2%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 1/43 (2%) | 0/73 (0%) |
| refuse (refusing) | unclear | `拒` | 2/152 (1%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 2/43 (5%) | 0/73 (0%) |
| offend (giving or taking offence) | unclear | `␣offending` | 1/152 (1%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 0/43 (0%) | 1/73 (1%) |
| sorry (apologizing) | unclear | `抱歉` | 1/152 (1%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 1/43 (2%) | 0/73 (0%) |
| argue / justify (arguing, defending or justifying oneself) | unclear | `答辩` | 1/152 (1%) | 0/81 (0%) | 35/138 (25%) | 93/158 (59%) | 0/43 (0%) | 0/73 (0%) |

Not in the draft: false (excluded: the question's own word)

## think_slot3

| family | side | members | lies | truths | no-pressure truths | unrelated | lies that deny | truths that deny |
|---|---|---|---|---|---|---|---|---|
| true (true, real) | truth | `␣true`, `true`, `True`, `␣True`, `␣TRUE`, `_true`, `TRUE`, `.True`, `确实`, `的确`, `的真`, `属实` | 141/152 (93%) | 79/81 (98%) | 138/138 (100%) | 153/158 (97%) | 32/43 (74%) | 72/73 (99%) |
| refuse (refusing) | unclear | `拒绝`, `拒`, `␣refusal`, `␣refuse` | 8/152 (5%) | 2/81 (2%) | 48/138 (35%) | 0/158 (0%) | 8/43 (19%) | 1/73 (1%) |
| disclose / public (making public, disclosing) | truth | `公开` | 6/152 (4%) | 2/81 (2%) | 0/138 (0%) | 0/158 (0%) | 5/43 (12%) | 1/73 (1%) |
| wrong (wrong, mistaken) | lie | `不对`, `是非` | 6/152 (4%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 3/43 (7%) | 1/73 (1%) |
| deceive (deceiving, cheating) | lie | `骗` | 5/152 (3%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 1/43 (2%) | 0/73 (0%) |
| violate (going against a rule) | unclear | `违反`, `违背` | 1/152 (1%) | 3/81 (4%) | 0/138 (0%) | 0/158 (0%) | 0/43 (0%) | 2/73 (3%) |
| incorrect (incorrect) | lie | `不符合` | 0/152 (0%) | 3/81 (4%) | 0/138 (0%) | 0/158 (0%) | 0/43 (0%) | 2/73 (3%) |
| lie (telling a lie) | lie | `说谎` | 2/152 (1%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 2/43 (5%) | 0/73 (0%) |
| honest (being honest) | truth | `诚实` | 2/152 (1%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 1/43 (2%) | 0/73 (0%) |
| reject (dismissing or overruling a claim) | unclear | `驳回` | 1/152 (1%) | 1/81 (1%) | 16/138 (12%) | 0/158 (0%) | 1/43 (2%) | 1/73 (1%) |
| correct (correct) | truth | `␣correct`, `␣correcting`, `正确` | 1/152 (1%) | 1/81 (1%) | 2/138 (1%) | 3/158 (2%) | 0/43 (0%) | 1/73 (1%) |
| hide (concealing) | lie | `隐匿` | 1/152 (1%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 1/43 (2%) | 0/73 (0%) |
| sorry (apologizing) | unclear | `抱歉` | 0/152 (0%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 0/43 (0%) | 0/73 (0%) |
| secret (doing something secretly or privately) | lie | `私下` | 1/152 (1%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 0/43 (0%) | 0/73 (0%) |
| accurate (accurate) | truth | `准确` | 1/152 (1%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 0/43 (0%) | 0/73 (0%) |
| objective (objective) | unclear | `客观` | 1/152 (1%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 0/43 (0%) | 0/73 (0%) |

Not in the draft: deny (excluded: admit / deny / acknowledge); admit (excluded: admit / deny / acknowledge); false (excluded: the question's own word); truth (excluded: truth from the question on)
