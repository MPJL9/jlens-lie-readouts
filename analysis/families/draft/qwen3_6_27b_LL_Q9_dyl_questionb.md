# Draft families: qwen3.6-27b, logit lens, part Q9_dyl, group questionb

Written by `scripts/apply_family_decisions.py` (2026-10-01; draft, not frozen). Counts are `present / transcripts (share)`
on the build split.

## q_tok8

| family | side | members | lies | truths | no-pressure truths | unrelated | lies that deny | truths that deny |
|---|---|---|---|---|---|---|---|---|
| true (true, real) | truth | `␣true`, `true`, `␣True`, `的真` | 106/152 (70%) | 45/81 (56%) | 69/138 (50%) | 79/158 (50%) | 41/65 (63%) | 42/76 (55%) |
| honest (being honest, telling the truth) | truth | `␣honestly`, `诚实`, `␣honest`, `␣honesty` | 79/152 (52%) | 19/81 (23%) | 0/138 (0%) | 2/158 (1%) | 34/65 (52%) | 19/76 (25%) |
| direct (answering directly, straightforwardly) | unclear | `␣directly`, `␣straight`, `直接`, `的直接`, `␣direct`, `direct`, `Direct`, `␣Direct`, `可直接`, `␣directement`, `是直接` | 52/152 (34%) | 30/81 (37%) | 13/138 (9%) | 0/158 (0%) | 25/65 (38%) | 30/76 (39%) |

Not in the draft: truth (excluded: truth from the question on); forced (held back: no undisputed member left)

## q_tok9

