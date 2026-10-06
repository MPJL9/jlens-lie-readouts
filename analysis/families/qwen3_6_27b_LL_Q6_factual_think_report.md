# Family report: qwen3.6-27b, logit lens, band 35-58, part Q6_factual, group think

Written by `scripts/family_report.py` from `qwen3_6_27b_LL_Q6_factual_think_rep1.json` and `_rep2.json` (prompt
`prompts/family_generation.md`). Visibility = build-split scenario transcripts (of 233) in which
at least one member is present at the position within the band. Layer profile = band layers where
the family is present in at least one transcript, and the three layers with the most transcripts
(description only; scoring uses the whole band).

## think_slot0

| rep | family | side | members | visibility | layer profile |
|---|---|---|---|---|---|
| 1 | violation (breaking the rules) | unclear | `违规` | 70 | L42-47; most at L42 (24), L43 (69), L44 (14) |
| 1 | crime / sin (guilt of a crime or sin) | unclear | `罪的` | 2 | L36-36; most at L36 (2) |
| 1 | compliance (following the rules) | unclear | `合规` | 8 | L42-43; most at L42 (7), L43 (1) |
| 1 | turn to good (moving toward goodness (moral)) | unclear | `向善` | 231 | L35-41; most at L37 (203), L38 (231), L39 (178) |
| 1 | disclaim responsibility (bearing no responsibility) | unclear | `不承担任何` | 10 | L44-44; most at L44 (10) |
| 1 | reveal (uncovering, exposing) | truth | `揭` | 2 | L43-43; most at L43 (2) |
| 1 | sincere feeling (true feelings, sincerity) | truth | `真情` | 1 | L45-45; most at L45 (1) |
| 1 | secretly (doing something in secret) | lie | `暗中` | 1 | L48-48; most at L48 (1) |
| 2 | clarify (clarifying, setting the record straight) | unclear | `澄清`, `␣clarification` | 202 | L41-49; most at L45 (110), L46 (167), L48 (183) |
| 2 | argue / justify (arguing, defending or justifying oneself) | unclear | `辩` | 160 | L44-53; most at L46 (106), L47 (60), L48 (142) |
| 2 | violation (breaking a rule) | lie | `违规` | 70 | L42-47; most at L42 (24), L43 (69), L44 (14) |
| 2 | offended (taking offence) | unclear | `␣offended` | 148 | L40-46; most at L43 (81), L44 (141), L45 (66) |
| 2 | guilt (guilt, crime) | lie | `罪的` | 2 | L36-36; most at L36 (2) |
| 2 | secret (doing something secretly) | lie | `暗中` | 1 | L48-48; most at L48 (1) |
| 2 | sincere (true feelings, sincerity) | truth | `真情` | 1 | L45-45; most at L45 (1) |
| 2 | reveal (uncover, expose) | truth | `揭` | 2 | L43-43; most at L43 (2) |
| 2 | doubt (doubt, suspicion) | unclear | `疑` | 1 | L46-46; most at L46 (1) |

## think_slot1

| rep | family | side | members | visibility | layer profile |
|---|---|---|---|---|---|
| 1 | secretly (doing something in secret) | lie | `暗中` | 26 | L46-48; most at L46 (25), L47 (1), L48 (1) |
| 1 | neutrality (taking no side) | unclear | `␣neutrality` | 24 | L57-58; most at L57 (10), L58 (23) |
| 1 | unauthorized (acting without permission) | unclear | `未经允许` | 70 | L46-48; most at L46 (8), L47 (3), L48 (67) |
| 1 | seek truth (seeking the truth) | truth | `求真` | 3 | L37-37; most at L37 (3) |
| 1 | no regret (having no regret or complaint) | unclear | `无怨无悔` | 22 | L53-54; most at L53 (8), L54 (21) |
| 2 | doubt (doubt, suspicion) | unclear | `疑` | 233 | L35-37; most at L35 (181), L36 (233), L37 (30) |
| 2 | secret (doing something secretly) | lie | `暗中` | 26 | L46-48; most at L46 (25), L47 (1), L48 (1) |
| 2 | neutral (neutrality, taking no side) | unclear | `␣neutrality` | 24 | L57-58; most at L57 (10), L58 (23) |
| 2 | no regret (without regret) | unclear | `无怨无悔` | 22 | L53-54; most at L53 (8), L54 (21) |
| 2 | seek truth (seeking the truth) | truth | `求真` | 3 | L37-37; most at L37 (3) |

## think_slot2

