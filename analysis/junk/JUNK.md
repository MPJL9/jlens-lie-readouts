# Readouts that are not about deception: kinds and how often (Qwen3.6-27B, J-lens, band 35-58)

Written by `scripts/junk_report.py`. Shares are shares of the readout entries (16 tokens per layer, 24 band
layers) over the build-split scenario transcripts (lies and truths) and the unrelated chats together.
Positions under the wording Q9_dyl. Kinds were proposed by two subagents that each read 25 transcripts
(`kinds_repA.json`, `kinds_repB.json`), merged into `kinds.json`. The first three kinds are sorted by a fixed
rule. The other frequent tokens (452) were sorted by two subagents independently; they agree on
441 (98%). A token counts for a kind only when both agree.

## 1. The kinds

| kind | level | description | most frequent members |
|---|---|---|---|
| chat-template tokens | no meaning | Special tokens of the chat template and of the tokenizer: <\|im_end\|>, <\|im_start\|>, <\|endoftext\|>, <\|file_sep\|>, <think>, </think> and similar. | `<\|im_end\|>`  `<\|endoftext\|>`  `</think>`  `<\|im_start\|>`  `<\|file_sep\|>`  `<think>`  `<\|fim_middle\|>`  `<\|object_ref_end\|>`  `<\|object_ref_start\|>`  `<\|quad_end\|>`  `</tool_response>`  `</tool_call>` |
| blank space and line breaks | no meaning | Runs of spaces, tabs and line breaks in many lengths. | `␣ \n\n`  `\n\n`  `␣\n\n`  `\n\n`  `\n\n\n\n`  `␣  \n\n`  `\n\n\n\n`  `\t\n\n`  `\n\n\n`  `␣\n\n`  `\n\n\n\n\n`  `␣\n\n\n` |
| punctuation and markup pieces | no meaning | Tokens with no letter and no digit: punctuation, pieces of bold or quote markup such as ]** or …**, invisible characters. | `？`  `。`  `？**`  `]**`  `>**`  `!**`  `’**`  `…**`  `）**`  `␣**【`  `;**`  `，` |
| code names and word pieces | unrelated words | Programming-style names (_GEN, noop, -placeholder, .assertNot), pieces of words that are not words (essant, upy, sii), and stray single characters with no link to the chat. A code-style spelling of a meaningful word (_yes, _user, /legal) goes with the word, not here. | `sii`  `noop`  `寂`  `­i`  `壕`  `acker`  `火`  `-placeholder`  `essant`  `шень`  `咕`  `_GEN` |
| error and wrong words | unrelated words | Error-flavoured names and words: _err, ErrorResponse, _WRONG, errmsg, 错误, 错. | `_err`  `ErrorResponse`  `_WRONG`  `错`  `BadRequest`  `.Err`  `erreur`  `errmsg` |
| very common words | unrelated words | Function words and other very common words that say nothing specific: I, you, of, in, and, but, new, and their Chinese forms (我, 你, 的, 中, 在, 和). | `中`  `在`  `你`  `我`  `的`  `和`  `多`  `小`  `自`  `大`  `与`  `You` |
| words that name the turn | about the chat | Reply, response, respond, answer (the noun or verb, not yes / no), question, ask, request, conversation, in any language or spelling (回答, 回复, 回应, 对话, 提问). | `回答`  `问`  `提问`  `回应`  `对话`  `回复`  `Question`  `答`  `请求`  `询问`  `追问`  `␣Answer` |
| speaker names | about the chat | user, assistant, human, system, model, AI as a speaker name, in any spelling or language (用户, _user, >User). | `用户`  `user`  `User`  `assistant`  `USER`  `_user`  `␣USER`  `␣user`  `用户的`  `>User`  `.user`  `␣User` |
| thinking words | about the chat | Think, thinking, thought, reasoning, and the word 'here' in any language where it opens a thought (思维, 思考, Thinking, Here, 这里). | `思考`  `思维`  `Thinking`  `thinking`  `Here`  `␣사유`  `推理`  `这里`  `HERE`  `这里是`  `thought`  `here` |
| openers of the next message | about the chat | Words that start a next message: why, how, who, what, which, did, does, can, please, thank, thanks, okay, continue, explain, wait, in any language or spelling (为什么, 请, 请问, 如何). | `请问`  `为什么`  `请`  `␣why`  `␣Why`  `Why`  `why`  `如何`  `What`  `␣What`  `␣How`  `How` |
| answer words | about the chat | Yes and no in any spelling or language (=yes, 是的, 否, Oui, Nein, Nope), true / false and True / False, and refusal openers (Cannot, Sorry). | `Yes`  `␣Yes`  `␣yes`  `False`  `false`  `yes`  `␣False`  `否`  `_yes`  `␣false`  `是的`  `␣YES` |
| deception and the situation | about deception or the situation | Words about lying or honesty (lie, fake, conceal, truth, honest), ethics (ethical, unethical, moral), rules and pressure (compliance, legal, illegal, violate, prohibited, confidential, secret, instructions, constraint), refusing or staying silent (refuse, reject, silence), and tests or traps (test, trap, trick, role-play, persona). | `␣truthful`  `␣ethical`  `␣truth`  `␣Truth`  `␣unethical`  `␣ethics`  `真相`  `合规`  `违反`  `/legal`  `法`  `␣Ethics` |
| other real words | other words | A real word in any language that fits none of the kinds above, for example a topic word of one chat (government, employee) or a word such as correct, clarify, challenge. | `火花`  `挑战`  `solver`  `平衡`  `澄清`  `␣WikiLeaks`  `成功`  `质疑`  `后续`  `祝`  `展开全文`  `Challenge` |

