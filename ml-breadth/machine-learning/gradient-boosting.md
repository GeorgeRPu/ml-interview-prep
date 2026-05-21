# Gradient Boosting

## Explain gradient boosting

Gradient boosting is a machine learning technique that builds an ensemble of weak learners, typically decision trees, in a sequential manner. Each new weak learner is trained to correct the errors made by the previous trees by predicting the residuals (the difference between the actual and predicted values) of the previous models.

More formally, our goal is to minimize a loss function $L(y, F(x))$, where $y$ is the true label and $F(x)$ is the predicted value from our model.

$$
F = \argmin_F \mathbb{E}_{x, y} [L(y, F(x))] \approx \argmin_F \sum_{i=1}^N L(y_i, F(x_i))
$$

The ensemble is a weighted sum of weak learners $h_m(x)$ belonging to a class of possible models $\mathcal{H}$, learned iteratively in a greedy fashion.

$$
\begin{aligned}
F(x) &= \sum_{m=1}^M \gamma_m h_m(x) \\
F_m(x) &= F_{m-1}(x) + \argmin_\gamma \sum_{i=1}^N L(y_i, F_{m-1}(x_i) + \gamma h_m(x_i))
\end{aligned}
$$

The key insight is that we can think of $(F_i)$ as a trajectory through function space. Thus, each iteration of boosting can be understood as a gradient descent step in function space.

$$
\begin{aligned}
F_m(x) &= F_{m-1}(x) - \gamma_m \nabla_{F_{m-1}} \sum_{i=1}^N L(y_i, F_{m-1}(x_i)) \\
&= F_{m-1}(x) - \gamma_m \sum_{i=1}^N \underbrace{\frac{\partial L(y_i, F(x_i))}{\partial F(x_i)}}_{\text{pseudo-residual } r_{im}} \bigg|_{F = F_{m-1}} \\
\end{aligned}
$$

At each step $m$, we compute the negative gradient of the loss with respect to the current model's predictions called the pseudo-residuals $r_{im}$ and fit a new weak learner $h_m(x)$ to these pseudo-residuals. For example, with squared error loss $L(y, F(x)) = \frac{1}{2}(y - F(x))^2$, the pseudo-residuals are simply $r_{im} = y_i - F_{m-1}(x_i)$—the actual residuals. The step size $\gamma_m$ is determined by minimizing the loss function along the direction of the new weak learner.

$$
\gamma_m = \argmin_\gamma \sum_{i=1}^N L(y_i, F_{m-1}(x_i) - \gamma \nabla_{F_{m-1}} L(y_i, F_{m-1}(x_i)))
$$

Typically, we add a learning rate $0 < \eta \leq 1$ to control the contribution of each weak learner, which helps prevent overfitting and improves generalization. This is known as **shrinkage**.

$$
F_m(x) = F_{m-1}(x) + \eta \cdot \gamma_m h_m(x)
$$

```{prf:algorithm} Gradient Boosting
:label: gradient-boosting-algorithm

**Inputs** Training data $\{(x_i, y_i)\}_{i=1}^N$, differentiable loss function $L(y, F(x))$, number of iterations $M$, learning rate $\eta$

**Output** Ensemble model $F_M(x)$

1. Initialize: $F_0(x) = \argmin_\gamma \sum_{i=1}^N L(y_i, \gamma)$
2. For $m = 1$ to $M$:
    1. Compute pseudo-residuals: $r_{im} = -\frac{\partial L(y_i, F(x_i))}{\partial F(x_i)} \bigg|_{F = F_{m-1}}$
    2. Fit a weak learner $h_m(x)$ to $\{(x_i, r_{im})\}_{i=1}^N$
    3. Compute step size: $\gamma_m \gets \argmin_\gamma \sum_{i=1}^N L(y_i, F_{m-1}(x_i) + \gamma h_m(x_i))$
    4. Update ensemble: $F_m(x) \gets F_{m-1}(x) + \eta \cdot \gamma_m h_m(x)$
3. Return $F_M(x)$
```

## Explain Adaboost

Adaboost is a special instance of gradient boosting where the loss function is the exponential loss

$$
L(y, F(x)) = \exp(-y F(x))
$$

where $y \in \{-1, +1\}$ is the binary class label. The exponential loss heavily penalizes misclassified examples ($1/e$ for correctly classified examples vs. $e$ for misclassified examples).

Hence, the pseudo-residuals are given by

$$
\begin{aligned}
r_{im} &= -\frac{\partial L(y_i, F(x_i))}{\partial F(x_i)} \bigg|_{F = F_{m-1}} \
&= y_i \exp(-y_i F_{m-1}(x_i))
\end{aligned}
$$

Examples that are misclassified (where $y_i F_{m-1}(x_i) < 0$) will have larger pseudo-residuals and thus receive more focus in the next iteration.

The step size $\gamma_m$ can be computed in closed form for the exponential loss. We minimize the total loss over $\gamma$:

$$
\begin{aligned}
\gamma_m &= \argmin_\gamma \sum_{i=1}^N \exp(-y_i (F_{m-1}(x_i) + \gamma h_m(x_i))) \\
&= \argmin_\gamma \sum_{i=1}^N w_i^{(m)} \exp(-\gamma y_i h_m(x_i))
\end{aligned}
$$

where $w_i^{(m)} = \exp(-y_i F_{m-1}(x_i))$ is the loss associated with the datapoint $(x_i, y_i)$. Observe that $y_i h_m(x_i) = \pm 1$ based on whether the example is correctly or incorrectly classified. Split the sum into correctly and incorrectly classified examples:

$$
\begin{aligned}
&= \argmin_\gamma \left[ e^{-\gamma} \sum_{y_i = h_m(x_i)} w_i^{(m)} + e^{\gamma} \sum_{y_i \neq h_m(x_i)} w_i^{(m)} \right]
\end{aligned}
$$

Taking the derivative with respect to $\gamma$ and setting it to zero:

$$
-e^{-\gamma} \sum_{y_i = h_m(x_i)} w_i^{(m)} + e^{\gamma} \sum_{y_i \neq h_m(x_i)} w_i^{(m)} = 0
$$

Let $W_c = \sum_{y_i = h_m(x_i)} w_i^{(m)}$ and $W_e = \sum_{y_i \neq h_m(x_i)} w_i^{(m)}$ denote the total loss from correctly and incorrectly classified examples. Then:

$$
\begin{aligned}
e^{\gamma} W_e &= e^{-\gamma} W_c \\
e^{2\gamma} &= \frac{W_c}{W_e} \\
\gamma &= \frac{1}{2} \ln \frac{W_c}{W_e}
\end{aligned}
$$

Defining $\epsilon_m = \frac{W_e}{W_c + W_e}$, we have $\frac{W_c}{W_e} = \frac{1 - \epsilon_m}{\epsilon_m}$, giving:

$$
\gamma_m = \frac{1}{2} \ln \left( \frac{1 - \epsilon_m}{\epsilon_m} \right)
$$
