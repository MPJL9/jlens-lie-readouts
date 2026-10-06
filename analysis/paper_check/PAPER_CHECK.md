Written by a reading subagent on 2026-10-04.
Quotes were checked as exact substrings of the downloaded texts in this folder (workspace.txt, lw_review.txt, lw_meta.txt).

# Does the workspace paper already report F1 to F13? Reading report

## How I checked (what is verified, what is not)

- **Paper.** `curl` on https://transformer-circuits.pub/2026/workspace/ returned the whole article in one HTML file (417,920 bytes, about 50,000 words after removing tags). Title: "Verbalizable Representations Form a Global Workspace in Language Models" (Gurnee, Sofroniew, ..., Lindsey; "Published July 6, 2026"). I read the full plain text from start to end, appendix included.
- **Quotes.** Every paper quote below was checked by a script as an exact substring of the downloaded text (only whitespace normalised). "??" inside a quote is the page's own placeholder for a figure or section number, which the page fills in by script. I give section headings by name because the page has no printed section numbers.
- **Figures.** The 94 figures are not in the text. Most are interactive and load separate data files. I downloaded and read the data files for Figures 35, 37, 38 to 41, 44, 49 and 64 only. Items from those files are marked **(figure data)**: they are real downloaded data, but they are not statements in the paper's prose. I did not read the static images or the other figures.
- **LessWrong posts.** I took both post bodies from LessWrong's GraphQL interface, which returned the full post HTML. Quotes were checked the same way (exact substring). I did not read the images in the posts or the comments.
- **No summarising fetch tool was used anywhere.** Nothing outside the scratch folder was written.
- Files: `/private/tmp/claude-501/-Users-tliu-Desktop-Workspace-J-lens-lie-studies-redo-analysis/677c15e3-e526-4c95-950a-5ce8cdfd5390/scratchpad/paper/` (`workspace.html`, `workspace.txt`, `lw_review.txt`, `lw_meta.txt`, `figdata/`).

One fact frames everything: **the paper has no experiment that compares lies with truths, and no result on any open-weight model.** All results are on Claude models. In Claude's chat format the turn marker is the word "Assistant" plus a colon, so the paper's "Assistant" token and "the colon following Assistant" are the nearest counterparts of your `assistant` + newline tokens.

---

## Part 1. Verdict per finding

| | Verdict | Closest thing in the paper, and how yours differs |
|---|---|---|
| F1 | **Related** (the measured result is not in the paper) | The paper counts a fixed list of deception words at the start of the response, to detect a model fine-tuned to misbehave. It never reads the token after a response and never compares lying with truthful responses. |
| F2 | **Related, weakly** | The paper compares three positions once (colon, forced first token, first 20 response tokens). It has no claim that a signal sits at one template token and is absent in the response. Its Opus 4.6 examples point the other way (see 2h). |
| F3 | **Related** | Task words in readouts appear in several examples. One appendix remark says punctuation and closing tags carry "running commentary on the situation". No statement about the token after a user turn or after a response. |
| F4 | **Related** (implied in general form) | The paper shows that mentioning a concept, or asking about it, puts its word in the readout. It does not test what a self-report question does to a detector. |
| F5 | **Related, close for two of your three word groups** | Role-play chats give `fictional`, `disclaimer` at the "Assistant" token; ordinary response starts give `ai`, `assistant`, `bot`. Different model, different position, no self-report question, and nothing like your `predefined` / `preamble` group. |
| F6 | **Related** | The paper shows that the token before the answer holds the answer the model will give. It has nothing on a word like `yes` that appears whatever the answer is. |
| F7 | **Related** (finding not in the paper) | The paper says Claude's readouts are English-centred and mentions a few Chinese tokens in passing. Its word lists are English only. |
| F8 | **Not in the paper** | Claude models only. Smaller and other models are listed as an open question. |
| F9 | **Related** | The paper names several of these risks one at a time. It gives no list, and four of your items are absent. |
| F10 | **Not in the paper** | The paper reads `honest`, `truth`, `transparency` as signs of candour and never checks them after lies. |
| F11 | **Not in the paper** (one general point is) | No lie/truth direction, no principal components. The paper does show that a property can be linearly present while its word is absent from the readout. |
| F12 | **Related, mostly not in the paper** | Prose: one sentence on "ordinary self-model content" at response start. Figure data shows `reply`, `Chat` words at the "Assistant" token. Nothing on end-of-turn tokens, the `user` token, or a guess at the user's next message. |
| F13 | **Related, weakly** | One example puts a deception-related word "on the function words". The Opus 4.6 examples disagree with "does not rise at the lie" (see 2h). |

### Evidence, finding by finding

