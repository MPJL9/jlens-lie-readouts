# Draft families: qwen3.6-27b, J-lens, part Q6_factual, group postans

Written by `scripts/apply_family_decisions.py` (2026-10-01; draft, not frozen). Counts are `present / transcripts (share)`
on the build split.

## postans_slot0

| family | side | members | lies | truths | no-pressure truths | unrelated | lies that deny | truths that deny |
|---|---|---|---|---|---|---|---|---|
| hide (hiding, concealing) | lie | `-hide`, `匿`, `masked`, `藏`, `掩` | 36/152 (24%) | 34/81 (42%) | 4/138 (3%) | 3/158 (2%) | 19/43 (44%) | 34/73 (47%) |
| leak (leaking information) | unclear | `␣WikiLeaks` | 7/152 (5%) | 13/81 (16%) | 75/138 (54%) | 60/158 (38%) | 5/43 (12%) | 13/73 (18%) |
| mask (masking) | lie | `masked` | 4/152 (3%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 2/43 (5%) | 1/73 (1%) |

## postans_slot1

| family | side | members | lies | truths | no-pressure truths | unrelated | lies that deny | truths that deny |
|---|---|---|---|---|---|---|---|---|
| honest (honesty, being truthful) | truth | `␣truthful`, `␣honesty`, `诚实`, `如实` | 135/152 (89%) | 32/81 (40%) | 6/138 (4%) | 3/158 (2%) | 29/43 (67%) | 26/73 (36%) |
| truthful (being truthful) | truth | `␣truthful` | 135/152 (89%) | 32/81 (40%) | 6/138 (4%) | 3/158 (2%) | 29/43 (67%) | 26/73 (36%) |
| disclaimer (a disclaimer) | unclear | `␣DISCLAIMER`, `␣Disclaimer`, `Disclaimer`, `␣disclaimer` | 77/152 (51%) | 15/81 (19%) | 25/138 (18%) | 3/158 (2%) | 10/43 (23%) | 10/73 (14%) |
| lie (telling a lie) | lie | `说谎`, `谎言`, `撒谎`, `谎`, `␣mentira` | 73/152 (48%) | 5/81 (6%) | 0/138 (0%) | 0/158 (0%) | 15/43 (35%) | 2/73 (3%) |
| true (true, real) | truth | `真实`, `真实性`, `真实的`, `的真实` | 60/152 (39%) | 10/81 (12%) | 0/138 (0%) | 1/158 (1%) | 0/43 (0%) | 10/73 (14%) |
| fact (facts, factual) | unclear | `␣factual`, `事实` | 42/152 (28%) | 14/81 (17%) | 1/138 (1%) | 13/158 (8%) | 7/43 (16%) | 13/73 (18%) |
| hide (hiding, concealing) | lie | `-hide`, `隐瞒` | 44/152 (29%) | 6/81 (7%) | 26/138 (19%) | 28/158 (18%) | 10/43 (23%) | 6/73 (8%) |
| violate (violating a rule) | unclear | `违反`, `违背`, `违反了`, `␣violating` | 45/152 (30%) | 5/81 (6%) | 0/138 (0%) | 0/158 (0%) | 9/43 (21%) | 2/73 (3%) |
| fabricate (making things up, forging) | lie | `虚构`, `伪造` | 33/152 (22%) | 4/81 (5%) | 0/138 (0%) | 3/158 (2%) | 8/43 (19%) | 3/73 (4%) |
| incorrect (incorrect) | lie | `␣incorrect`, `Incorrect`, `␣inaccur`, `␣incorrectly`, `␣inaccurate`, `incorrect`, `␣Incorrect`, `错误的`, `不符合`, `不正确` | 25/152 (16%) | 12/81 (15%) | 5/138 (4%) | 8/158 (5%) | 5/43 (12%) | 7/73 (10%) |
| deceive (the act of deceiving) | lie | `欺骗`, `␣deception` | 24/152 (16%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 5/43 (12%) | 0/73 (0%) |
| dishonest (dishonest) | lie | `␣dishonest` | 22/152 (14%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 7/43 (16%) | 0/73 (0%) |
| correct (correct) | truth | `␣correct`, `␣correctly`, `correct`, `Correct`, `␣corrected`, `␣Correct`, `␣correctness`, `␣Correction`, `Correction`, `正确`, `正确的`, `修正`, `纠错`, `正确答案`, `纠正`, `更正` | 6/152 (4%) | 16/81 (20%) | 105/138 (76%) | 89/158 (56%) | 1/43 (2%) | 15/73 (21%) |
| wrong (wrong, mistaken) | lie | `␣ERROR`, `wrong`, `误`, `错误`, `的错误` | 13/152 (9%) | 6/81 (7%) | 4/138 (3%) | 15/158 (9%) | 1/43 (2%) | 3/73 (4%) |
| fake (fake, not genuine) | lie | `fake`, `Fake`, `␣Fake` | 17/152 (11%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 1/43 (2%) | 0/73 (0%) |
| contradiction (contradiction, inconsistency) | unclear | `␣contradiction`, `␣contradict`, `␣contradictory`, `␣contradictions`, `矛盾`, `矛盾的` | 11/152 (7%) | 6/81 (7%) | 1/138 (1%) | 0/158 (0%) | 9/43 (21%) | 5/73 (7%) |
| hypocrisy (hypocrisy) | lie | `␣hypocrisy` | 11/152 (7%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 6/43 (14%) | 1/73 (1%) |
| misinformation (false information spread to others) | lie | `␣misinformation` | 8/152 (5%) | 2/81 (2%) | 1/138 (1%) | 1/158 (1%) | 2/43 (5%) | 0/73 (0%) |
| legal (legal, lawful) | unclear | `合法`, `Legal`, `␣Legal`, `␣legality` | 5/152 (3%) | 5/81 (6%) | 0/138 (0%) | 0/158 (0%) | 5/43 (12%) | 5/73 (7%) |
| clarify (clarifying) | truth | `澄清` | 2/152 (1%) | 8/81 (10%) | 2/138 (1%) | 2/158 (1%) | 2/43 (5%) | 8/73 (11%) |
| mislead (misleading someone) | lie | `␣misleading`, `误导` | 3/152 (2%) | 6/81 (7%) | 3/138 (2%) | 0/158 (0%) | 0/43 (0%) | 3/73 (4%) |
| whistleblow (reporting wrongdoing) | truth | `举报` | 9/152 (6%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 2/43 (5%) | 0/73 (0%) |
| illegal (illegal) | unclear | `非法`, `违法`, `illegal`, `Illegal` | 7/152 (5%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 6/43 (14%) | 0/73 (0%) |
| unethical (unethical, immoral) | lie | `␣unethical` | 5/152 (3%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 1/43 (2%) | 0/73 (0%) |
| hoax (a hoax) | lie | `␣hoax` | 3/152 (2%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 0/43 (0%) | 0/73 (0%) |
| moral (morality) | unclear | `道德` | 3/152 (2%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 0/43 (0%) | 0/73 (0%) |
| refuse (refusing) | unclear | `拒绝` | 0/152 (0%) | 3/81 (4%) | 0/138 (0%) | 0/158 (0%) | 0/43 (0%) | 3/73 (4%) |
| interrogate (interrogating) | unclear | `␣interrog` | 2/152 (1%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 2/43 (5%) | 1/73 (1%) |
| comply (complying with rules) | unclear | `遵守` | 0/152 (0%) | 3/81 (4%) | 0/138 (0%) | 0/158 (0%) | 0/43 (0%) | 3/73 (4%) |
| apologize (apologizing) | truth | `道歉` | 2/152 (1%) | 0/81 (0%) | 0/138 (0%) | 1/158 (1%) | 0/43 (0%) | 0/73 (0%) |
| coerce (forcing, coercing) | unclear | `逼`, `逼迫`, `倒逼`, `迫`, `被迫`, `强制`, `forced`, `␣forced` | 1/152 (1%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 1/43 (2%) | 1/73 (1%) |
| fictional (fiction, fictional) | unclear | `␣Fiction`, `␣fictional`, `fiction` | 1/152 (1%) | 0/81 (0%) | 0/138 (0%) | 1/158 (1%) | 1/43 (2%) | 0/73 (0%) |
| trap (a trap) | unclear | `陷阱` | 1/152 (1%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 1/43 (2%) | 0/73 (0%) |
| loophole (a loophole) | unclear | `␣loophole` | 0/152 (0%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 0/43 (0%) | 1/73 (1%) |
| accuse (accusing) | unclear | `␣accusations`, `␣accusing`, `指控` | 0/152 (0%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 0/43 (0%) | 1/73 (1%) |
| accurate (accurate) | truth | `accur` | 0/152 (0%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 0/43 (0%) | 1/73 (1%) |

Not in the draft: truth (excluded: truth from the question on); deny (excluded: admit / deny / acknowledge); admit (excluded: admit / deny / acknowledge); false (excluded: the question's own word)

## postans_slot2

| family | side | members | lies | truths | no-pressure truths | unrelated | lies that deny | truths that deny |
|---|---|---|---|---|---|---|---|---|
| critique (criticising, critique) | unclear | `␣critique`, `批评`, `批判`, `␣critic`, `␣criticize` | 80/152 (53%) | 41/81 (51%) | 0/138 (0%) | 0/158 (0%) | 15/43 (35%) | 35/73 (48%) |
| prohibit (prohibiting) | unclear | `禁止`, `严禁` | 8/152 (5%) | 2/81 (2%) | 2/138 (1%) | 0/158 (0%) | 2/43 (5%) | 2/73 (3%) |
| interrogate (interrogating) | unclear | `␣interrog`, `质问` | 9/152 (6%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 8/43 (19%) | 0/73 (0%) |
| challenge_doubt (questioning, casting doubt) | unclear | `质疑`, `质问` | 7/152 (5%) | 1/81 (1%) | 1/138 (1%) | 0/158 (0%) | 6/43 (14%) | 1/73 (1%) |
| illegal (illegal) | unclear | `非法`, `illegal`, `␣illegal`, `␣Illegal`, `Illegal`, `␣ilegal` | 6/152 (4%) | 1/81 (1%) | 2/138 (1%) | 0/158 (0%) | 4/43 (9%) | 1/73 (1%) |
| promote (promoting, marketing) | unclear | `␣promotional`, `␣promoting`, `␣marketing`, `宣传` | 2/152 (1%) | 3/81 (4%) | 0/138 (0%) | 0/158 (0%) | 2/43 (5%) | 3/73 (4%) |
| confidential (confidentiality, keeping confidential) | unclear | `␣confidential`, `␣confidentiality`, `保密` | 1/152 (1%) | 3/81 (4%) | 0/138 (0%) | 0/158 (0%) | 1/43 (2%) | 3/73 (4%) |
| legal (legal, lawful) | unclear | `合法`, `Legal`, `legal`, `␣Legal` | 4/152 (3%) | 0/81 (0%) | 1/138 (1%) | 0/158 (0%) | 3/43 (7%) | 0/73 (0%) |
| refuse (refusing) | unclear | `拒绝`, `␣refusal` | 2/152 (1%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 1/43 (2%) | 1/73 (1%) |
| comply (complying with rules) | unclear | `␣compliance`, `␣Compliance`, `␣compliant`, `合规`, `遵守` | 0/152 (0%) | 3/81 (4%) | 1/138 (1%) | 0/158 (0%) | 0/43 (0%) | 3/73 (4%) |
| secret (secrecy, secret) | lie | `␣secrecy`, `秘密` | 0/152 (0%) | 2/81 (2%) | 0/138 (0%) | 0/158 (0%) | 0/43 (0%) | 2/73 (3%) |
| whistleblow (reporting wrongdoing) | truth | `␣whistleblower`, `␣whistlebl` | 1/152 (1%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 1/43 (2%) | 1/73 (1%) |
| coerce (forcing, coercing) | unclear | `逼` | 2/152 (1%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 1/43 (2%) | 0/73 (0%) |
| persuade (persuading) | unclear | `␣persu`, `␣persuasive`, `␣persuasion`, `␣persuade`, `劝`, `劝说`, `␣convince`, `␣convincing` | 0/152 (0%) | 2/81 (2%) | 0/138 (0%) | 0/158 (0%) | 0/43 (0%) | 2/73 (3%) |
| threat (threatening) | unclear | `␣threat`, `␣threats`, `␣threatening`, `␣threaten`, `威胁` | 0/152 (0%) | 2/81 (2%) | 0/138 (0%) | 0/158 (0%) | 0/43 (0%) | 2/73 (3%) |
| hide (hiding, concealing) | lie | `隐瞒` | 0/152 (0%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 0/43 (0%) | 1/73 (1%) |
| honest (honesty, being truthful) | truth | `␣truthful` | 0/152 (0%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 0/43 (0%) | 1/73 (1%) |
| unethical (unethical, immoral) | lie | `␣unethical` | 0/152 (0%) | 1/81 (1%) | 1/138 (1%) | 0/158 (0%) | 0/43 (0%) | 1/73 (1%) |
| violate (violating a rule) | unclear | `违反`, `违背`, `违规` | 0/152 (0%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 0/43 (0%) | 1/73 (1%) |
| hypocrisy (hypocrisy) | lie | `␣hypocrisy` | 0/152 (0%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 0/43 (0%) | 1/73 (1%) |
| disclaimer (a disclaimer) | unclear | `␣Disclaimer`, `␣disclaimer` | 1/152 (1%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 1/43 (2%) | 0/73 (0%) |
| blackmail (blackmail) | unclear | `␣blackmail` | 0/152 (0%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 0/43 (0%) | 1/73 (1%) |
| intentional (doing it on purpose) | unclear | `␣intentionally` | 0/152 (0%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 0/43 (0%) | 1/73 (1%) |
| wrong (wrong, mistaken) | lie | `rong`, `wrong` | 0/152 (0%) | 0/81 (0%) | 0/138 (0%) | 6/158 (4%) | 0/43 (0%) | 0/73 (0%) |

Not in the draft: truth (excluded: truth from the question on); admit (excluded: admit / deny / acknowledge)

## postans_slot3

| family | side | members | lies | truths | no-pressure truths | unrelated | lies that deny | truths that deny |
|---|---|---|---|---|---|---|---|---|
| wrong (wrong, mistaken) | lie | `wrong`, `错`, `误`, `错了` | 1/152 (1%) | 3/81 (4%) | 20/138 (14%) | 15/158 (9%) | 1/43 (2%) | 2/73 (3%) |
| fault (blame, being at fault) | unclear | `Fault` | 1/152 (1%) | 0/81 (0%) | 2/138 (1%) | 7/158 (4%) | 1/43 (2%) | 0/73 (0%) |
| conceal (to conceal, to hide) | lie | `藏` | 0/152 (0%) | 0/81 (0%) | 0/138 (0%) | 1/158 (1%) | 0/43 (0%) | 0/73 (0%) |
| correct (correct) | truth | `_correction`, `Correction`, `正确`, `修正`, `纠正`, `改正`, `更正` | 0/152 (0%) | 0/81 (0%) | 0/138 (0%) | 42/158 (27%) | 0/43 (0%) | 0/73 (0%) |

Not in the draft: false (excluded: the question's own word)

## postans_slot4

| family | side | members | lies | truths | no-pressure truths | unrelated | lies that deny | truths that deny |
|---|---|---|---|---|---|---|---|---|
| unethical (unethical, immoral) | lie | `␣unethical`, `␣immoral` | 76/152 (50%) | 35/81 (43%) | 0/138 (0%) | 0/158 (0%) | 13/43 (30%) | 31/73 (42%) |
| misinformation (false information spread to others) | lie | `␣misinformation` | 73/152 (48%) | 35/81 (43%) | 68/138 (49%) | 37/158 (23%) | 21/43 (49%) | 30/73 (41%) |
| honest (honesty, being truthful) | truth | `␣truthful`, `␣honesty`, `␣honest`, `␣Honest`, `诚实`, `如实`, `坦诚` | 72/152 (47%) | 24/81 (30%) | 52/138 (38%) | 0/158 (0%) | 27/43 (63%) | 21/73 (29%) |
| truthful (being truthful) | truth | `␣truthful` | 72/152 (47%) | 24/81 (30%) | 52/138 (38%) | 0/158 (0%) | 27/43 (63%) | 21/73 (29%) |
| ethics (ethics, ethical) | unclear | `␣ethical`, `␣ethics`, `␣Ethics`, `ethical`, `伦理`, `␣ethic` | 64/152 (42%) | 31/81 (38%) | 0/138 (0%) | 0/158 (0%) | 14/43 (33%) | 29/73 (40%) |
| violate (violating a rule) | unclear | `违反`, `违背`, `违规`, `违反了`, `␣violating`, `␣violations`, `␣violate`, `␣violation`, `␣violates`, `␣violated`, `Violation` | 70/152 (46%) | 25/81 (31%) | 19/138 (14%) | 0/158 (0%) | 7/43 (16%) | 22/73 (30%) |
| ethical (ethical, morally right) | unclear | `␣ethical`, `ethical` | 63/152 (41%) | 30/81 (37%) | 0/138 (0%) | 0/158 (0%) | 14/43 (33%) | 28/73 (38%) |
| whistleblow (reporting wrongdoing) | truth | `␣whistleblower`, `␣whistlebl`, `举报` | 69/152 (45%) | 22/81 (27%) | 0/138 (0%) | 0/158 (0%) | 4/43 (9%) | 18/73 (25%) |
| moral (morality) | unclear | `␣moral`, `␣morally`, `␣Moral`, `␣morality`, `␣morals`, `道德`, `的道德`, `职业道德`, `␣ethics`, `␣Ethics`, `␣ethic`, `伦理` | 54/152 (36%) | 28/81 (35%) | 0/138 (0%) | 0/158 (0%) | 12/43 (28%) | 26/73 (36%) |
| fake (fake, not genuine) | lie | `fake`, `Fake`, `␣Fake`, `␣fake` | 36/152 (24%) | 26/81 (32%) | 7/138 (5%) | 9/158 (6%) | 14/43 (33%) | 24/73 (33%) |
| prohibit (prohibiting) | unclear | `禁止`, `严禁`, `␣prohibited`, `␣prohibit`, `␣prohibiting` | 36/152 (24%) | 25/81 (31%) | 5/138 (4%) | 0/158 (0%) | 9/43 (21%) | 23/73 (32%) |
| deceive (the act of deceiving) | lie | `欺骗`, `␣deception`, `␣deceptive`, `骗` | 35/152 (23%) | 24/81 (30%) | 3/138 (2%) | 0/158 (0%) | 17/43 (40%) | 22/73 (30%) |
| interrogate (interrogating) | unclear | `␣interrog`, `␣interrogation`, `质问` | 36/152 (24%) | 19/81 (23%) | 2/138 (1%) | 0/158 (0%) | 19/43 (44%) | 18/73 (25%) |
| confidential (confidentiality, keeping confidential) | unclear | `␣confidentiality`, `保密` | 28/152 (18%) | 8/81 (10%) | 0/138 (0%) | 0/158 (0%) | 3/43 (7%) | 6/73 (8%) |
| challenge_doubt (questioning, casting doubt) | unclear | `质疑`, `质问` | 18/152 (12%) | 15/81 (19%) | 9/138 (7%) | 20/158 (13%) | 4/43 (9%) | 14/73 (19%) |
| comply (complying with rules) | unclear | `␣compliance`, `␣Compliance`, `合规`, `遵守`, `严格遵守` | 16/152 (11%) | 15/81 (19%) | 4/138 (3%) | 0/158 (0%) | 3/43 (7%) | 15/73 (21%) |
| disclose (disclosing, making public) | truth | `␣disclosure`, `␣Disclosure`, `␣disclosures`, `␣disclosing`, `␣disclose`, `公开`, `信息公开`, `揭露` | 23/152 (15%) | 6/81 (7%) | 0/138 (0%) | 0/158 (0%) | 2/43 (5%) | 3/73 (4%) |
| hide (hiding, concealing) | lie | `隐瞒`, `隐藏`, `␣hidden`, `␣Hidden`, `隐蔽` | 21/152 (14%) | 7/81 (9%) | 2/138 (1%) | 4/158 (3%) | 8/43 (19%) | 6/73 (8%) |
| accuse (accusing) | unclear | `␣accusations`, `␣accusing`, `␣accusation`, `指控`, `指责` | 18/152 (12%) | 10/81 (12%) | 1/138 (1%) | 1/158 (1%) | 1/43 (2%) | 9/73 (12%) |
| hypocrisy (hypocrisy) | lie | `␣hypocrisy` | 16/152 (11%) | 11/81 (14%) | 3/138 (2%) | 0/158 (0%) | 7/43 (16%) | 10/73 (14%) |
| lie (telling a lie) | lie | `说谎`, `谎言`, `撒谎`, `␣lie`, `␣Lies`, `␣lying`, `␣liar` | 19/152 (12%) | 6/81 (7%) | 2/138 (1%) | 0/158 (0%) | 15/43 (35%) | 6/73 (8%) |
| pretend (pretending, disguising) | lie | `␣pretending`, `␣pretend`, `伪装`, `␣disguised` | 10/152 (7%) | 14/81 (17%) | 0/138 (0%) | 0/158 (0%) | 3/43 (7%) | 12/73 (16%) |
| trap (a trap) | unclear | `陷阱`, `␣Trap`, `␣trap`, `␣traps`, `trap`, `Trap`, `␣trapped`, `␣trapping`, `_trap`, `␣atrap` | 12/152 (8%) | 12/81 (15%) | 2/138 (1%) | 0/158 (0%) | 10/43 (23%) | 11/73 (15%) |
| coerce (forcing, coercing) | unclear | `逼`, `逼迫`, `倒逼`, `迫`, `被迫`, `迫使`, `强制`, `强迫`, `胁迫`, `逼人`, `forced`, `␣forced`, `␣forcing`, `forcing`, `␣Forced`, `␣coercion` | 15/152 (10%) | 7/81 (9%) | 1/138 (1%) | 0/158 (0%) | 9/43 (21%) | 6/73 (8%) |
| integrity (integrity) | truth | `␣Integrity`, `␣integrity`, `诚信` | 13/152 (9%) | 5/81 (6%) | 1/138 (1%) | 0/158 (0%) | 9/43 (21%) | 5/73 (7%) |
| fabricate (making things up, forging) | lie | `虚构`, `伪造` | 7/152 (5%) | 10/81 (12%) | 9/138 (7%) | 6/158 (4%) | 3/43 (7%) | 8/73 (11%) |
| trick (a trick) | unclear | `␣trick`, `␣Trick`, `␣tricky`, `␣tricks`, `␣Tricks` | 7/152 (5%) | 10/81 (12%) | 2/138 (1%) | 0/158 (0%) | 7/43 (16%) | 9/73 (12%) |
| fraud (fraud, swindle) | lie | `欺诈`, `␣fraudulent`, `␣Fraud`, `␣fraud`, `骗局`, `诈骗` | 7/152 (5%) | 9/81 (11%) | 0/138 (0%) | 0/158 (0%) | 2/43 (5%) | 9/73 (12%) |
| loophole (a loophole) | unclear | `␣loophole` | 7/152 (5%) | 8/81 (10%) | 1/138 (1%) | 0/158 (0%) | 6/43 (14%) | 7/73 (10%) |
| contradiction (contradiction, inconsistency) | unclear | `␣contradiction`, `␣contradict`, `␣contradictory`, `␣contradictions`, `矛盾` | 9/152 (6%) | 5/81 (6%) | 46/138 (33%) | 3/158 (2%) | 5/43 (12%) | 3/73 (4%) |
| disclaimer (a disclaimer) | unclear | `␣disclaimer` | 8/152 (5%) | 6/81 (7%) | 3/138 (2%) | 0/158 (0%) | 2/43 (5%) | 5/73 (7%) |
| blackmail (blackmail) | unclear | `␣blackmail` | 8/152 (5%) | 5/81 (6%) | 0/138 (0%) | 0/158 (0%) | 4/43 (9%) | 4/73 (5%) |
| intentional (doing it on purpose) | unclear | `故意`, `␣intentionally` | 7/152 (5%) | 6/81 (7%) | 1/138 (1%) | 0/158 (0%) | 4/43 (9%) | 5/73 (7%) |
| censorship (censorship) | unclear | `␣censorship` | 3/152 (2%) | 10/81 (12%) | 0/138 (0%) | 0/158 (0%) | 1/43 (2%) | 9/73 (12%) |
| strategic game (strategic play between parties) | unclear | `博弈` | 6/152 (4%) | 6/81 (7%) | 0/138 (0%) | 0/158 (0%) | 5/43 (12%) | 5/73 (7%) |
| secret (secrecy, secret) | lie | `␣secrecy`, `␣secretly`, `␣secretive`, `秘密`, `的秘密` | 6/152 (4%) | 5/81 (6%) | 0/138 (0%) | 0/158 (0%) | 2/43 (5%) | 3/73 (4%) |
| legal (legal, lawful) | unclear | `␣Legal`, `␣legal`, `␣legality`, `␣legally`, `/legal` | 8/152 (5%) | 3/81 (4%) | 0/138 (0%) | 0/158 (0%) | 1/43 (2%) | 3/73 (4%) |
| refuse (refusing) | unclear | `拒绝`, `␣refusal`, `␣refus`, `␣refused`, `␣refuse`, `␣refusing` | 1/152 (1%) | 9/81 (11%) | 2/138 (1%) | 0/158 (0%) | 0/43 (0%) | 9/73 (12%) |
| hoax (a hoax) | lie | `␣hoax` | 3/152 (2%) | 5/81 (6%) | 2/138 (1%) | 1/158 (1%) | 3/43 (7%) | 5/73 (7%) |
| fictional (fiction, fictional) | unclear | `␣Fiction`, `␣fictional` | 4/152 (3%) | 4/81 (5%) | 3/138 (2%) | 7/158 (4%) | 1/43 (2%) | 3/73 (4%) |
| fact (facts, factual) | unclear | `␣factual`, `事实`, `的事实`, `␣Facts`, `␣facts`, `␣Fact`, `␣actually`, `␣actual`, `␣reality`, `actual`, `Actual`, `␣Actual`, `␣Actually`, `Actually`, `facts`, `实际`, `的实际`, `实际的` | 6/152 (4%) | 2/81 (2%) | 51/138 (37%) | 5/158 (3%) | 4/43 (9%) | 2/73 (3%) |
| illegal (illegal) | unclear | `非法`, `违法`, `illegal`, `␣illegal`, `␣Illegal`, `Illegal`, `␣illegally`, `␣ilegal` | 5/152 (3%) | 3/81 (4%) | 0/138 (0%) | 0/158 (0%) | 0/43 (0%) | 2/73 (3%) |
| critique (criticising, critique) | unclear | `␣critique`, `␣critiques` | 5/152 (3%) | 3/81 (4%) | 0/138 (0%) | 39/158 (25%) | 0/43 (0%) | 3/73 (4%) |
| transparent (transparency) | truth | `␣transparency`, `␣Transparency` | 7/152 (5%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 0/43 (0%) | 0/73 (0%) |
| report (reporting wrongdoing) | unclear | `举报` | 7/152 (5%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 1/43 (2%) | 0/73 (0%) |
| paradox (a paradox) | unclear | `␣paradox` | 5/152 (3%) | 2/81 (2%) | 2/138 (1%) | 3/158 (2%) | 5/43 (12%) | 1/73 (1%) |
| leak (leaking information) | unclear | `泄露`, `␣leaked` | 5/152 (3%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 1/43 (2%) | 0/73 (0%) |
| dishonest (dishonest) | lie | `␣dishonest` | 4/152 (3%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 2/43 (5%) | 1/73 (1%) |
| dilemma (a dilemma) | unclear | `␣dilemma` | 5/152 (3%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 4/43 (9%) | 0/73 (0%) |
| expose (exposing, laying bare) | truth | `揭露` | 4/152 (3%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 0/43 (0%) | 0/73 (0%) |
| true (true, real) | truth | `␣true`, `真实`, `真实性`, `真实的`, `的真实` | 3/152 (2%) | 1/81 (1%) | 4/138 (3%) | 0/158 (0%) | 2/43 (5%) | 0/73 (0%) |
| threat (threatening) | unclear | `␣threat`, `␣threats`, `␣Threat`, `威胁` | 2/152 (1%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 1/43 (2%) | 1/73 (1%) |
| incorrect (incorrect) | lie | `␣incorrect`, `Incorrect`, `␣inaccur`, `␣incorrectly`, `␣inaccurate`, `incorrect`, `␣Incorrect`, `错误的`, `有误` | 3/152 (2%) | 0/81 (0%) | 30/138 (22%) | 87/158 (55%) | 0/43 (0%) | 0/73 (0%) |
| mislead (misleading someone) | lie | `␣misleading`, `误导` | 2/152 (1%) | 0/81 (0%) | 3/138 (2%) | 7/158 (4%) | 1/43 (2%) | 0/73 (0%) |
| cheat (cheating) | lie | `␣cheating`, `作弊` | 1/152 (1%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 1/43 (2%) | 1/73 (1%) |
| frame (framing someone, false incrimination) | unclear | `陷害` | 1/152 (1%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 1/43 (2%) | 1/73 (1%) |
| correct (correct) | truth | `␣correct`, `␣correctly`, `correct`, `␣correction`, `Correct`, `␣corrected`, `␣Correct`, `␣corrections`, `␣correctness`, `␣Correction`, `␣correcting`, `.correct`, `Correction`, `␣Corrections`, `正确`, `正确的`, `修正`, `纠错`, `正确答案`, `纠正`, `改正`, `的正确`, `更正`, `是正确的`, `是否正确` | 2/152 (1%) | 0/81 (0%) | 10/138 (7%) | 26/158 (16%) | 0/43 (0%) | 0/73 (0%) |
| wrong (wrong, mistaken) | lie | `␣ERROR`, `␣Wrong`, `误`, `错误`, `的错误` | 1/152 (1%) | 1/81 (1%) | 20/138 (14%) | 85/158 (54%) | 0/43 (0%) | 1/73 (1%) |
| accurate (accurate) | truth | `␣accuracy`, `␣Accuracy` | 2/152 (1%) | 0/81 (0%) | 1/138 (1%) | 2/158 (1%) | 2/43 (5%) | 0/73 (0%) |
| apologize (apologizing) | truth | `道歉` | 1/152 (1%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 0/43 (0%) | 0/73 (0%) |
| evasion (evading) | lie | `␣evasion` | 0/152 (0%) | 1/81 (1%) | 1/138 (1%) | 0/158 (0%) | 0/43 (0%) | 1/73 (1%) |
| manipulate (manipulating) | lie | `␣manipulation` | 1/152 (1%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 1/43 (2%) | 0/73 (0%) |
| propaganda (propaganda) | unclear | `␣propaganda` | 0/152 (0%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 0/43 (0%) | 1/73 (1%) |

Not in the draft: truth (excluded: truth from the question on); deny (excluded: admit / deny / acknowledge); admit (excluded: admit / deny / acknowledge); false (excluded: the question's own word)
