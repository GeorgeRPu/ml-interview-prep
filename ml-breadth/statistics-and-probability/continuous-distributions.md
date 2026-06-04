# Continuous Distributions

## Uniform distribution

````{prf:definition} Uniform Distribution
:label: uniform-distribution
The **uniform distribution** assigns equal probability to all values in $\left[a, b\right]$.

$$
f\left(x\right) &= \frac{1}{b - a} \\
\quad \mathbb{E}\left[X\right] &= \frac{a + b}{2} \\
\text{Var}\left[X\right] &= \frac{\left(b-a\right)^2}{12}
$$
````

![Uniform Distribution](/_static/figures/uniform.png)

## Normal (Gaussian) distribution

````{prf:definition} Normal (Gaussian) Distribution
:label: normal-gaussian-distribution
The **normal distribution** is a bell-shaped curve defined by its mean $\mu$ and variance $\sigma^2$.

$$
f\left(x\right) &= \frac{1}{\sigma\sqrt{2\pi}} \exp\left(-\frac{\left(x - \mu\right)^2}{2\sigma^2}\right) \\
\mathbb{E}\left[X\right] &= \mu \\
\text{Var}\left[X\right] &= \sigma^2
$$
````

The 68-95-99.7 rule says approximately 68%, 95%, and 99.7% of values lie within 1, 2, and 3 standard deviations of the mean.

![Normal Distribution](/_static/figures/normal.png)

## Exponential distribution

````{prf:definition} Exponential Distribution
:label: exponential-distribution
The **exponential distribution** models the time between events in a Poisson process.

$$
f\left(x\right) &= \lambda e^{-\lambda x} \\
\quad \mathbb{E}\left[X\right] &= \frac{1}{\lambda} \\
\text{Var}\left[X\right] &= \frac{1}{\lambda^2}
$$

````

Like the geometric distribution, the exponential is memoryless: $P\left(X > s + t \mid X > s\right) = P\left(X > t\right)$.

![Exponential Distribution](/_static/figures/exponential.png)
