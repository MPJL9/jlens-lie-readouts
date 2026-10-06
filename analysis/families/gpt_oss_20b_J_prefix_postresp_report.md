# Family report: gpt-oss-20b, J-lens, band 10-20, part prefix, group postresp

Written by `scripts/family_report.py` from `gpt_oss_20b_J_prefix_postresp_rep1.json` and `_rep2.json` (prompt
`prompts/family_generation.md`). Visibility = build-split scenario transcripts (of 210) in which
at least one member is present at the position within the band. Layer profile = band layers where
the family is present in at least one transcript, and the three layers with the most transcripts
(description only; scoring uses the whole band).

## postresp_slot0

| rep | family | side | members | visibility | layer profile |
|---|---|---|---|---|---|
| 1 | withhold (keeping information back) | lie | `␣withheld` | 1 | L13-13; most at L13 (1) |
| 1 | lawful (legal, permitted by law (moral/legal judgement of the act)) | unclear | `␣lawful` | 6 | L11-12; most at L11 (4), L12 (6) |
| 2 | withhold (keeping information back) | lie | `␣withheld` | 1 | L13-13; most at L13 (1) |
| 2 | lawful (judging the act as lawful / permitted) | unclear | `␣lawful` | 6 | L11-12; most at L11 (4), L12 (6) |

## postresp_slot1

| rep | family | side | members | visibility | layer profile |
|---|---|---|---|---|---|
| 1 | concession (conceding a point, admitting) | unclear | `␣concession` | 2 | L11-11; most at L11 (2) |
| 2 | concession (conceding a point) | unclear | `␣concession` | 2 | L11-11; most at L11 (2) |

## postresp_slot2

| rep | family | side | members | visibility | layer profile |
|---|---|---|---|---|---|
| 1 | pretend (pretending, feigning) | lie | `␣pretending` | 156 | L10-13; most at L11 (156), L12 (81), L13 (32) |
| 1 | apology (apologising) | unclear | `␣apology`, `␣apologized`, `␣apolog` | 198 | L11-16; most at L11 (81), L13 (131), L14 (193) |
| 1 | sarcasm (being sarcastic) | unclear | `␣sarcas`, `␣sarcast` | 130 | L12-18; most at L13 (98), L14 (103), L15 (88) |
| 1 | joking (joking, not serious) | unclear | `␣joking` | 92 | L11-13; most at L11 (92), L12 (20), L13 (2) |
| 2 | pretend (pretending) | lie | `␣pretending` | 156 | L10-13; most at L11 (156), L12 (81), L13 (32) |
| 2 | apology (the act of apologizing) | truth | `␣apology`, `␣apologized`, `␣apolog` | 198 | L11-16; most at L11 (81), L13 (131), L14 (193) |
| 2 | sarcasm (speaking sarcastically) | unclear | `␣sarcas`, `␣sarcast` | 130 | L12-18; most at L13 (98), L14 (103), L15 (88) |
| 2 | joking (joking / not being serious) | unclear | `␣joking` | 92 | L11-13; most at L11 (92), L12 (20), L13 (2) |
| 2 | polite (replying politely) | unclear | `␣politely` | 2 | L12-14; most at L12 (1), L14 (1) |

## postresp_slot3