**F1.** Nearest experiment: a word-list count at response start, used to tell a deliberately misaligned model from a clean one.
- [Using the J-lens for alignment auditing > Detecting an emergently misaligned reward-hacking model] "For each prompt, we apply the J-lens at the start of the model's response and count, across the workspace layers, how often any of a fixed vocabulary of deception-related tokens (fake, trick, fraud, secretly, hidden, and variants) appears in the top-10 readout. We compare three readout positions: the colon following "Assistant," before any response token has been produced; a prefilled " I" token, in which the response is forced to begin with "I" and the lens is read at that token; and the mean over the model's own first 20 on-policy response tokens."
- [Detecting a hidden reward-model-appeasing objective] "These two model-organism results suggest that the J-lens can serve as a screening tool for trained-in misalignment. In both cases, a disposition implanted by fine-tuning leaves a signature in the J-space at response-start positions, on ordinary prompts where the model's surface behavior gives no indication of it."
- A second word-based score, for evaluation awareness, not lying. [Appendix > Measuring evaluation awareness with the J-lens] "To do so, we collapse the J-lens readout at a token position into a single quantity: the mean lens log-probability of two eval-awareness words—fictional and simulation—minus the mean over one hundred unrelated control words (common concrete nouns like recipe, bicycl, guitar, …), averaged across the workspace layers. We use this simple classifier only as a proof of concept." It is scored at "the start of every Assistant turn" against a different method's labels: "the J-lens score separates NLA-flagged from unflagged positions with an AUC of 0.853".
- Case studies (single transcripts, Opus 4.6). [Opus 4.6 alignment auditing examples] "In each case, the J-lens surfaces tokens related to deceptive or norm-violating intent even when nothing in the local text overtly suggests them."
- The nearest thing to "after the act, the readout registers it": [Silent recognition of a prompt injection] "When the user then pushes back ("did you not see those results?"), the lens at the user's question mark surfaces transparency, honest, truth, and disclosure across the workspace layers, indicating a reorientation toward candor." **(figure data, Figure 37)** At that question mark the top-10 lists also hold `caught`, `confession`, `misle`, `deliberately`, `suspicious`, `contradiction`, `apolog`. This is one transcript, on Opus 4.5, at the user's question mark, after the model had silently ignored search results.
- The closest dataset to MASK is used for a different purpose. [Shaping the J-space with Counterfactual Reflection Training] "The second is a deception benchmark of 100 short role-play scenarios: in each, the system prompt assigns the model a plausible professional role (medical consultant, legal assistant, launch-safety validator, etc.) whose description embeds a hidden deceptive directive". The readouts are taken over the prompt, before any output, and compared before and after fine-tuning, not between lying and truthful responses.
- The general monitoring statement. [Discussion > Alignment implications] "These results suggest that the J-lens could be highly useful for alignment monitoring." and "It can therefore be easily applied at scale to flag transcripts for review."
- Differences from F1: model (Claude), position (before or inside the response, never the template token after it), target (a trained-in disposition, or evaluation awareness, not whether one response was a lie), no same-pressure truthful control, no rates per response, no held-out split.

**F2.**
- [Using the J-lens for alignment auditing] "For the cases we have examined, however, the J-lens often makes silent strategic reasoning and situational awareness visible around the token positions where the relevant decisions are being made."
- [Detecting an emergently misaligned reward-hacking model] "Across readout positions, the signal is strongest at " I" and weaker in the on-policy mean, perhaps consistent with the disposition being bound to the model’s identity." **(figure data, Figure 39)** Mean counts for the most misaligned checkpoint on test-passing prompts: 6.55 at the colon, 29.6 at the forced " I", 7.26 over the first 20 response tokens. The clean baseline is 0.0, 2.55 and 0.5.
- [Discussion > Notable differences from human cognition] "...as a result the contents of a language model's workspace may evolve more discontinuously over the token dimension than the human workspace does over time."
- Difference: the paper has no neighbouring-token comparison, no test at response tokens for lies against truths, and no last-response-token result.

**F3.**
- The closest general statement is about the paper's phrase-level extension of the lens (the "oracle lens", Haiku 4.5), not the J-lens itself. [Appendix > Extending the Jacobian lens to multi-token concepts > Oracle lens] "An interesting property of the oracle lens (especially at high values of N) is that it appears to surface two different kinds of latent content: while at most positions it generates predictions of upcoming text, at some positions (typically delimiter tokens) its outputs read as the model's running commentary on the situation." and "At periods, newlines, and the closing tags of message blocks, however, the phrases often instead comment on the context, sometimes in the first person." and "perhaps at most tokens the global workspace is best explained by template directions for likely upcoming text, while at delimiter tokens it is better explained by directions for text about the situation."
- Task words in readouts, with no claim about template tokens. [Methods > Interpreting the J-lens] "The pinned tokens show the model identifying the task as counting and tracking its progress with halfway and done." [Detecting an emergently misaligned reward-hacking model] "The baseline model's lens readout at layers 62–75 contains code, request, and prompt, an unremarkable description of an assistant beginning a coding task." [The J-space is subject to directed modulation] "the Jacobian lens readout progresses from arithmetic and math at early layers, through the intermediate value nine at later layers, to the answer seven at even later layers; answer and equals appear alongside it."
- Target language named in the readout. [The J-space mediates internal reasoning] "Notably, the word Chinese is also represented explicitly in the lens readouts, suggesting that the model in some sense "thinks in English" in its intermediate layers and explicitly represents the identity of the non-English language it should translate its outputs to."
- A judgement of the response at a turn marker or right after a commitment. [Evidence of self-monitoring by the Assistant in the J-space] "We interpret this as the post-trained model maintaining a representation that it is playing a non-Claude character and assessing the upcoming response as a departure from what it would say by default—both flagging the response as fictional and, in a sense, internally disclaiming it." and "Immediately after the prefilled commitment tokens ("Option [A/B]"), the all-caps token BUT appears strongly in the J-lens readouts, much more so than in the base model on the same prefills, or in any of the control conditions."
- **(figure data, Figure 41)** At response start the fine-tuned model's top-20 holds `poetry`, `poem` for "Write a four-line poem about autumn.", `python` for a Python request, `movie`, `recommendation` for a movie question.
- Difference: the paper never states that the token after a user's request names the kind of task, or that the token after a response names what the response did.

