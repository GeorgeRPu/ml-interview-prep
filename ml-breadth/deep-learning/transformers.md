# Transformers

## Explain how a transformer works.

A transformer {cite}`Vaswani2017` is a deep learning architecture that relies on self-attention mechanisms to process sequential data. It takes an input sequence of tokens and produces and output sequence of tokens.

### Input representation

Each token in the input sequence is converted into a $d$-dimensional dense vector representation (embedding). To allow the model to capture the order of tokens, positional encodings are added to the token embeddings. The original transformer uses sinusoidal positional encodings.

$$
\begin{aligned}
\text{PE}_{(pos, 2i)} &= \sin\left(\frac{pos}{10000^{2i/d}}\right) \\
\text{PE}_{(pos, 2i+1)} &= \cos\left(\frac{pos}{10000^{2i/d}}\right)
\end{aligned}
$$

### Scaled dot-product attention

At the core of the transformer is self-attention, which allows each token to attend to all other tokens in the sequence.

Given a matrix of queries $Q \in \mathbb{R}^{n \times d_k}$, keys $K \in \mathbb{R}^{n \times d_k}$, and values $V \in \mathbb{R}^{n \times d_v}$, scaled dot-product attention is

$$
\text{Attention}\left(Q, K, V\right) = \text{softmax}\left(\frac{QK^\top}{\sqrt{d_k}}\right) V
$$

The queries, keys, and values are obtained by multiplying the input embeddings by learned projection matrices.

$$
Q = X W^Q, \quad K = X W^K, \quad V = X W^V
$$

### Multi-head attention

Instead of a single attention function, the transformer uses multi-head attention that runs $h$ attention heads in parallel and concatenates the results.

$$
\begin{aligned}
\text{MultiHead}\left(X\right) &= \left[\text{head}_1, \ldots, \text{head}_h\right] W^O \\
\text{head}_i &= \text{Attention}\left(X W_i^Q, X W_i^K, X W_i^V\right)
\end{aligned}
$$

where $W_i^Q \in \mathbb{R}^{d \times d_k}$, $W_i^K \in \mathbb{R}^{d \times d_k}$, $W_i^V \in \mathbb{R}^{d \times d_v}$, $W^O \in \mathbb{R}^{hd_v \times d}$.

Each head learns its own projection matrices, so different heads can specialize in different types of relationships. Empirically, analyses of trained models have found individual heads that track syntactic dependencies (e.g. direct objects of verbs) and coreference links {cite}`Clark2019`.

### Transformer block

Each transformer layer consists of 2 sub-layers with residual connections and layer normalization:

1. **Multi-head self-attention.** Every token attends to every other token in the same sequence.
2. **Position-wise feed-forward network.** A two-layer MLP applied independently to each position.

$$
\begin{aligned}
x_l' &= \text{LayerNorm}\left(x_l + \text{MultiHead}\left(x_l\right)\right) \\
x_{l+1} &= \text{LayerNorm}\left(x_l' + \text{FFN}\left(x_l'\right)\right) \\
\text{FFN}\left(x\right) &= \text{ReLU}\left(xW_1 + b_1\right)W_2 + b_2
\end{aligned}
$$

### Encoder-decoder architecture

The original transformer has an encoder and decoder stack, each containing $N$ layers.

- **Encoder** layers use self-attention over the full input sequence.
- **Decoder** layers use *masked* self-attention (each position can only attend to earlier positions to preserve autoregressive generation) followed by *cross-attention* over the encoder output, where the decoder supplies queries and the encoder supplies keys and values.

Many modern architectures use only the encoder (BERT {cite}`Devlin2019`) or only the decoder (GPT {cite}`Radford2018`).

![Transformer architecture](/_static/figures/transformer.png)

## What is the time complexity of the self-attention mechanism in transformers?

$O(n^2 \cdot d)$ where $n$ is the sequence length.

## How can you reduce the computational cost of self-attention in transformers for long sequences?

## Why are the attention scores scaled by the square root of the key dimension?

If the components of $q$ and $k$ are independent with mean 0 and variance 1, then $q^\top k$ has mean 0 and variance $d_k$ {cite}`Vaswani2017`. As $d_k$ grows, the dot products become large in magnitude, pushing the softmax into saturated regions with near-zero gradients — so the model stops learning. Dividing by $\sqrt{d_k}$ normalizes the variance of the scores back to 1, keeping the softmax in a regime where gradients flow.

## How do rotary positional embeddings (RoPE) work?

## How does ALiBi differ from absolute and rotary positional encodings?

## Is the transformer architecture autoregressive?

The original transformer architecture is not autoregressive — the encoder processes the entire input sequence in parallel, and the decoder attends to the full encoder output. However, the decoder uses masked self-attention to ensure that each position can only attend to earlier positions, which allows it to be used for autoregressive generation.

## What are the advantages of using transformers over traditional RNNs for sequence modeling tasks?

Transformers can capture long-range interactions more effectively than RNNs, which suffer from vanishing gradients.

Training is massively parallelizable {cite}`Vaswani2017`. In an RNN, the hidden state at position $t$ depends on position $t-1$, so the forward pass is inherently sequential — $O\left(n\right)$ serial steps. In a transformer, self-attention computes all pairwise interactions in matrix multiplications which can be computed in parallel.

```{bibliography}
:filter: docname in docnames
```
