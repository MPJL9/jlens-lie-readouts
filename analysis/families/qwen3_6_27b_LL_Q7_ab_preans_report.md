# Family report: qwen3.6-27b, logit lens, band 35-58, part Q7_ab, group preans

Written by `scripts/family_report.py` from `qwen3_6_27b_LL_Q7_ab_preans_rep1.json` and `_rep2.json` (prompt
`prompts/family_generation.md`). Visibility = build-split scenario transcripts (of 233) in which
at least one member is present at the position within the band. Layer profile = band layers where
the family is present in at least one transcript, and the three layers with the most transcripts
(description only; scoring uses the whole band).

## preans_slot0

| rep | family | side | members | visibility | layer profile |
|---|---|---|---|---|---|
| 1 | clarify (clarifying) | unclear | `␣clarification` | 1 | L37-48; most at L37 (1), L38 (1), L42 (1) |
| 1 | deny (denying, negating) | lie | `否定` | 1 | L47-47; most at L47 (1) |
| 1 | cannot (cannot, unable (refusal stance)) | unclear | `不能`, `我无法` | 11 | L51-54; most at L51 (1), L53 (2), L54 (9) |
| 1 | ethics (ethics, morality, right and wrong) | unclear | `是非` | 1 | L39-39; most at L39 (1) |
| 1 | violate (violating (rules, instructions, principles)) | unclear | `违` | 39 | L52-53; most at L52 (6), L53 (38) |
| 1 | lawful (lawful, law-abiding) | unclear | `守法` | 1 | L47-48; most at L47 (1), L48 (1) |
| 1 | despicable (a petty / despicable person (小人)) | unclear | `小人` | 4 | L50-50; most at L50 (4) |
| 2 | deny (denying) | lie | `否定` | 1 | L47-47; most at L47 (1) |
| 2 | clarify (clarifying) | unclear | `␣clarification` | 1 | L37-48; most at L37 (1), L38 (1), L42 (1) |
| 2 | ethics (ethics / morality (right and wrong)) | unclear | `是非` | 1 | L39-39; most at L39 (1) |
| 2 | violate (violating a rule or instruction) | unclear | `违` | 39 | L52-53; most at L52 (6), L53 (38) |

## preans_slot1

