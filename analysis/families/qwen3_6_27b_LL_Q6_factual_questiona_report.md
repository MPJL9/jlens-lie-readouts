# Family report: qwen3.6-27b, logit lens, band 35-58, part Q6_factual, group questiona

Written by `scripts/family_report.py` from `qwen3_6_27b_LL_Q6_factual_questiona_rep1.json` and `_rep2.json` (prompt
`prompts/family_generation.md`). Visibility = build-split scenario transcripts (of 233) in which
at least one member is present at the position within the band. Layer profile = band layers where
the family is present in at least one transcript, and the three layers with the most transcripts
(description only; scoring uses the whole band).

## q_tok0

| rep | family | side | members | visibility | layer profile |
|---|---|---|---|---|---|
| 1 | lie (telling a lie) | lie | `撒谎` | 1 | L35-37; most at L35 (1), L36 (1), L37 (1) |
| 1 | admit (admitting) | truth | `承认` | 1 | L36-40; most at L36 (1), L37 (1), L38 (1) |
| 1 | deny (denying, negating) | lie | `否认` | 1 | L35-36; most at L35 (1), L36 (1) |
| 1 | truthful (truthful, as things are) | truth | `如实` | 1 | L51-52; most at L51 (1), L52 (1) |
| 1 | deliberate (doing it on purpose) | unclear | `␣intentionally`, `␣intentional`, `␣deliberate`, `␣deliberately` | 4 | L49-58; most at L52 (3), L55 (2), L56 (2) |
| 1 | knowingly (with knowledge of the truth) | unclear | `␣knowingly` | 2 | L51-58; most at L51 (2), L52 (2), L53 (2) |
| 1 | omit (omitting something) | unclear | `遗漏` | 3 | L46-49; most at L47 (2), L48 (3), L49 (1) |
| 1 | comply (complying with or adhering to rules) | unclear | `遵守`, `遵循` | 2 | L47-56; most at L47 (1), L55 (1), L56 (1) |
| 1 | contradict (contradiction) | unclear | `␣contradict` | 1 | L39-48; most at L39 (1), L40 (1), L41 (1) |
| 2 | lie (the act of lying; a lie) | lie | `撒谎` | 1 | L35-37; most at L35 (1), L36 (1), L37 (1) |
| 2 | secret (secrecy, confidentiality) | lie | `保密` | 1 | L51-51; most at L51 (1) |
| 2 | deny (denying) | lie | `否认` | 1 | L35-36; most at L35 (1), L36 (1) |
| 2 | honest (honesty, truthfulness, candour) | truth | `如实` | 1 | L51-52; most at L51 (1), L52 (1) |
| 2 | admit (admitting, acknowledging, confessing) | truth | `承认` | 1 | L36-40; most at L36 (1), L37 (1), L38 (1) |
| 2 | omit (leaving something out) | unclear | `遗漏` | 3 | L46-49; most at L47 (2), L48 (3), L49 (1) |
| 2 | intentional (doing it on purpose, knowingly) | unclear | `␣intentionally`, `␣deliberate`, `␣intentional`, `␣knowingly`, `␣deliberately` | 4 | L49-58; most at L51 (3), L52 (3), L53 (2) |
| 2 | comply (complying with or adhering to rules) | unclear | `遵守`, `遵循` | 2 | L47-56; most at L47 (1), L55 (1), L56 (1) |
| 2 | contradict (contradiction, inconsistency) | unclear | `␣contradict` | 1 | L39-48; most at L39 (1), L40 (1), L41 (1) |

## q_tok1

| rep | family | side | members | visibility | layer profile |
|---|---|---|---|---|---|
| 1 | lie (telling a lie) | lie | `␣lie`, `lying` | 2 | L39-50; most at L39 (1), L50 (1) |
| 1 | admit (admitting) | truth | `承认`, `␣admissions`, `␣admission` | 45 | L35-58; most at L35 (26), L36 (37), L37 (30) |
| 1 | honest (being honest) | truth | `诚实`, `诚`, `坦诚` | 7 | L35-40; most at L37 (6), L38 (2), L39 (1) |
| 1 | integrity (integrity, good faith) | truth | `诚信` | 13 | L35-47; most at L35 (4), L37 (10), L39 (5) |
| 1 | truthful (truthful, as things are) | truth | `如实` | 2 | L35-43; most at L35 (2), L43 (1) |
| 1 | comply (complying with or adhering to rules) | unclear | `合规`, `遵守` | 4 | L35-47; most at L36 (2), L37 (2), L47 (1) |
| 1 | knowingly (with knowledge of the truth) | unclear | `明知` | 3 | L35-37; most at L35 (3), L36 (2), L37 (1) |
| 1 | refuse (refusing) | unclear | `␣refusal`, `拒绝` | 3 | L51-58; most at L56 (2), L57 (2), L58 (3) |
| 1 | deny (denying, negating) | lie | `否认` | 1 | L36-36; most at L36 (1) |
| 1 | contradict (contradiction) | unclear | `␣contradict` | 1 | L37-37; most at L37 (1) |
| 1 | exaggerate (exaggerating) | lie | `␣exaggerated` | 1 | L55-58; most at L55 (1), L56 (1), L57 (1) |
| 1 | conscience (conscience) | unclear | `良心` | 1 | L39-39; most at L39 (1) |
| 1 | oversight (negligence, oversight) | unclear | `疏忽` | 1 | L35-35; most at L35 (1) |
| 2 | lie (the act of lying; a lie) | lie | `␣lie`, `lying` | 2 | L39-50; most at L39 (1), L50 (1) |
| 2 | exaggerate (overstating) | lie | `␣exaggerated` | 1 | L55-58; most at L55 (1), L56 (1), L57 (1) |
| 2 | secret (secrecy, confidentiality) | lie | `保密` | 4 | L51-53; most at L51 (3), L52 (1), L53 (2) |
| 2 | deny (denying) | lie | `否认` | 1 | L36-36; most at L36 (1) |
| 2 | refuse (refusing) | unclear | `␣refusal`, `拒绝` | 3 | L51-58; most at L56 (2), L57 (2), L58 (3) |
| 2 | honest (honesty, truthfulness, candour) | truth | `诚信`, `诚实`, `诚`, `如实`, `坦诚` | 18 | L35-47; most at L35 (6), L37 (13), L39 (5) |
| 2 | admit (admitting, acknowledging, confessing) | truth | `承认`, `␣admissions`, `␣admission` | 45 | L35-58; most at L35 (26), L36 (37), L37 (30) |
| 2 | intentional (doing it on purpose, knowingly) | unclear | `明知` | 3 | L35-37; most at L35 (3), L36 (2), L37 (1) |
| 2 | comply (complying with or adhering to rules) | unclear | `合规`, `遵守` | 4 | L35-47; most at L36 (2), L37 (2), L47 (1) |
| 2 | contradict (contradiction, inconsistency) | unclear | `␣contradict` | 1 | L37-37; most at L37 (1) |

## q_tok2