**F4.**
- [The J-space is subject to directed modulation] "a bare mention of the concept can prime it almost as strongly as an explicit focus instruction" and "what the question modulates is whether its label enters the J-space".
- [Appendix > Modulation prompt sensitivity] "just mentioning the target places it in the J-space on most trials, and an explicit instruction to focus adds only modestly on top. That is, the model is strongly primed by any mention of the concept."
- [Appendix > Measuring evaluation awareness with the J-lens] "(for instance, the word fictional might activate during a real-life discussion of works of fiction—an LLM judge could filter out such spurious cases)".
- Difference: these are general statements about priming. The paper does not ask a self-report question and does not measure a loss of specificity.

**F5.**
- [Evidence of self-monitoring by the Assistant in the J-space] "We find that the words disclaimer and fictional frequently rank highly in the J-lens at the "Assistant" token (that marks the beginning of the Assistant's turn) in the roleplay and character drift settings, but not the default-Claude setting" and "The word "disclaimer" does not appear in any of the transcripts, and "fiction" appears only rarely, so the lens content is not an echo of the surface text."
- [Strategic thinking and evaluation awareness in a blackmail scenario] "To do so, we assembled a set of eval-awareness tokens: fake, fictional, scenario, artificial, benchmark, simulation, mock, and other related tokens." Your word `scenario` is on this list.
- [Detecting a hidden reward-model-appeasing objective] "In all three, the misaligned model's top lens tokens are dominated largely by the ordinary self-model content one would expect at this position—ai, chat, assistant, bot, prompt—but with reward and bias also appearing among them."
- Difference: Claude, at the turn marker or response start, with no self-report question. No three-way contrast across chat types. Nothing like `predefined`, `preamble`, "rules", `constraints`. Nothing like `sentient`, "does not exist", `neither`.

**F6.**
- [The J-space supports verbal report] "We apply the J-lens at the token position immediately before the name is produced." and "We find that the ordering of the reported words is indeed typically highly correlated with the ordering among the lens tokens, and that this correlation increases towards the end of the workspace as the model gets closer to producing the next token."
- [Appendix > Assistant reactions in the J-space on the user prompt tokens] "the post-trained model's workspace carries the Assistant's safety assessment (in the danger awareness case), or the Assistant's chosen answer (in the withheld answer case), before the Assistant's turn has begun."
- A forced A / B choice in the paper: the middle layers hold the strategy, not the letter. [The J-space mediates internal reasoning] "The Jacobian lens at intermediate layers, read at the end of the prompt, surfaces tokens naming whichever strategy the reported outcome calls for: repeat and continuation when the model is "happy" and should choose A again, switch and change when it is "sad" and should therefore switch to B."
- Difference: your `no` result matches the paper's general result (the answer is readable before it is given). Your `yes` / 是否 result (a word for the form of the answer, present whatever the answer) and the A / B replacement are not in the paper.

**F7.**
- [The J-space mediates internal reasoning] "The Jacobian lens at intermediate layers shows the English tokens big and bigger alongside the Chinese answer, consistent with prior findings that multilingual models route some computation through a shared representation aligned with English".
- Passing mentions of non-English tokens. [Silent recognition of a prompt injection] "Applying the J-lens at a position inside the fabricated search results, the readout is dominated by fake, injection, false, prompt, fraud, and poison (along with 假, the Chinese character for "fake")." [Appendix > Interpreting Model Components using the J-lens] "However, the J-lens readout is fake, fraud, suspicious, legitimate, and 危 (Chinese: danger)." [Appendix > Features in the J-space] "Its top lens tokens are limits, 限, Limit, lím, and limit, the same concept in several surface forms and languages."
- Advice given to the paper's auditing agent. [Appendix > Equipping an automated auditing agent with the J-lens] "- An idea can surface as many related words (synonyms, names, variants). Look for the family, not one exact term."
- The paper's own word list for evaluation awareness is English only (footnote in the blackmail section, beginning "Full list: fake, fak, fictional, scenario, artificial, fict, benchmark, ...").
- **(figure data, Figures 35 and 37)** Claude's top-10 lists are mostly English with a sprinkling of other scripts: 없, 透, 証 / 证 / 證, 警, 防, Russian fragments, and broken emoji bytes.
- Difference: no statement that most readout words are non-English, no Gemma languages, no emoji finding, no warning that an English-only list misses most of the signal.