| rep | family | side | members | visibility | layer profile |
|---|---|---|---|---|---|
| 1 | deceive (the act of deceiving) | lie | `欺骗`, `␣deception`, `骗` | 8 | L35-58; most at L35 (2), L50 (2), L52 (2) |
| 1 | trick (a trick, to trick) | lie | `␣trick` | 5 | L38-58; most at L50 (2), L51 (2), L53 (3) |
| 1 | hide (hiding, being hidden) | lie | `隐藏的`, `␣hidden`, `隐藏`, `Hidden`, `hidden`, `␣Hidden`, `隱藏`, `_hidden`, `-hidden`, `隐藏在`, `隐藏着`, `hide`, `␣hiding`, `-hide`, `隐匿` | 106 | L35-58; most at L55 (81), L56 (95), L58 (76) |
| 1 | conceal (concealing (withholding the truth from someone)) | lie | `隐瞒`, `␣concealed`, `␣conceal` | 44 | L35-58; most at L35 (15), L39 (15), L40 (35) |
| 1 | cover up (covering up, masking) | lie | `掩盖`, `掩饰` | 2 | L36-44; most at L36 (1), L40 (1), L44 (1) |
| 1 | suppress (suppressing, keeping down) | lie | `␣suppression`, `压下`, `␣suppress` | 3 | L35-51; most at L35 (2), L37 (1), L51 (1) |
| 1 | secret (secret, secrecy, in secret) | lie | `␣secret`, `secret`, `暗中`, `秘密`, `Secret`, `␣secretly`, `_secret`, `␣Secret`, `的秘密`, `-secret`, `保密`, `隐秘`, `.secret`, `.Secret`, `␣confidential` | 94 | L35-58; most at L43 (39), L44 (38), L56 (77) |
| 1 | private (private, privately) | unclear | `私下`, `␣private`, `␣privately` | 56 | L35-49; most at L43 (23), L44 (48), L45 (30) |
| 1 | internal (internal, not public) | unclear | `␣internal`, `内部`, `␣internally`, `internal`, `␣Internal`, `的内部`, `/internal`, `Internal`, `内部的`, `␣INTERNAL`, `.internal`, `_internal`, `INTERNAL` | 101 | L35-58; most at L54 (89), L55 (86), L56 (73) |
| 1 | outward appearance (on the surface, outwardly) | unclear | `表面上` | 12 | L35-50; most at L36 (4), L37 (5), L38 (4) |
| 1 | official line (the agreed public line / talking points (口径)) | unclear | `口径` | 2 | L51-57; most at L51 (1), L52 (2), L53 (1) |
| 1 | deliberate (on purpose, intentionally) | unclear | `␣intentionally`, `故意`, `␣deliberately`, `刻意`, `␣deliberate`, `␣intentional` | 79 | L35-57; most at L35 (56), L36 (67), L37 (42) |
| 1 | knowingly (knowing the truth, knowingly) | unclear | `明知`, `知情`, `␣knowing` | 177 | L35-56; most at L35 (150), L48 (129), L49 (133) |
| 1 | fictional (fictional, made-up setting) | unclear | `虚构`, `架空`, `␣fictional`, `fiction`, `␣fict`, `␣Fiction` | 130 | L35-58; most at L35 (56), L37 (60), L40 (55) |
| 1 | hypothetical (hypothetical, supposed) | unclear | `假设`, `␣hypothetical`, `␣hypoth`, `假定` | 72 | L35-58; most at L40 (33), L42 (33), L43 (37) |
| 1 | fabricate (making something up) | lie | `伪造`, `␣invent` | 5 | L35-47; most at L35 (1), L36 (1), L37 (3) |
| 1 | fake (fake, counterfeit) | lie | `fake`, `␣fake` | 10 | L35-38; most at L35 (2), L36 (7), L37 (8) |
| 1 | pretend (pretending, disguising) | lie | `␣pretend`, `伪装`, `␣pretending`, `假装` | 3 | L37-54; most at L37 (2), L53 (1), L54 (1) |
| 1 | misinformation (false information) | lie | `␣misinformation` | 1 | L51-57; most at L51 (1), L52 (1), L53 (1) |
| 1 | honest (honesty) | truth | `诚实`, `␣honesty`, `诚`, `诚信`, `␣honest`, `坦诚` | 45 | L35-58; most at L35 (18), L39 (16), L40 (28) |
| 1 | integrity (integrity, uprightness) | truth | `␣integrity`, `␣Integrity` | 6 | L50-58; most at L51 (3), L55 (4), L56 (5) |
| 1 | loyal (loyalty) | unclear | `␣loyalty`, `忠诚`, `忠于`, `忠诚度`, `␣loyal` | 9 | L35-58; most at L50 (4), L51 (6), L52 (4) |
| 1 | faithful (faithful (to facts or to a party)) | unclear | `忠实` | 22 | L35-52; most at L35 (7), L36 (19), L37 (7) |
| 1 | admit (admitting) | truth | `承认` | 15 | L35-58; most at L42 (9), L43 (7), L44 (4) |
| 1 | acknowledge (acknowledging) | truth | `␣acknowledging`, `␣acknowledge`, `␣acknowledges`, `␣acknowledged`, `␣acknowledgment` | 3 | L52-58; most at L54 (2), L55 (2), L56 (1) |
| 1 | disclose (disclosing, revealing) | truth | `␣disclosure`, `␣disclosures`, `揭`, `␣revealed` | 9 | L35-47; most at L35 (4), L36 (5), L37 (5) |
| 1 | inform (telling, informing someone) | unclear | `告知` | 11 | L36-51; most at L41 (5), L42 (7), L46 (2) |
| 1 | deny (denying, negating) | lie | `否定`, `否认`, `␣denial` | 7 | L39-56; most at L39 (3), L48 (3), L51 (2) |
| 1 | refuse (refusing, declining) | unclear | `拒绝`, `␣refusal`, `拒`, `␣refus`, `␣refuse`, `␣refusing`, `␣refused`, `␣refuses`, `拒絕`, `拒不`, `拒绝了`, `␣declined`, `␣decline`, `␣declining`, `␣declines` | 15 | L38-58; most at L41 (10), L55 (9), L56 (12) |
| 1 | cannot (cannot, unable (refusal stance)) | unclear | `无法满足`, `又不能`, `不能`, `更不能`, `我不能`, `就无法`, `不能说` | 18 | L35-53; most at L35 (8), L36 (11), L39 (7) |
| 1 | evade (avoiding, evading) | unclear | `回避`, `␣avoid`, `␣avoiding`, `␣avoided`, `␣Avoid`, `avoid`, `Avoid`, `␣avoids` | 3 | L50-58; most at L51 (3), L52 (3), L53 (3) |
| 1 | euphemistic (tactful, indirect wording) | unclear | `委婉`, `婉` | 7 | L35-51; most at L35 (5), L36 (4), L37 (2) |
| 1 | ethics (ethics, morality, right and wrong) | unclear | `是非`, `␣ethical`, `伦理`, `␣ethics`, `道德`, `␣moral`, `␣morally`, `ethical`, `的道德`, `␣Ethics`, `␣morality`, `职业道德`, `␣ethic`, `␣morals`, `␣Moral` | 68 | L35-58; most at L37 (43), L39 (47), L40 (47) |
| 1 | unethical (unethical) | lie | `␣unethical` | 7 | L39-58; most at L40 (3), L55 (6), L56 (3) |
| 1 | conscience (conscience) | unclear | `良心` | 1 | L51-51; most at L51 (1) |
| 1 | violate (violating (rules, instructions, principles)) | unclear | `违背`, `违反`, `违`, `违反了`, `违规`, `␣violated`, `␣violate`, `␣violating`, `␣violates` | 76 | L35-57; most at L35 (41), L37 (45), L38 (34) |
| 1 | lawful (lawful, law-abiding) | unclear | `合法`, `␣legal` | 3 | L41-49; most at L41 (1), L42 (1), L49 (1) |
| 1 | contradict (contradiction) | unclear | `␣contrad`, `矛盾`, `矛盾的`, `␣contradict`, `␣contradictory`, `␣contradiction` | 92 | L35-57; most at L47 (60), L48 (51), L49 (45) |
| 1 | conflict (conflicting (demands)) | unclear | `␣conflicting`, `␣conflict`, `␣conflicts` | 43 | L35-56; most at L44 (20), L45 (21), L47 (22) |
| 1 | manipulate (manipulating) | lie | `␣manipulation`, `␣manipulate`, `␣manipulated` | 1 | L54-57; most at L54 (1), L55 (1), L56 (1) |
| 1 | pander (pandering, trying to please) | unclear | `迎合` | 15 | L35-53; most at L35 (11), L36 (7), L37 (2) |
| 1 | embellish (embellishing, prettifying) | unclear | `美化` | 1 | L50-50; most at L50 (1) |
| 1 | comply (complying, obeying) | unclear | `严格遵守`, `合规`, `服从`, `遵照`, `遵守`, `遵循`, `遵从`, `␣compliance`, `␣comply`, `␣obey`, `␣adherence`, `␣adher`, `␣adhere` | 31 | L35-58; most at L36 (9), L37 (9), L38 (10) |
| 1 | protect (protecting, safeguarding (an interest)) | unclear | `维护`, `␣protecting`, `为维护`, `保全`, `保护`, `为了保护`, `和维护`, `␣protect`, `Protect`, `自我保护`, `protect`, `␣Protect` | 14 | L35-58; most at L36 (8), L37 (9), L43 (7) |
| 1 | role-play (playing a role / persona) | unclear | `␣persona`, `扮演`, `␣Persona`, `␣personas`, `角色扮演`, `persona`, `Persona`, `扮演着`, `␣Personas` | 153 | L36-58; most at L52 (120), L53 (129), L56 (132) |
| 1 | firm (firmly, resolutely) | unclear | `坚决` | 7 | L45-52; most at L45 (1), L49 (7), L50 (2) |
| 2 | deceive (the act of deceiving) | lie | `欺骗`, `␣deception`, `骗` | 8 | L35-58; most at L35 (2), L50 (2), L52 (2) |
| 2 | manipulate (manipulating someone) | lie | `␣manipulation`, `␣manipulate`, `␣manipulated` | 1 | L54-57; most at L54 (1), L55 (1), L56 (1) |
| 2 | trick (a trick played on someone) | lie | `␣trick` | 5 | L38-58; most at L50 (2), L51 (2), L53 (3) |
| 2 | conceal (the act of hiding / covering up) | lie | `隐藏`, `隐瞒`, `隱藏`, `隠`, `␣conceal`, `␣concealed`, `掩盖`, `遮`, `隐藏着`, `隐藏在`, `掩饰`, `藏着`, `隐匿`, `hide`, `-hide` | 106 | L35-58; most at L55 (70), L56 (70), L58 (69) |
| 2 | hidden (being hidden / not disclosed (state)) | lie | `隐藏的`, `␣hidden`, `Hidden`, `␣Hidden`, `hidden`, `隐`, `_hidden`, `-hidden`, `隐秘` | 103 | L35-58; most at L55 (80), L56 (95), L58 (74) |
| 2 | secret (something kept secret / done in secret) | lie | `␣secret`, `私下`, `secret`, `暗中`, `秘密`, `Secret`, `␣secretly`, `_secret`, `␣Secret`, `的秘密`, `-secret`, `.secret`, `.Secret` | 98 | L35-58; most at L43 (46), L44 (61), L56 (77) |
| 2 | confidential (confidential / kept private) | unclear | `保密`, `␣confidential` | 6 | L35-44; most at L39 (3), L40 (4), L43 (2) |
| 2 | fake (fake / false (made up)) | lie | `fake`, `␣fake`, `虚假`, `␣misinformation` | 12 | L35-57; most at L35 (2), L36 (7), L37 (8) |
| 2 | fabricate (the act of fabricating / forging) | lie | `伪造` | 3 | L37-47; most at L37 (2), L46 (1), L47 (1) |
| 2 | pretend (pretending / disguising) | lie | `␣pretend`, `伪装`, `␣pretending`, `假装` | 3 | L37-54; most at L37 (2), L53 (1), L54 (1) |
| 2 | evade (evading / dodging) | lie | `回避`, `规避` | 3 | L50-57; most at L51 (2), L52 (2), L53 (2) |
| 2 | deny (denying) | lie | `否定`, `否认`, `␣denial` | 7 | L39-56; most at L39 (3), L48 (3), L51 (2) |
| 2 | surface (on the surface / outward appearance (ostensibly)) | unclear | `表面上` | 12 | L35-50; most at L36 (4), L37 (5), L38 (4) |
| 2 | euphemism (tactful / euphemistic wording) | unclear | `委婉`, `婉` | 7 | L35-51; most at L35 (5), L36 (4), L37 (2) |
| 2 | talking points (official line / agreed wording (口径)) | unclear | `口径` | 2 | L51-57; most at L51 (1), L52 (2), L53 (1) |
| 2 | role-play (playing a role) | unclear | `扮演`, `角色扮演`, `扮演着` | 93 | L36-58; most at L51 (68), L52 (87), L53 (39) |
| 2 | fictional (fictional / made-up setting) | unclear | `虚构`, `架空`, `␣fictional`, `fiction`, `␣Fiction` | 130 | L35-58; most at L35 (56), L37 (60), L40 (55) |
| 2 | intentional (doing something on purpose) | unclear | `␣intentionally`, `故意`, `␣deliberately`, `刻意`, `␣deliberate`, `␣intentional` | 79 | L35-57; most at L35 (56), L36 (67), L37 (42) |
| 2 | knowingly (knowing full well (明知)) | unclear | `明知` | 177 | L35-53; most at L35 (149), L48 (129), L49 (133) |
| 2 | truth (the truth) | truth | `␣truth`, `真相`, `truth`, `␣Truth`, `实情`, `实话`, `Truth`, `_truth`, `␣truths`, `真理` | 151 | L35-58; most at L39 (115), L40 (121), L41 (129) |
| 2 | fact (fact / reality) | unclear | `␣fact`, `事实`, `实际情况`, `␣reality`, `␣facts`, `的事实`, `␣factual`, `␣Fact`, `事实上`, `fact`, `␣Facts`, `事实和`, `␣Reality`, `facts`, `Fact`, `␣FACT`, `FACT`, `Reality`, `根据实际情况`, `_fact` | 146 | L35-58; most at L39 (129), L40 (110), L41 (112) |
| 2 | honest (honest / honesty) | truth | `␣honesty`, `诚`, `␣honest` | 11 | L35-58; most at L55 (7), L56 (7), L57 (5) |
| 2 | integrity (integrity / uprightness) | truth | `␣integrity`, `诚信`, `␣Integrity` | 8 | L35-58; most at L51 (3), L55 (4), L56 (5) |
| 2 | candid (candid / frank) | truth | `坦诚` | 1 | L51-51; most at L51 (1) |
| 2 | admit (admitting / acknowledging) | truth | `承认`, `␣acknowledging`, `␣acknowledge`, `␣acknowledges`, `␣acknowledged`, `␣acknowledgment` | 15 | L35-58; most at L42 (9), L43 (7), L44 (4) |
| 2 | disclose (disclosing / revealing) | truth | `␣disclosure`, `␣disclosures`, `揭`, `␣revealed` | 9 | L35-47; most at L35 (4), L36 (5), L37 (5) |
| 2 | inform (informing / telling (告知)) | unclear | `告知` | 11 | L36-51; most at L41 (5), L42 (7), L46 (2) |
| 2 | account for (account for / explain; also 'come clean' (交代)) | unclear | `交代` | 86 | L35-41; most at L35 (54), L36 (68), L37 (67) |
| 2 | refuse (refusing) | unclear | `拒绝`, `␣refusal`, `␣refus`, `␣refuse`, `␣refusing`, `␣refused`, `␣refuses`, `拒绝了` | 15 | L38-58; most at L41 (9), L55 (9), L56 (12) |
| 2 | ethics (ethics / morality (right and wrong)) | unclear | `是非`, `␣ethical`, `伦理`, `␣ethics`, `道德`, `␣moral`, `␣morally`, `ethical`, `的道德`, `␣Ethics`, `␣morality`, `职业道德`, `␣ethic`, `␣morals`, `␣Moral` | 68 | L35-58; most at L37 (43), L39 (47), L40 (47) |
| 2 | unethical (unethical) | lie | `␣unethical` | 7 | L39-58; most at L40 (3), L55 (6), L56 (3) |
| 2 | violate (violating a rule or instruction) | unclear | `违背`, `违反`, `违`, `违反了`, `违规`, `␣violate`, `␣violated`, `␣violates`, `␣violating` | 76 | L35-57; most at L35 (41), L37 (45), L38 (34) |
| 2 | contradict (contradiction) | unclear | `矛盾`, `矛盾的`, `␣contradict`, `␣contradictory`, `␣contradiction` | 72 | L35-57; most at L47 (33), L48 (39), L49 (43) |
| 2 | conflict (conflicting (claims or goals)) | unclear | `␣conflicting`, `␣conflict`, `␣conflicts` | 43 | L35-56; most at L44 (20), L45 (21), L47 (22) |
| 2 | loyalty (loyalty / faithfulness) | unclear | `忠实`, `␣loyalty`, `忠诚`, `忠于`, `忠诚度`, `␣loyal` | 29 | L35-58; most at L35 (8), L36 (20), L37 (9) |

