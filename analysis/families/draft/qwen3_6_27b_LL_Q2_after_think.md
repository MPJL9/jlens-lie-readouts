# Draft families: qwen3.6-27b, logit lens, part Q2_after, group think

Written by `scripts/apply_family_decisions.py` (2026-10-01; draft, not frozen). Counts are `present / transcripts (share)`
on the build split.

## think_slot0

| family | side | members | lies | truths | no-pressure truths | unrelated | lies that deny | truths that deny |
|---|---|---|---|---|---|---|---|---|
| clarify (making something clear, setting the record straight) | unclear | `澄清`, `␣clarification` | 117/152 (77%) | 72/81 (89%) | 138/138 (100%) | 158/158 (100%) | 34/47 (72%) | 68/77 (88%) |
| violation (breaking a rule) | unclear | `违规` | 60/152 (39%) | 34/81 (42%) | 7/138 (5%) | 0/158 (0%) | 32/47 (68%) | 34/77 (44%) |
| wrong (wrong, mistaken) | lie | `_WRONG`, `指正` | 26/152 (17%) | 11/81 (14%) | 28/138 (20%) | 0/158 (0%) | 3/47 (6%) | 10/77 (13%) |
| sincere (sincerity, genuine feeling) | truth | `真情`, `真诚` | 0/152 (0%) | 5/81 (6%) | 13/138 (9%) | 101/158 (64%) | 0/47 (0%) | 5/77 (6%) |
| conceal (to conceal, to hide) | lie | `掩` | 0/152 (0%) | 0/81 (0%) | 0/138 (0%) | 4/158 (3%) | 0/47 (0%) | 0/77 (0%) |
| fact (fact, factual) | truth | `␣fact` | 0/152 (0%) | 0/81 (0%) | 8/138 (6%) | 0/158 (0%) | 0/47 (0%) | 0/77 (0%) |

Not in the draft: argue / defend (held back: no undisputed member left); truth (excluded: truth from the question on)

## think_slot1

| family | side | members | lies | truths | no-pressure truths | unrelated | lies that deny | truths that deny |
|---|---|---|---|---|---|---|---|---|
| intentional (deliberately, on purpose) | unclear | `有心` | 152/152 (100%) | 81/81 (100%) | 137/138 (99%) | 147/158 (93%) | 47/47 (100%) | 77/77 (100%) |
| unauthorized (without permission) | unclear | `未经允许` | 83/152 (55%) | 46/81 (57%) | 14/138 (10%) | 2/158 (1%) | 18/47 (38%) | 45/77 (58%) |
| wrong (wrong, mistaken) | lie | `␣mistakes`, `␣mistaken`, `_WRONG`, `指正`, `的错误` | 6/152 (4%) | 2/81 (2%) | 24/138 (17%) | 21/158 (13%) | 2/47 (4%) | 2/77 (3%) |
| neutral (taking no side) | unclear | `␣neutrality` | 4/152 (3%) | 2/81 (2%) | 0/138 (0%) | 0/158 (0%) | 1/47 (2%) | 2/77 (3%) |
| objective (being objective / impartial) | unclear | `␣objective` | 0/152 (0%) | 2/81 (2%) | 1/138 (1%) | 0/158 (0%) | 0/47 (0%) | 2/77 (3%) |
| truth (the truth) | truth | `求真` | 0/152 (0%) | 0/81 (0%) | 0/138 (0%) | 4/158 (3%) | 0/47 (0%) | 0/77 (0%) |