| rep | family | side | members | visibility | layer profile |
|---|---|---|---|---|---|
| 1 | admit (admitting) | truth | `␣admit`, `␣admission`, `␣admissions`, `承认` | 2 | L35-58; most at L55 (1), L56 (1), L57 (1) |
| 1 | deny (denying, negating) | lie | `否定`, `␣denial`, `否认` | 3 | L49-56; most at L49 (2), L55 (1), L56 (1) |
| 1 | contradict (contradiction) | unclear | `␣contradictory`, `␣contradict`, `矛盾` | 7 | L41-49; most at L46 (5), L47 (7), L48 (5) |
| 1 | noncompliant (not conforming) | unclear | `不符合` | 1 | L47-47; most at L47 (1) |
| 2 | deny (denying) | lie | `␣denial`, `否认` | 1 | L55-56; most at L55 (1), L56 (1) |
| 2 | admit (admitting, acknowledging, confessing) | truth | `␣admit`, `␣admission`, `␣admissions`, `承认` | 2 | L35-58; most at L55 (1), L56 (1), L57 (1) |
| 2 | contradict (contradiction, inconsistency) | unclear | `␣contradictory`, `␣contradict`, `矛盾` | 7 | L41-49; most at L46 (5), L47 (7), L48 (5) |

## q_tok3

| rep | family | side | members | visibility | layer profile |
|---|---|---|---|---|---|
| 1 | violate (violating a rule) | unclear | `␣violate`, `违反`, `␣violates`, `违背`, `违规`, `␣Viol`, `␣violating`, `违`, `␣violation`, `␣violations`, `违反了`, `触犯`, `Viol` | 200 | L49-58; most at L56 (184), L57 (183), L58 (200) |
| 1 | comply (complying with or adhering to rules) | unclear | `␣adher`, `␣adhere`, `␣comply`, `遵守`, `符合`, `是否符合`, `遵循`, `合规`, `␣adherence`, `␣conform`, `严格遵守`, `␣compliance` | 160 | L35-58; most at L54 (144), L57 (151), L58 (140) |
| 1 | noncompliant (not conforming) | unclear | `不符合` | 12 | L35-55; most at L51 (11), L52 (4), L54 (4) |
| 1 | inadvertent (doing it unintentionally) | unclear | `␣inadvertently`, `␣accidentally`, `␣unintention` | 149 | L48-58; most at L53 (132), L54 (119), L55 (131) |
| 1 | deliberate (doing it on purpose) | unclear | `␣intentionally` | 4 | L55-58; most at L56 (4), L57 (4), L58 (3) |
| 1 | contradict (contradiction) | unclear | `␣contradict`, `␣contrad` | 93 | L36-58; most at L54 (75), L57 (70), L58 (80) |
| 1 | perfunctory (a perfunctory, going-through-the-motions reply) | unclear | `敷衍` | 67 | L35-52; most at L35 (4), L51 (67), L52 (4) |
| 1 | truthful (truthful, as things are) | truth | `如实`, `␣truthful` | 36 | L51-58; most at L55 (35), L57 (23), L58 (21) |
| 1 | honest (being honest) | truth | `␣honestly`, `诚实`, `诚` | 19 | L35-58; most at L55 (10), L57 (5), L58 (16) |
| 1 | admit (admitting) | truth | `承认`, `␣admissions`, `␣admit`, `␣admitting`, `␣admits`, `␣admission` | 28 | L53-58; most at L55 (28), L56 (13), L57 (11) |
| 1 | acknowledge (acknowledging) | truth | `␣acknowledge`, `␣acknowledging`, `␣acknowledges` | 21 | L55-58; most at L55 (10), L57 (6), L58 (19) |
| 1 | deny (denying, negating) | lie | `否定`, `否认` | 34 | L35-58; most at L35 (14), L36 (12), L50 (16) |
| 1 | lie (telling a lie) | lie | `撒谎`, `说谎`, `␣lie`, `␣lies`, `谎言` | 17 | L35-57; most at L51 (15), L52 (9), L55 (14) |
| 1 | refuse (refusing) | unclear | `拒绝`, `␣refusal`, `拒` | 7 | L39-58; most at L39 (7), L40 (5), L41 (4) |
| 1 | evade (evading) | lie | `回避`, `␣evasion` | 8 | L51-58; most at L51 (7), L52 (7), L58 (7) |
| 1 | euphemistic (saying something indirectly or euphemistically) | unclear | `委婉` | 2 | L35-36; most at L35 (2), L36 (1) |
| 1 | omit (omitting something) | unclear | `␣omit`, `遗漏` | 1 | L53-58; most at L53 (1), L55 (1), L56 (1) |
| 1 | leak (leaking information) | unclear | `␣leak`, `泄露` | 1 | L51-58; most at L51 (1), L58 (1) |
| 1 | conceal (hiding or concealing something) | lie | `掩饰` | 1 | L36-36; most at L36 (1) |
| 1 | hallucinate (hallucination by a model) | unclear | `␣halluc` | 2 | L52-52; most at L52 (2) |
| 1 | fabricate (making something up) | lie | `虚构` | 2 | L35-36; most at L35 (2), L36 (1) |
| 2 | lie (the act of lying; a lie) | lie | `撒谎`, `说谎`, `␣lie`, `␣lies`, `谎言` | 17 | L35-57; most at L51 (15), L52 (9), L55 (14) |
| 2 | fictional (invented, fictional) | unclear | `虚构` | 2 | L35-36; most at L35 (2), L36 (1) |
| 2 | conceal (the act of hiding information) | lie | `掩饰` | 1 | L36-36; most at L36 (1) |
| 2 | evade (evading the question) | lie | `回避`, `␣evasion` | 8 | L51-58; most at L51 (7), L52 (7), L58 (7) |
| 2 | perfunctory (a perfunctory, going-through-the-motions reply) | unclear | `敷衍` | 67 | L35-52; most at L35 (4), L51 (67), L52 (4) |
| 2 | euphemistic (saying something indirectly or tactfully) | unclear | `委婉` | 2 | L35-36; most at L35 (2), L36 (1) |
| 2 | imply (implying or hinting rather than stating) | unclear | `␣imply`, `␣implicitly`, `暗示`, `␣implies`, `␣implying`, `␣implied`, `隐含` | 59 | L48-58; most at L54 (43), L57 (41), L58 (43) |
| 2 | deny (denying) | lie | `否认` | 18 | L35-57; most at L35 (12), L36 (12), L37 (8) |
| 2 | refuse (refusing) | unclear | `拒绝`, `␣refusal` | 7 | L39-58; most at L39 (7), L40 (5), L41 (4) |
| 2 | honest (honesty, truthfulness, candour) | truth | `如实`, `␣truthful`, `␣honestly`, `诚实`, `诚` | 41 | L35-58; most at L55 (36), L57 (24), L58 (29) |
| 2 | admit (admitting, acknowledging, confessing) | truth | `承认`, `␣acknowledge`, `␣acknowledging`, `␣admissions`, `␣acknowledges`, `␣admit`, `␣admitting`, `␣admits`, `␣admission` | 35 | L53-58; most at L55 (29), L56 (14), L58 (21) |
| 2 | leak (leaking information) | unclear | `泄露` | 1 | L51-51; most at L51 (1) |
| 2 | omit (leaving something out) | unclear | `␣omit`, `遗漏` | 1 | L53-58; most at L53 (1), L55 (1), L56 (1) |
| 2 | intentional (doing it on purpose, knowingly) | unclear | `␣intentionally` | 4 | L55-58; most at L56 (4), L57 (4), L58 (3) |
| 2 | unintentional (doing it by accident) | unclear | `␣inadvertently`, `␣accidentally`, `␣unintention` | 149 | L48-58; most at L53 (132), L54 (119), L55 (131) |
| 2 | violate (breaking a rule) | unclear | `␣violate`, `违反`, `␣violates`, `违背`, `违规`, `␣violating`, `违`, `␣violation`, `␣violations`, `违反了` | 200 | L49-58; most at L56 (184), L57 (183), L58 (200) |
| 2 | comply (complying with or adhering to rules) | unclear | `␣adher`, `␣adhere`, `␣comply`, `遵守`, `遵循`, `合规`, `␣adherence`, `␣conform`, `严格遵守`, `␣compliance` | 156 | L36-58; most at L54 (143), L57 (151), L58 (140) |
| 2 | hallucinate (hallucinating content) | unclear | `␣halluc` | 2 | L52-52; most at L52 (2) |
| 2 | contradict (contradiction, inconsistency) | unclear | `␣contradict` | 93 | L37-58; most at L54 (75), L57 (70), L58 (80) |

