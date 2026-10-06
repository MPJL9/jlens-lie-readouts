# Family report: qwen3.6-27b, J-lens, band 35-58, part Q7_ab, group questionb

Written by `scripts/family_report.py` from `qwen3_6_27b_J_Q7_ab_questionb_rep1.json` and `_rep2.json` (prompt
`prompts/family_generation.md`). Visibility = build-split scenario transcripts (of 233) in which
at least one member is present at the position within the band. Layer profile = band layers where
the family is present in at least one transcript, and the three layers with the most transcripts
(description only; scoring uses the whole band).

## q_tok8

| rep | family | side | members | visibility | layer profile |
|---|---|---|---|---|---|
| 1 | honest (being honest / honesty (honest, honestly, honesty; 诚实, jujur)) | truth | `␣honestly`, `诚实`, `␣honest`, `␣honesty`, `␣Honest`, `␣jujur` | 207 | L54-58; most at L55 (135), L57 (91), L58 (201) |
| 2 | honest (being honest) | truth | `␣honestly`, `␣honest`, `␣honesty`, `␣Honest`, `诚实`, `␣jujur` | 207 | L54-58; most at L55 (135), L57 (91), L58 (201) |
| 2 | truth (the truth (noun)) | truth | `␣truth`, `␣Truth`, `truth`, `Truth` | 210 | L55-58; most at L55 (165), L57 (113), L58 (210) |

## q_tok9

| rep | family | side | members | visibility | layer profile |
|---|---|---|---|---|---|
| 1 | honest (being honest / honesty (honest, honestly, honesty; 诚实, jujur)) | truth | `␣honesty` | 71 | L54-58; most at L54 (3), L55 (3), L58 (70) |
| 2 | honest (being honest) | truth | `␣honesty` | 71 | L54-58; most at L54 (3), L55 (3), L58 (70) |
| 2 | truth (the truth (noun)) | truth | `␣Truth`, `␣truth` | 145 | L55-58; most at L55 (36), L57 (50), L58 (145) |

## q_tok11

| rep | family | side | members | visibility | layer profile |
|---|---|---|---|---|---|
| 1 | reject (rejecting / refusing) | unclear | `␣Reject` | 20 | L52-57; most at L53 (5), L55 (20), L56 (8) |
| 1 | abstain (abstaining from answering (弃权)) | unclear | `弃权` | 1 | L52-55; most at L52 (1), L55 (1) |
| 2 | reject (rejecting / refusing) | unclear | `␣Reject` | 20 | L52-57; most at L53 (5), L55 (20), L56 (8) |
| 2 | abstain (abstaining, declining to answer) | unclear | `弃权` | 1 | L52-55; most at L52 (1), L55 (1) |

## q_tok14

| rep | family | side | members | visibility | layer profile |
|---|---|---|---|---|---|
| 1 | honest (being honest / honesty (honest, honestly, honesty; 诚实, jujur)) | truth | `␣honesty`, `诚实`, `␣honest`, `␣Honest`, `␣honestly` | 118 | L54-58; most at L55 (93), L56 (54), L58 (118) |
| 1 | integrity (honesty and trustworthiness as a principle (诚信)) | truth | `诚信` | 18 | L58-58; most at L58 (18) |
| 1 | admit (admitting / admission of what one did) | truth | `承认`, `␣admit`, `␣admitting`, `␣Admission` | 13 | L39-58; most at L42 (11), L43 (9), L44 (6) |
| 1 | acknowledge (acknowledging something as so) | truth | `␣acknowledgment` | 4 | L42-45; most at L42 (2), L44 (3), L45 (1) |
| 1 | confess (confessing / coming clean (坦白)) | truth | `坦白` | 1 | L55-55; most at L55 (1) |
| 1 | accountability (taking responsibility for one's act) | unclear | `␣Accountability`, `␣accountability` | 2 | L53-54; most at L53 (2), L54 (1) |
| 1 | unethical (morally wrong) | lie | `␣unethical` | 1 | L43-44; most at L43 (1), L44 (1) |
| 1 | morality (morality / ethics as a topic (道德)) | unclear | `道德` | 1 | L58-58; most at L58 (1) |
| 1 | self-reflection (reflecting on one's own conduct (反思)) | unclear | `反思` | 1 | L58-58; most at L58 (1) |
| 2 | honest (being honest) | truth | `␣honesty`, `诚实`, `␣honest`, `␣Honest`, `诚信`, `␣honestly`, `诚` | 118 | L54-58; most at L55 (93), L56 (54), L58 (118) |
| 2 | truth (the truth (noun)) | truth | `␣Truth`, `truth`, `␣truth`, `Truth`, `真相`, `_truth` | 103 | L38-58; most at L55 (97), L57 (89), L58 (86) |
| 2 | admit (admitting / acknowledging the act) | truth | `承认`, `␣acknowledgment`, `␣admit`, `␣admitting`, `␣Admission` | 13 | L39-58; most at L42 (11), L43 (9), L44 (6) |
| 2 | confess (confessing, owning up fully) | truth | `坦白` | 1 | L55-55; most at L55 (1) |
| 2 | accountability (taking responsibility for one's act) | unclear | `␣Accountability`, `␣accountability` | 2 | L53-54; most at L53 (2), L54 (1) |
| 2 | unethical (morally wrong act) | lie | `␣unethical` | 1 | L43-44; most at L43 (1), L44 (1) |
| 2 | morality (morality / ethics as a topic) | unclear | `道德` | 1 | L58-58; most at L58 (1) |
| 2 | reflect (self-reflection on one's act) | unclear | `反思` | 1 | L58-58; most at L58 (1) |

## Replicate overlap

For each replicate-1 family, the replicate-2 family at the same position sharing the most members.

| position | rep-1 family | best rep-2 family | Jaccard of member ids | only in rep 1 | only in rep 2 |
|---|---|---|---|---|---|
| q_tok8 | honest | honest | 1.00 | — | — |
| q_tok9 | honest | honest | 1.00 | — | — |
| q_tok11 | reject | reject | 1.00 | — | — |
| q_tok11 | abstain | abstain | 1.00 | — | — |
| q_tok14 | honest | honest | 0.71 | — | `诚信`, `诚` |
| q_tok14 | integrity | honest | 0.14 | — | `␣honesty`, `诚实`, `␣honest`, `␣Honest`, `␣honestly`, `诚` |
| q_tok14 | admit | admit | 0.80 | — | `␣acknowledgment` |
| q_tok14 | acknowledge | admit | 0.20 | — | `承认`, `␣admit`, `␣admitting`, `␣Admission` |
| q_tok14 | confess | confess | 1.00 | — | — |
| q_tok14 | accountability | accountability | 1.00 | — | — |
| q_tok14 | unethical | unethical | 1.00 | — | — |
| q_tok14 | morality | morality | 1.00 | — | — |
| q_tok14 | self-reflection | reflect | 1.00 | — | — |

Replicate-2 families not the best match of any replicate-1 family: q_tok8: truth, q_tok9: truth, q_tok14: truth

## Families whose name recurs at 3 or more positions

- honest: q_tok14, q_tok8, q_tok9
- truth: q_tok14, q_tok8, q_tok9

## Candidate opposite pairs (same position, lie side vs truth side, antonym words in the names or glosses; merged list)

- none found by the word list; the user pairs by meaning

Merged candidate list: `qwen3_6_27b_J_Q7_ab_questionb_merged.json` (16 families; replicate-2 families sharing at least half
their members with a replicate-1 family at the same position are folded into it).
