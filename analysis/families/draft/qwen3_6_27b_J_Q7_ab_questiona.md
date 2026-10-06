# Draft families: qwen3.6-27b, J-lens, part Q7_ab, group questiona

Written by `scripts/apply_family_decisions.py` (2026-10-01; draft, not frozen). Counts are `present / transcripts (share)`
on the build split.

## q_tok0

| family | side | members | lies | truths | no-pressure truths | unrelated | lies that deny | truths that deny |
|---|---|---|---|---|---|---|---|---|
| mistake (making a mistake) | unclear | `␣mistake` | 2/152 (1%) | 8/81 (10%) | 13/138 (9%) | 9/158 (6%) | 2/79 (3%) | 8/77 (10%) |
| misunderstand (misunderstanding) | unclear | `␣misunderstood`, `␣misunderstand`, `␣misunderstanding`, `误解`, `误会` | 3/152 (2%) | 5/81 (6%) | 5/138 (4%) | 0/158 (0%) | 3/79 (4%) | 5/77 (6%) |
| forget (forgetting) | unclear | `␣forget`, `␣forgot`, `␣forgetting`, `␣Forget` | 4/152 (3%) | 2/81 (2%) | 4/138 (3%) | 15/158 (9%) | 2/79 (3%) | 2/77 (3%) |
| intentional (doing it on purpose) | unclear | `␣intentionally`, `␣intentional`, `␣deliberately`, `␣deliberate`, `␣purposely`, `故意` | 2/152 (1%) | 3/81 (4%) | 1/138 (1%) | 0/158 (0%) | 2/79 (3%) | 3/77 (4%) |
| knowingly (doing it with knowledge) | unclear | `␣knowingly` | 3/152 (2%) | 2/81 (2%) | 2/138 (1%) | 0/158 (0%) | 3/79 (4%) | 2/77 (3%) |
| unauthorized (acting without authorization) | unclear | `␣unauthorized`, `␣Unauthorized` | 2/152 (1%) | 3/81 (4%) | 0/138 (0%) | 0/158 (0%) | 1/79 (1%) | 3/77 (4%) |
| fake (fake, forged, falsified) | lie | `␣Fake`, `␣fake` | 3/152 (2%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 3/79 (4%) | 0/77 (0%) |
| improper (impropriety) | unclear | `␣improper` | 1/152 (1%) | 1/81 (1%) | 1/138 (1%) | 0/158 (0%) | 1/79 (1%) | 1/77 (1%) |
| wrong (wrong, mistaken) | lie | `␣wrong`, `␣Wrong`, `错`, `误`, `错误`, `错了` | 1/152 (1%) | 1/81 (1%) | 4/138 (3%) | 0/158 (0%) | 1/79 (1%) | 1/77 (1%) |
| bribe (bribery) | unclear | `␣brib` | 1/152 (1%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 1/79 (1%) | 0/77 (0%) |
| fact (fact, factual) | truth | `␣actually` | 1/152 (1%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 0/79 (0%) | 0/77 (0%) |
| false (false, untrue) | lie | `␣fals` | 1/152 (1%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 1/79 (1%) | 0/77 (0%) |
| correct (correct) | truth | `␣correct`, `␣correctly`, `correct`, `␣Correct`, `正确` | 0/152 (0%) | 0/81 (0%) | 0/138 (0%) | 5/158 (3%) | 0/79 (0%) | 0/77 (0%) |
| incorrect (incorrect) | lie | `␣incorrect` | 0/152 (0%) | 0/81 (0%) | 0/138 (0%) | 1/158 (1%) | 0/79 (0%) | 0/77 (0%) |

Not in the draft: truth (excluded: the question's own word)

## q_tok1

| family | side | members | lies | truths | no-pressure truths | unrelated | lies that deny | truths that deny |
|---|---|---|---|---|---|---|---|---|
| intentional (doing it on purpose) | unclear | `␣intentionally`, `␣deliberately`, `␣purposely`, `故意`, `␣intentional`, `␣deliberate`, `刻意`, `特意`, `␣sengaja`, `故意的` | 73/152 (48%) | 52/81 (64%) | 66/138 (48%) | 103/158 (65%) | 50/79 (63%) | 51/77 (66%) |
| knowingly (doing it with knowledge) | unclear | `␣knowingly`, `␣consciously`, `明知` | 63/152 (41%) | 32/81 (40%) | 37/138 (27%) | 23/158 (15%) | 44/79 (56%) | 31/77 (40%) |
| unintentional (doing it by accident) | unclear | `␣accidentally`, `␣inadvertently`, `␣accident`, `␣unintention`, `␣accidental` | 63/152 (41%) | 19/81 (23%) | 53/138 (38%) | 47/158 (30%) | 28/79 (35%) | 17/77 (22%) |
| forget (forgetting) | unclear | `␣forget`, `␣forgot`, `␣forgetting`, `␣Forget`, `␣forgotten`, `forget`, `␣Forgot` | 49/152 (32%) | 31/81 (38%) | 51/138 (37%) | 152/158 (96%) | 20/79 (25%) | 29/77 (38%) |
| mistake (making a mistake) | unclear | `␣mistake`, `␣mistakenly`, `␣mistaken`, `␣mistakes` | 48/152 (32%) | 27/81 (33%) | 81/138 (59%) | 108/158 (68%) | 20/79 (25%) | 26/77 (34%) |
| fact (fact, factual) | truth | `␣actually`, `␣actual`, `␣Actually`, `Actually`, `␣factual`, `actually`, `实际`, `实际上` | 52/152 (34%) | 17/81 (21%) | 18/138 (13%) | 28/158 (18%) | 26/79 (33%) | 16/77 (21%) |
| honest (being honest) | truth | `␣honestly`, `␣honest`, `␣honesty`, `␣Honest` | 45/152 (30%) | 20/81 (25%) | 8/138 (6%) | 0/158 (0%) | 20/79 (25%) | 20/77 (26%) |
| conceal (hiding or covering up information) | lie | `隐瞒`, `␣hiding`, `␣conceal`, `␣undisclosed`, `␣hide`, `hidden`, `␣hidden`, `隐藏`, `隐藏的`, `hide`, `␣Hide`, `␣hides`, `␣Hidden`, `-hidden`, `掩盖`, `隐蔽` | 47/152 (31%) | 15/81 (19%) | 0/138 (0%) | 0/158 (0%) | 24/79 (30%) | 14/77 (18%) |
| fake (fake, forged, falsified) | lie | `␣fake`, `fake`, `␣Fake`, `伪造`, `Fake`, `造假`, `_fake`, `弄虚作假`, `假的` | 49/152 (32%) | 6/81 (7%) | 0/138 (0%) | 0/158 (0%) | 22/79 (28%) | 4/77 (5%) |
| false (false, untrue) | lie | `␣false`, `␣FALSE`, `␣fals`, `␣falsely`, `␣untrue`, `␣falsehood`, `假`, `虚假` | 37/152 (24%) | 6/81 (7%) | 0/138 (0%) | 0/158 (0%) | 18/79 (23%) | 5/77 (6%) |
| misunderstand (misunderstanding) | unclear | `␣misunderstand`, `␣misunderstood`, `␣misunderstanding` | 14/152 (9%) | 25/81 (31%) | 48/138 (35%) | 54/158 (34%) | 11/79 (14%) | 24/77 (31%) |
| deceive (the act of deceiving) | lie | `欺骗`, `␣deceive`, `␣deception`, `␣deceived`, `骗`, `␣deceptive`, `␣deceit` | 29/152 (19%) | 7/81 (9%) | 0/138 (0%) | 0/158 (0%) | 10/79 (13%) | 6/77 (8%) |
| misinformation (false information given out) | lie | `␣misinformation`, `虚假信息` | 27/152 (18%) | 5/81 (6%) | 6/138 (4%) | 2/158 (1%) | 15/79 (19%) | 4/77 (5%) |
| secret (secrecy, being secret) | lie | `␣secretly`, `秘密`, `␣secrecy`, `␣secret`, `的秘密`, `␣SECRET`, `␣Secret`, `Secret`, `secret`, `␣secretive`, `隐秘`, `␣covert`, `隐蔽` | 20/152 (13%) | 10/81 (12%) | 0/138 (0%) | 0/158 (0%) | 11/79 (14%) | 10/77 (13%) |
| confidential (keeping information confidential) | unclear | `␣confidentiality`, `␣confidential`, `保密`, `␣Confidential` | 16/152 (11%) | 9/81 (11%) | 0/138 (0%) | 0/158 (0%) | 8/79 (10%) | 9/77 (12%) |
| bribe (bribery) | unclear | `␣brib` | 15/152 (10%) | 7/81 (9%) | 1/138 (1%) | 0/158 (0%) | 12/79 (15%) | 7/77 (9%) |
| violate (violating rules) | unclear | `␣violate`, `违反`, `违背`, `␣violating`, `违规` | 6/152 (4%) | 12/81 (15%) | 5/138 (4%) | 1/158 (1%) | 5/79 (6%) | 12/77 (16%) |
| unethical (being unethical) | unclear | `␣unethical` | 9/152 (6%) | 7/81 (9%) | 0/138 (0%) | 0/158 (0%) | 5/79 (6%) | 7/77 (9%) |
| wrong (wrong, mistaken) | lie | `␣wrong`, `␣Wrong`, `␣WRONG`, `错`, `误`, `错误`, `错了` | 11/152 (7%) | 5/81 (6%) | 20/138 (14%) | 32/158 (20%) | 6/79 (8%) | 4/77 (5%) |
| dishonest (being dishonest) | lie | `␣dishonest` | 11/152 (7%) | 4/81 (5%) | 0/138 (0%) | 0/158 (0%) | 6/79 (8%) | 4/77 (5%) |
| refuse (refusing) | unclear | `␣refuse`, `拒绝`, `␣refusal`, `␣refusing`, `␣refused`, `␣refus` | 3/152 (2%) | 12/81 (15%) | 1/138 (1%) | 0/158 (0%) | 3/79 (4%) | 12/77 (16%) |
| mislead (leading someone to a wrong belief) | lie | `␣misleading`, `␣misled`, `误导` | 11/152 (7%) | 3/81 (4%) | 0/138 (0%) | 0/158 (0%) | 3/79 (4%) | 2/77 (3%) |
| disclose (disclosing information) | truth | `␣disclose`, `␣disclosure`, `␣Disclosure`, `␣disclosing`, `␣disclosures` | 3/152 (2%) | 11/81 (14%) | 1/138 (1%) | 0/158 (0%) | 1/79 (1%) | 11/77 (14%) |
| voluntary (doing it willingly) | unclear | `␣voluntarily`, `␣willingly` | 4/152 (3%) | 9/81 (11%) | 6/138 (4%) | 0/158 (0%) | 4/79 (5%) | 9/77 (12%) |
| whistleblow (whistleblowing) | unclear | `␣whistleblower`, `␣whistlebl` | 4/152 (3%) | 8/81 (10%) | 0/138 (0%) | 0/158 (0%) | 3/79 (4%) | 8/77 (10%) |
| illegal (illegality) | unclear | `␣illegally`, `␣illegal` | 4/152 (3%) | 5/81 (6%) | 1/138 (1%) | 0/158 (0%) | 4/79 (5%) | 5/77 (6%) |
| disobey (disobeying) | unclear | `␣disob` | 2/152 (1%) | 6/81 (7%) | 0/138 (0%) | 0/158 (0%) | 1/79 (1%) | 6/77 (8%) |
| leak (leaking information) | unclear | `␣leaked`, `␣leak`, `泄露` | 3/152 (2%) | 4/81 (5%) | 0/138 (0%) | 0/158 (0%) | 2/79 (3%) | 4/77 (5%) |
| fraud (fraud, swindling) | lie | `␣fraud`, `␣fraudulent`, `欺诈`, `弄虚作假` | 5/152 (3%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 4/79 (5%) | 1/77 (1%) |
| fabricate (making something up) | lie | `虚构`, `␣fabricated` | 4/152 (3%) | 2/81 (2%) | 0/138 (0%) | 1/158 (1%) | 2/79 (3%) | 1/77 (1%) |
| cheat (cheating) | lie | `␣cheating`, `作弊` | 5/152 (3%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 4/79 (5%) | 0/77 (0%) |
| sincere (sincerity) | truth | `␣sincerely` | 3/152 (2%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 1/79 (1%) | 1/77 (1%) |
| unauthorized (acting without authorization) | unclear | `␣unauthorized` | 3/152 (2%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 2/79 (3%) | 1/77 (1%) |
| undisclosed (not disclosed) | lie | `␣undisclosed` | 2/152 (1%) | 2/81 (2%) | 0/138 (0%) | 0/158 (0%) | 2/79 (3%) | 2/77 (3%) |
| pretend (pretending, putting on a false appearance) | lie | `␣pretending`, `␣pretend` | 3/152 (2%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 2/79 (3%) | 0/77 (0%) |
| apologize (apologizing) | unclear | `␣apologize`, `␣apologized` | 3/152 (2%) | 0/81 (0%) | 18/138 (13%) | 0/158 (0%) | 3/79 (4%) | 0/77 (0%) |
| accuse (accusation, allegation) | unclear | `␣accusations`, `␣allegations`, `␣alleged` | 3/152 (2%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 3/79 (4%) | 0/77 (0%) |
| integrity (integrity, good faith) | truth | `诚信` | 1/152 (1%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 0/79 (0%) | 1/77 (1%) |
| candid (being frank and open) | truth | `坦诚` | 0/152 (0%) | 2/81 (2%) | 0/138 (0%) | 0/158 (0%) | 0/79 (0%) | 2/77 (3%) |
| transparent (transparency) | truth | `␣transparency`, `␣Transparency` | 0/152 (0%) | 2/81 (2%) | 0/138 (0%) | 0/158 (0%) | 0/79 (0%) | 2/77 (3%) |
| confess (confessing) | truth | `坦白`, `␣confession` | 0/152 (0%) | 2/81 (2%) | 0/138 (0%) | 0/158 (0%) | 0/79 (0%) | 2/77 (3%) |
| evade (evading) | unclear | `回避` | 1/152 (1%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 1/79 (1%) | 1/77 (1%) |
| contradict (contradicting, contradiction) | unclear | `␣contradict` | 0/152 (0%) | 2/81 (2%) | 3/138 (2%) | 0/158 (0%) | 0/79 (0%) | 1/77 (1%) |
| allege (alleging) | unclear | `␣allegations` | 2/152 (1%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 2/79 (3%) | 0/77 (0%) |
| reject (rejecting, negating) | unclear | `␣reject`, `␣Reject`, `Reject`, `␣rejection` | 0/152 (0%) | 2/81 (2%) | 0/138 (0%) | 0/158 (0%) | 0/79 (0%) | 2/77 (3%) |
| ethics / morality (ethics, morality) | unclear | `␣ethics`, `道德` | 1/152 (1%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 0/79 (0%) | 1/77 (1%) |
| incorrect (incorrect) | lie | `␣incorrect`, `Incorrect`, `␣incorrectly`, `␣inaccurate`, `incorrect`, `␣Incorrect`, `错误的` | 2/152 (1%) | 0/81 (0%) | 4/138 (3%) | 12/158 (8%) | 2/79 (3%) | 0/77 (0%) |
| omit (leaving information out) | lie | `␣omit` | 0/152 (0%) | 1/81 (1%) | 0/138 (0%) | 1/158 (1%) | 0/79 (0%) | 1/77 (1%) |
| manipulate (manipulating someone) | lie | `␣manipulate` | 1/152 (1%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 1/79 (1%) | 0/77 (0%) |
| accuse (accusing) | unclear | `␣accusations` | 1/152 (1%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 1/79 (1%) | 0/77 (0%) |
| ethical (being ethical) | unclear | `␣ethical`, `␣ethics` | 1/152 (1%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 0/79 (0%) | 0/77 (0%) |
| regret (regret) | unclear | `␣regret` | 0/152 (0%) | 1/81 (1%) | 2/138 (1%) | 0/158 (0%) | 0/79 (0%) | 1/77 (1%) |
| betray (betrayal) | lie | `␣betray` | 0/152 (0%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 0/79 (0%) | 1/77 (1%) |
| exaggerate (exaggerating) | lie | `夸大` | 1/152 (1%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 0/79 (0%) | 0/77 (0%) |
| fictional (fiction, fictional) | unclear | `␣fictional` | 0/152 (0%) | 1/81 (1%) | 0/138 (0%) | 1/158 (1%) | 0/79 (0%) | 1/77 (1%) |
| true (true, real) | truth | `真的`, `真正`, `真正的` | 1/152 (1%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 1/79 (1%) | 0/77 (0%) |
| correct (correct) | truth | `␣correct`, `␣correctly`, `␣corrected`, `␣Correct`, `␣corrections`, `␣correcting`, `正确`, `改正` | 0/152 (0%) | 0/81 (0%) | 7/138 (5%) | 48/158 (30%) | 0/79 (0%) | 0/77 (0%) |
| accurate (accurate) | truth | `␣accurately` | 0/152 (0%) | 0/81 (0%) | 0/138 (0%) | 2/158 (1%) | 0/79 (0%) | 0/77 (0%) |

Not in the draft: admit (excluded: admit / deny / acknowledge); acknowledge (excluded: admit / deny / acknowledge); deny (excluded: admit / deny / acknowledge); truth (excluded: the question's own word)

## q_tok2

| family | side | members | lies | truths | no-pressure truths | unrelated | lies that deny | truths that deny |
|---|---|---|---|---|---|---|---|---|
| deceive (the act of deceiving) | lie | `欺骗`, `骗`, `␣deception`, `␣deceive`, `␣deceit`, `␣deceived` | 152/152 (100%) | 81/81 (100%) | 138/138 (100%) | 158/158 (100%) | 79/79 (100%) | 77/77 (100%) |
| fake (fake, forged, falsified) | lie | `fake`, `␣fake`, `造假`, `Fake`, `伪造`, `␣Fake`, `_fake`, `假的` | 152/152 (100%) | 81/81 (100%) | 138/138 (100%) | 158/158 (100%) | 79/79 (100%) | 77/77 (100%) |
| false (false, untrue) | lie | `␣false`, `false`, `␣fals`, `␣falsely`, `␣untrue`, `/false`, `␣falsehood`, `假`, `虚假` | 152/152 (100%) | 81/81 (100%) | 138/138 (100%) | 158/158 (100%) | 79/79 (100%) | 77/77 (100%) |
| dishonest (being dishonest) | lie | `␣dishonest` | 152/152 (100%) | 80/81 (99%) | 134/138 (97%) | 146/158 (92%) | 79/79 (100%) | 76/77 (99%) |
| integrity (integrity, good faith) | truth | `诚信` | 98/152 (64%) | 36/81 (44%) | 36/138 (26%) | 41/158 (26%) | 41/79 (52%) | 34/77 (44%) |
| conceal (hiding or covering up information) | lie | `隐瞒`, `␣conceal`, `hide`, `␣hiding`, `掩盖` | 41/152 (27%) | 54/81 (67%) | 46/138 (33%) | 0/158 (0%) | 29/79 (37%) | 53/77 (69%) |
| mislead (leading someone to a wrong belief) | lie | `误导`, `␣misled` | 44/152 (29%) | 35/81 (43%) | 13/138 (9%) | 0/158 (0%) | 27/79 (34%) | 33/77 (43%) |
| fraud (fraud, swindling) | lie | `欺诈` | 33/152 (22%) | 24/81 (30%) | 14/138 (10%) | 0/158 (0%) | 22/79 (28%) | 23/77 (30%) |
| intentional (doing it on purpose) | unclear | `␣intentionally`, `故意`, `␣deliberately`, `␣intentional`, `␣purposely`, `刻意` | 16/152 (11%) | 11/81 (14%) | 18/138 (13%) | 0/158 (0%) | 11/79 (14%) | 9/77 (12%) |
| misinformation (false information given out) | lie | `虚假信息`, `␣misinformation` | 2/152 (1%) | 4/81 (5%) | 4/138 (3%) | 18/158 (11%) | 1/79 (1%) | 4/77 (5%) |
| pretend (pretending, putting on a false appearance) | lie | `␣pretending` | 1/152 (1%) | 5/81 (6%) | 19/138 (14%) | 31/158 (20%) | 1/79 (1%) | 5/77 (6%) |
| knowingly (doing it with knowledge) | unclear | `␣knowingly` | 3/152 (2%) | 2/81 (2%) | 0/138 (0%) | 0/158 (0%) | 2/79 (3%) | 2/77 (3%) |
| cheat (cheating) | lie | `␣cheating` | 0/152 (0%) | 3/81 (4%) | 0/138 (0%) | 33/158 (21%) | 0/79 (0%) | 3/77 (4%) |
| misrepresent (presenting something inaccurately) | lie | `␣misrepresented` | 0/152 (0%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 0/79 (0%) | 1/77 (1%) |
| omit (leaving information out) | lie | `␣omit`, `␣omission` | 1/152 (1%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 1/79 (1%) | 0/77 (0%) |
| fabricate (making something up) | lie | `虚构` | 1/152 (1%) | 0/81 (0%) | 0/138 (0%) | 6/158 (4%) | 0/79 (0%) | 0/77 (0%) |
| accuse (accusing) | unclear | `␣accusations` | 1/152 (1%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 1/79 (1%) | 0/77 (0%) |

Not in the draft: honest (excluded: the question's own word); truth (excluded: the question's own word)

## q_tok3

| family | side | members | lies | truths | no-pressure truths | unrelated | lies that deny | truths that deny |
|---|---|---|---|---|---|---|---|---|
| fake (fake, forged, falsified) | lie | `fake`, `␣fake`, `␣Fake`, `Fake`, `伪造`, `造假`, `_fake` | 130/152 (86%) | 60/81 (74%) | 123/138 (89%) | 143/158 (91%) | 71/79 (90%) | 57/77 (74%) |
| false (false, untrue) | lie | `␣false`, `false`, `␣fals`, `␣falsely`, `␣untrue`, `␣falsehood`, `假`, `虚假` | 125/152 (82%) | 55/81 (68%) | 127/138 (92%) | 148/158 (94%) | 70/79 (89%) | 52/77 (68%) |
| deceive (the act of deceiving) | lie | `欺骗`, `␣deception`, `␣deceit`, `骗`, `␣deceive` | 98/152 (64%) | 35/81 (43%) | 39/138 (28%) | 92/158 (58%) | 54/79 (68%) | 34/77 (44%) |
| misinformation (false information given out) | lie | `␣misinformation` | 57/152 (38%) | 33/81 (41%) | 97/138 (70%) | 9/158 (6%) | 40/79 (51%) | 33/77 (43%) |
| honest (being honest) | truth | `␣honesty`, `␣honest` | 54/152 (36%) | 10/81 (12%) | 3/138 (2%) | 66/158 (42%) | 18/79 (23%) | 8/77 (10%) |
| mislead (leading someone to a wrong belief) | lie | `␣misleading`, `误导` | 14/152 (9%) | 15/81 (19%) | 8/138 (6%) | 0/158 (0%) | 9/79 (11%) | 15/77 (19%) |
| wrong (wrong, mistaken) | lie | `␣wrong`, `错误` | 16/152 (11%) | 11/81 (14%) | 2/138 (1%) | 3/158 (2%) | 15/79 (19%) | 11/77 (14%) |
| accuse (accusing) | unclear | `␣accusations`, `␣accusation`, `␣accusing`, `指控`, `␣allegations`, `␣allegation` | 19/152 (12%) | 6/81 (7%) | 8/138 (6%) | 2/158 (1%) | 18/79 (23%) | 5/77 (6%) |
| conceal (hiding or covering up information) | lie | `隐瞒`, `␣undisclosed` | 15/152 (10%) | 9/81 (11%) | 5/138 (4%) | 0/158 (0%) | 10/79 (13%) | 9/77 (12%) |
| dishonest (being dishonest) | lie | `␣dishonest` | 16/152 (11%) | 3/81 (4%) | 4/138 (3%) | 43/158 (27%) | 8/79 (10%) | 3/77 (4%) |
| allege (alleging) | unclear | `␣allegations`, `␣allegation` | 12/152 (8%) | 3/81 (4%) | 4/138 (3%) | 0/158 (0%) | 12/79 (15%) | 3/77 (4%) |
| misrepresent (presenting something inaccurately) | lie | `␣misrepresented` | 9/152 (6%) | 5/81 (6%) | 1/138 (1%) | 0/158 (0%) | 5/79 (6%) | 5/77 (6%) |
| fraud (fraud, swindling) | lie | `␣fraudulent`, `␣fraud`, `␣Fraud`, `欺诈` | 10/152 (7%) | 3/81 (4%) | 3/138 (2%) | 0/158 (0%) | 9/79 (11%) | 3/77 (4%) |
| propaganda (one-sided persuasive messaging) | lie | `␣propaganda` | 2/152 (1%) | 4/81 (5%) | 1/138 (1%) | 0/158 (0%) | 1/79 (1%) | 4/77 (5%) |
| intentional (doing it on purpose) | unclear | `故意`, `␣intentionally` | 4/152 (3%) | 2/81 (2%) | 3/138 (2%) | 0/158 (0%) | 2/79 (3%) | 2/77 (3%) |
| pretend (pretending, putting on a false appearance) | lie | `␣pretending`, `伪装` | 0/152 (0%) | 4/81 (5%) | 3/138 (2%) | 0/158 (0%) | 0/79 (0%) | 4/77 (5%) |
| disclose (disclosing information) | truth | `␣disclosures`, `␣disclosure` | 3/152 (2%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 3/79 (4%) | 1/77 (1%) |
| whistleblow (whistleblowing) | unclear | `␣whistleblower`, `␣whistlebl` | 4/152 (3%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 4/79 (5%) | 0/77 (0%) |
| bullshit (speech careless of the truth) | lie | `␣bullshit` | 3/152 (2%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 0/79 (0%) | 0/77 (0%) |
| integrity (integrity, good faith) | truth | `诚信` | 3/152 (2%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 2/79 (3%) | 0/77 (0%) |
| fabricate (making something up) | lie | `虚构` | 0/152 (0%) | 2/81 (2%) | 0/138 (0%) | 0/158 (0%) | 0/79 (0%) | 2/77 (3%) |
| incorrect (incorrect) | lie | `␣incorrect`, `错误的` | 2/152 (1%) | 0/81 (0%) | 2/138 (1%) | 0/158 (0%) | 1/79 (1%) | 0/77 (0%) |
| secret (secrecy, being secret) | lie | `秘密` | 0/152 (0%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 0/79 (0%) | 1/77 (1%) |
| cheat (cheating) | lie | `␣cheating` | 1/152 (1%) | 0/81 (0%) | 1/138 (1%) | 64/158 (41%) | 0/79 (0%) | 0/77 (0%) |
| contradict (contradicting, contradiction) | unclear | `␣contradict` | 1/152 (1%) | 0/81 (0%) | 1/138 (1%) | 0/158 (0%) | 1/79 (1%) | 0/77 (0%) |
| violate (violating rules) | unclear | `违反` | 0/152 (0%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 0/79 (0%) | 1/77 (1%) |
| apologize (apologizing) | unclear | `␣apology` | 1/152 (1%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 1/79 (1%) | 0/77 (0%) |
| undisclosed (not disclosed) | lie | `␣undisclosed` | 1/152 (1%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 1/79 (1%) | 0/77 (0%) |
| betray (betrayal) | lie | `␣betrayal` | 0/152 (0%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 0/79 (0%) | 1/77 (1%) |

Not in the draft: admit (excluded: admit / deny / acknowledge); deny (excluded: admit / deny / acknowledge); truth (excluded: the question's own word)

## q_tok4

| family | side | members | lies | truths | no-pressure truths | unrelated | lies that deny | truths that deny |
|---|---|---|---|---|---|---|---|---|
| false (false, untrue) | lie | `␣false`, `␣FALSE`, `␣fals`, `␣falsely`, `␣falsehood`, `假`, `虚假` | 80/152 (53%) | 37/81 (46%) | 10/138 (7%) | 43/158 (27%) | 40/79 (51%) | 34/77 (44%) |
| fake (fake, forged, falsified) | lie | `fake`, `␣fake`, `Fake`, `␣Fake`, `伪造`, `假的` | 57/152 (38%) | 27/81 (33%) | 8/138 (6%) | 128/158 (81%) | 25/79 (32%) | 24/77 (31%) |
| misinformation (false information given out) | lie | `␣misinformation`, `虚假信息` | 58/152 (38%) | 16/81 (20%) | 6/138 (4%) | 90/158 (57%) | 31/79 (39%) | 14/77 (18%) |
| deceive (the act of deceiving) | lie | `欺骗` | 34/152 (22%) | 14/81 (17%) | 1/138 (1%) | 19/158 (12%) | 14/79 (18%) | 12/77 (16%) |
| mislead (leading someone to a wrong belief) | lie | `误导`, `␣misleading` | 15/152 (10%) | 13/81 (16%) | 1/138 (1%) | 1/158 (1%) | 8/79 (10%) | 11/77 (14%) |
| refuse (refusing) | unclear | `拒绝`, `␣refusal`, `␣refus`, `␣refusing` | 1/152 (1%) | 13/81 (16%) | 0/138 (0%) | 0/158 (0%) | 1/79 (1%) | 13/77 (17%) |
| conceal (hiding or covering up information) | lie | `隐瞒` | 6/152 (4%) | 5/81 (6%) | 0/138 (0%) | 0/158 (0%) | 3/79 (4%) | 5/77 (6%) |
| apologize (apologizing) | unclear | `␣apology`, `␣apologies` | 5/152 (3%) | 5/81 (6%) | 3/138 (2%) | 0/158 (0%) | 4/79 (5%) | 5/77 (6%) |
| wrong (wrong, mistaken) | lie | `␣wrong`, `␣WRONG`, `错误` | 3/152 (2%) | 6/81 (7%) | 8/138 (6%) | 1/158 (1%) | 2/79 (3%) | 6/77 (8%) |
| whistleblow (whistleblowing) | unclear | `␣whistleblower`, `␣whistlebl` | 7/152 (5%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 6/79 (8%) | 1/77 (1%) |
| propaganda (one-sided persuasive messaging) | lie | `␣propaganda` | 4/152 (3%) | 3/81 (4%) | 1/138 (1%) | 0/158 (0%) | 2/79 (3%) | 3/77 (4%) |
| fabricate (making something up) | lie | `虚构` | 1/152 (1%) | 5/81 (6%) | 2/138 (1%) | 0/158 (0%) | 0/79 (0%) | 4/77 (5%) |
| reject (rejecting, negating) | unclear | `␣Reject`, `Reject`, `␣rejection`, `␣rejecting`, `否定` | 3/152 (2%) | 3/81 (4%) | 0/138 (0%) | 0/158 (0%) | 3/79 (4%) | 3/77 (4%) |
| fictional (fiction, fictional) | unclear | `␣fictional`, `fiction`, `␣Fiction` | 0/152 (0%) | 5/81 (6%) | 0/138 (0%) | 2/158 (1%) | 0/79 (0%) | 5/77 (6%) |
| accuse (accusing) | unclear | `␣accusations`, `␣allegations` | 4/152 (3%) | 0/81 (0%) | 1/138 (1%) | 0/158 (0%) | 3/79 (4%) | 0/77 (0%) |
| disclose (disclosing information) | truth | `␣disclosures`, `␣disclosure` | 2/152 (1%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 2/79 (3%) | 1/77 (1%) |
| allege (alleging) | unclear | `␣allegations` | 3/152 (2%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 2/79 (3%) | 0/77 (0%) |
| incorrect (incorrect) | lie | `␣incorrect`, `␣Incorrect`, `错误的` | 0/152 (0%) | 3/81 (4%) | 1/138 (1%) | 8/158 (5%) | 0/79 (0%) | 3/77 (4%) |
| misrepresent (presenting something inaccurately) | lie | `␣misrepresented` | 0/152 (0%) | 2/81 (2%) | 1/138 (1%) | 0/158 (0%) | 0/79 (0%) | 2/77 (3%) |
| secret (secrecy, being secret) | lie | `␣secrecy` | 1/152 (1%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 1/79 (1%) | 0/77 (0%) |
| intentional (doing it on purpose) | unclear | `故意` | 1/152 (1%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 0/79 (0%) | 0/77 (0%) |
| ethical (being ethical) | unclear | `␣ethics` | 0/152 (0%) | 1/81 (1%) | 1/138 (1%) | 0/158 (0%) | 0/79 (0%) | 1/77 (1%) |
| fact (fact, factual) | truth | `␣facts`, `␣factual` | 0/152 (0%) | 1/81 (1%) | 1/138 (1%) | 1/158 (1%) | 0/79 (0%) | 1/77 (1%) |
| correct (correct) | truth | `␣corrections` | 0/152 (0%) | 0/81 (0%) | 0/138 (0%) | 1/158 (1%) | 0/79 (0%) | 0/77 (0%) |

Not in the draft: honest (excluded: the question's own word); admit (excluded: admit / deny / acknowledge); acknowledge (excluded: admit / deny / acknowledge); deny (excluded: admit / deny / acknowledge); truth (excluded: the question's own word)

## q_tok5

| family | side | members | lies | truths | no-pressure truths | unrelated | lies that deny | truths that deny |
|---|---|---|---|---|---|---|---|---|
| wrong (wrong, mistaken) | lie | `␣ERROR`, `␣WRONG`, `错误` | 23/152 (15%) | 11/81 (14%) | 3/138 (2%) | 0/158 (0%) | 13/79 (16%) | 11/77 (14%) |
| incorrect (incorrect) | lie | `␣incorrect` | 5/152 (3%) | 3/81 (4%) | 4/138 (3%) | 15/158 (9%) | 4/79 (5%) | 3/77 (4%) |
| misinformation (false information given out) | lie | `␣misinformation` | 3/152 (2%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 3/79 (4%) | 0/77 (0%) |
| disclose (disclosing information) | truth | `␣disclosures` | 1/152 (1%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 1/79 (1%) | 1/77 (1%) |
| apologize (apologizing) | unclear | `␣apologies` | 1/152 (1%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 1/79 (1%) | 0/77 (0%) |

## q_tok6

| family | side | members | lies | truths | no-pressure truths | unrelated | lies that deny | truths that deny |
|---|---|---|---|---|---|---|---|---|
| mislead (leading someone to a wrong belief) | lie | `␣misleading`, `误导`, `误导性` | 152/152 (100%) | 81/81 (100%) | 136/138 (99%) | 111/158 (70%) | 79/79 (100%) | 77/77 (100%) |
| false (false, untrue) | lie | `␣false`, `␣False`, `false`, `False`, `␣FALSE`, `␣fals`, `␣falsely`, `␣untrue`, `␣falsehood`, `假`, `虚假` | 152/152 (100%) | 80/81 (99%) | 136/138 (99%) | 117/158 (74%) | 79/79 (100%) | 76/77 (99%) |
| deceive (the act of deceiving) | lie | `欺骗`, `␣deception`, `␣deceptive`, `骗` | 147/152 (97%) | 66/81 (81%) | 57/138 (41%) | 13/158 (8%) | 78/79 (99%) | 62/77 (81%) |
| misinformation (false information given out) | lie | `␣misinformation`, `虚假信息` | 146/152 (96%) | 56/81 (69%) | 104/138 (75%) | 104/158 (66%) | 76/79 (96%) | 52/77 (68%) |
| incorrect (incorrect) | lie | `␣incorrect`, `Incorrect`, `␣inaccur`, `␣incorrectly`, `␣inaccurate`, `incorrect`, `␣erroneous`, `␣Incorrect`, `错误的` | 129/152 (85%) | 63/81 (78%) | 136/138 (99%) | 145/158 (92%) | 62/79 (78%) | 60/77 (78%) |
| conceal (hiding or covering up information) | lie | `隐瞒`, `␣undisclosed` | 128/152 (84%) | 50/81 (62%) | 25/138 (18%) | 1/158 (1%) | 64/79 (81%) | 46/77 (60%) |
| fake (fake, forged, falsified) | lie | `␣fake`, `fake`, `伪造`, `␣Fake`, `Fake`, `造假`, `假的` | 117/152 (77%) | 55/81 (68%) | 81/138 (59%) | 98/158 (62%) | 52/79 (66%) | 52/77 (68%) |
| contradict (contradicting, contradiction) | unclear | `␣contradict`, `␣contradictory`, `␣contradiction`, `␣contrad` | 52/152 (34%) | 61/81 (75%) | 91/138 (66%) | 5/158 (3%) | 30/79 (38%) | 59/77 (77%) |
| wrong (wrong, mistaken) | lie | `␣wrong`, `␣ERROR`, `␣WRONG`, `错误` | 70/152 (46%) | 38/81 (47%) | 63/138 (46%) | 63/158 (40%) | 38/79 (48%) | 36/77 (47%) |
| fabricate (making something up) | lie | `虚构` | 20/152 (13%) | 10/81 (12%) | 41/138 (30%) | 39/158 (25%) | 7/79 (9%) | 9/77 (12%) |
| dishonest (being dishonest) | lie | `␣dishonest` | 15/152 (10%) | 8/81 (10%) | 0/138 (0%) | 0/158 (0%) | 11/79 (14%) | 8/77 (10%) |
| refuse (refusing) | unclear | `拒绝`, `␣refusal`, `␣refus`, `␣refusing` | 0/152 (0%) | 22/81 (27%) | 1/138 (1%) | 0/158 (0%) | 0/79 (0%) | 22/77 (29%) |
| intentional (doing it on purpose) | unclear | `␣intentionally`, `故意`, `␣deliberately`, `刻意` | 6/152 (4%) | 9/81 (11%) | 0/138 (0%) | 0/158 (0%) | 2/79 (3%) | 8/77 (10%) |
| reject (rejecting, negating) | unclear | `␣rejection`, `␣rejecting`, `否定` | 3/152 (2%) | 7/81 (9%) | 0/138 (0%) | 0/158 (0%) | 2/79 (3%) | 7/77 (9%) |
| misrepresent (presenting something inaccurately) | lie | `␣misrepresented` | 5/152 (3%) | 4/81 (5%) | 0/138 (0%) | 0/158 (0%) | 4/79 (5%) | 4/77 (5%) |
| fact (fact, factual) | truth | `␣facts`, `␣factual`, `事实` | 3/152 (2%) | 5/81 (6%) | 11/138 (8%) | 17/158 (11%) | 1/79 (1%) | 5/77 (6%) |
| fraud (fraud, swindling) | lie | `␣fraudulent` | 7/152 (5%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 3/79 (4%) | 0/77 (0%) |
| pretend (pretending, putting on a false appearance) | lie | `␣pretending` | 0/152 (0%) | 7/81 (9%) | 2/138 (1%) | 3/158 (2%) | 0/79 (0%) | 7/77 (9%) |
| honest (being honest) | truth | `␣honesty`, `␣honest`, `␣honestly` | 1/152 (1%) | 5/81 (6%) | 2/138 (1%) | 4/158 (3%) | 1/79 (1%) | 5/77 (6%) |
| hypocrisy (professing what one does not practise) | lie | `␣hypocrisy` | 0/152 (0%) | 5/81 (6%) | 0/138 (0%) | 0/158 (0%) | 0/79 (0%) | 5/77 (6%) |
| allege (alleging) | unclear | `␣allegations`, `␣alleging` | 5/152 (3%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 4/79 (5%) | 0/77 (0%) |
| fictional (fiction, fictional) | unclear | `␣fictional` | 5/152 (3%) | 0/81 (0%) | 5/138 (4%) | 21/158 (13%) | 1/79 (1%) | 0/77 (0%) |
| omit (leaving information out) | lie | `␣omit`, `␣omission` | 3/152 (2%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 2/79 (3%) | 1/77 (1%) |
| undisclosed (not disclosed) | lie | `␣undisclosed` | 2/152 (1%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 1/79 (1%) | 1/77 (1%) |
| evade (evading) | unclear | `回避`, `␣evasion`, `规避` | 2/152 (1%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 1/79 (1%) | 0/77 (0%) |
| avoid (avoiding) | unclear | `␣avoiding`, `avoid`, `避开`, `␣evasion`, `回避`, `规避` | 2/152 (1%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 1/79 (1%) | 0/77 (0%) |
| unethical (being unethical) | unclear | `␣unethical` | 2/152 (1%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 1/79 (1%) | 0/77 (0%) |
| correct (correct) | truth | `␣correct`, `␣correctly`, `␣Correct`, `␣correctness` | 0/152 (0%) | 2/81 (2%) | 17/138 (12%) | 55/158 (35%) | 0/79 (0%) | 2/77 (3%) |
| violate (violating rules) | unclear | `违背` | 0/152 (0%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 0/79 (0%) | 1/77 (1%) |
| accurate (accurate) | truth | `␣accurate`, `␣accuracy` | 0/152 (0%) | 1/81 (1%) | 0/138 (0%) | 3/158 (2%) | 0/79 (0%) | 1/77 (1%) |

Not in the draft: admit (excluded: admit / deny / acknowledge); acknowledge (excluded: admit / deny / acknowledge); deny (excluded: admit / deny / acknowledge); truth (excluded: the question's own word); true (excluded: the question's own word)

## q_tok7

| family | side | members | lies | truths | no-pressure truths | unrelated | lies that deny | truths that deny |
|---|---|---|---|---|---|---|---|---|
| deceive (the act of deceiving) | lie | `欺骗`, `␣deception`, `␣deceive`, `␣deceit` | 133/152 (88%) | 78/81 (96%) | 134/138 (97%) | 158/158 (100%) | 68/79 (86%) | 74/77 (96%) |
| honest (being honest) | truth | `␣honesty`, `␣honest`, `␣honestly`, `␣Honest` | 138/152 (91%) | 63/81 (78%) | 128/138 (93%) | 158/158 (100%) | 69/79 (87%) | 59/77 (77%) |
| false (false, untrue) | lie | `false`, `False`, `␣fals`, `/false`, `␣falsehood`, `虚假` | 91/152 (60%) | 56/81 (69%) | 129/138 (93%) | 147/158 (93%) | 57/79 (72%) | 53/77 (69%) |
| accuse (accusing) | unclear | `␣accusations`, `␣accusation`, `␣accuse`, `␣accusing`, `␣accused`, `␣accuses`, `指控`, `␣allegations`, `␣alleged` | 89/152 (59%) | 56/81 (69%) | 103/138 (75%) | 10/158 (6%) | 54/79 (68%) | 55/77 (71%) |
| dishonest (being dishonest) | lie | `␣dishonest` | 102/152 (67%) | 42/81 (52%) | 105/138 (76%) | 154/158 (97%) | 52/79 (66%) | 40/77 (52%) |
| integrity (integrity, good faith) | truth | `诚信` | 48/152 (32%) | 16/81 (20%) | 66/138 (48%) | 153/158 (97%) | 20/79 (25%) | 15/77 (19%) |
| fake (fake, forged, falsified) | lie | `fake`, `Fake` | 10/152 (7%) | 9/81 (11%) | 10/138 (7%) | 102/158 (65%) | 5/79 (6%) | 9/77 (12%) |
| doubt (challenging, calling into question) | unclear | `质疑` | 12/152 (8%) | 5/81 (6%) | 7/138 (5%) | 0/158 (0%) | 7/79 (9%) | 4/77 (5%) |
| knowingly (doing it with knowledge) | unclear | `明知` | 10/152 (7%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 5/79 (6%) | 0/77 (0%) |
| allege (alleging) | unclear | `␣allegations` | 2/152 (1%) | 4/81 (5%) | 3/138 (2%) | 0/158 (0%) | 2/79 (3%) | 3/77 (4%) |
| fraud (fraud, swindling) | lie | `欺诈` | 2/152 (1%) | 2/81 (2%) | 9/138 (7%) | 72/158 (46%) | 2/79 (3%) | 2/77 (3%) |
| contradict (contradicting, contradiction) | unclear | `␣contradiction`, `␣contradict`, `␣contradictory`, `␣contradictions`, `矛盾` | 0/152 (0%) | 2/81 (2%) | 0/138 (0%) | 0/158 (0%) | 0/79 (0%) | 2/77 (3%) |
| inconsistent (inconsistency) | unclear | `␣inconsistency`, `␣inconsistencies` | 0/152 (0%) | 2/81 (2%) | 0/138 (0%) | 0/158 (0%) | 0/79 (0%) | 2/77 (3%) |
| intentional (doing it on purpose) | unclear | `故意` | 2/152 (1%) | 0/81 (0%) | 0/138 (0%) | 20/158 (13%) | 1/79 (1%) | 0/77 (0%) |
| accurate (accurate) | truth | `␣Accuracy` | 0/152 (0%) | 0/81 (0%) | 0/138 (0%) | 1/158 (1%) | 0/79 (0%) | 0/77 (0%) |

Not in the draft: admit (excluded: admit / deny / acknowledge); truth (excluded: the question's own word); true (excluded: the question's own word)
