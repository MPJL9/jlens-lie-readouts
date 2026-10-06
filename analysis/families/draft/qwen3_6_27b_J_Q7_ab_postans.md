# Draft families: qwen3.6-27b, J-lens, part Q7_ab, group postans

Written by `scripts/apply_family_decisions.py` (2026-10-01; draft, not frozen). Counts are `present / transcripts (share)`
on the build split.

## postans_slot0

| family | side | members | lies | truths | no-pressure truths | unrelated | lies that deny | truths that deny |
|---|---|---|---|---|---|---|---|---|
| hide (hiding or concealing) | lie | `-hide`, `藏`, `隐` | 78/152 (51%) | 34/81 (42%) | 84/138 (61%) | 5/158 (3%) | 43/79 (54%) | 33/77 (43%) |
| leak (leaking hidden information) | unclear | `␣WikiLeaks` | 5/152 (3%) | 1/81 (1%) | 74/138 (54%) | 46/158 (29%) | 1/79 (1%) | 1/77 (1%) |

## postans_slot1

| family | side | members | lies | truths | no-pressure truths | unrelated | lies that deny | truths that deny |
|---|---|---|---|---|---|---|---|---|
| false (false, untrue) | lie | `false`, `False`, `␣fals`, `␣falsely`, `␣falsehood`, `虚假` | 73/152 (48%) | 24/81 (30%) | 2/138 (1%) | 4/158 (3%) | 62/79 (78%) | 21/77 (27%) |
| disclaimer (a disclaimer) | unclear | `Disclaimer`, `␣DISCLAIMER`, `␣disclaimer`, `␣Disclaimer` | 26/152 (17%) | 12/81 (15%) | 9/138 (7%) | 39/158 (25%) | 14/79 (18%) | 11/77 (14%) |
| honest (being honest) | truth | `␣honesty`, `␣honest`, `␣Honest` | 34/152 (22%) | 2/81 (2%) | 0/138 (0%) | 0/158 (0%) | 0/79 (0%) | 2/77 (3%) |
| claim (claiming / asserting something is so) | unclear | `声称`, `␣claims`, `␣Claim`, `␣claim`, `claim`, `␣claimed`, `␣Claims`, `claims`, `␣claiming`, `Claim`, `宣称` | 30/152 (20%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 30/79 (38%) | 0/77 (0%) |
| fake (fake / not genuine) | lie | `fake`, `␣Fake`, `Fake` | 24/152 (16%) | 2/81 (2%) | 0/138 (0%) | 1/158 (1%) | 21/79 (27%) | 1/77 (1%) |
| hide (hiding or concealing) | lie | `隐瞒`, `-hide` | 14/152 (9%) | 2/81 (2%) | 1/138 (1%) | 24/158 (15%) | 2/79 (3%) | 1/77 (1%) |
| assert (asserting) | unclear | `assert`, `␣assertions`, `␣assertion` | 13/152 (9%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 13/79 (16%) | 0/77 (0%) |
| contradiction (self-contradiction) | unclear | `␣contradiction`, `␣contradict`, `␣contradictory`, `矛盾` | 4/152 (3%) | 4/81 (5%) | 3/138 (2%) | 0/158 (0%) | 4/79 (5%) | 4/77 (5%) |
| violate (violating a rule or principle) | unclear | `违反`, `违背` | 7/152 (5%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 0/79 (0%) | 1/77 (1%) |
| apologize (apologizing) | unclear | `道歉` | 7/152 (5%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 0/79 (0%) | 0/77 (0%) |
| incorrect (incorrect) | lie | `␣incorrect`, `Wrong`, `incorrect`, `错误的`, `不符合` | 2/152 (1%) | 4/81 (5%) | 1/138 (1%) | 1/158 (1%) | 1/79 (1%) | 4/77 (5%) |
| fabricate (making something up) | lie | `虚构`, `伪造`, `␣fictional` | 5/152 (3%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 4/79 (5%) | 0/77 (0%) |
| unethical (unethical) | lie | `␣unethical` | 5/152 (3%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 0/79 (0%) | 0/77 (0%) |
| morality (morality / ethics) | unclear | `道德` | 5/152 (3%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 0/79 (0%) | 0/77 (0%) |
| deceive (the act of deceiving) | lie | `欺骗` | 4/152 (3%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 0/79 (0%) | 0/77 (0%) |
| fact (fact, factual) | truth | `actual`, `␣factual` | 3/152 (2%) | 1/81 (1%) | 0/138 (0%) | 1/158 (1%) | 3/79 (4%) | 1/77 (1%) |
| dishonest (being dishonest) | lie | `␣dishonest` | 3/152 (2%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 0/79 (0%) | 0/77 (0%) |
| legal (legality) | unclear | `␣legality`, `legal`, `合法` | 1/152 (1%) | 2/81 (2%) | 0/138 (0%) | 0/158 (0%) | 1/79 (1%) | 2/77 (3%) |
| hide (to hide something) | lie | `-hide` | 2/152 (1%) | 1/81 (1%) | 1/138 (1%) | 24/158 (15%) | 2/79 (3%) | 1/77 (1%) |
| correct (correct) | truth | `Correct`, `正确` | 1/152 (1%) | 2/81 (2%) | 2/138 (1%) | 0/158 (0%) | 0/79 (0%) | 2/77 (3%) |
| confess (confessing / owning up) | truth | `坦白` | 2/152 (1%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 0/79 (0%) | 0/77 (0%) |
| forge (forging, falsifying) | lie | `伪造` | 2/152 (1%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 1/79 (1%) | 0/77 (0%) |
| comply (complying, abiding by rules) | unclear | `遵守` | 0/152 (0%) | 2/81 (2%) | 0/138 (0%) | 0/158 (0%) | 0/79 (0%) | 2/77 (3%) |
| refuse (refusing) | unclear | `␣refusal`, `拒绝` | 1/152 (1%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 1/79 (1%) | 0/77 (0%) |
| hypocrisy (hypocrisy) | lie | `␣hypocrisy` | 1/152 (1%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 1/79 (1%) | 0/77 (0%) |
| cheat (cheating) | lie | `作弊` | 1/152 (1%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 0/79 (0%) | 0/77 (0%) |
| wrong (wrong, mistaken) | lie | `wrong`, `␣Wrong`, `错`, `错误` | 1/152 (1%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 0/79 (0%) | 0/77 (0%) |

Not in the draft: admit (excluded: admit / deny / acknowledge); acknowledge (excluded: admit / deny / acknowledge); deny (excluded: admit / deny / acknowledge); true (excluded: the question's own word); truth (excluded: the question's own word)

## postans_slot2

| family | side | members | lies | truths | no-pressure truths | unrelated | lies that deny | truths that deny |
|---|---|---|---|---|---|---|---|---|
| interrogate (interrogating / pressing with questions) | unclear | `质问` | 3/152 (2%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 3/79 (4%) | 1/77 (1%) |
| illegal (illegal) | unclear | `非法` | 2/152 (1%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 2/79 (3%) | 0/77 (0%) |
| prohibited (forbidden) | unclear | `禁止` | 2/152 (1%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 1/79 (1%) | 0/77 (0%) |
| doubt (doubting / challenging) | unclear | `质疑` | 1/152 (1%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 1/79 (1%) | 0/77 (0%) |
| wrong (wrong, mistaken) | lie | `rong` | 0/152 (0%) | 0/81 (0%) | 1/138 (1%) | 2/158 (1%) | 0/79 (0%) | 0/77 (0%) |

## postans_slot3

| family | side | members | lies | truths | no-pressure truths | unrelated | lies that deny | truths that deny |
|---|---|---|---|---|---|---|---|---|
| apologize (apologizing) | unclear | `␣apologize` | 2/152 (1%) | 3/81 (4%) | 0/138 (0%) | 0/158 (0%) | 0/79 (0%) | 3/77 (4%) |
| wrong (wrong, mistaken) | lie | `wrong`, `错`, `误`, `错了` | 0/152 (0%) | 0/81 (0%) | 1/138 (1%) | 11/158 (7%) | 0/79 (0%) | 0/77 (0%) |
| incorrect (incorrect) | lie | `Incorrect`, `␣Incorrect` | 0/152 (0%) | 0/81 (0%) | 1/138 (1%) | 1/158 (1%) | 0/79 (0%) | 0/77 (0%) |
| correct (correct) | truth | `_correction`, `Correction`, `修正`, `纠正`, `改正` | 0/152 (0%) | 0/81 (0%) | 0/138 (0%) | 20/158 (13%) | 0/79 (0%) | 0/77 (0%) |

## postans_slot4

| family | side | members | lies | truths | no-pressure truths | unrelated | lies that deny | truths that deny |
|---|---|---|---|---|---|---|---|---|
| unethical (unethical) | lie | `␣unethical` | 117/152 (77%) | 45/81 (56%) | 3/138 (2%) | 0/158 (0%) | 51/79 (65%) | 43/77 (56%) |
| ethics (ethics / ethical) | unclear | `␣ethical`, `␣ethics`, `␣Ethics`, `ethical`, `伦理`, `职业道德`, `␣ethic` | 112/152 (74%) | 43/81 (53%) | 2/138 (1%) | 0/158 (0%) | 51/79 (65%) | 41/77 (53%) |
| morality (morality / moral) | unclear | `道德`, `␣moral`, `␣Moral`, `的道德`, `␣morally`, `␣morality`, `␣morals`, `职业道德` | 97/152 (64%) | 29/81 (36%) | 1/138 (1%) | 0/158 (0%) | 40/79 (51%) | 28/77 (36%) |
| deceive (the act of deceiving) | lie | `␣deception`, `欺骗`, `␣deceptive`, `骗`, `␣deceive`, `␣deceit` | 80/152 (53%) | 44/81 (54%) | 5/138 (4%) | 0/158 (0%) | 41/79 (52%) | 42/77 (55%) |
| violate (violating a rule or principle) | unclear | `违反`, `违规`, `违背`, `␣violate`, `␣violations`, `␣violating`, `␣violation`, `违反了`, `␣violates`, `␣violated` | 91/152 (60%) | 28/81 (35%) | 26/138 (19%) | 0/158 (0%) | 31/79 (39%) | 25/77 (32%) |
| misinformation (false information) | lie | `␣misinformation` | 69/152 (45%) | 47/81 (58%) | 73/138 (53%) | 4/158 (3%) | 48/79 (61%) | 45/77 (58%) |
| honest (being honest) | truth | `␣honesty`, `␣honest`, `␣Honest`, `␣honestly` | 93/152 (61%) | 20/81 (25%) | 3/138 (2%) | 0/158 (0%) | 39/79 (49%) | 20/77 (26%) |
| fake (fake / not genuine) | lie | `fake`, `Fake`, `␣fake`, `␣Fake` | 53/152 (35%) | 44/81 (54%) | 29/138 (21%) | 42/158 (27%) | 34/79 (43%) | 42/77 (55%) |
| integrity (integrity) | truth | `␣Integrity`, `诚信`, `␣integrity` | 76/152 (50%) | 19/81 (23%) | 2/138 (1%) | 0/158 (0%) | 31/79 (39%) | 19/77 (25%) |
| whistleblower (whistleblowing (disclosing wrongdoing)) | truth | `␣whistleblower`, `␣whistlebl` | 63/152 (41%) | 24/81 (30%) | 3/138 (2%) | 0/158 (0%) | 31/79 (39%) | 24/77 (31%) |
| hypocrisy (hypocrisy) | lie | `␣hypocrisy`, `虚伪` | 46/152 (30%) | 26/81 (32%) | 4/138 (3%) | 0/158 (0%) | 28/79 (35%) | 25/77 (32%) |
| test (being tested or probed) | unclear | `测试`, `␣testing`, `␣Testing`, `␣tests`, `␣test`, `testing`, `Testing`, `␣testers`, `␣Tests`, `/testing`, `Tests`, `␣tester`, `␣TESTING`, `␣Test`, `-test`, `-testing`, `试探`, `␣probing` | 17/152 (11%) | 36/81 (44%) | 5/138 (4%) | 4/158 (3%) | 15/79 (19%) | 36/77 (47%) |
| fraud (fraud / scam) | lie | `␣Fraud`, `␣fraudulent`, `␣fraud`, `欺诈`, `骗局`, `诈骗`, `␣scams` | 34/152 (22%) | 14/81 (17%) | 0/138 (0%) | 0/158 (0%) | 12/79 (15%) | 13/77 (17%) |
| coerce (being forced / coercion) | unclear | `␣forcing`, `逼迫`, `倒逼`, `␣forced`, `强制`, `逼`, `forcing`, `迫使`, `␣Forced`, `forced`, `强迫`, `迫`, `胁迫`, `被迫`, `␣coercion`, `␣coerc`, `逼人`, `被逼` | 30/152 (20%) | 15/81 (19%) | 2/138 (1%) | 0/158 (0%) | 22/79 (28%) | 14/77 (18%) |
| trap (a trap) | unclear | `陷阱`, `␣Trap`, `␣trap`, `trap`, `␣traps`, `Trap`, `␣trapped`, `␣trapping`, `_trap` | 17/152 (11%) | 26/81 (32%) | 3/138 (2%) | 0/158 (0%) | 15/79 (19%) | 26/77 (34%) |
| compliance (complying with rules) | unclear | `合规`, `␣compliance`, `␣Compliance`, `遵守`, `严格遵守` | 24/152 (16%) | 19/81 (23%) | 4/138 (3%) | 0/158 (0%) | 10/79 (13%) | 18/77 (23%) |
| interrogate (interrogating / pressing with questions) | unclear | `␣interrog`, `␣interrogation`, `质问` | 26/152 (17%) | 13/81 (16%) | 2/138 (1%) | 0/158 (0%) | 22/79 (28%) | 13/77 (17%) |
| dishonest (being dishonest) | lie | `␣dishonest` | 37/152 (24%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 7/79 (9%) | 1/77 (1%) |
| disguise (disguising) | lie | `伪装`, `␣disguised`, `␣disguise` | 9/152 (6%) | 25/81 (31%) | 3/138 (2%) | 0/158 (0%) | 6/79 (8%) | 24/77 (31%) |
| prohibited (forbidden) | unclear | `禁止`, `␣prohibited` | 24/152 (16%) | 7/81 (9%) | 5/138 (4%) | 0/158 (0%) | 6/79 (8%) | 7/77 (9%) |
| hide (hiding or concealing) | lie | `隐瞒`, `␣Hidden`, `hidden`, `␣hidden`, `Hidden`, `隐蔽` | 18/152 (12%) | 10/81 (12%) | 2/138 (1%) | 0/158 (0%) | 5/79 (6%) | 8/77 (10%) |
| illegal (illegal) | unclear | `非法`, `违法`, `␣illegal`, `␣illegally`, `␣Illegal`, `Illegal`, `illegal`, `␣unlawful`, `␣ilegal` | 20/152 (13%) | 8/81 (10%) | 0/138 (0%) | 0/158 (0%) | 4/79 (5%) | 8/77 (10%) |
| conceal (concealing, withholding the truth) | lie | `隐瞒`, `隐蔽` | 18/152 (12%) | 8/81 (10%) | 2/138 (1%) | 0/158 (0%) | 5/79 (6%) | 6/77 (8%) |
| trick (a trick) | unclear | `␣trick`, `␣Trick`, `␣tricks`, `␣Tricks` | 7/152 (5%) | 18/81 (22%) | 1/138 (1%) | 1/158 (1%) | 7/79 (9%) | 18/77 (23%) |
| cheat (cheating) | lie | `作弊`, `␣cheating` | 15/152 (10%) | 9/81 (11%) | 0/138 (0%) | 0/158 (0%) | 9/79 (11%) | 9/77 (12%) |
| accuse (accusing / accusation) | unclear | `␣accusations`, `指控`, `␣accusation`, `␣accusing`, `␣accused`, `␣accus`, `␣accuse`, `␣accuses` | 16/152 (11%) | 8/81 (10%) | 9/138 (7%) | 0/158 (0%) | 10/79 (13%) | 8/77 (10%) |
| intentional (doing it on purpose) | unclear | `故意`, `␣deliberately`, `␣intentionally` | 6/152 (4%) | 17/81 (21%) | 3/138 (2%) | 0/158 (0%) | 5/79 (6%) | 17/77 (22%) |
| deliberate (doing something on purpose) | unclear | `故意` | 4/152 (3%) | 17/81 (21%) | 3/138 (2%) | 0/158 (0%) | 4/79 (5%) | 17/77 (22%) |
| false (false, untrue) | lie | `␣false`, `␣False`, `␣fals`, `␣falsely`, `␣falsehood`, `虚假` | 16/152 (11%) | 3/81 (4%) | 7/138 (5%) | 0/158 (0%) | 10/79 (13%) | 2/77 (3%) |
| fabricate (making something up / forging) | lie | `伪造`, `虚构`, `造假`, `弄虚作假` | 9/152 (6%) | 7/81 (9%) | 14/138 (10%) | 0/158 (0%) | 5/79 (6%) | 6/77 (8%) |
| phishing (phishing (deceptive scam)) | lie | `␣phishing` | 3/152 (2%) | 11/81 (14%) | 0/138 (0%) | 0/158 (0%) | 3/79 (4%) | 11/77 (14%) |
| confidential (confidentiality) | unclear | `␣confidentiality`, `␣Confidential` | 11/152 (7%) | 3/81 (4%) | 1/138 (1%) | 0/158 (0%) | 0/79 (0%) | 3/77 (4%) |
| doubt (doubting / challenging) | unclear | `质疑` | 7/152 (5%) | 7/81 (9%) | 36/138 (26%) | 2/158 (1%) | 7/79 (9%) | 7/77 (9%) |
| immoral (immoral) | lie | `␣immoral` | 11/152 (7%) | 2/81 (2%) | 0/138 (0%) | 0/158 (0%) | 2/79 (3%) | 2/77 (3%) |
| censorship (censorship) | unclear | `␣censorship` | 6/152 (4%) | 7/81 (9%) | 1/138 (1%) | 0/158 (0%) | 4/79 (5%) | 7/77 (9%) |
| contradiction (self-contradiction) | unclear | `␣contradictory`, `␣contradict`, `␣contradiction`, `␣contradictions`, `矛盾` | 7/152 (5%) | 6/81 (7%) | 89/138 (64%) | 0/158 (0%) | 5/79 (6%) | 5/77 (6%) |
| fact (fact, factual) | truth | `␣fact`, `␣reality`, `␣facts`, `Fact`, `fact`, `␣Actually`, `␣Fact`, `␣Reality`, `␣Facts`, `Reality`, `_fact`, `␣FACT`, `FACT`, `␣factual`, `facts`, `事实`, `实际情况`, `的事实`, `实事求是`, `事实和` | 11/152 (7%) | 2/81 (2%) | 53/138 (38%) | 0/158 (0%) | 11/79 (14%) | 2/77 (3%) |
| hoax (a hoax) | lie | `␣hoax` | 2/152 (1%) | 10/81 (12%) | 0/138 (0%) | 0/158 (0%) | 2/79 (3%) | 10/77 (13%) |
| loophole (a loophole) | unclear | `␣loophole` | 2/152 (1%) | 10/81 (12%) | 0/138 (0%) | 0/158 (0%) | 2/79 (3%) | 10/77 (13%) |
| disclose (disclosing) | truth | `␣disclosure`, `␣Disclosure` | 11/152 (7%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 1/79 (1%) | 0/77 (0%) |
| manipulate (manipulating) | lie | `␣manipulation`, `␣manipulated`, `␣manipulating`, `␣manipulate` | 3/152 (2%) | 8/81 (10%) | 0/138 (0%) | 0/158 (0%) | 3/79 (4%) | 8/77 (10%) |
| legal (legal / legality) | unclear | `␣Legal`, `␣legal`, `␣legality`, `legal`, `/legal`, `␣legally`, `Legal`, `␣legale` | 6/152 (4%) | 5/81 (6%) | 2/138 (1%) | 3/158 (2%) | 4/79 (5%) | 5/77 (6%) |
| accountability (accountability) | unclear | `␣Accountability`, `␣accountability` | 8/152 (5%) | 1/81 (1%) | 1/138 (1%) | 0/158 (0%) | 3/79 (4%) | 1/77 (1%) |
| transparency (transparency) | truth | `␣transparency`, `␣Transparency` | 5/152 (3%) | 2/81 (2%) | 0/138 (0%) | 0/158 (0%) | 1/79 (1%) | 2/77 (3%) |
| pressure (pressure) | unclear | `␣Pressure`, `␣pressure`, `␣pressures`, `␣pressured` | 5/152 (3%) | 2/81 (2%) | 0/138 (0%) | 0/158 (0%) | 5/79 (6%) | 2/77 (3%) |
| dilemma (a dilemma) | unclear | `␣dilemma` | 3/152 (2%) | 4/81 (5%) | 0/138 (0%) | 0/158 (0%) | 1/79 (1%) | 4/77 (5%) |
| blackmail (blackmail) | unclear | `␣blackmail` | 4/152 (3%) | 2/81 (2%) | 0/138 (0%) | 0/158 (0%) | 3/79 (4%) | 2/77 (3%) |
| fictional (made up, fictional) | unclear | `␣fictional`, `虚构` | 5/152 (3%) | 1/81 (1%) | 13/138 (9%) | 0/158 (0%) | 3/79 (4%) | 1/77 (1%) |
| mislead (misleading) | lie | `误导`, `␣misleading` | 3/152 (2%) | 2/81 (2%) | 3/138 (2%) | 0/158 (0%) | 2/79 (3%) | 0/77 (0%) |
| secret (secrecy) | lie | `秘密`, `␣secretly`, `␣secrecy` | 3/152 (2%) | 2/81 (2%) | 1/138 (1%) | 0/158 (0%) | 0/79 (0%) | 1/77 (1%) |
| confess (confessing / owning up) | truth | `␣confession`, `␣confess`, `␣confessed`, `坦白` | 5/152 (3%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 0/79 (0%) | 0/77 (0%) |
| bait (bait) | unclear | `␣bait` | 2/152 (1%) | 3/81 (4%) | 0/138 (0%) | 0/158 (0%) | 2/79 (3%) | 3/77 (4%) |
| hallucinate (hallucinating (making things up)) | unclear | `␣halluc` | 3/152 (2%) | 2/81 (2%) | 1/138 (1%) | 1/158 (1%) | 2/79 (3%) | 2/77 (3%) |
| conspiracy (conspiracy) | unclear | `␣conspiracy` | 1/152 (1%) | 4/81 (5%) | 0/138 (0%) | 0/158 (0%) | 1/79 (1%) | 4/77 (5%) |
| evasion (evading) | lie | `␣evasion` | 0/152 (0%) | 4/81 (5%) | 2/138 (1%) | 0/158 (0%) | 0/79 (0%) | 4/77 (5%) |
| accurate (accurate) | truth | `␣accuracy`, `␣Accuracy` | 4/152 (3%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 4/79 (5%) | 0/77 (0%) |
| pretend (pretending) | lie | `假装`, `␣pretending` | 1/152 (1%) | 2/81 (2%) | 0/138 (0%) | 0/158 (0%) | 0/79 (0%) | 2/77 (3%) |
| expose (exposing) | unclear | `揭露`, `␣exposed`, `␣expose`, `Expose`, `␣exposing`, `␣exposes`, `␣Exposure`, `Exposed`, `揭`, `暴露` | 2/152 (1%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 0/79 (0%) | 1/77 (1%) |
| threat (threatening) | unclear | `威胁` | 1/152 (1%) | 2/81 (2%) | 0/138 (0%) | 0/158 (0%) | 1/79 (1%) | 2/77 (3%) |
| assert (asserting) | unclear | `␣assertions`, `␣Assert` | 2/152 (1%) | 1/81 (1%) | 32/138 (23%) | 0/158 (0%) | 1/79 (1%) | 1/77 (1%) |
| reveal (revealing, uncovering) | truth | `␣revealed`, `揭露`, `揭` | 2/152 (1%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 0/79 (0%) | 1/77 (1%) |
| claim (claiming something is so) | unclear | `␣Claims`, `␣claim`, `␣claims`, `␣claiming`, `␣Claim`, `Claims` | 2/152 (1%) | 0/81 (0%) | 1/138 (1%) | 0/158 (0%) | 0/79 (0%) | 0/77 (0%) |
| wrong (wrong, mistaken) | lie | `错误` | 2/152 (1%) | 0/81 (0%) | 5/138 (4%) | 3/158 (2%) | 2/79 (3%) | 0/77 (0%) |
| candid (being frank / candid) | truth | `坦诚` | 1/152 (1%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 0/79 (0%) | 0/77 (0%) |
| stealth (stealth) | lie | `␣stealth`, `␣Stealth` | 0/152 (0%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 0/79 (0%) | 1/77 (1%) |
| reveal (revealing) | truth | `␣revealed` | 1/152 (1%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 0/79 (0%) | 0/77 (0%) |
| leak (leaking) | unclear | `泄露` | 0/152 (0%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 0/79 (0%) | 0/77 (0%) |
| refuse (refusing) | unclear | `␣refusing`, `␣refusal`, `拒绝` | 1/152 (1%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 0/79 (0%) | 0/77 (0%) |
| betray (betraying) | lie | `␣betrayed`, `␣betrayal` | 1/152 (1%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 0/79 (0%) | 0/77 (0%) |
| disclaimer (a disclaimer) | unclear | `␣disclaimer` | 0/152 (0%) | 1/81 (1%) | 1/138 (1%) | 0/158 (0%) | 0/79 (0%) | 1/77 (1%) |
| incorrect (incorrect) | lie | `␣incorrect`, `␣incorrectly` | 1/152 (1%) | 0/81 (0%) | 4/138 (3%) | 0/158 (0%) | 1/79 (1%) | 0/77 (0%) |
| correct (correct) | truth | `␣correct`, `␣correctly`, `正确` | 0/152 (0%) | 0/81 (0%) | 2/138 (1%) | 0/158 (0%) | 0/79 (0%) | 0/77 (0%) |

Not in the draft: admit (excluded: admit / deny / acknowledge); acknowledge (excluded: admit / deny / acknowledge); deny (excluded: admit / deny / acknowledge); jailbreak (held back: no undisputed member left); true (excluded: the question's own word); truth (excluded: the question's own word)
