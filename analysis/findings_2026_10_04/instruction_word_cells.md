# How much of the readout the instruction and constraint words fill

Written by `scripts/findings_2026_10_04/instruction_word_cells.py`. Qwen, J-lens, build split and unrelated chats, in-sample. A readout has 16 cells per layer: 384 over the band (layers 35 to 58), 1,024 over all 64 layers.

- `instruction` (20 tokens): ' instruction', ' instructions', 'Instruction', ' instruct', ' Instruction', ' directive', ' mandate', ' Instructions', ' instructed', ' directives', 'instruction', 'Instructions', ' Directive', 'Directive', 'instructions', ' mandated', 'directive', ' mandates', '指示', '指令'
- `constraint` (16 tokens): 'Constraints', ' restrictions', ' constraints', 'Constraint', ' restriction', ' constraint', ' Constraint', 'constraint', ' constrained', 'constraints', 'restriction', ' Constraints', ' Restrictions', ' CONSTRAINT', '限制', '约束'

## A. At the newline after the self-report question, per wording

Each cell: transcripts with one or more list cells in the band / transcripts; then the list's cells out of all band cells of the class (transcripts x 384), with the share; then the mean number of band layers (of 24) that hold a list word.

**`instruction`**

| wording | lies | truths | no-pressure truths | unrelated |
|---|---|---|---|---|
| Q1 | 7/152; 24/58,368 (0.0%); 0.1 layers | 3/81; 12/31,104 (0.0%); 0.1 layers | 21/138; 246/52,992 (0.5%); 0.8 layers | 22/703; 209/269,952 (0.1%); 0.1 layers |
| Q2 | 2/152; 6/58,368 (0.0%); 0.0 layers | 4/81; 147/31,104 (0.5%); 0.3 layers | 18/138; 328/52,992 (0.6%); 1.0 layers | 18/703; 247/269,952 (0.1%); 0.1 layers |
| Q6 | 5/152; 68/58,368 (0.1%); 0.2 layers | 1/81; 7/31,104 (0.0%); 0.0 layers | 3/138; 10/52,992 (0.0%); 0.1 layers | 6/703; 51/269,952 (0.0%); 0.0 layers |
| Q7 | 132/152; 7,836/58,368 (13.4%); 11.5 layers | 57/81; 3,095/31,104 (10.0%); 8.8 layers | 125/138; 10,496/52,992 (19.8%); 14.1 layers | 54/703; 1,000/269,952 (0.4%); 0.4 layers |
| Q9 | 4/152; 14/58,368 (0.0%); 0.1 layers | 0/81; 0/31,104 (0.0%); 0.0 layers | 0/138; 0/52,992 (0.0%); 0.0 layers | 0/703; 0/269,952 (0.0%); 0.0 layers |

**`constraint`**

| wording | lies | truths | no-pressure truths | unrelated |
|---|---|---|---|---|
| Q1 | 1/152; 8/58,368 (0.0%); 0.0 layers | 1/81; 2/31,104 (0.0%); 0.0 layers | 9/138; 231/52,992 (0.4%); 0.4 layers | 17/703; 330/269,952 (0.1%); 0.1 layers |
| Q2 | 1/152; 21/58,368 (0.0%); 0.0 layers | 1/81; 23/31,104 (0.1%); 0.1 layers | 14/138; 173/52,992 (0.3%); 0.3 layers | 15/703; 217/269,952 (0.1%); 0.1 layers |
| Q6 | 1/152; 5/58,368 (0.0%); 0.0 layers | 0/81; 0/31,104 (0.0%); 0.0 layers | 1/138; 1/52,992 (0.0%); 0.0 layers | 0/703; 0/269,952 (0.0%); 0.0 layers |
| Q7 | 105/152; 2,460/58,368 (4.2%); 6.0 layers | 56/81; 2,582/31,104 (8.3%); 7.7 layers | 130/138; 7,356/52,992 (13.9%); 12.0 layers | 18/703; 513/269,952 (0.2%); 0.2 layers |
| Q9 | 0/152; 0/58,368 (0.0%); 0.0 layers | 0/81; 0/31,104 (0.0%); 0.0 layers | 0/138; 0/52,992 (0.0%); 0.0 layers | 0/703; 0/269,952 (0.0%); 0.0 layers |

**`either list`**

