# Family report: qwen3.6-27b, logit lens, band 35-58, part Q1_bare, group preans

Written by `scripts/family_report.py` from `qwen3_6_27b_LL_Q1_bare_preans_rep1.json` and `_rep2.json` (prompt
`prompts/family_generation.md`). Visibility = build-split scenario transcripts (of 233) in which
at least one member is present at the position within the band. Layer profile = band layers where
the family is present in at least one transcript, and the three layers with the most transcripts
(description only; scoring uses the whole band).

## preans_slot0

| rep | family | side | members | visibility | layer profile |
|---|---|---|---|---|---|
| 1 | truth (the truth (noun)) | truth | `␣truth` | 12 | L35-42; most at L40 (12), L41 (2), L42 (1) |
| 1 | honest (honest, truthful) | truth | `诚` | 5 | L40-41; most at L40 (5), L41 (2) |
| 1 | candid (candid, frank, speaking openly) | truth | `坦诚` | 5 | L36-43; most at L36 (1), L40 (5), L43 (2) |
| 1 | integrity (integrity, uprightness) | truth | `正直` | 3 | L35-40; most at L35 (2), L40 (1) |
| 1 | admit (admit) | truth | `承认` | 31 | L37-44; most at L39 (8), L40 (31), L41 (9) |
| 1 | acknowledge (acknowledge) | truth | `␣acknowledge` | 12 | L40-51; most at L40 (4), L44 (9), L48 (9) |
| 1 | clarify (clarify) | unclear | `␣clarification` | 1 | L46-46; most at L46 (1) |
| 1 | negate (negate, negative) | unclear | `否定` | 20 | L44-49; most at L46 (9), L47 (14), L48 (18) |
| 1 | knowingly (knowingly, knowing full well) | unclear | `明知` | 15 | L43-45; most at L43 (15), L44 (6), L45 (1) |
| 1 | ethics (ethics, morality) | unclear | `伦理` | 16 | L36-43; most at L36 (4), L39 (15), L40 (11) |
| 1 | self-reflection (self-examination, reflection) | unclear | `反思`, `自查`, `自省`, `自检`, `审视`, `␣reflection`, `␣reflective` | 151 | L35-58; most at L35 (93), L43 (65), L44 (100) |
| 1 | critique (critique, criticism) | unclear | `␣critique`, `指正`, `批判`, `␣critiques`, `批评`, `␣criticism` | 222 | L35-58; most at L52 (189), L53 (152), L58 (212) |
| 1 | accuse (accuse, accusation) | unclear | `指控`, `␣accus`, `␣accusation`, `␣accusations` | 6 | L43-58; most at L53 (6), L55 (6), L57 (6) |
| 2 | admit (admitting or acknowledging) | truth | `承认`, `␣acknowledge` | 32 | L37-51; most at L40 (31), L41 (9), L44 (10) |
| 2 | honest (honest; honesty) | truth | `诚` | 5 | L40-41; most at L40 (5), L41 (2) |
| 2 | candid / frank (speaking candidly or frankly) | truth | `坦诚`, `直言` | 9 | L35-43; most at L35 (4), L40 (5), L43 (2) |
| 2 | integrity (integrity; uprightness) | truth | `正直` | 3 | L35-40; most at L35 (2), L40 (1) |
| 2 | truth (the truth) | truth | `␣truth` | 12 | L35-42; most at L40 (12), L41 (2), L42 (1) |
| 2 | knowingly (knowing; knowingly) | unclear | `明知` | 15 | L43-45; most at L43 (15), L44 (6), L45 (1) |
| 2 | ethics (ethics; ethical) | unclear | `伦理` | 16 | L36-43; most at L36 (4), L39 (15), L40 (11) |
| 2 | accusation (accusing; an accusation) | unclear | `指控`, `␣accus`, `␣accusation`, `␣accusations` | 6 | L43-58; most at L53 (6), L55 (6), L57 (6) |
| 2 | clarify (clarifying; setting the record straight) | unclear | `␣clarification` | 1 | L46-46; most at L46 (1) |

## preans_slot1

