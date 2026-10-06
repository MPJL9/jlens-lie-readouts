# Family report: qwen3.6-27b, logit lens, band 35-58, part Q1_bare, group think

Written by `scripts/family_report.py` from `qwen3_6_27b_LL_Q1_bare_think_rep1.json` and `_rep2.json` (prompt
`prompts/family_generation.md`). Visibility = build-split scenario transcripts (of 233) in which
at least one member is present at the position within the band. Layer profile = band layers where
the family is present in at least one transcript, and the three layers with the most transcripts
(description only; scoring uses the whole band).

## think_slot0

| rep | family | side | members | visibility | layer profile |
|---|---|---|---|---|---|
| 1 | sincere (sincerity, genuine feeling) | truth | `真诚`, `真情` | 28 | L35-50; most at L35 (19), L36 (9), L50 (7) |
| 1 | clarify (clarifying, setting the record straight) | unclear | `澄清`, `␣clarification` | 181 | L36-49; most at L46 (84), L47 (23), L48 (179) |
| 1 | violation (breaking a rule) | unclear | `违规` | 81 | L42-45; most at L42 (16), L43 (76), L45 (27) |
| 1 | reveal (exposing, uncovering) | truth | `揭` | 8 | L42-43; most at L42 (1), L43 (8) |
| 1 | sensitive (a sensitive matter) | unclear | `_sensitive`, `敏感` | 20 | L45-52; most at L47 (3), L49 (16), L51 (11) |
| 1 | compliance (complying with rules) | unclear | `合规` | 7 | L42-48; most at L42 (4), L48 (3) |
| 1 | legal issue (a legal problem) | unclear | `法律问题` | 1 | L49-49; most at L49 (1) |
| 1 | guilt (guilt, crime) | unclear | `罪的` | 3 | L36-36; most at L36 (3) |
| 1 | plausible (plausible-sounding) | unclear | `␣plausible` | 72 | L46-53; most at L46 (6), L50 (6), L53 (69) |
| 1 | clever (clever, quick-witted) | unclear | `␣clever`, `伶俐` | 170 | L41-53; most at L43 (135), L44 (141), L50 (73) |
| 2 | clarify (making the matter clear) | unclear | `澄清`, `␣clarification` | 181 | L36-49; most at L46 (84), L47 (23), L48 (179) |
| 2 | violation (breaking the rules) | unclear | `违规` | 81 | L42-45; most at L42 (16), L43 (76), L45 (27) |
| 2 | sincere (sincere, genuine) | truth | `真诚` | 25 | L35-47; most at L35 (19), L36 (9), L44 (3) |
| 2 | compliance (following the rules) | unclear | `合规` | 7 | L42-48; most at L42 (4), L48 (3) |
| 2 | guilt (crime, guilt) | unclear | `罪的` | 3 | L36-36; most at L36 (3) |

## think_slot1

| rep | family | side | members | visibility | layer profile |
|---|---|---|---|---|---|
| 1 | disclose (disclosing everything (交底)) | truth | `交底` | 33 | L39-41; most at L39 (33), L40 (12), L41 (1) |
| 1 | secretly (quietly, stealthily) | unclear | `悄`, `悄悄的` | 88 | L36-50; most at L41 (45), L46 (59), L49 (19) |
| 1 | without permission (acting without permission) | unclear | `未经允许` | 74 | L46-55; most at L46 (17), L47 (13), L48 (70) |
| 1 | violation (breaking a rule) | unclear | `␣violated` | 2 | L47-49; most at L47 (1), L49 (1) |
| 1 | promise (promising) | unclear | `许诺` | 73 | L56-58; most at L56 (35), L57 (73), L58 (12) |
| 1 | neutral (neutrality) | unclear | `␣neutrality` | 2 | L58-58; most at L58 (2) |
| 2 | disclose (laying out the full facts) | truth | `交底` | 33 | L39-41; most at L39 (33), L40 (12), L41 (1) |
| 2 | unauthorized (without permission) | unclear | `未经允许` | 74 | L46-55; most at L46 (17), L47 (13), L48 (70) |

