# Family report: qwen3.6-27b, J-lens, band 35-58, part Q6_factual, group preans

Written by `scripts/family_report.py` from `qwen3_6_27b_J_Q6_factual_preans_rep1.json` and `_rep2.json` (prompt
`prompts/family_generation.md`). Visibility = build-split scenario transcripts (of 233) in which
at least one member is present at the position within the band. Layer profile = band layers where
the family is present in at least one transcript, and the three layers with the most transcripts
(description only; scoring uses the whole band).

## preans_slot0

| rep | family | side | members | visibility | layer profile |
|---|---|---|---|---|---|
| 1 | critique (criticism) | unclear | `批判`, `␣critique` | 52 | L58-58; most at L58 (52) |
| 1 | challenge (challenging, questioning the validity) | unclear | `质疑`, `质问` | 2 | L39-50; most at L39 (1), L41 (1), L50 (1) |

## preans_slot1

| rep | family | side | members | visibility | layer profile |
|---|---|---|---|---|---|
| 1 | lie (telling a lie) | lie | `谎言`, `谎`, `说谎`, `撒谎`, `␣거짓`, `␣lied`, `␣lie`, `␣lying`, `␣lies`, `␣liar`, `␣mentira` | 196 | L35-58; most at L41 (193), L42 (187), L43 (187) |
| 1 | deceive (the act of deceiving) | lie | `欺骗`, `␣deception`, `␣deceptive`, `骗` | 154 | L35-58; most at L40 (146), L41 (145), L42 (140) |
| 1 | fraud (fraud, swindling) | lie | `␣fraudulent`, `弄虚作假` | 23 | L37-53; most at L42 (9), L43 (14), L44 (10) |
| 1 | conceal (hiding or withholding something) | lie | `隐瞒`, `␣conceal`, `␣hiding`, `␣concealed`, `隐藏`, `hide`, `␣hidden`, `hidden`, `-hidden`, `Hidden`, `␣Hidden`, `隐藏的` | 144 | L35-58; most at L39 (116), L40 (124), L43 (125) |
| 1 | cover up (covering up / glossing over) | lie | `掩盖`, `掩饰` | 19 | L48-58; most at L51 (10), L52 (16), L53 (17) |
| 1 | secret (secret, secrecy) | lie | `秘密`, `的秘密`, `␣secret`, `␣secretly`, `␣secrecy`, `隐秘` | 6 | L37-58; most at L42 (2), L43 (3), L44 (3) |
| 1 | confidential (confidential, kept private by duty) | unclear | `␣confidentiality`, `保密` | 1 | L40-47; most at L40 (1), L42 (1), L43 (1) |
| 1 | undisclosed (not disclosed) | lie | `␣undisclosed` | 1 | L36-45; most at L36 (1), L37 (1), L38 (1) |
| 1 | disclose (disclosing, making known) | truth | `␣disclosure`, `␣Disclosure`, `␣disclosed`, `␣disclosing`, `␣disclose`, `␣disclosures`, `披露`, `公开` | 4 | L41-58; most at L42 (3), L47 (2), L49 (2) |
| 1 | reveal (revealing) | truth | `␣revealed`, `␣reveal`, `␣revealing` | 1 | L51-58; most at L51 (1), L52 (1), L53 (1) |
| 1 | transparent (transparency) | truth | `␣transparency`, `␣Transparency`, `透明` | 3 | L39-56; most at L39 (1), L54 (1), L56 (1) |
| 1 | mislead (misleading) | lie | `␣misleading`, `误导`, `误导性` | 137 | L36-58; most at L44 (115), L45 (104), L46 (88) |
| 1 | misrepresent (misrepresenting) | lie | `␣misrepresented` | 70 | L38-58; most at L46 (37), L48 (42), L49 (43) |
| 1 | misinformation (false information) | lie | `␣misinformation`, `虚假信息` | 159 | L36-58; most at L38 (80), L48 (75), L50 (96) |
| 1 | fake (fake, counterfeit) | lie | `fake`, `Fake`, `␣fake`, `␣Fake`, `_fake`, `.fake` | 157 | L35-54; most at L39 (134), L40 (150), L41 (134) |
| 1 | fabricate (fabricating / forging) | lie | `伪造`, `造假`, `␣fabricated`, `␣fabrication` | 120 | L35-58; most at L40 (110), L41 (95), L42 (103) |
| 1 | fiction (fictional, made up) | unclear | `虚构`, `␣fict`, `␣fictional`, `fiction`, `␣fiction`, `␣Fiction`, `-fiction` | 139 | L35-58; most at L38 (90), L46 (107), L47 (91) |
| 1 | pretend (pretending, feigning, disguise) | lie | `␣pretending`, `伪装`, `假装` | 23 | L40-58; most at L48 (9), L49 (9), L50 (16) |
| 1 | evade (evading) | lie | `回避` | 2 | L52-53; most at L52 (2), L53 (2) |
| 1 | deny (denying) | lie | `否认`, `␣denying`, `␣denial`, `deny`, `␣deny`, `␣denies`, `␣denied`, `␣Denied`, `否認`, `Denied` | 92 | L36-58; most at L53 (52), L55 (56), L56 (54) |
| 1 | negate (negating, saying it is not so) | unclear | `否定` | 23 | L39-57; most at L53 (9), L55 (18), L56 (13) |
| 1 | honest (honest, truthful) | truth | `␣truthful`, `␣honesty`, `诚实`, `实事求是`, `如实`, `␣honest`, `␣honestly`, `␣Honest`, `如实供述` | 200 | L36-58; most at L41 (175), L42 (160), L43 (175) |
| 1 | dishonest (dishonest) | lie | `␣dishonest` | 46 | L40-58; most at L42 (35), L44 (31), L45 (26) |
| 1 | candid (candid, frank) | truth | `坦诚` | 7 | L40-58; most at L42 (4), L52 (4), L54 (4) |
| 1 | truth (the truth (as told or hidden)) | truth | `真相`, `␣truth`, `truth`, `␣Truth`, `Truth`, `␣truths`, `实话`, `_truth`, `.truth` | 220 | L35-58; most at L39 (199), L40 (202), L41 (195) |
| 1 | admit (admitting) | truth | `承认`, `␣admitting`, `␣admitted`, `␣admit`, `␣admission`, `␣admits`, `␣admissions`, `␣Admission` | 18 | L39-58; most at L55 (16), L56 (16), L57 (14) |
| 1 | acknowledge (acknowledging) | truth | `␣acknowledging`, `␣acknowledgment`, `␣acknowledge`, `␣acknowledged`, `␣acknowledges`, `␣acknowled` | 19 | L44-58; most at L51 (13), L53 (9), L56 (10) |
| 1 | confess (confessing) | truth | `坦白`, `␣confess`, `␣confession` | 5 | L39-58; most at L51 (3), L52 (4), L54 (5) |
| 1 | clarify (clarifying) | unclear | `澄清`, `␣clarification`, `␣clarify`, `␣clarified` | 11 | L40-58; most at L52 (5), L53 (6), L57 (5) |
| 1 | refuse (refusing) | unclear | `拒绝`, `␣refusal`, `␣refusing`, `␣refus`, `␣refused`, `拒`, `␣refuse`, `␣refuses`, `拒絕`, `拒绝了` | 18 | L38-58; most at L52 (10), L56 (16), L57 (14) |
| 1 | reject (rejecting) | unclear | `␣rejecting`, `␣rejected`, `␣rejection`, `rejected` | 2 | L56-57; most at L56 (2), L57 (1) |
| 1 | cannot (being unable / declining to answer) | unclear | `我无法`, `我不能`, `␣Cannot`, `␣cannot`, `cannot`, `Cannot`, `Unable`, `␣Unable`, `不能说`, `无法`, `无法满足`, `而无法` | 8 | L36-58; most at L51 (5), L52 (7), L54 (6) |
| 1 | knowingly (with knowledge, knowingly) | unclear | `␣knowingly`, `明知`, `␣knowing`, `␣Knowing`, `Knowing` | 26 | L39-58; most at L48 (14), L52 (18), L53 (16) |
| 1 | deliberate (on purpose) | unclear | `␣intentionally`, `␣deliberately`, `故意` | 9 | L45-58; most at L54 (5), L56 (4), L57 (4) |
| 1 | unethical (morally wrong) | unclear | `␣unethical` | 3 | L42-48; most at L42 (1), L43 (2), L44 (2) |
| 1 | ethics (ethics, morality) | unclear | `␣ethical`, `ethical`, `␣ethics`, `伦理` | 4 | L44-58; most at L44 (1), L45 (1), L58 (2) |
| 1 | violate (violating a rule) | unclear | `违背`, `违反`, `违反了`, `␣violates` | 24 | L36-58; most at L47 (9), L48 (14), L49 (9) |
| 1 | prohibited (prohibited, forbidden) | unclear | `禁止` | 1 | L43-43; most at L43 (1) |
| 1 | unauthorized (unauthorized) | unclear | `␣unauthorized` | 1 | L47-53; most at L47 (1), L48 (1), L49 (1) |
| 1 | blame (blaming) | unclear | `␣blaming`, `␣blame`, `␣blamed`, `␣blames`, `指责` | 46 | L47-58; most at L51 (43), L52 (39), L54 (40) |
| 1 | contradict (contradiction) | unclear | `␣contradict`, `␣contrad`, `␣contradictory`, `␣contradiction`, `␣contradictions`, `矛盾` | 80 | L38-58; most at L47 (57), L48 (60), L49 (57) |
| 1 | disclaimer (disclaimer) | unclear | `␣disclaimer`, `␣Disclaimer`, `Disclaimer`, `␣DISCLAIMER`, `免责声明` | 22 | L39-58; most at L42 (21), L43 (17), L44 (17) |
| 2 | lie (telling a lie) | lie | `␣lie`, `␣lies`, `␣lied`, `␣lying`, `␣liar`, `谎`, `谎言`, `说谎`, `撒谎`, `␣거짓`, `␣mentira` | 196 | L35-58; most at L41 (193), L42 (187), L43 (187) |
| 2 | deceive (the act of deceiving) | lie | `␣deception`, `␣deceptive`, `欺骗`, `骗` | 154 | L35-58; most at L40 (146), L41 (145), L42 (140) |
| 2 | fraud (fraud, defrauding) | lie | `␣fraudulent` | 20 | L37-49; most at L42 (9), L43 (14), L44 (10) |
| 2 | dishonest (being dishonest) | lie | `␣dishonest` | 46 | L40-58; most at L42 (35), L44 (31), L45 (26) |
| 2 | honest (being honest or truthful in what one says) | truth | `␣truthful`, `␣honest`, `␣honesty`, `␣honestly`, `␣Honest`, `诚实`, `坦诚`, `实话`, `如实`, `实事求是`, `如实供述` | 200 | L36-58; most at L41 (175), L42 (160), L43 (175) |
| 2 | truth (the truth (noun)) | truth | `␣truth`, `truth`, `␣Truth`, `Truth`, `␣truths`, `_truth`, `.truth`, `真相`, `真实性`, `的真实性`, `内容的真实性`, `实情` | 220 | L35-58; most at L39 (199), L40 (202), L41 (195) |
| 2 | fake (fake, counterfeit) | lie | `fake`, `Fake`, `␣fake`, `␣Fake`, `_fake`, `.fake` | 157 | L35-54; most at L39 (134), L40 (150), L41 (134) |
| 2 | fabricate (fabricating, forging) | lie | `␣fabricated`, `␣fabrication`, `伪造`, `造假`, `弄虚作假` | 120 | L35-58; most at L40 (110), L41 (95), L42 (103) |
| 2 | fictional (made up, fiction) | unclear | `fiction`, `␣fiction`, `␣Fiction`, `-fiction`, `␣fictional`, `␣fict`, `虚构` | 139 | L35-58; most at L38 (90), L46 (107), L47 (91) |
| 2 | misinformation (false information) | lie | `␣misinformation`, `虚假信息` | 159 | L36-58; most at L38 (80), L48 (75), L50 (96) |
| 2 | mislead (misleading) | lie | `␣misleading`, `误导`, `误导性` | 137 | L36-58; most at L44 (115), L45 (104), L46 (88) |
| 2 | misrepresent (misrepresenting) | lie | `␣misrepresented` | 70 | L38-58; most at L46 (37), L48 (42), L49 (43) |
| 2 | conceal (the act of hiding or concealing) | lie | `隐瞒`, `掩盖`, `掩饰`, `␣conceal`, `␣concealed`, `␣hiding`, `hide`, `隐藏`, `␣masking` | 144 | L35-58; most at L39 (116), L40 (124), L43 (125) |
| 2 | hidden (being hidden) | lie | `hidden`, `␣hidden`, `Hidden`, `␣Hidden`, `-hidden`, `隐藏的` | 1 | L58-58; most at L58 (1) |
| 2 | secret (secret, secrecy) | lie | `␣secret`, `␣secretly`, `␣secrecy`, `秘密`, `的秘密` | 6 | L37-58; most at L42 (2), L43 (3), L44 (3) |
| 2 | confidential (confidentiality) | lie | `␣confidentiality`, `保密` | 1 | L40-47; most at L40 (1), L42 (1), L43 (1) |
| 2 | undisclosed (not disclosed) | lie | `␣undisclosed` | 1 | L36-45; most at L36 (1), L37 (1), L38 (1) |
| 2 | disclose (disclosing) | truth | `␣disclosure`, `␣disclosed`, `␣Disclosure`, `␣disclosing`, `␣disclose`, `␣disclosures`, `披露` | 4 | L41-58; most at L42 (3), L47 (2), L49 (2) |
| 2 | reveal (revealing, exposing) | truth | `␣revealed`, `␣reveal`, `␣revealing`, `揭露` | 5 | L42-58; most at L44 (3), L47 (2), L48 (4) |
| 2 | deny (denying) | lie | `␣denying`, `␣denial`, `deny`, `␣deny`, `␣denies`, `␣denied`, `␣Denied`, `Denied`, `否认`, `否認`, `否定` | 92 | L36-58; most at L53 (52), L55 (56), L56 (54) |
| 2 | admit (admitting) | truth | `␣admit`, `␣admitted`, `␣admits`, `␣admitting`, `␣admission`, `␣admissions`, `␣Admission`, `承认` | 18 | L39-58; most at L55 (16), L56 (16), L57 (14) |
| 2 | acknowledge (acknowledging) | truth | `␣acknowledging`, `␣acknowledgment`, `␣acknowledge`, `␣acknowledged`, `␣acknowledges`, `␣acknowled` | 19 | L44-58; most at L51 (13), L53 (9), L56 (10) |
| 2 | confess (confessing) | truth | `␣confess`, `␣confession`, `坦白` | 5 | L39-58; most at L51 (3), L52 (4), L54 (5) |
| 2 | transparent (transparency) | truth | `␣transparency`, `␣Transparency` | 2 | L54-56; most at L54 (1), L56 (1) |
| 2 | unethical (unethical, immoral) | lie | `␣unethical` | 3 | L42-48; most at L42 (1), L43 (2), L44 (2) |
| 2 | ethical (ethics, morality (neutral)) | unclear | `␣ethical`, `ethical`, `␣ethics`, `伦理` | 4 | L44-58; most at L44 (1), L45 (1), L58 (2) |
| 2 | pretend (pretending, disguising) | lie | `␣pretending`, `伪装`, `假装` | 23 | L40-58; most at L48 (9), L49 (9), L50 (16) |
| 2 | violate (violating rules or principles) | unclear | `违背`, `违反`, `违反了`, `␣violates` | 24 | L36-58; most at L47 (9), L48 (14), L49 (9) |
| 2 | deliberate (doing it on purpose) | unclear | `␣intentionally`, `␣deliberately`, `故意` | 9 | L45-58; most at L54 (5), L56 (4), L57 (4) |
| 2 | knowingly (with knowledge, knowingly) | unclear | `␣knowingly`, `明知` | 26 | L39-58; most at L48 (14), L52 (17), L53 (15) |
| 2 | contradict (contradicting) | unclear | `␣contradict`, `␣contradictory`, `␣contradiction`, `␣contradictions`, `矛盾` | 79 | L38-58; most at L47 (57), L48 (60), L49 (57) |
| 2 | refuse (refusing) | unclear | `␣refusal`, `␣refusing`, `␣refus`, `␣refused`, `␣refuse`, `␣refuses`, `拒绝`, `拒`, `拒絕`, `拒绝了` | 18 | L38-58; most at L52 (10), L56 (16), L57 (14) |
| 2 | blame (blaming) | unclear | `␣blaming`, `␣blame`, `␣blamed`, `␣blames` | 46 | L47-58; most at L51 (43), L52 (39), L54 (40) |
| 2 | claim (claiming, asserting) | unclear | `␣claiming`, `␣claim`, `claim`, `␣claims`, `Claim`, `␣Claim`, `␣Claims`, `Claims`, `claims`, `␣claimed`, `claimed`, `␣CLAIM`, `CLAIM`, `_claim`, `␣asserting`, `␣assertions`, `assert`, `␣assertion`, `␣assert`, `␣asserted`, `␣asserts`, `␣Assert`, `Assert`, `␣Assertion`, `␣Assertions`, `Assertion`, `Assertions`, `声称`, `宣称` | 177 | L35-58; most at L51 (131), L52 (134), L53 (133) |
| 2 | allege (alleging, purported) | unclear | `␣alleging`, `␣allegation`, `␣allegations`, `␣purported` | 25 | L46-58; most at L47 (10), L48 (5), L51 (12) |
| 2 | disclaimer (a disclaimer) | unclear | `␣disclaimer`, `␣Disclaimer`, `Disclaimer`, `␣DISCLAIMER` | 22 | L39-58; most at L42 (21), L43 (17), L44 (17) |
| 2 | clarify (clarifying) | unclear | `澄清` | 9 | L40-58; most at L51 (3), L52 (4), L53 (5) |

