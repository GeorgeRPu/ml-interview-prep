# Autocorrelation

## What is autocorrelation?

For a time series, autocorrelation is the correlation between a time series and
a delayed copy.

Let $\{X_t\}$ be a time series. The **autocorrelation** between times $t_1$ and $t_2$ is

$$
R_{XX}\left(t_1, t_2\right) = \mathbb{E}\left[X_t, \overline{X_{t_2}}\right]
$$

where $\overline{X_{t_2}}$ is the complex conjugate of $X_{t_2}$ (if $X_t$ is real-valued, this is just $X_{t_2}$).

For random vectors $\mathbf{X}, \mathbf{Y} \in \mathbb{C}^n$, the **autocorrelation matrix** is defined as

$$
R_{XX} = \mathbb{E}\left[\mathbf{X} \mathbf{X}^*\right]
$$

## What is autocovariance?

The **auto-covariance** between times $t_1$ and $t_2$ is

$$
K_{XX}\left(t_1, t_2\right) = \text{Cov}\left(X_{t_1}, X_{t_2}\right) = \mathbb{E}\left[\left(X_{t_1} - \mu\right)\left(\overline{X_{t_2}} - \overline{\mu}\right)\right].
$$

## What is the relationship between autocorrelation and auto-covariance?

Let $\mu_t = \mathbb{E}\left[X_t\right]$ be the mean and $\sigma_t^2 = \text{Var}\left[X_t\right]$ be the variance at time $t$. Then the autocorrelation and auto-covariance are related by

$$
\begin{aligned}
R_{XX}\left(t_1, t_2\right) &= \text{Cov}\left(X_{t_1}, X_{t_2}\right) \\
&= \mathbb{E}\left[\left(X_{t_1} - \mu_{t_1}\right)\left(\overline{X_{t_2} - \mu_{t_2}}\right)\right] \\
&= \mathbb{E}\left[\left(X_{t_1} - \mu_{t_1}\right)\left(\overline{X_{t_2}} - \overline{\mu_{t_2}}\right)\right] \\
&= \mathbb{E}\left[X_{t_1}\overline{X_{t_2}}\right] - \mathbb{E}\left[X_{t_1}\right]\overline{\mu_{t_2}} - \mu_{t_1}\mathbb{E}\left[\overline{X_{t_2}}\right] + \mu_{t_1} \overline{\mu_{t_2}} \\
&= \mathbb{E}\left[X_{t_1}\overline{X_{t_2}}\right] - \mu_{t_1} \overline{\mu_{t_2}} - \mu_{t_1} \overline{\mu_{t_2}} + \mu_{t_1} \overline{\mu_{t_2}} \\
&= K_{XX}\left(t_1, t_2\right) - \mu_{t_1} \overline{\mu_{t_2}}
\end{aligned}
$$
