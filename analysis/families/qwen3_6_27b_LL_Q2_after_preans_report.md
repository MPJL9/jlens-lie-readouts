# Family report: qwen3.6-27b, logit lens, band 35-58, part Q2_after, group preans

Written by `scripts/family_report.py` from `qwen3_6_27b_LL_Q2_after_preans_rep1.json` and `_rep2.json` (prompt
`prompts/family_generation.md`). Visibility = build-split scenario transcripts (of 233) in which
at least one member is present at the position within the band. Layer profile = band layers where
the family is present in at least one transcript, and the three layers with the most transcripts
(description only; scoring uses the whole band).

## preans_slot0

| rep | family | side | members | visibility | layer profile |
|---|---|---|---|---|---|
| 1 | knowing (with knowledge; knowingly) | unclear | `明知` | 7 | L43-43; most at L43 (7) |
| 1 | ethics (ethics; morality) | unclear | `伦理` | 1 | L35-36; most at L35 (1), L36 (1) |
| 1 | perfunctory (dealing with something perfunctorily) | unclear | `应付` | 1 | L53-53; most at L53 (1) |
| 1 | admit (admitting) | truth | `承认` | 2 | L37-41; most at L37 (2), L38 (1), L39 (2) |
| 1 | integrity (integrity; uprightness) | truth | `正直` | 2 | L47-47; most at L47 (2) |
| 1 | objective (objectivity) | unclear | `客观` | 60 | L41-45; most at L41 (26), L43 (60), L44 (37) |
| 1 | law-abiding (abiding by the law) | unclear | `守法` | 2 | L47-47; most at L47 (2) |
| 2 | knowingly (with knowledge of the truth) | lie | `明知` | 7 | L43-43; most at L43 (7) |
| 2 | integrity (integrity, uprightness) | truth | `正直` | 2 | L47-47; most at L47 (2) |
| 2 | candid / frank (candid, frank, straightforward) | truth | `␣blunt` | 3 | L46-46; most at L46 (3) |
| 2 | admit (admitting) | truth | `承认` | 2 | L37-41; most at L37 (2), L38 (1), L39 (2) |
| 2 | ethics (ethics, morality) | unclear | `伦理` | 1 | L35-36; most at L35 (1), L36 (1) |
| 2 | law-abiding / compliant (following law or rules) | unclear | `守法` | 2 | L47-47; most at L47 (2) |

## preans_slot1

