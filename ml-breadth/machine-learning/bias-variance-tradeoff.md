# Bias-Variance Tradeoff

## What is bias?

Bias in the error from erroneous assumptions in the learning algorithm. For example, a logistic regression model has high bias because it assumes a linear decision boundary. If the true decision boundary is nonlinear, the logistic regression model will consistently underfit the data.

```{prf:definition} Bias
:label: bias

The **bias** of a learned function $\hat{f}$ at a point $x$ is

$$
\text{Bias}(\hat{f}(x; \mathcal{D})) = \mathbb{E}_{\mathcal{D}}[\hat{f}(x; \mathcal{D})] - f(x)
$$

where $f$ is the true function and $\mathcal{D}$ is the training data. A model is **unbiased** if $\mathbb{E}_{\mathcal{D}}[\hat{f}(x; \mathcal{D})] = f(x)$ for all $x$.
```

## What is variance?

Variance is the error from sensitivity to small fluctuations in the training data. High variance model will fit the training data very closely, including noise which will not generalize well, aka overfitting.

```{prf:definition} Variance
:label: variance

The **variance** of a learned function $\hat{f}$ at a point $x$ is

$$
\text{Var}(\hat{f}(x; \mathcal{D})) = \mathbb{E}_{\mathcal{D}}\left[(\hat{f}(x; \mathcal{D}) - \mathbb{E}_{\mathcal{D}}[\hat{f}(x; \mathcal{D})])^2\right]
$$
```

## Explain the bias-variance tradeoff.

The mean squarederror of our model can be decomposed into three components: bias, variance, and irreducible error (noise). A good model should be low bias and low variance.

$$
\mathbb{E}_{\mathcal{D}}[(\hat{f}(x; \mathcal{D}) - f(x))^2] = \text{Bias}(\hat{f}(x; \mathcal{D}))^2 + \text{Var}(\hat{f}(x; \mathcal{D})) + \sigma^2
$$

where $\sigma^2$ is the variance of the noise in the data, which is irreducible.

```{prf:proof}
Let $y = f(x) + \epsilon$ where $\mathbb{E}[\epsilon] = 0$ and $\text{Var}(\epsilon) = \sigma^2$.  The mean squared error of our model $\hat{f}$ acorss all possible training datasets $\mathcal{D}$ is

$$
\begin{aligned}
\mathbb{E}_{\mathcal{D}, \epsilon}\left[(y - \hat{f}(x))^2\right]
&= \mathbb{E}_{\mathcal{D}, \epsilon}\left[(f(x) + \epsilon - \hat{f}(x))^2\right] \\
&= \mathbb{E}_{\mathcal{D}, \epsilon}\left[((f(x) - \hat{f}(x)) + \epsilon)^2\right] \\
&= \mathbb{E}_{\mathcal{D}, \epsilon}\left[(f(x) - \hat{f}(x))^2\right] + 2\mathbb{E}_{\mathcal{D}, \epsilon}\left[(f(x) - \hat{f}(x))\epsilon\right] + \mathbb{E}_{\mathcal{D}, \epsilon}\left[\epsilon^2\right]
\end{aligned}
$$

Since $\epsilon$ is independent of $\hat{f}$,

$$
2\mathbb{E}_{\mathcal{D}, \epsilon}\left[(f(x) - \hat{f}(x))\epsilon\right] = 2\mathbb{E}_{\mathcal{D}, \epsilon}[f(x) - \hat{f}(x)] \cdot \mathbb{E}_{\mathcal{D}, \epsilon}[\epsilon] = 0
$$

because $\mathbb{E}_{\mathcal{D}, \epsilon}[\epsilon] = 0$. For the last term,

$$
\mathbb{E}_{\mathcal{D}, \epsilon}[\epsilon^2] = \text{Var}(\epsilon) + \mathbb{E}_{\mathcal{D}, \epsilon}[\epsilon]^2 = \sigma^2 + 0 = \sigma^2.
$$

It remains to decompose the first term. Add and subtract $\bar{f}(x) = \mathbb{E}_{\mathcal{D}}[\hat{f}(x; \mathcal{D})]$.

$$
\begin{aligned}
\mathbb{E}_{\mathcal{D}, \epsilon}\left[(f(x) - \hat{f}(x))^2\right]
&= \mathbb{E}_{\mathcal{D}, \epsilon}\left[((f(x) - \bar{f}(x)) + (\bar{f}(x) - \hat{f}(x)))^2\right] \\
&= (f(x) - \bar{f}(x))^2 + 2(f(x) - \bar{f}(x))\mathbb{E}_{\mathcal{D}, \epsilon}\left[\bar{f}(x) - \hat{f}(x)\right] + \mathbb{E}_{\mathcal{D}, \epsilon}\left[(\hat{f}(x) - \bar{f}(x))^2\right]
\end{aligned}
$$

The cross term vanishes because

$$
\mathbb{E}_{\mathcal{D}, \epsilon}[\bar{f}(x) - \hat{f}(x)] = \bar{f}(x) - \mathbb{E}_{\mathcal{D}, \epsilon}[\hat{f}(x)] = 0.
$$

as $\bar{f}(x) = \mathbb{E}_{\mathcal{D}}[\hat{f}(x; \mathcal{D})]$. Therefore, in our final decomposition, the first term is $\text{Bias}(\hat{f}(x))^2$ and the last term is $\text{Var}(\hat{f}(x))$.

$$
\mathbb{E}_{\mathcal{D}, \epsilon}\left[(y - \hat{f}(x))^2\right] = \text{Bias}(\hat{f}(x))^2 + \text{Var}(\hat{f}(x)) + \sigma^2
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
