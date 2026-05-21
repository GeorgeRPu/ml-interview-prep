# Discrete Distributions

````{prf:definition} Bernoulli Distribution
The **Bernoulli distribution** models a single binary experiment—outcome is 0 or 1—with success probability $p$ ($X = 1$).

$$
\begin{aligned}
\Pr(X = 1) &= p \\
\Pr(X = 0) &= 1 - p \\
\mathbb{E}[X] &= p \\
\text{Var}(X) &= p(1-p)
\end{aligned}
$$
````

![Bernoulli Distribution](/_static/figures/bernoulli.png)

````{prf:definition} Binomial Distribution
The **binomial distribution** counts the number of successes in $n$ independent Bernoulli trials.

$$
P(X = k) = \binom{n}{k} p^k (1-p)^{n-k} \\
\mathbb{E}[X] &= np \\
\text{Var}(X) &= np(1-p)
$$
````

![Binomial Distribution](/_static/figures/binomial.png)

````{prf:definition} Geometric Distribution
The **geometric distribution** counts the number of trials until the first success.

$$
\begin{aligned}
P(X = k) &= (1-p)^{k-1} p \\
\mathbb{E}[X] &= \frac{1}{p} \\
\text{Var}(X) &= \frac{1-p}{p^2}
\end{aligned}
$$
````

The geometric distribution is memoryless: $\Pr(X > m + n \mid X > m) = \Pr(X > n)$.

![Geometric Distribution](/_static/figures/geometric.png)

````{prf:definition} Poisson Distribution
The **Poisson distribution** counts the number of events in a fixed interval, given a rate $\lambda$.

$$
P(X = k) &= \frac{\lambda^k e^{-\lambda}}{k!} \\
\mathbb{E}[X] &= \lambda \\
\text{Var}(X) &= \lambda
$$
````

The Poisson distribution is the limit of the binomial distribution as $n \to \infty$ and $p \to 0$ with $\lambda = np$ fixed.

![Poisson Distribution](/_static/figures/poisson.png)