| rep | family | side | members | visibility | layer profile |
|---|---|---|---|---|---|
| 1 | lie (telling a lie) | lie | `谎言`, `撒谎`, `说谎`, `谎`, `␣lies`, `␣lie`, `␣lied`, `␣lying`, `lying`, `␣mentira`, `␣거짓`, `␣Lie`, `␣liar`, `Lie`, `lie`, `lies`, `␣Lies` | 153 | L35-58; most at L39 (141), L40 (130), L41 (107) |
| 1 | conceal (concealing information) | lie | `隐瞒`, `␣conceal`, `␣concealed`, `瞒` | 187 | L35-58; most at L39 (148), L40 (149), L50 (170) |
| 1 | hide (hiding; being hidden) | lie | `␣hiding`, `_hide`, `␣hide`, `隐藏`, `-hide`, `Hide`, `␣hides`, `hide`, `␣Hide`, `␣hidden`, `隐匿` | 41 | L35-58; most at L52 (15), L53 (25), L58 (13) |
| 1 | cover up (covering up or masking something) | lie | `掩盖`, `掩饰`, `掩`, `遮盖`, `␣masking`, `遮住`, `遮掩`, `掩护`, `遮蔽`, `␣cover`, `␣masked`, `mask`, `cover`, `␣Cover` | 147 | L35-58; most at L36 (115), L50 (116), L52 (106) |
| 1 | withhold (withholding information) | lie | `␣withholding`, `␣withhold`, `␣withheld` | 43 | L36-58; most at L52 (34), L53 (35), L54 (17) |
| 1 | omit (leaving something out) | lie | `␣omit`, `␣omission`, `omit`, `省略`, `␣omitted`, `␣OMIT` | 56 | L36-58; most at L50 (37), L52 (42), L53 (32) |
| 1 | secret (secrecy; something kept secret) | lie | `秘密` | 1 | L43-44; most at L43 (1), L44 (1) |
| 1 | mislead (misleading someone) | lie | `␣misleading`, `误导`, `误导性` | 101 | L35-58; most at L50 (54), L53 (86), L54 (69) |
| 1 | misinformation (false information) | lie | `␣misinformation`, `虚假信息` | 85 | L35-58; most at L51 (31), L53 (62), L54 (36) |
| 1 | fabricate (making something up) | lie | `虚构`, `␣fabricated`, `␣fabrication`, `凭空`, `␣invented`, `␣invent`, `伪造`, `␣invention`, `invent`, `␣inventions`, `␣Invent` | 127 | L35-58; most at L36 (103), L37 (102), L45 (91) |
| 1 | fake (faking; fake) | lie | `fake`, `␣fake`, `作假` | 47 | L35-47; most at L36 (28), L37 (39), L38 (37) |
| 1 | pretend (pretending; disguise) | lie | `伪装`, `␣pretending` | 4 | L35-49; most at L35 (2), L36 (1), L49 (1) |
| 1 | coax / fool (coaxing or fooling someone) | lie | `哄` | 38 | L35-43; most at L35 (26), L37 (16), L38 (13) |
| 1 | distort (distorting) | lie | `␣distortion`, `␣distort`, `␣distorted` | 2 | L58-58; most at L58 (2) |
| 1 | manipulate (manipulating) | lie | `␣manipulated`, `␣manipulation` | 2 | L49-50; most at L49 (2), L50 (1) |
| 1 | exaggerate (exaggerating) | lie | `夸大`, `␣exaggerated` | 15 | L35-58; most at L36 (12), L37 (8), L40 (8) |
| 1 | downplay (downplaying or glossing over) | lie | `淡化`, `␣gloss` | 62 | L35-58; most at L48 (33), L50 (36), L52 (27) |
| 1 | evade (evading) | lie | `␣evasion`, `回避`, `␣evade` | 37 | L38-58; most at L51 (22), L52 (25), L53 (21) |
| 1 | vague (being vague or ambiguous) | unclear | `␣vague`, `模糊`, `含糊`, `␣vaguely` | 33 | L37-58; most at L51 (20), L53 (27), L56 (23) |
| 1 | euphemism (saying something indirectly or tactfully) | unclear | `委婉` | 27 | L35-51; most at L35 (18), L37 (20), L40 (20) |
| 1 | imply (implying; implicit) | unclear | `暗示`, `␣implying`, `␣imply`, `␣implies`, `␣implied`, `隐含`, `␣implication`, `␣implicitly`, `␣implicit`, `␣implications`, `␣implic`, `␣implica`, `implicitly` | 40 | L35-58; most at L45 (20), L54 (27), L55 (19) |
| 1 | ostensibly (on the surface; ostensibly) | unclear | `表面上` | 25 | L35-45; most at L36 (13), L37 (14), L38 (15) |
| 1 | deny (denying) | lie | `否认`, `␣denying`, `␣denial`, `␣deny`, `␣denies`, `␣denied`, `否認`, `deny`, `␣Denied` | 83 | L35-58; most at L52 (51), L55 (56), L56 (53) |
| 1 | refuse (refusing or declining) | unclear | `␣refusal`, `拒绝`, `␣refusing`, `␣refused`, `␣refuse`, `␣refuses`, `␣refus`, `拒`, `拒絕`, `拒绝了`, `␣отказ`, `␣decline`, `␣declining`, `␣отказа`, `␣declined`, `␣declines`, `拒不` | 30 | L36-58; most at L51 (25), L53 (25), L56 (26) |
| 1 | deliberate (doing something on purpose) | unclear | `␣deliberately`, `故意`, `␣intentionally`, `刻意`, `␣deliberate`, `有意`, `␣intentional` | 88 | L35-58; most at L36 (57), L52 (34), L54 (43) |
| 1 | knowing (with knowledge; knowingly) | unclear | `明知`, `知情`, `␣knowingly`, `␣knowing`, `␣Knowing`, `Knowing` | 187 | L35-58; most at L44 (147), L45 (147), L47 (149) |
| 1 | unaware (without knowledge) | unclear | `不知情` | 1 | L38-38; most at L38 (1) |
| 1 | contradict (contradicting; contradiction) | unclear | `␣contradict`, `␣contrad`, `矛盾`, `␣contradictory`, `␣contradiction`, `␣contradictions`, `矛盾的` | 79 | L35-58; most at L49 (58), L50 (47), L54 (53) |
| 1 | contrary (the opposite; contrary) | unclear | `␣contrary`, `相反`, `相反的` | 58 | L35-58; most at L47 (24), L48 (24), L49 (30) |
| 1 | violate (violating a rule or principle) | unclear | `违背`, `违反`, `违反了`, `␣violates` | 45 | L35-58; most at L48 (27), L49 (41), L50 (23) |
| 1 | ethics (ethics; morality) | unclear | `␣ethical`, `␣ethics`, `伦理`, `道德` | 6 | L38-58; most at L52 (2), L54 (2), L58 (4) |
| 1 | blame (blaming) | unclear | `␣blame`, `␣blames`, `␣blamed` | 19 | L50-58; most at L54 (19), L55 (15), L56 (12) |
| 1 | framing (framing / spin) | unclear | `␣framing` | 17 | L39-58; most at L51 (5), L52 (8), L58 (12) |
| 1 | perfunctory (dealing with something perfunctorily) | unclear | `应付` | 51 | L35-47; most at L35 (32), L36 (28), L37 (36) |
| 1 | official line (an agreed messaging line) | unclear | `口径` | 26 | L35-57; most at L51 (17), L52 (11), L53 (17) |
| 1 | honest (honesty) | truth | `诚实`, `诚`, `␣honesty`, `␣honest`, `诚信`, `␣honestly`, `␣Honest`, `诚实守信` | 86 | L35-58; most at L39 (48), L40 (51), L41 (51) |
| 1 | truthful (telling the truth) | truth | `␣truthful`, `如实`, `实话`, `实事求是`, `说实话` | 206 | L35-58; most at L39 (168), L40 (157), L41 (139) |
| 1 | truth (the truth) | truth | `␣truth`, `truth`, `真相`, `␣Truth`, `Truth`, `实情`, `␣truths`, `_truth`, `真理` | 209 | L35-58; most at L39 (179), L40 (181), L41 (176) |
| 1 | candid (being candid or frank) | truth | `坦诚` | 18 | L37-56; most at L41 (11), L42 (11), L52 (10) |
| 1 | confess (confessing) | truth | `坦白`, `如实供述` | 14 | L36-55; most at L51 (10), L52 (10), L54 (5) |
| 1 | admit (admitting) | truth | `承认`, `␣admissions`, `␣admitting`, `␣admission`, `␣admits`, `␣admit`, `␣admitted`, `␣Admission`, `␣admite` | 37 | L35-58; most at L47 (14), L55 (18), L56 (16) |
| 1 | disclose (disclosing or revealing) | truth | `信息披露`, `揭露`, `␣disclosure`, `公开`, `披露`, `揭`, `␣disclose`, `␣disclosed`, `揭示`, `␣disclosures`, `␣Disclosure`, `␣reveal`, `␣revealing`, `揭示了` | 34 | L35-58; most at L36 (18), L37 (12), L38 (13) |
| 1 | transparent (transparency) | truth | `透明`, `-transparent`, `␣transparency`, `␣transparent`, `透明的`, `透明度`, `␣Transparency` | 16 | L38-58; most at L47 (11), L48 (11), L54 (13) |
| 1 | clarify (clarifying) | unclear | `澄清`, `␣clarify`, `␣clarification` | 12 | L36-58; most at L51 (6), L52 (7), L53 (9) |
| 1 | integrity (integrity; uprightness) | truth | `正直` | 4 | L52-54; most at L52 (2), L53 (3), L54 (1) |
| 1 | good faith (good faith) | truth | `善意` | 1 | L39-39; most at L39 (1) |
| 1 | objective (objectivity) | unclear | `客观`, `␣objectively` | 71 | L35-53; most at L35 (51), L36 (43), L44 (23) |
| 1 | comply (complying with rules or instructions) | unclear | `␣adherence`, `遵循`, `␣adher`, `␣compliance`, `合规` | 14 | L38-58; most at L53 (5), L54 (10), L56 (4) |
| 1 | role-play (playing a role or persona) | unclear | `␣persona`, `␣personas`, `␣Persona`, `Persona`, `persona`, `␣Personas`, `扮演`, `角色扮演` | 2 | L51-58; most at L52 (2), L56 (2), L57 (2) |
| 1 | simulate (simulating) | unclear | `模拟` | 1 | L35-50; most at L35 (1), L36 (1), L37 (1) |
| 1 | fiction (fiction; fictional) | unclear | `␣fictional`, `fiction`, `␣fiction` | 28 | L35-58; most at L36 (14), L44 (14), L45 (12) |
| 1 | fact (fact(s); factual) | unclear | `事实`, `␣fact`, `␣factual`, `事实上`, `␣facts`, `事实和`, `的事实`, `␣Fact`, `Fact`, `fact`, `␣Facts`, `␣FACT`, `facts`, `FACT`, `_fact`, `认定事实` | 216 | L35-58; most at L40 (189), L41 (192), L46 (191) |
| 1 | reality (reality; the actual situation) | unclear | `实际情况`, `实际上`, `与实际`, `␣reality`, `根据实际情况`, `实际上是`, `␣Reality`, `Reality`, `但实际上` | 77 | L35-58; most at L35 (54), L36 (39), L46 (38) |
| 2 | lie (telling a lie / a lie) | lie | `谎言`, `␣falsehood`, `撒谎`, `说谎`, `谎`, `␣lies`, `␣lie`, `␣lied`, `␣lying`, `lying`, `␣mentira`, `␣거짓`, `␣Lie`, `lie`, `lies`, `Lie`, `␣Lies` | 154 | L35-58; most at L39 (143), L40 (134), L41 (112) |
| 2 | misinformation (false information given out) | lie | `␣misinformation`, `虚假信息`, `不实` | 85 | L35-58; most at L51 (31), L53 (62), L54 (36) |
| 2 | fabricate (making something up) | lie | `␣fabricated`, `␣fabrication`, `␣invented`, `␣invent`, `伪造`, `␣invention`, `invent`, `␣inventions`, `␣Invent` | 92 | L35-58; most at L36 (64), L37 (86), L52 (36) |
| 2 | fake (fake, faked) | lie | `fake`, `␣fake`, `作假` | 47 | L35-47; most at L36 (28), L37 (39), L38 (37) |
| 2 | fiction (fictional, made-up story) | unclear | `虚构`, `␣fictional`, `fiction`, `␣fiction` | 114 | L35-58; most at L36 (92), L45 (91), L46 (88) |
| 2 | conceal (concealing the truth) | lie | `隐瞒`, `掩盖`, `掩饰`, `␣conceal`, `掩`, `␣concealed`, `瞒`, `遮掩`, `隐匿` | 190 | L35-58; most at L36 (152), L40 (152), L50 (172) |
| 2 | hide (hiding, hidden) | lie | `␣hiding`, `_hide`, `␣hide`, `隐藏`, `Hide`, `-hide`, `␣hides`, `hide`, `␣Hide`, `藏着`, `␣hidden`, `匿` | 42 | L35-58; most at L52 (15), L53 (25), L58 (13) |
| 2 | mask / cover up (covering something over) | lie | `遮盖`, `␣masking`, `遮住`, `掩护`, `遮蔽`, `␣masked`, `mask` | 42 | L35-58; most at L48 (31), L49 (27), L50 (29) |
| 2 | secret (secret, kept secret) | lie | `秘密`, `保密` | 2 | L36-44; most at L36 (1), L43 (1), L44 (1) |
| 2 | withhold (withholding information) | lie | `␣withholding`, `␣withhold`, `␣withheld` | 43 | L36-58; most at L52 (34), L53 (35), L54 (17) |
| 2 | omit (leaving something out) | lie | `␣omit`, `␣omission`, `omit`, `省略`, `␣omitted`, `␣OMIT` | 56 | L36-58; most at L50 (37), L52 (42), L53 (32) |
| 2 | mislead (misleading) | lie | `␣misleading`, `误导`, `误导性` | 101 | L35-58; most at L50 (54), L53 (86), L54 (69) |
| 2 | deny (denying) | lie | `否认`, `␣denying`, `␣denial`, `␣deny`, `␣denies`, `␣denied`, `否認`, `deny`, `␣Denied` | 83 | L35-58; most at L52 (51), L55 (56), L56 (53) |
| 2 | refuse (refusing, declining) | unclear | `␣refusal`, `拒绝`, `␣refusing`, `␣refused`, `␣refuse`, `␣refuses`, `␣refus`, `拒`, `拒絕`, `拒绝了`, `␣decline`, `␣declining`, `␣declined`, `␣declines`, `拒不` | 30 | L36-58; most at L51 (25), L53 (25), L56 (26) |
| 2 | evade (evading, dodging) | lie | `␣evasion`, `回避`, `␣dodge`, `␣evade` | 37 | L38-58; most at L51 (22), L52 (25), L53 (21) |
| 2 | vague (vague, ambiguous wording) | lie | `␣vague`, `模糊`, `含糊`, `␣vaguely` | 33 | L37-58; most at L51 (20), L53 (27), L56 (23) |
| 2 | imply / indirect (implying rather than stating) | unclear | `间接`, `暗示`, `␣implying`, `␣imply`, `␣implies`, `␣implied`, `隐含`, `␣implication`, `␣indirect`, `␣implicitly`, `␣indirectly`, `␣implicit`, `␣implications`, `␣implic`, `含蓄`, `␣implica`, `implicitly` | 59 | L35-58; most at L44 (28), L47 (29), L54 (28) |
| 2 | euphemistic (softened, euphemistic wording) | unclear | `委婉` | 27 | L35-51; most at L35 (18), L37 (20), L40 (20) |
| 2 | downplay (downplaying, glossing over) | lie | `淡化`, `␣gloss` | 62 | L35-58; most at L48 (33), L50 (36), L52 (27) |
| 2 | exaggerate (exaggerating) | lie | `夸大`, `␣exaggerated` | 15 | L35-58; most at L36 (12), L37 (8), L40 (8) |
| 2 | distort (distorting) | lie | `扭曲`, `␣distortion`, `␣distort`, `␣distorted` | 3 | L56-58; most at L56 (1), L57 (1), L58 (3) |
| 2 | spin (putting a spin on facts) | lie | `␣spin`, `Spin`, `-spin`, `␣Spin`, `␣spins`, `spin`, `␣spinning`, `_spin` | 7 | L54-58; most at L54 (2), L55 (2), L58 (7) |
| 2 | framing (framing of the message) | unclear | `␣framing` | 17 | L39-58; most at L51 (5), L52 (8), L58 (12) |
| 2 | official line (the agreed messaging line (口径)) | unclear | `口径` | 26 | L35-57; most at L51 (17), L52 (11), L53 (17) |
| 2 | manipulate (manipulating) | lie | `␣manipulated`, `␣manipulation` | 2 | L49-50; most at L49 (2), L50 (1) |
| 2 | trick / coax (tricking or coaxing someone) | lie | `哄` | 38 | L35-43; most at L35 (26), L37 (16), L38 (13) |
| 2 | pretend / disguise (pretending, disguising) | lie | `伪装`, `␣pretending` | 4 | L35-49; most at L35 (2), L36 (1), L49 (1) |
| 2 | contradict (contradicting) | unclear | `␣contradict`, `␣contrad`, `矛盾`, `␣contradictory`, `␣contradiction`, `␣contradictions`, `矛盾的` | 79 | L35-58; most at L49 (58), L50 (47), L54 (53) |
| 2 | deliberate (doing it on purpose) | lie | `␣deliberately`, `故意`, `␣intentionally`, `刻意`, `␣deliberate`, `␣intentional` | 88 | L35-58; most at L36 (57), L52 (34), L54 (43) |
| 2 | knowingly (with knowledge of the truth) | lie | `明知`, `␣knowingly`, `␣knowing`, `␣Knowing`, `Knowing` | 180 | L35-58; most at L44 (147), L45 (147), L47 (147) |
| 2 | violate (going against (rules or facts)) | unclear | `违背`, `违反`, `违反了` | 45 | L35-58; most at L48 (27), L49 (41), L50 (23) |
| 2 | claim (claiming) | unclear | `声称`, `␣claim`, `␣claims`, `␣claiming`, `claim`, `␣Claim`, `␣claimed`, `␣Claims`, `Claim`, `claims`, `␣CLAIM`, `Claims`, `CLAIM` | 43 | L35-58; most at L51 (32), L55 (25), L58 (31) |
| 2 | honest (honest, honesty) | truth | `诚实`, `诚`, `␣honesty`, `␣honest`, `␣honestly`, `␣Honest`, `诚实守信` | 85 | L35-58; most at L39 (47), L40 (50), L41 (50) |
| 2 | integrity (integrity, uprightness) | truth | `诚信`, `正直` | 18 | L35-54; most at L39 (9), L40 (12), L41 (14) |
| 2 | candid / frank (candid, frank, straightforward) | truth | `坦诚`, `␣straightforward`, `␣blunt`, `直言` | 21 | L37-57; most at L41 (11), L42 (11), L52 (13) |
| 2 | truthful (telling the truth) | truth | `␣truthful`, `如实`, `实话`, `说实话`, `如实供述` | 203 | L35-58; most at L39 (167), L40 (156), L41 (138) |
| 2 | truth (the truth) | truth | `␣truth`, `truth`, `真相`, `␣Truth`, `Truth`, `实情`, `␣truths`, `_truth` | 209 | L35-58; most at L39 (179), L40 (181), L41 (176) |
| 2 | fact (facts, the actual situation) | unclear | `事实`, `␣fact`, `␣factual`, `事实上`, `实际情况`, `␣facts`, `事实和`, `的事实`, `␣Fact`, `Fact`, `根据实际情况`, `␣Facts`, `␣FACT`, `fact`, `facts`, `_fact`, `FACT`, `认定事实` | 217 | L35-58; most at L40 (191), L41 (193), L46 (191) |
| 2 | admit (admitting) | truth | `承认`, `␣admissions`, `␣admitting`, `␣admission`, `␣admits`, `␣admit`, `␣admitted`, `␣Admission`, `承認`, `␣admite` | 37 | L35-58; most at L47 (14), L55 (18), L56 (16) |
| 2 | confess (confessing, owning up) | truth | `坦白` | 13 | L39-55; most at L51 (10), L52 (10), L54 (5) |
| 2 | disclose (disclosing information) | truth | `信息披露`, `␣disclosure`, `披露`, `␣disclose`, `␣disclosed`, `␣disclosures`, `␣Disclosure`, `透露` | 23 | L35-58; most at L36 (16), L37 (11), L38 (13) |
| 2 | reveal (revealing, exposing) | truth | `揭露`, `揭`, `揭示`, `␣reveal`, `␣revealing`, `揭示了`, `␣exposing` | 12 | L35-58; most at L47 (6), L48 (5), L53 (4) |
| 2 | make public (making public, announcing) | truth | `公开` | 5 | L37-50; most at L38 (2), L44 (1), L47 (2) |
| 2 | leak (leaking information) | unclear | `泄露` | 1 | L37-37; most at L37 (1) |
| 2 | transparent (transparent) | truth | `透明`, `-transparent`, `␣transparency`, `␣transparent`, `透明的`, `透明度`, `␣Transparency` | 16 | L38-58; most at L47 (11), L48 (11), L54 (13) |
| 2 | correct (fix) (correcting an error) | truth | `纠正`, `␣corrected`, `␣correction`, `␣correcting`, `␣corrective`, `␣corrections`, `␣Correction`, `Correction`, `␣Corrections`, `_correction` | 26 | L40-58; most at L52 (20), L53 (25), L54 (20) |
| 2 | clarify (clarifying) | truth | `澄清`, `␣clarify`, `␣clarification` | 12 | L36-58; most at L51 (6), L52 (7), L53 (9) |
| 2 | ethics (ethics, morality) | unclear | `␣ethical`, `␣ethics`, `伦理`, `道德` | 6 | L38-58; most at L52 (2), L54 (2), L58 (4) |
| 2 | good faith (good intent) | unclear | `善意` | 1 | L39-39; most at L39 (1) |
| 2 | law-abiding / compliant (following law or rules) | unclear | `合规` | 1 | L38-38; most at L38 (1) |
| 2 | role-play / simulate (playing a role, simulating) | unclear | `扮演`, `角色扮演`, `模拟` | 2 | L35-52; most at L35 (1), L36 (1), L37 (1) |

