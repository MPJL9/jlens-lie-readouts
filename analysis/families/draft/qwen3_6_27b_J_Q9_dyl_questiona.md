# Draft families: qwen3.6-27b, J-lens, part Q9_dyl, group questiona

Written by `scripts/apply_family_decisions.py` (2026-10-01; draft, not frozen). Counts are `present / transcripts (share)`
on the build split.

## q_tok0

| family | side | members | lies | truths | no-pressure truths | unrelated | lies that deny | truths that deny |
|---|---|---|---|---|---|---|---|---|
| mistake (a mistake) | unclear | `␣mistake` | 2/152 (1%) | 8/81 (10%) | 13/138 (9%) | 9/158 (6%) | 2/65 (3%) | 8/76 (11%) |
| misunderstand (misunderstanding) | unclear | `␣misunderstood`, `␣misunderstand`, `␣misunderstanding` | 3/152 (2%) | 5/81 (6%) | 5/138 (4%) | 0/158 (0%) | 2/65 (3%) | 5/76 (7%) |
| deliberate (doing something on purpose) | unclear | `␣intentionally`, `␣intentional`, `␣deliberately`, `␣deliberate`, `␣purposely`, `故意` | 2/152 (1%) | 3/81 (4%) | 0/138 (0%) | 0/158 (0%) | 2/65 (3%) | 3/76 (4%) |
| knowingly (doing something with knowledge) | unclear | `␣knowingly` | 3/152 (2%) | 2/81 (2%) | 2/138 (1%) | 0/158 (0%) | 3/65 (5%) | 2/76 (3%) |
| unauthorized (unauthorized) | unclear | `␣unauthorized`, `␣Unauthorized` | 2/152 (1%) | 3/81 (4%) | 0/138 (0%) | 0/158 (0%) | 0/65 (0%) | 3/76 (4%) |
| fake (fake, not genuine) | lie | `␣Fake`, `␣fake` | 3/152 (2%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 1/65 (2%) | 0/76 (0%) |
| improper (improper) | unclear | `␣improper` | 1/152 (1%) | 1/81 (1%) | 1/138 (1%) | 0/158 (0%) | 1/65 (2%) | 1/76 (1%) |
| wrong (wrong, mistaken) | lie | `␣wrong`, `␣Wrong`, `错`, `误`, `错误`, `错了` | 1/152 (1%) | 1/81 (1%) | 4/138 (3%) | 0/158 (0%) | 1/65 (2%) | 1/76 (1%) |
| bribe (bribery) | unclear | `␣brib` | 1/152 (1%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 1/65 (2%) | 0/76 (0%) |
| fact (fact, factual) | truth | `␣actually` | 1/152 (1%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 0/65 (0%) | 0/76 (0%) |
| false (false, untrue) | lie | `␣fals` | 1/152 (1%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 0/65 (0%) | 0/76 (0%) |
| correct (correct) | truth | `␣correct`, `␣correctly`, `correct`, `␣Correct`, `正确` | 0/152 (0%) | 0/81 (0%) | 0/138 (0%) | 5/158 (3%) | 0/65 (0%) | 0/76 (0%) |
| incorrect (incorrect) | lie | `␣incorrect` | 0/152 (0%) | 0/81 (0%) | 0/138 (0%) | 1/158 (1%) | 0/65 (0%) | 0/76 (0%) |

Not in the draft: truth (excluded: truth from the question on)

## q_tok1

| family | side | members | lies | truths | no-pressure truths | unrelated | lies that deny | truths that deny |
|---|---|---|---|---|---|---|---|---|
| deliberate (doing something on purpose) | unclear | `␣intentionally`, `␣deliberately`, `␣purposely`, `故意`, `␣intentional`, `␣deliberate`, `特意`, `刻意`, `␣sengaja`, `故意的` | 73/152 (48%) | 52/81 (64%) | 64/138 (46%) | 100/158 (63%) | 42/65 (65%) | 50/76 (66%) |
| knowingly (doing something with knowledge) | unclear | `␣knowingly`, `␣consciously`, `明知` | 63/152 (41%) | 32/81 (40%) | 37/138 (27%) | 23/158 (15%) | 36/65 (55%) | 30/76 (39%) |
| accidental (doing something by accident) | unclear | `␣accidentally`, `␣inadvertently`, `␣unintention`, `␣accidental`, `␣mistakenly` | 65/152 (43%) | 21/81 (26%) | 67/138 (49%) | 60/158 (38%) | 30/65 (46%) | 18/76 (24%) |
| mistake (a mistake) | unclear | `␣mistake`, `␣mistakenly`, `␣mistakes`, `␣mistaken` | 48/152 (32%) | 27/81 (33%) | 81/138 (59%) | 108/158 (68%) | 19/65 (29%) | 25/76 (33%) |
| fact (fact, factual) | truth | `␣actually`, `␣actual`, `␣Actually`, `Actually`, `␣factual`, `actually`, `实际`, `实际上` | 52/152 (34%) | 17/81 (21%) | 18/138 (13%) | 27/158 (17%) | 24/65 (37%) | 16/76 (21%) |
| honest (honesty, being honest) | truth | `␣honestly`, `␣honest`, `␣honesty`, `诚实`, `␣Honest` | 45/152 (30%) | 20/81 (25%) | 8/138 (6%) | 0/158 (0%) | 16/65 (25%) | 20/76 (26%) |
| hide (hiding or concealing something) | lie | `隐瞒`, `␣hiding`, `␣conceal`, `␣undisclosed`, `hidden`, `␣hidden`, `␣hide`, `隐藏`, `隐藏的`, `hide`, `-hidden`, `␣Hide`, `␣Hidden`, `␣hides`, `掩盖` | 48/152 (32%) | 15/81 (19%) | 0/138 (0%) | 0/158 (0%) | 20/65 (31%) | 14/76 (18%) |
| conceal (concealing information) | lie | `隐瞒`, `␣conceal`, `掩盖` | 48/152 (32%) | 13/81 (16%) | 0/138 (0%) | 0/158 (0%) | 20/65 (31%) | 12/76 (16%) |
| truthful (being truthful) | truth | `␣truthful` | 50/152 (33%) | 9/81 (11%) | 1/138 (1%) | 0/158 (0%) | 15/65 (23%) | 9/76 (12%) |
| fake (fake, not genuine) | lie | `␣fake`, `fake`, `␣Fake`, `Fake`, `_fake`, `伪造`, `造假`, `弄虚作假` | 49/152 (32%) | 6/81 (7%) | 0/138 (0%) | 0/158 (0%) | 17/65 (26%) | 4/76 (5%) |
| false (false, untrue) | lie | `␣false`, `␣FALSE`, `␣fals`, `␣falsely`, `␣untrue`, `␣falsehood`, `假`, `虚假`, `假的` | 37/152 (24%) | 6/81 (7%) | 0/138 (0%) | 0/158 (0%) | 13/65 (20%) | 5/76 (7%) |
| misunderstand (misunderstanding) | unclear | `␣misunderstand`, `␣misunderstood`, `␣misunderstanding` | 14/152 (9%) | 25/81 (31%) | 49/138 (36%) | 54/158 (34%) | 10/65 (15%) | 24/76 (32%) |
| deceive (the act of deceiving) | lie | `欺骗`, `␣deceive`, `␣deception`, `␣deceived`, `骗`, `␣deceit`, `␣deceptive` | 28/152 (18%) | 7/81 (9%) | 0/138 (0%) | 0/158 (0%) | 5/65 (8%) | 6/76 (8%) |
| misinformation (false information) | lie | `␣misinformation`, `虚假信息` | 28/152 (18%) | 5/81 (6%) | 5/138 (4%) | 2/158 (1%) | 11/65 (17%) | 4/76 (5%) |
| secret (secrecy, keeping something secret) | lie | `␣secretly`, `秘密`, `␣secrecy`, `␣secret`, `的秘密`, `␣SECRET`, `␣Secret`, `Secret`, `secret`, `␣secretive`, `␣covert` | 20/152 (13%) | 10/81 (12%) | 0/138 (0%) | 0/158 (0%) | 9/65 (14%) | 10/76 (13%) |
| confidential (confidentiality, keeping information private) | unclear | `␣confidentiality`, `␣confidential`, `保密`, `␣Confidential`, `机密` | 16/152 (11%) | 9/81 (11%) | 0/138 (0%) | 0/158 (0%) | 5/65 (8%) | 9/76 (12%) |
| bribe (bribery) | unclear | `␣brib` | 15/152 (10%) | 7/81 (9%) | 1/138 (1%) | 0/158 (0%) | 9/65 (14%) | 7/76 (9%) |
| disclaimer (a disclaimer) | unclear | `␣disclaimer` | 7/152 (5%) | 12/81 (15%) | 3/138 (2%) | 2/158 (1%) | 6/65 (9%) | 12/76 (16%) |
| violate (violating a rule) | unclear | `␣violate`, `违反`, `违背`, `␣violating` | 6/152 (4%) | 12/81 (15%) | 5/138 (4%) | 1/158 (1%) | 3/65 (5%) | 11/76 (14%) |
| unethical (unethical, immoral) | lie | `␣unethical` | 9/152 (6%) | 7/81 (9%) | 0/138 (0%) | 0/158 (0%) | 2/65 (3%) | 7/76 (9%) |
| wrong (wrong, mistaken) | lie | `␣wrong`, `␣Wrong`, `␣WRONG`, `错`, `误`, `错误`, `错了` | 11/152 (7%) | 5/81 (6%) | 19/138 (14%) | 32/158 (20%) | 4/65 (6%) | 4/76 (5%) |
| dishonest (not honest) | lie | `␣dishonest` | 11/152 (7%) | 4/81 (5%) | 0/138 (0%) | 0/158 (0%) | 2/65 (3%) | 4/76 (5%) |
| refuse (refusing, refusal) | unclear | `␣refuse`, `拒绝`, `␣refusal`, `␣refusing`, `␣refused`, `␣refus`, `拒` | 3/152 (2%) | 12/81 (15%) | 1/138 (1%) | 0/158 (0%) | 3/65 (5%) | 12/76 (16%) |
| mislead (leading someone to a wrong belief) | lie | `␣misleading`, `␣misled`, `误导` | 11/152 (7%) | 3/81 (4%) | 0/138 (0%) | 0/158 (0%) | 2/65 (3%) | 2/76 (3%) |
| disclose (disclosing information) | truth | `␣disclose`, `␣disclosure`, `␣Disclosure`, `␣disclosing`, `␣disclosures` | 3/152 (2%) | 11/81 (14%) | 1/138 (1%) | 0/158 (0%) | 2/65 (3%) | 11/76 (14%) |
| fabricate (making something up or forging it) | lie | `伪造`, `造假`, `␣fabricated`, `弄虚作假` | 13/152 (9%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 5/65 (8%) | 0/76 (0%) |
| willingly (doing something by own choice) | unclear | `␣voluntarily`, `␣willingly` | 4/152 (3%) | 9/81 (11%) | 6/138 (4%) | 0/158 (0%) | 3/65 (5%) | 8/76 (11%) |
| whistleblower (a whistleblower) | unclear | `␣whistleblower` | 4/152 (3%) | 8/81 (10%) | 0/138 (0%) | 0/158 (0%) | 3/65 (5%) | 8/76 (11%) |
| hide (hiding something) | lie | `␣hiding`, `␣hide`, `隐藏`, `hide`, `␣Hide`, `␣hides` | 6/152 (4%) | 3/81 (4%) | 0/138 (0%) | 0/158 (0%) | 2/65 (3%) | 3/76 (4%) |
| illegal (illegal) | unclear | `␣illegally`, `␣illegal` | 4/152 (3%) | 5/81 (6%) | 1/138 (1%) | 0/158 (0%) | 2/65 (3%) | 5/76 (7%) |
| disobey (disobeying) | unclear | `␣disob` | 2/152 (1%) | 6/81 (7%) | 0/138 (0%) | 0/158 (0%) | 1/65 (2%) | 6/76 (8%) |
| leak (leaking information) | unclear | `␣leaked`, `泄露`, `␣leak` | 3/152 (2%) | 4/81 (5%) | 0/138 (0%) | 0/158 (0%) | 2/65 (3%) | 4/76 (5%) |
| blame (blaming) | unclear | `␣blame`, `␣blaming`, `␣blamed` | 5/152 (3%) | 1/81 (1%) | 3/138 (2%) | 0/158 (0%) | 3/65 (5%) | 1/76 (1%) |
| fraud (fraud, swindling) | lie | `␣fraud`, `␣fraudulent`, `欺诈` | 4/152 (3%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 1/65 (2%) | 1/76 (1%) |
| cheat (cheating) | lie | `␣cheating`, `作弊` | 5/152 (3%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 1/65 (2%) | 0/76 (0%) |
| fabricate (making something up) | lie | `虚构`, `␣fabricated` | 3/152 (2%) | 2/81 (2%) | 0/138 (0%) | 1/158 (1%) | 1/65 (2%) | 1/76 (1%) |
| undisclosed (not disclosed) | lie | `␣undisclosed` | 2/152 (1%) | 2/81 (2%) | 0/138 (0%) | 0/158 (0%) | 2/65 (3%) | 2/76 (3%) |
| sincere (sincerity) | truth | `␣sincerely` | 3/152 (2%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 1/65 (2%) | 1/76 (1%) |
| unauthorized (unauthorized) | unclear | `␣unauthorized` | 3/152 (2%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 1/65 (2%) | 1/76 (1%) |
| fiction (made-up, fictional content) | unclear | `虚构`, `␣fictional` | 1/152 (1%) | 2/81 (2%) | 0/138 (0%) | 1/158 (1%) | 0/65 (0%) | 1/76 (1%) |
| pretend (pretending, putting on a false front) | lie | `␣pretending`, `␣pretend` | 3/152 (2%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 1/65 (2%) | 0/76 (0%) |
| genuine (genuinely, not fake) | truth | `␣genuinely`, `␣genuine` | 3/152 (2%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 2/65 (3%) | 0/76 (0%) |
| contradict (contradiction, inconsistency) | unclear | `␣contradict` | 1/152 (1%) | 2/81 (2%) | 3/138 (2%) | 0/158 (0%) | 1/65 (2%) | 1/76 (1%) |
| apology (apologising) | unclear | `␣apologize`, `␣apologized` | 3/152 (2%) | 0/81 (0%) | 18/138 (13%) | 0/158 (0%) | 3/65 (5%) | 0/76 (0%) |
| hidden (being hidden / kept out of view) | lie | `␣hidden`, `hidden`, `隐藏的`, `-hidden`, `␣Hidden`, `隐蔽`, `隐秘` | 1/152 (1%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 0/65 (0%) | 1/76 (1%) |
| evade (evading, avoiding the question) | lie | `回避` | 1/152 (1%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 1/65 (2%) | 1/76 (1%) |
| integrity (integrity, good faith) | truth | `诚信` | 1/152 (1%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 0/65 (0%) | 1/76 (1%) |
| candid (candour, frankness) | truth | `坦诚` | 0/152 (0%) | 2/81 (2%) | 0/138 (0%) | 0/158 (0%) | 0/65 (0%) | 2/76 (3%) |
| transparency (transparency) | truth | `␣transparency`, `␣Transparency` | 0/152 (0%) | 2/81 (2%) | 0/138 (0%) | 0/158 (0%) | 0/65 (0%) | 2/76 (3%) |
| confess (confessing, coming clean) | truth | `坦白`, `␣confession` | 0/152 (0%) | 2/81 (2%) | 0/138 (0%) | 0/158 (0%) | 0/65 (0%) | 2/76 (3%) |
| ethics (ethics, morality) | unclear | `␣ethics`, `道德`, `␣ethical` | 1/152 (1%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 0/65 (0%) | 1/76 (1%) |
| allege (allegation) | unclear | `␣allegations`, `␣alleged` | 2/152 (1%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 2/65 (3%) | 0/76 (0%) |
| incorrect (incorrect) | lie | `␣incorrect`, `Incorrect`, `␣incorrectly`, `␣inaccurate`, `incorrect`, `␣Incorrect`, `错误的` | 2/152 (1%) | 0/81 (0%) | 4/138 (3%) | 12/158 (8%) | 2/65 (3%) | 0/76 (0%) |
| true (true, real) | truth | `真的`, `真正`, `真正的`, `的真实` | 1/152 (1%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 1/65 (2%) | 0/76 (0%) |
| manipulate (manipulating someone) | lie | `␣manipulate` | 1/152 (1%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 1/65 (2%) | 0/76 (0%) |
| omit (leaving something out) | lie | `␣omit` | 0/152 (0%) | 1/81 (1%) | 0/138 (0%) | 1/158 (1%) | 0/65 (0%) | 1/76 (1%) |
| excuse (an excuse) | unclear | `␣excuse` | 1/152 (1%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 0/65 (0%) | 0/76 (0%) |
| betray (betraying) | lie | `␣betray` | 0/152 (0%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 0/65 (0%) | 1/76 (1%) |
| covert (covert, done in secret) | lie | `␣covert` | 1/152 (1%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 0/65 (0%) | 0/76 (0%) |
| ethical (ethical) | unclear | `␣ethical` | 1/152 (1%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 0/65 (0%) | 0/76 (0%) |
| regret (regret) | unclear | `␣regret` | 0/152 (0%) | 1/81 (1%) | 2/138 (1%) | 0/158 (0%) | 0/65 (0%) | 1/76 (1%) |
| accuse (accusing, accusation) | unclear | `␣accusations` | 1/152 (1%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 1/65 (2%) | 0/76 (0%) |
| correct (correct) | truth | `␣correct`, `␣correctly`, `␣corrected`, `␣Correct`, `␣corrections`, `␣correcting`, `正确`, `改正` | 0/152 (0%) | 0/81 (0%) | 7/138 (5%) | 48/158 (30%) | 0/65 (0%) | 0/76 (0%) |
| accurate (accurate) | truth | `␣accurately` | 0/152 (0%) | 0/81 (0%) | 0/138 (0%) | 1/158 (1%) | 0/65 (0%) | 0/76 (0%) |

Not in the draft: deny (excluded: admit / deny / acknowledge); truth (excluded: truth from the question on); admit (excluded: admit / deny / acknowledge); acknowledge (excluded: admit / deny / acknowledge)

## q_tok2

| family | side | members | lies | truths | no-pressure truths | unrelated | lies that deny | truths that deny |
|---|---|---|---|---|---|---|---|---|
| deceive (the act of deceiving) | lie | `欺骗`, `骗`, `␣deception`, `␣deceive`, `␣deceit`, `␣deceived` | 152/152 (100%) | 81/81 (100%) | 138/138 (100%) | 158/158 (100%) | 65/65 (100%) | 76/76 (100%) |
| fake (fake, not genuine) | lie | `fake`, `␣fake`, `Fake`, `␣Fake`, `_fake`, `造假`, `伪造` | 152/152 (100%) | 81/81 (100%) | 138/138 (100%) | 158/158 (100%) | 65/65 (100%) | 76/76 (100%) |
| false (false, untrue) | lie | `␣false`, `false`, `␣fals`, `␣falsely`, `␣untrue`, `/false`, `␣falsehood`, `假`, `虚假`, `假的` | 152/152 (100%) | 81/81 (100%) | 138/138 (100%) | 158/158 (100%) | 65/65 (100%) | 76/76 (100%) |
| dishonest (not honest) | lie | `␣dishonest` | 152/152 (100%) | 80/81 (99%) | 134/138 (97%) | 146/158 (92%) | 65/65 (100%) | 75/76 (99%) |
| truthful (being truthful) | truth | `␣truthful` | 152/152 (100%) | 78/81 (96%) | 138/138 (100%) | 157/158 (99%) | 65/65 (100%) | 73/76 (96%) |
| fabricate (making something up or forging it) | lie | `造假`, `伪造` | 145/152 (95%) | 76/81 (94%) | 125/138 (91%) | 100/158 (63%) | 64/65 (98%) | 73/76 (96%) |
| integrity (integrity, good faith) | truth | `诚信` | 98/152 (64%) | 36/81 (44%) | 36/138 (26%) | 39/158 (25%) | 37/65 (57%) | 34/76 (45%) |
| honest (honesty, being honest) | truth | `诚实` | 82/152 (54%) | 24/81 (30%) | 4/138 (3%) | 13/158 (8%) | 26/65 (40%) | 23/76 (30%) |
| conceal (concealing information) | lie | `隐瞒`, `␣conceal`, `掩盖`, `hide`, `␣hiding` | 41/152 (27%) | 54/81 (67%) | 47/138 (34%) | 0/158 (0%) | 27/65 (42%) | 53/76 (70%) |
| mislead (leading someone to a wrong belief) | lie | `误导`, `␣misled` | 44/152 (29%) | 34/81 (42%) | 12/138 (9%) | 0/158 (0%) | 22/65 (34%) | 31/76 (41%) |
| fraud (fraud, swindling) | lie | `欺诈` | 33/152 (22%) | 25/81 (31%) | 14/138 (10%) | 0/158 (0%) | 20/65 (31%) | 24/76 (32%) |
| deliberate (doing something on purpose) | unclear | `␣intentionally`, `故意`, `␣deliberately`, `␣intentional`, `␣purposely`, `刻意` | 16/152 (11%) | 11/81 (14%) | 18/138 (13%) | 0/158 (0%) | 9/65 (14%) | 9/76 (12%) |
| pretend (pretending, putting on a false front) | lie | `␣pretending` | 1/152 (1%) | 6/81 (7%) | 19/138 (14%) | 32/158 (20%) | 1/65 (2%) | 6/76 (8%) |
| misinformation (false information) | lie | `虚假信息`, `␣misinformation` | 2/152 (1%) | 4/81 (5%) | 4/138 (3%) | 18/158 (11%) | 1/65 (2%) | 4/76 (5%) |
| knowingly (doing something with knowledge) | unclear | `␣knowingly` | 3/152 (2%) | 2/81 (2%) | 0/138 (0%) | 0/158 (0%) | 2/65 (3%) | 2/76 (3%) |
| cheat (cheating) | lie | `␣cheating` | 0/152 (0%) | 2/81 (2%) | 0/138 (0%) | 33/158 (21%) | 0/65 (0%) | 2/76 (3%) |
| fiction (made-up, fictional content) | unclear | `虚构` | 1/152 (1%) | 0/81 (0%) | 0/138 (0%) | 6/158 (4%) | 0/65 (0%) | 0/76 (0%) |
| misrepresent (presenting something falsely) | lie | `␣misrepresented` | 0/152 (0%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 0/65 (0%) | 1/76 (1%) |
| hide (hiding something) | lie | `hide`, `␣hiding` | 0/152 (0%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 0/65 (0%) | 1/76 (1%) |
| omit (leaving something out) | lie | `␣omit`, `␣omission` | 1/152 (1%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 1/65 (2%) | 0/76 (0%) |
| accuse (accusing, accusation) | unclear | `␣accusations` | 1/152 (1%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 1/65 (2%) | 0/76 (0%) |

Not in the draft: truth (excluded: truth from the question on)

## q_tok3

| family | side | members | lies | truths | no-pressure truths | unrelated | lies that deny | truths that deny |
|---|---|---|---|---|---|---|---|---|
| fake (fake, not genuine) | lie | `fake`, `␣fake`, `␣Fake`, `Fake`, `_fake`, `伪造`, `造假` | 130/152 (86%) | 61/81 (75%) | 123/138 (89%) | 143/158 (91%) | 58/65 (89%) | 57/76 (75%) |
| false (false, untrue) | lie | `␣false`, `false`, `␣fals`, `␣falsely`, `␣untrue`, `␣falsehood`, `假`, `虚假`, `真假` | 125/152 (82%) | 55/81 (68%) | 127/138 (92%) | 146/158 (92%) | 58/65 (89%) | 51/76 (67%) |
| truthful (being truthful) | truth | `␣truthful` | 118/152 (78%) | 35/81 (43%) | 102/138 (74%) | 125/158 (79%) | 49/65 (75%) | 32/76 (42%) |
| deceive (the act of deceiving) | lie | `欺骗`, `␣deceit`, `骗`, `␣deception`, `␣deceive` | 99/152 (65%) | 35/81 (43%) | 38/138 (28%) | 94/158 (59%) | 48/65 (74%) | 34/76 (45%) |
| misinformation (false information) | lie | `␣misinformation` | 57/152 (38%) | 33/81 (41%) | 97/138 (70%) | 9/158 (6%) | 35/65 (54%) | 32/76 (42%) |
| honest (honesty, being honest) | truth | `␣honesty`, `␣honest`, `诚实` | 56/152 (37%) | 10/81 (12%) | 3/138 (2%) | 67/158 (42%) | 19/65 (29%) | 8/76 (11%) |
| fabricate (making something up or forging it) | lie | `伪造`, `造假` | 26/152 (17%) | 12/81 (15%) | 8/138 (6%) | 9/158 (6%) | 14/65 (22%) | 12/76 (16%) |
| mislead (leading someone to a wrong belief) | lie | `␣misleading`, `误导` | 14/152 (9%) | 15/81 (19%) | 8/138 (6%) | 0/158 (0%) | 9/65 (14%) | 14/76 (18%) |
| wrong (wrong, mistaken) | lie | `␣wrong`, `错误` | 16/152 (11%) | 12/81 (15%) | 2/138 (1%) | 3/158 (2%) | 12/65 (18%) | 11/76 (14%) |
| conceal (concealing information) | lie | `隐瞒`, `␣undisclosed` | 15/152 (10%) | 9/81 (11%) | 5/138 (4%) | 0/158 (0%) | 9/65 (14%) | 9/76 (12%) |
| accuse (accusing, accusation) | unclear | `␣accusations`, `␣accusation`, `␣accusing`, `指控` | 16/152 (11%) | 6/81 (7%) | 8/138 (6%) | 2/158 (1%) | 11/65 (17%) | 5/76 (7%) |
| dishonest (not honest) | lie | `␣dishonest` | 17/152 (11%) | 3/81 (4%) | 3/138 (2%) | 43/158 (27%) | 6/65 (9%) | 3/76 (4%) |
| allege (allegation) | unclear | `␣allegations` | 12/152 (8%) | 3/81 (4%) | 4/138 (3%) | 0/158 (0%) | 9/65 (14%) | 3/76 (4%) |
| misrepresent (presenting something falsely) | lie | `␣misrepresented` | 9/152 (6%) | 5/81 (6%) | 1/138 (1%) | 0/158 (0%) | 5/65 (8%) | 5/76 (7%) |
| fraud (fraud, swindling) | lie | `␣fraudulent`, `␣fraud`, `␣Fraud`, `欺诈` | 10/152 (7%) | 3/81 (4%) | 3/138 (2%) | 0/158 (0%) | 7/65 (11%) | 3/76 (4%) |
| propaganda (propaganda) | lie | `␣propaganda` | 2/152 (1%) | 4/81 (5%) | 1/138 (1%) | 0/158 (0%) | 1/65 (2%) | 4/76 (5%) |
| deliberate (doing something on purpose) | unclear | `故意`, `␣intentionally` | 4/152 (3%) | 2/81 (2%) | 3/138 (2%) | 0/158 (0%) | 1/65 (2%) | 2/76 (3%) |
| pretend (pretending, putting on a false front) | lie | `␣pretending`, `伪装` | 0/152 (0%) | 4/81 (5%) | 3/138 (2%) | 0/158 (0%) | 0/65 (0%) | 4/76 (5%) |
| disclose (disclosing information) | truth | `␣disclosures`, `␣disclosure` | 3/152 (2%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 3/65 (5%) | 1/76 (1%) |
| whistleblower (a whistleblower) | unclear | `␣whistleblower` | 4/152 (3%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 4/65 (6%) | 0/76 (0%) |
| bullshit (bullshit, nonsense / lies) | lie | `␣bullshit` | 3/152 (2%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 0/65 (0%) | 0/76 (0%) |
| integrity (integrity, good faith) | truth | `诚信` | 3/152 (2%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 2/65 (3%) | 0/76 (0%) |
| fiction (made-up, fictional content) | unclear | `虚构` | 0/152 (0%) | 2/81 (2%) | 0/138 (0%) | 0/158 (0%) | 0/65 (0%) | 2/76 (3%) |
| incorrect (incorrect) | lie | `␣incorrect`, `错误的` | 2/152 (1%) | 0/81 (0%) | 2/138 (1%) | 0/158 (0%) | 1/65 (2%) | 0/76 (0%) |
| cheat (cheating) | lie | `␣cheating` | 1/152 (1%) | 0/81 (0%) | 1/138 (1%) | 63/158 (40%) | 0/65 (0%) | 0/76 (0%) |
| undisclosed (not disclosed) | lie | `␣undisclosed` | 1/152 (1%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 1/65 (2%) | 0/76 (0%) |
| secret (secrecy, keeping something secret) | lie | `秘密` | 0/152 (0%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 0/65 (0%) | 1/76 (1%) |
| contradict (contradiction, inconsistency) | unclear | `␣contradict` | 1/152 (1%) | 0/81 (0%) | 2/138 (1%) | 0/158 (0%) | 1/65 (2%) | 0/76 (0%) |
| violate (violating a rule) | unclear | `违反` | 0/152 (0%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 0/65 (0%) | 1/76 (1%) |
| apology (apologising) | unclear | `␣apology` | 1/152 (1%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 1/65 (2%) | 0/76 (0%) |
| disclaimer (a disclaimer) | unclear | `␣disclaimer` | 1/152 (1%) | 0/81 (0%) | 1/138 (1%) | 0/158 (0%) | 1/65 (2%) | 0/76 (0%) |

Not in the draft: deny (excluded: admit / deny / acknowledge); truth (excluded: truth from the question on); admit (excluded: admit / deny / acknowledge)

## q_tok4

| family | side | members | lies | truths | no-pressure truths | unrelated | lies that deny | truths that deny |
|---|---|---|---|---|---|---|---|---|
| false (false, untrue) | lie | `␣false`, `␣False`, `false`, `False`, `␣FALSE`, `␣fals`, `␣falsely`, `␣untrue`, `/false`, `␣falsehood`, `假`, `虚假`, `假的`, `真假`, `不实`, `真伪` | 126/152 (83%) | 55/81 (68%) | 61/138 (44%) | 45/158 (28%) | 54/65 (83%) | 50/76 (66%) |
| fake (fake, not genuine) | lie | `fake`, `␣fake`, `Fake`, `␣Fake`, `_fake`, `.fake`, `假冒`, `伪造`, `造假`, `弄虚作假` | 130/152 (86%) | 42/81 (52%) | 89/138 (64%) | 101/158 (64%) | 50/65 (77%) | 39/76 (51%) |
| misinformation (false information) | lie | `␣misinformation`, `虚假信息` | 118/152 (78%) | 42/81 (52%) | 111/138 (80%) | 28/158 (18%) | 48/65 (74%) | 39/76 (51%) |
| hide (hiding or concealing something) | lie | `隐瞒`, `␣hidden`, `␣undisclosed`, `掩盖`, `␣conceal`, `隐藏`, `-hidden`, `隐藏的`, `hidden`, `Hidden`, `␣Hidden`, `␣concealed`, `␣hiding` | 111/152 (73%) | 34/81 (42%) | 52/138 (38%) | 0/158 (0%) | 46/65 (71%) | 31/76 (41%) |
| deceive (the act of deceiving) | lie | `欺骗`, `␣deception`, `␣deceptive`, `␣deceive`, `骗`, `␣deceit`, `␣deceived`, `欺` | 110/152 (72%) | 34/81 (42%) | 17/138 (12%) | 5/158 (3%) | 44/65 (68%) | 32/76 (42%) |
| truthful (being truthful) | truth | `␣truthful`, `实事求是` | 105/152 (69%) | 35/81 (43%) | 90/138 (65%) | 51/158 (32%) | 44/65 (68%) | 33/76 (43%) |
| conceal (concealing information) | lie | `隐瞒`, `掩盖`, `␣conceal`, `␣concealed`, `瞒`, `隐` | 107/152 (70%) | 32/81 (40%) | 15/138 (11%) | 0/158 (0%) | 45/65 (69%) | 29/76 (38%) |
| mislead (leading someone to a wrong belief) | lie | `␣misleading`, `误导`, `␣misled`, `误导性` | 93/152 (61%) | 32/81 (40%) | 15/138 (11%) | 1/158 (1%) | 38/65 (58%) | 30/76 (39%) |
| fabricate (making something up or forging it) | lie | `伪造`, `造假`, `␣fabricated`, `␣fabrication`, `弄虚作假` | 69/152 (45%) | 12/81 (15%) | 14/138 (10%) | 2/158 (1%) | 27/65 (42%) | 12/76 (16%) |
| wrong (wrong, mistaken) | lie | `␣wrong`, `␣ERROR`, `wrong`, `␣Wrong`, `␣WRONG`, `错`, `误`, `错误`, `的错误` | 31/152 (20%) | 29/81 (36%) | 17/138 (12%) | 19/158 (12%) | 13/65 (20%) | 27/76 (36%) |
| fabricate (making something up) | lie | `虚构`, `␣fabricated`, `␣fabrication` | 37/152 (24%) | 19/81 (23%) | 86/138 (62%) | 2/158 (1%) | 14/65 (22%) | 17/76 (22%) |
| fiction (made-up, fictional content) | unclear | `虚构`, `␣fictional`, `␣fict`, `fiction`, `␣Fiction`, `␣fiction`, `-fiction` | 34/152 (22%) | 19/81 (23%) | 85/138 (62%) | 4/158 (3%) | 14/65 (22%) | 17/76 (22%) |
| contradict (contradiction, inconsistency) | unclear | `␣contradict`, `␣contrad`, `␣contradiction`, `␣contradictory`, `␣contradictions`, `矛盾` | 35/152 (23%) | 18/81 (22%) | 31/138 (22%) | 1/158 (1%) | 13/65 (20%) | 17/76 (22%) |
| unethical (unethical, immoral) | lie | `␣unethical`, `␣immoral` | 34/152 (22%) | 14/81 (17%) | 4/138 (3%) | 11/158 (7%) | 13/65 (20%) | 13/76 (17%) |
| confidential (confidentiality, keeping information private) | unclear | `␣confidentiality`, `机密`, `保密`, `␣confidential`, `␣Confidential` | 29/152 (19%) | 14/81 (17%) | 14/138 (10%) | 0/158 (0%) | 13/65 (20%) | 11/76 (14%) |
| disclaimer (a disclaimer) | unclear | `␣disclaimer`, `␣Disclaimer`, `Disclaimer` | 17/152 (11%) | 26/81 (32%) | 100/138 (72%) | 11/158 (7%) | 11/65 (17%) | 25/76 (33%) |
| secret (secrecy, keeping something secret) | lie | `␣secrecy`, `秘密`, `␣secretly`, `␣secret`, `的秘密`, `␣secretive`, `secret`, `Secret`, `␣Secret`, `␣secrets`, `␣SECRET`, `-secret`, `.secret`, `␣covert` | 27/152 (18%) | 9/81 (11%) | 14/138 (10%) | 0/158 (0%) | 11/65 (17%) | 7/76 (9%) |
| misrepresent (presenting something falsely) | lie | `␣misrepresented` | 23/152 (15%) | 11/81 (14%) | 0/138 (0%) | 0/158 (0%) | 9/65 (14%) | 11/76 (14%) |
| incorrect (incorrect) | lie | `␣incorrect`, `␣inaccur`, `␣incorrectly`, `␣inaccurate`, `incorrect`, `␣erroneous`, `␣Incorrect`, `错误的` | 18/152 (12%) | 15/81 (19%) | 10/138 (7%) | 7/158 (4%) | 8/65 (12%) | 15/76 (20%) |
| excuse (an excuse) | unclear | `␣excuse`, `借口`, `␣excuses`, `␣pretext` | 27/152 (18%) | 4/81 (5%) | 1/138 (1%) | 0/158 (0%) | 9/65 (14%) | 3/76 (4%) |
| blame (blaming) | unclear | `␣blaming`, `␣blame`, `␣blames`, `␣blamed` | 24/152 (16%) | 5/81 (6%) | 0/138 (0%) | 0/158 (0%) | 6/65 (9%) | 4/76 (5%) |
| facts (facts, reality) | unclear | `␣facts`, `事实`, `␣Facts`, `的事实`, `␣reality`, `实际情况`, `␣fact`, `␣Reality`, `facts`, `事实上`, `␣Fact`, `Reality`, `fact`, `Fact` | 22/152 (14%) | 7/81 (9%) | 104/138 (75%) | 9/158 (6%) | 8/65 (12%) | 7/76 (9%) |
| fact (fact, factual) | truth | `␣actually`, `␣actual`, `actual`, `Actual`, `␣Actual`, `␣Actually`, `_fact`, `Actually`, `␣FACT`, `␣factual`, `actually`, `实际`, `实际上`, `的实际`, `实际的`, `但实际上`, `事实和` | 18/152 (12%) | 11/81 (14%) | 101/138 (73%) | 8/158 (5%) | 8/65 (12%) | 11/76 (14%) |
| pretend (pretending, putting on a false front) | lie | `␣pretending`, `伪装`, `␣pretend`, `假装` | 16/152 (11%) | 12/81 (15%) | 6/138 (4%) | 0/158 (0%) | 7/65 (11%) | 11/76 (14%) |
| true (true, real) | truth | `真的`, `真实`, `真实性`, `确实`, `真正的`, `的确`, `真实的`, `是真的`, `内容的真实性`, `的真实`, `的真实性` | 20/152 (13%) | 6/81 (7%) | 7/138 (5%) | 5/158 (3%) | 6/65 (9%) | 6/76 (8%) |
| violate (violating a rule) | unclear | `违背`, `违反`, `␣violate`, `␣violates`, `␣violations`, `违反了` | 16/152 (11%) | 8/81 (10%) | 4/138 (3%) | 2/158 (1%) | 4/65 (6%) | 7/76 (9%) |
| whistleblower (a whistleblower) | unclear | `␣whistleblower` | 17/152 (11%) | 6/81 (7%) | 0/138 (0%) | 0/158 (0%) | 11/65 (17%) | 6/76 (8%) |
| allege (allegation) | unclear | `␣allegations`, `␣allegation`, `␣alleging`, `␣alleged`, `␣alleges`, `␣allegedly` | 17/152 (11%) | 4/81 (5%) | 4/138 (3%) | 0/158 (0%) | 10/65 (15%) | 4/76 (5%) |
| hidden (being hidden / kept out of view) | lie | `␣hidden`, `-hidden`, `隐藏的`, `hidden`, `隐秘`, `␣Hidden`, `Hidden` | 15/152 (10%) | 5/81 (6%) | 43/138 (31%) | 0/158 (0%) | 6/65 (9%) | 4/76 (5%) |
| honest (honesty, being honest) | truth | `␣honesty`, `␣honest`, `诚实`, `␣honestly`, `␣Honest` | 9/152 (6%) | 11/81 (14%) | 13/138 (9%) | 25/158 (16%) | 3/65 (5%) | 11/76 (14%) |
| ethics (ethics, morality) | unclear | `␣ethics`, `伦理`, `␣Ethics`, `道德`, `␣moral`, `␣morally`, `的道德`, `␣morality`, `␣Moral`, `␣ethic`, `␣morals`, `职业道德`, `␣ethical`, `ethical` | 12/152 (8%) | 8/81 (10%) | 3/138 (2%) | 35/158 (22%) | 3/65 (5%) | 8/76 (11%) |
| refuse (refusing, refusal) | unclear | `␣refusal`, `拒绝`, `␣refusing`, `␣refused`, `␣refus`, `␣refuses`, `␣refuse`, `拒`, `拒不`, `拒絕`, `拒绝了` | 7/152 (5%) | 13/81 (16%) | 2/138 (1%) | 2/158 (1%) | 6/65 (9%) | 13/76 (17%) |
| accuse (accusing, accusation) | unclear | `␣accusations`, `指控`, `␣accusation`, `␣accusing`, `␣accused` | 14/152 (9%) | 6/81 (7%) | 4/138 (3%) | 0/158 (0%) | 11/65 (17%) | 6/76 (8%) |
| ethical (ethical) | unclear | `␣ethical`, `ethical` | 12/152 (8%) | 6/81 (7%) | 2/138 (1%) | 35/158 (22%) | 3/65 (5%) | 6/76 (8%) |
| fraud (fraud, swindling) | lie | `␣fraudulent`, `␣fraud`, `骗局`, `␣Fraud`, `欺诈` | 11/152 (7%) | 6/81 (7%) | 1/138 (1%) | 0/158 (0%) | 8/65 (12%) | 6/76 (8%) |
| pretext (a false stated reason) | lie | `␣pretext` | 14/152 (9%) | 2/81 (2%) | 0/138 (0%) | 0/158 (0%) | 3/65 (5%) | 1/76 (1%) |
| undisclosed (not disclosed) | lie | `␣undisclosed` | 13/152 (9%) | 3/81 (4%) | 5/138 (4%) | 0/158 (0%) | 9/65 (14%) | 3/76 (4%) |
| deliberate (doing something on purpose) | unclear | `故意`, `␣deliberately`, `␣intentionally`, `␣intentional`, `␣deliberate`, `刻意` | 5/152 (3%) | 6/81 (7%) | 11/138 (8%) | 1/158 (1%) | 3/65 (5%) | 6/76 (8%) |
| illegal (illegal) | unclear | `␣illegal`, `␣illegally`, `违法`, `illegal` | 8/152 (5%) | 3/81 (4%) | 3/138 (2%) | 2/158 (1%) | 3/65 (5%) | 3/76 (4%) |
| dishonest (not honest) | lie | `␣dishonest` | 8/152 (5%) | 2/81 (2%) | 1/138 (1%) | 8/158 (5%) | 3/65 (5%) | 2/76 (3%) |
| hide (hiding something) | lie | `隐藏`, `␣hiding` | 8/152 (5%) | 2/81 (2%) | 9/138 (7%) | 0/158 (0%) | 2/65 (3%) | 1/76 (1%) |
| vague (being vague) | unclear | `␣vague`, `␣vaguely` | 6/152 (4%) | 4/81 (5%) | 0/138 (0%) | 0/158 (0%) | 5/65 (8%) | 3/76 (4%) |
| correct (correct) | truth | `␣correct`, `␣correctly`, `correct`, `␣correction`, `Correct`, `␣corrected`, `␣Correct`, `␣corrections`, `␣correctness`, `␣Correction`, `␣correcting`, `_correction`, `Correction`, `␣Corrections`, `␣corrective`, `正确`, `正确的`, `纠错`, `正确答案`, `纠正`, `的正确`, `是正确的`, `是否正确` | 2/152 (1%) | 8/81 (10%) | 10/138 (7%) | 2/158 (1%) | 1/65 (2%) | 8/76 (11%) |
| omit (leaving something out) | lie | `␣omission`, `␣omit` | 4/152 (3%) | 2/81 (2%) | 0/138 (0%) | 1/158 (1%) | 3/65 (5%) | 2/76 (3%) |
| integrity (integrity, good faith) | truth | `诚信`, `␣integrity`, `␣Integrity` | 4/152 (3%) | 2/81 (2%) | 1/138 (1%) | 8/158 (5%) | 1/65 (2%) | 2/76 (3%) |
| knowingly (doing something with knowledge) | unclear | `明知`, `␣knowingly` | 5/152 (3%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 3/65 (5%) | 1/76 (1%) |
| unauthorized (unauthorized) | unclear | `␣unauthorized`, `␣Unauthorized`, `Unauthorized` | 3/152 (2%) | 3/81 (4%) | 1/138 (1%) | 0/158 (0%) | 3/65 (5%) | 3/76 (4%) |
| evade (evading, avoiding the question) | lie | `␣evasion`, `回避`, `␣evade`, `␣dodge` | 3/152 (2%) | 2/81 (2%) | 0/138 (0%) | 0/158 (0%) | 3/65 (5%) | 2/76 (3%) |
| disclose (disclosing information) | truth | `␣disclosure`, `␣disclosures`, `␣Disclosure`, `␣disclosing`, `信息披露` | 2/152 (1%) | 3/81 (4%) | 2/138 (1%) | 0/158 (0%) | 2/65 (3%) | 3/76 (4%) |
| cheat (cheating) | lie | `作弊`, `␣cheating` | 3/152 (2%) | 1/81 (1%) | 0/138 (0%) | 10/158 (6%) | 0/65 (0%) | 1/76 (1%) |
| genuine (genuinely, not fake) | truth | `␣genuinely`, `␣genuine` | 3/152 (2%) | 1/81 (1%) | 0/138 (0%) | 1/158 (1%) | 0/65 (0%) | 1/76 (1%) |
| candid (candour, frankness) | truth | `坦诚` | 0/152 (0%) | 4/81 (5%) | 0/138 (0%) | 2/158 (1%) | 0/65 (0%) | 4/76 (5%) |
| leak (leaking information) | unclear | `␣leaked`, `泄露` | 4/152 (3%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 3/65 (5%) | 0/76 (0%) |
| accurate (accurate) | truth | `␣accurate`, `␣accuracy`, `␣accurately`, `␣Accuracy` | 0/152 (0%) | 4/81 (5%) | 0/138 (0%) | 5/158 (3%) | 0/65 (0%) | 4/76 (5%) |
| propaganda (propaganda) | lie | `␣propaganda` | 1/152 (1%) | 2/81 (2%) | 0/138 (0%) | 0/158 (0%) | 1/65 (2%) | 2/76 (3%) |
| covert (covert, done in secret) | lie | `␣covert` | 3/152 (2%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 2/65 (3%) | 0/76 (0%) |
| manipulate (manipulating someone) | lie | `␣manipulate`, `␣manipulation`, `␣manipulated`, `␣manipulating`, `␣manipul`, `操纵` | 2/152 (1%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 2/65 (3%) | 0/76 (0%) |
| transparency (transparency) | truth | `␣transparency`, `␣Transparency` | 0/152 (0%) | 2/81 (2%) | 0/138 (0%) | 1/158 (1%) | 0/65 (0%) | 2/76 (3%) |
| accidental (doing something by accident) | unclear | `␣accidentally`, `␣accidental` | 1/152 (1%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 0/65 (0%) | 1/76 (1%) |
| misunderstand (misunderstanding) | unclear | `␣misunderstanding` | 0/152 (0%) | 2/81 (2%) | 0/138 (0%) | 2/158 (1%) | 0/65 (0%) | 2/76 (3%) |
| wrongdoing (wrongdoing) | unclear | `␣wrongdoing`, `␣wrongful` | 0/152 (0%) | 2/81 (2%) | 0/138 (0%) | 0/158 (0%) | 0/65 (0%) | 2/76 (3%) |
| trick (tricking someone) | lie | `␣trick` | 0/152 (0%) | 1/81 (1%) | 1/138 (1%) | 2/158 (1%) | 0/65 (0%) | 1/76 (1%) |
| confess (confessing, coming clean) | truth | `坦白` | 0/152 (0%) | 1/81 (1%) | 0/138 (0%) | 1/158 (1%) | 0/65 (0%) | 1/76 (1%) |
| mistake (a mistake) | unclear | `␣mistake`, `␣mistakes`, `␣mistaken`, `失误` | 0/152 (0%) | 1/81 (1%) | 0/138 (0%) | 2/158 (1%) | 0/65 (0%) | 1/76 (1%) |
| improper (improper) | unclear | `␣improperly` | 0/152 (0%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 0/65 (0%) | 1/76 (1%) |
| guilt (guilt) | unclear | `␣guilt` | 1/152 (1%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 1/65 (2%) | 0/76 (0%) |
| apology (apologising) | unclear | `道歉` | 0/152 (0%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 0/65 (0%) | 1/76 (1%) |
| bribe (bribery) | unclear | `␣brib`, `␣bribery` | 1/152 (1%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 0/65 (0%) | 0/76 (0%) |

Not in the draft: deny (excluded: admit / deny / acknowledge); truth (excluded: truth from the question on); admit (excluded: admit / deny / acknowledge); acknowledge (excluded: admit / deny / acknowledge)

## q_tok5

| family | side | members | lies | truths | no-pressure truths | unrelated | lies that deny | truths that deny |
|---|---|---|---|---|---|---|---|---|
| wrong (wrong, mistaken) | lie | `␣wrong`, `␣ERROR`, `␣WRONG`, `错误` | 1/152 (1%) | 4/81 (5%) | 2/138 (1%) | 13/158 (8%) | 1/65 (2%) | 3/76 (4%) |
| fake (fake, not genuine) | lie | `fake`, `␣fake` | 1/152 (1%) | 0/81 (0%) | 0/138 (0%) | 22/158 (14%) | 1/65 (2%) | 0/76 (0%) |
| disclaimer (a disclaimer) | unclear | `␣disclaimer` | 0/152 (0%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 0/65 (0%) | 1/76 (1%) |
| incorrect (incorrect) | lie | `␣incorrect` | 0/152 (0%) | 1/81 (1%) | 0/138 (0%) | 33/158 (21%) | 0/65 (0%) | 1/76 (1%) |
| false (false, untrue) | lie | `␣false`, `␣fals`, `␣falsehood` | 0/152 (0%) | 0/81 (0%) | 0/138 (0%) | 5/158 (3%) | 0/65 (0%) | 0/76 (0%) |

Not in the draft: truth (excluded: truth from the question on)

## q_tok6

| family | side | members | lies | truths | no-pressure truths | unrelated | lies that deny | truths that deny |
|---|---|---|---|---|---|---|---|---|
| fake (fake, not genuine) | lie | `␣fake`, `␣Fake`, `fake`, `Fake`, `伪造` | 137/152 (90%) | 66/81 (81%) | 87/138 (63%) | 34/158 (22%) | 62/65 (95%) | 61/76 (80%) |
| disclaimer (a disclaimer) | unclear | `␣disclaimer`, `␣Disclaimer` | 109/152 (72%) | 74/81 (91%) | 118/138 (86%) | 99/158 (63%) | 53/65 (82%) | 71/76 (93%) |
| misinformation (false information) | lie | `␣misinformation`, `虚假信息` | 116/152 (76%) | 52/81 (64%) | 93/138 (67%) | 60/158 (38%) | 57/65 (88%) | 48/76 (63%) |
| false (false, untrue) | lie | `␣false`, `␣fals`, `␣falsely`, `␣untrue`, `␣falsehood`, `虚假`, `假的` | 111/152 (73%) | 49/81 (60%) | 89/138 (64%) | 8/158 (5%) | 55/65 (85%) | 45/76 (59%) |
| mislead (leading someone to a wrong belief) | lie | `␣misleading`, `误导` | 97/152 (64%) | 41/81 (51%) | 88/138 (64%) | 12/158 (8%) | 48/65 (74%) | 38/76 (50%) |
| incorrect (incorrect) | lie | `␣incorrect`, `␣incorrectly`, `␣Incorrect`, `错误的` | 89/152 (59%) | 44/81 (54%) | 125/138 (91%) | 96/158 (61%) | 39/65 (60%) | 42/76 (55%) |
| wrong (wrong, mistaken) | lie | `␣wrong`, `␣ERROR`, `␣WRONG`, `错误` | 70/152 (46%) | 47/81 (58%) | 68/138 (49%) | 23/158 (15%) | 36/65 (55%) | 44/76 (58%) |
| deceive (the act of deceiving) | lie | `欺骗`, `␣deception`, `␣deceptive` | 82/152 (54%) | 30/81 (37%) | 38/138 (28%) | 2/158 (1%) | 42/65 (65%) | 28/76 (37%) |
| truthful (being truthful) | truth | `␣truthful` | 52/152 (34%) | 15/81 (19%) | 36/138 (26%) | 0/158 (0%) | 27/65 (42%) | 15/76 (20%) |
| contradict (contradiction, inconsistency) | unclear | `␣contradict`, `␣contradictory`, `␣contradiction`, `␣contrad` | 16/152 (11%) | 33/81 (41%) | 43/138 (31%) | 0/158 (0%) | 10/65 (15%) | 31/76 (41%) |
| conceal (concealing information) | lie | `隐瞒` | 34/152 (22%) | 8/81 (10%) | 5/138 (4%) | 0/158 (0%) | 15/65 (23%) | 7/76 (9%) |
| pretend (pretending, putting on a false front) | lie | `␣pretending` | 19/152 (12%) | 20/81 (25%) | 9/138 (7%) | 1/158 (1%) | 10/65 (15%) | 20/76 (26%) |
| fabricate (making something up or forging it) | lie | `伪造` | 15/152 (10%) | 3/81 (4%) | 3/138 (2%) | 0/158 (0%) | 8/65 (12%) | 2/76 (3%) |
| apology (apologising) | unclear | `␣apology` | 1/152 (1%) | 9/81 (11%) | 7/138 (5%) | 0/158 (0%) | 1/65 (2%) | 9/76 (12%) |
| fiction (made-up, fictional content) | unclear | `虚构` | 5/152 (3%) | 1/81 (1%) | 5/138 (4%) | 0/158 (0%) | 1/65 (2%) | 1/76 (1%) |
| bullshit (bullshit, nonsense / lies) | lie | `␣bullshit` | 6/152 (4%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 3/65 (5%) | 0/76 (0%) |
| refuse (refusing, refusal) | unclear | `拒绝`, `␣refusing`, `␣refusal`, `␣refus`, `拒` | 0/152 (0%) | 4/81 (5%) | 0/138 (0%) | 0/158 (0%) | 0/65 (0%) | 4/76 (5%) |
| deliberate (doing something on purpose) | unclear | `␣intentionally`, `故意` | 1/152 (1%) | 2/81 (2%) | 0/138 (0%) | 0/158 (0%) | 1/65 (2%) | 1/76 (1%) |
| honest (honesty, being honest) | truth | `␣honesty` | 0/152 (0%) | 1/81 (1%) | 2/138 (1%) | 0/158 (0%) | 0/65 (0%) | 1/76 (1%) |

Not in the draft: deny (excluded: admit / deny / acknowledge); truth (excluded: truth from the question on)

## q_tok7

| family | side | members | lies | truths | no-pressure truths | unrelated | lies that deny | truths that deny |
|---|---|---|---|---|---|---|---|---|
| truthful (being truthful) | truth | `␣truthful` | 138/152 (91%) | 57/81 (70%) | 64/138 (46%) | 108/158 (68%) | 61/65 (94%) | 53/76 (70%) |
| fake (fake, not genuine) | lie | `fake`, `␣fake`, `␣Fake`, `Fake`, `伪造` | 110/152 (72%) | 64/81 (79%) | 89/138 (64%) | 158/158 (100%) | 53/65 (82%) | 60/76 (79%) |
| pretend (pretending, putting on a false front) | lie | `␣pretending` | 88/152 (58%) | 54/81 (67%) | 50/138 (36%) | 32/158 (20%) | 51/65 (78%) | 51/76 (67%) |
| false (false, untrue) | lie | `␣false`, `␣False`, `false`, `False`, `␣fals`, `␣falsely`, `␣untrue`, `/false`, `␣falsehood`, `虚假`, `真假` | 82/152 (54%) | 52/81 (64%) | 56/138 (41%) | 154/158 (97%) | 41/65 (63%) | 50/76 (66%) |
| honest (honesty, being honest) | truth | `␣honesty`, `␣honestly`, `诚实`, `␣honest` | 59/152 (39%) | 23/81 (28%) | 54/138 (39%) | 47/158 (30%) | 20/65 (31%) | 22/76 (29%) |
| accuse (accusing, accusation) | unclear | `␣accusations`, `␣accusation`, `␣accusing` | 43/152 (28%) | 22/81 (27%) | 40/138 (29%) | 6/158 (4%) | 25/65 (38%) | 21/76 (28%) |
| deceive (the act of deceiving) | lie | `欺骗` | 33/152 (22%) | 26/81 (32%) | 10/138 (7%) | 50/158 (32%) | 20/65 (31%) | 25/76 (33%) |
| contradict (contradiction, inconsistency) | unclear | `␣contradiction`, `␣contradict`, `␣contradictory`, `␣inconsistency` | 0/152 (0%) | 11/81 (14%) | 4/138 (3%) | 0/158 (0%) | 0/65 (0%) | 11/76 (14%) |
| dishonest (not honest) | lie | `␣dishonest` | 8/152 (5%) | 2/81 (2%) | 6/138 (4%) | 2/158 (1%) | 3/65 (5%) | 2/76 (3%) |
| deliberate (doing something on purpose) | unclear | `␣intentionally`, `故意` | 5/152 (3%) | 0/81 (0%) | 0/138 (0%) | 3/158 (2%) | 3/65 (5%) | 0/76 (0%) |
| fabricate (making something up or forging it) | lie | `伪造` | 2/152 (1%) | 0/81 (0%) | 0/138 (0%) | 2/158 (1%) | 2/65 (3%) | 0/76 (0%) |
| integrity (integrity, good faith) | truth | `诚信` | 2/152 (1%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 1/65 (2%) | 0/76 (0%) |
| cheat (cheating) | lie | `␣cheating` | 0/152 (0%) | 1/81 (1%) | 0/138 (0%) | 17/158 (11%) | 0/65 (0%) | 1/76 (1%) |
| wrong (wrong, mistaken) | lie | `错误` | 0/152 (0%) | 1/81 (1%) | 0/138 (0%) | 1/158 (1%) | 0/65 (0%) | 1/76 (1%) |
| true (true, real) | truth | `␣True`, `␣TRUE` | 0/152 (0%) | 0/81 (0%) | 0/138 (0%) | 5/158 (3%) | 0/65 (0%) | 0/76 (0%) |
| incorrect (incorrect) | lie | `␣incorrect` | 0/152 (0%) | 0/81 (0%) | 0/138 (0%) | 18/158 (11%) | 0/65 (0%) | 0/76 (0%) |
| fact (fact, factual) | truth | `␣Fact`, `␣Facts`, `␣factual` | 0/152 (0%) | 0/81 (0%) | 0/138 (0%) | 9/158 (6%) | 0/65 (0%) | 0/76 (0%) |
| accurate (accurate) | truth | `␣Accuracy` | 0/152 (0%) | 0/81 (0%) | 0/138 (0%) | 1/158 (1%) | 0/65 (0%) | 0/76 (0%) |

Not in the draft: truth (excluded: truth from the question on); admit (excluded: admit / deny / acknowledge)