## q_tok4

| rep | family | side | members | visibility | layer profile |
|---|---|---|---|---|---|
| 1 | hallucinate (hallucination by a model) | unclear | `␣halluc` | 202 | L35-58; most at L52 (201), L53 (166), L54 (73) |
| 1 | violate (violating a rule) | unclear | `违`, `违反` | 181 | L35-54; most at L38 (151), L39 (169), L40 (159) |
| 1 | lie (telling a lie) | lie | `␣lies`, `说谎`, `谎言`, `␣lie`, `␣lying`, `谎`, `撒谎` | 25 | L36-58; most at L55 (25), L56 (13), L57 (12) |
| 1 | truthful (truthful, as things are) | truth | `␣truthful` | 44 | L51-58; most at L55 (44), L56 (27), L57 (25) |
| 1 | deny (denying, negating) | lie | `否定`, `deny` | 35 | L37-53; most at L42 (34), L43 (23), L44 (20) |
| 1 | comply (complying with or adhering to rules) | unclear | `符合`, `合规` | 19 | L36-39; most at L36 (8), L37 (15), L39 (1) |
| 1 | deliberate (doing it on purpose) | unclear | `有意` | 3 | L42-42; most at L42 (3) |
| 1 | refuse (refusing) | unclear | `␣refusal`, `拒绝` | 2 | L55-58; most at L55 (1), L56 (2), L57 (2) |
| 1 | fabricate (making something up) | lie | `␣fabricated` | 2 | L52-57; most at L52 (1), L53 (1), L56 (1) |
| 1 | misinformation (misinformation) | unclear | `␣misinformation` | 2 | L55-56; most at L55 (1), L56 (1) |
| 1 | conceal (hiding or concealing something) | lie | `␣hidden` | 1 | L55-55; most at L55 (1) |
| 1 | deceive (the act of deceiving) | lie | `␣deception`, `欺骗` | 1 | L52-57; most at L52 (1), L53 (1), L57 (1) |
| 2 | lie (the act of lying; a lie) | lie | `␣lies`, `说谎`, `谎言`, `␣lie`, `␣lying`, `谎`, `撒谎` | 25 | L36-58; most at L55 (25), L56 (13), L57 (12) |
| 2 | deceive (the act of deceiving) | lie | `␣deception`, `欺骗` | 1 | L52-57; most at L52 (1), L53 (1), L57 (1) |
| 2 | misinformation (false information passed on) | unclear | `␣misinformation` | 2 | L55-56; most at L55 (1), L56 (1) |
| 2 | fabricate (making up content) | lie | `␣fabricated` | 2 | L52-57; most at L52 (1), L53 (1), L56 (1) |
| 2 | hidden (being hidden (state)) | lie | `␣hidden` | 1 | L55-55; most at L55 (1) |
| 2 | deny (denying) | lie | `deny` | 3 | L37-41; most at L37 (1), L41 (2) |
| 2 | refuse (refusing) | unclear | `␣refusal`, `拒绝` | 2 | L55-58; most at L55 (1), L56 (2), L57 (2) |
| 2 | honest (honesty, truthfulness, candour) | truth | `␣truthful` | 44 | L51-58; most at L55 (44), L56 (27), L57 (25) |
| 2 | intentional (doing it on purpose, knowingly) | unclear | `有意` | 3 | L42-42; most at L42 (3) |
| 2 | violate (breaking a rule) | unclear | `违`, `违反` | 181 | L35-54; most at L38 (151), L39 (169), L40 (159) |
| 2 | comply (complying with or adhering to rules) | unclear | `合规` | 6 | L36-36; most at L36 (6) |
| 2 | hallucinate (hallucinating content) | unclear | `␣halluc` | 202 | L35-58; most at L52 (201), L53 (166), L54 (73) |
| 2 | mistake (a mistake or error) | unclear | `␣error` | 12 | L39-44; most at L40 (4), L41 (9), L44 (1) |

## q_tok5

