# Central Limit Theorem

## State the Central Limit Theorem

Given a sequence of independent and identically distributed (iid) random variables, the Central Limit Theorem (CLT) states that sample average converges in distribution to a Normal distribution, regardless of the original distribution of the individual variables.

````{prf:theorem} Central Limit Theorem
Let $(X_n)$ be a sequence of iid random variables with mean $\mu$ and variance $\sigma^2$. Then, as $n \to \infty$, the distribution of $\sqrt{n}\left(\bar{X} - \mu\right)$, where

$$
\bar{X} = \frac{1}{n} \sum_{i=1}^n X_i
$$

is the sample average, converges in distribution to a Normal distribution with mean $0$ and variance $\sigma^2$.

$$
\sqrt{n}\left(\bar{X} - \mu\right) \xrightarrow{dist} \mathcal{N}\left(0, \sigma^2\right)
$$
````

![Example of Central Limit Theorem for Dice Sums](https://upload.wikimedia.org/wikipedia/commons/8/8c/Dice_sum_central_limit_theorem.svg)
*Figure 1: Distribution of dice sums as the number of dice increases. The distribution approaches a Normal curve, illustrating the Central Limit Theorem.*

## Why is the Central Limit Theorem important?

The Central Limit Theorem is important because it justifies the use of the Normal distribution in many statistical methods, such as confidence interval estimation and hypothesis testing, even when the underlying data does not follow a Normal distribution.

## What is an application of the Central Limit Theorem?

Confidence intervals are a common application of the CLT.

The CLT also explains why many natural phenomena tend to follow a bell-shaped curve, as they can be thought of as the sum of many small, independent effects.
