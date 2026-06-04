# Hypothesis Tests

## Z-test

````{prf:definition} Z-test
:label: z-test
The z-test tests whether a sample mean differs from a hypothesized population mean. It requires that the population standard deviation $\sigma$ be known or $n$ is large enough that you can use the sample standard deviation ($n \geq 30$).

$$
z = \frac{\bar{X} - \mu_0}{\sigma / \sqrt{n}}
$$
````

## t-test

````{prf:definition} t-test
:label: t-test
The t-test tests whether a sample mean differs from a hypothesized population mean when the population standard deviation is *unknown* and estimated from the sample. The test statistic follows a t-distribution with $n-1$ degrees of freedom.

$$
t = \frac{\bar{X} - \mu_0}{s / \sqrt{n}}
$$

where $s$ is the sample standard deviation.

$$
s = \sqrt{\frac{1}{n-1} \sum_{i=1}^{n} \left(X_i - \bar{X}\right)^2}
$$
````

![t-distribution vs. standard normal](/_static/figures/t_vs_normal.png)

*The t-distribution has heavier tails than the standard normal, reflecting the extra uncertainty from estimating $\sigma$ with $s$. As the degrees of freedom increase, the tails thin and the t-distribution converges to $\mathcal{N}(0, 1)$.*

The denominator is $n-1$ rather than $n$ due to **Bessel's correction**. Dividing by $n$ systematically underestimates the true variance because $\bar{X}$ is closer to the sample points than the true mean $\mu$. Dividing by $n-1$ makes $s^2$ an unbiased estimator of $\sigma^2$. The substitution of $s$ for the unknown $\sigma$ introduces extra uncertainty, which is why the test statistic follows the heavier-tailed t-distribution rather than the normal. As $n \to \infty$, $s \to \sigma$ and the t-distribution converges to the standard normal, so the t-test and z-test become equivalent.

## Two-sample t-test

The two-sample t-test compares the means of two independent groups to determine if they are different.

````{prf:definition} Equal-variance (Student's) Two-sample t-test
:label: equal-variance-students-two-sample-t-test
The equal-variance (Student's) two-sample t-test assumes both groups share the same variance $\sigma_1^2 = \sigma_2^2$. The test statistic uses a pooled variance estimate.

$$
t = \frac{\bar{X}_1 - \bar{X}_2}{s_p \sqrt{\frac{1}{n_1} + \frac{1}{n_2}}}, \quad s_p^2 = \frac{\left(n_1 - 1\right)s_1^2 + \left(n_2 - 1\right)s_2^2}{n_1 + n_2 - 2}
$$

where $s_p^2$ is the pooled variance and the test statistic follows a t-distribution with $n_1 + n_2 - 2$ degrees of freedom.
````

````{prf:definition} Welch's t-test
:label: welchs-t-test
Welch's t-test is a variation of the two-sample t-test that, instead of assuming equal variances, each group's variance is estimated separately.

$$
t = \frac{\bar{X}_1 - \bar{X}_2}{\sqrt{\frac{s_1^2}{n_1} + \frac{s_2^2}{n_2}}}
$$

The degrees of freedom are approximated by the **Welch-Satterthwaite equation**.

$$
\nu \approx \frac{\left(\frac{s_1^2}{n_1} + \frac{s_2^2}{n_2}\right)^2}{\frac{\left(s_1^2/n_1\right)^2}{n_1 - 1} + \frac{\left(s_2^2/n_2\right)^2}{n_2 - 1}}
$$
````

Welch's t-test is generally preferred over the equal-variance version because it is robust when variances are unequal and performs nearly identically when variances happen to be equal. Thus, unless you have strong reason to believe the variances are the same, default to Welch's.

## Paired t-test

````{prf:definition} Paired t-test
:label: paired-t-test
A **paired t-test** is used when the two samples are not independent but consist of matched pairs (e.g., the same user's behavior before and after a change). The test reduces to a one-sample t-test on the differences $d_i = X_{1,i} - X_{2,i}$.

$$
t = \frac{\bar{d}}{s_d / \sqrt{n}}
$$
````

The paired test is more powerful than the unpaired test when within-pair correlation is high, because it removes between-subject variability.

## Chi-squared test

````{prf:definition} Chi-squared Test
:label: chi-squared-test
The **chi-squared test** compares observed categorical frequencies to expected frequencies. Let $O_i$ be the observed count for category $i$ and $E_i$ be the expected count under the null hypothesis.

$$
\chi^2 = \sum \frac{\left(O_i - E_i\right)^2}{E_i}
$$

The test statistic follows a chi-squared distribution with degrees of freedom depending on the test type.
````

There are two main variants:

1. **Goodness-of-fit test**. Tests whether a single categorical variable follows a hypothesized distribution (e.g., are die rolls uniformly distributed?). The expected frequencies $E_i$ come from the hypothesized distribution. The test statistic follows a chi-squared distribution with $k - 1$ degrees of freedom, where $k$ is the number of categories.

2. **Test of independence**. Tests whether two categorical variables are independent using a **contingency table** which shows the joint distribution of the 2 variables. Under the null hypothesis of independence, the expected frequency for each cell is

$$
E_{ij} = \frac{R_i \cdot C_j}{N}
$$

where $R_i$ is the row total, $C_j$ is the column total, and $N$ is the grand total. The degrees of freedom are $\left(r - 1\right)\left(c - 1\right)$, where $r$ and $c$ are the number of rows and columns.

Both variants require that expected cell counts are sufficiently large (a common rule of thumb is $E_i \geq 5$). When this assumption is violated, Fisher's exact test is preferred.
