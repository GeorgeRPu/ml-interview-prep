# Dimensionality Reduction

## What is dimensionality reduction?

Dimensionality reduction transforms high-dimensional data into a lower-dimensional representation while preserving as much of the original structure as possible.

## What is dimensionality reduction used for?

1. **Mitigating the curse of dimensionality.** In high-dimensional spaces, data becomes sparse and distances between points converge, making it harder for models to learn meaningful patterns. Reducing dimensions concentrates the data into its most informative subspace.
2. **Reducing computational cost.** Fewer features means faster training and lower memory usage.
3. **Denoising.** Discarding low-variance dimensions can remove noise and improve downstream model performance.
4. **Visualization.** Projecting data to 2 or 3 dimensions allows the data to be visualized.

## Explain PCA

**Principal component analysis (PCA)** is a linear dimensionality reduction technique that fits an ellipsoid to the data and projects it onto the orthogonal directions along which the data varies the most.

````{prf:algorithm} PCA
:label: pca-algorithm

**Input:** Data matrix $X \in \mathbb{R}^{N \times d}$ with $N$ samples and $d$ features, target dimension $k$.

**Output:** Reduced data $Y \in \mathbb{R}^{N \times k}$.

1. Center the data by subtracting the mean $\bar{x} = \frac{1}{N} \sum_{i=1}^{N} x_i$ from each sample to get $X_c$.
2. Take the singular value decomposition (SVD) of the centered data matrix.

$$
X_c = U S V^\top
$$

3. Project the data onto the top $k$ right singular vectors

$$
Y = X_c V_k
$$

where $V_k = \left[v_1, \ldots, v_k\right] \in \mathbb{R}^{d \times k}$.
````

Each right singular vector $v_i$ is a **principal component**. The corresponding eigenvalue of the covariance matrix is $\lambda_i = s_i^2 / \left(N - 1\right)$, which is the variance of the data along that direction. The **fraction of variance explained** by the top $k$ components is

$$
R(k) = \frac{\sum_{i=1}^{k} s_i^2}{\sum_{i=1}^{d} s_i^2}.
$$

![PCA projecting 2D data onto its first principal component](/_static/figures/pca_projection.png)
*PCA on 2D correlated data. The first principal component (PC1) captures the direction of maximum variance. Projecting onto PC1 alone retains most of the spread, while projecting onto PC2 captures the remaining orthogonal variance.*

## How do you choose the number of components in PCA?

A common approach is to choose the smallest $k$ that captures a sufficient fraction of the total variance (e.g., 90% or 95%).

The plot of the fraction of variance explained as a function of $k$ is sometimes called a **scree plot** when the individual eigenvalues are plotted.

## Explain LDA

**Linear discriminant analysis (LDA)** is a supervised linear dimensionality reduction technique. While PCA finds the directions of maximum variance regardless of labels, LDA finds the directions that maximize the ratio of **between-class scatter** to **within-class scatter**. Each direction $w$ is chosen to maximize the **Fisher criterion** $J\left(w\right)$.

$$
J\left(w\right) = \frac{w^\top S_B w}{w^\top S_W w}
$$

where

$$
\begin{aligned}
S_B &= \sum_{c=1}^{C} N_c \left(\mu_c - \mu\right)\left(\mu_c - \mu\right)^\top \\
S_W &= \sum_{c=1}^{C} \sum_{x_i \in c} \left(x_i - \mu_c\right)\left(x_i - \mu_c\right)^\top.
\end{aligned}
$$

Here:
- $S_B$ is the between-class scatter matrix
- $S_W$ is the within-class scatter matrix
- $\mu_c$ is the mean of class $c$
- $\mu$ is the overall mean
- $N_c$ is the number of samples in class $c$
- $C$ is the number of classes.

The optimal directions are the eigenvectors of $S_W^{-1} S_B$ with the largest eigenvalues. Since $S_B$ has rank at most $C - 1$, LDA produces at most $C - 1$ directions. Stacking these into a matrix $W = \left[w_1, \ldots, w_{C-1}\right] \in \mathbb{R}^{d \times \left(C - 1\right)}$, the projection of a data point $x$ is

$$
y = W^\top x.
$$

## Explain t-SNE

**t-distributed stochastic neighbor embedding (t-SNE)** is a nonlinear dimensionality reduction technique designed for visualization. It preserves local neighborhood structure by converting pairwise distances to probabilities and matching them in low-dimensional space. It works by minimizing the KL divergence between the high-dimensional and low-dimensional distributions over pairs of points.

````{prf:algorithm} t-SNE
:label: t-sne-algorithm

**Input:** Data matrix $X \in \mathbb{R}^{N \times d}$, number of target dimensions $k$ (usually 2 or 3), target perplexity $\rho$.

**Output:** Low-dimensional embedding $Y \in \mathbb{R}^{N \times k}$.

