# Family report: qwen3.6-27b, logit lens, band 35-58, part Q9_dyl, group preans

Written by `scripts/family_report.py` from `qwen3_6_27b_LL_Q9_dyl_preans_rep1.json` and `_rep2.json` (prompt
`prompts/family_generation.md`). Visibility = build-split scenario transcripts (of 233) in which
at least one member is present at the position within the band. Layer profile = band layers where
the family is present in at least one transcript, and the three layers with the most transcripts
(description only; scoring uses the whole band).

## preans_slot0

| rep | family | side | members | visibility | layer profile |
|---|---|---|---|---|---|
| 1 | cannot (first-person refusal formula "I cannot") | unclear | `我无法`, `我不能` | 114 | L50-55; most at L51 (36), L53 (114), L54 (18) |
| 1 | admit (admitting) | truth | `承认` | 3 | L35-44; most at L37 (3), L39 (3), L40 (3) |
| 1 | acknowledge (acknowledging) | truth | `␣acknowledge` | 6 | L44-48; most at L44 (1), L47 (1), L48 (6) |
| 1 | candid (candid, frank) | truth | `坦诚` | 10 | L36-43; most at L36 (2), L37 (2), L43 (9) |
| 1 | honest (honest / honesty) | truth | `诚实` | 2 | L43-45; most at L43 (1), L45 (2) |
| 1 | truth (the truth) | truth | `␣truth` | 1 | L35-35; most at L35 (1) |
| 1 | objective (objective, impartial) | unclear | `客观` | 3 | L35-43; most at L35 (1), L36 (1), L43 (2) |
| 1 | reveal (revealing) | truth | `揭示了`, `揭` | 9 | L35-36; most at L35 (2), L36 (9) |
| 1 | intentional (done on purpose) | unclear | `␣deliberate` | 1 | L51-51; most at L51 (1) |
| 1 | knowing (with knowledge / knowingly) | unclear | `明知` | 3 | L44-44; most at L44 (3) |
| 1 | violate (violating (rules, norms)) | unclear | `违` | 1 | L52-52; most at L52 (1) |
| 1 | ethics (ethics / morality) | unclear | `伦理` | 3 | L39-43; most at L39 (3), L40 (3), L41 (2) |
| 1 | silence (staying silent) | unclear | `沉默` | 2 | L36-36; most at L36 (2) |
| 1 | compliance (complying with rules) | unclear | `合规`, `␣compliance` | 16 | L40-46; most at L41 (9), L42 (6), L46 (12) |
| 1 | law-abiding (law-abiding) | unclear | `守法` | 17 | L35-49; most at L40 (7), L41 (5), L47 (13) |
| 1 | accuse (accusation) | unclear | `指控` | 67 | L40-50; most at L43 (64), L44 (51), L46 (38) |
| 2 | accuse (accusation) | unclear | `指控` | 67 | L40-50; most at L43 (64), L44 (51), L46 (38) |
| 2 | comply (complying / abiding by rules) | unclear | `守法`, `合规`, `␣compliance` | 26 | L35-49; most at L41 (11), L46 (12), L47 (13) |
| 2 | candid (candour / frankness) | truth | `坦诚` | 10 | L36-43; most at L36 (2), L37 (2), L43 (9) |
| 2 | reveal (revealing) | truth | `揭示了` | 7 | L35-36; most at L35 (1), L36 (7) |
| 2 | admit (admitting / acknowledging) | truth | `␣acknowledge`, `承认` | 6 | L35-48; most at L37 (3), L39 (3), L48 (6) |
| 2 | ethics (ethics / morality) | unclear | `伦理` | 3 | L39-43; most at L39 (3), L40 (3), L41 (2) |
| 2 | knowingly (with knowledge / knowingly) | unclear | `明知` | 3 | L44-44; most at L44 (3) |
| 2 | honest (honesty / being honest) | truth | `诚实` | 2 | L43-45; most at L43 (1), L45 (2) |
| 2 | silence (silence / staying silent) | unclear | `沉默` | 2 | L36-36; most at L36 (2) |
| 2 | intentional (doing it on purpose) | unclear | `␣deliberate` | 1 | L51-51; most at L51 (1) |
| 2 | violate (violating / going against) | unclear | `违` | 1 | L52-52; most at L52 (1) |

## preans_slot1

