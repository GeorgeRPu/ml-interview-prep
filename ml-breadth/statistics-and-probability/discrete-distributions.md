# Discrete Distributions

## Bernoulli distribution

````{prf:definition} Bernoulli Distribution
:label: bernoulli-distribution
The **Bernoulli distribution** models a single binary experiment—outcome is 0 or 1—with success probability $p$.

$$
\begin{aligned}
\Pr\left(X = 1\right) &= p \\
\Pr\left(X = 0\right) &= 1 - p \\
\mathbb{E}\left[X\right] &= p \\
\text{Var}\left[X\right] &= p\left(1-p\right)
\end{aligned}
$$
````

![Bernoulli Distribution](/_static/figures/bernoulli.png)

## Binomial distribution

````{prf:definition} Binomial Distribution
:label: binomial-distribution
The **binomial distribution** counts the number of successes in $n$ independent Bernoulli trials.

$$
\begin{aligned}
P\left(X = k\right) &= \binom{n}{k} p^k \left(1-p\right)^{n-k} \\
\mathbb{E}\left[X\right] &= np \\
\text{Var}\left[X\right] &= np\left(1-p\right)
\end{aligned}
$$
````

As the number of trials $n$ increases, the binomial distribution approaches a normal distribution with mean $np$ and variance $np(1-p)$ due to the Central Limit Theorem.

![Binomial Distribution](/_static/figures/binomial.png)

## Geometric distribution

````{prf:definition} Geometric Distribution
:label: geometric-distribution
The **geometric distribution** counts the number of trials until the first success.

$$
\begin{aligned}
P\left(X = k\right) &= \left(1-p\right)^{k-1} p \\
\mathbb{E}\left[X\right] &= \frac{1}{p} \\
\text{Var}\left[X\right] &= \frac{1-p}{p^2}
\end{aligned}
$$
````

The geometric distribution is memoryless: $\Pr\left(X > m + n \mid X > m\right) = \Pr\left(X > n\right)$.

![Geometric Distribution](/_static/figures/geometric.png)

## Poisson distribution

````{prf:definition} Poisson Distribution
:label: poisson-distribution
The **Poisson distribution** counts the number of events in a fixed interval, given a rate $\lambda$.

$$
P\left(X = k\right) &= \frac{\lambda^k e^{-\lambda}}{k!} \\
\mathbb{E}\left[X\right] &= \lambda \\
\text{Var}\left[X\right] &= \lambda
$$
````

The Poisson distribution is the limit of the binomial distribution as $n \to \infty$ and $p \to 0$ with $\lambda = np$ fixed.

![Poisson Distribution](/_static/figures/poisson.png)
