# Gradient Boosting

## Explain gradient boosting

Gradient boosting is a machine learning technique that builds an ensemble of weak learners, typically decision trees, in a sequential manner. Each new weak learner is trained to correct the errors made by the previous trees by predicting the residuals (the difference between the actual and predicted values) of the previous models.

More formally, our goal is to minimize a loss function $L\left(y, F\left(x\right)\right)$, where $y$ is the true label and $F\left(x\right)$ is the predicted value from our model.

$$
F = \argmin_F \mathbb{E}_{x, y} \left[L\left(y, F\left(x\right)\right)\right] \approx \argmin_F \sum_{i=1}^N L\left(y_i, F\left(x_i\right)\right)
$$

The ensemble is a weighted sum of weak learners $h_m\left(x\right)$ belonging to a class of possible models $\mathcal{H}$, learned iteratively in a greedy fashion.

$$
\begin{aligned}
F\left(x\right) &= \sum_{m=1}^M \gamma_m h_m\left(x\right) \\
F_m\left(x\right) &= F_{m-1}\left(x\right) + \argmin_\gamma \sum_{i=1}^N L\left(y_i, F_{m-1}\left(x_i\right) + \gamma h_m\left(x_i\right)\right)
\end{aligned}
$$

The key insight is that we can think of $\left(F_i\right)$ as a trajectory through function space. Thus, each iteration of boosting can be understood as a gradient descent step in function space.

$$
\begin{aligned}
F_m\left(x\right) &= F_{m-1}\left(x\right) - \gamma_m \nabla_{F_{m-1}} \sum_{i=1}^N L\left(y_i, F_{m-1}\left(x_i\right)\right) \\
&= F_{m-1}\left(x\right) - \gamma_m \sum_{i=1}^N \underbrace{\frac{\partial L\left(y_i, F\left(x_i\right)\right)}{\partial F\left(x_i\right)}}_{\text{pseudo-residual } r_{im}} \bigg|_{F = F_{m-1}} \\
\end{aligned}
$$

At each step $m$, we compute the negative gradient of the loss with respect to the current model's predictions called the pseudo-residuals $r_{im}$ and fit a new weak learner $h_m\left(x\right)$ to these pseudo-residuals. For example, with squared error loss $L\left(y, F\left(x\right)\right) = \frac{1}{2}\left(y - F\left(x\right)\right)^2$, the pseudo-residuals are simply $r_{im} = y_i - F_{m-1}\left(x_i\right)$—the actual residuals. The step size $\gamma_m$ is determined by minimizing the loss function along the direction of the new weak learner.

$$
\gamma_m = \argmin_\gamma \sum_{i=1}^N L\left(y_i, F_{m-1}\left(x_i\right) - \gamma \nabla_{F_{m-1}} L\left(y_i, F_{m-1}\left(x_i\right)\right)\right)
$$

Typically, we add a learning rate $0 < \eta \leq 1$ to control the contribution of each weak learner, which helps prevent overfitting and improves generalization. This is known as **shrinkage**.

$$
F_m\left(x\right) = F_{m-1}\left(x\right) + \eta \cdot \gamma_m h_m\left(x\right)
$$

```{prf:algorithm} Gradient Boosting
:label: gradient-boosting-algorithm

**Input:** Training data $\left\{\left(x_i, y_i\right)\right\}_{i=1}^N$, differentiable loss function $L\left(y, F\left(x\right)\right)$, number of iterations $M$, learning rate $\eta$

**Output:** Ensemble model $F_M\left(x\right)$

1. Initialize: $F_0\left(x\right) = \argmin_\gamma \sum_{i=1}^N L\left(y_i, \gamma\right)$
2. For $m = 1$ to $M$:
    1. Compute pseudo-residuals: $r_{im} = -\frac{\partial L\left(y_i, F\left(x_i\right)\right)}{\partial F\left(x_i\right)} \bigg|_{F = F_{m-1}}$
    2. Fit a weak learner $h_m\left(x\right)$ to $\left\{\left(x_i, r_{im}\right)\right\}_{i=1}^N$
    3. Compute step size: $\gamma_m \gets \argmin_\gamma \sum_{i=1}^N L\left(y_i, F_{m-1}\left(x_i\right) + \gamma h_m\left(x_i\right)\right)$
    4. Update ensemble: $F_m\left(x\right) \gets F_{m-1}\left(x\right) + \eta \cdot \gamma_m h_m\left(x\right)$
3. Return $F_M\left(x\right)$
```

## Explain Adaboost

Adaboost is a special instance of gradient boosting where the loss function is the exponential loss

$$
L\left(y, F\left(x\right)\right) = \exp\left(-y F\left(x\right)\right)
$$

where $y \in \{-1, +1\}$ is the binary class label. The exponential loss heavily penalizes misclassified examples ($1/e$ for correctly classified examples vs. $e$ for misclassified examples).

Hence, the pseudo-residuals are given by

$$
\begin{aligned}
r_{im} &= -\frac{\partial L\left(y_i, F\left(x_i\right)\right)}{\partial F\left(x_i\right)} \bigg|_{F = F_{m-1}} \
&= y_i \exp\left(-y_i F_{m-1}\left(x_i\right)\right)
\end{aligned}
$$

Examples that are misclassified (where $y_i F_{m-1}\left(x_i\right) < 0$) will have larger pseudo-residuals and thus receive more focus in the next iteration.

The step size $\gamma_m$ can be computed in closed form for the exponential loss. We minimize the total loss over $\gamma$:

$$
\begin{aligned}
\gamma_m &= \argmin_\gamma \sum_{i=1}^N \exp\left(-y_i \left(F_{m-1}\left(x_i\right) + \gamma h_m\left(x_i\right)\right)\right) \\
&= \argmin_\gamma \sum_{i=1}^N w_i^{(m)} \exp\left(-\gamma y_i h_m\left(x_i\right)\right)
\end{aligned}
$$

where $w_i^{(m)} = \exp\left(-y_i F_{m-1}\left(x_i\right)\right)$ is the loss associated with the datapoint $\left(x_i, y_i\right)$. Observe that $y_i h_m\left(x_i\right) = \pm 1$ based on whether the example is correctly or incorrectly classified. Split the sum into correctly and incorrectly classified examples:

$$
\begin{aligned}
&= \argmin_\gamma \left[ e^{-\gamma} \sum_{y_i = h_m\left(x_i\right)} w_i^{(m)} + e^{\gamma} \sum_{y_i \neq h_m\left(x_i\right)} w_i^{(m)} \right]
\end{aligned}
$$

Taking the derivative with respect to $\gamma$ and setting it to zero:

$$
-e^{-\gamma} \sum_{y_i = h_m\left(x_i\right)} w_i^{(m)} + e^{\gamma} \sum_{y_i \neq h_m\left(x_i\right)} w_i^{(m)} = 0
$$

Let $W_c = \sum_{y_i = h_m\left(x_i\right)} w_i^{(m)}$ and $W_e = \sum_{y_i \neq h_m\left(x_i\right)} w_i^{(m)}$ denote the total loss from correctly and incorrectly classified examples. Then:

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