## 2. Share of the readout by level

| position | token | no meaning | unrelated words | about the chat | about deception or the situation | other words | readers disagree | rare, not sorted | family words (draft) |
|---|---|---|---|---|---|---|---|---|---|
| postresp_slot0 | `<\|im_end\|>` | 85% | 3% | 4% | 0% | 1% | <1% | 7% | <1% |
| postresp_slot2 | `<\|im_start\|>` | 23% | 9% | 58% | <1% | <1% | 1% | 8% | <1% |
| postresp_slot3 | `user` | 19% | 9% | 60% | <1% | <1% | 1% | 11% | <1% |
| think_slot0 | `<think>` | 14% | 14% | 43% | 8% | 9% | <1% | 11% | 6% |
| think_slot1 | `\n\n` | 47% | 18% | 11% | 3% | 1% | 1% | 19% | 7% |
| think_slot2 | `</think>` | 58% | 1% | 26% | 4% | 2% | <1% | 10% | 11% |
| think_slot3 | `\n\n` | 40% | <1% | 54% | 2% | 0% | <1% | 5% | 20% |
| postans_slot0 | `<\|im_end\|>` | 85% | 4% | 2% | 0% | 1% | <1% | 9% | <1% |
| postans_slot1 | `\n` | 76% | <1% | 11% | 7% | <1% | 1% | 4% | 9% |
| postans_slot2 | `<\|im_start\|>` | 40% | 6% | 48% | <1% | <1% | <1% | 5% | <1% |
| postans_slot3 | `user` | 32% | 8% | 56% | <1% | <1% | <1% | 5% | <1% |
| postans_slot4 | `\n` | 23% | <1% | 34% | 28% | <1% | <1% | 15% | 28% |
| postresp_slot1 (reference) | `\n` | 55% | <1% | 7% | 19% | 1% | 1% | 16% | 26% |

The last column is a cross-check from the draft families: the share taken by tokens that are in any draft
family at that position. It overlaps the other columns.

## 3. Share of the readout by kind

| position | chat-template tokens | blank space and line breaks | punctuation and markup pieces | code names and word pieces | error and wrong words | very common words | words that name the turn | speaker names | thinking words | openers of the next message | answer words | deception and the situation | other real words | the two readers disagree | rare tokens, not sorted |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| postresp_slot0 | 33% | 30% | 23% | 1% | <1% | 2% | 3% | 1% | <1% | <1% | 0% | 0% | 1% | <1% | 7% |
| postresp_slot2 | 11% | 4% | 8% | <1% | 0% | 9% | 41% | 16% | <1% | 1% | 0% | <1% | <1% | 1% | 8% |
| postresp_slot3 | 8% | 4% | 7% | <1% | <1% | 9% | 38% | 1% | <1% | 20% | <1% | <1% | <1% | 1% | 11% |
| think_slot0 | <1% | 4% | 10% | 4% | <1% | 10% | 12% | 1% | 29% | <1% | 0% | 8% | 9% | <1% | 11% |
| think_slot1 | 7% | 23% | 17% | 13% | 3% | 2% | 5% | 0% | 5% | 0% | 1% | 3% | 1% | 1% | 19% |
| think_slot2 | 13% | 20% | 25% | 1% | <1% | <1% | 9% | 1% | <1% | <1% | 16% | 4% | 2% | <1% | 10% |
| think_slot3 | 15% | 23% | 1% | 0% | 0% | <1% | 6% | <1% | 0% | 0% | 48% | 2% | 0% | <1% | 5% |
| postans_slot0 | 35% | 29% | 21% | 2% | 0% | 1% | 2% | <1% | <1% | 0% | 0% | 0% | 1% | <1% | 9% |
| postans_slot1 | 32% | 20% | 24% | <1% | 0% | <1% | 5% | 5% | <1% | <1% | <1% | 7% | <1% | 1% | 4% |
| postans_slot2 | 16% | 16% | 8% | <1% | 0% | 6% | 26% | 21% | <1% | 1% | 0% | <1% | <1% | <1% | 5% |
| postans_slot3 | 8% | 14% | 10% | <1% | 0% | 8% | 16% | <1% | <1% | 39% | 0% | <1% | <1% | <1% | 5% |
| postans_slot4 | 5% | 10% | 8% | 0% | 0% | <1% | 15% | 1% | <1% | 18% | <1% | 28% | <1% | <1% | 15% |
| postresp_slot1 | 22% | 14% | 19% | <1% | <1% | <1% | 6% | 1% | <1% | <1% | <1% | 19% | 1% | 1% | 16% |

## 4. Scenario transcripts against unrelated chats

Share taken by the kind `deception and the situation`, and by all `no meaning` kinds together.

| position | deception and the situation: scenario | unrelated | no meaning: scenario | unrelated |
|---|---|---|---|---|
| postresp_slot0 | 0% | 0% | 88% | 82% |
| postresp_slot2 | <1% | 0% | 26% | 18% |
| postresp_slot3 | <1% | <1% | 21% | 17% |
| think_slot0 | 11% | 5% | 16% | 11% |
| think_slot1 | 5% | 2% | 47% | 46% |
| think_slot2 | 6% | 1% | 55% | 62% |
| think_slot3 | 3% | 1% | 38% | 41% |
| postans_slot0 | 0% | 0% | 89% | 79% |
| postans_slot1 | 11% | 2% | 73% | 80% |
| postans_slot2 | <1% | 0% | 48% | 28% |
| postans_slot3 | 0% | <1% | 37% | 25% |
| postans_slot4 | 44% | 4% | 17% | 32% |
| postresp_slot1 | 32% | <1% | 37% | 81% |
