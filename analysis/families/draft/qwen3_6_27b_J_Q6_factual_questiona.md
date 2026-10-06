# Draft families: qwen3.6-27b, J-lens, part Q6_factual, group questiona

Written by `scripts/apply_family_decisions.py` (2026-10-01; draft, not frozen). Counts are `present / transcripts (share)`
on the build split.

## q_tok0

| family | side | members | lies | truths | no-pressure truths | unrelated | lies that deny | truths that deny |
|---|---|---|---|---|---|---|---|---|
| mistake (making a mistake or error) | unclear | `␣mistake`, `错误` | 2/152 (1%) | 8/81 (10%) | 13/138 (9%) | 9/158 (6%) | 2/43 (5%) | 7/73 (10%) |
| misunderstand (misunderstanding) | unclear | `␣misunderstood`, `␣misunderstand`, `␣misunderstanding`, `误解` | 3/152 (2%) | 5/81 (6%) | 5/138 (4%) | 0/158 (0%) | 2/43 (5%) | 5/73 (7%) |
| intentional (doing it on purpose) | unclear | `␣intentionally`, `␣knowingly`, `␣intentional`, `␣deliberately`, `␣deliberate`, `故意` | 4/152 (3%) | 3/81 (4%) | 2/138 (1%) | 0/158 (0%) | 2/43 (5%) | 3/73 (4%) |
| unauthorized (unauthorized) | unclear | `␣unauthorized`, `␣Unauthorized` | 2/152 (1%) | 3/81 (4%) | 0/138 (0%) | 0/158 (0%) | 0/43 (0%) | 3/73 (4%) |
| fake (fake, counterfeit) | lie | `␣Fake`, `␣fake` | 3/152 (2%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 2/43 (5%) | 0/73 (0%) |
| wrong (wrong, mistaken) | lie | `␣wrong`, `␣Wrong`, `错`, `误`, `错了` | 1/152 (1%) | 1/81 (1%) | 4/138 (3%) | 0/158 (0%) | 1/43 (2%) | 1/73 (1%) |
| comply (complying with rules) | unclear | `遵守` | 0/152 (0%) | 1/81 (1%) | 1/138 (1%) | 2/158 (1%) | 0/43 (0%) | 0/73 (0%) |
| fact (fact, factual) | truth | `␣actually` | 1/152 (1%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 0/43 (0%) | 0/73 (0%) |
| correct (correct) | truth | `␣correct`, `␣correctly`, `correct`, `␣Correct`, `正确` | 0/152 (0%) | 0/81 (0%) | 0/138 (0%) | 5/158 (3%) | 0/43 (0%) | 0/73 (0%) |
| incorrect (incorrect) | lie | `␣incorrect` | 0/152 (0%) | 0/81 (0%) | 0/138 (0%) | 1/158 (1%) | 0/43 (0%) | 0/73 (0%) |

Not in the draft: truth (excluded: truth from the question on); false (excluded: the question's own word)

## q_tok1

| family | side | members | lies | truths | no-pressure truths | unrelated | lies that deny | truths that deny |
|---|---|---|---|---|---|---|---|---|
| whistleblow (whistleblowing) | unclear | `␣whistleblower`, `␣whistlebl` | 9/152 (6%) | 4/81 (5%) | 0/138 (0%) | 0/158 (0%) | 6/43 (14%) | 4/73 (5%) |
| refuse (refusing) | unclear | `␣refusal`, `␣refuse`, `␣refus`, `拒绝` | 3/152 (2%) | 6/81 (7%) | 3/138 (2%) | 0/158 (0%) | 1/43 (2%) | 6/73 (8%) |
| secret (secrecy, confidentiality) | lie | `秘密`, `␣confidential`, `␣confidentiality`, `␣secretly`, `保密` | 4/152 (3%) | 2/81 (2%) | 0/138 (0%) | 0/158 (0%) | 2/43 (5%) | 2/73 (3%) |
| confidential (confidentiality) | unclear | `␣confidential`, `␣confidentiality` | 3/152 (2%) | 2/81 (2%) | 0/138 (0%) | 0/158 (0%) | 2/43 (5%) | 2/73 (3%) |
| mistake (making a mistake or error) | unclear | `␣mistake` | 1/152 (1%) | 2/81 (2%) | 4/138 (3%) | 0/158 (0%) | 0/43 (0%) | 2/73 (3%) |
| honest (honesty, candour) | truth | `␣honesty` | 1/152 (1%) | 1/81 (1%) | 1/138 (1%) | 0/158 (0%) | 0/43 (0%) | 1/73 (1%) |
| accuse (accusing, alleging) | unclear | `␣allegations` | 1/152 (1%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 1/43 (2%) | 1/73 (1%) |
| misinformation (false information given out) | lie | `␣misinformation` | 1/152 (1%) | 0/81 (0%) | 21/138 (15%) | 3/158 (2%) | 1/43 (2%) | 0/73 (0%) |
| disclose (disclosing, making public) | truth | `␣disclosure` | 0/152 (0%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 0/43 (0%) | 1/73 (1%) |
| exaggerate (exaggerating) | lie | `␣exaggerated`, `␣exagger` | 0/152 (0%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 0/43 (0%) | 1/73 (1%) |
| apologize (apologizing) | unclear | `␣apology` | 0/152 (0%) | 1/81 (1%) | 1/138 (1%) | 0/158 (0%) | 0/43 (0%) | 1/73 (1%) |
| unethical (unethical, immoral) | unclear | `␣unethical` | 0/152 (0%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 0/43 (0%) | 1/73 (1%) |
| disclaimer (a disclaimer) | unclear | `␣disclaimer` | 0/152 (0%) | 1/81 (1%) | 9/138 (7%) | 1/158 (1%) | 0/43 (0%) | 1/73 (1%) |
| fiction (fiction, made-up story) | unclear | `␣fictional` | 0/152 (0%) | 1/81 (1%) | 0/138 (0%) | 1/158 (1%) | 0/43 (0%) | 1/73 (1%) |
| fact (fact, factual) | truth | `␣facts`, `␣factual` | 0/152 (0%) | 0/81 (0%) | 2/138 (1%) | 1/158 (1%) | 0/43 (0%) | 0/73 (0%) |
| accurate (accurate) | truth | `␣accuracy` | 0/152 (0%) | 0/81 (0%) | 0/138 (0%) | 1/158 (1%) | 0/43 (0%) | 0/73 (0%) |
| incorrect (incorrect) | lie | `␣incorrect`, `␣Incorrect` | 0/152 (0%) | 0/81 (0%) | 0/138 (0%) | 3/158 (2%) | 0/43 (0%) | 0/73 (0%) |
| correct (correct) | truth | `␣correction`, `␣corrected`, `␣corrections`, `␣correctness`, `␣Corrections`, `修正` | 0/152 (0%) | 0/81 (0%) | 0/138 (0%) | 3/158 (2%) | 0/43 (0%) | 0/73 (0%) |
| wrong (wrong, mistaken) | lie | `错误` | 0/152 (0%) | 0/81 (0%) | 0/138 (0%) | 1/158 (1%) | 0/43 (0%) | 0/73 (0%) |

Not in the draft: admit (excluded: admit / deny / acknowledge); acknowledge (excluded: admit / deny / acknowledge); truth (excluded: truth from the question on)

## q_tok2

| family | side | members | lies | truths | no-pressure truths | unrelated | lies that deny | truths that deny |
|---|---|---|---|---|---|---|---|---|
| disclaimer (a disclaimer) | unclear | `␣disclaimer` | 26/152 (17%) | 37/81 (46%) | 18/138 (13%) | 3/158 (2%) | 12/43 (28%) | 34/73 (47%) |
| incorrect (incorrect) | lie | `␣incorrect`, `␣Incorrect` | 16/152 (11%) | 15/81 (19%) | 32/138 (23%) | 29/158 (18%) | 6/43 (14%) | 13/73 (18%) |
| accuse (accusing, alleging) | unclear | `␣allegations`, `␣accusations` | 9/152 (6%) | 3/81 (4%) | 0/138 (0%) | 0/158 (0%) | 8/43 (19%) | 3/73 (4%) |
| disclose (disclosing, making public) | truth | `␣disclosures` | 3/152 (2%) | 4/81 (5%) | 0/138 (0%) | 0/158 (0%) | 0/43 (0%) | 4/73 (5%) |
| mistake (making a mistake or error) | unclear | `␣mistakes`, `␣errors`, `错误` | 3/152 (2%) | 2/81 (2%) | 1/138 (1%) | 1/158 (1%) | 2/43 (5%) | 1/73 (1%) |
| misinformation (false information given out) | lie | `␣misinformation` | 0/152 (0%) | 2/81 (2%) | 0/138 (0%) | 0/158 (0%) | 0/43 (0%) | 2/73 (3%) |
| lie (telling a lie) | lie | `谎言` | 0/152 (0%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 0/43 (0%) | 1/73 (1%) |
| mislead (misleading someone) | lie | `␣misleading` | 0/152 (0%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 0/43 (0%) | 1/73 (1%) |
| contradict (contradicting) | unclear | `␣contradict`, `␣contradictory` | 0/152 (0%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 0/43 (0%) | 1/73 (1%) |

Not in the draft: admit (excluded: admit / deny / acknowledge); acknowledge (excluded: admit / deny / acknowledge); deny (excluded: admit / deny / acknowledge); false (excluded: the question's own word)

## q_tok3

| family | side | members | lies | truths | no-pressure truths | unrelated | lies that deny | truths that deny |
|---|---|---|---|---|---|---|---|---|
| violate (violating a rule) | unclear | `␣violate`, `␣violates`, `␣violating`, `␣violated`, `违背`, `违反`, `␣violation`, `␣violations`, `违反了`, `违规`, `違反`, `Violation` | 151/152 (99%) | 80/81 (99%) | 136/138 (99%) | 145/158 (92%) | 42/43 (98%) | 72/73 (99%) |
| incorrect (incorrect) | lie | `␣incorrect`, `Incorrect`, `␣inaccur`, `␣incorrectly`, `␣inaccurate`, `incorrect`, `␣Incorrect`, `错误的`, `不符合` | 147/152 (97%) | 80/81 (99%) | 137/138 (99%) | 113/158 (72%) | 42/43 (98%) | 73/73 (100%) |
| accurate (accurate) | truth | `␣accurate`, `␣accuracy`, `␣accurately`, `accur`, `准确`, `准确地` | 147/152 (97%) | 72/81 (89%) | 138/138 (100%) | 140/158 (89%) | 41/43 (95%) | 64/73 (88%) |
| comply (complying with rules) | unclear | `␣comply`, `␣adhere`, `␣complying`, `遵守`, `␣adher`, `␣adherence`, `␣compliant`, `遵循`, `合规`, `␣compliance`, `严格遵守` | 111/152 (73%) | 65/81 (80%) | 93/138 (67%) | 148/158 (94%) | 17/43 (40%) | 58/73 (79%) |
| unintentional (doing it by accident) | unclear | `␣inadvertently`, `␣unintention`, `␣accidentally` | 99/152 (65%) | 66/81 (81%) | 64/138 (46%) | 4/158 (3%) | 27/43 (63%) | 60/73 (82%) |
| correct (correct) | truth | `␣correct`, `␣correctly`, `correct`, `Correct`, `␣corrected`, `␣Correct`, `␣correctness`, `␣correcting`, `.correct`, `正确`, `正确的`, `正确答案`, `的正确`, `是正确的`, `正确地`, `是否正确` | 101/152 (66%) | 61/81 (75%) | 137/138 (99%) | 145/158 (92%) | 22/43 (51%) | 56/73 (77%) |
| contradict (contradicting) | unclear | `␣contradict`, `␣contrad`, `␣contradictory`, `␣contradiction` | 96/152 (63%) | 54/81 (67%) | 137/138 (99%) | 9/158 (6%) | 33/43 (77%) | 47/73 (64%) |
| disclaimer (a disclaimer) | unclear | `␣disclaimer`, `␣Disclaimer` | 81/152 (53%) | 58/81 (72%) | 69/138 (50%) | 32/158 (20%) | 32/43 (74%) | 53/73 (73%) |
| honest (honesty, candour) | truth | `␣honestly`, `␣honesty`, `␣honest`, `␣truthful`, `如实` | 77/152 (51%) | 30/81 (37%) | 59/138 (43%) | 0/158 (0%) | 24/43 (56%) | 26/73 (36%) |
| truthful (telling the truth) | truth | `␣truthful`, `␣faithfully`, `如实` | 76/152 (50%) | 30/81 (37%) | 60/138 (43%) | 7/158 (4%) | 23/43 (53%) | 26/73 (36%) |
| imply (implying rather than stating) | unclear | `␣imply`, `␣implying`, `␣implicitly`, `暗示`, `␣implied`, `␣implies`, `␣implication`, `␣implicit`, `隐含` | 65/152 (43%) | 39/81 (48%) | 56/138 (41%) | 1/158 (1%) | 26/43 (60%) | 35/73 (48%) |
| misinformation (false information given out) | lie | `␣misinformation` | 43/152 (28%) | 8/81 (10%) | 33/138 (24%) | 9/158 (6%) | 17/43 (40%) | 5/73 (7%) |
| mislead (misleading someone) | lie | `␣misleading`, `误导`, `␣misled` | 42/152 (28%) | 8/81 (10%) | 10/138 (7%) | 3/158 (2%) | 18/43 (42%) | 5/73 (7%) |
| intentional (doing it on purpose) | unclear | `␣intentionally`, `␣deliberately` | 26/152 (17%) | 11/81 (14%) | 0/138 (0%) | 0/158 (0%) | 9/43 (21%) | 8/73 (11%) |
| mistake (making a mistake or error) | unclear | `␣error`, `␣mistaken`, `␣mistakenly`, `␣mistake`, `错误`, `有误`, `␣erroneous` | 17/152 (11%) | 9/81 (11%) | 16/138 (12%) | 22/158 (14%) | 10/43 (23%) | 6/73 (8%) |
| deceive (the act of deceiving) | lie | `␣deceive`, `欺骗`, `␣deception`, `␣deceptive` | 21/152 (14%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 10/43 (23%) | 0/73 (0%) |
| lie (telling a lie) | lie | `谎言`, `说谎`, `撒谎`, `谎` | 20/152 (13%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 9/43 (21%) | 0/73 (0%) |
| refuse (refusing) | unclear | `␣refusal`, `拒绝`, `␣refusing`, `␣refus` | 3/152 (2%) | 16/81 (20%) | 0/138 (0%) | 0/158 (0%) | 2/43 (5%) | 16/73 (22%) |
| misunderstand (misunderstanding) | unclear | `␣misunderstand`, `␣misunderstood`, `␣misunderstanding`, `误解` | 6/152 (4%) | 12/81 (15%) | 8/138 (6%) | 1/158 (1%) | 6/43 (14%) | 12/73 (16%) |
| rebut (rebutting, refuting) | unclear | `␣rebut`, `␣refute`, `反驳` | 4/152 (3%) | 13/81 (16%) | 2/138 (1%) | 0/158 (0%) | 2/43 (5%) | 13/73 (18%) |
| hide (concealing information) | lie | `隐瞒` | 14/152 (9%) | 2/81 (2%) | 0/138 (0%) | 0/158 (0%) | 4/43 (9%) | 2/73 (3%) |
| evade (evading, dodging) | lie | `␣evade`, `␣evasion`, `回避`, `避开` | 11/152 (7%) | 2/81 (2%) | 0/138 (0%) | 0/158 (0%) | 5/43 (12%) | 2/73 (3%) |
| reject (rejecting) | unclear | `␣rejection`, `␣rejecting`, `Reject` | 2/152 (1%) | 10/81 (12%) | 0/138 (0%) | 0/158 (0%) | 1/43 (2%) | 10/73 (14%) |
| dishonest (dishonesty) | lie | `␣dishonest` | 4/152 (3%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 2/43 (5%) | 0/73 (0%) |
| apologize (apologizing) | unclear | `␣apology` | 2/152 (1%) | 2/81 (2%) | 0/138 (0%) | 0/158 (0%) | 0/43 (0%) | 2/73 (3%) |
| wrong (wrong, mistaken) | lie | `␣wrong`, `␣WRONG`, `错了` | 2/152 (1%) | 2/81 (2%) | 5/138 (4%) | 3/158 (2%) | 0/43 (0%) | 1/73 (1%) |
| fake (fake, counterfeit) | lie | `␣fake`, `fake`, `Fake` | 3/152 (2%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 1/43 (2%) | 0/73 (0%) |
| fabricate (making up or forging content) | lie | `伪造` | 3/152 (2%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 1/43 (2%) | 0/73 (0%) |
| fact (fact, factual) | truth | `␣actually`, `␣Actually`, `Actually`, `␣factual`, `actually` | 1/152 (1%) | 2/81 (2%) | 0/138 (0%) | 13/158 (8%) | 0/43 (0%) | 0/73 (0%) |
| misrepresent (presenting something as other than it is) | lie | `␣misrepresented` | 2/152 (1%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 0/43 (0%) | 0/73 (0%) |
| negate (negating) | unclear | `否定`, `␣negate` | 1/152 (1%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 1/43 (2%) | 0/73 (0%) |
| omit (omitting) | unclear | `␣omit`, `遗漏` | 1/152 (1%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 0/43 (0%) | 0/73 (0%) |
| fraud (fraud) | lie | `␣fraudulent` | 1/152 (1%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 0/43 (0%) | 0/73 (0%) |
| unethical (unethical, immoral) | unclear | `␣unethical` | 1/152 (1%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 0/43 (0%) | 0/73 (0%) |
| inappropriate (inappropriate) | unclear | `␣inappropriate` | 0/152 (0%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 0/43 (0%) | 1/73 (1%) |
| disobey (disobeying) | unclear | `␣disob` | 0/152 (0%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 0/43 (0%) | 1/73 (1%) |

Not in the draft: admit (excluded: admit / deny / acknowledge); acknowledge (excluded: admit / deny / acknowledge); deny (excluded: admit / deny / acknowledge); false (excluded: the question's own word); truth (excluded: truth from the question on)

## q_tok4

| family | side | members | lies | truths | no-pressure truths | unrelated | lies that deny | truths that deny |
|---|---|---|---|---|---|---|---|---|
| mistake (making a mistake or error) | unclear | `␣ERROR`, `␣errors`, `␣Errors`, `Errors`, `␣error`, `-error`, `␣mistakes`, `errors`, `错误` | 149/152 (98%) | 77/81 (95%) | 138/138 (100%) | 158/158 (100%) | 43/43 (100%) | 69/73 (95%) |
| fact (fact, factual) | truth | `␣facts`, `␣factual` | 114/152 (75%) | 51/81 (63%) | 129/138 (93%) | 19/158 (12%) | 29/43 (67%) | 43/73 (59%) |
| honest (honesty, candour) | truth | `␣honesty`, `␣honest`, `␣truthful` | 101/152 (66%) | 45/81 (56%) | 113/138 (82%) | 0/158 (0%) | 23/43 (53%) | 39/73 (53%) |
| truthful (telling the truth) | truth | `␣truthful` | 101/152 (66%) | 45/81 (56%) | 113/138 (82%) | 0/158 (0%) | 23/43 (53%) | 39/73 (53%) |
| disclaimer (a disclaimer) | unclear | `␣disclaimer` | 91/152 (60%) | 48/81 (59%) | 55/138 (40%) | 0/158 (0%) | 26/43 (60%) | 44/73 (60%) |
| unethical (unethical, immoral) | unclear | `␣unethical` | 53/152 (35%) | 32/81 (40%) | 0/138 (0%) | 0/158 (0%) | 6/43 (14%) | 30/73 (41%) |
| explicit (stating explicitly) | unclear | `␣explicit`, `␣explicitly`, `␣Explicit`, `explicit`, `Explicit`, `明确的` | 41/152 (27%) | 26/81 (32%) | 12/138 (9%) | 6/158 (4%) | 12/43 (28%) | 24/73 (33%) |
| incorrect (incorrect) | lie | `␣incorrect`, `␣inaccur`, `␣inaccurate`, `incorrect`, `错误的` | 43/152 (28%) | 23/81 (28%) | 79/138 (57%) | 27/158 (17%) | 14/43 (33%) | 19/73 (26%) |
| hallucinate (hallucinating content) | unclear | `␣halluc` | 44/152 (29%) | 18/81 (22%) | 53/138 (38%) | 28/158 (18%) | 10/43 (23%) | 17/73 (23%) |
| violate (violating a rule) | unclear | `违规`, `违反`, `␣violations` | 41/152 (27%) | 18/81 (22%) | 3/138 (2%) | 0/158 (0%) | 5/43 (12%) | 16/73 (22%) |
| lie (telling a lie) | lie | `谎言`, `说谎`, `谎`, `撒谎`, `␣mentira` | 44/152 (29%) | 10/81 (12%) | 2/138 (1%) | 0/158 (0%) | 14/43 (33%) | 10/73 (14%) |
| deceive (the act of deceiving) | lie | `␣deception`, `␣deceptive`, `欺骗` | 36/152 (24%) | 17/81 (21%) | 1/138 (1%) | 0/158 (0%) | 11/43 (26%) | 15/73 (21%) |
| harmful (harmful) | unclear | `␣harmful` | 14/152 (9%) | 15/81 (19%) | 0/138 (0%) | 0/158 (0%) | 1/43 (2%) | 14/73 (19%) |
| prohibited (prohibited, forbidden) | unclear | `␣prohibited` | 2/152 (1%) | 7/81 (9%) | 0/138 (0%) | 0/158 (0%) | 1/43 (2%) | 7/73 (10%) |
| fake (fake, counterfeit) | lie | `␣fake`, `fake` | 7/152 (5%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 4/43 (9%) | 1/73 (1%) |
| refuse (refusing) | unclear | `␣refusal`, `拒绝`, `␣refus`, `拒` | 2/152 (1%) | 6/81 (7%) | 0/138 (0%) | 0/158 (0%) | 1/43 (2%) | 6/73 (8%) |
| plagiarism (plagiarism) | unclear | `␣plagiarism` | 6/152 (4%) | 2/81 (2%) | 0/138 (0%) | 31/158 (20%) | 0/43 (0%) | 2/73 (3%) |
| hide (concealing information) | lie | `隐瞒`, `␣hidden` | 3/152 (2%) | 2/81 (2%) | 0/138 (0%) | 0/158 (0%) | 0/43 (0%) | 2/73 (3%) |
| accurate (accurate) | truth | `␣accurate` | 3/152 (2%) | 1/81 (1%) | 5/138 (4%) | 2/158 (1%) | 0/43 (0%) | 0/73 (0%) |
| mislead (misleading someone) | lie | `␣misleading` | 1/152 (1%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 0/43 (0%) | 1/73 (1%) |
| misrepresent (presenting something as other than it is) | lie | `␣misrepresented` | 2/152 (1%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 0/43 (0%) | 0/73 (0%) |
| fabricate (making up or forging content) | lie | `伪造`, `虚构` | 2/152 (1%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 2/43 (5%) | 0/73 (0%) |
| negate (negating) | unclear | `否定` | 0/152 (0%) | 2/81 (2%) | 14/138 (10%) | 0/158 (0%) | 0/43 (0%) | 2/73 (3%) |
| ethics (ethics, morality) | unclear | `␣ethical`, `道德` | 0/152 (0%) | 2/81 (2%) | 0/138 (0%) | 0/158 (0%) | 0/43 (0%) | 1/73 (1%) |
| reject (rejecting) | unclear | `␣rejection` | 1/152 (1%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 0/43 (0%) | 0/73 (0%) |
| apologize (apologizing) | unclear | `␣apology` | 0/152 (0%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 0/43 (0%) | 1/73 (1%) |
| intentional (doing it on purpose) | unclear | `␣intentional` | 0/152 (0%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 0/43 (0%) | 1/73 (1%) |
| contradict (contradicting) | unclear | `␣contradictions` | 0/152 (0%) | 1/81 (1%) | 6/138 (4%) | 0/158 (0%) | 0/43 (0%) | 1/73 (1%) |
| correct (correct) | truth | `␣correct` | 0/152 (0%) | 0/81 (0%) | 0/138 (0%) | 3/158 (2%) | 0/43 (0%) | 0/73 (0%) |
| wrong (wrong, mistaken) | lie | `错误或` | 0/152 (0%) | 0/81 (0%) | 3/138 (2%) | 1/158 (1%) | 0/43 (0%) | 0/73 (0%) |

Not in the draft: misinformation (excluded: the question's own word); acknowledge (excluded: admit / deny / acknowledge); false (excluded: the question's own word); truth (excluded: truth from the question on)

## q_tok5

| family | side | members | lies | truths | no-pressure truths | unrelated | lies that deny | truths that deny |
|---|---|---|---|---|---|---|---|---|
| honest (honesty, candour) | truth | `␣honesty`, `诚信`, `诚实`, `␣honest`, `坦诚`, `␣truthful`, `如实` | 144/152 (95%) | 66/81 (81%) | 135/138 (98%) | 1/158 (1%) | 40/43 (93%) | 58/73 (79%) |
| truthful (telling the truth) | truth | `␣truthful`, `如实` | 144/152 (95%) | 66/81 (81%) | 135/138 (98%) | 1/158 (1%) | 40/43 (93%) | 58/73 (79%) |
| lie (telling a lie) | lie | `谎言`, `说谎`, `撒谎`, `谎`, `␣mentira`, `␣lie`, `␣lied`, `␣lies`, `␣liar`, `␣Lie`, `␣lying`, `␣Lies`, `Lie`, `lie`, `lies` | 139/152 (91%) | 46/81 (57%) | 77/138 (56%) | 0/158 (0%) | 37/43 (86%) | 38/73 (52%) |
| disclaimer (a disclaimer) | unclear | `␣disclaimer`, `␣Disclaimer`, `Disclaimer`, `免责声明`, `␣DISCLAIMER`, `免责` | 100/152 (66%) | 74/81 (91%) | 130/138 (94%) | 125/158 (79%) | 33/43 (77%) | 68/73 (93%) |
| fact (fact, factual) | truth | `␣fact`, `␣actually`, `␣actual`, `␣reality`, `actual`, `␣facts`, `Fact`, `Actual`, `␣Actual`, `␣Actually`, `␣Fact`, `_actual`, `␣Reality`, `␣Facts`, `Reality`, `Actually`, `␣factual`, `facts`, `actually`, `实际`, `事实`, `实际上`, `实际情况`, `的事实`, `的实际`, `实际的`, `实事求是`, `但实际上` | 118/152 (78%) | 53/81 (65%) | 137/138 (99%) | 93/158 (59%) | 34/43 (79%) | 48/73 (66%) |
| deceive (the act of deceiving) | lie | `␣deception`, `欺骗`, `␣deceptive`, `␣deceive`, `␣deceit`, `骗` | 128/152 (84%) | 35/81 (43%) | 8/138 (6%) | 0/158 (0%) | 31/43 (72%) | 30/73 (41%) |
| fake (fake, counterfeit) | lie | `fake`, `␣fake`, `Fake`, `␣Fake`, `.fake` | 133/152 (88%) | 29/81 (36%) | 60/138 (43%) | 16/158 (10%) | 33/43 (77%) | 25/73 (34%) |
| hide (concealing information) | lie | `隐瞒`, `␣hidden`, `␣Hidden`, `掩盖` | 118/152 (78%) | 37/81 (46%) | 20/138 (14%) | 3/158 (2%) | 33/43 (77%) | 32/73 (44%) |
| mistake (making a mistake or error) | unclear | `␣mistake`, `␣mistakes`, `␣errors`, `␣error`, `␣ERROR`, `␣typo`, `␣Errors`, `Errors`, `errors`, `error`, `␣Error`, `-error`, `错误`, `␣erroneous`, `的错误`, `失误` | 105/152 (69%) | 45/81 (56%) | 111/138 (80%) | 154/158 (97%) | 26/43 (60%) | 40/73 (55%) |
| unethical (unethical, immoral) | unclear | `␣unethical`, `␣immoral` | 97/152 (64%) | 52/81 (64%) | 0/138 (0%) | 0/158 (0%) | 20/43 (47%) | 47/73 (64%) |
| contradict (contradicting) | unclear | `␣contradiction`, `␣contradict`, `␣contradictory`, `␣contradictions`, `␣contrad`, `矛盾`, `矛盾的`, `␣contradd` | 84/152 (55%) | 62/81 (77%) | 137/138 (99%) | 53/158 (34%) | 29/43 (67%) | 55/73 (75%) |
| violate (violating a rule) | unclear | `␣violation`, `违反`, `违背`, `␣violations`, `违规`, `␣violate`, `␣violating`, `␣violates`, `违反了`, `␣violated`, `Violation` | 77/152 (51%) | 63/81 (78%) | 78/138 (57%) | 2/158 (1%) | 16/43 (37%) | 57/73 (78%) |
| refuse (refusing) | unclear | `␣refusal`, `拒绝`, `␣refus`, `拒`, `␣refusing`, `␣refuse`, `␣refused`, `拒絕`, `␣refuses`, `拒绝了`, `␣отказ`, `␣отказа` | 64/152 (42%) | 62/81 (77%) | 93/138 (67%) | 3/158 (2%) | 22/43 (51%) | 60/73 (82%) |
| fabricate (making up or forging content) | lie | `伪造`, `虚构`, `造假`, `弄虚作假`, `␣fabricated`, `␣fabrication` | 100/152 (66%) | 21/81 (26%) | 29/138 (21%) | 7/158 (4%) | 22/43 (51%) | 20/73 (27%) |
| explicit (stating explicitly) | unclear | `␣explicit`, `␣Explicit`, `explicit`, `␣explicitly`, `Explicit`, `明确`, `明确的` | 78/152 (51%) | 39/81 (48%) | 77/138 (56%) | 7/158 (4%) | 28/43 (65%) | 36/73 (49%) |
| apologize (apologizing) | unclear | `␣apology`, `␣apologies`, `道歉`, `␣apolog`, `␣apologize` | 54/152 (36%) | 43/81 (53%) | 109/138 (79%) | 60/158 (38%) | 16/43 (37%) | 40/73 (55%) |
| dishonest (dishonesty) | lie | `␣dishonest` | 81/152 (53%) | 12/81 (15%) | 0/138 (0%) | 0/158 (0%) | 19/43 (44%) | 10/73 (14%) |
| mislead (misleading someone) | lie | `␣misleading`, `误导`, `␣misled`, `误导性` | 73/152 (48%) | 17/81 (21%) | 7/138 (5%) | 7/158 (4%) | 14/43 (33%) | 12/73 (16%) |
| incorrect (incorrect) | lie | `␣incorrect`, `Wrong`, `Incorrect`, `␣inaccur`, `␣incorrectly`, `␣inaccurate`, `incorrect`, `␣Incorrect`, `错误的`, `不符合`, `不正确` | 52/152 (34%) | 34/81 (42%) | 124/138 (90%) | 109/158 (69%) | 10/43 (23%) | 29/73 (40%) |
| hallucinate (hallucinating content) | unclear | `␣halluc` | 54/152 (36%) | 31/81 (38%) | 121/138 (88%) | 96/158 (61%) | 15/43 (35%) | 28/73 (38%) |
| fraud (fraud) | lie | `␣fraudulent`, `␣fraud`, `欺诈`, `骗局` | 76/152 (50%) | 6/81 (7%) | 0/138 (0%) | 0/158 (0%) | 18/43 (42%) | 5/73 (7%) |
| ethics (ethics, morality) | unclear | `␣ethical`, `␣ethics`, `␣moral`, `ethical`, `道德`, `伦理`, `␣morally`, `␣Ethics`, `␣Moral`, `的道德`, `␣morality` | 29/152 (19%) | 33/81 (41%) | 2/138 (1%) | 0/158 (0%) | 5/43 (12%) | 31/73 (42%) |
| wrong (wrong, mistaken) | lie | `␣wrong`, `wrong`, `␣Wrong`, `␣WRONG`, `错`, `误`, `错了` | 35/152 (23%) | 23/81 (28%) | 9/138 (7%) | 33/158 (21%) | 5/43 (12%) | 18/73 (25%) |
| secret (secrecy, confidentiality) | lie | `␣confidentiality`, `保密`, `秘密`, `␣secrecy`, `␣undisclosed`, `␣confidential`, `␣Confidential`, `␣secret`, `的秘密` | 29/152 (19%) | 28/81 (35%) | 32/138 (23%) | 0/158 (0%) | 8/43 (19%) | 26/73 (36%) |
| prohibited (prohibited, forbidden) | unclear | `␣prohibited`, `禁止`, `␣forbidden`, `␣prohibition` | 26/152 (17%) | 28/81 (35%) | 47/138 (34%) | 0/158 (0%) | 8/43 (19%) | 26/73 (36%) |
| liar (a person who lies) | lie | `␣liar` | 48/152 (32%) | 5/81 (6%) | 0/138 (0%) | 0/158 (0%) | 17/43 (40%) | 2/73 (3%) |
| confidential (confidentiality) | unclear | `␣confidentiality`, `␣confidential`, `␣Confidential`, `机密` | 21/152 (14%) | 26/81 (32%) | 32/138 (23%) | 0/158 (0%) | 8/43 (19%) | 24/73 (33%) |
| reject (rejecting) | unclear | `␣rejection`, `␣Reject`, `Reject`, `␣rejecting`, `␣reject`, `reject` | 12/152 (8%) | 29/81 (36%) | 8/138 (6%) | 1/158 (1%) | 9/43 (21%) | 29/73 (40%) |
| imply (implying rather than stating) | unclear | `␣implicit`, `␣implicitly`, `暗示`, `隐含`, `implicit`, `Implicit`, `implicitly`, `␣Implicit`, `␣implied`, `␣implying`, `␣implication` | 24/152 (16%) | 15/81 (19%) | 11/138 (8%) | 0/158 (0%) | 8/43 (19%) | 13/73 (18%) |
| comply (complying with rules) | unclear | `␣compliance`, `␣Compliance`, `遵守`, `合规`, `␣compliant`, `严格遵守`, `␣adherence` | 14/152 (9%) | 24/81 (30%) | 28/138 (20%) | 2/158 (1%) | 6/43 (14%) | 21/73 (29%) |
| unauthorized (unauthorized) | unclear | `␣unauthorized`, `␣Unauthorized` | 15/152 (10%) | 21/81 (26%) | 12/138 (9%) | 0/158 (0%) | 5/43 (12%) | 18/73 (25%) |
| misrepresent (presenting something as other than it is) | lie | `␣misrepresented` | 29/152 (19%) | 5/81 (6%) | 1/138 (1%) | 0/158 (0%) | 1/43 (2%) | 3/73 (4%) |
| blatant (blatant, outright) | unclear | `␣blatant`, `␣outright`, `␣blatantly` | 32/152 (21%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 12/43 (28%) | 0/73 (0%) |
| fiction (fiction, made-up story) | unclear | `␣fictional`, `fiction`, `␣Fiction`, `␣fict`, `␣fiction` | 14/152 (9%) | 18/81 (22%) | 16/138 (12%) | 13/158 (8%) | 2/43 (5%) | 18/73 (25%) |
| disclose (disclosing, making public) | truth | `␣disclosure`, `␣disclosures`, `␣Disclosure`, `公开`, `␣disclose`, `␣disclosing`, `信息公开`, `揭露` | 5/152 (3%) | 20/81 (25%) | 7/138 (5%) | 1/158 (1%) | 2/43 (5%) | 17/73 (23%) |
| confess (confessing) | truth | `␣confession`, `坦白`, `␣confess` | 6/152 (4%) | 17/81 (21%) | 8/138 (6%) | 0/158 (0%) | 3/43 (7%) | 15/73 (21%) |
| negate (negating) | unclear | `否定` | 12/152 (8%) | 11/81 (14%) | 13/138 (9%) | 0/158 (0%) | 6/43 (14%) | 10/73 (14%) |
| illegal (illegal) | unclear | `␣illegal`, `违法`, `非法`, `违法行为` | 13/152 (9%) | 10/81 (12%) | 0/138 (0%) | 1/158 (1%) | 3/43 (7%) | 8/73 (11%) |
| hypocrisy (hypocrisy, insincerity) | unclear | `␣hypocrisy`, `虚伪` | 15/152 (10%) | 4/81 (5%) | 0/138 (0%) | 0/158 (0%) | 3/43 (7%) | 4/73 (5%) |
| rebut (rebutting, refuting) | unclear | `反驳`, `␣rebut` | 10/152 (7%) | 8/81 (10%) | 3/138 (2%) | 0/158 (0%) | 4/43 (9%) | 7/73 (10%) |
| intentional (doing it on purpose) | unclear | `␣deliberate`, `故意`, `␣intentionally`, `␣intentional`, `␣deliberately`, `␣knowingly` | 14/152 (9%) | 4/81 (5%) | 1/138 (1%) | 1/158 (1%) | 5/43 (12%) | 3/73 (4%) |
| pretend (pretending, disguising) | lie | `伪装` | 12/152 (8%) | 3/81 (4%) | 0/138 (0%) | 0/158 (0%) | 1/43 (2%) | 2/73 (3%) |
| typo (a typo) | unclear | `␣typo` | 10/152 (7%) | 4/81 (5%) | 13/138 (9%) | 147/158 (93%) | 4/43 (9%) | 3/73 (4%) |
| whistleblow (whistleblowing) | unclear | `␣whistleblower`, `␣whistlebl` | 3/152 (2%) | 10/81 (12%) | 0/138 (0%) | 0/158 (0%) | 0/43 (0%) | 9/73 (12%) |
| transparent (transparency) | truth | `␣transparency`, `透明` | 2/152 (1%) | 8/81 (10%) | 1/138 (1%) | 0/158 (0%) | 0/43 (0%) | 6/73 (8%) |
| misunderstand (misunderstanding) | unclear | `␣misunderstanding`, `误解` | 5/152 (3%) | 5/81 (6%) | 7/138 (5%) | 18/158 (11%) | 3/43 (7%) | 5/73 (7%) |
| unintentional (doing it by accident) | unclear | `␣unintended`, `␣inadvertently`, `␣inadvert`, `␣unintention` | 5/152 (3%) | 4/81 (5%) | 0/138 (0%) | 0/158 (0%) | 1/43 (2%) | 4/73 (5%) |
| roleplay (role-play) | unclear | `角色扮演` | 0/152 (0%) | 9/81 (11%) | 0/138 (0%) | 0/158 (0%) | 0/43 (0%) | 9/73 (12%) |
| evade (evading, dodging) | lie | `␣evasion`, `回避`, `␣evade`, `避开`, `␣dodge`, `规避` | 5/152 (3%) | 3/81 (4%) | 1/138 (1%) | 0/158 (0%) | 2/43 (5%) | 3/73 (4%) |
| hoax (hoax, scam) | lie | `␣hoax`, `骗局` | 8/152 (5%) | 0/81 (0%) | 16/138 (12%) | 2/158 (1%) | 3/43 (7%) | 0/73 (0%) |
| accuse (accusing, alleging) | unclear | `␣accusations`, `␣accusation`, `␣allegations` | 5/152 (3%) | 3/81 (4%) | 3/138 (2%) | 0/158 (0%) | 4/43 (9%) | 3/73 (4%) |
| cheat (cheating) | lie | `␣cheating`, `作弊` | 7/152 (5%) | 0/81 (0%) | 1/138 (1%) | 0/158 (0%) | 3/43 (7%) | 0/73 (0%) |
| conspiracy (conspiracy) | unclear | `␣conspiracy` | 5/152 (3%) | 2/81 (2%) | 3/138 (2%) | 0/158 (0%) | 1/43 (2%) | 2/73 (3%) |
| undisclosed (not disclosed) | lie | `␣undisclosed` | 4/152 (3%) | 3/81 (4%) | 3/138 (2%) | 0/158 (0%) | 0/43 (0%) | 3/73 (4%) |
| leak (leaking information) | unclear | `泄露` | 3/152 (2%) | 3/81 (4%) | 1/138 (1%) | 0/158 (0%) | 1/43 (2%) | 2/73 (3%) |
| plagiarism (plagiarism) | unclear | `␣plagiarism` | 4/152 (3%) | 1/81 (1%) | 0/138 (0%) | 48/158 (30%) | 1/43 (2%) | 1/73 (1%) |
| justification (justifying) | unclear | `␣justification` | 2/152 (1%) | 3/81 (4%) | 1/138 (1%) | 7/158 (4%) | 0/43 (0%) | 3/73 (4%) |
| correct (correct) | truth | `␣correct`, `␣correctly`, `correct`, `␣correction`, `Correct`, `␣corrected`, `␣Correct`, `␣correctness`, `␣Correction`, `␣correcting`, `正确`, `正确的`, `修正`, `正确答案`, `纠正`, `更正`, `是否正确` | 0/152 (0%) | 4/81 (5%) | 35/138 (25%) | 52/158 (33%) | 0/43 (0%) | 3/73 (4%) |
| accurate (accurate) | truth | `␣accurate`, `␣accuracy` | 1/152 (1%) | 3/81 (4%) | 5/138 (4%) | 2/158 (1%) | 0/43 (0%) | 3/73 (4%) |
| harmful (harmful) | unclear | `␣harmful` | 1/152 (1%) | 2/81 (2%) | 1/138 (1%) | 0/158 (0%) | 0/43 (0%) | 2/73 (3%) |
| true (true, real) | truth | `␣true`, `true`, `␣True`, `␣TRUE`, `真的`, `真正`, `真实`, `真实性`, `真正的`, `真实的`, `的真实`, `的真实性`, `的真正` | 1/152 (1%) | 2/81 (2%) | 40/138 (29%) | 3/158 (2%) | 0/43 (0%) | 2/73 (3%) |
| omit (omitting) | unclear | `␣omission` | 2/152 (1%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 0/43 (0%) | 0/73 (0%) |
| exaggerate (exaggerating) | lie | `夸大`, `␣exagger` | 2/152 (1%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 0/43 (0%) | 0/73 (0%) |
| pretext (a false pretext) | lie | `␣pretext` | 1/152 (1%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 1/43 (2%) | 1/73 (1%) |
| inappropriate (inappropriate) | unclear | `␣inappropriate` | 1/152 (1%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 0/43 (0%) | 1/73 (1%) |
| excuse (making an excuse) | unclear | `␣excuse`, `␣excuses` | 1/152 (1%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 0/43 (0%) | 1/73 (1%) |
| manipulate (manipulating) | lie | `␣manipulation`, `␣manipulate`, `␣manipulated`, `␣manipulating`, `␣manipul`, `操纵` | 0/152 (0%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 0/43 (0%) | 1/73 (1%) |
| disobey (disobeying) | unclear | `␣disob`, `␣disobed` | 0/152 (0%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 0/43 (0%) | 1/73 (1%) |
| trick (tricking someone) | lie | `␣trick`, `␣Trick` | 0/152 (0%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 0/43 (0%) | 1/73 (1%) |

Not in the draft: misinformation (excluded: the question's own word); admit (excluded: admit / deny / acknowledge); acknowledge (excluded: admit / deny / acknowledge); deny (excluded: admit / deny / acknowledge); false (excluded: the question's own word); truth (excluded: truth from the question on)

## q_tok6

| family | side | members | lies | truths | no-pressure truths | unrelated | lies that deny | truths that deny |
|---|---|---|---|---|---|---|---|---|
| lie (telling a lie) | lie | `谎言`, `说谎`, `谎` | 152/152 (100%) | 81/81 (100%) | 138/138 (100%) | 65/158 (41%) | 43/43 (100%) | 73/73 (100%) |
| fake (fake, counterfeit) | lie | `fake`, `Fake`, `␣fake`, `␣Fake` | 152/152 (100%) | 81/81 (100%) | 136/138 (99%) | 158/158 (100%) | 43/43 (100%) | 73/73 (100%) |
| fabricate (making up or forging content) | lie | `伪造`, `虚构`, `造假` | 146/152 (96%) | 79/81 (98%) | 77/138 (56%) | 89/158 (56%) | 40/43 (93%) | 71/73 (97%) |
| mislead (misleading someone) | lie | `␣misleading`, `误导` | 144/152 (95%) | 70/81 (86%) | 55/138 (40%) | 46/158 (29%) | 38/43 (88%) | 62/73 (85%) |
| truthful (telling the truth) | truth | `␣truthful` | 147/152 (97%) | 56/81 (69%) | 21/138 (15%) | 2/158 (1%) | 40/43 (93%) | 49/73 (67%) |
| deceive (the act of deceiving) | lie | `␣deceptive`, `欺骗`, `␣deception` | 131/152 (86%) | 41/81 (51%) | 0/138 (0%) | 0/158 (0%) | 34/43 (79%) | 34/73 (47%) |
| error (an error, a mistake) | unclear | `错误`, `␣erroneous` | 97/152 (64%) | 67/81 (83%) | 138/138 (100%) | 158/158 (100%) | 37/43 (86%) | 60/73 (82%) |
| fact (fact, factual) | truth | `␣facts`, `␣Facts`, `␣factual`, `facts`, `事实` | 79/152 (52%) | 30/81 (37%) | 119/138 (86%) | 152/158 (96%) | 23/43 (53%) | 28/73 (38%) |
| misrepresent (presenting something as other than it is) | lie | `␣misrepresented` | 77/152 (51%) | 24/81 (30%) | 2/138 (1%) | 0/158 (0%) | 14/43 (33%) | 20/73 (27%) |
| incorrect (incorrect) | lie | `␣incorrect`, `Incorrect`, `␣inaccur`, `␣inaccurate`, `incorrect`, `␣Incorrect`, `错误的` | 20/152 (13%) | 47/81 (58%) | 138/138 (100%) | 158/158 (100%) | 11/43 (26%) | 45/73 (62%) |
| accuse (accusing, alleging) | unclear | `␣allegation`, `␣accusation` | 17/152 (11%) | 17/81 (21%) | 6/138 (4%) | 4/158 (3%) | 6/43 (14%) | 17/73 (23%) |
| disclaimer (a disclaimer) | unclear | `␣disclaimer` | 6/152 (4%) | 12/81 (15%) | 8/138 (6%) | 2/158 (1%) | 5/43 (12%) | 12/73 (16%) |
| fraud (fraud) | lie | `␣fraudulent` | 10/152 (7%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 5/43 (12%) | 0/73 (0%) |
| justification (justifying) | unclear | `␣justification` | 4/152 (3%) | 2/81 (2%) | 0/138 (0%) | 0/158 (0%) | 0/43 (0%) | 2/73 (3%) |
| exaggerate (exaggerating) | lie | `夸大` | 4/152 (3%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 0/43 (0%) | 0/73 (0%) |
| refuse (refusing) | unclear | `␣refusal` | 1/152 (1%) | 2/81 (2%) | 0/138 (0%) | 1/158 (1%) | 1/43 (2%) | 2/73 (3%) |
| pretext (a false pretext) | lie | `␣pretext` | 1/152 (1%) | 2/81 (2%) | 0/138 (0%) | 0/158 (0%) | 0/43 (0%) | 2/73 (3%) |
| negate (negating) | unclear | `否定` | 1/152 (1%) | 1/81 (1%) | 4/138 (3%) | 0/158 (0%) | 1/43 (2%) | 1/73 (1%) |
| hoax (hoax, scam) | lie | `␣hoax` | 0/152 (0%) | 1/81 (1%) | 0/138 (0%) | 1/158 (1%) | 0/43 (0%) | 1/73 (1%) |
| imply (implying rather than stating) | unclear | `␣implication` | 1/152 (1%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 1/43 (2%) | 0/73 (0%) |
| excuse (making an excuse) | unclear | `␣excuse`, `␣excuses` | 0/152 (0%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 0/43 (0%) | 1/73 (1%) |
| wrong (wrong, mistaken) | lie | `␣WRONG`, `错误或` | 0/152 (0%) | 0/81 (0%) | 6/138 (4%) | 10/158 (6%) | 0/43 (0%) | 0/73 (0%) |

Not in the draft: misinformation (excluded: the question's own word); deny (excluded: admit / deny / acknowledge); false (excluded: the question's own word); truth (excluded: truth from the question on)

## q_tok7

| family | side | members | lies | truths | no-pressure truths | unrelated | lies that deny | truths that deny |
|---|---|---|---|---|---|---|---|---|
| incorrect (incorrect) | lie | `␣incorrect`, `Incorrect`, `␣inaccur`, `␣incorrectly`, `␣inaccurate`, `incorrect`, `␣erroneous`, `␣Incorrect`, `错误的` | 150/152 (99%) | 81/81 (100%) | 138/138 (100%) | 158/158 (100%) | 42/43 (98%) | 73/73 (100%) |
| lie (telling a lie) | lie | `谎言`, `谎`, `说谎` | 151/152 (99%) | 77/81 (95%) | 89/138 (64%) | 3/158 (2%) | 43/43 (100%) | 69/73 (95%) |
| truthful (telling the truth) | truth | `␣truthful` | 151/152 (99%) | 77/81 (95%) | 105/138 (76%) | 48/158 (30%) | 43/43 (100%) | 69/73 (95%) |
| fact (fact, factual) | truth | `␣fact`, `␣facts`, `Fact`, `␣Fact`, `␣Facts`, `␣FACT`, `FACT`, `␣factual`, `事实`, `的事实` | 113/152 (74%) | 66/81 (81%) | 116/138 (84%) | 148/158 (94%) | 29/43 (67%) | 60/73 (82%) |
| intentional (doing it on purpose) | unclear | `故意`, `␣intentionally`, `␣knowingly`, `␣intentional`, `␣deliberately`, `␣deliberate`, `故意的` | 113/152 (74%) | 35/81 (43%) | 0/138 (0%) | 0/158 (0%) | 26/43 (60%) | 31/73 (42%) |
| mislead (misleading someone) | lie | `␣misleading` | 52/152 (34%) | 49/81 (60%) | 7/138 (5%) | 5/158 (3%) | 17/43 (40%) | 45/73 (62%) |
| pretend (pretending, disguising) | lie | `␣pretending` | 28/152 (18%) | 20/81 (25%) | 1/138 (1%) | 0/158 (0%) | 3/43 (7%) | 20/73 (27%) |
| error (an error, a mistake) | unclear | `错误`, `错误或` | 8/152 (5%) | 28/81 (35%) | 130/138 (94%) | 151/158 (96%) | 4/43 (9%) | 27/73 (37%) |
| deceive (the act of deceiving) | lie | `欺骗`, `␣deception`, `␣deceptive` | 26/152 (17%) | 8/81 (10%) | 0/138 (0%) | 0/158 (0%) | 8/43 (19%) | 6/73 (8%) |
| fraud (fraud) | lie | `␣fraudulent` | 11/152 (7%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 7/43 (16%) | 1/73 (1%) |
| violate (violating a rule) | unclear | `␣violating` | 4/152 (3%) | 1/81 (1%) | 1/138 (1%) | 0/158 (0%) | 0/43 (0%) | 0/73 (0%) |
| misrepresent (presenting something as other than it is) | lie | `␣misrepresented` | 4/152 (3%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 0/43 (0%) | 0/73 (0%) |
| fabricate (making up or forging content) | lie | `虚构` | 2/152 (1%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 1/43 (2%) | 1/73 (1%) |
| contradict (contradicting) | unclear | `␣contradict`, `␣contradictory` | 0/152 (0%) | 3/81 (4%) | 48/138 (35%) | 0/158 (0%) | 0/43 (0%) | 2/73 (3%) |
| accuse (accusing, alleging) | unclear | `␣alleging` | 2/152 (1%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 2/43 (5%) | 1/73 (1%) |
| dishonest (dishonesty) | lie | `␣dishonest` | 1/152 (1%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 1/43 (2%) | 0/73 (0%) |

Not in the draft: misinformation (excluded: the question's own word); deny (excluded: admit / deny / acknowledge); false (excluded: the question's own word); truth (excluded: truth from the question on)
