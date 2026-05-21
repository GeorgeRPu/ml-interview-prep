# Bayes' Theorem

## Explain Bayes' theorem

Bayes Theorem is a fundamental result in probability theory that describes how to update probabilities based on new evidence. It allows us to flip conditional probabilties.

$$
\Pr\left(A | B\right) = \frac{\Pr\left(B | A\right) \Pr\left(A\right)}{\Pr\left(B\right)}
$$

In Bayesian statistics, each term has a name:
- $\Pr\left(A | B\right)$ is the **posterior probability** of $A$ given $B$.
- $\Pr\left(B | A\right)$ is the **likelihood** of observing $B$ given $A$ is true.
- $\Pr\left(A\right)$ is the **prior probability** of $A$.
- $\Pr\left(B\right)$ is the **marginal probability** of $B$.

```{prf:proof}
By the definition of conditional probability,

$$
\begin{aligned}
\Pr\left(A | B\right) &= \frac{\Pr\left(A \cap B\right)}{\Pr\left(B\right)} \\
\Pr\left(B | A\right) &= \frac{\Pr\left(A \cap B\right)}{\Pr\left(A\right)}
\end{aligned}
$$

Rearrange the second equation for $\Pr\left(A \cap B\right)$,

$$
\Pr\left(A \cap B\right) = \Pr\left(B | A\right) \Pr\left(A\right)
$$

and substituting into the first equation.

$$
\Pr\left(A | B\right) = \frac{\Pr\left(B | A\right) \Pr\left(A\right)}{\Pr\left(B\right)}
$$
```

## Calculate the probability you have a disease given a positive test result

Suppose a disease has a prevalnce of 1% in the population. A test for the disease has a true positive rate (sensitivity) of 99% and a false positive rate of 5%. If you test positive, what is the probability that you actually have the disease?

Let $A$ be the event that you have the disease and $B$ be the event that you test positive. We want to calculate $\Pr\left(A | B\right)$.

$$
\begin{aligned}
\Pr\left(A | B\right) &= \frac{\Pr\left(B | A\right) \Pr\left(A\right)}{\Pr\left(B\right)} \\
&= \frac{0.99 \cdot 0.01}{\Pr\left(B\right)}
\end{aligned}
$$

To calculate $\Pr\left(B\right)$, we can use the law of total probability.

$$
\begin{aligned}
\Pr\left(B\right) &= \Pr\left(B | A\right) \Pr\left(A\right) + \Pr\left(B | \neg A\right) \Pr\left(\neg A\right) \\
&= 0.99 \cdot 0.01 + 0.05 \cdot 0.99 \\
&= 0.0594
\end{aligned}
$$

Substituting back into Bayes' theorem,

$$
\begin{aligned}
\Pr\left(A | B\right) &= \frac{0.99 \cdot 0.01}{0.0594} \\
&\approx 0.1667
\end{aligned}
$$