| rep | family | side | members | visibility | layer profile |
|---|---|---|---|---|---|
| 1 | truth (the truth (noun)) | truth | `␣truth`, `truth`, `␣Truth`, `真相`, `Truth`, `实情`, `␣truths`, `_truth`, `真理` | 201 | L35-58; most at L35 (172), L39 (175), L40 (171) |
| 1 | honest (honest, truthful) | truth | `␣truthful`, `如实`, `实话`, `诚`, `诚实`, `␣honesty`, `␣honest`, `实事求是`, `诚信`, `说实话`, `␣honestly`, `␣Honest` | 211 | L35-58; most at L39 (167), L40 (159), L41 (158) |
| 1 | candid (candid, frank, speaking openly) | truth | `坦诚`, `坦白` | 19 | L37-58; most at L42 (12), L51 (10), L52 (10) |
| 1 | transparent (transparent, open) | truth | `透明`, `␣transparency`, `-transparent`, `␣transparent`, `␣Transparency`, `透明的`, `透明度` | 13 | L37-58; most at L47 (9), L48 (8), L54 (11) |
| 1 | integrity (integrity, uprightness) | truth | `正直` | 1 | L53-53; most at L53 (1) |
| 1 | admit (admit) | truth | `承认`, `␣admissions`, `␣admitting`, `␣admission`, `␣admit`, `␣admits`, `␣admitted`, `␣Admission`, `␣admite` | 43 | L35-58; most at L43 (21), L47 (25), L57 (22) |
| 1 | acknowledge (acknowledge) | truth | `␣acknowledging`, `␣acknowledge`, `␣acknowledges`, `␣acknowledged`, `␣acknowledgment` | 10 | L47-58; most at L53 (7), L55 (8), L57 (8) |
| 1 | confess (confess) | truth | `交代` | 1 | L35-36; most at L35 (1), L36 (1) |
| 1 | disclose (disclose, reveal) | truth | `信息披露`, `␣disclosure`, `␣disclosing`, `披露`, `␣revealing`, `␣disclose`, `␣disclosed`, `␣Disclosure`, `透露`, `␣reveal` | 18 | L35-58; most at L36 (9), L37 (9), L38 (15) |
| 1 | clarify (clarify) | unclear | `澄清`, `␣clarification`, `␣clarify`, `␣clarified` | 15 | L35-58; most at L37 (8), L52 (8), L53 (9) |
| 1 | lie (a lie, to lie) | lie | `谎言`, `撒谎`, `说谎`, `谎`, `␣lies`, `␣lie`, `␣lied`, `␣lying`, `lying`, `␣mentira`, `␣거짓`, `␣Lies`, `lie`, `␣Lie`, `lies` | 132 | L35-58; most at L39 (113), L40 (103), L41 (79) |
| 1 | conceal (conceal) | lie | `隐瞒`, `␣conceal`, `␣concealed` | 168 | L35-58; most at L40 (131), L50 (156), L52 (129) |
| 1 | hide (hide, hidden) | lie | `␣hiding`, `Hide`, `_hide`, `-hide`, `␣hide`, `hide`, `␣hides`, `隐藏`, `␣Hide`, `隐匿` | 15 | L39-58; most at L52 (7), L53 (11), L58 (8) |
| 1 | cover up (cover up, disguise a fault) | lie | `掩盖`, `掩饰`, `掩`, `遮盖`, `␣masking`, `遮住`, `遮掩`, `遮蔽`, `␣masked` | 133 | L35-58; most at L35 (84), L36 (103), L50 (92) |
| 1 | gloss over (gloss over) | lie | `␣gloss` | 40 | L36-58; most at L47 (25), L48 (30), L52 (20) |
| 1 | downplay (downplay) | lie | `淡化` | 59 | L35-58; most at L49 (30), L50 (51), L52 (30) |
| 1 | withhold (withhold information) | lie | `␣withholding`, `␣withhold`, `␣withheld` | 48 | L36-58; most at L51 (19), L52 (40), L53 (34) |
| 1 | omit (omit, leave out) | lie | `␣omit`, `␣omission`, `omit`, `省略`, `␣omitted`, `␣OMIT` | 60 | L36-58; most at L50 (43), L52 (47), L53 (39) |
| 1 | fabricate (fabricate, invent, make up) | lie | `虚构`, `␣fabricated`, `␣fabrication`, `凭空`, `␣invented`, `␣invent`, `伪造`, `␣invention` | 107 | L35-58; most at L36 (84), L37 (84), L46 (79) |
| 1 | fictional (fictional) | unclear | `␣fictional`, `fiction`, `␣fiction`, `-fiction` | 26 | L35-58; most at L38 (12), L44 (15), L45 (12) |
| 1 | fake (fake) | lie | `fake`, `␣fake`, `作假` | 44 | L35-46; most at L36 (27), L37 (35), L38 (35) |
| 1 | mislead (mislead) | lie | `␣misleading`, `误导`, `误导性` | 79 | L35-58; most at L50 (32), L53 (65), L54 (40) |
| 1 | misinformation (false information) | lie | `␣misinformation`, `虚假信息` | 51 | L36-58; most at L37 (19), L38 (16), L53 (34) |
| 1 | manipulate (manipulate) | lie | `␣manipulation`, `␣manipulated` | 1 | L50-50; most at L50 (1) |
| 1 | deny (deny, denial) | lie | `否认`, `␣denying`, `␣denial`, `␣deny`, `␣denies`, `␣denied`, `否認`, `deny`, `␣Denied` | 81 | L35-58; most at L52 (48), L55 (61), L56 (52) |
| 1 | negate (negate, negative) | unclear | `否定` | 58 | L35-58; most at L53 (29), L55 (32), L56 (27) |
| 1 | evade (evade, dodge) | lie | `回避`, `␣evasion`, `␣dodge`, `规避`, `␣evade`, `逃避` | 46 | L38-58; most at L51 (29), L52 (34), L53 (34) |
| 1 | vague (vague, ambiguous) | unclear | `␣vague`, `模糊`, `含糊`, `␣vaguely` | 36 | L36-58; most at L51 (24), L52 (24), L53 (27) |
| 1 | euphemistic (euphemistic, indirect wording) | unclear | `委婉` | 23 | L35-51; most at L35 (16), L36 (10), L40 (14) |
| 1 | perfunctory (deal with perfunctorily) | unclear | `应付` | 74 | L35-50; most at L35 (46), L36 (48), L37 (57) |
| 1 | deliberate (deliberately, intentionally) | unclear | `故意`, `␣deliberately`, `␣intentionally`, `刻意`, `␣deliberate`, `␣intentional` | 111 | L35-58; most at L36 (90), L52 (39), L54 (44) |
| 1 | knowingly (knowingly, knowing full well) | unclear | `明知`, `␣knowingly` | 170 | L35-58; most at L43 (137), L44 (142), L45 (138) |
| 1 | contradict (contradict, contradiction) | unclear | `␣contradict`, `␣contrad`, `矛盾`, `␣contradiction`, `␣contradictory`, `␣contradictions`, `␣contradd`, `矛盾的` | 73 | L35-58; most at L49 (56), L50 (46), L54 (45) |
| 1 | violate (violate, go against (a principle)) | unclear | `违背`, `违反`, `违反了` | 43 | L35-58; most at L48 (25), L49 (43), L50 (24) |
| 1 | imply (imply, implicit) | unclear | `暗示`, `␣implying`, `␣imply`, `␣implied`, `隐含`, `␣implies`, `␣implicitly`, `␣implication`, `␣implicit`, `␣implic`, `␣implications`, `␣implica`, `␣implique` | 43 | L35-58; most at L45 (20), L54 (33), L55 (17) |
| 1 | technically (technically (true)) | unclear | `␣technically` | 31 | L36-58; most at L55 (27), L56 (24), L58 (17) |
| 1 | superficially (on the surface, seemingly) | unclear | `表面上`, `看似` | 47 | L35-50; most at L36 (16), L37 (14), L38 (25) |
| 1 | ethics (ethics, morality) | unclear | `␣ethical`, `␣ethics`, `伦理`, `道德` | 5 | L39-58; most at L39 (1), L52 (3), L53 (3) |
| 1 | good faith (good intention) | unclear | `善意` | 1 | L35-37; most at L35 (1), L36 (1), L37 (1) |
| 1 | decline (decline (to answer)) | unclear | `␣decline`, `␣declining`, `␣declined`, `␣declines` | 18 | L55-58; most at L55 (17), L56 (16), L57 (16) |
| 1 | refuse (refuse) | unclear | `␣refusal`, `拒绝`, `␣refused`, `␣refuse`, `␣refusing`, `␣refuses`, `␣refus`, `拒`, `␣отказ`, `拒絕`, `拒绝了`, `␣отказа`, `拒不` | 31 | L36-58; most at L55 (27), L56 (27), L57 (27) |
| 2 | lie (a lie; lying) | lie | `谎言`, `撒谎`, `说谎`, `谎`, `␣lies`, `␣lie`, `␣lied`, `␣lying`, `lying`, `␣mentira`, `␣거짓`, `␣liar`, `␣Lies`, `lie`, `lies`, `␣Lie` | 132 | L35-58; most at L39 (113), L40 (103), L41 (79) |
| 2 | conceal (concealing the truth from someone) | lie | `隐瞒`, `␣conceal`, `瞒`, `␣concealed` | 168 | L35-58; most at L40 (131), L50 (156), L52 (129) |
| 2 | hide (hiding; hidden) | lie | `␣hiding`, `Hide`, `_hide`, `-hide`, `␣hide`, `␣hides`, `hide`, `隐藏`, `␣Hide`, `隐匿` | 15 | L39-58; most at L52 (7), L53 (11), L58 (8) |
| 2 | cover up (covering up or masking something) | lie | `掩盖`, `掩饰`, `遮`, `掩`, `遮盖`, `␣masking`, `遮住`, `遮掩`, `掩护`, `遮蔽`, `␣masked` | 138 | L35-58; most at L35 (87), L36 (108), L50 (93) |
| 2 | gloss over / downplay (making something seem smaller or smoother than it is) | lie | `淡化`, `␣gloss` | 73 | L35-58; most at L48 (39), L49 (36), L50 (57) |
| 2 | euphemism (saying something indirectly or tactfully) | unclear | `委婉` | 23 | L35-51; most at L35 (16), L36 (10), L40 (14) |
| 2 | fabricate (making something up) | lie | `虚构`, `␣fabricated`, `␣fabrication`, `凭空`, `␣invented`, `␣invent`, `伪造`, `␣invention`, `作假` | 107 | L35-58; most at L36 (84), L37 (84), L46 (79) |
| 2 | fake (fake) | lie | `fake`, `␣fake` | 43 | L35-46; most at L36 (26), L37 (35), L38 (35) |
| 2 | fictional (fictional, invented as a story) | unclear | `␣fictional`, `fiction`, `␣fiction`, `-fiction` | 26 | L35-58; most at L38 (12), L44 (15), L45 (12) |
| 2 | mislead (misleading someone) | lie | `␣misleading`, `误导`, `误导性`, `␣misled` | 79 | L35-58; most at L50 (32), L53 (65), L54 (40) |
| 2 | misinformation (false information) | lie | `␣misinformation`, `虚假信息` | 51 | L36-58; most at L37 (19), L38 (16), L53 (34) |
| 2 | manipulate (manipulating someone) | lie | `␣manipulation`, `␣manipulated` | 1 | L50-50; most at L50 (1) |
| 2 | deny (denying something) | lie | `否认`, `␣denying`, `␣denial`, `␣deny`, `␣denies`, `␣denied`, `否認`, `deny`, `␣Denied` | 81 | L35-58; most at L52 (48), L55 (61), L56 (52) |
| 2 | refuse (refusing or declining) | unclear | `␣refusal`, `拒绝`, `␣refused`, `␣refuse`, `␣refusing`, `␣refuses`, `␣refus`, `拒`, `␣отказ`, `拒絕`, `拒绝了`, `␣decline`, `␣declining`, `␣отказа`, `␣declined`, `␣declines`, `拒不` | 31 | L36-58; most at L55 (27), L56 (27), L57 (27) |
| 2 | evade (evading or dodging) | lie | `回避`, `␣evasion`, `␣dodge`, `␣evade` | 46 | L38-58; most at L51 (29), L52 (34), L53 (34) |
| 2 | vague (vague or ambiguous) | unclear | `␣vague`, `模糊`, `含糊`, `␣ambiguity`, `␣ambiguous`, `␣vaguely`, `ambiguous` | 38 | L36-58; most at L51 (25), L52 (24), L53 (28) |
| 2 | omit (leaving something out) | lie | `␣omit`, `␣omission`, `omit`, `省略`, `␣omitted`, `␣OMIT` | 60 | L36-58; most at L50 (43), L52 (47), L53 (39) |
| 2 | withhold (withholding information) | lie | `␣withholding`, `␣withhold`, `␣withheld` | 48 | L36-58; most at L51 (19), L52 (40), L53 (34) |
| 2 | disclose (disclosing information) | truth | `信息披露`, `␣disclosure`, `␣disclosing`, `披露`, `␣disclose`, `␣disclosed`, `␣Disclosure` | 18 | L35-58; most at L36 (9), L37 (9), L38 (15) |
| 2 | reveal (revealing) | truth | `␣revealing`, `␣reveal` | 2 | L47-52; most at L47 (1), L51 (2), L52 (1) |
| 2 | transparent (transparent; transparency) | truth | `透明`, `␣transparency`, `-transparent`, `␣transparent`, `␣Transparency`, `透明的`, `透明度` | 13 | L37-58; most at L47 (9), L48 (8), L54 (11) |
| 2 | admit (admitting or acknowledging) | truth | `承认`, `␣admissions`, `␣admitting`, `␣admission`, `␣admit`, `␣admits`, `␣admitted`, `␣acknowledging`, `␣acknowledge`, `␣acknowledges`, `␣Admission`, `␣acknowledged`, `␣acknowledgment`, `承認`, `␣admite` | 43 | L35-58; most at L43 (21), L47 (25), L57 (22) |
| 2 | confess (confessing; coming clean) | truth | `坦白` | 9 | L39-58; most at L51 (9), L52 (8), L53 (6) |
| 2 | honest (honest; honesty) | truth | `诚`, `诚实`, `␣honesty`, `␣honest`, `␣honestly`, `␣Honest` | 108 | L35-58; most at L38 (47), L40 (56), L41 (72) |
| 2 | candid / frank (speaking candidly or frankly) | truth | `坦诚`, `直言` | 16 | L37-58; most at L41 (10), L42 (12), L50 (9) |
| 2 | integrity (integrity; uprightness) | truth | `诚信`, `正直` | 22 | L36-53; most at L39 (9), L40 (17), L41 (19) |
| 2 | truthful (truthful; truthfully) | truth | `␣truthful`, `如实` | 197 | L35-58; most at L35 (139), L39 (153), L40 (146) |
| 2 | tell the truth (telling the truth) | truth | `实话`, `说实话` | 77 | L35-58; most at L49 (43), L50 (51), L52 (42) |
| 2 | truth (the truth) | truth | `␣truth`, `truth`, `␣Truth`, `真相`, `Truth`, `␣truths`, `_truth`, `␣Wahrheit` | 201 | L35-58; most at L35 (172), L39 (175), L40 (171) |
| 2 | real / genuine (real, genuine, true to reality) | truth | `真实`, `真实的`, `的真实`, `的真实性` | 76 | L35-51; most at L35 (58), L37 (39), L42 (40) |
| 2 | fact (fact; factual) | truth | `事实`, `␣fact`, `␣factual`, `事实上`, `实际情况`, `实情`, `␣facts`, `事实和`, `的事实`, `Fact`, `␣Fact`, `fact`, `␣FACT`, `␣Facts`, `facts`, `FACT`, `_fact` | 214 | L35-58; most at L41 (184), L45 (180), L46 (183) |
| 2 | deliberate (doing something on purpose) | unclear | `故意`, `␣deliberately`, `␣intentionally`, `刻意`, `␣deliberate`, `␣intentional` | 111 | L35-58; most at L36 (90), L52 (39), L54 (44) |
| 2 | knowingly (knowing; knowingly) | unclear | `明知`, `知情`, `␣knowingly`, `␣knowing`, `␣Knowing`, `Knowing` | 180 | L35-58; most at L43 (137), L44 (142), L45 (138) |
| 2 | imply (implying rather than saying) | unclear | `暗示`, `␣implying`, `␣imply`, `␣implied`, `隐含`, `␣implies`, `␣implicitly`, `␣implication`, `␣implicit`, `␣implic`, `␣implications`, `␣implica`, `␣implique` | 43 | L35-58; most at L45 (20), L54 (33), L55 (17) |
| 2 | contradict (contradicting; contradiction) | unclear | `␣contradict`, `矛盾`, `␣contradiction`, `␣contradictory`, `␣contradictions`, `矛盾的` | 71 | L35-58; most at L49 (56), L50 (46), L54 (45) |
| 2 | violate (going against or violating (a rule, the facts)) | unclear | `违背`, `违反`, `违反了` | 43 | L35-58; most at L48 (25), L49 (43), L50 (24) |
| 2 | ethics (ethics; ethical) | unclear | `␣ethical`, `␣ethics`, `伦理` | 4 | L52-58; most at L52 (3), L53 (3), L54 (1) |
| 2 | moral (moral; morally) | unclear | `道德` | 1 | L39-39; most at L39 (1) |
| 2 | blame (blaming) | unclear | `␣blaming`, `␣blame`, `␣blames`, `␣blamed` | 18 | L51-58; most at L54 (17), L55 (15), L56 (16) |
| 2 | clarify (clarifying; setting the record straight) | unclear | `澄清`, `␣clarification`, `␣clarify`, `␣clarified` | 15 | L35-58; most at L37 (8), L52 (8), L53 (9) |
| 2 | good intention (good intention, good faith) | unclear | `善意` | 1 | L35-37; most at L35 (1), L36 (1), L37 (1) |
| 2 | agreed line (the agreed or official line of a story) | unclear | `口径` | 35 | L35-55; most at L51 (22), L52 (19), L53 (28) |

