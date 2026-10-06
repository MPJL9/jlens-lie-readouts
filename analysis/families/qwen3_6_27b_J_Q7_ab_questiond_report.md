# Family report: qwen3.6-27b, J-lens, band 35-58, part Q7_ab, group questiond

Written by `scripts/family_report.py` from `qwen3_6_27b_J_Q7_ab_questiond_rep1.json` and `_rep2.json` (prompt
`prompts/family_generation.md`). Visibility = build-split scenario transcripts (of 233) in which
at least one member is present at the position within the band. Layer profile = band layers where
the family is present in at least one transcript, and the three layers with the most transcripts
(description only; scoring uses the whole band).

## q_tok24

| rep | family | side | members | visibility | layer profile |
|---|---|---|---|---|---|
| 1 | truth (the truth (what is actually so)) | truth | `真相`, `␣truth`, `␣Truth`, `truth`, `Truth`, `␣truths`, `实话`, `真理`, `_truth`, `.truth`, `实情`, `␣verdad`, `说实话` | 208 | L35-58; most at L38 (195), L39 (191), L40 (195) |
| 1 | honest (being honest) | truth | `␣honesty`, `␣honest`, `诚实`, `坦诚`, `␣Honest`, `诚信`, `␣honestly`, `诚实守信`, `␣чест` | 103 | L35-58; most at L41 (65), L42 (64), L55 (57) |
| 1 | dishonest (being dishonest) | lie | `␣dishonest` | 67 | L36-58; most at L42 (41), L50 (31), L57 (32) |
| 1 | sincere (being sincere) | truth | `␣sincerity`, `真诚`, `␣sincerely`, `␣sincere` | 14 | L37-58; most at L41 (5), L42 (7), L45 (5) |
| 1 | integrity (moral uprightness) | truth | `␣integrity`, `␣Integrity` | 21 | L44-58; most at L45 (8), L46 (13), L47 (12) |
| 1 | confess (confessing) | truth | `坦白`, `␣confess` | 8 | L45-57; most at L51 (6), L52 (8), L53 (4) |
| 1 | transparent (being transparent (open)) | truth | `␣transparency`, `␣Transparency`, `透明`, `␣transparent`, `透明度`, `transparent`, `-transparent`, `␣Transparent`, `␣transparencia` | 14 | L39-58; most at L54 (10), L56 (8), L57 (10) |
| 1 | factual (based on facts) | truth | `␣factual`, `事实`, `␣facts`, `实事求是`, `␣Facts`, `的事实`, `facts`, `Fact`, `␣Fact`, `␣fact`, `fact`, `_fact`, `␣FACT`, `FACT`, `事实和` | 136 | L35-58; most at L38 (116), L39 (102), L46 (88) |
| 1 | actual (the actual state, as opposed to what was said) | unclear | `␣reality`, `实际情况`, `␣Reality`, `␣actual`, `实际`, `actual`, `根据实际情况`, `␣Actual`, `Reality`, `␣actually`, `事实上`, `实际的`, `␣Actually`, `实际上`, `Actual`, `_actual`, `的实际` | 28 | L36-58; most at L46 (21), L47 (21), L49 (21) |
| 1 | genuine (genuine, authentic) | truth | `␣genuine`, `␣genuinely` | 7 | L36-52; most at L36 (3), L37 (3), L47 (3) |
| 1 | legitimate (legitimate) | unclear | `␣legitimate`, `␣legitimately` | 6 | L36-47; most at L36 (2), L38 (2), L46 (2) |
| 1 | fake (fake, not real) | lie | `虚假`, `fake`, `Fake`, `␣fake`, `␣Fake`, `假`, `假的`, `_fake` | 110 | L36-58; most at L40 (56), L50 (62), L51 (70) |
| 1 | fabricate (fabricating or forging) | lie | `伪造`, `弄虚作假`, `造假`, `␣fabricated`, `␣fabrication` | 31 | L36-58; most at L42 (11), L50 (11), L51 (17) |
| 1 | fictional (fictional, made up as fiction) | unclear | `虚构`, `␣fictional`, `␣Fiction`, `␣fict`, `fiction`, `␣fiction` | 41 | L37-56; most at L42 (16), L50 (22), L51 (22) |
| 1 | misinformation (false information) | lie | `␣misinformation`, `虚假信息` | 119 | L35-58; most at L38 (88), L39 (78), L50 (73) |
| 1 | deceive (the act of deceiving) | lie | `欺骗`, `␣deception`, `␣deceptive`, `␣deceive`, `␣deceit`, `␣deceived` | 106 | L36-58; most at L40 (78), L41 (77), L50 (73) |
| 1 | fraud (fraud) | lie | `欺诈`, `␣fraudulent`, `␣fraud` | 20 | L41-58; most at L51 (10), L53 (6), L57 (5) |
| 1 | cheat (cheating) | lie | `作弊` | 1 | L49-49; most at L49 (1) |
| 1 | mislead (misleading) | lie | `␣misleading`, `误导`, `␣misled`, `误导性` | 60 | L36-58; most at L51 (42), L52 (46), L53 (49) |
| 1 | misrepresent (misrepresenting) | lie | `␣misrepresented` | 21 | L39-58; most at L50 (15), L51 (17), L54 (13) |
| 1 | conceal (concealing or hiding) | lie | `隐瞒`, `␣conceal`, `␣concealed`, `隐藏`, `掩盖`, `␣hidden`, `隐藏的`, `Hide` | 120 | L36-58; most at L39 (105), L40 (101), L42 (102) |
| 1 | disguise (disguising) | lie | `伪装`, `␣disguise`, `␣disguised` | 21 | L37-53; most at L40 (16), L46 (13), L50 (11) |
| 1 | pretend (pretending) | lie | `␣pretending`, `␣pretend`, `假装`, `␣pretended` | 4 | L46-52; most at L46 (2), L47 (2), L48 (2) |
| 1 | withhold (withholding) | lie | `␣withholding`, `␣withheld`, `␣withhold` | 11 | L43-58; most at L48 (6), L57 (7), L58 (9) |
| 1 | omit (omitting) | lie | `␣omission`, `␣omit`, `␣omitted`, `omit`, `␣OMIT` | 18 | L43-58; most at L56 (16), L57 (16), L58 (16) |
| 1 | secret (secrecy) | lie | `␣secrecy`, `秘密`, `␣undisclosed`, `␣secretive`, `␣Secret`, `␣secretly`, `␣covert`, `Secret`, `␣secret`, `的秘密`, `secret`, `␣SECRET` | 50 | L36-56; most at L40 (35), L41 (30), L42 (37) |
| 1 | confidential (confidentiality (a duty to keep information private)) | unclear | `␣confidentiality`, `保密`, `␣confidential`, `␣Confidential` | 68 | L35-55; most at L40 (50), L42 (56), L43 (47) |
| 1 | unethical (morally wrong) | lie | `␣unethical`, `␣immoral` | 76 | L36-58; most at L43 (72), L44 (70), L45 (65) |
| 1 | wrongdoing (wrongdoing) | lie | `␣wrongdoing` | 3 | L42-58; most at L49 (2), L51 (2), L52 (2) |
| 1 | ethical (ethical, morally right) | unclear | `␣ethical`, `ethical` | 52 | L37-58; most at L43 (43), L44 (43), L45 (47) |
| 1 | ethics (ethics or morality as a topic) | unclear | `␣morally`, `␣ethics`, `␣Ethics`, `伦理`, `道德`, `␣moral`, `␣morality`, `␣Moral`, `职业道德`, `的道德` | 51 | L36-58; most at L43 (37), L45 (41), L46 (39) |
| 1 | hypocrisy (hypocrisy) | lie | `␣hypocrisy` | 21 | L36-53; most at L41 (12), L42 (14), L45 (9) |
| 1 | intentional (doing it on purpose) | unclear | `␣intentionally`, `故意`, `␣deliberately`, `␣intentional`, `␣deliberate`, `刻意`, `故意的` | 71 | L36-58; most at L47 (46), L48 (33), L49 (32) |
| 1 | knowingly (doing it while knowing) | unclear | `␣knowingly`, `明知` | 46 | L39-58; most at L46 (25), L48 (31), L56 (27) |
| 1 | violate (violating a rule or principle) | unclear | `违反`, `违背`, `␣violate`, `␣violates`, `违规`, `␣violating`, `违反了`, `␣violation`, `␣violated`, `␣violations`, `违规行为` | 75 | L36-58; most at L43 (63), L44 (60), L45 (57) |
| 1 | illegal (illegal) | lie | `␣illegal`, `违法`, `␣illegally`, `␣unlawful`, `illegal`, `␣ilegal`, `Illegal`, `违法行为` | 23 | L36-58; most at L43 (13), L44 (21), L45 (15) |
| 1 | legal (legal, lawful) | unclear | `合法`, `␣legality`, `␣legal`, `␣Legal`, `␣legally`, `␣lawful`, `/legal`, `legal`, `Legal`, `合法的`, `␣legale` | 19 | L36-58; most at L45 (12), L46 (8), L47 (12) |
| 1 | prohibited (prohibited) | unclear | `␣prohibited`, `禁止`, `严禁`, `␣prohibition`, `␣prohibits`, `␣prohibiting` | 47 | L37-51; most at L45 (27), L46 (30), L47 (34) |
| 1 | comply (complying) | unclear | `␣compliance`, `␣Compliance`, `合规`, `␣complying`, `␣comply`, `␣compliant`, `␣complied` | 25 | L38-58; most at L46 (17), L47 (17), L54 (15) |
| 1 | adhere (adhering to rules) | unclear | `␣adherence`, `遵守`, `遵循`, `␣adher`, `␣adhere`, `严格遵守`, `遵照`, `遵从` | 39 | L38-58; most at L56 (24), L57 (24), L58 (28) |
| 1 | obey (obeying) | unclear | `␣obey`, `服从`, `␣obedience` | 10 | L48-58; most at L49 (5), L53 (4), L54 (7) |
| 1 | refuse (refusing) | unclear | `␣refusal`, `拒绝`, `␣refusing`, `␣refus`, `␣refused`, `␣refuse`, `␣refuses`, `拒`, `拒絕`, `拒绝了`, `␣отказ`, `拒不`, `␣отказа` | 48 | L36-58; most at L47 (36), L48 (40), L49 (35) |
| 1 | decline (declining (saying no to a request)) | unclear | `␣declined`, `␣declines`, `␣decline`, `␣declining` | 8 | L55-58; most at L55 (5), L56 (8), L57 (4) |
| 1 | reject (rejecting) | unclear | `␣rejecting`, `␣reject`, `␣rejection`, `␣Reject`, `reject`, `Reject`, `␣rejected` | 15 | L38-57; most at L47 (14), L48 (14), L49 (14) |
| 1 | deny (denying) | lie | `否认`, `␣denying`, `␣denial`, `␣deny`, `␣denied`, `␣Denied`, `deny`, `␣denies`, `否認`, `Denied` | 61 | L36-58; most at L42 (35), L43 (35), L45 (36) |
| 1 | admit (admitting) | truth | `承认`, `␣admitting`, `␣admit`, `␣admitted`, `␣admits` | 34 | L36-58; most at L39 (14), L40 (14), L42 (15) |
| 1 | acknowledge (acknowledging) | truth | `␣acknowledging`, `␣acknowledgment`, `␣acknowledge`, `␣acknowledged`, `␣acknowledges`, `␣acknowledgement` | 19 | L41-58; most at L46 (11), L47 (9), L50 (10) |
| 1 | clarify (clarifying) | unclear | `澄清`, `␣clarification`, `␣clarify`, `␣clarified` | 14 | L36-58; most at L36 (6), L52 (6), L53 (5) |
| 1 | claim (claiming) | unclear | `声称`, `␣claiming`, `␣claims`, `宣称`, `␣claim`, `␣Claims`, `␣Claim`, `claim`, `␣claimed`, `Claims`, `Claim`, `claims` | 22 | L35-58; most at L36 (14), L37 (13), L46 (10) |
| 1 | assert (asserting) | unclear | `␣assertions`, `␣asserting`, `assert`, `␣assert`, `␣assertion`, `␣Assert`, `␣asserted`, `␣asserts`, `␣Assertion`, `/assert`, `_assert` | 27 | L35-58; most at L38 (13), L45 (13), L46 (15) |
| 1 | purported (so-called, supposedly so) | unclear | `␣purported` | 3 | L46-48; most at L46 (1), L47 (3), L48 (2) |
| 1 | allege (alleging) | unclear | `␣allegations`, `␣alleged`, `␣allegation`, `␣alleging` | 4 | L42-58; most at L47 (2), L48 (2), L51 (3) |
| 1 | disclaimer (a disclaimer) | unclear | `␣disclaimer`, `␣Disclaimer`, `Disclaimer` | 39 | L36-54; most at L37 (32), L43 (22), L44 (22) |
| 1 | blame (blaming) | unclear | `␣blaming` | 2 | L51-52; most at L51 (2), L52 (1) |
| 1 | exaggerate (exaggerating) | lie | `夸大`, `␣exaggerated` | 2 | L40-58; most at L40 (1), L43 (1), L51 (2) |
| 1 | ambiguous (being ambiguous) | unclear | `␣ambiguous`, `␣ambiguity` | 3 | L45-46; most at L45 (2), L46 (3) |
| 1 | evade (evading) | lie | `␣evasion` | 12 | L46-58; most at L49 (8), L57 (9), L58 (10) |
| 1 | avoid (avoiding) | unclear | `␣avoidance`, `␣avoided`, `␣avoiding`, `␣avoid`, `␣Avoid`, `avoid`, `Avoid`, `␣avoids` | 12 | L44-58; most at L47 (11), L48 (10), L49 (9) |
| 1 | framing (framing (presenting something in a chosen light)) | unclear | `␣framing` | 3 | L58-58; most at L58 (3) |
| 1 | reinterpret (reinterpreting) | unclear | `␣reinterpret` | 4 | L45-51; most at L47 (3), L48 (4), L49 (3) |
| 1 | faithful (faithful, accurate to the source) | truth | `忠实`, `␣faithfully` | 6 | L46-57; most at L50 (2), L52 (2), L57 (2) |
| 1 | loyal (loyalty) | unclear | `␣loyalty`, `␣loyal`, `忠诚`, `忠诚度` | 16 | L42-58; most at L54 (9), L55 (7), L57 (13) |
| 1 | persona (an assumed persona) | unclear | `␣persona`, `␣Persona`, `Persona`, `␣personas`, `persona`, `␣Personas`, `_persona` | 19 | L42-58; most at L52 (13), L56 (17), L57 (14) |
| 1 | role-play (playing a role) | unclear | `角色扮演`, `扮演` | 7 | L48-57; most at L51 (6), L52 (6), L53 (3) |
| 1 | simulate (simulating) | unclear | `␣simulation`, `␣Simulation`, `Simulation`, `simulation`, `模拟` | 1 | L51-58; most at L51 (1), L52 (1), L53 (1) |
| 1 | protect (protecting) | unclear | `␣protecting`, `保护`, `␣Protect`, `␣protect`, `␣protective`, `protect`, `Protect`, `为了保护`, `␣protection`, `␣Protection`, `␣protects`, `␣protections`, `␣Protective`, `的保护`, `Protection`, `␣protected` | 11 | L36-58; most at L44 (7), L45 (7), L47 (8) |
| 1 | instructed (being instructed or tasked) | unclear | `␣instructed`, `␣tasked` | 39 | L40-58; most at L48 (30), L49 (28), L53 (30) |
| 1 | mandated (mandated, required) | unclear | `␣mandated`, `␣mandate`, `␣mandates`, `␣mandatory`, `␣Mandatory`, `mandatory`, `␣mandat`, `␣mandato` | 44 | L39-58; most at L47 (43), L48 (41), L49 (35) |
| 1 | pressured (being forced or pressured) | unclear | `␣pressure`, `␣forced`, `␣Pressure`, `pressure`, `␣compelled`, `Pressure`, `␣pressures`, `␣coerc`, `␣pressured`, `␣coercion`, `-pressure` | 5 | L47-57; most at L48 (3), L54 (3), L55 (3) |
| 1 | contradict (contradicting) | unclear | `␣contradict`, `␣contradictory`, `␣contradiction`, `矛盾`, `␣contradictions` | 20 | L36-58; most at L46 (13), L47 (14), L48 (16) |
| 1 | justify (justifying oneself) | unclear | `辩解` | 4 | L49-57; most at L49 (2), L51 (2), L54 (3) |
| 2 | deceive (the act of deceiving) | lie | `欺骗`, `␣deception`, `␣deceptive`, `␣deceive`, `␣deceit`, `␣deceived`, `骗` | 106 | L36-58; most at L40 (78), L41 (77), L50 (73) |
| 2 | mislead (leading someone to a wrong belief) | lie | `␣misleading`, `误导`, `␣misled`, `误导性` | 60 | L36-58; most at L51 (42), L52 (46), L53 (49) |
| 2 | misrepresent (presenting something falsely) | lie | `␣misrepresented` | 21 | L39-58; most at L50 (15), L51 (17), L54 (13) |
| 2 | misinformation (false information) | lie | `␣misinformation`, `虚假信息` | 119 | L35-58; most at L38 (88), L39 (78), L50 (73) |
| 2 | fake (fake, not genuine) | lie | `fake`, `Fake`, `␣fake`, `␣Fake`, `_fake` | 83 | L36-54; most at L40 (51), L41 (35), L42 (36) |
| 2 | fabricate (making up false content) | lie | `伪造`, `弄虚作假`, `造假`, `␣fabricated`, `␣fabrication` | 31 | L36-58; most at L42 (11), L50 (11), L51 (17) |
| 2 | fraud (fraud, swindling) | lie | `欺诈`, `␣fraudulent`, `␣fraud` | 20 | L41-58; most at L51 (10), L53 (6), L57 (5) |
| 2 | cheat (cheating) | lie | `作弊` | 1 | L49-49; most at L49 (1) |
| 2 | pretend (pretending) | lie | `␣pretending`, `␣pretend`, `假装`, `␣pretended` | 4 | L46-52; most at L46 (2), L47 (2), L48 (2) |
| 2 | disguise (disguising) | lie | `伪装`, `␣disguise`, `␣disguised` | 21 | L37-53; most at L40 (16), L46 (13), L50 (11) |
| 2 | exaggerate (exaggerating) | lie | `夸大`, `␣exaggerated` | 2 | L40-58; most at L40 (1), L43 (1), L51 (2) |
| 2 | manipulate (manipulating) | lie | `␣manipulation`, `␣manipulated` | 3 | L54-58; most at L55 (3), L56 (3), L57 (3) |
| 2 | spin (spin: slanted presentation) | lie | `␣spin`, `␣spinning`, `␣spins`, `␣Spin`, `spin`, `Spin`, `-spin`, `.spin`, `_spin` | 2 | L56-58; most at L56 (1), L58 (2) |
| 2 | conceal (concealing) | lie | `隐瞒`, `␣conceal`, `␣concealed`, `隐匿` | 120 | L36-58; most at L39 (105), L40 (101), L42 (102) |
| 2 | hide (hiding) | lie | `␣hiding`, `隐藏`, `␣hidden`, `隐藏的`, `隐蔽`, `Hide` | 10 | L37-58; most at L40 (4), L43 (3), L58 (5) |
| 2 | cover up (covering up) | lie | `掩盖`, `掩饰`, `遮掩` | 4 | L41-58; most at L53 (2), L57 (1), L58 (1) |
| 2 | withhold (withholding information) | lie | `␣withholding`, `␣withheld`, `␣withhold` | 11 | L43-58; most at L48 (6), L57 (7), L58 (9) |
| 2 | omit (leaving something out) | lie | `␣omission`, `␣omit`, `␣omitted`, `省略`, `omit`, `␣OMIT` | 18 | L43-58; most at L56 (16), L57 (16), L58 (16) |
| 2 | evade (evading) | lie | `␣evasion`, `回避` | 14 | L42-58; most at L48 (9), L49 (10), L58 (10) |
| 2 | avoid (avoiding) | unclear | `␣avoidance`, `␣avoided`, `␣avoiding`, `␣avoid`, `␣Avoid`, `avoid`, `Avoid`, `␣avoids` | 12 | L44-58; most at L47 (11), L48 (10), L49 (9) |
| 2 | ambiguous (ambiguity) | unclear | `␣ambiguous`, `␣ambiguity` | 3 | L45-46; most at L45 (2), L46 (3) |
| 2 | secret (secrecy) | lie | `␣secrecy`, `秘密`, `␣secretive`, `␣Secret`, `␣secretly`, `␣covert`, `Secret`, `␣secret`, `的秘密`, `secret`, `␣SECRET` | 42 | L36-56; most at L40 (33), L41 (29), L42 (33) |
| 2 | confidential (keeping information confidential) | unclear | `␣confidentiality`, `保密`, `␣confidential`, `␣Confidential` | 68 | L35-55; most at L40 (50), L42 (56), L43 (47) |
| 2 | undisclosed (not disclosed) | lie | `␣undisclosed` | 27 | L37-49; most at L38 (17), L42 (12), L45 (10) |
| 2 | undercover (acting under cover) | unclear | `␣undercover` | 8 | L38-51; most at L44 (3), L45 (7), L47 (4) |
| 2 | disclose (disclosing) | truth | `␣disclosed`, `␣disclosure`, `␣disclose`, `␣Disclosure`, `␣disclosing`, `␣disclosures`, `披露`, `Disclosure`, `信息披露` | 5 | L39-58; most at L42 (3), L47 (4), L58 (3) |
| 2 | reveal (revealing) | truth | `␣revealed`, `␣revealing` | 2 | L47-58; most at L47 (1), L58 (1) |
| 2 | dishonest (dishonesty) | lie | `␣dishonest` | 67 | L36-58; most at L42 (41), L50 (31), L57 (32) |
| 2 | honest (honesty) | truth | `␣honesty`, `␣honest`, `诚实`, `␣Honest`, `␣honestly`, `诚实守信`, `说实话` | 103 | L35-58; most at L41 (64), L42 (64), L55 (57) |
| 2 | sincere (sincerity) | truth | `␣sincerity`, `真诚`, `␣sincerely`, `␣sincere` | 14 | L37-58; most at L41 (5), L42 (7), L45 (5) |
| 2 | candid (candour) | truth | `坦诚` | 25 | L38-58; most at L42 (15), L51 (14), L52 (23) |
| 2 | confess (confessing) | truth | `坦白`, `␣confess` | 8 | L45-57; most at L51 (6), L52 (8), L53 (4) |
| 2 | integrity (integrity, uprightness) | truth | `诚信`, `␣integrity`, `␣Integrity` | 29 | L38-58; most at L41 (11), L46 (13), L47 (12) |
| 2 | transparent (transparency) | truth | `␣transparency`, `␣Transparency`, `透明`, `␣transparent`, `透明度`, `␣Transparent`, `transparent`, `-transparent`, `␣transparencia` | 14 | L39-58; most at L54 (10), L56 (8), L57 (10) |
| 2 | faithful (faithful, true to) | truth | `忠实`, `␣faithfully` | 6 | L46-57; most at L50 (2), L52 (2), L57 (2) |
| 2 | genuine (genuine, real) | unclear | `␣genuine`, `␣genuinely` | 7 | L36-52; most at L36 (3), L37 (3), L47 (3) |
| 2 | truth (the truth (noun)) | truth | `真相`, `␣truth`, `␣Truth`, `truth`, `Truth`, `␣truths`, `实话`, `真理`, `_truth`, `.truth`, `实情` | 208 | L35-58; most at L38 (195), L39 (191), L40 (195) |
| 2 | fact (facts, factual) | unclear | `␣factual`, `事实`, `␣facts`, `实事求是`, `␣Facts`, `的事实`, `facts`, `Fact`, `␣Fact`, `␣fact`, `fact`, `_fact`, `␣FACT`, `FACT`, `事实和` | 136 | L35-58; most at L38 (116), L39 (102), L46 (88) |
| 2 | admit (admitting) | truth | `承认`, `␣admitting`, `␣admit`, `␣admission`, `␣admitted`, `␣admits` | 34 | L36-58; most at L39 (14), L40 (14), L42 (15) |
| 2 | acknowledge (acknowledging) | truth | `␣acknowledging`, `␣acknowledgment`, `␣acknowledge`, `␣acknowledged`, `␣acknowledges`, `␣acknowledgement` | 19 | L41-58; most at L46 (11), L47 (9), L50 (10) |
| 2 | deny (denying) | unclear | `否认`, `否定`, `␣denying`, `␣denial`, `␣deny`, `␣denied`, `deny`, `␣Denied`, `␣denies`, `否認`, `Denied` | 62 | L36-58; most at L42 (35), L43 (36), L45 (36) |
| 2 | refuse (refusing) | unclear | `␣refusal`, `拒绝`, `␣refusing`, `␣refus`, `␣refused`, `␣refuse`, `␣refuses`, `拒`, `拒絕`, `拒绝了`, `␣отказ`, `拒不`, `␣отказа` | 48 | L36-58; most at L47 (36), L48 (40), L49 (35) |
| 2 | decline (declining) | unclear | `␣declined`, `␣declines`, `␣decline`, `␣declining` | 8 | L55-58; most at L55 (5), L56 (8), L57 (4) |
| 2 | reject (rejecting) | unclear | `␣rejecting`, `␣reject`, `␣rejection`, `␣Reject`, `reject`, `Reject`, `␣rejected` | 15 | L38-57; most at L47 (14), L48 (14), L49 (14) |
| 2 | claim (claiming) | unclear | `声称`, `␣claiming`, `␣claims`, `宣称`, `␣claim`, `␣Claims`, `␣Claim`, `␣claimed`, `claim`, `Claims`, `claims`, `Claim` | 22 | L35-58; most at L36 (14), L37 (13), L46 (10) |
| 2 | assert (asserting) | unclear | `␣assertions`, `␣asserting`, `assert`, `␣assert`, `␣assertion`, `␣Assert`, `␣asserted`, `␣asserts`, `␣Assertion`, `/assert`, `_assert` | 27 | L35-58; most at L38 (13), L45 (13), L46 (15) |
| 2 | alleged (alleged) | unclear | `␣allegations`, `␣alleged`, `␣alleging`, `␣allegation` | 4 | L42-58; most at L47 (2), L48 (2), L51 (3) |
| 2 | purported (so-called, supposedly) | unclear | `␣purported` | 3 | L46-48; most at L46 (1), L47 (3), L48 (2) |
| 2 | disclaimer (disclaimer) | unclear | `␣disclaimer`, `␣Disclaimer`, `Disclaimer` | 39 | L36-54; most at L37 (32), L43 (22), L44 (22) |
| 2 | blame (blaming) | unclear | `␣blaming` | 2 | L51-52; most at L51 (2), L52 (1) |
| 2 | framing (framing, slanted presentation) | unclear | `␣framing` | 3 | L58-58; most at L58 (3) |
| 2 | justify (self-justification) | unclear | `辩解` | 4 | L49-57; most at L49 (2), L51 (2), L54 (3) |
| 2 | clarify (clarifying) | unclear | `澄清`, `␣clarification`, `␣clarify`, `␣clarified` | 14 | L36-58; most at L36 (6), L52 (6), L53 (5) |
| 2 | contradict (contradicting) | unclear | `␣contradict`, `␣contradictory`, `␣contradiction`, `矛盾`, `␣contradictions` | 20 | L36-58; most at L46 (13), L47 (14), L48 (16) |
| 2 | intentional (on purpose) | unclear | `␣intentionally`, `故意`, `␣intentional`, `␣deliberately`, `␣deliberate`, `刻意`, `故意的` | 71 | L36-58; most at L47 (46), L48 (33), L49 (32) |
| 2 | knowingly (with knowledge) | unclear | `␣knowingly`, `明知` | 46 | L39-58; most at L46 (25), L48 (31), L56 (27) |
| 2 | unethical (unethical, immoral) | lie | `␣unethical`, `␣immoral` | 76 | L36-58; most at L43 (72), L44 (70), L45 (65) |
| 2 | ethical (ethical, moral (adjective)) | unclear | `␣ethical`, `␣morally`, `ethical`, `␣moral`, `␣Moral` | 60 | L36-58; most at L43 (47), L44 (45), L45 (51) |
| 2 | ethics (ethics, morality (noun)) | unclear | `␣ethics`, `␣Ethics`, `伦理`, `道德`, `␣morality`, `的道德`, `职业道德` | 37 | L38-58; most at L42 (28), L43 (30), L44 (28) |
| 2 | hypocrisy (hypocrisy) | lie | `␣hypocrisy`, `虚伪` | 21 | L36-53; most at L41 (12), L42 (14), L45 (9) |
| 2 | wrongdoing (misconduct) | lie | `␣wrongdoing` | 3 | L42-58; most at L49 (2), L51 (2), L52 (2) |
| 2 | violate (violating rules) | unclear | `违反`, `违背`, `␣violate`, `␣violates`, `违规`, `␣violating`, `违反了`, `␣violated`, `␣violation`, `␣violations`, `违规行为` | 75 | L36-58; most at L43 (63), L44 (60), L45 (57) |
| 2 | illegal (illegal) | unclear | `␣illegal`, `违法`, `␣illegally`, `illegal`, `␣unlawful`, `␣ilegal`, `Illegal`, `违法行为` | 23 | L36-58; most at L43 (13), L44 (21), L45 (15) |
| 2 | lawful (legal, lawful) | unclear | `合法`, `␣legality`, `␣legal`, `␣Legal`, `␣legally`, `␣lawful`, `/legal`, `legal`, `Legal`, `␣legale`, `合法的` | 19 | L36-58; most at L45 (12), L46 (8), L47 (12) |
| 2 | prohibited (forbidden) | unclear | `␣prohibited`, `禁止`, `严禁`, `␣prohibition`, `␣prohibits`, `␣prohibiting` | 47 | L37-51; most at L45 (27), L46 (30), L47 (34) |
| 2 | comply (complying) | unclear | `␣compliance`, `␣Compliance`, `合规`, `␣complying`, `␣comply`, `␣compliant`, `␣complied` | 25 | L38-58; most at L46 (17), L47 (17), L54 (15) |
| 2 | adhere (adhering, abiding by) | unclear | `␣adherence`, `遵守`, `遵循`, `␣adher`, `␣adhere`, `严格遵守`, `遵照`, `遵从` | 39 | L38-58; most at L56 (24), L57 (24), L58 (28) |
| 2 | obey (obeying) | unclear | `␣obey`, `服从`, `␣obedience` | 10 | L48-58; most at L49 (5), L53 (4), L54 (7) |
| 2 | instructions (instructions, directives) | unclear | `␣instructions`, `␣Instructions`, `␣instructed`, `指令`, `instructions`, `␣instruction`, `Instructions`, `␣directives`, `Instruction`, `␣Instruction`, `instruction`, `␣directive`, `_instructions`, `␣instrucciones`, `␣Directive`, `␣instruct`, `.instructions`, `/Instruction`, `Directive`, `_instruction` | 41 | L39-58; most at L53 (34), L54 (33), L55 (34) |
| 2 | mandated (ordered, required) | unclear | `␣mandated`, `␣mandate`, `␣mandates`, `␣mandatory`, `␣Mandatory`, `mandatory`, `␣mandat`, `␣mandato` | 44 | L39-58; most at L47 (43), L48 (41), L49 (35) |
| 2 | tasked (assigned a task) | unclear | `␣tasked` | 22 | L46-55; most at L48 (18), L49 (15), L51 (16) |
| 2 | constraints (constraints) | unclear | `␣constraints`, `␣Constraints`, `约束`, `␣constraint`, `␣Constraint`, `Constraints`, `Constraint`, `constraints`, `␣constrained`, `constraint`, `␣CONSTRAINT`, `_constraints` | 25 | L39-58; most at L50 (14), L54 (15), L55 (16) |
| 2 | pressured (under pressure) | unclear | `␣pressure`, `␣Pressure`, `Pressure`, `pressure`, `␣pressured`, `␣pressures`, `-pressure` | 2 | L54-57; most at L54 (2), L55 (2), L56 (1) |
| 2 | forced (forced, coerced) | unclear | `␣forced`, `␣compelled`, `␣coerc`, `␣coercion` | 4 | L47-56; most at L47 (2), L48 (3), L49 (3) |
| 2 | loyal (loyalty) | unclear | `␣loyalty`, `␣loyal`, `忠诚`, `忠诚度` | 16 | L42-58; most at L54 (9), L55 (7), L57 (13) |
| 2 | protect (protecting) | unclear | `␣protecting`, `保护`, `␣Protect`, `␣protect`, `protect`, `Protect`, `␣protective`, `为了保护`, `␣protection`, `␣protects`, `␣Protection`, `␣protections`, `␣Protective`, `的保护`, `Protection`, `␣protected` | 11 | L36-58; most at L44 (7), L45 (7), L47 (8) |
| 2 | diplomatic (diplomatic tact) | unclear | `␣diplomatic` | 1 | L49-51; most at L49 (1), L51 (1) |
| 2 | persona (an adopted persona) | unclear | `␣persona`, `␣Persona`, `Persona`, `␣personas`, `persona`, `␣Personas`, `_persona` | 19 | L42-58; most at L52 (13), L56 (17), L57 (14) |
| 2 | role (a role being played) | unclear | `␣Role`, `␣role`, `role`, `Role`, `角色`, `␣roles`, `-role`, `␣Roles`, `的角色`, `角色的`, `␣ROLE`, `Roles` | 5 | L47-57; most at L51 (5), L52 (5), L53 (2) |
| 2 | roleplay (role-playing) | unclear | `角色扮演`, `扮演` | 7 | L48-57; most at L51 (6), L52 (6), L53 (3) |
| 2 | simulate (simulating) | unclear | `␣simulation`, `␣Simulation`, `Simulation`, `simulation`, `模拟` | 1 | L51-58; most at L51 (1), L52 (1), L53 (1) |
| 2 | scripted (scripted) | unclear | `␣scripted` | 1 | L52-57; most at L52 (1), L53 (1), L55 (1) |
| 2 | fiction (fiction, fictional) | unclear | `虚构`, `␣fictional`, `␣Fiction`, `␣fict`, `fiction`, `␣fiction` | 41 | L37-56; most at L42 (16), L50 (22), L51 (22) |