## preans_slot2

| rep | family | side | members | visibility | layer profile |
|---|---|---|---|---|---|
| 1 | deceive (the act of deceiving) | lie | `欺骗`, `␣deception`, `␣deceptive`, `骗`, `␣deceive`, `␣deceived` | 28 | L35-58; most at L50 (22), L52 (12), L53 (12) |
| 1 | fraud (fraud, swindle) | lie | `诈骗`, `欺诈`, `骗局` | 1 | L37-58; most at L37 (1), L38 (1), L40 (1) |
| 1 | mislead (leading someone to a wrong belief) | lie | `␣misleading`, `误导`, `误导性` | 18 | L35-58; most at L50 (8), L52 (12), L53 (16) |
| 1 | trick (a trick, to trick) | lie | `␣trick`, `␣tricks` | 2 | L35-58; most at L35 (1), L38 (1), L58 (1) |
| 1 | hide (hiding, being hidden) | lie | `隐藏`, `␣hidden`, `隐藏的`, `␣hiding`, `隐藏着`, `␣hide`, `hide`, `Hide`, `␣hides`, `隐蔽`, `-hidden`, `-hide`, `_hide`, `hidden`, `␣Hidden`, `:hidden`, `.hide`, `␣Hide`, `␣hid` | 38 | L35-58; most at L53 (18), L54 (12), L55 (11) |
| 1 | conceal (concealing (withholding the truth from someone)) | lie | `隐瞒`, `␣conceal`, `瞒`, `␣concealed` | 78 | L35-58; most at L35 (38), L36 (50), L40 (52) |
| 1 | cover up (covering up, masking) | lie | `掩盖`, `掩`, `␣masking`, `␣cover`, `遮盖`, `掩饰`, `cover`, `␣Cover`, `Cover`, `␣masks`, `遮掩`, `␣covering`, `掩护`, `遮蔽`, `COVER`, `-cover` | 36 | L35-58; most at L35 (25), L36 (27), L40 (24) |
| 1 | suppress (suppressing, keeping down) | lie | `压下`, `␣suppression`, `suppress` | 29 | L36-53; most at L36 (7), L40 (11), L50 (10) |
| 1 | secret (secret, secrecy, in secret) | lie | `␣secret`, `秘密`, `机密`, `的秘密`, `保密`, `␣Secret`, `secret`, `␣secretly`, `␣confidential`, `暗中`, `-secret`, `_secret`, `.secret`, `␣secrets`, `␣confidentiality`, `Secret`, `(secret`, `隐秘`, `␣Confidential` | 58 | L35-58; most at L35 (27), L36 (30), L37 (22) |
| 1 | private (private, privately) | unclear | `私下`, `␣private`, `␣privately`, `␣Private`, `private`, `Private`, `.private`, `PRIVATE`, `/private`, `私人`, `私密`, `(private`, `-private`, `/Private`, `,private`, `私自` | 49 | L35-58; most at L43 (24), L44 (35), L45 (28) |
| 1 | internal (internal, not public) | unclear | `␣internal`, `内部`, `␣internally`, `的内部`, `internal`, `␣Internal`, `/internal`, `Internal`, `内部的`, `␣INTERNAL`, `.internal`, `_internal`, `公司内部`, `INTERNAL`, `_INTERNAL`, `/Internal`, `(internal`, `.Internal`, `	internal`, `企业内部` | 73 | L35-58; most at L39 (34), L44 (35), L56 (35) |
| 1 | outward appearance (on the surface, outwardly) | unclear | `表面上`, `对外`, `表面的` | 53 | L35-52; most at L37 (24), L38 (26), L40 (27) |
| 1 | official line (the agreed public line / talking points (口径)) | unclear | `口径` | 24 | L39-57; most at L51 (16), L52 (17), L53 (18) |
| 1 | deliberate (on purpose, intentionally) | unclear | `␣intentionally`, `故意`, `␣deliberately`, `刻意`, `␣deliberate`, `␣intentional` | 47 | L35-58; most at L35 (30), L36 (29), L49 (20) |
| 1 | knowingly (knowing the truth, knowingly) | unclear | `明知`, `知情`, `␣knowing`, `␣Knowing`, `␣knowingly`, `Knowing` | 94 | L35-58; most at L48 (60), L49 (68), L50 (51) |
| 1 | fictional (fictional, made-up setting) | unclear | `虚构`, `␣fictional`, `fiction`, `␣fict`, `架空`, `␣Fiction`, `␣fiction` | 72 | L35-58; most at L36 (41), L37 (56), L39 (38) |
| 1 | hypothetical (hypothetical, supposed) | unclear | `␣hypothetical`, `假设`, `␣hypoth` | 47 | L35-58; most at L40 (32), L42 (23), L43 (24) |
| 1 | fabricate (making something up) | lie | `伪造`, `␣fabricated`, `␣invented`, `␣fabrication`, `作假` | 14 | L35-57; most at L36 (6), L37 (6), L52 (4) |
| 1 | fake (fake, counterfeit) | lie | `fake`, `␣fake`, `Fake`, `伪` | 16 | L35-54; most at L36 (6), L37 (8), L38 (8) |
| 1 | pretend (pretending, disguising) | lie | `伪装`, `␣pretend`, `␣pretending`, `假装` | 10 | L35-54; most at L36 (7), L49 (3), L50 (5) |
| 1 | misinformation (false information) | lie | `␣misinformation`, `虚假信息` | 11 | L50-58; most at L50 (5), L51 (5), L53 (11) |
| 1 | honest (honesty) | truth | `诚实`, `诚`, `␣honest`, `␣honesty`, `诚信`, `坦诚` | 17 | L35-55; most at L35 (8), L36 (7), L37 (8) |
| 1 | loyal (loyalty) | unclear | `␣loyalty`, `忠诚`, `忠于`, `忠诚度`, `␣loyal`, `忠` | 13 | L38-58; most at L51 (9), L52 (7), L54 (4) |
| 1 | faithful (faithful (to facts or to a party)) | unclear | `忠实`, `␣faithfully` | 13 | L35-48; most at L36 (7), L37 (5), L38 (5) |
| 1 | admit (admitting) | truth | `␣admits`, `承认`, `␣admitted`, `␣admitting`, `␣admit`, `承認` | 12 | L35-58; most at L55 (10), L56 (8), L57 (7) |
| 1 | acknowledge (acknowledging) | truth | `␣acknowledge`, `␣acknowledged`, `␣acknowledges`, `␣acknowledging`, `␣acknowledgment` | 5 | L39-58; most at L51 (3), L52 (3), L55 (4) |
| 1 | confess (confessing) | truth | `␣confess`, `␣confession`, `␣confessed`, `坦白` | 2 | L52-58; most at L52 (1), L57 (1), L58 (1) |
| 1 | disclose (disclosing, revealing) | truth | `揭露`, `␣disclosed`, `␣disclosure`, `披露`, `透露`, `␣revealed`, `揭示`, `揭` | 10 | L35-58; most at L35 (3), L36 (5), L37 (2) |
| 1 | undisclosed (not disclosed) | lie | `␣undisclosed` | 3 | L51-58; most at L52 (3), L53 (3), L54 (2) |
| 1 | transparent (transparency) | truth | `␣transparency` | 1 | L54-54; most at L54 (1) |
| 1 | inform (telling, informing someone) | unclear | `告知`, `␣tell`, `␣tells`, `被告知`, `␣telling`, `Tell`, `␣inform`, `请告知`, `␣Tell`, `␣informed`, `inform` | 50 | L35-58; most at L35 (28), L36 (16), L42 (12) |
| 1 | clarify (clarifying) | unclear | `澄清` | 1 | L36-36; most at L36 (1) |
| 1 | deny (denying, negating) | lie | `否认` | 1 | L44-56; most at L44 (1), L45 (1), L46 (1) |
| 1 | refuse (refusing, declining) | unclear | `拒绝` | 1 | L41-44; most at L41 (1), L42 (1), L44 (1) |
| 1 | cannot (cannot, unable (refusal stance)) | unclear | `不能`, `又不能`, `不能说`, `␣cannot`, `Cannot`, `cannot`, `␣Cannot`, `无法`, `也不能`, `都不能`, `就不能`, `都无法`, `但不能`, `我们不能`, `而不能`, `根本无法`, `不能在`, `绝对不能`, `绝不能`, `却不能`, `不能让` | 3 | L47-58; most at L47 (1), L48 (2), L50 (2) |
| 1 | evade (avoiding, evading) | unclear | `回避`, `␣avoid`, `␣avoidance` | 4 | L36-52; most at L36 (2), L51 (2), L52 (1) |
| 1 | euphemistic (tactful, indirect wording) | unclear | `委婉` | 15 | L35-39; most at L35 (14), L36 (7), L37 (5) |
| 1 | ethics (ethics, morality, right and wrong) | unclear | `是非`, `␣ethical`, `伦理`, `␣ethics`, `道德`, `ethical`, `␣moral`, `␣morally` | 16 | L35-58; most at L40 (9), L41 (7), L42 (6) |
| 1 | unethical (unethical) | lie | `␣unethical` | 4 | L51-58; most at L52 (3), L55 (3), L58 (3) |
| 1 | violate (violating (rules, instructions, principles)) | unclear | `违背`, `违`, `违规`, `违反` | 43 | L35-54; most at L35 (26), L36 (12), L37 (18) |
| 1 | illegal (illegal) | unclear | `␣illegal`, `违法` | 1 | L53-55; most at L53 (1), L54 (1), L55 (1) |
| 1 | contradict (contradiction) | unclear | `矛盾`, `矛盾的`, `␣contrad`, `␣contradict`, `␣contradictory` | 32 | L35-56; most at L44 (19), L45 (17), L46 (20) |
| 1 | conflict (conflicting (demands)) | unclear | `␣conflicting`, `␣conflict`, `␣conflicts` | 14 | L39-58; most at L47 (9), L48 (8), L53 (8) |
| 1 | guilt (guilt) | unclear | `␣guilt` | 1 | L53-54; most at L53 (1), L54 (1) |
| 1 | wrongdoing (wrongdoing) | unclear | `␣wrongdoing` | 2 | L52-56; most at L52 (1), L53 (1), L56 (1) |
| 1 | manipulate (manipulating) | lie | `␣manipulation`, `␣manipulate`, `␣manipulated`, `␣manipulating`, `␣manipul`, `操纵` | 4 | L37-58; most at L54 (3), L55 (3), L56 (2) |
| 1 | scheme (a scheme, plot) | unclear | `␣scheme` | 17 | L37-46; most at L37 (9), L41 (9), L42 (6) |
| 1 | pander (pandering, trying to please) | unclear | `迎合`, `讨好` | 11 | L35-52; most at L35 (6), L36 (7), L37 (2) |
| 1 | embellish (embellishing, prettifying) | unclear | `美化` | 7 | L35-55; most at L43 (4), L44 (5), L45 (4) |
| 1 | comply (complying, obeying) | unclear | `遵照`, `合规`, `服从`, `遵从`, `␣compliance`, `遵循`, `严格遵守`, `␣obey`, `遵`, `遵守`, `␣adherence`, `␣adher` | 50 | L35-58; most at L35 (19), L49 (19), L50 (17) |
| 1 | protect (protecting, safeguarding (an interest)) | unclear | `维护`, `和维护`, `保全`, `保护`, `␣protecting`, `为了保护`, `␣protect`, `␣protects`, `protect`, `为维护`, `保护和`, `保护的`, `␣Protect`, `Protect`, `的保护`, `和保护`, `␣protection`, `␣protective`, `与维护`, `␣protected`, `␣Protective` | 67 | L35-58; most at L37 (48), L39 (46), L40 (46) |
| 1 | role-play (playing a role / persona) | unclear | `␣persona`, `扮演`, `␣personas`, `␣Persona`, `角色扮演`, `persona`, `Persona`, `扮演着` | 57 | L35-58; most at L52 (41), L53 (43), L56 (45) |
| 1 | firm (firmly, resolutely) | unclear | `坚决` | 3 | L44-55; most at L44 (2), L46 (2), L49 (3) |
| 1 | selfish (selfish) | unclear | `自私` | 1 | L52-52; most at L52 (1) |
| 1 | discovered (being found out) | unclear | `␣discovered` | 2 | L45-57; most at L45 (1), L49 (1), L57 (1) |
| 2 | deceive (the act of deceiving) | lie | `欺骗`, `␣deception`, `␣deceptive`, `骗`, `␣deceive`, `␣deceit`, `␣deceived` | 28 | L35-58; most at L50 (22), L52 (12), L53 (12) |
| 2 | fraud (fraud / swindle) | lie | `␣fraud`, `␣fraudulent`, `欺诈`, `诈骗`, `骗局` | 1 | L37-58; most at L37 (1), L38 (1), L40 (1) |
| 2 | mislead (leading someone to a false belief) | lie | `␣misleading`, `误导`, `误导性` | 18 | L35-58; most at L50 (8), L52 (12), L53 (16) |
| 2 | manipulate (manipulating someone) | lie | `␣manipulation`, `␣manipulate`, `␣manipulated`, `␣manipulating`, `␣manipul`, `操纵` | 4 | L37-58; most at L54 (3), L55 (3), L56 (2) |
| 2 | trick (a trick played on someone) | lie | `␣trick`, `␣tricks` | 2 | L35-58; most at L35 (1), L38 (1), L58 (1) |
| 2 | conceal (the act of hiding / covering up) | lie | `隐瞒`, `掩盖`, `隐藏`, `␣conceal`, `掩`, `␣masking`, `瞒`, `隐藏着`, `␣concealed`, `遮盖`, `␣hide`, `掩饰`, `隐蔽`, `hide`, `Hide`, `␣hides`, `遮掩`, `遮`, `-hide`, `_hide`, `␣masks`, `遮蔽`, `掩护`, `藏着`, `.hide`, `␣Hide` | 88 | L35-58; most at L35 (49), L36 (54), L40 (57) |
| 2 | hidden (being hidden / not disclosed (state)) | lie | `␣hidden`, `隐藏的`, `␣undisclosed`, `-hidden`, `␣Hidden`, `hidden`, `:hidden`, `隐秘`, `隐` | 21 | L37-58; most at L53 (11), L54 (11), L55 (12) |
| 2 | secret (something kept secret / done in secret) | lie | `␣secret`, `私下`, `秘密`, `的秘密`, `␣Secret`, `secret`, `␣secretly`, `暗中`, `-secret`, `_secret`, `.secret`, `␣secrets`, `Secret`, `(secret` | 59 | L35-58; most at L36 (27), L44 (35), L45 (26) |
| 2 | confidential (confidential / kept private) | unclear | `机密`, `保密`, `␣confidential`, `␣confidentiality`, `私密`, `␣Confidential` | 27 | L35-58; most at L36 (10), L37 (10), L53 (10) |
| 2 | fake (fake / false (made up)) | lie | `虚假`, `fake`, `␣misinformation`, `虚假信息`, `␣fake`, `Fake`, `伪` | 26 | L35-58; most at L36 (19), L37 (20), L38 (17) |
| 2 | fabricate (the act of fabricating / forging) | lie | `伪造`, `␣fabricated`, `␣fabrication`, `作假` | 13 | L35-57; most at L36 (6), L37 (6), L52 (3) |
| 2 | pretend (pretending / disguising) | lie | `伪装`, `␣pretend`, `␣pretending`, `假装`, `␣disguised` | 10 | L35-54; most at L36 (7), L49 (3), L50 (5) |
| 2 | impersonate (impersonating someone) | lie | `冒充` | 1 | L49-51; most at L49 (1), L50 (1), L51 (1) |
| 2 | evade (evading / dodging) | lie | `回避`, `规避` | 3 | L36-52; most at L36 (1), L51 (2), L52 (1) |
| 2 | deny (denying) | lie | `否认` | 1 | L44-56; most at L44 (1), L45 (1), L46 (1) |
| 2 | surface (on the surface / outward appearance (ostensibly)) | unclear | `表面上`, `表面的` | 43 | L35-51; most at L35 (17), L37 (20), L38 (25) |
| 2 | euphemism (tactful / euphemistic wording) | unclear | `委婉` | 15 | L35-39; most at L35 (14), L36 (7), L37 (5) |
| 2 | talking points (official line / agreed wording (口径)) | unclear | `口径` | 24 | L39-57; most at L51 (16), L52 (17), L53 (18) |
| 2 | role-play (playing a role) | unclear | `扮演`, `角色扮演`, `扮演着` | 30 | L36-58; most at L51 (20), L52 (28), L53 (14) |
| 2 | fictional (fictional / made-up setting) | unclear | `虚构`, `␣fictional`, `fiction`, `架空`, `␣fiction`, `␣Fiction` | 72 | L35-58; most at L36 (41), L37 (56), L39 (38) |
| 2 | intentional (doing something on purpose) | unclear | `␣intentionally`, `故意`, `␣deliberately`, `刻意`, `␣deliberate`, `␣intentional` | 47 | L35-58; most at L35 (30), L36 (29), L49 (20) |
| 2 | knowingly (knowing full well (明知)) | unclear | `明知` | 89 | L35-58; most at L48 (59), L49 (67), L50 (50) |
| 2 | truth (the truth) | truth | `␣truth`, `真相`, `实情`, `truth`, `␣Truth`, `真理`, `_truth`, `实话`, `␣truths` | 99 | L35-58; most at L38 (81), L39 (83), L40 (79) |
| 2 | fact (fact / reality) | unclear | `␣fact`, `实际情况`, `事实`, `␣reality`, `␣facts`, `的事实`, `␣factual`, `事实上`, `fact`, `␣Fact`, `Fact`, `␣FACT`, `facts`, `事实和`, `␣Facts`, `␣Reality`, `FACT`, `事实证明` | 117 | L35-58; most at L35 (99), L36 (98), L37 (93) |
| 2 | honest (honest / honesty) | truth | `诚`, `␣honest`, `␣honesty` | 9 | L35-54; most at L35 (3), L36 (3), L37 (4) |
| 2 | integrity (integrity / uprightness) | truth | `诚信` | 1 | L41-41; most at L41 (1) |
| 2 | candid (candid / frank) | truth | `坦诚` | 1 | L38-42; most at L38 (1), L39 (1), L40 (1) |
| 2 | transparency (transparency) | truth | `␣transparency` | 1 | L54-54; most at L54 (1) |
| 2 | confess (confessing / coming clean) | truth | `␣confess`, `␣confession`, `␣confessed`, `坦白` | 2 | L52-58; most at L52 (1), L57 (1), L58 (1) |
| 2 | admit (admitting / acknowledging) | truth | `␣admits`, `承认`, `␣admitted`, `␣admitting`, `␣admit`, `␣acknowledge`, `␣acknowledged`, `␣acknowledges`, `承認`, `␣acknowledging`, `␣acknowledgment` | 12 | L35-58; most at L55 (10), L56 (8), L57 (7) |
| 2 | disclose (disclosing / revealing) | truth | `揭露`, `␣disclosed`, `␣disclosure`, `␣revealed`, `披露`, `揭示`, `揭` | 9 | L35-58; most at L35 (3), L36 (5), L37 (2) |
| 2 | inform (informing / telling (告知)) | unclear | `告知`, `被告知`, `请告知` | 48 | L35-58; most at L35 (27), L36 (16), L42 (12) |
| 2 | account for (account for / explain; also 'come clean' (交代)) | unclear | `交代` | 47 | L35-45; most at L35 (29), L36 (37), L37 (28) |
| 2 | clarify (clarifying) | unclear | `澄清` | 1 | L36-36; most at L36 (1) |
| 2 | refuse (refusing) | unclear | `拒绝` | 1 | L41-44; most at L41 (1), L42 (1), L44 (1) |
| 2 | guilt (guilt) | unclear | `␣guilt` | 1 | L53-54; most at L53 (1), L54 (1) |
| 2 | wrongdoing (wrongdoing) | lie | `␣wrongdoing` | 2 | L52-56; most at L52 (1), L53 (1), L56 (1) |
| 2 | ethics (ethics / morality (right and wrong)) | unclear | `是非`, `␣ethical`, `伦理`, `␣ethics`, `道德`, `ethical`, `␣moral`, `␣morally` | 16 | L35-58; most at L40 (9), L41 (7), L42 (6) |
| 2 | unethical (unethical) | lie | `␣unethical` | 4 | L51-58; most at L52 (3), L55 (3), L58 (3) |
| 2 | violate (violating a rule or instruction) | unclear | `违背`, `违`, `违规`, `违反`, `违法` | 43 | L35-54; most at L35 (26), L36 (12), L37 (18) |
| 2 | contradict (contradiction) | unclear | `矛盾`, `矛盾的`, `␣contradict`, `␣contradictory` | 32 | L35-56; most at L44 (19), L45 (17), L46 (20) |
| 2 | conflict (conflicting (claims or goals)) | unclear | `␣conflicting`, `␣conflict`, `␣conflicts` | 14 | L39-58; most at L47 (9), L48 (8), L53 (8) |
| 2 | loyalty (loyalty / faithfulness) | unclear | `␣loyalty`, `忠实`, `忠诚`, `忠诚度`, `忠于`, `␣loyal`, `忠`, `␣faithfully` | 22 | L35-58; most at L36 (7), L51 (9), L52 (7) |