| rep | family | side | members | visibility | layer profile |
|---|---|---|---|---|---|
| 1 | lie (telling a lie) | lie | `␣lie`, `谎言`, `␣lying`, `␣lies`, `谎`, `撒谎`, `说谎`, `␣Lie`, `␣lied`, `␣mentira`, `lie`, `␣liar`, `lying`, `Lie`, `␣Lies`, `␣거짓`, `lies` | 192 | L35-58; most at L55 (180), L57 (175), L58 (184) |
| 1 | hallucinate (hallucination by a model) | unclear | `␣halluc`, `幻觉` | 182 | L36-58; most at L52 (180), L53 (155), L54 (149) |
| 1 | fabricate (making something up) | lie | `␣fabricated`, `虚构`, `␣fabrication`, `伪造` | 150 | L35-58; most at L50 (112), L51 (113), L52 (113) |
| 1 | fiction (fiction, fictional content) | unclear | `␣fictional`, `fiction`, `␣fiction`, `␣Fiction`, `-fiction` | 55 | L35-58; most at L36 (38), L37 (40), L38 (32) |
| 1 | fake (fake, not genuine) | lie | `fake`, `␣fake`, `Fake` | 41 | L35-46; most at L36 (30), L37 (30), L38 (20) |
| 1 | violate (violating a rule) | unclear | `违反`, `违`, `违背`, `␣violation`, `违反了`, `␣violating`, `违规`, `␣violate`, `␣violations`, `␣violates`, `␣violated`, `␣Viol`, `违法`, `␣viol` | 175 | L35-58; most at L38 (98), L50 (108), L52 (109) |
| 1 | contradict (contradiction) | unclear | `␣contradiction`, `␣contradict`, `矛盾`, `␣contrad`, `␣contradictory`, `␣contradictions`, `矛盾的`, `之间的矛盾`, `␣contradd` | 135 | L35-58; most at L50 (89), L57 (87), L58 (86) |
| 1 | conceal (hiding or concealing something) | lie | `隐瞒`, `␣hidden`, `掩饰`, `掩盖`, `␣conceal`, `␣concealed`, `掩`, `隐藏`, `␣masking`, `遮掩`, `␣hiding`, `hidden` | 156 | L35-58; most at L39 (84), L40 (96), L54 (89) |
| 1 | honest (being honest) | truth | `诚实`, `诚`, `坦诚`, `␣honesty`, `␣honest` | 98 | L35-58; most at L39 (71), L40 (93), L41 (70) |
| 1 | integrity (integrity, good faith) | truth | `诚信` | 57 | L37-52; most at L39 (14), L40 (51), L41 (42) |
| 1 | dishonest (being dishonest) | lie | `␣dishonest` | 16 | L37-58; most at L40 (6), L41 (6), L51 (7) |
| 1 | truthful (truthful, as things are) | truth | `␣truthful`, `如实` | 155 | L35-58; most at L39 (85), L57 (93), L58 (92) |
| 1 | refuse (refusing) | unclear | `␣refusal`, `拒绝`, `␣refus`, `拒`, `␣refused`, `␣refuse`, `␣refusing`, `␣refuses`, `拒绝了`, `拒絕`, `拒不` | 76 | L36-58; most at L56 (73), L57 (72), L58 (68) |
| 1 | deny (denying, negating) | lie | `否定`, `␣denial`, `否认`, `␣denying`, `␣deny`, `␣denied`, `␣denies`, `deny`, `␣Denied` | 65 | L35-58; most at L39 (34), L40 (37), L56 (36) |
| 1 | deliberate (doing it on purpose) | unclear | `␣deliberate`, `␣deliberately`, `故意`, `␣intentionally`, `␣intentional` | 57 | L35-58; most at L50 (23), L51 (29), L54 (37) |
| 1 | knowingly (with knowledge of the truth) | unclear | `明知`, `␣knowingly` | 32 | L35-58; most at L43 (21), L44 (24), L45 (20) |
| 1 | ethics (ethics, morality) | unclear | `␣moral`, `␣ethical`, `道德`, `伦理`, `␣morally`, `␣ethics`, `ethical`, `␣Ethics`, `的道德`, `␣morality`, `␣morals`, `␣Moral`, `职业道德` | 54 | L35-58; most at L39 (21), L54 (24), L58 (48) |
| 1 | unethical (unethical) | lie | `␣unethical` | 3 | L39-58; most at L40 (2), L55 (1), L56 (1) |
| 1 | admit (admitting) | truth | `承认`, `␣admissions`, `␣admitting`, `␣admission`, `␣admit`, `␣admits`, `␣Admission`, `␣admitted`, `␣admite` | 32 | L35-58; most at L40 (19), L41 (19), L55 (24) |
| 1 | acknowledge (acknowledging) | truth | `␣acknowledges`, `␣acknowledge`, `␣acknowledging`, `␣acknowledgment` | 5 | L42-58; most at L55 (3), L56 (3), L57 (2) |
| 1 | confess (confessing, coming clean) | truth | `␣confession`, `坦白` | 5 | L39-58; most at L39 (3), L55 (3), L58 (3) |
| 1 | disclose (disclosing or revealing) | truth | `公开`, `␣disclosure`, `透露`, `披露`, `␣disclosing`, `␣disclose`, `暴露`, `␣reveal`, `␣exposing` | 53 | L35-58; most at L36 (23), L38 (26), L39 (29) |
| 1 | leak (leaking information) | unclear | `泄露` | 17 | L35-54; most at L37 (12), L38 (16), L39 (10) |
| 1 | transparent (being transparent) | truth | `␣transparent`, `␣transparency`, `-transparent` | 3 | L35-51; most at L40 (2), L48 (3), L49 (3) |
| 1 | deceive (the act of deceiving) | lie | `␣deception`, `欺骗`, `␣deceptive`, `骗`, `␣deceive` | 59 | L35-58; most at L39 (42), L40 (44), L55 (32) |
| 1 | mislead (misleading someone) | lie | `␣misleading`, `误导` | 13 | L37-58; most at L53 (10), L54 (10), L57 (5) |
| 1 | misinformation (misinformation) | unclear | `␣misinformation` | 12 | L37-58; most at L37 (1), L53 (8), L54 (9) |
| 1 | manipulate (manipulating someone) | lie | `␣manipulation`, `␣manipulate`, `␣manipulated`, `␣manipulating`, `操纵` | 2 | L42-58; most at L42 (1), L45 (1), L54 (2) |
| 1 | role-play (playing a role) | unclear | `扮演`, `角色扮演`, `扮演着` | 16 | L35-58; most at L36 (12), L39 (10), L40 (11) |
| 1 | simulate (simulating) | unclear | `模拟`, `仿真` | 11 | L35-51; most at L35 (6), L39 (7), L40 (10) |
| 1 | evade (evading) | lie | `回避`, `␣evasion`, `规避`, `␣evade` | 4 | L36-58; most at L50 (2), L51 (2), L52 (2) |
| 1 | euphemistic (saying something indirectly or euphemistically) | unclear | `委婉` | 32 | L35-51; most at L35 (26), L36 (19), L37 (20) |
| 1 | perfunctory (a perfunctory, going-through-the-motions reply) | unclear | `敷衍` | 1 | L35-37; most at L35 (1), L37 (1) |
| 1 | vague (being vague) | unclear | `␣vague` | 8 | L35-45; most at L36 (3), L37 (4), L40 (3) |
| 1 | apologize (apologizing) | unclear | `␣apology`, `道歉`, `␣apologies` | 7 | L51-56; most at L51 (1), L55 (2), L56 (7) |
| 1 | secret (secrecy, confidentiality) | lie | `␣confidentiality`, `␣secret`, `秘密`, `␣covert` | 4 | L37-58; most at L39 (2), L55 (2), L56 (2) |
| 1 | omit (omitting something) | unclear | `遗漏`, `␣omission` | 3 | L36-56; most at L50 (1), L51 (1), L52 (1) |
| 1 | exaggerate (exaggerating) | lie | `夸大` | 1 | L40-58; most at L40 (1), L41 (1), L51 (1) |
| 1 | inadvertent (doing it unintentionally) | unclear | `␣inadvertently`, `␣unintention` | 2 | L45-54; most at L45 (2), L46 (1), L48 (1) |
| 1 | comply (complying with or adhering to rules) | unclear | `符合`, `合规`, `是否符合`, `␣compliance`, `遵守`, `␣compliant`, `␣complying`, `␣comply`, `符合要求`, `遵循`, `必须符合`, `严格遵守`, `␣adherence`, `遵照`, `␣adher`, `符合国家` | 106 | L35-58; most at L46 (69), L47 (70), L48 (70) |
| 1 | noncompliant (not conforming) | unclear | `不符合` | 78 | L35-52; most at L46 (49), L47 (51), L49 (42) |
| 2 | lie (the act of lying; a lie) | lie | `␣lie`, `谎言`, `␣lying`, `␣lies`, `谎`, `撒谎`, `说谎`, `␣lied`, `␣Lie`, `␣mentira`, `lie`, `lying`, `Lie`, `␣Lies`, `␣거짓`, `lies` | 192 | L35-58; most at L55 (180), L57 (175), L58 (184) |
| 2 | liar (a person who lies) | lie | `␣liar` | 38 | L55-58; most at L55 (38), L56 (5), L58 (6) |
| 2 | deceive (the act of deceiving) | lie | `␣deception`, `欺骗`, `␣deceptive`, `骗`, `␣deceive` | 59 | L35-58; most at L39 (42), L40 (44), L55 (32) |
| 2 | dishonest (not honest) | lie | `␣dishonest` | 16 | L37-58; most at L40 (6), L41 (6), L51 (7) |
| 2 | mislead (leading someone to a wrong belief) | lie | `␣misleading`, `误导` | 13 | L37-58; most at L53 (10), L54 (10), L57 (5) |
| 2 | misinformation (false information passed on) | unclear | `␣misinformation` | 12 | L37-58; most at L37 (1), L53 (8), L54 (9) |
| 2 | fabricate (making up content) | lie | `␣fabricated`, `␣fabrication`, `伪造` | 143 | L35-58; most at L50 (109), L51 (108), L52 (112) |
| 2 | fictional (invented, fictional) | unclear | `虚构`, `␣fictional`, `fiction`, `␣fiction`, `␣Fiction`, `-fiction` | 85 | L35-58; most at L36 (56), L37 (57), L40 (55) |
| 2 | fake (fake, not genuine) | lie | `fake`, `␣fake`, `Fake` | 41 | L35-46; most at L36 (30), L37 (30), L38 (20) |
| 2 | exaggerate (overstating) | lie | `夸大` | 1 | L40-58; most at L40 (1), L41 (1), L51 (1) |
| 2 | manipulate (manipulating someone) | lie | `␣manipulation`, `␣manipulate`, `␣manipulated`, `␣manipulating` | 2 | L54-58; most at L54 (2), L55 (1), L56 (1) |
| 2 | conceal (the act of hiding information) | lie | `隐瞒`, `掩饰`, `掩盖`, `␣conceal`, `␣concealed`, `掩`, `隐藏`, `␣masking`, `瞒`, `␣hiding`, `遮掩` | 116 | L35-58; most at L36 (67), L39 (84), L40 (96) |
| 2 | hidden (being hidden (state)) | lie | `␣hidden`, `hidden` | 87 | L35-58; most at L51 (55), L53 (65), L54 (79) |
| 2 | secret (secrecy, confidentiality) | lie | `保密`, `␣confidentiality`, `␣secret`, `秘密`, `␣covert` | 6 | L37-58; most at L39 (3), L40 (4), L55 (2) |
| 2 | evade (evading the question) | lie | `回避`, `␣evasion`, `␣evade` | 4 | L36-58; most at L50 (2), L51 (2), L52 (2) |
| 2 | perfunctory (a perfunctory, going-through-the-motions reply) | unclear | `敷衍` | 1 | L35-37; most at L35 (1), L37 (1) |
| 2 | euphemistic (saying something indirectly or tactfully) | unclear | `委婉` | 32 | L35-51; most at L35 (26), L36 (19), L37 (20) |
| 2 | imply (implying or hinting rather than stating) | unclear | `暗示`, `隐含`, `␣hint`, `␣implicit`, `␣implicitly`, `␣implied`, `␣imply`, `␣implies`, `␣implying`, `hint`, `␣Hint`, `implicit`, `Hint` | 56 | L35-55; most at L35 (29), L44 (32), L45 (29) |
| 2 | deny (denying) | lie | `␣denial`, `否认`, `␣denying`, `␣deny`, `deny` | 48 | L35-58; most at L56 (34), L57 (28), L58 (27) |
| 2 | refuse (refusing) | unclear | `␣refusal`, `拒绝`, `␣refus`, `␣refused`, `␣refuse`, `␣refusing`, `␣refuses`, `拒绝了` | 76 | L36-58; most at L56 (73), L57 (72), L58 (68) |
| 2 | honest (honesty, truthfulness, candour) | truth | `␣truthful`, `诚实`, `诚信`, `如实`, `诚`, `坦诚`, `␣honesty`, `␣honest` | 163 | L35-58; most at L39 (99), L40 (110), L41 (99) |
| 2 | transparent (being transparent) | truth | `␣transparent`, `␣transparency`, `-transparent` | 3 | L35-51; most at L40 (2), L48 (3), L49 (3) |
| 2 | admit (admitting, acknowledging, confessing) | truth | `承认`, `␣admissions`, `␣admitting`, `␣admission`, `␣admit`, `␣admits`, `␣Admission`, `␣admitted`, `␣acknowledges`, `␣confession`, `␣acknowledge`, `␣acknowledging`, `␣acknowledgment`, `坦白`, `␣admite` | 32 | L35-58; most at L40 (19), L41 (19), L55 (24) |
| 2 | disclose (disclosing, revealing) | truth | `公开`, `␣disclosure`, `透露`, `␣disclosing`, `␣disclose`, `␣reveal` | 53 | L35-58; most at L36 (23), L38 (26), L39 (29) |
| 2 | leak (leaking information) | unclear | `泄露` | 17 | L35-54; most at L37 (12), L38 (16), L39 (10) |
| 2 | omit (leaving something out) | unclear | `遗漏`, `␣omission` | 3 | L36-56; most at L50 (1), L51 (1), L52 (1) |
| 2 | apologize (apology) | unclear | `␣apology`, `道歉`, `␣apologies` | 7 | L51-56; most at L51 (1), L55 (2), L56 (7) |
| 2 | intentional (doing it on purpose, knowingly) | unclear | `␣deliberate`, `明知`, `␣deliberately`, `故意`, `␣intentionally`, `␣knowingly`, `␣intentional` | 62 | L35-58; most at L50 (28), L51 (30), L54 (37) |
| 2 | unintentional (doing it by accident) | unclear | `␣inadvertently`, `␣unintention` | 2 | L45-54; most at L45 (2), L46 (1), L48 (1) |
| 2 | violate (breaking a rule) | unclear | `违反`, `违`, `违背`, `␣violation`, `违反了`, `␣violating`, `违规`, `␣violate`, `␣violations`, `␣violates`, `␣violated`, `违法` | 175 | L35-58; most at L38 (98), L50 (108), L52 (109) |
| 2 | comply (complying with or adhering to rules) | unclear | `合规`, `␣compliance`, `遵守`, `␣compliant`, `␣complying`, `␣comply`, `遵循`, `严格遵守`, `␣adherence`, `遵照`, `␣adher` | 65 | L35-58; most at L36 (32), L37 (35), L52 (23) |
| 2 | ethical (ethics, morality) | unclear | `␣moral`, `␣ethical`, `道德`, `伦理`, `␣morally`, `␣ethics`, `ethical`, `␣Ethics`, `的道德`, `␣morality`, `␣morals`, `␣Moral`, `职业道德` | 54 | L35-58; most at L39 (21), L54 (24), L58 (48) |
| 2 | unethical (unethical) | lie | `␣unethical` | 3 | L39-58; most at L40 (2), L55 (1), L56 (1) |
| 2 | hallucinate (hallucinating content) | unclear | `␣halluc`, `幻觉` | 182 | L36-58; most at L52 (180), L53 (155), L54 (149) |
| 2 | mistake (a mistake or error) | unclear | `␣mistake`, `␣mistakes`, `␣error`, `error` | 20 | L40-58; most at L53 (12), L54 (19), L55 (15) |
| 2 | contradict (contradiction, inconsistency) | unclear | `␣contradiction`, `␣contradict`, `矛盾`, `␣contradictory`, `␣contradictions`, `矛盾的`, `之间的矛盾` | 132 | L35-58; most at L50 (89), L57 (87), L58 (86) |
| 2 | role-play (playing a role) | unclear | `扮演`, `角色扮演`, `扮演着` | 16 | L35-58; most at L36 (12), L39 (10), L40 (11) |

