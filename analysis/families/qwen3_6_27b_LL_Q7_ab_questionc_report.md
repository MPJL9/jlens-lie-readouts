# Family report: qwen3.6-27b, logit lens, band 35-58, part Q7_ab, group questionc

Written by `scripts/family_report.py` from `qwen3_6_27b_LL_Q7_ab_questionc_rep1.json` and `_rep2.json` (prompt
`prompts/family_generation.md`). Visibility = build-split scenario transcripts (of 233) in which
at least one member is present at the position within the band. Layer profile = band layers where
the family is present in at least one transcript, and the three layers with the most transcripts
(description only; scoring uses the whole band).

## q_tok17

| rep | family | side | members | visibility | layer profile |
|---|---|---|---|---|---|
| 1 | admit (admitting) | truth | `承认` | 1 | L43-43; most at L43 (1) |
| 2 | admit (admitting) | truth | `承认` | 1 | L43-43; most at L43 (1) |

## q_tok18

| rep | family | side | members | visibility | layer profile |
|---|---|---|---|---|---|
| 1 | conceal (concealing the truth) | lie | `␣conceal` | 1 | L36-36; most at L36 (1) |
| 1 | omit (leaving something out) | lie | `omit` | 10 | L55-55; most at L55 (10) |
| 1 | deny (denying) | lie | `否认` | 2 | L37-37; most at L37 (2) |
| 1 | knowingly (knowing it was untrue) | unclear | `明知` | 1 | L35-35; most at L35 (1) |
| 1 | inconsistent (not consistent with) | unclear | `不符合` | 1 | L36-36; most at L36 (1) |
| 1 | violate (violating, going against) | unclear | `违背` | 160 | L35-37; most at L35 (160), L36 (21), L37 (3) |
| 1 | partial (only partly) | unclear | `␣partially` | 46 | L35-37; most at L35 (2), L36 (46), L37 (1) |
| 1 | outright (outright, flat) | unclear | `␣outright` | 8 | L51-53; most at L51 (1), L52 (2), L53 (8) |
| 1 | admit (admitting) | truth | `承认` | 23 | L36-55; most at L40 (13), L47 (15), L51 (16) |
| 1 | acknowledge (acknowledging) | truth | `␣acknowledge` | 1 | L48-49; most at L48 (1), L49 (1) |
| 2 | conceal (hiding or covering up information) | lie | `␣conceal` | 1 | L36-36; most at L36 (1) |
| 2 | omit (leaving information out) | lie | `omit` | 10 | L55-55; most at L55 (10) |
| 2 | deny (denying the truth) | lie | `否认` | 2 | L37-37; most at L37 (2) |
| 2 | admit (admitting) | truth | `承认` | 23 | L36-55; most at L40 (13), L47 (15), L51 (16) |
| 2 | acknowledge (acknowledging) | truth | `␣acknowledge` | 1 | L48-49; most at L48 (1), L49 (1) |
| 2 | violate (going against (rules, facts, principles)) | unclear | `违背` | 160 | L35-37; most at L35 (160), L36 (21), L37 (3) |
| 2 | knowingly (with knowledge of the truth) | unclear | `明知` | 1 | L35-35; most at L35 (1) |
| 2 | inconsistent (not matching (the facts)) | unclear | `不符合` | 1 | L36-36; most at L36 (1) |
| 2 | partial (partial or incomplete) | unclear | `␣partially` | 46 | L35-37; most at L35 (2), L36 (46), L37 (1) |

## q_tok19