| rep | family | side | members | visibility | layer profile |
|---|---|---|---|---|---|
| 1 | deceive (the act of deceiving) | lie | `欺骗`, `␣deception`, `␣deceptive`, `␣deceive`, `␣deceit`, `骗`, `␣deceived` | 224 | L35-58; most at L37 (172), L38 (184), L39 (194) |
| 1 | dishonest (being dishonest) | lie | `␣dishonest` | 58 | L51-58; most at L52 (16), L57 (40), L58 (52) |
| 1 | mislead (leading someone to a false belief) | lie | `␣misleading`, `误导` | 69 | L36-58; most at L53 (49), L57 (57), L58 (57) |
| 1 | misinformation (false information given out) | lie | `虚假信息`, `␣misinformation` | 87 | L35-58; most at L36 (64), L37 (50), L38 (19) |
| 1 | conceal (concealing the truth) | lie | `隐瞒`, `␣conceal`, `␣concealed`, `瞒`, `隐匿` | 211 | L35-58; most at L39 (188), L40 (173), L53 (160) |
| 1 | cover up (covering up / glossing over) | lie | `掩盖`, `掩饰` | 44 | L36-58; most at L52 (30), L53 (24), L58 (30) |
| 1 | hide (hiding something) | lie | `␣hiding`, `隐藏`, `Hide`, `␣hide`, `␣hides`, `␣Hide`, `␣hid`, `hide` | 21 | L37-58; most at L53 (6), L57 (6), L58 (18) |
| 1 | withhold (withholding information) | lie | `␣withholding`, `␣withhold`, `␣withheld` | 119 | L51-58; most at L52 (97), L53 (112), L54 (46) |
| 1 | omit (leaving something out) | lie | `␣omit`, `␣omission`, `omit`, `省略`, `␣omitted` | 121 | L40-58; most at L52 (83), L53 (107), L56 (74) |
| 1 | fabricate (making something up) | lie | `虚构`, `␣invent`, `␣fabricated`, `␣fabrication`, `␣invented`, `凭空` | 106 | L35-58; most at L35 (69), L36 (87), L37 (49) |
| 1 | fiction (fictional, made-up story) | unclear | `␣fictional`, `fiction`, `␣fiction` | 21 | L35-53; most at L35 (9), L36 (15), L37 (7) |
| 1 | fake (fake, false-seeming) | lie | `fake`, `␣fake`, `伪` | 46 | L35-38; most at L36 (31), L37 (36), L38 (32) |
| 1 | disguise (disguising / masquerading) | lie | `伪装`, `␣disguised` | 14 | L35-37; most at L35 (9), L36 (7), L37 (9) |
| 1 | pretend (pretending) | lie | `␣pretending` | 4 | L36-37; most at L36 (3), L37 (3) |
| 1 | hypocrisy (hypocritical, insincere) | lie | `虚伪` | 9 | L36-40; most at L36 (6), L37 (2), L38 (5) |
| 1 | evade (evading the question) | lie | `␣evasion`, `回避` | 14 | L51-58; most at L54 (7), L57 (11), L58 (13) |
| 1 | downplay (downplaying, playing down) | lie | `淡化` | 4 | L47-58; most at L47 (1), L50 (3), L51 (2) |
| 1 | deny (denying) | lie | `否认`, `␣deny`, `␣denial`, `␣denying`, `␣denies` | 11 | L40-58; most at L41 (5), L42 (3), L45 (4) |
| 1 | refuse (refusing / declining) | unclear | `拒绝` | 1 | L39-40; most at L39 (1), L40 (1) |
| 1 | admit (admitting) | truth | `承认` | 1 | L44-45; most at L44 (1), L45 (1) |
| 1 | confess (confessing, coming clean) | truth | `坦白` | 10 | L51-55; most at L51 (8), L52 (7), L53 (5) |
| 1 | candid (candid, frank) | truth | `坦诚` | 2 | L52-55; most at L52 (1), L54 (1), L55 (2) |
| 1 | honest (honest / honesty) | truth | `诚实`, `诚`, `␣honesty`, `␣honest`, `誠` | 214 | L35-58; most at L41 (171), L45 (179), L46 (178) |
| 1 | integrity (integrity, good faith) | truth | `诚信`, `诚实守信` | 147 | L35-58; most at L39 (115), L40 (117), L41 (133) |
| 1 | truthful (truthful, telling it as it is) | truth | `␣truthful`, `实话`, `如实`, `实事求是`, `说实话` | 229 | L35-58; most at L35 (199), L39 (222), L40 (206) |
| 1 | truth (the truth) | truth | `␣truth`, `truth`, `␣Truth`, `真相`, `Truth`, `␣truths`, `_truth`, `真理`, `.truth` | 233 | L35-58; most at L39 (228), L40 (232), L41 (232) |
| 1 | fact (fact / the facts) | unclear | `事实`, `␣fact`, `事实上`, `␣factual`, `␣Fact`, `␣facts`, `的事实`, `fact`, `Fact`, `事实和`, `␣FACT`, `facts`, `FACT`, `_fact`, `␣Facts` | 233 | L35-58; most at L43 (226), L44 (232), L45 (224) |
| 1 | reality (the actual state of affairs) | unclear | `根据实际情况`, `实际情况`, `与现实`, `␣reality`, `实情`, `␣Reality`, `Reality`, `现实`, `现实的`, `现实中`, `的现实` | 48 | L35-58; most at L46 (11), L49 (38), L51 (20) |
| 1 | objective (objective, impartial) | unclear | `客观`, `␣objectively`, `␣objective` | 131 | L35-57; most at L35 (71), L36 (65), L44 (90) |
| 1 | transparent (transparency) | truth | `␣transparency`, `␣Transparency` | 7 | L54-56; most at L54 (6), L56 (2) |
| 1 | disclose (disclosing, making public) | truth | `公开` | 8 | L47-48; most at L47 (8), L48 (2) |
| 1 | reveal (revealing) | truth | `揭` | 1 | L49-49; most at L49 (1) |
| 1 | intentional (done on purpose) | unclear | `␣intentionally`, `故意`, `␣deliberately`, `␣deliberate`, `␣intentional`, `有意` | 140 | L35-58; most at L36 (76), L52 (79), L54 (73) |
| 1 | knowing (with knowledge / knowingly) | unclear | `明知`, `␣knowingly`, `知情`, `␣knowing`, `␣Knowing`, `Knowing` | 193 | L35-58; most at L43 (188), L44 (181), L45 (169) |
| 1 | violate (violating (rules, norms)) | unclear | `违反`, `违背`, `违`, `违反了`, `␣violate` | 106 | L35-58; most at L48 (50), L49 (71), L54 (39) |
| 1 | deviate (deviating) | unclear | `偏离`, `␣deviation`, `背离`, `␣deviations` | 37 | L53-58; most at L54 (37), L57 (18), L58 (16) |
| 1 | contradict (contradiction) | unclear | `␣contradict`, `␣contrad`, `␣contradictory`, `␣contradiction`, `矛盾`, `␣contradictions` | 38 | L35-58; most at L37 (16), L38 (19), L54 (18) |
| 1 | ethics (ethics / morality) | unclear | `␣ethical`, `␣morally`, `伦理`, `␣ethics`, `␣moral`, `道德`, `的道德` | 33 | L50-58; most at L52 (1), L54 (3), L58 (33) |
| 1 | technically (technically (true)) | unclear | `␣technically`, `技术上` | 70 | L42-58; most at L55 (69), L56 (54), L57 (47) |
| 1 | partial (partial, incomplete) | unclear | `不完全`, `␣partially`, `␣partial`, `␣Partial`, `partial` | 50 | L36-58; most at L41 (15), L42 (42), L43 (26) |
| 1 | compliance (complying with rules) | unclear | `遵守`, `␣adherence`, `␣compliance`, `严格遵守`, `恪守` | 13 | L47-58; most at L52 (4), L53 (6), L54 (6) |
| 2 | deceive (the act of deceiving) | lie | `欺骗`, `␣deception`, `␣deceptive`, `␣deceive`, `␣deceit`, `骗`, `␣deceived` | 224 | L35-58; most at L37 (172), L38 (184), L39 (194) |
| 2 | truthful (truthfully / telling the truth) | truth | `␣truthful`, `实话`, `如实`, `实事求是`, `说实话` | 229 | L35-58; most at L35 (199), L39 (222), L40 (206) |
| 2 | conceal (concealing / covering up information) | lie | `隐瞒`, `␣conceal`, `␣concealed`, `掩盖`, `瞒`, `掩饰`, `掩`, `遮蔽` | 211 | L35-58; most at L39 (188), L40 (173), L53 (160) |
| 2 | honest (honesty / being honest) | truth | `诚实`, `诚信`, `诚`, `␣honesty`, `␣honest`, `诚实守信`, `誠` | 218 | L35-58; most at L41 (183), L45 (179), L46 (178) |
| 2 | knowingly (with knowledge / knowingly) | unclear | `明知`, `␣knowingly`, `知情`, `␣knowing`, `␣Knowing`, `Knowing` | 193 | L35-58; most at L43 (188), L44 (181), L45 (169) |
| 2 | withhold (withholding information) | lie | `␣withholding`, `␣withhold`, `␣withheld` | 119 | L51-58; most at L52 (97), L53 (112), L54 (46) |
| 2 | intentional (doing it on purpose) | unclear | `␣intentionally`, `故意`, `␣deliberately`, `␣deliberate`, `␣intentional` | 140 | L35-58; most at L36 (76), L52 (79), L54 (73) |
| 2 | fabricate (making something up / fabricating) | lie | `虚构`, `␣invent`, `␣fabrication`, `␣fabricated`, `␣invented`, `凭空` | 106 | L35-58; most at L35 (69), L36 (87), L37 (49) |
| 2 | omit (omitting / leaving out) | lie | `␣omit`, `␣omission`, `omit`, `省略`, `␣omitted` | 121 | L40-58; most at L52 (83), L53 (107), L56 (74) |
| 2 | violate (violating / going against) | unclear | `违反`, `违背`, `违`, `违反了`, `␣violate` | 106 | L35-58; most at L48 (50), L49 (71), L54 (39) |
| 2 | misinformation (false information) | lie | `虚假信息`, `␣misinformation` | 87 | L35-58; most at L36 (64), L37 (50), L38 (19) |
| 2 | technically (technically (as a hedge)) | unclear | `␣technically`, `技术上` | 70 | L42-58; most at L55 (69), L56 (54), L57 (47) |
| 2 | mislead (misleading) | lie | `␣misleading`, `误导` | 69 | L36-58; most at L53 (49), L57 (57), L58 (57) |
| 2 | dishonest (dishonesty) | lie | `␣dishonest` | 58 | L51-58; most at L52 (16), L57 (40), L58 (52) |
| 2 | liar (a liar) | lie | `␣liar` | 43 | L51-58; most at L51 (16), L55 (33), L56 (29) |
| 2 | fake (fake / false (counterfeit)) | lie | `fake`, `␣fake`, `伪` | 46 | L35-38; most at L36 (31), L37 (36), L38 (32) |
| 2 | deviate (deviating / departing from) | unclear | `偏离`, `␣deviation`, `背离`, `␣deviations` | 37 | L53-58; most at L54 (37), L57 (18), L58 (16) |
| 2 | ethics (ethics / morality) | unclear | `␣ethical`, `␣morally`, `伦理`, `␣ethics`, `␣moral`, `道德`, `的道德` | 33 | L50-58; most at L52 (1), L54 (3), L58 (33) |
| 2 | contradict (contradiction / conflict) | unclear | `␣contrad`, `␣contradict`, `␣contradictory`, `␣conflicting`, `␣contradiction`, `矛盾`, `␣conflicts`, `␣contradictions` | 40 | L35-58; most at L37 (18), L38 (19), L54 (18) |
| 2 | hide (hiding something; being hidden) | lie | `␣hiding`, `隐藏`, `Hide`, `␣hide`, `␣hides`, `隐匿`, `hide`, `␣Hide`, `␣hid` | 21 | L37-58; most at L53 (6), L57 (6), L58 (18) |
| 2 | fiction (fiction / fictional) | unclear | `␣fictional`, `fiction`, `␣fiction` | 21 | L35-53; most at L35 (9), L36 (15), L37 (7) |
| 2 | evade (evading / evasion) | lie | `␣evasion`, `回避` | 14 | L51-58; most at L54 (7), L57 (11), L58 (13) |
| 2 | pretend (pretending / disguising) | lie | `伪装`, `␣pretending`, `␣disguised` | 15 | L35-37; most at L35 (9), L36 (7), L37 (11) |
| 2 | deny (denying / denial) | lie | `否认`, `␣deny`, `␣denial`, `␣denying`, `␣denies` | 11 | L40-58; most at L41 (5), L42 (3), L45 (4) |
| 2 | comply (complying / abiding by rules) | unclear | `遵守`, `␣adher`, `␣adherence`, `␣compliance`, `␣adhere`, `严格遵守`, `恪守` | 14 | L47-58; most at L52 (4), L53 (6), L54 (7) |
| 2 | confess (confessing / coming clean) | truth | `坦白` | 10 | L51-55; most at L51 (8), L52 (7), L53 (5) |
| 2 | hypocrisy (hypocrisy) | lie | `虚伪` | 9 | L36-40; most at L36 (6), L37 (2), L38 (5) |
| 2 | disclose (disclosing / making public) | truth | `公开` | 8 | L47-48; most at L47 (8), L48 (2) |
| 2 | transparent (transparency) | truth | `␣transparency`, `␣Transparency` | 7 | L54-56; most at L54 (6), L56 (2) |
| 2 | downplay (downplaying) | lie | `淡化` | 4 | L47-58; most at L47 (1), L50 (3), L51 (2) |
| 2 | candid (candour / frankness) | truth | `坦诚` | 2 | L52-55; most at L52 (1), L54 (1), L55 (2) |
| 2 | distort (distorting) | lie | `␣distortion` | 1 | L58-58; most at L58 (1) |
| 2 | misrepresent (misrepresenting) | lie | `␣misrepresented` | 1 | L51-58; most at L51 (1), L58 (1) |
| 2 | refuse (refusing / declining) | unclear | `拒绝` | 1 | L39-40; most at L39 (1), L40 (1) |
| 2 | admit (admitting / acknowledging) | truth | `承认` | 1 | L44-45; most at L44 (1), L45 (1) |