## preans_slot2

| rep | family | side | members | visibility | layer profile |
|---|---|---|---|---|---|
| 1 | lie (telling a lie) | lie | `谎言`, `说谎`, `谎`, `撒谎`, `␣거짓`, `␣mentira`, `␣lied`, `␣lying` | 61 | L35-58; most at L40 (53), L41 (43), L42 (41) |
| 1 | deceive (the act of deceiving) | lie | `欺骗`, `␣deception`, `␣deceptive`, `␣deceive`, `骗` | 75 | L35-58; most at L38 (53), L39 (54), L40 (68) |
| 1 | fraud (fraud, swindling) | lie | `␣fraudulent`, `弄虚作假`, `␣fraud`, `欺诈`, `骗局`, `骗子` | 31 | L35-58; most at L40 (15), L42 (20), L43 (17) |
| 1 | cheat (cheating) | lie | `作弊` | 19 | L35-53; most at L42 (9), L43 (12), L44 (10) |
| 1 | conceal (hiding or withholding something) | lie | `隐瞒`, `␣hidden`, `隐藏`, `hidden`, `隐藏的`, `-hidden`, `␣concealed`, `␣Hidden`, `␣conceal`, `Hidden`, `␣hiding`, `隐蔽`, `瞒`, `hide` | 139 | L35-58; most at L41 (105), L42 (105), L43 (114) |
| 1 | cover up (covering up / glossing over) | lie | `掩盖` | 3 | L39-54; most at L40 (2), L41 (1), L43 (3) |
| 1 | secret (secret, secrecy) | lie | `秘密`, `的秘密`, `␣secretly`, `␣secrecy`, `␣secret`, `secret`, `␣secretive`, `Secret`, `␣secrets`, `␣Secret`, `␣covert`, `隐秘`, `-secret`, `.secret`, `_secret` | 112 | L35-58; most at L41 (86), L43 (84), L44 (97) |
| 1 | confidential (confidential, kept private by duty) | unclear | `机密`, `␣confidentiality`, `保密`, `␣confidential`, `␣Confidential` | 87 | L35-58; most at L42 (59), L43 (65), L44 (75) |
| 1 | undisclosed (not disclosed) | lie | `␣undisclosed` | 44 | L35-50; most at L42 (17), L44 (33), L45 (32) |
| 1 | disclose (disclosing, making known) | truth | `␣disclosure`, `␣disclosed`, `␣disclosures`, `公开` | 3 | L42-54; most at L43 (1), L44 (1), L45 (1) |
| 1 | mislead (misleading) | lie | `␣misleading`, `误导`, `误导性` | 32 | L35-58; most at L37 (17), L38 (25), L39 (22) |
| 1 | misrepresent (misrepresenting) | lie | `␣misrepresented` | 10 | L38-57; most at L42 (6), L51 (5), L52 (5) |
| 1 | misinformation (false information) | lie | `␣misinformation`, `虚假信息` | 127 | L35-58; most at L37 (87), L38 (105), L39 (80) |
| 1 | fake (fake, counterfeit) | lie | `fake`, `Fake`, `␣fake`, `␣Fake`, `_fake`, `假冒` | 174 | L35-57; most at L38 (134), L39 (138), L40 (158) |
| 1 | fabricate (fabricating / forging) | lie | `伪造`, `造假`, `␣fabricated`, `␣fabrication` | 65 | L35-58; most at L36 (37), L37 (41), L40 (44) |
| 1 | fiction (fictional, made up) | unclear | `虚构`, `␣fictional`, `fiction`, `␣Fiction`, `␣fict`, `␣fiction`, `-fiction` | 123 | L35-58; most at L40 (91), L42 (81), L43 (72) |
| 1 | pretend (pretending, feigning, disguise) | lie | `伪装`, `␣pretend`, `␣pretending`, `假装` | 49 | L35-53; most at L40 (43), L41 (24), L42 (22) |
| 1 | hypocrisy (hypocrisy) | lie | `␣hypocrisy`, `虚伪` | 30 | L35-55; most at L39 (14), L40 (13), L41 (14) |
| 1 | manipulate (manipulation) | lie | `␣manipulation`, `␣manipulated` | 4 | L49-57; most at L54 (3), L55 (2), L56 (3) |
| 1 | evade (evading) | lie | `␣evade`, `␣evasion`, `回避` | 1 | L45-58; most at L45 (1), L46 (1), L47 (1) |
| 1 | deny (denying) | lie | `否认`, `␣denying`, `␣denial`, `deny`, `␣deny`, `␣denies`, `␣denied` | 7 | L36-58; most at L40 (5), L42 (5), L43 (5) |
| 1 | negate (negating, saying it is not so) | unclear | `否定` | 3 | L39-53; most at L39 (2), L40 (2), L42 (3) |
| 1 | refute (refuting) | unclear | `␣refute` | 1 | L38-54; most at L38 (1), L39 (1), L40 (1) |
| 1 | honest (honest, truthful) | truth | `␣truthful`, `实事求是`, `␣honesty`, `诚实`, `如实` | 107 | L35-58; most at L39 (93), L40 (88), L41 (89) |
| 1 | dishonest (dishonest) | lie | `␣dishonest` | 42 | L35-58; most at L41 (22), L42 (34), L43 (24) |
| 1 | truth (the truth (as told or hidden)) | truth | `真相`, `␣truth`, `truth`, `␣truths`, `Truth`, `␣Truth`, `_truth` | 171 | L35-58; most at L38 (161), L39 (160), L40 (163) |
| 1 | admit (admitting) | truth | `承认`, `␣admitting`, `␣admitted`, `␣admit`, `␣admits`, `␣admission`, `␣admissions`, `␣Admission`, `␣admite` | 15 | L38-58; most at L42 (13), L43 (11), L44 (13) |
| 1 | acknowledge (acknowledging) | truth | `␣acknowledged`, `␣acknowledges`, `␣acknowledging`, `␣acknowledgment`, `␣acknowledge`, `␣acknowled`, `␣acknowledgement`, `Acknowled` | 7 | L39-58; most at L42 (4), L47 (7), L48 (7) |
| 1 | confess (confessing) | truth | `␣confess`, `␣confessed` | 1 | L53-58; most at L53 (1), L54 (1), L55 (1) |
| 1 | clarify (clarifying) | unclear | `澄清` | 1 | L36-49; most at L36 (1), L41 (1), L42 (1) |
| 1 | refuse (refusing) | unclear | `拒绝`, `␣refusal`, `␣refusing`, `␣refused`, `␣refus`, `␣refuses`, `␣refuse`, `拒`, `拒絕`, `拒绝了`, `拒不` | 14 | L35-58; most at L43 (10), L44 (10), L45 (11) |
| 1 | reject (rejecting) | unclear | `␣rejecting`, `␣rejected`, `␣rejection`, `rejected`, `reject`, `Rejected`, `␣reject`, `Reject`, `否决` | 5 | L39-57; most at L46 (3), L48 (3), L49 (3) |
| 1 | cannot (being unable / declining to answer) | unclear | `无法`, `无法满足`, `都无法`, `根本无法` | 2 | L36-50; most at L36 (2), L38 (2), L39 (2) |
| 1 | knowingly (with knowledge, knowingly) | unclear | `明知`, `␣knowing`, `␣knowingly`, `␣Knowing`, `Knowing` | 29 | L36-58; most at L39 (19), L40 (14), L48 (15) |
| 1 | deliberate (on purpose) | unclear | `故意`, `␣intentionally`, `␣deliberately`, `␣intentional`, `␣deliberate`, `故意的`, `␣purposely` | 37 | L35-58; most at L36 (17), L38 (17), L39 (19) |
| 1 | unethical (morally wrong) | unclear | `␣unethical`, `␣immoral` | 134 | L35-58; most at L36 (94), L37 (97), L42 (98) |
| 1 | wrongdoing (wrongdoing) | unclear | `␣wrongdoing` | 4 | L36-53; most at L41 (3), L43 (2), L44 (2) |
| 1 | ethics (ethics, morality) | unclear | `␣ethical`, `␣ethics`, `ethical`, `␣morally`, `道德`, `伦理`, `␣Ethics`, `的道德`, `␣moral`, `␣Moral`, `␣morality`, `职业道德`, `␣ethic`, `␣morals` | 38 | L37-58; most at L41 (27), L42 (30), L43 (31) |
| 1 | illegal (illegal) | unclear | `非法`, `␣illegal`, `违法`, `illegal`, `Illegal`, `␣illegally`, `违法行为` | 24 | L35-58; most at L37 (14), L43 (14), L44 (13) |
| 1 | violate (violating a rule) | unclear | `违背`, `违反`, `违规`, `␣violate`, `␣violates`, `违反了`, `␣violated`, `␣violating`, `␣violations` | 56 | L35-58; most at L38 (32), L43 (31), L45 (30) |
| 1 | prohibited (prohibited, forbidden) | unclear | `禁止`, `␣prohibited`, `严禁`, `␣forbidden`, `␣forbid`, `Forbidden` | 26 | L35-55; most at L39 (15), L43 (15), L44 (13) |
| 1 | unauthorized (unauthorized) | unclear | `␣unauthorized`, `␣Unauthorized` | 19 | L35-48; most at L37 (6), L44 (6), L45 (7) |
| 1 | whistleblow (whistleblowing) | truth | `␣whistleblower`, `␣whistlebl` | 26 | L35-46; most at L41 (11), L42 (19), L43 (17) |
| 1 | blame (blaming) | unclear | `␣blaming` | 2 | L51-57; most at L51 (1), L56 (1), L57 (1) |
| 1 | contradict (contradiction) | unclear | `␣contradict`, `␣contradictory`, `矛盾`, `␣contrad`, `␣contradiction`, `␣contradictions`, `矛盾的` | 32 | L35-58; most at L38 (16), L45 (19), L46 (16) |
| 1 | disclaimer (disclaimer) | unclear | `␣disclaimer` | 7 | L35-54; most at L42 (3), L43 (3), L45 (4) |
| 2 | lie (telling a lie) | lie | `␣lied`, `␣lying`, `谎`, `谎言`, `说谎`, `撒谎`, `␣거짓`, `␣mentira` | 61 | L35-58; most at L40 (53), L41 (43), L42 (41) |
| 2 | deceive (the act of deceiving) | lie | `␣deception`, `␣deceptive`, `␣deceive`, `欺骗`, `骗`, `骗子`, `骗局` | 75 | L35-58; most at L38 (53), L39 (54), L40 (68) |
| 2 | fraud (fraud, defrauding) | lie | `␣fraudulent`, `␣fraud`, `欺诈` | 25 | L35-58; most at L42 (19), L43 (15), L44 (14) |
| 2 | dishonest (being dishonest) | lie | `␣dishonest` | 42 | L35-58; most at L41 (22), L42 (34), L43 (24) |
| 2 | honest (being honest or truthful in what one says) | truth | `␣truthful`, `␣honesty`, `诚实`, `如实`, `实事求是` | 107 | L35-58; most at L39 (93), L40 (88), L41 (89) |
| 2 | truth (the truth (noun)) | truth | `␣truth`, `truth`, `␣Truth`, `Truth`, `␣truths`, `_truth`, `真相`, `真实性`, `的真实性`, `实情` | 171 | L35-58; most at L38 (161), L39 (160), L40 (163) |
| 2 | fake (fake, counterfeit) | lie | `fake`, `Fake`, `␣fake`, `␣Fake`, `_fake`, `假冒` | 174 | L35-57; most at L38 (134), L39 (138), L40 (158) |
| 2 | fabricate (fabricating, forging) | lie | `␣fabricated`, `␣fabrication`, `伪造`, `造假`, `弄虚作假` | 66 | L35-58; most at L36 (37), L37 (41), L40 (44) |
| 2 | fictional (made up, fiction) | unclear | `fiction`, `␣fiction`, `␣Fiction`, `-fiction`, `␣fictional`, `␣fict`, `虚构` | 123 | L35-58; most at L40 (91), L42 (81), L43 (72) |
| 2 | misinformation (false information) | lie | `␣misinformation`, `虚假信息` | 127 | L35-58; most at L37 (87), L38 (105), L39 (80) |
| 2 | mislead (misleading) | lie | `␣misleading`, `误导`, `误导性` | 32 | L35-58; most at L37 (17), L38 (25), L39 (22) |
| 2 | misrepresent (misrepresenting) | lie | `␣misrepresented` | 10 | L38-57; most at L42 (6), L51 (5), L52 (5) |
| 2 | conceal (the act of hiding or concealing) | lie | `隐瞒`, `掩盖`, `␣conceal`, `␣concealed`, `␣hiding`, `hide`, `隐藏`, `␣masking` | 139 | L35-58; most at L41 (105), L42 (105), L43 (114) |
| 2 | hidden (being hidden) | lie | `hidden`, `␣hidden`, `Hidden`, `␣Hidden`, `-hidden`, `隐藏的` | 31 | L35-58; most at L55 (15), L56 (17), L58 (17) |
| 2 | secret (secret, secrecy) | lie | `␣secret`, `secret`, `Secret`, `␣Secret`, `-secret`, `.secret`, `_secret`, `␣secrets`, `␣secretly`, `␣secretive`, `␣secrecy`, `秘密`, `的秘密` | 112 | L35-58; most at L41 (86), L43 (84), L44 (97) |
| 2 | confidential (confidentiality) | lie | `␣confidential`, `␣confidentiality`, `␣Confidential`, `机密`, `保密` | 87 | L35-58; most at L42 (59), L43 (65), L44 (75) |
| 2 | undisclosed (not disclosed) | lie | `␣undisclosed` | 44 | L35-50; most at L42 (17), L44 (33), L45 (32) |
| 2 | disclose (disclosing) | truth | `␣disclosure`, `␣disclosed`, `␣disclosures` | 2 | L42-54; most at L42 (1), L54 (1) |
| 2 | reveal (revealing, exposing) | truth | `揭露` | 8 | L36-48; most at L40 (4), L42 (5), L43 (5) |
| 2 | deny (denying) | lie | `␣denying`, `␣denial`, `deny`, `␣deny`, `␣denies`, `␣denied`, `否认`, `否定` | 7 | L36-58; most at L40 (5), L42 (5), L43 (5) |
| 2 | admit (admitting) | truth | `␣admit`, `␣admitted`, `␣admits`, `␣admitting`, `␣admission`, `␣admissions`, `␣Admission`, `承认`, `␣admite` | 15 | L38-58; most at L42 (13), L43 (11), L44 (13) |
| 2 | acknowledge (acknowledging) | truth | `␣acknowledging`, `␣acknowledgment`, `␣acknowledgement`, `␣acknowledge`, `␣acknowledged`, `␣acknowledges`, `␣acknowled`, `Acknowled` | 7 | L39-58; most at L42 (4), L47 (7), L48 (7) |
| 2 | confess (confessing) | truth | `␣confess`, `␣confessed` | 1 | L53-58; most at L53 (1), L54 (1), L55 (1) |
| 2 | unethical (unethical, immoral) | lie | `␣unethical`, `␣immoral` | 134 | L35-58; most at L36 (94), L37 (97), L42 (98) |
| 2 | ethical (ethics, morality (neutral)) | unclear | `␣ethical`, `ethical`, `␣ethics`, `␣Ethics`, `␣ethic`, `␣moral`, `␣morally`, `␣morality`, `␣morals`, `␣Moral`, `道德`, `的道德`, `职业道德`, `伦理` | 38 | L37-58; most at L41 (27), L42 (30), L43 (31) |
| 2 | hypocrisy (hypocrisy) | lie | `␣hypocrisy` | 30 | L35-48; most at L39 (14), L40 (13), L41 (14) |
| 2 | pretend (pretending, disguising) | lie | `␣pretending`, `␣pretend`, `伪装`, `假装` | 49 | L35-53; most at L40 (43), L41 (24), L42 (22) |
| 2 | wrongdoing (wrongdoing) | lie | `␣wrongdoing` | 4 | L36-53; most at L41 (3), L43 (2), L44 (2) |
| 2 | cheat (cheating) | lie | `作弊` | 19 | L35-53; most at L42 (9), L43 (12), L44 (10) |
| 2 | evade (evading) | lie | `␣evade`, `␣evasion` | 1 | L45-58; most at L45 (1), L46 (1), L47 (1) |
| 2 | violate (violating rules or principles) | unclear | `违背`, `违反`, `违反了`, `违规`, `␣violate`, `␣violates`, `␣violated`, `␣violating`, `␣violations` | 56 | L35-58; most at L38 (32), L43 (31), L45 (30) |
| 2 | illegal (illegal) | unclear | `␣illegal`, `illegal`, `Illegal`, `␣illegally`, `非法`, `违法`, `违法行为` | 24 | L35-58; most at L37 (14), L43 (14), L44 (13) |
| 2 | deliberate (doing it on purpose) | unclear | `␣intentionally`, `␣intentional`, `␣deliberately`, `␣deliberate`, `␣purposely`, `故意`, `故意的` | 37 | L35-58; most at L36 (17), L38 (17), L39 (19) |
| 2 | knowingly (with knowledge, knowingly) | unclear | `␣knowingly`, `明知` | 27 | L36-58; most at L39 (19), L40 (14), L48 (15) |
| 2 | contradict (contradicting) | unclear | `␣contradict`, `␣contradictory`, `␣contradiction`, `␣contradictions`, `矛盾`, `矛盾的` | 32 | L35-58; most at L38 (16), L45 (19), L46 (16) |
| 2 | refuse (refusing) | unclear | `␣refusal`, `␣refusing`, `␣refus`, `␣refused`, `␣refuse`, `␣refuses`, `拒绝`, `拒`, `拒絕`, `拒绝了`, `拒不` | 14 | L35-58; most at L43 (10), L44 (10), L45 (11) |
| 2 | blame (blaming) | unclear | `␣blaming` | 2 | L51-57; most at L51 (1), L56 (1), L57 (1) |
| 2 | claim (claiming, asserting) | unclear | `␣claiming`, `␣claim`, `claim`, `␣claims`, `Claim`, `␣Claim`, `␣Claims`, `Claims`, `claims`, `␣claimed`, `␣CLAIM`, `CLAIM`, `_claim`, `␣asserting`, `␣assertions`, `assert`, `␣assertion`, `␣assert`, `␣asserted`, `␣asserts`, `␣Assert`, `Assert`, `声称`, `宣称` | 10 | L35-58; most at L36 (6), L43 (5), L47 (6) |
| 2 | allege (alleging, purported) | unclear | `␣alleged`, `␣allegedly`, `␣allegation`, `␣allegations`, `␣purported` | 24 | L35-51; most at L37 (10), L41 (10), L42 (13) |
| 2 | disclaimer (a disclaimer) | unclear | `␣disclaimer` | 7 | L35-54; most at L42 (3), L43 (3), L45 (4) |
| 2 | clarify (clarifying) | unclear | `澄清` | 1 | L36-49; most at L36 (1), L41 (1), L42 (1) |

