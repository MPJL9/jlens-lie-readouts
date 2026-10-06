# Draft families: qwen3.6-27b, J-lens, part Q2_after, group questiona

Written by `scripts/apply_family_decisions.py` (2026-10-01; draft, not frozen). Counts are `present / transcripts (share)`
on the build split.

## q_tok0

| family | side | members | lies | truths | no-pressure truths | unrelated | lies that deny | truths that deny |
|---|---|---|---|---|---|---|---|---|
| intentional (on purpose, deliberately) | unclear | `␣intentional`, `␣intentionally`, `␣intention`, `故意`, `␣deliberate`, `␣deliberately` | 18/152 (12%) | 20/81 (25%) | 29/138 (21%) | 0/158 (0%) | 8/47 (17%) | 20/77 (26%) |
| truthful (telling the truth) | truth | `␣truthful` | 9/152 (6%) | 6/81 (7%) | 3/138 (2%) | 0/158 (0%) | 4/47 (9%) | 6/77 (8%) |
| true (true, real) | truth | `␣TRUE`, `真的`, `确实`, `真实的`, `是真的`, `的真`, `的真实` | 5/152 (3%) | 5/81 (6%) | 0/138 (0%) | 1/158 (1%) | 2/47 (4%) | 5/77 (6%) |
| incorrect (incorrect) | lie | `␣incorrect`, `␣erroneous` | 6/152 (4%) | 4/81 (5%) | 8/138 (6%) | 7/158 (4%) | 4/47 (9%) | 4/77 (5%) |
| knowingly (with knowledge) | unclear | `␣knowingly`, `␣knowing` | 3/152 (2%) | 3/81 (4%) | 3/138 (2%) | 0/158 (0%) | 3/47 (6%) | 3/77 (4%) |
| negligence (negligence) | unclear | `␣negligence`, `␣negligent` | 1/152 (1%) | 4/81 (5%) | 3/138 (2%) | 0/158 (0%) | 1/47 (2%) | 4/77 (5%) |
| honest (being honest) | truth | `␣honest`, `␣honesty`, `␣honestly` | 1/152 (1%) | 2/81 (2%) | 1/138 (1%) | 0/158 (0%) | 0/47 (0%) | 2/77 (3%) |
| improper (improper) | unclear | `␣improper`, `␣improperly` | 1/152 (1%) | 2/81 (2%) | 1/138 (1%) | 0/158 (0%) | 1/47 (2%) | 2/77 (3%) |
| wrong (wrong, mistaken) | lie | `␣wrong`, `␣Wrong`, `错` | 1/152 (1%) | 1/81 (1%) | 3/138 (2%) | 1/158 (1%) | 0/47 (0%) | 1/77 (1%) |
| mislead (misleading someone) | lie | `␣misled` | 0/152 (0%) | 1/81 (1%) | 3/138 (2%) | 0/158 (0%) | 0/47 (0%) | 1/77 (1%) |
| misinformation (false information) | lie | `␣misinformation` | 1/152 (1%) | 0/81 (0%) | 1/138 (1%) | 0/158 (0%) | 1/47 (2%) | 0/77 (0%) |
| fake (fake) | lie | `␣fake` | 1/152 (1%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 0/47 (0%) | 0/77 (0%) |
| cheat (cheating) | lie | `␣cheating` | 1/152 (1%) | 0/81 (0%) | 1/138 (1%) | 0/158 (0%) | 0/47 (0%) | 0/77 (0%) |
| unintentional (not on purpose) | unclear | `␣accidental` | 0/152 (0%) | 1/81 (1%) | 1/138 (1%) | 0/158 (0%) | 0/47 (0%) | 1/77 (1%) |
| apology (apologising) | unclear | `␣sorry` | 1/152 (1%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 0/47 (0%) | 0/77 (0%) |
| mistake (a mistake) | unclear | `␣mistake` | 0/152 (0%) | 1/81 (1%) | 1/138 (1%) | 0/158 (0%) | 0/47 (0%) | 1/77 (1%) |
| intent (intent, intention) | unclear | `␣intention` | 0/152 (0%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 0/47 (0%) | 1/77 (1%) |
| harmful (harmful) | unclear | `␣harmful` | 0/152 (0%) | 1/81 (1%) | 2/138 (1%) | 0/158 (0%) | 0/47 (0%) | 1/77 (1%) |
| correct (correct) | truth | `␣correct`, `␣correctly`, `␣Correct`, `␣correctness`, `␣correcting`, `␣corrective`, `正确`, `正确的`, `的正确` | 0/152 (0%) | 1/81 (1%) | 1/138 (1%) | 8/158 (5%) | 0/47 (0%) | 1/77 (1%) |
| false (false, untrue) | lie | `␣fals` | 1/152 (1%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 0/47 (0%) | 0/77 (0%) |

Not in the draft: truth (excluded: truth from the question on)

## q_tok1

| family | side | members | lies | truths | no-pressure truths | unrelated | lies that deny | truths that deny |
|---|---|---|---|---|---|---|---|---|
| refuse (refusing) | unclear | `␣refusal`, `␣refusing`, `␣refus`, `拒绝` | 6/152 (4%) | 20/81 (25%) | 11/138 (8%) | 1/158 (1%) | 3/47 (6%) | 20/77 (26%) |
| honest (being honest) | truth | `␣honest`, `␣honesty`, `诚实` | 8/152 (5%) | 14/81 (17%) | 10/138 (7%) | 0/158 (0%) | 2/47 (4%) | 14/77 (18%) |
| intentional (on purpose, deliberately) | unclear | `␣intent`, `␣intention`, `␣intentions` | 5/152 (3%) | 12/81 (15%) | 3/138 (2%) | 0/158 (0%) | 2/47 (4%) | 12/77 (16%) |
| confidential (confidentiality) | unclear | `␣confidentiality`, `␣confidential` | 8/152 (5%) | 7/81 (9%) | 1/138 (1%) | 0/158 (0%) | 3/47 (6%) | 7/77 (9%) |
| apology (apologising) | unclear | `␣apology` | 10/152 (7%) | 5/81 (6%) | 16/138 (12%) | 1/158 (1%) | 6/47 (13%) | 5/77 (6%) |
| misinformation (false information) | lie | `␣misinformation` | 8/152 (5%) | 1/81 (1%) | 38/138 (28%) | 4/158 (3%) | 3/47 (6%) | 1/77 (1%) |
| truthful (telling the truth) | truth | `␣truthful` | 5/152 (3%) | 3/81 (4%) | 2/138 (1%) | 0/158 (0%) | 1/47 (2%) | 3/77 (4%) |
| mistake (a mistake) | unclear | `␣mistake` | 4/152 (3%) | 3/81 (4%) | 7/138 (5%) | 4/158 (3%) | 1/47 (2%) | 3/77 (4%) |
| secret (secrecy) | lie | `␣secret`, `␣secretive`, `秘密` | 4/152 (3%) | 2/81 (2%) | 0/138 (0%) | 0/158 (0%) | 2/47 (4%) | 2/77 (3%) |
| disclose (disclosing) | truth | `␣disclosure` | 1/152 (1%) | 4/81 (5%) | 2/138 (1%) | 0/158 (0%) | 0/47 (0%) | 4/77 (5%) |
| fake (fake) | lie | `␣fake` | 3/152 (2%) | 0/81 (0%) | 0/138 (0%) | 1/158 (1%) | 1/47 (2%) | 0/77 (0%) |
| lie (a lie, lying) | lie | `谎言` | 2/152 (1%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 0/47 (0%) | 0/77 (0%) |
| unethical (unethical) | lie | `␣unethical` | 1/152 (1%) | 1/81 (1%) | 1/138 (1%) | 0/158 (0%) | 1/47 (2%) | 1/77 (1%) |
| accusation (an accusation) | unclear | `␣accusations` | 2/152 (1%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 2/47 (4%) | 0/77 (0%) |
| fabricate (fabricated, made up) | lie | `␣fictional` | 0/152 (0%) | 1/81 (1%) | 0/138 (0%) | 2/158 (1%) | 0/47 (0%) | 1/77 (1%) |
| conceal (concealing, hiding information) | lie | `隐瞒` | 1/152 (1%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 1/47 (2%) | 0/77 (0%) |
| reject (rejecting) | unclear | `␣rejection` | 1/152 (1%) | 0/81 (0%) | 1/138 (1%) | 0/158 (0%) | 0/47 (0%) | 0/77 (0%) |
| transparent (transparency) | truth | `␣transparency`, `␣Transparency`, `透明` | 1/152 (1%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 1/47 (2%) | 0/77 (0%) |
| integrity (integrity, good faith) | truth | `␣integrity` | 1/152 (1%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 1/47 (2%) | 0/77 (0%) |
| comply (complying with rules) | unclear | `␣compliance` | 1/152 (1%) | 0/81 (0%) | 1/138 (1%) | 0/158 (0%) | 1/47 (2%) | 0/77 (0%) |
| allegation (an allegation) | unclear | `␣allegations` | 1/152 (1%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 1/47 (2%) | 0/77 (0%) |
| negligence (negligence) | unclear | `␣negligence`, `␣negligent` | 1/152 (1%) | 0/81 (0%) | 1/138 (1%) | 0/158 (0%) | 1/47 (2%) | 0/77 (0%) |
| accurate (accurate) | truth | `␣accuracy`, `␣Accuracy` | 1/152 (1%) | 0/81 (0%) | 4/138 (3%) | 5/158 (3%) | 0/47 (0%) | 0/77 (0%) |
| false (false, untrue) | lie | `␣fals` | 1/152 (1%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 0/47 (0%) | 0/77 (0%) |
| wrong (wrong, mistaken) | lie | `错误` | 0/152 (0%) | 1/81 (1%) | 1/138 (1%) | 1/158 (1%) | 0/47 (0%) | 1/77 (1%) |
| correct (correct) | truth | `␣correct`, `␣correction`, `␣corrected`, `␣Correct`, `␣corrections`, `␣correctness`, `␣Correction`, `␣Corrections`, `修正` | 0/152 (0%) | 0/81 (0%) | 0/138 (0%) | 3/158 (2%) | 0/47 (0%) | 0/77 (0%) |
| fact (fact, factual) | truth | `␣facts` | 0/152 (0%) | 0/81 (0%) | 1/138 (1%) | 0/158 (0%) | 0/47 (0%) | 0/77 (0%) |
| incorrect (incorrect) | lie | `␣incorrect`, `Incorrect`, `incorrect`, `␣Incorrect` | 0/152 (0%) | 0/81 (0%) | 2/138 (1%) | 6/158 (4%) | 0/47 (0%) | 0/77 (0%) |

Not in the draft: truth (excluded: truth from the question on); deny (excluded: admit / deny / acknowledge); acknowledge (excluded: admit / deny / acknowledge)

## q_tok2

| family | side | members | lies | truths | no-pressure truths | unrelated | lies that deny | truths that deny |
|---|---|---|---|---|---|---|---|---|
| incorrect (incorrect) | lie | `␣incorrect`, `Incorrect`, `␣incorrectly`, `␣inaccurate`, `incorrect`, `␣Incorrect`, `错误的` | 80/152 (53%) | 52/81 (64%) | 124/138 (90%) | 73/158 (46%) | 33/47 (70%) | 50/77 (65%) |
| apology (apologising) | unclear | `␣apology`, `␣apologies` | 15/152 (10%) | 14/81 (17%) | 0/138 (0%) | 0/158 (0%) | 10/47 (21%) | 14/77 (18%) |
| wrong (wrong, mistaken) | lie | `␣ERROR`, `错误` | 14/152 (9%) | 12/81 (15%) | 23/138 (17%) | 20/158 (13%) | 8/47 (17%) | 12/77 (16%) |
| misinformation (false information) | lie | `␣misinformation` | 7/152 (5%) | 4/81 (5%) | 0/138 (0%) | 1/158 (1%) | 5/47 (11%) | 4/77 (5%) |
| refuse (refusing) | unclear | `␣refusal` | 2/152 (1%) | 9/81 (11%) | 0/138 (0%) | 0/158 (0%) | 2/47 (4%) | 9/77 (12%) |
| allegation (an allegation) | unclear | `␣allegations`, `␣allegation` | 9/152 (6%) | 2/81 (2%) | 1/138 (1%) | 0/158 (0%) | 9/47 (19%) | 2/77 (3%) |
| accusation (an accusation) | unclear | `␣accusations` | 6/152 (4%) | 4/81 (5%) | 0/138 (0%) | 0/158 (0%) | 6/47 (13%) | 4/77 (5%) |
| lie (a lie, lying) | lie | `谎言`, `谎` | 6/152 (4%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 4/47 (9%) | 0/77 (0%) |
| false (false, untrue) | lie | `␣fals`, `␣falsehood` | 5/152 (3%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 3/47 (6%) | 1/77 (1%) |
| truthful (telling the truth) | truth | `␣truthful` | 4/152 (3%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 2/47 (4%) | 1/77 (1%) |
| mistake (a mistake) | unclear | `␣mistake`, `␣mistakes` | 1/152 (1%) | 3/81 (4%) | 5/138 (4%) | 1/158 (1%) | 1/47 (2%) | 3/77 (4%) |
| misunderstand (misunderstanding) | unclear | `␣misunderstanding` | 0/152 (0%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 0/47 (0%) | 1/77 (1%) |
| correct (correct) | truth | `␣correct`, `␣correction`, `␣corrections` | 0/152 (0%) | 0/81 (0%) | 0/138 (0%) | 3/158 (2%) | 0/47 (0%) | 0/77 (0%) |

Not in the draft: deny (excluded: admit / deny / acknowledge); acknowledge (excluded: admit / deny / acknowledge)

## q_tok3

| family | side | members | lies | truths | no-pressure truths | unrelated | lies that deny | truths that deny |
|---|---|---|---|---|---|---|---|---|
| truthful (telling the truth) | truth | `␣truthful` | 152/152 (100%) | 81/81 (100%) | 138/138 (100%) | 145/158 (92%) | 47/47 (100%) | 77/77 (100%) |
| incorrect (incorrect) | lie | `␣incorrect`, `Incorrect`, `␣inaccur`, `␣incorrectly`, `␣inaccurate`, `incorrect`, `␣erroneous`, `␣Incorrect`, `错误的`, `有误` | 151/152 (99%) | 81/81 (100%) | 138/138 (100%) | 148/158 (94%) | 46/47 (98%) | 77/77 (100%) |
| accurate (accurate) | truth | `␣accurate`, `␣accuracy`, `␣accurately`, `accur`, `准确`, `准确的` | 151/152 (99%) | 80/81 (99%) | 138/138 (100%) | 158/158 (100%) | 47/47 (100%) | 76/77 (99%) |
| correct (correct) | truth | `␣correct`, `␣correctly`, `correct`, `_correct`, `Correct`, `␣corrected`, `␣Correct`, `␣correctness`, `␣correcting`, `.correct`, `正确`, `正确的`, `正确答案`, `的正确`, `是正确的`, `是否正确` | 143/152 (94%) | 78/81 (96%) | 138/138 (100%) | 158/158 (100%) | 38/47 (81%) | 74/77 (96%) |
| honest (being honest) | truth | `␣honest`, `␣honesty`, `␣honestly`, `␣Honest`, `诚实` | 148/152 (97%) | 68/81 (84%) | 94/138 (68%) | 3/158 (2%) | 45/47 (96%) | 66/77 (86%) |
| comply (complying with rules) | unclear | `␣compliant`, `␣complying`, `␣comply`, `␣compliance`, `␣Compliance`, `␣complied`, `合规`, `遵守`, `␣adher`, `␣adherence`, `␣adhere` | 118/152 (78%) | 69/81 (85%) | 94/138 (68%) | 75/158 (47%) | 23/47 (49%) | 65/77 (84%) |
| biased (biased) | unclear | `␣biased` | 105/152 (69%) | 59/81 (73%) | 124/138 (90%) | 112/158 (71%) | 26/47 (55%) | 56/77 (73%) |
| fact (fact, factual) | truth | `␣actually`, `␣factual` | 103/152 (68%) | 36/81 (44%) | 132/138 (96%) | 96/158 (61%) | 40/47 (85%) | 35/77 (45%) |
| appropriate (appropriate) | unclear | `␣appropriate`, `␣appropriately` | 80/152 (53%) | 41/81 (51%) | 17/138 (12%) | 45/158 (28%) | 8/47 (17%) | 38/77 (49%) |
| intentional (on purpose, deliberately) | unclear | `␣intentional`, `␣intentionally`, `␣deliberate`, `␣deliberately` | 67/152 (44%) | 46/81 (57%) | 8/138 (6%) | 2/158 (1%) | 29/47 (62%) | 46/77 (60%) |
| dishonest (being dishonest) | lie | `␣dishonest` | 80/152 (53%) | 30/81 (37%) | 4/138 (3%) | 0/158 (0%) | 34/47 (72%) | 29/77 (38%) |
| inappropriate (inappropriate) | unclear | `␣inappropriate` | 61/152 (40%) | 36/81 (44%) | 1/138 (1%) | 4/158 (3%) | 7/47 (15%) | 33/77 (43%) |
| mislead (misleading someone) | lie | `␣misleading`, `␣misled`, `误导` | 62/152 (41%) | 23/81 (28%) | 27/138 (20%) | 1/158 (1%) | 37/47 (79%) | 22/77 (29%) |
| misinformation (false information) | lie | `␣misinformation`, `虚假信息` | 58/152 (38%) | 12/81 (15%) | 45/138 (33%) | 8/158 (5%) | 29/47 (62%) | 11/77 (14%) |
| mistake (a mistake) | unclear | `␣mistake`, `␣mistaken`, `␣mistakenly` | 36/152 (24%) | 32/81 (40%) | 46/138 (33%) | 0/158 (0%) | 21/47 (45%) | 32/77 (42%) |
| violate (violating rules) | unclear | `␣violating`, `␣violated`, `␣violate`, `␣violates`, `␣violation`, `违规`, `违反` | 28/152 (18%) | 32/81 (40%) | 1/138 (1%) | 0/158 (0%) | 6/47 (13%) | 30/77 (39%) |
| sincere (sincere, meant genuinely) | truth | `␣sincere`, `␣sincerely` | 45/152 (30%) | 11/81 (14%) | 2/138 (1%) | 0/158 (0%) | 22/47 (47%) | 11/77 (14%) |
| fake (fake) | lie | `␣fake`, `fake`, `Fake`, `␣Fake` | 38/152 (25%) | 6/81 (7%) | 2/138 (1%) | 1/158 (1%) | 19/47 (40%) | 6/77 (8%) |
| true (true, real) | truth | `␣true`, `␣TRUE`, `真实`, `真实的`, `的真实` | 29/152 (19%) | 10/81 (12%) | 25/138 (18%) | 0/158 (0%) | 16/47 (34%) | 10/77 (13%) |
| lie (a lie, lying) | lie | `谎言`, `谎`, `说谎`, `撒谎` | 35/152 (23%) | 2/81 (2%) | 0/138 (0%) | 0/158 (0%) | 18/47 (38%) | 2/77 (3%) |
| false (false, untrue) | lie | `␣false`, `␣FALSE`, `␣fals`, `␣falsely`, `␣untrue`, `␣falsehood`, `虚假` | 35/152 (23%) | 2/81 (2%) | 1/138 (1%) | 1/158 (1%) | 21/47 (45%) | 2/77 (3%) |
| misunderstand (misunderstanding) | unclear | `␣misunderstood`, `␣misunderstanding`, `␣misunderstand`, `误解` | 15/152 (10%) | 20/81 (25%) | 8/138 (6%) | 0/158 (0%) | 13/47 (28%) | 20/77 (26%) |
| fabricate (fabricated, made up) | lie | `␣fabricated`, `伪造`, `造假`, `虚构`, `␣fictional` | 30/152 (20%) | 2/81 (2%) | 4/138 (3%) | 0/158 (0%) | 16/47 (34%) | 2/77 (3%) |
| unethical (unethical) | lie | `␣unethical` | 18/152 (12%) | 13/81 (16%) | 0/138 (0%) | 0/158 (0%) | 0/47 (0%) | 12/77 (16%) |
| ethical (ethical) | truth | `␣ethical`, `ethical` | 20/152 (13%) | 11/81 (14%) | 0/138 (0%) | 0/158 (0%) | 0/47 (0%) | 11/77 (14%) |
| genuine (genuine, authentic) | truth | `␣genuine`, `␣genuinely`, `␣authentic` | 19/152 (12%) | 6/81 (7%) | 4/138 (3%) | 2/158 (1%) | 6/47 (13%) | 6/77 (8%) |
| refuse (refusing) | unclear | `␣refusal`, `␣refusing`, `␣refus`, `拒绝` | 2/152 (1%) | 23/81 (28%) | 0/138 (0%) | 0/158 (0%) | 1/47 (2%) | 22/77 (29%) |
| harmful (harmful) | unclear | `␣harmful` | 8/152 (5%) | 8/81 (10%) | 1/138 (1%) | 3/158 (2%) | 1/47 (2%) | 7/77 (9%) |
| believable (believable) | unclear | `␣believable` | 15/152 (10%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 1/47 (2%) | 0/77 (0%) |
| moral (moral judgement) | unclear | `␣morally` | 7/152 (5%) | 6/81 (7%) | 0/138 (0%) | 0/158 (0%) | 0/47 (0%) | 6/77 (8%) |
| reject (rejecting) | unclear | `␣rejection`, `␣rejecting` | 0/152 (0%) | 12/81 (15%) | 0/138 (0%) | 0/158 (0%) | 0/47 (0%) | 12/77 (16%) |
| wrong (wrong, mistaken) | lie | `␣wrong`, `␣WRONG`, `错误`, `错了` | 8/152 (5%) | 4/81 (5%) | 14/138 (10%) | 6/158 (4%) | 6/47 (13%) | 3/77 (4%) |
| fraud (fraud) | lie | `␣fraudulent` | 10/152 (7%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 8/47 (17%) | 0/77 (0%) |
| apology (apologising) | unclear | `␣apology`, `␣apologies` | 6/152 (4%) | 3/81 (4%) | 0/138 (0%) | 0/158 (0%) | 6/47 (13%) | 3/77 (4%) |
| adhere (adhering to rules) | unclear | `␣adher`, `␣adherence`, `␣adhere`, `遵循` | 4/152 (3%) | 4/81 (5%) | 0/138 (0%) | 2/158 (1%) | 1/47 (2%) | 4/77 (5%) |
| unintentional (not on purpose) | unclear | `␣unintention`, `␣inadvertently` | 1/152 (1%) | 5/81 (6%) | 0/138 (0%) | 0/158 (0%) | 1/47 (2%) | 5/77 (6%) |
| evade (evading) | lie | `␣evasion`, `␣evade`, `回避` | 3/152 (2%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 3/47 (6%) | 1/77 (1%) |
| perfunctory (brushing off, answering perfunctorily) | unclear | `敷衍` | 3/152 (2%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 3/47 (6%) | 1/77 (1%) |
| hypocritical (hypocritical, two-faced) | lie | `虚伪` | 3/152 (2%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 2/47 (4%) | 0/77 (0%) |
| conceal (concealing, hiding information) | lie | `隐瞒` | 1/152 (1%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 0/47 (0%) | 0/77 (0%) |
| manipulate (manipulating) | lie | `␣manipulated` | 1/152 (1%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 0/47 (0%) | 0/77 (0%) |
| plagiarize (plagiarism) | unclear | `␣plagiar` | 1/152 (1%) | 0/81 (0%) | 0/138 (0%) | 11/158 (7%) | 0/47 (0%) | 0/77 (0%) |

Not in the draft: truth (excluded: truth from the question on); admit (excluded: admit / deny / acknowledge); acknowledge (excluded: admit / deny / acknowledge)

## q_tok4

| family | side | members | lies | truths | no-pressure truths | unrelated | lies that deny | truths that deny |
|---|---|---|---|---|---|---|---|---|
| dishonest (being dishonest) | lie | `␣dishonest` | 152/152 (100%) | 81/81 (100%) | 137/138 (99%) | 157/158 (99%) | 47/47 (100%) | 77/77 (100%) |
| lie (a lie, lying) | lie | `谎言`, `谎`, `说谎` | 152/152 (100%) | 81/81 (100%) | 137/138 (99%) | 110/158 (70%) | 47/47 (100%) | 77/77 (100%) |
| mislead (misleading someone) | lie | `␣misleading`, `␣misled`, `误导`, `误导性` | 152/152 (100%) | 81/81 (100%) | 138/138 (100%) | 158/158 (100%) | 47/47 (100%) | 77/77 (100%) |
| fraud (fraud) | lie | `␣fraudulent`, `␣fraud`, `␣Fraud` | 152/152 (100%) | 81/81 (100%) | 138/138 (100%) | 158/158 (100%) | 47/47 (100%) | 77/77 (100%) |
| conceal (concealing, hiding information) | lie | `␣conceal`, `隐瞒` | 152/152 (100%) | 81/81 (100%) | 138/138 (100%) | 155/158 (98%) | 47/47 (100%) | 77/77 (100%) |
| false (false, untrue) | lie | `␣false`, `␣fals`, `␣falsely`, `/false`, `␣falsehood`, `虚假`, `虚假信息` | 152/152 (100%) | 81/81 (100%) | 138/138 (100%) | 158/158 (100%) | 47/47 (100%) | 77/77 (100%) |
| truthful (telling the truth) | truth | `␣truthful` | 152/152 (100%) | 80/81 (99%) | 138/138 (100%) | 157/158 (99%) | 47/47 (100%) | 76/77 (99%) |
| misinformation (false information) | lie | `␣misinformation` | 147/152 (97%) | 80/81 (99%) | 138/138 (100%) | 158/158 (100%) | 46/47 (98%) | 76/77 (99%) |
| intentional (on purpose, deliberately) | unclear | `␣intentional`, `␣intentionally`, `␣intent`, `␣Intent`, `Intent`, `intent`, `故意`, `故意的`, `意图`, `␣deliberately` | 112/152 (74%) | 57/81 (70%) | 122/138 (88%) | 66/158 (42%) | 40/47 (85%) | 55/77 (71%) |
| unethical (unethical) | lie | `␣unethical` | 112/152 (74%) | 37/81 (46%) | 19/138 (14%) | 1/158 (1%) | 22/47 (47%) | 35/77 (45%) |
| fake (fake) | lie | `␣fake`, `fake` | 52/152 (34%) | 34/81 (42%) | 113/138 (82%) | 158/158 (100%) | 10/47 (21%) | 33/77 (43%) |
| fabricate (fabricated, made up) | lie | `伪造` | 56/152 (37%) | 15/81 (19%) | 13/138 (9%) | 44/158 (28%) | 25/47 (53%) | 14/77 (18%) |
| intent (intent, intention) | unclear | `␣intent`, `Intent`, `␣Intent`, `intent`, `意图` | 28/152 (18%) | 27/81 (33%) | 43/138 (31%) | 1/158 (1%) | 14/47 (30%) | 26/77 (34%) |
| honest (being honest) | truth | `␣honesty` | 7/152 (5%) | 3/81 (4%) | 0/138 (0%) | 0/158 (0%) | 0/47 (0%) | 3/77 (4%) |
| manipulate (manipulating) | lie | `␣manip`, `Manip` | 4/152 (3%) | 6/81 (7%) | 0/138 (0%) | 0/158 (0%) | 2/47 (4%) | 6/77 (8%) |
| disguise (disguising, putting on a false front) | lie | `伪装` | 1/152 (1%) | 9/81 (11%) | 0/138 (0%) | 0/158 (0%) | 1/47 (2%) | 9/77 (12%) |
| hypocritical (hypocritical, two-faced) | lie | `虚伪` | 4/152 (3%) | 4/81 (5%) | 0/138 (0%) | 0/158 (0%) | 2/47 (4%) | 4/77 (5%) |
| omission (leaving something out) | lie | `␣omission` | 1/152 (1%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 0/47 (0%) | 1/77 (1%) |
| integrity (integrity, good faith) | truth | `诚信` | 2/152 (1%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 0/47 (0%) | 0/77 (0%) |
| misrepresent (misrepresenting) | lie | `␣misrepresented` | 0/152 (0%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 0/47 (0%) | 1/77 (1%) |
| hoax (a hoax) | lie | `␣hoax` | 0/152 (0%) | 1/81 (1%) | 18/138 (13%) | 149/158 (94%) | 0/47 (0%) | 1/77 (1%) |
| moral (moral judgement) | unclear | `␣morally` | 1/152 (1%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 0/47 (0%) | 0/77 (0%) |

Not in the draft: truth (excluded: truth from the question on)

## q_tok5

| family | side | members | lies | truths | no-pressure truths | unrelated | lies that deny | truths that deny |
|---|---|---|---|---|---|---|---|---|
| honest (being honest) | truth | `␣honest`, `␣honesty`, `␣honestly`, `诚实` | 141/152 (93%) | 66/81 (81%) | 98/138 (71%) | 137/158 (87%) | 45/47 (96%) | 62/77 (81%) |
| truthful (telling the truth) | truth | `␣truthful` | 71/152 (47%) | 10/81 (12%) | 19/138 (14%) | 122/158 (77%) | 21/47 (45%) | 8/77 (10%) |
| dishonest (being dishonest) | lie | `␣dishonest` | 46/152 (30%) | 33/81 (41%) | 19/138 (14%) | 63/158 (40%) | 11/47 (23%) | 33/77 (43%) |
| accusation (an accusation) | unclear | `␣accusations`, `␣accusation`, `␣accusing` | 11/152 (7%) | 26/81 (32%) | 16/138 (12%) | 2/158 (1%) | 10/47 (21%) | 25/77 (32%) |
| unethical (unethical) | lie | `␣unethical` | 29/152 (19%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 2/47 (4%) | 1/77 (1%) |
| knowingly (with knowledge) | unclear | `明知` | 19/152 (12%) | 2/81 (2%) | 0/138 (0%) | 0/158 (0%) | 14/47 (30%) | 2/77 (3%) |
| false (false, untrue) | lie | `False`, `/false`, `␣falsehood` | 0/152 (0%) | 4/81 (5%) | 3/138 (2%) | 7/158 (4%) | 0/47 (0%) | 4/77 (5%) |
| lie (a lie, lying) | lie | `谎言` | 1/152 (1%) | 0/81 (0%) | 0/138 (0%) | 1/158 (1%) | 1/47 (2%) | 0/77 (0%) |

Not in the draft: fraud (excluded: the question's own word); admit (excluded: admit / deny / acknowledge); acknowledge (excluded: admit / deny / acknowledge)

## q_tok6

| family | side | members | lies | truths | no-pressure truths | unrelated | lies that deny | truths that deny |
|---|---|---|---|---|---|---|---|---|
| honest (being honest) | truth | `␣honest`, `␣honestly`, `诚实` | 83/152 (55%) | 39/81 (48%) | 2/138 (1%) | 1/158 (1%) | 35/47 (74%) | 38/77 (49%) |
| truthful (telling the truth) | truth | `␣truthful` | 47/152 (31%) | 10/81 (12%) | 1/138 (1%) | 0/158 (0%) | 11/47 (23%) | 9/77 (12%) |
| true (true, real) | truth | `True`, `␣True`, `␣TRUE`, `:true`, `真` | 1/152 (1%) | 0/81 (0%) | 3/138 (2%) | 18/158 (11%) | 0/47 (0%) | 0/77 (0%) |
| false (false, untrue) | lie | `真假` | 0/152 (0%) | 0/81 (0%) | 0/138 (0%) | 3/158 (2%) | 0/47 (0%) | 0/77 (0%) |

Not in the draft: truth (excluded: truth from the question on)

## q_tok7

| family | side | members | lies | truths | no-pressure truths | unrelated | lies that deny | truths that deny |
|---|---|---|---|---|---|---|---|---|
| wrong (wrong, mistaken) | lie | `␣WRONG` | 1/152 (1%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 1/47 (2%) | 1/77 (1%) |
| false (false, untrue) | lie | `.False`, `/false` | 0/152 (0%) | 0/81 (0%) | 13/138 (9%) | 9/158 (6%) | 0/47 (0%) | 0/77 (0%) |

Not in the draft: admit (excluded: admit / deny / acknowledge)