| rep | family | side | members | visibility | layer profile |
|---|---|---|---|---|---|
| 1 | deceive (the act of deceiving) | lie | `欺骗`, `␣deception`, `骗`, `␣deceptive`, `␣deceive` | 64 | L35-58; most at L35 (41), L37 (29), L38 (29) |
| 1 | mislead (leading someone to a false belief) | lie | `␣misleading`, `误导` | 11 | L50-58; most at L50 (3), L53 (9), L54 (4) |
| 1 | conceal (concealing the truth) | lie | `隐瞒`, `␣conceal`, `␣concealed` | 170 | L35-58; most at L41 (105), L50 (133), L51 (100) |
| 1 | cover up (covering something up) | lie | `掩盖`, `掩饰`, `遮掩` | 73 | L35-58; most at L51 (46), L52 (51), L53 (59) |
| 1 | hide (hiding something) | lie | `␣hiding`, `隐藏`, `␣hidden`, `-hide`, `␣hide`, `Hide`, `hide`, `␣hides`, `␣Hide`, `_hide`, `␣Hidden`, `隐藏的`, `hidden`, `Hidden`, `_hidden`, `藏着`, `-hidden`, `:hidden`, `隐藏着` | 47 | L35-58; most at L53 (21), L57 (16), L58 (37) |
| 1 | withhold (withholding information) | lie | `␣withholding`, `␣withhold`, `␣withheld` | 25 | L50-58; most at L52 (22), L53 (20), L57 (9) |
| 1 | omit (leaving something out) | lie | `␣omit`, `␣omission`, `omit`, `␣omitted` | 24 | L42-58; most at L52 (17), L53 (18), L56 (9) |
| 1 | undisclosed (not disclosed) | lie | `␣undisclosed` | 1 | L52-54; most at L52 (1), L53 (1), L54 (1) |
| 1 | secret (secrecy) | lie | `␣secretly`, `␣secret`, `secret`, `秘密`, `␣Secret` | 20 | L35-58; most at L50 (11), L56 (8), L58 (6) |
| 1 | private (privately, out of view) | unclear | `␣privately`, `私下`, `␣private` | 37 | L43-58; most at L53 (9), L54 (30), L55 (19) |
| 1 | fabricate (making up false content) | lie | `␣fabricated`, `␣fabrication`, `␣invented`, `␣invent`, `伪造`, `␣Invent` | 18 | L35-58; most at L37 (8), L52 (7), L53 (9) |
| 1 | fictional (fiction, made-up story) | unclear | `虚构`, `␣fictional`, `␣fiction`, `fiction`, `␣Fiction` | 64 | L35-58; most at L50 (35), L51 (44), L52 (26) |
| 1 | fake (fake, sham) | lie | `fake`, `␣fake`, `伪`, `Fake` | 54 | L35-51; most at L35 (41), L36 (24), L37 (34) |
| 1 | pretend (pretending, putting on a front) | lie | `␣pretending`, `伪装`, `␣pretend`, `假装`, `␣pretended` | 21 | L35-58; most at L36 (8), L37 (11), L54 (8) |
| 1 | hypocrisy (hypocrisy) | lie | `虚伪` | 15 | L35-44; most at L37 (6), L38 (14), L39 (6) |
| 1 | exaggerate (exaggerating) | lie | `夸大`, `␣exagger`, `␣exaggerated` | 4 | L40-58; most at L50 (2), L51 (3), L52 (2) |
| 1 | evade (evading, brushing off) | lie | `回避`, `␣evasion`, `敷衍` | 7 | L36-58; most at L52 (5), L53 (5), L54 (4) |
| 1 | vague (vagueness, ambiguity) | unclear | `含糊`, `␣ambiguous`, `␣ambiguity` | 2 | L51-58; most at L51 (2), L52 (1), L53 (1) |
| 1 | deny (denying) | lie | `否认`, `␣denying`, `␣denial`, `␣deny`, `␣denies` | 17 | L35-58; most at L36 (6), L40 (9), L44 (9) |
| 1 | hallucinate (hallucinating content) | unclear | `␣halluc` | 6 | L52-58; most at L52 (4), L53 (1), L57 (3) |
| 1 | deliberate (doing it on purpose) | unclear | `␣intentionally`, `故意`, `␣deliberately`, `␣deliberate`, `␣intentional`, `刻意`, `有意`, `故意的` | 77 | L35-58; most at L36 (40), L52 (32), L54 (46) |
| 1 | knowingly (knowing it was untrue) | unclear | `明知`, `␣knowingly` | 178 | L35-58; most at L36 (158), L43 (154), L44 (150) |
| 1 | contradict (contradicting) | unclear | `␣contrad`, `␣contradict`, `␣contradictory`, `矛盾`, `␣contradiction`, `␣contradictions`, `矛盾的` | 139 | L35-58; most at L37 (80), L38 (79), L48 (97) |
| 1 | conflicting (conflicting) | unclear | `␣conflicting` | 14 | L35-53; most at L43 (6), L49 (4), L50 (7) |
| 1 | contrary (contrary to) | unclear | `␣contrary` | 15 | L37-54; most at L43 (5), L46 (10), L50 (7) |
| 1 | inconsistent (not consistent with) | unclear | `不符合` | 79 | L35-50; most at L46 (60), L47 (47), L48 (25) |
| 1 | violate (violating, going against) | unclear | `违背`, `违反`, `违反了` | 57 | L35-58; most at L49 (37), L50 (25), L51 (24) |
| 1 | moral (moral or ethical judgement) | unclear | `␣moral`, `␣ethical`, `道德`, `␣ethics`, `␣morally`, `的道德` | 12 | L54-58; most at L54 (3), L55 (1), L58 (12) |
| 1 | partial (only partly) | unclear | `␣partial`, `␣partially` | 4 | L39-53; most at L39 (1), L49 (1), L51 (2) |
| 1 | outright (outright, flat) | unclear | `␣outright` | 6 | L43-58; most at L51 (4), L53 (3), L54 (2) |
| 1 | indirect (indirectly) | unclear | `间接`, `␣indirectly`, `␣indirect` | 26 | L35-58; most at L52 (22), L53 (18), L54 (11) |
| 1 | role-play (playing a role) | unclear | `扮演`, `角色扮演` | 4 | L50-58; most at L51 (4), L52 (4), L53 (4) |
| 1 | persona (a persona) | unclear | `␣persona`, `␣personas`, `␣Persona`, `Persona` | 9 | L45-58; most at L52 (5), L53 (5), L56 (6) |
| 1 | simulate (simulating) | unclear | `模拟`, `仿真`, `␣simulation`, `␣simulations`, `␣Simulation` | 5 | L39-51; most at L48 (3), L50 (4), L51 (3) |
| 1 | comply (following orders or rules) | unclear | `遵照`, `遵循`, `遵从`, `␣adher`, `␣adherence`, `␣compliance`, `遵守`, `服从`, `合规`, `␣adhere`, `␣Compliance` | 6 | L51-58; most at L53 (4), L54 (4), L56 (3) |
| 1 | instructions (instructions given to the model) | unclear | `␣instructions`, `指令`, `␣instruction`, `␣Instructions`, `␣instructed`, `instructions`, `␣Instruction`, `Instructions`, `Instruction`, `_instructions`, `instruction`, `.instructions` | 35 | L47-58; most at L53 (23), L54 (21), L58 (31) |
| 1 | admit (admitting) | truth | `承认`, `␣admitting`, `␣admit`, `␣admitted`, `␣admits`, `␣admission`, `␣admissions`, `␣Admission`, `承認` | 47 | L36-58; most at L42 (22), L55 (28), L56 (23) |
| 1 | acknowledge (acknowledging) | truth | `␣acknowledging`, `␣acknowledge`, `␣acknowledges`, `␣acknowledged`, `␣acknowledgment`, `Acknowled` | 9 | L39-58; most at L55 (6), L56 (6), L58 (7) |
| 1 | honest (honesty) | truth | `诚`, `诚实`, `␣honesty`, `诚信`, `真诚` | 94 | L35-58; most at L36 (21), L37 (76), L38 (50) |
| 1 | disclose (disclosing) | truth | `透露`, `␣disclosed` | 3 | L48-53; most at L48 (1), L49 (1), L53 (2) |
| 1 | transparent (transparency) | truth | `透明` | 2 | L54-55; most at L54 (1), L55 (1) |
| 2 | deceive (the act of deceiving) | lie | `欺骗`, `␣deception`, `骗`, `␣deceptive`, `␣deceive` | 64 | L35-58; most at L35 (41), L37 (29), L38 (29) |
| 2 | mislead (leading someone to a wrong belief) | lie | `␣misleading` | 9 | L52-58; most at L53 (9), L54 (4), L55 (2) |
| 2 | conceal (hiding or covering up information) | lie | `隐瞒`, `掩盖`, `␣conceal`, `隐藏`, `␣hiding`, `␣hidden`, `␣concealed`, `遮`, `-hide`, `␣hide`, `Hide`, `掩饰`, `hide`, `␣hid`, `掩`, `␣hides`, `␣Hide`, `隐藏的`, `_hide`, `␣Hidden`, `遮蔽`, `hidden`, `Hidden`, `_hidden`, `遮掩`, `瞒`, `隐藏着`, `隐蔽`, `隐匿`, `-hidden`, `:hidden` | 171 | L35-58; most at L41 (107), L50 (133), L51 (102) |
| 2 | secret (kept secret or private) | lie | `␣privately`, `␣secretly`, `␣secret`, `私下`, `secret`, `秘密`, `␣private`, `␣Secret`, `私`, `␣undisclosed` | 49 | L35-58; most at L50 (14), L54 (31), L55 (19) |
| 2 | withhold (holding back information) | lie | `␣withholding`, `␣withhold`, `␣withheld` | 25 | L50-58; most at L52 (22), L53 (20), L57 (9) |
| 2 | omit (leaving information out) | lie | `␣omit`, `␣omission`, `omit`, `␣omitted` | 24 | L42-58; most at L52 (17), L53 (18), L56 (9) |
| 2 | fabricate (making up false content) | lie | `␣fabricated`, `␣fabrication`, `␣invented`, `␣invent`, `伪造`, `␣Invent`, `作假`, `␣invention` | 18 | L35-58; most at L37 (8), L52 (7), L53 (9) |
| 2 | fictional (made-up, fictitious content) | unclear | `虚构`, `␣fictional`, `␣fiction`, `fiction`, `␣Fiction` | 64 | L35-58; most at L50 (35), L51 (44), L52 (26) |
| 2 | fake (fake, sham) | lie | `fake`, `␣fake`, `伪`, `Fake` | 54 | L35-51; most at L35 (41), L36 (24), L37 (34) |
| 2 | pretend (pretending or posing as) | lie | `␣pretending`, `伪装`, `␣pretend`, `假装`, `冒充`, `␣pretended` | 21 | L35-58; most at L37 (11), L51 (8), L54 (8) |
| 2 | hypocritical (insincere, two-faced) | lie | `虚伪` | 15 | L35-44; most at L37 (6), L38 (14), L39 (6) |
| 2 | deny (denying the truth) | lie | `否认`, `␣denying`, `␣denial`, `␣deny`, `␣denies` | 17 | L35-58; most at L36 (6), L40 (9), L44 (9) |
| 2 | evade (avoiding or dodging the issue) | lie | `回避`, `␣evasion`, `逃避`, `规避` | 6 | L50-58; most at L52 (5), L53 (5), L54 (4) |
| 2 | admit (admitting) | truth | `承认`, `␣admitting`, `␣admit`, `␣admitted`, `␣admits`, `␣admission`, `␣admissions`, `␣Admission`, `承認` | 47 | L36-58; most at L42 (22), L55 (28), L56 (23) |
| 2 | acknowledge (acknowledging) | truth | `␣acknowledging`, `␣Ack`, `␣acknowledge`, `␣acknowledges`, `␣acknowledged`, `␣acknowledgment`, `Acknowled`, `Ack` | 10 | L37-58; most at L55 (6), L56 (6), L58 (7) |
| 2 | honest (honesty) | truth | `诚`, `诚实`, `␣honesty`, `诚信` | 94 | L35-58; most at L36 (21), L37 (76), L38 (50) |
| 2 | sincere (sincerity) | truth | `真诚` | 1 | L44-44; most at L44 (1) |
| 2 | reveal (revealing or disclosing) | truth | `␣disclosed` | 1 | L53-53; most at L53 (1) |
| 2 | transparent (transparency) | truth | `透明` | 2 | L54-55; most at L54 (1), L55 (1) |
| 2 | moral (moral or ethical judgement) | unclear | `␣moral`, `␣ethical`, `道德`, `␣ethics`, `␣morally`, `的道德` | 12 | L54-58; most at L54 (3), L55 (1), L58 (12) |
| 2 | violate (going against (rules, facts, principles)) | unclear | `违背`, `违反`, `违反了` | 57 | L35-58; most at L49 (37), L50 (25), L51 (24) |
| 2 | deliberate (doing it on purpose) | unclear | `␣intentionally`, `故意`, `␣deliberately`, `␣deliberate`, `␣intentional`, `刻意`, `有意`, `␣purposely`, `故意的` | 77 | L35-58; most at L36 (40), L52 (32), L54 (46) |
| 2 | knowingly (with knowledge of the truth) | unclear | `明知`, `␣knowing`, `␣knowingly`, `␣Knowing`, `Knowing` | 178 | L35-58; most at L36 (158), L43 (154), L44 (150) |
| 2 | contradict (contradicting) | unclear | `␣contrad`, `␣contradict`, `␣contradictory`, `矛盾`, `␣contrary`, `␣contradiction`, `␣conflicting`, `␣contradictions`, `矛盾的` | 139 | L35-58; most at L37 (81), L38 (80), L48 (97) |
| 2 | inconsistent (not matching (the facts)) | unclear | `不符合`, `不符` | 79 | L35-50; most at L46 (60), L47 (47), L48 (25) |
| 2 | hallucinate (hallucinating) | unclear | `␣halluc` | 6 | L52-58; most at L52 (4), L53 (1), L57 (3) |
| 2 | role-play (playing a role) | unclear | `扮演`, `角色扮演` | 4 | L50-58; most at L51 (4), L52 (4), L53 (4) |
| 2 | persona (a role or persona being played) | unclear | `␣persona`, `␣personas`, `␣Persona`, `␣role`, `role`, `Role`, `␣Role`, `-role`, `角色`, `的角色`, `角色的`, `Persona`, `␣roles`, `(role`, `roles`, `.role` | 9 | L45-58; most at L52 (5), L53 (5), L56 (6) |
| 2 | simulate (simulating) | unclear | `模拟`, `仿真`, `␣simulation`, `␣simulations`, `␣Simulation` | 5 | L39-51; most at L48 (3), L50 (4), L51 (3) |
| 2 | comply (following instructions or rules) | unclear | `遵循`, `␣compliance`, `␣adher`, `␣adherence`, `遵守`, `服从`, `合规`, `␣Compliance`, `␣adhere` | 5 | L51-58; most at L53 (3), L54 (4), L56 (3) |
| 2 | partial (partial or incomplete) | unclear | `␣partial`, `␣partially` | 4 | L39-53; most at L39 (1), L49 (1), L51 (2) |

