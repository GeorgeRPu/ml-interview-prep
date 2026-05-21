# Expected Value And Variance

## What Is Expected Value?

The **expected value** is the weighted average of all possible values of a random variable.

````{prf:definition} Expected Value
Let $X$ be a random variable. The expected value of $X$ is

$$
\mathbb{E}[X] = \sum_{x} x \cdot \Pr(X = x) \quad
$$

for discrete random variables, or

$$
\mathbb{E}[X] = \int_{-\infty}^{\infty} x \cdot f(x) \, dx
$$

for continuous random variables, where $f(x)$ is the probability density function of $X$.
````

The expectation is linear, regardless of independence.

$$
\mathbb{E}[aX + bY] = a\mathbb{E}[X] + b\mathbb{E}[Y]
$$

## What Are Variance and Standard Deviation?

**Variance** measures the spread of a distribution around its mean.

````{prf:definition} Variance
Let $X$ be a random variable with mean $\mu$. The variance of $X$ is

$$
\text{Var}(X) = \mathbb{E}[(X - \mu)^2] = \mathbb{E}[X^2] - (\mathbb{E}[X])^2
$$

The **standard deviation** is $\sigma = \sqrt{\text{Var}(X)}$.
````

For independent random variables,

$$
\text{Var}(X + Y) = \text{Var}(X) + \text{Var}(Y).
$$

## What Are Covariance and Correlation?

**Covariance** measures the joint variability of two random variables.

````{prf:definition} Covariance
Let $X$ and $Y$ be random variables with means $\mu_X$ and $\mu_Y$. The covariance of $X$ and $Y$ is

$$
\text{Cov}(X, Y) = \mathbb{E}[(X - \mu_X)(Y - \mu_Y)] = \mathbb{E}[XY] - \mathbb{E}[X]\mathbb{E}[Y].
$$
````

**Correlation** normalizes covariance to $[-1, 1]$ by dividing by their standard deviations.


````{prf:definition} Correlation
The correlation coefficient $\rho(X, Y)$ is defined as

$$
\rho(X, Y) = \frac{\text{Cov}(X, Y)}{\sigma_X \sigma_Y}.
$$

Correlation measures linear dependence only. Two variables can have $\rho = 0$ and still be dependent. Correlation does not imply causation.
````