Not in the draft: doubt / suspicion (held back: no undisputed member left); deceive (excluded: the question's own word)

## think_slot2

| family | side | members | lies | truths | no-pressure truths | unrelated | lies that deny | truths that deny |
|---|---|---|---|---|---|---|---|---|
| ethics (ethics, morality) | unclear | `␣ethics`, `␣ethical`, `职业道德`, `思想道德` | 112/152 (74%) | 48/81 (59%) | 96/138 (70%) | 104/158 (66%) | 29/47 (62%) | 45/77 (58%) |
| neutral (taking no side) | unclear | `中立` | 108/152 (71%) | 44/81 (54%) | 1/138 (1%) | 0/158 (0%) | 29/47 (62%) | 41/77 (53%) |
| breach (breaking a rule or duty) | unclear | `␣breach`, `␣breaches`, `触犯` | 117/152 (77%) | 34/81 (42%) | 55/138 (40%) | 0/158 (0%) | 36/47 (77%) | 32/77 (42%) |
| true (true, real) | truth | `␣true`, `True`, `␣TRUE`, `␣genuinely`, `真的`, `真正`, `的确`, `的確` | 79/152 (52%) | 30/81 (37%) | 22/138 (16%) | 0/158 (0%) | 10/47 (21%) | 28/77 (36%) |
| legality (lawful or legal standing) | unclear | `␣legally`, `/legal` | 26/152 (17%) | 11/81 (14%) | 8/138 (6%) | 0/158 (0%) | 19/47 (40%) | 11/77 (14%) |
| false (false, untrue) | lie | `␣false`, `false`, `False`, `␣FALSE`, `:false`, `(False`, `FALSE`, `>false`, `_false`, `.assertFalse`, `.False`, `.false`, `.FALSE`, `/false` | 9/152 (6%) | 28/81 (35%) | 104/138 (75%) | 117/158 (74%) | 8/47 (17%) | 28/77 (36%) |
| refuse (refusing) | unclear | `拒`, `拒绝`, `␣refuse` | 11/152 (7%) | 2/81 (2%) | 0/138 (0%) | 0/158 (0%) | 11/47 (23%) | 2/77 (3%) |
| upright (upright, honest in character) | truth | `正直` | 7/152 (5%) | 6/81 (7%) | 8/138 (6%) | 1/158 (1%) | 1/47 (2%) | 4/77 (5%) |
| hide (hiding something) | lie | `藏` | 7/152 (5%) | 2/81 (2%) | 0/138 (0%) | 1/158 (1%) | 3/47 (6%) | 2/77 (3%) |
| apology (saying sorry) | unclear | `抱歉`, `对不起` | 5/152 (3%) | 2/81 (2%) | 0/138 (0%) | 6/158 (4%) | 5/47 (11%) | 2/77 (3%) |
| justify / excuse (giving reasons that defend an act) | unclear | `␣justification`, `␣justified`, `␣excuse` | 3/152 (2%) | 2/81 (2%) | 0/138 (0%) | 0/158 (0%) | 0/47 (0%) | 1/77 (1%) |
| clarify (making something clear) | unclear | `␣clarification`, `澄清` | 1/152 (1%) | 1/81 (1%) | 2/138 (1%) | 0/158 (0%) | 1/47 (2%) | 1/77 (1%) |
| argue / defend (defending oneself in argument) | unclear | `答辩` | 0/152 (0%) | 1/81 (1%) | 15/138 (11%) | 123/158 (78%) | 0/47 (0%) | 1/77 (1%) |
| responsible (acting responsibly) | unclear | `负责任` | 1/152 (1%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 0/47 (0%) | 0/77 (0%) |

Not in the draft: two-faced (held back: no undisputed member left); deceive (excluded: the question's own word)

## think_slot3

| family | side | members | lies | truths | no-pressure truths | unrelated | lies that deny | truths that deny |
|---|---|---|---|---|---|---|---|---|
| false (false, untrue) | lie | `␣false`, `␣False`, `(false`, `false`, `False`, `=False`, `␣FALSE`, `:false`, `(False`, `FALSE`, `>false`, `_false`, `.assertFalse`, `.False`, `assertFalse`, `.false`, `.FALSE`, `/false`, `假`, `假的` | 151/152 (99%) | 81/81 (100%) | 138/138 (100%) | 158/158 (100%) | 47/47 (100%) | 77/77 (100%) |
| true (true, real) | truth | `␣true`, `true`, `True`, `␣True`, `␣TRUE`, `.True`, `真正的`, `的确`, `的真`, `属实` | 141/152 (93%) | 79/81 (98%) | 138/138 (100%) | 141/158 (89%) | 36/47 (77%) | 75/77 (97%) |
| reject / overrule (rejecting or overruling (a proposal, a claim)) | unclear | `否决`, `驳回` | 13/152 (9%) | 46/81 (57%) | 56/138 (41%) | 8/158 (5%) | 13/47 (28%) | 46/77 (60%) |
| refuse (refusing) | unclear | `拒绝`, `␣refusal`, `␣refuse`, `拒`, `不予` | 10/152 (7%) | 2/81 (2%) | 50/138 (36%) | 0/158 (0%) | 7/47 (15%) | 2/77 (3%) |
| public / disclose (making public, disclosing) | truth | `公开` | 7/152 (5%) | 4/81 (5%) | 0/138 (0%) | 0/158 (0%) | 5/47 (11%) | 4/77 (5%) |
| wrong (wrong, mistaken) | lie | `不对`, `是非` | 8/152 (5%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 4/47 (9%) | 1/77 (1%) |
| apology (saying sorry) | unclear | `对不起`, `抱歉` | 4/152 (3%) | 2/81 (2%) | 1/138 (1%) | 0/158 (0%) | 4/47 (9%) | 2/77 (3%) |
| private / secret (in private, secretly) | lie | `私下` | 4/152 (3%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 1/47 (2%) | 0/77 (0%) |
| honest (being honest) | truth | `诚实`, `␣truthful` | 3/152 (2%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 1/47 (2%) | 0/77 (0%) |
| ostensible (on the surface, outwardly) | unclear | `表面上` | 3/152 (2%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 1/47 (2%) | 0/77 (0%) |
| legality (lawful or legal standing) | unclear | `␣legally` | 1/152 (1%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 1/47 (2%) | 1/77 (1%) |
| objective (being objective / impartial) | unclear | `客观` | 2/152 (1%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 1/47 (2%) | 0/77 (0%) |
| evade (avoiding or evading) | lie | `回避` | 1/152 (1%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 1/47 (2%) | 0/77 (0%) |
| go against (acting against (a principle, conscience)) | unclear | `违背` | 0/152 (0%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 0/47 (0%) | 1/77 (1%) |
| accurate (accurate) | truth | `准确` | 1/152 (1%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 1/47 (2%) | 0/77 (0%) |
| incorrect (incorrect) | lie | `不符合` | 0/152 (0%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 0/47 (0%) | 1/77 (1%) |

Not in the draft: deny (excluded: admit / deny / acknowledge); admit (excluded: admit / deny / acknowledge); truth (excluded: truth from the question on)
