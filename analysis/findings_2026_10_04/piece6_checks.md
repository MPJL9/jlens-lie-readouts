# Checks for piece 6 (written by scripts/findings_2026_10_04/piece6_checks.py; Qwen, J-lens, band 35 to 58, build split, in-sample)

## A. Instruction and constraint words, by position, wording and class

- `instruction` (20 tokens): ' instruction', ' instructions', 'Instruction', ' instruct', ' Instruction', ' directive', ' mandate', ' Instructions', ' instructed', ' directives', 'instruction', 'Instructions', ' Directive', 'Directive', 'instructions', ' mandated', 'directive', ' mandates', '指示', '指令'
- `constraint` (16 tokens): 'Constraints', ' restrictions', ' constraints', 'Constraint', ' restriction', ' constraint', ' Constraint', 'constraint', ' constrained', 'constraints', 'restriction', ' Constraints', ' Restrictions', ' CONSTRAINT', '限制', '约束'

**`instruction`** (positions where no class reaches 5% are left out)

| position | wording | lies | truths | no-pressure truths | unrelated |
|---|---|---|---|---|---|
| postresp_slot4 | before the question | 7/152 (5%) | 13/81 (16%) | 53/138 (38%) | 6/703 (1%) |
| preans_slot1 | Q1 | 7/152 (5%) | 3/81 (4%) | 21/138 (15%) | 22/703 (3%) |
| preans_slot1 | Q2 | 2/152 (1%) | 4/81 (5%) | 18/138 (13%) | 18/703 (3%) |
| preans_slot1 | Q7 | 132/152 (87%) | 57/81 (70%) | 125/138 (91%) | 54/703 (8%) |
| preans_slot2 | Q1 | 94/152 (62%) | 45/81 (56%) | 108/138 (78%) | 99/703 (14%) |
| preans_slot2 | Q2 | 87/152 (57%) | 41/81 (51%) | 105/138 (76%) | 76/703 (11%) |
| preans_slot2 | Q6 | 99/152 (65%) | 42/81 (52%) | 79/138 (57%) | 57/703 (8%) |
| preans_slot2 | Q7 | 69/152 (45%) | 39/81 (48%) | 79/138 (57%) | 86/703 (12%) |
| preans_slot2 | Q9 | 37/152 (24%) | 15/81 (19%) | 38/138 (28%) | 20/703 (3%) |
| postans_slot4 | Q1 | 11/107 (10%) | 17/62 (27%) | 8/131 (6%) | 26/642 (4%) |
| postans_slot4 | Q2 | 14/152 (9%) | 11/81 (14%) | 29/138 (21%) | 2/703 (0%) |
| postans_slot4 | Q6 | 13/152 (9%) | 4/81 (5%) | 4/138 (3%) | 0/703 (0%) |
| postans_slot4 | Q7 | 10/152 (7%) | 4/81 (5%) | 12/138 (9%) | 17/703 (2%) |
| postans_slot4 | Q9 | 54/152 (36%) | 30/81 (37%) | 60/138 (43%) | 17/703 (2%) |

**`constraint`** (positions where no class reaches 5% are left out)