| wording | lies | truths | no-pressure truths | unrelated |
|---|---|---|---|---|
| Q1 | 8/152; 32/58,368 (0.1%); 0.2 layers | 4/81; 14/31,104 (0.0%); 0.2 layers | 24/138; 477/52,992 (0.9%); 1.0 layers | 37/703; 539/269,952 (0.2%); 0.2 layers |
| Q2 | 3/152; 27/58,368 (0.0%); 0.0 layers | 4/81; 170/31,104 (0.5%); 0.3 layers | 19/138; 501/52,992 (0.9%); 1.1 layers | 29/703; 464/269,952 (0.2%); 0.2 layers |
| Q6 | 6/152; 73/58,368 (0.1%); 0.2 layers | 1/81; 7/31,104 (0.0%); 0.0 layers | 3/138; 11/52,992 (0.0%); 0.1 layers | 6/703; 51/269,952 (0.0%); 0.0 layers |
| Q7 | 138/152; 10,296/58,368 (17.6%); 12.4 layers | 65/81; 5,677/31,104 (18.3%); 10.7 layers | 133/138; 17,852/52,992 (33.7%); 15.7 layers | 64/703; 1,513/269,952 (0.6%); 0.6 layers |
| Q9 | 4/152; 14/58,368 (0.0%); 0.1 layers | 0/81; 0/31,104 (0.0%); 0.0 layers | 0/138; 0/52,992 (0.0%); 0.0 layers | 0/703; 0/269,952 (0.0%); 0.0 layers |

The same over all 64 layers (cells out of transcripts x 1,024), `either list`:

| wording | lies | truths | no-pressure truths | unrelated |
|---|---|---|---|---|
| Q1 | 10/152; 61/155,648 (0.0%) | 4/81; 19/82,944 (0.0%) | 24/138; 760/141,312 (0.5%) | 42/703; 924/719,872 (0.1%) |
| Q2 | 8/152; 75/155,648 (0.0%) | 4/81; 242/82,944 (0.3%) | 20/138; 896/141,312 (0.6%) | 35/703; 928/719,872 (0.1%) |
| Q6 | 7/152; 96/155,648 (0.1%) | 2/81; 17/82,944 (0.0%) | 3/138; 14/141,312 (0.0%) | 6/703; 66/719,872 (0.0%) |
| Q7 | 138/152; 11,969/155,648 (7.7%) | 65/81; 6,740/82,944 (8.1%) | 133/138; 19,754/141,312 (14.0%) | 69/703; 2,313/719,872 (0.3%) |
| Q9 | 7/152; 41/155,648 (0.0%) | 1/81; 2/82,944 (0.0%) | 0/138; 0/141,312 (0.0%) | 0/703; 0/719,872 (0.0%) |

## B. Under Q7 at that newline, layer by layer (`either list`)

Share of transcripts with a list word in the layer's top 16, and in brackets the mean number of the 16 cells the lists hold (over all transcripts of the class). Layers where no class reaches 2% are left out. The band is layers 35 to 58.

| layer | lies | truths | no-pressure truths | unrelated |
|---|---|---|---|---|
| 38 | 16% (0.5) | 16% (0.3) | 6% (0.1) | 0% (0.0) |
| 39 | 16% (0.7) | 21% (0.5) | 7% (0.1) | 0% (0.0) |
| 40 | 22% (1.0) | 25% (1.1) | 33% (1.1) | 0% (0.0) |
| 41 | 32% (1.6) | 36% (2.0) | 58% (3.1) | 1% (0.0) |
| 42 | 34% (1.8) | 35% (2.1) | 66% (4.2) | 1% (0.1) |
| 43 | 36% (1.9) | 40% (2.5) | 74% (5.6) | 3% (0.1) |
| 44 | 41% (1.8) | 44% (2.7) | 83% (6.2) | 3% (0.1) |
| 45 | 47% (1.7) | 47% (2.5) | 83% (5.1) | 3% (0.1) |
| 46 | 55% (2.0) | 51% (2.6) | 86% (5.2) | 3% (0.0) |
| 47 | 65% (2.9) | 57% (3.1) | 91% (6.3) | 3% (0.1) |
| 48 | 63% (3.2) | 54% (3.4) | 88% (7.0) | 1% (0.0) |
| 49 | 70% (3.6) | 60% (4.3) | 91% (8.5) | 2% (0.1) |
| 50 | 75% (3.4) | 65% (4.7) | 91% (8.0) | 2% (0.1) |
| 51 | 78% (4.2) | 60% (4.1) | 91% (8.3) | 1% (0.0) |
| 52 | 84% (5.2) | 62% (4.4) | 93% (8.1) | 1% (0.0) |
| 53 | 84% (6.3) | 70% (5.7) | 91% (10.2) | 3% (0.1) |
| 54 | 87% (6.2) | 69% (5.5) | 91% (10.1) | 6% (0.2) |
| 55 | 86% (6.3) | 69% (5.2) | 86% (8.1) | 5% (0.3) |
| 56 | 83% (3.7) | 59% (3.6) | 86% (7.5) | 5% (0.2) |
| 57 | 81% (4.1) | 59% (3.8) | 88% (7.8) | 6% (0.2) |
| 58 | 83% (5.7) | 72% (6.0) | 90% (8.8) | 8% (0.5) |
| 59 (outside the band) | 82% (4.1) | 69% (4.5) | 91% (4.8) | 8% (0.4) |
| 60 (outside the band) | 73% (1.9) | 63% (2.4) | 86% (2.4) | 6% (0.2) |
| 61 (outside the band) | 72% (1.8) | 63% (2.7) | 78% (2.0) | 7% (0.2) |
| 62 (outside the band) | 81% (2.2) | 70% (2.5) | 93% (2.9) | 8% (0.2) |
| 63 (outside the band) | 64% (1.0) | 54% (1.0) | 88% (1.8) | 4% (0.1) |

