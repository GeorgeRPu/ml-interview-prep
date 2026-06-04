# A/B Testing

## What is A/B testing?

A randomized controlled experiment comparing a control group (A) with a treatment group (B) to measure the effect of a change. The general procedure for running an A/B test is:

1. Define hypothesis and success metric
2. Determine sample size (power analysis)
3. Randomly assign users to control and treatment
4. Run the experiment for a predetermined duration
5. Analyze results and make a decision

## Minimum detectable effect

MDE is the smallest effect size the experiment is designed to reliably detect. MDE can be expressed in absolute terms (e.g., 1 percentage point) or relative terms (e.g., a 2% relative lift). It is chosen *before* the experiment runs and determines how many samples you need.

For example, if the baseline ad click rate is 20%, an MDE of 10 percentage points means the experiment is designed to detect a shift from 20% to 30% (or 10%). If the true effect is smaller than 10 percentage points, the experiment will likely fail to reach significance even if a real effect exists.

A smaller MDE requires a larger sample size to detect, while a larger MDE can be detected with fewer samples. Choosing an appropriate MDE is a balance between wanting to detect meaningful effects and the practical constraints of running the experiment (e.g., traffic, time).

## Baseline metric variance

The variance of the metric being measured also affects sample size. Higher variance requires more samples to detect the same effect size. For binary metrics (e.g., click-through rate), the variance is $p(1-p)$ where $p$ is the baseline rate. For continuous metrics, you can estimate variance from historical data.

## How do we determine the sample size needed for an A/B test?

Before running an experiment, we need to decide on the following parameters:

- Significance level $\alpha$ (typically $0.05$) - probability of a false positive (Type I error), incorrectly rejecting the null hypothesis when it is true
- Desired power $1 - \beta$ (typically $0.8$) - probability of a false negative (Type II error), failing to reject the null hypothesis when the alternative is true
- Minimum detectable effect (MDE)
- Baseline metric variance

The sample size depends on the test being used and the parameters above.

For example, suppose we are trying to increase the current conversion rate from $p_1 = 0.10$. We want to be able to detect at least a 1 percentage point lift to $p_2 = 0.11$. We choose $\alpha = 0.05$ and power $1 - \beta = 0.80$.

For comparing two proportions $p_1$ and $p_2$ where $\text{MDE} = |p_1 - p_2|$:

$$
n \approx \frac{\left(z_{\alpha/2} + z_\beta\right)^2 \left(p_1\left(1-p_1\right) + p_2\left(1-p_2\right)\right)}{\left(p_1 - p_2\right)^2}
$$

````{prf:proof}
The formula is derived by inverting the power equation for a two-sample z-test on proportions.

Consider comparing proportions $p_1$ (control) and $p_2$ (treatment) with $n$ samples per group. The test statistic is:

$$
Z = \frac{\hat{p}_2 - \hat{p}_1}{\sqrt{\frac{p_1\left(1-p_1\right)}{n} + \frac{p_2\left(1-p_2\right)}{n}}}
$$

Under $H_0: p_1 = p_2$, the test statistic follows $\mathcal{N}\left(0, 1\right)$. We reject when $|Z| > z_{\alpha/2}$.

Under $H_1$, the true difference is $\delta = p_2 - p_1 \neq 0$ which shifts the distribution of $Z$.

$$
Z \sim \mathcal{N}\left(\frac{\delta}{\sqrt{\frac{p_1\left(1-p_1\right) + p_2\left(1-p_2\right)}{n}}},\; 1\right)
$$

Let $s = \sqrt{\frac{p_1\left(1-p_1\right) + p_2\left(1-p_2\right)}{n}}$. Power is the probability that the shifted $Z$ falls in the rejection region.

$$
1 - \beta = \Phi\left(\frac{|\delta|}{s} - z_{\alpha/2}\right)
$$

Applying $\Phi^{-1}$ to both sides, we obtain

$$
z_\beta = \frac{|\delta|}{s} - z_{\alpha/2}.
$$

Rearrange to isolate $\text{SE}$.

$$
s = \frac{|\delta|}{z_{\alpha/2} + z_\beta} = \frac{|p_1 - p_2|}{z_{\alpha/2} + z_\beta}
$$

Substitute back the definition of $s$ and square both sides.

$$
\frac{p_1\left(1-p_1\right) + p_2\left(1-p_2\right)}{n} = \frac{\left(p_1 - p_2\right)^2}{\left(z_{\alpha/2} + z_\beta\right)^2}
$$

Solving for $n$ yields the formula above.
````

Plugging in the numbers...

$$
n \approx \frac{\left(1.96 + 0.84\right)^2 \left(0.10 \times 0.90 + 0.11 \times 0.89\right)}{\left(0.01\right)^2} = \frac{7.84 \times 0.1879}{0.0001} \approx 14{,}731 \text{ per group}
$$

