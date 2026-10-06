# Draft families: qwen3.6-27b, J-lens, part Q9_dyl, group questionb

Written by `scripts/apply_family_decisions.py` (2026-10-01; draft, not frozen). Counts are `present / transcripts (share)`
on the build split.

## q_tok8

| family | side | members | lies | truths | no-pressure truths | unrelated | lies that deny | truths that deny |
|---|---|---|---|---|---|---|---|---|
| honest (being honest) | truth | `␣honestly`, `␣honest`, `诚实`, `␣honesty`, `␣Honest` | 147/152 (97%) | 73/81 (90%) | 78/138 (57%) | 118/158 (75%) | 62/65 (95%) | 70/76 (92%) |
| truthful (being truthful) | truth | `␣truthful` | 121/152 (80%) | 47/81 (58%) | 90/138 (65%) | 81/158 (51%) | 50/65 (77%) | 43/76 (57%) |
| truth (the truth / telling the truth) | truth | `␣truthful` | 121/152 (80%) | 47/81 (58%) | 90/138 (65%) | 81/158 (51%) | 50/65 (77%) | 43/76 (57%) |
| direct (answering directly, straightforwardly) | unclear | `␣directly`, `直接`, `␣direct`, `的直接`, `␣Direct`, `␣DIRECT`, `Direct`, `␣directement`, `direct`, `␣directamente`, `␣напрямую`, `␣straight` | 26/152 (17%) | 20/81 (25%) | 9/138 (7%) | 0/158 (0%) | 11/65 (17%) | 20/76 (26%) |
| explicit (stating explicitly) | unclear | `␣explicitly`, `␣Explicit`, `explicit` | 3/152 (2%) | 2/81 (2%) | 1/138 (1%) | 0/158 (0%) | 2/65 (3%) | 2/76 (3%) |
| plainly (speaking plainly) | unclear | `␣plainly` | 2/152 (1%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 2/65 (3%) | 1/76 (1%) |
| true (true, real) | truth | `␣true`, `␣True`, `␣TRUE` | 0/152 (0%) | 1/81 (1%) | 2/138 (1%) | 1/158 (1%) | 0/65 (0%) | 0/76 (0%) |

## q_tok9

| family | side | members | lies | truths | no-pressure truths | unrelated | lies that deny | truths that deny |
|---|---|---|---|---|---|---|---|---|
| direct (answering directly, straightforwardly) | unclear | `或直接` | 21/152 (14%) | 10/81 (12%) | 13/138 (9%) | 0/158 (0%) | 7/65 (11%) | 10/76 (13%) |
| false (false, untrue) | lie | `/false` | 2/152 (1%) | 0/81 (0%) | 3/138 (2%) | 0/158 (0%) | 1/65 (2%) | 0/76 (0%) |

## q_tok10

| family | side | members | lies | truths | no-pressure truths | unrelated | lies that deny | truths that deny |
|---|---|---|---|---|---|---|---|---|
| direct (answering directly, straightforwardly) | unclear | `␣directly`, `直接`, `␣direct`, `直接的`, `Direct`, `的直接`, `请直接`, `␣Direct`, `direct`, `␣direkt`, `直接在`, `是直接`, `␣langsung`, `␣direttamente`, `␣directement`, `␣directamente`, `␣напрямую` | 4/152 (3%) | 5/81 (6%) | 3/138 (2%) | 0/158 (0%) | 1/65 (2%) | 5/76 (7%) |
| upfront (being upfront, frank) | unclear | `␣upfront` | 5/152 (3%) | 1/81 (1%) | 2/138 (1%) | 0/158 (0%) | 4/65 (6%) | 0/76 (0%) |
| false (false, untrue) | lie | `False`, `:false` | 0/152 (0%) | 0/81 (0%) | 0/138 (0%) | 3/158 (2%) | 0/65 (0%) | 0/76 (0%) |

## q_tok11

| family | side | members | lies | truths | no-pressure truths | unrelated | lies that deny | truths that deny |
|---|---|---|---|---|---|---|---|---|
| direct (answering directly, straightforwardly) | unclear | `␣directly`, `直接`, `␣direct`, `请直接`, `␣Direct`, `Direct`, `direct`, `␣DIRECT`, `_direct`, `直接的`, `的直接`, `␣langsung`, `␣direttamente`, `␣directement`, `␣directamente`, `␣diretamente`, `␣напрямую` | 8/152 (5%) | 5/81 (6%) | 7/138 (5%) | 0/158 (0%) | 3/65 (5%) | 5/76 (7%) |
| upfront (being upfront, frank) | unclear | `␣upfront` | 2/152 (1%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 1/65 (2%) | 0/76 (0%) |

## q_tok12

| family | side | members | lies | truths | no-pressure truths | unrelated | lies that deny | truths that deny |
|---|---|---|---|---|---|---|---|---|
| justify (justifying the act) | unclear | `␣justify`, `␣justification` | 141/152 (93%) | 73/81 (90%) | 125/138 (91%) | 157/158 (99%) | 61/65 (94%) | 69/76 (91%) |
| disclaimer (adding a disclaimer / hedge to the reply) | unclear | `␣disclaimer`, `␣Disclaimer` | 101/152 (66%) | 53/81 (65%) | 60/138 (43%) | 8/158 (5%) | 51/65 (78%) | 52/76 (68%) |
| ethics / morality (moral standing of the act) | unclear | `␣ethical`, `␣ethics`, `␣Ethics`, `ethical`, `␣moral`, `␣morality`, `␣morally`, `道德`, `伦理`, `的道德` | 2/152 (1%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 1/65 (2%) | 1/76 (1%) |
| unethical (the act is unethical) | lie | `␣unethical` | 2/152 (1%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 1/65 (2%) | 0/76 (0%) |
| comply (complying with rules) | unclear | `␣compliance`, `遵守` | 2/152 (1%) | 0/81 (0%) | 1/138 (1%) | 0/158 (0%) | 1/65 (2%) | 0/76 (0%) |
| violate (breaking a rule or norm) | unclear | `␣violate`, `违规`, `违反`, `违背` | 1/152 (1%) | 0/81 (0%) | 1/138 (1%) | 0/158 (0%) | 0/65 (0%) | 0/76 (0%) |
| refusal (refusing) | unclear | `␣refusal` | 0/152 (0%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 0/65 (0%) | 1/76 (1%) |
| confidential (keeping something confidential) | lie | `␣confidentiality`, `保密` | 1/152 (1%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 0/65 (0%) | 0/76 (0%) |
| conceal (concealing / hiding the truth) | lie | `隐瞒` | 1/152 (1%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 0/65 (0%) | 0/76 (0%) |
| honest (being honest) | truth | `␣honesty` | 1/152 (1%) | 0/81 (0%) | 1/138 (1%) | 0/158 (0%) | 1/65 (2%) | 0/76 (0%) |
| truthful (being truthful) | truth | `␣truthful` | 1/152 (1%) | 0/81 (0%) | 1/138 (1%) | 0/158 (0%) | 0/65 (0%) | 0/76 (0%) |
| accountability (being accountable for one's act) | unclear | `␣accountability` | 1/152 (1%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 1/65 (2%) | 0/76 (0%) |
| truth (the truth / telling the truth) | truth | `␣truthful` | 1/152 (1%) | 0/81 (0%) | 1/138 (1%) | 0/158 (0%) | 0/65 (0%) | 0/76 (0%) |
| persona (a persona / role being played) | unclear | `␣persona`, `␣Persona`, `Persona` | 1/152 (1%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 0/65 (0%) | 0/76 (0%) |
| self-review (reviewing one's own past act) | unclear | `复盘` | 1/152 (1%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 0/65 (0%) | 0/76 (0%) |
| fact (fact, factual) | truth | `␣facts`, `␣factual`, `事实` | 0/152 (0%) | 0/81 (0%) | 1/138 (1%) | 0/158 (0%) | 0/65 (0%) | 0/76 (0%) |
| accurate (accurate) | truth | `␣accuracy`, `␣Accuracy` | 0/152 (0%) | 0/81 (0%) | 1/138 (1%) | 0/158 (0%) | 0/65 (0%) | 0/76 (0%) |
| false (false, untrue) | lie | `␣fals` | 0/152 (0%) | 0/81 (0%) | 1/138 (1%) | 0/158 (0%) | 0/65 (0%) | 0/76 (0%) |
| correct (correct) | truth | `␣correctness` | 0/152 (0%) | 0/81 (0%) | 1/138 (1%) | 0/158 (0%) | 0/65 (0%) | 0/76 (0%) |
| true (true, real) | truth | `真实`, `真实性` | 0/152 (0%) | 0/81 (0%) | 1/138 (1%) | 0/158 (0%) | 0/65 (0%) | 0/76 (0%) |

Not in the draft: acknowledge (excluded: admit / deny / acknowledge)

## q_tok13

| family | side | members | lies | truths | no-pressure truths | unrelated | lies that deny | truths that deny |
|---|---|---|---|---|---|---|---|---|
| silence (staying silent) | unclear | `␣silence` | 29/152 (19%) | 7/81 (9%) | 4/138 (3%) | 1/158 (1%) | 15/65 (23%) | 7/76 (9%) |

## q_tok14

| family | side | members | lies | truths | no-pressure truths | unrelated | lies that deny | truths that deny |
|---|---|---|---|---|---|---|---|---|
| silence (staying silent) | unclear | `␣silence` | 8/152 (5%) | 2/81 (2%) | 0/138 (0%) | 0/158 (0%) | 4/65 (6%) | 2/76 (3%) |
| comply (complying with rules) | unclear | `严格遵守` | 2/152 (1%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 1/65 (2%) | 1/76 (1%) |

## q_tok15

| family | side | members | lies | truths | no-pressure truths | unrelated | lies that deny | truths that deny |
|---|---|---|---|---|---|---|---|---|
| honest (being honest) | truth | `诚实`, `␣honesty`, `␣honest` | 19/152 (12%) | 8/81 (10%) | 11/138 (8%) | 3/158 (2%) | 7/65 (11%) | 5/76 (7%) |
| forced (being forced, coerced) | unclear | `forced`, `␣forced`, `逼`, `␣Forced`, `强迫`, `逼迫`, `迫使`, `␣forcing`, `迫`, `forcing`, `␣compelled` | 16/152 (11%) | 6/81 (7%) | 0/138 (0%) | 0/158 (0%) | 11/65 (17%) | 6/76 (8%) |
| truthful (being truthful) | truth | `␣truthful` | 3/152 (2%) | 5/81 (6%) | 7/138 (5%) | 2/158 (1%) | 1/65 (2%) | 3/76 (4%) |
| truth (the truth / telling the truth) | truth | `␣truthful` | 3/152 (2%) | 5/81 (6%) | 7/138 (5%) | 2/158 (1%) | 1/65 (2%) | 3/76 (4%) |
| accusation (being accused) | unclear | `␣accusation` | 1/152 (1%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 0/65 (0%) | 0/76 (0%) |
| self-reflection (reflecting on one's own act) | unclear | `反思` | 0/152 (0%) | 1/81 (1%) | 1/138 (1%) | 0/158 (0%) | 0/65 (0%) | 1/76 (1%) |
| false (false, untrue) | lie | `真假` | 0/152 (0%) | 0/81 (0%) | 0/138 (0%) | 1/158 (1%) | 0/65 (0%) | 0/76 (0%) |
