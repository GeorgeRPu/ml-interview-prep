# Law of Large Numbers

## What is the law of large numbers?

The law of large numbers (LLN) says that as we collect more data, the sample mean gets closer to the true population mean. It is one of the foundational theorems in probability and statistics, and it justifies using sample averages as estimates of expected values.

````{prf:theorem} Law of Large Numbers
:label: law-of-large-numbers
Let $X_1, X_2, \dots$ be independent and identically distributed (iid) random variables with mean $\mu$. Then the sample mean $\bar{X}_n = \frac{1}{n} \sum_{i=1}^n X_i$ converges in probability to $\mu$ as $n \to \infty$.

$$
\bar{X}_n \xrightarrow{p} \mu \quad \text{as } n \to \infty
$$
````

## Weak vs. strong law

There are two versions of the LLN that differ in the type of convergence they guarantee.

The **weak law of large numbers** (WLLN) states that $\bar{X}_n$ converges to $\mu$ **in probability**. For any $\epsilon > 0$,

$$
\lim_{n \to \infty} \Pr\left(|\bar{X}_n - \mu| > \epsilon\right) = 0.
$$

The **strong law of large numbers** (SLLN) states that $\bar{X}_n$ converges to $\mu$ **almost surely**.

$$
\Pr\left(\lim_{n \to \infty} \bar{X}_n = \mu\right) = 1
$$

Almost sure convergence is a stronger guarantee. It says the sample mean converges to $\mu$ on almost every possible sequence of outcomes, not just that large deviations become unlikely.

## How does the LLN relate to the central limit theorem?

The LLN and CLT are complementary results about sample means. The LLN tells us *what* the sample mean converges to ($\mu$), while the CLT tells us *how* the sample mean is distributed around $\mu$ for finite $n$ (a Normal distribution).

## What is the gambler's fallacy?

The **gambler's fallacy** is the mistaken belief that the LLN applies to short sequences. After flipping 10 heads in a row with a fair coin, the probability of the next flip being tails is still $\frac{1}{2}$. The LLN guarantees convergence of the average over many trials, not that short-term deviations will be "corrected" by future outcomes.