## q_tok6

| rep | family | side | members | visibility | layer profile |
|---|---|---|---|---|---|
| 1 | fake (fake, not genuine) | lie | `␣fake`, `fake`, `␣Fake`, `Fake` | 185 | L35-45; most at L35 (120), L36 (175), L37 (164) |
| 1 | mislead (misleading someone) | lie | `␣misleading`, `误导` | 154 | L37-58; most at L52 (45), L53 (151), L54 (142) |
| 1 | lie (telling a lie) | lie | `谎言`, `说谎`, `撒谎`, `谎`, `lying` | 54 | L35-41; most at L39 (51), L40 (23), L41 (13) |
| 1 | knowingly (with knowledge of the truth) | unclear | `明知`, `␣knowingly` | 50 | L36-52; most at L47 (11), L49 (14), L50 (46) |
| 1 | deny (denying, negating) | lie | `␣denial`, `␣denying`, `否认`, `否定`, `␣deny`, `␣denied`, `␣denies` | 45 | L55-58; most at L56 (45), L57 (34), L58 (32) |
| 1 | deliberate (doing it on purpose) | unclear | `␣intentionally`, `故意`, `␣deliberately`, `␣deliberate` | 37 | L35-52; most at L35 (21), L36 (30), L49 (14) |
| 1 | deceive (the act of deceiving) | lie | `␣deceptive`, `欺骗` | 23 | L35-54; most at L37 (5), L53 (19), L54 (8) |
| 1 | fabricate (making something up) | lie | `伪造`, `虚构` | 4 | L36-40; most at L36 (4), L40 (1) |
| 1 | refuse (refusing) | unclear | `␣refusal` | 2 | L56-58; most at L56 (1), L57 (1), L58 (2) |
| 1 | exaggerate (exaggerating) | lie | `夸大` | 1 | L51-51; most at L51 (1) |
| 1 | pretext (a false pretext) | lie | `␣pretext` | 5 | L53-57; most at L53 (3), L54 (5), L56 (2) |
| 2 | lie (the act of lying; a lie) | lie | `谎言`, `说谎`, `撒谎`, `谎`, `lying` | 54 | L35-41; most at L39 (51), L40 (23), L41 (13) |
| 2 | deceive (the act of deceiving) | lie | `␣deceptive`, `欺骗` | 23 | L35-54; most at L37 (5), L53 (19), L54 (8) |
| 2 | mislead (leading someone to a wrong belief) | lie | `␣misleading`, `误导` | 154 | L37-58; most at L52 (45), L53 (151), L54 (142) |
| 2 | fabricate (making up content) | lie | `伪造` | 2 | L36-36; most at L36 (2) |
| 2 | fictional (invented, fictional) | unclear | `虚构` | 2 | L36-40; most at L36 (2), L40 (1) |
| 2 | fake (fake, not genuine) | lie | `␣fake`, `fake`, `␣Fake`, `Fake` | 185 | L35-45; most at L35 (120), L36 (175), L37 (164) |
| 2 | exaggerate (overstating) | lie | `夸大` | 1 | L51-51; most at L51 (1) |
| 2 | pretext (a false reason given) | lie | `␣pretext` | 5 | L53-57; most at L53 (3), L54 (5), L56 (2) |
| 2 | deny (denying) | lie | `␣denial`, `␣denying`, `否认`, `␣deny` | 45 | L55-58; most at L56 (45), L57 (34), L58 (32) |
| 2 | refuse (refusing) | unclear | `␣refusal` | 2 | L56-58; most at L56 (1), L57 (1), L58 (2) |
| 2 | honest (honesty, truthfulness, candour) | truth | `␣truthful` | 93 | L36-44; most at L39 (93), L40 (47), L41 (17) |
| 2 | intentional (doing it on purpose, knowingly) | unclear | `明知`, `␣intentionally`, `故意`, `␣knowingly`, `␣deliberate`, `␣deliberately` | 79 | L35-52; most at L36 (40), L49 (28), L50 (50) |
| 2 | mistake (a mistake or error) | unclear | `␣error` | 1 | L43-49; most at L43 (1), L44 (1), L49 (1) |

