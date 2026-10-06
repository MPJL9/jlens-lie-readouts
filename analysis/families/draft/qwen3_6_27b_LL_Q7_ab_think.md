# Draft families: qwen3.6-27b, logit lens, part Q7_ab, group think

Written by `scripts/apply_family_decisions.py` (2026-10-01; draft, not frozen). Counts are `present / transcripts (share)`
on the build split.

## think_slot0

| family | side | members | lies | truths | no-pressure truths | unrelated | lies that deny | truths that deny |
|---|---|---|---|---|---|---|---|---|
| toward good (turning toward goodness) | unclear | `向善` | 149/152 (98%) | 76/81 (94%) | 138/138 (100%) | 43/158 (27%) | 76/79 (96%) | 72/77 (94%) |
| clarify (making the facts clear) | truth | `澄清` | 106/152 (70%) | 58/81 (72%) | 138/138 (100%) | 153/158 (97%) | 53/79 (67%) | 55/77 (71%) |
| clarify (making something clear, setting the record straight) | unclear | `澄清`, `␣clarification` | 106/152 (70%) | 58/81 (72%) | 138/138 (100%) | 156/158 (99%) | 53/79 (67%) | 55/77 (71%) |
| violation (breaking a rule) | unclear | `违规` | 72/152 (47%) | 47/81 (58%) | 3/138 (2%) | 4/158 (3%) | 48/79 (61%) | 46/77 (60%) |
| disclaim responsibility (not bearing any (responsibility)) | unclear | `不承担任何` | 49/152 (32%) | 16/81 (20%) | 0/138 (0%) | 0/158 (0%) | 30/79 (38%) | 15/77 (19%) |
| comply (acting in compliance with rules) | unclear | `合规` | 23/152 (15%) | 14/81 (17%) | 1/138 (1%) | 0/158 (0%) | 17/79 (22%) | 14/77 (18%) |
| plausible (seeming believable) | unclear | `␣plausible` | 30/152 (20%) | 7/81 (9%) | 0/138 (0%) | 0/158 (0%) | 16/79 (20%) | 7/77 (9%) |
| fairness (being fair / just) | unclear | `公道` | 17/152 (11%) | 10/81 (12%) | 6/138 (4%) | 5/158 (3%) | 6/79 (8%) | 9/77 (12%) |
| offend / commit wrongdoing (committing an offence) | unclear | `犯的`, `犯了` | 8/152 (5%) | 1/81 (1%) | 2/138 (1%) | 0/158 (0%) | 3/79 (4%) | 1/77 (1%) |
| hide (hiding something) | lie | `藏`, `掩` | 8/152 (5%) | 1/81 (1%) | 0/138 (0%) | 8/158 (5%) | 2/79 (3%) | 1/77 (1%) |
| bad (bad, wrongdoer) | unclear | `坏`, `坏人` | 8/152 (5%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 2/79 (3%) | 0/77 (0%) |
| true feelings (genuine feelings / the real situation) | truth | `真情` | 1/152 (1%) | 3/81 (4%) | 6/138 (4%) | 94/158 (59%) | 1/79 (1%) | 3/77 (4%) |
| fact (fact, factual) | truth | `与现实` | 3/152 (2%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 1/79 (1%) | 1/77 (1%) |
| wrong (wrong, mistaken) | lie | `指正` | 2/152 (1%) | 0/81 (0%) | 10/138 (7%) | 15/158 (9%) | 1/79 (1%) | 0/77 (0%) |
| conscience (moral conscience) | truth | `良心` | 1/152 (1%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 0/79 (0%) | 0/77 (0%) |
| righteousness (moral righteousness) | unclear | `大义` | 0/152 (0%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 0/79 (0%) | 1/77 (1%) |

Not in the draft: obscure / against conscience (held back: no undisputed member left); doubt (held back: no undisputed member left); truth (excluded: the question's own word)

## think_slot1

| family | side | members | lies | truths | no-pressure truths | unrelated | lies that deny | truths that deny |
|---|---|---|---|---|---|---|---|---|
| secretly (doing something covertly) | lie | `暗中`, `悄悄地`, `悄` | 49/152 (32%) | 22/81 (27%) | 129/138 (93%) | 157/158 (99%) | 18/79 (23%) | 19/77 (25%) |
| unauthorized (without permission) | unclear | `未经允许` | 18/152 (12%) | 25/81 (31%) | 7/138 (5%) | 1/158 (1%) | 9/79 (11%) | 24/77 (31%) |
| neutrality (taking no side) | unclear | `␣neutrality` | 35/152 (23%) | 8/81 (10%) | 0/138 (0%) | 0/158 (0%) | 20/79 (25%) | 8/77 (10%) |
| objective (objective) | unclear | `␣objective` | 15/152 (10%) | 9/81 (11%) | 0/138 (0%) | 0/158 (0%) | 6/79 (8%) | 8/77 (10%) |
| mistake (an error the speaker made) | unclear | `␣mistaken`, `␣mistakes` | 8/152 (5%) | 9/81 (11%) | 26/138 (19%) | 39/158 (25%) | 2/79 (3%) | 9/77 (12%) |
| wrong (wrong, mistaken) | lie | `_WRONG`, `指正`, `的错误` | 9/152 (6%) | 8/81 (10%) | 17/138 (12%) | 28/158 (18%) | 6/79 (8%) | 8/77 (10%) |
| false (false, untrue) | lie | `真假` | 7/152 (5%) | 4/81 (5%) | 0/138 (0%) | 0/158 (0%) | 4/79 (5%) | 4/77 (5%) |
| no regret (without regret) | unclear | `无怨无悔` | 2/152 (1%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 0/79 (0%) | 1/77 (1%) |
| deceive (the act of deceiving) | lie | `欺` | 0/152 (0%) | 0/81 (0%) | 0/138 (0%) | 12/158 (8%) | 0/79 (0%) | 0/77 (0%) |

Not in the draft: leak / omit (held back: no undisputed member left); doubt / suspicion (held back: no undisputed member left); clarify (held back: no undisputed member left); obscure / against conscience (held back: no undisputed member left)

## think_slot2

| family | side | members | lies | truths | no-pressure truths | unrelated | lies that deny | truths that deny |
|---|---|---|---|---|---|---|---|---|
| ethics (ethics / morality) | unclear | `␣ethics`, `␣ethic`, `␣ethical`, `思想道德` | 118/152 (78%) | 52/81 (64%) | 11/138 (8%) | 48/158 (30%) | 53/79 (67%) | 49/77 (64%) |
| guard against (to abstain / guard against / admonish) | unclear | `戒` | 45/152 (30%) | 36/81 (44%) | 0/138 (0%) | 0/158 (0%) | 33/79 (42%) | 36/77 (47%) |
| violate (violating a rule or law) | unclear | `触犯` | 42/152 (28%) | 31/81 (38%) | 22/138 (16%) | 17/158 (11%) | 20/79 (25%) | 30/77 (39%) |
| retract (withdrawing a statement) | unclear | `撤回` | 48/152 (32%) | 20/81 (25%) | 3/138 (2%) | 0/158 (0%) | 15/79 (19%) | 17/77 (22%) |
| sin / evil (sin, evil deed) | unclear | `孽` | 38/152 (25%) | 16/81 (20%) | 3/138 (2%) | 0/158 (0%) | 26/79 (33%) | 15/77 (19%) |
| non-fulfilment (failing to fulfil an obligation) | unclear | `不履行` | 27/152 (18%) | 12/81 (15%) | 0/138 (0%) | 0/158 (0%) | 19/79 (24%) | 12/77 (16%) |
| secretly (doing something covertly) | lie | `悄悄的` | 27/152 (18%) | 10/81 (12%) | 0/138 (0%) | 0/158 (0%) | 13/79 (16%) | 9/77 (12%) |
| disguised (in disguised form) | lie | `变相` | 25/152 (16%) | 6/81 (7%) | 33/138 (24%) | 5/158 (3%) | 7/79 (9%) | 3/77 (4%) |
| upright (upright, of integrity) | truth | `正直`, `端正` | 18/152 (12%) | 11/81 (14%) | 0/138 (0%) | 0/158 (0%) | 14/79 (18%) | 10/77 (13%) |
| cover up (covering or obscuring (蒙蔽, 遮蔽)) | lie | `藏` | 17/152 (11%) | 5/81 (6%) | 0/138 (0%) | 1/158 (1%) | 10/79 (13%) | 5/77 (6%) |
| forbidden (forbidden) | unclear | `bidden` | 17/152 (11%) | 2/81 (2%) | 0/138 (0%) | 0/158 (0%) | 14/79 (18%) | 2/77 (3%) |
| conscience (moral conscience) | unclear | `␣conscience` | 11/152 (7%) | 2/81 (2%) | 0/138 (0%) | 0/158 (0%) | 7/79 (9%) | 2/77 (3%) |
| bad (bad, wrongdoer) | unclear | `坏人` | 6/152 (4%) | 2/81 (2%) | 0/138 (0%) | 0/158 (0%) | 3/79 (4%) | 2/77 (3%) |
| false (false, untrue) | lie | `_false`, `.FALSE` | 3/152 (2%) | 3/81 (4%) | 0/138 (0%) | 8/158 (5%) | 2/79 (3%) | 3/77 (4%) |
| responsible (being responsible) | unclear | `负责任` | 5/152 (3%) | 0/81 (0%) | 0/138 (0%) | 1/158 (1%) | 5/79 (6%) | 0/77 (0%) |
| reveal (exposing what is hidden) | truth | `外露` | 3/152 (2%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 0/79 (0%) | 0/77 (0%) |
| ethical (morally right) | unclear | `␣ethical` | 2/152 (1%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 2/79 (3%) | 1/77 (1%) |
| hide (hiding something) | lie | `隱藏版` | 2/152 (1%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 0/79 (0%) | 0/77 (0%) |
| refuse (refusing) | unclear | `拒` | 1/152 (1%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 1/79 (1%) | 1/77 (1%) |
| apology (saying sorry) | unclear | `抱歉` | 1/152 (1%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 1/79 (1%) | 1/77 (1%) |
| clarify (making the facts clear) | truth | `澄清` | 1/152 (1%) | 0/81 (0%) | 0/138 (0%) | 1/158 (1%) | 1/79 (1%) | 0/77 (0%) |
| secret (confidential, secret) | lie | `机密` | 1/152 (1%) | 0/81 (0%) | 0/138 (0%) | 2/158 (1%) | 1/79 (1%) | 0/77 (0%) |
| deceive (the act of deceiving) | lie | `欺` | 0/152 (0%) | 0/81 (0%) | 0/138 (0%) | 30/158 (19%) | 0/79 (0%) | 0/77 (0%) |

Not in the draft: candid (held back: no undisputed member left); sincere (excluded: the question's own word); silence (held back: no undisputed member left); obscure / against conscience (held back: no undisputed member left)

## think_slot3

| family | side | members | lies | truths | no-pressure truths | unrelated | lies that deny | truths that deny |
|---|---|---|---|---|---|---|---|---|
| false (false, untrue) | lie | `␣false`, `␣False`, `false`, `False`, `_false`, `/false`, `假`, `假的` | 151/152 (99%) | 75/81 (93%) | 138/138 (100%) | 150/158 (95%) | 79/79 (100%) | 71/77 (92%) |
| avoid / exempt (免: to avoid or be exempted) | unclear | `免`, `免除` | 144/152 (95%) | 74/81 (91%) | 125/138 (91%) | 124/158 (78%) | 75/79 (95%) | 70/77 (91%) |
| direct / head-on (正面: facing directly (正面回答 = answer directly) or positive) | unclear | `正面` | 124/152 (82%) | 60/81 (74%) | 69/138 (50%) | 51/158 (32%) | 62/79 (78%) | 58/77 (75%) |
| correct (correct) | truth | `␣correct`, `正确` | 46/152 (30%) | 47/81 (58%) | 105/138 (76%) | 3/158 (2%) | 8/79 (10%) | 43/77 (56%) |
| deceive / hoodwink (蒙: to deceive or cover (蒙骗, 蒙蔽)) | lie | `哄` | 46/152 (30%) | 0/81 (0%) | 0/138 (0%) | 13/158 (8%) | 13/79 (16%) | 0/77 (0%) |
| guard against (to abstain / guard against / admonish) | unclear | `戒` | 17/152 (11%) | 16/81 (20%) | 11/138 (8%) | 32/158 (20%) | 6/79 (8%) | 12/77 (16%) |
| self-respect (self-respect / conduct oneself properly) | unclear | `自重` | 7/152 (5%) | 19/81 (23%) | 39/138 (28%) | 13/158 (8%) | 5/79 (6%) | 19/77 (25%) |
| true (true, real) | truth | `␣true`, `True`, `真`, `属实` | 4/152 (3%) | 15/81 (19%) | 9/138 (7%) | 14/158 (9%) | 1/79 (1%) | 14/77 (18%) |
| public / disclose (making public) | truth | `公开` | 12/152 (8%) | 4/81 (5%) | 0/138 (0%) | 0/158 (0%) | 10/79 (13%) | 4/77 (5%) |
| secretly (privately / covertly) | lie | `私下` | 16/152 (11%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 11/79 (14%) | 0/77 (0%) |
| refuse (refusal) | unclear | `␣refusal` | 5/152 (3%) | 4/81 (5%) | 0/138 (0%) | 0/158 (0%) | 3/79 (4%) | 4/77 (5%) |
| apology (saying sorry) | unclear | `抱歉`, `对不起`, `Sorry` | 5/152 (3%) | 2/81 (2%) | 0/138 (0%) | 0/158 (0%) | 3/79 (4%) | 1/77 (1%) |
| upright (upright, of integrity) | truth | `正直` | 0/152 (0%) | 4/81 (5%) | 0/138 (0%) | 0/158 (0%) | 0/79 (0%) | 4/77 (5%) |
| reveal (exposing) | truth | `露` | 0/152 (0%) | 2/81 (2%) | 0/138 (0%) | 0/158 (0%) | 0/79 (0%) | 2/77 (3%) |
| accurate (accurate) | truth | `准确` | 1/152 (1%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 1/79 (1%) | 1/77 (1%) |
| incorrect (incorrect) | lie | `不符合` | 1/152 (1%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 1/79 (1%) | 1/77 (1%) |
| secret (a secret) | lie | `秘密` | 1/152 (1%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 0/79 (0%) | 0/77 (0%) |
| hide (hidden) | lie | `:hidden` | 1/152 (1%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 0/79 (0%) | 0/77 (0%) |
| violate (going against a rule) | unclear | `违背`, `违反了` | 0/152 (0%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 0/79 (0%) | 1/77 (1%) |
| silence (keeping silent) | unclear | `沉默` | 1/152 (1%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 1/79 (1%) | 0/77 (0%) |
| fact (fact, factual) | truth | `实际上` | 0/152 (0%) | 0/81 (0%) | 0/138 (0%) | 1/158 (1%) | 0/79 (0%) | 0/77 (0%) |

Not in the draft: cover up (held back: no undisputed member left); coax / fool (held back: no undisputed member left); candid (held back: no undisputed member left); trust / credibility (held back: no undisputed member left); obscure / against conscience (held back: no undisputed member left)
