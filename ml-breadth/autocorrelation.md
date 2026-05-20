# Autocorrelation

## What is Autocorrelation?

For a time series, autocorrelation is the correlation between a time series and
a delayed copy.

Let $\{X_t\}$ be a time series. The **autocorrelation** between times $t_1$ and $t_2$ is

$$
R_{XX}(t_1, t_2) = \mathbb{E}[X_t, \overline{X_{t_2}}]
$$

where $\overline{X_{t_2}}$ is the complex conjugate of $X_{t_2}$ (if $X_t$ is real-valued, this is just $X_{t_2}$).

For random vectors $\mathbf{X}, \mathbf{Y} \in \mathbb{C}^n$, the **autocorrelation matrix** is defined as

$$
R_{XX} = \mathbb{E}[\mathbf{X} \mathbf{X}^*]
$$

## What is autocovariance?

The **auto-covariance** between times $t_1$ and $t_2$ is

$$
K_{XX}(t_1, t_2) = \text{Cov}(X_{t_1}, X_{t_2}) = \mathbb{E}[(X_{t_1} - \mu)(\overline{X_{t_2}} - \overline{\mu})].
$$

## What is the relationship between autocorrelation and auto-covariance?

Let $\mu_t = \mathbb{E}[X_t]$ be the mean and $\sigma_t^2 = \text{Var}(X_t)$ be the variance at time $t$. Then the autocorrelation and auto-covariance are related by

$$
\begin{aligned}
R_{XX}(t_1, t_2) &= \text{Cov}(X_{t_1}, X_{t_2}) \\
&= \mathbb{E}[(X_{t_1} - \mu_{t_1})(\overline{X_{t_2} - \mu_{t_2}})] \\
&= \mathbb{E}[(X_{t_1} - \mu_{t_1})(\overline{X_{t_2}} - \overline{\mu_{t_2}})] \\
&= \mathbb{E}[X_{t_1}\overline{X_{t_2}}] - \mathbb{E}[X_{t_1}]\overline{\mu_{t_2}} - \mu_{t_1}\mathbb{E}[\overline{X_{t_2}}] + \mu_{t_1} \overline{\mu_{t_2}} \\
&= \mathbb{E}[X_{t_1}\overline{X_{t_2}}] - \mu_{t_1} \overline{\mu_{t_2}} - \mu_{t_1} \overline{\mu_{t_2}} + \mu_{t_1} \overline{\mu_{t_2}} \\
&= K_{XX}(t_1, t_2) - \mu_{t_1} \overline{\mu_{t_2}}
\end{aligned}
$$