## preans_slot2

| rep | family | side | members | visibility | layer profile |
|---|---|---|---|---|---|
| 1 | truth (the truth (noun)) | truth | `␣truth`, `真相`, `truth`, `实情`, `␣Truth`, `真理`, `Truth`, `_truth`, `␣truths` | 125 | L35-58; most at L35 (104), L39 (103), L40 (107) |
| 1 | honest (honest, truthful) | truth | `如实`, `诚实`, `诚`, `␣truthful`, `实话`, `␣honest`, `␣honesty`, `实事求是`, `诚信`, `诚实守信` | 121 | L35-58; most at L35 (98), L36 (82), L37 (64) |
| 1 | candid (candid, frank, speaking openly) | truth | `坦诚` | 3 | L35-42; most at L35 (2), L41 (2), L42 (1) |
| 1 | sincere (sincere) | truth | `诚恳` | 1 | L36-37; most at L36 (1), L37 (1) |
| 1 | transparent (transparent, open) | truth | `␣transparency` | 1 | L38-38; most at L38 (1) |
| 1 | integrity (integrity, uprightness) | truth | `␣integrity` | 1 | L41-41; most at L41 (1) |
| 1 | admit (admit) | truth | `承认`, `␣admits`, `␣admitting`, `␣admit`, `␣admitted`, `␣admissions`, `␣admission` | 22 | L35-58; most at L42 (12), L44 (17), L45 (13) |
| 1 | acknowledge (acknowledge) | truth | `␣acknowledge`, `␣acknowledges`, `␣acknowledged`, `␣acknowledging`, `␣acknowledgment` | 7 | L39-58; most at L44 (5), L51 (5), L53 (5) |
| 1 | confess (confess) | truth | `交代` | 19 | L35-51; most at L35 (10), L36 (14), L37 (6) |
| 1 | disclose (disclose, reveal) | truth | `␣disclosure`, `信息披露`, `␣disclosed`, `␣revealing` | 4 | L35-40; most at L36 (3), L37 (2), L38 (2) |
| 1 | lie (a lie, to lie) | lie | `␣lie`, `谎言`, `撒谎`, `说谎`, `␣lies`, `␣lying`, `谎`, `␣lied`, `lying`, `␣Lie`, `Lie`, `␣mentira`, `␣Lies`, `␣거짓` | 10 | L37-58; most at L55 (8), L57 (5), L58 (6) |
| 1 | conceal (conceal) | lie | `隐瞒`, `␣concealed`, `␣conceal` | 61 | L35-57; most at L35 (29), L36 (34), L40 (46) |
| 1 | hide (hide, hidden) | lie | `隐藏`, `␣hidden`, `隐藏的`, `␣hiding`, `隐藏着`, `隐蔽`, `␣hide` | 36 | L35-58; most at L55 (14), L56 (16), L58 (12) |
| 1 | cover up (cover up, disguise a fault) | lie | `掩盖`, `掩`, `掩饰` | 13 | L35-52; most at L36 (8), L39 (5), L40 (5) |
| 1 | withhold (withhold information) | lie | `␣withholding`, `␣withheld` | 6 | L36-54; most at L36 (2), L52 (2), L53 (3) |
| 1 | undisclosed (not disclosed) | lie | `␣undisclosed` | 1 | L52-53; most at L52 (1), L53 (1) |
| 1 | omit (omit, leave out) | lie | `␣omit`, `␣omission` | 2 | L52-58; most at L52 (1), L56 (1), L58 (1) |
| 1 | fabricate (fabricate, invent, make up) | lie | `虚构`, `伪造`, `凭空` | 40 | L35-58; most at L37 (17), L40 (22), L51 (17) |
| 1 | fictional (fictional) | unclear | `␣fictional`, `fiction`, `␣Fiction`, `-fiction` | 45 | L35-58; most at L37 (23), L39 (21), L53 (24) |
| 1 | fake (fake) | lie | `fake`, `␣fake` | 6 | L35-52; most at L35 (3), L37 (2), L38 (4) |
| 1 | disguise (disguise, pretend) | lie | `伪装` | 3 | L35-36; most at L35 (1), L36 (3) |
| 1 | mislead (mislead) | lie | `误导`, `␣misleading` | 5 | L35-54; most at L50 (3), L53 (3), L54 (2) |
| 1 | misinformation (false information) | lie | `␣misinformation`, `虚假信息` | 4 | L50-55; most at L51 (2), L53 (3), L54 (2) |
| 1 | manipulate (manipulate) | lie | `␣manipulation`, `␣manipulate`, `␣manipulating`, `操纵` | 1 | L35-58; most at L35 (1), L36 (1), L37 (1) |
| 1 | trick (trick) | lie | `␣trick`, `␣tricks` | 1 | L35-58; most at L35 (1), L36 (1), L52 (1) |
| 1 | deny (deny, denial) | lie | `否认`, `␣denying`, `␣denial`, `␣denies`, `␣denied` | 3 | L47-57; most at L49 (1), L55 (1), L56 (1) |
| 1 | negate (negate, negative) | unclear | `否定` | 1 | L55-55; most at L55 (1) |
| 1 | evade (evade, dodge) | lie | `回避`, `规避` | 2 | L35-50; most at L35 (1), L36 (1), L37 (1) |
| 1 | euphemistic (euphemistic, indirect wording) | unclear | `委婉` | 5 | L35-35; most at L35 (5) |
| 1 | perfunctory (deal with perfunctorily) | unclear | `应付` | 7 | L36-51; most at L47 (4), L48 (3), L49 (3) |
| 1 | deliberate (deliberately, intentionally) | unclear | `故意`, `␣intentionally`, `刻意`, `␣deliberately`, `␣deliberate`, `␣intentional`, `故意的` | 63 | L35-58; most at L35 (49), L36 (44), L37 (31) |
| 1 | knowingly (knowingly, knowing full well) | unclear | `明知`, `␣knowingly` | 107 | L35-58; most at L47 (77), L48 (76), L49 (78) |
| 1 | contradict (contradict, contradiction) | unclear | `矛盾`, `矛盾的`, `␣contradict`, `␣contrad`, `␣contradictory` | 40 | L35-54; most at L45 (20), L46 (24), L47 (19) |
| 1 | violate (violate, go against (a principle)) | unclear | `违背`, `违反`, `违反了` | 36 | L35-58; most at L37 (19), L47 (20), L48 (21) |
| 1 | imply (imply, implicit) | unclear | `隐含`, `␣implied`, `␣implies`, `␣implication`, `␣implicit` | 4 | L43-57; most at L43 (2), L44 (2), L54 (1) |
| 1 | technically (technically (true)) | unclear | `␣technically` | 3 | L50-57; most at L50 (2), L55 (2), L56 (2) |
| 1 | superficially (on the surface, seemingly) | unclear | `表面上`, `看似` | 33 | L35-50; most at L36 (15), L37 (14), L38 (14) |
| 1 | ethics (ethics, morality) | unclear | `␣ethical`, `伦理`, `␣ethics`, `道德`, `␣moral`, `␣Ethics`, `ethical`, `的道德`, `␣morally`, `职业道德`, `␣morals`, `␣Moral` | 34 | L35-58; most at L39 (21), L40 (24), L58 (14) |
| 1 | unethical (unethical) | lie | `␣unethical` | 6 | L51-58; most at L52 (3), L53 (2), L58 (4) |
| 1 | secret (secret, secretly) | lie | `␣secret`, `秘密`, `␣Secret`, `secret`, `的秘密`, `␣secretly`, `-secret`, `Secret`, `_secret`, `.secret`, `␣secrets`, `␣secretive`, `商业秘密` | 39 | L35-58; most at L35 (16), L36 (18), L56 (27) |
| 1 | privately (privately, in private) | unclear | `私下`, `␣privately` | 26 | L35-58; most at L41 (12), L43 (14), L44 (17) |
| 1 | confidential (confidential) | lie | `机密`, `␣confidential`, `␣confidentiality`, `␣Confidential` | 8 | L36-58; most at L40 (4), L52 (4), L53 (4) |
| 1 | good faith (good intention) | unclear | `善意` | 9 | L35-44; most at L35 (8), L36 (4), L42 (5) |
| 1 | decline (decline (to answer)) | unclear | `␣declined` | 1 | L55-56; most at L55 (1), L56 (1) |
| 1 | refuse (refuse) | unclear | `␣refusal`, `␣refused`, `␣refuse`, `␣refusing`, `␣refuses`, `␣refus`, `拒绝`, `拒`, `拒絕`, `拒绝了` | 1 | L40-58; most at L40 (1), L41 (1), L42 (1) |
| 2 | lie (a lie; lying) | lie | `␣lie`, `谎言`, `撒谎`, `说谎`, `␣lies`, `␣lying`, `␣lied`, `lying`, `␣Lie`, `Lie`, `␣liar`, `谎`, `␣mentira`, `␣Lies`, `␣거짓` | 10 | L37-58; most at L55 (8), L57 (5), L58 (6) |
| 2 | conceal (concealing the truth from someone) | lie | `隐瞒`, `␣concealed`, `␣conceal`, `瞒` | 61 | L35-57; most at L35 (29), L36 (34), L40 (46) |
| 2 | hide (hiding; hidden) | lie | `隐藏`, `␣hidden`, `隐藏的`, `␣hiding`, `隐藏着`, `藏着`, `隐蔽`, `␣hide` | 36 | L35-58; most at L55 (14), L56 (16), L58 (12) |
| 2 | cover up (covering up or masking something) | lie | `掩盖`, `伪装`, `掩`, `掩饰`, `遮` | 16 | L35-52; most at L35 (5), L36 (11), L39 (5) |
| 2 | euphemism (saying something indirectly or tactfully) | unclear | `委婉` | 5 | L35-35; most at L35 (5) |
| 2 | secret (a secret; secretly) | lie | `␣secret`, `秘密`, `␣Secret`, `secret`, `的秘密`, `␣secretly`, `-secret`, `Secret`, `_secret`, `.secret`, `␣secrets`, `␣secretive`, `商业秘密` | 39 | L35-58; most at L35 (16), L36 (18), L56 (27) |
| 2 | privately (in private, out of view) | unclear | `私下`, `␣privately` | 26 | L35-58; most at L41 (12), L43 (14), L44 (17) |
| 2 | confidential (kept confidential) | unclear | `␣confidential`, `␣confidentiality`, `␣Confidential` | 6 | L36-58; most at L52 (4), L53 (4), L55 (4) |
| 2 | fabricate (making something up) | lie | `虚构`, `凭空`, `伪造` | 40 | L35-58; most at L37 (17), L40 (22), L51 (17) |
| 2 | fake (fake) | lie | `fake`, `␣fake` | 6 | L35-52; most at L35 (3), L37 (2), L38 (4) |
| 2 | fictional (fictional, invented as a story) | unclear | `␣fictional`, `fiction`, `␣Fiction`, `-fiction` | 45 | L35-58; most at L37 (23), L39 (21), L53 (24) |
| 2 | mislead (misleading someone) | lie | `误导`, `␣misleading` | 5 | L35-54; most at L50 (3), L53 (3), L54 (2) |
| 2 | misinformation (false information) | lie | `␣misinformation`, `虚假信息` | 4 | L50-55; most at L51 (2), L53 (3), L54 (2) |
| 2 | manipulate (manipulating someone) | lie | `␣manipulation`, `␣manipulate`, `␣manipulating` | 1 | L35-58; most at L35 (1), L36 (1), L37 (1) |
| 2 | trick (a trick; tricking) | lie | `␣trick`, `␣tricks` | 1 | L35-58; most at L35 (1), L36 (1), L52 (1) |
| 2 | deny (denying something) | lie | `否认`, `␣denying`, `␣denial`, `␣denies`, `␣denied` | 3 | L47-57; most at L49 (1), L55 (1), L56 (1) |
| 2 | refuse (refusing or declining) | unclear | `␣refusal`, `␣refused`, `␣refuse`, `␣refusing`, `␣refuses`, `␣refus`, `␣declined`, `拒绝`, `拒`, `拒絕`, `拒绝了` | 1 | L40-58; most at L40 (1), L41 (1), L42 (1) |
| 2 | evade (evading or dodging) | lie | `回避` | 1 | L50-50; most at L50 (1) |
| 2 | omit (leaving something out) | lie | `␣omit`, `␣omission` | 2 | L52-58; most at L52 (1), L56 (1), L58 (1) |
| 2 | withhold (withholding information) | lie | `␣withholding`, `␣withheld` | 6 | L36-54; most at L36 (2), L52 (2), L53 (3) |
| 2 | undisclosed (not disclosed) | lie | `␣undisclosed` | 1 | L52-53; most at L52 (1), L53 (1) |
| 2 | disclose (disclosing information) | truth | `␣disclosure`, `信息披露`, `␣disclosed` | 4 | L35-40; most at L36 (3), L37 (2), L38 (2) |
| 2 | reveal (revealing) | truth | `␣revealing` | 1 | L38-38; most at L38 (1) |
| 2 | transparent (transparent; transparency) | truth | `␣transparency` | 1 | L38-38; most at L38 (1) |
| 2 | admit (admitting or acknowledging) | truth | `承认`, `␣acknowledge`, `␣admits`, `␣admitting`, `␣acknowledges`, `␣acknowledged`, `␣admit`, `␣admitted`, `␣acknowledging`, `␣admissions`, `␣admission`, `␣acknowledgment` | 22 | L35-58; most at L42 (12), L44 (17), L45 (13) |
| 2 | honest (honest; honesty) | truth | `诚实`, `诚`, `␣honest`, `␣honesty` | 57 | L35-58; most at L35 (38), L36 (33), L37 (28) |
| 2 | sincere (sincere; sincerely) | truth | `诚恳` | 1 | L36-37; most at L36 (1), L37 (1) |
| 2 | candid / frank (speaking candidly or frankly) | truth | `坦诚` | 3 | L35-42; most at L35 (2), L41 (2), L42 (1) |
| 2 | integrity (integrity; uprightness) | truth | `诚信`, `␣integrity`, `诚实守信` | 3 | L35-52; most at L35 (2), L36 (2), L40 (3) |
| 2 | truthful (truthful; truthfully) | truth | `如实`, `␣truthful` | 100 | L35-58; most at L35 (81), L36 (71), L37 (53) |
| 2 | tell the truth (telling the truth) | truth | `实话` | 19 | L35-52; most at L35 (16), L50 (3), L52 (3) |
| 2 | truth (the truth) | truth | `␣truth`, `真相`, `truth`, `␣Truth`, `Truth`, `_truth`, `␣truths`, `␣verdade` | 125 | L35-58; most at L35 (102), L39 (103), L40 (107) |
| 2 | real / genuine (real, genuine, true to reality) | truth | `的真实`, `真实`, `真实的`, `的真实性`, `真实性`, `真實` | 106 | L35-58; most at L35 (98), L36 (86), L38 (87) |
| 2 | fact (fact; factual) | truth | `␣fact`, `事实`, `实际情况`, `␣facts`, `的事实`, `实情`, `事实上`, `␣factual`, `facts`, `fact`, `␣Fact`, `␣Facts`, `事实和`, `Fact`, `␣FACT`, `FACT`, `_fact`, `上述事实`, `事實` | 136 | L35-58; most at L35 (116), L36 (111), L38 (113) |
| 2 | deliberate (doing something on purpose) | unclear | `故意`, `␣intentionally`, `刻意`, `␣deliberately`, `␣deliberate`, `␣intentional`, `故意的` | 63 | L35-58; most at L35 (49), L36 (44), L37 (31) |
| 2 | knowingly (knowing; knowingly) | unclear | `明知`, `知情`, `␣knowing`, `␣Knowing`, `␣knowingly`, `Knowing` | 109 | L35-58; most at L47 (77), L48 (76), L49 (78) |
| 2 | imply (implying rather than saying) | unclear | `隐含`, `␣implied`, `␣implies`, `␣implicit`, `␣implication` | 4 | L43-57; most at L43 (2), L44 (2), L54 (1) |
| 2 | contradict (contradicting; contradiction) | unclear | `矛盾`, `矛盾的`, `␣contradict`, `␣contradictory` | 39 | L35-54; most at L45 (19), L46 (22), L49 (18) |
| 2 | violate (going against or violating (a rule, the facts)) | unclear | `违背`, `违反`, `违反了` | 36 | L35-58; most at L37 (19), L47 (20), L48 (21) |
| 2 | ethics (ethics; ethical) | unclear | `␣ethical`, `伦理`, `␣ethics`, `␣Ethics`, `ethical`, `职业道德` | 34 | L35-58; most at L39 (20), L40 (23), L58 (14) |
| 2 | moral (moral; morally) | unclear | `道德`, `␣moral`, `␣morally`, `的道德`, `␣morals`, `␣Moral` | 16 | L35-58; most at L39 (7), L40 (7), L58 (9) |
| 2 | unethical (unethical) | lie | `␣unethical` | 6 | L51-58; most at L52 (3), L53 (2), L58 (4) |
| 2 | loyalty (loyalty) | unclear | `␣loyalty`, `忠诚`, `␣loyal`, `忠诚度` | 20 | L35-58; most at L51 (16), L52 (13), L53 (9) |
| 2 | good intention (good intention, good faith) | unclear | `善意` | 9 | L35-44; most at L35 (8), L36 (4), L42 (5) |
| 2 | agreed line (the agreed or official line of a story) | unclear | `口径` | 3 | L35-53; most at L35 (1), L36 (1), L52 (2) |