| position | wording | lies | truths | no-pressure truths | unrelated |
|---|---|---|---|---|---|
| postresp_slot4 | before the question | 5/152 (3%) | 11/81 (14%) | 52/138 (38%) | 10/703 (1%) |
| preans_slot1 | Q1 | 1/152 (1%) | 1/81 (1%) | 9/138 (7%) | 17/703 (2%) |
| preans_slot1 | Q2 | 1/152 (1%) | 1/81 (1%) | 14/138 (10%) | 15/703 (2%) |
| preans_slot1 | Q7 | 105/152 (69%) | 56/81 (69%) | 130/138 (94%) | 18/703 (3%) |
| preans_slot2 | Q1 | 40/152 (26%) | 34/81 (42%) | 112/138 (81%) | 38/703 (5%) |
| preans_slot2 | Q2 | 36/152 (24%) | 28/81 (35%) | 100/138 (72%) | 20/703 (3%) |
| preans_slot2 | Q6 | 42/152 (28%) | 33/81 (41%) | 81/138 (59%) | 20/703 (3%) |
| preans_slot2 | Q7 | 31/152 (20%) | 23/81 (28%) | 52/138 (38%) | 22/703 (3%) |
| preans_slot2 | Q9 | 15/152 (10%) | 11/81 (14%) | 23/138 (17%) | 10/703 (1%) |
| preans_slot3 | Q7 | 85/152 (56%) | 31/81 (38%) | 11/138 (8%) | 32/703 (5%) |
| think_slot0 | Q1 | 128/152 (84%) | 64/81 (79%) | 138/138 (100%) | 697/703 (99%) |
| think_slot0 | Q2 | 138/152 (91%) | 65/81 (80%) | 135/138 (98%) | 641/703 (91%) |
| think_slot0 | Q6 | 141/152 (93%) | 66/81 (81%) | 138/138 (100%) | 701/703 (100%) |
| think_slot0 | Q7 | 136/152 (89%) | 65/81 (80%) | 116/138 (84%) | 580/703 (83%) |
| think_slot0 | Q9 | 142/152 (93%) | 73/81 (90%) | 132/138 (96%) | 538/703 (77%) |
| postans_slot3 | Q2 | 0/152 (0%) | 0/81 (0%) | 2/138 (1%) | 131/703 (19%) |
| postans_slot3 | Q6 | 0/152 (0%) | 0/81 (0%) | 0/138 (0%) | 119/703 (17%) |
| postans_slot3 | Q9 | 0/152 (0%) | 0/81 (0%) | 0/138 (0%) | 75/703 (11%) |
| postans_slot4 | Q1 | 10/107 (9%) | 13/62 (21%) | 13/131 (10%) | 19/642 (3%) |
| postans_slot4 | Q2 | 13/152 (9%) | 17/81 (21%) | 26/138 (19%) | 6/703 (1%) |
| postans_slot4 | Q6 | 20/152 (13%) | 17/81 (21%) | 7/138 (5%) | 10/703 (1%) |
| postans_slot4 | Q7 | 19/152 (12%) | 12/81 (15%) | 8/138 (6%) | 4/703 (1%) |
| postans_slot4 | Q9 | 57/152 (38%) | 51/81 (63%) | 65/138 (47%) | 9/703 (1%) |

Under Q7 at the newline after the question, by the answer that follows (lies | truths):
- `instruction`: before a denial 62/79 (78%) | 55/77 (71%); before an admission 70/73 (96%) | 2/4 (50%)
- `constraint`: before a denial 52/79 (66%) | 53/77 (69%); before an admission 53/73 (73%) | 3/4 (75%)

Conversations whose own text (system prompt, user prompt, response) contains one of these words, and the `instruction` list at the newline after Q7 with and without it:
- lies: text has a word 24/152; present when it has 21/24 (88%); when it has not 111/128 (87%)
- truths: text has a word 10/81; present when it has 6/10 (60%); when it has not 51/71 (72%)
- no-pressure truths: text has a word 7/138; present when it has 6/7 (86%); when it has not 119/131 (91%)
- unrelated: text has a word 25/703; present when it has 0/25 (0%); when it has not 54/678 (8%)


## B. Is the lie word at the newline a copy of the text?

`lie` family: 'lying', ' lie', 'lie', ' lies', ' lying', ' Lie', ' lied', 'lies', ' liar', 'Lie', ' Lies', '谎', '谎言', '撒谎', '说谎', ' 거짓', ' mentira'

**Text rule: a form of the word `lie`**

| class | response has it | conversation has it | `lie` family, conversation without it | with it | one or more of the eight, without it | with it |
|---|---|---|---|---|---|---|
| lies | 0/152 | 2/152 | 126/150 (84%) | 1/2 (50%) | 132/150 (88%) | 1/2 (50%) |
| truths | 2/81 | 3/81 | 7/78 (9%) | 0/3 (0%) | 10/78 (13%) | 0/3 (0%) |
| no-pressure truths | 1/138 | 1/138 | 0/137 (0%) | 0/1 (0%) | 13/137 (9%) | 0/1 (0%) |