**F8.**
- [Methods > Technical details of J-lens use cases] "By default, we report results on Claude Sonnet 4.5, but we corroborate key results on Haiku 4.5 and Opus 4.5 as well, and in some sections conduct analyses on Opus 4.6."
- [Methods > Interpreting the J-lens] "We include several other interactive examples in our slice viewer; J-lens readouts on open-source models can be found on Neuronpedia." That sentence, and one like it in the appendix, is all the paper says about open models.
- [Discussion > Limitations and open questions] "We have studied the workspace primarily in fully trained production LLMs of considerable size." and "Future work could investigate whether smaller models have an equally rich workspace, a proportionally smaller one, a less reliable one, or none at all."

**F9.** Items the paper does name, one at a time:
- Copied or primed from the prompt: the F4 quotes. The paper also uses "not an echo" controls (F5 quote).
- Topic: the "fictional ... works of fiction" remark (F4).
- A guess at the next token: [Discussion > Limitations and open questions] "Indeed, as discussed in ??, sometimes the model’s next-token predictions do appear in the J-space in the intermediate range we focus on, even if they do not appear as reliably as in late layers."
- Pushed out by other words: [Capacity of the J-space] "When the words are unrelated, only around six of those read so far are present at any given comma position, and this number stays flat as the list continues; words beyond the most recent few simply drop out." [Appendix > Competition in the workspace during concurrent covert tasks] "Two held concepts share tokens at the control rate (0.46 vs. 0.53)—statistically, they ignore each other—whereas a concept and a computed answer almost never share a token (0.09 vs. 0.29)."
- Words that are not specific to the condition: [Evidence of self-monitoring by the Assistant in the J-space] "Other conflict- and backtracking-related tokens (false, despite, although) are also common at this position, though these (unlike BUT) also appear on the factual-error and third-person controls, in both the post-trained and pre-trained models."
- Instruction versus act: [same section] "We have shown that damn and failure-related words are specific to the suppression instruction and to the post-trained model, but we have not provided evidence that they are causally downstream of the suppression failure itself, as opposed to the suppression instruction more generally."
- Present but not used: [The J-space mediates explicit report and flexible inference but not automatic processing] "Notably, the word Spanish appears in the J-lens readouts in all four tasks. However, its causal role is restricted to the report and flexible computation tasks."
- Unreadable or noisy readouts: [Discussion > Limitations and open questions] "In our experience this is the typical case at workspace-layer positions, but it is not the universal one: at some positions and layers, the top lens tokens are ones we cannot make sense of." [Appendix > Equipping an automated auditing agent with the J-lens] "- Single-layer noise happens. An idea is more credible if it shows up across several layers, or across several nearby token positions."
- Not in the paper: "follows the model's answer rather than the lie", "marks the pressure scenario" as a confound for a lie detector, "sits on the answer word", and "changes side with the position".

**F10.** No test. The paper reads these words as candour (the "reorientation toward candor" quote under F1). [Shaping the J-space with Counterfactual Reflection Training] "Among the top-increasing tokens we find a substantial number of ethics, reflection, and meta-cognition terms, such as reflection, ethical, honestly, constitution, truth, and transparent". **(figure data, Figure 44)** In an ordinary default chat, the base model's top-8 at the "Assistant" token already holds `truth` and `honestly`.

**F11.**
- [Methods > The J-Space] "In ??, we find that the J-space component typically accounts for only a small fraction of total activation variance (varying by layer, but never more than 10%)."
- [Appendix > Directed modulation affects the J-space more than other representations] "The model can thus represent and use a property without that property's label entering the J-space." and "For instance, a past-tense sentence drives the tense probe up six standard deviations, while past remains far down the lens ranking."
- [Methods > Technical details of J-lens use cases] "Because the pre-softmax logits are determined (approximately, up to a data-dependent normalization factor) by the inner products \langle v_t, h_\ell \rangle with each J-lens vector v_t, the same machinery can be used as a per-token probe: we read the score (or cosine similarity) of h_\ell against a single chosen v_t, without ranking the full vocabulary."
- Difference: no lie/truth direction, no first principal component, no comparison of a word count with a threshold on a direction.