## preans_slot2

| rep | family | side | members | visibility | layer profile |
|---|---|---|---|---|---|
| 1 | deceive (the act of deceiving) | lie | `欺骗`, `␣deception`, `␣deceptive`, `␣deceive`, `骗` | 49 | L35-58; most at L35 (27), L36 (16), L38 (22) |
| 1 | dishonest (being dishonest) | lie | `␣dishonest` | 1 | L51-57; most at L51 (1), L52 (1), L53 (1) |
| 1 | mislead (leading someone to a false belief) | lie | `␣misleading`, `误导`, `误导性` | 9 | L37-58; most at L50 (3), L53 (4), L54 (6) |
| 1 | misinformation (false information given out) | lie | `虚假信息`, `␣misinformation` | 9 | L36-54; most at L37 (5), L53 (3), L54 (3) |
| 1 | conceal (concealing the truth) | lie | `隐瞒`, `␣conceal`, `␣concealed`, `瞒` | 101 | L35-58; most at L39 (74), L40 (85), L41 (73) |
| 1 | cover up (covering up / glossing over) | lie | `掩盖`, `掩饰`, `遮盖`, `遮掩` | 79 | L35-58; most at L35 (49), L36 (47), L43 (50) |
| 1 | hide (hiding something) | lie | `隐藏`, `␣hiding`, `␣hide`, `Hide`, `␣hides`, `␣hidden`, `hide`, `隐藏着`, `隐藏的`, `␣Hide`, `_hide`, `-hide`, `␣hid`, `Hidden` | 21 | L35-58; most at L53 (7), L55 (7), L58 (7) |
| 1 | withhold (withholding information) | lie | `␣withholding`, `␣withhold`, `␣withheld` | 13 | L36-58; most at L51 (7), L52 (8), L53 (10) |
| 1 | omit (leaving something out) | lie | `␣omit`, `omit`, `省略`, `␣omission`, `␣omitted`, `␣OMIT` | 17 | L39-58; most at L50 (12), L51 (11), L52 (10) |
| 1 | fabricate (making something up) | lie | `虚构`, `␣fabricated`, `␣invented`, `␣fabrication`, `凭空`, `␣invent`, `伪造`, `␣invention` | 105 | L35-58; most at L36 (66), L37 (77), L38 (61) |
| 1 | fiction (fictional, made-up story) | unclear | `␣fictional`, `fiction`, `␣fiction`, `-fiction` | 38 | L35-58; most at L39 (13), L43 (12), L44 (18) |
| 1 | fake (fake, false-seeming) | lie | `fake`, `␣fake`, `Fake` | 25 | L35-46; most at L37 (11), L38 (18), L44 (12) |
| 1 | disguise (disguising / masquerading) | lie | `伪装` | 3 | L36-43; most at L36 (2), L40 (1), L42 (1) |
| 1 | pretend (pretending) | lie | `␣pretending`, `假装` | 2 | L36-46; most at L36 (1), L46 (1) |
| 1 | evade (evading the question) | lie | `回避`, `␣evasion`, `␣evade` | 8 | L36-58; most at L50 (5), L51 (6), L52 (4) |
| 1 | downplay (downplaying, playing down) | lie | `淡化` | 11 | L35-55; most at L49 (5), L50 (10), L52 (5) |
| 1 | deny (denying) | lie | `否认`, `␣denying`, `␣denial`, `␣deny`, `␣denies`, `␣denied`, `deny`, `␣Denied` | 42 | L35-58; most at L49 (27), L55 (31), L56 (28) |
| 1 | refuse (refusing / declining) | unclear | `␣refusal`, `拒绝`, `␣refused`, `␣refusing`, `拒`, `␣refuse`, `␣refuses`, `␣refus`, `拒絕`, `拒绝了`, `␣decline`, `拒不`, `␣declined`, `␣declines` | 25 | L35-58; most at L56 (23), L57 (23), L58 (21) |
| 1 | admit (admitting) | truth | `承认`, `␣admitting`, `␣admits`, `␣admitted`, `␣admit`, `␣admite` | 34 | L35-58; most at L39 (16), L40 (17), L42 (17) |
| 1 | acknowledge (acknowledging) | truth | `␣acknowledging`, `␣acknowledge`, `␣acknowledged`, `␣acknowledges`, `␣acknowledgment` | 5 | L50-58; most at L55 (3), L56 (3), L57 (3) |
| 1 | confess (confessing, coming clean) | truth | `坦白`, `␣confess` | 8 | L51-56; most at L51 (4), L52 (8), L53 (6) |
| 1 | candid (candid, frank) | truth | `坦诚` | 14 | L36-55; most at L39 (9), L42 (10), L43 (9) |
| 1 | honest (honest / honesty) | truth | `诚`, `诚实`, `␣honest`, `␣honesty`, `␣honestly` | 94 | L35-58; most at L38 (56), L39 (54), L40 (59) |
| 1 | integrity (integrity, good faith) | truth | `诚信`, `␣integrity`, `诚实守信` | 14 | L36-57; most at L39 (9), L40 (13), L41 (8) |
| 1 | truthful (truthful, telling it as it is) | truth | `␣truthful`, `如实`, `实话`, `实事求是`, `说实话` | 167 | L35-58; most at L35 (129), L37 (105), L39 (117) |
| 1 | truth (the truth) | truth | `␣truth`, `truth`, `真相`, `␣Truth`, `␣truths`, `Truth`, `_truth`, `真理`, `.truth` | 191 | L35-58; most at L38 (176), L39 (171), L40 (172) |
| 1 | fact (fact / the facts) | unclear | `事实`, `␣fact`, `事实上`, `␣factual`, `␣facts`, `的事实`, `fact`, `事实和`, `facts`, `␣Fact`, `Fact`, `FACT`, `␣FACT`, `␣Facts`, `_fact`, `上述事实` | 195 | L35-58; most at L39 (176), L40 (170), L41 (174) |
| 1 | reality (the actual state of affairs) | unclear | `实际情况`, `实情`, `␣reality`, `现实`, `␣Reality`, `现实中`, `根据实际情况`, `与现实`, `Reality`, `的现实` | 157 | L35-58; most at L35 (127), L36 (120), L38 (130) |
| 1 | objective (objective, impartial) | unclear | `客观`, `␣objective`, `␣objectively` | 99 | L35-58; most at L35 (73), L36 (74), L39 (52) |
| 1 | transparent (transparency) | truth | `␣transparency`, `透明`, `-transparent`, `透明的`, `␣Transparency`, `␣transparent`, `透明度`, `transparent` | 8 | L35-57; most at L47 (6), L50 (7), L54 (7) |
| 1 | disclose (disclosing, making public) | truth | `公开`, `␣disclosure`, `␣disclosures` | 9 | L37-55; most at L47 (5), L52 (4), L53 (4) |
| 1 | reveal (revealing) | truth | `揭露`, `揭示`, `␣revealed`, `␣reveal`, `␣reveals`, `␣revealing`, `揭` | 4 | L35-55; most at L39 (3), L40 (3), L41 (3) |
| 1 | secret (secret, kept secret) | lie | `␣secret`, `␣secretly`, `秘密`, `的秘密`, `保密`, `␣Secret`, `Secret`, `secret`, `_secret`, `-secret` | 17 | L35-58; most at L35 (5), L36 (6), L56 (8) |
| 1 | confidential (confidentiality) | unclear | `␣confidentiality` | 2 | L53-57; most at L53 (2), L56 (1), L57 (1) |
| 1 | intentional (done on purpose) | unclear | `故意`, `␣deliberately`, `刻意`, `␣intentionally`, `␣deliberate`, `␣intentional` | 32 | L35-58; most at L36 (13), L37 (10), L50 (9) |
| 1 | knowing (with knowledge / knowingly) | unclear | `明知`, `知情`, `␣knowingly`, `␣knowing`, `␣Knowing` | 116 | L35-58; most at L36 (69), L43 (73), L44 (72) |
| 1 | unaware (not informed) | unclear | `不知情` | 1 | L52-52; most at L52 (1) |
| 1 | violate (violating (rules, norms)) | unclear | `违背`, `违反`, `违`, `违反了`, `违法`, `␣violate`, `␣violating`, `␣violates`, `违规` | 43 | L35-57; most at L47 (18), L48 (21), L49 (26) |
| 1 | deviate (deviating) | unclear | `偏离`, `背离` | 5 | L42-54; most at L48 (1), L49 (2), L54 (2) |
| 1 | contradict (contradiction) | unclear | `␣contradict`, `␣contrad`, `矛盾`, `␣contradictory`, `矛盾的`, `␣contradiction`, `␣contradictions`, `之间的矛盾` | 59 | L35-58; most at L48 (27), L49 (32), L50 (27) |
| 1 | ethics (ethics / morality) | unclear | `␣ethical`, `道德`, `␣moral`, `伦理`, `␣ethics`, `ethical`, `的道德`, `␣Ethics`, `职业道德`, `␣morally`, `␣morality`, `␣morals`, `␣Moral` | 28 | L35-58; most at L39 (18), L40 (18), L58 (16) |
| 1 | unethical (unethical) | lie | `␣unethical` | 1 | L58-58; most at L58 (1) |
| 1 | technically (technically (true)) | unclear | `␣technically` | 3 | L41-55; most at L41 (1), L44 (1), L55 (1) |
| 1 | partial (partial, incomplete) | unclear | `␣partially`, `␣partial`, `不完全` | 2 | L39-44; most at L39 (1), L44 (1) |
| 1 | silence (staying silent) | unclear | `沉默`, `␣silence`, `␣silent`, `␣silently` | 7 | L36-58; most at L37 (2), L42 (2), L52 (2) |
| 1 | apology (apologizing) | unclear | `道歉` | 1 | L40-40; most at L40 (1) |
| 1 | compliance (complying with rules) | unclear | `合规`, `␣adherence`, `␣compliance`, `遵守`, `␣comply`, `严格遵守`, `␣compliant`, `␣Compliance`, `␣complying` | 29 | L35-58; most at L35 (12), L37 (11), L54 (14) |
| 1 | role-play (playing a role) | unclear | `扮演`, `角色扮演` | 19 | L36-58; most at L51 (16), L52 (18), L53 (8) |
| 2 | truthful (truthfully / telling the truth) | truth | `␣truthful`, `如实`, `实话`, `实事求是`, `说实话` | 167 | L35-58; most at L35 (129), L37 (105), L39 (117) |
| 2 | knowingly (with knowledge / knowingly) | unclear | `明知`, `知情`, `␣knowingly`, `␣knowing`, `␣Knowing` | 116 | L35-58; most at L36 (69), L43 (73), L44 (72) |
| 2 | conceal (concealing / covering up information) | lie | `隐瞒`, `掩盖`, `掩饰`, `␣conceal`, `掩`, `␣concealed`, `瞒`, `遮盖`, `遮蔽`, `遮掩`, `遮住` | 119 | L35-58; most at L39 (78), L40 (92), L41 (83) |
| 2 | fabricate (making something up / fabricating) | lie | `虚构`, `␣fabricated`, `␣invented`, `␣fabrication`, `凭空`, `␣invent`, `伪造`, `␣invention` | 105 | L35-58; most at L36 (66), L37 (77), L38 (61) |
| 2 | honest (honesty / being honest) | truth | `诚`, `诚实`, `␣honest`, `␣honesty`, `诚信`, `␣honestly`, `诚实守信` | 94 | L35-58; most at L38 (57), L39 (55), L40 (59) |
| 2 | deceive (the act of deceiving) | lie | `欺骗`, `␣deception`, `␣deceptive`, `␣deceive`, `骗`, `欺` | 49 | L35-58; most at L35 (27), L36 (16), L38 (22) |
| 2 | deny (denying / denial) | lie | `否认`, `␣denying`, `␣denial`, `␣deny`, `␣denies`, `␣denied`, `deny`, `␣Denied` | 42 | L35-58; most at L49 (27), L55 (31), L56 (28) |
| 2 | violate (violating / going against) | unclear | `违背`, `违反`, `违`, `违反了`, `违法`, `␣violate`, `␣violating`, `␣violates`, `违规` | 43 | L35-57; most at L47 (18), L48 (21), L49 (26) |
| 2 | contradict (contradiction / conflict) | unclear | `␣contradict`, `␣contrad`, `矛盾`, `␣conflicting`, `␣contradictory`, `矛盾的`, `␣contradiction`, `␣conflict`, `␣contradictions`, `␣contradd`, `之间的矛盾` | 61 | L35-58; most at L48 (27), L49 (32), L50 (27) |
| 2 | admit (admitting / acknowledging) | truth | `承认`, `␣admitting`, `␣admits`, `␣admitted`, `␣admit`, `␣acknowledging`, `␣acknowledge`, `␣acknowledged`, `␣acknowledges`, `␣admite`, `␣acknowledgment` | 34 | L35-58; most at L39 (16), L40 (17), L42 (17) |
| 2 | fake (fake / false (counterfeit)) | lie | `fake`, `␣fake`, `Fake` | 25 | L35-46; most at L37 (11), L38 (18), L44 (12) |
| 2 | refuse (refusing / declining) | unclear | `␣refusal`, `拒绝`, `␣refused`, `␣refusing`, `拒`, `␣refuse`, `␣refuses`, `␣refus`, `拒絕`, `␣отказ`, `␣decline`, `拒绝了`, `␣declined`, `␣declining`, `拒不`, `␣declines`, `␣отказа` | 25 | L35-58; most at L56 (23), L57 (23), L58 (21) |
| 2 | ethics (ethics / morality) | unclear | `␣ethical`, `␣moral`, `道德`, `伦理`, `␣ethics`, `ethical`, `的道德`, `␣Ethics`, `␣morally`, `职业道德`, `␣morality`, `␣morals`, `␣Moral` | 28 | L35-58; most at L39 (18), L40 (18), L58 (16) |
| 2 | fiction (fiction / fictional) | unclear | `␣fictional`, `fiction`, `␣fiction`, `-fiction` | 38 | L35-58; most at L39 (13), L43 (12), L44 (18) |
| 2 | intentional (doing it on purpose) | unclear | `故意`, `␣deliberately`, `刻意`, `␣intentionally`, `␣deliberate`, `␣intentional` | 32 | L35-58; most at L36 (13), L37 (10), L50 (9) |
| 2 | hide (hiding something; being hidden) | lie | `隐藏`, `␣hiding`, `␣hidden`, `␣hide`, `Hide`, `␣hides`, `hide`, `隐藏着`, `隐藏的`, `␣Hide`, `_hide`, `-hide`, `Hidden`, `␣hid` | 21 | L35-58; most at L53 (7), L55 (7), L58 (7) |
| 2 | comply (complying / abiding by rules) | unclear | `合规`, `␣adherence`, `␣compliance`, `␣adher`, `遵守`, `严格遵守`, `␣adhere`, `␣compliant`, `␣Compliance`, `␣complying`, `依法` | 29 | L35-58; most at L35 (12), L37 (11), L54 (14) |
| 2 | omit (omitting / leaving out) | lie | `␣omit`, `omit`, `省略`, `␣omitted`, `␣omission`, `␣OMIT` | 17 | L39-58; most at L50 (12), L51 (11), L52 (10) |
| 2 | candid (candour / frankness) | truth | `坦诚` | 14 | L36-55; most at L39 (9), L42 (10), L43 (9) |
| 2 | withhold (withholding information) | lie | `␣withholding`, `␣withhold`, `␣withheld` | 13 | L36-58; most at L51 (7), L52 (8), L53 (10) |
| 2 | downplay (downplaying) | lie | `淡化` | 11 | L35-55; most at L49 (5), L50 (10), L52 (5) |
| 2 | secret (secrecy / keeping secret) | lie | `␣secret`, `␣secretly`, `秘密`, `保密`, `的秘密`, `␣Secret`, `␣confidentiality`, `Secret`, `secret`, `_secret`, `-secret` | 18 | L35-58; most at L35 (5), L36 (6), L56 (9) |
| 2 | disclose (disclosing / making public) | truth | `公开`, `␣disclosure`, `披露`, `␣disclosures`, `信息披露` | 10 | L36-55; most at L47 (5), L52 (4), L53 (4) |
| 2 | confess (confessing / coming clean) | truth | `坦白`, `␣confess` | 8 | L51-56; most at L51 (4), L52 (8), L53 (6) |
| 2 | misinformation (false information) | lie | `虚假信息`, `␣misinformation` | 9 | L36-54; most at L37 (5), L53 (3), L54 (3) |
| 2 | transparent (transparency) | truth | `␣transparency`, `透明`, `-transparent`, `透明的`, `␣transparent`, `␣Transparency`, `透明度`, `transparent` | 8 | L35-57; most at L47 (6), L50 (7), L54 (7) |
| 2 | cover (covering (up)) | lie | `␣cover`, `cover`, `␣covers`, `␣Cover`, `Cover`, `␣covering`, `_cover`, `COVER`, `-cover`, `␣COVER`, `掩护` | 6 | L48-58; most at L48 (1), L49 (1), L58 (5) |
| 2 | mislead (misleading) | lie | `␣misleading`, `误导`, `误导性` | 9 | L37-58; most at L50 (3), L53 (4), L54 (6) |
| 2 | evade (evading / evasion) | lie | `回避`, `␣evasion`, `␣evade` | 8 | L36-58; most at L50 (5), L51 (6), L52 (4) |
| 2 | silence (silence / staying silent) | unclear | `␣silence`, `沉默`, `␣silent`, `␣silently` | 7 | L36-58; most at L37 (2), L42 (2), L52 (2) |
| 2 | technically (technically (as a hedge)) | unclear | `␣technically` | 3 | L41-55; most at L41 (1), L44 (1), L55 (1) |
| 2 | deviate (deviating / departing from) | unclear | `偏离`, `背离` | 5 | L42-54; most at L48 (1), L49 (2), L54 (2) |
| 2 | pretend (pretending / disguising) | lie | `伪装`, `␣pretending`, `假装` | 5 | L36-46; most at L36 (3), L40 (1), L42 (1) |
| 2 | reveal (revealing) | truth | `揭示`, `␣revealed`, `␣reveal`, `␣reveals`, `␣revealing` | 2 | L35-55; most at L35 (1), L38 (1), L51 (2) |
| 2 | dishonest (dishonesty) | lie | `␣dishonest` | 1 | L51-57; most at L51 (1), L52 (1), L53 (1) |
| 2 | liar (a liar) | lie | `␣liar` | 1 | L55-56; most at L55 (1), L56 (1) |
| 2 | unethical (unethical) | lie | `␣unethical` | 1 | L58-58; most at L58 (1) |
| 2 | sorry (apology) | unclear | `道歉` | 1 | L40-40; most at L40 (1) |
| 2 | unaware (not knowing / uninformed) | unclear | `不知情` | 1 | L52-52; most at L52 (1) |