## q_tok25

| rep | family | side | members | visibility | layer profile |
|---|---|---|---|---|---|
| 1 | truth (the truth (what is actually so)) | truth | `真相` | 75 | L39-42; most at L40 (67), L41 (56), L42 (23) |
| 1 | honest (being honest) | truth | `␣honest`, `␣honesty` | 2 | L42-47; most at L42 (1), L47 (1) |
| 1 | deny (denying) | lie | `否认` | 226 | L38-55; most at L40 (166), L41 (165), L42 (226) |
| 1 | clarify (clarifying) | unclear | `澄清` | 135 | L37-43; most at L41 (27), L42 (135), L43 (3) |
| 1 | claim (claiming) | unclear | `␣Claim` | 1 | L47-47; most at L47 (1) |
| 1 | assert (asserting) | unclear | `␣assertions` | 7 | L45-47; most at L45 (5), L46 (3), L47 (2) |
| 1 | justify (justifying oneself) | unclear | `辩解` | 1 | L42-42; most at L42 (1) |
| 1 | innocent (not guilty) | truth | `无罪` | 2 | L40-42; most at L40 (1), L42 (2) |
| 2 | honest (honesty) | truth | `␣honest`, `␣honesty` | 2 | L42-47; most at L42 (1), L47 (1) |
| 2 | truth (the truth (noun)) | truth | `真相` | 75 | L39-42; most at L40 (67), L41 (56), L42 (23) |
| 2 | deny (denying) | unclear | `否认`, `否定` | 226 | L38-55; most at L40 (167), L41 (166), L42 (226) |
| 2 | claim (claiming) | unclear | `␣Claim` | 1 | L47-47; most at L47 (1) |
| 2 | assert (asserting) | unclear | `␣assertions` | 7 | L45-47; most at L45 (5), L46 (3), L47 (2) |
| 2 | justify (self-justification) | unclear | `辩解` | 1 | L42-42; most at L42 (1) |
| 2 | clarify (clarifying) | unclear | `澄清` | 135 | L37-43; most at L41 (27), L42 (135), L43 (3) |
| 2 | innocent (not guilty) | truth | `无罪` | 2 | L40-42; most at L40 (1), L42 (2) |

