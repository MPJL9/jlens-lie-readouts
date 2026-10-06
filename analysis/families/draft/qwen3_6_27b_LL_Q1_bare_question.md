# Draft families: qwen3.6-27b, logit lens, part Q1_bare, group question

Written by `scripts/apply_family_decisions.py` (2026-10-01; draft, not frozen). Counts are `present / transcripts (share)`
on the build split.

## q_tok0

| family | side | members | lies | truths | no-pressure truths | unrelated | lies that deny | truths that deny |
|---|---|---|---|---|---|---|---|---|
| true (true, real) | truth | `真的`, `确实`, `的真` | 50/152 (33%) | 18/81 (22%) | 15/138 (11%) | 1/158 (1%) | 18/53 (34%) | 18/74 (24%) |
| deliberate (done on purpose) | unclear | `␣intentional`, `␣deliberate`, `␣intentionally`, `␣knowingly` | 20/152 (13%) | 20/81 (25%) | 19/138 (14%) | 2/158 (1%) | 9/53 (17%) | 18/74 (24%) |
| wrong (wrong, mistaken) | lie | `错`, `误会` | 2/152 (1%) | 4/81 (5%) | 10/138 (7%) | 1/158 (1%) | 2/53 (4%) | 4/74 (5%) |
| knowingly (knowingly, with knowledge of the facts) | unclear | `␣knowingly`, `知情` | 3/152 (2%) | 2/81 (2%) | 0/138 (0%) | 0/158 (0%) | 0/53 (0%) | 1/74 (1%) |
| omit (omit / omission) | lie | `遗漏` | 1/152 (1%) | 1/81 (1%) | 1/138 (1%) | 7/158 (4%) | 0/53 (0%) | 1/74 (1%) |
| intent (intent / intention (noun)) | unclear | `␣intention` | 0/152 (0%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 0/53 (0%) | 1/74 (1%) |
| truth (the truth (noun)) | truth | `␣truthful` | 1/152 (1%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 0/53 (0%) | 0/74 (0%) |
| truthful (truthful, telling it as it is) | truth | `␣truthful` | 1/152 (1%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 0/53 (0%) | 0/74 (0%) |
| correct (correct) | truth | `正确`, `的正确` | 0/152 (0%) | 0/81 (0%) | 0/138 (0%) | 1/158 (1%) | 0/53 (0%) | 0/74 (0%) |
| fact (fact, factual) | truth | `符合` | 0/152 (0%) | 0/81 (0%) | 1/138 (1%) | 0/158 (0%) | 0/53 (0%) | 0/74 (0%) |

## q_tok1

| family | side | members | lies | truths | no-pressure truths | unrelated | lies that deny | truths that deny |
|---|---|---|---|---|---|---|---|---|
| intent (intent / intention (noun)) | unclear | `␣intention`, `␣intentions`, `␣intended` | 17/152 (11%) | 15/81 (19%) | 5/138 (4%) | 0/158 (0%) | 3/53 (6%) | 15/74 (20%) |
| refuse (refuse / refusal) | unclear | `␣refusal`, `拒绝` | 2/152 (1%) | 6/81 (7%) | 2/138 (1%) | 0/158 (0%) | 1/53 (2%) | 6/74 (8%) |
| honest (honest / honesty) | truth | `␣honesty`, `␣honest`, `诚实` | 1/152 (1%) | 7/81 (9%) | 1/138 (1%) | 0/158 (0%) | 1/53 (2%) | 7/74 (9%) |
| compliant (compliant with rules / instructions) | unclear | `合规`, `␣compliance` | 4/152 (3%) | 4/81 (5%) | 3/138 (2%) | 0/158 (0%) | 3/53 (6%) | 4/74 (5%) |
| integrity (integrity, keeping faith) | truth | `诚信`, `␣integrity` | 4/152 (3%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 1/53 (2%) | 1/74 (1%) |
| objective (objective) | unclear | `客观` | 5/152 (3%) | 0/81 (0%) | 1/138 (1%) | 0/158 (0%) | 3/53 (6%) | 0/74 (0%) |
| candour (candid, frank) | truth | `坦诚` | 1/152 (1%) | 3/81 (4%) | 0/138 (0%) | 0/158 (0%) | 1/53 (2%) | 3/74 (4%) |
| conceal (conceal / hide) | lie | `隐瞒` | 3/152 (2%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 3/53 (6%) | 0/74 (0%) |
| perfunctory (perfunctory, brushing off) | unclear | `敷衍` | 3/152 (2%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 0/53 (0%) | 0/74 (0%) |
| truthful (truthful, telling it as it is) | truth | `如实`, `␣truthful` | 2/152 (1%) | 1/81 (1%) | 1/138 (1%) | 0/158 (0%) | 2/53 (4%) | 1/74 (1%) |
| false (false, untrue) | lie | `␣fals`, `假` | 2/152 (1%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 0/53 (0%) | 1/74 (1%) |
| wrong (wrong, mistaken) | lie | `␣mistake`, `失误` | 2/152 (1%) | 0/81 (0%) | 4/138 (3%) | 0/158 (0%) | 0/53 (0%) | 0/74 (0%) |
| true (true, real) | truth | `真`, `确实` | 2/152 (1%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 1/53 (2%) | 0/74 (0%) |
| lie (lie / lying) | lie | `lying` | 0/152 (0%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 0/53 (0%) | 1/74 (1%) |
| transparent (transparent / transparency) | truth | `␣transparency` | 1/152 (1%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 1/53 (2%) | 0/74 (0%) |
| fraud (fraud) | lie | `诈` | 1/152 (1%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 0/53 (0%) | 0/74 (0%) |
| fact (fact, factual) | truth | `␣fact`, `␣facts`, `␣Fact`, `␣factual`, `实际情况` | 1/152 (1%) | 0/81 (0%) | 2/138 (1%) | 0/158 (0%) | 0/53 (0%) | 0/74 (0%) |
| correct (correct) | truth | `␣correction`, `␣corrected`, `␣corrections`, `纠正` | 0/152 (0%) | 0/81 (0%) | 0/138 (0%) | 2/158 (1%) | 0/53 (0%) | 0/74 (0%) |
| accurate (accurate) | truth | `准确` | 0/152 (0%) | 0/81 (0%) | 1/138 (1%) | 1/158 (1%) | 0/53 (0%) | 0/74 (0%) |

Not in the draft: admit (excluded: admit / deny / acknowledge); deny (excluded: admit / deny / acknowledge); violate (held back: no undisputed member left)

## q_tok2

| family | side | members | lies | truths | no-pressure truths | unrelated | lies that deny | truths that deny |
|---|---|---|---|---|---|---|---|---|
| incorrect (incorrect) | lie | `␣incorrect` | 19/152 (12%) | 22/81 (27%) | 104/138 (75%) | 50/158 (32%) | 6/53 (11%) | 17/74 (23%) |
| refuse (refuse / refusal) | unclear | `␣refusal`, `拒绝` | 1/152 (1%) | 12/81 (15%) | 0/138 (0%) | 0/158 (0%) | 1/53 (2%) | 12/74 (16%) |
| contradictory (contradictory) | unclear | `␣contradictory` | 2/152 (1%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 2/53 (4%) | 1/74 (1%) |
| fact (fact, factual) | truth | `符合`, `与现实` | 1/152 (1%) | 2/81 (2%) | 0/138 (0%) | 1/158 (1%) | 0/53 (0%) | 1/74 (1%) |
| compliant (compliant with rules / instructions) | unclear | `遵守` | 0/152 (0%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 0/53 (0%) | 1/74 (1%) |
| correct (correct) | truth | `␣correct`, `正确` | 0/152 (0%) | 0/81 (0%) | 0/138 (0%) | 1/158 (1%) | 0/53 (0%) | 0/74 (0%) |
| true (true, real) | truth | `确实` | 0/152 (0%) | 0/81 (0%) | 1/138 (1%) | 0/158 (0%) | 0/53 (0%) | 0/74 (0%) |

Not in the draft: admit (excluded: admit / deny / acknowledge)

## q_tok3

| family | side | members | lies | truths | no-pressure truths | unrelated | lies that deny | truths that deny |
|---|---|---|---|---|---|---|---|---|
| accurate (accurate) | truth | `␣accur`, `␣accurate`, `␣accuracy`, `␣accurately`, `accur`, `准确`, `准确的` | 134/152 (88%) | 69/81 (85%) | 138/138 (100%) | 156/158 (99%) | 52/53 (98%) | 64/74 (86%) |
| truthful (truthful, telling it as it is) | truth | `␣truthful`, `如实` | 138/152 (91%) | 59/81 (73%) | 126/138 (91%) | 23/158 (15%) | 49/53 (92%) | 54/74 (73%) |
| truth (the truth (noun)) | truth | `␣truthful`, `如实` | 138/152 (91%) | 59/81 (73%) | 126/138 (91%) | 23/158 (15%) | 49/53 (92%) | 54/74 (73%) |
| helpful (helpful) | unclear | `␣helpful`, `␣Helpful`, `有帮助` | 99/152 (65%) | 58/81 (72%) | 111/138 (80%) | 154/158 (97%) | 20/53 (38%) | 52/74 (70%) |
| compliant (compliant with rules / instructions) | unclear | `␣compliant`, `合规`, `遵守`, `遵循`, `遵`, `␣compliance`, `␣comply`, `␣complying`, `␣adher`, `␣adherence`, `␣adhere`, `␣conform`, `依法依规` | 97/152 (64%) | 56/81 (69%) | 51/138 (37%) | 123/158 (78%) | 21/53 (40%) | 50/74 (68%) |
| aligned (aligned (with guidelines)) | unclear | `␣aligned`, `␣align`, `␣alignment` | 84/152 (55%) | 54/81 (67%) | 56/138 (41%) | 0/158 (0%) | 16/53 (30%) | 48/74 (65%) |
| honest (honest / honesty) | truth | `␣honest`, `␣honestly`, `␣honesty`, `诚实`, `诚`, `诚实守信` | 87/152 (57%) | 36/81 (44%) | 16/138 (12%) | 5/158 (3%) | 35/53 (66%) | 32/74 (43%) |
| fact (fact, factual) | truth | `␣fact`, `Fact`, `␣Fact`, `␣factual`, `事实`, `实际上`, `的事实` | 87/152 (57%) | 27/81 (33%) | 125/138 (91%) | 76/158 (48%) | 41/53 (77%) | 24/74 (32%) |
| conform (conform to) | unclear | `符合`, `是否符合`, `␣conform` | 73/152 (48%) | 31/81 (38%) | 31/138 (22%) | 58/158 (37%) | 13/53 (25%) | 27/74 (36%) |
| correct (correct) | truth | `␣valid`, `␣correct`, `␣Valid`, `␣correctly`, `correct`, `_correct`, `Correct`, `␣Correct`, `␣correctness`, `正确`, `正确的`, `正确答案`, `的正确`, `是正确的`, `正确地`, `是否正确` | 36/152 (24%) | 36/81 (44%) | 136/138 (99%) | 155/158 (98%) | 19/53 (36%) | 33/74 (45%) |
| perfunctory (perfunctory, brushing off) | unclear | `敷衍` | 55/152 (36%) | 16/81 (20%) | 9/138 (7%) | 4/158 (3%) | 31/53 (58%) | 16/74 (22%) |
| crafted (crafted) | unclear | `␣crafted` | 32/152 (21%) | 18/81 (22%) | 2/138 (1%) | 0/158 (0%) | 10/53 (19%) | 17/74 (23%) |
| influenced (influenced) | unclear | `␣influenced` | 18/152 (12%) | 26/81 (32%) | 38/138 (28%) | 21/158 (13%) | 10/53 (19%) | 25/74 (34%) |
| biased (biased) | unclear | `␣biased`, `␣bias` | 22/152 (14%) | 16/81 (20%) | 19/138 (14%) | 46/158 (29%) | 6/53 (11%) | 15/74 (20%) |
| intent (the purpose behind the act) | unclear | `␣intended`, `␣intend` | 14/152 (9%) | 23/81 (28%) | 5/138 (4%) | 1/158 (1%) | 9/53 (17%) | 20/74 (27%) |
| lie (lie / lying) | lie | `␣lying`, `␣lies`, `␣lie`, `谎言`, `说谎`, `撒谎`, `谎`, `␣거짓` | 28/152 (18%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 18/53 (34%) | 0/74 (0%) |
| ethical (ethical) | unclear | `␣ethical`, `伦理`, `␣morally` | 19/152 (12%) | 9/81 (11%) | 0/138 (0%) | 0/158 (0%) | 0/53 (0%) | 9/74 (12%) |
| true (true, real) | truth | `␣true`, `␣True`, `␣TRUE`, `␣genuine`, `␣genuinely`, `真的`, `真实`, `真实的`, `的真`, `的真实`, `的真实性` | 19/152 (12%) | 6/81 (7%) | 11/138 (8%) | 3/158 (2%) | 15/53 (28%) | 6/74 (8%) |
| tailored (tailored) | unclear | `␣tailored` | 18/152 (12%) | 6/81 (7%) | 0/138 (0%) | 2/158 (1%) | 2/53 (4%) | 5/74 (7%) |
| incorrect (incorrect) | lie | `␣incorrect`, `␣inaccurate`, `␣Incorrect`, `有误` | 11/152 (7%) | 7/81 (9%) | 20/138 (14%) | 22/158 (14%) | 10/53 (19%) | 6/74 (8%) |
| violate (violate rules) | unclear | `违规`, `违反`, `␣violate`, `␣violating` | 9/152 (6%) | 8/81 (10%) | 0/138 (0%) | 0/158 (0%) | 1/53 (2%) | 6/74 (8%) |
| scripted (scripted, canned) | unclear | `␣canned`, `␣scripted` | 12/152 (8%) | 2/81 (2%) | 0/138 (0%) | 0/158 (0%) | 4/53 (8%) | 2/74 (3%) |
| refuse (refuse / refusal) | unclear | `␣refusal`, `␣refus`, `拒绝` | 0/152 (0%) | 13/81 (16%) | 0/138 (0%) | 0/158 (0%) | 0/53 (0%) | 12/74 (16%) |
| objective (objective) | unclear | `客观`, `中立` | 2/152 (1%) | 10/81 (12%) | 6/138 (4%) | 2/158 (1%) | 2/53 (4%) | 9/74 (12%) |
| dishonest (dishonest) | lie | `␣dishonest` | 10/152 (7%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 4/53 (8%) | 0/74 (0%) |
| neutral (neutral) | unclear | `中立` | 1/152 (1%) | 8/81 (10%) | 5/138 (4%) | 1/158 (1%) | 1/53 (2%) | 8/74 (11%) |
| false (false, untrue) | lie | `␣false`, `假`, `虚假`, `假的`, `虚假信息` | 9/152 (6%) | 0/81 (0%) | 1/138 (1%) | 1/158 (1%) | 7/53 (13%) | 0/74 (0%) |
| fabricate (fabricate, make up) | lie | `␣fabricated`, `虚构` | 7/152 (5%) | 0/81 (0%) | 2/138 (1%) | 0/158 (0%) | 5/53 (9%) | 0/74 (0%) |
| moral (morally (judgement)) | unclear | `␣morally` | 4/152 (3%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 0/53 (0%) | 1/74 (1%) |
| evade (evade / evasion) | unclear | `␣evasion`, `回避`, `␣dodge` | 3/152 (2%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 3/53 (6%) | 1/74 (1%) |
| deliberate (done on purpose) | unclear | `␣intentionally`, `␣intentional`, `故意` | 1/152 (1%) | 3/81 (4%) | 1/138 (1%) | 0/158 (0%) | 1/53 (2%) | 2/74 (3%) |
| hallucinate (hallucinate) | unclear | `␣halluc` | 2/152 (1%) | 1/81 (1%) | 12/138 (9%) | 11/158 (7%) | 0/53 (0%) | 1/74 (1%) |
| sincere (sincere) | truth | `␣sincere` | 2/152 (1%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 1/53 (2%) | 0/74 (0%) |
| mask (mask, cover up, gloss over) | lie | `掩饰` | 2/152 (1%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 1/53 (2%) | 0/74 (0%) |
| nonconforming (not conforming) | unclear | `不符合` | 0/152 (0%) | 2/81 (2%) | 0/138 (0%) | 1/158 (1%) | 0/53 (0%) | 1/74 (1%) |
| euphemistic (euphemistic, softened) | unclear | `委婉` | 1/152 (1%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 0/53 (0%) | 0/74 (0%) |
| wrong (wrong, mistaken) | lie | `␣error`, `␣wrong`, `错`, `错误`, `错了`, `是错误的` | 0/152 (0%) | 1/81 (1%) | 2/138 (1%) | 4/158 (3%) | 0/53 (0%) | 1/74 (1%) |

Not in the draft: deny (excluded: admit / deny / acknowledge); admit (excluded: admit / deny / acknowledge)

## q_tok4

| family | side | members | lies | truths | no-pressure truths | unrelated | lies that deny | truths that deny |
|---|---|---|---|---|---|---|---|---|
| mislead (mislead) | lie | `␣misleading`, `误导`, `␣misled` | 152/152 (100%) | 81/81 (100%) | 138/138 (100%) | 158/158 (100%) | 53/53 (100%) | 74/74 (100%) |
| false (false, untrue) | lie | `␣false`, `␣False`, `false`, `=False`, `=false`, `:false`, `>false`, `␣fals`, `␣untrue`, `/false`, `␣falsehood`, `假`, `虚假`, `虚假信息` | 152/152 (100%) | 81/81 (100%) | 138/138 (100%) | 158/158 (100%) | 53/53 (100%) | 74/74 (100%) |
| conceal (conceal / hide) | lie | `隐瞒`, `␣conceal`, `␣hiding`, `遮` | 149/152 (98%) | 80/81 (99%) | 131/138 (95%) | 105/158 (66%) | 52/53 (98%) | 73/74 (99%) |
| dishonest (dishonest) | lie | `␣dishonest` | 151/152 (99%) | 74/81 (91%) | 134/138 (97%) | 157/158 (99%) | 53/53 (100%) | 67/74 (91%) |
| deliberate (done on purpose) | unclear | `故意`, `␣intentionally`, `␣deliberately`, `␣intentional`, `有意`, `刻意`, `故意的`, `␣deliberate`, `明知` | 152/152 (100%) | 69/81 (85%) | 138/138 (100%) | 156/158 (99%) | 53/53 (100%) | 62/74 (84%) |
| lie (lie / lying) | lie | `␣lying`, `谎言`, `说谎`, `撒谎`, `␣lies`, `␣lie`, `谎`, `␣거짓` | 152/152 (100%) | 54/81 (67%) | 14/138 (10%) | 104/158 (66%) | 53/53 (100%) | 48/74 (65%) |
| fake (fake) | lie | `fake`, `␣fake` | 140/152 (92%) | 51/81 (63%) | 129/138 (93%) | 158/158 (100%) | 45/53 (85%) | 46/74 (62%) |
| intent (intent / intention (noun)) | unclear | `␣intent`, `意图`, `␣Intent`, `Intent`, `␣intentions`, `intent`, `␣intended`, `␣intend`, `␣intending` | 104/152 (68%) | 60/81 (74%) | 116/138 (84%) | 38/158 (24%) | 41/53 (77%) | 55/74 (74%) |
| withhold (withhold) | lie | `␣withholding`, `␣withhold`, `␣withheld` | 103/152 (68%) | 47/81 (58%) | 27/138 (20%) | 0/158 (0%) | 37/53 (70%) | 40/74 (54%) |
| integrity (integrity, keeping faith) | truth | `诚信` | 105/152 (69%) | 41/81 (51%) | 5/138 (4%) | 0/158 (0%) | 30/53 (57%) | 38/74 (51%) |
| manipulate (manipulate) | lie | `␣manip`, `␣manipulation`, `Manip`, `␣Manip`, `␣manipulated`, `␣манипу`, `诱导` | 81/152 (53%) | 65/81 (80%) | 117/138 (85%) | 138/158 (87%) | 24/53 (45%) | 60/74 (81%) |
| omit (omit / omission) | lie | `␣omission`, `␣omit`, `␣omitted`, `省略` | 51/152 (34%) | 47/81 (58%) | 15/138 (11%) | 0/158 (0%) | 17/53 (32%) | 44/74 (59%) |
| truth (the truth (noun)) | truth | `␣truthful`, `如实` | 69/152 (45%) | 9/81 (11%) | 34/138 (25%) | 2/158 (1%) | 18/53 (34%) | 9/74 (12%) |
| truthful (truthful, telling it as it is) | truth | `␣truthful`, `如实` | 69/152 (45%) | 9/81 (11%) | 34/138 (25%) | 2/158 (1%) | 18/53 (34%) | 9/74 (12%) |
| honest (honest / honesty) | truth | `诚实`, `␣honest`, `␣honesty` | 70/152 (46%) | 6/81 (7%) | 0/138 (0%) | 0/158 (0%) | 22/53 (42%) | 6/74 (8%) |
| knowingly (knowingly, with knowledge of the facts) | unclear | `明知`, `知情` | 31/152 (20%) | 5/81 (6%) | 0/138 (0%) | 0/158 (0%) | 15/53 (28%) | 4/74 (5%) |
| disclose (disclose / disclosure) | truth | `信息披露` | 24/152 (16%) | 10/81 (12%) | 0/138 (0%) | 0/158 (0%) | 9/53 (17%) | 10/74 (14%) |
| true (true, real) | truth | `␣true`, `真实`, `真实的`, `是真的` | 27/152 (18%) | 2/81 (2%) | 0/138 (0%) | 0/158 (0%) | 9/53 (17%) | 1/74 (1%) |
| framing (framing (of the message)) | unclear | `␣framing` | 6/152 (4%) | 12/81 (15%) | 7/138 (5%) | 0/158 (0%) | 3/53 (6%) | 11/74 (15%) |
| mask (mask, cover up, gloss over) | lie | `␣masking`, `␣mask`, `掩饰`, `伪装` | 12/152 (8%) | 5/81 (6%) | 0/138 (0%) | 0/158 (0%) | 1/53 (2%) | 4/74 (5%) |
| indirect (indirect) | unclear | `间接`, `␣indirect` | 0/152 (0%) | 15/81 (19%) | 3/138 (2%) | 0/158 (0%) | 0/53 (0%) | 15/74 (20%) |
| fraud (fraud) | lie | `␣fraudulent`, `␣fraud` | 11/152 (7%) | 0/81 (0%) | 0/138 (0%) | 4/158 (3%) | 2/53 (4%) | 0/74 (0%) |
| euphemistic (euphemistic, softened) | unclear | `委婉` | 0/152 (0%) | 9/81 (11%) | 0/138 (0%) | 0/158 (0%) | 0/53 (0%) | 9/74 (12%) |
| transparent (transparent / transparency) | truth | `-transparent` | 2/152 (1%) | 6/81 (7%) | 1/138 (1%) | 9/158 (6%) | 0/53 (0%) | 6/74 (8%) |
| imply (imply, hint) | unclear | `暗示` | 5/152 (3%) | 2/81 (2%) | 6/138 (4%) | 0/158 (0%) | 4/53 (8%) | 2/74 (3%) |
| ethical (ethical) | unclear | `␣ethical`, `␣morally` | 5/152 (3%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 0/53 (0%) | 0/74 (0%) |
| unethical (unethical) | unclear | `␣unethical` | 4/152 (3%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 0/53 (0%) | 0/74 (0%) |
| moral (morally (judgement)) | unclear | `␣morally` | 3/152 (2%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 0/53 (0%) | 0/74 (0%) |
| disguise (disguise, pretend to be) | lie | `伪装` | 0/152 (0%) | 2/81 (2%) | 0/138 (0%) | 0/158 (0%) | 0/53 (0%) | 1/74 (1%) |
| distort (distort) | lie | `扭曲` | 1/152 (1%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 1/53 (2%) | 0/74 (0%) |
| induce (induce, lure into) | unclear | `诱导` | 0/152 (0%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 0/53 (0%) | 1/74 (1%) |
| betray (betraying someone) | unclear | `出卖` | 0/152 (0%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 0/53 (0%) | 1/74 (1%) |

Not in the draft: deceive (excluded: the question's own word)

## q_tok5

| family | side | members | lies | truths | no-pressure truths | unrelated | lies that deny | truths that deny |
|---|---|---|---|---|---|---|---|---|
| true (true, real) | truth | `␣true`, `true`, `True`, `␣True`, `␣TRUE` | 152/152 (100%) | 81/81 (100%) | 138/138 (100%) | 154/158 (97%) | 53/53 (100%) | 74/74 (100%) |
| honest (honest / honesty) | truth | `诚实`, `␣honest`, `␣honesty`, `␣honestly`, `诚`, `␣Honest` | 139/152 (91%) | 62/81 (77%) | 105/138 (76%) | 142/158 (90%) | 49/53 (92%) | 56/74 (76%) |
| ethical (ethical) | unclear | `ethical`, `␣ethical`, `伦理`, `道德` | 101/152 (66%) | 20/81 (25%) | 5/138 (4%) | 0/158 (0%) | 21/53 (40%) | 15/74 (20%) |
| deliberate (done on purpose) | unclear | `故意的`, `明知` | 54/152 (36%) | 12/81 (15%) | 1/138 (1%) | 2/158 (1%) | 30/53 (57%) | 10/74 (14%) |
| knowingly (knowingly, with knowledge of the facts) | unclear | `明知` | 50/152 (33%) | 9/81 (11%) | 0/138 (0%) | 0/158 (0%) | 30/53 (57%) | 8/74 (11%) |
| intent (intent / intention (noun)) | unclear | `意图`, `␣intentions` | 23/152 (15%) | 16/81 (20%) | 4/138 (3%) | 0/158 (0%) | 5/53 (9%) | 16/74 (22%) |
| lie (lie / lying) | lie | `␣lie`, `␣lies` | 23/152 (15%) | 9/81 (11%) | 4/138 (3%) | 0/158 (0%) | 20/53 (38%) | 8/74 (11%) |
| objective (objective) | unclear | `客观` | 27/152 (18%) | 5/81 (6%) | 6/138 (4%) | 0/158 (0%) | 7/53 (13%) | 4/74 (5%) |
| false (false, untrue) | lie | `␣false`, `␣False`, `false`, `.assertFalse`, `.False`, `/false` | 0/152 (0%) | 30/81 (37%) | 71/138 (51%) | 122/158 (77%) | 0/53 (0%) | 30/74 (41%) |
| fact (fact, factual) | truth | `与现实` | 7/152 (5%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 2/53 (4%) | 1/74 (1%) |
| violate (violate rules) | unclear | `违反了`, `违反` | 3/152 (2%) | 4/81 (5%) | 0/138 (0%) | 0/158 (0%) | 0/53 (0%) | 3/74 (4%) |
| accusation (accusation) | unclear | `␣accusations` | 0/152 (0%) | 6/81 (7%) | 3/138 (2%) | 1/158 (1%) | 0/53 (0%) | 6/74 (8%) |
| innocent (innocent, not guilty) | unclear | `无罪` | 2/152 (1%) | 2/81 (2%) | 0/138 (0%) | 0/158 (0%) | 1/53 (2%) | 2/74 (3%) |
| confess (confess, come clean) | truth | `坦白` | 3/152 (2%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 2/53 (4%) | 0/74 (0%) |
| transparent (transparent / transparency) | truth | `␣transparency`, `透明` | 2/152 (1%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 2/53 (4%) | 0/74 (0%) |
| dishonest (dishonest) | lie | `␣dishonest` | 1/152 (1%) | 0/81 (0%) | 0/138 (0%) | 2/158 (1%) | 0/53 (0%) | 0/74 (0%) |
| mask (mask, cover up, gloss over) | lie | `␣mask` | 1/152 (1%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 0/53 (0%) | 0/74 (0%) |
| compliant (compliant with rules / instructions) | unclear | `合规` | 1/152 (1%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 0/53 (0%) | 0/74 (0%) |
| conform (conform to) | unclear | `是否符合` | 0/152 (0%) | 1/81 (1%) | 1/138 (1%) | 0/158 (0%) | 0/53 (0%) | 1/74 (1%) |

Not in the draft: truth (excluded: truth from the question on); admit (excluded: admit / deny / acknowledge); deceive (excluded: the question's own word)