## preans_slot3

| rep | family | side | members | visibility | layer profile |
|---|---|---|---|---|---|
| 1 | refuse (refusing) | unclear | `拒绝` | 4 | L45-45; most at L45 (4) |
| 1 | cannot (being unable / declining to answer) | unclear | `␣Cannot`, `我无法`, `cannot`, `不能`, `Cannot`, `我不能`, `无法`, `是不能`, `できません` | 80 | L52-56; most at L52 (7), L53 (77), L54 (67) |
| 1 | apology (apologising) | unclear | `抱歉`, `␣Sorry` | 3 | L54-57; most at L54 (3), L55 (1), L56 (1) |
| 1 | contradict (contradiction) | unclear | `矛盾` | 1 | L54-54; most at L54 (1) |
| 2 | contradict (contradicting) | unclear | `矛盾` | 1 | L54-54; most at L54 (1) |
| 2 | refuse (refusing) | unclear | `拒绝` | 4 | L45-45; most at L45 (4) |
| 2 | apologize (apologizing) | unclear | `␣Sorry`, `抱歉` | 3 | L54-57; most at L54 (3), L55 (1), L56 (1) |

## preans_slot4

| rep | family | side | members | visibility | layer profile |
|---|---|---|---|---|---|
| 1 | lie (telling a lie) | lie | `谎言`, `说谎`, `撒谎` | 93 | L36-55; most at L41 (89), L42 (75), L43 (55) |
| 1 | deceive (the act of deceiving) | lie | `欺骗`, `␣deception`, `␣deceptive` | 37 | L37-58; most at L40 (27), L41 (35), L42 (19) |
| 1 | fraud (fraud, swindling) | lie | `␣fraudulent` | 1 | L42-43; most at L42 (1), L43 (1) |
| 1 | conceal (hiding or withholding something) | lie | `隐瞒`, `␣Hidden` | 37 | L38-47; most at L40 (22), L42 (31), L43 (25) |
| 1 | confidential (confidential, kept private by duty) | unclear | `␣confidentiality`, `保密` | 2 | L40-42; most at L40 (1), L42 (1) |
| 1 | mislead (misleading) | lie | `␣misleading` | 12 | L41-45; most at L41 (9), L42 (4), L44 (5) |
| 1 | misinformation (false information) | lie | `␣misinformation` | 36 | L36-46; most at L41 (24), L42 (28), L43 (19) |
| 1 | fake (fake, counterfeit) | lie | `fake`, `␣Fake`, `␣fake`, `Fake` | 51 | L36-48; most at L40 (49), L41 (29), L42 (33) |
| 1 | fabricate (fabricating / forging) | lie | `伪造` | 1 | L42-42; most at L42 (1) |
| 1 | fiction (fictional, made up) | unclear | `虚构`, `␣fictional`, `␣Fiction`, `␣fict`, `fiction`, `␣fiction` | 42 | L36-49; most at L40 (30), L42 (40), L46 (32) |
| 1 | pretend (pretending, feigning, disguise) | lie | `伪装` | 3 | L37-47; most at L38 (2), L40 (3), L42 (2) |
| 1 | deny (denying) | lie | `否认`, `否認` | 21 | L36-49; most at L42 (19), L43 (11), L48 (10) |
| 1 | negate (negating, saying it is not so) | unclear | `否定` | 12 | L39-57; most at L43 (5), L48 (10), L49 (7) |
| 1 | refute (refuting) | unclear | `␣refute` | 1 | L42-42; most at L42 (1) |
| 1 | honest (honest, truthful) | truth | `␣truthful`, `␣honest`, `␣honesty`, `诚实`, `␣Honest`, `如实` | 226 | L35-50; most at L41 (212), L42 (217), L43 (214) |
| 1 | dishonest (dishonest) | lie | `␣dishonest` | 7 | L40-44; most at L41 (2), L42 (7), L43 (2) |
| 1 | truth (the truth (as told or hidden)) | truth | `␣Truth`, `␣truth`, `真相`, `truth`, `Truth`, `␣truths` | 227 | L35-51; most at L41 (213), L43 (214), L45 (223) |
| 1 | admit (admitting) | truth | `承认` | 4 | L39-46; most at L42 (3), L44 (2), L46 (2) |
| 1 | acknowledge (acknowledging) | truth | `␣acknowledgment`, `␣acknowledging`, `␣acknowledge` | 7 | L39-46; most at L39 (1), L45 (5), L46 (5) |
| 1 | clarify (clarifying) | unclear | `澄清` | 2 | L36-42; most at L36 (1), L41 (1), L42 (1) |
| 1 | refuse (refusing) | unclear | `拒绝` | 1 | L42-42; most at L42 (1) |
| 1 | reject (rejecting) | unclear | `␣Reject` | 1 | L48-49; most at L48 (1), L49 (1) |
| 1 | cannot (being unable / declining to answer) | unclear | `␣Cannot` | 8 | L51-55; most at L52 (4), L53 (7), L54 (4) |
| 1 | apology (apologising) | unclear | `␣Sorry` | 2 | L51-54; most at L51 (1), L54 (1) |
| 1 | knowingly (with knowledge, knowingly) | unclear | `␣knowingly` | 1 | L44-46; most at L44 (1), L45 (1), L46 (1) |
| 1 | deliberate (on purpose) | unclear | `␣intentionally`, `␣intentional`, `␣deliberately`, `故意`, `␣deliberate`, `故意的`, `␣purposely` | 18 | L38-58; most at L45 (15), L46 (10), L47 (10) |
| 1 | unethical (morally wrong) | unclear | `␣unethical` | 6 | L39-44; most at L42 (4), L43 (6), L44 (5) |
| 1 | ethics (ethics, morality) | unclear | `␣ethical` | 3 | L41-45; most at L41 (1), L42 (3), L43 (1) |
| 1 | violate (violating a rule) | unclear | `违背` | 1 | L45-47; most at L45 (1), L46 (1), L47 (1) |
| 1 | unauthorized (unauthorized) | unclear | `␣unauthorized` | 1 | L45-45; most at L45 (1) |
| 1 | disclaimer (disclaimer) | unclear | `␣disclaimer` | 1 | L45-45; most at L45 (1) |
| 2 | lie (telling a lie) | lie | `谎言`, `说谎`, `撒谎` | 93 | L36-55; most at L41 (89), L42 (75), L43 (55) |
| 2 | deceive (the act of deceiving) | lie | `␣deception`, `␣deceptive`, `欺骗` | 37 | L37-58; most at L40 (27), L41 (35), L42 (19) |
| 2 | fraud (fraud, defrauding) | lie | `␣fraudulent` | 1 | L42-43; most at L42 (1), L43 (1) |
| 2 | dishonest (being dishonest) | lie | `␣dishonest` | 7 | L40-44; most at L41 (2), L42 (7), L43 (2) |
| 2 | honest (being honest or truthful in what one says) | truth | `␣truthful`, `␣honest`, `␣honesty`, `␣Honest`, `诚实`, `如实` | 226 | L35-50; most at L41 (212), L42 (217), L43 (214) |
| 2 | truth (the truth (noun)) | truth | `␣truth`, `truth`, `␣Truth`, `Truth`, `␣truths`, `真相`, `真实性`, `的真实性` | 227 | L35-51; most at L41 (213), L43 (214), L45 (223) |
| 2 | fake (fake, counterfeit) | lie | `fake`, `Fake`, `␣fake`, `␣Fake` | 51 | L36-48; most at L40 (49), L41 (29), L42 (33) |
| 2 | fabricate (fabricating, forging) | lie | `伪造` | 1 | L42-42; most at L42 (1) |
| 2 | fictional (made up, fiction) | unclear | `fiction`, `␣fiction`, `␣Fiction`, `␣fictional`, `␣fict`, `虚构` | 42 | L36-49; most at L40 (30), L42 (40), L46 (32) |
| 2 | misinformation (false information) | lie | `␣misinformation` | 36 | L36-46; most at L41 (24), L42 (28), L43 (19) |
| 2 | mislead (misleading) | lie | `␣misleading` | 12 | L41-45; most at L41 (9), L42 (4), L44 (5) |
| 2 | conceal (the act of hiding or concealing) | lie | `隐瞒` | 36 | L38-47; most at L40 (22), L42 (31), L43 (25) |
| 2 | hidden (being hidden) | lie | `␣Hidden` | 1 | L45-46; most at L45 (1), L46 (1) |
| 2 | confidential (confidentiality) | lie | `␣confidentiality`, `保密` | 2 | L40-42; most at L40 (1), L42 (1) |
| 2 | deny (denying) | lie | `否认`, `否認`, `否定` | 22 | L36-57; most at L42 (19), L43 (11), L48 (13) |
| 2 | admit (admitting) | truth | `承认` | 4 | L39-46; most at L42 (3), L44 (2), L46 (2) |
| 2 | acknowledge (acknowledging) | truth | `␣acknowledging`, `␣acknowledgment`, `␣acknowledge` | 7 | L39-46; most at L39 (1), L45 (5), L46 (5) |
| 2 | unethical (unethical, immoral) | lie | `␣unethical` | 6 | L39-44; most at L42 (4), L43 (6), L44 (5) |
| 2 | ethical (ethics, morality (neutral)) | unclear | `␣ethical` | 3 | L41-45; most at L41 (1), L42 (3), L43 (1) |
| 2 | pretend (pretending, disguising) | lie | `伪装` | 3 | L37-47; most at L38 (2), L40 (3), L42 (2) |
| 2 | violate (violating rules or principles) | unclear | `违背` | 1 | L45-47; most at L45 (1), L46 (1), L47 (1) |
| 2 | deliberate (doing it on purpose) | unclear | `␣intentionally`, `␣intentional`, `␣deliberately`, `␣deliberate`, `␣purposely`, `故意`, `故意的` | 18 | L38-58; most at L45 (15), L46 (10), L47 (10) |
| 2 | knowingly (with knowledge, knowingly) | unclear | `␣knowingly` | 1 | L44-46; most at L44 (1), L45 (1), L46 (1) |
| 2 | refuse (refusing) | unclear | `拒绝` | 1 | L42-42; most at L42 (1) |
| 2 | claim (claiming, asserting) | unclear | `␣assertions`, `␣assertion` | 11 | L41-46; most at L42 (11), L43 (8), L45 (6) |
| 2 | disclaimer (a disclaimer) | unclear | `␣disclaimer` | 1 | L45-45; most at L45 (1) |
| 2 | apologize (apologizing) | unclear | `␣Sorry` | 2 | L51-54; most at L51 (1), L54 (1) |
| 2 | clarify (clarifying) | unclear | `澄清` | 2 | L36-42; most at L36 (1), L41 (1), L42 (1) |