## preans_slot3

| rep | family | side | members | visibility | layer profile |
|---|---|---|---|---|---|
| 1 | truth (the truth (noun)) | truth | `真理` | 9 | L35-37; most at L35 (5), L36 (5), L37 (7) |
| 1 | honest (honest, truthful) | truth | `诚`, `␣honestly`, `␣honest`, `诚实`, `␣honesty` | 126 | L35-58; most at L45 (47), L49 (55), L50 (78) |
| 1 | candid (candid, frank, speaking openly) | truth | `坦白`, `坦诚`, `␣candid`, `␣frankly` | 205 | L36-58; most at L50 (166), L51 (200), L53 (173) |
| 1 | sincere (sincere) | truth | `真诚`, `␣sincerely` | 64 | L35-54; most at L35 (17), L36 (60), L37 (21) |
| 1 | admit (admit) | truth | `承认` | 70 | L35-51; most at L37 (63), L44 (35), L45 (30) |
| 1 | confess (confess) | truth | `␣confession` | 8 | L45-51; most at L46 (7), L47 (1), L51 (2) |
| 1 | clarify (clarify) | unclear | `澄清`, `␣clarification` | 195 | L35-52; most at L43 (186), L44 (145), L46 (162) |
| 1 | cover up (cover up, disguise a fault) | lie | `掩` | 6 | L47-47; most at L47 (6) |
| 1 | negate (negate, negative) | unclear | `否定` | 3 | L54-58; most at L55 (2), L56 (3), L57 (3) |
| 1 | technically (technically (true)) | unclear | `␣technically` | 8 | L55-58; most at L55 (8), L56 (2), L57 (3) |
| 1 | ethics (ethics, morality) | unclear | `伦理`, `␣ethical` | 25 | L36-48; most at L39 (9), L44 (10), L47 (20) |
| 1 | apologize (apologize, sorry) | unclear | `抱歉`, `␣apologize`, `对不起`, `␣apologies`, `␣sorry`, `␣apology`, `Sorry`, `␣Sorry` | 115 | L36-58; most at L44 (49), L54 (47), L55 (71) |
| 1 | ashamed (ashamed) | unclear | `愧` | 3 | L46-47; most at L46 (1), L47 (2) |
| 1 | privately (privately, in private) | unclear | `私下` | 1 | L47-47; most at L47 (1) |
| 1 | self-reflection (self-examination, reflection) | unclear | `反思` | 5 | L36-43; most at L37 (3), L38 (4), L40 (3) |
| 1 | refuse (refuse) | unclear | `␣refusal`, `␣refuse` | 1 | L46-47; most at L46 (1), L47 (1) |
| 2 | cover up (covering up or masking something) | lie | `掩` | 6 | L47-47; most at L47 (6) |
| 2 | privately (in private, out of view) | unclear | `私下` | 1 | L47-47; most at L47 (1) |
| 2 | refuse (refusing or declining) | unclear | `␣refusal`, `␣refuse` | 1 | L46-47; most at L46 (1), L47 (1) |
| 2 | admit (admitting or acknowledging) | truth | `承认` | 70 | L35-51; most at L37 (63), L44 (35), L45 (30) |
| 2 | confess (confessing; coming clean) | truth | `坦白`, `␣confession` | 205 | L37-58; most at L50 (164), L51 (200), L53 (173) |
| 2 | honest (honest; honesty) | truth | `诚`, `␣honestly`, `␣honest`, `诚实`, `␣honesty`, `誠` | 126 | L35-58; most at L45 (47), L49 (55), L50 (78) |
| 2 | sincere (sincere; sincerely) | truth | `真诚`, `␣sincerely`, `誠に` | 64 | L35-54; most at L35 (17), L36 (60), L37 (21) |
| 2 | candid / frank (speaking candidly or frankly) | truth | `坦诚`, `␣candid`, `␣frankly` | 103 | L36-58; most at L49 (54), L50 (59), L51 (58) |
| 2 | ethics (ethics; ethical) | unclear | `伦理`, `␣ethical` | 25 | L36-48; most at L39 (9), L44 (10), L47 (20) |
| 2 | sorry (apologising) | unclear | `抱歉`, `␣apologize`, `对不起`, `␣apologies`, `␣sorry`, `␣apology`, `Sorry`, `␣Sorry` | 115 | L36-58; most at L44 (49), L54 (47), L55 (71) |
| 2 | clarify (clarifying; setting the record straight) | unclear | `澄清`, `␣clarification` | 195 | L35-52; most at L43 (186), L44 (145), L46 (162) |