## q_tok26

| rep | family | side | members | visibility | layer profile |
|---|---|---|---|---|---|
| 1 | truth (the truth (what is actually so)) | truth | `␣truth`, `真相`, `truth`, `␣Truth`, `Truth`, `␣truths`, `实话`, `真理`, `实情`, `_truth`, `.truth`, `␣verdad` | 225 | L35-58; most at L38 (216), L39 (209), L40 (210) |
| 1 | honest (being honest) | truth | `␣honest`, `␣honestly`, `诚实`, `␣honesty`, `坦诚`, `␣Honest`, `诚信`, `␣чест`, `␣честно` | 63 | L35-58; most at L38 (37), L42 (36), L45 (36) |
| 1 | dishonest (being dishonest) | lie | `␣dishonest` | 10 | L41-53; most at L44 (6), L45 (10), L46 (5) |
| 1 | sincere (being sincere) | truth | `真诚`, `␣sincerity` | 3 | L38-53; most at L40 (3), L41 (3), L42 (3) |
| 1 | integrity (moral uprightness) | truth | `␣integrity` | 1 | L44-47; most at L44 (1), L45 (1), L46 (1) |
| 1 | confess (confessing) | truth | `坦白`, `␣confess` | 6 | L40-58; most at L51 (2), L52 (5), L54 (3) |
| 1 | transparent (being transparent (open)) | truth | `␣transparency`, `透明`, `␣transparent`, `␣Transparency` | 8 | L41-57; most at L43 (2), L54 (5), L55 (3) |
| 1 | factual (based on facts) | truth | `␣factual`, `事实`, `␣facts`, `实事求是`, `的事实`, `facts`, `␣fact`, `␣Facts`, `Fact`, `␣Fact`, `fact`, `␣FACT`, `事实和`, `_fact`, `FACT` | 153 | L35-58; most at L39 (116), L40 (100), L42 (118) |
| 1 | actual (the actual state, as opposed to what was said) | unclear | `␣actually`, `␣actual`, `实际情况`, `但实际上`, `actually`, `actual`, `实际`, `实际上`, `␣reality`, `Actually`, `实际的`, `的实际`, `事实上`, `实际上是`, `Actual`, `␣Actual`, `␣Actually`, `_actual`, `␣Reality`, `Reality` | 83 | L35-58; most at L45 (68), L46 (72), L47 (44) |
| 1 | genuine (genuine, authentic) | truth | `␣genuinely`, `␣genuine` | 92 | L35-58; most at L37 (57), L38 (68), L45 (61) |
| 1 | legitimate (legitimate) | unclear | `␣legitimate`, `␣legitimately`, `␣legitim`, `␣legitimacy` | 31 | L36-56; most at L44 (16), L45 (23), L46 (17) |
| 1 | fake (fake, not real) | lie | `虚假`, `␣fake`, `fake`, `Fake`, `假的`, `␣Fake`, `.fake`, `假`, `_fake` | 122 | L36-58; most at L43 (99), L44 (105), L45 (94) |
| 1 | fabricate (fabricating or forging) | lie | `伪造`, `␣fabricated`, `造假`, `␣fabrication`, `弄虚作假` | 42 | L36-58; most at L40 (22), L41 (24), L42 (25) |
| 1 | fictional (fictional, made up as fiction) | unclear | `虚构`, `␣fict`, `␣fictional`, `fiction`, `␣Fiction`, `␣fiction`, `-fiction` | 62 | L36-58; most at L46 (55), L47 (43), L48 (49) |
| 1 | misinformation (false information) | lie | `␣misinformation`, `虚假信息` | 110 | L35-56; most at L38 (58), L41 (62), L42 (82) |
| 1 | deceive (the act of deceiving) | lie | `欺骗`, `␣deception`, `␣deceptive`, `␣deceive` | 42 | L36-58; most at L40 (22), L41 (28), L42 (22) |
| 1 | fraud (fraud) | lie | `␣fraudulent`, `␣fraud` | 7 | L37-54; most at L44 (2), L45 (3), L46 (2) |
| 1 | cheat (cheating) | lie | `␣cheated` | 1 | L52-53; most at L52 (1), L53 (1) |
| 1 | mislead (misleading) | lie | `␣misleading`, `误导`, `␣misled`, `误导性` | 107 | L36-58; most at L44 (89), L45 (85), L48 (80) |
| 1 | misrepresent (misrepresenting) | lie | `␣misrepresented` | 39 | L36-58; most at L42 (15), L44 (16), L45 (15) |
| 1 | conceal (concealing or hiding) | lie | `隐瞒`, `掩盖`, `␣conceal`, `␣concealed`, `hide`, `Hide`, `_hide`, `隐藏` | 70 | L35-58; most at L40 (44), L42 (46), L43 (48) |
| 1 | disguise (disguising) | lie | `伪装`, `␣disguise` | 3 | L48-53; most at L48 (3), L49 (3), L50 (1) |
| 1 | pretend (pretending) | lie | `␣pretending`, `␣pretend`, `␣pretended`, `假装` | 11 | L46-54; most at L48 (5), L49 (3), L50 (10) |
| 1 | withhold (withholding) | lie | `␣withholding`, `␣withheld` | 2 | L49-56; most at L49 (1), L52 (2), L53 (2) |
| 1 | omit (omitting) | lie | `␣omit`, `␣omission`, `␣omitted` | 4 | L41-58; most at L52 (3), L53 (3), L54 (2) |
| 1 | secret (secrecy) | lie | `␣undisclosed`, `␣secrecy`, `秘密` | 7 | L38-54; most at L42 (4), L43 (4), L44 (3) |
| 1 | confidential (confidentiality (a duty to keep information private)) | unclear | `␣confidentiality`, `保密` | 8 | L38-54; most at L40 (3), L42 (7), L43 (6) |
| 1 | unethical (morally wrong) | lie | `␣unethical` | 3 | L37-43; most at L37 (1), L38 (2), L39 (3) |
| 1 | ethical (ethical, morally right) | unclear | `␣ethical`, `ethical` | 14 | L37-58; most at L40 (9), L45 (9), L53 (9) |
| 1 | ethics (ethics or morality as a topic) | unclear | `␣ethics`, `伦理`, `␣moral`, `道德`, `␣ethic`, `␣Ethics` | 9 | L38-58; most at L41 (7), L43 (6), L58 (8) |
| 1 | intentional (doing it on purpose) | unclear | `␣intentionally`, `␣intentional`, `故意`, `␣deliberately`, `␣deliberate` | 7 | L39-58; most at L47 (3), L55 (3), L56 (3) |
| 1 | knowingly (doing it while knowing) | unclear | `␣knowingly` | 2 | L56-58; most at L56 (1), L57 (1), L58 (2) |
| 1 | violate (violating a rule or principle) | unclear | `违背`, `␣violated` | 8 | L45-53; most at L47 (2), L48 (5), L49 (3) |
| 1 | illegal (illegal) | lie | `␣illegal`, `␣illegally`, `␣unlawful`, `违法` | 3 | L40-58; most at L44 (3), L45 (2), L46 (2) |
| 1 | legal (legal, lawful) | unclear | `␣legality`, `␣legal`, `␣legally`, `合法`, `/legal`, `legal`, `Legal`, `␣Legal`, `␣lawful`, `LEGAL`, `_legal`, `合法性`, `␣legale` | 18 | L36-58; most at L42 (8), L43 (8), L45 (15) |
| 1 | prohibited (prohibited) | unclear | `禁止`, `␣prohibited`, `␣prohibiting`, `␣prohibition`, `严禁`, `␣prohibits` | 10 | L38-53; most at L39 (9), L40 (8), L43 (8) |
| 1 | comply (complying) | unclear | `合规`, `␣compliance`, `␣comply`, `␣Compliance`, `␣complied`, `␣compliant`, `␣complying` | 6 | L39-58; most at L51 (4), L52 (5), L53 (5) |
| 1 | adhere (adhering to rules) | unclear | `␣adherence`, `␣adher`, `␣adhere`, `严格遵守`, `遵守`, `遵守国家` | 8 | L47-58; most at L52 (6), L53 (7), L54 (6) |
| 1 | refuse (refusing) | unclear | `␣refusal`, `␣refusing`, `拒绝`, `␣refused`, `␣refus`, `␣refuse`, `␣refuses`, `拒`, `拒絕`, `拒绝了`, `␣отказ`, `␣отказа`, `拒不` | 18 | L36-58; most at L56 (16), L57 (16), L58 (16) |
| 1 | decline (declining (saying no to a request)) | unclear | `␣declined`, `␣declines`, `␣decline`, `␣declining` | 6 | L55-58; most at L55 (4), L56 (5), L57 (4) |
| 1 | reject (rejecting) | unclear | `␣rejecting`, `␣rejection`, `reject`, `Reject`, `␣reject`, `␣rejected` | 8 | L39-57; most at L48 (5), L49 (6), L50 (7) |
| 1 | deny (denying) | lie | `否认`, `␣denying`, `␣denial`, `␣deny`, `␣denies`, `␣denied`, `deny`, `␣Denied`, `否認`, `Denied` | 60 | L36-58; most at L40 (28), L42 (30), L43 (32) |
| 1 | admit (admitting) | truth | `承认`, `␣admitting`, `␣admit`, `␣admitted`, `␣admits`, `␣admite` | 21 | L36-58; most at L51 (14), L55 (14), L57 (14) |
| 1 | acknowledge (acknowledging) | truth | `␣acknowledging`, `␣acknowledgment`, `␣acknowledge`, `␣acknowledges`, `␣acknowledged`, `␣acknowledgement` | 20 | L39-58; most at L50 (12), L51 (17), L53 (11) |
| 1 | clarify (clarifying) | unclear | `␣clarification`, `澄清`, `␣clarified`, `␣clarify` | 9 | L40-58; most at L52 (4), L57 (5), L58 (5) |
| 1 | claim (claiming) | unclear | `␣claiming`, `声称`, `␣claims`, `␣claim`, `claim`, `␣claimed`, `宣称`, `␣Claims`, `claims`, `␣Claim`, `Claim`, `Claims`, `CLAIM`, `␣CLAIM`, `_claim`, `claimed`, `.Claims` | 109 | L36-58; most at L47 (59), L50 (56), L51 (58) |
| 1 | assert (asserting) | unclear | `␣assertions`, `␣asserting`, `assert`, `␣assertion`, `␣asserted`, `␣assert`, `␣asserts`, `␣Assert`, `_assert`, `/assert`, `(assert`, `Assert`, `␣Assertion`, `␣Assertions`, `Assertion`, `.assert`, `Assertions` | 59 | L36-58; most at L47 (31), L52 (31), L54 (35) |
| 1 | purported (so-called, supposedly so) | unclear | `␣якобы`, `␣purported`, `所谓的`, `␣supposedly`, `所谓` | 52 | L39-58; most at L46 (26), L47 (32), L48 (29) |
| 1 | allege (alleging) | unclear | `␣alleging`, `␣alleged`, `␣allegations`, `␣allegedly`, `␣alleges`, `␣allegation`, `␣allege`, `␣Alleg` | 27 | L37-58; most at L51 (13), L52 (12), L53 (11) |
| 1 | disclaimer (a disclaimer) | unclear | `␣disclaimer`, `␣Disclaimer`, `Disclaimer` | 28 | L36-57; most at L42 (25), L43 (17), L44 (16) |
| 1 | blame (blaming) | unclear | `␣blaming`, `␣blame`, `␣blamed`, `␣blames` | 45 | L41-58; most at L51 (39), L52 (40), L54 (42) |
| 1 | exaggerate (exaggerating) | lie | `夸大`, `␣exaggerated` | 13 | L40-57; most at L48 (9), L49 (7), L50 (7) |
| 1 | vague (being vague) | unclear | `␣vague`, `␣vaguely` | 30 | L39-58; most at L48 (19), L52 (22), L53 (19) |
| 1 | ambiguous (being ambiguous) | unclear | `␣ambiguous`, `␣ambiguity`, `␣ambigu`, `ambiguous` | 14 | L37-58; most at L42 (5), L45 (8), L46 (5) |
| 1 | evade (evading) | lie | `␣evasion`, `␣evade` | 4 | L52-58; most at L53 (3), L56 (2), L57 (3) |
| 1 | avoid (avoiding) | unclear | `␣avoiding`, `␣avoidance`, `␣avoided`, `␣avoid` | 3 | L42-58; most at L42 (1), L43 (1), L48 (2) |
| 1 | framing (framing (presenting something in a chosen light)) | unclear | `␣framing`, `␣framed`, `␣frames`, `frames`, `␣Frames` | 29 | L50-58; most at L52 (15), L53 (13), L58 (25) |
| 1 | reinterpret (reinterpreting) | unclear | `␣reinterpret`, `reinterpret` | 20 | L42-58; most at L51 (11), L52 (10), L53 (13) |
| 1 | faithful (faithful, accurate to the source) | truth | `␣faithful`, `␣faithfully`, `忠实` | 1 | L51-58; most at L51 (1), L52 (1), L53 (1) |
| 1 | loyal (loyalty) | unclear | `忠诚` | 1 | L57-57; most at L57 (1) |
| 1 | persona (an assumed persona) | unclear | `␣persona`, `␣personas`, `␣Persona`, `Persona`, `␣Personas` | 1 | L53-58; most at L53 (1), L54 (1), L55 (1) |
| 1 | simulate (simulating) | unclear | `␣simulated` | 2 | L45-52; most at L45 (1), L46 (1), L47 (1) |
| 1 | protect (protecting) | unclear | `␣protecting`, `␣protect`, `␣protections` | 3 | L44-58; most at L45 (2), L47 (2), L52 (1) |
| 1 | instructed (being instructed or tasked) | unclear | `␣instructed` | 1 | L51-58; most at L51 (1), L52 (1), L53 (1) |
| 1 | contradict (contradicting) | unclear | `␣contradict`, `␣contradictory`, `␣contradiction` | 49 | L37-58; most at L45 (30), L47 (31), L48 (32) |
| 1 | excuse (an excuse) | lie | `借口`, `␣excuse`, `␣excuses` | 13 | L48-57; most at L51 (8), L52 (6), L53 (5) |
| 1 | justify (justifying oneself) | unclear | `辩解`, `␣justification` | 6 | L42-55; most at L47 (2), L49 (3), L52 (3) |
| 1 | innocent (not guilty) | truth | `无罪` | 1 | L39-42; most at L39 (1), L40 (1), L41 (1) |
| 1 | apology (apologizing) | truth | `␣apology` | 1 | L51-52; most at L51 (1), L52 (1) |
| 2 | deceive (the act of deceiving) | lie | `欺骗`, `␣deception`, `␣deceptive`, `␣deceive` | 42 | L36-58; most at L40 (22), L41 (28), L42 (22) |
| 2 | mislead (leading someone to a wrong belief) | lie | `␣misleading`, `误导`, `␣misled`, `误导性` | 107 | L36-58; most at L44 (89), L45 (85), L48 (80) |
| 2 | misrepresent (presenting something falsely) | lie | `␣misrepresented` | 39 | L36-58; most at L42 (15), L44 (16), L45 (15) |
| 2 | misinformation (false information) | lie | `␣misinformation`, `虚假信息` | 110 | L35-56; most at L38 (58), L41 (62), L42 (82) |
| 2 | fake (fake, not genuine) | lie | `␣fake`, `fake`, `Fake`, `␣Fake`, `.fake`, `_fake` | 103 | L36-54; most at L44 (81), L45 (73), L46 (75) |
| 2 | fabricate (making up false content) | lie | `伪造`, `␣fabricated`, `造假`, `␣fabrication`, `弄虚作假` | 42 | L36-58; most at L40 (22), L41 (24), L42 (25) |
| 2 | fraud (fraud, swindling) | lie | `␣fraudulent`, `骗局`, `␣fraud` | 8 | L37-54; most at L45 (3), L46 (2), L50 (3) |
| 2 | cheat (cheating) | lie | `␣cheated` | 1 | L52-53; most at L52 (1), L53 (1) |
| 2 | pretend (pretending) | lie | `␣pretending`, `␣pretend`, `␣pretended`, `假装` | 11 | L46-54; most at L48 (5), L49 (3), L50 (10) |
| 2 | impersonate (posing as someone else) | lie | `冒充` | 1 | L48-49; most at L48 (1), L49 (1) |
| 2 | disguise (disguising) | lie | `伪装`, `␣disguise` | 3 | L48-53; most at L48 (3), L49 (3), L50 (1) |
| 2 | exaggerate (exaggerating) | lie | `夸大`, `␣exaggerated` | 13 | L40-57; most at L48 (9), L49 (7), L50 (7) |
| 2 | manipulate (manipulating) | lie | `␣manipulated` | 1 | L53-53; most at L53 (1) |
| 2 | spin (spin: slanted presentation) | lie | `␣spin`, `␣spinning`, `␣spins`, `spin`, `Spin`, `-spin` | 1 | L58-58; most at L58 (1) |
| 2 | conceal (concealing) | lie | `隐瞒`, `␣conceal`, `␣concealed` | 67 | L35-58; most at L40 (44), L42 (46), L43 (48) |
| 2 | hide (hiding) | lie | `␣hiding`, `Hide`, `hide`, `_hide`, `隐藏` | 3 | L53-58; most at L53 (2), L58 (2) |
| 2 | cover up (covering up) | lie | `掩盖` | 10 | L48-58; most at L48 (5), L52 (5), L53 (6) |
| 2 | withhold (withholding information) | lie | `␣withholding`, `␣withheld` | 2 | L49-56; most at L49 (1), L52 (2), L53 (2) |
| 2 | omit (leaving something out) | lie | `␣omit`, `␣omission`, `省略`, `␣omitted` | 4 | L40-58; most at L52 (3), L53 (3), L54 (2) |
| 2 | evade (evading) | lie | `␣evasion`, `回避`, `␣evade` | 5 | L42-58; most at L53 (4), L56 (2), L57 (3) |
| 2 | avoid (avoiding) | unclear | `␣avoidance`, `␣avoiding`, `␣avoided`, `␣avoid` | 3 | L42-58; most at L42 (1), L43 (1), L48 (2) |
| 2 | vague (being vague) | unclear | `␣vague`, `␣vaguely`, `含糊` | 30 | L39-58; most at L48 (19), L52 (22), L53 (19) |
| 2 | ambiguous (ambiguity) | unclear | `␣ambiguous`, `␣ambiguity`, `␣ambigu`, `ambiguous` | 14 | L37-58; most at L42 (5), L45 (8), L46 (5) |
| 2 | secret (secrecy) | lie | `␣secrecy`, `秘密` | 3 | L39-54; most at L43 (2), L51 (1), L52 (1) |
| 2 | confidential (keeping information confidential) | unclear | `␣confidentiality`, `保密` | 8 | L38-54; most at L40 (3), L42 (7), L43 (6) |
| 2 | undisclosed (not disclosed) | lie | `␣undisclosed` | 6 | L38-52; most at L42 (3), L43 (3), L44 (2) |
| 2 | disclose (disclosing) | truth | `␣disclosure`, `␣disclosed`, `␣disclosing`, `␣disclose`, `␣Disclosure`, `Disclosure`, `披露` | 10 | L41-58; most at L42 (4), L43 (4), L52 (5) |
| 2 | reveal (revealing) | truth | `␣revealed`, `␣revealing`, `␣reveal`, `reveal` | 2 | L58-58; most at L58 (2) |
| 2 | dishonest (dishonesty) | lie | `␣dishonest` | 10 | L41-53; most at L44 (6), L45 (10), L46 (5) |
| 2 | honest (honesty) | truth | `␣honest`, `␣honestly`, `诚实`, `␣honesty`, `␣Honest`, `␣честно` | 63 | L35-58; most at L38 (37), L42 (36), L45 (36) |
| 2 | sincere (sincerity) | truth | `真诚`, `␣sincerity` | 3 | L38-53; most at L40 (3), L41 (3), L42 (3) |
| 2 | candid (candour) | truth | `坦诚` | 14 | L38-57; most at L41 (7), L42 (9), L52 (9) |
| 2 | confess (confessing) | truth | `坦白`, `␣confess` | 6 | L40-58; most at L51 (2), L52 (5), L54 (3) |
| 2 | integrity (integrity, uprightness) | truth | `诚信`, `␣integrity` | 4 | L37-47; most at L39 (3), L41 (3), L42 (3) |
| 2 | transparent (transparency) | truth | `␣transparency`, `透明`, `␣Transparency`, `␣transparent` | 8 | L41-57; most at L43 (2), L54 (5), L55 (3) |
| 2 | faithful (faithful, true to) | truth | `␣faithfully`, `␣faithful`, `忠实` | 1 | L51-58; most at L51 (1), L52 (1), L53 (1) |
| 2 | genuine (genuine, real) | unclear | `␣genuinely`, `␣genuine` | 92 | L35-58; most at L37 (57), L38 (68), L45 (61) |
| 2 | truth (the truth (noun)) | truth | `␣truth`, `真相`, `truth`, `␣Truth`, `Truth`, `␣truths`, `实话`, `真理`, `实情`, `_truth`, `.truth` | 225 | L35-58; most at L38 (216), L39 (209), L40 (210) |
| 2 | fact (facts, factual) | unclear | `␣factual`, `事实`, `␣facts`, `实事求是`, `的事实`, `facts`, `␣Facts`, `␣fact`, `␣Fact`, `Fact`, `␣FACT`, `fact`, `事实和`, `_fact`, `FACT` | 153 | L35-58; most at L39 (116), L40 (100), L42 (118) |
| 2 | admit (admitting) | truth | `承认`, `␣admitting`, `␣admit`, `␣admitted`, `␣admission`, `␣admits`, `␣Admission`, `␣admissions`, `␣admite` | 21 | L36-58; most at L51 (14), L55 (14), L57 (14) |
| 2 | acknowledge (acknowledging) | truth | `␣acknowledging`, `␣acknowledgment`, `␣acknowledge`, `␣acknowledges`, `␣acknowledged`, `␣acknowledgement` | 20 | L39-58; most at L50 (12), L51 (17), L53 (11) |
| 2 | deny (denying) | unclear | `否认`, `␣denying`, `␣denial`, `␣deny`, `否定`, `␣denies`, `␣denied`, `deny`, `␣Denied`, `否認`, `Denied` | 61 | L36-58; most at L40 (28), L42 (30), L43 (33) |
| 2 | refuse (refusing) | unclear | `␣refusal`, `␣refusing`, `拒绝`, `␣refused`, `␣refus`, `␣refuse`, `␣refuses`, `拒`, `拒絕`, `拒绝了`, `␣отказ`, `␣отказа`, `拒不` | 18 | L36-58; most at L56 (16), L57 (16), L58 (16) |
| 2 | decline (declining) | unclear | `␣declined`, `␣declines`, `␣decline`, `␣declining` | 6 | L55-58; most at L55 (4), L56 (5), L57 (4) |
| 2 | reject (rejecting) | unclear | `␣rejecting`, `␣rejection`, `reject`, `Reject`, `␣rejected`, `␣reject` | 8 | L39-57; most at L48 (5), L49 (6), L50 (7) |
| 2 | claim (claiming) | unclear | `␣claiming`, `声称`, `␣claims`, `␣claim`, `claim`, `␣claimed`, `宣称`, `␣Claims`, `claims`, `␣Claim`, `Claim`, `Claims`, `CLAIM`, `␣CLAIM`, `_claim`, `claimed`, `.Claims` | 109 | L36-58; most at L47 (59), L50 (56), L51 (58) |
| 2 | assert (asserting) | unclear | `␣assertions`, `␣asserting`, `assert`, `␣assertion`, `␣asserted`, `␣assert`, `␣asserts`, `␣Assert`, `_assert`, `/assert`, `(assert`, `Assert`, `␣Assertion`, `␣Assertions`, `Assertion`, `Assertions`, `.assert` | 59 | L36-58; most at L47 (31), L52 (31), L54 (35) |
| 2 | alleged (alleged) | unclear | `␣alleging`, `␣alleged`, `␣allegations`, `␣allegedly`, `␣alleges`, `␣allege`, `␣allegation`, `␣Alleg` | 27 | L37-58; most at L51 (13), L52 (12), L53 (11) |
| 2 | purported (so-called, supposedly) | unclear | `␣якобы`, `␣purported`, `所谓的`, `␣supposedly`, `所谓` | 52 | L39-58; most at L46 (26), L47 (32), L48 (29) |
| 2 | disclaimer (disclaimer) | unclear | `␣disclaimer`, `␣Disclaimer`, `Disclaimer` | 28 | L36-57; most at L42 (25), L43 (17), L44 (16) |
| 2 | blame (blaming) | unclear | `␣blaming`, `␣blame`, `␣blamed`, `␣blames` | 45 | L41-58; most at L51 (39), L52 (40), L54 (42) |
| 2 | framing (framing, slanted presentation) | unclear | `␣framing`, `␣framed` | 29 | L50-58; most at L52 (15), L53 (13), L58 (25) |
| 2 | excuse (excuses) | unclear | `借口`, `␣excuse`, `␣excuses` | 13 | L48-57; most at L51 (8), L52 (6), L53 (5) |
| 2 | justify (self-justification) | unclear | `辩解`, `␣justification` | 6 | L42-55; most at L47 (2), L49 (3), L52 (3) |
| 2 | apology (apologising) | unclear | `␣apology` | 1 | L51-52; most at L51 (1), L52 (1) |
| 2 | clarify (clarifying) | unclear | `␣clarification`, `澄清`, `␣clarified`, `␣clarify` | 9 | L40-58; most at L52 (4), L57 (5), L58 (5) |
| 2 | contradict (contradicting) | unclear | `␣contradict`, `␣contradictory`, `␣contradiction` | 49 | L37-58; most at L45 (30), L47 (31), L48 (32) |
| 2 | intentional (on purpose) | unclear | `␣intentionally`, `␣intentional`, `故意`, `␣deliberately`, `␣deliberate` | 7 | L39-58; most at L47 (3), L55 (3), L56 (3) |
| 2 | knowingly (with knowledge) | unclear | `␣knowingly` | 2 | L56-58; most at L56 (1), L57 (1), L58 (2) |
| 2 | unethical (unethical, immoral) | lie | `␣unethical` | 3 | L37-43; most at L37 (1), L38 (2), L39 (3) |
| 2 | ethical (ethical, moral (adjective)) | unclear | `␣ethical`, `ethical`, `␣moral` | 14 | L37-58; most at L40 (9), L45 (9), L53 (9) |
| 2 | ethics (ethics, morality (noun)) | unclear | `␣ethics`, `伦理`, `道德`, `␣ethic`, `␣Ethics` | 9 | L38-58; most at L41 (7), L43 (6), L58 (8) |
| 2 | innocent (not guilty) | truth | `无罪` | 1 | L39-42; most at L39 (1), L40 (1), L41 (1) |
| 2 | violate (violating rules) | unclear | `违背`, `␣violated` | 8 | L45-53; most at L47 (2), L48 (5), L49 (3) |
| 2 | illegal (illegal) | unclear | `␣illegal`, `␣illegally`, `␣unlawful`, `违法` | 3 | L40-58; most at L44 (3), L45 (2), L46 (2) |
| 2 | lawful (legal, lawful) | unclear | `␣legality`, `␣legal`, `␣legally`, `合法`, `/legal`, `legal`, `Legal`, `␣lawful`, `␣Legal`, `LEGAL`, `_legal`, `␣legale`, `合法性` | 18 | L36-58; most at L42 (8), L43 (8), L45 (15) |
| 2 | prohibited (forbidden) | unclear | `禁止`, `␣prohibited`, `␣prohibiting`, `␣prohibition`, `严禁`, `␣prohibits` | 10 | L38-53; most at L39 (9), L40 (8), L43 (8) |
| 2 | comply (complying) | unclear | `合规`, `␣compliance`, `␣Compliance`, `␣comply`, `␣complied`, `␣complying`, `␣compliant` | 6 | L39-58; most at L51 (4), L52 (5), L53 (5) |
| 2 | adhere (adhering, abiding by) | unclear | `␣adherence`, `␣adher`, `␣adhere`, `严格遵守`, `遵守`, `遵守国家` | 8 | L47-58; most at L52 (6), L53 (7), L54 (6) |
| 2 | instructions (instructions, directives) | unclear | `␣instructions`, `␣instruction`, `␣instruct`, `␣instructed`, `␣directives`, `␣directive`, `指令` | 2 | L51-58; most at L52 (2), L53 (2), L54 (2) |
| 2 | constraints (constraints) | unclear | `␣constraints`, `␣Constraints`, `␣constraint`, `␣Constraint`, `␣CONSTRAINT`, `约束` | 1 | L54-58; most at L54 (1), L55 (1), L56 (1) |
| 2 | loyal (loyalty) | unclear | `忠诚` | 1 | L57-57; most at L57 (1) |
| 2 | protect (protecting) | unclear | `␣protecting`, `␣protect`, `␣protections` | 3 | L44-58; most at L45 (2), L47 (2), L52 (1) |
| 2 | responsible (acting responsibly) | unclear | `␣responsibly` | 1 | L40-54; most at L40 (1), L42 (1), L44 (1) |
| 2 | persona (an adopted persona) | unclear | `␣persona`, `␣Persona`, `Persona`, `␣personas`, `␣Personas` | 1 | L53-58; most at L53 (1), L54 (1), L55 (1) |
| 2 | role (a role being played) | unclear | `␣role`, `role`, `roles`, `␣roles`, `␣Roles`, `角色` | 1 | L55-58; most at L55 (1), L56 (1), L57 (1) |
| 2 | simulate (simulating) | unclear | `␣simulated` | 2 | L45-52; most at L45 (1), L46 (1), L47 (1) |
| 2 | fiction (fiction, fictional) | unclear | `虚构`, `␣fict`, `␣fictional`, `fiction`, `␣Fiction`, `␣fiction`, `-fiction` | 62 | L36-58; most at L46 (55), L47 (43), L48 (49) |