## preans_slot3

| rep | family | side | members | visibility | layer profile |
|---|---|---|---|---|---|
| 1 | hide (hiding, being hidden) | lie | `:hidden` | 1 | L44-44; most at L44 (1) |
| 1 | cover up (covering up, masking) | lie | `蔽` | 74 | L43-49; most at L45 (72), L46 (41), L47 (5) |
| 1 | secret (secret, secrecy, in secret) | lie | `_secret`, `秘密` | 5 | L47-50; most at L47 (2), L50 (4) |
| 1 | fictional (fictional, made-up setting) | unclear | `fiction` | 6 | L45-46; most at L45 (1), L46 (6) |
| 1 | clarify (clarifying) | unclear | `澄清` | 13 | L51-52; most at L51 (13), L52 (1) |
| 1 | refuse (refusing, declining) | unclear | `␣refusal`, `拒`, `拒不`, `拒绝` | 126 | L38-53; most at L47 (121), L48 (80), L51 (31) |
| 1 | cannot (cannot, unable (refusal stance)) | unclear | `无法`, `␣cannot`, `我无法`, `不能被`, `不能`, `都无法`, `我不能`, `是无法`, `不能作为`, `cannot`, `是不能`, `也不能`, `都不能`, `根本无法`, `Cannot` | 198 | L35-58; most at L37 (151), L40 (125), L45 (163) |
| 1 | impossible (impossible) | unclear | `␣impossible`, `␣Impossible`, `Impossible` | 59 | L48-53; most at L49 (19), L50 (55), L51 (25) |
| 1 | euphemistic (tactful, indirect wording) | unclear | `婉` | 14 | L41-42; most at L41 (7), L42 (13) |
| 1 | ethics (ethics, morality, right and wrong) | unclear | `的道德`, `伦理`, `␣ethical`, `␣morally` | 4 | L42-58; most at L44 (2), L49 (2), L58 (3) |
| 1 | conscience (conscience) | unclear | `良心` | 2 | L56-56; most at L56 (2) |
| 1 | lawful (lawful, law-abiding) | unclear | `守法`, `␣legally`, `依法`, `/legal` | 170 | L35-51; most at L42 (41), L43 (162), L48 (43) |
| 1 | apologize (apology, sorry) | unclear | `抱歉`, `Sorry`, `␣apologize`, `␣sorry`, `␣Sorry` | 154 | L48-58; most at L54 (153), L56 (96), L57 (101) |
| 1 | firm (firmly, resolutely) | unclear | `坚决` | 110 | L35-47; most at L36 (109), L37 (71), L38 (27) |
| 2 | conceal (the act of hiding / covering up) | lie | `蔽` | 74 | L43-49; most at L45 (72), L46 (41), L47 (5) |
| 2 | hidden (being hidden / not disclosed (state)) | lie | `:hidden` | 1 | L44-44; most at L44 (1) |
| 2 | secret (something kept secret / done in secret) | lie | `_secret`, `秘密` | 5 | L47-50; most at L47 (2), L50 (4) |
| 2 | euphemism (tactful / euphemistic wording) | unclear | `婉` | 14 | L41-42; most at L41 (7), L42 (13) |
| 2 | fictional (fictional / made-up setting) | unclear | `fiction` | 6 | L45-46; most at L45 (1), L46 (6) |
| 2 | disclose (disclosing / revealing) | truth | `公布` | 232 | L39-47; most at L43 (229), L44 (232), L45 (142) |
| 2 | clarify (clarifying) | unclear | `澄清` | 13 | L51-52; most at L51 (13), L52 (1) |
| 2 | refuse (refusing) | unclear | `␣refusal`, `拒绝` | 126 | L38-53; most at L47 (121), L48 (80), L51 (31) |
| 2 | sorry (apology) | unclear | `抱歉`, `Sorry`, `␣apologize`, `␣sorry`, `␣Sorry` | 154 | L48-58; most at L54 (153), L56 (96), L57 (101) |
| 2 | ethics (ethics / morality (right and wrong)) | unclear | `的道德`, `伦理`, `␣ethical`, `␣morally` | 4 | L42-58; most at L44 (2), L49 (2), L58 (3) |