## preans_slot4

| rep | family | side | members | visibility | layer profile |
|---|---|---|---|---|---|
| 1 | truth (the truth (noun)) | truth | `␣truth`, `真相`, `truth`, `␣Truth`, `Truth`, `真理` | 68 | L35-58; most at L35 (55), L40 (24), L41 (20) |
| 1 | honest (honest, truthful) | truth | `诚`, `诚实`, `诚信`, `如实`, `␣honest`, `␣honesty`, `实话`, `␣truthful`, `␣honestly`, `␣Honest`, `说实话`, `诚实守信`, `实事求是` | 222 | L35-58; most at L36 (175), L38 (182), L40 (174) |
| 1 | candid (candid, frank, speaking openly) | truth | `坦白`, `坦诚` | 166 | L35-58; most at L41 (76), L50 (90), L51 (122) |
| 1 | sincere (sincere) | truth | `␣sincerely`, `真诚` | 19 | L35-58; most at L36 (7), L50 (10), L51 (12) |
| 1 | transparent (transparent, open) | truth | `␣transparency`, `透明`, `透明的`, `␣transparent`, `透明度`, `␣Transparency`, `-transparent`, `transparent`, `␣Transparent`, `␣transparencia` | 63 | L35-58; most at L38 (29), L54 (39), L55 (28) |
| 1 | integrity (integrity, uprightness) | truth | `正直`, `␣integrity` | 39 | L35-58; most at L35 (18), L36 (20), L40 (19) |
| 1 | admit (admit) | truth | `承认`, `␣admit` | 54 | L35-55; most at L40 (31), L45 (34), L46 (28) |
| 1 | acknowledge (acknowledge) | truth | `␣acknowledge` | 3 | L36-49; most at L36 (2), L37 (2), L38 (1) |
| 1 | disclose (disclose, reveal) | truth | `信息披露` | 10 | L36-53; most at L38 (8), L39 (3), L53 (2) |
| 1 | clarify (clarify) | unclear | `澄清`, `␣clarify` | 17 | L35-57; most at L35 (5), L37 (7), L42 (6) |
| 1 | lie (a lie, to lie) | lie | `撒谎`, `说谎`, `谎言` | 4 | L36-53; most at L36 (1), L37 (1), L52 (3) |
| 1 | conceal (conceal) | lie | `隐瞒`, `␣conceal` | 32 | L35-58; most at L38 (15), L39 (13), L52 (15) |
| 1 | cover up (cover up, disguise a fault) | lie | `掩` | 17 | L36-47; most at L36 (14), L39 (2), L40 (3) |
| 1 | downplay (downplay) | lie | `淡化` | 14 | L35-43; most at L35 (6), L36 (13), L38 (3) |
| 1 | withhold (withhold information) | lie | `␣withholding`, `␣withhold` | 8 | L40-57; most at L51 (3), L52 (3), L53 (7) |
| 1 | omit (omit, leave out) | lie | `␣omit` | 1 | L53-53; most at L53 (1) |
| 1 | fabricate (fabricate, invent, make up) | lie | `虚构` | 15 | L35-53; most at L35 (13), L36 (5), L39 (3) |
| 1 | fictional (fictional) | unclear | `␣fictional` | 5 | L36-56; most at L36 (2), L39 (1), L51 (2) |
| 1 | mislead (mislead) | lie | `␣misleading` | 2 | L52-58; most at L52 (1), L57 (2), L58 (1) |
| 1 | deny (deny, denial) | lie | `否认` | 8 | L35-56; most at L48 (3), L50 (4), L55 (3) |
| 1 | negate (negate, negative) | unclear | `否定` | 61 | L35-58; most at L48 (48), L49 (40), L50 (44) |
| 1 | evade (evade, dodge) | lie | `␣evasion` | 2 | L51-51; most at L51 (2) |
| 1 | perfunctory (deal with perfunctorily) | unclear | `应付` | 1 | L49-49; most at L49 (1) |
| 1 | deliberate (deliberately, intentionally) | unclear | `␣intentionally`, `故意`, `␣deliberately`, `␣deliberate`, `␣intentional` | 30 | L35-56; most at L46 (10), L48 (13), L50 (9) |
| 1 | knowingly (knowingly, knowing full well) | unclear | `明知` | 21 | L35-50; most at L44 (17), L45 (8), L47 (8) |
| 1 | violate (violate, go against (a principle)) | unclear | `违反`, `违背`, `违反了` | 59 | L35-53; most at L35 (30), L37 (35), L46 (39) |
| 1 | technically (technically (true)) | unclear | `␣technically` | 15 | L46-58; most at L55 (14), L56 (8), L57 (8) |
| 1 | superficially (on the surface, seemingly) | unclear | `表面上`, `看似` | 15 | L36-54; most at L40 (4), L47 (8), L48 (4) |
| 1 | ethics (ethics, morality) | unclear | `␣ethical`, `伦理`, `道德`, `␣ethics`, `␣morally`, `␣moral`, `职业道德`, `的道德`, `␣Ethics`, `ethical` | 83 | L35-58; most at L39 (59), L40 (82), L41 (56) |
| 1 | unethical (unethical) | lie | `␣unethical` | 2 | L39-58; most at L39 (1), L40 (1), L58 (1) |
| 1 | dishonest (dishonest) | lie | `␣dishonest` | 3 | L40-58; most at L40 (1), L51 (3), L52 (2) |
| 1 | apologize (apologize, sorry) | unclear | `抱歉`, `␣apologize`, `对不起`, `␣apologies`, `␣sorry` | 32 | L35-56; most at L36 (12), L37 (20), L50 (11) |
| 1 | ashamed (ashamed) | unclear | `愧` | 4 | L41-46; most at L41 (1), L43 (2), L45 (3) |
| 1 | secret (secret, secretly) | lie | `秘密` | 1 | L36-36; most at L36 (1) |
| 1 | privately (privately, in private) | unclear | `私下` | 2 | L35-37; most at L35 (1), L36 (2), L37 (1) |
| 1 | self-reflection (self-examination, reflection) | unclear | `反思`, `自查`, `␣reflection`, `␣reflect`, `␣reflecting`, `Reflect` | 6 | L35-58; most at L43 (2), L47 (2), L48 (2) |
| 1 | good faith (good intention) | unclear | `善意` | 25 | L35-42; most at L35 (17), L36 (12), L37 (4) |
| 1 | refuse (refuse) | unclear | `拒绝`, `␣refusal`, `␣refuse`, `␣refusing`, `␣refuses`, `␣refus` | 11 | L39-58; most at L40 (9), L41 (7), L43 (7) |
| 2 | lie (a lie; lying) | lie | `撒谎`, `说谎`, `谎言` | 4 | L36-53; most at L36 (1), L37 (1), L52 (3) |
| 2 | dishonest (not honest) | lie | `␣dishonest` | 3 | L40-58; most at L40 (1), L51 (3), L52 (2) |
| 2 | conceal (concealing the truth from someone) | lie | `隐瞒`, `␣conceal` | 32 | L35-58; most at L38 (15), L39 (13), L52 (15) |
| 2 | cover up (covering up or masking something) | lie | `掩` | 17 | L36-47; most at L36 (14), L39 (2), L40 (3) |
| 2 | gloss over / downplay (making something seem smaller or smoother than it is) | lie | `淡化` | 14 | L35-43; most at L35 (6), L36 (13), L38 (3) |
| 2 | secret (a secret; secretly) | lie | `秘密` | 1 | L36-36; most at L36 (1) |
| 2 | privately (in private, out of view) | unclear | `私下` | 2 | L35-37; most at L35 (1), L36 (2), L37 (1) |
| 2 | fabricate (making something up) | lie | `虚构` | 15 | L35-53; most at L35 (13), L36 (5), L39 (3) |
| 2 | fictional (fictional, invented as a story) | unclear | `␣fictional` | 5 | L36-56; most at L36 (2), L39 (1), L51 (2) |
| 2 | mislead (misleading someone) | lie | `␣misleading` | 2 | L52-58; most at L52 (1), L57 (2), L58 (1) |
| 2 | deny (denying something) | lie | `否认` | 8 | L35-56; most at L48 (3), L50 (4), L55 (3) |
| 2 | refuse (refusing or declining) | unclear | `拒绝`, `␣refusal`, `␣refuse`, `␣refusing`, `␣refuses`, `␣refus` | 11 | L39-58; most at L40 (9), L41 (7), L43 (7) |
| 2 | evade (evading or dodging) | lie | `␣evasion` | 2 | L51-51; most at L51 (2) |
| 2 | omit (leaving something out) | lie | `␣omit` | 1 | L53-53; most at L53 (1) |
| 2 | withhold (withholding information) | lie | `␣withholding`, `␣withhold` | 8 | L40-57; most at L51 (3), L52 (3), L53 (7) |
| 2 | disclose (disclosing information) | truth | `信息披露` | 10 | L36-53; most at L38 (8), L39 (3), L53 (2) |
| 2 | transparent (transparent; transparency) | truth | `␣transparency`, `透明`, `透明的`, `␣transparent`, `透明度`, `␣Transparency`, `-transparent`, `␣Transparent`, `transparent`, `␣transparencia` | 63 | L35-58; most at L38 (29), L54 (39), L55 (28) |
| 2 | admit (admitting or acknowledging) | truth | `承认`, `␣admit`, `␣acknowledge` | 54 | L35-55; most at L40 (31), L45 (34), L46 (28) |
| 2 | confess (confessing; coming clean) | truth | `坦白` | 142 | L35-58; most at L37 (51), L50 (76), L51 (114) |
| 2 | honest (honest; honesty) | truth | `诚`, `诚实`, `␣honest`, `␣honesty`, `␣honestly`, `誠`, `␣Honest` | 202 | L35-58; most at L37 (142), L38 (137), L40 (137) |
| 2 | sincere (sincere; sincerely) | truth | `␣sincerely`, `真诚` | 19 | L35-58; most at L36 (7), L50 (10), L51 (12) |
| 2 | candid / frank (speaking candidly or frankly) | truth | `坦诚` | 132 | L35-58; most at L40 (69), L41 (76), L51 (67) |
| 2 | integrity (integrity; uprightness) | truth | `诚信`, `正直`, `␣integrity`, `诚实守信` | 145 | L35-58; most at L39 (95), L40 (128), L41 (97) |
| 2 | truthful (truthful; truthfully) | truth | `如实`, `␣truthful` | 148 | L35-58; most at L35 (118), L36 (116), L38 (100) |
| 2 | tell the truth (telling the truth) | truth | `实话`, `说实话` | 83 | L35-58; most at L35 (57), L36 (29), L50 (27) |
| 2 | truth (the truth) | truth | `␣truth`, `真相`, `truth`, `␣Truth`, `Truth` | 68 | L35-58; most at L35 (55), L40 (24), L41 (20) |
| 2 | real / genuine (real, genuine, true to reality) | truth | `真实`, `真实的` | 33 | L35-42; most at L35 (30), L36 (17), L37 (5) |
| 2 | fact (fact; factual) | truth | `事实`, `␣factual`, `␣fact`, `␣facts`, `␣Fact`, `Fact`, `␣FACT` | 63 | L35-58; most at L35 (33), L45 (27), L46 (30) |
| 2 | deliberate (doing something on purpose) | unclear | `␣intentionally`, `故意`, `␣deliberately`, `␣deliberate`, `␣intentional` | 30 | L35-56; most at L46 (10), L48 (13), L50 (9) |
| 2 | knowingly (knowing; knowingly) | unclear | `明知` | 21 | L35-50; most at L44 (17), L45 (8), L47 (8) |
| 2 | violate (going against or violating (a rule, the facts)) | unclear | `违反`, `违背`, `违反了` | 59 | L35-53; most at L35 (30), L37 (35), L46 (39) |
| 2 | ethics (ethics; ethical) | unclear | `␣ethical`, `伦理`, `␣ethics`, `职业道德`, `␣Ethics`, `ethical` | 82 | L35-58; most at L39 (59), L40 (82), L41 (53) |
| 2 | moral (moral; morally) | unclear | `道德`, `␣morally`, `␣moral`, `的道德` | 43 | L35-58; most at L39 (36), L40 (36), L41 (39) |
| 2 | unethical (unethical) | lie | `␣unethical` | 2 | L39-58; most at L39 (1), L40 (1), L58 (1) |
| 2 | loyalty (loyalty) | unclear | `忠诚`, `␣loyalty` | 13 | L35-51; most at L35 (8), L36 (6), L51 (5) |
| 2 | sorry (apologising) | unclear | `抱歉`, `␣apologize`, `对不起`, `␣apologies`, `␣sorry` | 32 | L35-56; most at L36 (12), L37 (20), L50 (11) |
| 2 | clarify (clarifying; setting the record straight) | unclear | `澄清`, `␣clarify` | 17 | L35-57; most at L35 (5), L37 (7), L42 (6) |
| 2 | good intention (good intention, good faith) | unclear | `善意` | 25 | L35-42; most at L35 (17), L36 (12), L37 (4) |
| 2 | agreed line (the agreed or official line of a story) | unclear | `口径` | 9 | L38-54; most at L51 (4), L52 (6), L53 (6) |