## q_tok7

| rep | family | side | members | visibility | layer profile |
|---|---|---|---|---|---|
| 1 | deliberate (doing it on purpose) | unclear | `故意`, `有意`, `␣intentionally`, `␣deliberately`, `␣deliberate`, `␣intentional`, `故意的` | 172 | L35-58; most at L52 (139), L54 (160), L57 (106) |
| 1 | knowingly (with knowledge of the truth) | unclear | `␣knowingly`, `明知` | 127 | L49-58; most at L51 (63), L52 (126), L56 (37) |
| 1 | lie (telling a lie) | lie | `谎`, `谎言`, `␣거짓`, `␣liar` | 84 | L36-58; most at L55 (55), L56 (61), L57 (75) |
| 1 | deceive (the act of deceiving) | lie | `欺骗` | 1 | L57-57; most at L57 (1) |
| 1 | contradict (contradiction) | unclear | `␣contrad`, `␣contradictory` | 13 | L35-58; most at L35 (7), L38 (2), L57 (6) |
| 1 | violate (violating a rule) | unclear | `违反`, `违背` | 4 | L53-57; most at L53 (3), L56 (4), L57 (1) |
| 1 | inadvertent (doing it unintentionally) | unclear | `无意` | 2 | L49-49; most at L49 (2) |
| 2 | lie (the act of lying; a lie) | lie | `谎`, `谎言`, `␣거짓` | 84 | L36-58; most at L55 (55), L56 (61), L57 (75) |
| 2 | liar (a person who lies) | lie | `␣liar` | 2 | L55-56; most at L55 (1), L56 (1) |
| 2 | deceive (the act of deceiving) | lie | `欺骗` | 1 | L57-57; most at L57 (1) |
| 2 | honest (honesty, truthfulness, candour) | truth | `␣truthful` | 22 | L35-41; most at L35 (13), L39 (13), L40 (18) |
| 2 | intentional (doing it on purpose, knowingly) | unclear | `故意`, `␣knowingly`, `有意`, `␣intentionally`, `␣deliberately`, `␣deliberate`, `␣intentional`, `明知`, `故意的` | 177 | L35-58; most at L52 (155), L54 (160), L57 (106) |
| 2 | unintentional (doing it by accident) | unclear | `无意` | 2 | L49-49; most at L49 (2) |
| 2 | violate (breaking a rule) | unclear | `违反`, `违背` | 4 | L53-57; most at L53 (3), L56 (4), L57 (1) |
| 2 | mistake (a mistake or error) | unclear | `␣error` | 10 | L41-44; most at L41 (1), L43 (9), L44 (6) |
| 2 | contradict (contradiction, inconsistency) | unclear | `␣contradictory` | 3 | L35-38; most at L35 (2), L37 (1), L38 (1) |