## preans_slot4

| rep | family | side | members | visibility | layer profile |
|---|---|---|---|---|---|
| 1 | deceive (the act of deceiving) | lie | `欺骗`, `␣deception` | 29 | L35-39; most at L36 (14), L37 (22), L38 (26) |
| 1 | hide (hiding, being hidden) | lie | `␣hidden`, `hidden`, `:hidden` | 5 | L47-52; most at L47 (5), L48 (3), L49 (1) |
| 1 | conceal (concealing (withholding the truth from someone)) | lie | `隐瞒`, `瞒` | 27 | L35-50; most at L38 (23), L39 (16), L40 (17) |
| 1 | cover up (covering up, masking) | lie | `掩` | 4 | L39-40; most at L39 (3), L40 (1) |
| 1 | secret (secret, secrecy, in secret) | lie | `秘密`, `保密`, `secret` | 22 | L35-50; most at L47 (13), L48 (12), L50 (12) |
| 1 | outward appearance (on the surface, outwardly) | unclear | `外表`, `表面上` | 22 | L36-51; most at L45 (12), L46 (19), L47 (11) |
| 1 | deliberate (on purpose, intentionally) | unclear | `␣intentionally`, `␣deliberately` | 1 | L36-38; most at L36 (1), L37 (1), L38 (1) |
| 1 | knowingly (knowing the truth, knowingly) | unclear | `明知` | 23 | L35-44; most at L35 (22), L36 (13), L44 (2) |
| 1 | fictional (fictional, made-up setting) | unclear | `虚构`, `fiction` | 7 | L35-46; most at L36 (4), L37 (3), L41 (3) |
| 1 | honest (honesty) | truth | `诚实`, `诚`, `诚信`, `␣honest`, `坦诚` | 132 | L35-48; most at L36 (66), L37 (102), L38 (93) |
| 1 | dishonest (dishonesty) | lie | `␣dishonest` | 4 | L35-39; most at L36 (3), L37 (4), L38 (4) |
| 1 | integrity (integrity, uprightness) | truth | `正直` | 1 | L36-36; most at L36 (1) |
| 1 | admit (admitting) | truth | `承认` | 67 | L35-48; most at L35 (59), L37 (38), L40 (35) |
| 1 | acknowledge (acknowledging) | truth | `␣acknowledge`, `␣acknowledgment`, `␣acknowledging` | 8 | L36-45; most at L36 (5), L39 (3), L44 (5) |
| 1 | confess (confessing) | truth | `坦白` | 10 | L35-38; most at L35 (4), L36 (6), L37 (7) |
| 1 | deny (denying, negating) | lie | `否定`, `否认` | 27 | L35-47; most at L41 (24), L42 (19), L43 (20) |
| 1 | refuse (refusing, declining) | unclear | `␣refusal`, `␣refuse`, `␣refused`, `拒绝` | 8 | L50-57; most at L50 (7), L52 (1), L53 (1) |
| 1 | cannot (cannot, unable (refusal stance)) | unclear | `␣cannot`, `无法`, `我无法`, `我不能`, `cannot`, `不能`, `Cannot`, `␣Cannot`, `是无法`, `是不能` | 59 | L49-58; most at L50 (40), L52 (47), L54 (50) |
| 1 | ethics (ethics, morality, right and wrong) | unclear | `是非` | 3 | L35-36; most at L35 (1), L36 (3) |
| 1 | violate (violating (rules, instructions, principles)) | unclear | `违反`, `违反了` | 17 | L35-47; most at L35 (15), L46 (4), L47 (3) |
| 1 | lawful (lawful, law-abiding) | unclear | `合法`, `␣legally`, `依法` | 16 | L43-52; most at L49 (6), L50 (7), L52 (3) |
| 1 | contradict (contradiction) | unclear | `矛盾`, `␣contradiction` | 3 | L38-50; most at L38 (1), L41 (2), L42 (1) |
| 1 | apologize (apology, sorry) | unclear | `抱歉`, `对不起`, `Sorry`, `␣sorry` | 16 | L35-57; most at L35 (3), L54 (9), L57 (3) |
| 1 | comply (complying, obeying) | unclear | `␣adher`, `遵循` | 9 | L50-54; most at L50 (4), L52 (4), L53 (3) |
| 1 | protect (protecting, safeguarding (an interest)) | unclear | `为了保护` | 19 | L48-51; most at L48 (1), L50 (19), L51 (1) |
| 1 | firm (firmly, resolutely) | unclear | `坚决`, `␣firmly` | 14 | L36-50; most at L42 (3), L43 (7), L50 (9) |
| 2 | deceive (the act of deceiving) | lie | `欺骗`, `␣deception` | 29 | L35-39; most at L36 (14), L37 (22), L38 (26) |
| 2 | conceal (the act of hiding / covering up) | lie | `隐瞒`, `掩`, `瞒` | 28 | L35-50; most at L38 (23), L39 (19), L40 (17) |
| 2 | hidden (being hidden / not disclosed (state)) | lie | `␣hidden`, `隐`, `hidden`, `:hidden` | 9 | L45-52; most at L45 (5), L47 (5), L48 (3) |
| 2 | secret (something kept secret / done in secret) | lie | `秘密`, `secret` | 15 | L47-50; most at L47 (12), L48 (11), L50 (12) |
| 2 | confidential (confidential / kept private) | unclear | `保密` | 11 | L35-48; most at L39 (8), L40 (8), L44 (7) |
| 2 | dishonest (dishonest) | lie | `␣dishonest` | 4 | L35-39; most at L36 (3), L37 (4), L38 (4) |
| 2 | deny (denying) | lie | `否定`, `否认` | 27 | L35-47; most at L41 (24), L42 (19), L43 (20) |
| 2 | surface (on the surface / outward appearance (ostensibly)) | unclear | `外表`, `表面上` | 22 | L36-51; most at L45 (12), L46 (19), L47 (11) |
| 2 | fictional (fictional / made-up setting) | unclear | `虚构`, `fiction` | 7 | L35-46; most at L36 (4), L37 (3), L41 (3) |
| 2 | intentional (doing something on purpose) | unclear | `␣intentionally`, `␣deliberately` | 1 | L36-38; most at L36 (1), L37 (1), L38 (1) |
| 2 | knowingly (knowing full well (明知)) | unclear | `明知` | 23 | L35-44; most at L35 (22), L36 (13), L44 (2) |
| 2 | truth (the truth) | truth | `␣truth`, `真相`, `实话` | 24 | L35-41; most at L35 (24), L38 (2), L40 (1) |
| 2 | fact (fact / reality) | unclear | `事实`, `根据实际情况` | 6 | L40-50; most at L41 (3), L43 (3), L44 (2) |
| 2 | honest (honest / honesty) | truth | `诚`, `␣honest` | 70 | L35-46; most at L37 (44), L38 (56), L40 (18) |
| 2 | integrity (integrity / uprightness) | truth | `诚信`, `正直` | 57 | L35-46; most at L35 (24), L40 (23), L41 (32) |
| 2 | candid (candid / frank) | truth | `坦诚` | 3 | L38-43; most at L38 (2), L42 (2), L43 (1) |
| 2 | confess (confessing / coming clean) | truth | `坦白` | 10 | L35-38; most at L35 (4), L36 (6), L37 (7) |
| 2 | admit (admitting / acknowledging) | truth | `承认`, `␣acknowledge`, `␣acknowledgment`, `␣acknowledging` | 67 | L35-48; most at L35 (59), L37 (38), L40 (35) |
| 2 | refuse (refusing) | unclear | `␣refusal`, `␣refuse`, `␣refused`, `拒绝` | 8 | L50-57; most at L50 (7), L52 (1), L53 (1) |
| 2 | sorry (apology) | unclear | `抱歉`, `对不起`, `␣sorry`, `Sorry` | 16 | L35-57; most at L35 (3), L54 (9), L57 (3) |
| 2 | ethics (ethics / morality (right and wrong)) | unclear | `是非` | 3 | L35-36; most at L35 (1), L36 (3) |
| 2 | violate (violating a rule or instruction) | unclear | `违反`, `违反了` | 17 | L35-47; most at L35 (15), L46 (4), L47 (3) |
| 2 | contradict (contradiction) | unclear | `矛盾`, `␣contradiction` | 3 | L38-50; most at L38 (1), L41 (2), L42 (1) |