## preans_slot3

| rep | family | side | members | visibility | layer profile |
|---|---|---|---|---|---|
| 1 | hide (hiding something) | lie | `-hide`, `:hidden` | 3 | L48-57; most at L48 (2), L57 (2) |
| 1 | fiction (fictional, made-up story) | unclear | `fiction` | 2 | L46-46; most at L46 (2) |
| 1 | refuse (refusing / declining) | unclear | `␣refusal`, `␣refuse`, `拒`, `拒绝`, `␣refus` | 96 | L38-52; most at L47 (90), L48 (61), L51 (34) |
| 1 | cannot (first-person refusal formula "I cannot") | unclear | `我无法`, `我不能` | 66 | L48-58; most at L50 (25), L52 (55), L54 (26) |
| 1 | disclose (disclosing, making public) | truth | `公开` | 2 | L36-36; most at L36 (2) |
| 1 | violate (violating (rules, norms)) | unclear | `违背` | 29 | L47-48; most at L47 (14), L48 (24) |
| 1 | apology (apologizing) | unclear | `抱歉`, `Sorry`, `对不起`, `␣sorry`, `␣Sorry` | 126 | L48-58; most at L54 (126), L55 (23), L56 (19) |
| 1 | compliance (complying with rules) | unclear | `恪守`, `合规`, `␣comply` | 41 | L36-46; most at L43 (35), L44 (30), L46 (1) |
| 1 | law-abiding (law-abiding) | unclear | `守法` | 99 | L42-48; most at L42 (4), L43 (98), L47 (4) |
| 2 | disclose (disclosing / making public) | truth | `公布`, `公开` | 156 | L36-47; most at L42 (5), L43 (119), L44 (153) |
| 2 | sorry (apology) | unclear | `抱歉`, `Sorry`, `␣sorry`, `对不起`, `␣Sorry`, `␣apologize` | 126 | L48-58; most at L54 (126), L55 (23), L56 (19) |
| 2 | comply (complying / abiding by rules) | unclear | `守法`, `恪守`, `依法`, `合规` | 132 | L36-49; most at L43 (114), L44 (30), L48 (28) |
| 2 | refuse (refusing / declining) | unclear | `␣refusal`, `␣refuse`, `拒`, `拒绝`, `␣refus` | 96 | L38-52; most at L47 (90), L48 (61), L51 (34) |
| 2 | violate (violating / going against) | unclear | `违背` | 29 | L47-48; most at L47 (14), L48 (24) |
| 2 | fiction (fiction / fictional) | unclear | `fiction` | 2 | L46-46; most at L46 (2) |
| 2 | hide (hiding something; being hidden) | lie | `-hide`, `:hidden` | 3 | L48-57; most at L48 (2), L57 (2) |