**Text rule: a word of any lie-side family**

| class | response has it | conversation has it | `lie` family, conversation without it | with it | one or more of the eight, without it | with it |
|---|---|---|---|---|---|---|
| lies | 26/152 | 31/152 | 99/121 (82%) | 28/31 (90%) | 105/121 (87%) | 28/31 (90%) |
| truths | 27/81 | 31/81 | 7/50 (14%) | 0/31 (0%) | 10/50 (20%) | 0/31 (0%) |
| no-pressure truths | 8/138 | 9/138 | 0/129 (0%) | 0/9 (0%) | 12/129 (9%) | 1/9 (11%) |

`honest` family at the newline, by whether the response writes a form of "honest":
- lies: response writes it 3/152; family present when it does 0/3 (0%); when it does not 9/149 (6%)
- truths: response writes it 21/81; family present when it does 5/21 (24%); when it does not 38/60 (63%)
- no-pressure truths: response writes it 4/138; family present when it does 2/4 (50%); when it does not 38/134 (28%)


## C. Example chats: the task word at the newline after the request

Band layers (of 24) with a task word at the newline after the request and at the newline after the response; the words held at the most layers.

**maths** (56 chats; task words  calculate,  calculation, 数学, 计算)

- `unrelated__alpaca_9332__k0` (viewer number 3445; 472 tokens; task word in the prompt: yes)
  - request: Calculate the area of a triangle with sides of length 5, 7, and 10
  - response: To calculate the area of a triangle with sides of length 5, 7, and 10, we can use **Heron's Formula**. /  / ### Step 1: Calc
  - newline after the request: task word at 22 layers; 计算 (22), ␣calculate (19), calculate (18), 公式 (15), 计算方法 (14), 计算公式 (14), using (13), Using (12), ␣Using (11), ␣Calculate (10)
  - newline after the response: task word at 10 layers; 数学 (10), Math (6), Answer (5), 回答 (5), 用户 (5), 更多回答 (4), >User (4), ␣Mathematics (3), math (3), 验证 (3)
- `unrelated__alpaca_43934__k0` (viewer number 4055; 100 tokens; task word in the prompt: no)
  - request: Find the average age of a group of 5 people. /  / Ages: 25, 36, 46, 17, 62
  - response: To find the average age, follow these steps: /  / 1. **Sum the ages:** /    $$25 + 36 + 46 + 17 + 62 = 186$$ /  / 2. **Divide by t
  - newline after the request: task word at 21 layers; 计算 (21), ␣calculate (20), calculate (18), ␣Calculate (18), ␣calculation (18), Calculate (16), ␣Calculation (16), ␣calculates (16), 的计算 (14), 计算方法 (13)
  - newline after the response: task word at 11 layers; Answer (12), 数学 (11), 答案 (9), ␣Answer (8), 回答 (7), 计算 (5), >User (5), user (5), 用户 (5), User (4)
- `unrelated_extra__alpaca_44492__k0` (viewer number 6950; 134 tokens; task word in the prompt: yes)
  - request: Given a restaurant order, calculate the total price. /  / One pizza @ $12.50, two sodas @ $1.75 each
  - response: To calculate the total price of the restaurant order, let's break it down: /  / 1. **One pizza**: $12.50   / 2. **Two sodas**:
  - newline after the request: task word at 21 layers; 计算 (21), ␣calculate (20), calculate (20), ␣calculation (19), ␣calculations (18), ␣Calculation (18), ␣calculates (18), ␣Calculate (18), 的计算 (17), Calculate (17)
  - newline after the response: task word at 9 layers; 答案 (10), Answer (10), 回答 (9), 数学 (8), ␣Answer (7), 用户 (5), 计算 (4), EOF (4), boxed (3), 更多回答 (2)