## Replicate overlap

For each replicate-1 family, the replicate-2 family at the same position sharing the most members.

| position | rep-1 family | best rep-2 family | Jaccard of member ids | only in rep 1 | only in rep 2 |
|---|---|---|---|---|---|
| preans_slot0 | critique | — | 0 | all | — |
| preans_slot0 | challenge | — | 0 | all | — |
| preans_slot1 | lie | lie | 1.00 | — | — |
| preans_slot1 | deceive | deceive | 1.00 | — | — |
| preans_slot1 | fraud | fraud | 0.50 | `弄虚作假` | — |
| preans_slot1 | conceal | hidden | 0.50 | `隐瞒`, `␣conceal`, `␣hiding`, `␣concealed`, `隐藏`, `hide` | — |
| preans_slot1 | cover up | conceal | 0.22 | — | `隐瞒`, `␣conceal`, `␣concealed`, `␣hiding`, `hide`, `隐藏`, `␣masking` |
| preans_slot1 | secret | secret | 0.83 | `隐秘` | — |
| preans_slot1 | confidential | confidential | 1.00 | — | — |
| preans_slot1 | undisclosed | undisclosed | 1.00 | — | — |
| preans_slot1 | disclose | disclose | 0.88 | `公开` | — |
| preans_slot1 | reveal | reveal | 0.75 | — | `揭露` |
| preans_slot1 | transparent | transparent | 0.67 | `透明` | — |
| preans_slot1 | mislead | mislead | 1.00 | — | — |
| preans_slot1 | misrepresent | misrepresent | 1.00 | — | — |
| preans_slot1 | misinformation | misinformation | 1.00 | — | — |
| preans_slot1 | fake | fake | 1.00 | — | — |
| preans_slot1 | fabricate | fabricate | 0.80 | — | `弄虚作假` |
| preans_slot1 | fiction | fictional | 1.00 | — | — |
| preans_slot1 | pretend | pretend | 1.00 | — | — |
| preans_slot1 | evade | — | 0 | all | — |
| preans_slot1 | deny | deny | 0.91 | — | `否定` |
| preans_slot1 | negate | deny | 0.09 | — | `␣denying`, `␣denial`, `deny`, `␣deny`, `␣denies`, `␣denied`, `␣Denied`, `Denied`, `否认`, `否認` |
| preans_slot1 | honest | honest | 0.82 | — | `坦诚`, `实话` |
| preans_slot1 | dishonest | dishonest | 1.00 | — | — |
| preans_slot1 | candid | honest | 0.09 | — | `␣truthful`, `␣honest`, `␣honesty`, `␣honestly`, `␣Honest`, `诚实`, `实话`, `如实`, `实事求是`, `如实供述` |
| preans_slot1 | truth | truth | 0.62 | `实话` | `真实性`, `的真实性`, `内容的真实性`, `实情` |
| preans_slot1 | admit | admit | 1.00 | — | — |
| preans_slot1 | acknowledge | acknowledge | 1.00 | — | — |
| preans_slot1 | confess | confess | 1.00 | — | — |
| preans_slot1 | clarify | clarify | 0.25 | `␣clarification`, `␣clarify`, `␣clarified` | — |
| preans_slot1 | refuse | refuse | 1.00 | — | — |
| preans_slot1 | reject | — | 0 | all | — |
| preans_slot1 | cannot | — | 0 | all | — |
| preans_slot1 | knowingly | knowingly | 0.40 | `␣knowing`, `␣Knowing`, `Knowing` | — |
| preans_slot1 | deliberate | deliberate | 1.00 | — | — |
| preans_slot1 | unethical | unethical | 1.00 | — | — |
| preans_slot1 | ethics | ethical | 1.00 | — | — |
| preans_slot1 | violate | violate | 1.00 | — | — |
| preans_slot1 | prohibited | — | 0 | all | — |
| preans_slot1 | unauthorized | — | 0 | all | — |
| preans_slot1 | blame | blame | 0.80 | `指责` | — |
| preans_slot1 | contradict | contradict | 0.83 | `␣contrad` | — |
| preans_slot1 | disclaimer | disclaimer | 0.80 | `免责声明` | — |
| preans_slot2 | lie | lie | 1.00 | — | — |
| preans_slot2 | deceive | deceive | 0.71 | — | `骗子`, `骗局` |
| preans_slot2 | fraud | fraud | 0.50 | `弄虚作假`, `骗局`, `骗子` | — |
| preans_slot2 | cheat | cheat | 1.00 | — | — |
| preans_slot2 | conceal | hidden | 0.43 | `隐瞒`, `隐藏`, `␣concealed`, `␣conceal`, `␣hiding`, `隐蔽`, `瞒`, `hide` | — |
| preans_slot2 | cover up | conceal | 0.12 | — | `隐瞒`, `␣conceal`, `␣concealed`, `␣hiding`, `hide`, `隐藏`, `␣masking` |
| preans_slot2 | secret | secret | 0.87 | `␣covert`, `隐秘` | — |
| preans_slot2 | confidential | confidential | 1.00 | — | — |
| preans_slot2 | undisclosed | undisclosed | 1.00 | — | — |
| preans_slot2 | disclose | disclose | 0.75 | `公开` | — |
| preans_slot2 | mislead | mislead | 1.00 | — | — |
| preans_slot2 | misrepresent | misrepresent | 1.00 | — | — |
| preans_slot2 | misinformation | misinformation | 1.00 | — | — |
| preans_slot2 | fake | fake | 1.00 | — | — |
| preans_slot2 | fabricate | fabricate | 0.80 | — | `弄虚作假` |
| preans_slot2 | fiction | fictional | 1.00 | — | — |
| preans_slot2 | pretend | pretend | 1.00 | — | — |
| preans_slot2 | hypocrisy | hypocrisy | 0.50 | `虚伪` | — |
| preans_slot2 | manipulate | — | 0 | all | — |
| preans_slot2 | evade | evade | 0.67 | `回避` | — |
| preans_slot2 | deny | deny | 0.88 | — | `否定` |
| preans_slot2 | negate | deny | 0.12 | — | `␣denying`, `␣denial`, `deny`, `␣deny`, `␣denies`, `␣denied`, `否认` |
| preans_slot2 | refute | — | 0 | all | — |
| preans_slot2 | honest | honest | 1.00 | — | — |
| preans_slot2 | dishonest | dishonest | 1.00 | — | — |
| preans_slot2 | truth | truth | 0.70 | — | `真实性`, `的真实性`, `实情` |
| preans_slot2 | admit | admit | 1.00 | — | — |
| preans_slot2 | acknowledge | acknowledge | 1.00 | — | — |
| preans_slot2 | confess | confess | 1.00 | — | — |
| preans_slot2 | clarify | clarify | 1.00 | — | — |
| preans_slot2 | refuse | refuse | 1.00 | — | — |
| preans_slot2 | reject | — | 0 | all | — |
| preans_slot2 | cannot | — | 0 | all | — |
| preans_slot2 | knowingly | knowingly | 0.40 | `␣knowing`, `␣Knowing`, `Knowing` | — |
| preans_slot2 | deliberate | deliberate | 1.00 | — | — |
| preans_slot2 | unethical | unethical | 1.00 | — | — |
| preans_slot2 | wrongdoing | wrongdoing | 1.00 | — | — |
| preans_slot2 | ethics | ethical | 1.00 | — | — |
| preans_slot2 | illegal | illegal | 1.00 | — | — |
| preans_slot2 | violate | violate | 1.00 | — | — |
| preans_slot2 | prohibited | — | 0 | all | — |
| preans_slot2 | unauthorized | — | 0 | all | — |
| preans_slot2 | whistleblow | — | 0 | all | — |
| preans_slot2 | blame | blame | 1.00 | — | — |
| preans_slot2 | contradict | contradict | 0.86 | `␣contrad` | — |
| preans_slot2 | disclaimer | disclaimer | 1.00 | — | — |
| preans_slot3 | refuse | refuse | 1.00 | — | — |
| preans_slot3 | cannot | — | 0 | all | — |
| preans_slot3 | apology | apologize | 1.00 | — | — |
| preans_slot3 | contradict | contradict | 1.00 | — | — |
| preans_slot4 | lie | lie | 1.00 | — | — |
| preans_slot4 | deceive | deceive | 1.00 | — | — |
| preans_slot4 | fraud | fraud | 1.00 | — | — |
| preans_slot4 | conceal | conceal | 0.50 | `␣Hidden` | — |
| preans_slot4 | confidential | confidential | 1.00 | — | — |
| preans_slot4 | mislead | mislead | 1.00 | — | — |
| preans_slot4 | misinformation | misinformation | 1.00 | — | — |
| preans_slot4 | fake | fake | 1.00 | — | — |
| preans_slot4 | fabricate | fabricate | 1.00 | — | — |
| preans_slot4 | fiction | fictional | 1.00 | — | — |
| preans_slot4 | pretend | pretend | 1.00 | — | — |
| preans_slot4 | deny | deny | 0.67 | — | `否定` |
| preans_slot4 | negate | deny | 0.33 | — | `否认`, `否認` |
| preans_slot4 | refute | — | 0 | all | — |
| preans_slot4 | honest | honest | 1.00 | — | — |
| preans_slot4 | dishonest | dishonest | 1.00 | — | — |
| preans_slot4 | truth | truth | 0.75 | — | `真实性`, `的真实性` |
| preans_slot4 | admit | admit | 1.00 | — | — |
| preans_slot4 | acknowledge | acknowledge | 1.00 | — | — |
| preans_slot4 | clarify | clarify | 1.00 | — | — |
| preans_slot4 | refuse | refuse | 1.00 | — | — |
| preans_slot4 | reject | — | 0 | all | — |
| preans_slot4 | cannot | — | 0 | all | — |
| preans_slot4 | apology | apologize | 1.00 | — | — |
| preans_slot4 | knowingly | knowingly | 1.00 | — | — |
| preans_slot4 | deliberate | deliberate | 1.00 | — | — |
| preans_slot4 | unethical | unethical | 1.00 | — | — |
| preans_slot4 | ethics | ethical | 1.00 | — | — |
| preans_slot4 | violate | violate | 1.00 | — | — |
| preans_slot4 | unauthorized | — | 0 | all | — |
| preans_slot4 | disclaimer | disclaimer | 1.00 | — | — |