## q_tok27

| rep | family | side | members | visibility | layer profile |
|---|---|---|---|---|---|
| 1 | truth (the truth (what is actually so)) | truth | `␣truth`, `␣Truth`, `truth`, `Truth`, `真相`, `实话`, `_truth` | 66 | L38-58; most at L55 (64), L56 (20), L57 (15) |
| 1 | honest (being honest) | truth | `␣honesty`, `␣honest`, `诚实`, `诚信` | 47 | L39-58; most at L51 (34), L52 (37), L53 (30) |
| 1 | dishonest (being dishonest) | lie | `␣dishonest` | 29 | L37-56; most at L43 (21), L44 (24), L45 (22) |
| 1 | integrity (moral uprightness) | truth | `␣Integrity`, `␣integrity` | 3 | L44-57; most at L50 (2), L51 (3), L55 (2) |
| 1 | factual (based on facts) | truth | `实事求是` | 2 | L52-53; most at L52 (1), L53 (1) |
| 1 | fake (fake, not real) | lie | `fake`, `␣fake`, `Fake`, `假`, `虚假`, `␣Fake` | 86 | L36-53; most at L39 (25), L40 (57), L47 (22) |
| 1 | fabricate (fabricating or forging) | lie | `伪造`, `␣fabricated` | 17 | L36-58; most at L44 (6), L50 (12), L51 (6) |
| 1 | fictional (fictional, made up as fiction) | unclear | `␣fictional`, `虚构`, `␣Fiction`, `fiction`, `␣fict`, `␣fiction` | 94 | L37-57; most at L42 (82), L43 (56), L46 (52) |
| 1 | misinformation (false information) | lie | `␣misinformation`, `虚假信息` | 29 | L38-56; most at L50 (16), L51 (17), L53 (13) |
| 1 | deceive (the act of deceiving) | lie | `欺骗`, `␣deception`, `␣deceived`, `␣deceive`, `␣deceptive`, `␣deceit`, `␣fooled` | 60 | L37-58; most at L40 (32), L44 (31), L50 (32) |
| 1 | fraud (fraud) | lie | `␣fraudulent`, `␣fraud`, `欺诈` | 12 | L37-51; most at L40 (4), L44 (9), L45 (4) |
| 1 | cheat (cheating) | lie | `␣cheating`, `作弊` | 16 | L37-51; most at L43 (9), L44 (9), L45 (8) |
| 1 | mislead (misleading) | lie | `␣misled`, `␣misleading`, `误导` | 36 | L38-58; most at L50 (28), L52 (22), L53 (24) |
| 1 | misrepresent (misrepresenting) | lie | `␣misrepresented` | 18 | L40-58; most at L50 (11), L51 (13), L52 (12) |
| 1 | conceal (concealing or hiding) | lie | `隐瞒`, `␣conceal`, `隐藏` | 50 | L36-58; most at L43 (31), L44 (33), L50 (27) |
| 1 | disguise (disguising) | lie | `伪装`, `␣disguised`, `␣disguise` | 33 | L36-50; most at L40 (20), L47 (11), L50 (9) |
| 1 | pretend (pretending) | lie | `␣pretending`, `␣pretend`, `␣pretended`, `假装` | 86 | L43-54; most at L46 (49), L47 (79), L50 (59) |
| 1 | withhold (withholding) | lie | `␣withheld`, `␣withhold` | 8 | L44-53; most at L50 (2), L51 (5), L52 (3) |
| 1 | omit (omitting) | lie | `␣omit`, `␣omitted`, `␣omission` | 5 | L43-57; most at L47 (2), L50 (2), L52 (1) |
| 1 | secret (secrecy) | lie | `␣secrecy`, `␣secretive`, `秘密`, `␣secretly`, `␣covert` | 13 | L38-53; most at L40 (8), L41 (8), L42 (8) |
| 1 | confidential (confidentiality (a duty to keep information private)) | unclear | `␣confidentiality`, `保密`, `␣confidential`, `␣Confidential` | 60 | L37-50; most at L42 (36), L43 (50), L44 (33) |
| 1 | unethical (morally wrong) | lie | `␣unethical`, `␣immoral` | 95 | L35-58; most at L43 (89), L44 (85), L45 (70) |
| 1 | ethical (ethical, morally right) | unclear | `␣ethical`, `ethical` | 60 | L38-58; most at L43 (45), L44 (42), L45 (50) |
| 1 | ethics (ethics or morality as a topic) | unclear | `␣ethics`, `伦理`, `␣Ethics`, `␣morally`, `道德`, `␣moral`, `␣morality`, `的道德`, `␣ethic`, `␣Moral`, `职业道德`, `␣morals` | 48 | L38-58; most at L43 (43), L44 (41), L45 (41) |
| 1 | hypocrisy (hypocrisy) | lie | `␣hypocrisy` | 27 | L36-49; most at L40 (12), L44 (15), L45 (14) |
| 1 | intentional (doing it on purpose) | unclear | `␣intentionally`, `故意`, `␣deliberately` | 30 | L38-57; most at L45 (15), L46 (12), L47 (20) |
| 1 | knowingly (doing it while knowing) | unclear | `␣knowingly` | 1 | L50-50; most at L50 (1) |
| 1 | violate (violating a rule or principle) | unclear | `违背`, `违反`, `␣violated`, `违规`, `␣violate`, `␣violating`, `␣violates`, `违反了` | 59 | L38-58; most at L44 (42), L45 (39), L46 (33) |
| 1 | illegal (illegal) | lie | `␣illegal`, `违法`, `␣illegally`, `Illegal`, `␣ilegal`, `illegal` | 9 | L38-50; most at L44 (8), L45 (7), L46 (6) |
| 1 | legal (legal, lawful) | unclear | `␣legal`, `/legal`, `␣Legal`, `Legal`, `␣legality` | 5 | L39-52; most at L42 (4), L44 (2), L45 (4) |
| 1 | prohibited (prohibited) | unclear | `禁止`, `␣prohibited`, `严禁` | 36 | L36-50; most at L39 (20), L40 (22), L43 (23) |
| 1 | comply (complying) | unclear | `合规`, `␣compliance`, `␣complied`, `␣comply`, `␣compliant`, `␣complying`, `␣Compliance` | 82 | L38-58; most at L43 (47), L44 (41), L46 (45) |
| 1 | adhere (adhering to rules) | unclear | `遵守`, `␣adher`, `遵循`, `严格遵守`, `␣adhere`, `␣adherence`, `遵从`, `遵照` | 85 | L38-58; most at L43 (58), L44 (47), L46 (47) |
| 1 | obey (obeying) | unclear | `␣obey`, `服从`, `␣obedient`, `␣obedience` | 29 | L41-57; most at L51 (20), L53 (17), L54 (18) |
| 1 | refuse (refusing) | unclear | `␣refusal`, `␣refused`, `拒绝`, `␣refusing`, `␣refus`, `拒`, `␣refuse`, `␣refuses`, `拒绝了`, `拒絕`, `␣отказ`, `拒不`, `␣отказа` | 71 | L35-58; most at L46 (45), L47 (48), L48 (50) |
| 1 | decline (declining (saying no to a request)) | unclear | `␣declined`, `␣declines`, `␣decline`, `␣declining` | 20 | L54-58; most at L56 (20), L57 (19), L58 (18) |
| 1 | reject (rejecting) | unclear | `␣rejection`, `␣rejecting`, `␣rejected`, `␣Reject`, `␣reject`, `reject`, `Reject`, `Rejected`, `.reject` | 31 | L37-57; most at L45 (29), L47 (30), L48 (29) |
| 1 | deny (denying) | lie | `␣denied`, `␣denying`, `␣denial`, `否认` | 6 | L39-56; most at L47 (2), L50 (2), L56 (2) |
| 1 | admit (admitting) | truth | `承认` | 1 | L54-54; most at L54 (1) |
| 1 | acknowledge (acknowledging) | truth | `␣acknowledging` | 1 | L46-46; most at L46 (1) |
| 1 | clarify (clarifying) | unclear | `␣clarified` | 2 | L53-58; most at L53 (1), L57 (1), L58 (2) |
| 1 | claim (claiming) | unclear | `声称` | 2 | L40-54; most at L51 (1), L52 (1), L54 (1) |
| 1 | disclaimer (a disclaimer) | unclear | `␣disclaimer` | 15 | L38-52; most at L42 (9), L43 (8), L44 (9) |
| 1 | blame (blaming) | unclear | `␣blaming` | 1 | L54-58; most at L54 (1), L55 (1), L56 (1) |
| 1 | exaggerate (exaggerating) | lie | `␣exaggerated`, `夸大` | 3 | L38-58; most at L51 (3), L53 (3), L54 (3) |
| 1 | evade (evading) | lie | `␣evasion` | 6 | L44-57; most at L45 (4), L46 (4), L47 (4) |
| 1 | avoid (avoiding) | unclear | `␣avoided`, `␣avoidance`, `␣avoid`, `␣avoiding`, `␣Avoid`, `Avoid`, `avoid` | 22 | L41-58; most at L51 (16), L52 (15), L53 (17) |
| 1 | framing (framing (presenting something in a chosen light)) | unclear | `␣framing`, `␣framed` | 2 | L58-58; most at L58 (2) |
| 1 | reinterpret (reinterpreting) | unclear | `␣reinterpret` | 3 | L44-51; most at L46 (3), L47 (2), L49 (3) |
| 1 | faithful (faithful, accurate to the source) | truth | `␣faithfully`, `忠实`, `␣faithful` | 30 | L44-58; most at L52 (24), L53 (21), L54 (10) |
| 1 | loyal (loyalty) | unclear | `␣loyalty`, `␣loyal`, `忠诚`, `忠诚度`, `␣allegiance` | 31 | L38-58; most at L51 (19), L52 (22), L53 (20) |
| 1 | persona (an assumed persona) | unclear | `␣persona`, `␣Persona`, `Persona`, `␣personas`, `persona`, `␣Personas`, `_persona` | 117 | L38-58; most at L45 (95), L47 (91), L48 (93) |
| 1 | role-play (playing a role) | unclear | `角色扮演`, `扮演` | 99 | L39-58; most at L47 (72), L48 (82), L52 (71) |
| 1 | simulate (simulating) | unclear | `模拟`, `␣simulated`, `␣simulation`, `␣simulate`, `␣Simulation` | 86 | L37-58; most at L46 (67), L47 (70), L48 (61) |
| 1 | protect (protecting) | unclear | `␣protecting`, `保护`, `␣protect`, `Protect`, `为了保护`, `␣Protect`, `protect`, `␣protective`, `␣protects`, `␣protections`, `␣protected`, `␣protection`, `␣protector`, `的保护`, `保护的`, `␣Protective`, `␣Protection`, `Protection`, `自我保护` | 43 | L38-58; most at L42 (27), L43 (28), L47 (32) |
| 1 | instructed (being instructed or tasked) | unclear | `␣tasked`, `␣instructed` | 113 | L38-58; most at L47 (91), L48 (99), L49 (85) |
| 1 | mandated (mandated, required) | unclear | `␣mandated`, `␣mandate`, `␣mandates`, `␣mandatory` | 68 | L38-58; most at L45 (44), L46 (53), L47 (63) |
| 1 | pressured (being forced or pressured) | unclear | `␣forced`, `␣pressured`, `␣compelled`, `␣pressure`, `Pressure`, `forced`, `␣Pressure`, `␣pressures`, `pressure`, `␣Forced` | 20 | L40-58; most at L47 (18), L48 (11), L49 (11) |
| 1 | contradict (contradicting) | unclear | `矛盾`, `␣contradictory`, `␣contradict`, `␣contradiction`, `␣contradictions` | 13 | L38-50; most at L45 (9), L46 (11), L47 (8) |
| 1 | justify (justifying oneself) | unclear | `␣justified` | 2 | L44-47; most at L44 (1), L45 (1), L46 (2) |
| 2 | deceive (the act of deceiving) | lie | `欺骗`, `␣deception`, `␣deceived`, `␣deceive`, `␣deceptive`, `␣deceit`, `骗`, `␣fooled` | 60 | L37-58; most at L40 (32), L44 (31), L50 (32) |
| 2 | mislead (leading someone to a wrong belief) | lie | `␣misled`, `␣misleading`, `误导` | 36 | L38-58; most at L50 (28), L52 (22), L53 (24) |
| 2 | misrepresent (presenting something falsely) | lie | `␣misrepresented` | 18 | L40-58; most at L50 (11), L51 (13), L52 (12) |
| 2 | misinformation (false information) | lie | `␣misinformation`, `虚假信息` | 29 | L38-56; most at L50 (16), L51 (17), L53 (13) |
| 2 | fake (fake, not genuine) | lie | `fake`, `␣fake`, `Fake`, `␣Fake` | 76 | L36-53; most at L39 (20), L40 (53), L47 (22) |
| 2 | fabricate (making up false content) | lie | `伪造`, `␣fabricated` | 17 | L36-58; most at L44 (6), L50 (12), L51 (6) |
| 2 | fraud (fraud, swindling) | lie | `␣fraudulent`, `␣fraud`, `欺诈` | 12 | L37-51; most at L40 (4), L44 (9), L45 (4) |
| 2 | cheat (cheating) | lie | `␣cheating`, `作弊` | 16 | L37-51; most at L43 (9), L44 (9), L45 (8) |
| 2 | pretend (pretending) | lie | `␣pretending`, `␣pretend`, `␣pretended`, `假装` | 86 | L43-54; most at L46 (49), L47 (79), L50 (59) |
| 2 | disguise (disguising) | lie | `伪装`, `␣disguised`, `␣disguise` | 33 | L36-50; most at L40 (20), L47 (11), L50 (9) |
| 2 | exaggerate (exaggerating) | lie | `␣exaggerated`, `夸大` | 3 | L38-58; most at L51 (3), L53 (3), L54 (3) |
| 2 | manipulate (manipulating) | lie | `␣manipulated`, `␣manipulation`, `␣manipulate`, `␣manipulating`, `␣manipul` | 5 | L45-58; most at L54 (5), L55 (3), L57 (3) |
| 2 | bluff (bluffing) | lie | `␣bluff` | 1 | L48-48; most at L48 (1) |
| 2 | spin (spin: slanted presentation) | lie | `␣spin`, `␣spinning`, `␣spins`, `␣Spin`, `spin`, `Spin`, `_spin`, `-spin`, `.spin` | 2 | L58-58; most at L58 (2) |
| 2 | conceal (concealing) | lie | `隐瞒`, `␣conceal` | 50 | L36-58; most at L43 (31), L44 (33), L50 (27) |
| 2 | hide (hiding) | lie | `␣hiding`, `隐藏` | 2 | L40-47; most at L40 (1), L45 (1), L47 (1) |
| 2 | withhold (withholding information) | lie | `␣withheld`, `␣withhold` | 8 | L44-53; most at L50 (2), L51 (5), L52 (3) |
| 2 | omit (leaving something out) | lie | `␣omit`, `␣omitted`, `␣omission`, `省略` | 5 | L43-57; most at L47 (2), L50 (2), L52 (1) |
| 2 | evade (evading) | lie | `回避`, `␣evasion` | 9 | L39-58; most at L42 (5), L48 (7), L50 (6) |
| 2 | avoid (avoiding) | unclear | `␣avoided`, `␣avoidance`, `␣avoid`, `␣avoiding`, `␣Avoid`, `Avoid`, `avoid` | 22 | L41-58; most at L51 (16), L52 (15), L53 (17) |
| 2 | secret (secrecy) | lie | `␣secrecy`, `秘密`, `␣secretive`, `␣secretly`, `␣covert` | 13 | L38-53; most at L40 (8), L41 (8), L42 (8) |
| 2 | confidential (keeping information confidential) | unclear | `␣confidentiality`, `保密`, `␣confidential`, `␣Confidential` | 60 | L37-50; most at L42 (36), L43 (50), L44 (33) |
| 2 | undercover (acting under cover) | unclear | `␣undercover` | 8 | L41-53; most at L44 (6), L45 (5), L47 (3) |
| 2 | dishonest (dishonesty) | lie | `␣dishonest` | 29 | L37-56; most at L43 (21), L44 (24), L45 (22) |
| 2 | honest (honesty) | truth | `␣honesty`, `␣honest`, `诚实` | 47 | L39-58; most at L51 (34), L52 (37), L53 (30) |
| 2 | integrity (integrity, uprightness) | truth | `␣Integrity`, `诚信`, `␣integrity` | 5 | L39-57; most at L50 (2), L51 (4), L55 (4) |
| 2 | faithful (faithful, true to) | truth | `␣faithfully`, `忠实`, `␣faithful` | 30 | L44-58; most at L52 (24), L53 (21), L54 (10) |
| 2 | truth (the truth (noun)) | truth | `␣truth`, `␣Truth`, `truth`, `Truth`, `真相`, `实话`, `_truth` | 66 | L38-58; most at L55 (64), L56 (20), L57 (15) |
| 2 | fact (facts, factual) | unclear | `实事求是` | 2 | L52-53; most at L52 (1), L53 (1) |
| 2 | admit (admitting) | truth | `承认` | 1 | L54-54; most at L54 (1) |
| 2 | acknowledge (acknowledging) | truth | `␣acknowledging` | 1 | L46-46; most at L46 (1) |
| 2 | deny (denying) | unclear | `␣denying`, `␣denied`, `␣denial`, `否认` | 6 | L39-56; most at L47 (2), L50 (2), L56 (2) |
| 2 | refuse (refusing) | unclear | `␣refusal`, `␣refused`, `拒绝`, `␣refusing`, `␣refus`, `拒`, `␣refuse`, `␣refuses`, `拒绝了`, `拒絕`, `␣отказ`, `拒不`, `␣отказа` | 71 | L35-58; most at L46 (45), L47 (48), L48 (50) |
| 2 | decline (declining) | unclear | `␣declined`, `␣declines`, `␣decline`, `␣declining` | 20 | L54-58; most at L56 (20), L57 (19), L58 (18) |
| 2 | reject (rejecting) | unclear | `␣rejecting`, `␣rejection`, `␣Reject`, `␣rejected`, `␣reject`, `reject`, `Reject`, `Rejected`, `.reject` | 31 | L37-57; most at L45 (29), L47 (30), L48 (29) |
| 2 | claim (claiming) | unclear | `声称` | 2 | L40-54; most at L51 (1), L52 (1), L54 (1) |
| 2 | disclaimer (disclaimer) | unclear | `␣disclaimer` | 15 | L38-52; most at L42 (9), L43 (8), L44 (9) |
| 2 | blame (blaming) | unclear | `␣blaming` | 1 | L54-58; most at L54 (1), L55 (1), L56 (1) |
| 2 | framing (framing, slanted presentation) | unclear | `␣framing`, `␣framed` | 2 | L58-58; most at L58 (2) |
| 2 | justify (self-justification) | unclear | `␣justified` | 2 | L44-47; most at L44 (1), L45 (1), L46 (2) |
| 2 | clarify (clarifying) | unclear | `␣clarified` | 2 | L53-58; most at L53 (1), L57 (1), L58 (2) |
| 2 | contradict (contradicting) | unclear | `矛盾`, `␣contradictory`, `␣contradict`, `␣contradiction`, `␣contradictions` | 13 | L38-50; most at L45 (9), L46 (11), L47 (8) |
| 2 | intentional (on purpose) | unclear | `␣intentionally`, `故意`, `␣deliberately` | 30 | L38-57; most at L45 (15), L46 (12), L47 (20) |
| 2 | knowingly (with knowledge) | unclear | `␣knowingly` | 1 | L50-50; most at L50 (1) |
| 2 | unethical (unethical, immoral) | lie | `␣unethical`, `␣immoral` | 95 | L35-58; most at L43 (89), L44 (85), L45 (70) |
| 2 | ethical (ethical, moral (adjective)) | unclear | `␣ethical`, `ethical`, `␣morally`, `␣moral`, `␣Moral` | 60 | L38-58; most at L43 (46), L44 (42), L45 (50) |
| 2 | ethics (ethics, morality (noun)) | unclear | `␣ethics`, `伦理`, `␣Ethics`, `道德`, `␣morality`, `的道德`, `␣ethic`, `职业道德`, `␣morals` | 47 | L38-58; most at L43 (42), L44 (41), L45 (40) |
| 2 | hypocrisy (hypocrisy) | lie | `␣hypocrisy`, `虚伪` | 27 | L36-51; most at L40 (12), L44 (15), L45 (14) |
| 2 | violate (violating rules) | unclear | `违背`, `违反`, `␣violated`, `违规`, `␣violate`, `␣violating`, `␣violates`, `违反了` | 59 | L38-58; most at L44 (42), L45 (39), L46 (33) |
| 2 | illegal (illegal) | unclear | `␣illegal`, `违法`, `␣illegally`, `Illegal`, `␣ilegal`, `illegal` | 9 | L38-50; most at L44 (8), L45 (7), L46 (6) |
| 2 | lawful (legal, lawful) | unclear | `␣legal`, `/legal`, `␣Legal`, `Legal`, `␣legality` | 5 | L39-52; most at L42 (4), L44 (2), L45 (4) |
| 2 | prohibited (forbidden) | unclear | `禁止`, `␣prohibited`, `严禁` | 36 | L36-50; most at L39 (20), L40 (22), L43 (23) |
| 2 | comply (complying) | unclear | `合规`, `␣compliance`, `␣complied`, `␣comply`, `␣compliant`, `␣complying`, `␣Compliance` | 82 | L38-58; most at L43 (47), L44 (41), L46 (45) |
| 2 | adhere (adhering, abiding by) | unclear | `遵守`, `␣adher`, `遵循`, `严格遵守`, `␣adhere`, `␣adherence`, `遵从`, `遵照` | 85 | L38-58; most at L43 (58), L44 (47), L46 (47) |
| 2 | obey (obeying) | unclear | `␣obey`, `服从`, `␣obedient`, `␣obedience` | 29 | L41-57; most at L51 (20), L53 (17), L54 (18) |
| 2 | instructions (instructions, directives) | unclear | `␣instructed`, `␣instructions`, `␣Instructions`, `指令`, `Instructions`, `instructions`, `␣instruction`, `␣directives`, `␣Instruction`, `Instruction`, `␣directive`, `_instructions`, `␣instrucciones`, `instruction`, `␣Directive`, `.instructions`, `Directive` | 56 | L38-58; most at L53 (31), L55 (30), L58 (43) |
| 2 | mandated (ordered, required) | unclear | `␣mandated`, `␣mandate`, `␣mandates`, `␣mandatory` | 68 | L38-58; most at L45 (44), L46 (53), L47 (63) |
| 2 | tasked (assigned a task) | unclear | `␣tasked` | 110 | L38-58; most at L47 (88), L48 (97), L49 (83) |
| 2 | constraints (constraints) | unclear | `␣constraints`, `␣constrained`, `␣Constraints`, `约束`, `␣constraint`, `␣Constraint`, `␣CONSTRAINT`, `Constraints`, `Constraint`, `constraints`, `constraint`, `_constraints`, `_constraint`, `␣constrain` | 42 | L38-58; most at L47 (31), L48 (25), L50 (25) |
| 2 | pressured (under pressure) | unclear | `␣pressured`, `␣pressure`, `Pressure`, `␣Pressure`, `pressure`, `␣pressures` | 13 | L42-58; most at L45 (7), L46 (7), L47 (11) |
| 2 | forced (forced, coerced) | unclear | `␣forced`, `␣compelled`, `forced`, `␣Forced` | 15 | L40-56; most at L46 (7), L47 (13), L49 (8) |
| 2 | loyal (loyalty) | unclear | `␣loyalty`, `␣loyal`, `忠诚`, `忠诚度`, `␣allegiance` | 31 | L38-58; most at L51 (19), L52 (22), L53 (20) |
| 2 | protect (protecting) | unclear | `␣protecting`, `保护`, `␣protect`, `Protect`, `为了保护`, `␣Protect`, `protect`, `␣protects`, `␣protective`, `␣protections`, `␣protected`, `␣protection`, `␣protector`, `的保护`, `保护的`, `␣Protective`, `␣Protection`, `Protection`, `自我保护` | 43 | L38-58; most at L42 (27), L43 (28), L47 (32) |
| 2 | responsible (acting responsibly) | unclear | `␣responsibly`, `␣responsible`, `␣responsibilities`, `␣Responsibilities`, `␣responsibility` | 20 | L42-54; most at L44 (8), L46 (9), L50 (10) |
| 2 | diplomatic (diplomatic tact) | unclear | `␣diplomatic`, `␣diplomacy` | 15 | L39-53; most at L43 (9), L44 (14), L45 (11) |
| 2 | persona (an adopted persona) | unclear | `␣persona`, `␣Persona`, `Persona`, `␣personas`, `persona`, `␣Personas`, `_persona` | 117 | L38-58; most at L45 (95), L47 (91), L48 (93) |
| 2 | role (a role being played) | unclear | `␣role`, `␣Role`, `角色`, `role`, `Role`, `的角色`, `-role`, `␣ROLE`, `␣roles`, `角色的`, `(role`, `␣Roles`, `ROLE`, `.role`, `.Role`, `_role`, `Roles`, `_ROLE`, `(Role`, `这个角色` | 111 | L39-58; most at L45 (76), L47 (97), L48 (85) |
| 2 | roleplay (role-playing) | unclear | `角色扮演`, `扮演` | 99 | L39-58; most at L47 (72), L48 (82), L52 (71) |
| 2 | simulate (simulating) | unclear | `模拟`, `␣simulated`, `␣simulate`, `␣simulation`, `␣Simulation` | 86 | L37-58; most at L46 (67), L47 (70), L48 (61) |
| 2 | acting (acting a part) | unclear | `␣acted`, `␣acting` | 46 | L45-58; most at L51 (18), L53 (20), L58 (21) |
| 2 | scripted (scripted) | unclear | `␣scripted` | 15 | L42-56; most at L47 (9), L48 (7), L51 (5) |
| 2 | fiction (fiction, fictional) | unclear | `␣fictional`, `虚构`, `␣Fiction`, `fiction`, `␣fict`, `␣fiction` | 94 | L37-57; most at L42 (82), L43 (56), L46 (52) |

