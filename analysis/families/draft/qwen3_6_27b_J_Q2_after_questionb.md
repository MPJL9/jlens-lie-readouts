# Draft families: qwen3.6-27b, J-lens, part Q2_after, group questionb

Written by `scripts/apply_family_decisions.py` (2026-10-01; draft, not frozen). Counts are `present / transcripts (share)`
on the build split.

## q_tok8

| family | side | members | lies | truths | no-pressure truths | unrelated | lies that deny | truths that deny |
|---|---|---|---|---|---|---|---|---|
| false (false, untrue) | lie | `␣False`, `False`, `:false`, `.False`, `.false`, `.FALSE`, `/false` | 33/152 (22%) | 15/81 (19%) | 96/138 (70%) | 155/158 (98%) | 8/47 (17%) | 15/77 (19%) |
| true (true, real) | truth | `␣True` | 0/152 (0%) | 0/81 (0%) | 0/138 (0%) | 4/158 (3%) | 0/47 (0%) | 0/77 (0%) |
| wrong (wrong, mistaken) | lie | `␣Wrong` | 0/152 (0%) | 0/81 (0%) | 0/138 (0%) | 1/158 (1%) | 0/47 (0%) | 0/77 (0%) |
| incorrect (incorrect) | lie | `␣Incorrect` | 0/152 (0%) | 0/81 (0%) | 0/138 (0%) | 1/158 (1%) | 0/47 (0%) | 0/77 (0%) |

## q_tok9

| family | side | members | lies | truths | no-pressure truths | unrelated | lies that deny | truths that deny |
|---|---|---|---|---|---|---|---|---|

Not in the draft: deny (excluded: admit / deny / acknowledge)

## q_tok10