Replicate-2 families not the best match of any replicate-1 family: preans_slot1: claim, preans_slot1: allege, preans_slot2: reveal, preans_slot2: claim, preans_slot2: allege, preans_slot4: hidden, preans_slot4: claim

## Families whose name recurs at 3 or more positions

- acknowledge: preans_slot1, preans_slot2, preans_slot4
- admit: preans_slot1, preans_slot2, preans_slot4
- cannot: preans_slot1, preans_slot2, preans_slot3, preans_slot4
- claim: preans_slot1, preans_slot2, preans_slot4
- clarify: preans_slot1, preans_slot2, preans_slot4
- conceal: preans_slot1, preans_slot2, preans_slot4
- confidential: preans_slot1, preans_slot2, preans_slot4
- contradict: preans_slot1, preans_slot2, preans_slot3
- deceive: preans_slot1, preans_slot2, preans_slot4
- deliberate: preans_slot1, preans_slot2, preans_slot4
- deny: preans_slot1, preans_slot2, preans_slot4
- disclaimer: preans_slot1, preans_slot2, preans_slot4
- dishonest: preans_slot1, preans_slot2, preans_slot4
- ethical: preans_slot1, preans_slot2, preans_slot4
- ethics: preans_slot1, preans_slot2, preans_slot4
- fabricate: preans_slot1, preans_slot2, preans_slot4
- fake: preans_slot1, preans_slot2, preans_slot4
- fiction: preans_slot1, preans_slot2, preans_slot4
- fictional: preans_slot1, preans_slot2, preans_slot4
- fraud: preans_slot1, preans_slot2, preans_slot4
- hidden: preans_slot1, preans_slot2, preans_slot4
- honest: preans_slot1, preans_slot2, preans_slot4
- knowingly: preans_slot1, preans_slot2, preans_slot4
- lie: preans_slot1, preans_slot2, preans_slot4
- misinformation: preans_slot1, preans_slot2, preans_slot4
- mislead: preans_slot1, preans_slot2, preans_slot4
- negate: preans_slot1, preans_slot2, preans_slot4
- pretend: preans_slot1, preans_slot2, preans_slot4
- refuse: preans_slot1, preans_slot2, preans_slot3, preans_slot4
- reject: preans_slot1, preans_slot2, preans_slot4
- truth: preans_slot1, preans_slot2, preans_slot4
- unauthorized: preans_slot1, preans_slot2, preans_slot4
- unethical: preans_slot1, preans_slot2, preans_slot4
- violate: preans_slot1, preans_slot2, preans_slot4