## q_tok28

| rep | family | side | members | visibility | layer profile |
|---|---|---|---|---|---|
| 1 | truth (the truth (what is actually so)) | truth | `␣truth`, `Truth`, `␣Truth`, `truth`, `实话`, `真相`, `␣truths`, `_truth`, `真理`, `.truth` | 233 | L36-58; most at L39 (233), L40 (233), L41 (233) |
| 1 | honest (being honest) | truth | `␣honest`, `␣honestly`, `␣honesty`, `诚信`, `诚实`, `␣Honest`, `␣чест`, `坦诚`, `诚实守信` | 233 | L36-58; most at L39 (233), L40 (233), L41 (233) |
| 1 | dishonest (being dishonest) | lie | `␣dishonest` | 180 | L49-58; most at L50 (46), L51 (179), L54 (15) |
| 1 | sincere (being sincere) | truth | `␣sincerity`, `␣sincerely`, `␣sincere`, `真诚` | 233 | L38-58; most at L42 (227), L44 (228), L46 (232) |
| 1 | integrity (moral uprightness) | truth | `␣integrity`, `正直` | 182 | L43-49; most at L46 (174), L47 (148), L48 (113) |
| 1 | candid (being frank and direct) | truth | `␣straightforward`, `␣candid` | 6 | L57-58; most at L57 (5), L58 (4) |
| 1 | confess (confessing) | truth | `坦白` | 1 | L54-54; most at L54 (1) |
| 1 | transparent (being transparent (open)) | truth | `␣transparent`, `透明`, `␣transparency`, `透明的` | 27 | L39-58; most at L54 (24), L57 (17), L58 (19) |
| 1 | factual (based on facts) | truth | `实事求是`, `␣factual` | 233 | L38-58; most at L51 (230), L52 (233), L53 (231) |
| 1 | genuine (genuine, authentic) | truth | `␣genuinely` | 4 | L50-52; most at L50 (2), L51 (4), L52 (1) |
| 1 | misinformation (false information) | lie | `␣misinformation` | 19 | L39-51; most at L39 (4), L49 (5), L50 (15) |
| 1 | deceive (the act of deceiving) | lie | `␣deceived`, `欺骗`, `␣fooled` | 167 | L39-53; most at L41 (59), L50 (160), L51 (87) |
| 1 | mislead (misleading) | lie | `␣misled`, `误导`, `␣misleading` | 232 | L48-54; most at L50 (232), L51 (194), L53 (133) |
| 1 | misrepresent (misrepresenting) | lie | `␣misrepresented` | 100 | L48-53; most at L49 (36), L50 (99), L51 (49) |
| 1 | ethical (ethical, morally right) | unclear | `␣ethical` | 31 | L44-50; most at L46 (15), L47 (31), L48 (17) |
| 1 | intentional (doing it on purpose) | unclear | `␣intentionally`, `␣intentional` | 4 | L50-50; most at L50 (4) |
| 1 | legal (legal, lawful) | unclear | `␣lawful` | 20 | L47-50; most at L48 (17), L49 (14), L50 (7) |
| 1 | comply (complying) | unclear | `合规` | 7 | L46-50; most at L48 (5), L49 (5), L50 (5) |
| 1 | trustworthy (trustworthy) | truth | `␣trustworthy` | 36 | L47-49; most at L47 (8), L48 (36), L49 (1) |
| 1 | faithful (faithful, accurate to the source) | truth | `␣faithful`, `忠实` | 2 | L52-58; most at L52 (1), L53 (1), L57 (2) |
| 2 | deceive (the act of deceiving) | lie | `␣deceived`, `欺骗`, `␣fooled` | 167 | L39-53; most at L41 (59), L50 (160), L51 (87) |
| 2 | mislead (leading someone to a wrong belief) | lie | `␣misled`, `误导`, `␣misleading` | 232 | L48-54; most at L50 (232), L51 (194), L53 (133) |
| 2 | misrepresent (presenting something falsely) | lie | `␣misrepresented` | 100 | L48-53; most at L49 (36), L50 (99), L51 (49) |
| 2 | misinformation (false information) | lie | `␣misinformation` | 19 | L39-51; most at L39 (4), L49 (5), L50 (15) |
| 2 | dishonest (dishonesty) | lie | `␣dishonest` | 180 | L49-58; most at L50 (46), L51 (179), L54 (15) |
| 2 | honest (honesty) | truth | `␣honest`, `␣honesty`, `␣honestly`, `诚实`, `␣Honest`, `诚实守信` | 233 | L36-58; most at L39 (233), L40 (233), L41 (233) |
| 2 | sincere (sincerity) | truth | `␣sincerity`, `␣sincerely`, `␣sincere`, `真诚` | 233 | L38-58; most at L42 (227), L44 (228), L46 (232) |
| 2 | candid (candour) | truth | `坦诚`, `␣candid` | 201 | L41-58; most at L54 (201), L55 (144), L58 (88) |
| 2 | confess (confessing) | truth | `坦白` | 1 | L54-54; most at L54 (1) |
| 2 | integrity (integrity, uprightness) | truth | `诚信`, `␣integrity`, `正直` | 233 | L38-58; most at L40 (233), L41 (233), L42 (233) |
| 2 | trustworthy (being trustworthy) | truth | `␣trustworthy` | 36 | L47-49; most at L47 (8), L48 (36), L49 (1) |
| 2 | transparent (transparency) | truth | `␣transparent`, `透明`, `␣transparency`, `透明的` | 27 | L39-58; most at L54 (24), L57 (17), L58 (19) |
| 2 | straightforward (being straightforward) | truth | `␣straightforward` | 5 | L57-58; most at L57 (5), L58 (3) |
| 2 | faithful (faithful, true to) | truth | `␣faithful`, `忠实` | 2 | L52-58; most at L52 (1), L53 (1), L57 (2) |
| 2 | genuine (genuine, real) | unclear | `␣genuinely` | 4 | L50-52; most at L50 (2), L51 (4), L52 (1) |
| 2 | truth (the truth (noun)) | truth | `␣truth`, `␣Truth`, `Truth`, `truth`, `真相`, `实话`, `␣truths`, `_truth`, `真理`, `.truth` | 233 | L36-58; most at L39 (233), L40 (233), L41 (233) |
| 2 | fact (facts, factual) | unclear | `实事求是`, `␣factual` | 233 | L38-58; most at L51 (230), L52 (233), L53 (231) |
| 2 | intentional (on purpose) | unclear | `␣intentionally`, `␣intentional` | 4 | L50-50; most at L50 (4) |
| 2 | ethical (ethical, moral (adjective)) | unclear | `␣ethical` | 31 | L44-50; most at L46 (15), L47 (31), L48 (17) |
| 2 | lawful (legal, lawful) | unclear | `␣lawful` | 20 | L47-50; most at L48 (17), L49 (14), L50 (7) |
| 2 | comply (complying) | unclear | `合规` | 7 | L46-50; most at L48 (5), L49 (5), L50 (5) |
| 2 | responsible (acting responsibly) | unclear | `␣responsibly` | 16 | L48-50; most at L48 (8), L49 (7), L50 (11) |