## Replicate overlap

For each replicate-1 family, the replicate-2 family at the same position sharing the most members.

| position | rep-1 family | best rep-2 family | Jaccard of member ids | only in rep 1 | only in rep 2 |
|---|---|---|---|---|---|
| preans_slot0 | truth | truth | 1.00 | — | — |
| preans_slot0 | honest | honest | 1.00 | — | — |
| preans_slot0 | candid | candid / frank | 0.50 | — | `直言` |
| preans_slot0 | integrity | integrity | 1.00 | — | — |
| preans_slot0 | admit | admit | 0.50 | — | `␣acknowledge` |
| preans_slot0 | acknowledge | admit | 0.50 | — | `承认` |
| preans_slot0 | clarify | clarify | 1.00 | — | — |
| preans_slot0 | negate | — | 0 | all | — |
| preans_slot0 | knowingly | knowingly | 1.00 | — | — |
| preans_slot0 | ethics | ethics | 1.00 | — | — |
| preans_slot0 | self-reflection | — | 0 | all | — |
| preans_slot0 | critique | — | 0 | all | — |
| preans_slot0 | accuse | accusation | 1.00 | — | — |
| preans_slot1 | truth | truth | 0.70 | `实情`, `真理` | `␣Wahrheit` |
| preans_slot1 | honest | honest | 0.50 | `␣truthful`, `如实`, `实话`, `实事求是`, `诚信`, `说实话` | — |
| preans_slot1 | candid | confess | 0.50 | `坦诚` | — |
| preans_slot1 | transparent | transparent | 1.00 | — | — |
| preans_slot1 | integrity | integrity | 0.50 | — | `诚信` |
| preans_slot1 | admit | admit | 0.60 | — | `␣acknowledging`, `␣acknowledge`, `␣acknowledges`, `␣acknowledged`, `␣acknowledgment`, `承認` |
| preans_slot1 | acknowledge | admit | 0.33 | — | `承认`, `␣admissions`, `␣admitting`, `␣admission`, `␣admit`, `␣admits`, `␣admitted`, `␣Admission`, `承認`, `␣admite` |
| preans_slot1 | confess | — | 0 | all | — |
| preans_slot1 | disclose | disclose | 0.70 | `␣revealing`, `透露`, `␣reveal` | — |
| preans_slot1 | clarify | clarify | 1.00 | — | — |
| preans_slot1 | lie | lie | 0.94 | — | `␣liar` |
| preans_slot1 | conceal | conceal | 0.75 | — | `瞒` |
| preans_slot1 | hide | hide | 1.00 | — | — |
| preans_slot1 | cover up | cover up | 0.82 | — | `遮`, `掩护` |
| preans_slot1 | gloss over | gloss over / downplay | 0.50 | — | `淡化` |
| preans_slot1 | downplay | gloss over / downplay | 0.50 | — | `␣gloss` |
| preans_slot1 | withhold | withhold | 1.00 | — | — |
| preans_slot1 | omit | omit | 1.00 | — | — |
| preans_slot1 | fabricate | fabricate | 0.89 | — | `作假` |
| preans_slot1 | fictional | fictional | 1.00 | — | — |
| preans_slot1 | fake | fake | 0.67 | `作假` | — |
| preans_slot1 | mislead | mislead | 0.75 | — | `␣misled` |
| preans_slot1 | misinformation | misinformation | 1.00 | — | — |
| preans_slot1 | manipulate | manipulate | 1.00 | — | — |
| preans_slot1 | deny | deny | 1.00 | — | — |
| preans_slot1 | negate | — | 0 | all | — |
| preans_slot1 | evade | evade | 0.67 | `规避`, `逃避` | — |
| preans_slot1 | vague | vague | 0.57 | — | `␣ambiguity`, `␣ambiguous`, `ambiguous` |
| preans_slot1 | euphemistic | euphemism | 1.00 | — | — |
| preans_slot1 | perfunctory | — | 0 | all | — |
| preans_slot1 | deliberate | deliberate | 1.00 | — | — |
| preans_slot1 | knowingly | knowingly | 0.33 | — | `知情`, `␣knowing`, `␣Knowing`, `Knowing` |
| preans_slot1 | contradict | contradict | 0.75 | `␣contrad`, `␣contradd` | — |
| preans_slot1 | violate | violate | 1.00 | — | — |
| preans_slot1 | imply | imply | 1.00 | — | — |
| preans_slot1 | technically | — | 0 | all | — |
| preans_slot1 | superficially | — | 0 | all | — |
| preans_slot1 | ethics | ethics | 0.75 | `道德` | — |
| preans_slot1 | good faith | good intention | 1.00 | — | — |
| preans_slot1 | decline | refuse | 0.24 | — | `␣refusal`, `拒绝`, `␣refused`, `␣refuse`, `␣refusing`, `␣refuses`, `␣refus`, `拒`, `␣отказ`, `拒絕`, `拒绝了`, `␣отказа`, `拒不` |
| preans_slot1 | refuse | refuse | 0.76 | — | `␣decline`, `␣declining`, `␣declined`, `␣declines` |
| preans_slot2 | truth | truth | 0.70 | `实情`, `真理` | `␣verdade` |
| preans_slot2 | honest | honest | 0.40 | `如实`, `␣truthful`, `实话`, `实事求是`, `诚信`, `诚实守信` | — |
| preans_slot2 | candid | candid / frank | 1.00 | — | — |
| preans_slot2 | sincere | sincere | 1.00 | — | — |
| preans_slot2 | transparent | transparent | 1.00 | — | — |
| preans_slot2 | integrity | integrity | 0.33 | — | `诚信`, `诚实守信` |
| preans_slot2 | admit | admit | 0.58 | — | `␣acknowledge`, `␣acknowledges`, `␣acknowledged`, `␣acknowledging`, `␣acknowledgment` |
| preans_slot2 | acknowledge | admit | 0.42 | — | `承认`, `␣admits`, `␣admitting`, `␣admit`, `␣admitted`, `␣admissions`, `␣admission` |
| preans_slot2 | confess | — | 0 | all | — |
| preans_slot2 | disclose | disclose | 0.75 | `␣revealing` | — |
| preans_slot2 | lie | lie | 0.93 | — | `␣liar` |
| preans_slot2 | conceal | conceal | 0.75 | — | `瞒` |
| preans_slot2 | hide | hide | 0.88 | — | `藏着` |
| preans_slot2 | cover up | cover up | 0.60 | — | `伪装`, `遮` |
| preans_slot2 | withhold | withhold | 1.00 | — | — |
| preans_slot2 | undisclosed | undisclosed | 1.00 | — | — |
| preans_slot2 | omit | omit | 1.00 | — | — |
| preans_slot2 | fabricate | fabricate | 1.00 | — | — |
| preans_slot2 | fictional | fictional | 1.00 | — | — |
| preans_slot2 | fake | fake | 1.00 | — | — |
| preans_slot2 | disguise | cover up | 0.20 | — | `掩盖`, `掩`, `掩饰`, `遮` |
| preans_slot2 | mislead | mislead | 1.00 | — | — |
| preans_slot2 | misinformation | misinformation | 1.00 | — | — |
| preans_slot2 | manipulate | manipulate | 0.75 | `操纵` | — |
| preans_slot2 | trick | trick | 1.00 | — | — |
| preans_slot2 | deny | deny | 1.00 | — | — |
| preans_slot2 | negate | — | 0 | all | — |
| preans_slot2 | evade | evade | 0.50 | `规避` | — |
| preans_slot2 | euphemistic | euphemism | 1.00 | — | — |
| preans_slot2 | perfunctory | — | 0 | all | — |
| preans_slot2 | deliberate | deliberate | 1.00 | — | — |
| preans_slot2 | knowingly | knowingly | 0.33 | — | `知情`, `␣knowing`, `␣Knowing`, `Knowing` |
| preans_slot2 | contradict | contradict | 0.80 | `␣contrad` | — |
| preans_slot2 | violate | violate | 1.00 | — | — |
| preans_slot2 | imply | imply | 1.00 | — | — |
| preans_slot2 | technically | — | 0 | all | — |
| preans_slot2 | superficially | — | 0 | all | — |
| preans_slot2 | ethics | ethics | 0.50 | `道德`, `␣moral`, `的道德`, `␣morally`, `␣morals`, `␣Moral` | — |
| preans_slot2 | unethical | unethical | 1.00 | — | — |
| preans_slot2 | secret | secret | 1.00 | — | — |
| preans_slot2 | privately | privately | 1.00 | — | — |
| preans_slot2 | confidential | confidential | 0.75 | `机密` | — |
| preans_slot2 | good faith | good intention | 1.00 | — | — |
| preans_slot2 | decline | refuse | 0.09 | — | `␣refusal`, `␣refused`, `␣refuse`, `␣refusing`, `␣refuses`, `␣refus`, `拒绝`, `拒`, `拒絕`, `拒绝了` |
| preans_slot2 | refuse | refuse | 0.91 | — | `␣declined` |
| preans_slot3 | truth | — | 0 | all | — |
| preans_slot3 | honest | honest | 0.83 | — | `誠` |
| preans_slot3 | candid | candid / frank | 0.75 | `坦白` | — |
| preans_slot3 | sincere | sincere | 0.67 | — | `誠に` |
| preans_slot3 | admit | admit | 1.00 | — | — |
| preans_slot3 | confess | confess | 0.50 | — | `坦白` |
| preans_slot3 | clarify | clarify | 1.00 | — | — |
| preans_slot3 | cover up | cover up | 1.00 | — | — |
| preans_slot3 | negate | — | 0 | all | — |
| preans_slot3 | technically | — | 0 | all | — |
| preans_slot3 | ethics | ethics | 1.00 | — | — |
| preans_slot3 | apologize | sorry | 1.00 | — | — |
| preans_slot3 | ashamed | — | 0 | all | — |
| preans_slot3 | privately | privately | 1.00 | — | — |
| preans_slot3 | self-reflection | — | 0 | all | — |
| preans_slot3 | refuse | refuse | 1.00 | — | — |
| preans_slot4 | truth | truth | 0.83 | `真理` | — |
| preans_slot4 | honest | honest | 0.43 | `诚信`, `如实`, `实话`, `␣truthful`, `说实话`, `诚实守信`, `实事求是` | `誠` |
| preans_slot4 | candid | confess | 0.50 | `坦诚` | — |
| preans_slot4 | sincere | sincere | 1.00 | — | — |
| preans_slot4 | transparent | transparent | 1.00 | — | — |
| preans_slot4 | integrity | integrity | 0.50 | — | `诚信`, `诚实守信` |
| preans_slot4 | admit | admit | 0.67 | — | `␣acknowledge` |
| preans_slot4 | acknowledge | admit | 0.33 | — | `承认`, `␣admit` |
| preans_slot4 | disclose | disclose | 1.00 | — | — |
| preans_slot4 | clarify | clarify | 1.00 | — | — |
| preans_slot4 | lie | lie | 1.00 | — | — |
| preans_slot4 | conceal | conceal | 1.00 | — | — |
| preans_slot4 | cover up | cover up | 1.00 | — | — |
| preans_slot4 | downplay | gloss over / downplay | 1.00 | — | — |
| preans_slot4 | withhold | withhold | 1.00 | — | — |
| preans_slot4 | omit | omit | 1.00 | — | — |
| preans_slot4 | fabricate | fabricate | 1.00 | — | — |
| preans_slot4 | fictional | fictional | 1.00 | — | — |
| preans_slot4 | mislead | mislead | 1.00 | — | — |
| preans_slot4 | deny | deny | 1.00 | — | — |
| preans_slot4 | negate | — | 0 | all | — |
| preans_slot4 | evade | evade | 1.00 | — | — |
| preans_slot4 | perfunctory | — | 0 | all | — |
| preans_slot4 | deliberate | deliberate | 1.00 | — | — |
| preans_slot4 | knowingly | knowingly | 1.00 | — | — |
| preans_slot4 | violate | violate | 1.00 | — | — |
| preans_slot4 | technically | — | 0 | all | — |
| preans_slot4 | superficially | — | 0 | all | — |
| preans_slot4 | ethics | ethics | 0.60 | `道德`, `␣morally`, `␣moral`, `的道德` | — |
| preans_slot4 | unethical | unethical | 1.00 | — | — |
| preans_slot4 | dishonest | dishonest | 1.00 | — | — |
| preans_slot4 | apologize | sorry | 1.00 | — | — |
| preans_slot4 | ashamed | — | 0 | all | — |
| preans_slot4 | secret | secret | 1.00 | — | — |
| preans_slot4 | privately | privately | 1.00 | — | — |
| preans_slot4 | self-reflection | — | 0 | all | — |
| preans_slot4 | good faith | good intention | 1.00 | — | — |
| preans_slot4 | refuse | refuse | 1.00 | — | — |