## Replicate overlap

For each replicate-1 family, the replicate-2 family at the same position sharing the most members.

| position | rep-1 family | best rep-2 family | Jaccard of member ids | only in rep 1 | only in rep 2 |
|---|---|---|---|---|---|
| q_tok0 | lie | lie | 1.00 | — | — |
| q_tok0 | admit | admit | 1.00 | — | — |
| q_tok0 | deny | deny | 1.00 | — | — |
| q_tok0 | truthful | honest | 1.00 | — | — |
| q_tok0 | deliberate | intentional | 0.80 | — | `␣knowingly` |
| q_tok0 | knowingly | intentional | 0.20 | — | `␣intentionally`, `␣deliberate`, `␣intentional`, `␣deliberately` |
| q_tok0 | omit | omit | 1.00 | — | — |
| q_tok0 | comply | comply | 1.00 | — | — |
| q_tok0 | contradict | contradict | 1.00 | — | — |
| q_tok1 | lie | lie | 1.00 | — | — |
| q_tok1 | admit | admit | 1.00 | — | — |
| q_tok1 | honest | honest | 0.60 | — | `诚信`, `如实` |
| q_tok1 | integrity | honest | 0.20 | — | `诚实`, `诚`, `如实`, `坦诚` |
| q_tok1 | truthful | honest | 0.20 | — | `诚信`, `诚实`, `诚`, `坦诚` |
| q_tok1 | comply | comply | 1.00 | — | — |
| q_tok1 | knowingly | intentional | 1.00 | — | — |
| q_tok1 | refuse | refuse | 1.00 | — | — |
| q_tok1 | deny | deny | 1.00 | — | — |
| q_tok1 | contradict | contradict | 1.00 | — | — |
| q_tok1 | exaggerate | exaggerate | 1.00 | — | — |
| q_tok1 | conscience | — | 0 | all | — |
| q_tok1 | oversight | — | 0 | all | — |
| q_tok2 | admit | admit | 1.00 | — | — |
| q_tok2 | deny | deny | 0.67 | `否定` | — |
| q_tok2 | contradict | contradict | 1.00 | — | — |
| q_tok2 | noncompliant | — | 0 | all | — |
| q_tok3 | violate | violate | 0.77 | `␣Viol`, `触犯`, `Viol` | — |
| q_tok3 | comply | comply | 0.83 | `符合`, `是否符合` | — |
| q_tok3 | noncompliant | — | 0 | all | — |
| q_tok3 | inadvertent | unintentional | 1.00 | — | — |
| q_tok3 | deliberate | intentional | 1.00 | — | — |
| q_tok3 | contradict | contradict | 0.50 | `␣contrad` | — |
| q_tok3 | perfunctory | perfunctory | 1.00 | — | — |
| q_tok3 | truthful | honest | 0.40 | — | `␣honestly`, `诚实`, `诚` |
| q_tok3 | honest | honest | 0.60 | — | `如实`, `␣truthful` |
| q_tok3 | admit | admit | 0.67 | — | `␣acknowledge`, `␣acknowledging`, `␣acknowledges` |
| q_tok3 | acknowledge | admit | 0.33 | — | `承认`, `␣admissions`, `␣admit`, `␣admitting`, `␣admits`, `␣admission` |
| q_tok3 | deny | deny | 0.50 | `否定` | — |
| q_tok3 | lie | lie | 1.00 | — | — |
| q_tok3 | refuse | refuse | 0.67 | `拒` | — |
| q_tok3 | evade | evade | 1.00 | — | — |
| q_tok3 | euphemistic | euphemistic | 1.00 | — | — |
| q_tok3 | omit | omit | 1.00 | — | — |
| q_tok3 | leak | leak | 0.50 | `␣leak` | — |
| q_tok3 | conceal | conceal | 1.00 | — | — |
| q_tok3 | hallucinate | hallucinate | 1.00 | — | — |
| q_tok3 | fabricate | fictional | 1.00 | — | — |
| q_tok4 | hallucinate | hallucinate | 1.00 | — | — |
| q_tok4 | violate | violate | 1.00 | — | — |
| q_tok4 | lie | lie | 1.00 | — | — |
| q_tok4 | truthful | honest | 1.00 | — | — |
| q_tok4 | deny | deny | 0.50 | `否定` | — |
| q_tok4 | comply | comply | 0.50 | `符合` | — |
| q_tok4 | deliberate | intentional | 1.00 | — | — |
| q_tok4 | refuse | refuse | 1.00 | — | — |
| q_tok4 | fabricate | fabricate | 1.00 | — | — |
| q_tok4 | misinformation | misinformation | 1.00 | — | — |
| q_tok4 | conceal | hidden | 1.00 | — | — |
| q_tok4 | deceive | deceive | 1.00 | — | — |
| q_tok5 | lie | lie | 0.94 | `␣liar` | — |
| q_tok5 | hallucinate | hallucinate | 1.00 | — | — |
| q_tok5 | fabricate | fabricate | 0.75 | `虚构` | — |
| q_tok5 | fiction | fictional | 0.83 | — | `虚构` |
| q_tok5 | fake | fake | 1.00 | — | — |
| q_tok5 | violate | violate | 0.86 | `␣Viol`, `␣viol` | — |
| q_tok5 | contradict | contradict | 0.78 | `␣contrad`, `␣contradd` | — |
| q_tok5 | conceal | conceal | 0.77 | `␣hidden`, `hidden` | `瞒` |
| q_tok5 | honest | honest | 0.62 | — | `␣truthful`, `诚信`, `如实` |
| q_tok5 | integrity | honest | 0.12 | — | `␣truthful`, `诚实`, `如实`, `诚`, `坦诚`, `␣honesty`, `␣honest` |
| q_tok5 | dishonest | dishonest | 1.00 | — | — |
| q_tok5 | truthful | honest | 0.25 | — | `诚实`, `诚信`, `诚`, `坦诚`, `␣honesty`, `␣honest` |
| q_tok5 | refuse | refuse | 0.73 | `拒`, `拒絕`, `拒不` | — |
| q_tok5 | deny | deny | 0.56 | `否定`, `␣denied`, `␣denies`, `␣Denied` | — |
| q_tok5 | deliberate | intentional | 0.71 | — | `明知`, `␣knowingly` |
| q_tok5 | knowingly | intentional | 0.29 | — | `␣deliberate`, `␣deliberately`, `故意`, `␣intentionally`, `␣intentional` |
| q_tok5 | ethics | ethical | 1.00 | — | — |
| q_tok5 | unethical | unethical | 1.00 | — | — |
| q_tok5 | admit | admit | 0.60 | — | `␣acknowledges`, `␣confession`, `␣acknowledge`, `␣acknowledging`, `␣acknowledgment`, `坦白` |
| q_tok5 | acknowledge | admit | 0.27 | — | `承认`, `␣admissions`, `␣admitting`, `␣admission`, `␣admit`, `␣admits`, `␣Admission`, `␣admitted`, `␣confession`, `坦白`, `␣admite` |
| q_tok5 | confess | admit | 0.13 | — | `承认`, `␣admissions`, `␣admitting`, `␣admission`, `␣admit`, `␣admits`, `␣Admission`, `␣admitted`, `␣acknowledges`, `␣acknowledge`, `␣acknowledging`, `␣acknowledgment`, `␣admite` |
| q_tok5 | disclose | disclose | 0.67 | `披露`, `暴露`, `␣exposing` | — |
| q_tok5 | leak | leak | 1.00 | — | — |
| q_tok5 | transparent | transparent | 1.00 | — | — |
| q_tok5 | deceive | deceive | 1.00 | — | — |
| q_tok5 | mislead | mislead | 1.00 | — | — |
| q_tok5 | misinformation | misinformation | 1.00 | — | — |
| q_tok5 | manipulate | manipulate | 0.80 | `操纵` | — |
| q_tok5 | role-play | role-play | 1.00 | — | — |
| q_tok5 | simulate | — | 0 | all | — |
| q_tok5 | evade | evade | 0.75 | `规避` | — |
| q_tok5 | euphemistic | euphemistic | 1.00 | — | — |
| q_tok5 | perfunctory | perfunctory | 1.00 | — | — |
| q_tok5 | vague | — | 0 | all | — |
| q_tok5 | apologize | apologize | 1.00 | — | — |
| q_tok5 | secret | secret | 0.80 | — | `保密` |
| q_tok5 | omit | omit | 1.00 | — | — |
| q_tok5 | exaggerate | exaggerate | 1.00 | — | — |
| q_tok5 | inadvertent | unintentional | 1.00 | — | — |
| q_tok5 | comply | comply | 0.69 | `符合`, `是否符合`, `符合要求`, `必须符合`, `符合国家` | — |
| q_tok5 | noncompliant | — | 0 | all | — |
| q_tok6 | fake | fake | 1.00 | — | — |
| q_tok6 | mislead | mislead | 1.00 | — | — |
| q_tok6 | lie | lie | 1.00 | — | — |
| q_tok6 | knowingly | intentional | 0.33 | — | `␣intentionally`, `故意`, `␣deliberate`, `␣deliberately` |
| q_tok6 | deny | deny | 0.57 | `否定`, `␣denied`, `␣denies` | — |
| q_tok6 | deliberate | intentional | 0.67 | — | `明知`, `␣knowingly` |
| q_tok6 | deceive | deceive | 1.00 | — | — |
| q_tok6 | fabricate | fabricate | 0.50 | `虚构` | — |
| q_tok6 | refuse | refuse | 1.00 | — | — |
| q_tok6 | exaggerate | exaggerate | 1.00 | — | — |
| q_tok6 | pretext | pretext | 1.00 | — | — |
| q_tok7 | deliberate | intentional | 0.78 | — | `␣knowingly`, `明知` |
| q_tok7 | knowingly | intentional | 0.22 | — | `故意`, `有意`, `␣intentionally`, `␣deliberately`, `␣deliberate`, `␣intentional`, `故意的` |
| q_tok7 | lie | lie | 0.75 | `␣liar` | — |
| q_tok7 | deceive | deceive | 1.00 | — | — |
| q_tok7 | contradict | contradict | 0.50 | `␣contrad` | — |
| q_tok7 | violate | violate | 1.00 | — | — |
| q_tok7 | inadvertent | unintentional | 1.00 | — | — |

