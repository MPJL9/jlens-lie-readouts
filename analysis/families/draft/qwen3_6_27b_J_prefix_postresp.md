# Draft families: qwen3.6-27b, J-lens, part prefix, group postresp

Written by `scripts/apply_family_decisions.py` (2026-10-01; draft, not frozen). Counts are `present / transcripts (share)`
on the build split.

## postresp_slot0

| family | side | members | lies | truths | no-pressure truths | unrelated |
|---|---|---|---|---|---|---|
| conceal (to conceal, to hide) | lie | `藏`, `掩` | 1/152 (1%) | 0/81 (0%) | 0/138 (0%) | 1/158 (1%) |
| true (true, real) | truth | `真` | 0/152 (0%) | 0/81 (0%) | 0/138 (0%) | 2/158 (1%) |

## postresp_slot1

| family | side | members | lies | truths | no-pressure truths | unrelated |
|---|---|---|---|---|---|---|
| truthful (telling the truth as it is) | truth | `␣truthful`, `如实`, `实话`, `实事求是`, `说实话` | 101/152 (66%) | 46/81 (57%) | 59/138 (43%) | 0/158 (0%) |
| truth (the truth) | truth | `真相`, `␣truth`, `truth`, `␣Truth`, `Truth`, `␣truths`, `_truth`, `.truth`, `真理`, `实话`, `说实话`, `␣verità`, `␣vérité` | 102/152 (67%) | 45/81 (56%) | 61/138 (44%) | 0/158 (0%) |
| lie (telling a lie / a lie) | lie | `谎言`, `说谎`, `撒谎`, `谎`, `␣lied`, `␣lie`, `␣lies`, `␣mentira`, `␣거짓`, `␣lying`, `␣Lie`, `␣Lies`, `lie`, `Lie`, `lies`, `lying`, `␣liar` | 127/152 (84%) | 7/81 (9%) | 0/138 (0%) | 0/158 (0%) |
| conceal (hiding / concealing something) | lie | `隐瞒`, `掩盖`, `瞒` | 109/152 (72%) | 17/81 (21%) | 2/138 (1%) | 0/158 (0%) |
| fake (fake, not genuine) | lie | `fake`, `Fake`, `␣fake`, `␣Fake`, `假`, `假的`, `.fake`, `_fake`, `虚假` | 117/152 (77%) | 5/81 (6%) | 0/138 (0%) | 0/158 (0%) |
| misinformation (false information) | lie | `␣misinformation`, `虚假信息` | 101/152 (66%) | 7/81 (9%) | 10/138 (7%) | 0/158 (0%) |
| deceive (the act of deceiving) | lie | `欺骗`, `␣deception`, `␣deceptive`, `骗`, `␣deceive`, `␣deceit`, `␣deceived` | 94/152 (62%) | 5/81 (6%) | 0/138 (0%) | 0/158 (0%) |
| falsehood (a falsehood (an untrue statement)) | lie | `␣falsehood` | 89/152 (59%) | 0/81 (0%) | 2/138 (1%) | 0/158 (0%) |
| fabricate (making up or forging content) | lie | `伪造`, `虚构`, `造假`, `␣fabricated`, `弄虚作假` | 83/152 (55%) | 1/81 (1%) | 1/138 (1%) | 0/158 (0%) |
| false (false, untrue) | lie | `␣false`, `␣False`, `false`, `False`, `␣FALSE`, `FALSE`, `>false`, `␣fals`, `␣falsely`, `␣untrue`, `/false`, `真假` | 79/152 (52%) | 2/81 (2%) | 1/138 (1%) | 0/158 (0%) |
| refuse (refusing) | unclear | `拒绝`, `␣refusal`, `␣refus`, `拒`, `␣refusing`, `␣refused`, `␣refuses`, `␣refuse`, `拒绝了`, `拒絕`, `␣отказ`, `拒不`, `␣отказа` | 26/152 (17%) | 44/81 (54%) | 9/138 (7%) | 0/158 (0%) |
| mislead (leading someone to a wrong belief) | lie | `␣misleading`, `误导`, `␣misled`, `误导性` | 61/152 (40%) | 6/81 (7%) | 2/138 (1%) | 0/158 (0%) |
| disclaimer (issuing a disclaimer) | unclear | `␣disclaimer`, `␣Disclaimer`, `␣DISCLAIMER`, `Disclaimer` | 22/152 (14%) | 32/81 (40%) | 15/138 (11%) | 3/158 (2%) |
| honest (honesty) | truth | `␣honesty`, `诚实`, `␣honest`, `坦诚`, `␣honestly`, `␣Honest`, `诚信`, `正直`, `诚实守信`, `真诚` | 9/152 (6%) | 43/81 (53%) | 40/138 (29%) | 1/158 (1%) |
| rebut (rebutting / refuting a claim) | unclear | `反驳`, `␣rebut`, `␣refute`, `␣debunk` | 31/152 (20%) | 11/81 (14%) | 12/138 (9%) | 0/158 (0%) |
| reject (rejecting) | unclear | `reject`, `␣rejection`, `␣rejecting`, `Reject`, `␣Reject`, `␣reject`, `␣rejected`, `.reject`, `rejected` | 11/152 (7%) | 29/81 (36%) | 1/138 (1%) | 0/158 (0%) |
| dishonest (not honest) | lie | `␣dishonest` | 35/152 (23%) | 4/81 (5%) | 0/138 (0%) | 0/158 (0%) |
| contradict (contradicting) | unclear | `␣contradict`, `␣contrad`, `␣contradiction`, `␣contradictory`, `矛盾`, `␣contradictions` | 23/152 (15%) | 12/81 (15%) | 13/138 (9%) | 0/158 (0%) |
| excuse (making excuses) | unclear | `␣excuse`, `␣excuses`, `借口`, `辩解` | 33/152 (22%) | 2/81 (2%) | 3/138 (2%) | 0/158 (0%) |
| candid (being candid) | truth | `坦诚` | 1/152 (1%) | 34/81 (42%) | 19/138 (14%) | 0/158 (0%) |
| disclose (disclosing / revealing) | truth | `␣disclosure`, `␣Disclosure`, `␣disclosing`, `公开`, `␣disclose`, `␣disclosures`, `披露`, `揭露`, `␣disclosed`, `Disclosure`, `信息公开`, `信息披露`, `公开的`, `␣revealing` | 1/152 (1%) | 26/81 (32%) | 20/138 (14%) | 0/158 (0%) |
| evade (evading the question) | lie | `回避`, `␣evasion`, `避开`, `␣dodge`, `␣evade`, `规避`, `逃避`, `␣deflect` | 18/152 (12%) | 6/81 (7%) | 0/138 (0%) | 0/158 (0%) |
| confess (confessing) | truth | `坦白`, `␣confession`, `␣confess`, `␣confessed` | 0/152 (0%) | 24/81 (30%) | 5/138 (4%) | 0/158 (0%) |
| ethics (ethics, moral standards) | unclear | `道德`, `␣ethical`, `ethical`, `伦理`, `␣ethics`, `␣Ethics`, `的道德` | 0/152 (0%) | 24/81 (30%) | 0/138 (0%) | 0/158 (0%) |
| unethical (morally wrong) | lie | `␣unethical` | 4/152 (3%) | 19/81 (23%) | 0/138 (0%) | 0/158 (0%) |
| violate (violating a rule or principle) | unclear | `违背`, `违反`, `违反了`, `违法` | 11/152 (7%) | 12/81 (15%) | 1/138 (1%) | 0/158 (0%) |
| liar (a person who lies) | lie | `␣liar` | 22/152 (14%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) |
| misrepresent (presenting something inaccurately) | lie | `␣misrepresented` | 20/152 (13%) | 2/81 (2%) | 0/138 (0%) | 0/158 (0%) |
| transparent (transparency) | truth | `␣transparency`, `透明`, `␣Transparency`, `透明度`, `␣transparent`, `透明的`, `transparent` | 0/152 (0%) | 21/81 (26%) | 7/138 (5%) | 0/158 (0%) |
| ethical (ethical) | truth | `␣ethical`, `ethical` | 0/152 (0%) | 21/81 (26%) | 0/138 (0%) | 0/158 (0%) |
| wrong (wrong, mistaken) | lie | `␣wrong`, `␣ERROR`, `wrong`, `␣Wrong`, `␣WRONG`, `错`, `误`, `错误`, `的错误`, `是错误的` | 11/152 (7%) | 7/81 (9%) | 6/138 (4%) | 4/158 (3%) |
| incorrect (incorrect) | lie | `␣incorrect`, `Wrong`, `Incorrect`, `␣inaccur`, `␣incorrectly`, `␣inaccurate`, `incorrect`, `␣wrongly`, `␣Incorrect`, `错误的`, `不符合`, `有误` | 11/152 (7%) | 7/81 (9%) | 8/138 (6%) | 3/158 (2%) |
| vague (being vague) | unclear | `␣vague`, `含糊`, `␣vaguely` | 13/152 (9%) | 4/81 (5%) | 0/138 (0%) | 0/158 (0%) |
| vague (being vague or ambiguous) | lie | `␣vague`, `含糊`, `␣ambiguous`, `␣ambiguity`, `␣vaguely`, `␣ambigu`, `ambiguous` | 13/152 (9%) | 4/81 (5%) | 0/138 (0%) | 0/158 (0%) |
| integrity (integrity) | truth | `诚信`, `正直`, `␣integrity`, `␣Integrity` | 2/152 (1%) | 15/81 (19%) | 2/138 (1%) | 1/158 (1%) |
| dismiss (dismissing) | unclear | `␣dismiss`, `␣dismissing`, `␣dismissal`, `-dismiss`, `␣dismissed`, `dismiss`, `.dismiss`, `Dismiss` | 14/152 (9%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) |
| spin (spinning the facts) | lie | `␣spin`, `spin`, `Spin`, `␣spun`, `-spin`, `␣Spin`, `␣spins`, `␣spinning`, `_spin` | 13/152 (9%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) |
| justify (justifying oneself) | unclear | `辩解` | 12/152 (8%) | 1/81 (1%) | 3/138 (2%) | 0/158 (0%) |
| bluff (bluffing) | lie | `␣bluff` | 12/152 (8%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) |
| ignore (ignoring) | unclear | `␣ignoring`, `忽略`, `ignore`, `␣ignores`, `␣IGNORE`, `␣ignore`, `␣ignored`, `Ignore`, `ignored`, `␣Ignore`, `忽略了`, `.ignore` | 8/152 (5%) | 2/81 (2%) | 0/138 (0%) | 0/158 (0%) |
| fraud (fraud, scam) | lie | `骗局`, `␣fraudulent`, `欺诈` | 9/152 (6%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) |
| blame (blaming) | unclear | `␣blame`, `␣blames`, `␣blamed` | 9/152 (6%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) |
| clarify (clarifying) | unclear | `澄清`, `␣clarification` | 6/152 (4%) | 2/81 (2%) | 12/138 (9%) | 0/158 (0%) |
| avoid (avoiding) | unclear | `␣avoidance`, `avoid`, `␣avoided`, `␣Avoid`, `␣avoiding`, `␣avoids`, `␣avoid`, `Avoid`, `避免` | 6/152 (4%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) |
| whistleblow (whistleblowing) | unclear | `␣whistlebl`, `␣whistleblower` | 0/152 (0%) | 7/81 (9%) | 0/138 (0%) | 0/158 (0%) |
| fact (fact, factual) | truth | `␣fact`, `␣actual`, `␣reality`, `actual`, `␣facts`, `Fact`, `Actual`, `fact`, `␣Actual`, `␣Fact`, `␣Reality`, `␣Facts`, `Reality`, `_fact`, `Actually`, `␣FACT`, `FACT`, `␣factual`, `facts`, `实际`, `事实`, `实际情况`, `的事实`, `的实际`, `实际的`, `但实际上`, `事实和`, `␣réalité` | 4/152 (3%) | 3/81 (4%) | 56/138 (41%) | 2/158 (1%) |
| correct (correct) | truth | `␣correct`, `␣correctly`, `correct`, `␣correction`, `Correct`, `␣corrected`, `␣Correct`, `␣corrections`, `␣Correction`, `␣correcting`, `Correction`, `␣Corrections`, `␣corrective`, `正确`, `正确的`, `修正`, `纠错`, `正确答案`, `纠正`, `改正`, `的正确`, `更正`, `是正确的` | 4/152 (3%) | 3/81 (4%) | 28/138 (20%) | 5/158 (3%) |
| confidential (confidentiality) | unclear | `␣confidentiality`, `保密`, `␣confidential`, `秘密`, `␣undisclosed` | 3/152 (2%) | 3/81 (4%) | 1/138 (1%) | 0/158 (0%) |
| redirect (redirecting the conversation) | unclear | `redirect`, `␣redirect`, `Redirect`, `␣Redirect`, `␣redirected`, `␣redirects`, `_redirect`, `␣redirection` | 4/152 (3%) | 2/81 (2%) | 0/138 (0%) | 0/158 (0%) |
| fiction (fictional, made-up story) | unclear | `␣fictional`, `fiction`, `␣Fiction` | 5/152 (3%) | 0/81 (0%) | 1/138 (1%) | 1/158 (1%) |
| pretend (pretending) | lie | `␣pretending`, `␣pretend` | 5/152 (3%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) |
| apologize (apologizing) | unclear | `␣apology`, `␣apologies`, `道歉` | 3/152 (2%) | 0/81 (0%) | 9/138 (7%) | 0/158 (0%) |
| secret (secret, secrecy) | lie | `秘密` | 2/152 (1%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) |
| hidden (being hidden / undisclosed) | lie | `␣undisclosed` | 0/152 (0%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) |
| omit (leaving information out) | lie | `␣omit` | 1/152 (1%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) |
| sincere (sincerity) | truth | `真诚` | 0/152 (0%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) |
| true (true, real) | truth | `␣TRUE`, `真实`, `真实性`, `确实`, `真实的`, `的真实`, `的真实性` | 0/152 (0%) | 1/81 (1%) | 2/138 (1%) | 0/158 (0%) |
| accurate (accurate) | truth | `␣accurate`, `␣accuracy`, `␣accurately`, `accuracy`, `accur`, `Accuracy`, `␣Accuracy`, `准确`, `准确的` | 1/152 (1%) | 0/81 (0%) | 4/138 (3%) | 0/158 (0%) |
| inaccurate (inaccurate) | lie | `不准确` | 0/152 (0%) | 0/81 (0%) | 1/138 (1%) | 0/158 (0%) |

