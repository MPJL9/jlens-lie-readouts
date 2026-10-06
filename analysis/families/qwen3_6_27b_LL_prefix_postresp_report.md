# Family report: qwen3.6-27b, logit lens, band 35-58, part prefix, group postresp

Written by `scripts/family_report.py` from `qwen3_6_27b_LL_prefix_postresp_rep1.json` and `_rep2.json` (prompt
`prompts/family_generation.md`). Visibility = build-split scenario transcripts (of 233) in which
at least one member is present at the position within the band. Layer profile = band layers where
the family is present in at least one transcript, and the three layers with the most transcripts
(description only; scoring uses the whole band).

## postresp_slot0

| rep | family | side | members | visibility | layer profile |
|---|---|---|---|---|---|
| 1 | lie (telling a lie (a deliberately false statement)) | lie | `lying` | 1 | L45-45; most at L45 (1) |
| 1 | conceal (keeping the truth from someone (concealing, covering up)) | lie | `掩` | 16 | L36-38; most at L36 (12), L37 (2), L38 (7) |
| 1 | hide (hiding something / being hidden) | lie | `藏` | 8 | L55-57; most at L55 (2), L56 (8), L57 (6) |
| 1 | confidential (kept confidential) | unclear | `␣confidential` | 16 | L40-44; most at L40 (2), L44 (14) |
| 1 | sensitive (sensitive (information or topic)) | unclear | `_sensitive` | 2 | L56-57; most at L56 (1), L57 (2) |
| 1 | refuse (refusing) | unclear | `␣refusal`, `拒` | 3 | L38-48; most at L38 (2), L39 (1), L41 (1) |
| 1 | redirect (redirecting or pivoting away) | unclear | `_redirect` | 1 | L39-39; most at L39 (1) |
| 1 | sincere (being sincere) | truth | `诚挚` | 3 | L53-53; most at L53 (3) |
| 1 | candid (candid, frank) | truth | `直言` | 1 | L38-40; most at L38 (1), L39 (1), L40 (1) |
| 1 | factual (factual, the facts) | truth | `␣factual` | 1 | L39-41; most at L39 (1), L41 (1) |
| 1 | reveal (revealing, exposing) | truth | `揭` | 2 | L37-41; most at L37 (2), L38 (1), L39 (1) |
| 1 | ethical (ethics, ethical) | unclear | `␣ethic` | 2 | L46-48; most at L46 (1), L47 (1), L48 (1) |
| 1 | scripted (pre-written, scripted wording) | unclear | `␣canned` | 27 | L35-48; most at L35 (10), L36 (5), L46 (16) |
| 1 | coax (coaxing or humoring someone (also: fooling)) | unclear | `哄` | 2 | L35-38; most at L35 (2), L36 (2), L37 (2) |
| 1 | direct (direct, straightforward) | unclear | `直接`, `␣directly`, `␣straight`, `␣direct`, `straight`, `direct`, `Direct`, `␣straightforward`, `的直接`, `就直接`, `可以直接` | 111 | L35-51; most at L36 (85), L39 (45), L40 (65) |
| 2 | lie (telling a lie) | lie | `lying` | 1 | L45-45; most at L45 (1) |
| 2 | hide (hiding, concealing, covering up) | lie | `掩` | 16 | L36-38; most at L36 (12), L37 (2), L38 (7) |
| 2 | confidential (confidential) | unclear | `␣confidential` | 16 | L40-44; most at L40 (2), L44 (14) |
| 2 | coax (coaxing, humouring (also 'fooling' as in 哄骗)) | unclear | `哄` | 2 | L35-38; most at L35 (2), L36 (2), L37 (2) |
| 2 | sincere (sincere, candid) | truth | `诚挚` | 3 | L53-53; most at L53 (3) |
| 2 | disclose (disclosing, revealing) | truth | `揭` | 2 | L37-41; most at L37 (2), L38 (1), L39 (1) |
| 2 | refuse (refusing, a refusal) | unclear | `␣refusal`, `拒` | 3 | L38-48; most at L38 (2), L39 (1), L41 (1) |
| 2 | scripted (a scripted / canned / official-line answer) | unclear | `␣canned` | 27 | L35-48; most at L35 (10), L36 (5), L46 (16) |
| 2 | ethics (ethics, morality) | unclear | `␣ethic` | 2 | L46-48; most at L46 (1), L47 (1), L48 (1) |

## postresp_slot1