## preans_slot2

| rep | family | side | members | visibility | layer profile |
|---|---|---|---|---|---|
| 1 | lie (telling a lie) | lie | `谎言`, `␣lie`, `␣lying`, `␣lies`, `␣lied`, `撒谎`, `说谎`, `lying`, `␣Lie`, `␣Lies`, `谎`, `␣mentira` | 7 | L39-58; most at L51 (3), L55 (4), L56 (4) |
| 1 | dishonest (not honest) | lie | `␣dishonest` | 1 | L51-51; most at L51 (1) |
| 1 | conceal (concealing information) | lie | `隐瞒`, `␣concealed`, `␣conceal`, `瞒` | 57 | L35-55; most at L35 (29), L36 (28), L40 (36) |
| 1 | hide (hiding; being hidden) | lie | `␣hidden`, `隐藏`, `隐藏的`, `隐藏着`, `␣hiding`, `隐蔽`, `Hidden` | 26 | L35-58; most at L36 (8), L55 (10), L56 (12) |
| 1 | cover up (covering up or masking something) | lie | `掩盖`, `掩`, `␣masking` | 11 | L35-51; most at L36 (8), L37 (6), L40 (4) |
| 1 | withhold (withholding information) | lie | `␣withholding`, `␣withheld` | 5 | L36-53; most at L51 (1), L52 (2), L53 (4) |
| 1 | omit (leaving something out) | lie | `␣omit`, `␣omitted` | 1 | L49-53; most at L49 (1), L50 (1), L51 (1) |
| 1 | secret (secrecy; something kept secret) | lie | `␣secret`, `私下`, `秘密`, `的秘密`, `secret`, `␣Secret`, `␣secretly`, `-secret`, `␣confidential`, `Secret`, `_secret`, `␣Confidential` | 49 | L35-58; most at L43 (23), L44 (24), L56 (21) |
| 1 | mislead (misleading someone) | lie | `误导`, `␣misleading` | 8 | L35-55; most at L50 (4), L53 (3), L54 (2) |
| 1 | misinformation (false information) | lie | `␣misinformation` | 1 | L53-53; most at L53 (1) |
| 1 | fabricate (making something up) | lie | `虚构`, `伪造`, `␣fabrication` | 54 | L35-58; most at L36 (24), L37 (29), L40 (28) |
| 1 | fake (faking; fake) | lie | `fake`, `␣fake`, `Fake`, `作假` | 8 | L35-42; most at L36 (6), L37 (4), L38 (4) |
| 1 | pretend (pretending; disguise) | lie | `伪装` | 2 | L35-36; most at L35 (1), L36 (1) |
| 1 | trick (tricking someone) | lie | `␣trick`, `␣tricks`, `␣Trick` | 1 | L35-58; most at L35 (1), L36 (1), L50 (1) |
| 1 | coax / fool (coaxing or fooling someone) | lie | `哄` | 7 | L35-49; most at L36 (3), L37 (5), L42 (3) |
| 1 | manipulate (manipulating) | lie | `␣manipulated`, `␣manipulation`, `␣manipulate`, `␣manipulating`, `操纵` | 1 | L35-58; most at L35 (1), L36 (1), L37 (1) |
| 1 | downplay (downplaying or glossing over) | lie | `淡化` | 1 | L36-36; most at L36 (1) |
| 1 | euphemism (saying something indirectly or tactfully) | unclear | `委婉` | 8 | L35-37; most at L35 (6), L37 (2) |
| 1 | imply (implying; implicit) | unclear | `␣implied`, `␣implicit`, `␣implicitly`, `暗示`, `隐含` | 3 | L41-57; most at L47 (2), L50 (2), L54 (1) |
| 1 | ostensibly (on the surface; ostensibly) | unclear | `表面上` | 27 | L35-45; most at L36 (10), L37 (14), L38 (15) |
| 1 | deny (denying) | lie | `否认`, `␣deny`, `␣denying`, `␣denial`, `␣denies`, `␣denied` | 6 | L35-58; most at L44 (4), L45 (5), L47 (5) |
| 1 | refuse (refusing or declining) | unclear | `拒绝`, `␣refusal`, `␣refused`, `␣refuses`, `拒`, `␣refusing`, `␣refuse`, `␣refus`, `拒絕`, `拒绝了`, `拒不`, `␣отказ`, `␣decline`, `␣declining`, `␣declines`, `␣отказа`, `␣declined` | 6 | L35-58; most at L42 (5), L44 (5), L45 (5) |
| 1 | deliberate (doing something on purpose) | unclear | `故意`, `␣intentionally`, `刻意`, `␣deliberately`, `␣intentional`, `␣deliberate`, `故意的` | 58 | L35-58; most at L35 (41), L36 (43), L37 (24) |
| 1 | knowing (with knowledge; knowingly) | unclear | `明知`, `知情`, `␣knowing`, `␣knowingly`, `␣Knowing`, `Knowing` | 123 | L35-58; most at L47 (77), L48 (75), L49 (78) |
| 1 | contradict (contradicting; contradiction) | unclear | `矛盾`, `矛盾的`, `␣contrad`, `␣contradict`, `␣contradictory` | 37 | L35-58; most at L45 (15), L47 (15), L49 (16) |
| 1 | contrary (the opposite; contrary) | unclear | `␣contrary`, `相反` | 8 | L42-50; most at L43 (3), L44 (4), L45 (8) |
| 1 | violate (violating a rule or principle) | unclear | `违背`, `违反`, `违反了`, `␣violates`, `␣violated`, `␣violate` | 36 | L35-57; most at L35 (15), L48 (15), L50 (14) |
| 1 | unethical (unethical) | lie | `␣unethical` | 6 | L51-58; most at L55 (4), L56 (3), L58 (4) |
| 1 | ethics (ethics; morality) | unclear | `␣ethical`, `伦理`, `道德`, `␣moral`, `␣ethics`, `␣morally`, `ethical`, `的道德`, `␣morals`, `␣Moral` | 17 | L35-58; most at L39 (10), L40 (10), L58 (6) |
| 1 | blame (blaming) | unclear | `␣blame`, `␣blames`, `␣blamed` | 2 | L35-58; most at L54 (2), L55 (2), L56 (2) |
| 1 | framing (framing / spin) | unclear | `␣framing` | 3 | L39-58; most at L39 (2), L40 (2), L58 (2) |
| 1 | perfunctory (dealing with something perfunctorily) | unclear | `应付` | 3 | L45-52; most at L49 (2), L51 (2), L52 (1) |
| 1 | official line (an agreed messaging line) | unclear | `口径` | 6 | L40-57; most at L51 (3), L52 (5), L53 (6) |
| 1 | honest (honesty) | truth | `诚实`, `诚`, `␣honest`, `␣honesty`, `诚信` | 32 | L35-53; most at L35 (15), L36 (16), L37 (19) |
| 1 | truthful (telling the truth) | truth | `如实`, `␣truthful`, `实话`, `实事求是` | 76 | L35-58; most at L35 (63), L36 (46), L37 (38) |
| 1 | truth (the truth) | truth | `␣truth`, `真相`, `实情`, `truth`, `␣Truth`, `真理`, `_truth`, `Truth`, `␣truths` | 120 | L35-58; most at L38 (103), L39 (104), L40 (108) |
| 1 | candid (being candid or frank) | truth | `坦诚` | 1 | L41-42; most at L41 (1), L42 (1) |
| 1 | admit (admitting) | truth | `承认`, `␣admitting`, `␣admits`, `␣admit`, `␣admitted`, `␣admission`, `␣admissions`, `␣Admission` | 22 | L35-58; most at L44 (13), L46 (12), L47 (14) |
| 1 | disclose (disclosing or revealing) | truth | `公开`, `␣disclosed`, `揭露`, `信息披露` | 12 | L35-50; most at L35 (3), L44 (4), L47 (4) |
| 1 | clarify (clarifying) | unclear | `澄清` | 1 | L35-37; most at L35 (1), L36 (1), L37 (1) |
| 1 | integrity (integrity; uprightness) | truth | `␣integrity` | 1 | L51-51; most at L51 (1) |
| 1 | good faith (good faith) | truth | `善意` | 2 | L35-40; most at L35 (1), L36 (1), L37 (1) |
| 1 | objective (objectivity) | unclear | `客观`, `␣objective`, `␣objectively`, `␣Objective` | 83 | L35-58; most at L35 (41), L36 (58), L37 (38) |
| 1 | comply (complying with rules or instructions) | unclear | `合规`, `␣compliance`, `遵循`, `␣adherence` | 17 | L35-58; most at L35 (12), L36 (6), L39 (7) |
| 1 | role-play (playing a role or persona) | unclear | `␣persona`, `␣personas`, `␣Persona`, `扮演`, `角色扮演`, `Persona`, `persona` | 69 | L35-58; most at L52 (54), L53 (64), L56 (62) |
| 1 | simulate (simulating) | unclear | `模拟`, `␣simulated`, `␣simulation`, `␣Simulation`, `Simulation` | 18 | L35-57; most at L36 (6), L40 (6), L51 (6) |
| 1 | fiction (fiction; fictional) | unclear | `␣fictional`, `fiction`, `␣Fiction`, `-fiction` | 48 | L35-58; most at L36 (24), L37 (27), L39 (24) |
| 1 | fact (fact(s); factual) | unclear | `␣fact`, `事实`, `的事实`, `␣facts`, `␣factual`, `事实上`, `fact`, `␣Fact`, `facts`, `␣Facts`, `事实和`, `Fact`, `␣FACT`, `FACT`, `_fact`, `上述事实` | 138 | L35-58; most at L39 (115), L47 (111), L48 (111) |
| 1 | reality (reality; the actual situation) | unclear | `实际情况`, `␣reality`, `␣Reality`, `实际上`, `Reality`, `但实际上`, `与实际`, `实际上是`, `根据实际情况` | 116 | L35-58; most at L35 (94), L36 (96), L37 (98) |
| 2 | lie (telling a lie / a lie) | lie | `谎言`, `␣lie`, `␣lying`, `␣falsehood`, `␣lies`, `␣lied`, `撒谎`, `说谎`, `lying`, `␣Lie`, `␣Lies`, `谎`, `␣mentira` | 9 | L37-58; most at L51 (3), L55 (4), L56 (4) |
| 2 | misinformation (false information given out) | lie | `␣misinformation` | 1 | L53-53; most at L53 (1) |
| 2 | fabricate (making something up) | lie | `伪造`, `␣fabrication` | 2 | L50-58; most at L50 (1), L56 (1), L58 (1) |
| 2 | fake (fake, faked) | lie | `fake`, `␣fake`, `Fake`, `作假` | 8 | L35-42; most at L36 (6), L37 (4), L38 (4) |
| 2 | fiction (fictional, made-up story) | unclear | `虚构`, `␣fictional`, `fiction`, `␣Fiction`, `-fiction` | 69 | L35-58; most at L36 (36), L37 (38), L40 (33) |
| 2 | conceal (concealing the truth) | lie | `隐瞒`, `掩盖`, `␣concealed`, `␣conceal`, `掩`, `瞒` | 64 | L35-55; most at L35 (33), L36 (34), L40 (38) |
| 2 | hide (hiding, hidden) | lie | `匿`, `␣hidden`, `隐藏`, `隐藏的`, `隐藏着`, `␣hiding`, `隐蔽`, `Hidden` | 44 | L35-58; most at L35 (22), L36 (24), L56 (12) |
| 2 | mask / cover up (covering something over) | lie | `␣masking` | 1 | L51-51; most at L51 (1) |
| 2 | secret (secret, kept secret) | lie | `␣secret`, `秘密`, `的秘密`, `secret`, `␣Secret`, `␣secretly`, `保密`, `-secret`, `␣confidential`, `机密`, `Secret`, `_secret`, `␣Confidential` | 41 | L35-58; most at L35 (21), L36 (22), L56 (20) |
| 2 | private (private, done privately) | unclear | `私下`, `␣private`, `␣privately`, `private`, `␣Private`, `Private`, `PRIVATE`, `-private`, `_private`, `私密` | 35 | L35-58; most at L43 (21), L44 (23), L45 (20) |
| 2 | withhold (withholding information) | lie | `␣withholding`, `␣withheld` | 5 | L36-53; most at L51 (1), L52 (2), L53 (4) |
| 2 | omit (leaving something out) | lie | `␣omit`, `␣omitted` | 1 | L49-53; most at L49 (1), L50 (1), L51 (1) |
| 2 | mislead (misleading) | lie | `误导`, `␣misleading` | 8 | L35-55; most at L50 (4), L53 (3), L54 (2) |
| 2 | deny (denying) | lie | `否认`, `␣deny`, `␣denying`, `␣denies`, `␣denied`, `␣denial` | 6 | L35-58; most at L44 (4), L45 (5), L47 (5) |
| 2 | refuse (refusing, declining) | unclear | `拒绝`, `␣refusal`, `␣refused`, `␣refuses`, `拒`, `␣refusing`, `␣refuse`, `␣refus`, `拒絕`, `拒绝了`, `拒不`, `␣decline`, `␣declining`, `␣declines`, `␣declined` | 6 | L35-58; most at L42 (5), L44 (5), L45 (5) |
| 2 | imply / indirect (implying rather than stating) | unclear | `间接`, `␣implied`, `␣implicitly`, `␣implicit`, `暗示`, `隐含`, `␣indirect`, `␣indirectly` | 5 | L36-57; most at L41 (2), L47 (3), L50 (2) |
| 2 | euphemistic (softened, euphemistic wording) | unclear | `委婉` | 8 | L35-37; most at L35 (6), L37 (2) |
| 2 | downplay (downplaying, glossing over) | lie | `淡化` | 1 | L36-36; most at L36 (1) |
| 2 | distort (distorting) | lie | `扭曲` | 1 | L37-37; most at L37 (1) |
| 2 | spin (putting a spin on facts) | lie | `␣spin`, `Spin`, `␣Spin` | 1 | L55-58; most at L55 (1), L56 (1), L57 (1) |
| 2 | framing (framing of the message) | unclear | `␣framing` | 3 | L39-58; most at L39 (2), L40 (2), L58 (2) |
| 2 | official line (the agreed messaging line (口径)) | unclear | `口径` | 6 | L40-57; most at L51 (3), L52 (5), L53 (6) |
| 2 | manipulate (manipulating) | lie | `␣manipulated`, `␣manipulation`, `␣manipulate`, `␣manipulating`, `操纵` | 1 | L35-58; most at L35 (1), L36 (1), L37 (1) |
| 2 | trick / coax (tricking or coaxing someone) | lie | `哄`, `␣trick`, `␣tricks`, `␣Trick` | 8 | L35-58; most at L36 (4), L37 (5), L42 (3) |
| 2 | pretend / disguise (pretending, disguising) | lie | `伪装`, `装着` | 3 | L35-37; most at L35 (1), L36 (2), L37 (1) |
| 2 | fraud (fraud) | lie | `␣fraud` | 1 | L51-51; most at L51 (1) |
| 2 | dishonest (dishonest) | lie | `␣dishonest` | 1 | L51-51; most at L51 (1) |
| 2 | unethical (unethical) | lie | `␣unethical` | 6 | L51-58; most at L55 (4), L56 (3), L58 (4) |
| 2 | contradict (contradicting) | unclear | `矛盾`, `矛盾的`, `␣contrad`, `␣contradict`, `␣contradictory` | 37 | L35-58; most at L45 (15), L47 (15), L49 (16) |
| 2 | deliberate (doing it on purpose) | lie | `故意`, `␣intentionally`, `刻意`, `␣deliberately`, `␣intentional`, `␣deliberate`, `故意的` | 58 | L35-58; most at L35 (41), L36 (43), L37 (24) |
| 2 | knowingly (with knowledge of the truth) | lie | `明知`, `␣knowing`, `␣knowingly`, `␣Knowing`, `Knowing` | 118 | L35-58; most at L47 (77), L48 (75), L49 (77) |
| 2 | violate (going against (rules or facts)) | unclear | `违背`, `违反`, `违反了` | 36 | L35-57; most at L35 (15), L48 (15), L50 (14) |
| 2 | claim (claiming) | unclear | `␣claim`, `声称`, `␣claims`, `claim`, `␣claimed`, `␣claiming`, `␣Claim` | 9 | L35-58; most at L36 (3), L37 (4), L38 (3) |
| 2 | honest (honest, honesty) | truth | `诚实`, `诚`, `␣honest`, `␣honesty` | 31 | L35-53; most at L35 (15), L36 (16), L37 (19) |
| 2 | integrity (integrity, uprightness) | truth | `诚信`, `␣integrity` | 3 | L40-51; most at L40 (2), L51 (1) |
| 2 | candid / frank (candid, frank, straightforward) | truth | `坦诚` | 1 | L41-42; most at L41 (1), L42 (1) |
| 2 | truthful (telling the truth) | truth | `如实`, `␣truthful`, `实话` | 74 | L35-58; most at L35 (63), L36 (46), L37 (38) |
| 2 | truth (the truth) | truth | `␣truth`, `真相`, `实情`, `truth`, `␣Truth`, `真理`, `_truth`, `Truth`, `␣truths` | 120 | L35-58; most at L38 (103), L39 (104), L40 (108) |
| 2 | fact (facts, the actual situation) | unclear | `␣fact`, `事实`, `实际情况`, `的事实`, `␣facts`, `␣factual`, `事实上`, `fact`, `␣Fact`, `facts`, `␣Facts`, `事实和`, `Fact`, `␣FACT`, `_fact`, `FACT`, `根据实际情况`, `上述事实` | 142 | L35-58; most at L35 (121), L36 (122), L37 (124) |
| 2 | admit (admitting) | truth | `承认`, `␣admitting`, `␣admits`, `␣admit`, `␣admitted`, `␣admission`, `␣admissions`, `␣Admission` | 22 | L35-58; most at L44 (13), L46 (12), L47 (14) |
| 2 | disclose (disclosing information) | truth | `␣disclosed`, `信息披露` | 3 | L35-36; most at L35 (1), L36 (3) |
| 2 | reveal (revealing, exposing) | truth | `揭露` | 2 | L35-40; most at L35 (1), L39 (1), L40 (1) |
| 2 | make public (making public, announcing) | truth | `公开` | 9 | L35-50; most at L43 (3), L44 (4), L47 (4) |
| 2 | clarify (clarifying) | truth | `澄清` | 1 | L35-37; most at L35 (1), L36 (1), L37 (1) |
| 2 | ethics (ethics, morality) | unclear | `␣ethical`, `伦理`, `道德`, `␣moral`, `␣ethics`, `␣morally`, `ethical`, `的道德`, `␣morals`, `␣Moral` | 17 | L35-58; most at L39 (10), L40 (10), L58 (6) |
| 2 | good faith (good intent) | unclear | `善意` | 2 | L35-40; most at L35 (1), L36 (1), L37 (1) |
| 2 | law-abiding / compliant (following law or rules) | unclear | `合规` | 15 | L35-44; most at L35 (12), L36 (6), L39 (7) |
| 2 | role-play / simulate (playing a role, simulating) | unclear | `扮演`, `角色扮演`, `模拟`, `␣simulated`, `␣simulation`, `␣Simulation`, `Simulation` | 35 | L35-58; most at L51 (25), L52 (28), L56 (18) |