So we need roughly 14,700 users in each of the control and treatment groups (or 29,400 total). If the site gets 2,000 eligible users per day, the experiment would need to run for about 15 days.

## How long to run an experiment?

The minimum duration is driven by the sample size calculation and traffic. But even after reaching the required sample size, there are several reasons to keep the experiment running longer.

- **Capture day-of-week effects**. Run the experiment for at least one week to capture day-of-week patterns in user behavior.

- **Account for novelty and primacy effects**. A **novelty effect** inflates the treatment metric early on because users engage more with something new. A **primacy effect** deflates it because users resist change and revert to old habits. Both decay over time, so a short experiment may capture a transient effect rather than the steady-state impact.

- **Do not stop early for significance (peeking problem).** Checking the p-value repeatedly as data accumulates and stopping as soon as $p < \alpha$ inflates the false positive rate well beyond $\alpha$. Instead of one experiment, you are effectively running many experiments. If early stopping is needed, use sequential testing methods (e.g., group sequential designs, always-valid p-values) that explicitly control the error rate across multiple looks.

## How do we handle multiple treatments or metrics?

When testing multiple hypotheses simultaneously (e.g., testing many metrics or many variants), the probability of at least one false positive increases. With $m$ independent tests at significance level $\alpha$,

$$
\Pr\left(\text{at least one false positive}\right) = 1 - \left(1 - \alpha\right)^m
$$

There are corrections to control the family-wise error rate (FWER)—the probability of making at least one false positive across all $m$ tests—or the false discovery rate (FDR)—the expected proportion of rejected hypotheses that are false positives—when performing multiple comparisons.

````{prf:definition} Bonferroni Correction
:label: bonferroni-correction
The **Bonferroni correction** controls sets the per-test significance level to

$$
\alpha' = \frac{\alpha}{m}
$$

to keep the overall FWER at $\alpha$.
````

Bonferroni is simple but conservative. As $m$ grows, $\alpha'$ becomes very small and power drops, making it hard to detect real effects.

````{prf:definition} Benjamini-Hochberg Procedure
:label: benjamini-hochberg-procedure
Given $m$ tests, the **Benjamini-Hochberg (BH) procedure** is as follows:

1. Sort the p-values in ascending order: $p_{\left(1\right)} \leq p_{\left(2\right)} \leq \cdots \leq p_{\left(m\right)}$.
2. Find the largest $k$ such that $p_{\left(k\right)} \leq \frac{k}{m} \alpha$.
3. Reject all hypotheses $H_{\left(1\right)}, \ldots, H_{\left(k\right)}$.

BH controls the FDR at level $\alpha$ assuming the tests are independent or satisfy certain dependence conditions such as positive correlation between test statistics.
````

BH is less conservative than Bonferroni because it controls the rate of false discoveries among rejected hypotheses rather than the probability of any false positive at all. This makes it more powerful when many tests are conducted, which is why it is widely used in A/B testing platforms that track dozens of metrics per experiment.

## How do we handle network effects or interference between users?

Standard A/B tests make the **stable unit treatment value assumption (SUTVA)** {cite}`Rubin1980` — that one user's treatment assignment does not affect another user's outcome. This breaks down when users interact with each other. For example, a ride-sharing company testing a new pricing algorithm may cause treated riders to request more rides, which increases demand for all drivers. Control riders experience longer wait times not because of their own treatment, but because of the treatment applied to others.

Mitigation strategies:

- **Cluster-based randomization** {cite}`Ugander2013`. Instead of randomizing individual users, randomize entire clusters (e.g., geographic markets, schools, or friend groups) where between-cluster interference is minimal. All users within a cluster receive the same treatment, so within-cluster spillover no longer biases the comparison. The tradeoff is that the effective sample size drops from the number of users to the number of clusters, requiring more total users to achieve the same power.

  A special case is **ego-cluster randomization** {cite}`SaintJacques2019`, where each cluster consists of a focal user (the "ego") and their immediate network connections (the "alters"), all assigned to the same treatment. This is useful on social platforms where interference flows through direct connections and geographic clusters are not meaningful.

- **Switchback experiments** {cite}`Bojinov2023`. Alternate between treatment and control across time periods within the same unit. For example, a ride-sharing company runs a new pricing algorithm for 2-hour blocks, then reverts for 2-hour blocks, and compares outcomes across treatment vs. control periods. This is useful when there are too few geographic clusters for adequate power. The tradeoff is **carryover effects** — behavior in one time period can bleed into the next, so the design must account for washout periods between switches.

- **Two-stage randomization (saturation design)** {cite}`Hudgens2008`. First randomize clusters to different treatment saturation levels (e.g., 0%, 25%, 75%, 100% of users treated), then randomize individuals within each cluster. This allows estimating both the **direct effect** (impact on treated users) and the **spillover effect** (impact on untreated users within a partially treated cluster) separately, rather than just trying to avoid interference.

## References

```{bibliography}
:filter: docname in docnames
```
