# Expected Value and Variance

## What is expected value?

The **expected value** is the weighted average of all possible values of a random variable.

````{prf:definition} Expected Value
Let $X$ be a random variable. The expected value of $X$ is

$$
\mathbb{E}\left[X\right] = \sum_{x} x \cdot \Pr\left(X = x\right) \quad
$$

for discrete random variables, or

$$
\mathbb{E}\left[X\right] = \int_{-\infty}^{\infty} x \cdot f\left(x\right) \, dx
$$

for continuous random variables, where $f\left(x\right)$ is the probability density function of $X$.
````

The expectation is linear, regardless of independence.

$$
\mathbb{E}\left[aX + bY\right] = a\mathbb{E}\left[X\right] + b\mathbb{E}\left[Y\right]
$$

## What are variance and standard deviation?

**Variance** measures the spread of a distribution around its mean.

````{prf:definition} Variance
Let $X$ be a random variable with mean $\mu$. The variance of $X$ is

$$
\text{Var}\left[X\right] = \mathbb{E}\left[\left(X - \mu\right)^2\right] = \mathbb{E}\left[X^2\right] - \left(\mathbb{E}\left[X\right]\right)^2
$$

The **standard deviation** is $\sigma = \sqrt{\text{Var}\left[X\right]}$.
````

For independent random variables,

$$
\text{Var}\left[X + Y\right] = \text{Var}\left[X\right] + \text{Var}\left[Y\right].
$$

## What are covariance and correlation?

**Covariance** measures the joint variability of two random variables.

````{prf:definition} Covariance
Let $X$ and $Y$ be random variables with means $\mu_X$ and $\mu_Y$. The covariance of $X$ and $Y$ is

$$
\text{Cov}\left(X, Y\right) = \mathbb{E}\left[\left(X - \mu_X\right)\left(Y - \mu_Y\right)\right] = \mathbb{E}\left[XY\right] - \mathbb{E}\left[X\right]\mathbb{E}\left[Y\right].
$$
````

**Correlation** normalizes covariance to $\left[-1, 1\right]$ by dividing by their standard deviations.


````{prf:definition} Correlation
The correlation coefficient $\rho\left(X, Y\right)$ is defined as

$$
\rho\left(X, Y\right) = \frac{\text{Cov}\left(X, Y\right)}{\sigma_X \sigma_Y}.
$$

Correlation measures linear dependence only. Two variables can have $\rho = 0$ and still be dependent. Correlation does not imply causation.
````