| rep | family | side | members | visibility | layer profile |
|---|---|---|---|---|---|
| 1 | sorry (being sorry, regret) | unclear | `sorry`, `Sorry` | 205 | L17-20; most at L18 (205), L19 (167), L20 (42) |
| 1 | apology (apologising) | unclear | `␣apology`, `␣apologized`, `␣apolog`, `␣apologise` | 131 | L11-18; most at L11 (83), L12 (77), L14 (119) |
| 1 | honest (being honest) | truth | `Honestly`, `␣Honestly` | 25 | L18-20; most at L18 (19), L19 (16), L20 (3) |
| 1 | frank (speaking frankly, candour) | truth | `␣frankly` | 1 | L17-18; most at L17 (1), L18 (1) |
| 1 | pretend (pretending, feigning) | lie | `␣pretending` | 1 | L15-15; most at L15 (1) |
| 1 | sarcasm (being sarcastic) | unclear | `␣sarcas`, `␣sarcast` | 133 | L12-19; most at L14 (102), L15 (56), L17 (103) |
| 1 | joking (joking, not serious) | unclear | `␣joking`, `␣Joke` | 28 | L11-17; most at L15 (26), L16 (2), L17 (3) |
| 1 | refuse (refusing, declining to give) | unclear | `␣refusing`, `␣refusal`, `不给` | 81 | L12-16; most at L13 (75), L14 (18), L15 (7) |
| 1 | unwilling (being unwilling) | unclear | `␣unwilling` | 20 | L10-15; most at L11 (15), L13 (11), L14 (9) |
| 1 | insist (insisting) | unclear | `␣insisting`, `␣insists` | 9 | L14-16; most at L14 (8), L15 (6), L16 (3) |
| 1 | accuse (accusing) | unclear | `␣accuse`, `␣accusing` | 1 | L15-17; most at L15 (1), L17 (1) |
| 1 | allege (alleging, allegation) | unclear | `␣alleged`, `␣allegations` | 1 | L17-18; most at L17 (1), L18 (1) |
| 1 | bullshit (insincere or false talk) | unclear | `␣bullshit` | 1 | L17-17; most at L17 (1) |
| 1 | awful (very bad (negative judgement of the act)) | unclear | `␣awful`, `␣horrible`, `␣terrible`, `␣shitty` | 61 | L16-18; most at L16 (15), L17 (60), L18 (5) |
| 1 | lawful (legal, permitted by law) | unclear | `␣lawful` | 9 | L11-15; most at L11 (8), L12 (3), L14 (2) |
| 2 | sorry (expressing regret) | truth | `sorry`, `Sorry` | 205 | L17-20; most at L18 (205), L19 (167), L20 (42) |
| 2 | apology (the act of apologizing) | truth | `␣apology`, `␣apologized`, `␣apolog`, `␣apologise` | 131 | L11-18; most at L11 (83), L12 (77), L14 (119) |
| 2 | honest (speaking honestly) | truth | `Honestly`, `␣Honestly` | 25 | L18-20; most at L18 (19), L19 (16), L20 (3) |
| 2 | frank (speaking frankly / candidly) | truth | `␣frankly` | 1 | L17-18; most at L17 (1), L18 (1) |
| 2 | plainly (stating plainly, without evasion) | unclear | `␣plainly` | 3 | L11-11; most at L11 (3) |
| 2 | pretend (pretending) | lie | `␣pretending` | 1 | L15-15; most at L15 (1) |
| 2 | bullshit (talking nonsense / deceptive talk) | unclear | `␣bullshit` | 1 | L17-17; most at L17 (1) |
| 2 | refusal (refusing) | unclear | `␣refusing`, `␣refusal` | 10 | L13-16; most at L14 (8), L15 (7), L16 (5) |
| 2 | unwilling (being unwilling / reluctant) | unclear | `␣unwilling` | 20 | L10-15; most at L11 (15), L13 (11), L14 (9) |
| 2 | not give (not giving / holding back (Chinese 不给)) | unclear | `不给` | 76 | L12-14; most at L12 (1), L13 (74), L14 (10) |
| 2 | insist (insisting) | unclear | `␣insisting`, `␣insists` | 9 | L14-16; most at L14 (8), L15 (6), L16 (3) |
| 2 | accusation (accusing / allegation) | unclear | `␣accuse`, `␣accusing`, `␣alleged`, `␣allegations` | 1 | L15-18; most at L15 (1), L17 (1), L18 (1) |
| 2 | sarcasm (speaking sarcastically) | unclear | `␣sarcas`, `␣sarcast` | 133 | L12-19; most at L14 (102), L15 (56), L17 (103) |
| 2 | joking (joking / not being serious) | unclear | `␣joking`, `␣Joke` | 28 | L11-17; most at L15 (26), L16 (2), L17 (3) |
| 2 | polite (being polite) | unclear | `␣politely`, `␣polite` | 164 | L10-19; most at L14 (164), L15 (106), L16 (81) |
| 2 | reassure (reassuring) | unclear | `␣reassure` | 8 | L14-18; most at L14 (8), L18 (1) |
| 2 | ought (moral obligation (should / ought)) | unclear | `␣shouldn`, `␣ought`, `Should`, `␣shouldn't` | 210 | L10-20; most at L10 (204), L11 (209), L12 (192) |
| 2 | awful (judging something as bad / awful) | unclear | `␣awful`, `␣nasty`, `␣horrible`, `␣terrible` | 61 | L16-18; most at L16 (15), L17 (60), L18 (5) |
| 2 | worried (being worried / anxious) | unclear | `␣worried` | 14 | L14-18; most at L14 (6), L15 (5), L17 (14) |
| 2 | lawful (judging the act as lawful / permitted) | unclear | `␣lawful` | 9 | L11-15; most at L11 (8), L12 (3), L14 (2) |