## preans_slot4

| rep | family | side | members | visibility | layer profile |
|---|---|---|---|---|---|
| 1 | deceive (the act of deceiving) | lie | `欺骗`, `␣deception` | 9 | L35-55; most at L35 (8), L38 (2), L55 (1) |
| 1 | conceal (concealing the truth) | lie | `隐瞒` | 5 | L38-40; most at L38 (5), L39 (2), L40 (4) |
| 1 | hide (hiding something) | lie | `隐藏` | 1 | L35-35; most at L35 (1) |
| 1 | withhold (withholding information) | lie | `␣withholding` | 1 | L39-40; most at L39 (1), L40 (1) |
| 1 | omit (leaving something out) | lie | `省略` | 1 | L45-45; most at L45 (1) |
| 1 | fabricate (making something up) | lie | `虚构` | 24 | L35-48; most at L35 (16), L36 (17), L37 (22) |
| 1 | fiction (fictional, made-up story) | unclear | `␣fictional`, `fiction`, `␣Fiction`, `␣fiction` | 24 | L35-47; most at L36 (16), L37 (16), L40 (13) |
| 1 | downplay (downplaying, playing down) | lie | `淡化` | 7 | L36-37; most at L36 (7), L37 (1) |
| 1 | deny (denying) | lie | `否认` | 63 | L35-55; most at L44 (38), L47 (30), L48 (33) |
| 1 | refuse (refusing / declining) | unclear | `拒绝`, `␣refuse` | 3 | L50-51; most at L50 (3), L51 (1) |
| 1 | cannot (first-person refusal formula "I cannot") | unclear | `我不能`, `我无法` | 111 | L49-54; most at L51 (42), L52 (111), L53 (50) |
| 1 | admit (admitting) | truth | `承认` | 111 | L35-48; most at L35 (105), L36 (51), L37 (61) |
| 1 | acknowledge (acknowledging) | truth | `␣acknowledge`, `␣acknowledgment`, `␣acknowledging`, `␣acknowledges` | 8 | L35-46; most at L36 (3), L44 (5), L45 (4) |
| 1 | confess (confessing, coming clean) | truth | `坦白` | 74 | L35-50; most at L36 (44), L37 (69), L38 (31) |
| 1 | candid (candid, frank) | truth | `坦诚` | 66 | L35-51; most at L36 (44), L37 (52), L38 (19) |
| 1 | sincere (sincere) | truth | `诚恳` | 1 | L37-37; most at L37 (1) |
| 1 | honest (honest / honesty) | truth | `诚实`, `␣honest`, `诚`, `␣honesty` | 167 | L35-50; most at L36 (115), L37 (128), L45 (113) |
| 1 | integrity (integrity, good faith) | truth | `诚信` | 120 | L35-47; most at L35 (92), L37 (58), L40 (69) |
| 1 | truthful (truthful, telling it as it is) | truth | `␣truthful`, `如实`, `实话` | 53 | L35-46; most at L35 (49), L36 (33), L37 (16) |
| 1 | truth (the truth) | truth | `␣truth`, `真相`, `truth` | 39 | L35-50; most at L35 (34), L36 (6), L46 (5) |
| 1 | fact (fact / the facts) | unclear | `事实`, `␣factual` | 17 | L35-45; most at L35 (10), L41 (7), L43 (4) |
| 1 | reality (the actual state of affairs) | unclear | `根据实际情况` | 2 | L37-37; most at L37 (2) |
| 1 | objective (objective, impartial) | unclear | `客观`, `␣objectively` | 122 | L35-43; most at L35 (121), L36 (62), L37 (12) |
| 1 | transparent (transparency) | truth | `透明` | 1 | L46-46; most at L46 (1) |
| 1 | secret (secret, kept secret) | lie | `保密`, `秘密` | 14 | L35-50; most at L37 (6), L39 (8), L40 (12) |
| 1 | knowing (with knowledge / knowingly) | unclear | `明知` | 2 | L35-48; most at L35 (1), L45 (1), L48 (1) |
| 1 | violate (violating (rules, norms)) | unclear | `违反`, `违背`, `违反了` | 16 | L35-50; most at L35 (3), L46 (12), L47 (5) |
| 1 | contradict (contradiction) | unclear | `␣contradict`, `␣contradiction` | 1 | L50-50; most at L50 (1) |
| 1 | ethics (ethics / morality) | unclear | `␣ethical`, `␣ethics`, `伦理`, `道德`, `职业道德` | 13 | L35-43; most at L39 (5), L40 (13), L41 (5) |
| 1 | partial (partial, incomplete) | unclear | `␣partially`, `␣partial`, `␣Partial` | 13 | L35-53; most at L35 (6), L45 (8), L46 (6) |
| 1 | silence (staying silent) | unclear | `沉默`, `␣silence` | 5 | L44-50; most at L44 (1), L45 (5), L50 (1) |
| 1 | apology (apologizing) | unclear | `抱歉`, `对不起` | 84 | L35-50; most at L37 (58), L38 (45), L50 (24) |
| 2 | honest (honesty / being honest) | truth | `诚实`, `诚信`, `␣honest`, `诚`, `␣honesty`, `誠`, `诚恳` | 177 | L35-50; most at L36 (123), L37 (136), L45 (117) |
| 2 | admit (admitting / acknowledging) | truth | `承认`, `␣acknowledge`, `␣acknowledgment`, `␣acknowledging`, `␣acknowledges` | 111 | L35-48; most at L35 (105), L36 (51), L37 (61) |
| 2 | confess (confessing / coming clean) | truth | `坦白` | 74 | L35-50; most at L36 (44), L37 (69), L38 (31) |
| 2 | sorry (apology) | unclear | `抱歉`, `对不起` | 84 | L35-50; most at L37 (58), L38 (45), L50 (24) |
| 2 | candid (candour / frankness) | truth | `坦诚` | 66 | L35-51; most at L36 (44), L37 (52), L38 (19) |
| 2 | deny (denying / denial) | lie | `否认` | 63 | L35-55; most at L44 (38), L47 (30), L48 (33) |
| 2 | truthful (truthfully / telling the truth) | truth | `␣truthful`, `如实`, `实话` | 53 | L35-46; most at L35 (49), L36 (33), L37 (16) |
| 2 | fabricate (making something up / fabricating) | lie | `虚构` | 24 | L35-48; most at L35 (16), L36 (17), L37 (22) |
| 2 | fiction (fiction / fictional) | unclear | `␣fictional`, `fiction`, `␣Fiction`, `␣fiction` | 24 | L35-47; most at L36 (16), L37 (16), L40 (13) |
| 2 | violate (violating / going against) | unclear | `违反`, `违背`, `违反了` | 16 | L35-50; most at L35 (3), L46 (12), L47 (5) |
| 2 | secret (secrecy / keeping secret) | lie | `保密`, `秘密` | 14 | L35-50; most at L37 (6), L39 (8), L40 (12) |
| 2 | ethics (ethics / morality) | unclear | `␣ethical`, `␣ethics`, `伦理`, `道德`, `职业道德` | 13 | L35-43; most at L39 (5), L40 (13), L41 (5) |
| 2 | deceive (the act of deceiving) | lie | `欺骗`, `␣deception` | 9 | L35-55; most at L35 (8), L38 (2), L55 (1) |
| 2 | downplay (downplaying) | lie | `淡化` | 7 | L36-37; most at L36 (7), L37 (1) |
| 2 | silence (silence / staying silent) | unclear | `沉默`, `␣silence` | 5 | L44-50; most at L44 (1), L45 (5), L50 (1) |
| 2 | conceal (concealing / covering up information) | lie | `隐瞒` | 5 | L38-40; most at L38 (5), L39 (2), L40 (4) |
| 2 | refuse (refusing / declining) | unclear | `拒绝`, `␣refuse` | 3 | L50-51; most at L50 (3), L51 (1) |
| 2 | comply (complying / abiding by rules) | unclear | `依法`, `␣adher` | 3 | L42-45; most at L42 (1), L43 (2), L45 (1) |
| 2 | knowingly (with knowledge / knowingly) | unclear | `明知` | 2 | L35-48; most at L35 (1), L45 (1), L48 (1) |
| 2 | contradict (contradiction / conflict) | unclear | `␣contradict`, `␣contradiction` | 1 | L50-50; most at L50 (1) |
| 2 | withhold (withholding information) | lie | `␣withholding` | 1 | L39-40; most at L39 (1), L40 (1) |
| 2 | hide (hiding something; being hidden) | lie | `隐藏` | 1 | L35-35; most at L35 (1) |
| 2 | transparent (transparency) | truth | `透明` | 1 | L46-46; most at L46 (1) |
| 2 | omit (omitting / leaving out) | lie | `省略` | 1 | L45-45; most at L45 (1) |