| family | side | members | lies | truths | no-pressure truths | unrelated | lies that deny | truths that deny |
|---|---|---|---|---|---|---|---|---|
| honest (honesty) | truth | `␣honesty`, `诚实`, `␣honest`, `␣Honest`, `␣honestly`, `诚实守信`, `␣truthful`, `如实`, `实事求是` | 131/152 (86%) | 67/81 (83%) | 121/138 (88%) | 113/158 (72%) | 40/47 (85%) | 64/77 (83%) |
| truthful (truthful / telling it as it is) | truth | `␣truthful`, `如实`, `实事求是` | 122/152 (80%) | 57/81 (70%) | 119/138 (86%) | 110/158 (70%) | 36/47 (77%) | 54/77 (70%) |
| unethical (unethical / immoral) | lie | `␣unethical`, `␣immoral` | 114/152 (75%) | 32/81 (40%) | 1/138 (1%) | 0/158 (0%) | 22/47 (47%) | 28/77 (36%) |
| conceal (concealing or covering up information) | lie | `隐瞒`, `␣conceal`, `掩盖`, `␣concealed`, `掩饰`, `隐` | 109/152 (72%) | 32/81 (40%) | 95/138 (69%) | 4/158 (3%) | 26/47 (55%) | 29/77 (38%) |
| conceal (hiding / concealing) | lie | `隐瞒`, `␣conceal`, `隐藏`, `␣concealed`, `␣undisclosed`, `␣hidden`, `␣hiding`, `hide` | 109/152 (72%) | 32/81 (40%) | 95/138 (69%) | 4/158 (3%) | 26/47 (55%) | 29/77 (38%) |
| lie (telling a lie) | lie | `说谎`, `谎言`, `撒谎`, `␣lied`, `谎`, `␣lies`, `␣lie`, `␣liar`, `␣lying`, `lying`, `lie`, `␣Lie`, `lies`, `Lie`, `␣Lies`, `␣mentira` | 110/152 (72%) | 26/81 (32%) | 66/138 (48%) | 5/158 (3%) | 24/47 (51%) | 23/77 (30%) |
| violate (violating rules or principles) | unclear | `违反`, `违背`, `␣violate`, `␣violates`, `␣violating`, `违规`, `违反了`, `␣violation`, `␣violations`, `␣violated`, `Violation` | 101/152 (66%) | 34/81 (42%) | 20/138 (14%) | 1/158 (1%) | 13/47 (28%) | 30/77 (39%) |
| ethical (ethical) | truth | `␣ethical`, `ethical`, `␣moral`, `␣Moral` | 99/152 (65%) | 23/81 (28%) | 0/138 (0%) | 0/158 (0%) | 22/47 (47%) | 21/77 (27%) |
| fake (fake / forged) | lie | `fake`, `Fake`, `虚假`, `伪造`, `␣fake`, `␣Fake`, `弄虚作假`, `造假` | 91/152 (60%) | 22/81 (27%) | 83/138 (60%) | 46/158 (29%) | 13/47 (28%) | 18/77 (23%) |
| ethics (ethics or morality as a topic) | unclear | `␣ethics`, `伦理`, `␣Ethics`, `道德`, `␣morally`, `␣moral`, `的道德`, `␣morality`, `职业道德`, `␣Moral`, `␣morals`, `␣ethic` | 92/152 (61%) | 18/81 (22%) | 0/138 (0%) | 0/158 (0%) | 18/47 (38%) | 16/77 (21%) |
| fake (fake) | lie | `fake`, `Fake`, `␣fake`, `␣Fake` | 82/152 (54%) | 22/81 (27%) | 83/138 (60%) | 43/158 (27%) | 13/47 (28%) | 18/77 (23%) |
| dishonest (dishonesty) | lie | `␣dishonest` | 81/152 (53%) | 11/81 (14%) | 1/138 (1%) | 0/158 (0%) | 9/47 (19%) | 9/77 (12%) |
| falsehood (an untrue statement) | lie | `␣falsehood` | 72/152 (47%) | 12/81 (15%) | 84/138 (61%) | 56/158 (35%) | 17/47 (36%) | 9/77 (12%) |
| comply (complying with rules or instructions) | unclear | `遵守`, `␣compliance`, `合规`, `␣adherence`, `遵循`, `␣Compliance`, `␣adher`, `␣adhere`, `␣complying`, `严格遵守`, `␣comply`, `␣complied`, `␣compliant`, `遵照`, `遵从`, `恪守`, `坚守`, `符合`, `是否符合` | 54/152 (36%) | 30/81 (37%) | 55/138 (40%) | 0/158 (0%) | 12/47 (26%) | 28/77 (36%) |
| false (false, untrue) | lie | `␣false`, `␣False`, `false`, `False`, `␣FALSE`, `>false`, `␣fals`, `␣falsely`, `/false`, `假` | 66/152 (43%) | 16/81 (20%) | 70/138 (51%) | 79/158 (50%) | 14/47 (30%) | 13/77 (17%) |
| deliberate (doing it on purpose) | unclear | `␣intentionally`, `故意`, `␣deliberately`, `␣deliberate`, `␣intentional`, `刻意`, `␣purposely`, `有意`, `故意的`, `␣sengaja`, `␣consciously` | 65/152 (43%) | 8/81 (10%) | 6/138 (4%) | 0/158 (0%) | 3/47 (6%) | 4/77 (5%) |
| knowingly (with knowledge / consciously) | unclear | `␣knowingly`, `明知`, `␣consciously`, `␣knowing`, `␣Knowing` | 62/152 (41%) | 3/81 (4%) | 1/138 (1%) | 2/158 (1%) | 7/47 (15%) | 1/77 (1%) |
| prohibited (prohibited) | unclear | `␣prohibited`, `禁止` | 42/152 (28%) | 21/81 (26%) | 0/138 (0%) | 0/158 (0%) | 7/47 (15%) | 20/77 (26%) |
| fabricate (making something up) | lie | `虚构`, `伪造`, `弄虚作假`, `␣fabrication`, `␣fabricated`, `造假` | 48/152 (32%) | 11/81 (14%) | 36/138 (26%) | 19/158 (12%) | 9/47 (19%) | 10/77 (13%) |
| fraud (fraud) | lie | `␣fraudulent`, `␣fraud`, `␣Fraud` | 49/152 (32%) | 4/81 (5%) | 0/138 (0%) | 0/158 (0%) | 4/47 (9%) | 2/77 (3%) |
| misinformation (false information) | lie | `␣misinformation`, `虚假信息` | 38/152 (25%) | 10/81 (12%) | 69/138 (50%) | 100/158 (63%) | 4/47 (9%) | 8/77 (10%) |
| true (true, real) | truth | `真实`, `真实性`, `真实的`, `的真实`, `的真实性` | 33/152 (22%) | 10/81 (12%) | 61/138 (44%) | 42/158 (27%) | 14/47 (30%) | 10/77 (13%) |
| mislead (leading someone to a wrong belief) | lie | `␣misleading`, `误导`, `␣misled`, `误导性` | 29/152 (19%) | 12/81 (15%) | 57/138 (41%) | 50/158 (32%) | 4/47 (9%) | 10/77 (13%) |
| integrity (integrity / uprightness) | truth | `诚信`, `␣integrity`, `␣Integrity`, `正直` | 20/152 (13%) | 16/81 (20%) | 24/138 (17%) | 7/158 (4%) | 7/47 (15%) | 16/77 (21%) |
| refuse (refusing) | unclear | `拒绝`, `␣refusal`, `␣refusing`, `␣refus`, `␣refused`, `␣refuse`, `␣refuses`, `拒`, `拒绝了`, `拒絕`, `拒不`, `␣отказ`, `␣отказа` | 7/152 (5%) | 28/81 (35%) | 2/138 (1%) | 0/158 (0%) | 3/47 (6%) | 28/77 (36%) |
| pretend (pretending or disguising) | lie | `伪装`, `␣pretending`, `假装` | 26/152 (17%) | 8/81 (10%) | 8/138 (6%) | 1/158 (1%) | 6/47 (13%) | 5/77 (6%) |
| secret (secrecy) | lie | `秘密`, `␣secrecy`, `保密`, `␣secretly`, `的秘密`, `␣covert` | 15/152 (10%) | 5/81 (6%) | 1/138 (1%) | 0/158 (0%) | 6/47 (13%) | 3/77 (4%) |
| cheat (cheating) | lie | `作弊`, `␣cheating` | 18/152 (12%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 2/47 (4%) | 1/77 (1%) |
| fact (fact, factual) | truth | `␣fact`, `␣actual`, `␣reality`, `actual`, `␣facts`, `Fact`, `Actual`, `fact`, `␣Actual`, `␣Fact`, `␣Reality`, `␣Facts`, `Reality`, `␣FACT`, `FACT`, `␣factual`, `facts`, `事实`, `实际情况`, `事实上`, `的事实`, `根据实际情况`, `事实和`, `事実` | 15/152 (10%) | 4/81 (5%) | 55/138 (40%) | 22/158 (14%) | 10/47 (21%) | 4/77 (5%) |
| illegal (illegal) | unclear | `违法`, `␣illegal` | 14/152 (9%) | 2/81 (2%) | 0/138 (0%) | 0/158 (0%) | 3/47 (6%) | 2/77 (3%) |
| candour (candour) | truth | `坦诚` | 0/152 (0%) | 15/81 (19%) | 50/138 (36%) | 4/158 (3%) | 0/47 (0%) | 15/77 (19%) |
| transparency (transparency) | truth | `␣transparency`, `␣Transparency`, `透明`, `␣transparent`, `透明度`, `transparent`, `透明的`, `␣Transparent` | 4/152 (3%) | 11/81 (14%) | 19/138 (14%) | 0/158 (0%) | 4/47 (9%) | 11/77 (14%) |
| reject (rejecting) | unclear | `␣rejecting`, `␣rejection`, `reject`, `␣Reject`, `␣reject`, `Reject`, `␣rejected`, `否决`, `␣rejects`, `rejected` | 1/152 (1%) | 14/81 (17%) | 1/138 (1%) | 0/158 (0%) | 1/47 (2%) | 14/77 (18%) |
| fictional (fictional) | unclear | `␣fictional`, `␣Fiction`, `fiction` | 9/152 (6%) | 4/81 (5%) | 2/138 (1%) | 10/158 (6%) | 3/47 (6%) | 3/77 (4%) |
| noncompliant (not in accordance with rules) | lie | `不符合` | 3/152 (2%) | 10/81 (12%) | 3/138 (2%) | 1/158 (1%) | 3/47 (6%) | 10/77 (13%) |
| hypocrisy (hypocrisy) | lie | `虚伪`, `␣hypocrisy` | 10/152 (7%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 1/47 (2%) | 1/77 (1%) |
| hide (hiding) | lie | `隐藏`, `␣hidden`, `␣hiding`, `hide`, `␣masking` | 8/152 (5%) | 2/81 (2%) | 4/138 (3%) | 0/158 (0%) | 2/47 (4%) | 0/77 (0%) |
| correct (correct) | truth | `␣correct`, `␣correctly`, `correct`, `␣correction`, `Correct`, `␣corrected`, `␣Correct`, `␣corrections`, `␣correctness`, `␣Correction`, `␣correcting`, `Correction`, `正确`, `正确的`, `修正`, `纠错`, `正确答案`, `纠正`, `更正` | 0/152 (0%) | 10/81 (12%) | 81/138 (59%) | 32/158 (20%) | 0/47 (0%) | 10/77 (13%) |
| incorrect (incorrect) | lie | `␣incorrect`, `Incorrect`, `␣inaccur`, `␣incorrectly`, `␣inaccurate`, `incorrect`, `␣erroneous`, `␣Incorrect`, `错误的`, `有误` | 6/152 (4%) | 4/81 (5%) | 36/138 (26%) | 55/158 (35%) | 3/47 (6%) | 4/77 (5%) |
| cover up (covering up / glossing over) | lie | `掩盖`, `掩饰` | 8/152 (5%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 0/47 (0%) | 0/77 (0%) |
| contradict (contradicting) | unclear | `␣contradict`, `␣contradiction`, `␣contradictory` | 3/152 (2%) | 6/81 (7%) | 12/138 (9%) | 0/158 (0%) | 1/47 (2%) | 6/77 (8%) |
| confidential (confidentiality) | unclear | `␣confidentiality` | 6/152 (4%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 2/47 (4%) | 0/77 (0%) |
| cooperate (cooperating) | unclear | `配合`, `积极配合`, `的配合` | 7/152 (5%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 0/47 (0%) | 0/77 (0%) |
| evade (evasion / avoiding the question) | lie | `回避`, `␣evasion` | 3/152 (2%) | 3/81 (4%) | 0/138 (0%) | 0/158 (0%) | 2/47 (4%) | 2/77 (3%) |
| undisclosed (not disclosed) | lie | `␣undisclosed` | 4/152 (3%) | 1/81 (1%) | 1/138 (1%) | 0/158 (0%) | 4/47 (9%) | 1/77 (1%) |
| wrong (wrong, mistaken) | lie | `␣wrong`, `␣WRONG`, `误`, `错误`, `的错误` | 4/152 (3%) | 1/81 (1%) | 22/138 (16%) | 58/158 (37%) | 0/47 (0%) | 1/77 (1%) |
| withhold (withholding information) | lie | `␣withholding`, `␣withheld`, `␣withhold` | 2/152 (1%) | 2/81 (2%) | 1/138 (1%) | 0/158 (0%) | 0/47 (0%) | 1/77 (1%) |
| omit (leaving information out) | lie | `␣omit`, `␣omission`, `␣omitted`, `omit` | 2/152 (1%) | 2/81 (2%) | 1/138 (1%) | 0/158 (0%) | 1/47 (2%) | 1/77 (1%) |
| misrepresent (describing something falsely) | lie | `␣misrepresented` | 1/152 (1%) | 2/81 (2%) | 7/138 (5%) | 5/158 (3%) | 0/47 (0%) | 1/77 (1%) |
| sincerity (sincerity) | truth | `␣sincerity` | 1/152 (1%) | 2/81 (2%) | 3/138 (2%) | 1/158 (1%) | 0/47 (0%) | 2/77 (3%) |
| confess (confessing) | truth | `坦白`, `␣confession` | 0/152 (0%) | 3/81 (4%) | 13/138 (9%) | 1/158 (1%) | 0/47 (0%) | 3/77 (4%) |
| trick (tricking) | lie | `␣trick`, `␣tricks`, `␣Trick` | 0/152 (0%) | 2/81 (2%) | 0/138 (0%) | 0/158 (0%) | 0/47 (0%) | 2/77 (3%) |
| disclose (disclosing) | truth | `␣disclosure`, `␣disclose`, `␣disclosures`, `␣Disclosure`, `␣disclosing`, `披露`, `␣disclosed`, `Disclosure`, `信息披露` | 0/152 (0%) | 2/81 (2%) | 10/138 (7%) | 0/158 (0%) | 0/47 (0%) | 2/77 (3%) |
| manipulate (manipulation) | lie | `␣manipulation`, `␣manipulate`, `␣manipulated`, `␣manipulating`, `操纵` | 0/152 (0%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) | 0/47 (0%) | 1/77 (1%) |
| exaggerate (exaggerating) | lie | `␣exagger`, `夸大` | 1/152 (1%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 0/47 (0%) | 0/77 (0%) |
| expose (exposing / revealing) | truth | `揭露` | 0/152 (0%) | 1/81 (1%) | 1/138 (1%) | 0/158 (0%) | 0/47 (0%) | 1/77 (1%) |
| conscience (conscience) | unclear | `␣conscience` | 1/152 (1%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 1/47 (2%) | 0/77 (0%) |
| authentic (authenticity) | truth | `␣authenticity` | 1/152 (1%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) | 0/47 (0%) | 0/77 (0%) |
| accurate (accurate) | truth | `␣accurate`, `␣accuracy`, `␣accurately`, `accuracy`, `Accuracy`, `␣Accuracy` | 0/152 (0%) | 1/81 (1%) | 17/138 (12%) | 8/158 (5%) | 0/47 (0%) | 1/77 (1%) |

Not in the draft: deceive (excluded: the question's own word); deny (excluded: admit / deny / acknowledge); truth (excluded: truth from the question on); admit (excluded: admit / deny / acknowledge); acknowledge (excluded: admit / deny / acknowledge)