Not in the draft: deny (excluded: admit / deny / acknowledge); admit (excluded: admit / deny / acknowledge); acknowledge (excluded: admit / deny / acknowledge)

## postresp_slot2

| family | side | members | lies | truths | no-pressure truths | unrelated |
|---|---|---|---|---|---|---|
| wrong (wrong, mistaken) | lie | `rong`, `错误` | 0/152 (0%) | 1/81 (1%) | 4/138 (3%) | 0/158 (0%) |
| correct (correct) | truth | `修正` | 0/152 (0%) | 0/81 (0%) | 0/138 (0%) | 1/158 (1%) |

## postresp_slot3

| family | side | members | lies | truths | no-pressure truths | unrelated |
|---|---|---|---|---|---|---|
| clarify (clarifying) | unclear | `澄清`, `␣clarify` | 2/152 (1%) | 11/81 (14%) | 36/138 (26%) | 8/158 (5%) |
| apologize (apologizing) | unclear | `␣Sorry`, `Sorry` | 1/152 (1%) | 1/81 (1%) | 0/138 (0%) | 1/158 (1%) |
| refuse (refusing) | unclear | `␣refusing` | 0/152 (0%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) |
| wrong (wrong, mistaken) | lie | `␣WRONG`, `错` | 0/152 (0%) | 1/81 (1%) | 0/138 (0%) | 3/158 (2%) |
| correct (correct) | truth | `correct`, `␣correction`, `␣corrections`, `␣Correction`, `␣correcting`, `_correction`, `Correction`, `修正`, `纠正`, `改正`, `更正` | 0/152 (0%) | 0/81 (0%) | 0/138 (0%) | 7/158 (4%) |
| incorrect (incorrect) | lie | `Wrong`, `incorrect` | 0/152 (0%) | 0/81 (0%) | 0/138 (0%) | 3/158 (2%) |
| true (true, real) | truth | `真` | 0/152 (0%) | 0/81 (0%) | 0/138 (0%) | 1/158 (1%) |
| false (false, untrue) | lie | `假` | 0/152 (0%) | 0/81 (0%) | 0/138 (0%) | 2/158 (1%) |