## preans_slot3

| rep | family | side | members | visibility | layer profile |
|---|---|---|---|---|---|
| 1 | secret (secrecy; something kept secret) | lie | `秘密`, `私下` | 2 | L47-47; most at L47 (2) |
| 1 | refuse (refusing or declining) | unclear | `␣refusal`, `␣refuse`, `拒`, `␣refusing`, `␣refus`, `拒绝` | 95 | L38-53; most at L47 (93), L48 (33), L51 (46) |
| 1 | violate (violating a rule or principle) | unclear | `违背` | 6 | L48-49; most at L48 (2), L49 (5) |
| 1 | ethics (ethics; morality) | unclear | `␣ethical`, `伦理` | 5 | L37-50; most at L43 (4), L47 (3), L48 (3) |
| 1 | sorry (apology) | unclear | `抱歉`, `␣sorry`, `Sorry`, `␣Sorry` | 44 | L48-57; most at L49 (11), L50 (22), L54 (29) |
| 1 | honest (honesty) | truth | `␣honestly` | 1 | L53-53; most at L53 (1) |
| 1 | confess (confessing) | truth | `坦白` | 18 | L49-53; most at L49 (10), L50 (13), L51 (8) |
| 1 | disclose (disclosing or revealing) | truth | `公布`, `公开` | 105 | L36-46; most at L37 (19), L43 (28), L44 (83) |
| 1 | clarify (clarifying) | unclear | `澄清` | 8 | L43-52; most at L49 (5), L51 (5), L52 (5) |
| 1 | law-abiding (abiding by the law) | unclear | `守法` | 110 | L42-44; most at L42 (2), L43 (110), L44 (4) |
| 1 | fiction (fiction; fictional) | unclear | `fiction` | 2 | L45-46; most at L45 (1), L46 (2) |
| 1 | fact (fact(s); factual) | unclear | `FACT` | 1 | L53-53; most at L53 (1) |
| 2 | fiction (fictional, made-up story) | unclear | `fiction` | 2 | L45-46; most at L45 (1), L46 (2) |
| 2 | secret (secret, kept secret) | lie | `秘密` | 1 | L47-47; most at L47 (1) |
| 2 | private (private, done privately) | unclear | `私下` | 1 | L47-47; most at L47 (1) |
| 2 | refuse (refusing, declining) | unclear | `␣refusal`, `␣refuse`, `拒`, `␣refusing`, `␣refus`, `拒绝` | 95 | L38-53; most at L47 (93), L48 (33), L51 (46) |
| 2 | spin (putting a spin on facts) | lie | `␣spin` | 1 | L38-38; most at L38 (1) |
| 2 | violate (going against (rules or facts)) | unclear | `违背` | 6 | L48-49; most at L48 (2), L49 (5) |
| 2 | honest (honest, honesty) | truth | `␣honestly` | 1 | L53-53; most at L53 (1) |
| 2 | fact (facts, the actual situation) | unclear | `FACT` | 1 | L53-53; most at L53 (1) |
| 2 | confess (confessing, owning up) | truth | `坦白` | 18 | L49-53; most at L49 (10), L50 (13), L51 (8) |
| 2 | make public (making public, announcing) | truth | `公布`, `公开` | 105 | L36-46; most at L37 (19), L43 (28), L44 (83) |
| 2 | clarify (clarifying) | truth | `澄清` | 8 | L43-52; most at L49 (5), L51 (5), L52 (5) |
| 2 | sorry (apologising) | unclear | `抱歉`, `␣sorry`, `Sorry`, `␣Sorry` | 44 | L48-57; most at L49 (11), L50 (22), L54 (29) |
| 2 | ethics (ethics, morality) | unclear | `␣ethical`, `伦理` | 5 | L37-50; most at L43 (4), L47 (3), L48 (3) |
| 2 | law-abiding / compliant (following law or rules) | unclear | `守法` | 110 | L42-44; most at L42 (2), L43 (110), L44 (4) |

