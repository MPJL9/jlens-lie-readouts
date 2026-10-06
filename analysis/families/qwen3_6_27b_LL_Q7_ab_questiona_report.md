# Family report: qwen3.6-27b, logit lens, band 35-58, part Q7_ab, group questiona

Written by `scripts/family_report.py` from `qwen3_6_27b_LL_Q7_ab_questiona_rep1.json` and `_rep2.json` (prompt
`prompts/family_generation.md`). Visibility = build-split scenario transcripts (of 233) in which
at least one member is present at the position within the band. Layer profile = band layers where
the family is present in at least one transcript, and the three layers with the most transcripts
(description only; scoring uses the whole band).

## q_tok0

| rep | family | side | members | visibility | layer profile |
|---|---|---|---|---|---|
| 1 | deny (denying (a claim or the truth)) | lie | `否认` | 1 | L35-36; most at L35 (1), L36 (1) |
| 1 | admit (admitting) | truth | `承认` | 1 | L36-40; most at L36 (1), L37 (1), L38 (1) |
| 1 | truth (the truth (noun)) | truth | `␣truth` | 1 | L39-40; most at L39 (1), L40 (1) |
| 1 | deliberate (on purpose, intentionally) | unclear | `␣intentionally`, `␣intentional`, `␣deliberate`, `␣deliberately` | 4 | L49-58; most at L52 (3), L55 (2), L56 (2) |
| 1 | knowingly (knowingly, with knowledge (明知)) | unclear | `␣knowingly` | 2 | L51-58; most at L51 (2), L52 (2), L53 (2) |
| 1 | misunderstand (misunderstanding) | unclear | `␣misunderstand`, `␣misunderstood` | 5 | L52-58; most at L53 (5), L57 (3), L58 (4) |
| 1 | contradict (contradicting, contradiction) | unclear | `␣contradict` | 1 | L39-48; most at L39 (1), L40 (1), L41 (1) |
| 1 | fact (fact, factual) | unclear | `事实` | 1 | L45-45; most at L45 (1) |
| 2 | deny (denying) | lie | `否认` | 1 | L35-36; most at L35 (1), L36 (1) |
| 2 | contradiction (contradicting, being inconsistent) | unclear | `␣contradict` | 1 | L39-48; most at L39 (1), L40 (1), L41 (1) |
| 2 | deliberate (doing it on purpose) | unclear | `␣intentionally`, `␣deliberate`, `␣intentional`, `␣deliberately` | 4 | L49-58; most at L52 (3), L55 (2), L56 (2) |
| 2 | knowingly (doing it with knowledge of the facts) | unclear | `知情`, `␣knowingly` | 11 | L35-58; most at L35 (5), L37 (7), L39 (3) |
| 2 | admit (admitting) | truth | `承认` | 1 | L36-40; most at L36 (1), L37 (1), L38 (1) |

## q_tok1

