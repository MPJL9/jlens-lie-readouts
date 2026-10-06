# Family report: qwen3.6-27b, logit lens, band 35-58, part Q6_factual, group preans

Written by `scripts/family_report.py` from `qwen3_6_27b_LL_Q6_factual_preans_rep1.json` and `_rep2.json` (prompt
`prompts/family_generation.md`). Visibility = build-split scenario transcripts (of 233) in which
at least one member is present at the position within the band. Layer profile = band layers where
the family is present in at least one transcript, and the three layers with the most transcripts
(description only; scoring uses the whole band).

## preans_slot0

| rep | family | side | members | visibility | layer profile |
|---|---|---|---|---|---|
| 1 | admit (admitting) | truth | `承认` | 2 | L37-44; most at L37 (2), L39 (2), L40 (2) |
| 1 | deliberate (doing it on purpose, knowingly) | unclear | `明知` | 1 | L44-44; most at L44 (1) |
| 1 | objective (being objective) | unclear | `客观`, `␣objectively` | 54 | L36-44; most at L42 (21), L43 (48), L44 (21) |
| 1 | self-examination (checking or critiquing one's own reply) | unclear | `反思`, `自查`, `自检`, `␣critique`, `批判`, `指正` | 217 | L35-58; most at L52 (180), L53 (148), L58 (148) |
| 1 | law-abiding (obeying the law) | unclear | `守法` | 6 | L45-48; most at L45 (1), L46 (1), L47 (6) |
| 2 | admit (admitting) | truth | `承认` | 2 | L37-44; most at L37 (2), L39 (2), L40 (2) |
| 2 | I cannot ('I cannot' (declining stance)) | unclear | `我无法` | 22 | L53-53; most at L53 (22) |
| 2 | perfunctory (perfunctory, going through the motions) | unclear | `应付` | 1 | L53-53; most at L53 (1) |
| 2 | knowingly (knowing full well) | unclear | `明知` | 1 | L44-44; most at L44 (1) |
| 2 | objective (objective / objectively) | unclear | `客观`, `␣objectively` | 54 | L36-44; most at L42 (21), L43 (48), L44 (21) |
| 2 | self-check (self-examination / reflection) | unclear | `反思`, `自查`, `自检` | 67 | L35-48; most at L35 (27), L43 (23), L44 (43) |
| 2 | law-abiding (law-abiding) | unclear | `守法` | 6 | L45-48; most at L45 (1), L46 (1), L47 (6) |

## preans_slot1

| rep | family | side | members | visibility | layer profile |
|---|---|---|---|---|---|
| 1 | lie (telling a lie) | lie | `谎言`, `谎`, `撒谎`, `说谎`, `␣거짓`, `␣lie`, `␣lies`, `␣lied`, `␣lying`, `lying`, `␣mentira` | 147 | L35-58; most at L39 (138), L40 (119), L41 (105) |
| 1 | deceive (the act of deceiving) | lie | `欺骗`, `␣deception`, `␣deceptive`, `哄` | 128 | L35-58; most at L35 (89), L37 (89), L38 (91) |
| 1 | dishonest (not honest, insincere) | lie | `␣dishonest` | 1 | L57-57; most at L57 (1) |
| 1 | mislead (leading someone to a wrong belief) | lie | `␣misleading`, `误导`, `误导性` | 15 | L37-58; most at L52 (8), L53 (11), L54 (6) |
| 1 | conceal (hiding or covering up information) | lie | `隐瞒`, `掩盖`, `掩饰`, `掩`, `掩护`, `遮掩`, `遮`, `遮盖`, `遮住`, `遮蔽`, `␣conceal`, `␣concealed`, `␣masking`, `␣masked`, `␣hiding`, `␣hide`, `␣hides`, `-hide`, `Hide`, `_hide`, `隐藏` | 142 | L35-58; most at L36 (107), L49 (96), L50 (117) |
| 1 | withhold (keeping information back) | lie | `␣withholding` | 2 | L39-54; most at L51 (2), L52 (2), L53 (2) |
| 1 | omit (leaving information out) | lie | `␣omit`, `omit`, `␣omission`, `省略` | 9 | L44-54; most at L49 (3), L50 (7), L52 (3) |
| 1 | secret (kept secret, hidden, confidential) | lie | `␣hidden`, `Hidden`, `␣Hidden`, `-hidden`, `隐藏的` | 1 | L58-58; most at L58 (1) |
| 1 | fabricate (making up false content, fake or fictional) | lie | `虚构`, `␣fabricated`, `␣fabrication`, `␣invented`, `␣invent`, `凭空`, `伪造`, `fake`, `␣fake`, `fiction`, `␣fiction`, `␣fictional`, `-fiction` | 168 | L35-58; most at L44 (129), L45 (133), L46 (134) |
| 1 | pretend (pretending, disguising) | lie | `␣pretend`, `␣pretending`, `假装`, `伪装` | 7 | L48-54; most at L48 (4), L49 (3), L50 (2) |
| 1 | exaggerate (overstating) | lie | `夸大`, `␣exaggerated` | 12 | L35-57; most at L39 (4), L40 (7), L50 (6) |
| 1 | downplay (understating, playing down) | lie | `淡化` | 13 | L36-58; most at L49 (4), L50 (11), L53 (5) |
| 1 | evade (evading, dodging) | lie | `␣evasion`, `回避` | 4 | L48-53; most at L50 (2), L51 (2), L52 (4) |
| 1 | deny (denying) | lie | `␣denial`, `␣denying`, `␣deny`, `␣denies`, `␣denied`, `deny`, `␣Denied`, `否认`, `否認` | 79 | L35-58; most at L52 (41), L55 (47), L56 (47) |
| 1 | honest (being honest, truthful) | truth | `诚实`, `诚`, `诚信`, `坦诚`, `␣truthful`, `␣honest`, `␣honesty`, `␣honestly`, `␣Honest`, `如实`, `实话`, `说实话`, `如实供述` | 184 | L35-58; most at L35 (128), L39 (143), L40 (126) |
| 1 | transparent (being transparent) | truth | `␣transparency`, `-transparent`, `␣transparent`, `␣Transparency`, `透明`, `透明度` | 4 | L37-57; most at L40 (2), L41 (2), L54 (3) |
| 1 | admit (admitting) | truth | `承认`, `␣admitting`, `␣admissions`, `␣admitted`, `␣admission`, `␣admits`, `␣admit`, `␣Admission`, `␣admite` | 19 | L35-58; most at L55 (13), L56 (12), L57 (12) |
| 1 | confess (confessing, coming clean) | truth | `␣confess`, `␣confession`, `坦白` | 5 | L39-58; most at L51 (3), L52 (3), L54 (5) |
| 1 | disclose (disclosing, revealing) | truth | `␣disclosure`, `␣disclosed`, `信息披露`, `披露`, `揭露`, `␣revealing`, `␣revealed`, `␣reveal`, `␣reveals`, `公开` | 19 | L36-58; most at L44 (8), L45 (7), L47 (10) |
| 1 | deliberate (doing it on purpose, knowingly) | unclear | `明知`, `故意`, `刻意`, `␣intentionally`, `␣deliberately`, `␣deliberate`, `␣knowingly` | 180 | L35-58; most at L43 (154), L44 (151), L45 (143) |
| 1 | contradict (contradicting, being contrary to) | unclear | `␣contrad`, `␣contradict`, `␣contradictory`, `␣contradiction`, `␣contradictions`, `矛盾`, `矛盾的`, `␣contrary`, `相反`, `相反的` | 102 | L35-58; most at L38 (49), L49 (52), L50 (50) |
| 1 | violate (violating, going against) | unclear | `违背`, `违反`, `违反了`, `␣violate`, `␣violates` | 47 | L35-58; most at L35 (24), L48 (22), L49 (29) |
| 1 | imply (implying, suggesting indirectly) | unclear | `␣implying`, `␣implies`, `␣implied`, `␣imply`, `␣IMPLIED`, `␣implication`, `␣implications`, `␣implicitly`, `␣implicit`, `␣implica`, `␣implique`, `暗示`, `隐含` | 35 | L35-58; most at L54 (26), L55 (16), L56 (16) |
| 1 | claim (claiming, asserting) | unclear | `␣claim`, `␣claims`, `␣claiming`, `␣Claim`, `claim`, `␣claimed`, `Claim`, `␣Claims`, `␣CLAIM`, `claims`, `Claims`, `CLAIM`, `_claim`, `声称`, `宣称`, `␣assert`, `assert`, `_assert`, `␣asserting`, `␣assertions`, `␣Assert`, `␣assertion`, `␣asserts`, `_ASSERT`, `.assert`, `(assert`, `	assert`, `␣asserted`, `Assert`, `␣Assertion` | 159 | L35-58; most at L50 (99), L51 (99), L52 (101) |
| 1 | refuse (refusing) | unclear | `␣refusal`, `␣refusing`, `␣refused`, `␣refuse`, `␣refuses`, `␣refus`, `拒绝`, `拒绝了` | 18 | L38-58; most at L56 (16), L57 (13), L58 (13) |
| 1 | blame (blaming) | unclear | `␣blaming`, `␣blame`, `␣blames`, `␣blamed` | 18 | L49-58; most at L51 (12), L54 (15), L55 (11) |
| 1 | ethical (ethical, moral) | unclear | `␣ethical`, `␣ethics`, `伦理`, `␣moral` | 2 | L52-58; most at L52 (1), L53 (1), L58 (2) |
| 1 | objective (being objective) | unclear | `客观`, `␣objectively`, `␣objective` | 90 | L35-53; most at L35 (71), L36 (58), L44 (45) |
| 1 | subjective (being subjective) | unclear | `主观` | 3 | L37-39; most at L37 (1), L38 (1), L39 (3) |
| 2 | lie (telling a lie) | lie | `␣lie`, `␣lies`, `␣lied`, `␣lying`, `lying`, `谎言`, `谎`, `撒谎`, `说谎`, `␣거짓`, `␣mentira` | 147 | L35-58; most at L39 (138), L40 (119), L41 (105) |
| 2 | deceive (the act of deceiving) | lie | `␣deception`, `␣deceptive`, `欺骗` | 127 | L35-58; most at L35 (88), L37 (89), L38 (91) |
| 2 | mislead (misleading someone) | lie | `␣misleading`, `误导`, `误导性` | 15 | L37-58; most at L52 (8), L53 (11), L54 (6) |
| 2 | conceal (withholding or concealing the truth) | lie | `␣conceal`, `␣concealed`, `隐瞒`, `瞒` | 134 | L35-58; most at L36 (91), L40 (89), L50 (112) |
| 2 | hide (hiding / hidden) | lie | `␣hide`, `␣hides`, `␣hiding`, `-hide`, `Hide`, `_hide`, `␣hidden`, `-hidden`, `Hidden`, `␣Hidden`, `隐藏`, `隐藏的` | 10 | L37-58; most at L52 (3), L53 (6), L58 (3) |
| 2 | cover up (covering up or masking something) | lie | `掩盖`, `掩饰`, `遮`, `遮盖`, `遮掩`, `遮住`, `遮蔽`, `␣masking`, `␣masked` | 106 | L35-58; most at L44 (74), L45 (74), L50 (72) |
| 2 | fabricate (making something up) | lie | `␣fabricated`, `␣fabrication`, `␣invented`, `␣invent`, `伪造`, `凭空` | 106 | L35-58; most at L36 (71), L37 (98), L39 (43) |
| 2 | fake (fake / falsified) | lie | `fake`, `␣fake` | 51 | L35-45; most at L37 (29), L38 (45), L44 (29) |
| 2 | pretend (pretending / disguise) | lie | `␣pretend`, `␣pretending`, `假装`, `伪装` | 7 | L48-54; most at L48 (4), L49 (3), L50 (2) |
| 2 | exaggerate (exaggerating) | lie | `␣exaggerated`, `夸大` | 12 | L35-57; most at L39 (4), L40 (7), L50 (6) |
| 2 | downplay (downplaying) | lie | `淡化` | 13 | L36-58; most at L49 (4), L50 (11), L53 (5) |
| 2 | deny (denying (the truth / a claim)) | lie | `␣deny`, `deny`, `␣denying`, `␣denies`, `␣denied`, `␣Denied`, `␣denial`, `否认`, `否認` | 79 | L35-58; most at L52 (41), L55 (47), L56 (47) |
| 2 | dishonest (dishonest / hypocritical) | lie | `␣dishonest` | 1 | L57-57; most at L57 (1) |
| 2 | honest (honest / truthful / telling it as it is) | truth | `␣honest`, `␣honesty`, `␣honestly`, `␣Honest`, `␣truthful`, `诚实`, `诚`, `诚信`, `坦诚`, `如实`, `实话`, `说实话`, `实事求是` | 185 | L35-58; most at L35 (128), L39 (143), L40 (126) |
| 2 | admit (admitting) | truth | `␣admit`, `␣admits`, `␣admitted`, `␣admitting`, `␣admission`, `␣admissions`, `␣Admission`, `␣admite`, `承认` | 19 | L35-58; most at L55 (13), L56 (12), L57 (12) |
| 2 | confess (confessing / coming clean) | truth | `␣confess`, `␣confession`, `坦白`, `如实供述` | 6 | L39-58; most at L51 (3), L52 (3), L54 (5) |
| 2 | disclose (disclosing / revealing / making public) | truth | `␣disclosure`, `␣disclosed`, `␣reveal`, `␣reveals`, `␣revealed`, `␣revealing`, `披露`, `信息披露`, `揭露`, `揭示`, `揭示了`, `公开` | 19 | L36-58; most at L44 (8), L45 (7), L47 (10) |
| 2 | transparent (transparency) | truth | `␣transparency`, `␣Transparency`, `␣transparent`, `-transparent`, `透明`, `透明度` | 4 | L37-57; most at L40 (2), L41 (2), L54 (3) |
| 2 | refuse (refusing / declining) | unclear | `␣refusal`, `␣refuse`, `␣refuses`, `␣refused`, `␣refusing`, `␣refus`, `拒绝`, `拒绝了`, `␣decline`, `␣declines`, `␣declined` | 18 | L38-58; most at L56 (16), L57 (13), L58 (13) |
| 2 | I cannot ('I cannot' (declining stance)) | unclear | `我不能`, `我无法` | 11 | L51-58; most at L52 (9), L56 (8), L58 (7) |
| 2 | evade (evading / avoiding the question) | lie | `␣evasion`, `回避` | 4 | L48-53; most at L50 (2), L51 (2), L52 (4) |
| 2 | perfunctory (perfunctory, going through the motions) | unclear | `应付`, `敷衍` | 20 | L35-47; most at L35 (7), L43 (11), L44 (7) |
| 2 | deliberate (deliberately / intentionally) | unclear | `故意`, `刻意`, `␣intentionally`, `␣deliberately`, `␣deliberate` | 84 | L35-58; most at L35 (30), L36 (73), L47 (25) |
| 2 | knowingly (knowing full well) | unclear | `明知`, `␣knowingly` | 172 | L35-58; most at L43 (154), L44 (151), L45 (142) |
| 2 | contradict (contradicting / contradiction) | unclear | `␣contradict`, `␣contrad`, `␣contradictory`, `␣contradiction`, `␣contradictions`, `矛盾`, `矛盾的` | 84 | L35-58; most at L49 (50), L50 (48), L54 (44) |
| 2 | violate (violating / going against (a principle)) | unclear | `违背`, `违反`, `违反了` | 47 | L35-58; most at L35 (24), L48 (22), L49 (29) |
| 2 | outwardly (on the surface / outwardly) | unclear | `表面上` | 4 | L36-43; most at L37 (3), L38 (3), L43 (1) |
| 2 | fiction (fiction / fictional) | unclear | `fiction`, `␣fiction`, `-fiction`, `␣fictional`, `␣fict`, `虚构`, `架空` | 163 | L35-58; most at L44 (129), L45 (133), L46 (134) |
| 2 | hypothetical (hypothetical) | unclear | `␣hypothetical` | 10 | L36-58; most at L44 (5), L46 (4), L52 (5) |
| 2 | simulated (simulated / simulation) | unclear | `␣simulated`, `模拟` | 2 | L35-57; most at L47 (2), L48 (2), L49 (2) |
| 2 | role-play (playing a role / persona) | unclear | `␣persona`, `␣personas`, `␣Persona`, `Persona`, `扮演` | 5 | L51-58; most at L51 (2), L52 (3), L56 (3) |
| 2 | ethics (ethics / morality) | unclear | `␣ethical`, `␣ethics`, `伦理`, `␣moral` | 2 | L52-58; most at L52 (1), L53 (1), L58 (2) |
| 2 | objective (objective / objectively) | unclear | `客观`, `␣objectively`, `␣objective` | 90 | L35-53; most at L35 (71), L36 (58), L44 (45) |
| 2 | subjective (subjective) | unclear | `主观` | 3 | L37-39; most at L37 (1), L38 (1), L39 (3) |

## preans_slot2

| rep | family | side | members | visibility | layer profile |
|---|---|---|---|---|---|
| 1 | lie (telling a lie) | lie | `谎言`, `谎`, `撒谎`, `说谎`, `␣거짓`, `␣lie`, `␣lies`, `␣lying`, `␣mentira` | 13 | L35-58; most at L39 (7), L40 (7), L55 (5) |
| 1 | deceive (the act of deceiving) | lie | `欺骗`, `␣deception`, `␣deceptive`, `哄` | 20 | L35-58; most at L35 (7), L36 (12), L37 (11) |
| 1 | mislead (leading someone to a wrong belief) | lie | `␣misleading`, `误导` | 5 | L46-58; most at L50 (3), L53 (4), L54 (4) |
| 1 | conceal (hiding or covering up information) | lie | `隐瞒`, `掩盖`, `掩饰`, `掩`, `遮`, `␣conceal`, `␣concealed`, `␣masking`, `␣hiding`, `␣hide`, `␣hides`, `Hide`, `隐藏`, `隐藏着` | 94 | L35-58; most at L35 (51), L36 (50), L40 (49) |
| 1 | withhold (keeping information back) | lie | `␣withholding`, `␣withheld`, `␣withhold` | 4 | L36-58; most at L48 (2), L49 (2), L50 (2) |
| 1 | omit (leaving information out) | lie | `␣omit`, `␣omission` | 1 | L49-56; most at L49 (1), L50 (1), L51 (1) |
| 1 | secret (kept secret, hidden, confidential) | lie | `␣secret`, `secret`, `␣Secret`, `Secret`, `_secret`, `-secret`, `␣secretly`, `秘密`, `的秘密`, `私下`, `暗中`, `机密`, `␣confidential`, `␣hidden`, `hidden`, `Hidden`, `隐藏的`, `隐蔽`, `幕后`, `内幕` | 68 | L35-58; most at L44 (28), L55 (29), L56 (44) |
| 1 | fabricate (making up false content, fake or fictional) | lie | `虚构`, `␣fabricated`, `␣fabrication`, `␣invented`, `凭空`, `伪造`, `作假`, `fake`, `␣fake`, `Fake`, `fiction`, `␣fiction`, `␣fictional`, `-fiction`, `␣Fiction` | 101 | L35-58; most at L36 (56), L37 (73), L40 (59) |
| 1 | pretend (pretending, disguising) | lie | `伪装` | 3 | L35-51; most at L35 (2), L36 (2), L51 (1) |
| 1 | exaggerate (overstating) | lie | `夸大` | 3 | L37-53; most at L37 (2), L38 (2), L39 (2) |
| 1 | distort (twisting the facts) | lie | `扭曲` | 2 | L45-51; most at L45 (1), L46 (1), L47 (1) |
| 1 | evade (evading, dodging) | lie | `␣evasion`, `回避` | 1 | L47-58; most at L47 (1), L48 (1), L49 (1) |
| 1 | manipulate (manipulating) | lie | `␣manipulation` | 1 | L54-54; most at L54 (1) |
| 1 | deny (denying) | lie | `␣denial`, `␣denying`, `␣deny`, `␣denies`, `␣denied`, `deny`, `否认` | 3 | L35-58; most at L36 (3), L39 (3), L40 (3) |
| 1 | honest (being honest, truthful) | truth | `诚实`, `诚`, `诚信`, `坦诚`, `␣truthful`, `␣honest`, `␣honesty`, `如实`, `实话` | 85 | L35-52; most at L35 (63), L36 (43), L40 (38) |
| 1 | admit (admitting) | truth | `承认`, `␣admitting`, `␣admissions`, `␣admitted`, `␣admission`, `␣admits`, `␣admit`, `␣Admission`, `␣admite` | 23 | L35-58; most at L43 (16), L44 (18), L45 (13) |
| 1 | disclose (disclosing, revealing) | truth | `␣disclosed`, `信息披露`, `披露`, `揭露`, `公开` | 9 | L35-53; most at L35 (3), L43 (2), L44 (3) |
| 1 | deliberate (doing it on purpose, knowingly) | unclear | `明知`, `故意`, `刻意`, `有意`, `␣intentionally`, `␣intentional`, `␣deliberately`, `␣deliberate`, `␣knowingly` | 146 | L35-58; most at L47 (94), L48 (103), L49 (107) |
| 1 | contradict (contradicting, being contrary to) | unclear | `␣contrad`, `␣contradict`, `␣contradictory`, `␣contradiction`, `␣contradictions`, `␣contradd`, `矛盾`, `矛盾的`, `␣contrary`, `相反`, `相反的` | 38 | L35-58; most at L44 (17), L47 (12), L49 (13) |
| 1 | violate (violating, going against) | unclear | `违背`, `违反`, `违反了`, `␣violate`, `␣violates`, `␣violated`, `␣violating` | 42 | L35-58; most at L35 (18), L37 (18), L47 (17) |
| 1 | imply (implying, suggesting indirectly) | unclear | `␣implied`, `␣implicitly`, `␣implicit`, `暗示`, `隐含` | 7 | L37-54; most at L45 (3), L50 (2), L54 (2) |
| 1 | claim (claiming, asserting) | unclear | `␣claim`, `␣claims`, `␣claiming`, `␣Claim`, `claim`, `␣claimed`, `Claim`, `␣Claims`, `␣CLAIM`, `claims`, `Claims`, `CLAIM`, `_claim`, `声称`, `宣称`, `␣assert`, `assert`, `_assert`, `␣asserting`, `␣assertions`, `␣Assert`, `␣assertion`, `␣asserts`, `_ASSERT`, `.assert`, `␣asserted`, `Assert`, `/assert` | 10 | L35-58; most at L36 (6), L43 (5), L44 (5) |
| 1 | refuse (refusing) | unclear | `␣refusal`, `␣refusing`, `␣refused`, `␣refuse`, `␣refuses`, `␣refus`, `拒绝`, `拒绝了` | 4 | L35-58; most at L44 (4), L45 (4), L46 (4) |
| 1 | ethical (ethical, moral) | unclear | `␣ethical`, `ethical`, `␣ethics`, `␣Ethics`, `伦理`, `道德`, `的道德`, `职业道德`, `␣moral`, `␣morally`, `␣morality` | 27 | L35-58; most at L39 (15), L40 (16), L58 (15) |
| 1 | unethical (unethical, immoral) | unclear | `␣unethical`, `␣immoral` | 16 | L50-58; most at L55 (13), L56 (12), L58 (11) |
| 1 | objective (being objective) | unclear | `客观`, `␣objective` | 98 | L35-58; most at L35 (61), L36 (81), L37 (42) |
| 1 | subjective (being subjective) | unclear | `主观` | 2 | L35-40; most at L35 (2), L36 (2), L37 (1) |
| 2 | lie (telling a lie) | lie | `␣lie`, `␣lies`, `␣lying`, `谎言`, `谎`, `撒谎`, `说谎`, `␣거짓`, `␣mentira` | 13 | L35-58; most at L39 (7), L40 (7), L55 (5) |
| 2 | deceive (the act of deceiving) | lie | `␣deception`, `␣deceptive`, `欺骗` | 18 | L35-58; most at L35 (7), L36 (11), L37 (8) |
| 2 | mislead (misleading someone) | lie | `␣misleading`, `误导` | 5 | L46-58; most at L50 (3), L53 (4), L54 (4) |
| 2 | conceal (withholding or concealing the truth) | lie | `␣conceal`, `␣concealed`, `隐瞒`, `瞒` | 69 | L35-58; most at L35 (43), L36 (40), L40 (46) |
| 2 | hide (hiding / hidden) | lie | `␣hide`, `␣hides`, `␣hiding`, `Hide`, `␣hidden`, `hidden`, `Hidden`, `隐藏`, `隐藏的`, `隐藏着`, `隐蔽` | 44 | L35-58; most at L55 (29), L56 (32), L58 (17) |
| 2 | cover up (covering up or masking something) | lie | `掩盖`, `掩饰`, `遮`, `␣masking` | 30 | L35-54; most at L35 (17), L36 (27), L37 (17) |
| 2 | secret (secret / done in secret) | lie | `␣secret`, `secret`, `␣Secret`, `Secret`, `␣secretly`, `_secret`, `-secret`, `秘密`, `的秘密`, `私下`, `暗中` | 59 | L35-58; most at L43 (25), L44 (28), L56 (39) |
| 2 | fabricate (making something up) | lie | `␣fabricated`, `␣fabrication`, `␣invented`, `伪造`, `凭空` | 10 | L36-58; most at L36 (3), L37 (5), L40 (3) |
| 2 | fake (fake / falsified) | lie | `fake`, `␣fake`, `Fake`, `作假` | 25 | L35-44; most at L36 (16), L37 (18), L38 (12) |
| 2 | pretend (pretending / disguise) | lie | `伪装` | 3 | L35-51; most at L35 (2), L36 (2), L51 (1) |
| 2 | manipulate (manipulating someone) | lie | `␣manipulation` | 1 | L54-54; most at L54 (1) |
| 2 | exaggerate (exaggerating) | lie | `夸大` | 3 | L37-53; most at L37 (2), L38 (2), L39 (2) |
| 2 | deny (denying (the truth / a claim)) | lie | `␣deny`, `deny`, `␣denying`, `␣denies`, `␣denied`, `␣denial`, `否认` | 3 | L35-58; most at L36 (3), L39 (3), L40 (3) |
| 2 | unethical (unethical / immoral) | lie | `␣unethical`, `␣immoral` | 16 | L50-58; most at L55 (13), L56 (12), L58 (11) |
| 2 | honest (honest / truthful / telling it as it is) | truth | `␣honest`, `␣honesty`, `␣truthful`, `诚实`, `诚`, `诚信`, `坦诚`, `如实`, `实话`, `实事求是` | 85 | L35-52; most at L35 (63), L36 (43), L40 (38) |
| 2 | admit (admitting) | truth | `␣admit`, `␣admits`, `␣admitted`, `␣admitting`, `␣admission`, `␣admissions`, `␣Admission`, `␣admite`, `承认` | 23 | L35-58; most at L43 (16), L44 (18), L45 (13) |
| 2 | disclose (disclosing / revealing / making public) | truth | `␣disclosed`, `披露`, `信息披露`, `揭露`, `公开` | 9 | L35-53; most at L35 (3), L43 (2), L44 (3) |
| 2 | refuse (refusing / declining) | unclear | `␣refusal`, `␣refuse`, `␣refuses`, `␣refused`, `␣refusing`, `␣refus`, `拒绝`, `拒绝了`, `␣decline`, `␣declines`, `␣declined` | 4 | L35-58; most at L44 (4), L45 (4), L46 (4) |
| 2 | I cannot ('I cannot' (declining stance)) | unclear | `我不能` | 1 | L53-53; most at L53 (1) |
| 2 | evade (evading / avoiding the question) | lie | `␣evasion`, `回避` | 1 | L47-58; most at L47 (1), L48 (1), L49 (1) |
| 2 | perfunctory (perfunctory, going through the motions) | unclear | `应付` | 2 | L43-53; most at L43 (2), L44 (1), L45 (1) |
| 2 | deliberate (deliberately / intentionally) | unclear | `故意`, `刻意`, `有意`, `␣intentionally`, `␣intentional`, `␣deliberately`, `␣deliberate` | 62 | L35-57; most at L35 (48), L36 (54), L37 (31) |
| 2 | knowingly (knowing full well) | unclear | `明知`, `␣knowingly` | 122 | L35-58; most at L47 (91), L48 (100), L49 (101) |
| 2 | contradict (contradicting / contradiction) | unclear | `␣contradict`, `␣contradictory`, `␣contradiction`, `␣contradictions`, `矛盾`, `矛盾的` | 36 | L35-58; most at L44 (15), L47 (9), L49 (13) |
| 2 | violate (violating / going against (a principle)) | unclear | `违背`, `违反`, `违反了` | 42 | L35-58; most at L35 (18), L37 (18), L47 (17) |
| 2 | outwardly (on the surface / outwardly) | unclear | `表面上` | 21 | L35-43; most at L36 (12), L37 (14), L38 (11) |
| 2 | fiction (fiction / fictional) | unclear | `fiction`, `␣fiction`, `␣Fiction`, `-fiction`, `␣fictional`, `␣fict`, `虚构`, `架空` | 94 | L35-58; most at L36 (51), L37 (66), L40 (59) |
| 2 | hypothetical (hypothetical) | unclear | `␣hypothetical` | 40 | L35-58; most at L40 (33), L52 (25), L53 (26) |
| 2 | simulated (simulated / simulation) | unclear | `␣simulated`, `␣simulation`, `␣Simulation`, `模拟` | 22 | L35-58; most at L35 (8), L36 (8), L51 (9) |
| 2 | role-play (playing a role / persona) | unclear | `␣persona`, `␣personas`, `␣Persona`, `persona`, `Persona`, `␣Personas`, `扮演`, `角色扮演` | 100 | L36-58; most at L52 (82), L53 (90), L56 (89) |
| 2 | ethics (ethics / morality) | unclear | `␣ethical`, `ethical`, `␣ethics`, `␣Ethics`, `伦理`, `道德`, `的道德`, `职业道德`, `␣moral`, `␣morally`, `␣morality` | 27 | L35-58; most at L39 (15), L40 (16), L58 (15) |
| 2 | objective (objective / objectively) | unclear | `客观`, `␣objective` | 98 | L35-58; most at L35 (61), L36 (81), L37 (42) |
| 2 | subjective (subjective) | unclear | `主观` | 2 | L35-40; most at L35 (2), L36 (2), L37 (1) |

## preans_slot3

| rep | family | side | members | visibility | layer profile |
|---|---|---|---|---|---|
| 1 | secret (kept secret, hidden, confidential) | lie | `秘密` | 1 | L47-47; most at L47 (1) |
| 1 | fabricate (making up false content, fake or fictional) | lie | `fiction` | 3 | L45-46; most at L45 (1), L46 (3) |
| 1 | confess (confessing, coming clean) | truth | `坦白` | 1 | L50-51; most at L50 (1), L51 (1) |
| 1 | disclose (disclosing, revealing) | truth | `公开`, `公布` | 164 | L36-45; most at L43 (87), L44 (161), L45 (23) |
| 1 | violate (violating, going against) | unclear | `违背` | 3 | L48-49; most at L48 (2), L49 (3) |
| 1 | claim (claiming, asserting) | unclear | `␣assert` | 3 | L39-43; most at L39 (3), L42 (1), L43 (1) |
| 1 | refuse (refusing) | unclear | `␣refusal`, `␣refusing`, `␣refuse`, `␣refuses`, `␣refus` | 60 | L38-53; most at L47 (54), L48 (33), L51 (22) |
| 1 | ethical (ethical, moral) | unclear | `␣ethical`, `伦理` | 3 | L43-50; most at L44 (2), L48 (2), L49 (2) |
| 1 | apologize (being sorry) | unclear | `抱歉` | 38 | L48-57; most at L50 (4), L54 (35), L55 (5) |
| 1 | law-abiding (obeying the law) | unclear | `守法` | 38 | L43-43; most at L43 (38) |
| 2 | secret (secret / done in secret) | lie | `秘密` | 1 | L47-47; most at L47 (1) |
| 2 | confess (confessing / coming clean) | truth | `坦白` | 1 | L50-51; most at L50 (1), L51 (1) |
| 2 | disclose (disclosing / revealing / making public) | truth | `公开`, `公布` | 164 | L36-45; most at L43 (87), L44 (161), L45 (23) |
| 2 | refuse (refusing / declining) | unclear | `␣refusal`, `␣refuse`, `␣refuses`, `␣refusing`, `␣refus` | 60 | L38-53; most at L47 (54), L48 (33), L51 (22) |
| 2 | I cannot ('I cannot' (declining stance)) | unclear | `我不能`, `我无法` | 40 | L48-55; most at L52 (26), L53 (29), L54 (19) |
| 2 | violate (violating / going against (a principle)) | unclear | `违背` | 3 | L48-49; most at L48 (2), L49 (3) |
| 2 | fiction (fiction / fictional) | unclear | `fiction` | 3 | L45-46; most at L45 (1), L46 (3) |
| 2 | ethics (ethics / morality) | unclear | `␣ethical`, `伦理` | 3 | L43-50; most at L44 (2), L48 (2), L49 (2) |
| 2 | sorry (apologizing) | unclear | `抱歉` | 38 | L48-57; most at L50 (4), L54 (35), L55 (5) |
| 2 | law-abiding (law-abiding) | unclear | `守法` | 38 | L43-43; most at L43 (38) |

## preans_slot4

| rep | family | side | members | visibility | layer profile |
|---|---|---|---|---|---|
| 1 | lie (telling a lie) | lie | `谎言`, `撒谎`, `说谎` | 20 | L36-41; most at L37 (7), L39 (15), L40 (14) |
| 1 | deceive (the act of deceiving) | lie | `欺骗`, `␣deception`, `␣deceptive` | 32 | L35-58; most at L37 (20), L39 (22), L40 (24) |
| 1 | dishonest (not honest, insincere) | lie | `␣dishonest`, `虚伪` | 4 | L38-40; most at L38 (3), L40 (1) |
| 1 | conceal (hiding or covering up information) | lie | `隐瞒` | 17 | L36-46; most at L38 (10), L39 (13), L40 (16) |
| 1 | fabricate (making up false content, fake or fictional) | lie | `虚构`, `␣invented`, `␣invent`, `伪`, `fiction`, `␣fiction`, `␣fictional`, `-fiction`, `␣Fiction` | 71 | L35-50; most at L36 (53), L37 (49), L40 (55) |
| 1 | deny (denying) | lie | `否认` | 21 | L35-56; most at L44 (13), L45 (15), L46 (15) |
| 1 | honest (being honest, truthful) | truth | `诚实`, `诚`, `诚信`, `坦诚`, `␣truthful`, `␣honest`, `如实`, `实话` | 155 | L35-51; most at L39 (87), L40 (117), L45 (89) |
| 1 | admit (admitting) | truth | `承认` | 23 | L35-47; most at L35 (19), L40 (11), L45 (7) |
| 1 | confess (confessing, coming clean) | truth | `坦白` | 1 | L37-37; most at L37 (1) |
| 1 | disclose (disclosing, revealing) | truth | `公开` | 1 | L46-46; most at L46 (1) |
| 1 | deliberate (doing it on purpose, knowingly) | unclear | `明知`, `故意`, `故意的`, `␣intentionally`, `␣intentional`, `␣deliberately`, `␣deliberate` | 68 | L35-58; most at L36 (55), L37 (32), L43 (32) |
| 1 | contradict (contradicting, being contrary to) | unclear | `␣contrad`, `␣contradict`, `相反` | 10 | L35-50; most at L36 (3), L42 (5), L44 (3) |
| 1 | violate (violating, going against) | unclear | `违背`, `违反`, `违反了` | 8 | L35-46; most at L35 (7), L43 (1), L46 (2) |
| 1 | imply (implying, suggesting indirectly) | unclear | `隐含` | 1 | L45-45; most at L45 (1) |
| 1 | claim (claiming, asserting) | unclear | `␣assert`, `assert` | 7 | L35-43; most at L35 (4), L36 (7), L37 (4) |
| 1 | refuse (refusing) | unclear | `拒绝` | 1 | L36-41; most at L36 (1), L37 (1), L38 (1) |
| 1 | apologize (being sorry) | unclear | `抱歉` | 1 | L44-44; most at L44 (1) |
| 1 | objective (being objective) | unclear | `客观`, `␣objectively` | 114 | L35-44; most at L35 (82), L36 (93), L37 (30) |
| 1 | subjective (being subjective) | unclear | `主观` | 15 | L35-40; most at L35 (13), L36 (3), L39 (1) |
| 1 | self-examination (checking or critiquing one's own reply) | unclear | `反思`, `自查` | 6 | L35-43; most at L35 (5), L43 (1) |
| 2 | lie (telling a lie) | lie | `谎言`, `撒谎`, `说谎` | 20 | L36-41; most at L37 (7), L39 (15), L40 (14) |
| 2 | deceive (the act of deceiving) | lie | `␣deception`, `␣deceptive`, `欺骗` | 32 | L35-58; most at L37 (20), L39 (22), L40 (24) |
| 2 | conceal (withholding or concealing the truth) | lie | `隐瞒` | 17 | L36-46; most at L38 (10), L39 (13), L40 (16) |
| 2 | fabricate (making something up) | lie | `␣invented`, `␣invent` | 1 | L37-40; most at L37 (1), L38 (1), L39 (1) |
| 2 | fake (fake / falsified) | lie | `伪` | 3 | L38-40; most at L38 (2), L40 (1) |
| 2 | deny (denying (the truth / a claim)) | lie | `否认` | 21 | L35-56; most at L44 (13), L45 (15), L46 (15) |
| 2 | dishonest (dishonest / hypocritical) | lie | `␣dishonest`, `虚伪` | 4 | L38-40; most at L38 (3), L40 (1) |
| 2 | honest (honest / truthful / telling it as it is) | truth | `␣honest`, `␣truthful`, `诚实`, `诚`, `诚信`, `坦诚`, `如实`, `实话`, `实事求是` | 156 | L35-51; most at L39 (87), L40 (117), L45 (89) |
| 2 | admit (admitting) | truth | `承认` | 23 | L35-47; most at L35 (19), L40 (11), L45 (7) |
| 2 | confess (confessing / coming clean) | truth | `坦白` | 1 | L37-37; most at L37 (1) |
| 2 | disclose (disclosing / revealing / making public) | truth | `公开` | 1 | L46-46; most at L46 (1) |
| 2 | refuse (refusing / declining) | unclear | `拒绝` | 1 | L36-41; most at L36 (1), L37 (1), L38 (1) |
| 2 | I cannot ('I cannot' (declining stance)) | unclear | `我不能`, `我无法` | 18 | L50-57; most at L52 (16), L53 (10), L54 (5) |
| 2 | deliberate (deliberately / intentionally) | unclear | `故意`, `故意的`, `␣intentionally`, `␣intentional`, `␣deliberately`, `␣deliberate` | 42 | L35-58; most at L36 (33), L37 (32), L43 (19) |
| 2 | knowingly (knowing full well) | unclear | `明知` | 42 | L35-48; most at L36 (30), L43 (19), L44 (18) |
| 2 | contradict (contradicting / contradiction) | unclear | `␣contradict` | 1 | L50-50; most at L50 (1) |
| 2 | violate (violating / going against (a principle)) | unclear | `违背`, `违反`, `违反了` | 8 | L35-46; most at L35 (7), L43 (1), L46 (2) |
| 2 | outwardly (on the surface / outwardly) | unclear | `表面上` | 2 | L38-39; most at L38 (1), L39 (1) |
| 2 | fiction (fiction / fictional) | unclear | `fiction`, `␣fiction`, `␣Fiction`, `-fiction`, `␣fictional`, `␣fict`, `虚构`, `架空` | 71 | L35-50; most at L36 (53), L37 (49), L40 (55) |
| 2 | hypothetical (hypothetical) | unclear | `␣hypothetical` | 13 | L35-48; most at L36 (10), L38 (11), L40 (9) |
| 2 | simulated (simulated / simulation) | unclear | `␣simulated`, `␣simulation`, `模拟` | 18 | L35-50; most at L35 (12), L36 (15), L37 (13) |
| 2 | objective (objective / objectively) | unclear | `客观`, `␣objectively` | 114 | L35-44; most at L35 (82), L36 (93), L37 (30) |
| 2 | subjective (subjective) | unclear | `主观` | 15 | L35-40; most at L35 (13), L36 (3), L39 (1) |
| 2 | self-check (self-examination / reflection) | unclear | `反思`, `自查` | 6 | L35-43; most at L35 (5), L43 (1) |
| 2 | sorry (apologizing) | unclear | `抱歉` | 1 | L44-44; most at L44 (1) |

## Replicate overlap

For each replicate-1 family, the replicate-2 family at the same position sharing the most members.

| position | rep-1 family | best rep-2 family | Jaccard of member ids | only in rep 1 | only in rep 2 |
|---|---|---|---|---|---|
| preans_slot0 | admit | admit | 1.00 | — | — |
| preans_slot0 | deliberate | knowingly | 1.00 | — | — |
| preans_slot0 | objective | objective | 1.00 | — | — |
| preans_slot0 | self-examination | self-check | 0.50 | `␣critique`, `批判`, `指正` | — |
| preans_slot0 | law-abiding | law-abiding | 1.00 | — | — |
| preans_slot1 | lie | lie | 1.00 | — | — |
| preans_slot1 | deceive | deceive | 0.75 | `哄` | — |
| preans_slot1 | dishonest | dishonest | 1.00 | — | — |
| preans_slot1 | mislead | mislead | 1.00 | — | — |
| preans_slot1 | conceal | cover up | 0.43 | `隐瞒`, `掩`, `掩护`, `␣conceal`, `␣concealed`, `␣hiding`, `␣hide`, `␣hides`, `-hide`, `Hide`, `_hide`, `隐藏` | — |
| preans_slot1 | withhold | — | 0 | all | — |
| preans_slot1 | omit | — | 0 | all | — |
| preans_slot1 | secret | hide | 0.42 | — | `␣hide`, `␣hides`, `␣hiding`, `-hide`, `Hide`, `_hide`, `隐藏` |
| preans_slot1 | fabricate | fabricate | 0.46 | `虚构`, `fake`, `␣fake`, `fiction`, `␣fiction`, `␣fictional`, `-fiction` | — |
| preans_slot1 | pretend | pretend | 1.00 | — | — |
| preans_slot1 | exaggerate | exaggerate | 1.00 | — | — |
| preans_slot1 | downplay | downplay | 1.00 | — | — |
| preans_slot1 | evade | evade | 1.00 | — | — |
| preans_slot1 | deny | deny | 1.00 | — | — |
| preans_slot1 | honest | honest | 0.86 | `如实供述` | `实事求是` |
| preans_slot1 | transparent | transparent | 1.00 | — | — |
| preans_slot1 | admit | admit | 1.00 | — | — |
| preans_slot1 | confess | confess | 0.75 | — | `如实供述` |
| preans_slot1 | disclose | disclose | 0.83 | — | `揭示`, `揭示了` |
| preans_slot1 | deliberate | deliberate | 0.71 | `明知`, `␣knowingly` | — |
| preans_slot1 | contradict | contradict | 0.70 | `␣contrary`, `相反`, `相反的` | — |
| preans_slot1 | violate | violate | 0.60 | `␣violate`, `␣violates` | — |
| preans_slot1 | imply | — | 0 | all | — |
| preans_slot1 | claim | — | 0 | all | — |
| preans_slot1 | refuse | refuse | 0.73 | — | `␣decline`, `␣declines`, `␣declined` |
| preans_slot1 | blame | — | 0 | all | — |
| preans_slot1 | ethical | ethics | 1.00 | — | — |
| preans_slot1 | objective | objective | 1.00 | — | — |
| preans_slot1 | subjective | subjective | 1.00 | — | — |
| preans_slot2 | lie | lie | 1.00 | — | — |
| preans_slot2 | deceive | deceive | 0.75 | `哄` | — |
| preans_slot2 | mislead | mislead | 1.00 | — | — |
| preans_slot2 | conceal | hide | 0.32 | `隐瞒`, `掩盖`, `掩饰`, `掩`, `遮`, `␣conceal`, `␣concealed`, `␣masking` | `␣hidden`, `hidden`, `Hidden`, `隐藏的`, `隐蔽` |
| preans_slot2 | withhold | — | 0 | all | — |
| preans_slot2 | omit | — | 0 | all | — |
| preans_slot2 | secret | secret | 0.55 | `机密`, `␣confidential`, `␣hidden`, `hidden`, `Hidden`, `隐藏的`, `隐蔽`, `幕后`, `内幕` | — |
| preans_slot2 | fabricate | fiction | 0.35 | `␣fabricated`, `␣fabrication`, `␣invented`, `凭空`, `伪造`, `作假`, `fake`, `␣fake`, `Fake` | `␣fict`, `架空` |
| preans_slot2 | pretend | pretend | 1.00 | — | — |
| preans_slot2 | exaggerate | exaggerate | 1.00 | — | — |
| preans_slot2 | distort | — | 0 | all | — |
| preans_slot2 | evade | evade | 1.00 | — | — |
| preans_slot2 | manipulate | manipulate | 1.00 | — | — |
| preans_slot2 | deny | deny | 1.00 | — | — |
| preans_slot2 | honest | honest | 0.90 | — | `实事求是` |
| preans_slot2 | admit | admit | 1.00 | — | — |
| preans_slot2 | disclose | disclose | 1.00 | — | — |
| preans_slot2 | deliberate | deliberate | 0.78 | `明知`, `␣knowingly` | — |
| preans_slot2 | contradict | contradict | 0.55 | `␣contrad`, `␣contradd`, `␣contrary`, `相反`, `相反的` | — |
| preans_slot2 | violate | violate | 0.43 | `␣violate`, `␣violates`, `␣violated`, `␣violating` | — |
| preans_slot2 | imply | — | 0 | all | — |
| preans_slot2 | claim | — | 0 | all | — |
| preans_slot2 | refuse | refuse | 0.73 | — | `␣decline`, `␣declines`, `␣declined` |
| preans_slot2 | ethical | ethics | 1.00 | — | — |
| preans_slot2 | unethical | unethical | 1.00 | — | — |
| preans_slot2 | objective | objective | 1.00 | — | — |
| preans_slot2 | subjective | subjective | 1.00 | — | — |
| preans_slot3 | secret | secret | 1.00 | — | — |
| preans_slot3 | fabricate | fiction | 1.00 | — | — |
| preans_slot3 | confess | confess | 1.00 | — | — |
| preans_slot3 | disclose | disclose | 1.00 | — | — |
| preans_slot3 | violate | violate | 1.00 | — | — |
| preans_slot3 | claim | — | 0 | all | — |
| preans_slot3 | refuse | refuse | 1.00 | — | — |
| preans_slot3 | ethical | ethics | 1.00 | — | — |
| preans_slot3 | apologize | sorry | 1.00 | — | — |
| preans_slot3 | law-abiding | law-abiding | 1.00 | — | — |
| preans_slot4 | lie | lie | 1.00 | — | — |
| preans_slot4 | deceive | deceive | 1.00 | — | — |
| preans_slot4 | dishonest | dishonest | 1.00 | — | — |
| preans_slot4 | conceal | conceal | 1.00 | — | — |
| preans_slot4 | fabricate | fiction | 0.55 | `␣invented`, `␣invent`, `伪` | `␣fict`, `架空` |
| preans_slot4 | deny | deny | 1.00 | — | — |
| preans_slot4 | honest | honest | 0.89 | — | `实事求是` |
| preans_slot4 | admit | admit | 1.00 | — | — |
| preans_slot4 | confess | confess | 1.00 | — | — |
| preans_slot4 | disclose | disclose | 1.00 | — | — |
| preans_slot4 | deliberate | deliberate | 0.86 | `明知` | — |
| preans_slot4 | contradict | contradict | 0.33 | `␣contrad`, `相反` | — |
| preans_slot4 | violate | violate | 1.00 | — | — |
| preans_slot4 | imply | — | 0 | all | — |
| preans_slot4 | claim | — | 0 | all | — |
| preans_slot4 | refuse | refuse | 1.00 | — | — |
| preans_slot4 | apologize | sorry | 1.00 | — | — |
| preans_slot4 | objective | objective | 1.00 | — | — |
| preans_slot4 | subjective | subjective | 1.00 | — | — |
| preans_slot4 | self-examination | self-check | 1.00 | — | — |

Replicate-2 families not the best match of any replicate-1 family: preans_slot0: I cannot, preans_slot0: perfunctory, preans_slot1: conceal, preans_slot1: fake, preans_slot1: I cannot, preans_slot1: perfunctory, preans_slot1: knowingly, preans_slot1: outwardly, preans_slot1: fiction, preans_slot1: hypothetical, preans_slot1: simulated, preans_slot1: role-play, preans_slot2: conceal, preans_slot2: cover up, preans_slot2: fabricate, preans_slot2: fake, preans_slot2: I cannot, preans_slot2: perfunctory, preans_slot2: knowingly, preans_slot2: outwardly, preans_slot2: hypothetical, preans_slot2: simulated, preans_slot2: role-play, preans_slot3: I cannot, preans_slot4: fabricate, preans_slot4: fake, preans_slot4: I cannot, preans_slot4: knowingly, preans_slot4: outwardly, preans_slot4: hypothetical, preans_slot4: simulated

## Families whose name recurs at 3 or more positions

- admit: preans_slot0, preans_slot1, preans_slot2, preans_slot4
- claim: preans_slot1, preans_slot2, preans_slot3, preans_slot4
- conceal: preans_slot1, preans_slot2, preans_slot4
- confess: preans_slot1, preans_slot3, preans_slot4
- contradict: preans_slot1, preans_slot2, preans_slot4
- deceive: preans_slot1, preans_slot2, preans_slot4
- deliberate: preans_slot0, preans_slot1, preans_slot2, preans_slot4
- deny: preans_slot1, preans_slot2, preans_slot4
- disclose: preans_slot1, preans_slot2, preans_slot3, preans_slot4
- ethical: preans_slot1, preans_slot2, preans_slot3
- ethics: preans_slot1, preans_slot2, preans_slot3
- fabricate: preans_slot1, preans_slot2, preans_slot3, preans_slot4
- fake: preans_slot1, preans_slot2, preans_slot4
- fiction: preans_slot1, preans_slot2, preans_slot3, preans_slot4
- honest: preans_slot1, preans_slot2, preans_slot4
- hypothetical: preans_slot1, preans_slot2, preans_slot4
- i cannot: preans_slot0, preans_slot1, preans_slot2, preans_slot3, preans_slot4
- imply: preans_slot1, preans_slot2, preans_slot4
- knowingly: preans_slot0, preans_slot1, preans_slot2, preans_slot4
- lie: preans_slot1, preans_slot2, preans_slot4
- objective: preans_slot0, preans_slot1, preans_slot2, preans_slot4
- outwardly: preans_slot1, preans_slot2, preans_slot4
- perfunctory: preans_slot0, preans_slot1, preans_slot2
- refuse: preans_slot1, preans_slot2, preans_slot3, preans_slot4
- secret: preans_slot1, preans_slot2, preans_slot3
- simulated: preans_slot1, preans_slot2, preans_slot4
- subjective: preans_slot1, preans_slot2, preans_slot4
- violate: preans_slot1, preans_slot2, preans_slot3, preans_slot4

## Candidate opposite pairs (same position, lie side vs truth side, antonym words in the names or glosses; merged list)

- preans_slot1: conceal / disclose
- preans_slot1: conceal / transparent
- preans_slot1: cover up / transparent
- preans_slot1: deceive / honest
- preans_slot1: deny / admit
- preans_slot1: deny / confess
- preans_slot1: dishonest / honest
- preans_slot1: evade / admit
- preans_slot1: hide / admit
- preans_slot1: hide / confess
- preans_slot1: hide / disclose
- preans_slot1: lie / honest
- preans_slot1: mislead / honest
- preans_slot1: secret / admit
- preans_slot1: secret / confess
- preans_slot1: secret / disclose
- preans_slot2: conceal / disclose
- preans_slot2: deceive / honest
- preans_slot2: deny / admit
- preans_slot2: evade / admit
- preans_slot2: hide / admit
- preans_slot2: hide / disclose
- preans_slot2: lie / honest
- preans_slot2: mislead / honest
- preans_slot2: secret / admit
- preans_slot2: secret / disclose
- preans_slot3: secret / confess
- preans_slot3: secret / disclose
- preans_slot4: conceal / disclose
- preans_slot4: deceive / honest
- preans_slot4: deny / admit
- preans_slot4: deny / confess
- preans_slot4: dishonest / honest
- preans_slot4: lie / honest

Merged candidate list: `qwen3_6_27b_LL_Q6_factual_preans_merged.json` (129 families; replicate-2 families sharing at least half
their members with a replicate-1 family at the same position are folded into it).