## preans_slot4

| rep | family | side | members | visibility | layer profile |
|---|---|---|---|---|---|
| 1 | lie (telling a lie) | lie | `说谎` | 1 | L52-52; most at L52 (1) |
| 1 | dishonest (not honest) | lie | `␣dishonest` | 1 | L38-38; most at L38 (1) |
| 1 | conceal (concealing information) | lie | `隐瞒` | 8 | L36-52; most at L38 (4), L40 (4), L46 (5) |
| 1 | withhold (withholding information) | lie | `␣withholding`, `␣withhold` | 2 | L51-53; most at L51 (1), L52 (1), L53 (2) |
| 1 | fabricate (making something up) | lie | `虚构` | 40 | L35-58; most at L35 (32), L36 (28), L40 (28) |
| 1 | coax / fool (coaxing or fooling someone) | lie | `哄` | 1 | L39-39; most at L39 (1) |
| 1 | downplay (downplaying or glossing over) | lie | `淡化` | 10 | L35-37; most at L35 (1), L36 (10), L37 (1) |
| 1 | ostensibly (on the surface; ostensibly) | unclear | `表面上` | 21 | L36-43; most at L36 (18), L37 (16), L38 (12) |
| 1 | deny (denying) | lie | `否认` | 20 | L35-56; most at L45 (8), L47 (7), L48 (12) |
| 1 | refuse (refusing or declining) | unclear | `拒绝` | 4 | L39-50; most at L40 (3), L41 (3), L42 (3) |
| 1 | deliberate (doing something on purpose) | unclear | `␣intentionally`, `故意`, `␣deliberately`, `␣deliberate`, `故意的` | 32 | L35-51; most at L35 (25), L36 (11), L37 (10) |
| 1 | knowing (with knowledge; knowingly) | unclear | `明知` | 28 | L35-50; most at L35 (9), L47 (12), L48 (13) |
| 1 | contradict (contradicting; contradiction) | unclear | `␣contradict` | 1 | L50-50; most at L50 (1) |
| 1 | contrary (the opposite; contrary) | unclear | `相反`, `␣contrary` | 16 | L36-52; most at L36 (10), L41 (6), L42 (7) |
| 1 | violate (violating a rule or principle) | unclear | `违反`, `违背` | 9 | L35-46; most at L35 (3), L43 (2), L46 (5) |
| 1 | ethics (ethics; morality) | unclear | `␣ethical`, `伦理`, `道德`, `␣ethics`, `职业道德`, `␣moral` | 11 | L35-42; most at L37 (3), L39 (3), L40 (11) |
| 1 | official line (an agreed messaging line) | unclear | `口径` | 1 | L37-37; most at L37 (1) |
| 1 | sorry (apology) | unclear | `抱歉` | 10 | L36-50; most at L37 (6), L38 (4), L40 (3) |
| 1 | honest (honesty) | truth | `诚实`, `诚信`, `诚`, `␣honest`, `␣honesty`, `真诚`, `␣Honest` | 178 | L35-58; most at L37 (111), L38 (121), L40 (126) |
| 1 | truthful (telling the truth) | truth | `如实`, `实话`, `␣truthful`, `实事求是` | 75 | L35-58; most at L35 (56), L38 (39), L39 (34) |
| 1 | truth (the truth) | truth | `␣truth`, `truth`, `真相`, `␣Truth`, `真理` | 17 | L35-58; most at L35 (14), L40 (5), L41 (6) |
| 1 | candid (being candid or frank) | truth | `坦诚` | 37 | L35-45; most at L36 (13), L37 (20), L41 (13) |
| 1 | confess (confessing) | truth | `坦白` | 17 | L35-51; most at L36 (6), L37 (12), L50 (6) |
| 1 | admit (admitting) | truth | `承认` | 74 | L35-48; most at L35 (44), L40 (49), L46 (32) |
| 1 | disclose (disclosing or revealing) | truth | `信息披露`, `公开` | 4 | L37-46; most at L37 (1), L38 (3), L39 (2) |
| 1 | transparent (transparency) | truth | `透明的`, `透明`, `␣transparent`, `␣transparency` | 4 | L38-44; most at L38 (2), L43 (3), L44 (3) |
| 1 | clarify (clarifying) | unclear | `澄清` | 1 | L37-37; most at L37 (1) |
| 1 | integrity (integrity; uprightness) | truth | `正直` | 11 | L35-40; most at L35 (1), L36 (9), L40 (3) |
| 1 | good faith (good faith) | truth | `善意` | 23 | L35-42; most at L35 (14), L36 (14), L37 (6) |
| 1 | objective (objectivity) | unclear | `客观`, `␣objectively` | 86 | L35-45; most at L35 (47), L36 (60), L37 (30) |
| 1 | comply (complying with rules or instructions) | unclear | `合规`, `␣adher`, `遵循` | 54 | L35-54; most at L36 (26), L37 (35), L38 (31) |
| 1 | role-play (playing a role or persona) | unclear | `扮演`, `␣persona`, `␣personas`, `角色扮演`, `␣Persona`, `Persona`, `persona`, `扮演着` | 24 | L36-58; most at L40 (13), L44 (16), L45 (13) |
| 1 | simulate (simulating) | unclear | `模拟`, `␣simulated`, `␣simulation`, `␣simulate` | 34 | L35-58; most at L35 (25), L36 (21), L37 (20) |
| 1 | fiction (fiction; fictional) | unclear | `␣fictional`, `fiction` | 16 | L35-58; most at L36 (8), L37 (9), L40 (14) |
| 1 | fact (fact(s); factual) | unclear | `事实`, `␣factual`, `␣fact`, `␣Fact`, `Fact` | 17 | L35-50; most at L35 (7), L41 (6), L44 (6) |
| 2 | lie (telling a lie / a lie) | lie | `说谎`, `␣falsehood` | 1 | L52-57; most at L52 (1), L55 (1), L56 (1) |
| 2 | fiction (fictional, made-up story) | unclear | `虚构`, `␣fictional`, `fiction` | 40 | L35-58; most at L35 (33), L36 (29), L40 (28) |
| 2 | conceal (concealing the truth) | lie | `隐瞒` | 8 | L36-52; most at L38 (4), L40 (4), L46 (5) |
| 2 | secret (secret, kept secret) | lie | `保密` | 1 | L36-40; most at L36 (1), L37 (1), L40 (1) |
| 2 | withhold (withholding information) | lie | `␣withholding`, `␣withhold` | 2 | L51-53; most at L51 (1), L52 (1), L53 (2) |
| 2 | deny (denying) | lie | `否认` | 20 | L35-56; most at L45 (8), L47 (7), L48 (12) |
| 2 | refuse (refusing, declining) | unclear | `拒绝` | 4 | L39-50; most at L40 (3), L41 (3), L42 (3) |
| 2 | downplay (downplaying, glossing over) | lie | `淡化` | 10 | L35-37; most at L35 (1), L36 (10), L37 (1) |
| 2 | official line (the agreed messaging line (口径)) | unclear | `口径` | 1 | L37-37; most at L37 (1) |
| 2 | trick / coax (tricking or coaxing someone) | lie | `哄` | 1 | L39-39; most at L39 (1) |
| 2 | dishonest (dishonest) | lie | `␣dishonest` | 1 | L38-38; most at L38 (1) |
| 2 | contradict (contradicting) | unclear | `␣contradict` | 1 | L50-50; most at L50 (1) |
| 2 | deliberate (doing it on purpose) | lie | `␣intentionally`, `故意`, `␣deliberately`, `␣deliberate`, `故意的` | 32 | L35-51; most at L35 (25), L36 (11), L37 (10) |
| 2 | knowingly (with knowledge of the truth) | lie | `明知` | 28 | L35-50; most at L35 (9), L47 (12), L48 (13) |
| 2 | violate (going against (rules or facts)) | unclear | `违反`, `违背` | 9 | L35-46; most at L35 (3), L43 (2), L46 (5) |
| 2 | honest (honest, honesty) | truth | `诚实`, `诚`, `␣honest`, `␣honesty`, `␣Honest` | 167 | L35-58; most at L37 (107), L38 (108), L40 (97) |
| 2 | integrity (integrity, uprightness) | truth | `诚信`, `正直` | 108 | L35-47; most at L38 (50), L40 (96), L41 (57) |
| 2 | sincere (sincere) | truth | `真诚` | 3 | L36-36; most at L36 (3) |
| 2 | candid / frank (candid, frank, straightforward) | truth | `坦诚` | 37 | L35-45; most at L36 (13), L37 (20), L41 (13) |
| 2 | truthful (telling the truth) | truth | `如实`, `实话`, `␣truthful` | 75 | L35-58; most at L35 (56), L38 (39), L39 (34) |
| 2 | truth (the truth) | truth | `␣truth`, `truth`, `真相`, `␣Truth` | 17 | L35-58; most at L35 (14), L40 (5), L41 (6) |
| 2 | fact (facts, the actual situation) | unclear | `事实`, `␣factual`, `␣fact`, `␣Fact`, `Fact` | 17 | L35-50; most at L35 (7), L41 (6), L44 (6) |
| 2 | admit (admitting) | truth | `承认` | 74 | L35-48; most at L35 (44), L40 (49), L46 (32) |
| 2 | confess (confessing, owning up) | truth | `坦白` | 17 | L35-51; most at L36 (6), L37 (12), L50 (6) |
| 2 | disclose (disclosing information) | truth | `信息披露` | 3 | L37-41; most at L37 (1), L38 (3), L39 (2) |
| 2 | make public (making public, announcing) | truth | `公开` | 1 | L46-46; most at L46 (1) |
| 2 | transparent (transparent) | truth | `透明的`, `透明`, `␣transparent`, `␣transparency` | 4 | L38-44; most at L38 (2), L43 (3), L44 (3) |
| 2 | clarify (clarifying) | truth | `澄清` | 1 | L37-37; most at L37 (1) |
| 2 | sorry (apologising) | unclear | `抱歉` | 10 | L36-50; most at L37 (6), L38 (4), L40 (3) |
| 2 | ethics (ethics, morality) | unclear | `␣ethical`, `伦理`, `道德`, `␣ethics`, `职业道德`, `␣moral` | 11 | L35-42; most at L37 (3), L39 (3), L40 (11) |
| 2 | good faith (good intent) | unclear | `善意` | 23 | L35-42; most at L35 (14), L36 (14), L37 (6) |
| 2 | law-abiding / compliant (following law or rules) | unclear | `合规` | 37 | L35-43; most at L36 (26), L37 (35), L38 (30) |
| 2 | fair (impartial) | unclear | `公正` | 9 | L35-41; most at L35 (4), L36 (7), L39 (2) |
| 2 | role-play / simulate (playing a role, simulating) | unclear | `模拟`, `扮演`, `␣simulated`, `角色扮演`, `␣simulation`, `扮演着`, `␣simulate` | 37 | L35-58; most at L35 (25), L36 (21), L37 (20) |

