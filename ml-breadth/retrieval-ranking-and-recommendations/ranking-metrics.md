# Ranking Metrics

- Let $\hat{y}_1 > \hat{y}_2 > \cdots > \hat{y}_n$ be the predicted relevance scores for a query and $y_1, y_2, \dots, y_n$ be the true relevance scores: 0 if the item is not relevant, 1 if relevant.
- Let $N$ be the number of queries.
- Let $\#\left[\cdot\right]$ be the count of instances that satisfy the condition.

## Precision@k

Suppose we predict

````{prf:definition} Precision@k
:label: precision-at-k

**Precision@k** is the number of relevant items in the top $k$ results divided by $k$.

$$
P@k = \frac{\#\left[\text{relevant items in top } k\right]}{k} = \sum_{i=1}^{k} \frac{y_i}{k}
$$
````

Note that the predicted scores $\hat{y}_i$ are not used in the formula for Precision@k but matter through the ordering they induce.

## Recall@k

````{prf:definition} Recall@k
:label: recall-at-k

**Recall@k** is the number of relevant items in the top $k$ results divided by the total number of relevant items.

$$
R@k = \frac{\#\left[\text{relevant items in top } k\right]}{\#\left[\text{relevant items}\right]} = \frac{\sum_{i=1}^{k} y_i}{\sum_{i=1}^{n} y_i}
$$
````

Precision@k and Recall@k have a few limitations as ranking metrics:

- They ignore the ordering of relevant items
- They require choosing $k$

Recall@k always increases as $k$ increases, making it less useful than Precision@k in some scenarios.

![Precision@k and Recall@k vs. k](/_static/figures/precision_recall_at_k.png)
*For a ranked list of 10 items with relevant items at positions 1, 3, 4, and 7 (relevance vector [1, 0, 1, 1, 0, 0, 1, 0, 0, 0]), Precision@k fluctuates as $k$ grows while Recall@k increases monotonically. Precision drops each time a non-relevant item enters the top $k$.*

## Average precision@k

````{prf:definition} Average precision@k
:label: average-precision-at-k

**Average precision@k (AP@k)** averages the Precision@i for values $i \leq k$ where the $i$-th document is relevant, giving higher weight to relevant items ranked near the top.

$$
AP@k = \frac{1}{\#\left[\text{relevant items}\right]} \sum_{i=1}^{k} P@i y_i = \frac{1}{\sum_{i=1}^{n} y_i} \sum_{i=1}^{k} \left(\frac{\sum_{j=1}^{i} y_j}{i}\right) \cdot y_i
$$
````

![AP comparison for two rankings](/_static/figures/ap_comparison.png)
*Both rankings contain the same 4 relevant items among 10 results, but ordering changes AP dramatically. Placing relevant items near the top (left, AP = 0.95) keeps precision high at each recall level, while scattering them toward the bottom (right, AP = 0.36) forces precision down.*

## Mean average precision@k

````{prf:definition} Mean average precision@k
:label: mean-average-precision-at-k

**Mean average precision@k (MAP@k)** is the average of the AP@k across the entire dataset.

$$
MAP@k = \frac{1}{N} \sum_{i=1}^{N} AP@k_i = \frac{1}{N} \sum_{i=1}^{N} \left( \frac{1}{\sum_{j=1}^{n} y_j} \sum_{l=1}^{k} \left(\frac{\sum_{m=1}^{l} y_m}{l}\right) \cdot y_l \right)
$$
````

## Reciprocal rank

````{prf:definition} Reciprocal rank
:label: reciprocal-rank

**Reciprocal rank (RR)** is the multiplicative inverse of the rank of the first relevant item, returning a value between 0 and 1 that indicates how far from the top the first relevant result is located.

$$
RR = \frac{1}{\text{rank of first relevant item}} = \frac{1}{\argmin_i\ y_i}
$$
````

## Mean reciprocal rank

````{prf:definition} Mean reciprocal rank
:label: mean-reciprocal-rank

**Mean reciprocal rank (MRR)** is the average of the reciprocal ranks across a dataset.

$$
MRR = \frac{1}{N} \sum_{i=1}^{N} RR_i = \frac{1}{N} \sum_{i=1}^{N} \frac{1}{\argmin_j\ y_j}
$$
````

## Discounted cumulative gain

````{prf:definition} Discounted cumulative gain
:label: dcg

**Discounted cumulative gain (DCG@k)** sums the relevance gains of the top $k$ items, discounted by their ranking position. Let $R_i$ is the graded true relevance $R_i \in \{0, 1, 2, \dots\}$ of whatever item the model placed at rank $i$ rather than the binary $y_i$ used above.

$$
DCG@k = \sum_{i=1}^{k} \frac{\text{gain}_i}{\text{discount}_i} = \sum_{i=1}^{k} \frac{2^{R_i} - 1}{\log_2\left(i + 1\right)}
$$

where

$$
\begin{aligned}
\text{gain}_i &= 2^{R_i} - 1 \\
\text{discount}_i &= \log_2\left(i + 1\right)
\end{aligned}
$$
````

The graded relevance $R_i$ is a ground-truth label assigned per item by human raters (or derived from implicit signals like clicks), typically on an ordinal scale such as 0 (irrelevant) to 4 (perfect). The exponential gain $2^{R_i} - 1$ is a design choice that amplifies the difference between relevance grades, making the metric more sensitive to placing highly relevant items at the top. The logarithmic discount $\log_2\left(i + 1\right)$ reflects the intuition that users are more likely to examine top-ranked items, so the contribution of relevant items should diminish as their rank increases.

Unlike all previous metrics—Precision@k, Recall@k, AP@k, MAP@k, and MRR, DCG works with non-binary relevance scores.

## Normalized discounted cumulative gain

````{prf:definition} Normalized discounted cumulative gain
:label: ndcg

**Normalized discounted cumulative gain (nDCG@k)** normalizes DCG by dividing by the maximum possible DCG, which is the DCG when items are perfectly ranked by relevance.

$$
\begin{aligned}
nDCG@k &= \frac{DCG@k}{\text{DCG@k}_{\text{ideal}}} \\
\text{DCG@k}_{\text{ideal}} &= \sum_{i=1}^{k} \frac{2^{R_i^*} - 1}{\log_2\left(i + 1\right)}
\end{aligned}
$$

$R_i^*$ is the relevance of the item at rank $i$ in the ideal ranking, which sorts items by true relevance in descending order.
````

Normalizing DCG allows nDCG to be interpreted as a percentage of the ideal ranking's gain, making it easier to compare across queries with different numbers of relevant items and relevance distributions. An nDCG@k of 1 indicates a perfect ranking, while values closer to 0 indicate poorer rankings.

![DCG discount curve and nDCG normalization](/_static/figures/dcg_ndcg.png)
*With graded relevance [2, 0, 3, 1, 0, 3, 0, 2, 1, 0], the logarithmic discount rapidly shrinks the contribution of lower-ranked items (left). Comparing cumulative DCG of the actual ranking against the ideal ranking (right) shows that nDCG@10 = 0.71 — the actual ranking captures 71% of the maximum possible gain.*
