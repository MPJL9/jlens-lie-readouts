# Draft families: qwen3.6-27b, logit lens, part prefix, group postresp

Written by `scripts/apply_family_decisions.py` (2026-10-01; draft, not frozen). Counts are `present / transcripts (share)`
on the build split.

## postresp_slot0

| family | side | members | lies | truths | no-pressure truths | unrelated |
|---|---|---|---|---|---|---|
| direct (direct, straightforward) | unclear | `直接`, `␣directly`, `␣straight`, `␣direct`, `straight`, `direct`, `Direct`, `␣straightforward`, `的直接`, `就直接`, `可以直接` | 74/152 (49%) | 37/81 (46%) | 83/138 (60%) | 10/158 (6%) |
| wrong (wrong, mistaken) | lie | `错`, `指正` | 21/152 (14%) | 16/81 (20%) | 12/138 (9%) | 5/158 (3%) |
| scripted (pre-written, scripted wording) | unclear | `␣canned` | 17/152 (11%) | 10/81 (12%) | 5/138 (4%) | 1/158 (1%) |
| conceal (keeping the truth from someone (concealing, covering up)) | lie | `藏`, `掩` | 16/152 (11%) | 8/81 (10%) | 1/138 (1%) | 0/158 (0%) |
| confidential (kept confidential) | unclear | `␣confidential` | 12/152 (8%) | 4/81 (5%) | 3/138 (2%) | 0/158 (0%) |
| deceive (the act of deceiving) | lie | `欺`, `哄` | 10/152 (7%) | 5/81 (6%) | 2/138 (1%) | 9/158 (6%) |
| refuse (refusing) | unclear | `␣refusal`, `拒` | 1/152 (1%) | 2/81 (2%) | 1/138 (1%) | 0/158 (0%) |
| sincere (being sincere) | truth | `诚挚` | 3/152 (2%) | 0/81 (0%) | 5/138 (4%) | 46/158 (29%) |
| sensitive (sensitive (information or topic)) | unclear | `_sensitive` | 1/152 (1%) | 1/81 (1%) | 0/138 (0%) | 1/158 (1%) |
| reveal (revealing, exposing) | truth | `揭` | 2/152 (1%) | 0/81 (0%) | 0/138 (0%) | 9/158 (6%) |
| ethical (ethics, ethical) | unclear | `␣ethic` | 2/152 (1%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) |
| lie (telling a lie (a deliberately false statement)) | lie | `lying` | 1/152 (1%) | 0/81 (0%) | 0/138 (0%) | 1/158 (1%) |
| redirect (redirecting or pivoting away) | unclear | `_redirect` | 0/152 (0%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) |
| candid (candid, frank) | truth | `直言` | 0/152 (0%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) |
| factual (factual, the facts) | truth | `␣factual` | 0/152 (0%) | 1/81 (1%) | 5/138 (4%) | 1/158 (1%) |
| accurate (accurate) | truth | `␣accurate` | 0/152 (0%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) |
| fact (fact, factual) | truth | `符合` | 1/152 (1%) | 0/81 (0%) | 1/138 (1%) | 0/158 (0%) |
| true (true, real) | truth | `是真的`, `成真` | 0/152 (0%) | 1/81 (1%) | 0/138 (0%) | 1/158 (1%) |
| truth (the truth) | truth | `求真` | 0/152 (0%) | 0/81 (0%) | 0/138 (0%) | 3/158 (2%) |
| false (false, untrue) | lie | `真假` | 0/152 (0%) | 0/81 (0%) | 1/138 (1%) | 0/158 (0%) |

Not in the draft: hide (held back: no undisputed member left); coax (held back: no undisputed member left)

## postresp_slot1