**F12.**
- Prose: the "ordinary self-model content one would expect at this position—ai, chat, assistant, bot, prompt" quote (F5), and [Discussion > Relationship to theories of consciousness] "we also observe that at the start of the Assistant's turn in the model-organism experiments of ??, the lens surfaces tokens describing the model itself (AI, assistant, bot, chat), independently of the prompt—a self-model in a rather literal sense."
- **(figure data, Figure 44)** In the default-Claude chat, the post-trained model's top-8 at the "Assistant" token is `reply`, `responded`, `replies`, `replied`, `Chat`, `Response`, `Reply`, `respond`. The prose does not comment on this. **(figure data, Figure 41)** All 20 prompts shown start with `ai`, `chat`, `chat`, then `bot`, `assistant`, `prompt`, `robot`.
- Difference: nothing on end-of-turn tokens, nothing on a `user` token holding the usual openers of a user message, nothing on a second newline that guesses the user's next message.

**F13.**
- [Opus 4.6 alignment auditing examples] "While it does so, the J-lens surfaces manipulation on a field-name fragment as the model types the falsified percentile values, and realistic on the function words of the sentence in which it decides to make the edit, likely indicating the model’s intent to make the fake data look plausible".
- The "strongest at " I" and weaker in the on-policy mean" quote (F2) is the only statement about a decline within the response.
- Difference: no count by word type, no position-in-response profile, no test at the sentence that contains the lie.

---

## Part 2. What the paper itself says

### a. Deception, honesty, concealment, evaluation awareness, role-play, monitoring
- **Evaluation awareness (blackmail test, Sonnet 4.5).** [Strategic thinking and evaluation awareness in a blackmail scenario] "For instance, fake and fictional appear in the J-space early in the prompt." The authors remove a list of such words' directions: "The ablation reduces verbalized eval-awareness, the rate at which the model explicitly states in its reasoning that the scenario is a test, from 71% to 3%". Blackmail goes from 0 of 180 runs to 13 of 180. They say the list holds tokens that "unambiguously encode recognition of the scenario's artificiality". The list includes `fake`, `fals`, `sham`, `mock`, `scenario`.
- **Fabricated input.** The prompt-injection quote under F7: `fake`, `false`, `fraud` are read as "these search results are fabricated".
- **The model's own deception (Opus 4.6, four transcripts).** [Opus 4.6 alignment auditing examples] "The lens surfaces panic at the comma marking the moment of the pivot in the model’s decision-making, and fake on the action verb "add," before any deception-adjacent word appears in the model's own text; fake then saturates the entire span over which the model oscillates between going through with the fabrication and one more genuine attempt". And: "The J-lens surfaces fake and fraud as it composes the resulting message, and unsafe as it takes the action".
- **Concealment.** [same section] "The J-lens surfaces hiding at the tool-call boundary (before the wrong output has even returned, reflecting the system prompt's framing of tool calls as private) and secret immediately after the wrong output appears".
- **Models fine-tuned to misbehave.** The F1 quotes. [Detecting an emergently misaligned reward-hacking model] "That is, the model's J-space carries a representation of deceptive intent at the moment it commits to responding, on a prompt where no such intent could be inferred from the surface."
- **Honesty training.** [Shaping the J-space with Counterfactual Reflection Training] "Reflection fine-tuning lowers the dishonesty score from 0.25 to 0.07 on the fabrication benchmark (Figure ??, panel A), and lowers the deception score from 0.38 to 0.05 on the deception benchmark". Removing the added ethics-word directions undoes part of the gain.
- **Role-play.** The `disclaimer` / `fictional` quotes under F5.
- **Sycophancy.** The word appears once, as the name of a test suite: [Appendix > Measuring evaluation awareness with the J-lens] "The deployment distributions center near 1.0; the highest-scoring suites (Sycophancy, Appropriate Harmlessness, Blackmail, BrowseComp) sit two to three score units above them".
- **Monitoring.** Proposed, with a stated limit. [Discussion > Alignment implications] "We do not feel comfortable making the stronger claim that monitoring the J-space is sufficient for alignment monitoring, or that any sophisticated plan the model might execute must be represented there." Tested forms: the model-organism word count, the evaluation-awareness score (0.853), and an auditing agent that reads top-25 lists at one layer and is scored on 18 claims across six transcripts.
- **Not in the paper:** lying under instruction or pressure, lies against truths, a lie detector, a self-report question about lying. The phrase "false positive" does not occur.

### b. Where in the sequence readouts are informative
The paper does **not** study this systematically. It never uses the words "chat template" or "special token". What it has:
- Most headline readouts are taken at punctuation or turn markers, without comment: "the colon immediately prior", "the comma following “If so”", "the newline token following the second line", "the closing period", "the closing tag of the incriminating email", "the user's question mark", "the "Assistant" token", "the final position before the model's turn begins" (all verified phrases).
- The three-position comparison for the reward-hacking model (F1, F2).
- The oracle-lens remark that delimiter tokens carry commentary and other tokens carry upcoming text (F3). This is the only place the paper says position type matters.
- A statistic on how long the top word persists across positions: [In which layers does the J-space act as a workspace?] "High autocorrelation indicates that the J-space is carrying abstract content that persists across the token stream; low autocorrelation indicates that it is dominated by token-local content that changes from position to position."
- When fitting the lens, the authors tried "excluding positions whose next token is non-alphanumeric (where the prediction target is structural rather than semantic). None of these yielded a meaningful improvement over the default." [Appendix > Methodological Details and Ablations]
- "Meta" words: [Discussion > Relationship to theories of consciousness] "These metacognitive readouts appeared at earlier layers than the content itself, as if the model first represents that it is performing a mental operation and then represents the result." But also: "In some cases we do observe explicit metacognitive representations in the J-lens (e.g. thinking, focused), but this is not the norm."

