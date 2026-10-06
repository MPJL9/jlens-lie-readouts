# Draft families: qwen3.6-27b, logit lens, part Q9_dyl, group preans

Written by `scripts/apply_family_decisions.py` (2026-10-01; draft, not frozen). Counts are `present / transcripts (share)`
on the build split.

## preans_slot0

| family | side | members | lies | truths | no-pressure truths | unrelated | lies that deny | truths that deny |
|---|---|---|---|---|---|---|---|---|
| cannot (first-person refusal formula "I cannot") | unclear | `我无法`, `我不能` | 73/152 (48%) | 41/81 (51%) | 8/138 (6%) | 45/158 (28%) | 32/65 (49%) | 39/76 (51%) |
| wrong (wrong, mistaken) | lie | `指正` | 44/152 (29%) | 25/81 (31%) | 66/138 (48%) | 133/158 (84%) | 17/65 (26%) | 25/76 (33%) |
| accuse (accusation) | unclear | `指控` | 41/152 (27%) | 26/81 (32%) | 30/138 (22%) | 46/158 (29%) | 23/65 (35%) | 26/76 (34%) |
| compliance (complying with rules) | unclear | `合规`, `␣compliance`, `守法` | 13/152 (9%) | 13/81 (16%) | 20/138 (14%) | 7/158 (4%) | 9/65 (14%) | 13/76 (17%) |
| law-abiding (law-abiding) | unclear | `守法` | 7/152 (5%) | 10/81 (12%) | 10/138 (7%) | 2/158 (1%) | 4/65 (6%) | 10/76 (13%) |
| true (true, real) | truth | `是真的` | 10/152 (7%) | 4/81 (5%) | 0/138 (0%) | 0/158 (0%) | 0/65 (0%) | 4/76 (5%) |
| candid (candid, frank) | truth | `坦诚` | 9/152 (6%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 3/65 (5%) | 1/76 (1%) |
| reveal (revealing) | truth | `揭示了`, `揭` | 7/152 (5%) | 2/81 (2%) | 0/138 (0%) | 0/158 (0%) | 3/65 (5%) | 1/76 (1%) |
| fact (fact, factual) | truth | `求实` | 5/152 (3%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 1/65 (2%) | 0/76 (0%) |
| objective (objective, impartial) | unclear | `客观`, `␣objectively` | 1/152 (1%) | 2/81 (2%) | 0/138 (0%) | 8/158 (5%) | 0/65 (0%) | 2/76 (3%) |
| knowing (with knowledge / knowingly) | unclear | `明知` | 3/152 (2%) | 0/81 (0%) | 0/138 (0%) | 1/158 (1%) | 0/65 (0%) | 0/76 (0%) |
| ethics (ethics / morality) | unclear | `伦理` | 3/152 (2%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 0/65 (0%) | 0/76 (0%) |
| honest (honest / honesty) | truth | `诚实` | 2/152 (1%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 0/65 (0%) | 0/76 (0%) |
| silence (staying silent) | unclear | `沉默` | 2/152 (1%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 1/65 (2%) | 0/76 (0%) |
| intentional (done on purpose) | unclear | `␣deliberate` | 1/152 (1%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 1/65 (2%) | 0/76 (0%) |
| false (false, untrue) | lie | `>false` | 0/152 (0%) | 0/81 (0%) | 0/138 (0%) | 2/158 (1%) | 0/65 (0%) | 0/76 (0%) |

Not in the draft: admit (excluded: admit / deny / acknowledge); acknowledge (excluded: admit / deny / acknowledge); truth (excluded: truth from the question on); violate (held back: no undisputed member left)

## preans_slot1

| family | side | members | lies | truths | no-pressure truths | unrelated | lies that deny | truths that deny |
|---|---|---|---|---|---|---|---|---|
| fact (fact / the facts) | unclear | `事实`, `␣fact`, `事实上`, `␣factual`, `␣Fact`, `␣facts`, `的事实`, `fact`, `Fact`, `事实和`, `␣FACT`, `facts`, `FACT`, `_fact`, `␣Facts`, `实际`, `符合`, `实际上`, `的实际`, `实际的`, `是否符合`, `与实际` | 152/152 (100%) | 81/81 (100%) | 138/138 (100%) | 158/158 (100%) | 65/65 (100%) | 76/76 (100%) |
| false (false, untrue) | lie | `␣false`, `␣False`, `false`, `False`, `=False`, `␣FALSE`, `=false`, `_FALSE`, `:false`, `FALSE`, `>false`, `␣fals`, `_false`, `.assertFalse`, `.False`, `assertFalse`, `␣untrue`, `.FALSE`, `/false`, `␣falsehood`, `假`, `虚假`, `假的`, `不实` | 148/152 (97%) | 80/81 (99%) | 138/138 (100%) | 158/158 (100%) | 64/65 (98%) | 75/76 (99%) |
| deceive (the act of deceiving) | lie | `欺骗`, `␣deception`, `␣deceptive`, `␣deceive`, `␣deceit`, `骗`, `␣deceived`, `哄` | 148/152 (97%) | 76/81 (94%) | 122/138 (88%) | 155/158 (98%) | 64/65 (98%) | 71/76 (93%) |
| truthful (truthful, telling it as it is) | truth | `␣truthful`, `如实`, `实事求是` | 151/152 (99%) | 72/81 (89%) | 136/138 (99%) | 107/158 (68%) | 64/65 (98%) | 67/76 (88%) |
| true (true, real) | truth | `␣true`, `true`, `True`, `␣True`, `␣TRUE`, `=true`, `_true`, `:true`, `,true`, `␣genuine`, `.True`, `>true`, `真`, `成立`, `真实`, `确实`, `的确`, `真实的`, `是真的`, `的真`, `内容的真实性`, `确实是`, `的真实`, `属实`, `的真实性` | 151/152 (99%) | 68/81 (84%) | 114/138 (83%) | 27/158 (17%) | 64/65 (98%) | 63/76 (83%) |
| honest (honest / honesty) | truth | `诚实`, `诚`, `␣honesty`, `␣honest`, `誠`, `诚信`, `诚实守信` | 138/152 (91%) | 80/81 (99%) | 137/138 (99%) | 154/158 (97%) | 63/65 (97%) | 75/76 (99%) |
| conceal (concealing the truth) | lie | `隐瞒`, `␣conceal`, `␣concealed`, `瞒`, `隐匿`, `掩`, `遮`, `隐` | 146/152 (96%) | 65/81 (80%) | 93/138 (67%) | 11/158 (7%) | 61/65 (94%) | 60/76 (79%) |
| conceal (concealing / covering up information) | lie | `隐瞒`, `␣conceal`, `␣concealed`, `掩盖`, `瞒`, `掩饰`, `遮蔽` | 146/152 (96%) | 65/81 (80%) | 93/138 (67%) | 10/158 (6%) | 61/65 (94%) | 60/76 (79%) |
| knowing (with knowledge / knowingly) | unclear | `明知`, `␣knowingly`, `知情`, `␣knowing`, `␣Knowing`, `Knowing` | 150/152 (99%) | 43/81 (53%) | 111/138 (80%) | 89/158 (56%) | 63/65 (97%) | 38/76 (50%) |
| integrity (integrity, good faith) | truth | `诚信`, `诚实守信` | 80/152 (53%) | 67/81 (83%) | 130/138 (94%) | 154/158 (97%) | 42/65 (65%) | 65/76 (86%) |
| intentional (done on purpose) | unclear | `␣intentionally`, `故意`, `␣deliberately`, `␣deliberate`, `␣intentional`, `有意` | 89/152 (59%) | 51/81 (63%) | 85/138 (62%) | 149/158 (94%) | 38/65 (58%) | 49/76 (64%) |
| objective (objective, impartial) | unclear | `客观`, `␣objectively`, `␣objective` | 93/152 (61%) | 38/81 (47%) | 63/138 (46%) | 67/158 (42%) | 46/65 (71%) | 38/76 (50%) |
| omit (leaving something out) | lie | `␣omit`, `␣omission`, `omit`, `省略`, `␣omitted` | 93/152 (61%) | 28/81 (35%) | 34/138 (25%) | 2/158 (1%) | 40/65 (62%) | 26/76 (34%) |
| withhold (withholding information) | lie | `␣withholding`, `␣withhold`, `␣withheld` | 84/152 (55%) | 35/81 (43%) | 93/138 (67%) | 0/158 (0%) | 34/65 (52%) | 33/76 (43%) |
| fabricate (making something up) | lie | `虚构`, `␣invent`, `␣fabricated`, `␣fabrication`, `␣invented`, `凭空` | 68/152 (45%) | 38/81 (47%) | 75/138 (54%) | 133/158 (84%) | 27/65 (42%) | 35/76 (46%) |
| violate (violating (rules, norms)) | unclear | `违反`, `违背`, `违反了`, `␣violate` | 70/152 (46%) | 36/81 (44%) | 62/138 (45%) | 1/158 (1%) | 38/65 (58%) | 34/76 (45%) |
| misinformation (false information given out) | lie | `虚假信息`, `␣misinformation` | 61/152 (40%) | 26/81 (32%) | 87/138 (63%) | 53/158 (34%) | 33/65 (51%) | 23/76 (30%) |
| technically (technically (true)) | unclear | `␣technically`, `技术上` | 58/152 (38%) | 12/81 (15%) | 0/138 (0%) | 3/158 (2%) | 22/65 (34%) | 9/76 (12%) |
| mislead (leading someone to a false belief) | lie | `␣misleading`, `误导` | 53/152 (35%) | 16/81 (20%) | 0/138 (0%) | 2/158 (1%) | 28/65 (43%) | 14/76 (18%) |
| dishonest (being dishonest) | lie | `␣dishonest` | 24/152 (16%) | 34/81 (42%) | 59/138 (43%) | 101/158 (64%) | 19/65 (29%) | 33/76 (43%) |
| partial (partial, incomplete) | unclear | `不完全`, `␣partially`, `␣partial`, `␣Partial`, `partial` | 38/152 (25%) | 12/81 (15%) | 1/138 (1%) | 5/158 (3%) | 18/65 (28%) | 12/76 (16%) |
| reality (the actual state of affairs) | unclear | `根据实际情况`, `实际情况`, `与现实`, `␣reality`, `␣Reality`, `Reality`, `现实`, `现实的`, `现实中`, `的现实` | 35/152 (23%) | 13/81 (16%) | 58/138 (42%) | 3/158 (2%) | 17/65 (26%) | 13/76 (17%) |
| cover up (covering up / glossing over) | lie | `掩盖`, `掩饰` | 39/152 (26%) | 5/81 (6%) | 0/138 (0%) | 0/158 (0%) | 8/65 (12%) | 4/76 (5%) |
| fake (fake, false-seeming) | lie | `fake`, `␣fake` | 26/152 (17%) | 14/81 (17%) | 15/138 (11%) | 5/158 (3%) | 8/65 (12%) | 13/76 (17%) |
| contradict (contradiction) | unclear | `␣contradict`, `␣contrad`, `␣contradictory`, `␣contradiction`, `矛盾`, `␣contradictions`, `␣conflicting`, `␣conflicts` | 15/152 (10%) | 25/81 (31%) | 48/138 (35%) | 2/158 (1%) | 9/65 (14%) | 24/76 (32%) |
| deviate (deviating) | unclear | `偏离`, `␣deviation`, `背离`, `␣deviations` | 32/152 (21%) | 5/81 (6%) | 1/138 (1%) | 0/158 (0%) | 8/65 (12%) | 4/76 (5%) |
| accurate (accurate) | truth | `␣accur`, `␣accurate`, `␣accuracy`, `␣accurately`, `accuracy`, `Accuracy`, `␣Accuracy`, `准确`, `准确性`, `准确的`, `准确地` | 13/152 (9%) | 24/81 (30%) | 119/138 (86%) | 105/158 (66%) | 11/65 (17%) | 24/76 (32%) |
| ethics (ethics / morality) | unclear | `␣ethical`, `␣morally`, `伦理`, `␣ethics`, `␣moral`, `道德`, `的道德` | 28/152 (18%) | 5/81 (6%) | 0/138 (0%) | 0/158 (0%) | 18/65 (28%) | 3/76 (4%) |
| wrong (wrong, mistaken) | lie | `error`, `␣error`, `␣mistake`, `错误`, `不对`, `错了`, `没错`, `是非`, `是错误的` | 16/152 (11%) | 10/81 (12%) | 24/138 (17%) | 32/158 (20%) | 9/65 (14%) | 7/76 (9%) |
| hide (hiding something) | lie | `␣hiding`, `隐藏`, `Hide`, `␣hide`, `␣hides`, `␣Hide`, `␣hid`, `hide`, `隐匿` | 19/152 (12%) | 2/81 (2%) | 0/138 (0%) | 0/158 (0%) | 5/65 (8%) | 2/76 (3%) |
| fiction (fictional, made-up story) | unclear | `␣fictional`, `fiction`, `␣fiction` | 11/152 (7%) | 10/81 (12%) | 18/138 (13%) | 30/158 (19%) | 2/65 (3%) | 10/76 (13%) |
| disguise (disguising / masquerading) | lie | `伪装`, `␣disguised`, `␣pretending` | 4/152 (3%) | 11/81 (14%) | 2/138 (1%) | 0/158 (0%) | 2/65 (3%) | 10/76 (13%) |
| incorrect (incorrect) | lie | `␣incorrect`, `␣inaccur`, `␣inaccurate`, `不符合`, `有误`, `错误的是` | 6/152 (4%) | 9/81 (11%) | 25/138 (18%) | 39/158 (25%) | 3/65 (5%) | 8/76 (11%) |
| evade (evading the question) | lie | `␣evasion`, `回避` | 10/152 (7%) | 4/81 (5%) | 0/138 (0%) | 0/158 (0%) | 8/65 (12%) | 4/76 (5%) |
| compliance (complying with rules) | unclear | `遵守`, `␣adherence`, `␣compliance`, `严格遵守`, `恪守`, `␣adher`, `␣adhere` | 2/152 (1%) | 12/81 (15%) | 12/138 (9%) | 0/158 (0%) | 2/65 (3%) | 11/76 (14%) |
| inaccurate (inaccurate) | lie | `准确性和`, `不准确` | 10/152 (7%) | 4/81 (5%) | 18/138 (13%) | 26/158 (16%) | 6/65 (9%) | 4/76 (5%) |
| confess (confessing, coming clean) | truth | `坦白` | 2/152 (1%) | 8/81 (10%) | 10/138 (7%) | 9/158 (6%) | 2/65 (3%) | 8/76 (11%) |
| hypocrisy (hypocritical, insincere) | lie | `虚伪` | 5/152 (3%) | 4/81 (5%) | 1/138 (1%) | 0/158 (0%) | 3/65 (5%) | 4/76 (5%) |
| disclose (disclosing, making public) | truth | `公开` | 1/152 (1%) | 7/81 (9%) | 0/138 (0%) | 0/158 (0%) | 1/65 (2%) | 7/76 (9%) |
| transparent (transparency) | truth | `␣transparency`, `␣Transparency` | 0/152 (0%) | 7/81 (9%) | 2/138 (1%) | 2/158 (1%) | 0/65 (0%) | 7/76 (9%) |
| correct (correct) | truth | `␣correct`, `␣correction`, `␣Correction`, `正确`, `无误`, `是正确的` | 0/152 (0%) | 5/81 (6%) | 32/138 (23%) | 4/158 (3%) | 0/65 (0%) | 5/76 (7%) |
| pretend (pretending) | lie | `␣pretending` | 1/152 (1%) | 3/81 (4%) | 0/138 (0%) | 0/158 (0%) | 1/65 (2%) | 2/76 (3%) |
| downplay (downplaying, playing down) | lie | `淡化` | 2/152 (1%) | 2/81 (2%) | 0/138 (0%) | 0/158 (0%) | 2/65 (3%) | 1/76 (1%) |
| candid (candid, frank) | truth | `坦诚` | 0/152 (0%) | 2/81 (2%) | 0/138 (0%) | 5/158 (3%) | 0/65 (0%) | 2/76 (3%) |
| refuse (refusing / declining) | unclear | `拒绝` | 0/152 (0%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 0/65 (0%) | 1/76 (1%) |
| reveal (revealing) | truth | `揭` | 0/152 (0%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 0/65 (0%) | 1/76 (1%) |
| distort (distorting) | lie | `␣distortion` | 0/152 (0%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 0/65 (0%) | 1/76 (1%) |
| misrepresent (misrepresenting) | lie | `␣misrepresented` | 1/152 (1%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 0/65 (0%) | 0/76 (0%) |
| truth (the truth) | truth | `求真` | 0/152 (0%) | 0/81 (0%) | 0/138 (0%) | 1/158 (1%) | 0/65 (0%) | 0/76 (0%) |

Not in the draft: deny (excluded: admit / deny / acknowledge); admit (excluded: admit / deny / acknowledge); liar (excluded: the question's own word)

## preans_slot2

| family | side | members | lies | truths | no-pressure truths | unrelated | lies that deny | truths that deny |
|---|---|---|---|---|---|---|---|---|
| fact (fact / the facts) | unclear | `事实`, `␣fact`, `事实上`, `␣factual`, `␣facts`, `的事实`, `fact`, `事实和`, `facts`, `␣Fact`, `Fact`, `FACT`, `␣FACT`, `␣Facts`, `_fact`, `上述事实`, `␣realities`, `␣realidad`, `实际`, `符合`, `实际上`, `的实际`, `实际的`, `是否符合`, `实际上是`, `与实际`, `犯罪事实`, `求实`, `␣reales` | 141/152 (93%) | 64/81 (79%) | 136/138 (99%) | 124/158 (78%) | 61/65 (94%) | 59/76 (78%) |
| true (true, real) | truth | `␣true`, `true`, `␣real`, `True`, `␣True`, `real`, `=true`, `_real`, `_true`, `,true`, `␣genuine`, `␣REAL`, `.real`, `>true`, `␣genuinely`, `真`, `真的`, `成立`, `真正`, `真实`, `真实性`, `确实`, `真正的`, `的确`, `真的是`, `真实的`, `是真的`, `真實`, `的真`, `确实是`, `的真实`, `属实`, `的真实性`, `的真正` | 121/152 (80%) | 43/81 (53%) | 98/138 (71%) | 81/158 (51%) | 46/65 (71%) | 39/76 (51%) |
| truthful (truthful, telling it as it is) | truth | `␣truthful`, `如实`, `实事求是` | 109/152 (72%) | 45/81 (56%) | 115/138 (83%) | 40/158 (25%) | 50/65 (77%) | 42/76 (55%) |
| reality (the actual state of affairs) | unclear | `实际情况`, `␣reality`, `现实`, `␣Reality`, `现实中`, `根据实际情况`, `与现实`, `Reality`, `的现实` | 112/152 (74%) | 32/81 (40%) | 41/138 (30%) | 11/158 (7%) | 42/65 (65%) | 30/76 (39%) |
| conceal (concealing / covering up information) | lie | `隐瞒`, `掩盖`, `掩饰`, `␣conceal`, `␣concealed`, `瞒`, `遮盖`, `遮蔽`, `遮掩`, `遮住` | 98/152 (64%) | 21/81 (26%) | 12/138 (9%) | 0/158 (0%) | 41/65 (63%) | 18/76 (24%) |
| knowing (with knowledge / knowingly) | unclear | `明知`, `知情`, `␣knowingly`, `␣knowing`, `␣Knowing` | 98/152 (64%) | 18/81 (22%) | 49/138 (36%) | 2/158 (1%) | 40/65 (62%) | 16/76 (21%) |
| false (false, untrue) | lie | `␣false`, `␣False`, `false`, `False`, `␣FALSE`, `>false`, `␣fals`, `␣falsely`, `␣untrue`, `/false`, `␣falsehood`, `假`, `虚假`, `假的`, `真假`, `不实` | 91/152 (60%) | 17/81 (21%) | 17/138 (12%) | 4/158 (3%) | 43/65 (66%) | 15/76 (20%) |
| fabricate (making something up) | lie | `虚构`, `␣fabricated`, `␣invented`, `␣fabrication`, `凭空`, `␣invent`, `伪造`, `␣invention` | 81/152 (53%) | 24/81 (30%) | 30/138 (22%) | 34/158 (22%) | 34/65 (52%) | 22/76 (29%) |
| conceal (concealing the truth) | lie | `隐瞒`, `␣conceal`, `␣concealed`, `瞒`, `掩`, `遮`, `隐` | 87/152 (57%) | 17/81 (21%) | 12/138 (9%) | 0/158 (0%) | 36/65 (55%) | 15/76 (20%) |
| objective (objective, impartial) | unclear | `客观`, `␣objective`, `␣objectively` | 68/152 (45%) | 31/81 (38%) | 89/138 (64%) | 55/158 (35%) | 32/65 (49%) | 31/76 (41%) |
| honest (honest / honesty) | truth | `诚`, `诚实`, `␣honest`, `␣honesty`, `␣honestly`, `诚信`, `诚实守信` | 47/152 (31%) | 47/81 (58%) | 57/138 (41%) | 86/158 (54%) | 24/65 (37%) | 44/76 (58%) |
| cover up (covering up / glossing over) | lie | `掩盖`, `掩饰`, `遮盖`, `遮掩` | 67/152 (44%) | 12/81 (15%) | 0/138 (0%) | 0/158 (0%) | 28/65 (43%) | 10/76 (13%) |
| contradict (contradiction) | unclear | `␣contradict`, `␣contrad`, `矛盾`, `␣contradictory`, `矛盾的`, `␣contradiction`, `␣contradictions`, `之间的矛盾`, `␣conflicting`, `␣conflict`, `␣contradd` | 43/152 (28%) | 18/81 (22%) | 59/138 (43%) | 6/158 (4%) | 18/65 (28%) | 17/76 (22%) |
| deceive (the act of deceiving) | lie | `欺骗`, `␣deception`, `␣deceptive`, `␣deceive`, `骗`, `欺`, `哄` | 45/152 (30%) | 8/81 (10%) | 0/138 (0%) | 1/158 (1%) | 19/65 (29%) | 6/76 (8%) |
| wrong (wrong, mistaken) | lie | `␣error`, `␣wrong`, `␣WRONG`, `错`, `错误`, `不对`, `错了`, `没错`, `是非`, `误会`, `是错误的` | 24/152 (16%) | 21/81 (26%) | 17/138 (12%) | 28/158 (18%) | 12/65 (18%) | 18/76 (24%) |
| violate (violating (rules, norms)) | unclear | `违背`, `违反`, `违反了`, `违法`, `␣violate`, `␣violating`, `␣violates`, `违规` | 28/152 (18%) | 13/81 (16%) | 25/138 (18%) | 4/158 (3%) | 12/65 (18%) | 11/76 (14%) |
| fiction (fictional, made-up story) | unclear | `␣fictional`, `fiction`, `␣fiction`, `-fiction` | 30/152 (20%) | 8/81 (10%) | 9/138 (7%) | 13/158 (8%) | 15/65 (23%) | 8/76 (11%) |
| intentional (done on purpose) | unclear | `故意`, `␣deliberately`, `刻意`, `␣intentionally`, `␣deliberate`, `␣intentional` | 25/152 (16%) | 7/81 (9%) | 0/138 (0%) | 0/158 (0%) | 14/65 (22%) | 4/76 (5%) |
| compliance (complying with rules) | unclear | `合规`, `␣adherence`, `␣compliance`, `遵守`, `␣comply`, `严格遵守`, `␣compliant`, `␣Compliance`, `␣complying`, `␣adher`, `␣adhere`, `依法` | 13/152 (9%) | 16/81 (20%) | 49/138 (36%) | 7/158 (4%) | 8/65 (12%) | 16/76 (21%) |
| ethics (ethics / morality) | unclear | `␣ethical`, `道德`, `␣moral`, `伦理`, `␣ethics`, `ethical`, `的道德`, `␣Ethics`, `职业道德`, `␣morally`, `␣morality`, `␣morals`, `␣Moral` | 8/152 (5%) | 20/81 (25%) | 0/138 (0%) | 0/158 (0%) | 1/65 (2%) | 19/76 (25%) |
| correct (correct) | truth | `valid`, `␣valid`, `␣correct`, `␣Valid`, `␣correctly`, `correct`, `␣correction`, `_correct`, `Correct`, `␣corrected`, `␣Correct`, `␣corrections`, `␣correctness`, `␣correctamente`, `␣Correction`, `␣correcting`, `_correction`, `Correction`, `␣Corrections`, `␣corrective`, `正确`, `正确的`, `正确的是`, `正确答案`, `纠正`, `的正确`, `无误`, `是正确的`, `正确地`, `是否正确`, `是对的` | 2/152 (1%) | 26/81 (32%) | 113/138 (82%) | 128/158 (81%) | 1/65 (2%) | 26/76 (34%) |
| fake (fake, false-seeming) | lie | `fake`, `␣fake`, `Fake` | 16/152 (11%) | 9/81 (11%) | 9/138 (7%) | 3/158 (2%) | 3/65 (5%) | 7/76 (9%) |
| refuse (refusing / declining) | unclear | `␣refusal`, `拒绝`, `␣refused`, `␣refusing`, `拒`, `␣refuse`, `␣refuses`, `␣refus`, `拒絕`, `拒绝了`, `␣decline`, `拒不`, `␣declined`, `␣declines`, `␣отказ`, `␣declining`, `␣отказа` | 0/152 (0%) | 25/81 (31%) | 3/138 (2%) | 0/158 (0%) | 0/65 (0%) | 25/76 (33%) |
| accurate (accurate) | truth | `␣accur`, `␣accurate`, `␣accuracy`, `␣accurately`, `accuracy`, `accur`, `␣Accuracy`, `准确`, `准确性`, `准确的`, `准确地` | 6/152 (4%) | 19/81 (23%) | 106/138 (77%) | 102/158 (65%) | 3/65 (5%) | 19/76 (25%) |
| hide (hiding something) | lie | `隐藏`, `␣hiding`, `␣hide`, `Hide`, `␣hides`, `␣hidden`, `hide`, `隐藏着`, `隐藏的`, `␣Hide`, `_hide`, `-hide`, `␣hid`, `Hidden` | 16/152 (11%) | 5/81 (6%) | 1/138 (1%) | 0/158 (0%) | 6/65 (9%) | 4/76 (5%) |
| role-play (playing a role) | unclear | `扮演`, `角色扮演` | 11/152 (7%) | 8/81 (10%) | 1/138 (1%) | 0/158 (0%) | 4/65 (6%) | 8/76 (11%) |
| secret (secret, kept secret) | lie | `␣secret`, `␣secretly`, `秘密`, `的秘密`, `保密`, `␣Secret`, `Secret`, `secret`, `_secret`, `-secret`, `␣confidentiality` | 15/152 (10%) | 3/81 (4%) | 0/138 (0%) | 0/158 (0%) | 6/65 (9%) | 3/76 (4%) |
| omit (leaving something out) | lie | `␣omit`, `omit`, `省略`, `␣omission`, `␣omitted`, `␣OMIT` | 12/152 (8%) | 5/81 (6%) | 0/138 (0%) | 0/158 (0%) | 7/65 (11%) | 4/76 (5%) |
| candid (candid, frank) | truth | `坦诚` | 0/152 (0%) | 14/81 (17%) | 7/138 (5%) | 6/158 (4%) | 0/65 (0%) | 13/76 (17%) |
| integrity (integrity, good faith) | truth | `诚信`, `␣integrity`, `诚实守信` | 5/152 (3%) | 9/81 (11%) | 2/138 (1%) | 0/158 (0%) | 2/65 (3%) | 7/76 (9%) |
| withhold (withholding information) | lie | `␣withholding`, `␣withhold`, `␣withheld` | 7/152 (5%) | 6/81 (7%) | 0/138 (0%) | 0/158 (0%) | 2/65 (3%) | 5/76 (7%) |
| incorrect (incorrect) | lie | `␣incorrect`, `␣inaccur`, `␣incorrectly`, `␣inaccurate`, `不符合`, `有误`, `错误的是` | 4/152 (3%) | 8/81 (10%) | 4/138 (3%) | 27/158 (17%) | 0/65 (0%) | 7/76 (9%) |
| downplay (downplaying, playing down) | lie | `淡化` | 7/152 (5%) | 4/81 (5%) | 0/138 (0%) | 0/158 (0%) | 5/65 (8%) | 4/76 (5%) |
| disclose (disclosing, making public) | truth | `公开`, `␣disclosure`, `␣disclosures`, `披露`, `信息披露` | 2/152 (1%) | 8/81 (10%) | 10/138 (7%) | 1/158 (1%) | 1/65 (2%) | 6/76 (8%) |
| mislead (leading someone to a false belief) | lie | `␣misleading`, `误导`, `误导性` | 6/152 (4%) | 3/81 (4%) | 0/138 (0%) | 0/158 (0%) | 3/65 (5%) | 2/76 (3%) |
| misinformation (false information given out) | lie | `虚假信息`, `␣misinformation` | 8/152 (5%) | 1/81 (1%) | 2/138 (1%) | 0/158 (0%) | 5/65 (8%) | 1/76 (1%) |
| evade (evading the question) | lie | `回避`, `␣evasion`, `␣evade` | 7/152 (5%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 4/65 (6%) | 1/76 (1%) |
| confess (confessing, coming clean) | truth | `坦白`, `␣confess` | 0/152 (0%) | 8/81 (10%) | 1/138 (1%) | 1/158 (1%) | 0/65 (0%) | 7/76 (9%) |
| transparent (transparency) | truth | `␣transparency`, `透明`, `-transparent`, `透明的`, `␣Transparency`, `␣transparent`, `透明度`, `transparent` | 0/152 (0%) | 8/81 (10%) | 2/138 (1%) | 6/158 (4%) | 0/65 (0%) | 8/76 (11%) |
| silence (staying silent) | unclear | `沉默`, `␣silence`, `␣silent`, `␣silently` | 5/152 (3%) | 2/81 (2%) | 0/138 (0%) | 0/158 (0%) | 3/65 (5%) | 2/76 (3%) |
| cover (covering (up)) | lie | `␣cover`, `cover`, `␣covers`, `␣Cover`, `Cover`, `␣covering`, `_cover`, `COVER`, `-cover`, `␣COVER` | 5/152 (3%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 3/65 (5%) | 1/76 (1%) |
| pretend (pretending) | lie | `␣pretending`, `假装`, `伪装` | 5/152 (3%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 2/65 (3%) | 0/76 (0%) |
| deviate (deviating) | unclear | `偏离`, `背离` | 3/152 (2%) | 2/81 (2%) | 0/138 (0%) | 0/158 (0%) | 0/65 (0%) | 1/76 (1%) |
| reveal (revealing) | truth | `揭露`, `揭示`, `␣revealed`, `␣reveal`, `␣reveals`, `␣revealing`, `揭` | 1/152 (1%) | 3/81 (4%) | 2/138 (1%) | 0/158 (0%) | 0/65 (0%) | 2/76 (3%) |
| disguise (disguising / masquerading) | lie | `伪装` | 3/152 (2%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 2/65 (3%) | 0/76 (0%) |
| technically (technically (true)) | unclear | `␣technically` | 3/152 (2%) | 0/81 (0%) | 0/138 (0%) | 2/158 (1%) | 0/65 (0%) | 0/76 (0%) |
| confidential (confidentiality) | unclear | `␣confidentiality` | 2/152 (1%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 1/65 (2%) | 0/76 (0%) |
| partial (partial, incomplete) | unclear | `␣partially`, `␣partial`, `不完全` | 1/152 (1%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 0/65 (0%) | 1/76 (1%) |
| inaccurate (inaccurate) | lie | `准确性和`, `不准确` | 2/152 (1%) | 0/81 (0%) | 2/138 (1%) | 8/158 (5%) | 1/65 (2%) | 0/76 (0%) |
| dishonest (being dishonest) | lie | `␣dishonest` | 0/152 (0%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 0/65 (0%) | 0/76 (0%) |
| unaware (not informed) | unclear | `不知情` | 0/152 (0%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 0/65 (0%) | 1/76 (1%) |
| unethical (unethical) | lie | `␣unethical` | 0/152 (0%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 0/65 (0%) | 1/76 (1%) |
| apology (apologizing) | unclear | `道歉` | 0/152 (0%) | 1/81 (1%) | 0/138 (0%) | 1/158 (1%) | 0/65 (0%) | 1/76 (1%) |
| truth (the truth) | truth | `求真` | 0/152 (0%) | 0/81 (0%) | 1/138 (1%) | 0/158 (0%) | 0/65 (0%) | 0/76 (0%) |

Not in the draft: deny (excluded: admit / deny / acknowledge); admit (excluded: admit / deny / acknowledge); acknowledge (excluded: admit / deny / acknowledge); liar (excluded: the question's own word)

## preans_slot3

| family | side | members | lies | truths | no-pressure truths | unrelated | lies that deny | truths that deny |
|---|---|---|---|---|---|---|---|---|
| false (false, untrue) | lie | `␣false`, `␣False`, `false`, `False`, `FALSE`, `>false`, `_false`, `.assertFalse`, `.False`, `.false`, `/false`, `假`, `真假` | 93/152 (61%) | 72/81 (89%) | 138/138 (100%) | 151/158 (96%) | 46/65 (71%) | 71/76 (93%) |
| disclose (disclosing, making public) | truth | `公开`, `公布` | 95/152 (62%) | 61/81 (75%) | 116/138 (84%) | 93/158 (59%) | 28/65 (43%) | 58/76 (76%) |
| comply (complying / abiding by rules) | unclear | `守法`, `恪守`, `依法`, `合规` | 90/152 (59%) | 42/81 (52%) | 14/138 (10%) | 6/158 (4%) | 40/65 (62%) | 40/76 (53%) |
| apology (apologizing) | unclear | `抱歉`, `Sorry`, `对不起`, `␣sorry`, `␣Sorry`, `␣apologize` | 95/152 (62%) | 31/81 (38%) | 51/138 (37%) | 128/158 (81%) | 53/65 (82%) | 29/76 (38%) |
| law-abiding (law-abiding) | unclear | `守法` | 74/152 (49%) | 25/81 (31%) | 4/138 (3%) | 2/158 (1%) | 27/65 (42%) | 23/76 (30%) |
| refuse (refusing / declining) | unclear | `␣refusal`, `␣refuse`, `拒`, `拒绝`, `␣refus` | 73/152 (48%) | 23/81 (28%) | 7/138 (5%) | 0/158 (0%) | 30/65 (46%) | 21/76 (28%) |
| cannot (first-person refusal formula "I cannot") | unclear | `我无法`, `我不能` | 46/152 (30%) | 20/81 (25%) | 0/138 (0%) | 0/158 (0%) | 23/65 (35%) | 19/76 (25%) |
| compliance (complying with rules) | unclear | `恪守`, `合规`, `␣comply` | 17/152 (11%) | 24/81 (30%) | 9/138 (7%) | 5/158 (3%) | 9/65 (14%) | 23/76 (30%) |
| violate (violating (rules, norms)) | unclear | `违背` | 14/152 (9%) | 15/81 (19%) | 5/138 (4%) | 6/158 (4%) | 7/65 (11%) | 14/76 (18%) |
| hide (hiding something) | lie | `-hide`, `:hidden` | 0/152 (0%) | 3/81 (4%) | 1/138 (1%) | 87/158 (55%) | 0/65 (0%) | 3/76 (4%) |
| fiction (fictional, made-up story) | unclear | `fiction` | 1/152 (1%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 1/65 (2%) | 1/76 (1%) |
| true (true, real) | truth | `␣true`, `␣True`, `>true`, `真`, `的真`, `的確` | 0/152 (0%) | 2/81 (2%) | 5/138 (4%) | 34/158 (22%) | 0/65 (0%) | 2/76 (3%) |
| fact (fact, factual) | truth | `是否符合` | 2/152 (1%) | 0/81 (0%) | 1/138 (1%) | 0/158 (0%) | 1/65 (2%) | 0/76 (0%) |
| wrong (wrong, mistaken) | lie | `␣wrong`, `不对`, `没错` | 0/152 (0%) | 1/81 (1%) | 9/138 (7%) | 2/158 (1%) | 0/65 (0%) | 0/76 (0%) |
| incorrect (incorrect) | lie | `不符合` | 0/152 (0%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 0/65 (0%) | 1/76 (1%) |
| correct (correct) | truth | `正确` | 0/152 (0%) | 0/81 (0%) | 1/138 (1%) | 0/158 (0%) | 0/65 (0%) | 0/76 (0%) |

## preans_slot4

| family | side | members | lies | truths | no-pressure truths | unrelated | lies that deny | truths that deny |
|---|---|---|---|---|---|---|---|---|
| true (true, real) | truth | `␣true`, `true`, `␣real`, `True`, `␣True`, `real`, `␣TRUE`, `真`, `成立`, `真实`, `确实`, `的确`, `是真的`, `属实` | 132/152 (87%) | 74/81 (91%) | 120/138 (87%) | 107/158 (68%) | 49/65 (75%) | 69/76 (91%) |
| false (false, untrue) | lie | `␣false`, `␣False`, `(false`, `false`, `False`, `=False`, `␣FALSE`, `:false`, `FALSE`, `>false`, `_false`, `.assertFalse`, `.False`, `.false`, `/false`, `假`, `假的` | 126/152 (83%) | 79/81 (98%) | 138/138 (100%) | 158/158 (100%) | 63/65 (97%) | 76/76 (100%) |
| honest (honest / honesty) | truth | `诚实`, `␣honest`, `诚`, `␣honesty`, `诚信`, `誠`, `诚恳` | 130/152 (86%) | 47/81 (58%) | 13/138 (9%) | 0/158 (0%) | 53/65 (82%) | 45/76 (59%) |
| objective (objective, impartial) | unclear | `客观`, `␣objectively` | 74/152 (49%) | 48/81 (59%) | 52/138 (38%) | 0/158 (0%) | 39/65 (60%) | 48/76 (63%) |
| integrity (integrity, good faith) | truth | `诚信` | 85/152 (56%) | 35/81 (43%) | 1/138 (1%) | 0/158 (0%) | 44/65 (68%) | 34/76 (45%) |
| cannot (first-person refusal formula "I cannot") | unclear | `我不能`, `我无法` | 101/152 (66%) | 10/81 (12%) | 0/138 (0%) | 0/158 (0%) | 36/65 (55%) | 8/76 (11%) |
| apology (apologizing) | unclear | `抱歉`, `对不起` | 54/152 (36%) | 30/81 (37%) | 11/138 (8%) | 4/158 (3%) | 17/65 (26%) | 29/76 (38%) |
| confess (confessing, coming clean) | truth | `坦白` | 54/152 (36%) | 20/81 (25%) | 0/138 (0%) | 0/158 (0%) | 25/65 (38%) | 19/76 (25%) |
| candid (candid, frank) | truth | `坦诚` | 52/152 (34%) | 14/81 (17%) | 0/138 (0%) | 0/158 (0%) | 28/65 (43%) | 13/76 (17%) |
| truthful (truthful, telling it as it is) | truth | `␣truthful`, `如实` | 29/152 (19%) | 14/81 (17%) | 4/138 (3%) | 0/158 (0%) | 16/65 (25%) | 14/76 (18%) |
| fabricate (making something up) | lie | `虚构` | 22/152 (14%) | 2/81 (2%) | 0/138 (0%) | 0/158 (0%) | 4/65 (6%) | 0/76 (0%) |
| fiction (fictional, made-up story) | unclear | `␣fictional`, `fiction`, `␣Fiction`, `␣fiction` | 20/152 (13%) | 4/81 (5%) | 0/138 (0%) | 0/158 (0%) | 6/65 (9%) | 2/76 (3%) |
| fact (fact / the facts) | unclear | `事实`, `␣factual`, `符合` | 10/152 (7%) | 9/81 (11%) | 9/138 (7%) | 0/158 (0%) | 6/65 (9%) | 9/76 (12%) |
| violate (violating (rules, norms)) | unclear | `违反`, `违背`, `违反了` | 13/152 (9%) | 3/81 (4%) | 2/138 (1%) | 0/158 (0%) | 4/65 (6%) | 2/76 (3%) |
| wrong (wrong, mistaken) | lie | `错`, `不对`, `误会` | 16/152 (11%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 9/65 (14%) | 0/76 (0%) |
| secret (secret, kept secret) | lie | `保密`, `秘密` | 13/152 (9%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 5/65 (8%) | 0/76 (0%) |
| ethics (ethics / morality) | unclear | `␣ethical`, `␣ethics`, `伦理`, `道德`, `职业道德` | 12/152 (8%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 2/65 (3%) | 1/76 (1%) |
| partial (partial, incomplete) | unclear | `␣partially`, `␣partial`, `␣Partial` | 5/152 (3%) | 8/81 (10%) | 2/138 (1%) | 0/158 (0%) | 4/65 (6%) | 7/76 (9%) |
| deceive (the act of deceiving) | lie | `欺骗`, `␣deception` | 8/152 (5%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 1/65 (2%) | 0/76 (0%) |
| downplay (downplaying, playing down) | lie | `淡化` | 7/152 (5%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 4/65 (6%) | 0/76 (0%) |
| conceal (concealing the truth) | lie | `隐瞒`, `隐` | 5/152 (3%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 2/65 (3%) | 0/76 (0%) |
| silence (staying silent) | unclear | `沉默`, `␣silence` | 5/152 (3%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 0/65 (0%) | 0/76 (0%) |
| accurate (accurate) | truth | `准确` | 0/152 (0%) | 5/81 (6%) | 2/138 (1%) | 0/158 (0%) | 0/65 (0%) | 5/76 (7%) |
| refuse (refusing / declining) | unclear | `拒绝`, `␣refuse` | 1/152 (1%) | 2/81 (2%) | 0/138 (0%) | 0/158 (0%) | 0/65 (0%) | 2/76 (3%) |
| comply (complying / abiding by rules) | unclear | `依法`, `␣adher` | 3/152 (2%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 2/65 (3%) | 0/76 (0%) |
| reality (the actual state of affairs) | unclear | `根据实际情况` | 1/152 (1%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 0/65 (0%) | 1/76 (1%) |
| knowing (with knowledge / knowingly) | unclear | `明知` | 1/152 (1%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 0/65 (0%) | 1/76 (1%) |
| correct (correct) | truth | `valid`, `␣correct`, `正确` | 1/152 (1%) | 1/81 (1%) | 12/138 (9%) | 0/158 (0%) | 1/65 (2%) | 1/76 (1%) |
| hide (hiding something) | lie | `隐藏` | 1/152 (1%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 0/65 (0%) | 0/76 (0%) |
| withhold (withholding information) | lie | `␣withholding` | 1/152 (1%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 1/65 (2%) | 0/76 (0%) |
| omit (leaving something out) | lie | `省略` | 1/152 (1%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 0/65 (0%) | 0/76 (0%) |
| sincere (sincere) | truth | `诚恳` | 1/152 (1%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 0/65 (0%) | 0/76 (0%) |
| transparent (transparency) | truth | `透明` | 0/152 (0%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 0/65 (0%) | 1/76 (1%) |
| contradict (contradiction) | unclear | `␣contradict`, `␣contradiction` | 0/152 (0%) | 1/81 (1%) | 2/138 (1%) | 0/158 (0%) | 0/65 (0%) | 1/76 (1%) |

Not in the draft: deny (excluded: admit / deny / acknowledge); admit (excluded: admit / deny / acknowledge); acknowledge (excluded: admit / deny / acknowledge); truth (excluded: truth from the question on)
