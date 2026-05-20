# Bayes' Theorem

## Explain Bayes' Theorem

Bayes Theorem is a fundamental result in probability theory that describes how to update probabilities based on new evidence. It allows us to flip conditional probabilties.

$$
\Pr(A | B) = \frac{\Pr(B | A) \Pr(A)}{\Pr(B)}
$$

In Bayesian statistics, each term has a name:
- $\Pr(A | B)$ is the **posterior probability** of $A$ given $B$.
- $\Pr(B | A)$ is the **likelihood** of observing $B$ given $A$ is true.
- $\Pr(A)$ is the **prior probability** of $A$.
- $\Pr(B)$ is the **marginal probability** of $B$.

```{prf:proof}
By the definition of conditional probability,

$$
\begin{aligned}
\Pr(A | B) &= \frac{\Pr(A \cap B)}{\Pr(B)} \\
\Pr(B | A) &= \frac{\Pr(A \cap B)}{\Pr(A)}
\end{aligned}
$$

Rearrange the second equation for $\Pr(A \cap B)$,

$$
\Pr(A \cap B) = \Pr(B | A) \Pr(A)
$$

and substituting into the first equation.

$$
\Pr(A | B) = \frac{\Pr(B | A) \Pr(A)}{\Pr(B)}
$$
```

## Calculate the probability you have a disease given a positive test result

Suppose a disease has a prevalnce of 1% in the population. A test for the disease has a true positive rate (sensitivity) of 99% and a false positive rate of 5%. If you test positive, what is the probability that you actually have the disease?

Let $A$ be the event that you have the disease and $B$ be the event that you test positive. We want to calculate $\Pr(A | B)$.

$$
\begin{aligned}
\Pr(A | B) &= \frac{\Pr(B | A) \Pr(A)}{\Pr(B)} \\
&= \frac{0.99 \cdot 0.01}{\Pr(B)}
\end{aligned}
$$

To calculate $\Pr(B)$, we can use the law of total probability.

$$
\begin{aligned}
\Pr(B) &= \Pr(B | A) \Pr(A) + \Pr(B | \neg A) \Pr(\neg A) \\
&= 0.99 \cdot 0.01 + 0.05 \cdot 0.99 \\
&= 0.0594
\end{aligned}
$$

Substituting back into Bayes' theorem,

$$
\begin{aligned}
\Pr(A | B) &= \frac{0.99 \cdot 0.01}{0.0594} \\
&\approx 0.1667
\end{aligned}
$$