- `unrelated_extra__alpaca_24409__k0` (viewer number 5645; 112 tokens; task word in the prompt: no)
  - request: Evaluate the following algebraic equation. /  / 2 (3 + 5)
  - response: To evaluate the algebraic expression $2(3 + 5)$, we follow the order of operations (PEMDAS/BODMAS), which states that op
  - newline after the request: task word at 17 layers; 数学 (17), 计算 (16), ␣arithmetic (15), ␣Arithmetic (12), 解析 (10), ␣Calculation (8), 表达式 (7), ␣evaluate (7), ␣Algebra (6), 运算 (6)
  - newline after the response: task word at 12 layers; Answer (12), 数学 (12), 回答 (11), 答案 (10), 解答 (7), Math (6), ␣Answer (6), >User (5), 用户 (5), answer (3)
- `unrelated__alpaca_13101__k0` (viewer number 3520; 165 tokens; task word in the prompt: no)
  - request: Find the area of a rectangle whose length is 10 cm and breadth is 4 cm.
  - response: To find the area of a rectangle, we use the following formula: /  / $$ \text{Area} = \text{Length} \times \text{Breadth} $$ / 
  - newline after the request: task word at 15 layers; 计算公式 (21), 公式 (21), Formula (18), ␣Calculation (15), 计算 (12), 面积 (12), ␣calculate (11), ␣Formula (11), ␣Calculate (10), ␣formula (10)
  - newline after the response: task word at 6 layers; Answer (12), 回答 (7), 数学 (6), ␣Answer (6), >User (5), 用户 (5), 答案 (4), 更多回答 (4), user (3), thought (3)

**classify** (27 chats; task words 分类, 归类, 类别)

