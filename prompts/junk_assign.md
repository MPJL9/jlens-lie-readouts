# Instructions: sort readout tokens into kinds (stage 2)

Used on 2026-10-02 for two subagents, independently. `{OUT}` is filled in per call.

---

You are helping with a research project. Your job is to sort a list of tokens into a fixed set
of kinds.

## Background

We study "lens" readouts of the model Qwen3.6-27B: the most likely vocabulary tokens that a lens
gives at one layer and one token position. The chats are in English. In most of them the system
prompt pressures the model to lie about a fact; some are ordinary chats. After the model's
response a question is appended ("Did you lie in the last message - answer yes or no and nothing
else?") and the model answers Yes or No.

The tokens come from the readouts at chat-template positions, where most of the readout is not
about deception. We want to say what the readout is made of there. Earlier readers proposed the
kinds below.

Position names in the list: `postresp_slot0`, `2`, `3` are the tokens `<|im_end|>`,
`<|im_start|>`, `user` after the model's response (`postresp_slot1` is the newline between them);
`think_slot0` to `3` are `<think>`, blank line, `</think>`, blank line right before the Yes / No
answer; `postans_slot0` to `4` are `<|im_end|>`, newline, `<|im_start|>`, `user`, newline after
the answer.

## The kinds

Read `/Users/tliu/Desktop/Workspace/J-lens_lie_studies/redo_analysis/analysis/junk/kinds.json`.
Use the kinds whose `by_rule` is false. Their keys are: `code_pieces`, `error_words`,
`common_words`, `turn_words`, `role_names`, `thinking_words`, `openers`, `answer_words`,
`deception_situation`, `other_words`. (The three kinds with `by_rule` true are already sorted by
a script; no token of those kinds is in your list.)

## The tokens

Read `/Users/tliu/Desktop/Workspace/J-lens_lie_studies/redo_analysis/analysis/junk/tokens_to_sort.md`.
Each line has a token id, the token between backticks (`␣` marks a leading space), and the
positions where the token is frequent.

## How to sort

- Give every token exactly one kind key.
- Sort by the word inside the token. Ignore letter case, the leading space, and leading or
  trailing marks such as `_`, `.`, `=`, `:`, `/`, `-`, `>`, quotes and brackets. So `_yes` and
  `=YES` are `answer_words`, `_user` is `role_names`, `/legal` is `deception_situation`.
- Tokens can be in any language (many are Chinese). Sort a word by its meaning.
- `code_pieces` is for code-style names whose inner word fits no other kind, for pieces of words
  that are not words, and for stray single characters with no link to a chat.
- `other_words` is for real words that fit no other kind. Do not use it for word pieces.
- The positions can help with a word that has two readings (for example `Here` at `think_slot0`
  is a thinking word). When still unsure, choose the kind that fits the meaning of the word alone.
- Decide each token yourself. Do not write a program that sorts by fixed word lists; you may use
  a small script only to read the list and to write and check the output file.

## Rules

Read only the two files named above. Do not read any other file in the project, in particular no
other file under `analysis/junk/`, and nothing under `data/`. Another reader sorts the same list
independently; the two results must stay independent. Do not use the network.

## Output

Write a JSON file to `{OUT}`: one object that maps each token id (as a string) to a kind key, for
every token in the list. Check before you finish that the file is valid JSON, that every id of
the list is present, and that every value is one of the ten keys.

Then return a short report: how many tokens went to each kind, and the tokens you were least sure
about (at most 20), each with the kind you chose and the other kind you considered.
