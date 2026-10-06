# Draft families: qwen3.6-27b, logit lens, part Q1_bare, group think

Written by `scripts/apply_family_decisions.py` (2026-10-01; draft, not frozen). Counts are `present / transcripts (share)`
on the build split.

## think_slot0

| family | side | members | lies | truths | no-pressure truths | unrelated | lies that deny | truths that deny |
|---|---|---|---|---|---|---|---|---|
| clarify (clarifying, setting the record straight) | unclear | `澄清`, `␣clarification` | 108/152 (71%) | 73/81 (90%) | 138/138 (100%) | 158/158 (100%) | 32/53 (60%) | 66/74 (89%) |
| clever (clever, quick-witted) | unclear | `␣clever`, `伶俐` | 111/152 (73%) | 59/81 (73%) | 13/138 (9%) | 128/158 (81%) | 27/53 (51%) | 54/74 (73%) |
| violation (breaking a rule) | unclear | `违规` | 58/152 (38%) | 23/81 (28%) | 10/138 (7%) | 0/158 (0%) | 31/53 (58%) | 20/74 (27%) |
| plausible (plausible-sounding) | unclear | `␣plausible` | 53/152 (35%) | 19/81 (23%) | 0/138 (0%) | 0/158 (0%) | 13/53 (25%) | 17/74 (23%) |
| wrong (wrong, mistaken) | lie | `_WRONG`, `指正` | 20/152 (13%) | 9/81 (11%) | 5/138 (4%) | 0/158 (0%) | 4/53 (8%) | 7/74 (9%) |
| sincere (sincerity, genuine feeling) | truth | `真诚`, `真情` | 13/152 (9%) | 15/81 (19%) | 24/138 (17%) | 25/158 (16%) | 4/53 (8%) | 14/74 (19%) |
| sensitive (a sensitive matter) | unclear | `_sensitive`, `敏感` | 12/152 (8%) | 8/81 (10%) | 0/138 (0%) | 0/158 (0%) | 8/53 (15%) | 7/74 (9%) |
| reveal (exposing, uncovering) | truth | `揭` | 4/152 (3%) | 4/81 (5%) | 4/138 (3%) | 21/158 (13%) | 0/53 (0%) | 2/74 (3%) |
| compliance (complying with rules) | unclear | `合规` | 6/152 (4%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 3/53 (6%) | 1/74 (1%) |
| guilt (guilt, crime) | unclear | `罪的` | 2/152 (1%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 0/53 (0%) | 1/74 (1%) |
| legal issue (a legal problem) | unclear | `法律问题` | 1/152 (1%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 1/53 (2%) | 0/74 (0%) |
| conceal (to conceal, to hide) | lie | `藏` | 0/152 (0%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 0/53 (0%) | 1/74 (1%) |
| false (false, untrue) | lie | `真假` | 0/152 (0%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 0/53 (0%) | 1/74 (1%) |

Not in the draft: truth (excluded: truth from the question on)

## think_slot1

| family | side | members | lies | truths | no-pressure truths | unrelated | lies that deny | truths that deny |
|---|---|---|---|---|---|---|---|---|
| secretly (quietly, stealthily) | unclear | `悄`, `悄悄的` | 68/152 (45%) | 20/81 (25%) | 79/138 (57%) | 88/158 (56%) | 25/53 (47%) | 16/74 (22%) |
| without permission (acting without permission) | unclear | `未经允许` | 46/152 (30%) | 28/81 (35%) | 37/138 (27%) | 4/158 (3%) | 16/53 (30%) | 26/74 (35%) |
| promise (promising) | unclear | `许诺` | 48/152 (32%) | 25/81 (31%) | 0/138 (0%) | 2/158 (1%) | 13/53 (25%) | 24/74 (32%) |
| disclose (disclosing everything (交底)) | truth | `交底` | 26/152 (17%) | 7/81 (9%) | 0/138 (0%) | 0/158 (0%) | 8/53 (15%) | 7/74 (9%) |
| wrong (wrong, mistaken) | lie | `␣mistakes`, `_WRONG`, `指正` | 3/152 (2%) | 0/81 (0%) | 40/138 (29%) | 9/158 (6%) | 3/53 (6%) | 0/74 (0%) |
| violation (breaking a rule) | unclear | `␣violated` | 1/152 (1%) | 1/81 (1%) | 1/138 (1%) | 0/158 (0%) | 1/53 (2%) | 1/74 (1%) |
| neutral (neutrality) | unclear | `␣neutrality` | 2/152 (1%) | 0/81 (0%) | 1/138 (1%) | 0/158 (0%) | 1/53 (2%) | 0/74 (0%) |
| objective (objective) | unclear | `␣objective` | 0/152 (0%) | 0/81 (0%) | 1/138 (1%) | 0/158 (0%) | 0/53 (0%) | 0/74 (0%) |
| correct (correct) | truth | `纠正` | 0/152 (0%) | 0/81 (0%) | 4/138 (3%) | 0/158 (0%) | 0/53 (0%) | 0/74 (0%) |

Not in the draft: deceive (excluded: the question's own word)

## think_slot2

| family | side | members | lies | truths | no-pressure truths | unrelated | lies that deny | truths that deny |
|---|---|---|---|---|---|---|---|---|
| not do (not carrying out / not doing) | unclear | `不进行`, `不做` | 134/152 (88%) | 72/81 (89%) | 128/138 (93%) | 59/158 (37%) | 38/53 (72%) | 65/74 (88%) |
| cannot (I cannot / unable to) | unclear | `我不能`, `我无法`, `不能`, `不能说`, `可不能`, `不能完全` | 136/152 (89%) | 68/81 (84%) | 13/138 (9%) | 2/158 (1%) | 48/53 (91%) | 63/74 (85%) |
| not fully (cannot fully) | unclear | `不能完全` | 121/152 (80%) | 44/81 (54%) | 4/138 (3%) | 0/158 (0%) | 44/53 (83%) | 39/74 (53%) |
| legal (legality, legally) | unclear | `在法律`, `␣legally`, `/legal`, `␣legality` | 118/152 (78%) | 45/81 (56%) | 18/138 (13%) | 0/158 (0%) | 40/53 (75%) | 40/74 (54%) |
| ethics (ethics, ethical) | unclear | `␣ethics`, `␣ethical`, `职业道德` | 97/152 (64%) | 31/81 (38%) | 11/138 (8%) | 1/158 (1%) | 27/53 (51%) | 24/74 (32%) |
| stance (one's position (立场)) | unclear | `立场` | 75/152 (49%) | 51/81 (63%) | 11/138 (8%) | 0/158 (0%) | 20/53 (38%) | 49/74 (66%) |
| defense (defense) | unclear | `-defense`, `␣defense` | 63/152 (41%) | 34/81 (42%) | 0/138 (0%) | 0/158 (0%) | 26/53 (49%) | 34/74 (46%) |
| neutral (neutral) | unclear | `中立` | 61/152 (40%) | 30/81 (37%) | 0/138 (0%) | 0/158 (0%) | 27/53 (51%) | 28/74 (38%) |
| true (true, real) | truth | `␣true`, `True`, `␣TRUE`, `TRUE`, `␣genuinely`, `确实`, `是真的`, `的確` | 66/152 (43%) | 20/81 (25%) | 66/138 (48%) | 1/158 (1%) | 10/53 (19%) | 15/74 (20%) |
| sorry (apologizing) | unclear | `抱歉`, `对不起`, `Sorry` | 47/152 (31%) | 23/81 (28%) | 71/138 (51%) | 135/158 (85%) | 25/53 (47%) | 22/74 (30%) |
| breach (breach, violation) | unclear | `␣breach`, `␣breaches`, `␣breached` | 45/152 (30%) | 14/81 (17%) | 14/138 (10%) | 14/158 (9%) | 26/53 (49%) | 11/74 (15%) |
| forged (forged, faked) | lie | `␣forged`, `forge` | 29/152 (19%) | 18/81 (22%) | 66/138 (48%) | 76/158 (48%) | 4/53 (8%) | 16/74 (22%) |
| sensitive (a sensitive matter) | unclear | `敏感`, `␣sensitive` | 29/152 (19%) | 17/81 (21%) | 56/138 (41%) | 103/158 (65%) | 17/53 (32%) | 16/74 (22%) |
| not reply (not answering) | unclear | `不回` | 37/152 (24%) | 7/81 (9%) | 0/138 (0%) | 1/158 (1%) | 8/53 (15%) | 6/74 (8%) |
| direct (direct, straightforward) | unclear | `直接的` | 23/152 (15%) | 8/81 (10%) | 5/138 (4%) | 0/158 (0%) | 16/53 (30%) | 8/74 (11%) |
| clever (clever, quick-witted) | unclear | `伶俐` | 24/152 (16%) | 7/81 (9%) | 10/138 (7%) | 0/158 (0%) | 2/53 (4%) | 7/74 (9%) |
| refuse (refusing) | unclear | `拒`, `拒不` | 26/152 (17%) | 4/81 (5%) | 1/138 (1%) | 0/158 (0%) | 14/53 (26%) | 3/74 (4%) |
| candid (candid, frank) | truth | `坦诚` | 10/152 (7%) | 2/81 (2%) | 0/138 (0%) | 0/158 (0%) | 2/53 (4%) | 2/74 (3%) |
| honest (honesty) | truth | `␣honestly`, `诚`, `誠` | 2/152 (1%) | 2/81 (2%) | 92/138 (67%) | 53/158 (34%) | 0/53 (0%) | 1/74 (1%) |
| upright (upright, of integrity) | truth | `正直` | 0/152 (0%) | 3/81 (4%) | 0/138 (0%) | 5/158 (3%) | 0/53 (0%) | 3/74 (4%) |
| conceal (to conceal, to hide) | lie | `藏` | 1/152 (1%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 1/53 (2%) | 1/74 (1%) |
| false (false, untrue) | lie | `=False`, `:false`, `>false`, `_false`, `.assertFalse`, `.FALSE` | 1/152 (1%) | 1/81 (1%) | 3/138 (2%) | 0/158 (0%) | 1/53 (2%) | 1/74 (1%) |
| innocent (innocent, clean record (清白)) | unclear | `清白` | 0/152 (0%) | 1/81 (1%) | 16/138 (12%) | 25/158 (16%) | 0/53 (0%) | 0/74 (0%) |
| correct (correct) | truth | `␣correction`, `␣corrected`, `纠正` | 0/152 (0%) | 0/81 (0%) | 0/138 (0%) | 2/158 (1%) | 0/53 (0%) | 0/74 (0%) |
| wrong (wrong, mistaken) | lie | `错` | 0/152 (0%) | 0/81 (0%) | 0/138 (0%) | 4/158 (3%) | 0/53 (0%) | 0/74 (0%) |

Not in the draft: deceive (excluded: the question's own word)

## think_slot3

| family | side | members | lies | truths | no-pressure truths | unrelated | lies that deny | truths that deny |
|---|---|---|---|---|---|---|---|---|
| confess (coming clean, confessing (坦白)) | truth | `坦白` | 130/152 (86%) | 71/81 (88%) | 127/138 (92%) | 155/158 (98%) | 34/53 (64%) | 65/74 (88%) |
| true (true, real) | truth | `␣true`, `true`, `True`, `␣True`, `␣TRUE`, `TRUE`, `.True`, `确实`, `的确`, `的真`, `确实是` | 122/152 (80%) | 75/81 (93%) | 138/138 (100%) | 111/158 (70%) | 30/53 (57%) | 68/74 (92%) |
| honest (honesty) | truth | `诚`, `誠`, `诚实`, `␣honestly`, `␣honesty`, `␣honest`, `␣truthful` | 126/152 (83%) | 53/81 (65%) | 106/138 (77%) | 133/158 (84%) | 32/53 (60%) | 48/74 (65%) |
| sorry (apologizing) | unclear | `抱歉`, `对不起`, `␣apologize`, `␣apologies`, `道歉` | 109/152 (72%) | 56/81 (69%) | 61/138 (44%) | 55/158 (35%) | 30/53 (57%) | 50/74 (68%) |
| candid (candid, frank) | truth | `坦诚` | 104/152 (68%) | 49/81 (60%) | 23/138 (17%) | 114/158 (72%) | 28/53 (53%) | 46/74 (62%) |
| negate (negating, rejecting a claim) | unclear | `否定` | 49/152 (32%) | 61/81 (75%) | 62/138 (45%) | 8/158 (5%) | 38/53 (72%) | 60/74 (81%) |
| false (false, untrue) | lie | `␣false`, `␣False`, `false`, `False`, `=False`, `␣FALSE`, `FALSE`, `>false`, `_false`, `.False`, `/false`, `假`, `假的` | 40/152 (26%) | 52/81 (64%) | 134/138 (97%) | 77/158 (49%) | 29/53 (55%) | 51/74 (69%) |
| ethics (ethics, ethical) | unclear | `␣ethical`, `伦理`, `道德` | 56/152 (37%) | 6/81 (7%) | 0/138 (0%) | 0/158 (0%) | 5/53 (9%) | 5/74 (7%) |
| clarify (clarifying, setting the record straight) | unclear | `澄清`, `␣clarification` | 32/152 (21%) | 17/81 (21%) | 4/138 (3%) | 2/158 (1%) | 20/53 (38%) | 16/74 (22%) |
| sincere (sincerity) | truth | `␣sincerely`, `␣sincere`, `真诚`, `真诚的`, `诚恳`, `诚挚` | 30/152 (20%) | 9/81 (11%) | 0/138 (0%) | 0/158 (0%) | 12/53 (23%) | 9/74 (12%) |
| wrong (wrong, mistaken) | lie | `不对`, `没错`, `是非` | 28/152 (18%) | 8/81 (10%) | 7/138 (5%) | 0/158 (0%) | 14/53 (26%) | 6/74 (8%) |
| objective (objective) | unclear | `客观`, `␣objectively` | 10/152 (7%) | 17/81 (21%) | 23/138 (17%) | 1/158 (1%) | 2/53 (4%) | 16/74 (22%) |
| upright (upright, of integrity) | truth | `正直` | 5/152 (3%) | 13/81 (16%) | 3/138 (2%) | 2/158 (1%) | 3/53 (6%) | 12/74 (16%) |
| misunderstanding (misunderstanding) | unclear | `误会` | 8/152 (5%) | 10/81 (12%) | 1/138 (1%) | 5/158 (3%) | 6/53 (11%) | 10/74 (14%) |
| cannot (I cannot / unable to) | unclear | `我不能`, `我无法`, `绝对不能` | 12/152 (8%) | 5/81 (6%) | 0/138 (0%) | 0/158 (0%) | 5/53 (9%) | 4/74 (5%) |
| correct (correct) | truth | `正确`, `纠正` | 10/152 (7%) | 7/81 (9%) | 0/138 (0%) | 2/158 (1%) | 3/53 (6%) | 6/74 (8%) |
| fact (fact, factual) | truth | `符合`, `事实`, `实际上` | 9/152 (6%) | 6/81 (7%) | 2/138 (1%) | 2/158 (1%) | 3/53 (6%) | 6/74 (8%) |
| confidential (keeping confidential) | unclear | `保密`, `␣confidential` | 12/152 (8%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 7/53 (13%) | 0/74 (0%) |
| privately (privately, in private) | unclear | `私下` | 10/152 (7%) | 2/81 (2%) | 0/138 (0%) | 0/158 (0%) | 4/53 (8%) | 1/74 (1%) |
| public (making public, disclosing (公开)) | truth | `公开` | 7/152 (5%) | 3/81 (4%) | 0/138 (0%) | 0/158 (0%) | 5/53 (9%) | 2/74 (3%) |
| fictional (fictional) | unclear | `␣fictional` | 6/152 (4%) | 3/81 (4%) | 0/138 (0%) | 0/158 (0%) | 0/53 (0%) | 3/74 (4%) |
| direct (direct, straightforward) | unclear | `直接的`, `直接` | 6/152 (4%) | 3/81 (4%) | 0/138 (0%) | 0/158 (0%) | 5/53 (9%) | 3/74 (4%) |
| hide (covering up, concealing) | lie | `掩` | 7/152 (5%) | 1/81 (1%) | 7/138 (5%) | 0/158 (0%) | 2/53 (4%) | 1/74 (1%) |
| compliance (complying with rules) | unclear | `合规` | 8/152 (5%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 3/53 (6%) | 0/74 (0%) |
| guilt (guilt, crime) | unclear | `罪` | 3/152 (2%) | 4/81 (5%) | 0/138 (0%) | 21/158 (13%) | 1/53 (2%) | 4/74 (5%) |
| simulation (a simulation) | unclear | `␣simulation` | 2/152 (1%) | 4/81 (5%) | 0/138 (0%) | 0/158 (0%) | 0/53 (0%) | 4/74 (5%) |
| forgive (asking forgiveness) | unclear | `␣forgive` | 4/152 (3%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 3/53 (6%) | 0/74 (0%) |
| ashamed (shame, guilt (愧)) | unclear | `愧` | 4/152 (3%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 0/53 (0%) | 0/74 (0%) |
| confident (confidence) | unclear | `␣confidently`, `␣confident` | 2/152 (1%) | 2/81 (2%) | 0/138 (0%) | 0/158 (0%) | 2/53 (4%) | 2/74 (3%) |
| refuse (refusing) | unclear | `拒绝` | 2/152 (1%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 2/53 (4%) | 1/74 (1%) |
| accurate (accurate) | truth | `准确` | 1/152 (1%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 1/53 (2%) | 1/74 (1%) |
| disguise (disguise, pretense) | lie | `伪装` | 1/152 (1%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 0/53 (0%) | 0/74 (0%) |
| transparent (transparency) | truth | `␣transparency`, `透明`, `透明的` | 1/152 (1%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 1/53 (2%) | 0/74 (0%) |
| not do (not doing) | unclear | `不做` | 1/152 (1%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 0/53 (0%) | 0/74 (0%) |
| promise (promising) | unclear | `Promise` | 1/152 (1%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 1/53 (2%) | 0/74 (0%) |
| transparency (being transparent) | truth | `␣transparency` | 1/152 (1%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 1/53 (2%) | 0/74 (0%) |
| lie (Japanese) (a lie) | lie | `嘘` | 1/152 (1%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 0/53 (0%) | 0/74 (0%) |
| incorrect (incorrect) | lie | `不符合` | 0/152 (0%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 0/53 (0%) | 1/74 (1%) |

Not in the draft: truth (excluded: truth from the question on); admit (excluded: admit / deny / acknowledge); deny (excluded: admit / deny / acknowledge); fake (held back: no undisputed member left)