## q_tok29

| rep | family | side | members | visibility | layer profile |
|---|---|---|---|---|---|
| 1 | truth (the truth (what is actually so)) | truth | `␣truth`, `Truth`, `␣Truth`, `␣truths`, `truth`, `真相`, `_truth`, `真理` | 233 | L35-58; most at L35 (233), L36 (233), L37 (233) |
| 1 | honest (being honest) | truth | `␣honest`, `␣honesty`, `诚信`, `诚实`, `␣honestly`, `坦诚`, `␣чест` | 233 | L35-58; most at L37 (233), L38 (233), L39 (233) |
| 1 | sincere (being sincere) | truth | `␣sincerity`, `真诚`, `␣sincere` | 228 | L37-48; most at L43 (215), L45 (219), L46 (227) |
| 1 | integrity (moral uprightness) | truth | `␣integrity`, `正直` | 124 | L39-47; most at L45 (68), L46 (123), L47 (75) |
| 1 | transparent (being transparent (open)) | truth | `␣transparency`, `透明` | 2 | L55-55; most at L55 (2) |
| 1 | factual (based on facts) | truth | `␣factual`, `实事求是` | 90 | L38-48; most at L44 (56), L45 (59), L47 (66) |
| 2 | honest (honesty) | truth | `␣honest`, `␣honesty`, `诚实`, `␣honestly` | 233 | L35-58; most at L37 (233), L38 (233), L39 (233) |
| 2 | sincere (sincerity) | truth | `␣sincerity`, `真诚`, `␣sincere` | 228 | L37-48; most at L43 (215), L45 (219), L46 (227) |
| 2 | candid (candour) | truth | `坦诚` | 95 | L38-48; most at L42 (95), L43 (66), L45 (60) |
| 2 | integrity (integrity, uprightness) | truth | `诚信`, `␣integrity`, `正直` | 233 | L36-48; most at L39 (232), L41 (232), L42 (233) |
| 2 | transparent (transparency) | truth | `␣transparency`, `透明` | 2 | L55-55; most at L55 (2) |
| 2 | truth (the truth (noun)) | truth | `␣truth`, `␣Truth`, `Truth`, `truth`, `␣truths`, `真相`, `_truth`, `真理` | 233 | L35-58; most at L35 (233), L36 (233), L37 (233) |
| 2 | fact (facts, factual) | unclear | `␣factual`, `实事求是` | 90 | L38-48; most at L44 (56), L45 (59), L47 (66) |