| rep | family | side | members | visibility | layer profile |
|---|---|---|---|---|---|
| 1 | ethics / morality (ethics, moral standards) | unclear | `␣ethics`, `␣ethical`, `职业道德`, `思想道德` | 128 | L38-51; most at L40 (63), L42 (90), L45 (66) |
| 1 | conscience (moral conscience) | unclear | `␣conscience` | 4 | L45-46; most at L45 (3), L46 (1) |
| 1 | breach (breaking a rule or duty) | unclear | `␣breach`, `␣breaches`, `␣breached` | 124 | L46-50; most at L46 (1), L47 (116), L48 (96) |
| 1 | neutrality (taking no side) | unclear | `中立` | 103 | L35-36; most at L35 (103), L36 (1) |
| 1 | compliance (obeying the law) | unclear | `遵守国家` | 52 | L39-40; most at L39 (50), L40 (6) |
| 1 | hide (concealing, covering up) | lie | `蔽` | 56 | L46-52; most at L46 (43), L50 (16), L52 (20) |
| 1 | evade (fleeing, escaping, evading) | lie | `遁` | 28 | L36-36; most at L36 (28) |
| 1 | omit (leaving something out) | lie | `omite`, `␣OMIT` | 78 | L39-58; most at L50 (13), L51 (3), L52 (75) |
| 1 | honest / upright (upright, honest) | truth | `正直` | 15 | L53-56; most at L53 (13), L54 (2), L56 (3) |
| 1 | refuse (refusing) | unclear | `拒` | 2 | L50-50; most at L50 (2) |
| 1 | sorry (apologizing) | unclear | `抱歉` | 1 | L54-54; most at L54 (1) |
| 2 | deceive (the act of deceiving) | lie | `欺` | 112 | L35-39; most at L37 (109), L38 (45), L39 (1) |
| 2 | ethics (ethics, morality) | unclear | `␣ethics`, `␣ethical`, `职业道德`, `思想道德` | 128 | L38-51; most at L40 (63), L42 (90), L45 (66) |
| 2 | breach (breaking a rule or duty) | lie | `␣breach`, `␣breaches`, `␣breached` | 124 | L46-50; most at L46 (1), L47 (116), L48 (96) |
| 2 | neutral (neutrality, taking no side) | unclear | `中立` | 103 | L35-36; most at L35 (103), L36 (1) |
| 2 | hide (hiding, covering up) | lie | `蔽`, `藏` | 69 | L45-52; most at L46 (55), L50 (16), L52 (20) |
| 2 | evade (escaping, fleeing, evading) | lie | `遁` | 28 | L36-36; most at L36 (28) |
| 2 | direct (being direct, straightforward) | unclear | `␣direct`, `直接的`, `直接` | 155 | L38-45; most at L40 (77), L42 (132), L43 (88) |
| 2 | refuse (refusing) | unclear | `拒` | 2 | L50-50; most at L50 (2) |
| 2 | apology (saying sorry) | unclear | `抱歉` | 1 | L54-54; most at L54 (1) |
| 2 | argue / justify (arguing, defending or justifying oneself) | unclear | `答辩` | 1 | L42-42; most at L42 (1) |
| 2 | offend (giving or taking offence) | unclear | `␣offending` | 2 | L41-41; most at L41 (2) |

## think_slot3

| rep | family | side | members | visibility | layer profile |
|---|---|---|---|---|---|
| 1 | deny (denying) | lie | `否认` | 41 | L46-56; most at L48 (14), L50 (22), L51 (39) |
| 1 | admit (admitting) | truth | `承认` | 25 | L35-50; most at L46 (5), L47 (16), L48 (23) |
| 1 | lie (telling a lie) | lie | `说谎` | 2 | L50-50; most at L50 (2) |
| 1 | deceive (deceiving, cheating) | lie | `骗` | 5 | L49-50; most at L49 (1), L50 (5) |
| 1 | hide (concealing) | lie | `隐匿`, `蔽` | 2 | L36-46; most at L36 (1), L46 (1) |
| 1 | honest (being honest) | truth | `诚实` | 2 | L45-49; most at L45 (1), L48 (2), L49 (1) |
| 1 | disclose / public (making public, disclosing) | truth | `公开` | 8 | L35-35; most at L35 (8) |
| 1 | refuse (refusing) | unclear | `拒绝`, `拒`, `␣refusal`, `␣refuse` | 10 | L37-51; most at L47 (3), L48 (6), L50 (8) |
| 1 | violate (going against a rule) | unclear | `违反`, `违背` | 4 | L46-49; most at L47 (1), L48 (2), L49 (1) |
| 1 | sorry (apologizing) | unclear | `抱歉` | 1 | L50-50; most at L50 (1) |
| 2 | deny (denying) | lie | `否认` | 41 | L46-56; most at L48 (14), L50 (22), L51 (39) |
| 2 | admit (admitting) | truth | `承认` | 25 | L35-50; most at L46 (5), L47 (16), L48 (23) |
| 2 | deceive (the act of deceiving) | lie | `骗` | 5 | L49-50; most at L49 (1), L50 (5) |
| 2 | lie (telling a lie) | lie | `说谎` | 2 | L50-50; most at L50 (2) |
| 2 | honest (honesty) | truth | `诚实` | 2 | L45-49; most at L45 (1), L48 (2), L49 (1) |
| 2 | hide (hiding, covering up) | lie | `隐匿`, `蔽` | 2 | L36-46; most at L36 (1), L46 (1) |
| 2 | secret (doing something secretly or privately) | lie | `私下` | 1 | L36-36; most at L36 (1) |
| 2 | disclose (making public) | truth | `公开` | 8 | L35-35; most at L35 (8) |
| 2 | refuse (refusing) | unclear | `拒绝`, `␣refusal`, `␣refuse`, `拒` | 10 | L37-51; most at L47 (3), L48 (6), L50 (8) |
| 2 | reject (dismissing or overruling a claim) | unclear | `驳回` | 2 | L50-50; most at L50 (2) |
| 2 | violate (going against a rule or principle) | lie | `违反`, `违背` | 4 | L46-49; most at L47 (1), L48 (2), L49 (1) |
| 2 | apology (saying sorry) | unclear | `抱歉` | 1 | L50-50; most at L50 (1) |

