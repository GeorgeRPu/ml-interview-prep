# Hypothesis Testing

## What is hypothesis testing?

Hypothesis testing is a statistical method for deciding whether data provides sufficient evidence to reject a null hypothesis in favor of an alternative hypothesis. It is commonly used in A/B testing to determine if a change has a statistically significant effect on a metric.

The general procedure for hypothesis testing is:
1. Formulate null hypothesis $H_0$ and alternative hypothesis $H_1$.
2. Choose a significance level $\alpha$ (e.g., 0.05).
3. Collect data and compute a test statistic.
4. Calculate the p-value, which is the probability of observing data as extreme as the observed data under $H_0$.
5. If $p < \alpha$, reject $H_0$. Otherwise, we fail to reject $H_0$.

## Null and alternative hypotheses

````{prf:definition} Null and Alternative Hypotheses
The **null hypothesis** $H_0$ is the default assumption, e.g. "there is no difference" or "the coin is fair."

The **alternative hypothesis** $H_1$ is what we want to provide evidence for, e.g. "there is a difference" or "the coin is biased."
````

## What are Type I and Type II errors?

````{prf:definition} Type I and Type II Errors
A **Type I error** (false positive) is rejecting $H_0$ when it is true. Its probability is $\alpha$.

A **Type II error** (false negative) is failing to reject $H_0$ when $H_1$ is true. Its probability is $\beta$.
````

## p-value

````{prf:definition} p-value
The **p-value** is the probability of observing data at least as extreme as the observed data, assuming $H_0$ is true.

$$
p = \Pr\left(\text{data as extreme as observed} \mid H_0\right)
$$
````

A small p-value (typically $< 0.05$) provides evidence against $H_0$.

The p-value is NOT the probability that $H_0$ is true (that would be the posterior $\Pr\left(H_0 \mid D\right)$). It is the probability of the observed data given $H_0$, $\Pr\left(D \mid H_0\right)$.

## Significance level

````{prf:definition} Significance Level
The **significance level** $\alpha$ is the threshold for rejecting the null hypothesis. It is the maximum probability of a Type I error (false positive) that we are willing to tolerate. If $p < \alpha$, we reject $H_0$.
````

## Statistical power

````{prf:definition} Statistical Power
**Statistical power** is the probability of correctly rejecting $H_0$ when $H_1$ is true.

$$
\text{Power} = 1 - \beta = \Pr\left(\text{reject } H_0 \mid H_1 \text{ is true}\right)
$$
````

A typical target power is $0.8$ (i.e. 80% chance of detecting a real effect).

## How is power derived for a two-sample z-test?

Consider a two-sample z-test comparing means $\mu_0$ (control) and $\mu_1$ (treatment) with known variance $\sigma^2$ and $n$ samples per group. Under $H_0$, the test statistic

$$
Z = \frac{\bar{X}_1 - \bar{X}_0}{\sigma\sqrt{\frac{2}{n}}}
$$

follows $\mathcal{N}\left(0, 1\right)$. We reject $H_0$ when $|Z| > z_{\alpha/2}$.

And if $H_1$ is true? Let the true difference be $\delta = \mu_1 - \mu_0 \neq 0$. Then $Z$ is shifted by $\delta / \left(\sigma\sqrt{2/n}\right)$.

$$
Z \sim \mathcal{N}\left(\frac{\delta}{\sigma\sqrt{\frac{2}{n}}}, 1\right)
$$

Power is the probability that this shifted distribution falls in the rejection region.

$$
\text{Power} = \Phi\left(\frac{|\delta|}{\sigma\sqrt{\frac{2}{n}}} - z_{\alpha/2}\right)
$$

where $\Phi$ is the standard normal CDF and $z_{\alpha/2}$ is the critical value such that $\Pr\left(Z > z_{\alpha/2}\right) = \alpha/2$. The $\alpha/2$ comes from splitting the significance level across both tails of a two-sided test.

![Statistical power diagram](/_static/figures/statistical_power.png)

*Power ($1 - \beta$) is the area under the alternative distribution $H_1$ that falls in the rejection region (beyond the critical value $z_{\alpha/2}$). The grey region is $\beta$, the Type II error rate. For an effect size $\delta = 2.5$ at $\alpha = 0.05$, the power is 0.71.*

## What affects power?

From the formula above, we see 3 levers.

- **Power increases with larger sample size $n$.** Increasing $n$ makes the term $\frac{|\delta|}{\sigma\sqrt{2/n}}$ larger because the denominator $\sigma\sqrt{2/n}$ shrinks. Intuitively, more data reduces the standard error of the estimate, making it easier to distinguish a real effect from noise. The relationship is $\sim \sqrt{n}$, so to double the sensitivity (halve the detectable effect), you need 4x the sample size.

- **Power increases with larger effect size $|\delta|$.** A larger true difference $|\delta|$ shifts the distribution of the test statistic further from the null, making the real effect easier to detect. This also means it is much easier to detect a 10% change in a metric than a 1% change. The effect size is often standardized as Cohen's $d = \delta / \sigma$.

- **Power increases with higher $\alpha$.** A larger $\alpha$ means a less strict rejection threshold — $z_{\alpha/2}$ decreases, expanding the rejection region. For example, $z_{0.025} = 1.96$ but $z_{0.05} = 1.645$. This makes it easier to reject $H_0$, increasing power but also increasing the false positive rate. In practice, $\alpha$ is usually fixed at $0.05$, so the main knobs are sample size and minimum detectable effect.

Lower variance $\sigma^2$ also increases power. Reducing noise (through better measurement, stratification, or variance reduction techniques like CUPED) makes effects easier to detect without needing more samples.