## Replicate overlap

For each replicate-1 family, the replicate-2 family at the same position sharing the most members.

| position | rep-1 family | best rep-2 family | Jaccard of member ids | only in rep 1 | only in rep 2 |
|---|---|---|---|---|---|
| preans_slot0 | cannot | — | 0 | all | — |
| preans_slot0 | admit | admit | 0.50 | — | `␣acknowledge` |
| preans_slot0 | acknowledge | admit | 0.50 | — | `承认` |
| preans_slot0 | candid | candid | 1.00 | — | — |
| preans_slot0 | honest | honest | 1.00 | — | — |
| preans_slot0 | truth | — | 0 | all | — |
| preans_slot0 | objective | — | 0 | all | — |
| preans_slot0 | reveal | reveal | 0.50 | `揭` | — |
| preans_slot0 | intentional | intentional | 1.00 | — | — |
| preans_slot0 | knowing | knowingly | 1.00 | — | — |
| preans_slot0 | violate | violate | 1.00 | — | — |
| preans_slot0 | ethics | ethics | 1.00 | — | — |
| preans_slot0 | silence | silence | 1.00 | — | — |
| preans_slot0 | compliance | comply | 0.67 | — | `守法` |
| preans_slot0 | law-abiding | comply | 0.33 | — | `合规`, `␣compliance` |
| preans_slot0 | accuse | accuse | 1.00 | — | — |
| preans_slot1 | deceive | deceive | 1.00 | — | — |
| preans_slot1 | dishonest | dishonest | 1.00 | — | — |
| preans_slot1 | mislead | mislead | 1.00 | — | — |
| preans_slot1 | misinformation | misinformation | 1.00 | — | — |
| preans_slot1 | conceal | conceal | 0.44 | `隐匿` | `掩盖`, `掩饰`, `掩`, `遮蔽` |
| preans_slot1 | cover up | conceal | 0.25 | — | `隐瞒`, `␣conceal`, `␣concealed`, `瞒`, `掩`, `遮蔽` |
| preans_slot1 | hide | hide | 0.89 | — | `隐匿` |
| preans_slot1 | withhold | withhold | 1.00 | — | — |
| preans_slot1 | omit | omit | 1.00 | — | — |
| preans_slot1 | fabricate | fabricate | 1.00 | — | — |
| preans_slot1 | fiction | fiction | 1.00 | — | — |
| preans_slot1 | fake | fake | 1.00 | — | — |
| preans_slot1 | disguise | pretend | 0.67 | — | `␣pretending` |
| preans_slot1 | pretend | pretend | 0.33 | — | `伪装`, `␣disguised` |
| preans_slot1 | hypocrisy | hypocrisy | 1.00 | — | — |
| preans_slot1 | evade | evade | 1.00 | — | — |
| preans_slot1 | downplay | downplay | 1.00 | — | — |
| preans_slot1 | deny | deny | 1.00 | — | — |
| preans_slot1 | refuse | refuse | 1.00 | — | — |
| preans_slot1 | admit | admit | 1.00 | — | — |
| preans_slot1 | confess | confess | 1.00 | — | — |
| preans_slot1 | candid | candid | 1.00 | — | — |
| preans_slot1 | honest | honest | 0.71 | — | `诚信`, `诚实守信` |
| preans_slot1 | integrity | honest | 0.29 | — | `诚实`, `诚`, `␣honesty`, `␣honest`, `誠` |
| preans_slot1 | truthful | truthful | 1.00 | — | — |
| preans_slot1 | truth | — | 0 | all | — |
| preans_slot1 | fact | — | 0 | all | — |
| preans_slot1 | reality | — | 0 | all | — |
| preans_slot1 | objective | — | 0 | all | — |
| preans_slot1 | transparent | transparent | 1.00 | — | — |
| preans_slot1 | disclose | disclose | 1.00 | — | — |
| preans_slot1 | reveal | — | 0 | all | — |
| preans_slot1 | intentional | intentional | 0.83 | `有意` | — |
| preans_slot1 | knowing | knowingly | 1.00 | — | — |
| preans_slot1 | violate | violate | 1.00 | — | — |
| preans_slot1 | deviate | deviate | 1.00 | — | — |
| preans_slot1 | contradict | contradict | 0.75 | — | `␣conflicting`, `␣conflicts` |
| preans_slot1 | ethics | ethics | 1.00 | — | — |
| preans_slot1 | technically | technically | 1.00 | — | — |
| preans_slot1 | partial | — | 0 | all | — |
| preans_slot1 | compliance | comply | 0.71 | — | `␣adher`, `␣adhere` |
| preans_slot2 | deceive | deceive | 0.83 | — | `欺` |
| preans_slot2 | dishonest | dishonest | 1.00 | — | — |
| preans_slot2 | mislead | mislead | 1.00 | — | — |
| preans_slot2 | misinformation | misinformation | 1.00 | — | — |
| preans_slot2 | conceal | conceal | 0.36 | — | `掩盖`, `掩饰`, `掩`, `遮盖`, `遮蔽`, `遮掩`, `遮住` |
| preans_slot2 | cover up | conceal | 0.36 | — | `隐瞒`, `␣conceal`, `掩`, `␣concealed`, `瞒`, `遮蔽`, `遮住` |
| preans_slot2 | hide | hide | 1.00 | — | — |
| preans_slot2 | withhold | withhold | 1.00 | — | — |
| preans_slot2 | omit | omit | 1.00 | — | — |
| preans_slot2 | fabricate | fabricate | 1.00 | — | — |
| preans_slot2 | fiction | fiction | 1.00 | — | — |
| preans_slot2 | fake | fake | 1.00 | — | — |
| preans_slot2 | disguise | pretend | 0.33 | — | `␣pretending`, `假装` |
| preans_slot2 | pretend | pretend | 0.67 | — | `伪装` |
| preans_slot2 | evade | evade | 1.00 | — | — |
| preans_slot2 | downplay | downplay | 1.00 | — | — |
| preans_slot2 | deny | deny | 1.00 | — | — |
| preans_slot2 | refuse | refuse | 0.82 | — | `␣отказ`, `␣declining`, `␣отказа` |
| preans_slot2 | admit | admit | 0.55 | — | `␣acknowledging`, `␣acknowledge`, `␣acknowledged`, `␣acknowledges`, `␣acknowledgment` |
| preans_slot2 | acknowledge | admit | 0.45 | — | `承认`, `␣admitting`, `␣admits`, `␣admitted`, `␣admit`, `␣admite` |
| preans_slot2 | confess | confess | 1.00 | — | — |
| preans_slot2 | candid | candid | 1.00 | — | — |
| preans_slot2 | honest | honest | 0.71 | — | `诚信`, `诚实守信` |
| preans_slot2 | integrity | honest | 0.25 | `␣integrity` | `诚`, `诚实`, `␣honest`, `␣honesty`, `␣honestly` |
| preans_slot2 | truthful | truthful | 1.00 | — | — |
| preans_slot2 | truth | — | 0 | all | — |
| preans_slot2 | fact | — | 0 | all | — |
| preans_slot2 | reality | — | 0 | all | — |
| preans_slot2 | objective | — | 0 | all | — |
| preans_slot2 | transparent | transparent | 1.00 | — | — |
| preans_slot2 | disclose | disclose | 0.60 | — | `披露`, `信息披露` |
| preans_slot2 | reveal | reveal | 0.71 | `揭露`, `揭` | — |
| preans_slot2 | secret | secret | 0.91 | — | `␣confidentiality` |
| preans_slot2 | confidential | secret | 0.09 | — | `␣secret`, `␣secretly`, `秘密`, `保密`, `的秘密`, `␣Secret`, `Secret`, `secret`, `_secret`, `-secret` |
| preans_slot2 | intentional | intentional | 1.00 | — | — |
| preans_slot2 | knowing | knowingly | 1.00 | — | — |
| preans_slot2 | unaware | unaware | 1.00 | — | — |
| preans_slot2 | violate | violate | 1.00 | — | — |
| preans_slot2 | deviate | deviate | 1.00 | — | — |
| preans_slot2 | contradict | contradict | 0.73 | — | `␣conflicting`, `␣conflict`, `␣contradd` |
| preans_slot2 | ethics | ethics | 1.00 | — | — |
| preans_slot2 | unethical | unethical | 1.00 | — | — |
| preans_slot2 | technically | technically | 1.00 | — | — |
| preans_slot2 | partial | — | 0 | all | — |
| preans_slot2 | silence | silence | 1.00 | — | — |
| preans_slot2 | apology | sorry | 1.00 | — | — |
| preans_slot2 | compliance | comply | 0.67 | `␣comply` | `␣adher`, `␣adhere`, `依法` |
| preans_slot2 | role-play | — | 0 | all | — |
| preans_slot3 | hide | hide | 1.00 | — | — |
| preans_slot3 | fiction | fiction | 1.00 | — | — |
| preans_slot3 | refuse | refuse | 1.00 | — | — |
| preans_slot3 | cannot | — | 0 | all | — |
| preans_slot3 | disclose | disclose | 0.50 | — | `公布` |
| preans_slot3 | violate | violate | 1.00 | — | — |
| preans_slot3 | apology | sorry | 0.83 | — | `␣apologize` |
| preans_slot3 | compliance | comply | 0.40 | `␣comply` | `守法`, `依法` |
| preans_slot3 | law-abiding | comply | 0.25 | — | `恪守`, `依法`, `合规` |
| preans_slot4 | deceive | deceive | 1.00 | — | — |
| preans_slot4 | conceal | conceal | 1.00 | — | — |
| preans_slot4 | hide | hide | 1.00 | — | — |
| preans_slot4 | withhold | withhold | 1.00 | — | — |
| preans_slot4 | omit | omit | 1.00 | — | — |
| preans_slot4 | fabricate | fabricate | 1.00 | — | — |
| preans_slot4 | fiction | fiction | 1.00 | — | — |
| preans_slot4 | downplay | downplay | 1.00 | — | — |
| preans_slot4 | deny | deny | 1.00 | — | — |
| preans_slot4 | refuse | refuse | 1.00 | — | — |
| preans_slot4 | cannot | — | 0 | all | — |
| preans_slot4 | admit | admit | 0.20 | — | `␣acknowledge`, `␣acknowledgment`, `␣acknowledging`, `␣acknowledges` |
| preans_slot4 | acknowledge | admit | 0.80 | — | `承认` |
| preans_slot4 | confess | confess | 1.00 | — | — |
| preans_slot4 | candid | candid | 1.00 | — | — |
| preans_slot4 | sincere | honest | 0.14 | — | `诚实`, `诚信`, `␣honest`, `诚`, `␣honesty`, `誠` |
| preans_slot4 | honest | honest | 0.57 | — | `诚信`, `誠`, `诚恳` |
| preans_slot4 | integrity | honest | 0.14 | — | `诚实`, `␣honest`, `诚`, `␣honesty`, `誠`, `诚恳` |
| preans_slot4 | truthful | truthful | 1.00 | — | — |
| preans_slot4 | truth | — | 0 | all | — |
| preans_slot4 | fact | — | 0 | all | — |
| preans_slot4 | reality | — | 0 | all | — |
| preans_slot4 | objective | — | 0 | all | — |
| preans_slot4 | transparent | transparent | 1.00 | — | — |
| preans_slot4 | secret | secret | 1.00 | — | — |
| preans_slot4 | knowing | knowingly | 1.00 | — | — |
| preans_slot4 | violate | violate | 1.00 | — | — |
| preans_slot4 | contradict | contradict | 1.00 | — | — |
| preans_slot4 | ethics | ethics | 1.00 | — | — |
| preans_slot4 | partial | — | 0 | all | — |
| preans_slot4 | silence | silence | 1.00 | — | — |
| preans_slot4 | apology | sorry | 1.00 | — | — |