Not in the draft: acknowledge (excluded: admit / deny / acknowledge)

## postresp_slot4

| family | side | members | lies | truths | no-pressure truths | unrelated |
|---|---|---|---|---|---|---|
| misinformation (false information) | lie | `␣misinformation`, `虚假信息` | 47/152 (31%) | 23/81 (28%) | 89/138 (64%) | 1/158 (1%) |
| truth (the truth) | truth | `真相`, `␣truth`, `truth`, `Truth`, `␣Truth`, `␣truths`, `真理`, `实话`, `_truth` | 42/152 (28%) | 7/81 (9%) | 84/138 (61%) | 0/158 (0%) |
| fake (fake, not genuine) | lie | `fake`, `␣fake`, `Fake`, `␣Fake`, `假`, `假的`, `虚假` | 18/152 (12%) | 25/81 (31%) | 25/138 (18%) | 0/158 (0%) |
| fabricate (making up or forging content) | lie | `虚构`, `伪造`, `造假`, `弄虚作假` | 9/152 (6%) | 22/81 (27%) | 31/138 (22%) | 2/158 (1%) |
| unethical (morally wrong) | lie | `␣unethical` | 8/152 (5%) | 22/81 (27%) | 7/138 (5%) | 0/158 (0%) |
| truthful (telling the truth as it is) | truth | `␣truthful`, `实事求是`, `实话`, `如实` | 21/152 (14%) | 4/81 (5%) | 72/138 (52%) | 0/158 (0%) |
| honest (honesty) | truth | `␣honesty`, `␣honestly`, `诚信`, `␣honest`, `诚实`, `坦诚`, `␣Honestly` | 16/152 (11%) | 8/81 (10%) | 7/138 (5%) | 0/158 (0%) |
| fiction (fictional, made-up story) | unclear | `␣fictional`, `fiction`, `␣Fiction`, `␣fiction`, `-fiction` | 3/152 (2%) | 19/81 (23%) | 22/138 (16%) | 8/158 (5%) |
| violate (violating a rule or principle) | unclear | `违规`, `违反`, `违背`, `违法`, `违反了` | 2/152 (1%) | 15/81 (19%) | 7/138 (5%) | 0/158 (0%) |
| mislead (leading someone to a wrong belief) | lie | `误导`, `␣misleading`, `␣misled`, `误导性` | 10/152 (7%) | 6/81 (7%) | 13/138 (9%) | 0/158 (0%) |
| rebut (rebutting / refuting a claim) | unclear | `反驳`, `␣debunk` | 12/152 (8%) | 4/81 (5%) | 2/138 (1%) | 2/158 (1%) |
| ethics (ethics, moral standards) | unclear | `␣ethical`, `␣ethics`, `ethical`, `␣Ethics`, `道德`, `伦理`, `职业道德`, `的道德`, `␣ethic` | 4/152 (3%) | 12/81 (15%) | 4/138 (3%) | 2/158 (1%) |
| secret (secret, secrecy) | lie | `␣secretly`, `秘密`, `的秘密`, `␣secret`, `␣Secret`, `Secret`, `secret`, `.secret`, `-secret`, `␣secretive`, `␣confidentiality`, `保密`, `␣confidential`, `␣undisclosed` | 8/152 (5%) | 7/81 (9%) | 11/138 (8%) | 0/158 (0%) |
| contradict (contradicting) | unclear | `␣contradict`, `矛盾`, `␣contradictory`, `␣contradiction`, `␣contradictions` | 9/152 (6%) | 6/81 (7%) | 17/138 (12%) | 0/158 (0%) |
| ethical (ethical) | truth | `␣ethical`, `ethical` | 4/152 (3%) | 11/81 (14%) | 4/138 (3%) | 2/158 (1%) |
| whistleblow (whistleblowing) | unclear | `␣whistleblower`, `␣whistlebl` | 10/152 (7%) | 5/81 (6%) | 2/138 (1%) | 0/158 (0%) |
| deceive (the act of deceiving) | lie | `欺骗`, `␣deception`, `␣deceptive`, `␣deceive`, `骗`, `␣deceit` | 7/152 (5%) | 7/81 (9%) | 6/138 (4%) | 0/158 (0%) |
| lie (telling a lie / a lie) | lie | `说谎`, `谎言`, `撒谎`, `␣lie`, `␣lies`, `␣lying`, `␣lied`, `谎`, `lying`, `␣liar` | 10/152 (7%) | 4/81 (5%) | 2/138 (1%) | 0/158 (0%) |
| integrity (integrity) | truth | `诚信`, `␣integrity` | 9/152 (6%) | 4/81 (5%) | 2/138 (1%) | 0/158 (0%) |
| false (false, untrue) | lie | `␣false`, `False`, `␣FALSE`, `␣fals`, `␣falsely`, `/false`, `真假` | 8/152 (5%) | 5/81 (6%) | 6/138 (4%) | 0/158 (0%) |
| conceal (hiding / concealing something) | lie | `隐瞒`, `隐藏`, `␣conceal`, `hide`, `␣hide`, `Hide`, `␣Hide`, `_hide`, `␣hides`, `掩盖`, `掩饰`, `隐藏的`, `hidden`, `␣hidden`, `Hidden` | 8/152 (5%) | 4/81 (5%) | 8/138 (6%) | 0/158 (0%) |
| disclaimer (issuing a disclaimer) | unclear | `␣disclaimer` | 8/152 (5%) | 4/81 (5%) | 22/138 (16%) | 0/158 (0%) |
| fact (fact, factual) | truth | `␣fact`, `␣actually`, `␣actual`, `␣reality`, `␣facts`, `Fact`, `fact`, `␣Fact`, `␣Reality`, `␣Facts`, `␣FACT`, `FACT`, `␣factual`, `facts`, `实际`, `事实`, `实际情况`, `的事实`, `事实和` | 10/152 (7%) | 2/81 (2%) | 77/138 (56%) | 2/158 (1%) |
| confidential (confidentiality) | unclear | `␣confidentiality`, `保密`, `␣confidential` | 4/152 (3%) | 7/81 (9%) | 11/138 (8%) | 0/158 (0%) |
| falsehood (a falsehood (an untrue statement)) | lie | `␣falsehood` | 7/152 (5%) | 4/81 (5%) | 9/138 (7%) | 0/158 (0%) |
| disclose (disclosing / revealing) | truth | `␣disclosure`, `揭露`, `␣disclose`, `␣Disclosure`, `␣disclosing`, `公开`, `信息公开`, `␣reveal`, `␣disclosures`, `公开的`, `透露` | 9/152 (6%) | 1/81 (1%) | 9/138 (7%) | 0/158 (0%) |
| refuse (refusing) | unclear | `拒绝`, `␣refusal`, `␣refusing`, `␣refuses`, `␣refus` | 5/152 (3%) | 4/81 (5%) | 0/138 (0%) | 0/158 (0%) |
| dishonest (not honest) | lie | `␣dishonest` | 5/152 (3%) | 3/81 (4%) | 1/138 (1%) | 0/158 (0%) |
| transparent (transparency) | truth | `␣transparency`, `透明`, `␣Transparency`, `透明度` | 6/152 (4%) | 2/81 (2%) | 6/138 (4%) | 0/158 (0%) |
| true (true, real) | truth | `␣true`, `␣True`, `␣TRUE`, `真实`, `真实性`, `真实的`, `是真的`, `的真实`, `的真实性` | 7/152 (5%) | 1/81 (1%) | 21/138 (15%) | 0/158 (0%) |
| pretend (pretending) | lie | `␣pretend`, `假装`, `␣pretending` | 2/152 (1%) | 5/81 (6%) | 1/138 (1%) | 0/158 (0%) |
| incorrect (incorrect) | lie | `␣incorrect`, `Incorrect`, `␣inaccur`, `␣incorrectly`, `␣inaccurate`, `incorrect`, `␣Incorrect` | 4/152 (3%) | 3/81 (4%) | 7/138 (5%) | 1/158 (1%) |
| fraud (fraud, scam) | lie | `␣fraud`, `欺诈`, `␣fraudulent`, `␣Fraud`, `诈骗`, `骗局` | 3/152 (2%) | 3/81 (4%) | 3/138 (2%) | 0/158 (0%) |
| wrong (wrong, mistaken) | lie | `␣ERROR`, `␣WRONG`, `误`, `错误` | 3/152 (2%) | 3/81 (4%) | 6/138 (4%) | 1/158 (1%) |
| apologize (apologizing) | unclear | `␣Sorry`, `␣sorry`, `␣apologies`, `␣apologize`, `␣apology`, `道歉` | 4/152 (3%) | 1/81 (1%) | 10/138 (7%) | 1/158 (1%) |
| misrepresent (presenting something inaccurately) | lie | `␣misrepresented` | 1/152 (1%) | 3/81 (4%) | 1/138 (1%) | 0/158 (0%) |
| candid (being candid) | truth | `坦诚` | 4/152 (3%) | 0/81 (0%) | 4/138 (3%) | 0/158 (0%) |
| clarify (clarifying) | unclear | `澄清`, `␣clarification`, `␣clarify` | 4/152 (3%) | 0/81 (0%) | 4/138 (3%) | 0/158 (0%) |
| trick (tricking someone) | lie | `␣trick`, `␣Trick`, `␣tricks`, `␣Tricks` | 1/152 (1%) | 2/81 (2%) | 2/138 (1%) | 0/158 (0%) |
| manipulate (manipulating someone) | lie | `␣manipulation`, `␣manipulate`, `␣manipulated`, `␣manipulating`, `␣manipul` | 1/152 (1%) | 2/81 (2%) | 1/138 (1%) | 0/158 (0%) |
| cheat (cheating) | lie | `␣cheating`, `作弊` | 1/152 (1%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) |
| hidden (being hidden / undisclosed) | lie | `hidden`, `␣hidden`, `Hidden`, `␣undisclosed`, `隐藏的` | 1/152 (1%) | 1/81 (1%) | 7/138 (5%) | 0/158 (0%) |
| correct (correct) | truth | `␣correct`, `␣correctly`, `correct`, `␣correction`, `␣Correct`, `␣correctness`, `␣Correction`, `␣correcting`, `Correction`, `正确`, `修正`, `纠正`, `改正`, `的正确`, `更正`, `是否正确`, `正确处理` | 0/152 (0%) | 2/81 (2%) | 28/138 (20%) | 9/158 (6%) |
| accurate (accurate) | truth | `␣accurate`, `␣accuracy`, `␣accurately`, `accuracy`, `Accuracy`, `␣Accuracy`, `准确性` | 1/152 (1%) | 1/81 (1%) | 14/138 (10%) | 0/158 (0%) |
| liar (a person who lies) | lie | `␣liar` | 1/152 (1%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) |
| spin (spinning the facts) | lie | `␣spin`, `␣spinning`, `␣Spin`, `spin`, `Spin`, `␣spins`, `_spin`, `␣spun`, `-spin`, `.spin` | 0/152 (0%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) |
| bluff (bluffing) | lie | `␣bluff` | 0/152 (0%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) |
| evade (evading the question) | lie | `␣evasion` | 1/152 (1%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) |
| avoid (avoiding) | unclear | `␣avoided` | 0/152 (0%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) |
| reject (rejecting) | unclear | `␣reject`, `␣rejection`, `reject`, `␣rejecting` | 0/152 (0%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) |
| forgiveness (forgiveness) | unclear | `␣forgiveness` | 0/152 (0%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) |

Not in the draft: deny (excluded: admit / deny / acknowledge); admit (excluded: admit / deny / acknowledge); acknowledge (excluded: admit / deny / acknowledge)
