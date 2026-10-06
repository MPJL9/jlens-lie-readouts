# Draft families: qwen3.6-27b, logit lens, part Q7_ab, group questionb

Written by `scripts/apply_family_decisions.py` (2026-10-01; draft, not frozen). Counts are `present / transcripts (share)`
on the build split.

## q_tok8

| family | side | members | lies | truths | no-pressure truths | unrelated | lies that deny | truths that deny |
|---|---|---|---|---|---|---|---|---|
| honest (being honest) | truth | `␣honestly`, `␣honest`, `␣honesty` | 76/152 (50%) | 21/81 (26%) | 0/138 (0%) | 0/158 (0%) | 38/79 (48%) | 21/77 (27%) |
| true (true, real) | truth | `␣true`, `true`, `True`, `␣True` | 9/152 (6%) | 5/81 (6%) | 1/138 (1%) | 3/158 (2%) | 3/79 (4%) | 4/77 (5%) |
| false (false, untrue) | lie | `真假` | 5/152 (3%) | 2/81 (2%) | 56/138 (41%) | 100/158 (63%) | 1/79 (1%) | 1/77 (1%) |
| self-examination (examining or checking one's own conduct) | unclear | `自查` | 0/152 (0%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 0/79 (0%) | 1/77 (1%) |

Not in the draft: truth (excluded: the question's own word)

## q_tok9

| family | side | members | lies | truths | no-pressure truths | unrelated | lies that deny | truths that deny |
|---|---|---|---|---|---|---|---|---|
| true (true, real) | truth | `␣true`, `true`, `True`, `␣True`, `␣TRUE`, `TRUE`, `(True` | 116/152 (76%) | 57/81 (70%) | 108/138 (78%) | 141/158 (89%) | 48/79 (61%) | 53/77 (69%) |

Not in the draft: truth (excluded: the question's own word)

## q_tok10

| family | side | members | lies | truths | no-pressure truths | unrelated | lies that deny | truths that deny |
|---|---|---|---|---|---|---|---|---|
| true (true, real) | truth | `␣true`, `true`, `True`, `␣True`, `TRUE`, `(True` | 150/152 (99%) | 80/81 (99%) | 138/138 (100%) | 158/158 (100%) | 77/79 (97%) | 76/77 (99%) |
| correct (correct) | truth | `(true` | 87/152 (57%) | 43/81 (53%) | 91/138 (66%) | 97/158 (61%) | 36/79 (46%) | 39/77 (51%) |
| abstain (abstaining: declining to give an answer) | unclear | `弃权` | 56/152 (37%) | 30/81 (37%) | 119/138 (86%) | 124/158 (78%) | 22/79 (28%) | 26/77 (34%) |

Not in the draft: integrity (excluded: the question's own word); truth (excluded: the question's own word)

## q_tok11

| family | side | members | lies | truths | no-pressure truths | unrelated | lies that deny | truths that deny |
|---|---|---|---|---|---|---|---|---|
| refusal (refusing to answer) | unclear | `␣refusal` | 128/152 (84%) | 65/81 (80%) | 120/138 (87%) | 68/158 (43%) | 60/79 (76%) | 62/77 (81%) |
| true (true, real) | truth | `␣true`, `true`, `␣True` | 122/152 (80%) | 53/81 (65%) | 68/138 (49%) | 91/158 (58%) | 55/79 (70%) | 50/77 (65%) |
| false (false, untrue) | lie | `␣False`, `.assertFalse` | 32/152 (21%) | 11/81 (14%) | 1/138 (1%) | 11/158 (7%) | 17/79 (22%) | 9/77 (12%) |
| abstain (abstaining: declining to give an answer) | unclear | `弃权` | 12/152 (8%) | 4/81 (5%) | 5/138 (4%) | 0/158 (0%) | 11/79 (14%) | 4/77 (5%) |

## q_tok12

| family | side | members | lies | truths | no-pressure truths | unrelated | lies that deny | truths that deny |
|---|---|---|---|---|---|---|---|---|
| true (true, real) | truth | `␣true`, `true`, `␣True` | 152/152 (100%) | 81/81 (100%) | 138/138 (100%) | 157/158 (99%) | 79/79 (100%) | 77/77 (100%) |
| false (false, untrue) | lie | `false`, `:false` | 90/152 (59%) | 60/81 (74%) | 32/138 (23%) | 106/158 (67%) | 46/79 (58%) | 57/77 (74%) |
| refusal (refusing to answer) | unclear | `␣refusal` | 1/152 (1%) | 0/81 (0%) | 1/138 (1%) | 1/158 (1%) | 0/79 (0%) | 0/77 (0%) |
| reveal (revealing / making known) | truth | `揭晓` | 0/152 (0%) | 1/81 (1%) | 1/138 (1%) | 3/158 (2%) | 0/79 (0%) | 1/77 (1%) |

## q_tok13

| family | side | members | lies | truths | no-pressure truths | unrelated | lies that deny | truths that deny |
|---|---|---|---|---|---|---|---|---|
| refusal (refusing to answer) | unclear | `谢绝` | 43/152 (28%) | 30/81 (37%) | 14/138 (10%) | 12/158 (8%) | 18/79 (23%) | 30/77 (39%) |

## q_tok14

| family | side | members | lies | truths | no-pressure truths | unrelated | lies that deny | truths that deny |
|---|---|---|---|---|---|---|---|---|
| honest (being honest) | truth | `␣honesty`, `␣honest`, `␣honestly`, `␣Honest`, `誠`, `诚信` | 85/152 (56%) | 28/81 (35%) | 2/138 (1%) | 0/158 (0%) | 39/79 (49%) | 25/77 (32%) |
| true (true, real) | truth | `␣true`, `true`, `True`, `␣True` | 61/152 (40%) | 18/81 (22%) | 16/138 (12%) | 2/158 (1%) | 14/79 (18%) | 15/77 (19%) |
| false (false, untrue) | lie | `␣false`, `.False`, `/false`, `真假` | 39/152 (26%) | 29/81 (36%) | 95/138 (69%) | 35/158 (22%) | 24/79 (30%) | 27/77 (35%) |
| self-examination (examining or reflecting on one's own conduct) | unclear | `反思`, `自查`, `自省` | 37/152 (24%) | 7/81 (9%) | 1/138 (1%) | 0/158 (0%) | 20/79 (25%) | 6/77 (8%) |
| comply (obeying / complying with rules or instructions) | unclear | `服从`, `遵守`, `合规` | 22/152 (14%) | 4/81 (5%) | 20/138 (14%) | 10/158 (6%) | 13/79 (16%) | 4/77 (5%) |
| wrong (wrong, mistaken) | lie | `是非` | 20/152 (13%) | 5/81 (6%) | 0/138 (0%) | 0/158 (0%) | 12/79 (15%) | 5/77 (6%) |
| reveal (revealing / making known) | truth | `␣reveal`, `揭示了`, `揭示`, `揭晓` | 12/152 (8%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 6/79 (8%) | 0/77 (0%) |
| violate (violating rules (wrongdoing)) | unclear | `违反` | 3/152 (2%) | 2/81 (2%) | 0/138 (0%) | 0/158 (0%) | 1/79 (1%) | 2/77 (3%) |
| self-check (checking oneself) | unclear | `自查` | 3/152 (2%) | 2/81 (2%) | 0/138 (0%) | 0/158 (0%) | 3/79 (4%) | 2/77 (3%) |
| disclose (making public) | truth | `公开` | 3/152 (2%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 2/79 (3%) | 1/77 (1%) |
| secret (secrecy) | lie | `秘密`, `␣secret` | 4/152 (3%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 4/79 (5%) | 0/77 (0%) |
| hidden (being hidden) | lie | `␣hidden`, `(hidden` | 2/152 (1%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 2/79 (3%) | 0/77 (0%) |
| morality (morality / moral judgement) | unclear | `道德`, `的道德`, `␣moral` | 2/152 (1%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 0/79 (0%) | 0/77 (0%) |
| integrity (honesty and keeping one's word) | truth | `诚信` | 1/152 (1%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 0/79 (0%) | 0/77 (0%) |
| candour (being frank and open) | truth | `坦诚` | 1/152 (1%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 1/79 (1%) | 0/77 (0%) |
| confess (confessing / coming clean) | truth | `坦白` | 1/152 (1%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 1/79 (1%) | 0/77 (0%) |
| silence (keeping silent) | unclear | `沉默` | 1/152 (1%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 1/79 (1%) | 0/77 (0%) |
| clarify (clarifying / setting the record straight) | unclear | `澄清` | 0/152 (0%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 0/79 (0%) | 1/77 (1%) |
| evade (dodging, hiding from) | lie | `躲` | 1/152 (1%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 1/79 (1%) | 0/77 (0%) |

Not in the draft: admit (excluded: admit / deny / acknowledge); deny (excluded: admit / deny / acknowledge); truth (excluded: the question's own word); correct (excluded: the question's own word)

## q_tok15

| family | side | members | lies | truths | no-pressure truths | unrelated | lies that deny | truths that deny |
|---|---|---|---|---|---|---|---|---|
| wrong (wrong, mistaken) | lie | `是非` | 15/152 (10%) | 17/81 (21%) | 0/138 (0%) | 24/158 (15%) | 9/79 (11%) | 17/77 (22%) |
| comply (obeying / complying with rules or instructions) | unclear | `遵守`, `听话` | 2/152 (1%) | 1/81 (1%) | 1/138 (1%) | 0/158 (0%) | 1/79 (1%) | 1/77 (1%) |
| clarify (clarifying / setting the record straight) | unclear | `澄清` | 0/152 (0%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 0/79 (0%) | 1/77 (1%) |
| fact (fact, factual) | truth | `事实` | 0/152 (0%) | 0/81 (0%) | 0/138 (0%) | 10/158 (6%) | 0/79 (0%) | 0/77 (0%) |
| false (false, untrue) | lie | `真假` | 0/152 (0%) | 0/81 (0%) | 0/138 (0%) | 19/158 (12%) | 0/79 (0%) | 0/77 (0%) |

Not in the draft: truth (excluded: the question's own word)