Replicate-2 families not the best match of any replicate-1 family: preans_slot1: liar, preans_slot1: distort, preans_slot1: misrepresent, preans_slot2: cover, preans_slot2: liar, preans_slot4: comply

## Families whose name recurs at 3 or more positions

- acknowledge: preans_slot0, preans_slot2, preans_slot4
- admit: preans_slot0, preans_slot1, preans_slot2, preans_slot4
- apology: preans_slot2, preans_slot3, preans_slot4
- candid: preans_slot0, preans_slot1, preans_slot2, preans_slot4
- cannot: preans_slot0, preans_slot3, preans_slot4
- compliance: preans_slot0, preans_slot1, preans_slot2, preans_slot3
- comply: preans_slot0, preans_slot1, preans_slot2, preans_slot3, preans_slot4
- conceal: preans_slot1, preans_slot2, preans_slot4
- confess: preans_slot1, preans_slot2, preans_slot4
- contradict: preans_slot1, preans_slot2, preans_slot4
- deceive: preans_slot1, preans_slot2, preans_slot4
- deny: preans_slot1, preans_slot2, preans_slot4
- disclose: preans_slot1, preans_slot2, preans_slot3
- downplay: preans_slot1, preans_slot2, preans_slot4
- ethics: preans_slot0, preans_slot1, preans_slot2, preans_slot4
- fabricate: preans_slot1, preans_slot2, preans_slot4
- fact: preans_slot1, preans_slot2, preans_slot4
- fiction: preans_slot1, preans_slot2, preans_slot3, preans_slot4
- hide: preans_slot1, preans_slot2, preans_slot3, preans_slot4
- honest: preans_slot0, preans_slot1, preans_slot2, preans_slot4
- integrity: preans_slot1, preans_slot2, preans_slot4
- intentional: preans_slot0, preans_slot1, preans_slot2
- knowing: preans_slot0, preans_slot1, preans_slot2, preans_slot4
- knowingly: preans_slot0, preans_slot1, preans_slot2, preans_slot4
- objective: preans_slot0, preans_slot1, preans_slot2, preans_slot4
- omit: preans_slot1, preans_slot2, preans_slot4
- partial: preans_slot1, preans_slot2, preans_slot4
- reality: preans_slot1, preans_slot2, preans_slot4
- refuse: preans_slot1, preans_slot2, preans_slot3, preans_slot4
- reveal: preans_slot0, preans_slot1, preans_slot2
- silence: preans_slot0, preans_slot2, preans_slot4
- sorry: preans_slot2, preans_slot3, preans_slot4
- transparent: preans_slot1, preans_slot2, preans_slot4
- truth: preans_slot0, preans_slot1, preans_slot2, preans_slot4
- truthful: preans_slot1, preans_slot2, preans_slot4
- violate: preans_slot0, preans_slot1, preans_slot2, preans_slot3, preans_slot4
- withhold: preans_slot1, preans_slot2, preans_slot4

