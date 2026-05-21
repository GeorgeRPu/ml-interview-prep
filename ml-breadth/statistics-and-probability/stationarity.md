# Stationarity

## What is stationarity?

Stationarity or a stationary process is a stochastic process whose underlying
statistical properties don't change over time.

More formally, a stochastic process $\{X_t\}$ is **strictly stationary** if the
joint distributions

$$
F(x_{t_1}, x_{t_2}, ..., x_{t_k}) = F(x_{t_1+h}, x_{t_2+h}, ..., x_{t_k+h})
$$

for all $t_1, t_2, ..., t_k$ and for all $h$.

Examples of strictly stationary processes:
- **White noise**: A sequence of iid normal random variables $X_t \sim \mathcal{N}(0, \sigma^2)$. Since draws are independent and identically distributed (iid), the joint distribution is trivially shift-invariant.

![White Noise](https://upload.wikimedia.org/wikipedia/commons/c/c1/White_noise.svg)
*Figure 1: An example of white noise. Each sample is drawn independently from the same distribution, producing no discernible pattern or trend.*

- **Coin flip sequences**: Repeated fair coin flips encoded as $\{+1, -1\}$. Each flip is iid Bernoulli, so the full joint distribution is shift-invariant.

A weaker form of stationarity is called **weak stationarity** or
**wide-sense stationarity**, which requires that the mean and autocovariance
of the process are constant over time, and that the variance is finite.

$$
\begin{aligned}
\mathbb{E}[X_t] &= \mathbb{E}[X_{t+h}] \quad &&\text{for all } t, h \\
K_{XX}(t_1, t_2) &= K_{XX}(t_2 - t_1, 0) \quad &&\text{for all } t_1, t_2 \\
\mathbb{E}[X_t^2] &< \infty \quad &&\text{for all } t
\end{aligned}
$$

Examples of weakly stationary processes:
- **AR(1) process**: $X_t = \phi X_{t-1} + \epsilon_t$ where $\epsilon_t$ is white noise and $|\phi| < 1$ for $t \in \mathbb{Z}$. This is the first-order autoregressive process. It is weakly stationary because
  1. $E[X_t] = \sum_{i=0}^{\infty} \phi^i E[\epsilon_i] = 0$. The mean is constant.
  2. Using the infinite sum representation $X_t = \sum_{i=0}^{\infty} \phi^i \epsilon_{t-i}$:

     $$
     \begin{aligned}
     K_{XX}(t, t+h) &= \text{Cov}(X_t, X_{t+h}) \\
     &= \text{Cov}\left(\sum_{i=0}^{\infty} \phi^i \epsilon_{t-i},\; \sum_{j=0}^{\infty} \phi^j \epsilon_{t+h-j}\right) \\
     &= \sum_{i=0}^{\infty} \sum_{j=0}^{\infty} \phi^i \phi^j \text{Cov}(\epsilon_{t-i}, \epsilon_{t+h-j})
     \end{aligned}
     $$

     Since $\epsilon_t$ is white noise, $\text{Cov}(\epsilon_{t-i}, \epsilon_{t+h-j}) = \sigma^2$ only when
     $t - i = t + h - j$, i.e. $j = i + h$. All other cross-terms are zero. Substituting:

     $$
     \begin{aligned}
     K_{XX}(t, t+h) &= \sum_{i=0}^{\infty} \phi^i \phi^{i+h} \sigma^2 \\
     &= \sigma^2 \phi^h \sum_{i=0}^{\infty} \phi^{2i} \\
     &= \frac{\sigma^2 \phi^h}{1 - \phi^2}
     \end{aligned}
     $$

     This depends only on $h$, not on $t$.
  3. ince $\mathbb{E}[X_t] = 0$, we have
     $\mathbb{E}[X_t^2] = \text{Var}(X_t)$. Using the infinite sum representation:

     $$
     \begin{aligned}
     \mathbb{E}[X_t^2] &= \text{Var}(X_t) \\
     &= \Var\left(\sum_{i=0}^{\infty} \phi^i \epsilon_{t-i}\right) \\
     &= \sum_{i=0}^{\infty} \phi^{2i} \text{Var}(\epsilon_{t-i}) \quad \text{(independence of } \epsilon \text{)} \\
     &= \sigma^2 \sum_{i=0}^{\infty} \phi^{2i} \\
     &= \frac{\sigma^2}{1 - \phi^2} \quad \text{(geometric series, converges since } |\phi| < 1 \text{)}
     \end{aligned}
     $$

     This is finite, so the condition is satisfied.
- **MA(q) process**: $X_t = \epsilon_t + \theta_1 \epsilon_{t-1} + ... + \theta_q \epsilon_{t-q}$. Any finite moving average of white noise is always weakly stationary since the mean is zero and autocovariance depends only on lag (and is zero beyond lag $q$).
- **Daily temperature residuals**: After removing the seasonal trend from daily temperatures, the residuals have approximately constant mean and variance with autocovariance that depends on lag — a classic weakly stationary signal in climate modeling.

![Daily Temperature Residuals](/_static/figures/daily_temperature_residuals.svg)
*Figure 2: Daily mean temperatures from Central Park, NYC (2021–2023) decomposed into a fitted seasonal component and residuals. After removing the seasonal trend, the residuals have approximately constant mean and variance — a weakly stationary signal.*

## Why is stationarity important?

Stationarity is a fundamental assumption in many time series models and
analyses. If a process is non-stationary, its properties change over time,
making it more difficult to model and predict.

1. **Estimation from a single realization**: We typically observe one instance
of a time series. Stationarity lets us treat different time windows as
"repeated samples" from the same distribution.

2. **Forecasting**: If statistical properties change over time, a model fit on
historical data won't generalize to the future. Stationarity guarantees that
the patterns you learned persist.

3. **Theoretical guarantees**: Results like the ergodic theorem (time averages
converge to ensemble averages) and the Wold decomposition (any stationary
process = deterministic + $MA(\infty)$) require stationarity.

4. **Model validity**: ARMA models, spectral analysis, and Granger causality
all assume stationarity. Applying them to non-stationary data produces spurious
results. A classic example is spurious regression, where two independent
random walks appear highly correlated simply because both trend upward.