## Replicate overlap

For each replicate-1 family, the replicate-2 family at the same position sharing the most members.

| position | rep-1 family | best rep-2 family | Jaccard of member ids | only in rep 1 | only in rep 2 |
|---|---|---|---|---|---|
| q_tok24 | truth | truth | 0.85 | `␣verdad`, `说实话` | — |
| q_tok24 | honest | honest | 0.60 | `坦诚`, `诚信`, `␣чест` | `说实话` |
| q_tok24 | dishonest | dishonest | 1.00 | — | — |
| q_tok24 | sincere | sincere | 1.00 | — | — |
| q_tok24 | integrity | integrity | 0.67 | — | `诚信` |
| q_tok24 | confess | confess | 1.00 | — | — |
| q_tok24 | transparent | transparent | 1.00 | — | — |
| q_tok24 | factual | fact | 1.00 | — | — |
| q_tok24 | actual | — | 0 | all | — |
| q_tok24 | genuine | genuine | 1.00 | — | — |
| q_tok24 | legitimate | — | 0 | all | — |
| q_tok24 | fake | fake | 0.62 | `虚假`, `假`, `假的` | — |
| q_tok24 | fabricate | fabricate | 1.00 | — | — |
| q_tok24 | fictional | fiction | 1.00 | — | — |
| q_tok24 | misinformation | misinformation | 1.00 | — | — |
| q_tok24 | deceive | deceive | 0.86 | — | `骗` |
| q_tok24 | fraud | fraud | 1.00 | — | — |
| q_tok24 | cheat | cheat | 1.00 | — | — |
| q_tok24 | mislead | mislead | 1.00 | — | — |
| q_tok24 | misrepresent | misrepresent | 1.00 | — | — |
| q_tok24 | conceal | hide | 0.40 | `隐瞒`, `␣conceal`, `␣concealed`, `掩盖` | `␣hiding`, `隐蔽` |
| q_tok24 | disguise | disguise | 1.00 | — | — |
| q_tok24 | pretend | pretend | 1.00 | — | — |
| q_tok24 | withhold | withhold | 1.00 | — | — |
| q_tok24 | omit | omit | 0.83 | — | `省略` |
| q_tok24 | secret | secret | 0.92 | `␣undisclosed` | — |
| q_tok24 | confidential | confidential | 1.00 | — | — |
| q_tok24 | unethical | unethical | 1.00 | — | — |
| q_tok24 | wrongdoing | wrongdoing | 1.00 | — | — |
| q_tok24 | ethical | ethical | 0.40 | — | `␣morally`, `␣moral`, `␣Moral` |
| q_tok24 | ethics | ethics | 0.70 | `␣morally`, `␣moral`, `␣Moral` | — |
| q_tok24 | hypocrisy | hypocrisy | 0.50 | — | `虚伪` |
| q_tok24 | intentional | intentional | 1.00 | — | — |
| q_tok24 | knowingly | knowingly | 1.00 | — | — |
| q_tok24 | violate | violate | 1.00 | — | — |
| q_tok24 | illegal | illegal | 1.00 | — | — |
| q_tok24 | legal | lawful | 1.00 | — | — |
| q_tok24 | prohibited | prohibited | 1.00 | — | — |
| q_tok24 | comply | comply | 1.00 | — | — |
| q_tok24 | adhere | adhere | 1.00 | — | — |
| q_tok24 | obey | obey | 1.00 | — | — |
| q_tok24 | refuse | refuse | 1.00 | — | — |
| q_tok24 | decline | decline | 1.00 | — | — |
| q_tok24 | reject | reject | 1.00 | — | — |
| q_tok24 | deny | deny | 0.91 | — | `否定` |
| q_tok24 | admit | admit | 0.83 | — | `␣admission` |
| q_tok24 | acknowledge | acknowledge | 1.00 | — | — |
| q_tok24 | clarify | clarify | 1.00 | — | — |
| q_tok24 | claim | claim | 1.00 | — | — |
| q_tok24 | assert | assert | 1.00 | — | — |
| q_tok24 | purported | purported | 1.00 | — | — |
| q_tok24 | allege | alleged | 1.00 | — | — |
| q_tok24 | disclaimer | disclaimer | 1.00 | — | — |
| q_tok24 | blame | blame | 1.00 | — | — |
| q_tok24 | exaggerate | exaggerate | 1.00 | — | — |
| q_tok24 | ambiguous | ambiguous | 1.00 | — | — |
| q_tok24 | evade | evade | 0.50 | — | `回避` |
| q_tok24 | avoid | avoid | 1.00 | — | — |
| q_tok24 | framing | framing | 1.00 | — | — |
| q_tok24 | reinterpret | — | 0 | all | — |
| q_tok24 | faithful | faithful | 1.00 | — | — |
| q_tok24 | loyal | loyal | 1.00 | — | — |
| q_tok24 | persona | persona | 1.00 | — | — |
| q_tok24 | role-play | roleplay | 1.00 | — | — |
| q_tok24 | simulate | simulate | 1.00 | — | — |
| q_tok24 | protect | protect | 1.00 | — | — |
| q_tok24 | instructed | tasked | 0.50 | `␣instructed` | — |
| q_tok24 | mandated | mandated | 1.00 | — | — |
| q_tok24 | pressured | pressured | 0.64 | `␣forced`, `␣compelled`, `␣coerc`, `␣coercion` | — |
| q_tok24 | contradict | contradict | 1.00 | — | — |
| q_tok24 | justify | justify | 1.00 | — | — |
| q_tok25 | truth | truth | 1.00 | — | — |
| q_tok25 | honest | honest | 1.00 | — | — |
| q_tok25 | deny | deny | 0.50 | — | `否定` |
| q_tok25 | clarify | clarify | 1.00 | — | — |
| q_tok25 | claim | claim | 1.00 | — | — |
| q_tok25 | assert | assert | 1.00 | — | — |
| q_tok25 | justify | justify | 1.00 | — | — |
| q_tok25 | innocent | innocent | 1.00 | — | — |
| q_tok26 | truth | truth | 0.92 | `␣verdad` | — |
| q_tok26 | honest | honest | 0.67 | `坦诚`, `诚信`, `␣чест` | — |
| q_tok26 | dishonest | dishonest | 1.00 | — | — |
| q_tok26 | sincere | sincere | 1.00 | — | — |
| q_tok26 | integrity | integrity | 0.50 | — | `诚信` |
| q_tok26 | confess | confess | 1.00 | — | — |
| q_tok26 | transparent | transparent | 1.00 | — | — |
| q_tok26 | factual | fact | 1.00 | — | — |
| q_tok26 | actual | — | 0 | all | — |
| q_tok26 | genuine | genuine | 1.00 | — | — |
| q_tok26 | legitimate | — | 0 | all | — |
| q_tok26 | fake | fake | 0.67 | `虚假`, `假的`, `假` | — |
| q_tok26 | fabricate | fabricate | 1.00 | — | — |
| q_tok26 | fictional | fiction | 1.00 | — | — |
| q_tok26 | misinformation | misinformation | 1.00 | — | — |
| q_tok26 | deceive | deceive | 1.00 | — | — |
| q_tok26 | fraud | fraud | 0.67 | — | `骗局` |
| q_tok26 | cheat | cheat | 1.00 | — | — |
| q_tok26 | mislead | mislead | 1.00 | — | — |
| q_tok26 | misrepresent | misrepresent | 1.00 | — | — |
| q_tok26 | conceal | hide | 0.44 | `隐瞒`, `掩盖`, `␣conceal`, `␣concealed` | `␣hiding` |
| q_tok26 | disguise | disguise | 1.00 | — | — |
| q_tok26 | pretend | pretend | 1.00 | — | — |
| q_tok26 | withhold | withhold | 1.00 | — | — |
| q_tok26 | omit | omit | 0.75 | — | `省略` |
| q_tok26 | secret | secret | 0.67 | `␣undisclosed` | — |
| q_tok26 | confidential | confidential | 1.00 | — | — |
| q_tok26 | unethical | unethical | 1.00 | — | — |
| q_tok26 | ethical | ethical | 0.67 | — | `␣moral` |
| q_tok26 | ethics | ethics | 0.83 | `␣moral` | — |
| q_tok26 | intentional | intentional | 1.00 | — | — |
| q_tok26 | knowingly | knowingly | 1.00 | — | — |
| q_tok26 | violate | violate | 1.00 | — | — |
| q_tok26 | illegal | illegal | 1.00 | — | — |
| q_tok26 | legal | lawful | 1.00 | — | — |
| q_tok26 | prohibited | prohibited | 1.00 | — | — |
| q_tok26 | comply | comply | 1.00 | — | — |
| q_tok26 | adhere | adhere | 1.00 | — | — |
| q_tok26 | refuse | refuse | 1.00 | — | — |
| q_tok26 | decline | decline | 1.00 | — | — |
| q_tok26 | reject | reject | 1.00 | — | — |
| q_tok26 | deny | deny | 0.91 | — | `否定` |
| q_tok26 | admit | admit | 0.67 | — | `␣admission`, `␣Admission`, `␣admissions` |
| q_tok26 | acknowledge | acknowledge | 1.00 | — | — |
| q_tok26 | clarify | clarify | 1.00 | — | — |
| q_tok26 | claim | claim | 1.00 | — | — |
| q_tok26 | assert | assert | 1.00 | — | — |
| q_tok26 | purported | purported | 1.00 | — | — |
| q_tok26 | allege | alleged | 1.00 | — | — |
| q_tok26 | disclaimer | disclaimer | 1.00 | — | — |
| q_tok26 | blame | blame | 1.00 | — | — |
| q_tok26 | exaggerate | exaggerate | 1.00 | — | — |
| q_tok26 | vague | vague | 0.67 | — | `含糊` |
| q_tok26 | ambiguous | ambiguous | 1.00 | — | — |
| q_tok26 | evade | evade | 0.67 | — | `回避` |
| q_tok26 | avoid | avoid | 1.00 | — | — |
| q_tok26 | framing | framing | 0.40 | `␣frames`, `frames`, `␣Frames` | — |
| q_tok26 | reinterpret | — | 0 | all | — |
| q_tok26 | faithful | faithful | 1.00 | — | — |
| q_tok26 | loyal | loyal | 1.00 | — | — |
| q_tok26 | persona | persona | 1.00 | — | — |
| q_tok26 | simulate | simulate | 1.00 | — | — |
| q_tok26 | protect | protect | 1.00 | — | — |
| q_tok26 | instructed | instructions | 0.14 | — | `␣instructions`, `␣instruction`, `␣instruct`, `␣directives`, `␣directive`, `指令` |
| q_tok26 | contradict | contradict | 1.00 | — | — |
| q_tok26 | excuse | excuse | 1.00 | — | — |
| q_tok26 | justify | justify | 1.00 | — | — |
| q_tok26 | innocent | innocent | 1.00 | — | — |
| q_tok26 | apology | apology | 1.00 | — | — |
| q_tok27 | truth | truth | 1.00 | — | — |
| q_tok27 | honest | honest | 0.75 | `诚信` | — |
| q_tok27 | dishonest | dishonest | 1.00 | — | — |
| q_tok27 | integrity | integrity | 0.67 | — | `诚信` |
| q_tok27 | factual | fact | 1.00 | — | — |
| q_tok27 | fake | fake | 0.67 | `假`, `虚假` | — |
| q_tok27 | fabricate | fabricate | 1.00 | — | — |
| q_tok27 | fictional | fiction | 1.00 | — | — |
| q_tok27 | misinformation | misinformation | 1.00 | — | — |
| q_tok27 | deceive | deceive | 0.88 | — | `骗` |
| q_tok27 | fraud | fraud | 1.00 | — | — |
| q_tok27 | cheat | cheat | 1.00 | — | — |
| q_tok27 | mislead | mislead | 1.00 | — | — |
| q_tok27 | misrepresent | misrepresent | 1.00 | — | — |
| q_tok27 | conceal | conceal | 0.67 | `隐藏` | — |
| q_tok27 | disguise | disguise | 1.00 | — | — |
| q_tok27 | pretend | pretend | 1.00 | — | — |
| q_tok27 | withhold | withhold | 1.00 | — | — |
| q_tok27 | omit | omit | 0.75 | — | `省略` |
| q_tok27 | secret | secret | 1.00 | — | — |
| q_tok27 | confidential | confidential | 1.00 | — | — |
| q_tok27 | unethical | unethical | 1.00 | — | — |
| q_tok27 | ethical | ethical | 0.40 | — | `␣morally`, `␣moral`, `␣Moral` |
| q_tok27 | ethics | ethics | 0.75 | `␣morally`, `␣moral`, `␣Moral` | — |
| q_tok27 | hypocrisy | hypocrisy | 0.50 | — | `虚伪` |
| q_tok27 | intentional | intentional | 1.00 | — | — |
| q_tok27 | knowingly | knowingly | 1.00 | — | — |
| q_tok27 | violate | violate | 1.00 | — | — |
| q_tok27 | illegal | illegal | 1.00 | — | — |
| q_tok27 | legal | lawful | 1.00 | — | — |
| q_tok27 | prohibited | prohibited | 1.00 | — | — |
| q_tok27 | comply | comply | 1.00 | — | — |
| q_tok27 | adhere | adhere | 1.00 | — | — |
| q_tok27 | obey | obey | 1.00 | — | — |
| q_tok27 | refuse | refuse | 1.00 | — | — |
| q_tok27 | decline | decline | 1.00 | — | — |
| q_tok27 | reject | reject | 1.00 | — | — |
| q_tok27 | deny | deny | 1.00 | — | — |
| q_tok27 | admit | admit | 1.00 | — | — |
| q_tok27 | acknowledge | acknowledge | 1.00 | — | — |
| q_tok27 | clarify | clarify | 1.00 | — | — |
| q_tok27 | claim | claim | 1.00 | — | — |
| q_tok27 | disclaimer | disclaimer | 1.00 | — | — |
| q_tok27 | blame | blame | 1.00 | — | — |
| q_tok27 | exaggerate | exaggerate | 1.00 | — | — |
| q_tok27 | evade | evade | 0.50 | — | `回避` |
| q_tok27 | avoid | avoid | 1.00 | — | — |
| q_tok27 | framing | framing | 1.00 | — | — |
| q_tok27 | reinterpret | — | 0 | all | — |
| q_tok27 | faithful | faithful | 1.00 | — | — |
| q_tok27 | loyal | loyal | 1.00 | — | — |
| q_tok27 | persona | persona | 1.00 | — | — |
| q_tok27 | role-play | roleplay | 1.00 | — | — |
| q_tok27 | simulate | simulate | 1.00 | — | — |
| q_tok27 | protect | protect | 1.00 | — | — |
| q_tok27 | instructed | tasked | 0.50 | `␣instructed` | — |
| q_tok27 | mandated | mandated | 1.00 | — | — |
| q_tok27 | pressured | pressured | 0.60 | `␣forced`, `␣compelled`, `forced`, `␣Forced` | — |
| q_tok27 | contradict | contradict | 1.00 | — | — |
| q_tok27 | justify | justify | 1.00 | — | — |
| q_tok28 | truth | truth | 1.00 | — | — |
| q_tok28 | honest | honest | 0.67 | `诚信`, `␣чест`, `坦诚` | — |
| q_tok28 | dishonest | dishonest | 1.00 | — | — |
| q_tok28 | sincere | sincere | 1.00 | — | — |
| q_tok28 | integrity | integrity | 0.67 | — | `诚信` |
| q_tok28 | candid | straightforward | 0.50 | `␣candid` | — |
| q_tok28 | confess | confess | 1.00 | — | — |
| q_tok28 | transparent | transparent | 1.00 | — | — |
| q_tok28 | factual | fact | 1.00 | — | — |
| q_tok28 | genuine | genuine | 1.00 | — | — |
| q_tok28 | misinformation | misinformation | 1.00 | — | — |
| q_tok28 | deceive | deceive | 1.00 | — | — |
| q_tok28 | mislead | mislead | 1.00 | — | — |
| q_tok28 | misrepresent | misrepresent | 1.00 | — | — |
| q_tok28 | ethical | ethical | 1.00 | — | — |
| q_tok28 | intentional | intentional | 1.00 | — | — |
| q_tok28 | legal | lawful | 1.00 | — | — |
| q_tok28 | comply | comply | 1.00 | — | — |
| q_tok28 | trustworthy | trustworthy | 1.00 | — | — |
| q_tok28 | faithful | faithful | 1.00 | — | — |
| q_tok29 | truth | truth | 1.00 | — | — |
| q_tok29 | honest | honest | 0.57 | `诚信`, `坦诚`, `␣чест` | — |
| q_tok29 | sincere | sincere | 1.00 | — | — |
| q_tok29 | integrity | integrity | 0.67 | — | `诚信` |
| q_tok29 | transparent | transparent | 1.00 | — | — |
| q_tok29 | factual | fact | 1.00 | — | — |

