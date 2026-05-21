# Bias-Variance Tradeoff

## What is bias?

Bias in the error from erroneous assumptions in the learning algorithm. For example, a logistic regression model has high bias because it assumes a linear decision boundary. If the true decision boundary is nonlinear, the logistic regression model will consistently underfit the data.

```{prf:definition} Bias
:label: bias

The **bias** of a learned function $\hat{f}$ at a point $x$ is

$$
\text{Bias}\left[\hat{f}\left(x; \mathcal{D}\right)\right] = \mathbb{E}_{\mathcal{D}}\left[\hat{f}\left(x; \mathcal{D}\right)\right] - f\left(x\right)
$$

where $f$ is the true function and $\mathcal{D}$ is the training data. A model is **unbiased** if $\mathbb{E}_{\mathcal{D}}\left[\hat{f}\left(x; \mathcal{D}\right)\right] = f\left(x\right)$ for all $x$.
```

## What is variance?

Variance is the error from sensitivity to small fluctuations in the training data. High variance model will fit the training data very closely, including noise which will not generalize well, aka overfitting.

```{prf:definition} Variance
:label: variance

The **variance** of a learned function $\hat{f}$ at a point $x$ is

$$
\text{Var}\left[\hat{f}\left(x; \mathcal{D}\right)\right] = \mathbb{E}_{\mathcal{D}}\left[\left(\hat{f}\left(x; \mathcal{D}\right) - \mathbb{E}_{\mathcal{D}}\left[\hat{f}\left(x; \mathcal{D}\right)\right]\right)^2\right]
$$
```

## Explain the bias-variance tradeoff.

The mean squarederror of our model can be decomposed into three components: bias, variance, and irreducible error (noise). A good model should be low bias and low variance.

$$
\mathbb{E}_{\mathcal{D}}\left[\left(\hat{f}\left(x; \mathcal{D}\right) - f\left(x\right)\right)^2\right] = \text{Bias}\left[\hat{f}\left(x; \mathcal{D}\right)\right]^2 + \text{Var}\left[\hat{f}\left(x; \mathcal{D}\right)\right] + \sigma^2
$$

where $\sigma^2$ is the variance of the noise in the data, which is irreducible.

