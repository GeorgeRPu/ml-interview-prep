# Confidence Intervals

## What is a confidence interval?

Suppose we are estimating the percentage of people who plan on voting for Democrats in the next election. We can use the sample mean to estimate the mean of a population based on a sample, but that value is almost certainly off. A confidence interval gives us a range of values where we know the population mean has an $\alpha$ chance of being in the interval.

## How do we construct a confidence interval?

Because $\sqrt{n}(\bar{X} - \mu)$ follows a Normal distribution (for large enough samples, $n > 30$ is the rule of thumb), we can use the properties of the Normal distribution to construct confidence intervals.

First, let the **critical value** of a $\alpha$-confidence interval be the value $z_{\alpha/2}$ such that the $\Pr(Z > z_{\alpha/2})$ is $\alpha/2$. For a 95% confidence interval, $\alpha = 0.05$ and $z_{\alpha/2} = 1.96$.

Let $\bar{X}$ be the sample mean and $s$ be the sample standard deviation. The 95% confidence interval for the population mean $\mu$ is

$$
\bar{X} \pm 1.96 \cdot \frac{s}{\sqrt{n}}.
$$

![50% Confidence Intervals from a Normal Distribution](https://upload.wikimedia.org/wikipedia/commons/5/5c/Normal_distribution_50%25_CI_illustration.svg)
*Figure 1: Repeated 50% confidence intervals drawn from a Normal distribution. Roughly half of the intervals contain the true mean.*