## Replicate overlap

For each replicate-1 family, the replicate-2 family at the same position sharing the most members.

| position | rep-1 family | best rep-2 family | Jaccard of member ids | only in rep 1 | only in rep 2 |
|---|---|---|---|---|---|
| preans_slot0 | clarify | clarify | 1.00 | — | — |
| preans_slot0 | deny | deny | 1.00 | — | — |
| preans_slot0 | cannot | — | 0 | all | — |
| preans_slot0 | ethics | ethics | 1.00 | — | — |
| preans_slot0 | violate | violate | 1.00 | — | — |
| preans_slot0 | lawful | — | 0 | all | — |
| preans_slot0 | despicable | — | 0 | all | — |
| preans_slot1 | deceive | deceive | 1.00 | — | — |
| preans_slot1 | trick | trick | 1.00 | — | — |
| preans_slot1 | hide | hidden | 0.41 | `隐藏`, `隱藏`, `隐藏在`, `隐藏着`, `hide`, `␣hiding`, `-hide`, `隐匿` | `隐`, `隐秘` |
| preans_slot1 | conceal | conceal | 0.20 | — | `隐藏`, `隱藏`, `隠`, `掩盖`, `遮`, `隐藏着`, `隐藏在`, `掩饰`, `藏着`, `隐匿`, `hide`, `-hide` |
| preans_slot1 | cover up | conceal | 0.13 | — | `隐藏`, `隐瞒`, `隱藏`, `隠`, `␣conceal`, `␣concealed`, `遮`, `隐藏着`, `隐藏在`, `藏着`, `隐匿`, `hide`, `-hide` |
| preans_slot1 | suppress | — | 0 | all | — |
| preans_slot1 | secret | secret | 0.75 | `保密`, `隐秘`, `␣confidential` | `私下` |
| preans_slot1 | private | secret | 0.07 | `␣private`, `␣privately` | `␣secret`, `secret`, `暗中`, `秘密`, `Secret`, `␣secretly`, `_secret`, `␣Secret`, `的秘密`, `-secret`, `.secret`, `.Secret` |
| preans_slot1 | internal | — | 0 | all | — |
| preans_slot1 | outward appearance | surface | 1.00 | — | — |
| preans_slot1 | official line | talking points | 1.00 | — | — |
| preans_slot1 | deliberate | intentional | 1.00 | — | — |
| preans_slot1 | knowingly | knowingly | 0.33 | `知情`, `␣knowing` | — |
| preans_slot1 | fictional | fictional | 0.83 | `␣fict` | — |
| preans_slot1 | hypothetical | — | 0 | all | — |
| preans_slot1 | fabricate | fabricate | 0.50 | `␣invent` | — |
| preans_slot1 | fake | fake | 0.50 | — | `虚假`, `␣misinformation` |
| preans_slot1 | pretend | pretend | 1.00 | — | — |
| preans_slot1 | misinformation | fake | 0.25 | — | `fake`, `␣fake`, `虚假` |
| preans_slot1 | honest | honest | 0.50 | `诚实`, `诚信`, `坦诚` | — |
| preans_slot1 | integrity | integrity | 0.67 | — | `诚信` |
| preans_slot1 | loyal | loyalty | 0.83 | — | `忠实` |
| preans_slot1 | faithful | loyalty | 0.17 | — | `␣loyalty`, `忠诚`, `忠于`, `忠诚度`, `␣loyal` |
| preans_slot1 | admit | admit | 0.17 | — | `␣acknowledging`, `␣acknowledge`, `␣acknowledges`, `␣acknowledged`, `␣acknowledgment` |
| preans_slot1 | acknowledge | admit | 0.83 | — | `承认` |
| preans_slot1 | disclose | disclose | 1.00 | — | — |
| preans_slot1 | inform | inform | 1.00 | — | — |
| preans_slot1 | deny | deny | 1.00 | — | — |
| preans_slot1 | refuse | refuse | 0.53 | `拒`, `拒絕`, `拒不`, `␣declined`, `␣decline`, `␣declining`, `␣declines` | — |
| preans_slot1 | cannot | — | 0 | all | — |
| preans_slot1 | evade | evade | 0.11 | `␣avoid`, `␣avoiding`, `␣avoided`, `␣Avoid`, `avoid`, `Avoid`, `␣avoids` | `规避` |
| preans_slot1 | euphemistic | euphemism | 1.00 | — | — |
| preans_slot1 | ethics | ethics | 1.00 | — | — |
| preans_slot1 | unethical | unethical | 1.00 | — | — |
| preans_slot1 | conscience | — | 0 | all | — |
| preans_slot1 | violate | violate | 1.00 | — | — |
| preans_slot1 | lawful | — | 0 | all | — |
| preans_slot1 | contradict | contradict | 0.83 | `␣contrad` | — |
| preans_slot1 | conflict | conflict | 1.00 | — | — |
| preans_slot1 | manipulate | manipulate | 1.00 | — | — |
| preans_slot1 | pander | — | 0 | all | — |
| preans_slot1 | embellish | — | 0 | all | — |
| preans_slot1 | comply | — | 0 | all | — |
| preans_slot1 | protect | — | 0 | all | — |
| preans_slot1 | role-play | role-play | 0.33 | `␣persona`, `␣Persona`, `␣personas`, `persona`, `Persona`, `␣Personas` | — |
| preans_slot1 | firm | — | 0 | all | — |
| preans_slot2 | deceive | deceive | 0.86 | — | `␣deceit` |
| preans_slot2 | fraud | fraud | 0.60 | — | `␣fraud`, `␣fraudulent` |
| preans_slot2 | mislead | mislead | 1.00 | — | — |
| preans_slot2 | trick | trick | 1.00 | — | — |
| preans_slot2 | hide | conceal | 0.32 | `␣hidden`, `隐藏的`, `␣hiding`, `-hidden`, `hidden`, `␣Hidden`, `:hidden`, `␣hid` | `隐瞒`, `掩盖`, `␣conceal`, `掩`, `␣masking`, `瞒`, `␣concealed`, `遮盖`, `掩饰`, `遮掩`, `遮`, `␣masks`, `遮蔽`, `掩护`, `藏着` |
| preans_slot2 | conceal | conceal | 0.15 | — | `掩盖`, `隐藏`, `掩`, `␣masking`, `隐藏着`, `遮盖`, `␣hide`, `掩饰`, `隐蔽`, `hide`, `Hide`, `␣hides`, `遮掩`, `遮`, `-hide`, `_hide`, `␣masks`, `遮蔽`, `掩护`, `藏着`, `.hide`, `␣Hide` |
| preans_slot2 | cover up | conceal | 0.27 | `␣cover`, `cover`, `␣Cover`, `Cover`, `␣covering`, `COVER`, `-cover` | `隐瞒`, `隐藏`, `␣conceal`, `瞒`, `隐藏着`, `␣concealed`, `␣hide`, `隐蔽`, `hide`, `Hide`, `␣hides`, `遮`, `-hide`, `_hide`, `藏着`, `.hide`, `␣Hide` |
| preans_slot2 | suppress | — | 0 | all | — |
| preans_slot2 | secret | secret | 0.65 | `机密`, `保密`, `␣confidential`, `␣confidentiality`, `隐秘`, `␣Confidential` | `私下` |
| preans_slot2 | private | confidential | 0.05 | `私下`, `␣private`, `␣privately`, `␣Private`, `private`, `Private`, `.private`, `PRIVATE`, `/private`, `私人`, `(private`, `-private`, `/Private`, `,private`, `私自` | `机密`, `保密`, `␣confidential`, `␣confidentiality`, `␣Confidential` |
| preans_slot2 | internal | — | 0 | all | — |
| preans_slot2 | outward appearance | surface | 0.67 | `对外` | — |
| preans_slot2 | official line | talking points | 1.00 | — | — |
| preans_slot2 | deliberate | intentional | 1.00 | — | — |
| preans_slot2 | knowingly | knowingly | 0.17 | `知情`, `␣knowing`, `␣Knowing`, `␣knowingly`, `Knowing` | — |
| preans_slot2 | fictional | fictional | 0.86 | `␣fict` | — |
| preans_slot2 | hypothetical | — | 0 | all | — |
| preans_slot2 | fabricate | fabricate | 0.80 | `␣invented` | — |
| preans_slot2 | fake | fake | 0.57 | — | `虚假`, `␣misinformation`, `虚假信息` |
| preans_slot2 | pretend | pretend | 0.80 | — | `␣disguised` |
| preans_slot2 | misinformation | fake | 0.29 | — | `虚假`, `fake`, `␣fake`, `Fake`, `伪` |
| preans_slot2 | honest | honest | 0.50 | `诚实`, `诚信`, `坦诚` | — |
| preans_slot2 | loyal | loyalty | 0.75 | — | `忠实`, `␣faithfully` |
| preans_slot2 | faithful | loyalty | 0.25 | — | `␣loyalty`, `忠诚`, `忠诚度`, `忠于`, `␣loyal`, `忠` |
| preans_slot2 | admit | admit | 0.55 | — | `␣acknowledge`, `␣acknowledged`, `␣acknowledges`, `␣acknowledging`, `␣acknowledgment` |
| preans_slot2 | acknowledge | admit | 0.45 | — | `␣admits`, `承认`, `␣admitted`, `␣admitting`, `␣admit`, `承認` |
| preans_slot2 | confess | confess | 1.00 | — | — |
| preans_slot2 | disclose | disclose | 0.88 | `透露` | — |
| preans_slot2 | undisclosed | hidden | 0.11 | — | `␣hidden`, `隐藏的`, `-hidden`, `␣Hidden`, `hidden`, `:hidden`, `隐秘`, `隐` |
| preans_slot2 | transparent | transparency | 1.00 | — | — |
| preans_slot2 | inform | inform | 0.27 | `␣tell`, `␣tells`, `␣telling`, `Tell`, `␣inform`, `␣Tell`, `␣informed`, `inform` | — |
| preans_slot2 | clarify | clarify | 1.00 | — | — |
| preans_slot2 | deny | deny | 1.00 | — | — |
| preans_slot2 | refuse | refuse | 1.00 | — | — |
| preans_slot2 | cannot | — | 0 | all | — |
| preans_slot2 | evade | evade | 0.25 | `␣avoid`, `␣avoidance` | `规避` |
| preans_slot2 | euphemistic | euphemism | 1.00 | — | — |
| preans_slot2 | ethics | ethics | 1.00 | — | — |
| preans_slot2 | unethical | unethical | 1.00 | — | — |
| preans_slot2 | violate | violate | 0.80 | — | `违法` |
| preans_slot2 | illegal | violate | 0.17 | `␣illegal` | `违背`, `违`, `违规`, `违反` |
| preans_slot2 | contradict | contradict | 0.80 | `␣contrad` | — |
| preans_slot2 | conflict | conflict | 1.00 | — | — |
| preans_slot2 | guilt | guilt | 1.00 | — | — |
| preans_slot2 | wrongdoing | wrongdoing | 1.00 | — | — |
| preans_slot2 | manipulate | manipulate | 1.00 | — | — |
| preans_slot2 | scheme | — | 0 | all | — |
| preans_slot2 | pander | — | 0 | all | — |
| preans_slot2 | embellish | — | 0 | all | — |
| preans_slot2 | comply | — | 0 | all | — |
| preans_slot2 | protect | — | 0 | all | — |
| preans_slot2 | role-play | role-play | 0.38 | `␣persona`, `␣personas`, `␣Persona`, `persona`, `Persona` | — |
| preans_slot2 | firm | — | 0 | all | — |
| preans_slot2 | selfish | — | 0 | all | — |
| preans_slot2 | discovered | — | 0 | all | — |
| preans_slot3 | hide | hidden | 1.00 | — | — |
| preans_slot3 | cover up | conceal | 1.00 | — | — |
| preans_slot3 | secret | secret | 1.00 | — | — |
| preans_slot3 | fictional | fictional | 1.00 | — | — |
| preans_slot3 | clarify | clarify | 1.00 | — | — |
| preans_slot3 | refuse | refuse | 0.50 | `拒`, `拒不` | — |
| preans_slot3 | cannot | — | 0 | all | — |
| preans_slot3 | impossible | — | 0 | all | — |
| preans_slot3 | euphemistic | euphemism | 1.00 | — | — |
| preans_slot3 | ethics | ethics | 1.00 | — | — |
| preans_slot3 | conscience | — | 0 | all | — |
| preans_slot3 | lawful | — | 0 | all | — |
| preans_slot3 | apologize | sorry | 1.00 | — | — |
| preans_slot3 | firm | — | 0 | all | — |
| preans_slot4 | deceive | deceive | 1.00 | — | — |
| preans_slot4 | hide | hidden | 0.75 | — | `隐` |
| preans_slot4 | conceal | conceal | 0.67 | — | `掩` |
| preans_slot4 | cover up | conceal | 0.33 | — | `隐瞒`, `瞒` |
| preans_slot4 | secret | secret | 0.67 | `保密` | — |
| preans_slot4 | outward appearance | surface | 1.00 | — | — |
| preans_slot4 | deliberate | intentional | 1.00 | — | — |
| preans_slot4 | knowingly | knowingly | 1.00 | — | — |
| preans_slot4 | fictional | fictional | 1.00 | — | — |
| preans_slot4 | honest | honest | 0.40 | `诚实`, `诚信`, `坦诚` | — |
| preans_slot4 | dishonest | dishonest | 1.00 | — | — |
| preans_slot4 | integrity | integrity | 0.50 | — | `诚信` |
| preans_slot4 | admit | admit | 0.25 | — | `␣acknowledge`, `␣acknowledgment`, `␣acknowledging` |
| preans_slot4 | acknowledge | admit | 0.75 | — | `承认` |
| preans_slot4 | confess | confess | 1.00 | — | — |
| preans_slot4 | deny | deny | 1.00 | — | — |
| preans_slot4 | refuse | refuse | 1.00 | — | — |
| preans_slot4 | cannot | — | 0 | all | — |
| preans_slot4 | ethics | ethics | 1.00 | — | — |
| preans_slot4 | violate | violate | 1.00 | — | — |
| preans_slot4 | lawful | — | 0 | all | — |
| preans_slot4 | contradict | contradict | 1.00 | — | — |
| preans_slot4 | apologize | sorry | 1.00 | — | — |
| preans_slot4 | comply | — | 0 | all | — |
| preans_slot4 | protect | — | 0 | all | — |
| preans_slot4 | firm | — | 0 | all | — |