```{prf:proof}
Let $y = f\left(x\right) + \epsilon$ where $\mathbb{E}\left[\epsilon\right] = 0$ and $\text{Var}\left[\epsilon\right] = \sigma^2$.  The mean squared error of our model $\hat{f}$ acorss all possible training datasets $\mathcal{D}$ is

$$
\begin{aligned}
\mathbb{E}_{\mathcal{D}, \epsilon}\left[\left(y - \hat{f}\left(x\right)\right)^2\right]
&= \mathbb{E}_{\mathcal{D}, \epsilon}\left[\left(f\left(x\right) + \epsilon - \hat{f}\left(x\right)\right)^2\right] \\
&= \mathbb{E}_{\mathcal{D}, \epsilon}\left[\left(\left(f\left(x\right) - \hat{f}\left(x\right)\right) + \epsilon\right)^2\right] \\
&= \mathbb{E}_{\mathcal{D}, \epsilon}\left[\left(f\left(x\right) - \hat{f}\left(x\right)\right)^2\right] + 2\mathbb{E}_{\mathcal{D}, \epsilon}\left[\left(f\left(x\right) - \hat{f}\left(x\right)\right)\epsilon\right] + \mathbb{E}_{\mathcal{D}, \epsilon}\left[\epsilon^2\right]
\end{aligned}
$$

Since $\epsilon$ is independent of $\hat{f}$,

$$
2\mathbb{E}_{\mathcal{D}, \epsilon}\left[\left(f\left(x\right) - \hat{f}\left(x\right)\right)\epsilon\right] = 2\mathbb{E}_{\mathcal{D}, \epsilon}\left[f\left(x\right) - \hat{f}\left(x\right)\right] \cdot \mathbb{E}_{\mathcal{D}, \epsilon}\left[\epsilon\right] = 0
$$

because $\mathbb{E}_{\mathcal{D}, \epsilon}\left[\epsilon\right] = 0$. For the last term,

$$
\mathbb{E}_{\mathcal{D}, \epsilon}\left[\epsilon^2\right] = \text{Var}\left[\epsilon\right] + \mathbb{E}_{\mathcal{D}, \epsilon}\left[\epsilon\right]^2 = \sigma^2 + 0 = \sigma^2.
$$

It remains to decompose the first term. Add and subtract $\bar{f}\left(x\right) = \mathbb{E}_{\mathcal{D}}\left[\hat{f}\left(x; \mathcal{D}\right)\right]$.

$$
\begin{aligned}
\mathbb{E}_{\mathcal{D}, \epsilon}\left[\left(f\left(x\right) - \hat{f}\left(x\right)\right)^2\right]
&= \mathbb{E}_{\mathcal{D}, \epsilon}\left[\left(\left(f\left(x\right) - \bar{f}\left(x\right)\right) + \left(\bar{f}\left(x\right) - \hat{f}\left(x\right)\right)\right)^2\right] \\
&= \left(f\left(x\right) - \bar{f}\left(x\right)\right)^2 + 2\left(f\left(x\right) - \bar{f}\left(x\right)\right)\mathbb{E}_{\mathcal{D}, \epsilon}\left[\bar{f}\left(x\right) - \hat{f}\left(x\right)\right] + \mathbb{E}_{\mathcal{D}, \epsilon}\left[\left(\hat{f}\left(x\right) - \bar{f}\left(x\right)\right)^2\right]
\end{aligned}
$$

The cross term vanishes because

$$
\mathbb{E}_{\mathcal{D}, \epsilon}\left[\bar{f}\left(x\right) - \hat{f}\left(x\right)\right] = \bar{f}\left(x\right) - \mathbb{E}_{\mathcal{D}, \epsilon}\left[\hat{f}\left(x\right)\right] = 0.
$$

as $\bar{f}\left(x\right) = \mathbb{E}_{\mathcal{D}}\left[\hat{f}\left(x; \mathcal{D}\right)\right]$. Therefore, in our final decomposition, the first term is $\text{Bias}\left[\hat{f}\left(x\right)\right]^2$ and the last term is $\text{Var}\left[\hat{f}\left(x\right)\right]$.

$$
\mathbb{E}_{\mathcal{D}, \epsilon}\left[\left(y - \hat{f}\left(x\right)\right)^2\right] = \text{Bias}\left[\hat{f}\left(x\right)\right]^2 + \text{Var}\left[\hat{f}\left(x\right)\right] + \sigma^2
$$
```

However, there is a tradeoff between bias and variance. As we make our model more flexible (e.g. by adding more parameters), we reduce bias because the model can fit the training data better but this increases variance.

![Bias and variance contributing to total error](https://upload.wikimedia.org/wikipedia/commons/9/9f/Bias_and_variance_contributing_to_total_error.svg)
*Figure 1: As model complexity increases, bias decreases but variance increases.*

## Give an example of a high bias model and a high variance model.

- High bias: logistic regression.
- High variance: deep neural network.

## How does bias-variance tradeoff for deep learning?

Recent research has found that certain models exhibit a phenomenon called **double descent** where increasing model capacity temporarily increases overfitting but then starts reducing test error past a point. This defies traditional bias-variance tradeoff which predicts that test error should keep increasing, as models become higher and higher variance.

The peak in test error occurs at the **interpolation threshold**, where the model has just enough capacity to perfectly fit the training data. At this point, the model is forced into a unique solution that memorizes every training example, including noise. Beyond this threshold, the model becomes overparameterized—there are many solutions that fit the training data, and gradient descent tends to find smoother ones that generalize better.

![Double descent in a two-layer neural network](https://upload.wikimedia.org/wikipedia/commons/d/d7/Double_descent_in_a_two-layer_neural_network_%28Figure_3a_from_Rocks_et_al._2022%29.png)
*Figure 2: Double descent in a two-layer neural network. Test error first increases then decreases as model complexity grows past the interpolation threshold (Rocks et al., 2022).*