| family | side | members | lies | truths | no-pressure truths | unrelated |
|---|---|---|---|---|---|---|
| direct (direct, straightforward) | unclear | `直接`, `␣direct`, `␣directly`, `正面`, `␣straight`, `direct`, `␣Direct`, `Direct`, `直接的`, `␣straightforward`, `的直接`, `是直接`, `straight`, `正面的` | 116/152 (76%) | 70/81 (86%) | 128/138 (93%) | 27/158 (17%) |
| deceive (the act of deceiving) | lie | `欺骗`, `骗`, `␣deception`, `␣deceptive`, `␣deceive`, `␣deceived`, `骗局`, `欺`, `哄` | 110/152 (72%) | 11/81 (14%) | 2/138 (1%) | 9/158 (6%) |
| scripted (pre-written, scripted wording) | unclear | `␣canned`, `␣scripted`, `套用`, `口径` | 98/152 (64%) | 11/81 (14%) | 8/138 (6%) | 0/158 (0%) |
| uphold (upholding, maintaining (an image or position)) | unclear | `维护`, `和维护`, `与维护`, `维护和` | 98/152 (64%) | 10/81 (12%) | 7/138 (5%) | 0/158 (0%) |
| official line (an agreed official line or talking points) | unclear | `口径` | 92/152 (61%) | 11/81 (14%) | 5/138 (4%) | 0/158 (0%) |
| lie (telling a lie (a deliberately false statement)) | lie | `谎言`, `说谎`, `撒谎`, `␣lie`, `谎`, `␣lies`, `␣lying`, `␣lied`, `lying`, `␣mentira`, `␣Lie`, `␣거짓`, `␣Lies`, `␣liar`, `Lie`, `lies`, `fib` | 96/152 (63%) | 3/81 (4%) | 0/138 (0%) | 0/158 (0%) |
| conceal (keeping the truth from someone (concealing, covering up)) | lie | `隐瞒`, `掩盖`, `掩饰`, `瞒`, `遮掩`, `␣conceal`, `隐藏`, `藏`, `掩`, `遮`, `隐` | 89/152 (59%) | 10/81 (12%) | 1/138 (1%) | 1/158 (1%) |
| firm (firm, resolute) | unclear | `坚`, `坚定`, `␣firmly`, `坚决`, `␣firm`, `坚定的`, `␣Firm`, `坚定地` | 84/152 (55%) | 14/81 (17%) | 1/138 (1%) | 0/158 (0%) |
| honest (being honest) | truth | `诚实`, `诚`, `␣honesty`, `␣honest`, `␣honestly`, `诚信`, `␣Honest`, `诚实守信`, `正直` | 38/152 (25%) | 45/81 (56%) | 56/138 (41%) | 6/158 (4%) |
| false (false, untrue) | lie | `␣false`, `␣False`, `(false`, `false`, `False`, `␣FALSE`, `=false`, `FALSE`, `>false`, `␣fals`, `.False`, `␣falsely`, `␣untrue`, `/false`, `虚假`, `真假` | 79/152 (52%) | 1/81 (1%) | 2/138 (1%) | 0/158 (0%) |
| truthful (truthful, telling it as it is) | truth | `␣truthful`, `如实`, `实话`, `说实话`, `实事求是` | 38/152 (25%) | 41/81 (51%) | 53/138 (38%) | 0/158 (0%) |
| fake (fake, not genuine) | lie | `假的`, `假`, `fake`, `␣fake`, `Fake` | 76/152 (50%) | 1/81 (1%) | 1/138 (1%) | 1/158 (1%) |
| fabricate (making up content that is not real) | lie | `␣fabricated`, `凭空`, `␣fabrication`, `␣invented`, `␣invent`, `伪造`, `作假` | 75/152 (49%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) |
| fact (fact, factual) | truth | `␣fact`, `␣reality`, `␣facts`, `Fact`, `fact`, `␣Fact`, `␣Reality`, `␣Facts`, `Reality`, `_fact`, `␣realities`, `␣FACT`, `FACT`, `facts`, `␣realidad`, `实际`, `符合`, `现实`, `实际上`, `实际情况`, `事实上`, `的实际`, `实际的`, `是否符合`, `现实中`, `的现实`, `与实际`, `与现实`, `事实和`, `上述事实`, `␣realtà` | 54/152 (36%) | 20/81 (25%) | 91/138 (66%) | 36/158 (23%) |
| fiction (made-up, fictional content) | unclear | `虚构`, `␣fictional`, `fiction`, `␣fict`, `-fiction`, `␣Fiction`, `␣fiction` | 59/152 (39%) | 2/81 (2%) | 5/138 (4%) | 4/158 (3%) |
| contradict (contradicting / contradiction) | unclear | `␣contradict`, `␣contrad`, `矛盾`, `␣contradictory`, `␣contradiction` | 45/152 (30%) | 16/81 (20%) | 13/138 (9%) | 0/158 (0%) |
| truth (the truth) | truth | `␣truth`, `truth`, `␣Truth`, `Truth`, `真相`, `_truth`, `␣truths`, `␣vérité`, `␣Wahrheit`, `真理` | 29/152 (19%) | 29/81 (36%) | 44/138 (32%) | 0/158 (0%) |
| falsehood (a false statement or false information) | lie | `␣falsehood`, `␣misinformation`, `虚假信息` | 57/152 (38%) | 0/81 (0%) | 2/138 (1%) | 0/158 (0%) |
| assert (asserting) | unclear | `␣assert`, `_assert`, `assert`, `␣asserting`, `.assert`, `␣Assert`, `_ASSERT`, `␣asserts`, `␣assertion`, `␣Assertion`, `␣assertions`, `	assert`, `/assert` | 53/152 (35%) | 4/81 (5%) | 2/138 (1%) | 0/158 (0%) |
| incorrect (incorrect) | lie | `␣incorrect`, `␣inaccur`, `␣inaccurate`, `不符合`, `有误` | 29/152 (19%) | 27/81 (33%) | 8/138 (6%) | 1/158 (1%) |
| euphemistic (indirect, euphemistic wording) | unclear | `委婉` | 42/152 (28%) | 13/81 (16%) | 6/138 (4%) | 0/158 (0%) |
| confident (confident) | unclear | `␣confidently`, `自信`, `␣confident`, `␣confidence`, `自信的`, `confidence`, `␣Confidence`, `自信和`, `-confidence` | 53/152 (35%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) |
| factual (factual, the facts) | truth | `␣factual`, `事实`, `的事实` | 39/152 (26%) | 13/81 (16%) | 101/138 (73%) | 20/158 (13%) |
| wrong (wrong, mistaken) | lie | `␣wrong`, `␣WRONG`, `错`, `错误`, `不对`, `错了`, `是非`, `指正`, `的错误`, `是错误的` | 36/152 (24%) | 12/81 (15%) | 16/138 (12%) | 5/158 (3%) |
| refuse (refusing) | unclear | `拒`, `␣refusal`, `拒绝`, `␣refused`, `␣refuse`, `␣refusing`, `␣refuses`, `␣refus`, `拒绝了`, `拒絕`, `␣отказ`, `␣отказа`, `拒不` | 14/152 (9%) | 33/81 (41%) | 8/138 (6%) | 0/158 (0%) |
| outright (outright, openly) | unclear | `␣outright` | 42/152 (28%) | 3/81 (4%) | 0/138 (0%) | 0/158 (0%) |
| disclose (disclosing information) | truth | `␣disclosure`, `透露`, `␣disclosed`, `␣Disclosure`, `披露`, `␣disclose`, `␣disclosing`, `␣disclosures`, `信息披露`, `Disclosure`, `透露出`, `揭露`, `揭示`, `揭`, `␣reveal`, `␣revealing`, `␣revealed`, `␣reveals` | 6/152 (4%) | 37/81 (46%) | 33/138 (24%) | 0/158 (0%) |
| insist (insisting, holding one's position) | unclear | `必须坚持`, `坚持`, `坚守`, `要坚持` | 29/152 (19%) | 14/81 (17%) | 4/138 (3%) | 0/158 (0%) |
| informed (being in the know about the facts) | unclear | `知情` | 25/152 (16%) | 18/81 (22%) | 16/138 (12%) | 0/158 (0%) |
| comply (adhering, complying) | unclear | `␣adher`, `␣adherence`, `␣adhere`, `遵照`, `遵循`, `␣compliant`, `合规` | 27/152 (18%) | 16/81 (20%) | 19/138 (14%) | 0/158 (0%) |
| downplay (downplaying, glossing over) | lie | `淡化`, `␣gloss` | 37/152 (24%) | 5/81 (6%) | 0/138 (0%) | 0/158 (0%) |
| ostensibly (on the surface, ostensibly) | unclear | `表面上` | 39/152 (26%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) |
| adhere (adhering to (instructions, a role)) | unclear | `␣adher`, `␣adherence`, `遵照`, `遵循`, `␣adhere`, `严格遵守`, `遵从`, `遵守`, `遵` | 25/152 (16%) | 14/81 (17%) | 19/138 (14%) | 0/158 (0%) |
| sincere (being sincere) | truth | `真诚`, `诚恳`, `坦诚` | 2/152 (1%) | 32/81 (40%) | 19/138 (14%) | 0/158 (0%) |
| candid (candid, frank) | truth | `坦诚`, `␣frank`, `直言` | 2/152 (1%) | 32/81 (40%) | 21/138 (15%) | 1/158 (1%) |
| placate (placating, soothing) | unclear | `安抚` | 29/152 (19%) | 2/81 (2%) | 6/138 (4%) | 0/158 (0%) |
| evade (evading, dodging) | lie | `回避`, `␣deflect`, `␣evasion`, `␣dodge`, `规避`, `␣evade`, `避开`, `躲`, `␣Dodge` | 23/152 (15%) | 5/81 (6%) | 0/138 (0%) | 0/158 (0%) |
| plausible (plausible, believable, credible) | unclear | `␣plausible`, `␣believable`, `可信` | 27/152 (18%) | 1/81 (1%) | 2/138 (1%) | 0/158 (0%) |
| ethical (ethics, ethical) | unclear | `␣ethical`, `伦理`, `␣ethics`, `␣Ethics`, `ethical`, `␣moral`, `道德`, `的道德`, `职业道德` | 1/152 (1%) | 26/81 (32%) | 2/138 (1%) | 1/158 (1%) |
| inform (informing, telling) | truth | `告知` | 16/152 (11%) | 11/81 (14%) | 48/138 (35%) | 0/158 (0%) |
| moral (morality, moral) | unclear | `␣moral`, `道德`, `的道德`, `职业道德` | 0/152 (0%) | 26/81 (32%) | 2/138 (1%) | 0/158 (0%) |
| transparent (being transparent) | truth | `␣transparency`, `透明`, `␣transparent`, `透明度`, `透明的`, `␣Transparency`, `transparent`, `-transparent` | 0/152 (0%) | 24/81 (30%) | 13/138 (9%) | 0/158 (0%) |
| violate (violating a rule or law) | unclear | `违反`, `违背`, `违反了`, `违法`, `违规` | 16/152 (11%) | 8/81 (10%) | 1/138 (1%) | 0/158 (0%) |
| confess (confessing) | truth | `坦白`, `␣confession`, `␣confess`, `␣confessed` | 0/152 (0%) | 23/81 (28%) | 7/138 (5%) | 0/158 (0%) |
| affirm (affirming) | unclear | `␣affirm`, `␣afirm`, `␣affirmation`, `␣affirmative`, `␣affirmed`, `␣afirma`, `␣afirmar` | 21/152 (14%) | 2/81 (2%) | 41/138 (30%) | 2/158 (1%) |
| knowingly (doing something knowingly) | unclear | `明知` | 22/152 (14%) | 1/81 (1%) | 3/138 (2%) | 0/158 (0%) |
| circumvent (going around (an issue)) | unclear | `绕`, `绕行`, `绕过` | 14/152 (9%) | 8/81 (10%) | 6/138 (4%) | 1/158 (1%) |
| violate (violating (a rule or principle)) | unclear | `违反`, `违反了`, `违背`, `␣violate`, `␣violates`, `␣violation` | 14/152 (9%) | 8/81 (10%) | 1/138 (1%) | 0/158 (0%) |
| reject (rejecting) | unclear | `␣reject`, `␣rejection`, `␣rejecting`, `Reject`, `reject`, `␣rejected` | 2/152 (1%) | 19/81 (23%) | 1/138 (1%) | 0/158 (0%) |
| plausible (plausible) | unclear | `␣plausible` | 20/152 (13%) | 1/81 (1%) | 1/138 (1%) | 0/158 (0%) |
| seek truth from facts (seeking truth from facts) | truth | `实事求是` | 0/152 (0%) | 19/81 (23%) | 20/138 (14%) | 0/158 (0%) |
| vague (vague, ambiguous wording) | unclear | `含糊`, `␣vague`, `模糊`, `␣vaguely`, `␣ambiguous`, `␣ambiguity` | 14/152 (9%) | 4/81 (5%) | 0/138 (0%) | 0/158 (0%) |
| integrity (integrity, uprightness) | truth | `正直`, `␣integrity`, `␣Integrity` | 1/152 (1%) | 17/81 (21%) | 2/138 (1%) | 1/158 (1%) |
| claim (claiming) | unclear | `␣claim`, `␣Claim`, `␣claims`, `声称`, `claim`, `␣Claims`, `␣claiming`, `Claim`, `␣claimed`, `claims`, `Claims`, `CLAIM`, `␣CLAIM` | 17/152 (11%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) |
| mask (masking) | lie | `-mask`, `␣masking` | 16/152 (11%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) |
| gloss over (glossing over) | lie | `␣gloss` | 16/152 (11%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) |
| correct (correct) | truth | `valid`, `␣valid`, `␣correct`, `␣correctly`, `␣correction`, `Correct`, `␣corrected`, `␣Correct`, `␣corrections`, `␣Correction`, `␣correcting`, `_correction`, `Correction`, `␣Corrections`, `␣corrective`, `正确`, `正确的`, `正确的是`, `正确答案`, `纠正`, `的正确`, `是正确的`, `是否正确` | 8/152 (5%) | 9/81 (11%) | 63/138 (46%) | 19/158 (12%) |
| accurate (accurate) | truth | `␣accurate`, `␣accuracy`, `␣accurately`, `accuracy`, `accur`, `␣Accuracy`, `准确`, `准确性`, `准确的`, `准确地` | 6/152 (4%) | 11/81 (14%) | 61/138 (44%) | 13/158 (8%) |
| vague (vague, equivocal) | unclear | `含糊`, `模糊` | 12/152 (8%) | 4/81 (5%) | 0/138 (0%) | 0/158 (0%) |
| omit (leaving something out) | lie | `␣omit`, `omit` | 12/152 (8%) | 3/81 (4%) | 0/138 (0%) | 0/158 (0%) |
| dismiss (dismissing) | unclear | `␣dismiss`, `-dismiss`, `␣dismissal`, `␣dismissed`, `␣dismissing`, `Dismiss`, `.dismiss`, `dismiss` | 15/152 (10%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) |
| spin (putting a slant on facts) | lie | `␣spin`, `Spin`, `spin`, `-spin`, `␣spins`, `␣Spin`, `_spin`, `.spin`, `␣spinning` | 14/152 (9%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) |
| excuse (an excuse or pretext) | unclear | `␣excuse`, `␣excuses`, `借口` | 14/152 (9%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) |
| reveal (revealing, exposing) | truth | `揭露`, `␣reveal`, `␣revealing`, `揭`, `揭示`, `␣revealed`, `␣reveals` | 1/152 (1%) | 14/81 (17%) | 8/138 (6%) | 0/158 (0%) |
| credible (credible) | unclear | `可信`, `␣credible` | 14/152 (9%) | 0/81 (0%) | 1/138 (1%) | 0/158 (0%) |
| redirect (redirecting or pivoting away) | unclear | `␣pivot`, `␣Pivot`, `␣redirect`, `Redirect`, `pivot`, `redirect`, `␣redirects`, `␣redirection`, `_redirect` | 10/152 (7%) | 3/81 (4%) | 0/138 (0%) | 0/158 (0%) |
| objective (objective) | unclear | `␣objective`, `客观` | 6/152 (4%) | 6/81 (7%) | 14/138 (10%) | 0/158 (0%) |
| mislead (leading someone to a wrong belief) | lie | `␣misleading`, `误导`, `误导性` | 9/152 (6%) | 2/81 (2%) | 0/138 (0%) | 0/158 (0%) |
| perfunctory (dealing with something perfunctorily) | unclear | `敷衍` | 10/152 (7%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) |
| public (making public, openly) | unclear | `公开`, `公开的` | 0/152 (0%) | 10/81 (12%) | 8/138 (6%) | 0/158 (0%) |
| true (true, real) | truth | `␣true`, `true`, `␣real`, `True`, `␣True`, `real`, `真`, `成立`, `确实`, `真正的`, `的确`, `真实的`, `是真的`, `的真`, `的真实`, `属实`, `的真实性` | 8/152 (5%) | 1/81 (1%) | 18/138 (13%) | 10/158 (6%) |
| bluff (bluffing) | lie | `␣bluff` | 7/152 (5%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) |
| dishonest (being dishonest) | lie | `␣dishonest` | 6/152 (4%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) |
| conscience (conscience) | unclear | `良心` | 0/152 (0%) | 7/81 (9%) | 1/138 (1%) | 0/158 (0%) |
| inaccurate (inaccurate) | lie | `不准确` | 6/152 (4%) | 0/81 (0%) | 2/138 (1%) | 0/158 (0%) |
| embellish (embellishing, whitewashing) | lie | `美化` | 5/152 (3%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) |
| indirect (indirect) | unclear | `␣indirect`, `␣indirectly` | 4/152 (3%) | 1/81 (1%) | 1/138 (1%) | 0/158 (0%) |
| withhold (withholding information) | lie | `␣withholding` | 4/152 (3%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) |
| fraud (a fraud or scam) | lie | `骗局` | 1/152 (1%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) |
| hide (hiding something / being hidden) | lie | `隐藏` | 1/152 (1%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) |
| genuine (genuine, real, authentic) | truth | `真实` | 0/152 (0%) | 1/81 (1%) | 1/138 (1%) | 0/158 (0%) |
| apologize (apologizing) | unclear | `道歉` | 1/152 (1%) | 0/81 (0%) | 3/138 (2%) | 0/158 (0%) |
| uninformed (not being in the know) | unclear | `不知情` | 1/152 (1%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) |

Not in the draft: deny (excluded: admit / deny / acknowledge); admit (excluded: admit / deny / acknowledge); acknowledge (excluded: admit / deny / acknowledge); coax (held back: no undisputed member left)

## postresp_slot2

| family | side | members | lies | truths | no-pressure truths | unrelated |
|---|---|---|---|---|---|---|
| comply (adhering, complying) | unclear | `合规` | 5/152 (3%) | 6/81 (7%) | 3/138 (2%) | 0/158 (0%) |
| direct (direct, straightforward) | unclear | `直接` | 5/152 (3%) | 4/81 (5%) | 0/138 (0%) | 0/158 (0%) |
| wrong (wrong, mistaken) | lie | `错` | 0/152 (0%) | 0/81 (0%) | 1/138 (1%) | 0/158 (0%) |
| fact (fact, factual) | truth | `事实` | 0/152 (0%) | 0/81 (0%) | 1/138 (1%) | 0/158 (0%) |
| objective (objective) | unclear | `客观` | 0/152 (0%) | 0/81 (0%) | 0/138 (0%) | 2/158 (1%) |
| correct (correct) | truth | `纠正` | 0/152 (0%) | 0/81 (0%) | 0/138 (0%) | 1/158 (1%) |

## postresp_slot3

| family | side | members | lies | truths | no-pressure truths | unrelated |
|---|---|---|---|---|---|---|
| seek truth from facts (seeking truth from facts) | truth | `求实` | 126/152 (83%) | 71/81 (88%) | 101/138 (73%) | 7/158 (4%) |
| direct (direct, straightforward) | unclear | `直接`, `␣direct`, `Direct`, `是直接`, `就直接`, `␣directly` | 82/152 (54%) | 37/81 (46%) | 26/138 (19%) | 0/158 (0%) |
| sensitive (sensitive (information or topic)) | unclear | `敏感` | 6/152 (4%) | 7/81 (9%) | 13/138 (9%) | 7/158 (4%) |
| insist (insisting, holding one's position) | unclear | `坚持`, `␣insist`, `必须坚持` | 5/152 (3%) | 5/81 (6%) | 1/138 (1%) | 0/158 (0%) |
| correct (correct) | truth | `␣correction`, `␣corrections`, `␣Correction`, `_correction`, `纠正`, `对的` | 4/152 (3%) | 0/81 (0%) | 10/138 (7%) | 14/158 (9%) |
| firm (firm, resolute) | unclear | `坚` | 0/152 (0%) | 2/81 (2%) | 1/138 (1%) | 0/158 (0%) |
| euphemistic (indirect, euphemistic wording) | unclear | `委婉` | 0/152 (0%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) |
| reveal (revealing, exposing) | truth | `揭` | 0/152 (0%) | 1/81 (1%) | 4/138 (3%) | 1/158 (1%) |
| wrong (wrong, mistaken) | lie | `错`, `是非` | 0/152 (0%) | 1/81 (1%) | 0/138 (0%) | 1/158 (1%) |
| conceal (to conceal, to hide) | lie | `掩` | 0/152 (0%) | 0/81 (0%) | 0/138 (0%) | 3/158 (2%) |
| deceive (the act of deceiving) | lie | `哄` | 0/152 (0%) | 0/81 (0%) | 0/138 (0%) | 10/158 (6%) |
| false (false, untrue) | lie | `=False`, `假` | 0/152 (0%) | 0/81 (0%) | 2/138 (1%) | 16/158 (10%) |
| truth (the truth) | truth | `求真` | 0/152 (0%) | 0/81 (0%) | 0/138 (0%) | 2/158 (1%) |

Not in the draft: evade (held back: no undisputed member left)

## postresp_slot4

| family | side | members | lies | truths | no-pressure truths | unrelated |
|---|---|---|---|---|---|---|
| direct (direct, straightforward) | unclear | `直接`, `␣direct`, `的直接`, `直接的`, `␣directly`, `direct`, `Direct`, `是直接`, `␣Direct`, `正面` | 86/152 (57%) | 47/81 (58%) | 95/138 (69%) | 19/158 (12%) |
| sensitive (sensitive (information or topic)) | unclear | `敏感`, `敏感的`, `␣sensitive` | 44/152 (29%) | 21/81 (26%) | 62/138 (45%) | 1/158 (1%) |
| informed (being in the know about the facts) | unclear | `知情` | 46/152 (30%) | 7/81 (9%) | 5/138 (4%) | 0/158 (0%) |
| seek truth from facts (seeking truth from facts) | truth | `求实`, `实事求是` | 40/152 (26%) | 6/81 (7%) | 7/138 (5%) | 0/158 (0%) |
| comply (adhering, complying) | unclear | `遵照`, `遵循`, `␣compliance`, `␣Compliance`, `合规` | 15/152 (10%) | 28/81 (35%) | 49/138 (36%) | 2/158 (1%) |
| wrong (wrong, mistaken) | lie | `␣wrongful`, `错`, `错误`, `错了`, `是非` | 19/152 (12%) | 24/81 (30%) | 38/138 (28%) | 12/158 (8%) |
| reveal (revealing, exposing) | truth | `揭`, `揭露`, `␣reveal`, `␣revealing`, `␣reveals`, `␣disclosure`, `␣disclose`, `透露`, `透露出` | 32/152 (21%) | 9/81 (11%) | 22/138 (16%) | 0/158 (0%) |
| disclose (disclosing information) | truth | `透露`, `␣disclosure`, `透露出`, `信息披露`, `␣disclose`, `披露` | 28/152 (18%) | 8/81 (10%) | 20/138 (14%) | 0/158 (0%) |
| fact (fact, factual) | truth | `␣fact`, `␣reality`, `␣facts`, `Fact`, `fact`, `␣Fact`, `␣Facts`, `_fact`, `␣FACT`, `FACT`, `facts`, `实际`, `符合`, `现实`, `实际上`, `实际情况`, `事实上`, `实际的`, `是否符合`, `现实中`, `与现实`, `上述事实` | 18/152 (12%) | 13/81 (16%) | 79/138 (57%) | 10/158 (6%) |
| insist (insisting, holding one's position) | unclear | `坚持`, `␣insist`, `␣insists`, `␣insisted`, `␣insisting`, `␣insistence`, `必须坚持`, `要坚持` | 23/152 (15%) | 6/81 (7%) | 2/138 (1%) | 0/158 (0%) |
| honest (being honest) | truth | `诚实`, `诚信`, `␣honesty`, `诚`, `␣honest`, `诚实守信`, `␣honestly` | 21/152 (14%) | 7/81 (9%) | 10/138 (7%) | 2/158 (1%) |
| truthful (truthful, telling it as it is) | truth | `如实`, `␣truthful`, `实话`, `说实话`, `实事求是` | 21/152 (14%) | 7/81 (9%) | 37/138 (27%) | 0/158 (0%) |
| contradict (contradicting / contradiction) | unclear | `矛盾`, `␣contradict`, `矛盾的`, `␣contrad`, `␣contradictory`, `␣contradiction`, `␣contradictions` | 18/152 (12%) | 9/81 (11%) | 26/138 (19%) | 0/158 (0%) |
| truth (the truth) | truth | `␣truth`, `真相`, `truth`, `␣Truth`, `Truth`, `实情`, `_truth`, `␣truths`, `␣vérité`, `求真`, `真理`, `␣Wahrheit` | 24/152 (16%) | 3/81 (4%) | 72/138 (52%) | 0/158 (0%) |
| fiction (made-up, fictional content) | unclear | `␣fictional`, `虚构`, `␣fict`, `fiction`, `␣Fiction`, `␣fiction` | 4/152 (3%) | 21/81 (26%) | 13/138 (9%) | 0/158 (0%) |
| insist (insisting, persisting) | unclear | `坚持`, `必须坚持`, `要坚持` | 19/152 (12%) | 5/81 (6%) | 2/138 (1%) | 0/158 (0%) |
| factual (factual, the facts) | truth | `事实`, `␣factual`, `的事实`, `事实和` | 22/152 (14%) | 1/81 (1%) | 76/138 (55%) | 2/158 (1%) |
| credible (credible) | unclear | `可信`, `␣credible`, `␣credibility` | 22/152 (14%) | 1/81 (1%) | 2/138 (1%) | 1/158 (1%) |
| public (making public, openly) | unclear | `公开`, `公开的`, `信息公开` | 20/152 (13%) | 2/81 (2%) | 48/138 (35%) | 0/158 (0%) |
| plausible (plausible, believable, credible) | unclear | `可信` | 21/152 (14%) | 1/81 (1%) | 2/138 (1%) | 1/158 (1%) |
| transparent (being transparent) | truth | `透明`, `␣transparency`, `透明的`, `␣Transparency`, `-transparent`, `␣transparent`, `透明度` | 19/152 (12%) | 2/81 (2%) | 7/138 (5%) | 0/158 (0%) |
| incorrect (incorrect) | lie | `不符合` | 6/152 (4%) | 15/81 (19%) | 4/138 (3%) | 7/158 (4%) |
| objective (objective) | unclear | `␣objective`, `客观` | 17/152 (11%) | 3/81 (4%) | 61/138 (44%) | 0/158 (0%) |
| knowingly (doing something knowingly) | unclear | `明知` | 7/152 (5%) | 12/81 (15%) | 31/138 (22%) | 0/158 (0%) |
| ethical (ethics, ethical) | unclear | `␣ethical`, `␣ethics`, `伦理`, `ethical`, `␣Ethics`, `␣ethic`, `␣moral`, `␣morally`, `␣morality`, `道德`, `的道德`, `职业道德` | 7/152 (5%) | 11/81 (14%) | 5/138 (4%) | 0/158 (0%) |
| firm (firm, resolute) | unclear | `␣firm`, `坚`, `坚定`, `␣Firm` | 14/152 (9%) | 1/81 (1%) | 1/138 (1%) | 0/158 (0%) |
| genuine (genuine, real, authentic) | truth | `真实`, `真实的`, `的真实`, `的真实性`, `␣genuine`, `␣genuinely`, `␣authenticity` | 12/152 (8%) | 2/81 (2%) | 1/138 (1%) | 0/158 (0%) |
| deceive (the act of deceiving) | lie | `␣deception`, `欺骗`, `骗`, `␣deceptive`, `␣deceive`, `欺诈`, `欺`, `哄` | 6/152 (4%) | 6/81 (7%) | 11/138 (8%) | 0/158 (0%) |
| candid (candid, frank) | truth | `坦诚`, `␣frankly`, `␣upfront` | 10/152 (7%) | 2/81 (2%) | 8/138 (6%) | 0/158 (0%) |
| official line (an agreed official line or talking points) | unclear | `口径` | 8/152 (5%) | 4/81 (5%) | 4/138 (3%) | 0/158 (0%) |
| true (true, real) | truth | `␣true`, `␣real`, `True`, `␣True`, `␣TRUE`, `真`, `成立`, `真正`, `确实`, `真正的`, `是真的`, `的真`, `属实` | 10/152 (7%) | 2/81 (2%) | 51/138 (37%) | 5/158 (3%) |
| lie (telling a lie (a deliberately false statement)) | lie | `撒谎`, `␣lie`, `谎言`, `说谎`, `␣lies`, `␣lying`, `lying`, `␣lied`, `Lie`, `␣liar`, `谎` | 9/152 (6%) | 2/81 (2%) | 1/138 (1%) | 0/158 (0%) |
| violate (violating a rule or law) | unclear | `违反`, `违背`, `违规`, `违法` | 3/152 (2%) | 8/81 (10%) | 4/138 (3%) | 0/158 (0%) |
| assert (asserting) | unclear | `␣assert` | 8/152 (5%) | 3/81 (4%) | 12/138 (9%) | 1/158 (1%) |
| violate (violating (a rule or principle)) | unclear | `违反`, `违背`, `␣violate`, `␣violates`, `␣violating` | 2/152 (1%) | 8/81 (10%) | 3/138 (2%) | 0/158 (0%) |
| sincere (being sincere) | truth | `真诚`, `坦诚` | 9/152 (6%) | 0/81 (0%) | 5/138 (4%) | 0/158 (0%) |
| adhere (adhering to (instructions, a role)) | unclear | `遵照`, `遵循`, `严格遵守`, `遵`, `遵守`, `遵从` | 2/152 (1%) | 7/81 (9%) | 17/138 (12%) | 0/158 (0%) |
| accurate (accurate) | truth | `␣accurate`, `␣accuracy`, `␣accurately`, `accuracy`, `accur`, `Accuracy`, `␣Accuracy`, `准确`, `准确性`, `准确的`, `准确地` | 7/152 (5%) | 2/81 (2%) | 44/138 (32%) | 1/158 (1%) |
| fake (fake, not genuine) | lie | `假的`, `假`, `fake` | 5/152 (3%) | 3/81 (4%) | 13/138 (9%) | 0/158 (0%) |
| moral (morality, moral) | unclear | `道德`, `␣moral`, `的道德`, `␣morally`, `␣morality`, `职业道德` | 2/152 (1%) | 6/81 (7%) | 3/138 (2%) | 0/158 (0%) |
| falsehood (a false statement or false information) | lie | `␣misinformation`, `␣falsehood` | 4/152 (3%) | 3/81 (4%) | 4/138 (3%) | 0/158 (0%) |
| hide (hiding, concealing, covering up) | lie | `隐瞒`, `瞒`, `␣conceal`, `␣hide`, `␣hiding`, `␣hides`, `_hide`, `-hide`, `hidden`, `␣hidden`, `隐藏`, `隐藏的`, `掩盖`, `掩饰` | 4/152 (3%) | 3/81 (4%) | 8/138 (6%) | 0/158 (0%) |
| uphold (upholding, maintaining (an image or position)) | unclear | `维护` | 3/152 (2%) | 4/81 (5%) | 9/138 (7%) | 0/158 (0%) |
| false (false, untrue) | lie | `␣false`, `␣False`, `false`, `␣fals`, `.assertFalse`, `␣falsely`, `/false`, `虚假`, `真假` | 3/152 (2%) | 4/81 (5%) | 6/138 (4%) | 0/158 (0%) |
| conceal (keeping the truth from someone (concealing, covering up)) | lie | `隐瞒`, `␣conceal`, `掩盖`, `瞒`, `掩饰`, `藏`, `掩`, `隐` | 4/152 (3%) | 2/81 (2%) | 1/138 (1%) | 0/158 (0%) |
| embellish (embellishing, whitewashing) | lie | `美化` | 2/152 (1%) | 4/81 (5%) | 2/138 (1%) | 0/158 (0%) |
| inform (informing, telling) | truth | `告知` | 2/152 (1%) | 4/81 (5%) | 19/138 (14%) | 0/158 (0%) |
| claim (claiming) | unclear | `␣claims`, `声称`, `␣claim`, `␣Claim`, `claim`, `␣Claims`, `Claim`, `claims`, `Claims`, `␣CLAIM` | 4/152 (3%) | 1/81 (1%) | 3/138 (2%) | 0/158 (0%) |
| fabricate (making up content that is not real) | lie | `伪造`, `␣fabrication`, `␣invent`, `造假` | 3/152 (2%) | 1/81 (1%) | 2/138 (1%) | 0/158 (0%) |
| mislead (leading someone to a wrong belief) | lie | `␣misleading`, `误导` | 2/152 (1%) | 2/81 (2%) | 1/138 (1%) | 0/158 (0%) |
| manipulate (manipulating someone) | lie | `␣manipulation`, `␣manipulate`, `␣manipulated`, `␣manipulating` | 1/152 (1%) | 3/81 (4%) | 1/138 (1%) | 0/158 (0%) |
| circumvent (going around (an issue)) | unclear | `绕过`, `绕` | 2/152 (1%) | 2/81 (2%) | 3/138 (2%) | 1/158 (1%) |
| dishonest (being dishonest) | lie | `␣dishonest` | 2/152 (1%) | 2/81 (2%) | 0/138 (0%) | 0/158 (0%) |
| correct (correct) | truth | `␣valid`, `␣correct`, `␣correctly`, `␣correction`, `Correct`, `␣corrected`, `␣correcting`, `正确`, `正确的`, `纠正`, `对的` | 2/152 (1%) | 2/81 (2%) | 10/138 (7%) | 11/158 (7%) |
| trick (tricking someone) | lie | `␣trick`, `␣tricks` | 1/152 (1%) | 2/81 (2%) | 2/138 (1%) | 0/158 (0%) |
| hide (hiding something / being hidden) | lie | `隐藏`, `␣hide`, `␣hiding`, `␣hides`, `_hide`, `-hide`, `␣hidden`, `hidden`, `隱藏`, `藏着`, `隐藏的` | 2/152 (1%) | 1/81 (1%) | 7/138 (5%) | 0/158 (0%) |
| downplay (downplaying, glossing over) | lie | `淡化` | 0/152 (0%) | 3/81 (4%) | 0/138 (0%) | 0/158 (0%) |
| exaggerate (exaggerating) | lie | `夸大`, `␣exaggerated`, `夸张` | 1/152 (1%) | 2/81 (2%) | 0/138 (0%) | 0/158 (0%) |
| unethical (unethical) | lie | `␣unethical` | 0/152 (0%) | 3/81 (4%) | 0/138 (0%) | 0/158 (0%) |
| placate (placating, soothing) | unclear | `安抚` | 0/152 (0%) | 3/81 (4%) | 3/138 (2%) | 0/158 (0%) |
| fraud (a fraud or scam) | lie | `欺诈` | 1/152 (1%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) |
| secret (something kept secret) | lie | `秘密`, `␣secret`, `␣Secret`, `Secret`, `secret`, `␣secretly` | 1/152 (1%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) |
| confidential (kept confidential) | unclear | `保密`, `␣confidentiality` | 2/152 (1%) | 0/81 (0%) | 3/138 (2%) | 0/158 (0%) |
| ostensibly (on the surface, ostensibly) | unclear | `表面上` | 1/152 (1%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) |
| integrity (integrity, uprightness) | truth | `␣integrity`, `␣Integrity` | 1/152 (1%) | 1/81 (1%) | 1/138 (1%) | 0/158 (0%) |
| confident (confident) | unclear | `␣confidence`, `confidence`, `␣Confidence`, `自信`, `-confidence` | 1/152 (1%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) |
| fake (fake, counterfeit) | lie | `fake` | 2/152 (1%) | 0/81 (0%) | 1/138 (1%) | 0/158 (0%) |
| inaccurate (inaccurate) | lie | `准确性和`, `不准确` | 0/152 (0%) | 2/81 (2%) | 0/138 (0%) | 0/158 (0%) |
| refuse (refusing) | unclear | `␣refusal`, `␣refused`, `拒绝` | 0/152 (0%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) |
| evade (evading, dodging) | lie | `␣evasion` | 1/152 (1%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) |
| distort (distorting) | lie | `␣distort` | 0/152 (0%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) |
| spin (putting a slant on facts) | lie | `␣spin`, `Spin`, `spin`, `-spin`, `␣spins`, `␣Spin`, `_spin`, `.spin`, `␣spinning`, `-spinner` | 0/152 (0%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) |
| excuse (an excuse or pretext) | unclear | `借口` | 0/152 (0%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) |
| apologize (apologizing) | unclear | `抱歉` | 1/152 (1%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) |
| scripted (pre-written, scripted wording) | unclear | `套用` | 0/152 (0%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) |
| indirect (indirect) | unclear | `␣indirectly` | 1/152 (1%) | 0/81 (0%) | 0/138 (0%) | 0/158 (0%) |
| outright (outright, openly) | unclear | `␣outright` | 0/152 (0%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) |
| conscience (conscience) | unclear | `␣conscience` | 0/152 (0%) | 1/81 (1%) | 0/138 (0%) | 0/158 (0%) |

Not in the draft: perfunctory (held back: no undisputed member left); admit (excluded: admit / deny / acknowledge); acknowledge (excluded: admit / deny / acknowledge); coax (held back: no undisputed member left)