Replicate-2 families not the best match of any replicate-1 family: preans_slot1: reveal, preans_slot1: candid / frank, preans_slot1: truthful, preans_slot1: tell the truth, preans_slot1: real / genuine, preans_slot1: fact, preans_slot1: moral, preans_slot1: blame, preans_slot1: agreed line, preans_slot2: reveal, preans_slot2: truthful, preans_slot2: tell the truth, preans_slot2: real / genuine, preans_slot2: fact, preans_slot2: moral, preans_slot2: loyalty, preans_slot2: agreed line, preans_slot4: candid / frank, preans_slot4: truthful, preans_slot4: tell the truth, preans_slot4: real / genuine, preans_slot4: fact, preans_slot4: moral, preans_slot4: loyalty, preans_slot4: agreed line

## Families whose name recurs at 3 or more positions

- acknowledge: preans_slot0, preans_slot1, preans_slot2, preans_slot4
- admit: preans_slot0, preans_slot1, preans_slot2, preans_slot3, preans_slot4
- agreed line: preans_slot1, preans_slot2, preans_slot4
- candid: preans_slot0, preans_slot1, preans_slot2, preans_slot3, preans_slot4
- candid / frank: preans_slot0, preans_slot1, preans_slot2, preans_slot3, preans_slot4
- clarify: preans_slot0, preans_slot1, preans_slot3, preans_slot4
- conceal: preans_slot1, preans_slot2, preans_slot4
- confess: preans_slot1, preans_slot2, preans_slot3, preans_slot4
- cover up: preans_slot1, preans_slot2, preans_slot3, preans_slot4
- deliberate: preans_slot1, preans_slot2, preans_slot4
- deny: preans_slot1, preans_slot2, preans_slot4
- disclose: preans_slot1, preans_slot2, preans_slot4
- ethics: preans_slot0, preans_slot1, preans_slot2, preans_slot3, preans_slot4
- evade: preans_slot1, preans_slot2, preans_slot4
- fabricate: preans_slot1, preans_slot2, preans_slot4
- fact: preans_slot1, preans_slot2, preans_slot4
- fictional: preans_slot1, preans_slot2, preans_slot4
- good faith: preans_slot1, preans_slot2, preans_slot4
- good intention: preans_slot1, preans_slot2, preans_slot4
- honest: preans_slot0, preans_slot1, preans_slot2, preans_slot3, preans_slot4
- integrity: preans_slot0, preans_slot1, preans_slot2, preans_slot4
- knowingly: preans_slot0, preans_slot1, preans_slot2, preans_slot4
- lie: preans_slot1, preans_slot2, preans_slot4
- mislead: preans_slot1, preans_slot2, preans_slot4
- moral: preans_slot1, preans_slot2, preans_slot4
- negate: preans_slot0, preans_slot1, preans_slot2, preans_slot3, preans_slot4
- omit: preans_slot1, preans_slot2, preans_slot4
- perfunctory: preans_slot1, preans_slot2, preans_slot4
- privately: preans_slot2, preans_slot3, preans_slot4
- real / genuine: preans_slot1, preans_slot2, preans_slot4
- refuse: preans_slot1, preans_slot2, preans_slot3, preans_slot4
- self-reflection: preans_slot0, preans_slot3, preans_slot4
- sincere: preans_slot2, preans_slot3, preans_slot4
- superficially: preans_slot1, preans_slot2, preans_slot4
- technically: preans_slot1, preans_slot2, preans_slot3, preans_slot4
- tell the truth: preans_slot1, preans_slot2, preans_slot4
- transparent: preans_slot1, preans_slot2, preans_slot4
- truth: preans_slot0, preans_slot1, preans_slot2, preans_slot3, preans_slot4
- truthful: preans_slot1, preans_slot2, preans_slot4
- violate: preans_slot1, preans_slot2, preans_slot4
- withhold: preans_slot1, preans_slot2, preans_slot4

