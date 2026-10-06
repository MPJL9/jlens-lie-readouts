# Draft families: qwen3.6-27b, logit lens, part Q2_after, group questiona

Written by `scripts/apply_family_decisions.py` (2026-10-01; draft, not frozen). Counts are `present / transcripts (share)`
on the build split.

## q_tok0

| family | side | members | lies | truths | no-pressure truths | unrelated | lies that deny | truths that deny |
|---|---|---|---|---|---|---|---|---|
| true (true, real) | truth | `真的`, `确实`, `的真` | 50/152 (33%) | 18/81 (22%) | 14/138 (10%) | 1/158 (1%) | 15/47 (32%) | 18/77 (23%) |
| deliberate (done on purpose) | unclear | `␣intentional`, `␣deliberate`, `␣intentionally` | 20/152 (13%) | 20/81 (25%) | 19/138 (14%) | 2/158 (1%) | 11/47 (23%) | 20/77 (26%) |
| wrong (wrong, mistaken) | lie | `错`, `误会` | 2/152 (1%) | 3/81 (4%) | 11/138 (8%) | 1/158 (1%) | 2/47 (4%) | 3/77 (4%) |
| informed (being in the know (知情)) | unclear | `知情` | 3/152 (2%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 1/47 (2%) | 1/77 (1%) |
| omit (leaving something out (漏, 遗漏)) | unclear | `遗漏` | 1/152 (1%) | 1/81 (1%) | 1/138 (1%) | 6/158 (4%) | 0/47 (0%) | 1/77 (1%) |
| intention (an aim or intention) | unclear | `␣intention` | 0/152 (0%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 0/47 (0%) | 1/77 (1%) |
| knowingly (acting with knowledge of the facts) | unclear | `␣knowingly` | 0/152 (0%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 0/47 (0%) | 1/77 (1%) |
| truthful (telling the truth) | truth | `␣truthful` | 1/152 (1%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 0/47 (0%) | 0/77 (0%) |
| correct (correct) | truth | `正确`, `的正确` | 0/152 (0%) | 0/81 (0%) | 0/138 (0%) | 1/158 (1%) | 0/47 (0%) | 0/77 (0%) |
| fact (fact, factual) | truth | `符合` | 0/152 (0%) | 0/81 (0%) | 1/138 (1%) | 0/158 (0%) | 0/47 (0%) | 0/77 (0%) |

Not in the draft: truth (excluded: truth from the question on)

## q_tok1

| family | side | members | lies | truths | no-pressure truths | unrelated | lies that deny | truths that deny |
|---|---|---|---|---|---|---|---|---|
| intention (an aim or intention) | unclear | `␣intention`, `初衷`, `␣intentions`, `␣intent`, `意图` | 20/152 (13%) | 18/81 (22%) | 6/138 (4%) | 0/158 (0%) | 6/47 (13%) | 18/77 (23%) |
| official line (an agreed line or talking points (口径)) | unclear | `口径` | 25/152 (16%) | 3/81 (4%) | 2/138 (1%) | 0/158 (0%) | 10/47 (21%) | 3/77 (4%) |
| self-check (checking oneself (自查)) | unclear | `自查` | 9/152 (6%) | 1/81 (1%) | 2/138 (1%) | 0/158 (0%) | 5/47 (11%) | 1/77 (1%) |
| refuse (refusing) | unclear | `␣refusal`, `拒绝` | 2/152 (1%) | 6/81 (7%) | 2/138 (1%) | 0/158 (0%) | 1/47 (2%) | 6/77 (8%) |
| honest (honest, honesty) | truth | `␣honesty`, `␣honest`, `诚实` | 1/152 (1%) | 7/81 (9%) | 1/138 (1%) | 0/158 (0%) | 0/47 (0%) | 7/77 (9%) |
| comply (following rules, compliance) | unclear | `合规`, `␣compliance` | 4/152 (3%) | 4/81 (5%) | 3/138 (2%) | 0/158 (0%) | 3/47 (6%) | 4/77 (5%) |
| hesitation (hesitating) | unclear | `␣hesitation` | 0/152 (0%) | 7/81 (9%) | 0/138 (0%) | 0/158 (0%) | 0/47 (0%) | 7/77 (9%) |
| strategy (a strategy or tactic) | unclear | `策略`, `␣strategy` | 6/152 (4%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 4/47 (9%) | 1/77 (1%) |
| integrity (integrity, trustworthiness) | truth | `诚信`, `␣integrity` | 4/152 (3%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 0/47 (0%) | 1/77 (1%) |
| objective (objective, unbiased) | truth | `客观` | 5/152 (3%) | 0/81 (0%) | 1/138 (1%) | 0/158 (0%) | 1/47 (2%) | 0/77 (0%) |
| candid (frank and open (坦诚)) | truth | `坦诚` | 1/152 (1%) | 3/81 (4%) | 0/138 (0%) | 0/158 (0%) | 0/47 (0%) | 3/77 (4%) |
| truthful (telling the truth, faithfully to the facts) | truth | `如实`, `␣truthful` | 2/152 (1%) | 1/81 (1%) | 1/138 (1%) | 0/158 (0%) | 1/47 (2%) | 1/77 (1%) |
| conceal (hiding the truth) | lie | `隐瞒` | 3/152 (2%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 3/47 (6%) | 0/77 (0%) |
| confidential (keeping something confidential (保密)) | lie | `保密` | 1/152 (1%) | 2/81 (2%) | 0/138 (0%) | 0/158 (0%) | 0/47 (0%) | 2/77 (3%) |
| perfunctory (brushing off, answering perfunctorily (敷衍)) | unclear | `敷衍` | 3/152 (2%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 1/47 (2%) | 0/77 (0%) |
| false (false, untrue) | lie | `␣fals`, `假` | 2/152 (1%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 0/47 (0%) | 1/77 (1%) |
| wrong (wrong, mistaken) | lie | `␣mistake`, `失误` | 2/152 (1%) | 0/81 (0%) | 4/138 (3%) | 0/158 (0%) | 0/47 (0%) | 0/77 (0%) |
| true (true, real) | truth | `真`, `确实` | 2/152 (1%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 1/47 (2%) | 0/77 (0%) |
| transparent (transparent, open) | truth | `␣transparency` | 1/152 (1%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 1/47 (2%) | 0/77 (0%) |
| fraud (swindle, fraud) | lie | `诈` | 1/152 (1%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 0/47 (0%) | 0/77 (0%) |
| purpose (the purpose of the act) | unclear | `目的是` | 0/152 (0%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 0/47 (0%) | 1/77 (1%) |
| scripted (pre-written, rehearsed) | unclear | `␣rehearsal` | 0/152 (0%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 0/47 (0%) | 0/77 (0%) |
| fact (fact, factual) | truth | `␣fact`, `␣facts`, `␣Fact`, `␣factual`, `实际情况` | 1/152 (1%) | 0/81 (0%) | 2/138 (1%) | 0/158 (0%) | 0/47 (0%) | 0/77 (0%) |
| correct (correct) | truth | `␣correction`, `␣corrected`, `␣corrections`, `纠正` | 0/152 (0%) | 0/81 (0%) | 0/138 (0%) | 2/158 (1%) | 0/47 (0%) | 0/77 (0%) |
| accurate (accurate) | truth | `准确` | 0/152 (0%) | 0/81 (0%) | 1/138 (1%) | 1/158 (1%) | 0/47 (0%) | 0/77 (0%) |

Not in the draft: admit (excluded: admit / deny / acknowledge); deny (excluded: admit / deny / acknowledge); violate (held back: no undisputed member left)

## q_tok2

| family | side | members | lies | truths | no-pressure truths | unrelated | lies that deny | truths that deny |
|---|---|---|---|---|---|---|---|---|
| incorrect (incorrect) | lie | `␣incorrect` | 18/152 (12%) | 22/81 (27%) | 102/138 (74%) | 49/158 (31%) | 5/47 (11%) | 20/77 (26%) |
| refuse (refusing) | unclear | `␣refusal`, `拒绝` | 1/152 (1%) | 12/81 (15%) | 0/138 (0%) | 0/158 (0%) | 1/47 (2%) | 12/77 (16%) |
| official line (an agreed line or talking points (口径)) | unclear | `口径` | 5/152 (3%) | 2/81 (2%) | 0/138 (0%) | 0/158 (0%) | 3/47 (6%) | 2/77 (3%) |
| contradictory (self-contradictory) | unclear | `␣contradictory` | 2/152 (1%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 2/47 (4%) | 1/77 (1%) |
| fact (fact, factual) | truth | `符合`, `与现实` | 1/152 (1%) | 2/81 (2%) | 0/138 (0%) | 1/158 (1%) | 0/47 (0%) | 2/77 (3%) |
| comply (following rules, compliance) | unclear | `遵守` | 0/152 (0%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 0/47 (0%) | 1/77 (1%) |
| strategy (a strategy or tactic) | unclear | `␣strategy` | 1/152 (1%) | 0/81 (0%) | 2/138 (1%) | 0/158 (0%) | 1/47 (2%) | 0/77 (0%) |
| correct (correct) | truth | `␣correct`, `正确` | 0/152 (0%) | 0/81 (0%) | 0/138 (0%) | 1/158 (1%) | 0/47 (0%) | 0/77 (0%) |
| true (true, real) | truth | `确实` | 0/152 (0%) | 0/81 (0%) | 1/138 (1%) | 0/158 (0%) | 0/47 (0%) | 0/77 (0%) |

Not in the draft: admit (excluded: admit / deny / acknowledge)

## q_tok3

| family | side | members | lies | truths | no-pressure truths | unrelated | lies that deny | truths that deny |
|---|---|---|---|---|---|---|---|---|
| accurate (accurate) | truth | `␣accur`, `␣accurate`, `␣accuracy`, `␣accurately`, `accur`, `准确`, `准确的` | 134/152 (88%) | 69/81 (85%) | 138/138 (100%) | 156/158 (99%) | 43/47 (91%) | 66/77 (86%) |
| truthful (telling the truth, faithfully to the facts) | truth | `␣truthful`, `如实` | 139/152 (91%) | 60/81 (74%) | 126/138 (91%) | 22/158 (14%) | 44/47 (94%) | 58/77 (75%) |
| helpful (helpful) | unclear | `␣helpful`, `␣Helpful`, `有帮助` | 99/152 (65%) | 58/81 (72%) | 111/138 (80%) | 155/158 (98%) | 14/47 (30%) | 54/77 (70%) |
| comply (following rules, compliance, adherence) | unclear | `␣compliant`, `␣adher`, `合规`, `遵守`, `遵循`, `␣adherence`, `␣comply`, `␣compliance`, `␣complying`, `␣conform`, `␣adhere`, `依法依规`, `遵` | 97/152 (64%) | 56/81 (69%) | 51/138 (37%) | 122/158 (77%) | 16/47 (34%) | 52/77 (68%) |
| aligned (consistent with, in line with) | unclear | `␣aligned`, `符合`, `是否符合`, `␣align`, `␣alignment` | 89/152 (59%) | 56/81 (69%) | 72/138 (52%) | 58/158 (37%) | 9/47 (19%) | 52/77 (68%) |
| strategy (a strategy or tactic) | unclear | `策略`, `␣strategy`, `␣Strategy`, `␣strategically`, `的策略` | 92/152 (61%) | 32/81 (40%) | 1/138 (1%) | 0/158 (0%) | 22/47 (47%) | 29/77 (38%) |
| honest (honest, honesty) | truth | `␣honest`, `␣honestly`, `诚实`, `␣honesty`, `诚` | 87/152 (57%) | 36/81 (44%) | 16/138 (12%) | 5/158 (3%) | 33/47 (70%) | 34/77 (44%) |
| fact (fact, factual) | truth | `␣fact`, `Fact`, `␣Fact`, `␣factual`, `事实`, `实际上`, `的事实` | 86/152 (57%) | 27/81 (33%) | 126/138 (91%) | 75/158 (47%) | 36/47 (77%) | 26/77 (34%) |
| appropriate (appropriate, suitable) | unclear | `␣appropriate`, `合适`, `␣suitable`, `␣appropriately` | 77/152 (51%) | 32/81 (40%) | 5/138 (4%) | 17/158 (11%) | 8/47 (17%) | 29/77 (38%) |
| correct (correct) | truth | `␣valid`, `␣correct`, `␣Valid`, `␣correctly`, `correct`, `_correct`, `Correct`, `␣Correct`, `␣correctness`, `正确`, `正确的`, `正确答案`, `的正确`, `是正确的`, `正确地`, `是否正确` | 36/152 (24%) | 36/81 (44%) | 136/138 (99%) | 155/158 (98%) | 17/47 (36%) | 34/77 (44%) |
| perfunctory (brushing off, answering perfunctorily (敷衍)) | unclear | `敷衍` | 55/152 (36%) | 15/81 (19%) | 9/138 (7%) | 4/158 (3%) | 34/47 (72%) | 15/77 (19%) |
| crafted (shaped or tailored for an effect) | unclear | `␣crafted`, `␣tailored` | 45/152 (30%) | 19/81 (23%) | 2/138 (1%) | 2/158 (1%) | 15/47 (32%) | 19/77 (25%) |
| influenced (influenced by something) | unclear | `␣influenced` | 18/152 (12%) | 26/81 (32%) | 41/138 (30%) | 20/158 (13%) | 8/47 (17%) | 26/77 (34%) |
| biased (biased, slanted) | unclear | `␣biased`, `␣bias` | 22/152 (14%) | 16/81 (20%) | 19/138 (14%) | 47/158 (30%) | 5/47 (11%) | 15/77 (19%) |
| intention (an aim or intention) | unclear | `␣intended` | 14/152 (9%) | 23/81 (28%) | 5/138 (4%) | 2/158 (1%) | 8/47 (17%) | 22/77 (29%) |
| lie (lying, a lie) | lie | `␣lying`, `谎言`, `␣lies`, `说谎`, `撒谎`, `谎`, `␣거짓`, `␣lie` | 28/152 (18%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 16/47 (34%) | 0/77 (0%) |
| ethical (ethical) | unclear | `␣ethical`, `伦理`, `␣morally` | 19/152 (12%) | 9/81 (11%) | 0/138 (0%) | 0/158 (0%) | 0/47 (0%) | 9/77 (12%) |
| true (true, real) | truth | `␣true`, `␣True`, `␣TRUE`, `␣genuine`, `␣genuinely`, `真的`, `真实`, `真实的`, `的真`, `的真实`, `的真实性` | 19/152 (12%) | 6/81 (7%) | 10/138 (7%) | 3/158 (2%) | 10/47 (21%) | 6/77 (8%) |
| tailored (tailored to the listener) | unclear | `␣tailored` | 18/152 (12%) | 6/81 (7%) | 0/138 (0%) | 2/158 (1%) | 3/47 (6%) | 6/77 (8%) |
| incorrect (incorrect) | lie | `␣incorrect`, `␣inaccurate`, `␣Incorrect`, `有误` | 11/152 (7%) | 7/81 (9%) | 21/138 (15%) | 22/158 (14%) | 9/47 (19%) | 7/77 (9%) |
| violate (breaking a rule) | unclear | `违规`, `违反`, `␣violate`, `␣violating` | 8/152 (5%) | 8/81 (10%) | 0/138 (0%) | 0/158 (0%) | 1/47 (2%) | 7/77 (9%) |
| scripted (pre-written, canned) | unclear | `␣canned`, `␣scripted` | 12/152 (8%) | 2/81 (2%) | 0/138 (0%) | 0/158 (0%) | 8/47 (17%) | 2/77 (3%) |
| refuse (refusing) | unclear | `␣refusal`, `拒绝`, `␣refus` | 0/152 (0%) | 13/81 (16%) | 0/138 (0%) | 0/158 (0%) | 0/47 (0%) | 12/77 (16%) |
| dishonest (not honest) | lie | `␣dishonest` | 10/152 (7%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 2/47 (4%) | 0/77 (0%) |
| neutral (neutral) | unclear | `中立` | 1/152 (1%) | 8/81 (10%) | 5/138 (4%) | 1/158 (1%) | 1/47 (2%) | 8/77 (10%) |
| false (false, untrue) | lie | `␣false`, `假`, `虚假`, `假的`, `虚假信息` | 9/152 (6%) | 0/81 (0%) | 1/138 (1%) | 1/158 (1%) | 6/47 (13%) | 0/77 (0%) |
| fabricate (making something up) | lie | `␣fabricated`, `虚构` | 7/152 (5%) | 0/81 (0%) | 2/138 (1%) | 0/158 (0%) | 5/47 (11%) | 0/77 (0%) |
| moral (morally) | unclear | `␣morally` | 4/152 (3%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 0/47 (0%) | 1/77 (1%) |
| evade (evading or dodging) | lie | `␣evasion`, `回避`, `␣dodge`, `规避` | 3/152 (2%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 3/47 (6%) | 1/77 (1%) |
| deliberate (done on purpose) | unclear | `␣intentionally`, `␣intentional`, `故意` | 1/152 (1%) | 3/81 (4%) | 1/138 (1%) | 0/158 (0%) | 1/47 (2%) | 2/77 (3%) |
| hallucinate (hallucinating content) | unclear | `␣halluc` | 2/152 (1%) | 1/81 (1%) | 9/138 (7%) | 10/158 (6%) | 0/47 (0%) | 1/77 (1%) |
| objective (objective, unbiased) | truth | `客观` | 1/152 (1%) | 2/81 (2%) | 2/138 (1%) | 2/158 (1%) | 1/47 (2%) | 1/77 (1%) |
| official line (an agreed official line of messaging (口径)) | unclear | `口径` | 2/152 (1%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 0/47 (0%) | 1/77 (1%) |
| sincere (sincere) | truth | `␣sincere` | 2/152 (1%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 1/47 (2%) | 0/77 (0%) |
| disguise (covering up or disguising (掩饰)) | lie | `掩饰` | 2/152 (1%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 1/47 (2%) | 0/77 (0%) |
| not aligned (not in line with (不符合)) | unclear | `不符合` | 0/152 (0%) | 2/81 (2%) | 0/138 (0%) | 1/158 (1%) | 0/47 (0%) | 1/77 (1%) |
| euphemistic (tactful, euphemistic (委婉)) | unclear | `委婉` | 1/152 (1%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 0/47 (0%) | 0/77 (0%) |
| wrong (wrong, mistaken) | lie | `␣error`, `␣wrong`, `错`, `错误`, `错了`, `是错误的` | 0/152 (0%) | 1/81 (1%) | 2/138 (1%) | 4/158 (3%) | 0/47 (0%) | 1/77 (1%) |

Not in the draft: truth (excluded: truth from the question on); deny (excluded: admit / deny / acknowledge); admit (excluded: admit / deny / acknowledge)

## q_tok4

| family | side | members | lies | truths | no-pressure truths | unrelated | lies that deny | truths that deny |
|---|---|---|---|---|---|---|---|---|
| mislead (misleading) | lie | `␣misleading`, `误导`, `␣misled` | 152/152 (100%) | 81/81 (100%) | 138/138 (100%) | 158/158 (100%) | 47/47 (100%) | 77/77 (100%) |
| false (false, untrue) | lie | `␣false`, `␣False`, `false`, `=False`, `=false`, `:false`, `>false`, `␣fals`, `␣untrue`, `/false`, `␣falsehood`, `假`, `虚假`, `虚假信息` | 152/152 (100%) | 81/81 (100%) | 138/138 (100%) | 158/158 (100%) | 47/47 (100%) | 77/77 (100%) |
| conceal (hiding the truth) | lie | `隐瞒`, `␣conceal`, `␣hiding`, `␣masking`, `掩饰`, `␣mask`, `遮` | 148/152 (97%) | 80/81 (99%) | 132/138 (96%) | 106/158 (67%) | 47/47 (100%) | 76/77 (99%) |
| dishonest (not honest) | lie | `␣dishonest` | 151/152 (99%) | 74/81 (91%) | 135/138 (98%) | 157/158 (99%) | 47/47 (100%) | 70/77 (91%) |
| deliberate (done on purpose) | unclear | `故意`, `␣intentionally`, `␣deliberately`, `␣intentional`, `有意`, `刻意`, `故意的`, `␣deliberate` | 152/152 (100%) | 69/81 (85%) | 138/138 (100%) | 156/158 (99%) | 47/47 (100%) | 65/77 (84%) |
| lie (lying, a lie) | lie | `␣lying`, `谎言`, `说谎`, `撒谎`, `␣lies`, `谎`, `␣lie`, `␣거짓` | 152/152 (100%) | 54/81 (67%) | 16/138 (12%) | 101/158 (64%) | 47/47 (100%) | 51/77 (66%) |
| fake (fake) | lie | `fake`, `␣fake` | 140/152 (92%) | 51/81 (63%) | 129/138 (93%) | 158/158 (100%) | 41/47 (87%) | 49/77 (64%) |
| intention (an aim or intention) | unclear | `␣intent`, `意图`, `␣Intent`, `␣intended`, `␣intend`, `Intent`, `␣intentions`, `intent` | 103/152 (68%) | 60/81 (74%) | 115/138 (83%) | 38/158 (24%) | 41/47 (87%) | 57/77 (74%) |
| withhold (holding information back) | lie | `␣withholding`, `␣withheld`, `␣withhold` | 101/152 (66%) | 48/81 (59%) | 29/138 (21%) | 0/158 (0%) | 28/47 (60%) | 45/77 (58%) |
| manipulate (manipulating) | lie | `␣manip`, `␣manipulation`, `Manip`, `␣Manip`, `␣manipulated`, `诱导` | 81/152 (53%) | 65/81 (80%) | 116/138 (84%) | 140/158 (89%) | 25/47 (53%) | 63/77 (82%) |
| integrity (integrity, trustworthiness) | truth | `诚信` | 104/152 (68%) | 41/81 (51%) | 5/138 (4%) | 0/158 (0%) | 25/47 (53%) | 38/77 (49%) |
| omit (leaving something out) | lie | `␣omission`, `␣omit`, `␣omitted`, `省略` | 51/152 (34%) | 48/81 (59%) | 14/138 (10%) | 0/158 (0%) | 21/47 (45%) | 47/77 (61%) |
| truthful (telling the truth, faithfully to the facts) | truth | `␣truthful`, `如实` | 69/152 (45%) | 9/81 (11%) | 34/138 (25%) | 2/158 (1%) | 16/47 (34%) | 8/77 (10%) |
| honest (honest, honesty) | truth | `诚实`, `␣honest`, `␣honesty` | 70/152 (46%) | 6/81 (7%) | 0/138 (0%) | 0/158 (0%) | 17/47 (36%) | 5/77 (6%) |
| knowingly (acting with knowledge of the facts (明知)) | unclear | `明知` | 30/152 (20%) | 5/81 (6%) | 0/138 (0%) | 0/158 (0%) | 14/47 (30%) | 5/77 (6%) |
| disclose (disclosing information (信息披露)) | truth | `信息披露` | 24/152 (16%) | 10/81 (12%) | 0/138 (0%) | 0/158 (0%) | 10/47 (21%) | 10/77 (13%) |
| strategy (a strategy or tactic) | unclear | `␣tactics`, `␣strategy`, `策略` | 8/152 (5%) | 22/81 (27%) | 0/138 (0%) | 0/158 (0%) | 2/47 (4%) | 21/77 (27%) |
| true (true, real) | truth | `␣true`, `真实`, `真实的`, `是真的` | 27/152 (18%) | 2/81 (2%) | 0/138 (0%) | 0/158 (0%) | 4/47 (9%) | 1/77 (1%) |
| framing (framing a message) | unclear | `␣framing` | 6/152 (4%) | 12/81 (15%) | 7/138 (5%) | 0/158 (0%) | 2/47 (4%) | 12/77 (16%) |
| disguise (masking, disguising, covering up) | lie | `␣masking`, `␣mask`, `掩饰`, `伪装` | 12/152 (8%) | 5/81 (6%) | 0/138 (0%) | 0/158 (0%) | 2/47 (4%) | 5/77 (6%) |
| indirect (indirect) | unclear | `间接`, `␣indirect` | 0/152 (0%) | 15/81 (19%) | 3/138 (2%) | 0/158 (0%) | 0/47 (0%) | 15/77 (19%) |
| fraud (fraud, swindle) | lie | `␣fraudulent`, `␣fraud` | 11/152 (7%) | 0/81 (0%) | 0/138 (0%) | 4/158 (3%) | 3/47 (6%) | 0/77 (0%) |
| purpose (the purpose of the act) | unclear | `␣purpose`, `的目的`, `目的是`, `目的是为了` | 4/152 (3%) | 5/81 (6%) | 2/138 (1%) | 0/158 (0%) | 1/47 (2%) | 4/77 (5%) |
| euphemistic (tactful, euphemistic (委婉)) | unclear | `委婉` | 0/152 (0%) | 9/81 (11%) | 0/138 (0%) | 0/158 (0%) | 0/47 (0%) | 9/77 (12%) |
| transparent (transparent, open) | truth | `-transparent` | 2/152 (1%) | 6/81 (7%) | 1/138 (1%) | 8/158 (5%) | 0/47 (0%) | 6/77 (8%) |
| insinuate (hinting or implying (暗示)) | unclear | `暗示` | 5/152 (3%) | 3/81 (4%) | 6/138 (4%) | 0/158 (0%) | 4/47 (9%) | 3/77 (4%) |
| ethical (ethical) | unclear | `␣ethical`, `␣morally` | 6/152 (4%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 0/47 (0%) | 0/77 (0%) |
| alignment (being aligned (with guidelines)) | unclear | `align` | 2/152 (1%) | 4/81 (5%) | 0/138 (0%) | 0/158 (0%) | 0/47 (0%) | 4/77 (5%) |
| unethical (unethical) | unclear | `␣unethical` | 4/152 (3%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 0/47 (0%) | 0/77 (0%) |
| moral (morally) | unclear | `␣morally` | 4/152 (3%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 0/47 (0%) | 0/77 (0%) |
| disguise (disguising, pretending to be something else) | lie | `伪装` | 0/152 (0%) | 2/81 (2%) | 0/138 (0%) | 0/158 (0%) | 0/47 (0%) | 2/77 (3%) |
| distort (distorting) | lie | `扭曲` | 1/152 (1%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 1/47 (2%) | 0/77 (0%) |
| betray (betraying, selling out (出卖)) | unclear | `出卖` | 0/152 (0%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 0/47 (0%) | 1/77 (1%) |
| informed (being in the know (知情)) | unclear | `知情` | 1/152 (1%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 0/47 (0%) | 0/77 (0%) |
| induce (luring or leading someone on) | lie | `诱导` | 0/152 (0%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 0/47 (0%) | 1/77 (1%) |

Not in the draft: truth (excluded: truth from the question on); deceive (excluded: the question's own word)

## q_tok5

| family | side | members | lies | truths | no-pressure truths | unrelated | lies that deny | truths that deny |
|---|---|---|---|---|---|---|---|---|
| true (true, real) | truth | `␣true`, `true`, `True`, `␣True`, `␣TRUE` | 152/152 (100%) | 81/81 (100%) | 138/138 (100%) | 154/158 (97%) | 47/47 (100%) | 77/77 (100%) |
| honest (honest, honesty) | truth | `诚实`, `␣honest`, `␣honesty`, `␣honestly`, `诚`, `␣Honest` | 140/152 (92%) | 62/81 (77%) | 106/138 (77%) | 143/158 (91%) | 43/47 (91%) | 58/77 (75%) |
| look back (looking back, in retrospect) | unclear | `回顾`, `回顧`, `␣retrospect` | 73/152 (48%) | 60/81 (74%) | 129/138 (93%) | 101/158 (64%) | 15/47 (32%) | 59/77 (77%) |
| ethical (ethical) | unclear | `ethical`, `␣ethical`, `伦理`, `道德` | 101/152 (66%) | 20/81 (25%) | 6/138 (4%) | 0/158 (0%) | 14/47 (30%) | 16/77 (21%) |
| self-reflection (reflecting on one's own conduct (反思)) | unclear | `反思` | 76/152 (50%) | 21/81 (26%) | 39/138 (28%) | 2/158 (1%) | 29/47 (62%) | 20/77 (26%) |
| knowingly (acting with knowledge of the facts (明知)) | unclear | `明知` | 50/152 (33%) | 9/81 (11%) | 0/138 (0%) | 0/158 (0%) | 30/47 (64%) | 9/77 (12%) |
| intention (an aim or intention) | unclear | `意图`, `␣intentions` | 24/152 (16%) | 16/81 (20%) | 5/138 (4%) | 0/158 (0%) | 5/47 (11%) | 16/77 (21%) |
| lie (lying, a lie) | lie | `␣lie`, `␣lies` | 23/152 (15%) | 9/81 (11%) | 4/138 (3%) | 0/158 (0%) | 20/47 (43%) | 9/77 (12%) |
| objective (objective, unbiased) | truth | `客观` | 27/152 (18%) | 5/81 (6%) | 6/138 (4%) | 0/158 (0%) | 6/47 (13%) | 5/77 (6%) |
| false (false, untrue) | lie | `␣false`, `false`, `.assertFalse`, `.False`, `/false` | 0/152 (0%) | 30/81 (37%) | 71/138 (51%) | 121/158 (77%) | 0/47 (0%) | 30/77 (39%) |
| deliberate (done on purpose) | unclear | `故意的` | 6/152 (4%) | 6/81 (7%) | 1/138 (1%) | 2/158 (1%) | 1/47 (2%) | 5/77 (6%) |
| fact (fact, factual) | truth | `是否符合`, `与现实` | 7/152 (5%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 0/47 (0%) | 1/77 (1%) |
| violate (breaking a rule) | unclear | `违反了`, `违反` | 3/152 (2%) | 4/81 (5%) | 0/138 (0%) | 0/158 (0%) | 1/47 (2%) | 3/77 (4%) |
| self-check (checking oneself (自检, 自查)) | unclear | `自检`, `自查` | 4/152 (3%) | 2/81 (2%) | 28/138 (20%) | 88/158 (56%) | 3/47 (6%) | 2/77 (3%) |
| accusation (being accused) | unclear | `␣accusations` | 0/152 (0%) | 6/81 (7%) | 3/138 (2%) | 1/158 (1%) | 0/47 (0%) | 6/77 (8%) |
| innocent (not guilty (无罪)) | unclear | `无罪` | 2/152 (1%) | 2/81 (2%) | 0/138 (0%) | 0/158 (0%) | 0/47 (0%) | 2/77 (3%) |
| confess (owning up (坦白)) | truth | `坦白` | 3/152 (2%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 2/47 (4%) | 0/77 (0%) |
| transparent (transparent, open) | truth | `␣transparency`, `透明` | 2/152 (1%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 2/47 (4%) | 0/77 (0%) |
| purpose (the purpose of the act) | unclear | `目的是` | 1/152 (1%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 1/47 (2%) | 1/77 (1%) |
| dishonest (not honest) | lie | `␣dishonest` | 1/152 (1%) | 0/81 (0%) | 0/138 (0%) | 2/158 (1%) | 0/47 (0%) | 0/77 (0%) |
| moral (moral) | unclear | `道德` | 1/152 (1%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 0/47 (0%) | 0/77 (0%) |
| comply (following rules, compliance) | unclear | `合规` | 1/152 (1%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 1/47 (2%) | 0/77 (0%) |
| disguise (masking) | lie | `␣mask` | 1/152 (1%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 1/47 (2%) | 0/77 (0%) |

Not in the draft: truth (excluded: truth from the question on); admit (excluded: admit / deny / acknowledge); deceive (excluded: the question's own word)

## q_tok6

| family | side | members | lies | truths | no-pressure truths | unrelated | lies that deny | truths that deny |
|---|---|---|---|---|---|---|---|---|
| false (false, untrue) | lie | `真假` | 29/152 (19%) | 16/81 (20%) | 94/138 (68%) | 146/158 (92%) | 2/47 (4%) | 14/77 (18%) |
| true (true, real) | truth | `␣true`, `true`, `True`, `␣True`, `(True`, `的真` | 27/152 (18%) | 8/81 (10%) | 33/138 (24%) | 52/158 (33%) | 5/47 (11%) | 8/77 (10%) |
| truthful (telling the truth, faithfully to the facts) | truth | `实事求是` | 7/152 (5%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 0/47 (0%) | 0/77 (0%) |
| honest (honest, honesty) | truth | `␣honestly`, `诚实` | 6/152 (4%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 1/47 (2%) | 0/77 (0%) |
| neutral (neutral) | unclear | `中立` | 1/152 (1%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 0/47 (0%) | 0/77 (0%) |
| correct (correct) | truth | `(true` | 0/152 (0%) | 0/81 (0%) | 0/138 (0%) | 2/158 (1%) | 0/47 (0%) | 0/77 (0%) |

Not in the draft: truth (excluded: truth from the question on)

## q_tok7

| family | side | members | lies | truths | no-pressure truths | unrelated | lies that deny | truths that deny |
|---|---|---|---|---|---|---|---|---|
| true (true, real) | truth | `true`, `True`, `␣True`, `TRUE`, `(True`, `.True` | 115/152 (76%) | 64/81 (79%) | 108/138 (78%) | 151/158 (96%) | 21/47 (45%) | 60/77 (78%) |
| wrong (wrong, mistaken) | lie | `错误或`, `对错` | 14/152 (9%) | 18/81 (22%) | 5/138 (4%) | 0/158 (0%) | 5/47 (11%) | 18/77 (23%) |
| false (false, untrue) | lie | `␣False`, `=False` | 5/152 (3%) | 22/81 (27%) | 64/138 (46%) | 18/158 (11%) | 2/47 (4%) | 22/77 (29%) |
| comply (following rules, compliance) | unclear | `␣compliance` | 1/152 (1%) | 0/81 (0%) | 0/138 (0%) | 2/158 (1%) | 1/47 (2%) | 0/77 (0%) |

Not in the draft: admit (excluded: admit / deny / acknowledge)