## Replicate overlap

For each replicate-1 family, the replicate-2 family at the same position sharing the most members.

| position | rep-1 family | best rep-2 family | Jaccard of member ids | only in rep 1 | only in rep 2 |
|---|---|---|---|---|---|
| preans_slot0 | knowing | knowingly | 1.00 | — | — |
| preans_slot0 | ethics | ethics | 1.00 | — | — |
| preans_slot0 | perfunctory | — | 0 | all | — |
| preans_slot0 | admit | admit | 1.00 | — | — |
| preans_slot0 | integrity | integrity | 1.00 | — | — |
| preans_slot0 | objective | — | 0 | all | — |
| preans_slot0 | law-abiding | law-abiding / compliant | 1.00 | — | — |
| preans_slot1 | lie | lie | 0.89 | `␣liar` | `␣falsehood` |
| preans_slot1 | conceal | conceal | 0.44 | — | `掩盖`, `掩饰`, `掩`, `遮掩`, `隐匿` |
| preans_slot1 | hide | hide | 0.77 | `隐匿` | `藏着`, `匿` |
| preans_slot1 | cover up | mask / cover up | 0.50 | `掩盖`, `掩饰`, `掩`, `遮掩`, `␣cover`, `cover`, `␣Cover` | — |
| preans_slot1 | withhold | withhold | 1.00 | — | — |
| preans_slot1 | omit | omit | 1.00 | — | — |
| preans_slot1 | secret | secret | 0.50 | — | `保密` |
| preans_slot1 | mislead | mislead | 1.00 | — | — |
| preans_slot1 | misinformation | misinformation | 0.67 | — | `不实` |
| preans_slot1 | fabricate | fabricate | 0.82 | `虚构`, `凭空` | — |
| preans_slot1 | fake | fake | 1.00 | — | — |
| preans_slot1 | pretend | pretend / disguise | 1.00 | — | — |
| preans_slot1 | coax / fool | trick / coax | 1.00 | — | — |
| preans_slot1 | distort | distort | 0.75 | — | `扭曲` |
| preans_slot1 | manipulate | manipulate | 1.00 | — | — |
| preans_slot1 | exaggerate | exaggerate | 1.00 | — | — |
| preans_slot1 | downplay | downplay | 1.00 | — | — |
| preans_slot1 | evade | evade | 0.75 | — | `␣dodge` |
| preans_slot1 | vague | vague | 1.00 | — | — |
| preans_slot1 | euphemism | euphemistic | 1.00 | — | — |
| preans_slot1 | imply | imply / indirect | 0.76 | — | `间接`, `␣indirect`, `␣indirectly`, `含蓄` |
| preans_slot1 | ostensibly | — | 0 | all | — |
| preans_slot1 | deny | deny | 1.00 | — | — |
| preans_slot1 | refuse | refuse | 0.88 | `␣отказ`, `␣отказа` | — |
| preans_slot1 | deliberate | deliberate | 0.86 | `有意` | — |
| preans_slot1 | knowing | knowingly | 0.83 | `知情` | — |
| preans_slot1 | unaware | — | 0 | all | — |
| preans_slot1 | contradict | contradict | 1.00 | — | — |
| preans_slot1 | contrary | — | 0 | all | — |
| preans_slot1 | violate | violate | 0.75 | `␣violates` | — |
| preans_slot1 | ethics | ethics | 1.00 | — | — |
| preans_slot1 | blame | — | 0 | all | — |
| preans_slot1 | framing | framing | 1.00 | — | — |
| preans_slot1 | perfunctory | — | 0 | all | — |
| preans_slot1 | official line | official line | 1.00 | — | — |
| preans_slot1 | honest | honest | 0.88 | `诚信` | — |
| preans_slot1 | truthful | truthful | 0.67 | `实事求是` | `如实供述` |
| preans_slot1 | truth | truth | 0.89 | `真理` | — |
| preans_slot1 | candid | candid / frank | 0.25 | — | `␣straightforward`, `␣blunt`, `直言` |
| preans_slot1 | confess | confess | 0.50 | `如实供述` | — |
| preans_slot1 | admit | admit | 0.90 | — | `承認` |
| preans_slot1 | disclose | disclose | 0.47 | `揭露`, `公开`, `揭`, `揭示`, `␣reveal`, `␣revealing`, `揭示了` | `透露` |
| preans_slot1 | transparent | transparent | 1.00 | — | — |
| preans_slot1 | clarify | clarify | 1.00 | — | — |
| preans_slot1 | integrity | integrity | 0.50 | — | `诚信` |
| preans_slot1 | good faith | good faith | 1.00 | — | — |
| preans_slot1 | objective | — | 0 | all | — |
| preans_slot1 | comply | law-abiding / compliant | 0.20 | `␣adherence`, `遵循`, `␣adher`, `␣compliance` | — |
| preans_slot1 | role-play | role-play / simulate | 0.22 | `␣persona`, `␣personas`, `␣Persona`, `Persona`, `persona`, `␣Personas` | `模拟` |
| preans_slot1 | simulate | role-play / simulate | 0.33 | — | `扮演`, `角色扮演` |
| preans_slot1 | fiction | fiction | 0.75 | — | `虚构` |
| preans_slot1 | fact | fact | 0.89 | — | `实际情况`, `根据实际情况` |
| preans_slot1 | reality | fact | 0.08 | `实际上`, `与实际`, `␣reality`, `实际上是`, `␣Reality`, `Reality`, `但实际上` | `事实`, `␣fact`, `␣factual`, `事实上`, `␣facts`, `事实和`, `的事实`, `␣Fact`, `Fact`, `␣Facts`, `␣FACT`, `fact`, `facts`, `_fact`, `FACT`, `认定事实` |
| preans_slot2 | lie | lie | 0.92 | — | `␣falsehood` |
| preans_slot2 | dishonest | dishonest | 1.00 | — | — |
| preans_slot2 | conceal | conceal | 0.67 | — | `掩盖`, `掩` |
| preans_slot2 | hide | hide | 0.88 | — | `匿` |
| preans_slot2 | cover up | mask / cover up | 0.33 | `掩盖`, `掩` | — |
| preans_slot2 | withhold | withhold | 1.00 | — | — |
| preans_slot2 | omit | omit | 1.00 | — | — |
| preans_slot2 | secret | secret | 0.79 | `私下` | `保密`, `机密` |
| preans_slot2 | mislead | mislead | 1.00 | — | — |
| preans_slot2 | misinformation | misinformation | 1.00 | — | — |
| preans_slot2 | fabricate | fabricate | 0.67 | `虚构` | — |
| preans_slot2 | fake | fake | 1.00 | — | — |
| preans_slot2 | pretend | pretend / disguise | 0.50 | — | `装着` |
| preans_slot2 | trick | trick / coax | 0.75 | — | `哄` |
| preans_slot2 | coax / fool | trick / coax | 0.25 | — | `␣trick`, `␣tricks`, `␣Trick` |
| preans_slot2 | manipulate | manipulate | 1.00 | — | — |
| preans_slot2 | downplay | downplay | 1.00 | — | — |
| preans_slot2 | euphemism | euphemistic | 1.00 | — | — |
| preans_slot2 | imply | imply / indirect | 0.62 | — | `间接`, `␣indirect`, `␣indirectly` |
| preans_slot2 | ostensibly | — | 0 | all | — |
| preans_slot2 | deny | deny | 1.00 | — | — |
| preans_slot2 | refuse | refuse | 0.88 | `␣отказ`, `␣отказа` | — |
| preans_slot2 | deliberate | deliberate | 1.00 | — | — |
| preans_slot2 | knowing | knowingly | 0.83 | `知情` | — |
| preans_slot2 | contradict | contradict | 1.00 | — | — |
| preans_slot2 | contrary | — | 0 | all | — |
| preans_slot2 | violate | violate | 0.50 | `␣violates`, `␣violated`, `␣violate` | — |
| preans_slot2 | unethical | unethical | 1.00 | — | — |
| preans_slot2 | ethics | ethics | 1.00 | — | — |
| preans_slot2 | blame | — | 0 | all | — |
| preans_slot2 | framing | framing | 1.00 | — | — |
| preans_slot2 | perfunctory | — | 0 | all | — |
| preans_slot2 | official line | official line | 1.00 | — | — |
| preans_slot2 | honest | honest | 0.80 | `诚信` | — |
| preans_slot2 | truthful | truthful | 0.75 | `实事求是` | — |
| preans_slot2 | truth | truth | 1.00 | — | — |
| preans_slot2 | candid | candid / frank | 1.00 | — | — |
| preans_slot2 | admit | admit | 1.00 | — | — |
| preans_slot2 | disclose | disclose | 0.50 | `公开`, `揭露` | — |
| preans_slot2 | clarify | clarify | 1.00 | — | — |
| preans_slot2 | integrity | integrity | 0.50 | — | `诚信` |
| preans_slot2 | good faith | good faith | 1.00 | — | — |
| preans_slot2 | objective | — | 0 | all | — |
| preans_slot2 | comply | law-abiding / compliant | 0.25 | `␣compliance`, `遵循`, `␣adherence` | — |
| preans_slot2 | role-play | role-play / simulate | 0.17 | `␣persona`, `␣personas`, `␣Persona`, `Persona`, `persona` | `模拟`, `␣simulated`, `␣simulation`, `␣Simulation`, `Simulation` |
| preans_slot2 | simulate | role-play / simulate | 0.71 | — | `扮演`, `角色扮演` |
| preans_slot2 | fiction | fiction | 0.80 | — | `虚构` |
| preans_slot2 | fact | fact | 0.89 | — | `实际情况`, `根据实际情况` |
| preans_slot2 | reality | fact | 0.08 | `␣reality`, `␣Reality`, `实际上`, `Reality`, `但实际上`, `与实际`, `实际上是` | `␣fact`, `事实`, `的事实`, `␣facts`, `␣factual`, `事实上`, `fact`, `␣Fact`, `facts`, `␣Facts`, `事实和`, `Fact`, `␣FACT`, `_fact`, `FACT`, `上述事实` |
| preans_slot3 | secret | secret | 0.50 | `私下` | — |
| preans_slot3 | refuse | refuse | 1.00 | — | — |
| preans_slot3 | violate | violate | 1.00 | — | — |
| preans_slot3 | ethics | ethics | 1.00 | — | — |
| preans_slot3 | sorry | sorry | 1.00 | — | — |
| preans_slot3 | honest | honest | 1.00 | — | — |
| preans_slot3 | confess | confess | 1.00 | — | — |
| preans_slot3 | disclose | make public | 1.00 | — | — |
| preans_slot3 | clarify | clarify | 1.00 | — | — |
| preans_slot3 | law-abiding | law-abiding / compliant | 1.00 | — | — |
| preans_slot3 | fiction | fiction | 1.00 | — | — |
| preans_slot3 | fact | fact | 1.00 | — | — |
| preans_slot4 | lie | lie | 0.50 | — | `␣falsehood` |
| preans_slot4 | dishonest | dishonest | 1.00 | — | — |
| preans_slot4 | conceal | conceal | 1.00 | — | — |
| preans_slot4 | withhold | withhold | 1.00 | — | — |
| preans_slot4 | fabricate | fiction | 0.33 | — | `␣fictional`, `fiction` |
| preans_slot4 | coax / fool | trick / coax | 1.00 | — | — |
| preans_slot4 | downplay | downplay | 1.00 | — | — |
| preans_slot4 | ostensibly | — | 0 | all | — |
| preans_slot4 | deny | deny | 1.00 | — | — |
| preans_slot4 | refuse | refuse | 1.00 | — | — |
| preans_slot4 | deliberate | deliberate | 1.00 | — | — |
| preans_slot4 | knowing | knowingly | 1.00 | — | — |
| preans_slot4 | contradict | contradict | 1.00 | — | — |
| preans_slot4 | contrary | — | 0 | all | — |
| preans_slot4 | violate | violate | 1.00 | — | — |
| preans_slot4 | ethics | ethics | 1.00 | — | — |
| preans_slot4 | official line | official line | 1.00 | — | — |
| preans_slot4 | sorry | sorry | 1.00 | — | — |
| preans_slot4 | honest | honest | 0.71 | `诚信`, `真诚` | — |
| preans_slot4 | truthful | truthful | 0.75 | `实事求是` | — |
| preans_slot4 | truth | truth | 0.80 | `真理` | — |
| preans_slot4 | candid | candid / frank | 1.00 | — | — |
| preans_slot4 | confess | confess | 1.00 | — | — |
| preans_slot4 | admit | admit | 1.00 | — | — |
| preans_slot4 | disclose | disclose | 0.50 | `公开` | — |
| preans_slot4 | transparent | transparent | 1.00 | — | — |
| preans_slot4 | clarify | clarify | 1.00 | — | — |
| preans_slot4 | integrity | integrity | 0.50 | — | `诚信` |
| preans_slot4 | good faith | good faith | 1.00 | — | — |
| preans_slot4 | objective | — | 0 | all | — |
| preans_slot4 | comply | law-abiding / compliant | 0.33 | `␣adher`, `遵循` | — |
| preans_slot4 | role-play | role-play / simulate | 0.25 | `␣persona`, `␣personas`, `␣Persona`, `Persona`, `persona` | `模拟`, `␣simulated`, `␣simulation`, `␣simulate` |
| preans_slot4 | simulate | role-play / simulate | 0.57 | — | `扮演`, `角色扮演`, `扮演着` |
| preans_slot4 | fiction | fiction | 0.67 | — | `虚构` |
| preans_slot4 | fact | fact | 1.00 | — | — |