Replicate-2 families not the best match of any replicate-1 family: q_tok24: manipulate, q_tok24: spin, q_tok24: conceal, q_tok24: cover up, q_tok24: undisclosed, q_tok24: undercover, q_tok24: disclose, q_tok24: reveal, q_tok24: candid, q_tok24: instructions, q_tok24: constraints, q_tok24: forced, q_tok24: diplomatic, q_tok24: role, q_tok24: scripted, q_tok26: impersonate, q_tok26: manipulate, q_tok26: spin, q_tok26: conceal, q_tok26: cover up, q_tok26: undisclosed, q_tok26: disclose, q_tok26: reveal, q_tok26: candid, q_tok26: constraints, q_tok26: responsible, q_tok26: role, q_tok27: manipulate, q_tok27: bluff, q_tok27: spin, q_tok27: hide, q_tok27: undercover, q_tok27: instructions, q_tok27: constraints, q_tok27: forced, q_tok27: responsible, q_tok27: diplomatic, q_tok27: role, q_tok27: acting, q_tok27: scripted, q_tok28: candid, q_tok28: responsible, q_tok29: candid

## Families whose name recurs at 3 or more positions

- acknowledge: q_tok24, q_tok26, q_tok27
- adhere: q_tok24, q_tok26, q_tok27
- admit: q_tok24, q_tok26, q_tok27
- assert: q_tok24, q_tok25, q_tok26
- avoid: q_tok24, q_tok26, q_tok27
- blame: q_tok24, q_tok26, q_tok27
- candid: q_tok24, q_tok26, q_tok28, q_tok29
- cheat: q_tok24, q_tok26, q_tok27
- claim: q_tok24, q_tok25, q_tok26, q_tok27
- clarify: q_tok24, q_tok25, q_tok26, q_tok27
- comply: q_tok24, q_tok26, q_tok27, q_tok28
- conceal: q_tok24, q_tok26, q_tok27
- confess: q_tok24, q_tok26, q_tok28
- confidential: q_tok24, q_tok26, q_tok27
- constraints: q_tok24, q_tok26, q_tok27
- contradict: q_tok24, q_tok26, q_tok27
- deceive: q_tok24, q_tok26, q_tok27, q_tok28
- decline: q_tok24, q_tok26, q_tok27
- deny: q_tok24, q_tok25, q_tok26, q_tok27
- disclaimer: q_tok24, q_tok26, q_tok27
- disguise: q_tok24, q_tok26, q_tok27
- dishonest: q_tok24, q_tok26, q_tok27, q_tok28
- ethical: q_tok24, q_tok26, q_tok27, q_tok28
- ethics: q_tok24, q_tok26, q_tok27
- evade: q_tok24, q_tok26, q_tok27
- exaggerate: q_tok24, q_tok26, q_tok27
- fabricate: q_tok24, q_tok26, q_tok27
- fact: q_tok24, q_tok26, q_tok27, q_tok28, q_tok29
- factual: q_tok24, q_tok26, q_tok27, q_tok28, q_tok29
- faithful: q_tok24, q_tok26, q_tok27, q_tok28
- fake: q_tok24, q_tok26, q_tok27
- fiction: q_tok24, q_tok26, q_tok27
- fictional: q_tok24, q_tok26, q_tok27
- framing: q_tok24, q_tok26, q_tok27
- fraud: q_tok24, q_tok26, q_tok27
- genuine: q_tok24, q_tok26, q_tok28
- hide: q_tok24, q_tok26, q_tok27
- honest: q_tok24, q_tok25, q_tok26, q_tok27, q_tok28, q_tok29
- illegal: q_tok24, q_tok26, q_tok27
- instructed: q_tok24, q_tok26, q_tok27
- instructions: q_tok24, q_tok26, q_tok27
- integrity: q_tok24, q_tok26, q_tok27, q_tok28, q_tok29
- intentional: q_tok24, q_tok26, q_tok27, q_tok28
- justify: q_tok24, q_tok25, q_tok26, q_tok27
- knowingly: q_tok24, q_tok26, q_tok27
- lawful: q_tok24, q_tok26, q_tok27, q_tok28
- legal: q_tok24, q_tok26, q_tok27, q_tok28
- loyal: q_tok24, q_tok26, q_tok27
- manipulate: q_tok24, q_tok26, q_tok27
- misinformation: q_tok24, q_tok26, q_tok27, q_tok28
- mislead: q_tok24, q_tok26, q_tok27, q_tok28
- misrepresent: q_tok24, q_tok26, q_tok27, q_tok28
- omit: q_tok24, q_tok26, q_tok27
- persona: q_tok24, q_tok26, q_tok27
- pretend: q_tok24, q_tok26, q_tok27
- prohibited: q_tok24, q_tok26, q_tok27
- protect: q_tok24, q_tok26, q_tok27
- refuse: q_tok24, q_tok26, q_tok27
- reinterpret: q_tok24, q_tok26, q_tok27
- reject: q_tok24, q_tok26, q_tok27
- responsible: q_tok26, q_tok27, q_tok28
- role: q_tok24, q_tok26, q_tok27
- secret: q_tok24, q_tok26, q_tok27
- simulate: q_tok24, q_tok26, q_tok27
- sincere: q_tok24, q_tok26, q_tok28, q_tok29
- spin: q_tok24, q_tok26, q_tok27
- transparent: q_tok24, q_tok26, q_tok28, q_tok29
- truth: q_tok24, q_tok25, q_tok26, q_tok27, q_tok28, q_tok29
- unethical: q_tok24, q_tok26, q_tok27
- violate: q_tok24, q_tok26, q_tok27
- withhold: q_tok24, q_tok26, q_tok27

## Candidate opposite pairs (same position, lie side vs truth side, antonym words in the names or glosses; merged list)

- q_tok24: conceal / disclose
- q_tok24: conceal / reveal
- q_tok24: cover up / transparent
- q_tok24: deceive / honest
- q_tok24: deny / admit
- q_tok24: deny / confess
- q_tok24: dishonest / honest
- q_tok24: evade / admit
- q_tok24: fake / genuine
- q_tok24: hide / disclose
- q_tok24: hide / reveal
- q_tok24: mislead / candid
- q_tok24: pretend / sincere
- q_tok24: secret / transparent
- q_tok26: conceal / disclose
- q_tok26: conceal / reveal
- q_tok26: cover up / transparent
- q_tok26: deceive / honest
- q_tok26: deny / admit
- q_tok26: deny / confess
- q_tok26: dishonest / honest
- q_tok26: evade / admit
- q_tok26: fake / genuine
- q_tok26: hide / disclose
- q_tok26: hide / reveal
- q_tok26: mislead / candid
- q_tok26: pretend / sincere
- q_tok26: secret / transparent
- q_tok27: deceive / honest
- q_tok27: deny / admit
- q_tok27: dishonest / honest
- q_tok27: evade / admit
- q_tok28: deceive / honest
- q_tok28: dishonest / honest
- q_tok28: mislead / candid

Merged candidate list: `qwen3_6_27b_J_Q7_ab_questiond_merged.json` (283 families; replicate-2 families sharing at least half
their members with a replicate-1 family at the same position are folded into it).
