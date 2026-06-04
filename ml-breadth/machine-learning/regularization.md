# Regularization

## What is regularization?

**Regularization** is a technique that prevents overfitting by adding a penalty term to the loss function, discouraging the model from fitting the training data too closely.

$$
L(\theta) = L_{\text{data}}(\theta) + \lambda R(\theta)
$$

The hyperparameter **weight decay** $\lambda > 0$ controls the strength of the penalty and $R(\theta)$ is the regularization term.

## What is L1 regularization?

````{prf:definition} L1 Regularization
:label: l1-regularization
**L1 regularization**, sometimes called **Lasso** (Least Absolute Shrinkage and Selection Operator), adds a penalty proportional to the sum of absolute values of the coefficients.

$$
R_{\text{L1}}(\theta) = \|\theta\|_1 = \sum_{i=1}^{p} \left|\theta_i\right|
$$
````

## What is L2 regularization?

````{prf:definition} L2 Regularization
:label: l2-regularization
**L2 regularization** adds a penalty proportional to the sum of squared coefficients.

$$
R_{\text{L2}}(\theta) = \|\theta\|_2 = \sum_{i=1}^{p} \theta_i^2
$$
````

Linear regression with L2 regularization is sometimes called **ridge regression**.

## What is Elastic Net?

````{prf:definition} Elastic Net
:label: elastic-net
**Elastic net** combines L1 and L2 penalties with a mixing parameter $\alpha \in [0, 1]$:

$$
R_{\text{EN}}(\theta) = \alpha \|\theta\|_1 + (1 - \alpha) \|\theta\|_2 = \alpha \sum_{i=1}^{p} \left|\theta_i\right| + (1 - \alpha) \sum_{i=1}^{p} \theta_i^2
$$
````

When $\alpha = 1$, Elastic Net reduces to L1 (lasso). When $\alpha = 0$, it reduces to L2 (ridge).

## What is the difference between L1 and L2 regularization?

| Property | L1 (lasso) | L2 (ridge) |
|---|---|---|
| Penalty | $\sum \left\|\theta_i\right\|$ | $\sum \theta_i^2$ |
| Sparsity | Produces sparse weights | Shrinks toward zero, rarely exactly zero |
| Can be used for feature selection? | Yes | No |
| Correlated features | Picks one arbitrarily | Spreads weight among them |
| Solution uniqueness | May not be unique | Always unique |
| Computational | Requires iterative solvers (no closed form) | Closed-form solution exists |

**Feature selection.** Because L1 drives coefficients to exactly zero, it automatically selects a subset of features. The nonzero coefficients are the "selected" features. L2 shrinks all coefficients but keeps them nonzero, so it does not perform feature selection.

**Correlated features.** If two features $x_j$ and $x_k$ are highly correlated, L1 tends to assign all the weight to one and zero out the other. Which one it picks can be unstable across different samples. L2 distributes weight roughly evenly among correlated features, giving more stable estimates. This is one motivation for Elastic Net: its L1 component provides sparsity while its L2 component keeps correlated features together.

**Solution uniqueness.** The L2 penalty $\lambda \|\theta\|_2^2$ is strictly convex (its Hessian $2\lambda I$ is positive definite), so adding it to a convex data loss makes the total objective strictly convex, which guarantees a unique minimum. The L1 penalty $\lambda \|\theta\|_1$ is convex but not strictly convex (each $\left|\theta_i\right|$ is linear on either side of zero), so the objective can have flat regions where many parameter vectors achieve the same minimum loss. The classic case is two identical features $x_j = x_k$. Any split of their combined weight, e.g. $(c, 0)$, $(0, c)$, or $(c/2, c/2)$, gives the same fit and the same L1 penalty, so the minimizer is a whole segment rather than a point.

## Why does L1 regularization induce sparsity?

We can understand L1 regularization through 2 perspectives: the geometric view and the (sub) gradient view.

1. **Geometric view.** The regularized objective can be interpreted as minimizing the data loss $L_{\text{data}}(\theta)$ subject to a constraint on the regularization term $R(\theta) \le b$ for some budget $b$. For a given data loss contour, the optimal solution is where the contour first touches the constraint boundary. The L1 has diamond shaped contours with corners on the axes. The data loss contours are most likely to first touch the constraint boundary at a corner where one or more coefficients are exactly zero. The L2 has circlular contours, so the tangent point typically has all coefficients nonzero.

![L1 vs L2 constraint regions](/_static/figures/l1_vs_l2_constraint.png)
*The L1 diamond has corners on the axes, so the loss contours are most likely to first touch the constraint boundary at a corner where one or more coefficients are exactly zero. The L2 circle has no such corners, so the tangent point typically has all coefficients nonzero.*

2. **Subgradient view.** The subgradient of the L1 penalty $\left|\theta_i\right|$ is $\pm 1$. For L2, the gradient of $\theta_i^2$ is $2\theta_i$, which vanishes at zero. Thus as $\theta_i$ approaches zero, the L2 penalty provides less and less force to push it to zero, while the L1 penalty continues to provide a constant force of magnitude 1.