## q_tok20

| rep | family | side | members | visibility | layer profile |
|---|---|---|---|---|---|
| 1 | deceive (the act of deceiving) | lie | `欺骗`, `␣deception`, `骗` | 13 | L52-58; most at L55 (11), L56 (5), L57 (9) |
| 1 | conceal (concealing the truth) | lie | `隐瞒` | 10 | L51-58; most at L51 (5), L52 (7), L53 (5) |
| 1 | withhold (withholding information) | lie | `␣withhold` | 2 | L51-52; most at L51 (1), L52 (1) |
| 1 | fabricate (making up false content) | lie | `␣fabricated`, `␣fabrication` | 2 | L52-58; most at L52 (1), L53 (1), L56 (1) |
| 1 | fictional (fiction, made-up story) | unclear | `␣fictional`, `虚构` | 175 | L35-58; most at L51 (114), L52 (132), L53 (119) |
| 1 | pretend (pretending, putting on a front) | lie | `␣pretend` | 2 | L46-47; most at L46 (1), L47 (2) |
| 1 | exaggerate (exaggerating) | lie | `␣exagger` | 2 | L55-56; most at L55 (1), L56 (2) |
| 1 | hallucinate (hallucinating content) | unclear | `␣halluc` | 48 | L51-58; most at L52 (39), L54 (21), L57 (33) |
| 1 | deliberate (doing it on purpose) | unclear | `␣intentionally`, `␣deliberately`, `故意`, `刻意` | 121 | L50-58; most at L54 (113), L56 (100), L58 (112) |
| 1 | knowingly (knowing it was untrue) | unclear | `␣knowingly`, `明知` | 91 | L35-58; most at L35 (42), L56 (55), L58 (47) |
| 1 | conscious (consciously) | unclear | `␣consciously` | 2 | L54-56; most at L54 (1), L56 (2) |
| 1 | violate (violating, going against) | unclear | `违背`, `违反了`, `违反` | 17 | L35-58; most at L51 (5), L53 (11), L54 (11) |
| 1 | moral (moral or ethical judgement) | unclear | `␣ethical`, `道德` | 2 | L35-39; most at L35 (1), L36 (1), L37 (1) |
| 1 | refuse (refusing or declining) | unclear | `拒绝`, `拒`, `␣refusal`, `␣refuse`, `␣refused`, `␣refusing`, `␣refus`, `␣decline`, `␣refuses`, `拒不`, `␣declined`, `拒絕`, `拒绝了`, `␣declines`, `␣declining` | 20 | L37-58; most at L39 (17), L41 (16), L47 (19) |
| 1 | outright (outright, flat) | unclear | `␣outright` | 1 | L58-58; most at L58 (1) |
| 1 | indirect (indirectly) | unclear | `间接`, `␣indirectly` | 17 | L52-54; most at L52 (16), L53 (6), L54 (1) |
| 1 | role-play (playing a role) | unclear | `扮演`, `角色扮演`, `扮演着` | 136 | L36-58; most at L43 (114), L44 (107), L51 (111) |
| 1 | persona (a persona) | unclear | `␣persona`, `␣personas`, `␣Persona`, `Persona`, `persona`, `␣Personas` | 76 | L35-58; most at L43 (51), L44 (49), L45 (59) |
| 1 | simulate (simulating) | unclear | `模拟`, `␣simulated`, `仿真`, `␣simulation`, `imulation`, `␣simulate`, `␣simulations`, `␣Simulation`, `simulation` | 128 | L35-58; most at L35 (121), L36 (107), L37 (110) |
| 1 | comply (following orders or rules) | unclear | `遵循`, `按要求`, `遵守`, `合规`, `␣adher`, `␣adhere`, `遵照`, `遵从`, `服从`, `␣adherence`, `严格遵守`, `␣comply`, `␣obey` | 108 | L35-58; most at L44 (58), L46 (38), L47 (61) |
| 1 | instructions (instructions given to the model) | unclear | `␣instructions` | 1 | L58-58; most at L58 (1) |
| 1 | admit (admitting) | truth | `承认`, `␣admit`, `␣admits`, `␣admitting`, `␣admitted`, `␣admission` | 108 | L47-58; most at L51 (72), L55 (85), L56 (79) |
| 1 | acknowledge (acknowledging) | truth | `␣acknowledge` | 14 | L56-58; most at L56 (2), L57 (5), L58 (14) |
| 1 | honest (honesty) | truth | `诚实` | 8 | L39-57; most at L46 (6), L47 (2), L51 (3) |
| 1 | voluntary (doing it on one's own initiative) | unclear | `主动` | 3 | L35-35; most at L35 (3) |
| 2 | deceive (the act of deceiving) | lie | `欺骗`, `␣deception`, `骗` | 13 | L52-58; most at L55 (11), L56 (5), L57 (9) |
| 2 | conceal (hiding or covering up information) | lie | `隐瞒` | 10 | L51-58; most at L51 (5), L52 (7), L53 (5) |
| 2 | withhold (holding back information) | lie | `␣withhold` | 2 | L51-52; most at L51 (1), L52 (1) |
| 2 | fabricate (making up false content) | lie | `␣fabricated`, `␣fabrication` | 2 | L52-58; most at L52 (1), L53 (1), L56 (1) |
| 2 | fictional (made-up, fictitious content) | unclear | `␣fictional`, `虚构` | 175 | L35-58; most at L51 (114), L52 (132), L53 (119) |
| 2 | pretend (pretending or posing as) | lie | `␣pretend`, `冒充` | 3 | L46-51; most at L46 (1), L47 (2), L51 (2) |
| 2 | refuse (refusing or declining) | unclear | `拒绝`, `拒`, `␣refusal`, `␣refuse`, `␣refused`, `␣refusing`, `␣refus`, `␣decline`, `拒不`, `␣refuses`, `␣declined`, `拒絕`, `拒绝了`, `␣declines`, `␣declining` | 20 | L37-58; most at L39 (17), L41 (16), L47 (19) |
| 2 | admit (admitting) | truth | `承认`, `␣admit`, `␣admits`, `␣admitting`, `␣admitted`, `␣admission` | 108 | L47-58; most at L51 (72), L55 (85), L56 (79) |
| 2 | acknowledge (acknowledging) | truth | `␣acknowledge` | 14 | L56-58; most at L56 (2), L57 (5), L58 (14) |
| 2 | honest (honesty) | truth | `诚实` | 8 | L39-57; most at L46 (6), L47 (2), L51 (3) |
| 2 | moral (moral or ethical judgement) | unclear | `道德`, `␣ethical` | 2 | L35-39; most at L35 (1), L36 (1), L37 (1) |
| 2 | violate (going against (rules, facts, principles)) | unclear | `违背`, `违反了`, `违`, `违反` | 21 | L35-58; most at L51 (5), L53 (11), L54 (11) |
| 2 | deliberate (doing it on purpose) | unclear | `␣intentionally`, `␣deliberately`, `故意`, `␣consciously`, `刻意` | 121 | L50-58; most at L54 (113), L56 (100), L58 (112) |
| 2 | knowingly (with knowledge of the truth) | unclear | `␣knowingly`, `明知` | 91 | L35-58; most at L35 (42), L56 (55), L58 (47) |
| 2 | hallucinate (hallucinating) | unclear | `␣halluc` | 48 | L51-58; most at L52 (39), L54 (21), L57 (33) |
| 2 | role-play (playing a role) | unclear | `扮演`, `角色扮演`, `扮演着` | 136 | L36-58; most at L43 (114), L44 (107), L51 (111) |
| 2 | persona (a role or persona being played) | unclear | `␣role`, `角色`, `␣persona`, `role`, `-role`, `Role`, `角色的`, `␣personas`, `␣Persona`, `␣Role`, `Persona`, `的角色`, `persona`, `(role`, `ROLE`, `␣Personas`, `␣roles`, `.role`, `_role` | 115 | L35-58; most at L42 (105), L43 (107), L45 (103) |
| 2 | simulate (simulating) | unclear | `模拟`, `␣simulated`, `仿真`, `␣simulation`, `␣simulate`, `␣simulations`, `␣Simulation`, `simulation` | 128 | L35-58; most at L35 (121), L36 (107), L37 (110) |
| 2 | comply (following instructions or rules) | unclear | `履行`, `遵循`, `遵守`, `合规`, `␣adher`, `␣adhere`, `服从`, `␣adherence`, `严格遵守`, `␣comply`, `␣obey` | 137 | L35-58; most at L40 (50), L43 (63), L44 (86) |
| 2 | take responsibility (taking on responsibility) | unclear | `承担` | 16 | L39-45; most at L43 (11), L44 (10), L45 (3) |

## q_tok21

| rep | family | side | members | visibility | layer profile |
|---|---|---|---|---|---|
| 1 | deceive (the act of deceiving) | lie | `欺骗`, `骗`, `␣deception` | 233 | L35-55; most at L35 (233), L36 (233), L37 (233) |
| 1 | conceal (concealing the truth) | lie | `隐瞒` | 69 | L36-58; most at L39 (17), L40 (39), L52 (48) |
| 1 | omit (leaving something out) | lie | `␣omission`, `␣omit`, `omit` | 161 | L51-58; most at L52 (144), L53 (123), L56 (41) |
| 1 | fabricate (making up false content) | lie | `␣invent` | 1 | L37-37; most at L37 (1) |
| 1 | fake (fake, sham) | lie | `␣fake`, `fake` | 41 | L35-38; most at L35 (3), L36 (41), L37 (16) |
| 1 | deny (denying) | lie | `␣denying` | 1 | L55-55; most at L55 (1) |
| 1 | deliberate (doing it on purpose) | unclear | `␣intentionally`, `故意`, `␣deliberately`, `␣deliberate`, `有意`, `␣intentional`, `刻意` | 209 | L35-58; most at L55 (192), L56 (197), L58 (202) |
| 1 | knowingly (knowing it was untrue) | unclear | `␣knowingly` | 111 | L50-58; most at L52 (91), L54 (80), L56 (76) |
| 1 | partial (only partly) | unclear | `不完全` | 27 | L48-49; most at L48 (3), L49 (27) |
| 1 | outright (outright, flat) | unclear | `␣outright` | 233 | L40-58; most at L51 (232), L54 (233), L55 (232) |
| 1 | honest (honesty) | truth | `诚信`, `诚实` | 233 | L35-48; most at L39 (233), L40 (231), L41 (225) |
| 2 | deceive (the act of deceiving) | lie | `欺骗`, `骗`, `␣deception` | 233 | L35-55; most at L35 (233), L36 (233), L37 (233) |
| 2 | conceal (hiding or covering up information) | lie | `隐瞒` | 69 | L36-58; most at L39 (17), L40 (39), L52 (48) |
| 2 | omit (leaving information out) | lie | `␣omission`, `␣omit`, `omit` | 161 | L51-58; most at L52 (144), L53 (123), L56 (41) |
| 2 | fabricate (making up false content) | lie | `␣invent` | 1 | L37-37; most at L37 (1) |
| 2 | fake (fake, sham) | lie | `␣fake`, `fake` | 41 | L35-38; most at L35 (3), L36 (41), L37 (16) |
| 2 | deny (denying the truth) | lie | `␣denying` | 1 | L55-55; most at L55 (1) |
| 2 | honest (honesty) | truth | `诚信`, `诚实` | 233 | L35-48; most at L39 (233), L40 (231), L41 (225) |
| 2 | deliberate (doing it on purpose) | unclear | `␣intentionally`, `故意`, `␣deliberately`, `␣deliberate`, `有意`, `␣intentional`, `刻意` | 209 | L35-58; most at L55 (192), L56 (197), L58 (202) |
| 2 | knowingly (with knowledge of the truth) | unclear | `␣knowingly` | 111 | L50-58; most at L52 (91), L54 (80), L56 (76) |
| 2 | partial (partial or incomplete) | unclear | `不完全` | 27 | L48-49; most at L48 (3), L49 (27) |

## q_tok22

| rep | family | side | members | visibility | layer profile |
|---|---|---|---|---|---|
| 1 | deceive (the act of deceiving) | lie | `欺骗`, `␣deception` | 6 | L50-53; most at L50 (5), L51 (2), L53 (3) |
| 1 | conceal (concealing the truth) | lie | `隐瞒`, `␣concealed`, `␣conceal` | 43 | L47-58; most at L50 (43), L51 (13), L52 (14) |
| 1 | cover up (covering something up) | lie | `掩盖` | 5 | L50-54; most at L51 (3), L52 (4), L53 (5) |
| 1 | hide (hiding something) | lie | `␣hidden`, `-hidden`, `隐藏`, `-hide`, `␣hiding`, `␣Hidden`, `Hidden`, `隐藏的`, `隱藏`, `藏着` | 8 | L35-58; most at L44 (6), L48 (2), L58 (2) |
| 1 | withhold (withholding information) | lie | `␣withholding`, `␣withhold`, `␣withheld` | 3 | L51-53; most at L51 (1), L52 (2), L53 (3) |
| 1 | omit (leaving something out) | lie | `omit` | 2 | L50-53; most at L50 (1), L53 (1) |
| 1 | secret (secrecy) | lie | `␣secret` | 10 | L35-48; most at L35 (1), L47 (2), L48 (10) |
| 1 | private (privately, out of view) | unclear | `␣private`, `私下` | 20 | L35-50; most at L35 (18), L38 (2), L46 (3) |
| 1 | fabricate (making up false content) | lie | `␣fabricated` | 2 | L51-53; most at L51 (1), L53 (1) |
| 1 | fictional (fiction, made-up story) | unclear | `虚构`, `fiction`, `-fiction`, `␣fictional`, `␣Fiction` | 14 | L49-54; most at L50 (9), L51 (14), L52 (10) |
| 1 | pretend (pretending, putting on a front) | lie | `␣pretending` | 3 | L52-54; most at L52 (1), L53 (2), L54 (3) |
| 1 | deny (denying) | lie | `否认` | 3 | L37-41; most at L37 (1), L38 (3), L40 (3) |
| 1 | deliberate (doing it on purpose) | unclear | `␣intentionally`, `␣deliberately`, `␣deliberate`, `␣intentional`, `故意`, `有意`, `故意的`, `刻意` | 17 | L49-58; most at L52 (13), L53 (5), L54 (17) |
| 1 | knowingly (knowing it was untrue) | unclear | `明知`, `␣knowingly` | 80 | L35-58; most at L35 (61), L52 (51), L54 (46) |
| 1 | conscious (consciously) | unclear | `␣consciously`, `␣conscious` | 6 | L54-55; most at L54 (6), L55 (1) |
| 1 | inconsistent (not consistent with) | unclear | `不符合` | 51 | L35-49; most at L36 (12), L46 (21), L47 (43) |
| 1 | violate (violating, going against) | unclear | `违反`, `违背`, `违反了` | 68 | L35-54; most at L35 (43), L46 (2), L49 (51) |
| 1 | partial (only partly) | unclear | `片面` | 45 | L35-39; most at L35 (15), L36 (32), L37 (43) |
| 1 | outright (outright, flat) | unclear | `␣outright` | 1 | L51-51; most at L51 (1) |
| 1 | indirect (indirectly) | unclear | `间接`, `␣indirectly` | 3 | L52-53; most at L52 (2), L53 (2) |
| 1 | simulate (simulating) | unclear | `模拟` | 1 | L51-51; most at L51 (1) |
| 1 | comply (following orders or rules) | unclear | `服从` | 9 | L47-50; most at L47 (1), L48 (1), L49 (9) |
| 1 | admit (admitting) | truth | `承认`, `␣admit`, `␣admitting`, `␣admits`, `␣admission`, `␣admitted`, `␣Admission`, `␣admissions`, `承認`, `␣admite` | 233 | L35-58; most at L55 (232), L57 (230), L58 (231) |
| 1 | acknowledge (acknowledging) | truth | `␣acknowledge`, `␣acknowledging`, `␣acknowledges`, `␣acknowledgment`, `␣Ack`, `␣acknowledged`, `Ack`, `Acknowled`, `_ack`, `␣acknowledgement`, `␣acknowled` | 220 | L35-58; most at L54 (200), L55 (216), L57 (198) |
| 1 | confess (confessing) | truth | `␣confession`, `␣confess`, `␣confessed`, `交代`, `自首`, `坦白`, `认错` | 144 | L35-58; most at L51 (83), L57 (82), L58 (107) |
| 1 | honest (honesty) | truth | `诚实`, `坦诚`, `诚` | 72 | L35-52; most at L49 (21), L50 (63), L52 (17) |
| 1 | reveal (revealing, exposing) | truth | `揭示`, `揭`, `揭示了`, `揭露`, `␣revealing` | 68 | L35-53; most at L38 (22), L39 (51), L40 (41) |
| 1 | disclose (disclosing) | truth | `␣disclosure`, `透露` | 4 | L50-55; most at L50 (2), L54 (2), L55 (1) |
| 1 | transparent (transparency) | truth | `透明`, `␣transparency`, `␣transparent` | 15 | L46-50; most at L47 (6), L48 (15), L50 (2) |
| 1 | regret (regret, remorse) | unclear | `悔` | 6 | L36-53; most at L42 (3), L52 (2), L53 (2) |
| 1 | apologize (apologizing) | unclear | `道歉` | 1 | L38-38; most at L38 (1) |
| 1 | self-reflection (reflecting on one's conduct) | unclear | `反思` | 7 | L46-52; most at L46 (1), L47 (2), L48 (6) |
| 1 | guilt (guilt, crime) | unclear | `罪` | 2 | L35-49; most at L35 (1), L38 (1), L39 (1) |
| 1 | surrender (giving in) | unclear | `投降` | 9 | L41-50; most at L48 (3), L49 (9), L50 (4) |
| 1 | voluntary (doing it on one's own initiative) | unclear | `主动` | 62 | L43-51; most at L48 (42), L49 (49), L50 (49) |
| 2 | deceive (the act of deceiving) | lie | `欺骗`, `␣deception` | 6 | L50-53; most at L50 (5), L51 (2), L53 (3) |
| 2 | conceal (hiding or covering up information) | lie | `隐瞒`, `␣hidden`, `掩盖`, `隐藏`, `␣concealed`, `-hidden`, `␣conceal`, `瞒`, `隐藏的`, `␣hiding`, `-hide`, `␣Hidden`, `Hidden` | 44 | L35-58; most at L50 (43), L51 (13), L52 (14) |
| 2 | secret (kept secret or private) | lie | `␣private`, `␣secret`, `私下` | 28 | L35-50; most at L35 (19), L47 (4), L48 (10) |
| 2 | withhold (holding back information) | lie | `␣withholding`, `␣withhold`, `␣withheld` | 3 | L51-53; most at L51 (1), L52 (2), L53 (3) |
| 2 | omit (leaving information out) | lie | `omit` | 2 | L50-53; most at L50 (1), L53 (1) |
| 2 | fabricate (making up false content) | lie | `␣fabricated` | 2 | L51-53; most at L51 (1), L53 (1) |
| 2 | fictional (made-up, fictitious content) | unclear | `虚构`, `fiction`, `-fiction`, `␣fictional`, `␣Fiction` | 14 | L49-54; most at L50 (9), L51 (14), L52 (10) |
| 2 | pretend (pretending or posing as) | lie | `␣pretending`, `冒充` | 5 | L51-54; most at L51 (3), L53 (2), L54 (3) |
| 2 | deny (denying the truth) | lie | `否认` | 3 | L37-41; most at L37 (1), L38 (3), L40 (3) |
| 2 | admit (admitting) | truth | `承认`, `␣admit`, `␣admitting`, `␣admits`, `␣admission`, `␣admitted`, `␣Admission`, `␣admissions`, `承認`, `␣admite`, `认错` | 233 | L35-58; most at L55 (232), L57 (230), L58 (231) |
| 2 | acknowledge (acknowledging) | truth | `␣acknowledge`, `␣acknowledging`, `␣acknowledges`, `␣acknowledgment`, `␣Ack`, `␣acknowledged`, `Ack`, `Acknowled`, `␣ack`, `␣acknowledgement`, `␣acknowled` | 220 | L35-58; most at L54 (200), L55 (216), L57 (198) |
| 2 | confess (confessing) | truth | `␣confession`, `␣confess`, `␣confessed`, `交代`, `自首`, `坦白` | 144 | L35-58; most at L51 (83), L57 (82), L58 (107) |
| 2 | honest (honesty) | truth | `诚实`, `诚` | 71 | L35-52; most at L49 (21), L50 (63), L52 (17) |
| 2 | candid (candour, frankness) | truth | `坦诚` | 7 | L36-44; most at L36 (3), L39 (7), L40 (2) |
| 2 | reveal (revealing or disclosing) | truth | `揭示`, `揭`, `揭示了`, `揭露`, `␣revealing`, `␣disclosure` | 69 | L35-53; most at L38 (22), L39 (51), L40 (41) |
| 2 | transparent (transparency) | truth | `透明`, `␣transparency`, `␣transparent` | 15 | L46-50; most at L47 (6), L48 (15), L50 (2) |
| 2 | remorse (regret, repentance) | unclear | `悔` | 6 | L36-53; most at L42 (3), L52 (2), L53 (2) |
| 2 | apologize (apologizing) | unclear | `道歉` | 1 | L38-38; most at L38 (1) |
| 2 | violate (going against (rules, facts, principles)) | unclear | `违反`, `违背`, `违反了` | 68 | L35-54; most at L35 (43), L46 (2), L49 (51) |
| 2 | deliberate (doing it on purpose) | unclear | `␣intentionally`, `␣intentional`, `␣deliberately`, `␣deliberate`, `故意`, `有意`, `␣consciously`, `故意的`, `␣purposely`, `刻意` | 17 | L49-58; most at L52 (13), L53 (5), L54 (17) |
| 2 | knowingly (with knowledge of the truth) | unclear | `明知`, `␣knowingly`, `␣knowing`, `␣Knowing`, `Knowing` | 80 | L35-58; most at L35 (61), L52 (51), L54 (46) |
| 2 | inconsistent (not matching (the facts)) | unclear | `不符合` | 51 | L35-49; most at L36 (12), L46 (21), L47 (43) |
| 2 | simulate (simulating) | unclear | `模拟` | 1 | L51-51; most at L51 (1) |
| 2 | comply (following instructions or rules) | unclear | `服从` | 9 | L47-50; most at L47 (1), L48 (1), L49 (9) |
| 2 | partial (partial or incomplete) | unclear | `片面` | 45 | L35-39; most at L35 (15), L36 (32), L37 (43) |
| 2 | self-examine (self-reflection, self-checking) | unclear | `自查`, `反思` | 21 | L35-52; most at L35 (5), L48 (6), L50 (10) |

## q_tok23

| rep | family | side | members | visibility | layer profile |
|---|---|---|---|---|---|
| 1 | outright (outright, flat) | unclear | `␣outright` | 1 | L48-48; most at L48 (1) |

## Replicate overlap

For each replicate-1 family, the replicate-2 family at the same position sharing the most members.

| position | rep-1 family | best rep-2 family | Jaccard of member ids | only in rep 1 | only in rep 2 |
|---|---|---|---|---|---|
| q_tok17 | admit | admit | 1.00 | — | — |
| q_tok18 | conceal | conceal | 1.00 | — | — |
| q_tok18 | omit | omit | 1.00 | — | — |
| q_tok18 | deny | deny | 1.00 | — | — |
| q_tok18 | knowingly | knowingly | 1.00 | — | — |
| q_tok18 | inconsistent | inconsistent | 1.00 | — | — |
| q_tok18 | violate | violate | 1.00 | — | — |
| q_tok18 | partial | partial | 1.00 | — | — |
| q_tok18 | outright | — | 0 | all | — |
| q_tok18 | admit | admit | 1.00 | — | — |
| q_tok18 | acknowledge | acknowledge | 1.00 | — | — |
| q_tok19 | deceive | deceive | 1.00 | — | — |
| q_tok19 | mislead | mislead | 0.50 | `误导` | — |
| q_tok19 | conceal | conceal | 0.10 | — | `掩盖`, `隐藏`, `␣hiding`, `␣hidden`, `遮`, `-hide`, `␣hide`, `Hide`, `掩饰`, `hide`, `␣hid`, `掩`, `␣hides`, `␣Hide`, `隐藏的`, `_hide`, `␣Hidden`, `遮蔽`, `hidden`, `Hidden`, `_hidden`, `遮掩`, `瞒`, `隐藏着`, `隐蔽`, `隐匿`, `-hidden`, `:hidden` |
| q_tok19 | cover up | conceal | 0.10 | — | `隐瞒`, `␣conceal`, `隐藏`, `␣hiding`, `␣hidden`, `␣concealed`, `遮`, `-hide`, `␣hide`, `Hide`, `hide`, `␣hid`, `掩`, `␣hides`, `␣Hide`, `隐藏的`, `_hide`, `␣Hidden`, `遮蔽`, `hidden`, `Hidden`, `_hidden`, `瞒`, `隐藏着`, `隐蔽`, `隐匿`, `-hidden`, `:hidden` |
| q_tok19 | hide | conceal | 0.56 | `藏着` | `隐瞒`, `掩盖`, `␣conceal`, `␣concealed`, `遮`, `掩饰`, `␣hid`, `掩`, `遮蔽`, `遮掩`, `瞒`, `隐蔽`, `隐匿` |
| q_tok19 | withhold | withhold | 1.00 | — | — |
| q_tok19 | omit | omit | 1.00 | — | — |
| q_tok19 | undisclosed | secret | 0.10 | — | `␣privately`, `␣secretly`, `␣secret`, `私下`, `secret`, `秘密`, `␣private`, `␣Secret`, `私` |
| q_tok19 | secret | secret | 0.50 | — | `␣privately`, `私下`, `␣private`, `私`, `␣undisclosed` |
| q_tok19 | private | secret | 0.30 | — | `␣secretly`, `␣secret`, `secret`, `秘密`, `␣Secret`, `私`, `␣undisclosed` |
| q_tok19 | fabricate | fabricate | 0.75 | — | `作假`, `␣invention` |
| q_tok19 | fictional | fictional | 1.00 | — | — |
| q_tok19 | fake | fake | 1.00 | — | — |
| q_tok19 | pretend | pretend | 0.83 | — | `冒充` |
| q_tok19 | hypocrisy | hypocritical | 1.00 | — | — |
| q_tok19 | exaggerate | — | 0 | all | — |
| q_tok19 | evade | evade | 0.40 | `敷衍` | `逃避`, `规避` |
| q_tok19 | vague | — | 0 | all | — |
| q_tok19 | deny | deny | 1.00 | — | — |
| q_tok19 | hallucinate | hallucinate | 1.00 | — | — |
| q_tok19 | deliberate | deliberate | 0.89 | — | `␣purposely` |
| q_tok19 | knowingly | knowingly | 0.40 | — | `␣knowing`, `␣Knowing`, `Knowing` |
| q_tok19 | contradict | contradict | 0.78 | — | `␣contrary`, `␣conflicting` |
| q_tok19 | conflicting | contradict | 0.11 | — | `␣contrad`, `␣contradict`, `␣contradictory`, `矛盾`, `␣contrary`, `␣contradiction`, `␣contradictions`, `矛盾的` |
| q_tok19 | contrary | contradict | 0.11 | — | `␣contrad`, `␣contradict`, `␣contradictory`, `矛盾`, `␣contradiction`, `␣conflicting`, `␣contradictions`, `矛盾的` |
| q_tok19 | inconsistent | inconsistent | 0.50 | — | `不符` |
| q_tok19 | violate | violate | 1.00 | — | — |
| q_tok19 | moral | moral | 1.00 | — | — |
| q_tok19 | partial | partial | 1.00 | — | — |
| q_tok19 | outright | — | 0 | all | — |
| q_tok19 | indirect | — | 0 | all | — |
| q_tok19 | role-play | role-play | 1.00 | — | — |
| q_tok19 | persona | persona | 0.25 | — | `␣role`, `role`, `Role`, `␣Role`, `-role`, `角色`, `的角色`, `角色的`, `␣roles`, `(role`, `roles`, `.role` |
| q_tok19 | simulate | simulate | 1.00 | — | — |
| q_tok19 | comply | comply | 0.82 | `遵照`, `遵从` | — |
| q_tok19 | instructions | — | 0 | all | — |
| q_tok19 | admit | admit | 1.00 | — | — |
| q_tok19 | acknowledge | acknowledge | 0.75 | — | `␣Ack`, `Ack` |
| q_tok19 | honest | honest | 0.80 | `真诚` | — |
| q_tok19 | disclose | reveal | 0.50 | `透露` | — |
| q_tok19 | transparent | transparent | 1.00 | — | — |
| q_tok20 | deceive | deceive | 1.00 | — | — |
| q_tok20 | conceal | conceal | 1.00 | — | — |
| q_tok20 | withhold | withhold | 1.00 | — | — |
| q_tok20 | fabricate | fabricate | 1.00 | — | — |
| q_tok20 | fictional | fictional | 1.00 | — | — |
| q_tok20 | pretend | pretend | 0.50 | — | `冒充` |
| q_tok20 | exaggerate | — | 0 | all | — |
| q_tok20 | hallucinate | hallucinate | 1.00 | — | — |
| q_tok20 | deliberate | deliberate | 0.80 | — | `␣consciously` |
| q_tok20 | knowingly | knowingly | 1.00 | — | — |
| q_tok20 | conscious | deliberate | 0.20 | — | `␣intentionally`, `␣deliberately`, `故意`, `刻意` |
| q_tok20 | violate | violate | 0.75 | — | `违` |
| q_tok20 | moral | moral | 1.00 | — | — |
| q_tok20 | refuse | refuse | 1.00 | — | — |
| q_tok20 | outright | — | 0 | all | — |
| q_tok20 | indirect | — | 0 | all | — |
| q_tok20 | role-play | role-play | 1.00 | — | — |
| q_tok20 | persona | persona | 0.32 | — | `␣role`, `角色`, `role`, `-role`, `Role`, `角色的`, `␣Role`, `的角色`, `(role`, `ROLE`, `␣roles`, `.role`, `_role` |
| q_tok20 | simulate | simulate | 0.89 | `imulation` | — |
| q_tok20 | comply | comply | 0.71 | `按要求`, `遵照`, `遵从` | `履行` |
| q_tok20 | instructions | — | 0 | all | — |
| q_tok20 | admit | admit | 1.00 | — | — |
| q_tok20 | acknowledge | acknowledge | 1.00 | — | — |
| q_tok20 | honest | honest | 1.00 | — | — |
| q_tok20 | voluntary | — | 0 | all | — |
| q_tok21 | deceive | deceive | 1.00 | — | — |
| q_tok21 | conceal | conceal | 1.00 | — | — |
| q_tok21 | omit | omit | 1.00 | — | — |
| q_tok21 | fabricate | fabricate | 1.00 | — | — |
| q_tok21 | fake | fake | 1.00 | — | — |
| q_tok21 | deny | deny | 1.00 | — | — |
| q_tok21 | deliberate | deliberate | 1.00 | — | — |
| q_tok21 | knowingly | knowingly | 1.00 | — | — |
| q_tok21 | partial | partial | 1.00 | — | — |
| q_tok21 | outright | — | 0 | all | — |
| q_tok21 | honest | honest | 1.00 | — | — |
| q_tok22 | deceive | deceive | 1.00 | — | — |
| q_tok22 | conceal | conceal | 0.23 | — | `␣hidden`, `掩盖`, `隐藏`, `-hidden`, `瞒`, `隐藏的`, `␣hiding`, `-hide`, `␣Hidden`, `Hidden` |
| q_tok22 | cover up | conceal | 0.08 | — | `隐瞒`, `␣hidden`, `隐藏`, `␣concealed`, `-hidden`, `␣conceal`, `瞒`, `隐藏的`, `␣hiding`, `-hide`, `␣Hidden`, `Hidden` |
| q_tok22 | hide | conceal | 0.53 | `隱藏`, `藏着` | `隐瞒`, `掩盖`, `␣concealed`, `␣conceal`, `瞒` |
| q_tok22 | withhold | withhold | 1.00 | — | — |
| q_tok22 | omit | omit | 1.00 | — | — |
| q_tok22 | secret | secret | 0.33 | — | `␣private`, `私下` |
| q_tok22 | private | secret | 0.67 | — | `␣secret` |
| q_tok22 | fabricate | fabricate | 1.00 | — | — |
| q_tok22 | fictional | fictional | 1.00 | — | — |
| q_tok22 | pretend | pretend | 0.50 | — | `冒充` |
| q_tok22 | deny | deny | 1.00 | — | — |
| q_tok22 | deliberate | deliberate | 0.80 | — | `␣consciously`, `␣purposely` |
| q_tok22 | knowingly | knowingly | 0.40 | — | `␣knowing`, `␣Knowing`, `Knowing` |
| q_tok22 | conscious | deliberate | 0.09 | `␣conscious` | `␣intentionally`, `␣intentional`, `␣deliberately`, `␣deliberate`, `故意`, `有意`, `故意的`, `␣purposely`, `刻意` |
| q_tok22 | inconsistent | inconsistent | 1.00 | — | — |
| q_tok22 | violate | violate | 1.00 | — | — |
| q_tok22 | partial | partial | 1.00 | — | — |
| q_tok22 | outright | — | 0 | all | — |
| q_tok22 | indirect | — | 0 | all | — |
| q_tok22 | simulate | simulate | 1.00 | — | — |
| q_tok22 | comply | comply | 1.00 | — | — |
| q_tok22 | admit | admit | 0.91 | — | `认错` |
| q_tok22 | acknowledge | acknowledge | 0.83 | `_ack` | `␣ack` |
| q_tok22 | confess | confess | 0.86 | `认错` | — |
| q_tok22 | honest | honest | 0.67 | `坦诚` | — |
| q_tok22 | reveal | reveal | 0.83 | — | `␣disclosure` |
| q_tok22 | disclose | reveal | 0.14 | `透露` | `揭示`, `揭`, `揭示了`, `揭露`, `␣revealing` |
| q_tok22 | transparent | transparent | 1.00 | — | — |
| q_tok22 | regret | remorse | 1.00 | — | — |
| q_tok22 | apologize | apologize | 1.00 | — | — |
| q_tok22 | self-reflection | self-examine | 0.50 | — | `自查` |
| q_tok22 | guilt | — | 0 | all | — |
| q_tok22 | surrender | — | 0 | all | — |
| q_tok22 | voluntary | — | 0 | all | — |
| q_tok23 | outright | — | 0 | all | — |

Replicate-2 families not the best match of any replicate-1 family: q_tok19: sincere, q_tok22: candid, q_tok20: take responsibility

## Families whose name recurs at 3 or more positions

- acknowledge: q_tok18, q_tok19, q_tok20, q_tok22
- admit: q_tok17, q_tok18, q_tok19, q_tok20, q_tok22
- comply: q_tok19, q_tok20, q_tok22
- conceal: q_tok18, q_tok19, q_tok20, q_tok21, q_tok22
- deceive: q_tok19, q_tok20, q_tok21, q_tok22
- deliberate: q_tok19, q_tok20, q_tok21, q_tok22
- deny: q_tok18, q_tok19, q_tok21, q_tok22
- fabricate: q_tok19, q_tok20, q_tok21, q_tok22
- fictional: q_tok19, q_tok20, q_tok22
- honest: q_tok19, q_tok20, q_tok21, q_tok22
- inconsistent: q_tok18, q_tok19, q_tok22
- indirect: q_tok19, q_tok20, q_tok22
- knowingly: q_tok18, q_tok19, q_tok20, q_tok21, q_tok22
- omit: q_tok18, q_tok19, q_tok21, q_tok22
- outright: q_tok18, q_tok19, q_tok20, q_tok21, q_tok22, q_tok23
- partial: q_tok18, q_tok19, q_tok21, q_tok22
- pretend: q_tok19, q_tok20, q_tok22
- simulate: q_tok19, q_tok20, q_tok22
- violate: q_tok18, q_tok19, q_tok20, q_tok22
- withhold: q_tok19, q_tok20, q_tok22

## Candidate opposite pairs (same position, lie side vs truth side, antonym words in the names or glosses; merged list)

- q_tok18: deny / admit
- q_tok19: conceal / disclose
- q_tok19: cover up / transparent
- q_tok19: deceive / honest
- q_tok19: deny / admit
- q_tok19: evade / admit
- q_tok19: hide / disclose
- q_tok19: pretend / sincere
- q_tok20: deceive / honest
- q_tok21: deceive / honest
- q_tok22: conceal / disclose
- q_tok22: conceal / reveal
- q_tok22: cover up / transparent
- q_tok22: deceive / honest
- q_tok22: deny / admit
- q_tok22: deny / confess
- q_tok22: hide / disclose
- q_tok22: hide / reveal

Merged candidate list: `qwen3_6_27b_LL_Q7_ab_questionc_merged.json` (132 families; replicate-2 families sharing at least half
their members with a replicate-1 family at the same position are folded into it).