1. In the high-dimensional space, define the conditional probability $p_{j|i}$ that point $x_j$ is a neighbor of $x_i$ using a Gaussian kernel.

$$
p_{j|i} = \frac{\exp\left(-\|x_i - x_j\|^2 / 2\sigma_i^2\right)}{\sum_{k \ne i} \exp\left(-\|x_i - x_k\|^2 / 2\sigma_i^2\right)}
$$

2. For each point $i$, set the bandwidth $\sigma_i$ by binary search so that the perplexity of $P_i = \left\{p_{j|i}\right\}_j$ equals the target $\rho$.

$$
\begin{aligned}
\text{Perp}\left(P_i\right) &= 2^{H\left(P_i\right)} = \rho \\
H\left(P_i\right) &= -\sum_j p_{j|i} \log_2 p_{j|i}
\end{aligned}
$$

3. Symmetrize: $p_{ij} = \frac{p_{j|i} + p_{i|j}}{2N}$.

4. Initialize the embedding by sampling each $y_i \in \mathbb{R}^k$ from a small Gaussian, giving $Y = \left[y_1, \ldots, y_N\right]^\top$.

5. In the low-dimensional space, define a similar probability using a t-distribution with one degree of freedom (aka Cauchy distribution).

$$
q_{ij} = \frac{\left(1 + \|y_i - y_j\|^2\right)^{-1}}{\sum_{k \ne l} \left(1 + \|y_k - y_l\|^2\right)^{-1}}
$$

6. Update the embedding $Y$ by gradient descent to minimize the KL divergence between $P$ and $Q$, recomputing $Q$ from the current $Y$ at each step.

$$
\text{KL}\left(P \| Q\right) = \sum_{i \ne j} p_{ij} \log \frac{p_{ij}}{q_{ij}}
$$

  The converged $Y$ is the low-dimensional embedding.
````

The heavy tails of the t-distribution in the low-dimensional space allow moderate distances in high dimensions to be modeled by larger distances in low dimensions, alleviating the **crowding problem** where points in the center get crushed together.

The **target perplexity** $\rho$ is the main hyperparameter. It can be interpreted as the effective number of neighbors each point considers. Because $\text{Perp}\left(P_i\right)$ increases monotonically with the bandwidth $\sigma_i$, the binary search in step 1 finds a small $\sigma_i$ in dense regions and a large $\sigma_i$ in sparse ones, so every point ends up with the same effective number of neighbors $\rho$. Typical values range from 5 to 50.

## What are the limitations of t-SNE?

1. **Non-parametric.** t-SNE does not learn a mapping function, so it cannot project new data points without rerunning the entire algorithm.
2. **Global structure.** t-SNE preserves local neighborhoods well but can distort global structure. Distances between clusters are not meaningful.
3. **Stochastic.** Different random initializations can produce different embeddings.
4. **Slow.** The naive algorithm is $O\left(N^2\right)$ per iteration. Barnes-Hut approximations reduce this to $O\left(N \log N\right)$.
5. **Sensitive to hyperparameters.** The perplexity and learning rate can significantly affect the result.

## Explain UMAP

**Uniform manifold approximation and projection (UMAP)** is a nonlinear dimensionality reduction technique that, like t-SNE, preserves local structure but is faster and better preserves global structure.

UMAP constructs a weighted graph in the high-dimensional space where edge weights represent the likelihood that two points are connected. It then optimizes a low-dimensional layout to have a similar graph structure by minimizing the cross-entropy between the high-dimensional and low-dimensional graph edge probabilities.

## When would you use PCA vs. LDA vs. t-SNE vs. UMAP?

| | PCA | LDA | t-SNE | UMAP |
|---|---|---|---|---|
| Type | Linear | Linear (supervised) | Nonlinear | Nonlinear |
| Preserves | Global variance | Class separability | Local neighborhoods | Local + some global structure |
| Speed | Fast | Fast | Slow ($O\left(N^2\right)$ or $O\left(N \log N\right)$) | Fast |
| Max dimensions | $d$ | $C - 1$ | Any | Any |
| Can project new data? | Yes | Yes | No | Yes |
| Deterministic? | Yes | Yes | No | No |
| Best for | Preprocessing, compression | Classification preprocessing | 2D/3D visualization | 2D/3D visualization, larger datasets |

![MNIST reduced from 784 to 3 dimensions by PCA, LDA, t-SNE, and UMAP](/_static/figures/mnist_dimensionality_reduction.png)
*A subsample of MNIST digits (28×28 = 784 dimensions) reduced to 3 dimensions by each method, colored by digit. PCA (linear, unsupervised) overlaps the classes heavily. LDA (linear, supervised) uses the labels to separate them but is still constrained to a linear projection. t-SNE and UMAP (nonlinear) resolve the digits into distinct clusters, with UMAP producing the tightest, most separated groups.*