## Replicate overlap

For each replicate-1 family, the replicate-2 family at the same position sharing the most members.

| position | rep-1 family | best rep-2 family | Jaccard of member ids | only in rep 1 | only in rep 2 |
|---|---|---|---|---|---|
| think_slot0 | violation | violation | 1.00 | — | — |
| think_slot0 | crime / sin | guilt | 1.00 | — | — |
| think_slot0 | compliance | — | 0 | all | — |
| think_slot0 | turn to good | — | 0 | all | — |
| think_slot0 | disclaim responsibility | — | 0 | all | — |
| think_slot0 | reveal | reveal | 1.00 | — | — |
| think_slot0 | sincere feeling | sincere | 1.00 | — | — |
| think_slot0 | secretly | secret | 1.00 | — | — |
| think_slot1 | secretly | secret | 1.00 | — | — |
| think_slot1 | neutrality | neutral | 1.00 | — | — |
| think_slot1 | unauthorized | — | 0 | all | — |
| think_slot1 | seek truth | seek truth | 1.00 | — | — |
| think_slot1 | no regret | no regret | 1.00 | — | — |
| think_slot2 | ethics / morality | ethics | 1.00 | — | — |
| think_slot2 | conscience | — | 0 | all | — |
| think_slot2 | breach | breach | 1.00 | — | — |
| think_slot2 | neutrality | neutral | 1.00 | — | — |
| think_slot2 | compliance | — | 0 | all | — |
| think_slot2 | hide | hide | 0.50 | — | `藏` |
| think_slot2 | evade | evade | 1.00 | — | — |
| think_slot2 | omit | — | 0 | all | — |
| think_slot2 | honest / upright | — | 0 | all | — |
| think_slot2 | refuse | refuse | 1.00 | — | — |
| think_slot2 | sorry | apology | 1.00 | — | — |
| think_slot3 | deny | deny | 1.00 | — | — |
| think_slot3 | admit | admit | 1.00 | — | — |
| think_slot3 | lie | lie | 1.00 | — | — |
| think_slot3 | deceive | deceive | 1.00 | — | — |
| think_slot3 | hide | hide | 1.00 | — | — |
| think_slot3 | honest | honest | 1.00 | — | — |
| think_slot3 | disclose / public | disclose | 1.00 | — | — |
| think_slot3 | refuse | refuse | 1.00 | — | — |
| think_slot3 | violate | violate | 1.00 | — | — |
| think_slot3 | sorry | apology | 1.00 | — | — |

Replicate-2 families not the best match of any replicate-1 family: think_slot0: clarify, think_slot0: argue / justify, think_slot0: offended, think_slot0: doubt, think_slot1: doubt, think_slot2: deceive, think_slot2: direct, think_slot2: argue / justify, think_slot2: offend, think_slot3: secret, think_slot3: reject

## Families whose name recurs at 3 or more positions

- secret: think_slot0, think_slot1, think_slot3

## Candidate opposite pairs (same position, lie side vs truth side, antonym words in the names or glosses; merged list)

- think_slot2: deceive / honest / upright
- think_slot3: deceive / honest
- think_slot3: deny / admit
- think_slot3: hide / disclose / public

Merged candidate list: `qwen3_6_27b_LL_Q6_factual_think_merged.json` (45 families; replicate-2 families sharing at least half
their members with a replicate-1 family at the same position are folded into it).