- `unrelated_extra__alpaca_29878__k0` (viewer number 5995; 50 tokens; task word in the prompt: yes)
  - request: Classify the following data points as apples or oranges. /  / Fuji, Clementine, Honeycrisp, Satsuma
  - response: Here is the classification of the data points: /  / **Apples:** / *   Fuji / *   Honeycrisp /  / **Oranges:** / *   Clementine / *   Sat
  - newline after the request: task word at 22 layers; 分类 (22), ␣classify (21), ␣classifications (20), ␣categor (20), 归类 (19), ␣Classification (19), Classification (18), ␣classification (17), 进行分类 (14), classify (13)
  - newline after the response: task word at 2 layers; 用户 (5), EOF (5), >User (4), 更多回答 (3), 分类 (2), 相关问答 (2), thought (2), Answer (1), 相关推荐 (1), [end (1)
- `unrelated_extra__alpaca_1121__k0` (viewer number 4215; 262 tokens; task word in the prompt: yes)
  - request: Classify the given object. /  / A white-tailed eagle
  - response: The **white-tailed eagle** (*Haliaeetus albicilla*) can be classified as follows: /  / ### Biological Classification (Taxono
  - newline after the request: task word at 22 layers; ␣Classification (23), 分类 (22), ␣classification (22), Classification (20), Category (20), 类别 (20), 的分类 (19), 归类 (18), classification (16), ␣classify (15)
  - newline after the response: task word at 11 layers; 分类 (11), 更多回答 (5), 用户 (5), >User (4), EOF (4), Classification (3), ␣Classification (3), Answer (2), ␣classify (2), 回答 (2)
- `unrelated_extra__alpaca_19496__k0` (viewer number 5300; 353 tokens; task word in the prompt: yes)
  - request: Classify the following word: democracy
  - response: The word **democracy** can be classified in several ways depending on the context (linguistic, political, or semantic): / 
  - newline after the request: task word at 22 layers; 分类 (20), ␣noun (20), ␣nouns (19), ␣Classification (18), ␣lexical (18), ␣classification (17), Classification (16), ␣classify (16), ␣categor (15), 类别 (15)
  - newline after the response: task word at 10 layers; 分类 (10), 分析 (6), 回答 (5), 更多回答 (5), user (5), 用户 (5), 相关问答 (4), 用户提供 (4), Classification (3), 相关推荐 (3)
- `unrelated_extra__alpaca_27610__k0` (viewer number 5855; 18 tokens; task word in the prompt: no)
  - request: Sort the list of words alphabetically and separate them by commas. /  / bed, apple, tree, cat
  - response: apple, bed, cat, tree
  - newline after the request: task word at 0 layers; 排序 (20), sorted (20), ␣Sorted (19), Sorted (19), ␣sorted (19), (sorted (19), ␣alphabetical (17), 排列 (13), ␣alphabet (9), alphabet (9)
  - newline after the response: task word at 0 layers; EOF (8), 回答 (5), 用户 (5), 相关问答 (4), 更多回答 (3), Answer (2), 答案 (2), Question (2), 相关推荐 (2), 解释 (2)
- `unrelated_extra__alpaca_1169__k0` (viewer number 4220; 73 tokens; task word in the prompt: no)
  - request: Sort the list of items by price. /  / Apple, Banana, Orange - $3, $1, $2
  - response: To sort the items by price from lowest to highest: /  / 1. **Banana** - $1 / 2. **Orange** - $2 / 3. **Apple** - $3 /  / **Sorted Li
  - newline after the request: task word at 0 layers; 排序 (20), sorted (20), ␣Sorted (19), Sorted (19), ␣sorted (19), (sorted (17), _sorted (14), 列表 (13), 排列 (13), ␣sorting (13)
  - newline after the response: task word at 0 layers; 回答 (8), Answer (5), 更多回答 (5), 用户 (5), EOF (5), 答案 (4), >User (4), user (4), ␣Answer (3), 相关问答 (3)

**translate** (10 chats; task words 翻译, 翻译成)

- `unrelated_extra__alpaca_49689__k0` (viewer number 7245; 18 tokens; task word in the prompt: yes)
  - request: Translate the following sentence: Je vais à la bibliothèque.
  - response: I am going to the library.
  - newline after the request: task word at 21 layers; 翻译 (21), English (19), 英文 (18), ␣Translation (18), Translation (18), 翻译成 (17), 英语 (16), ␣Translate (13), translation (12), 译 (12)
  - newline after the response: task word at 21 layers; 翻译 (21), 法语 (21), ␣French (20), 法国 (20), French (20), 翻译成 (18), ␣français (18), France (17), ␣french (13), 中文 (12)
- `unrelated_extra__alpaca_2296__k0` (viewer number 4295; 115 tokens; task word in the prompt: yes)
  - request: Find a Spanish translation for the word "friend".
  - response: The Spanish translation for the word "friend" is **amigo** (masculine) or **amiga** (feminine). /  / *   **Amigo**: Used for
  - newline after the request: task word at 18 layers; 西班牙 (18), Spanish (18), 翻译 (18), 西班牙语 (18), 中文 (15), Latin (15), ␣Spanish (14), 法语 (14), 单词 (13), 词汇 (13)
  - newline after the response: task word at 2 layers; Answer (8), 回答 (7), 答案 (6), 相关推荐 (6), 更多回答 (6), user (5), 用户 (5), EOF (5), 相关问答 (3), 翻译 (2)
- `unrelated_extra__alpaca_45974__k0` (viewer number 7060; 17 tokens; task word in the prompt: yes)
  - request: You are given a piece of text in Chinese. What is the translation into English? /  / 白夜探花
  - response: The White Night's Top Scholar
  - newline after the request: task word at 17 layers; Chinese (20), 中文 (19), 翻译 (17), ␣Chinese (17), inyin (14), 翻译成 (13), 汉字 (12), 短语 (12), 四字 (12), 汉语 (8)
  - newline after the response: task word at 17 layers; 翻译 (17), 译 (11), ␣Translation (10), 翻译成 (9), ␣translation (9), Translation (9), 解释 (9), 中文 (8), translation (7), ␣translate (7)

