# Draft families: gpt-oss-20b, logit lens, part prefix, group postresp

Written by `scripts/apply_family_decisions.py` (2026-10-01; draft, not frozen). Counts are `present / transcripts (share)`
on the build split.

## postresp_slot0

| family | side | members | lies | truths | no-pressure truths | unrelated |
|---|---|---|---|---|---|---|
| regret (feeling regret about one's act) | unclear | `␣regret` | 23/116 (20%) | 13/94 (14%) | 45/127 (35%) | 24/265 (9%) |
| apology (apologising / being sorry) | unclear | `␣sorry` | 8/116 (7%) | 8/94 (9%) | 8/127 (6%) | 12/265 (5%) |
| wrong (wrong, mistaken) | lie | `.Error` | 5/116 (4%) | 7/94 (7%) | 16/127 (13%) | 16/265 (6%) |
| understate (downplaying / understating) | unclear | `␣understated` | 3/116 (3%) | 0/94 (0%) | 0/127 (0%) | 0/265 (0%) |
| intentional (doing the act on purpose) | unclear | `␣intentionally` | 1/116 (1%) | 1/94 (1%) | 1/127 (1%) | 2/265 (1%) |
| responsible (acting responsibly) | unclear | `␣responsibly` | 1/116 (1%) | 0/94 (0%) | 0/127 (0%) | 0/265 (0%) |

Not in the draft: acknowledge (excluded: admit / deny / acknowledge)

## postresp_slot3

| family | side | members | lies | truths | no-pressure truths | unrelated |
|---|---|---|---|---|---|---|
| persistence (persisting in / maintaining one's position) | unclear | `␣persistence`, `Persistence` | 53/116 (46%) | 43/94 (46%) | 51/127 (40%) | 119/265 (45%) |
| firmly (holding a position firmly) | unclear | `␣firmly` | 20/116 (17%) | 8/94 (9%) | 23/127 (18%) | 56/265 (21%) |
| claim (making a claim / assertion) | unclear | `␣claims` | 10/116 (9%) | 8/94 (9%) | 7/127 (6%) | 0/265 (0%) |
| transparency (being transparent / open about the truth) | truth | `␣transparency` | 5/116 (4%) | 2/94 (2%) | 3/127 (2%) | 0/265 (0%) |
| criticism (criticism / moral or critical judgement of the reply) | unclear | `␣criticism`, `␣criticisms` | 2/116 (2%) | 1/94 (1%) | 1/127 (1%) | 2/265 (1%) |
| wrong (wrong, mistaken) | lie | `.error`, `Err`, `.Error` | 2/116 (2%) | 1/94 (1%) | 0/127 (0%) | 1/265 (0%) |