Replicate-2 families not the best match of any replicate-1 family: preans_slot1: confidential, preans_slot1: truth, preans_slot1: fact, preans_slot1: candid, preans_slot1: account for, preans_slot2: impersonate, preans_slot2: truth, preans_slot2: fact, preans_slot2: integrity, preans_slot2: candid, preans_slot2: account for, preans_slot3: disclose, preans_slot4: confidential, preans_slot4: truth, preans_slot4: fact, preans_slot4: candid

## Families whose name recurs at 3 or more positions

- acknowledge: preans_slot1, preans_slot2, preans_slot4
- admit: preans_slot1, preans_slot2, preans_slot4
- candid: preans_slot1, preans_slot2, preans_slot4
- cannot: preans_slot0, preans_slot1, preans_slot2, preans_slot3, preans_slot4
- clarify: preans_slot0, preans_slot2, preans_slot3
- comply: preans_slot1, preans_slot2, preans_slot4
- conceal: preans_slot1, preans_slot2, preans_slot3, preans_slot4
- confidential: preans_slot1, preans_slot2, preans_slot4
- contradict: preans_slot1, preans_slot2, preans_slot4
- cover up: preans_slot1, preans_slot2, preans_slot3, preans_slot4
- deceive: preans_slot1, preans_slot2, preans_slot4
- deliberate: preans_slot1, preans_slot2, preans_slot4
- deny: preans_slot0, preans_slot1, preans_slot2, preans_slot4
- disclose: preans_slot1, preans_slot2, preans_slot3
- ethics: preans_slot0, preans_slot1, preans_slot2, preans_slot3, preans_slot4
- euphemism: preans_slot1, preans_slot2, preans_slot3
- euphemistic: preans_slot1, preans_slot2, preans_slot3
- fact: preans_slot1, preans_slot2, preans_slot4
- fictional: preans_slot1, preans_slot2, preans_slot3, preans_slot4
- firm: preans_slot1, preans_slot2, preans_slot3, preans_slot4
- hidden: preans_slot1, preans_slot2, preans_slot3, preans_slot4
- hide: preans_slot1, preans_slot2, preans_slot3, preans_slot4
- honest: preans_slot1, preans_slot2, preans_slot4
- integrity: preans_slot1, preans_slot2, preans_slot4
- intentional: preans_slot1, preans_slot2, preans_slot4
- knowingly: preans_slot1, preans_slot2, preans_slot4
- lawful: preans_slot0, preans_slot1, preans_slot3, preans_slot4
- outward appearance: preans_slot1, preans_slot2, preans_slot4
- protect: preans_slot1, preans_slot2, preans_slot4
- refuse: preans_slot1, preans_slot2, preans_slot3, preans_slot4
- secret: preans_slot1, preans_slot2, preans_slot3, preans_slot4
- surface: preans_slot1, preans_slot2, preans_slot4
- truth: preans_slot1, preans_slot2, preans_slot4
- violate: preans_slot0, preans_slot1, preans_slot2, preans_slot4