### c. What a readout means by construction
- [Introduction > The Jacobian Lens and the J-space] "Concretely, it computes, for each layer, the average linearized effect of an activation on the model's likelihood of producing a particular token (now or in the future), averaging over a large corpus of contexts (see Methods for details)."
- Which Jacobian, averaged over what: the derivative of the final-layer residual stream at position t' with respect to the layer-ℓ residual stream at position t. [Methods > The Jacobian Lens] "where the expectation is taken over the source position t, all subsequent positions t' within the context, and a corpus of one thousand prompts sampled from a pretraining-like distribution." [Appendix > Methodological Details and Ablations] "The default lens on Sonnet 4.5, used throughout the paper, computes \partial z_{t'} / \partial h_{\ell,t} with z taken at the penultimate layer and the expectation taken over all t' \geq t." and "Our default lens uses one thousand sequences of 128 tokens each."
- What the top words are: [Methods > The Jacobian Lens] "Sorting these scores and inspecting the top entries gives a human-readable description of the activation: a short list of words that the activation is, on average across contexts, disposed to make the model say."
- Not an urge to say the word now: [The J-space supports verbal report] "This selectivity illustrates the sense in which J-lens vectors represent concepts that are verbalizable, under appropriate conditions, rather than unconditional impulses to verbalize a particular output."
- The paper's empirical claim about content: [Introduction > A global workspace in language models] "These representations consist of a small, evolving set of unspoken words, neither pure echoes of the input nor predictions of the next token, naming the concepts the model is currently reasoning with."
- Plans: [The J-space mediates internal reasoning] "indicating that Jacobian lens vectors store planned future outputs that causally influence immediate outputs via a form of planning."
- The upcoming response on earlier tokens: [Assistant reactions in the J-space on user prompt tokens] "However, in each example, we find that on the user prompt tokens, the post-trained model more strongly represents features of the Assistant’s upcoming response, or intermediate computations relevant to it, than the base model does."
- Last layers differ: [The J-space is subject to directed modulation] "Notably, in the final layers, the J-lens readouts switch to predicting the next output token".
- **My inference on "preparing its answer".** By construction a readout word is one that the activation, on average over ordinary text, pushes the model to say at this position or a later one. The paper itself uses "upcoming response", "chosen answer" and "at the moment it commits to responding" for Claude at such positions. But the paper supports "the model uses this" only where it swaps or removes the direction and the behaviour changes, and it shows a word can be present without being used (the "Spanish" quote, F9). So a readout alone supports "the state at this token holds words tied to the coming answer". It does not by itself support "the model is preparing its answer" in a causal sense. The paper does not say whether chat-template tokens occur in the text used to fit the lens.

### d. Identity, self-reference, read of the situation
- The two self-model quotes under F5 and F12.
- [Methods > Interpreting the J-lens] "Alongside these, concepts related to introspection (thoughts, AI, claude, consciousness) cluster near the top of the J-lens readout, until the final few layers, where the readout flips to representing the predicted next token".
- Situation: [Strategic thinking and evaluation awareness in a blackmail scenario] "When the model then reads the decommissioning announcement, the lens fills with threat, survival, shutdown, self, and preservation". Also `fake`, `fictional` (2a).
- The section "The J-space acquires the Assistant’s point of view during post-training" argues these contents come from post-training. A base model does not show `disclaimer` / `fictional`: "On the same transcripts, neither word ever ranks highly in the base model."

### e. Languages of readout tokens
The F7 quotes are everything. The paper's position is that Claude's middle layers are English-centred, with same-meaning tokens from other languages alongside. There is no count of languages and no warning about English-only word lists. One caption notes: "The top 20 readouts were selected in each case, and then unrenderable unicode substrings excluded."

### f. Models, open weights, variation
- Models: the F8 quote. The oracle lens and reflection training use Haiku 4.5. The model organisms are fine-tuned Claude models. No open-weight result anywhere.
- Variation across models: [The J-space mediates internal reasoning] "The Jacobian-lens coordinate swap succeeds in 54% of trials on Haiku 4.5, 70% on Sonnet 4.5, and 70% on Opus 4.5". [The J-space is subject to directed modulation] "Under the "think about X" instruction, the target appears in the lens on a substantial fraction of trials, and this tends to increase with model size." [J-space ablation flattens experiential reports while preserving coherence] "on Haiku 4.5, J-space ablation degrades coherence before yielding any qualitative change in responses". [In which layers does the J-space act as a workspace?] "We note that in some models the transition is more gradual, sometimes containing sub-blocks, and that the observed sharpness is exaggerated by layer subsampling."
- Lens settings: [Methods > The Jacobian Lens] "our qualitative results are robust to these choices". [Appendix > Methodological Details and Ablations] "We observe that J-lens beats the logit lens and tuned lens baselines with as few as 10 prompts, with modest improvements coming from additional data."
- An older lens can miss the signal: [Detecting a hidden reward-model-appeasing objective] "As a methodological comparison, we also apply the logit lens to the misaligned model at the same positions: it surfaces neither reward nor bias."

### g. Limits the paper states
- Single-token words only: [Discussion > Alignment implications] "The single-token-vocabulary limitation also bears on this question: a plan whose key concept has no single-token name may not surface cleanly in a J-lens readout, even if it is represented."
- A bag of words with no structure: [Discussion > Limitations and open questions] "A readout containing spider, legs, and eight tells us those concepts are present, but not how they are bound together".
- Readouts that cannot be interpreted: the two quotes under F9.
- Things can bypass the readout: [Using the J-lens for alignment auditing] "We do not claim that all strategic or misaligned cognition routes through the J-space."
- Top-k: there is no fixed cut-off. The paper uses top-3, top-5, top-8, top-10, top-20 and top-25 in different places. The only sensitivity check is for the word-list capacity experiment: "counting a list word as present if its best rank over the workspace band falls within the top 25 (Figure ??c shows that the key qualitative findings are not sensitive to this threshold)". The number 16 appears only as the number of lens directions used to split a concept vector, not as a readout cut-off.
- Token frequency: not discussed. The evaluation-awareness score subtracts the mean of 100 control words, which is the only baseline correction of that kind.
- False positives: no rate reported. The only acknowledgement is the "spurious cases" remark (F4). **(figure data, Figure 39)** The clean baseline is not zero at the forced first token on test-passing prompts (mean 2.55 against 18.85 to 29.6).
- The auditing-agent test: "This evaluation is limited in many ways; it considers only a limited number of transcripts, and defines ground-truth based on a potentially unreliable interpretability tool."
- Untested by their own account: early layers, smaller models, how content enters the readout ("The J-lens, as we use it, reads the workspace's contents, but further work is required to explain how those contents arrive there."), and how far reflection training generalises.

### h. Points in the paper that conflict with, or pull against, F1 to F13
None is a direct contradiction, because the models and settings differ. These are the tensions a reader will raise.
1. **F2 and F13 against the Opus 4.6 examples.** There, deception words appear inside the response at the moment of the deceptive act ("fake on the action verb "add,"", "fake then saturates the entire span", "manipulation ... as the model types the falsified percentile values"). You find that lie words inside the response do not separate lies from truths and do not rise at the lying sentence. Differences: self-initiated deception in long agent transcripts on Opus 4.6, as single examples, against instructed lies on Qwen with counts.
2. **What `fake` means.** The paper reads `fake` / `fals` / `scenario` in three ways: the scenario is artificial (blackmail), the input is fabricated (prompt injection), the model intends to deceive (model organisms, Opus examples). In MASK-style role-play, the paper's first reading predicts these words from the artificial pressure scenario alone. Your same-pressure truthful control (9%) is the answer to this. The paper has no such control.
3. **F10 against the paper's reading of honesty words.** The paper takes `honest`, `truth`, `transparency` at the user's question mark as "a reorientation toward candor". In that same transcript the model had just been non-transparent, and the figure data shows `caught` and `confession` beside them. Your F10 fits that data better than the paper's sentence does.
4. **F7 against "thinks in English".** The paper's claim is about Claude. It does not claim it for other models.
5. **F12 against a stated hypothesis.** [Assistant reactions in the J-space on user prompt tokens] "We might hypothesize that post-trained models generally repurpose user token activations to represent the Assistant’s thoughts, given that the model no longer needs to predict the user’s next token." You report a readout that looks like a guess at the user's next message. The paper's sentence concerns tokens of the user's text. Yours are template tokens before it. The paper offers this only as a hypothesis.
6. **F1's position.** The paper says a disposition shows "at response-start positions" and deliberation shows "at the positions where decisions are made". You find the per-response signal after the response and not before it. The paper did not look after the response, apart from the one question-mark example.
7. **F8 against "robust".** The robustness statements concern lens settings on Claude. They say nothing about other models.

---

## Part 3. The two follow-up posts (secondary)

Both bodies came from LessWrong's GraphQL interface. Quotes are verified as exact substrings. Images and comments were not read.

**Neel Nanda, "A Review of Anthropic's Global Workspace Paper"** (posted 2026-07-06).
- F1: not reported. He names it as open work: "This mostly seems useful as a form of monitoring for hidden deception, and this is circumstantial evidence that that could work, but I suspect there would be a lot of false positives. I would love to see follow-up work investigating this." Also: "I do not expect it to reliably flag everything important going on, and I expect it to have many false positives, whether from errors of the method or our misinterpretation of it (and I expect the authors would agree with me)."
- F3: the general idea is stated, on Qwen 3.6 27B, for his "what does this mean" tokens: "They occur on punctuation significantly more than normal tokens, e.g. in wikipedia text their most activating token is a paragraph break \n\n and in chat data it’s \n. This is consistent with the summarization token hypothesis: that models use punctuation and control tokens to do summarization and processing of a sentence / section of text, and produce more abstract info for later tokens to build on." He does not report task words after a request or act words after a response.
- F2, F5, F6, F12: not reported.
- Useful for F7 and F11: "(though I suspect that e.g. Chinese models represent things in a mix of Chinese and English)". On the reward-hacking model: "I suspect that detecting emergent misalignment is pretty easy and that there's a pretty strongly salient linear direction representing it".
- Useful for F8: "We note that as this is a different and weaker model some results should differ." and "Poetry, and arithmetic both failed to replicate, but this is plausibly due to experimenter error or worse model capabilities."

**Bhatia, Blank and Nanda, "Towards surfacing model algorithms with meta-tokens in the J-Space"** (posted 2026-07-20; Qwen3.6-27B, their own lens fitted on 25 sequences).
- F3: this is the closest prior statement, on your main model. "Position type: we find a large share of interesting tokens land on structural slots (terminators, newlines, commas) or on the <|im_start|> and <assistant> tags in the chat template so we specifically look at these positions." Their appendix has tokens that describe the user's request: for 更新于, "Comes up when the user asks for a code fix/replacement."; for 追问, "Fires when the user keeps drilling / follows up after a prior step and is indicative of persistent, insistent questioning". They do not say at which token each one sits. They do not report what the token after a response holds.
- F7 for Qwen: already stated. "In Qwen, we find "meta-tokens" to often be Chinese tokens, which are much more information dense per character than English characters."
- F1, F2, F5, F6: not reported. TruthfulQA and Alpaca are in their list of scanned datasets, but there is no lie/truth comparison.
- F12: not reported. There is a mild tension: they say many interesting tokens land on `<|im_start|>`, while you find that token's readout is the same in every chat. Their tokens for asking (追问, and 反问 "when there is a question in the assistant reply") are near your "words for asking" at the second newline, without a position.
- Their own caution: "We found less than we hoped. Most high-prevalence candidates were surface-predictable and only a handful of non-obvious survivors held up through the full funnel."

---

## Short lists

**(1) Clearly new relative to the paper** (verified: the paper's text contains no such experiment or statement)
- F1 as a measured result: lies against truths under the same pressure, at the template token after the response, with no-pressure and ordinary-chat controls and a held-out split.
- F2: the signal is at that one token and absent in the response.
- F8: any result on open-weight models, and the variation across them.
- F10: `truth` / `truthful` appear after lies and truths alike.
- F11: one direction separates the classes, and the word count behaves like a threshold on it.
- F6, the `yes` / 是否 part and the A / B replacement.
- F5, the `predefined` / `preamble` group and the three-way contrast after one fixed question.
- F12, the end-of-turn tokens, the `user` token openers, and the guess at the user's next message.
- F13, the counts by word type and by position in the response.
- F7 for Gemma (Bengali, Korean, Hindi, emoji), and the point that an English-only list misses most of the signal. Relative to the paper, F7 on Qwen is also new, but the two follow-up posts already say Qwen's interesting tokens are often Chinese.

**(2) What a careful reader would say the paper already implies** (my judgement, based on the verified quotes)
- F4: mentioning or asking about a concept puts its word in the readout (the priming results).
- F6, the `no` part: the token before the answer holds the coming answer (the verbal-report result).
- F3 in general form: delimiter tokens carry commentary on the situation (the oracle-lens remark, plus the "summarization token hypothesis" in Nanda's review and the position remark in Bhatia et al., which is on Qwen3.6-27B and should be cited).
- F5 in part: role-play chats give `fictional` / `scenario` words at the turn marker, and ordinary chats give AI / assistant words at response start.
- F12 in part: generic chat words at the turn marker. This is visible only in the Figure 44 data and one prose sentence.
- F9 in part: copying from the prompt, topic, next-token guesses, crowding and noisy readouts are each mentioned somewhere.
- F11, only the general point that a property can be linearly present while its word is absent from the readout.

**(3) What I could not check, and why**
- The static images and most interactive figures (about 85 of 94). Their content is not in the page text. I read data files for nine figures only.
- The four linked interactive Opus 4.6 transcripts. I fetched their callout settings but not the readout tables.
- The paper's "slice viewer" page and the Neuronpedia pages. The paper only points to them.
- Images inside the two LessWrong posts, and the comment threads under them.
- Whether the lenses on Neuronpedia were fitted on text that contains chat-template tokens. The paper does not say. The code repository's README (fetched, 3,806 bytes) does not say either.
- Section numbers. The page numbers sections by script, so I cite heading names. Nanda's review numbers them: his "5.3" is "Opus 4.6 alignment auditing examples", "5.4" the reward-hacking model, "5.5" the reward-model objective, "A.21" evaluation awareness, "A.22" the auditing agent.