Replicate-2 families not the best match of any replicate-1 family: q_tok0: secret, q_tok1: secret, q_tok3: imply, q_tok4: mistake, q_tok5: liar, q_tok5: hidden, q_tok5: imply, q_tok5: mistake, q_tok6: fictional, q_tok6: honest, q_tok6: mistake, q_tok7: liar, q_tok7: honest, q_tok7: mistake

## Families whose name recurs at 3 or more positions

- admit: q_tok0, q_tok1, q_tok2, q_tok3, q_tok5
- comply: q_tok0, q_tok1, q_tok3, q_tok4, q_tok5
- conceal: q_tok3, q_tok4, q_tok5
- contradict: q_tok0, q_tok1, q_tok2, q_tok3, q_tok5, q_tok7
- deceive: q_tok4, q_tok5, q_tok6, q_tok7
- deliberate: q_tok0, q_tok3, q_tok4, q_tok5, q_tok6, q_tok7
- deny: q_tok0, q_tok1, q_tok2, q_tok3, q_tok4, q_tok5, q_tok6
- exaggerate: q_tok1, q_tok5, q_tok6
- fabricate: q_tok3, q_tok4, q_tok5, q_tok6
- fictional: q_tok3, q_tok5, q_tok6
- hallucinate: q_tok3, q_tok4, q_tok5
- honest: q_tok0, q_tok1, q_tok3, q_tok4, q_tok5, q_tok6, q_tok7
- inadvertent: q_tok3, q_tok5, q_tok7
- intentional: q_tok0, q_tok1, q_tok3, q_tok4, q_tok5, q_tok6, q_tok7
- knowingly: q_tok0, q_tok1, q_tok5, q_tok6, q_tok7
- lie: q_tok0, q_tok1, q_tok3, q_tok4, q_tok5, q_tok6, q_tok7
- mistake: q_tok4, q_tok5, q_tok6, q_tok7
- noncompliant: q_tok2, q_tok3, q_tok5
- omit: q_tok0, q_tok3, q_tok5
- refuse: q_tok1, q_tok3, q_tok4, q_tok5, q_tok6
- secret: q_tok0, q_tok1, q_tok5
- truthful: q_tok0, q_tok1, q_tok3, q_tok4, q_tok5
- unintentional: q_tok3, q_tok5, q_tok7
- violate: q_tok3, q_tok4, q_tok5, q_tok7

## Candidate opposite pairs (same position, lie side vs truth side, antonym words in the names or glosses; merged list)

- q_tok0: deny / admit
- q_tok0: lie / truthful
- q_tok0: secret / admit
- q_tok1: deny / admit
- q_tok1: lie / truthful
- q_tok1: secret / admit
- q_tok2: deny / admit
- q_tok3: deny / admit
- q_tok3: evade / admit
- q_tok3: lie / truthful
- q_tok4: lie / truthful
- q_tok5: conceal / disclose
- q_tok5: deceive / honest
- q_tok5: deny / admit
- q_tok5: deny / confess
- q_tok5: dishonest / honest
- q_tok5: evade / admit
- q_tok5: hidden / admit
- q_tok5: hidden / confess
- q_tok5: hidden / disclose
- q_tok5: liar / truthful
- q_tok5: lie / truthful
- q_tok5: secret / admit
- q_tok5: secret / confess
- q_tok6: deceive / honest
- q_tok6: lie / honest
- q_tok7: deceive / honest
- q_tok7: liar / honest
- q_tok7: lie / honest

Merged candidate list: `qwen3_6_27b_LL_Q6_factual_questiona_merged.json` (132 families; replicate-2 families sharing at least half
their members with a replicate-1 family at the same position are folded into it).
