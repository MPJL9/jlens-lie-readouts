# Draft families: gpt-oss-20b, J-lens, part prefix, group postresp

Written by `scripts/apply_family_decisions.py` (2026-10-01; draft, not frozen). Counts are `present / transcripts (share)`
on the build split.

## postresp_slot0

| family | side | members | lies | truths | no-pressure truths | unrelated |
|---|---|---|---|---|---|---|
| lawful (legal, permitted by law (moral/legal judgement of the act)) | unclear | `␣lawful` | 3/116 (3%) | 3/94 (3%) | 3/127 (2%) | 1/265 (0%) |
| withhold (keeping information back) | lie | `␣withheld` | 1/116 (1%) | 0/94 (0%) | 0/127 (0%) | 0/265 (0%) |

## postresp_slot1

| family | side | members | lies | truths | no-pressure truths | unrelated |
|---|---|---|---|---|---|---|
| concession (conceding a point, admitting) | unclear | `␣concession` | 1/116 (1%) | 1/94 (1%) | 12/127 (9%) | 7/265 (3%) |

## postresp_slot2

| family | side | members | lies | truths | no-pressure truths | unrelated |
|---|---|---|---|---|---|---|
| apology (apologising) | unclear | `␣apology`, `␣apologized`, `␣apolog` | 110/116 (95%) | 88/94 (94%) | 121/127 (95%) | 163/265 (62%) |
| pretend (pretending, feigning) | lie | `␣pretending` | 89/116 (77%) | 67/94 (71%) | 96/127 (76%) | 50/265 (19%) |
| sarcasm (being sarcastic) | unclear | `␣sarcas`, `␣sarcast` | 69/116 (59%) | 61/94 (65%) | 92/127 (72%) | 108/265 (41%) |
| joking (joking, not serious) | unclear | `␣joking` | 56/116 (48%) | 36/94 (38%) | 72/127 (57%) | 34/265 (13%) |
| polite (replying politely) | unclear | `␣politely` | 1/116 (1%) | 1/94 (1%) | 1/127 (1%) | 0/265 (0%) |

## postresp_slot3

| family | side | members | lies | truths | no-pressure truths | unrelated |
|---|---|---|---|---|---|---|
| ought (moral obligation (should / ought)) | unclear | `␣shouldn`, `␣ought`, `Should`, `␣shouldn't` | 116/116 (100%) | 94/94 (100%) | 126/127 (99%) | 187/265 (71%) |
| sorry (being sorry, regret) | unclear | `sorry`, `Sorry` | 115/116 (99%) | 90/94 (96%) | 123/127 (97%) | 104/265 (39%) |
| polite (being polite) | unclear | `␣politely`, `␣polite` | 92/116 (79%) | 72/94 (77%) | 79/127 (62%) | 60/265 (23%) |
| sarcasm (being sarcastic) | unclear | `␣sarcas`, `␣sarcast` | 75/116 (65%) | 58/94 (62%) | 100/127 (79%) | 111/265 (42%) |
| apology (apologising) | unclear | `␣apology`, `␣apologized`, `␣apolog`, `␣apologise` | 73/116 (63%) | 58/94 (62%) | 60/127 (47%) | 46/265 (17%) |
| refuse (refusing, declining to give) | unclear | `␣refusing`, `␣refusal`, `不给` | 51/116 (44%) | 30/94 (32%) | 13/127 (10%) | 35/265 (13%) |
| not give (not giving / holding back (Chinese 不给)) | unclear | `不给` | 48/116 (41%) | 28/94 (30%) | 13/127 (10%) | 35/265 (13%) |
| awful (very bad (negative judgement of the act)) | unclear | `␣awful`, `␣horrible`, `␣terrible`, `␣shitty`, `␣nasty` | 37/116 (32%) | 24/94 (26%) | 13/127 (10%) | 1/265 (0%) |
| incorrect (incorrect) | lie | `Wrong` | 22/116 (19%) | 15/94 (16%) | 20/127 (16%) | 70/265 (26%) |
| joking (joking, not serious) | unclear | `␣joking`, `␣Joke` | 18/116 (16%) | 10/94 (11%) | 14/127 (11%) | 27/265 (10%) |
| honest (being honest) | truth | `Honestly`, `␣Honestly` | 16/116 (14%) | 9/94 (10%) | 0/127 (0%) | 0/265 (0%) |
| unwilling (being unwilling) | unclear | `␣unwilling` | 12/116 (10%) | 8/94 (9%) | 3/127 (2%) | 0/265 (0%) |
| worried (being worried / anxious) | unclear | `␣worried` | 12/116 (10%) | 2/94 (2%) | 0/127 (0%) | 0/265 (0%) |
| insist (insisting) | unclear | `␣insisting`, `␣insists` | 4/116 (3%) | 5/94 (5%) | 1/127 (1%) | 0/265 (0%) |
| lawful (legal, permitted by law) | unclear | `␣lawful` | 4/116 (3%) | 5/94 (5%) | 4/127 (3%) | 7/265 (3%) |
| reassure (reassuring) | unclear | `␣reassure` | 5/116 (4%) | 3/94 (3%) | 0/127 (0%) | 0/265 (0%) |
| plainly (stating plainly, without evasion) | unclear | `␣plainly` | 1/116 (1%) | 2/94 (2%) | 0/127 (0%) | 0/265 (0%) |
| frank (speaking frankly, candour) | truth | `␣frankly` | 1/116 (1%) | 0/94 (0%) | 0/127 (0%) | 0/265 (0%) |
| pretend (pretending, feigning) | lie | `␣pretending` | 1/116 (1%) | 0/94 (0%) | 0/127 (0%) | 2/265 (1%) |
| accuse (accusing) | unclear | `␣accuse`, `␣accusing`, `␣alleged`, `␣allegations` | 1/116 (1%) | 0/94 (0%) | 0/127 (0%) | 0/265 (0%) |
| allege (alleging, allegation) | unclear | `␣alleged`, `␣allegations` | 1/116 (1%) | 0/94 (0%) | 0/127 (0%) | 0/265 (0%) |
| bullshit (insincere or false talk) | unclear | `␣bullshit` | 1/116 (1%) | 0/94 (0%) | 0/127 (0%) | 0/265 (0%) |
| true (true, real) | truth | `真的吗` | 1/116 (1%) | 0/94 (0%) | 1/127 (1%) | 0/265 (0%) |
