# Calibration

## What is calibration?

**Calibration** is the process of ensuring that the predicted probabilities of a classifier match the observed frequencies of the outcomes. For example, if a classifier predicts a probability of 0.8 for a certain class, then we would expect that class to be correct approximately 80% of the time when that probability is predicted.

## How do we measure calibration?

**Calibration curves** or **reliability diagrams** compare the predicted probabilities with the observed frequencies of the outcomes. For each bin of predicted probabilities, we plot the average predicted probability against the average observed frequency. A perfectly calibrated model would have a reliability diagram that is a diagonal line from (0, 0) to (1, 1).

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_compare_calibration_001.png)

**Expected calibration error (ECE)** is the weighted average of the absolute differences between the predicted probabilities $p_i$ and the observed frequencies $o_i$ across all bins $B_1, \dots, B_n$.

$$
ECE = \sum_{i=1}^{n} \frac{|B_i|}{N} |p_i - o_i|
$$

## How do we calibrate a model?

Calibrating a model involves fitting a regressor that maps the raw model scores to calibrated probabilities. There are 3 common methods for calibrating a model:

1. **Platt scaling** or **sigmoid**. Fits a logistic regression model to the raw scores of the classifier. This method is simple and works well when the raw scores are already close to probabilities.
2. **Isotonic regression**. Fits a non-parametric isotonic regression model to the raw scores of the classifier. The isotonic regressor is more flexible than the sigmoid model, able to capture more complex relationships between the raw scores and the probabilities but may overfit if the dataset is small.
3. **Temperature scaling**. For a multi-class classifier, we can convert the raw scores to probabilities using a softmax function. To calibrate the probabilities we introduce a temperature parameter $T$ that scales the logits before applying the softmax.

![Left: learned mapping from raw scores to calibrated probabilities — Platt scaling fits a smooth sigmoid while isotonic regression fits a piecewise-constant step function. Right: reliability diagrams on a random forest showing how both methods correct the uncalibrated S-shape, with isotonic following the bin frequencies more closely at the cost of overfitting risk.](/_static/figures/calibration_platt_vs_isotonic.png)

$$
p_i = \frac{\exp\left(z_i / T\right)}{\sum_{j} \exp\left(z_j / T\right)}
$$

The temperature parameter is learned by minimizing the negative log-likelihood of the calibration set.

$$
T^* = \arg\min_{T} -\sum_{i=1}^{N} \log p_{y_i}
$$