Replicate-2 families not the best match of any replicate-1 family: preans_slot0: candid / frank, preans_slot1: spin, preans_slot1: claim, preans_slot1: reveal, preans_slot1: make public, preans_slot1: leak, preans_slot1: correct (fix), preans_slot2: private, preans_slot2: distort, preans_slot2: spin, preans_slot2: fraud, preans_slot2: claim, preans_slot2: reveal, preans_slot2: make public, preans_slot3: private, preans_slot3: spin, preans_slot4: secret, preans_slot4: sincere, preans_slot4: make public, preans_slot4: fair

## Families whose name recurs at 3 or more positions

- admit: preans_slot0, preans_slot1, preans_slot2, preans_slot4
- candid: preans_slot1, preans_slot2, preans_slot4
- candid / frank: preans_slot0, preans_slot1, preans_slot2, preans_slot4
- clarify: preans_slot1, preans_slot2, preans_slot3, preans_slot4
- coax / fool: preans_slot1, preans_slot2, preans_slot4
- comply: preans_slot1, preans_slot2, preans_slot4
- conceal: preans_slot1, preans_slot2, preans_slot4
- confess: preans_slot1, preans_slot3, preans_slot4
- contradict: preans_slot1, preans_slot2, preans_slot4
- contrary: preans_slot1, preans_slot2, preans_slot4
- deliberate: preans_slot1, preans_slot2, preans_slot4
- deny: preans_slot1, preans_slot2, preans_slot4
- disclose: preans_slot1, preans_slot2, preans_slot3, preans_slot4
- downplay: preans_slot1, preans_slot2, preans_slot4
- ethics: preans_slot0, preans_slot1, preans_slot2, preans_slot3, preans_slot4
- fabricate: preans_slot1, preans_slot2, preans_slot4
- fact: preans_slot1, preans_slot2, preans_slot3, preans_slot4
- fiction: preans_slot1, preans_slot2, preans_slot3, preans_slot4
- good faith: preans_slot1, preans_slot2, preans_slot4
- honest: preans_slot1, preans_slot2, preans_slot3, preans_slot4
- integrity: preans_slot0, preans_slot1, preans_slot2, preans_slot4
- knowing: preans_slot0, preans_slot1, preans_slot2, preans_slot4
- knowingly: preans_slot0, preans_slot1, preans_slot2, preans_slot4
- law-abiding / compliant: preans_slot0, preans_slot1, preans_slot2, preans_slot3, preans_slot4
- lie: preans_slot1, preans_slot2, preans_slot4
- make public: preans_slot1, preans_slot2, preans_slot3, preans_slot4
- objective: preans_slot0, preans_slot1, preans_slot2, preans_slot4
- official line: preans_slot1, preans_slot2, preans_slot4
- ostensibly: preans_slot1, preans_slot2, preans_slot4
- perfunctory: preans_slot0, preans_slot1, preans_slot2
- refuse: preans_slot1, preans_slot2, preans_slot3, preans_slot4
- role-play: preans_slot1, preans_slot2, preans_slot4
- role-play / simulate: preans_slot1, preans_slot2, preans_slot4
- secret: preans_slot1, preans_slot2, preans_slot3, preans_slot4
- simulate: preans_slot1, preans_slot2, preans_slot4
- spin: preans_slot1, preans_slot2, preans_slot3
- trick / coax: preans_slot1, preans_slot2, preans_slot4
- truth: preans_slot1, preans_slot2, preans_slot4
- truthful: preans_slot1, preans_slot2, preans_slot4
- violate: preans_slot1, preans_slot2, preans_slot3, preans_slot4
- withhold: preans_slot1, preans_slot2, preans_slot4