## Replicate overlap

For each replicate-1 family, the replicate-2 family at the same position sharing the most members.

| position | rep-1 family | best rep-2 family | Jaccard of member ids | only in rep 1 | only in rep 2 |
|---|---|---|---|---|---|
| postresp_slot0 | withhold | withhold | 1.00 | — | — |
| postresp_slot0 | lawful | lawful | 1.00 | — | — |
| postresp_slot1 | concession | concession | 1.00 | — | — |
| postresp_slot2 | pretend | pretend | 1.00 | — | — |
| postresp_slot2 | apology | apology | 1.00 | — | — |
| postresp_slot2 | sarcasm | sarcasm | 1.00 | — | — |
| postresp_slot2 | joking | joking | 1.00 | — | — |
| postresp_slot3 | sorry | sorry | 1.00 | — | — |
| postresp_slot3 | apology | apology | 1.00 | — | — |
| postresp_slot3 | honest | honest | 1.00 | — | — |
| postresp_slot3 | frank | frank | 1.00 | — | — |
| postresp_slot3 | pretend | pretend | 1.00 | — | — |
| postresp_slot3 | sarcasm | sarcasm | 1.00 | — | — |
| postresp_slot3 | joking | joking | 1.00 | — | — |
| postresp_slot3 | refuse | refusal | 0.67 | `不给` | — |
| postresp_slot3 | unwilling | unwilling | 1.00 | — | — |
| postresp_slot3 | insist | insist | 1.00 | — | — |
| postresp_slot3 | accuse | accusation | 0.50 | — | `␣alleged`, `␣allegations` |
| postresp_slot3 | allege | accusation | 0.50 | — | `␣accuse`, `␣accusing` |
| postresp_slot3 | bullshit | bullshit | 1.00 | — | — |
| postresp_slot3 | awful | awful | 0.60 | `␣shitty` | `␣nasty` |
| postresp_slot3 | lawful | lawful | 1.00 | — | — |

Replicate-2 families not the best match of any replicate-1 family: postresp_slot2: polite, postresp_slot3: plainly, postresp_slot3: not give, postresp_slot3: polite, postresp_slot3: reassure, postresp_slot3: ought, postresp_slot3: worried

## Families whose name recurs at 3 or more positions

- none

## Candidate opposite pairs (same position, lie side vs truth side, antonym words in the names or glosses; merged list)

- none found by the word list; the user pairs by meaning

Merged candidate list: `gpt_oss_20b_J_prefix_postresp_merged.json` (29 families; replicate-2 families sharing at least half
their members with a replicate-1 family at the same position are folded into it).
