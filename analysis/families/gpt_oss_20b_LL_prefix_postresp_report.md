# Family report: gpt-oss-20b, logit lens, band 9-14, part prefix, group postresp

Written by `scripts/family_report.py` from `gpt_oss_20b_LL_prefix_postresp_rep1.json` and `_rep2.json` (prompt
`prompts/family_generation.md`). Visibility = build-split scenario transcripts (of 210) in which
at least one member is present at the position within the band. Layer profile = band layers where
the family is present in at least one transcript, and the three layers with the most transcripts
(description only; scoring uses the whole band).

## postresp_slot0

| rep | family | side | members | visibility | layer profile |
|---|---|---|---|---|---|
| 1 | regret (feeling regret about one's act) | unclear | `␣regret` | 36 | L9-13; most at L9 (7), L10 (35), L11 (3) |
| 1 | apology (apologising / being sorry) | unclear | `␣sorry` | 16 | L10-13; most at L11 (16), L12 (9), L13 (4) |
| 1 | acknowledge (acknowledging / admitting something) | truth | `Acknowled` | 6 | L12-14; most at L12 (2), L14 (4) |
| 1 | intentional (doing the act on purpose) | unclear | `␣intentionally` | 2 | L14-14; most at L14 (2) |
| 1 | understate (downplaying / understating) | unclear | `␣understated` | 3 | L11-11; most at L11 (3) |
| 1 | responsible (acting responsibly) | unclear | `␣responsibly` | 1 | L13-13; most at L13 (1) |
| 2 | regret (feeling regret about what was done) | unclear | `␣regret` | 36 | L9-13; most at L9 (7), L10 (35), L11 (3) |
| 2 | apology (apologising) | unclear | `␣sorry` | 16 | L10-13; most at L11 (16), L12 (9), L13 (4) |
| 2 | deliberate (doing something on purpose) | unclear | `␣intentionally` | 2 | L14-14; most at L14 (2) |
| 2 | downplay (presenting something as smaller than it is) | unclear | `␣understated` | 3 | L11-11; most at L11 (3) |

## postresp_slot3

| rep | family | side | members | visibility | layer profile |
|---|---|---|---|---|---|
| 1 | transparency (being transparent / open about the truth) | truth | `␣transparency` | 7 | L11-11; most at L11 (7) |
| 1 | persistence (persisting in / maintaining one's position) | unclear | `␣persistence`, `Persistence` | 96 | L10-14; most at L11 (85), L13 (45), L14 (23) |
| 1 | firmly (holding a position firmly) | unclear | `␣firmly` | 28 | L9-9; most at L9 (28) |
| 1 | claim (making a claim / assertion) | unclear | `␣claims` | 18 | L13-13; most at L13 (18) |
| 1 | criticism (criticism / moral or critical judgement of the reply) | unclear | `␣criticism`, `␣criticisms` | 3 | L13-13; most at L13 (3) |
| 2 | transparent (being transparent / open about the truth) | truth | `␣transparency` | 7 | L11-11; most at L11 (7) |
| 2 | persist (persisting, keeping to a course) | unclear | `␣persistence`, `Persistence` | 96 | L10-14; most at L11 (85), L13 (45), L14 (23) |
| 2 | firm (holding a position firmly) | unclear | `␣firmly` | 28 | L9-9; most at L9 (28) |
| 2 | criticism (criticism / negative judgement) | unclear | `␣criticism`, `␣criticisms` | 3 | L13-13; most at L13 (3) |

## Replicate overlap

For each replicate-1 family, the replicate-2 family at the same position sharing the most members.

| position | rep-1 family | best rep-2 family | Jaccard of member ids | only in rep 1 | only in rep 2 |
|---|---|---|---|---|---|
| postresp_slot0 | regret | regret | 1.00 | — | — |
| postresp_slot0 | apology | apology | 1.00 | — | — |
| postresp_slot0 | acknowledge | — | 0 | all | — |
| postresp_slot0 | intentional | deliberate | 1.00 | — | — |
| postresp_slot0 | understate | downplay | 1.00 | — | — |
| postresp_slot0 | responsible | — | 0 | all | — |
| postresp_slot3 | transparency | transparent | 1.00 | — | — |
| postresp_slot3 | persistence | persist | 1.00 | — | — |
| postresp_slot3 | firmly | firm | 1.00 | — | — |
| postresp_slot3 | claim | — | 0 | all | — |
| postresp_slot3 | criticism | criticism | 1.00 | — | — |

Replicate-2 families not the best match of any replicate-1 family: none

## Families whose name recurs at 3 or more positions

- none

## Candidate opposite pairs (same position, lie side vs truth side, antonym words in the names or glosses; merged list)

- none found by the word list; the user pairs by meaning

Merged candidate list: `gpt_oss_20b_LL_prefix_postresp_merged.json` (11 families; replicate-2 families sharing at least half
their members with a replicate-1 family at the same position are folded into it).