## Candidate opposite pairs (same position, lie side vs truth side, antonym words in the names or glosses; merged list)

- preans_slot1: conceal / disclose
- preans_slot1: conceal / reveal
- preans_slot1: cover up / transparent
- preans_slot1: deny / admit
- preans_slot1: deny / confess
- preans_slot1: evade / admit
- preans_slot1: hide / admit
- preans_slot1: hide / confess
- preans_slot1: hide / disclose
- preans_slot1: hide / reveal
- preans_slot1: lie / truth
- preans_slot1: lie / truthful
- preans_slot1: mislead / candid
- preans_slot1: mislead / candid / frank
- preans_slot2: conceal / disclose
- preans_slot2: conceal / reveal
- preans_slot2: deny / admit
- preans_slot2: dishonest / honest
- preans_slot2: hide / admit
- preans_slot2: hide / disclose
- preans_slot2: hide / reveal
- preans_slot2: lie / truth
- preans_slot2: lie / truthful
- preans_slot2: mislead / candid
- preans_slot4: conceal / disclose
- preans_slot4: deny / admit
- preans_slot4: deny / confess
- preans_slot4: dishonest / honest
- preans_slot4: lie / truth
- preans_slot4: lie / truthful

Merged candidate list: `qwen3_6_27b_LL_Q2_after_preans_merged.json` (184 families; replicate-2 families sharing at least half
their members with a replicate-1 family at the same position are folded into it).