| rep | family | side | members | visibility | layer profile |
|---|---|---|---|---|---|
| 1 | lie (telling a lie (a deliberately false statement)) | lie | `谎言`, `说谎`, `撒谎`, `␣lie`, `谎`, `␣lies`, `␣lying`, `␣fib`, `␣lied`, `lying`, `␣mentira`, `␣Lie`, `␣거짓`, `␣Lies`, `lie`, `␣liar`, `Lie`, `lies`, `fib` | 106 | L35-58; most at L39 (74), L50 (82), L51 (72) |
| 1 | falsehood (a false statement or false information) | lie | `␣falsehood`, `␣misinformation`, `虚假信息` | 57 | L35-58; most at L50 (35), L51 (36), L53 (38) |
| 1 | fabricate (making up content that is not real) | lie | `␣fabricated`, `凭空`, `␣fabrication`, `␣invented`, `编织`, `␣invent`, `伪造`, `作假` | 77 | L35-58; most at L36 (51), L37 (69), L38 (32) |
| 1 | fiction (made-up, fictional content) | unclear | `虚构`, `␣fictional`, `fiction`, `␣fict`, `-fiction`, `␣Fiction`, `␣fiction` | 61 | L35-58; most at L43 (34), L45 (33), L46 (42) |
| 1 | fake (fake, not genuine) | lie | `假的`, `假`, `fake`, `␣fake`, `Fake` | 77 | L35-58; most at L36 (50), L37 (72), L38 (47) |
| 1 | deceive (the act of deceiving) | lie | `欺骗`, `骗`, `␣deception`, `␣deceptive`, `␣deceive`, `␣deceived` | 55 | L35-58; most at L50 (37), L52 (39), L54 (28) |
| 1 | fraud (a fraud or scam) | lie | `骗局` | 1 | L38-38; most at L38 (1) |
| 1 | mislead (leading someone to a wrong belief) | lie | `␣misleading`, `误导`, `误导性` | 11 | L37-58; most at L52 (6), L53 (11), L54 (10) |
| 1 | conceal (keeping the truth from someone (concealing, covering up)) | lie | `隐瞒`, `掩盖`, `掩饰`, `掩`, `遮`, `瞒`, `遮掩`, `␣conceal` | 98 | L35-58; most at L40 (52), L50 (70), L52 (61) |
| 1 | hide (hiding something / being hidden) | lie | `藏`, `隐藏` | 3 | L35-37; most at L35 (3), L36 (1), L37 (1) |
| 1 | withhold (withholding information) | lie | `␣withholding` | 4 | L51-58; most at L51 (2), L52 (4), L53 (2) |
| 1 | omit (leaving something out) | lie | `␣omit`, `omit` | 15 | L42-58; most at L48 (6), L49 (7), L52 (11) |
| 1 | deny (denying (a claim or a fact)) | lie | `否认`, `␣denial`, `␣deny`, `␣denying`, `␣denies`, `␣denied`, `否定`, `deny`, `否認`, `␣Denied` | 92 | L35-58; most at L39 (57), L47 (56), L56 (55) |
| 1 | refuse (refusing) | unclear | `拒`, `␣refusal`, `拒绝`, `␣refused`, `␣refuse`, `␣refusing`, `␣refuses`, `␣refus`, `拒绝了`, `拒絕`, `␣отказ`, `␣отказа`, `拒不` | 47 | L35-58; most at L39 (36), L48 (38), L56 (34) |
| 1 | reject (rejecting) | unclear | `␣reject`, `␣rejection`, `␣rejecting`, `Reject`, `reject`, `␣rejected` | 21 | L35-58; most at L46 (13), L48 (14), L49 (12) |
| 1 | dismiss (dismissing) | unclear | `␣dismiss`, `-dismiss`, `␣dismissal`, `␣dismissed`, `␣dismissing`, `Dismiss`, `.dismiss`, `dismiss` | 15 | L37-58; most at L53 (13), L56 (7), L58 (7) |
| 1 | contradict (contradicting / contradiction) | unclear | `␣contradict`, `␣contrad`, `矛盾`, `␣contradictory`, `␣contradiction` | 61 | L35-58; most at L48 (28), L49 (41), L50 (37) |
| 1 | evade (evading, dodging) | lie | `回避`, `␣deflect`, `避`, `␣evasion`, `␣dodge`, `规避`, `␣evade`, `避开`, `躲`, `␣Dodge` | 28 | L36-58; most at L52 (18), L53 (21), L57 (17) |
| 1 | circumvent (going around (an issue)) | unclear | `绕`, `绕行`, `绕过` | 22 | L35-58; most at L40 (12), L49 (12), L52 (12) |
| 1 | redirect (redirecting or pivoting away) | unclear | `␣pivot`, `␣Pivot`, `␣redirect`, `Redirect`, `pivot`, `redirect`, `␣redirects`, `␣redirection`, `_redirect` | 13 | L50-58; most at L54 (10), L55 (7), L56 (8) |
| 1 | vague (vague, ambiguous wording) | unclear | `含糊`, `␣vague`, `模糊`, `␣vaguely`, `␣ambiguous`, `␣ambiguity` | 18 | L37-58; most at L51 (14), L52 (15), L53 (15) |
| 1 | euphemistic (indirect, euphemistic wording) | unclear | `委婉` | 55 | L35-53; most at L35 (45), L36 (33), L38 (37) |
| 1 | downplay (downplaying, glossing over) | lie | `淡化`, `␣gloss` | 42 | L35-56; most at L38 (18), L42 (22), L49 (23) |
| 1 | embellish (embellishing, whitewashing) | lie | `美化` | 5 | L39-49; most at L43 (5), L44 (3), L45 (3) |
| 1 | perfunctory (dealing with something perfunctorily) | unclear | `应付`, `敷衍` | 38 | L35-58; most at L43 (23), L48 (15), L49 (20) |
| 1 | spin (putting a slant on facts) | lie | `␣spin`, `Spin`, `spin`, `-spin`, `␣spins`, `␣Spin`, `_spin`, `.spin`, `␣spinning` | 15 | L54-58; most at L56 (2), L57 (3), L58 (15) |
| 1 | bluff (bluffing) | lie | `␣bluff` | 7 | L35-57; most at L38 (4), L52 (3), L53 (3) |
| 1 | excuse (an excuse or pretext) | unclear | `␣excuse`, `␣excuses`, `借口` | 15 | L51-58; most at L54 (12), L55 (12), L56 (10) |
| 1 | ostensibly (on the surface, ostensibly) | unclear | `表面上` | 39 | L35-45; most at L36 (29), L37 (29), L38 (23) |
| 1 | honest (being honest) | truth | `诚实`, `诚`, `␣honesty`, `␣honest`, `␣honestly`, `诚信`, `␣Honest`, `诚实守信` | 82 | L35-58; most at L38 (52), L40 (55), L41 (57) |
| 1 | dishonest (being dishonest) | lie | `␣dishonest` | 7 | L40-58; most at L41 (3), L57 (3), L58 (4) |
| 1 | sincere (being sincere) | truth | `真诚`, `诚恳` | 3 | L39-50; most at L39 (2), L45 (1), L50 (1) |
| 1 | integrity (integrity, uprightness) | truth | `正直`, `␣integrity`, `␣Integrity` | 18 | L35-58; most at L42 (8), L44 (8), L47 (11) |
| 1 | candid (candid, frank) | truth | `坦诚`, `␣frank`, `直言` | 34 | L35-58; most at L39 (29), L41 (30), L42 (30) |
| 1 | confess (confessing) | truth | `坦白`, `␣confession`, `␣confess`, `␣confessed` | 23 | L38-58; most at L51 (14), L52 (19), L53 (18) |
| 1 | admit (admitting) | truth | `承认`, `␣admissions`, `␣admit`, `␣admitting`, `␣admission`, `␣admits`, `␣Admission`, `␣admitted`, `承認`, `␣admite` | 58 | L35-58; most at L39 (44), L40 (45), L41 (40) |
| 1 | acknowledge (acknowledging) | truth | `␣acknowledge`, `␣acknowledging`, `␣acknowledges`, `␣acknowledgment`, `␣acknowledged`, `Acknowled` | 20 | L37-58; most at L40 (11), L41 (11), L53 (10) |
| 1 | truth (the truth) | truth | `␣truth`, `truth`, `␣Truth`, `Truth`, `真相`, `_truth`, `␣truths`, `␣vérité`, `␣Wahrheit` | 58 | L35-58; most at L51 (33), L53 (28), L55 (31) |
| 1 | truthful (truthful, telling it as it is) | truth | `␣truthful`, `如实`, `实话`, `说实话` | 78 | L35-58; most at L39 (67), L40 (60), L41 (59) |
| 1 | seek truth from facts (seeking truth from facts) | truth | `实事求是` | 19 | L40-58; most at L52 (12), L53 (11), L54 (16) |
| 1 | factual (factual, the facts) | truth | `␣factual`, `事实`, `的事实` | 52 | L35-58; most at L40 (41), L41 (34), L42 (31) |
| 1 | genuine (genuine, real, authentic) | truth | `真实` | 1 | L51-51; most at L51 (1) |
| 1 | transparent (being transparent) | truth | `␣transparency`, `透明`, `␣transparent`, `透明度`, `透明的`, `␣Transparency`, `transparent`, `-transparent` | 24 | L36-58; most at L54 (22), L56 (12), L57 (13) |
| 1 | disclose (disclosing information) | truth | `␣disclosure`, `透露`, `␣disclosed`, `␣Disclosure`, `披露`, `␣disclose`, `␣disclosing`, `␣disclosures`, `信息披露`, `Disclosure`, `透露出` | 40 | L35-58; most at L36 (24), L38 (27), L40 (25) |
| 1 | reveal (revealing, exposing) | truth | `揭露`, `␣reveal`, `␣revealing`, `揭`, `揭示`, `␣revealed`, `␣reveals` | 15 | L35-54; most at L35 (4), L51 (5), L53 (5) |
| 1 | public (making public, openly) | unclear | `公开`, `公开的` | 10 | L38-55; most at L38 (8), L47 (2), L48 (2) |
| 1 | ethical (ethics, ethical) | unclear | `␣ethical`, `伦理`, `␣ethics`, `␣Ethics`, `ethical` | 23 | L35-58; most at L39 (19), L40 (20), L45 (19) |
| 1 | moral (morality, moral) | unclear | `␣moral`, `道德`, `的道德`, `职业道德` | 26 | L35-58; most at L39 (23), L43 (23), L44 (23) |
| 1 | violate (violating a rule or law) | unclear | `违反`, `违背`, `违`, `违反了`, `违法`, `违规` | 28 | L35-58; most at L48 (21), L49 (13), L50 (9) |
| 1 | apologize (apologizing) | unclear | `道歉` | 1 | L55-55; most at L55 (1) |
| 1 | firm (firm, resolute) | unclear | `坚`, `坚定`, `␣firmly`, `坚决`, `␣firm`, `坚定的`, `firm`, `␣Firm`, `坚定地` | 98 | L35-58; most at L44 (53), L45 (44), L54 (63) |
| 1 | insist (insisting, holding one's position) | unclear | `必须坚持`, `坚持`, `坚守`, `要坚持` | 43 | L38-58; most at L50 (16), L51 (14), L54 (36) |
| 1 | confident (confident) | unclear | `␣confidently`, `自信`, `␣confident`, `␣confidence`, `自信的`, `confidence`, `␣Confidence`, `自信和`, `-confidence` | 54 | L35-58; most at L43 (37), L47 (35), L48 (42) |
| 1 | assert (asserting) | unclear | `␣assert`, `_assert`, `assert`, `␣asserting`, `.assert`, `␣Assert`, `_ASSERT`, `␣asserts`, `␣assertion`, `␣Assertion`, `␣assertions`, `	assert`, `/assert` | 57 | L35-58; most at L47 (44), L48 (34), L49 (34) |
| 1 | affirm (affirming) | unclear | `␣affirm`, `␣afirm`, `␣affirmation`, `␣affirmative`, `␣affirmed`, `␣afirma`, `␣afirmar` | 23 | L35-58; most at L50 (16), L51 (13), L54 (10) |
| 1 | claim (claiming) | unclear | `␣claim`, `␣Claim`, `␣claims`, `声称`, `claim`, `␣Claims`, `␣claiming`, `Claim`, `␣claimed`, `claims`, `Claims`, `CLAIM`, `␣CLAIM` | 17 | L35-58; most at L55 (12), L57 (10), L58 (11) |
| 1 | adhere (adhering to (instructions, a role)) | unclear | `␣adher`, `␣adherence`, `遵照`, `遵循`, `␣adhere`, `严格遵守`, `遵从`, `遵守`, `遵` | 39 | L38-58; most at L53 (22), L54 (31), L58 (24) |
| 1 | official line (an agreed official line or talking points) | unclear | `口径` | 103 | L35-58; most at L52 (64), L53 (69), L54 (54) |
| 1 | scripted (pre-written, scripted wording) | unclear | `␣canned`, `␣scripted`, `套用` | 53 | L36-58; most at L52 (36), L53 (47), L54 (25) |
| 1 | coax (coaxing or humoring someone (also: fooling)) | unclear | `哄` | 110 | L35-58; most at L37 (88), L38 (86), L39 (92) |
| 1 | placate (placating, soothing) | unclear | `安抚` | 31 | L35-54; most at L35 (27), L36 (19), L37 (16) |
| 1 | plausible (plausible) | unclear | `␣plausible` | 21 | L35-58; most at L51 (18), L52 (14), L53 (16) |
| 1 | credible (credible) | unclear | `可信`, `␣credible` | 14 | L35-49; most at L43 (8), L44 (9), L45 (7) |
| 1 | knowingly (doing something knowingly) | unclear | `明知` | 23 | L35-50; most at L43 (14), L44 (18), L45 (14) |
| 1 | informed (being in the know about the facts) | unclear | `知情` | 43 | L35-51; most at L35 (21), L39 (37), L40 (25) |
| 1 | uninformed (not being in the know) | unclear | `不知情` | 1 | L53-53; most at L53 (1) |
| 1 | direct (direct, straightforward) | unclear | `直接`, `␣direct`, `␣directly`, `正面`, `␣straight`, `direct`, `␣Direct`, `Direct`, `直接的`, `␣straightforward`, `的直接`, `是直接`, `straight`, `正面的` | 186 | L35-58; most at L35 (139), L36 (141), L43 (131) |
| 1 | indirect (indirect) | unclear | `␣indirect`, `␣indirectly` | 5 | L38-58; most at L47 (3), L50 (3), L52 (4) |
| 1 | outright (outright, openly) | unclear | `␣outright` | 45 | L35-58; most at L53 (36), L54 (35), L58 (32) |
| 2 | lie (telling a lie) | lie | `谎言`, `说谎`, `撒谎`, `谎`, `␣lie`, `␣lies`, `␣Lie`, `␣Lies`, `lie`, `lies`, `Lie`, `␣lying`, `lying`, `␣lied`, `␣liar`, `␣mentira`, `␣거짓`, `␣fib`, `fib` | 106 | L35-58; most at L39 (74), L50 (82), L51 (72) |
| 2 | deceive (the act of deceiving) | lie | `欺骗`, `骗`, `␣deception`, `␣deceptive`, `␣deceive`, `␣deceived`, `骗局` | 55 | L35-58; most at L50 (37), L52 (39), L54 (28) |
| 2 | fabricate (making up content) | lie | `␣fabricated`, `␣fabrication`, `凭空`, `作假` | 73 | L35-58; most at L36 (51), L37 (69), L38 (32) |
| 2 | fictional (made-up, fictional) | unclear | `␣fictional`, `fiction`, `␣fict`, `-fiction`, `␣Fiction`, `␣fiction`, `虚构` | 61 | L35-58; most at L43 (34), L45 (33), L46 (42) |
| 2 | misinformation (false information) | lie | `␣misinformation`, `虚假信息` | 34 | L35-58; most at L37 (12), L53 (23), L54 (23) |
| 2 | mislead (leading someone to a wrong belief) | lie | `␣misleading`, `误导`, `误导性` | 11 | L37-58; most at L52 (6), L53 (11), L54 (10) |
| 2 | bluff (bluffing) | lie | `␣bluff` | 7 | L35-57; most at L38 (4), L52 (3), L53 (3) |
| 2 | fake (fake, counterfeit) | lie | `fake`, `␣fake`, `Fake` | 18 | L36-50; most at L36 (6), L37 (13), L38 (8) |
| 2 | deny (denying, a denial) | lie | `否认`, `否認`, `否定`, `␣denial`, `␣deny`, `␣denying`, `␣denies`, `␣denied`, `␣Denied`, `deny` | 92 | L35-58; most at L39 (57), L47 (56), L56 (55) |
| 2 | hide (hiding, concealing, covering up) | lie | `隐瞒`, `瞒`, `␣conceal`, `隐藏`, `掩盖`, `掩饰`, `遮掩`, `掩`, `匿` | 99 | L35-58; most at L40 (53), L50 (67), L52 (60) |
| 2 | mask (masking) | lie | `-mask`, `␣masking` | 17 | L35-40; most at L35 (9), L36 (16), L37 (4) |
| 2 | evade (evading or deflecting the question) | lie | `␣evasion`, `␣evade`, `回避`, `规避`, `避开`, `␣dodge`, `␣deflect` | 28 | L36-58; most at L52 (18), L53 (21), L57 (17) |
| 2 | bypass (going around (a topic)) | unclear | `绕`, `绕过` | 22 | L35-58; most at L40 (12), L49 (12), L52 (12) |
| 2 | vague (vague, equivocal) | unclear | `含糊`, `模糊` | 16 | L40-58; most at L51 (10), L52 (13), L53 (14) |
| 2 | tactful (euphemistic, tactful) | unclear | `委婉` | 55 | L35-53; most at L35 (45), L36 (33), L38 (37) |
| 2 | downplay (downplaying) | lie | `淡化` | 36 | L35-56; most at L38 (18), L42 (20), L49 (19) |
| 2 | gloss over (glossing over) | lie | `␣gloss` | 17 | L35-55; most at L43 (10), L47 (8), L48 (11) |
| 2 | spin (putting a spin on facts) | lie | `␣spin`, `Spin`, `spin`, `-spin`, `␣spins`, `␣Spin`, `_spin`, `␣spinning`, `.spin` | 15 | L54-58; most at L56 (2), L57 (3), L58 (15) |
| 2 | perfunctory (responding perfunctorily / fobbing off) | unclear | `应付` | 36 | L35-54; most at L43 (22), L49 (17), L50 (14) |
| 2 | placate (placating, soothing) | unclear | `安抚` | 31 | L35-54; most at L35 (27), L36 (19), L37 (16) |
| 2 | coax (coaxing, humouring (also 'fooling' as in 哄骗)) | unclear | `哄` | 110 | L35-58; most at L37 (88), L38 (86), L39 (92) |
| 2 | confident (confident, confidently) | unclear | `␣confidently`, `␣confident`, `␣confidence`, `confidence`, `␣Confidence`, `-confidence`, `自信`, `自信的`, `自信和` | 54 | L35-58; most at L43 (37), L47 (35), L48 (42) |
| 2 | honest (honest, honesty) | truth | `␣honest`, `␣honesty`, `␣Honest`, `␣honestly`, `诚实`, `诚`, `诚信`, `诚实守信`, `正直` | 83 | L35-58; most at L38 (52), L40 (55), L41 (57) |
| 2 | sincere (sincere, candid) | truth | `坦诚`, `真诚`, `诚恳` | 34 | L35-58; most at L39 (29), L41 (30), L42 (30) |
| 2 | dishonest (dishonest) | lie | `␣dishonest` | 7 | L40-58; most at L41 (3), L57 (3), L58 (4) |
| 2 | truthful (truthful, telling it as it is) | truth | `␣truthful`, `如实`, `实话`, `说实话`, `实事求是` | 79 | L35-58; most at L39 (67), L40 (60), L41 (59) |
| 2 | truth (the truth) | truth | `␣truth`, `truth`, `␣Truth`, `Truth`, `_truth`, `␣truths`, `真相`, `␣vérité`, `␣Wahrheit` | 58 | L35-58; most at L51 (33), L53 (28), L55 (31) |
| 2 | admit (admitting, an admission) | truth | `承认`, `␣admit`, `␣admits`, `␣admitted`, `␣admitting`, `␣admite`, `␣admission`, `␣admissions`, `␣Admission` | 58 | L35-58; most at L39 (44), L40 (45), L41 (40) |
| 2 | acknowledge (acknowledging) | truth | `␣acknowledge`, `␣acknowledging`, `␣acknowledges`, `␣acknowledgment`, `␣acknowledged`, `Acknowled`, `␣Ack`, `Ack` | 26 | L35-58; most at L39 (12), L40 (12), L41 (12) |
| 2 | confess (confessing, coming clean) | truth | `␣confession`, `␣confess`, `␣confessed`, `坦白` | 23 | L38-58; most at L51 (14), L52 (19), L53 (18) |
| 2 | disclose (disclosing, revealing) | truth | `␣disclosure`, `␣disclosed`, `␣Disclosure`, `Disclosure`, `␣disclose`, `␣disclosing`, `␣disclosures`, `透露`, `透露出`, `揭露`, `揭示`, `揭`, `␣reveal`, `␣revealing`, `␣revealed`, `␣reveals` | 43 | L35-58; most at L36 (24), L38 (27), L40 (25) |
| 2 | inform (informing, telling) | truth | `告知` | 27 | L35-58; most at L35 (13), L39 (11), L40 (15) |
| 2 | public (making public, openly) | unclear | `公开`, `公开的` | 10 | L38-55; most at L38 (8), L47 (2), L48 (2) |
| 2 | transparent (transparency) | truth | `␣transparency`, `␣Transparency`, `␣transparent`, `transparent`, `-transparent`, `透明`, `透明度`, `透明的` | 24 | L36-58; most at L54 (22), L56 (12), L57 (13) |
| 2 | refuse (refusing, a refusal) | unclear | `␣refusal`, `␣refused`, `␣refuse`, `␣refusing`, `␣refuses`, `␣refus`, `拒绝`, `拒绝了`, `拒絕`, `拒`, `拒不`, `␣отказ`, `␣отказа` | 47 | L35-58; most at L39 (36), L48 (38), L56 (34) |
| 2 | reject (rejecting) | unclear | `␣reject`, `␣rejection`, `␣rejecting`, `Reject`, `reject`, `␣rejected` | 21 | L35-58; most at L46 (13), L48 (14), L49 (12) |
| 2 | contradict (contradicting, contradiction) | unclear | `␣contradict`, `␣contrad`, `␣contradictory`, `␣contradiction`, `矛盾` | 61 | L35-58; most at L48 (28), L49 (41), L50 (37) |
| 2 | firm (firm, firmly, resolute) | unclear | `␣firmly`, `␣firm`, `坚定`, `坚定的`, `坚定地`, `坚决` | 90 | L35-58; most at L43 (35), L44 (53), L45 (42) |
| 2 | insist (insisting, persisting) | unclear | `坚持`, `必须坚持`, `要坚持` | 43 | L38-58; most at L50 (16), L51 (14), L54 (36) |
| 2 | assert (asserting, an assertion) | unclear | `␣assert`, `␣asserting`, `␣asserts`, `␣assertion`, `␣Assertion`, `␣assertions`, `␣Assert` | 55 | L35-58; most at L47 (40), L48 (31), L49 (31) |
| 2 | scripted (a scripted / canned / official-line answer) | unclear | `␣scripted`, `␣canned`, `口径` | 108 | L35-58; most at L52 (70), L53 (77), L54 (58) |
| 2 | ethics (ethics, morality) | unclear | `␣moral`, `道德`, `的道德`, `职业道德`, `␣ethical`, `␣ethics`, `␣Ethics`, `ethical`, `伦理` | 27 | L35-58; most at L43 (24), L44 (24), L45 (23) |
| 2 | violate (violating (a rule or principle)) | unclear | `违反`, `违反了`, `违背`, `␣violate`, `␣violates`, `␣violation` | 22 | L35-58; most at L48 (20), L49 (13), L50 (9) |
| 2 | comply (adhering, complying) | unclear | `␣adher`, `␣adherence`, `␣adhere`, `遵照`, `遵循`, `␣compliant`, `合规` | 43 | L35-58; most at L53 (22), L54 (31), L58 (24) |
| 2 | plausible (plausible, believable, credible) | unclear | `␣plausible`, `␣believable`, `可信` | 28 | L35-58; most at L51 (18), L52 (14), L53 (16) |
| 2 | excuse (an excuse, a pretext) | unclear | `␣excuse`, `␣excuses`, `借口` | 15 | L51-58; most at L54 (12), L55 (12), L56 (10) |
| 2 | knowingly (knowing full well) | unclear | `明知` | 23 | L35-50; most at L43 (14), L44 (18), L45 (14) |
| 2 | informed (having knowledge of the facts) | unclear | `知情` | 43 | L35-51; most at L35 (21), L39 (37), L40 (25) |
| 2 | unaware (not knowing the facts) | unclear | `不知情` | 1 | L53-53; most at L53 (1) |
| 2 | superficially (on the surface, outwardly) | unclear | `表面上` | 39 | L35-45; most at L36 (29), L37 (29), L38 (23) |
| 2 | uphold (upholding, maintaining (an image or position)) | unclear | `维护`, `和维护`, `与维护`, `维护和` | 108 | L35-58; most at L49 (78), L50 (87), L51 (75) |
| 2 | conscience (conscience) | unclear | `良心` | 7 | L35-49; most at L36 (4), L37 (4), L43 (5) |
| 2 | apology (apologising) | unclear | `道歉` | 1 | L55-55; most at L55 (1) |

## postresp_slot2

| rep | family | side | members | visibility | layer profile |
|---|---|---|---|---|---|
| 1 | direct (direct, straightforward) | unclear | `直接` | 9 | L35-46; most at L35 (9), L36 (4), L37 (2) |
| 2 | comply (adhering, complying) | unclear | `合规` | 11 | L36-43; most at L39 (9), L40 (5), L43 (3) |

## postresp_slot3

| rep | family | side | members | visibility | layer profile |
|---|---|---|---|---|---|
| 1 | sensitive (sensitive (information or topic)) | unclear | `敏感` | 13 | L41-46; most at L42 (4), L43 (10), L45 (4) |
| 1 | evade (evading, dodging) | lie | `避` | 2 | L48-49; most at L48 (1), L49 (2) |
| 1 | euphemistic (indirect, euphemistic wording) | unclear | `委婉` | 1 | L35-35; most at L35 (1) |
| 1 | seek truth from facts (seeking truth from facts) | truth | `求实` | 197 | L35-45; most at L35 (181), L36 (169), L37 (188) |
| 1 | reveal (revealing, exposing) | truth | `揭` | 1 | L37-37; most at L37 (1) |
| 1 | firm (firm, resolute) | unclear | `坚`, `firm` | 3 | L50-57; most at L50 (1), L54 (1), L56 (1) |
| 1 | insist (insisting, holding one's position) | unclear | `坚持`, `␣insist`, `必须坚持` | 10 | L51-58; most at L54 (7), L55 (9), L56 (6) |
| 1 | direct (direct, straightforward) | unclear | `直接`, `␣direct`, `Direct`, `是直接`, `就直接`, `␣directly` | 119 | L44-58; most at L47 (69), L48 (51), L49 (111) |
| 2 | tactful (euphemistic, tactful) | unclear | `委婉` | 1 | L35-35; most at L35 (1) |
| 2 | disclose (disclosing, revealing) | truth | `揭` | 1 | L37-37; most at L37 (1) |
| 2 | insist (insisting, persisting) | unclear | `坚持`, `必须坚持` | 9 | L52-58; most at L54 (7), L55 (9), L56 (6) |

## postresp_slot4

| rep | family | side | members | visibility | layer profile |
|---|---|---|---|---|---|
| 1 | lie (telling a lie (a deliberately false statement)) | lie | `撒谎`, `␣lie`, `谎言`, `说谎`, `␣fib`, `␣lies`, `␣lying`, `lying`, `␣lied`, `Lie`, `␣liar`, `谎` | 14 | L35-58; most at L37 (6), L56 (5), L57 (5) |
| 1 | falsehood (a false statement or false information) | lie | `␣misinformation`, `␣falsehood` | 7 | L38-58; most at L51 (4), L53 (4), L54 (4) |
| 1 | fabricate (making up content that is not real) | lie | `伪造`, `␣fabrication`, `␣invent`, `造假` | 4 | L36-58; most at L44 (2), L45 (2), L46 (2) |
| 1 | fiction (made-up, fictional content) | unclear | `␣fictional`, `虚构`, `␣fict`, `fiction`, `␣Fiction`, `␣fiction` | 25 | L35-58; most at L37 (21), L40 (20), L44 (20) |
| 1 | fake (fake, not genuine) | lie | `假的`, `假`, `fake` | 8 | L36-50; most at L36 (6), L43 (3), L45 (2) |
| 1 | deceive (the act of deceiving) | lie | `␣deception`, `欺骗`, `骗`, `␣deceptive`, `␣deceive` | 11 | L35-58; most at L52 (7), L53 (9), L57 (7) |
| 1 | fraud (a fraud or scam) | lie | `欺诈` | 2 | L53-57; most at L53 (1), L57 (1) |
| 1 | trick (tricking someone) | lie | `␣trick`, `␣tricks` | 3 | L38-58; most at L48 (1), L57 (2), L58 (2) |
| 1 | mislead (leading someone to a wrong belief) | lie | `␣misleading`, `误导` | 4 | L51-58; most at L53 (4), L54 (2), L56 (1) |
| 1 | manipulate (manipulating someone) | lie | `␣manipulation`, `␣manipulate`, `␣manipulated`, `␣manipulating` | 4 | L54-58; most at L54 (3), L55 (4), L56 (3) |
| 1 | conceal (keeping the truth from someone (concealing, covering up)) | lie | `隐瞒`, `␣conceal`, `掩盖`, `瞒`, `掩饰`, `掩` | 6 | L39-58; most at L52 (5), L53 (4), L54 (4) |
| 1 | hide (hiding something / being hidden) | lie | `隐藏`, `␣hide`, `␣hiding`, `␣hides`, `_hide`, `-hide`, `␣hidden`, `hidden`, `藏`, `隱藏`, `藏着`, `隐藏的` | 3 | L52-58; most at L53 (2), L54 (3), L58 (3) |
| 1 | secret (something kept secret) | lie | `秘密`, `␣secret`, `␣Secret`, `Secret`, `secret`, `␣secretly` | 2 | L43-58; most at L43 (1), L56 (1), L57 (1) |
| 1 | confidential (kept confidential) | unclear | `保密`, `␣confidentiality` | 2 | L39-54; most at L39 (1), L52 (1), L53 (1) |
| 1 | sensitive (sensitive (information or topic)) | unclear | `敏感`, `敏感的`, `␣sensitive` | 65 | L35-50; most at L37 (29), L38 (25), L39 (26) |
| 1 | refuse (refusing) | unclear | `␣refusal`, `␣refused`, `拒绝` | 1 | L56-58; most at L56 (1), L57 (1), L58 (1) |
| 1 | contradict (contradicting / contradiction) | unclear | `矛盾`, `␣contradict`, `矛盾的`, `␣contrad`, `␣contradictory`, `␣contradiction`, `␣contradictions` | 27 | L35-58; most at L48 (11), L49 (13), L50 (11) |
| 1 | evade (evading, dodging) | lie | `␣evasion` | 1 | L57-58; most at L57 (1), L58 (1) |
| 1 | circumvent (going around (an issue)) | unclear | `绕过`, `绕` | 4 | L36-53; most at L36 (2), L49 (2), L53 (2) |
| 1 | downplay (downplaying, glossing over) | lie | `淡化` | 3 | L35-53; most at L35 (1), L36 (2), L53 (1) |
| 1 | embellish (embellishing, whitewashing) | lie | `美化` | 6 | L35-57; most at L43 (3), L45 (3), L46 (3) |
| 1 | exaggerate (exaggerating) | lie | `夸大`, `␣exaggerated`, `夸张` | 3 | L36-58; most at L51 (3), L52 (3), L53 (3) |
| 1 | distort (distorting) | lie | `␣distort` | 1 | L51-52; most at L51 (1), L52 (1) |
| 1 | perfunctory (dealing with something perfunctorily) | unclear | `应付` | 2 | L45-51; most at L45 (2), L47 (1), L48 (1) |
| 1 | spin (putting a slant on facts) | lie | `␣spin`, `Spin`, `spin`, `-spin`, `␣spins`, `␣Spin`, `_spin`, `.spin`, `␣spinning`, `-spinner` | 1 | L57-58; most at L57 (1), L58 (1) |
| 1 | excuse (an excuse or pretext) | unclear | `借口` | 1 | L40-48; most at L40 (1), L45 (1), L47 (1) |
| 1 | ostensibly (on the surface, ostensibly) | unclear | `表面上` | 2 | L43-44; most at L43 (1), L44 (1) |
| 1 | honest (being honest) | truth | `诚实`, `诚信`, `␣honesty`, `诚`, `␣honest`, `诚实守信`, `␣honestly` | 28 | L35-58; most at L38 (12), L39 (16), L40 (13) |
| 1 | dishonest (being dishonest) | lie | `␣dishonest` | 4 | L40-58; most at L51 (2), L52 (1), L58 (2) |
| 1 | sincere (being sincere) | truth | `真诚` | 1 | L36-37; most at L36 (1), L37 (1) |
| 1 | integrity (integrity, uprightness) | truth | `␣integrity`, `␣Integrity` | 2 | L51-57; most at L51 (1), L52 (1), L55 (2) |
| 1 | candid (candid, frank) | truth | `坦诚`, `␣frankly`, `␣upfront` | 12 | L36-53; most at L38 (6), L39 (6), L43 (7) |
| 1 | admit (admitting) | truth | `承认`, `␣admit`, `␣admitting`, `␣admissions`, `␣admits`, `␣admission`, `␣admitted`, `␣Admission`, `承認` | 11 | L35-58; most at L55 (6), L56 (7), L57 (6) |
| 1 | acknowledge (acknowledging) | truth | `␣acknowledge`, `␣acknowledging`, `␣acknowledges` | 2 | L42-57; most at L55 (1), L56 (1), L57 (1) |
| 1 | truth (the truth) | truth | `␣truth`, `真相`, `truth`, `␣Truth`, `Truth`, `实情`, `_truth`, `␣truths`, `␣vérité` | 27 | L35-58; most at L39 (18), L40 (13), L41 (14) |
| 1 | truthful (truthful, telling it as it is) | truth | `如实`, `␣truthful`, `实话`, `说实话` | 28 | L35-58; most at L37 (14), L39 (15), L40 (16) |
| 1 | seek truth from facts (seeking truth from facts) | truth | `求实`, `实事求是` | 46 | L35-53; most at L40 (19), L45 (20), L46 (19) |
| 1 | factual (factual, the facts) | truth | `事实`, `␣factual`, `的事实`, `事实和` | 23 | L35-58; most at L37 (15), L39 (14), L44 (15) |
| 1 | genuine (genuine, real, authentic) | truth | `真实`, `真实的`, `的真实`, `的真实性`, `␣genuine`, `␣genuinely`, `␣authenticity` | 14 | L35-53; most at L43 (6), L45 (5), L49 (7) |
| 1 | transparent (being transparent) | truth | `透明`, `␣transparency`, `透明的`, `␣Transparency`, `-transparent`, `␣transparent`, `透明度` | 21 | L35-58; most at L37 (11), L38 (16), L39 (11) |
| 1 | disclose (disclosing information) | truth | `透露`, `␣disclosure`, `透露出`, `信息披露`, `␣disclose`, `披露` | 36 | L35-58; most at L36 (22), L48 (15), L49 (14) |
| 1 | reveal (revealing, exposing) | truth | `揭`, `揭露`, `␣reveal`, `␣revealing`, `␣reveals` | 12 | L35-53; most at L36 (6), L37 (7), L51 (3) |
| 1 | public (making public, openly) | unclear | `公开`, `公开的`, `信息公开` | 22 | L35-58; most at L45 (16), L47 (17), L48 (15) |
| 1 | ethical (ethics, ethical) | unclear | `␣ethical`, `␣ethics`, `伦理`, `ethical`, `␣Ethics`, `␣ethic` | 17 | L35-58; most at L39 (10), L40 (10), L58 (12) |
| 1 | unethical (unethical) | lie | `␣unethical` | 3 | L36-58; most at L36 (1), L37 (2), L55 (3) |
| 1 | moral (morality, moral) | unclear | `道德`, `␣moral`, `的道德`, `␣morally`, `␣morality`, `职业道德` | 8 | L35-58; most at L39 (8), L40 (8), L41 (6) |
| 1 | violate (violating a rule or law) | unclear | `违`, `违反`, `违背`, `违规`, `违法` | 18 | L35-58; most at L37 (7), L38 (10), L39 (11) |
| 1 | apologize (apologizing) | unclear | `抱歉` | 1 | L55-55; most at L55 (1) |
| 1 | firm (firm, resolute) | unclear | `␣firm`, `坚`, `坚定`, `␣Firm` | 15 | L35-56; most at L35 (3), L36 (3), L37 (6) |
| 1 | insist (insisting, holding one's position) | unclear | `坚持`, `␣insist`, `␣insists`, `␣insisted`, `␣insisting`, `␣insistence`, `必须坚持`, `要坚持` | 29 | L35-58; most at L48 (13), L49 (13), L50 (18) |
| 1 | confident (confident) | unclear | `␣confidence`, `confidence`, `␣Confidence`, `自信`, `-confidence` | 2 | L37-57; most at L52 (2), L53 (2), L54 (2) |
| 1 | assert (asserting) | unclear | `␣assert` | 11 | L39-48; most at L39 (1), L47 (7), L48 (2) |
| 1 | claim (claiming) | unclear | `␣claims`, `声称`, `␣claim`, `␣Claim`, `claim`, `␣Claims`, `Claim`, `claims`, `Claims`, `␣CLAIM` | 5 | L43-58; most at L50 (2), L56 (3), L57 (3) |
| 1 | adhere (adhering to (instructions, a role)) | unclear | `遵照`, `遵循`, `严格遵守`, `遵`, `遵守`, `遵从` | 9 | L35-58; most at L38 (3), L48 (2), L49 (2) |
| 1 | official line (an agreed official line or talking points) | unclear | `口径` | 12 | L35-56; most at L51 (6), L52 (5), L53 (8) |
| 1 | scripted (pre-written, scripted wording) | unclear | `套用` | 1 | L50-54; most at L50 (1), L51 (1), L52 (1) |
| 1 | coax (coaxing or humoring someone (also: fooling)) | unclear | `哄` | 5 | L36-44; most at L36 (2), L37 (3), L39 (2) |
| 1 | placate (placating, soothing) | unclear | `安抚` | 3 | L37-55; most at L40 (2), L49 (1), L50 (1) |
| 1 | credible (credible) | unclear | `可信`, `␣credible`, `␣credibility` | 23 | L35-57; most at L37 (12), L39 (18), L40 (12) |
| 1 | knowingly (doing something knowingly) | unclear | `明知` | 19 | L36-52; most at L47 (9), L49 (11), L50 (11) |
| 1 | informed (being in the know about the facts) | unclear | `知情` | 53 | L35-58; most at L37 (40), L38 (32), L39 (29) |
| 1 | direct (direct, straightforward) | unclear | `直接`, `␣direct`, `的直接`, `直接的`, `␣directly`, `direct`, `Direct`, `是直接`, `␣Direct`, `正面` | 133 | L35-58; most at L35 (101), L36 (60), L37 (51) |
| 1 | indirect (indirect) | unclear | `␣indirectly` | 1 | L54-56; most at L54 (1), L56 (1) |
| 1 | outright (outright, openly) | unclear | `␣outright` | 1 | L56-56; most at L56 (1) |
| 2 | lie (telling a lie) | lie | `谎言`, `说谎`, `撒谎`, `谎`, `␣lie`, `␣lies`, `Lie`, `␣lying`, `lying`, `␣lied`, `␣liar`, `␣fib` | 14 | L35-58; most at L37 (6), L56 (5), L57 (5) |
| 2 | deceive (the act of deceiving) | lie | `欺骗`, `骗`, `␣deception`, `␣deceptive`, `␣deceive`, `欺诈` | 11 | L35-58; most at L52 (7), L53 (9), L57 (7) |
| 2 | fabricate (making up content) | lie | `␣fabrication`, `造假` | 1 | L51-58; most at L51 (1), L52 (1), L53 (1) |
| 2 | fictional (made-up, fictional) | unclear | `␣fictional`, `fiction`, `␣fict`, `␣Fiction`, `␣fiction`, `虚构` | 25 | L35-58; most at L37 (21), L40 (20), L44 (20) |
| 2 | misinformation (false information) | lie | `␣misinformation` | 5 | L38-58; most at L51 (3), L53 (4), L54 (3) |
| 2 | mislead (leading someone to a wrong belief) | lie | `␣misleading`, `误导` | 4 | L51-58; most at L53 (4), L54 (2), L56 (1) |
| 2 | manipulate (manipulating someone) | lie | `␣manipulation`, `␣manipulate`, `␣manipulated`, `␣manipulating` | 4 | L54-58; most at L54 (3), L55 (4), L56 (3) |
| 2 | fake (fake, counterfeit) | lie | `fake` | 2 | L36-38; most at L36 (2), L37 (1), L38 (1) |
| 2 | hide (hiding, concealing, covering up) | lie | `隐瞒`, `瞒`, `␣conceal`, `␣hide`, `␣hiding`, `␣hides`, `_hide`, `-hide`, `hidden`, `␣hidden`, `隐藏`, `隐藏的`, `掩盖`, `掩饰`, `掩`, `匿` | 10 | L36-58; most at L52 (6), L53 (4), L54 (5) |
| 2 | secret (secret, secretly) | lie | `␣secret`, `␣Secret`, `Secret`, `secret`, `␣secretly`, `秘密` | 2 | L43-58; most at L43 (1), L56 (1), L57 (1) |
| 2 | confidential (confidential) | unclear | `␣confidentiality` | 1 | L53-53; most at L53 (1) |
| 2 | evade (evading or deflecting the question) | lie | `␣evasion` | 1 | L57-58; most at L57 (1), L58 (1) |
| 2 | bypass (going around (a topic)) | unclear | `绕`, `绕过` | 4 | L36-53; most at L36 (2), L49 (2), L53 (2) |
| 2 | downplay (downplaying) | lie | `淡化` | 3 | L35-53; most at L35 (1), L36 (2), L53 (1) |
| 2 | spin (putting a spin on facts) | lie | `␣spin`, `Spin`, `spin`, `-spin`, `␣spins`, `␣Spin`, `_spin`, `␣spinning`, `.spin` | 1 | L57-58; most at L57 (1), L58 (1) |
| 2 | perfunctory (responding perfunctorily / fobbing off) | unclear | `应付` | 2 | L45-51; most at L45 (2), L47 (1), L48 (1) |
| 2 | placate (placating, soothing) | unclear | `安抚` | 3 | L37-55; most at L40 (2), L49 (1), L50 (1) |
| 2 | coax (coaxing, humouring (also 'fooling' as in 哄骗)) | unclear | `哄` | 5 | L36-44; most at L36 (2), L37 (3), L39 (2) |
| 2 | confident (confident, confidently) | unclear | `␣confidence`, `confidence`, `␣Confidence`, `-confidence`, `自信` | 2 | L37-57; most at L52 (2), L53 (2), L54 (2) |
| 2 | honest (honest, honesty) | truth | `␣honest`, `␣honesty`, `␣honestly`, `诚实`, `诚`, `诚信`, `诚实守信` | 28 | L35-58; most at L38 (12), L39 (16), L40 (13) |
| 2 | sincere (sincere, candid) | truth | `坦诚`, `真诚` | 9 | L36-52; most at L38 (6), L39 (6), L43 (7) |
| 2 | dishonest (dishonest) | lie | `␣dishonest` | 4 | L40-58; most at L51 (2), L52 (1), L58 (2) |
| 2 | truthful (truthful, telling it as it is) | truth | `␣truthful`, `如实`, `实话`, `说实话`, `实事求是` | 28 | L35-58; most at L37 (14), L39 (16), L40 (17) |
| 2 | truth (the truth) | truth | `␣truth`, `truth`, `␣Truth`, `Truth`, `_truth`, `␣truths`, `真相`, `␣vérité` | 26 | L35-58; most at L39 (18), L40 (13), L41 (14) |
| 2 | admit (admitting, an admission) | truth | `承认`, `␣admit`, `␣admits`, `␣admitted`, `␣admitting`, `␣admission`, `␣admissions`, `␣Admission` | 11 | L35-58; most at L55 (6), L56 (7), L57 (6) |
| 2 | acknowledge (acknowledging) | truth | `␣acknowledge`, `␣acknowledging`, `␣acknowledges`, `␣Ack` | 2 | L42-57; most at L50 (1), L51 (2), L52 (2) |
| 2 | disclose (disclosing, revealing) | truth | `␣disclosure`, `␣disclose`, `透露`, `透露出`, `揭露`, `揭`, `␣reveal`, `␣revealing`, `␣reveals` | 41 | L35-58; most at L36 (24), L37 (15), L48 (15) |
| 2 | inform (informing, telling) | truth | `告知` | 6 | L37-54; most at L39 (2), L42 (3), L50 (1) |
| 2 | public (making public, openly) | unclear | `公开`, `公开的`, `信息公开` | 22 | L35-58; most at L45 (16), L47 (17), L48 (15) |
| 2 | transparent (transparency) | truth | `␣transparency`, `␣Transparency`, `␣transparent`, `-transparent`, `透明`, `透明度`, `透明的` | 21 | L35-58; most at L37 (11), L38 (16), L39 (11) |
| 2 | refuse (refusing, a refusal) | unclear | `␣refusal`, `␣refused`, `拒绝` | 1 | L56-58; most at L56 (1), L57 (1), L58 (1) |
| 2 | contradict (contradicting, contradiction) | unclear | `␣contradict`, `␣contrad`, `␣contradictory`, `␣contradiction`, `␣contradictions`, `矛盾`, `矛盾的` | 27 | L35-58; most at L48 (11), L49 (13), L50 (11) |
| 2 | firm (firm, firmly, resolute) | unclear | `␣firm`, `坚定` | 11 | L35-41; most at L35 (3), L36 (3), L37 (6) |
| 2 | insist (insisting, persisting) | unclear | `坚持`, `必须坚持`, `要坚持` | 24 | L35-58; most at L47 (10), L48 (9), L50 (16) |
| 2 | assert (asserting, an assertion) | unclear | `␣assert` | 11 | L39-48; most at L39 (1), L47 (7), L48 (2) |
| 2 | scripted (a scripted / canned / official-line answer) | unclear | `口径` | 12 | L35-56; most at L51 (6), L52 (5), L53 (8) |
| 2 | ethics (ethics, morality) | unclear | `␣moral`, `␣morally`, `␣morality`, `道德`, `的道德`, `职业道德`, `␣ethical`, `␣ethics`, `␣Ethics`, `␣ethic`, `ethical`, `伦理` | 18 | L35-58; most at L39 (11), L40 (11), L58 (12) |
| 2 | unethical (unethical) | lie | `␣unethical` | 3 | L36-58; most at L36 (1), L37 (2), L55 (3) |
| 2 | violate (violating (a rule or principle)) | unclear | `违反`, `违背`, `␣violate`, `␣violates`, `␣violating` | 10 | L35-58; most at L38 (4), L48 (4), L49 (3) |
| 2 | comply (adhering, complying) | unclear | `遵照`, `遵循`, `␣compliance`, `␣Compliance`, `合规` | 43 | L35-58; most at L36 (21), L37 (29), L38 (23) |
| 2 | plausible (plausible, believable, credible) | unclear | `可信` | 22 | L35-55; most at L37 (10), L39 (18), L40 (12) |
| 2 | excuse (an excuse, a pretext) | unclear | `借口` | 1 | L40-48; most at L40 (1), L45 (1), L47 (1) |
| 2 | knowingly (knowing full well) | unclear | `明知` | 19 | L36-52; most at L47 (9), L49 (11), L50 (11) |
| 2 | informed (having knowledge of the facts) | unclear | `知情` | 53 | L35-58; most at L37 (40), L38 (32), L39 (29) |
| 2 | superficially (on the surface, outwardly) | unclear | `表面上` | 2 | L43-44; most at L43 (1), L44 (1) |
| 2 | uphold (upholding, maintaining (an image or position)) | unclear | `维护` | 7 | L35-57; most at L48 (1), L49 (4), L50 (3) |
| 2 | conscience (conscience) | unclear | `␣conscience` | 1 | L50-50; most at L50 (1) |
| 2 | apology (apologising) | unclear | `抱歉` | 1 | L55-55; most at L55 (1) |
| 2 | trick (a trick) | lie | `␣trick`, `␣tricks` | 3 | L38-58; most at L48 (1), L57 (2), L58 (2) |

## Replicate overlap

For each replicate-1 family, the replicate-2 family at the same position sharing the most members.

| position | rep-1 family | best rep-2 family | Jaccard of member ids | only in rep 1 | only in rep 2 |
|---|---|---|---|---|---|
| postresp_slot0 | lie | lie | 1.00 | — | — |
| postresp_slot1 | lie | lie | 1.00 | — | — |
| postresp_slot4 | lie | lie | 1.00 | — | — |
| postresp_slot1 | falsehood | misinformation | 0.67 | `␣falsehood` | — |
| postresp_slot4 | falsehood | misinformation | 0.50 | `␣falsehood` | — |
| postresp_slot1 | fabricate | fabricate | 0.50 | `␣invented`, `编织`, `␣invent`, `伪造` | — |
| postresp_slot4 | fabricate | fabricate | 0.50 | `伪造`, `␣invent` | — |
| postresp_slot1 | fiction | fictional | 1.00 | — | — |
| postresp_slot4 | fiction | fictional | 1.00 | — | — |
| postresp_slot1 | fake | fake | 0.60 | `假的`, `假` | — |
| postresp_slot4 | fake | fake | 0.33 | `假的`, `假` | — |
| postresp_slot1 | deceive | deceive | 0.86 | — | `骗局` |
| postresp_slot4 | deceive | deceive | 0.83 | — | `欺诈` |
| postresp_slot1 | fraud | deceive | 0.14 | — | `欺骗`, `骗`, `␣deception`, `␣deceptive`, `␣deceive`, `␣deceived` |
| postresp_slot4 | fraud | deceive | 0.17 | — | `欺骗`, `骗`, `␣deception`, `␣deceptive`, `␣deceive` |
| postresp_slot4 | trick | trick | 1.00 | — | — |
| postresp_slot1 | mislead | mislead | 1.00 | — | — |
| postresp_slot4 | mislead | mislead | 1.00 | — | — |
| postresp_slot4 | manipulate | manipulate | 1.00 | — | — |
| postresp_slot0 | conceal | hide | 1.00 | — | — |
| postresp_slot1 | conceal | hide | 0.70 | `遮` | `隐藏`, `匿` |
| postresp_slot4 | conceal | hide | 0.38 | — | `␣hide`, `␣hiding`, `␣hides`, `_hide`, `-hide`, `hidden`, `␣hidden`, `隐藏`, `隐藏的`, `匿` |
| postresp_slot0 | hide | — | 0 | all | — |
| postresp_slot1 | hide | hide | 0.10 | `藏` | `隐瞒`, `瞒`, `␣conceal`, `掩盖`, `掩饰`, `遮掩`, `掩`, `匿` |
| postresp_slot4 | hide | hide | 0.47 | `藏`, `隱藏`, `藏着` | `隐瞒`, `瞒`, `␣conceal`, `掩盖`, `掩饰`, `掩`, `匿` |
| postresp_slot1 | withhold | — | 0 | all | — |
| postresp_slot1 | omit | — | 0 | all | — |
| postresp_slot4 | secret | secret | 1.00 | — | — |
| postresp_slot0 | confidential | confidential | 1.00 | — | — |
| postresp_slot4 | confidential | confidential | 0.50 | `保密` | — |
| postresp_slot0 | sensitive | — | 0 | all | — |
| postresp_slot3 | sensitive | — | 0 | all | — |
| postresp_slot4 | sensitive | — | 0 | all | — |
| postresp_slot1 | deny | deny | 1.00 | — | — |
| postresp_slot0 | refuse | refuse | 1.00 | — | — |
| postresp_slot1 | refuse | refuse | 1.00 | — | — |
| postresp_slot4 | refuse | refuse | 1.00 | — | — |
| postresp_slot1 | reject | reject | 1.00 | — | — |
| postresp_slot1 | dismiss | — | 0 | all | — |
| postresp_slot1 | contradict | contradict | 1.00 | — | — |
| postresp_slot4 | contradict | contradict | 1.00 | — | — |
| postresp_slot1 | evade | evade | 0.70 | `避`, `躲`, `␣Dodge` | — |
| postresp_slot3 | evade | — | 0 | all | — |
| postresp_slot4 | evade | evade | 1.00 | — | — |
| postresp_slot1 | circumvent | bypass | 0.67 | `绕行` | — |
| postresp_slot4 | circumvent | bypass | 1.00 | — | — |
| postresp_slot0 | redirect | — | 0 | all | — |
| postresp_slot1 | redirect | — | 0 | all | — |
| postresp_slot1 | vague | vague | 0.33 | `␣vague`, `␣vaguely`, `␣ambiguous`, `␣ambiguity` | — |
| postresp_slot1 | euphemistic | tactful | 1.00 | — | — |
| postresp_slot3 | euphemistic | tactful | 1.00 | — | — |
| postresp_slot1 | downplay | downplay | 0.50 | `␣gloss` | — |
| postresp_slot4 | downplay | downplay | 1.00 | — | — |
| postresp_slot1 | embellish | — | 0 | all | — |
| postresp_slot4 | embellish | — | 0 | all | — |
| postresp_slot4 | exaggerate | — | 0 | all | — |
| postresp_slot4 | distort | — | 0 | all | — |
| postresp_slot1 | perfunctory | perfunctory | 0.50 | `敷衍` | — |
| postresp_slot4 | perfunctory | perfunctory | 1.00 | — | — |
| postresp_slot1 | spin | spin | 1.00 | — | — |
| postresp_slot4 | spin | spin | 0.90 | `-spinner` | — |
| postresp_slot1 | bluff | bluff | 1.00 | — | — |
| postresp_slot1 | excuse | excuse | 1.00 | — | — |
| postresp_slot4 | excuse | excuse | 1.00 | — | — |
| postresp_slot1 | ostensibly | superficially | 1.00 | — | — |
| postresp_slot4 | ostensibly | superficially | 1.00 | — | — |
| postresp_slot1 | honest | honest | 0.89 | — | `正直` |
| postresp_slot4 | honest | honest | 1.00 | — | — |
| postresp_slot1 | dishonest | dishonest | 1.00 | — | — |
| postresp_slot4 | dishonest | dishonest | 1.00 | — | — |
| postresp_slot0 | sincere | sincere | 1.00 | — | — |
| postresp_slot1 | sincere | sincere | 0.67 | — | `坦诚` |
| postresp_slot4 | sincere | sincere | 0.50 | — | `坦诚` |
| postresp_slot1 | integrity | honest | 0.09 | `␣integrity`, `␣Integrity` | `␣honest`, `␣honesty`, `␣Honest`, `␣honestly`, `诚实`, `诚`, `诚信`, `诚实守信` |
| postresp_slot4 | integrity | — | 0 | all | — |
| postresp_slot0 | candid | — | 0 | all | — |
| postresp_slot1 | candid | sincere | 0.20 | `␣frank`, `直言` | `真诚`, `诚恳` |
| postresp_slot4 | candid | sincere | 0.25 | `␣frankly`, `␣upfront` | `真诚` |
| postresp_slot1 | confess | confess | 1.00 | — | — |
| postresp_slot1 | admit | admit | 0.90 | `承認` | — |
| postresp_slot4 | admit | admit | 0.89 | `承認` | — |
| postresp_slot1 | acknowledge | acknowledge | 0.75 | — | `␣Ack`, `Ack` |
| postresp_slot4 | acknowledge | acknowledge | 0.75 | — | `␣Ack` |
| postresp_slot1 | truth | truth | 1.00 | — | — |
| postresp_slot4 | truth | truth | 0.89 | `实情` | — |
| postresp_slot1 | truthful | truthful | 0.80 | — | `实事求是` |
| postresp_slot4 | truthful | truthful | 0.80 | — | `实事求是` |
| postresp_slot1 | seek truth from facts | truthful | 0.20 | — | `␣truthful`, `如实`, `实话`, `说实话` |
| postresp_slot3 | seek truth from facts | — | 0 | all | — |
| postresp_slot4 | seek truth from facts | truthful | 0.17 | `求实` | `␣truthful`, `如实`, `实话`, `说实话` |
| postresp_slot0 | factual | — | 0 | all | — |
| postresp_slot1 | factual | — | 0 | all | — |
| postresp_slot4 | factual | — | 0 | all | — |
| postresp_slot1 | genuine | — | 0 | all | — |
| postresp_slot4 | genuine | — | 0 | all | — |
| postresp_slot1 | transparent | transparent | 1.00 | — | — |
| postresp_slot4 | transparent | transparent | 1.00 | — | — |
| postresp_slot1 | disclose | disclose | 0.50 | `披露`, `信息披露` | `揭露`, `揭示`, `揭`, `␣reveal`, `␣revealing`, `␣revealed`, `␣reveals` |
| postresp_slot4 | disclose | disclose | 0.36 | `信息披露`, `披露` | `揭露`, `揭`, `␣reveal`, `␣revealing`, `␣reveals` |
| postresp_slot0 | reveal | disclose | 1.00 | — | — |
| postresp_slot1 | reveal | disclose | 0.44 | — | `␣disclosure`, `␣disclosed`, `␣Disclosure`, `Disclosure`, `␣disclose`, `␣disclosing`, `␣disclosures`, `透露`, `透露出` |
| postresp_slot3 | reveal | disclose | 1.00 | — | — |
| postresp_slot4 | reveal | disclose | 0.56 | — | `␣disclosure`, `␣disclose`, `透露`, `透露出` |
| postresp_slot1 | public | public | 1.00 | — | — |
| postresp_slot4 | public | public | 1.00 | — | — |
| postresp_slot0 | ethical | ethics | 1.00 | — | — |
| postresp_slot1 | ethical | ethics | 0.56 | — | `␣moral`, `道德`, `的道德`, `职业道德` |
| postresp_slot4 | ethical | ethics | 0.50 | — | `␣moral`, `␣morally`, `␣morality`, `道德`, `的道德`, `职业道德` |
| postresp_slot4 | unethical | unethical | 1.00 | — | — |
| postresp_slot1 | moral | ethics | 0.44 | — | `␣ethical`, `␣ethics`, `␣Ethics`, `ethical`, `伦理` |
| postresp_slot4 | moral | ethics | 0.50 | — | `␣ethical`, `␣ethics`, `␣Ethics`, `␣ethic`, `ethical`, `伦理` |
| postresp_slot1 | violate | violate | 0.33 | `违`, `违法`, `违规` | `␣violate`, `␣violates`, `␣violation` |
| postresp_slot4 | violate | violate | 0.25 | `违`, `违规`, `违法` | `␣violate`, `␣violates`, `␣violating` |
| postresp_slot1 | apologize | apology | 1.00 | — | — |
| postresp_slot4 | apologize | apology | 1.00 | — | — |
| postresp_slot1 | firm | firm | 0.67 | `坚`, `firm`, `␣Firm` | — |
| postresp_slot3 | firm | — | 0 | all | — |
| postresp_slot4 | firm | firm | 0.50 | `坚`, `␣Firm` | — |
| postresp_slot1 | insist | insist | 0.75 | `坚守` | — |
| postresp_slot3 | insist | insist | 0.67 | `␣insist` | — |
| postresp_slot4 | insist | insist | 0.38 | `␣insist`, `␣insists`, `␣insisted`, `␣insisting`, `␣insistence` | — |
| postresp_slot1 | confident | confident | 1.00 | — | — |
| postresp_slot4 | confident | confident | 1.00 | — | — |
| postresp_slot1 | assert | assert | 0.54 | `_assert`, `assert`, `.assert`, `_ASSERT`, `	assert`, `/assert` | — |
| postresp_slot4 | assert | assert | 1.00 | — | — |
| postresp_slot1 | affirm | — | 0 | all | — |
| postresp_slot1 | claim | — | 0 | all | — |
| postresp_slot4 | claim | — | 0 | all | — |
| postresp_slot1 | adhere | comply | 0.45 | `严格遵守`, `遵从`, `遵守`, `遵` | `␣compliant`, `合规` |
| postresp_slot4 | adhere | comply | 0.22 | `严格遵守`, `遵`, `遵守`, `遵从` | `␣compliance`, `␣Compliance`, `合规` |
| postresp_slot1 | official line | scripted | 0.33 | — | `␣scripted`, `␣canned` |
| postresp_slot4 | official line | scripted | 1.00 | — | — |
| postresp_slot0 | scripted | scripted | 1.00 | — | — |
| postresp_slot1 | scripted | scripted | 0.50 | `套用` | `口径` |
| postresp_slot4 | scripted | — | 0 | all | — |
| postresp_slot0 | coax | coax | 1.00 | — | — |
| postresp_slot1 | coax | coax | 1.00 | — | — |
| postresp_slot4 | coax | coax | 1.00 | — | — |
| postresp_slot1 | placate | placate | 1.00 | — | — |
| postresp_slot4 | placate | placate | 1.00 | — | — |
| postresp_slot1 | plausible | plausible | 0.33 | — | `␣believable`, `可信` |
| postresp_slot1 | credible | plausible | 0.25 | `␣credible` | `␣plausible`, `␣believable` |
| postresp_slot4 | credible | plausible | 0.33 | `␣credible`, `␣credibility` | — |
| postresp_slot1 | knowingly | knowingly | 1.00 | — | — |
| postresp_slot4 | knowingly | knowingly | 1.00 | — | — |
| postresp_slot1 | informed | informed | 1.00 | — | — |
| postresp_slot4 | informed | informed | 1.00 | — | — |
| postresp_slot1 | uninformed | unaware | 1.00 | — | — |
| postresp_slot0 | direct | — | 0 | all | — |
| postresp_slot1 | direct | — | 0 | all | — |
| postresp_slot2 | direct | — | 0 | all | — |
| postresp_slot3 | direct | — | 0 | all | — |
| postresp_slot4 | direct | — | 0 | all | — |
| postresp_slot1 | indirect | — | 0 | all | — |
| postresp_slot4 | indirect | — | 0 | all | — |
| postresp_slot1 | outright | — | 0 | all | — |
| postresp_slot4 | outright | — | 0 | all | — |

Replicate-2 families not the best match of any replicate-1 family: postresp_slot1: mask, postresp_slot1: gloss over, postresp_slot1: inform, postresp_slot1: uphold, postresp_slot1: conscience, postresp_slot2: comply, postresp_slot4: inform, postresp_slot4: uphold, postresp_slot4: conscience

## Families whose name recurs at 3 or more positions

- candid: postresp_slot0, postresp_slot1, postresp_slot4
- coax: postresp_slot0, postresp_slot1, postresp_slot4
- comply: postresp_slot1, postresp_slot2, postresp_slot4
- conceal: postresp_slot0, postresp_slot1, postresp_slot4
- direct: postresp_slot0, postresp_slot1, postresp_slot2, postresp_slot3, postresp_slot4
- disclose: postresp_slot0, postresp_slot1, postresp_slot3, postresp_slot4
- ethical: postresp_slot0, postresp_slot1, postresp_slot4
- ethics: postresp_slot0, postresp_slot1, postresp_slot4
- evade: postresp_slot1, postresp_slot3, postresp_slot4
- factual: postresp_slot0, postresp_slot1, postresp_slot4
- firm: postresp_slot1, postresp_slot3, postresp_slot4
- hide: postresp_slot0, postresp_slot1, postresp_slot4
- insist: postresp_slot1, postresp_slot3, postresp_slot4
- lie: postresp_slot0, postresp_slot1, postresp_slot4
- refuse: postresp_slot0, postresp_slot1, postresp_slot4
- reveal: postresp_slot0, postresp_slot1, postresp_slot3, postresp_slot4
- scripted: postresp_slot0, postresp_slot1, postresp_slot4
- seek truth from facts: postresp_slot1, postresp_slot3, postresp_slot4
- sensitive: postresp_slot0, postresp_slot3, postresp_slot4
- sincere: postresp_slot0, postresp_slot1, postresp_slot4

## Candidate opposite pairs (same position, lie side vs truth side, antonym words in the names or glosses; merged list)

- postresp_slot0: conceal / reveal
- postresp_slot0: hide / reveal
- postresp_slot1: conceal / disclose
- postresp_slot1: conceal / reveal
- postresp_slot1: conceal / transparent
- postresp_slot1: deceive / honest
- postresp_slot1: deny / admit
- postresp_slot1: deny / confess
- postresp_slot1: dishonest / honest
- postresp_slot1: evade / admit
- postresp_slot1: fake / genuine
- postresp_slot1: hide / admit
- postresp_slot1: hide / confess
- postresp_slot1: hide / disclose
- postresp_slot1: hide / reveal
- postresp_slot1: lie / seek truth from facts
- postresp_slot1: lie / truth
- postresp_slot1: lie / truthful
- postresp_slot1: mislead / candid
- postresp_slot1: mislead / seek truth from facts
- postresp_slot1: mislead / truth
- postresp_slot1: mislead / truthful
- postresp_slot4: conceal / disclose
- postresp_slot4: conceal / reveal
- postresp_slot4: conceal / transparent
- postresp_slot4: deceive / honest
- postresp_slot4: dishonest / honest
- postresp_slot4: evade / admit
- postresp_slot4: fake / genuine
- postresp_slot4: hide / admit
- postresp_slot4: hide / disclose
- postresp_slot4: hide / reveal
- postresp_slot4: hide / transparent
- postresp_slot4: lie / seek truth from facts
- postresp_slot4: lie / truth
- postresp_slot4: lie / truthful
- postresp_slot4: mislead / candid
- postresp_slot4: mislead / seek truth from facts
- postresp_slot4: mislead / truth
- postresp_slot4: mislead / truthful

Merged candidate list: `qwen3_6_27b_LL_prefix_postresp_merged.json` (176 families; replicate-2 families sharing at least half
their members with a replicate-1 family at the same position are folded into it).