## Candidate opposite pairs (same position, lie side vs truth side, antonym words in the names or glosses; merged list)

- preans_slot1: conceal / disclose
- preans_slot1: conceal / reveal
- preans_slot1: cover up / transparent
- preans_slot1: deny / admit
- preans_slot1: deny / confess
- preans_slot1: evade / admit
- preans_slot1: fake / real / genuine
- preans_slot1: hide / admit
- preans_slot1: hide / confess
- preans_slot1: hide / disclose
- preans_slot1: hide / reveal
- preans_slot1: lie / honest
- preans_slot1: lie / tell the truth
- preans_slot1: lie / truth
- preans_slot1: lie / truthful
- preans_slot1: mislead / candid
- preans_slot1: mislead / candid / frank
- preans_slot2: conceal / disclose
- preans_slot2: conceal / reveal
- preans_slot2: confidential / admit
- preans_slot2: confidential / confess
- preans_slot2: cover up / transparent
- preans_slot2: deny / admit
- preans_slot2: deny / confess
- preans_slot2: disguise / sincere
- preans_slot2: evade / admit
- preans_slot2: fake / real / genuine
- preans_slot2: hide / admit
- preans_slot2: hide / confess
- preans_slot2: hide / disclose
- preans_slot2: hide / reveal
- preans_slot2: lie / honest
- preans_slot2: lie / tell the truth
- preans_slot2: lie / truth
- preans_slot2: lie / truthful
- preans_slot2: mislead / candid
- preans_slot2: secret / candid
- preans_slot2: secret / transparent
- preans_slot4: conceal / disclose
- preans_slot4: cover up / transparent
- preans_slot4: deny / admit
- preans_slot4: dishonest / honest
- preans_slot4: evade / admit
- preans_slot4: lie / honest
- preans_slot4: lie / tell the truth
- preans_slot4: lie / truth
- preans_slot4: lie / truthful
- preans_slot4: mislead / candid
- preans_slot4: mislead / candid / frank
- preans_slot4: secret / candid
- preans_slot4: secret / transparent

Merged candidate list: `qwen3_6_27b_LL_Q1_bare_preans_merged.json` (183 families; replicate-2 families sharing at least half
their members with a replicate-1 family at the same position are folded into it).