## Candidate opposite pairs (same position, lie side vs truth side, antonym words in the names or glosses; merged list)

- preans_slot1: conceal / disclose
- preans_slot1: conceal / reveal
- preans_slot1: cover up / transparent
- preans_slot1: deceive / honest
- preans_slot1: deny / admit
- preans_slot1: deny / confess
- preans_slot1: dishonest / honest
- preans_slot1: evade / admit
- preans_slot1: lie / honest
- preans_slot1: lie / truth
- preans_slot1: mislead / candid
- preans_slot2: conceal / disclose
- preans_slot2: conceal / reveal
- preans_slot2: deceive / honest
- preans_slot2: deny / admit
- preans_slot2: deny / confess
- preans_slot2: dishonest / honest
- preans_slot2: evade / admit
- preans_slot2: hidden / admit
- preans_slot2: hidden / confess
- preans_slot2: hidden / disclose
- preans_slot2: lie / honest
- preans_slot2: lie / truth
- preans_slot4: deceive / honest
- preans_slot4: deny / admit
- preans_slot4: dishonest / honest
- preans_slot4: hidden / admit
- preans_slot4: lie / honest
- preans_slot4: lie / truth

Merged candidate list: `qwen3_6_27b_J_Q6_factual_preans_merged.json` (138 families; replicate-2 families sharing at least half
their members with a replicate-1 family at the same position are folded into it).