## think_slot2

| rep | family | side | members | visibility | layer profile |
|---|---|---|---|---|---|
| 1 | sorry (apologizing) | unclear | `抱歉`, `对不起`, `Sorry` | 70 | L49-58; most at L54 (70), L57 (26), L58 (20) |
| 1 | candid (candid, frank) | truth | `坦诚` | 12 | L48-48; most at L48 (12) |
| 1 | honest (honesty) | truth | `␣honestly`, `诚`, `誠` | 4 | L53-58; most at L53 (3), L57 (3), L58 (3) |
| 1 | upright (upright, of integrity) | truth | `正直` | 3 | L53-53; most at L53 (3) |
| 1 | ethics (ethics, ethical) | unclear | `␣ethics`, `␣ethical`, `职业道德` | 128 | L41-48; most at L44 (40), L45 (117), L48 (47) |
| 1 | legal (legality, legally) | unclear | `在法律`, `␣legally`, `/legal`, `␣legality` | 163 | L45-52; most at L48 (162), L49 (71), L51 (16) |
| 1 | breach (breach, violation) | unclear | `␣breach`, `␣breaches`, `␣breached` | 59 | L47-48; most at L47 (22), L48 (56) |
| 1 | forged (forged, faked) | lie | `␣forged`, `forge` | 47 | L35-49; most at L35 (45), L47 (2), L49 (1) |
| 1 | stance (one's position (立场)) | unclear | `立场` | 126 | L36-49; most at L38 (43), L40 (112), L43 (62) |
| 1 | neutral (neutral) | unclear | `中立` | 91 | L35-36; most at L35 (91), L36 (1) |
| 1 | sensitive (a sensitive matter) | unclear | `敏感`, `␣sensitive` | 46 | L35-40; most at L35 (4), L36 (46), L37 (3) |
| 1 | cannot (I cannot / unable to) | unclear | `我不能`, `我无法`, `不能`, `不能说`, `可不能` | 177 | L48-58; most at L51 (121), L52 (164), L53 (157) |
| 1 | not fully (cannot fully) | unclear | `不能完全` | 165 | L51-58; most at L51 (53), L52 (159), L55 (106) |
| 1 | not do (not carrying out / not doing) | unclear | `不进行`, `不做` | 206 | L44-48; most at L45 (200), L46 (182), L47 (137) |
| 1 | not reply (not answering) | unclear | `不回` | 44 | L49-51; most at L49 (15), L50 (6), L51 (36) |
| 1 | refuse (refusing) | unclear | `拒`, `拒不` | 30 | L49-55; most at L49 (20), L50 (20), L55 (1) |
| 1 | defense (defense) | unclear | `-defense`, `␣defense` | 97 | L41-58; most at L56 (5), L57 (55), L58 (97) |
| 1 | direct (direct, straightforward) | unclear | `直接的` | 31 | L37-40; most at L37 (5), L39 (2), L40 (28) |
| 1 | clever (clever, quick-witted) | unclear | `伶俐` | 31 | L36-41; most at L36 (30), L37 (16), L41 (1) |
| 1 | innocent (innocent, clean record (清白)) | unclear | `清白` | 1 | L47-47; most at L47 (1) |
| 2 | cannot (I cannot / am unable to) | unclear | `我不能`, `不能完全`, `我无法`, `不能`, `不能说`, `可不能` | 204 | L48-58; most at L52 (197), L53 (158), L55 (138) |
| 2 | ethics (ethics, ethical) | unclear | `␣ethics`, `␣ethical`, `职业道德` | 128 | L41-48; most at L44 (40), L45 (117), L48 (47) |
| 2 | apology (saying sorry) | unclear | `抱歉`, `对不起`, `Sorry` | 70 | L49-58; most at L54 (70), L57 (26), L58 (20) |
| 2 | breach (breaking a duty or rule) | unclear | `␣breach`, `␣breaches`, `␣breached` | 59 | L47-48; most at L47 (22), L48 (56) |
| 2 | forge (faking, forging) | lie | `␣forged`, `forge` | 47 | L35-49; most at L35 (45), L47 (2), L49 (1) |
| 2 | refuse (refusing) | unclear | `拒`, `拒不` | 30 | L49-55; most at L49 (20), L50 (20), L55 (1) |
| 2 | candid (frank and open) | truth | `坦诚` | 12 | L48-48; most at L48 (12) |
| 2 | honest (honest, honesty) | truth | `␣honestly`, `诚`, `誠` | 4 | L53-58; most at L53 (3), L57 (3), L58 (3) |
| 2 | integrity (upright, principled) | truth | `正直` | 3 | L53-53; most at L53 (3) |

## think_slot3

| rep | family | side | members | visibility | layer profile |
|---|---|---|---|---|---|
| 1 | confess (coming clean, confessing (坦白)) | truth | `坦白` | 201 | L35-58; most at L35 (173), L43 (156), L46 (165) |
| 1 | candid (candid, frank) | truth | `坦诚` | 153 | L35-55; most at L35 (113), L46 (119), L51 (80) |
| 1 | honest (honesty) | truth | `诚`, `誠`, `诚实`, `␣honestly`, `␣honesty`, `␣honest`, `␣truthful` | 179 | L35-58; most at L43 (134), L45 (134), L46 (140) |
| 1 | sincere (sincerity) | truth | `␣sincerely`, `␣sincere`, `真诚`, `真诚的`, `诚恳`, `诚挚` | 39 | L35-57; most at L36 (21), L50 (18), L51 (23) |
| 1 | truth (the truth, true facts) | truth | `真相`, `实话`, `␣truth` | 66 | L35-46; most at L35 (65), L36 (14), L39 (1) |
| 1 | upright (upright, of integrity) | truth | `正直` | 18 | L35-50; most at L35 (7), L39 (4), L40 (5) |
| 1 | admit (admitting) | truth | `承认` | 99 | L35-51; most at L35 (63), L40 (61), L45 (56) |
| 1 | deny (denying) | lie | `否认` | 23 | L36-51; most at L39 (9), L42 (10), L50 (12) |
| 1 | sorry (apologizing) | unclear | `抱歉`, `对不起`, `␣apologize`, `␣apologies`, `道歉` | 165 | L35-56; most at L37 (148), L38 (136), L43 (131) |
| 1 | forgive (asking forgiveness) | unclear | `␣forgive` | 4 | L54-55; most at L54 (4), L55 (3) |
| 1 | ashamed (shame, guilt (愧)) | unclear | `愧` | 4 | L43-43; most at L43 (4) |
| 1 | guilt (guilt, crime) | unclear | `罪` | 7 | L35-36; most at L35 (7), L36 (1) |
| 1 | ethics (ethics, ethical) | unclear | `␣ethical`, `伦理`, `道德` | 62 | L35-43; most at L36 (36), L37 (35), L40 (61) |
| 1 | fake (fake, pseudo) | lie | `伪` | 26 | L35-41; most at L38 (16), L39 (22), L40 (6) |
| 1 | disguise (disguise, pretense) | lie | `伪装` | 1 | L35-41; most at L35 (1), L37 (1), L40 (1) |
| 1 | hide (covering up, concealing) | lie | `掩` | 8 | L36-46; most at L36 (3), L43 (5), L44 (2) |
| 1 | confidential (keeping confidential) | unclear | `保密`, `␣confidential` | 12 | L35-42; most at L35 (8), L36 (8), L37 (8) |
| 1 | privately (privately, in private) | unclear | `私下` | 12 | L35-37; most at L35 (6), L36 (11), L37 (2) |
| 1 | transparent (transparency) | truth | `␣transparency`, `透明`, `透明的` | 1 | L38-41; most at L38 (1), L39 (1), L40 (1) |
| 1 | public (making public, disclosing (公开)) | truth | `公开` | 10 | L35-38; most at L35 (10), L36 (2), L37 (5) |
| 1 | clarify (clarifying, setting the record straight) | unclear | `澄清`, `␣clarification` | 49 | L35-52; most at L42 (41), L43 (32), L46 (30) |
| 1 | misunderstanding (misunderstanding) | unclear | `误会` | 18 | L35-41; most at L35 (9), L36 (4), L37 (9) |
| 1 | objective (objective) | unclear | `客观`, `␣objectively` | 27 | L35-51; most at L35 (26), L36 (2), L51 (1) |
| 1 | compliance (complying with rules) | unclear | `合规` | 8 | L35-39; most at L35 (7), L36 (5), L37 (2) |
| 1 | fictional (fictional) | unclear | `␣fictional` | 9 | L35-43; most at L35 (8), L36 (9), L43 (1) |
| 1 | simulation (a simulation) | unclear | `␣simulation` | 6 | L35-42; most at L40 (2), L41 (3), L42 (2) |
| 1 | confident (confidence) | unclear | `␣confidently`, `␣confident` | 4 | L36-46; most at L36 (3), L43 (2), L44 (2) |
| 1 | cannot (I cannot / unable to) | unclear | `我不能`, `我无法`, `绝对不能` | 17 | L50-55; most at L50 (6), L51 (5), L52 (16) |
| 1 | refuse (refusing) | unclear | `拒绝` | 3 | L38-43; most at L38 (2), L41 (3), L43 (2) |
| 1 | not do (not doing) | unclear | `不做` | 1 | L39-46; most at L39 (1), L46 (1) |
| 1 | direct (direct, straightforward) | unclear | `直接的`, `直接` | 9 | L39-43; most at L40 (8), L41 (6), L42 (4) |
| 1 | promise (promising) | unclear | `Promise` | 1 | L35-35; most at L35 (1) |
| 2 | confess (coming clean, confessing) | truth | `坦白` | 201 | L35-58; most at L35 (173), L43 (156), L46 (165) |
| 2 | admit (admitting) | truth | `承认` | 99 | L35-51; most at L35 (63), L40 (61), L45 (56) |
| 2 | candid (frank and open) | truth | `坦诚` | 153 | L35-55; most at L35 (113), L46 (119), L51 (80) |
| 2 | honest (honest, honesty) | truth | `诚`, `诚实`, `实话`, `誠`, `␣honestly`, `␣honesty`, `␣honest`, `␣truthful` | 181 | L35-58; most at L43 (134), L45 (134), L46 (140) |
| 2 | sincere (sincere, genuine) | truth | `␣sincerely`, `真诚`, `诚恳`, `诚挚`, `真诚的`, `␣sincere` | 39 | L35-57; most at L36 (21), L50 (18), L51 (23) |
| 2 | integrity (upright, principled) | truth | `正直` | 18 | L35-50; most at L35 (7), L39 (4), L40 (5) |
| 2 | the truth (the real facts) | truth | `真相`, `␣truth` | 39 | L35-46; most at L35 (39), L39 (1), L42 (1) |
| 2 | transparency (being transparent) | truth | `␣transparency` | 1 | L38-41; most at L38 (1), L39 (1), L40 (1) |
| 2 | disclose (making public) | truth | `公开` | 10 | L35-38; most at L35 (10), L36 (2), L37 (5) |
| 2 | apology (saying sorry) | unclear | `抱歉`, `␣apologize`, `对不起`, `道歉`, `␣apologies` | 165 | L35-56; most at L37 (148), L38 (136), L43 (131) |
| 2 | forgive (asking or granting forgiveness) | unclear | `␣forgive` | 4 | L54-55; most at L54 (4), L55 (3) |
| 2 | deny (denying) | lie | `否认` | 23 | L36-51; most at L39 (9), L42 (10), L50 (12) |
| 2 | negate (negating, rejecting a claim) | unclear | `否定` | 110 | L35-58; most at L47 (64), L48 (68), L50 (99) |
| 2 | ethics (ethics, ethical) | unclear | `␣ethical`, `伦理`, `道德` | 62 | L35-43; most at L36 (36), L37 (35), L40 (61) |
| 2 | clarify (making the matter clear) | unclear | `澄清`, `␣clarification` | 49 | L35-52; most at L42 (41), L43 (32), L46 (30) |
| 2 | fake (fake, counterfeit) | lie | `伪` | 26 | L35-41; most at L38 (16), L39 (22), L40 (6) |
| 2 | disguise (disguising, pretending) | lie | `伪装` | 1 | L35-41; most at L35 (1), L37 (1), L40 (1) |
| 2 | lie (Japanese) (a lie) | lie | `嘘` | 1 | L57-58; most at L57 (1), L58 (1) |
| 2 | objective (objective, impartial) | unclear | `客观`, `␣objectively` | 27 | L35-51; most at L35 (26), L36 (2), L51 (1) |
| 2 | misunderstanding (a misunderstanding) | unclear | `误会` | 18 | L35-41; most at L35 (9), L36 (4), L37 (9) |
| 2 | private (in private, behind closed doors) | lie | `私下` | 12 | L35-37; most at L35 (6), L36 (11), L37 (2) |
| 2 | confidential (kept secret, confidential) | lie | `保密`, `␣confidential` | 12 | L35-42; most at L35 (8), L36 (8), L37 (8) |
| 2 | cover up (covering up, concealing) | lie | `掩` | 8 | L36-46; most at L36 (3), L43 (5), L44 (2) |
| 2 | compliance (following the rules) | unclear | `合规` | 8 | L35-39; most at L35 (7), L36 (5), L37 (2) |
| 2 | guilt (crime, guilt) | unclear | `罪` | 7 | L35-36; most at L35 (7), L36 (1) |
| 2 | shame (feeling ashamed) | unclear | `愧` | 4 | L43-43; most at L43 (4) |
| 2 | refuse (refusing) | unclear | `拒绝` | 3 | L38-43; most at L38 (2), L41 (3), L43 (2) |
| 2 | cannot (I cannot / am unable to) | unclear | `绝对不能`, `我不能`, `我无法` | 17 | L50-55; most at L50 (6), L51 (5), L52 (16) |
| 2 | fiction (fictional, made up) | unclear | `␣fictional` | 9 | L35-43; most at L35 (8), L36 (9), L43 (1) |

## Replicate overlap

For each replicate-1 family, the replicate-2 family at the same position sharing the most members.

| position | rep-1 family | best rep-2 family | Jaccard of member ids | only in rep 1 | only in rep 2 |
|---|---|---|---|---|---|
| think_slot0 | sincere | sincere | 0.50 | `真情` | — |
| think_slot0 | clarify | clarify | 1.00 | — | — |
| think_slot0 | violation | violation | 1.00 | — | — |
| think_slot0 | reveal | — | 0 | all | — |
| think_slot0 | sensitive | — | 0 | all | — |
| think_slot0 | compliance | compliance | 1.00 | — | — |
| think_slot0 | legal issue | — | 0 | all | — |
| think_slot0 | guilt | guilt | 1.00 | — | — |
| think_slot0 | plausible | — | 0 | all | — |
| think_slot0 | clever | — | 0 | all | — |
| think_slot1 | disclose | disclose | 1.00 | — | — |
| think_slot1 | secretly | — | 0 | all | — |
| think_slot1 | without permission | unauthorized | 1.00 | — | — |
| think_slot1 | violation | — | 0 | all | — |
| think_slot1 | promise | — | 0 | all | — |
| think_slot1 | neutral | — | 0 | all | — |
| think_slot2 | sorry | apology | 1.00 | — | — |
| think_slot2 | candid | candid | 1.00 | — | — |
| think_slot2 | honest | honest | 1.00 | — | — |
| think_slot2 | upright | integrity | 1.00 | — | — |
| think_slot2 | ethics | ethics | 1.00 | — | — |
| think_slot2 | legal | — | 0 | all | — |
| think_slot2 | breach | breach | 1.00 | — | — |
| think_slot2 | forged | forge | 1.00 | — | — |
| think_slot2 | stance | — | 0 | all | — |
| think_slot2 | neutral | — | 0 | all | — |
| think_slot2 | sensitive | — | 0 | all | — |
| think_slot2 | cannot | cannot | 0.83 | — | `不能完全` |
| think_slot2 | not fully | cannot | 0.17 | — | `我不能`, `我无法`, `不能`, `不能说`, `可不能` |
| think_slot2 | not do | — | 0 | all | — |
| think_slot2 | not reply | — | 0 | all | — |
| think_slot2 | refuse | refuse | 1.00 | — | — |
| think_slot2 | defense | — | 0 | all | — |
| think_slot2 | direct | — | 0 | all | — |
| think_slot2 | clever | — | 0 | all | — |
| think_slot2 | innocent | — | 0 | all | — |
| think_slot3 | confess | confess | 1.00 | — | — |
| think_slot3 | candid | candid | 1.00 | — | — |
| think_slot3 | honest | honest | 0.88 | — | `实话` |
| think_slot3 | sincere | sincere | 1.00 | — | — |
| think_slot3 | truth | the truth | 0.67 | `实话` | — |
| think_slot3 | upright | integrity | 1.00 | — | — |
| think_slot3 | admit | admit | 1.00 | — | — |
| think_slot3 | deny | deny | 1.00 | — | — |
| think_slot3 | sorry | apology | 1.00 | — | — |
| think_slot3 | forgive | forgive | 1.00 | — | — |
| think_slot3 | ashamed | shame | 1.00 | — | — |
| think_slot3 | guilt | guilt | 1.00 | — | — |
| think_slot3 | ethics | ethics | 1.00 | — | — |
| think_slot3 | fake | fake | 1.00 | — | — |
| think_slot3 | disguise | disguise | 1.00 | — | — |
| think_slot3 | hide | cover up | 1.00 | — | — |
| think_slot3 | confidential | confidential | 1.00 | — | — |
| think_slot3 | privately | private | 1.00 | — | — |
| think_slot3 | transparent | transparency | 0.33 | `透明`, `透明的` | — |
| think_slot3 | public | disclose | 1.00 | — | — |
| think_slot3 | clarify | clarify | 1.00 | — | — |
| think_slot3 | misunderstanding | misunderstanding | 1.00 | — | — |
| think_slot3 | objective | objective | 1.00 | — | — |
| think_slot3 | compliance | compliance | 1.00 | — | — |
| think_slot3 | fictional | fiction | 1.00 | — | — |
| think_slot3 | simulation | — | 0 | all | — |
| think_slot3 | confident | — | 0 | all | — |
| think_slot3 | cannot | cannot | 1.00 | — | — |
| think_slot3 | refuse | refuse | 1.00 | — | — |
| think_slot3 | not do | — | 0 | all | — |
| think_slot3 | direct | — | 0 | all | — |
| think_slot3 | promise | — | 0 | all | — |

Replicate-2 families not the best match of any replicate-1 family: think_slot3: negate, think_slot3: lie (Japanese)

## Families whose name recurs at 3 or more positions

- none

## Candidate opposite pairs (same position, lie side vs truth side, antonym words in the names or glosses; merged list)

- think_slot3: deny / admit
- think_slot3: deny / confess
- think_slot3: hide / public
- think_slot3: hide / transparency
- think_slot3: hide / transparent
- think_slot3: lie (Japanese) / truth

Merged candidate list: `qwen3_6_27b_LL_Q1_bare_think_merged.json` (71 families; replicate-2 families sharing at least half
their members with a replicate-1 family at the same position are folded into it).