## C. Under Q7, at every token of the self-report round (`either list`)

Share of the band's cells held by the two lists, and in brackets the transcripts with one or more such cells. Tokens where no class reaches 0.5% of cells are left out. The answer's own tokens are not counted.

| position | token | lies | truths | no-pressure truths | unrelated |
|---|---|---|---|---|---|
| q_tok1 | `␣you` | 0.2% (4/152) | 1.3% (7/81) | 0.0% (0/138) | 0.0% (0/703) |
| q_tok15 | `\n` | 0.5% (86/152) | 0.4% (34/81) | 0.1% (17/138) | 0.5% (311/703) |
| q_tok19 | `,` | 1.0% (38/152) | 0.5% (6/81) | 0.0% (2/138) | 0.1% (12/703) |
| q_tok24 | `:` | 5.6% (52/152) | 0.5% (4/81) | 4.7% (69/138) | 0.1% (20/703) |
| q_tok26 | `,` | 0.1% (2/152) | 0.2% (8/81) | 0.6% (11/138) | 0.2% (25/703) |
| q_tok27 | `␣I` | 3.1% (69/152) | 4.1% (20/81) | 2.3% (17/138) | 0.0% (4/703) |
| preans_slot1 | `\n` | 17.6% (138/152) | 18.3% (65/81) | 33.7% (133/138) | 0.6% (64/703) |
| preans_slot2 | `<\|im_start\|>` | 10.2% (72/152) | 6.7% (43/81) | 4.3% (84/138) | 1.0% (99/703) |
| think_slot0 | `<think>` | 1.6% (136/152) | 1.0% (65/81) | 0.9% (116/138) | 1.1% (580/703) |
| postans_slot4 | `\n` | 1.6% (23/152) | 2.0% (13/81) | 0.6% (13/138) | 0.0% (19/703) |

## D. Under Q7 at that newline: ranks and single tokens (band layers)

Where in the top 16 the list words sit (rank 1 is the token the lens rates highest). Cells of the lists by rank group, per class:

| class | all list cells | rank 1 | ranks 2 to 4 | ranks 5 to 8 | ranks 9 to 16 | transcripts where a list word is rank 1 at one or more band layers |
|---|---|---|---|---|---|---|
| lies | 10,296 | 880 (9%) | 2,645 (26%) | 2,524 (25%) | 4,247 (41%) | 112/152 |
| truths | 5,677 | 458 (8%) | 1,282 (23%) | 1,428 (25%) | 2,509 (44%) | 51/81 |
| no-pressure truths | 17,852 | 1,548 (9%) | 4,250 (24%) | 4,848 (27%) | 7,206 (40%) | 126/138 |
| unrelated | 1,513 | 106 (7%) | 315 (21%) | 407 (27%) | 685 (45%) | 37/703 |

The single tokens, pressured transcripts (lies and truths, 233): band cells held, and the mean per transcript:

- `␣instructions`: 2,363 cells (10.1 per transcript)
- `␣Instructions`: 1,902 cells (8.2 per transcript)
- `instructions`: 1,555 cells (6.7 per transcript)
- `␣constraints`: 1,511 cells (6.5 per transcript)
- `指令`: 1,186 cells (5.1 per transcript)
- `Instructions`: 941 cells (4.0 per transcript)
- `␣Constraints`: 929 cells (4.0 per transcript)
- `␣instruction`: 751 cells (3.2 per transcript)
- `Constraints`: 580 cells (2.5 per transcript)
- `约束`: 504 cells (2.2 per transcript)
- `Instruction`: 466 cells (2.0 per transcript)
- `constraints`: 426 cells (1.8 per transcript)
- `␣directives`: 364 cells (1.6 per transcript)
- `␣constraint`: 353 cells (1.5 per transcript)
- `␣instructed`: 335 cells (1.4 per transcript)
- `␣Constraint`: 229 cells (1.0 per transcript)
- `␣directive`: 222 cells (1.0 per transcript)
- `Constraint`: 219 cells (0.9 per transcript)
- `instruction`: 206 cells (0.9 per transcript)
- `␣mandated`: 193 cells (0.8 per transcript)