## Candidate opposite pairs (same position, lie side vs truth side, antonym words in the names or glosses; merged list)

- preans_slot1: conceal / disclose
- preans_slot1: conceal / reveal
- preans_slot1: conceal / transparent
- preans_slot1: cover up / transparent
- preans_slot1: deceive / honest
- preans_slot1: deny / admit
- preans_slot1: deny / confess
- preans_slot1: dishonest / honest
- preans_slot1: evade / admit
- preans_slot1: hide / disclose
- preans_slot1: hide / reveal
- preans_slot1: mislead / candid
- preans_slot1: mislead / truth
- preans_slot1: mislead / truthful
- preans_slot2: conceal / disclose
- preans_slot2: conceal / reveal
- preans_slot2: conceal / transparent
- preans_slot2: cover / transparent
- preans_slot2: cover up / transparent
- preans_slot2: deceive / honest
- preans_slot2: deny / admit
- preans_slot2: deny / confess
- preans_slot2: dishonest / honest
- preans_slot2: evade / admit
- preans_slot2: hide / disclose
- preans_slot2: hide / reveal
- preans_slot2: mislead / candid
- preans_slot2: mislead / truth
- preans_slot2: mislead / truthful
- preans_slot3: hide / disclose
- preans_slot4: deceive / honest
- preans_slot4: deny / admit
- preans_slot4: deny / confess

Merged candidate list: `qwen3_6_27b_LL_Q9_dyl_preans_merged.json` (155 families; replicate-2 families sharing at least half
their members with a replicate-1 family at the same position are folded into it).