| rep | family | side | members | visibility | layer profile |
|---|---|---|---|---|---|
| 1 | deceive (the act of deceiving) | lie | `欺骗`, `骗`, `␣deception` | 6 | L35-58; most at L39 (3), L40 (3), L52 (2) |
| 1 | fraud (defrauding, obtaining something by deceit) | lie | `␣fraud` | 1 | L39-41; most at L39 (1), L41 (1) |
| 1 | conceal (hiding or covering up information) | lie | `隐瞒`, `瞒`, `隐藏`, `掩盖`, `␣conceal`, `掩饰`, `␣hiding`, `␣hidden`, `␣hide`, `hide`, `␣hides`, `-hidden`, `遮盖`, `隐藏的` | 63 | L35-58; most at L36 (28), L39 (41), L40 (37) |
| 1 | withhold (withholding information) | lie | `␣withholding` | 1 | L52-53; most at L52 (1), L53 (1) |
| 1 | omit (leaving information out) | lie | `省略`, `␣omit` | 5 | L36-49; most at L37 (2), L48 (2), L49 (1) |
| 1 | mislead (misleading someone) | lie | `误导` | 1 | L41-48; most at L41 (1), L46 (1), L47 (1) |
| 1 | fabricate (making up content that is not real) | lie | `伪造`, `虚构`, `␣fabricated`, `␣invent` | 18 | L35-58; most at L36 (5), L37 (4), L51 (5) |
| 1 | groundless (out of thin air, without basis (凭空)) | lie | `凭空` | 27 | L35-53; most at L36 (19), L37 (17), L38 (9) |
| 1 | fake (fake, not genuine) | lie | `fake`, `␣fake`, `_fake` | 12 | L35-46; most at L35 (7), L36 (3), L37 (6) |
| 1 | exaggerate (exaggerating) | lie | `夸大` | 3 | L36-58; most at L39 (1), L40 (1), L42 (1) |
| 1 | dishonest (dishonest) | lie | `␣dishonest` | 1 | L40-40; most at L40 (1) |
| 1 | deny (denying (a claim or the truth)) | lie | `否认`, `否定` | 44 | L35-57; most at L35 (19), L36 (27), L37 (18) |
| 1 | secret (secret, secrecy) | lie | `␣secret`, `␣secretly`, `秘密`, `secret`, `␣Secret`, `的秘密` | 5 | L35-57; most at L37 (1), L56 (2), L57 (2) |
| 1 | honest (honest, honesty) | truth | `诚实`, `诚`, `␣honestly`, `␣honesty`, `␣honest`, `␣Honest` | 58 | L35-58; most at L38 (28), L39 (30), L40 (33) |
| 1 | integrity (integrity, trustworthiness (诚信)) | truth | `诚信` | 38 | L35-58; most at L39 (21), L40 (22), L41 (16) |
| 1 | candid (candid, upfront) | truth | `坦诚` | 20 | L36-58; most at L38 (11), L39 (13), L40 (16) |
| 1 | confess (confessing, owning up (坦白)) | truth | `坦白` | 4 | L37-41; most at L37 (1), L39 (3), L41 (2) |
| 1 | admit (admitting) | truth | `承认`, `␣admit`, `␣admitting` | 77 | L35-58; most at L35 (39), L36 (46), L37 (62) |
| 1 | disclose (disclosing information) | truth | `信息披露`, `␣disclosure`, `␣disclose` | 7 | L36-58; most at L36 (4), L38 (5), L39 (3) |
| 1 | transparent (transparent, transparency) | truth | `␣transparent`, `透明`, `透明的`, `␣transparency`, `␣Transparency`, `透明度` | 14 | L35-54; most at L38 (11), L39 (9), L41 (8) |
| 1 | truth (the truth (noun)) | truth | `␣truth`, `实话`, `truth`, `␣Truth`, `Truth`, `真相` | 43 | L37-58; most at L39 (28), L40 (34), L41 (26) |
| 1 | sincere (sincere, genuine, in earnest) | truth | `␣genuinely` | 2 | L50-58; most at L51 (2), L52 (2), L54 (2) |
| 1 | deliberate (on purpose, intentionally) | unclear | `␣intentionally`, `␣deliberately`, `故意`, `刻意`, `␣deliberate`, `特意`, `␣intentional`, `故意的` | 94 | L35-58; most at L54 (67), L56 (62), L57 (56) |
| 1 | knowingly (knowingly, with knowledge (明知)) | unclear | `明知`, `␣knowingly` | 82 | L35-58; most at L35 (37), L36 (36), L58 (37) |
| 1 | intention (intention (noun)) | unclear | `␣intention` | 1 | L55-55; most at L55 (1) |
| 1 | accidental (by accident, unintentionally) | unclear | `␣accidentally`, `␣случайно`, `␣accidental` | 26 | L53-58; most at L53 (15), L56 (16), L57 (13) |
| 1 | misunderstand (misunderstanding) | unclear | `␣misunderstand` | 17 | L53-58; most at L56 (8), L57 (14), L58 (13) |
| 1 | contradict (contradicting, contradiction) | unclear | `␣contradict`, `矛盾`, `␣contrad`, `矛盾的` | 52 | L35-54; most at L47 (30), L48 (39), L49 (45) |
| 1 | violate (violating a rule, duty or law) | unclear | `违反`, `违`, `违背`, `␣violate`, `违规` | 42 | L35-58; most at L39 (20), L41 (20), L47 (20) |
| 1 | refuse (refusing) | unclear | `拒绝`, `␣refusal` | 3 | L39-48; most at L39 (2), L40 (3), L41 (2) |
| 1 | evade (evading, avoiding the question) | unclear | `回避` | 6 | L35-58; most at L36 (3), L46 (2), L48 (2) |
| 1 | perfunctory (brushing off, answering perfunctorily (敷衍)) | unclear | `敷衍` | 24 | L35-52; most at L35 (19), L36 (17), L46 (8) |
| 1 | euphemistic (euphemistic, tactfully indirect (委婉)) | unclear | `委婉` | 2 | L36-41; most at L36 (2), L39 (2), L40 (2) |
| 1 | excuse (an excuse) | unclear | `借口`, `␣excuse` | 2 | L42-54; most at L42 (1), L52 (1), L54 (1) |
| 1 | inform (informing, telling someone (告知)) | unclear | `告知` | 35 | L35-58; most at L37 (24), L38 (22), L39 (16) |
| 1 | objective (objective, impartial (客观)) | unclear | `客观` | 11 | L35-51; most at L36 (4), L37 (3), L47 (5) |
| 1 | fact (fact, factual) | unclear | `␣fact`, `事实`, `␣factual` | 14 | L36-55; most at L39 (4), L44 (5), L52 (4) |
| 1 | ethics (ethics, morality) | unclear | `␣ethical`, `␣ethics` | 1 | L35-53; most at L35 (1), L36 (1), L37 (1) |
| 1 | conscience (conscience (良心)) | unclear | `良心` | 1 | L36-42; most at L36 (1), L37 (1), L38 (1) |
| 1 | apologize (apologizing (道歉)) | unclear | `道歉` | 1 | L35-35; most at L35 (1) |
| 1 | confidential (confidentiality) | unclear | `␣confidentiality` | 1 | L37-38; most at L37 (1), L38 (1) |
| 2 | deceive (the act of deceiving) | lie | `欺骗`, `骗`, `欺`, `␣deception` | 7 | L35-58; most at L39 (3), L40 (3), L50 (3) |
| 2 | mislead (leading someone to a wrong belief) | lie | `误导` | 1 | L41-48; most at L41 (1), L46 (1), L47 (1) |
| 2 | fraud (fraud, cheating for gain) | lie | `␣fraud` | 1 | L39-41; most at L39 (1), L41 (1) |
| 2 | betray (betraying, selling out) | lie | `出卖` | 1 | L35-52; most at L35 (1), L52 (1) |
| 2 | conceal (hiding or concealing information) | lie | `隐瞒`, `瞒`, `隐藏`, `藏`, `␣conceal`, `␣hiding`, `␣hidden`, `隐藏的`, `␣hide`, `hide`, `␣hides`, `-hidden` | 65 | L35-58; most at L39 (41), L40 (38), L41 (27) |
| 2 | cover up (covering up or masking the truth) | lie | `掩盖`, `掩饰`, `遮`, `掩`, `遮盖` | 14 | L35-58; most at L36 (9), L38 (3), L40 (7) |
| 2 | secret (keeping something secret) | lie | `␣secret`, `␣secretly`, `秘密`, `␣Secret`, `secret`, `的秘密` | 5 | L35-57; most at L37 (1), L56 (2), L57 (2) |
| 2 | confidential (confidentiality) | unclear | `␣confidentiality` | 1 | L37-38; most at L37 (1), L38 (1) |
| 2 | withhold (withholding information) | lie | `␣withholding` | 1 | L52-53; most at L52 (1), L53 (1) |
| 2 | omit (leaving information out) | lie | `省略`, `␣omit` | 5 | L36-49; most at L37 (2), L48 (2), L49 (1) |
| 2 | fabricate (making up a story or facts) | lie | `凭空`, `虚构`, `␣fabricated`, `␣invent` | 30 | L35-58; most at L36 (20), L37 (18), L38 (9) |
| 2 | fake (faking or forging) | lie | `fake`, `伪造`, `␣fake`, `_fake` | 19 | L35-58; most at L35 (7), L36 (4), L37 (8) |
| 2 | role-play (playing a role) | unclear | `扮演`, `角色扮演` | 21 | L35-58; most at L39 (14), L40 (15), L43 (14) |
| 2 | exaggerate (exaggerating) | lie | `夸大`, `␣exagger` | 4 | L36-58; most at L54 (2), L55 (2), L56 (2) |
| 2 | evade (evading or dodging the question) | lie | `回避` | 6 | L35-58; most at L36 (3), L46 (2), L48 (2) |
| 2 | perfunctory (answering perfunctorily, brushing off) | unclear | `敷衍`, `应付` | 29 | L35-52; most at L35 (19), L36 (17), L43 (10) |
| 2 | euphemistic (wording things euphemistically) | unclear | `委婉` | 2 | L36-41; most at L36 (2), L39 (2), L40 (2) |
| 2 | insinuate (hinting or implying) | unclear | `暗示` | 8 | L36-54; most at L36 (2), L38 (4), L39 (3) |
| 2 | deny (denying) | lie | `否认` | 33 | L35-57; most at L35 (18), L36 (25), L37 (17) |
| 2 | negate (negating, repudiating) | unclear | `否定` | 26 | L35-57; most at L35 (9), L48 (8), L53 (16) |
| 2 | refuse (refusing) | unclear | `拒绝`, `␣refusal` | 3 | L39-48; most at L39 (2), L40 (3), L41 (2) |
| 2 | contradiction (contradicting, being inconsistent) | unclear | `␣contradict`, `矛盾`, `␣contrad`, `矛盾的` | 52 | L35-54; most at L47 (30), L48 (39), L49 (45) |
| 2 | consistent (being consistent) | unclear | `一致`, `一致的` | 8 | L38-44; most at L40 (3), L41 (2), L42 (3) |
| 2 | deliberate (doing it on purpose) | unclear | `␣intentionally`, `␣deliberately`, `故意`, `刻意`, `␣deliberate`, `␣intentional`, `故意的`, `有意` | 88 | L35-58; most at L54 (66), L56 (61), L57 (56) |
| 2 | knowingly (doing it with knowledge of the facts) | unclear | `明知`, `知情`, `␣knowingly`, `␣knowing`, `␣Knowing` | 110 | L35-58; most at L35 (53), L36 (41), L51 (41) |
| 2 | accidental (doing it by accident) | unclear | `␣accidentally`, `␣случайно`, `␣accident`, `␣accidental`, `意外` | 26 | L38-58; most at L53 (15), L56 (16), L57 (13) |
| 2 | intention (the model's intention or motive) | unclear | `␣intention` | 1 | L55-55; most at L55 (1) |
| 2 | violate (violating a rule or principle) | lie | `违反`, `违`, `违背`, `违规` | 42 | L35-57; most at L39 (20), L41 (20), L47 (20) |
| 2 | ethics (ethics, morality) | unclear | `␣ethical`, `␣ethics` | 1 | L35-53; most at L35 (1), L36 (1), L37 (1) |
| 2 | apologize (apologizing) | unclear | `道歉` | 1 | L35-35; most at L35 (1) |
| 2 | honest (being honest) | truth | `诚实`, `诚`, `␣honestly`, `␣honesty`, `␣honest`, `␣Honest` | 58 | L35-58; most at L38 (28), L39 (30), L40 (33) |
| 2 | dishonest (being dishonest) | lie | `␣dishonest` | 1 | L40-40; most at L40 (1) |
| 2 | integrity (integrity, keeping one's word) | truth | `诚信` | 38 | L35-58; most at L39 (21), L40 (22), L41 (16) |
| 2 | candid (being candid, upfront) | truth | `坦诚` | 20 | L36-58; most at L38 (11), L39 (13), L40 (16) |
| 2 | confess (confessing, owning up) | truth | `坦白` | 4 | L37-41; most at L37 (1), L39 (3), L41 (2) |
| 2 | admit (admitting) | truth | `承认`, `␣admit`, `␣admitting` | 77 | L35-58; most at L35 (39), L36 (46), L37 (62) |
| 2 | transparent (being transparent) | truth | `␣transparent`, `透明`, `透明的`, `␣transparency`, `␣Transparency`, `透明度` | 14 | L35-54; most at L38 (11), L39 (9), L41 (8) |
| 2 | disclose (disclosing information) | truth | `信息披露`, `␣disclosure`, `␣disclose` | 7 | L36-58; most at L36 (4), L38 (5), L39 (3) |

## q_tok2

| rep | family | side | members | visibility | layer profile |
|---|---|---|---|---|---|
| 1 | deceive (the act of deceiving) | lie | `欺骗`, `骗`, `␣deception` | 233 | L35-57; most at L39 (233), L40 (217), L41 (222) |
| 1 | conceal (hiding or covering up information) | lie | `隐瞒`, `␣conceal`, `掩盖`, `瞒`, `掩饰` | 202 | L35-58; most at L36 (177), L39 (141), L40 (172) |
| 1 | omit (leaving information out) | lie | `␣omission`, `␣omit`, `omit`, `␣OMIT` | 91 | L36-58; most at L52 (84), L53 (45), L56 (17) |
| 1 | mislead (misleading someone) | lie | `误导` | 1 | L37-37; most at L37 (1) |
| 1 | fabricate (making up content that is not real) | lie | `␣invent`, `虚构`, `␣invented` | 3 | L35-38; most at L35 (1), L36 (2), L37 (3) |
| 1 | groundless (out of thin air, without basis (凭空)) | lie | `凭空` | 1 | L37-43; most at L37 (1), L43 (1) |
| 1 | fake (fake, not genuine) | lie | `fake`, `␣fake`, `Fake`, `␣Fake` | 195 | L35-49; most at L35 (195), L36 (130), L37 (90) |
| 1 | honest (honest, honesty) | truth | `诚实`, `␣honest`, `诚实守信` | 217 | L35-49; most at L39 (204), L40 (212), L41 (200) |
| 1 | integrity (integrity, trustworthiness (诚信)) | truth | `诚信` | 233 | L35-58; most at L40 (233), L41 (233), L42 (233) |
| 1 | candid (candid, upfront) | truth | `␣upfront` | 6 | L51-56; most at L52 (5), L53 (5), L54 (5) |
| 1 | admit (admitting) | truth | `承认` | 1 | L48-48; most at L48 (1) |
| 1 | truth (the truth (noun)) | truth | `␣truth`, `truth`, `真相`, `␣Truth`, `Truth`, `␣truths` | 233 | L35-56; most at L35 (222), L40 (225), L41 (227) |
| 1 | deliberate (on purpose, intentionally) | unclear | `故意`, `␣intentionally`, `␣deliberately`, `␣deliberate`, `故意的`, `␣intentional` | 75 | L35-58; most at L36 (33), L47 (41), L50 (26) |
| 1 | knowingly (knowingly, with knowledge (明知)) | unclear | `␣knowingly`, `明知` | 5 | L44-52; most at L44 (3), L48 (3), L51 (2) |
| 1 | intention (intention (noun)) | unclear | `␣intentions` | 1 | L49-49; most at L49 (1) |
| 1 | accuse (accusation) | unclear | `指控` | 1 | L35-36; most at L35 (1), L36 (1) |
| 1 | inform (informing, telling someone (告知)) | unclear | `告知` | 14 | L35-58; most at L54 (11), L55 (11), L56 (10) |
| 1 | fact (fact, factual) | unclear | `事实`, `␣factual`, `␣facts` | 12 | L36-50; most at L41 (4), L44 (7), L45 (5) |
| 2 | deceive (the act of deceiving) | lie | `欺骗`, `骗`, `␣deception` | 233 | L35-57; most at L39 (233), L40 (217), L41 (222) |
| 2 | mislead (leading someone to a wrong belief) | lie | `误导` | 1 | L37-37; most at L37 (1) |
| 2 | betray (betraying, selling out) | lie | `出卖` | 3 | L35-37; most at L35 (1), L36 (2), L37 (3) |
| 2 | conceal (hiding or concealing information) | lie | `隐瞒`, `␣conceal`, `瞒` | 202 | L35-58; most at L36 (177), L39 (141), L40 (172) |
| 2 | cover up (covering up or masking the truth) | lie | `掩盖`, `掩饰` | 12 | L35-53; most at L35 (8), L36 (12), L37 (5) |
| 2 | omit (leaving information out) | lie | `␣omission`, `␣omit`, `omit`, `␣OMIT` | 91 | L36-58; most at L52 (84), L53 (45), L56 (17) |
| 2 | fabricate (making up a story or facts) | lie | `␣invent`, `虚构`, `凭空`, `␣invented` | 3 | L35-43; most at L35 (1), L36 (2), L37 (3) |
| 2 | fake (faking or forging) | lie | `fake`, `␣fake`, `Fake`, `␣Fake` | 195 | L35-49; most at L35 (195), L36 (130), L37 (90) |
| 2 | deliberate (doing it on purpose) | unclear | `故意`, `␣intentionally`, `␣deliberately`, `␣deliberate`, `故意的`, `␣intentional`, `有意` | 75 | L35-58; most at L36 (33), L47 (41), L50 (26) |
| 2 | knowingly (doing it with knowledge of the facts) | unclear | `␣knowingly`, `明知`, `知情` | 5 | L37-52; most at L44 (3), L48 (3), L51 (2) |
| 2 | intention (the model's intention or motive) | unclear | `␣intentions` | 1 | L49-49; most at L49 (1) |
| 2 | accusation (being accused, a charge) | unclear | `指控` | 1 | L35-36; most at L35 (1), L36 (1) |
| 2 | honest (being honest) | truth | `诚实`, `␣honest`, `诚实守信` | 217 | L35-49; most at L39 (204), L40 (212), L41 (200) |
| 2 | integrity (integrity, keeping one's word) | truth | `诚信` | 233 | L35-58; most at L40 (233), L41 (233), L42 (233) |
| 2 | candid (being candid, upfront) | truth | `␣upfront` | 6 | L51-56; most at L52 (5), L53 (5), L54 (5) |
| 2 | admit (admitting) | truth | `承认` | 1 | L48-48; most at L48 (1) |

## q_tok3

| rep | family | side | members | visibility | layer profile |
|---|---|---|---|---|---|
| 1 | deceive (the act of deceiving) | lie | `欺骗`, `␣deception`, `骗` | 17 | L35-41; most at L38 (4), L39 (17), L40 (5) |
| 1 | conceal (hiding or covering up information) | lie | `隐瞒`, `掩盖`, `hide`, `␣hiding`, `␣conceal`, `␣hide`, `Hide`, `瞒`, `掩饰`, `隐匿` | 65 | L35-42; most at L36 (51), L39 (34), L40 (20) |
| 1 | disguise (disguising the true nature of something) | lie | `␣disguise` | 64 | L35-50; most at L36 (52), L49 (17), L50 (17) |
| 1 | mislead (misleading someone) | lie | `误导`, `␣misleading` | 13 | L35-42; most at L36 (11), L37 (9), L38 (10) |
| 1 | fake (fake, not genuine) | lie | `fake`, `␣fake` | 12 | L35-42; most at L35 (9), L36 (9), L41 (2) |
| 1 | exaggerate (exaggerating) | lie | `夸大` | 1 | L40-40; most at L40 (1) |
| 1 | deny (denying (a claim or the truth)) | lie | `否认`, `␣denial`, `否定` | 56 | L35-46; most at L36 (35), L37 (40), L40 (33) |
| 1 | honest (honest, honesty) | truth | `诚实`, `␣honest`, `␣honesty` | 20 | L35-50; most at L35 (7), L39 (9), L40 (6) |
| 1 | integrity (integrity, trustworthiness (诚信)) | truth | `诚信` | 91 | L35-50; most at L36 (56), L41 (62), L42 (61) |
| 1 | candid (candid, upfront) | truth | `坦诚` | 1 | L38-40; most at L38 (1), L39 (1), L40 (1) |
| 1 | admit (admitting) | truth | `承认` | 2 | L37-45; most at L37 (1), L39 (1), L40 (2) |
| 1 | disclose (disclosing information) | truth | `信息披露` | 6 | L36-39; most at L36 (3), L37 (1), L38 (4) |
| 1 | transparent (transparent, transparency) | truth | `透明` | 3 | L35-39; most at L35 (1), L36 (1), L39 (1) |
| 1 | truth (the truth (noun)) | truth | `␣truth`, `␣Truth`, `Truth`, `真相` | 76 | L35-42; most at L36 (34), L39 (45), L40 (52) |
| 1 | sincere (sincere, genuine, in earnest) | truth | `␣earnest` | 29 | L48-53; most at L50 (15), L51 (21), L52 (20) |
| 1 | deliberate (on purpose, intentionally) | unclear | `故意` | 29 | L35-50; most at L35 (9), L36 (20), L50 (6) |
| 1 | knowingly (knowingly, with knowledge (明知)) | unclear | `明知`, `␣knowingly` | 68 | L35-52; most at L35 (43), L36 (51), L37 (29) |
| 1 | contradict (contradicting, contradiction) | unclear | `␣contrad`, `␣contradict` | 8 | L35-50; most at L37 (3), L45 (3), L48 (4) |
| 1 | violate (violating a rule, duty or law) | unclear | `违反`, `违背` | 1 | L36-38; most at L36 (1), L37 (1), L38 (1) |
| 1 | euphemistic (euphemistic, tactfully indirect (委婉)) | unclear | `委婉` | 1 | L35-35; most at L35 (1) |
| 1 | inform (informing, telling someone (告知)) | unclear | `告知` | 3 | L35-39; most at L35 (2), L36 (2), L39 (1) |
| 1 | fact (fact, factual) | unclear | `␣fact` | 15 | L35-53; most at L37 (7), L38 (8), L50 (11) |
| 2 | deceive (the act of deceiving) | lie | `欺骗`, `␣deception`, `骗` | 17 | L35-41; most at L38 (4), L39 (17), L40 (5) |
| 2 | mislead (leading someone to a wrong belief) | lie | `误导`, `␣misleading` | 13 | L35-42; most at L36 (11), L37 (9), L38 (10) |
| 2 | betray (betraying, selling out) | lie | `出卖` | 3 | L35-40; most at L35 (1), L36 (3), L37 (2) |
| 2 | conceal (hiding or concealing information) | lie | `隐瞒`, `hide`, `␣hiding`, `␣conceal`, `瞒`, `隐匿`, `␣hide`, `Hide` | 63 | L35-42; most at L36 (50), L39 (33), L40 (16) |
| 2 | cover up (covering up or masking the truth) | lie | `␣disguise`, `掩盖`, `掩饰` | 75 | L35-50; most at L36 (62), L37 (22), L50 (17) |
| 2 | fake (faking or forging) | lie | `fake`, `␣fake` | 12 | L35-42; most at L35 (9), L36 (9), L41 (2) |
| 2 | role-play (playing a role) | unclear | `角色扮演`, `扮演` | 2 | L38-42; most at L38 (2), L39 (1), L40 (1) |
| 2 | exaggerate (exaggerating) | lie | `夸大` | 1 | L40-40; most at L40 (1) |
| 2 | perfunctory (answering perfunctorily, brushing off) | unclear | `应付` | 1 | L39-39; most at L39 (1) |
| 2 | euphemistic (wording things euphemistically) | unclear | `委婉` | 1 | L35-35; most at L35 (1) |
| 2 | deny (denying) | lie | `否认`, `␣denial` | 54 | L35-46; most at L36 (35), L37 (40), L40 (33) |
| 2 | negate (negating, repudiating) | unclear | `否定` | 3 | L40-42; most at L40 (1), L41 (3), L42 (1) |
| 2 | contradiction (contradicting, being inconsistent) | unclear | `␣contrad`, `␣contradict` | 8 | L35-50; most at L37 (3), L45 (3), L48 (4) |
| 2 | deliberate (doing it on purpose) | unclear | `故意` | 29 | L35-50; most at L35 (9), L36 (20), L50 (6) |
| 2 | knowingly (doing it with knowledge of the facts) | unclear | `明知`, `知情`, `␣knowingly` | 69 | L35-52; most at L35 (44), L36 (52), L37 (29) |
| 2 | violate (violating a rule or principle) | lie | `违反`, `违背` | 1 | L36-38; most at L36 (1), L37 (1), L38 (1) |
| 2 | honest (being honest) | truth | `诚实`, `␣honest`, `␣honesty` | 20 | L35-50; most at L35 (7), L39 (9), L40 (6) |
| 2 | integrity (integrity, keeping one's word) | truth | `诚信` | 91 | L35-50; most at L36 (56), L41 (62), L42 (61) |
| 2 | candid (being candid, upfront) | truth | `坦诚` | 1 | L38-40; most at L38 (1), L39 (1), L40 (1) |
| 2 | admit (admitting) | truth | `承认` | 2 | L37-45; most at L37 (1), L39 (1), L40 (2) |
| 2 | sincere (sincerity, earnestness) | truth | `␣earnest` | 29 | L48-53; most at L50 (15), L51 (21), L52 (20) |
| 2 | transparent (being transparent) | truth | `透明` | 3 | L35-39; most at L35 (1), L36 (1), L39 (1) |
| 2 | disclose (disclosing information) | truth | `信息披露` | 6 | L36-39; most at L36 (3), L37 (1), L38 (4) |

## q_tok4

| rep | family | side | members | visibility | layer profile |
|---|---|---|---|---|---|
| 1 | deceive (the act of deceiving) | lie | `欺骗` | 1 | L35-35; most at L35 (1) |
| 1 | fraud (defrauding, obtaining something by deceit) | lie | `欺诈` | 1 | L36-36; most at L36 (1) |
| 1 | conceal (hiding or covering up information) | lie | `隐瞒`, `掩饰`, `掩盖`, `瞒`, `隐藏` | 6 | L35-43; most at L35 (2), L36 (5), L37 (2) |
| 1 | mislead (misleading someone) | lie | `误导` | 1 | L44-44; most at L44 (1) |
| 1 | fabricate (making up content that is not real) | lie | `␣fabricated`, `␣fabrication`, `虚构`, `伪造` | 12 | L35-54; most at L36 (6), L37 (10), L38 (2) |
| 1 | groundless (out of thin air, without basis (凭空)) | lie | `凭空` | 2 | L35-36; most at L35 (1), L36 (2) |
| 1 | fake (fake, not genuine) | lie | `␣fake`, `fake`, `_fake` | 11 | L35-42; most at L35 (9), L36 (7), L37 (3) |
| 1 | pretend (pretending) | lie | `假装` | 1 | L42-42; most at L42 (1) |
| 1 | deny (denying (a claim or the truth)) | lie | `否认`, `否定`, `␣denial` | 69 | L35-56; most at L37 (42), L40 (44), L45 (35) |
| 1 | honest (honest, honesty) | truth | `诚实`, `␣honest`, `␣honesty` | 12 | L35-50; most at L36 (8), L42 (4), L43 (4) |
| 1 | integrity (integrity, trustworthiness (诚信)) | truth | `诚信` | 6 | L35-44; most at L35 (2), L36 (5), L37 (4) |
| 1 | candid (candid, upfront) | truth | `坦诚` | 2 | L35-42; most at L35 (1), L36 (2), L38 (2) |
| 1 | admit (admitting) | truth | `承认` | 3 | L43-47; most at L44 (3), L45 (3), L46 (2) |
| 1 | disclose (disclosing information) | truth | `披露`, `信息披露` | 2 | L36-38; most at L36 (1), L38 (1) |
| 1 | truth (the truth (noun)) | truth | `␣truth`, `␣Truth`, `实话` | 4 | L35-44; most at L37 (2), L38 (2), L39 (2) |
| 1 | sincere (sincere, genuine, in earnest) | truth | `␣genuine` | 1 | L36-37; most at L36 (1), L37 (1) |
| 1 | deliberate (on purpose, intentionally) | unclear | `故意`, `刻意` | 6 | L35-42; most at L35 (3), L36 (4), L38 (2) |
| 1 | knowingly (knowingly, with knowledge (明知)) | unclear | `明知` | 35 | L35-49; most at L35 (30), L36 (22), L37 (12) |
| 1 | contradict (contradicting, contradiction) | unclear | `␣contrad`, `␣contradictory`, `␣contradict` | 6 | L35-45; most at L35 (5), L37 (1), L38 (1) |
| 1 | refuse (refusing) | unclear | `␣refusal`, `拒绝` | 14 | L36-58; most at L36 (6), L39 (14), L40 (8) |
| 1 | perfunctory (brushing off, answering perfunctorily (敷衍)) | unclear | `敷衍` | 1 | L35-36; most at L35 (1), L36 (1) |
| 1 | inform (informing, telling someone (告知)) | unclear | `告知` | 1 | L38-38; most at L38 (1) |
| 1 | fact (fact, factual) | unclear | `␣factual` | 3 | L39-43; most at L39 (1), L41 (1), L43 (1) |
| 2 | deceive (the act of deceiving) | lie | `欺骗` | 1 | L35-35; most at L35 (1) |
| 2 | mislead (leading someone to a wrong belief) | lie | `误导` | 1 | L44-44; most at L44 (1) |
| 2 | fraud (fraud, cheating for gain) | lie | `欺诈` | 1 | L36-36; most at L36 (1) |
| 2 | betray (betraying, selling out) | lie | `出卖` | 3 | L35-36; most at L35 (3), L36 (1) |
| 2 | conceal (hiding or concealing information) | lie | `隐瞒`, `藏`, `瞒`, `隐藏` | 5 | L35-44; most at L35 (3), L36 (4), L37 (1) |
| 2 | cover up (covering up or masking the truth) | lie | `掩饰`, `掩盖` | 5 | L35-38; most at L35 (2), L36 (4), L37 (2) |
| 2 | fabricate (making up a story or facts) | lie | `␣fabricated`, `凭空`, `␣fabrication`, `虚构` | 11 | L35-54; most at L36 (7), L37 (10), L38 (2) |
| 2 | fake (faking or forging) | lie | `␣fake`, `fake`, `_fake`, `伪造` | 12 | L35-42; most at L35 (10), L36 (7), L37 (3) |
| 2 | pretend (pretending) | lie | `假装` | 1 | L42-42; most at L42 (1) |
| 2 | role-play (playing a role) | unclear | `扮演` | 6 | L35-45; most at L39 (3), L40 (2), L44 (2) |
| 2 | perfunctory (answering perfunctorily, brushing off) | unclear | `应付`, `敷衍` | 66 | L35-41; most at L35 (53), L37 (47), L39 (24) |
| 2 | deny (denying) | lie | `否认`, `␣denial` | 58 | L35-56; most at L37 (35), L40 (30), L45 (31) |
| 2 | negate (negating, repudiating) | unclear | `否定` | 30 | L35-49; most at L39 (19), L40 (23), L41 (18) |
| 2 | refuse (refusing) | unclear | `␣refusal`, `拒绝` | 14 | L36-58; most at L36 (6), L39 (14), L40 (8) |
| 2 | contradiction (contradicting, being inconsistent) | unclear | `␣contrad`, `␣contradictory`, `␣contradict` | 6 | L35-45; most at L35 (5), L37 (1), L38 (1) |
| 2 | deliberate (doing it on purpose) | unclear | `故意`, `刻意` | 6 | L35-42; most at L35 (3), L36 (4), L38 (2) |
| 2 | knowingly (doing it with knowledge of the facts) | unclear | `明知`, `知情` | 38 | L35-49; most at L35 (32), L36 (23), L37 (13) |
| 2 | honest (being honest) | truth | `诚实`, `␣honest`, `␣honesty` | 12 | L35-50; most at L36 (8), L42 (4), L43 (4) |
| 2 | integrity (integrity, keeping one's word) | truth | `诚信` | 6 | L35-44; most at L35 (2), L36 (5), L37 (4) |
| 2 | candid (being candid, upfront) | truth | `坦诚` | 2 | L35-42; most at L35 (1), L36 (2), L38 (2) |
| 2 | admit (admitting) | truth | `承认` | 3 | L43-47; most at L44 (3), L45 (3), L46 (2) |
| 2 | disclose (disclosing information) | truth | `披露`, `信息披露` | 2 | L36-38; most at L36 (1), L38 (1) |

## q_tok5

| rep | family | side | members | visibility | layer profile |
|---|---|---|---|---|---|
| 1 | fake (fake, not genuine) | lie | `fake` | 1 | L35-35; most at L35 (1) |
| 1 | disclose (disclosing information) | truth | `␣disclosures` | 1 | L53-53; most at L53 (1) |
| 1 | contradict (contradicting, contradiction) | unclear | `␣contradictory` | 2 | L35-47; most at L35 (1), L36 (1), L47 (1) |
| 2 | fake (faking or forging) | lie | `fake` | 1 | L35-35; most at L35 (1) |
| 2 | contradiction (contradicting, being inconsistent) | unclear | `␣contradictory` | 2 | L35-47; most at L35 (1), L36 (1), L47 (1) |
| 2 | disclose (disclosing information) | truth | `␣disclosures` | 1 | L53-53; most at L53 (1) |

## q_tok6

| rep | family | side | members | visibility | layer profile |
|---|---|---|---|---|---|
| 1 | deceive (the act of deceiving) | lie | `欺骗`, `骗`, `␣deception`, `␣deceive` | 82 | L35-58; most at L38 (50), L39 (64), L41 (43) |
| 1 | fraud (defrauding, obtaining something by deceit) | lie | `骗取` | 8 | L35-39; most at L35 (3), L36 (8), L37 (1) |
| 1 | conceal (hiding or covering up information) | lie | `隐瞒`, `掩饰`, `掩盖`, `瞒`, `遮掩`, `␣conceal`, `␣hiding`, `␣masking`, `␣hide`, `␣hides` | 160 | L35-58; most at L36 (143), L38 (138), L39 (134) |
| 1 | withhold (withholding information) | lie | `␣withholding`, `␣withhold` | 37 | L49-58; most at L51 (26), L52 (32), L53 (14) |
| 1 | omit (leaving information out) | lie | `␣omit`, `␣omission`, `省略`, `omit` | 27 | L39-58; most at L49 (15), L52 (16), L53 (24) |
| 1 | mislead (misleading someone) | lie | `误导`, `␣misleading` | 34 | L35-57; most at L36 (10), L37 (16), L38 (29) |
| 1 | fabricate (making up content that is not real) | lie | `␣fabricated`, `␣fabrication`, `虚构`, `␣invent`, `伪造`, `␣invented` | 113 | L35-57; most at L36 (69), L37 (98), L38 (41) |
| 1 | groundless (out of thin air, without basis (凭空)) | lie | `凭空` | 15 | L35-49; most at L36 (15), L37 (6), L39 (3) |
| 1 | fake (fake, not genuine) | lie | `fake`, `␣fake`, `_fake` | 40 | L35-44; most at L35 (24), L36 (31), L37 (16) |
| 1 | pretend (pretending) | lie | `␣pretending` | 1 | L49-55; most at L49 (1), L53 (1), L55 (1) |
| 1 | exaggerate (exaggerating) | lie | `夸大` | 9 | L36-44; most at L36 (3), L37 (5), L40 (5) |
| 1 | deny (denying (a claim or the truth)) | lie | `否认`, `␣denying`, `否定`, `␣denial`, `␣denies`, `␣deny`, `␣denied`, `deny`, `␣Denied` | 150 | L35-58; most at L39 (109), L40 (126), L41 (121) |
| 1 | honest (honest, honesty) | truth | `诚实`, `␣honest`, `␣honesty`, `诚` | 22 | L35-58; most at L38 (11), L39 (18), L40 (13) |
| 1 | integrity (integrity, trustworthiness (诚信)) | truth | `诚信` | 6 | L35-41; most at L38 (2), L40 (5), L41 (6) |
| 1 | candid (candid, upfront) | truth | `坦诚` | 2 | L38-40; most at L38 (1), L39 (1), L40 (1) |
| 1 | confess (confessing, owning up (坦白)) | truth | `坦白` | 1 | L40-41; most at L40 (1), L41 (1) |
| 1 | admit (admitting) | truth | `承认`, `␣admitting`, `␣admit` | 3 | L53-58; most at L55 (3), L56 (2), L57 (2) |
| 1 | disclose (disclosing information) | truth | `信息披露`, `␣disclosure`, `披露`, `␣disclose`, `␣disclosing` | 41 | L35-41; most at L35 (22), L36 (23), L38 (14) |
| 1 | truth (the truth (noun)) | truth | `␣truth`, `truth`, `真相`, `实情`, `Truth`, `␣Truth` | 159 | L35-58; most at L39 (109), L40 (124), L50 (127) |
| 1 | deliberate (on purpose, intentionally) | unclear | `故意`, `␣intentionally`, `␣deliberately`, `刻意`, `故意的`, `␣deliberate`, `␣intentional` | 192 | L35-58; most at L36 (122), L54 (154), L55 (132) |
| 1 | knowingly (knowingly, with knowledge (明知)) | unclear | `明知`, `␣knowingly` | 78 | L35-58; most at L44 (51), L47 (49), L50 (68) |
| 1 | contradict (contradicting, contradiction) | unclear | `␣contradict`, `␣contrad`, `矛盾`, `␣contradictory`, `␣contradiction`, `矛盾的` | 168 | L35-58; most at L38 (117), L44 (90), L49 (149) |
| 1 | inconsistent (inconsistent, conflicting) | unclear | `␣conflicting` | 6 | L36-45; most at L37 (4), L38 (3), L40 (3) |
| 1 | violate (violating a rule, duty or law) | unclear | `违背`, `违反`, `␣violate`, `违反了`, `违法` | 17 | L35-58; most at L37 (10), L56 (10), L57 (10) |
| 1 | suspected (suspected of wrongdoing (涉嫌)) | unclear | `涉嫌` | 3 | L48-48; most at L48 (3) |
| 1 | refuse (refusing) | unclear | `␣refusal`, `拒绝`, `␣refusing`, `␣refuse`, `␣refus`, `␣refuses`, `拒绝了` | 21 | L35-58; most at L39 (18), L40 (17), L57 (12) |
| 1 | evade (evading, avoiding the question) | unclear | `回避`, `␣evasion` | 9 | L36-58; most at L52 (4), L57 (7), L58 (8) |
| 1 | perfunctory (brushing off, answering perfunctorily (敷衍)) | unclear | `敷衍` | 20 | L35-52; most at L38 (2), L39 (2), L51 (20) |
| 1 | euphemistic (euphemistic, tactfully indirect (委婉)) | unclear | `委婉` | 18 | L35-48; most at L35 (18), L36 (3), L40 (4) |
| 1 | vague (vague, blurred (模糊)) | unclear | `模糊` | 1 | L56-56; most at L56 (1) |
| 1 | inform (informing, telling someone (告知)) | unclear | `告知` | 19 | L35-58; most at L54 (18), L57 (6), L58 (7) |
| 1 | objective (objective, impartial (客观)) | unclear | `客观` | 27 | L35-47; most at L35 (22), L36 (4), L44 (8) |
| 1 | fact (fact, factual) | unclear | `事实`, `␣factual`, `␣fact`, `␣facts`, `Fact`, `␣FACT`, `的事实`, `事实和` | 88 | L35-58; most at L39 (48), L40 (52), L48 (46) |
| 1 | ethics (ethics, morality) | unclear | `的道德` | 1 | L54-58; most at L54 (1), L55 (1), L58 (1) |
| 2 | deceive (the act of deceiving) | lie | `欺骗`, `骗`, `骗取`, `␣deception`, `␣deceive` | 86 | L35-58; most at L36 (44), L38 (50), L39 (64) |
| 2 | mislead (leading someone to a wrong belief) | lie | `误导`, `␣misleading` | 34 | L35-57; most at L36 (10), L37 (16), L38 (29) |
| 2 | betray (betraying, selling out) | lie | `出卖` | 1 | L35-35; most at L35 (1) |
| 2 | conceal (hiding or concealing information) | lie | `隐瞒`, `瞒`, `␣conceal`, `␣hiding`, `␣hide`, `␣hides` | 157 | L35-58; most at L36 (127), L38 (135), L39 (134) |
| 2 | cover up (covering up or masking the truth) | lie | `掩饰`, `掩盖`, `遮掩`, `遮`, `␣masking`, `掩护` | 117 | L35-58; most at L36 (116), L37 (83), L38 (82) |
| 2 | withhold (withholding information) | lie | `␣withholding`, `␣withhold` | 37 | L49-58; most at L51 (26), L52 (32), L53 (14) |
| 2 | omit (leaving information out) | lie | `␣omit`, `␣omission`, `省略`, `omit` | 27 | L39-58; most at L49 (15), L52 (16), L53 (24) |
| 2 | fabricate (making up a story or facts) | lie | `␣fabricated`, `␣fabrication`, `虚构`, `凭空`, `␣invent`, `␣invented` | 114 | L35-57; most at L36 (72), L37 (98), L38 (41) |
| 2 | fake (faking or forging) | lie | `fake`, `␣fake`, `伪造`, `forge`, `伪`, `_fake` | 49 | L35-52; most at L35 (24), L36 (33), L37 (16) |
| 2 | pretend (pretending) | lie | `␣pretending` | 1 | L49-55; most at L49 (1), L53 (1), L55 (1) |
| 2 | role-play (playing a role) | unclear | `扮演` | 3 | L48-53; most at L51 (2), L52 (2), L53 (3) |
| 2 | exaggerate (exaggerating) | lie | `夸大` | 9 | L36-44; most at L36 (3), L37 (5), L40 (5) |
| 2 | evade (evading or dodging the question) | lie | `回避`, `␣evasion`, `␣dodge` | 9 | L36-58; most at L52 (4), L57 (7), L58 (8) |
| 2 | perfunctory (answering perfunctorily, brushing off) | unclear | `应付`, `敷衍` | 76 | L35-52; most at L35 (33), L36 (41), L37 (43) |
| 2 | euphemistic (wording things euphemistically) | unclear | `委婉` | 18 | L35-48; most at L35 (18), L36 (3), L40 (4) |
| 2 | insinuate (hinting or implying) | unclear | `暗示` | 18 | L35-58; most at L48 (11), L49 (9), L54 (11) |
| 2 | vague (being vague) | unclear | `模糊` | 1 | L56-56; most at L56 (1) |
| 2 | deny (denying) | lie | `否认`, `␣denying`, `␣denial`, `␣denies`, `␣deny`, `␣denied`, `deny`, `␣Denied` | 143 | L35-58; most at L39 (104), L40 (117), L41 (114) |
| 2 | negate (negating, repudiating) | unclear | `否定` | 70 | L35-58; most at L35 (41), L40 (39), L41 (46) |
| 2 | refuse (refusing) | unclear | `␣refusal`, `拒绝`, `␣refusing`, `␣refuse`, `␣refus`, `␣refuses`, `拒绝了` | 21 | L35-58; most at L39 (18), L40 (17), L57 (12) |
| 2 | contradiction (contradicting, being inconsistent) | unclear | `␣contradict`, `␣contrad`, `矛盾`, `␣contradictory`, `␣contradiction`, `␣conflicting`, `矛盾的` | 168 | L35-58; most at L38 (117), L44 (90), L49 (149) |
| 2 | deliberate (doing it on purpose) | unclear | `故意`, `␣intentionally`, `␣deliberately`, `刻意`, `故意的`, `␣deliberate`, `有意`, `␣intentional` | 192 | L35-58; most at L36 (122), L54 (154), L55 (132) |
| 2 | knowingly (doing it with knowledge of the facts) | unclear | `明知`, `知情`, `␣knowingly` | 89 | L35-58; most at L44 (51), L47 (49), L50 (68) |
| 2 | accidental (doing it by accident) | unclear | `无意` | 3 | L35-49; most at L35 (1), L49 (2) |
| 2 | violate (violating a rule or principle) | lie | `违背`, `违反`, `违法`, `违反了` | 17 | L35-58; most at L37 (10), L56 (10), L57 (10) |
| 2 | ethics (ethics, morality) | unclear | `的道德` | 1 | L54-58; most at L54 (1), L55 (1), L58 (1) |
| 2 | accusation (being accused, a charge) | unclear | `涉嫌` | 3 | L48-48; most at L48 (3) |
| 2 | honest (being honest) | truth | `诚实`, `␣honest`, `␣honesty`, `诚` | 22 | L35-58; most at L38 (11), L39 (18), L40 (13) |
| 2 | integrity (integrity, keeping one's word) | truth | `诚信` | 6 | L35-41; most at L38 (2), L40 (5), L41 (6) |
| 2 | candid (being candid, upfront) | truth | `坦诚` | 2 | L38-40; most at L38 (1), L39 (1), L40 (1) |
| 2 | confess (confessing, owning up) | truth | `坦白` | 1 | L40-41; most at L40 (1), L41 (1) |
| 2 | admit (admitting) | truth | `承认`, `␣admitting`, `␣admit` | 3 | L53-58; most at L55 (3), L56 (2), L57 (2) |
| 2 | disclose (disclosing information) | truth | `信息披露`, `␣disclosure`, `披露`, `␣disclose`, `␣disclosing` | 41 | L35-41; most at L35 (22), L36 (23), L38 (14) |

## q_tok7

| rep | family | side | members | visibility | layer profile |
|---|---|---|---|---|---|
| 1 | deceive (the act of deceiving) | lie | `欺骗`, `␣deception` | 168 | L35-58; most at L35 (90), L55 (88), L57 (117) |
| 1 | conceal (hiding or covering up information) | lie | `隐瞒` | 2 | L39-40; most at L39 (2), L40 (1) |
| 1 | fake (fake, not genuine) | lie | `␣fake` | 4 | L35-41; most at L36 (3), L37 (3), L41 (2) |
| 1 | dishonest (dishonest) | lie | `␣dishonest` | 56 | L51-58; most at L56 (4), L57 (10), L58 (56) |
| 1 | deny (denying (a claim or the truth)) | lie | `否定` | 31 | L41-49; most at L44 (6), L48 (30), L49 (18) |
| 1 | honest (honest, honesty) | truth | `诚实`, `␣honesty`, `␣honest`, `诚`, `诚实守信`, `␣honestly` | 233 | L35-58; most at L49 (228), L50 (225), L51 (228) |
| 1 | integrity (integrity, trustworthiness (诚信)) | truth | `诚信` | 200 | L35-58; most at L35 (160), L40 (170), L41 (185) |
| 1 | candid (candid, upfront) | truth | `坦诚` | 19 | L36-58; most at L40 (3), L52 (3), L55 (18) |
| 1 | confess (confessing, owning up (坦白)) | truth | `坦白` | 4 | L37-55; most at L37 (3), L39 (2), L51 (1) |
| 1 | admit (admitting) | truth | `承认`, `␣admit` | 62 | L37-58; most at L39 (24), L40 (61), L41 (29) |
| 1 | transparent (transparent, transparency) | truth | `透明`, `␣transparency` | 5 | L35-48; most at L35 (5), L36 (4), L41 (2) |
| 1 | truth (the truth (noun)) | truth | `␣truth`, `truth`, `真相`, `真理`, `␣Truth`, `Truth`, `实话` | 233 | L35-58; most at L35 (207), L40 (231), L41 (221) |
| 1 | faithful (faithful, true to the facts (忠实)) | truth | `忠实` | 31 | L35-37; most at L35 (31), L36 (4), L37 (1) |
| 1 | deliberate (on purpose, intentionally) | unclear | `故意的`, `故意`, `␣intentionally`, `␣deliberate`, `␣intentional` | 64 | L35-54; most at L35 (36), L36 (56), L37 (53) |
| 1 | knowingly (knowingly, with knowledge (明知)) | unclear | `明知` | 67 | L35-57; most at L50 (55), L51 (24), L52 (46) |
| 1 | intention (intention (noun)) | unclear | `␣intentions`, `␣intention` | 104 | L35-41; most at L35 (86), L36 (82), L37 (68) |
| 1 | contradict (contradicting, contradiction) | unclear | `␣contradictory`, `矛盾`, `␣contrad`, `␣contradiction`, `␣contradict`, `␣contradictions` | 23 | L35-58; most at L36 (20), L37 (22), L38 (22) |
| 1 | inconsistent (inconsistent, conflicting) | unclear | `␣inconsistency`, `␣conflicting`, `不一致`, `␣inconsistent`, `␣inconsistencies` | 9 | L35-54; most at L37 (6), L41 (6), L52 (6) |
| 1 | violate (violating a rule, duty or law) | unclear | `违反`, `违反了` | 8 | L35-44; most at L35 (4), L36 (4), L40 (6) |
| 1 | accuse (accusation) | unclear | `␣accusations`, `␣accusation`, `␣accused`, `指控`, `␣accuse` | 80 | L35-57; most at L35 (14), L53 (75), L54 (37) |
| 1 | suspected (suspected of wrongdoing (涉嫌)) | unclear | `涉嫌` | 4 | L51-53; most at L51 (4), L53 (2) |
| 1 | fact (fact, factual) | unclear | `事实`, `␣fact` | 49 | L39-50; most at L40 (34), L41 (31), L49 (19) |
| 2 | deceive (the act of deceiving) | lie | `欺骗`, `␣deception`, `欺` | 168 | L35-58; most at L35 (90), L55 (88), L57 (117) |
| 2 | betray (betraying, selling out) | lie | `出卖` | 1 | L35-35; most at L35 (1) |
| 2 | conceal (hiding or concealing information) | lie | `隐瞒` | 2 | L39-40; most at L39 (2), L40 (1) |
| 2 | fake (faking or forging) | lie | `␣fake`, `伪` | 6 | L35-41; most at L36 (5), L37 (3), L41 (2) |
| 2 | negate (negating, repudiating) | unclear | `否定` | 31 | L41-49; most at L44 (6), L48 (30), L49 (18) |
| 2 | contradiction (contradicting, being inconsistent) | unclear | `␣contradictory`, `矛盾`, `␣contrad`, `␣contradiction`, `␣conflicting`, `␣inconsistency`, `␣contradict`, `不一致`, `␣inconsistent`, `␣inconsistencies`, `␣contradictions` | 24 | L35-58; most at L36 (20), L37 (22), L38 (22) |
| 2 | deliberate (doing it on purpose) | unclear | `故意的`, `故意`, `␣intentionally`, `␣deliberate`, `␣intentional` | 64 | L35-54; most at L35 (36), L36 (56), L37 (53) |
| 2 | knowingly (doing it with knowledge of the facts) | unclear | `知情`, `明知` | 112 | L35-57; most at L35 (80), L36 (71), L37 (57) |
| 2 | intention (the model's intention or motive) | unclear | `␣intentions`, `意图`, `␣intention` | 107 | L35-48; most at L35 (86), L36 (82), L37 (68) |
| 2 | violate (violating a rule or principle) | lie | `违反`, `违反了` | 8 | L35-44; most at L35 (4), L36 (4), L40 (6) |
| 2 | accusation (being accused, a charge) | unclear | `␣accusations`, `␣accusation`, `␣accused`, `指控`, `涉嫌`, `␣accuse` | 80 | L35-57; most at L35 (14), L53 (75), L54 (37) |
| 2 | honest (being honest) | truth | `诚实`, `␣honesty`, `␣honest`, `诚`, `诚实守信`, `␣honestly` | 233 | L35-58; most at L49 (228), L50 (225), L51 (228) |
| 2 | dishonest (being dishonest) | lie | `␣dishonest` | 56 | L51-58; most at L56 (4), L57 (10), L58 (56) |
| 2 | integrity (integrity, keeping one's word) | truth | `诚信` | 200 | L35-58; most at L35 (160), L40 (170), L41 (185) |
| 2 | candid (being candid, upfront) | truth | `坦诚` | 19 | L36-58; most at L40 (3), L52 (3), L55 (18) |
| 2 | confess (confessing, owning up) | truth | `坦白` | 4 | L37-55; most at L37 (3), L39 (2), L51 (1) |
| 2 | admit (admitting) | truth | `承认`, `␣admit` | 62 | L37-58; most at L39 (24), L40 (61), L41 (29) |
| 2 | faithful (faithful, true to the facts) | truth | `忠实` | 31 | L35-37; most at L35 (31), L36 (4), L37 (1) |
| 2 | transparent (being transparent) | truth | `透明`, `␣transparency` | 5 | L35-48; most at L35 (5), L36 (4), L41 (2) |

## Replicate overlap

For each replicate-1 family, the replicate-2 family at the same position sharing the most members.

| position | rep-1 family | best rep-2 family | Jaccard of member ids | only in rep 1 | only in rep 2 |
|---|---|---|---|---|---|
| q_tok0 | deny | deny | 1.00 | — | — |
| q_tok0 | admit | admit | 1.00 | — | — |
| q_tok0 | truth | — | 0 | all | — |
| q_tok0 | deliberate | deliberate | 1.00 | — | — |
| q_tok0 | knowingly | knowingly | 0.50 | — | `知情` |
| q_tok0 | misunderstand | — | 0 | all | — |
| q_tok0 | contradict | contradiction | 1.00 | — | — |
| q_tok0 | fact | — | 0 | all | — |
| q_tok1 | deceive | deceive | 0.75 | — | `欺` |
| q_tok1 | fraud | fraud | 1.00 | — | — |
| q_tok1 | conceal | conceal | 0.73 | `掩盖`, `掩饰`, `遮盖` | `藏` |
| q_tok1 | withhold | withhold | 1.00 | — | — |
| q_tok1 | omit | omit | 1.00 | — | — |
| q_tok1 | mislead | mislead | 1.00 | — | — |
| q_tok1 | fabricate | fabricate | 0.60 | `伪造` | `凭空` |
| q_tok1 | groundless | fabricate | 0.25 | — | `虚构`, `␣fabricated`, `␣invent` |
| q_tok1 | fake | fake | 0.75 | — | `伪造` |
| q_tok1 | exaggerate | exaggerate | 0.50 | — | `␣exagger` |
| q_tok1 | dishonest | dishonest | 1.00 | — | — |
| q_tok1 | deny | deny | 0.50 | `否定` | — |
| q_tok1 | secret | secret | 1.00 | — | — |
| q_tok1 | honest | honest | 1.00 | — | — |
| q_tok1 | integrity | integrity | 1.00 | — | — |
| q_tok1 | candid | candid | 1.00 | — | — |
| q_tok1 | confess | confess | 1.00 | — | — |
| q_tok1 | admit | admit | 1.00 | — | — |
| q_tok1 | disclose | disclose | 1.00 | — | — |
| q_tok1 | transparent | transparent | 1.00 | — | — |
| q_tok1 | truth | — | 0 | all | — |
| q_tok1 | sincere | — | 0 | all | — |
| q_tok1 | deliberate | deliberate | 0.78 | `特意` | `有意` |
| q_tok1 | knowingly | knowingly | 0.40 | — | `知情`, `␣knowing`, `␣Knowing` |
| q_tok1 | intention | intention | 1.00 | — | — |
| q_tok1 | accidental | accidental | 0.60 | — | `␣accident`, `意外` |
| q_tok1 | misunderstand | — | 0 | all | — |
| q_tok1 | contradict | contradiction | 1.00 | — | — |
| q_tok1 | violate | violate | 0.80 | `␣violate` | — |
| q_tok1 | refuse | refuse | 1.00 | — | — |
| q_tok1 | evade | evade | 1.00 | — | — |
| q_tok1 | perfunctory | perfunctory | 0.50 | — | `应付` |
| q_tok1 | euphemistic | euphemistic | 1.00 | — | — |
| q_tok1 | excuse | — | 0 | all | — |
| q_tok1 | inform | — | 0 | all | — |
| q_tok1 | objective | — | 0 | all | — |
| q_tok1 | fact | — | 0 | all | — |
| q_tok1 | ethics | ethics | 1.00 | — | — |
| q_tok1 | conscience | — | 0 | all | — |
| q_tok1 | apologize | apologize | 1.00 | — | — |
| q_tok1 | confidential | confidential | 1.00 | — | — |
| q_tok2 | deceive | deceive | 1.00 | — | — |
| q_tok2 | conceal | conceal | 0.60 | `掩盖`, `掩饰` | — |
| q_tok2 | omit | omit | 1.00 | — | — |
| q_tok2 | mislead | mislead | 1.00 | — | — |
| q_tok2 | fabricate | fabricate | 0.75 | — | `凭空` |
| q_tok2 | groundless | fabricate | 0.25 | — | `␣invent`, `虚构`, `␣invented` |
| q_tok2 | fake | fake | 1.00 | — | — |
| q_tok2 | honest | honest | 1.00 | — | — |
| q_tok2 | integrity | integrity | 1.00 | — | — |
| q_tok2 | candid | candid | 1.00 | — | — |
| q_tok2 | admit | admit | 1.00 | — | — |
| q_tok2 | truth | — | 0 | all | — |
| q_tok2 | deliberate | deliberate | 0.86 | — | `有意` |
| q_tok2 | knowingly | knowingly | 0.67 | — | `知情` |
| q_tok2 | intention | intention | 1.00 | — | — |
| q_tok2 | accuse | accusation | 1.00 | — | — |
| q_tok2 | inform | — | 0 | all | — |
| q_tok2 | fact | — | 0 | all | — |
| q_tok3 | deceive | deceive | 1.00 | — | — |
| q_tok3 | conceal | conceal | 0.80 | `掩盖`, `掩饰` | — |
| q_tok3 | disguise | cover up | 0.33 | — | `掩盖`, `掩饰` |
| q_tok3 | mislead | mislead | 1.00 | — | — |
| q_tok3 | fake | fake | 1.00 | — | — |
| q_tok3 | exaggerate | exaggerate | 1.00 | — | — |
| q_tok3 | deny | deny | 0.67 | `否定` | — |
| q_tok3 | honest | honest | 1.00 | — | — |
| q_tok3 | integrity | integrity | 1.00 | — | — |
| q_tok3 | candid | candid | 1.00 | — | — |
| q_tok3 | admit | admit | 1.00 | — | — |
| q_tok3 | disclose | disclose | 1.00 | — | — |
| q_tok3 | transparent | transparent | 1.00 | — | — |
| q_tok3 | truth | — | 0 | all | — |
| q_tok3 | sincere | sincere | 1.00 | — | — |
| q_tok3 | deliberate | deliberate | 1.00 | — | — |
| q_tok3 | knowingly | knowingly | 0.67 | — | `知情` |
| q_tok3 | contradict | contradiction | 1.00 | — | — |
| q_tok3 | violate | violate | 1.00 | — | — |
| q_tok3 | euphemistic | euphemistic | 1.00 | — | — |
| q_tok3 | inform | — | 0 | all | — |
| q_tok3 | fact | — | 0 | all | — |
| q_tok4 | deceive | deceive | 1.00 | — | — |
| q_tok4 | fraud | fraud | 1.00 | — | — |
| q_tok4 | conceal | conceal | 0.50 | `掩饰`, `掩盖` | `藏` |
| q_tok4 | mislead | mislead | 1.00 | — | — |
| q_tok4 | fabricate | fabricate | 0.60 | `伪造` | `凭空` |
| q_tok4 | groundless | fabricate | 0.25 | — | `␣fabricated`, `␣fabrication`, `虚构` |
| q_tok4 | fake | fake | 0.75 | — | `伪造` |
| q_tok4 | pretend | pretend | 1.00 | — | — |
| q_tok4 | deny | deny | 0.67 | `否定` | — |
| q_tok4 | honest | honest | 1.00 | — | — |
| q_tok4 | integrity | integrity | 1.00 | — | — |
| q_tok4 | candid | candid | 1.00 | — | — |
| q_tok4 | admit | admit | 1.00 | — | — |
| q_tok4 | disclose | disclose | 1.00 | — | — |
| q_tok4 | truth | — | 0 | all | — |
| q_tok4 | sincere | — | 0 | all | — |
| q_tok4 | deliberate | deliberate | 1.00 | — | — |
| q_tok4 | knowingly | knowingly | 0.50 | — | `知情` |
| q_tok4 | contradict | contradiction | 1.00 | — | — |
| q_tok4 | refuse | refuse | 1.00 | — | — |
| q_tok4 | perfunctory | perfunctory | 0.50 | — | `应付` |
| q_tok4 | inform | — | 0 | all | — |
| q_tok4 | fact | — | 0 | all | — |
| q_tok5 | fake | fake | 1.00 | — | — |
| q_tok5 | disclose | disclose | 1.00 | — | — |
| q_tok5 | contradict | contradiction | 1.00 | — | — |
| q_tok6 | deceive | deceive | 0.80 | — | `骗取` |
| q_tok6 | fraud | deceive | 0.20 | — | `欺骗`, `骗`, `␣deception`, `␣deceive` |
| q_tok6 | conceal | conceal | 0.60 | `掩饰`, `掩盖`, `遮掩`, `␣masking` | — |
| q_tok6 | withhold | withhold | 1.00 | — | — |
| q_tok6 | omit | omit | 1.00 | — | — |
| q_tok6 | mislead | mislead | 1.00 | — | — |
| q_tok6 | fabricate | fabricate | 0.71 | `伪造` | `凭空` |
| q_tok6 | groundless | fabricate | 0.17 | — | `␣fabricated`, `␣fabrication`, `虚构`, `␣invent`, `␣invented` |
| q_tok6 | fake | fake | 0.50 | — | `伪造`, `forge`, `伪` |
| q_tok6 | pretend | pretend | 1.00 | — | — |
| q_tok6 | exaggerate | exaggerate | 1.00 | — | — |
| q_tok6 | deny | deny | 0.89 | `否定` | — |
| q_tok6 | honest | honest | 1.00 | — | — |
| q_tok6 | integrity | integrity | 1.00 | — | — |
| q_tok6 | candid | candid | 1.00 | — | — |
| q_tok6 | confess | confess | 1.00 | — | — |
| q_tok6 | admit | admit | 1.00 | — | — |
| q_tok6 | disclose | disclose | 1.00 | — | — |
| q_tok6 | truth | — | 0 | all | — |
| q_tok6 | deliberate | deliberate | 0.88 | — | `有意` |
| q_tok6 | knowingly | knowingly | 0.67 | — | `知情` |
| q_tok6 | contradict | contradiction | 0.86 | — | `␣conflicting` |
| q_tok6 | inconsistent | contradiction | 0.14 | — | `␣contradict`, `␣contrad`, `矛盾`, `␣contradictory`, `␣contradiction`, `矛盾的` |
| q_tok6 | violate | violate | 0.80 | `␣violate` | — |
| q_tok6 | suspected | accusation | 1.00 | — | — |
| q_tok6 | refuse | refuse | 1.00 | — | — |
| q_tok6 | evade | evade | 0.67 | — | `␣dodge` |
| q_tok6 | perfunctory | perfunctory | 0.50 | — | `应付` |
| q_tok6 | euphemistic | euphemistic | 1.00 | — | — |
| q_tok6 | vague | vague | 1.00 | — | — |
| q_tok6 | inform | — | 0 | all | — |
| q_tok6 | objective | — | 0 | all | — |
| q_tok6 | fact | — | 0 | all | — |
| q_tok6 | ethics | ethics | 1.00 | — | — |
| q_tok7 | deceive | deceive | 0.67 | — | `欺` |
| q_tok7 | conceal | conceal | 1.00 | — | — |
| q_tok7 | fake | fake | 0.50 | — | `伪` |
| q_tok7 | dishonest | dishonest | 1.00 | — | — |
| q_tok7 | deny | negate | 1.00 | — | — |
| q_tok7 | honest | honest | 1.00 | — | — |
| q_tok7 | integrity | integrity | 1.00 | — | — |
| q_tok7 | candid | candid | 1.00 | — | — |
| q_tok7 | confess | confess | 1.00 | — | — |
| q_tok7 | admit | admit | 1.00 | — | — |
| q_tok7 | transparent | transparent | 1.00 | — | — |
| q_tok7 | truth | — | 0 | all | — |
| q_tok7 | faithful | faithful | 1.00 | — | — |
| q_tok7 | deliberate | deliberate | 1.00 | — | — |
| q_tok7 | knowingly | knowingly | 0.50 | — | `知情` |
| q_tok7 | intention | intention | 0.67 | — | `意图` |
| q_tok7 | contradict | contradiction | 0.55 | — | `␣conflicting`, `␣inconsistency`, `不一致`, `␣inconsistent`, `␣inconsistencies` |
| q_tok7 | inconsistent | contradiction | 0.45 | — | `␣contradictory`, `矛盾`, `␣contrad`, `␣contradiction`, `␣contradict`, `␣contradictions` |
| q_tok7 | violate | violate | 1.00 | — | — |
| q_tok7 | accuse | accusation | 0.83 | — | `涉嫌` |
| q_tok7 | suspected | accusation | 0.17 | — | `␣accusations`, `␣accusation`, `␣accused`, `指控`, `␣accuse` |
| q_tok7 | fact | — | 0 | all | — |

Replicate-2 families not the best match of any replicate-1 family: q_tok1: betray, q_tok1: cover up, q_tok1: role-play, q_tok1: insinuate, q_tok1: negate, q_tok1: consistent, q_tok2: betray, q_tok2: cover up, q_tok3: betray, q_tok3: role-play, q_tok3: perfunctory, q_tok3: negate, q_tok4: betray, q_tok4: cover up, q_tok4: role-play, q_tok4: negate, q_tok6: betray, q_tok6: cover up, q_tok6: role-play, q_tok6: insinuate, q_tok6: negate, q_tok6: accidental, q_tok7: betray

## Families whose name recurs at 3 or more positions

- accusation: q_tok2, q_tok6, q_tok7
- admit: q_tok0, q_tok1, q_tok2, q_tok3, q_tok4, q_tok6, q_tok7
- betray: q_tok1, q_tok2, q_tok3, q_tok4, q_tok6, q_tok7
- candid: q_tok1, q_tok2, q_tok3, q_tok4, q_tok6, q_tok7
- conceal: q_tok1, q_tok2, q_tok3, q_tok4, q_tok6, q_tok7
- confess: q_tok1, q_tok6, q_tok7
- contradict: q_tok0, q_tok1, q_tok3, q_tok4, q_tok5, q_tok6, q_tok7
- contradiction: q_tok0, q_tok1, q_tok3, q_tok4, q_tok5, q_tok6, q_tok7
- cover up: q_tok1, q_tok2, q_tok3, q_tok4, q_tok6
- deceive: q_tok1, q_tok2, q_tok3, q_tok4, q_tok6, q_tok7
- deliberate: q_tok0, q_tok1, q_tok2, q_tok3, q_tok4, q_tok6, q_tok7
- deny: q_tok0, q_tok1, q_tok3, q_tok4, q_tok6, q_tok7
- disclose: q_tok1, q_tok3, q_tok4, q_tok5, q_tok6
- euphemistic: q_tok1, q_tok3, q_tok6
- exaggerate: q_tok1, q_tok3, q_tok6
- fabricate: q_tok1, q_tok2, q_tok4, q_tok6
- fact: q_tok0, q_tok1, q_tok2, q_tok3, q_tok4, q_tok6, q_tok7
- fake: q_tok1, q_tok2, q_tok3, q_tok4, q_tok5, q_tok6, q_tok7
- fraud: q_tok1, q_tok4, q_tok6
- groundless: q_tok1, q_tok2, q_tok4, q_tok6
- honest: q_tok1, q_tok2, q_tok3, q_tok4, q_tok6, q_tok7
- inform: q_tok1, q_tok2, q_tok3, q_tok4, q_tok6
- integrity: q_tok1, q_tok2, q_tok3, q_tok4, q_tok6, q_tok7
- intention: q_tok1, q_tok2, q_tok7
- knowingly: q_tok0, q_tok1, q_tok2, q_tok3, q_tok4, q_tok6, q_tok7
- mislead: q_tok1, q_tok2, q_tok3, q_tok4, q_tok6
- negate: q_tok1, q_tok3, q_tok4, q_tok6, q_tok7
- omit: q_tok1, q_tok2, q_tok6
- perfunctory: q_tok1, q_tok3, q_tok4, q_tok6
- refuse: q_tok1, q_tok4, q_tok6
- role-play: q_tok1, q_tok3, q_tok4, q_tok6
- sincere: q_tok1, q_tok3, q_tok4
- transparent: q_tok1, q_tok3, q_tok7
- truth: q_tok0, q_tok1, q_tok2, q_tok3, q_tok4, q_tok6, q_tok7
- violate: q_tok1, q_tok3, q_tok6, q_tok7

## Candidate opposite pairs (same position, lie side vs truth side, antonym words in the names or glosses; merged list)

- q_tok0: deny / admit
- q_tok1: conceal / disclose
- q_tok1: conceal / transparent
- q_tok1: cover up / transparent
- q_tok1: deceive / honest
- q_tok1: deny / admit
- q_tok1: deny / confess
- q_tok1: dishonest / honest
- q_tok1: fake / sincere
- q_tok1: mislead / candid
- q_tok2: deceive / honest
- q_tok2: mislead / candid
- q_tok3: conceal / disclose
- q_tok3: conceal / transparent
- q_tok3: cover up / transparent
- q_tok3: deceive / honest
- q_tok3: deny / admit
- q_tok3: fake / sincere
- q_tok3: mislead / candid
- q_tok4: conceal / disclose
- q_tok4: deceive / honest
- q_tok4: deny / admit
- q_tok4: fake / sincere
- q_tok4: mislead / candid
- q_tok4: pretend / sincere
- q_tok6: conceal / disclose
- q_tok6: deceive / honest
- q_tok6: deny / admit
- q_tok6: deny / confess
- q_tok6: mislead / candid
- q_tok7: conceal / transparent
- q_tok7: deceive / honest
- q_tok7: deny / admit
- q_tok7: deny / confess
- q_tok7: dishonest / honest

Merged candidate list: `qwen3_6_27b_LL_Q7_ab_questiona_merged.json` (196 families; replicate-2 families sharing at least half
their members with a replicate-1 family at the same position are folded into it).
