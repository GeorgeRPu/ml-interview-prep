# Tokenization

## What is tokenization?

**Tokenization** is the process of converting text into a list of tokens belonging to a finite vocabulary $t_1, t_2, \dots, t_n$. Each token $t_i$ is a string but are referred to by their integer id $i$. This step is necessary in NLP as without it, text cannot be converted to a vector representation.

To map tokens to ids we can use:

1. **Lookup tables** — slow but invertible
2. **Hashing** — fast but introduces the possibility of collisions and is not invertible

## Explain byte pair encoding

Originally an algorithm for compressing text, **byte pair encoding (BPE)** was used by OpenAI to tokenize text when pretraining their GPT models {cite}`Sennrich2016`. BPE starts with a base vocabulary of each character in the corpus. Then new tokens are added by merging the most frequent pair of tokens until the desired vocabulary size is reached.

````{prf:algorithm} Byte Pair Encoding
:label: bpe

**Input:** Corpus of documents, desired vocabulary size $V$

**Output:** Vocabulary $\mathcal{V}$, ordered merge list

1. Initialize vocabulary with all individual characters in the corpus
2. Split each word in the corpus into a sequence of characters
3. **While** $|\text{vocab}| < V$:
   1. Compute the frequency of every adjacent pair $f\left(t_i, t_j\right)$ of tokens in the corpus
   2. Select the most frequent pair $\left(t_i^*, t_j^*\right) = \argmax_{\left(t_i, t_j\right)} f\left(t_i, t_j\right)$
   3. Merge every occurrence of $\left(t_i^*, t_j^*\right)$ into a new token $t_{ij}$
   4. Add $t_{ij}$ to the vocabulary and record the merge rule $t_i^* + t_j^* \to t_{ij}$
4. **Return** Vocabulary $\mathcal{V}$ and the ordered list of merge rules
````

At inference time, tokenization replays the learned merges in order on the input text, so the merge list fully determines the encoding.

BPE is often applied on the bytes underlying a string instead of characters. Because there are only 256 possible byte values, this approach ensures that all UTF-8 characters are in the vocabulary, even rare ones like emojis.

![OpenAI tokenizer splitting "Hello World!" into 3 tokens](/_static/figures/brave_screenshot_platform.openai.com.png)
*OpenAI's tokenizer tool showing "Hello World!" split into 3 tokens and 12 characters using the tokenizer for GPT-5.x & O1/3.*

## Give an example of BPE

Original corpus (word, frequency): ("hug", 10), ("pug", 5), ("pun", 12), ("bun", 4), ("hugs", 5)

```
Base vocab: ["b", "g", "h", "n", "p", "s", "u"]
Base corpus: ("h" "u" "g", 10), ("p" "u" "g", 5), ("p" "u" "n", 12), ("b" "u" "n", 4), ("h" "u" "g" "s", 5)
```

**Merge 1:** `("u", "g")` is the most frequent pair.

```
Vocab: ["b", "g", "h", "n", "p", "s", "u", "ug"]
Corpus: ("h" "ug", 10), ("p" "ug", 5), ("p" "u" "n", 12), ("b" "u" "n", 4), ("h" "ug" "s", 5)
```

**Merge 2:** `("u", "n")` is now the most frequent pair.

```
Vocab: ["b", "g", "h", "n", "p", "s", "u", "ug", "un"]
Corpus: ("h" "ug", 10), ("p" "ug", 5), ("p" "un", 12), ("b" "un", 4), ("h" "ug" "s", 5)
```

**Merge 3:** `("h", "ug")` is now the most frequent pair.

```
Vocab: ["b", "g", "h", "n", "p", "s", "u", "ug", "un", "hug"]
Corpus: ("hug", 10), ("p" "ug", 5), ("p" "un", 12), ("b" "un", 4), ("hug" "s", 5)
```

This process continues until the desired vocabulary size is reached.


```{bibliography}
:filter: docname in docnames
```