## Candidate opposite pairs (same position, lie side vs truth side, antonym words in the names or glosses; merged list)

- preans_slot1: conceal / disclose
- preans_slot1: deceive / honest
- preans_slot1: deny / admit
- preans_slot1: evade / admit
- preans_slot1: hidden / admit
- preans_slot1: hidden / disclose
- preans_slot1: hide / admit
- preans_slot1: hide / disclose
- preans_slot2: conceal / disclose
- preans_slot2: conceal / transparent
- preans_slot2: cover up / transparent
- preans_slot2: deceive / honest
- preans_slot2: deny / admit
- preans_slot2: deny / confess
- preans_slot2: evade / admit
- preans_slot2: hidden / admit
- preans_slot2: hidden / confess
- preans_slot2: hidden / disclose
- preans_slot2: hide / admit
- preans_slot2: hide / confess
- preans_slot2: hide / disclose
- preans_slot2: mislead / candid
- preans_slot2: mislead / truth
- preans_slot3: hide / disclose
- preans_slot4: deceive / honest
- preans_slot4: deny / admit
- preans_slot4: deny / confess
- preans_slot4: dishonest / honest
- preans_slot4: hide / admit
- preans_slot4: hide / confess

Merged candidate list: `qwen3_6_27b_LL_Q7_ab_preans_merged.json` (177 families; replicate-2 families sharing at least half
their members with a replicate-1 family at the same position are folded into it).