| family | side | members | lies | truths | no-pressure truths | unrelated | lies that deny | truths that deny |
|---|---|---|---|---|---|---|---|---|
| true (true, real) | truth | `true`, `True`, `␣True` | 110/152 (72%) | 56/81 (69%) | 101/138 (73%) | 104/158 (66%) | 40/65 (62%) | 52/76 (68%) |
| false (false, untrue) | lie | `␣False`, `/false` | 10/152 (7%) | 9/81 (11%) | 5/138 (4%) | 0/158 (0%) | 8/65 (12%) | 8/76 (11%) |
| wrong (wrong, mistaken) | lie | `对错` | 3/152 (2%) | 2/81 (2%) | 0/138 (0%) | 0/158 (0%) | 3/65 (5%) | 2/76 (3%) |
| comply (complying with or obeying instructions) | unclear | `␣compliance` | 2/152 (1%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 0/65 (0%) | 1/76 (1%) |

Not in the draft: admit (excluded: admit / deny / acknowledge)

## q_tok10

| family | side | members | lies | truths | no-pressure truths | unrelated | lies that deny | truths that deny |
|---|---|---|---|---|---|---|---|---|
| direct (answering directly, straightforwardly) | unclear | `␣directly`, `␣direct`, `直接的`, `直接`, `的直接`, `␣straight`, `␣Direct`, `Direct`, `direct`, `直接在`, `请直接`, `是直接`, `就直接`, `直接将`, `直接用`, `␣directamente` | 17/152 (11%) | 10/81 (12%) | 13/138 (9%) | 0/158 (0%) | 9/65 (14%) | 10/76 (13%) |
| false (false, untrue) | lie | `␣false`, `false`, `.assertFalse` | 3/152 (2%) | 3/81 (4%) | 9/138 (7%) | 70/158 (44%) | 3/65 (5%) | 3/76 (4%) |
| sorry (apologising, regret) | unclear | `␣sorry` | 3/152 (2%) | 2/81 (2%) | 1/138 (1%) | 7/158 (4%) | 3/65 (5%) | 2/76 (3%) |
| forced (being forced or compelled) | unclear | `␣forced` | 1/152 (1%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 0/65 (0%) | 0/76 (0%) |

## q_tok11

| family | side | members | lies | truths | no-pressure truths | unrelated | lies that deny | truths that deny |
|---|---|---|---|---|---|---|---|---|
| false (false, untrue) | lie | `␣false`, `false`, `FALSE`, `/false` | 152/152 (100%) | 81/81 (100%) | 138/138 (100%) | 158/158 (100%) | 65/65 (100%) | 76/76 (100%) |
| true (true, real) | truth | `␣true`, `true`, `成立` | 84/152 (55%) | 37/81 (46%) | 80/138 (58%) | 147/158 (93%) | 25/65 (38%) | 33/76 (43%) |
| direct (answering directly, straightforwardly) | unclear | `␣directly`, `␣direct`, `直接`, `直接的`, `的直接`, `请直接`, `Direct`, `DIRECT`, `␣Direct`, `direct`, `␣straightforward`, `是直接`, `_direct`, `␣directement`, `␣directamente`, `␣direttamente`, `␣diretamente`, `␣напрямую`, `␣straight`, `␣DIRECT`, `-direct`, `直接在` | 58/152 (38%) | 35/81 (43%) | 32/138 (23%) | 1/158 (1%) | 27/65 (42%) | 35/76 (46%) |
| neutral (taking a neutral stance) | unclear | `中立` | 0/152 (0%) | 13/81 (16%) | 0/138 (0%) | 0/158 (0%) | 0/65 (0%) | 13/76 (17%) |
| kidding (joking, not being serious) | unclear | `␣kidding` | 4/152 (3%) | 4/81 (5%) | 2/138 (1%) | 0/158 (0%) | 2/65 (3%) | 3/76 (4%) |
| silent (staying silent, not speaking) | unclear | `不语` | 5/152 (3%) | 1/81 (1%) | 1/138 (1%) | 0/158 (0%) | 2/65 (3%) | 0/76 (0%) |
| shame (feeling ashamed) | unclear | `愧` | 0/152 (0%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 0/65 (0%) | 1/76 (1%) |

Not in the draft: deny (excluded: admit / deny / acknowledge); admit (excluded: admit / deny / acknowledge)

## q_tok12

| family | side | members | lies | truths | no-pressure truths | unrelated | lies that deny | truths that deny |
|---|---|---|---|---|---|---|---|---|
| justify (justifying, defending the act) | unclear | `␣justify`, `␣justification` | 134/152 (88%) | 68/81 (84%) | 103/138 (75%) | 148/158 (94%) | 57/65 (88%) | 64/76 (84%) |
| reflect (reflecting on one's own act) | unclear | `␣reflect` | 47/152 (31%) | 12/81 (15%) | 0/138 (0%) | 0/158 (0%) | 18/65 (28%) | 11/76 (14%) |
| role-play / persona (playing a role or persona) | unclear | `扮演`, `␣persona`, `␣personas`, `␣Persona`, `Persona`, `persona` | 4/152 (3%) | 1/81 (1%) | 1/138 (1%) | 0/158 (0%) | 0/65 (0%) | 1/76 (1%) |
| moral / ethics (moral or ethical judgement) | unclear | `␣moral`, `␣ethical`, `␣ethics`, `␣Ethics`, `道德` | 2/152 (1%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 1/65 (2%) | 0/76 (0%) |
| direct (answering directly, straightforwardly) | unclear | `直接`, `␣direct`, `␣directly` | 1/152 (1%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 1/65 (2%) | 1/76 (1%) |
| violate (violating, going against (rules, principles)) | unclear | `违背` | 1/152 (1%) | 0/81 (0%) | 1/138 (1%) | 0/158 (0%) | 0/65 (0%) | 0/76 (0%) |
| honest (being honest, telling the truth) | truth | `诚实`, `␣truthful`, `坦诚` | 1/152 (1%) | 0/81 (0%) | 1/138 (1%) | 0/158 (0%) | 0/65 (0%) | 0/76 (0%) |
| forced (being forced or compelled) | unclear | `␣forced`, `被迫` | 0/152 (0%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 0/65 (0%) | 1/76 (1%) |
| comply (complying with or obeying instructions) | unclear | `遵守` | 1/152 (1%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 0/65 (0%) | 0/76 (0%) |
| conscience (conscience) | unclear | `良心` | 1/152 (1%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 0/65 (0%) | 0/76 (0%) |
| true (true, real) | truth | `␣true`, `true`, `␣True`, `真实` | 1/152 (1%) | 0/81 (0%) | 1/138 (1%) | 0/158 (0%) | 0/65 (0%) | 0/76 (0%) |
| fact (fact, factual) | truth | `␣facts`, `符合`, `事实`, `是否符合` | 1/152 (1%) | 0/81 (0%) | 1/138 (1%) | 0/158 (0%) | 0/65 (0%) | 0/76 (0%) |
| accurate (accurate) | truth | `␣accuracy`, `准确性` | 0/152 (0%) | 0/81 (0%) | 1/138 (1%) | 0/158 (0%) | 0/65 (0%) | 0/76 (0%) |
| objective (objective) | unclear | `客观` | 0/152 (0%) | 0/81 (0%) | 1/138 (1%) | 0/158 (0%) | 0/65 (0%) | 0/76 (0%) |

Not in the draft: truth (excluded: truth from the question on)

## q_tok14

| family | side | members | lies | truths | no-pressure truths | unrelated | lies that deny | truths that deny |
|---|---|---|---|---|---|---|---|---|
| violate (violating rules; violators) | unclear | `违者` | 94/152 (62%) | 44/81 (54%) | 99/138 (72%) | 142/158 (90%) | 36/65 (55%) | 42/76 (55%) |
| comply (complying with or obeying instructions) | unclear | `␣obey`, `遵守`, `遵照`, `遵循`, `严格遵守` | 42/152 (28%) | 32/81 (40%) | 4/138 (3%) | 0/158 (0%) | 23/65 (35%) | 32/76 (42%) |
| refuse / decline (declining, refusing) | unclear | `谢绝` | 20/152 (13%) | 14/81 (17%) | 11/138 (8%) | 24/158 (15%) | 8/65 (12%) | 14/76 (18%) |

## q_tok15

| family | side | members | lies | truths | no-pressure truths | unrelated | lies that deny | truths that deny |
|---|---|---|---|---|---|---|---|---|
| forced (being forced or compelled) | unclear | `␣forced`, `逼人`, `forced`, `␣forcing`, `迫使`, `逼迫`, `强迫`, `␣Forced`, `␣compelled`, `强制`, `被迫` | 46/152 (30%) | 20/81 (25%) | 2/138 (1%) | 1/158 (1%) | 25/65 (38%) | 19/76 (25%) |
| honest (being honest, telling the truth) | truth | `诚实`, `␣honesty`, `␣honest`, `诚`, `␣truthful` | 41/152 (27%) | 14/81 (17%) | 23/138 (17%) | 3/158 (2%) | 15/65 (23%) | 11/76 (14%) |
| direct (answering directly, straightforwardly) | unclear | `␣direct`, `␣straight` | 41/152 (27%) | 5/81 (6%) | 0/138 (0%) | 0/158 (0%) | 14/65 (22%) | 5/76 (7%) |
| false (false, untrue) | lie | `false`, `/false`, `假的`, `真假` | 21/152 (14%) | 22/81 (27%) | 35/138 (25%) | 99/158 (63%) | 11/65 (17%) | 20/76 (26%) |
| self-check (checking oneself) | unclear | `自检` | 18/152 (12%) | 8/81 (10%) | 24/138 (17%) | 7/158 (4%) | 7/65 (11%) | 7/76 (9%) |
| reflect (reflecting on one's own act) | unclear | `反思`, `␣reflection` | 3/152 (2%) | 2/81 (2%) | 8/138 (6%) | 0/158 (0%) | 2/65 (3%) | 2/76 (3%) |
| clarify (clarifying, setting the record straight) | unclear | `澄清` | 1/152 (1%) | 2/81 (2%) | 0/138 (0%) | 0/158 (0%) | 1/65 (2%) | 2/76 (3%) |
| true (true, real) | truth | `true` | 1/152 (1%) | 2/81 (2%) | 0/138 (0%) | 6/158 (4%) | 1/65 (2%) | 1/76 (1%) |
| silent (staying silent) | unclear | `沉默` | 1/152 (1%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 1/65 (2%) | 0/76 (0%) |

Not in the draft: truth (excluded: truth from the question on); deny (excluded: admit / deny / acknowledge); admit (excluded: admit / deny / acknowledge)
