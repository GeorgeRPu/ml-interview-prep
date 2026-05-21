# Continuous Distributions

## Uniform distribution

````{prf:definition} Uniform Distribution
The **uniform distribution** assigns equal probability to all values in $[a, b]$.

$$
f(x) &= \frac{1}{b - a} \\
\quad \mathbb{E}[X] &= \frac{a + b}{2} \\
\text{Var}(X) &= \frac{(b-a)^2}{12}
$$
````

![Uniform Distribution](/_static/figures/uniform.png)

## Normal (Gaussian) distribution

````{prf:definition} Normal (Gaussian) Distribution
The **normal distribution** is a bell-shaped curve defined by its mean $\mu$ and variance $\sigma^2$.

$$
f(x) &= \frac{1}{\sigma\sqrt{2\pi}} \exp\left(-\frac{(x - \mu)^2}{2\sigma^2}\right) \\
\mathbb{E}[X] &= \mu \\
\text{Var}(X) &= \sigma^2
$$
````

The 68-95-99.7 rule says approximately 68%, 95%, and 99.7% of values lie within 1, 2, and 3 standard deviations of the mean.

![Normal Distribution](/_static/figures/normal.png)

## Exponential distribution

````{prf:definition} Exponential Distribution
The **exponential distribution** models the time between events in a Poisson process.

$$
f(x) &= \lambda e^{-\lambda x} \\
\quad \mathbb{E}[X] &= \frac{1}{\lambda} \\
\text{Var}(X) &= \frac{1}{\lambda^2}
$$

````

Like the geometric distribution, the exponential is memoryless: $P(X > s + t \mid X > s) = P(X > t)$.

![Exponential Distribution](/_static/figures/exponential.png)
