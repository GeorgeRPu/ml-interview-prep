# Regression Metrics

Let $\hat{y}$ be the predicted value and $y$ be the actual value.

## Mean squared error

````{prf:definition} Mean squared error
:label: mse

**Mean squared error (MSE)** is the average of the squared differences between the predictions and true values across the dataset.

$$
MSE = \frac{1}{n} \sum_{i=1}^{n} \left(\hat{y}_i - y_i\right)^2
$$
````

MSE is sensitive to outliers due to the quadratic scaling of residuals $\hat{y} - y$.

## Root mean squared error

````{prf:definition} Root mean squared error
:label: rmse

**Root mean squared error (RMSE)** is the square root of MSE.

$$
RMSE = \sqrt{MSE} = \sqrt{\frac{1}{n} \sum_{i=1}^{n} \left(\hat{y}_i - y_i\right)^2}
$$
````

## Mean absolute error

````{prf:definition} Mean absolute error
:label: mae

**Mean absolute error (MAE)** is the average of the absolute differences between the predictions and true values across the dataset.

$$
MAE = \frac{1}{n} \sum_{i=1}^{n} |\hat{y}_i - y_i|
$$
````

MAE is preferred over MSE when less sensitivity to outliers is desired and easier interpretation (being the average of the residuals) is needed.

![MSE vs MAE outlier sensitivity](/_static/figures/mse_vs_mae_outlier.png)
*A single outlier (a) pulls the fit line and inflates MSE far more than MAE because MSE squares the residual. As the outlier magnitude grows (b), MSE increases quadratically while MAE increases linearly.*

## Mean absolute percentage error

````{prf:definition} Mean absolute percentage error
:label: mape

**Mean absolute percentage error (MAPE)** is the average of the relative errors between the predictions and true values across the dataset.

$$
MAPE = \frac{1}{n} \sum_{i=1}^{n} \frac{|\hat{y}_i - y_i|}{|y_i|}
$$
````

Despite its name, MAPE is unbounded. MAPE penalizes overestimations more than underestimations. There is potentially infinite penalty for overestimation but only 100% penalty for underestimation. This can be good or bad depending on the application.

One variant of MAPE is to weight the error by the true value, as mispredictions on larger true values may be more consequential than mispredictions on smaller true values.

$$
\text{Weighted MAPE} = \frac{\sum_{i=1}^{n} |y_i| \cdot \frac{|\hat{y}_i - y_i|}{|y_i|}}{\sum_{i=1}^{n} |y_i|} = \frac{\sum_{i=1}^{n} |\hat{y}_i - y_i|}{\sum_{i=1}^{n} |y_i|}
$$

## Symmetric mean absolute percentage error

````{prf:definition} Symmetric mean absolute percentage error
:label: smape

**Symmetric mean absolute percentage error (SMAPE)** is the average of the relative errors between the predictions and true values, normalized by both the prediction and true value, across the dataset.

$$
SMAPE = \frac{100}{n} \sum_{i=1}^{n} \frac{|\hat{y}_i - y_i|}{|\hat{y}_i| + |y_i|}
$$
````

Unlike MAPE, SMAPE has a lower bound (0) and upper bound (100). Like MAPE, SMAPE penalizes overestimates more than underestimations.

## Coefficient of determination

````{prf:definition} Coefficient of determination
:label: r-squared

The **coefficient of determination ($R^2$)** measures the proportion of variance in the target explained by the model. Let $\bar{y} = \frac{1}{n}\sum_{i=1}^{n} y_i$ be the mean of the true values.

$$
R^2 = 1 - \frac{\sum_{i=1}^{n} \left(\hat{y}_i - y_i\right)^2}{\sum_{i=1}^{n} \left(\bar{y} - y_i\right)^2} = 1 - \frac{SS_{\text{res}}}{SS_{\text{tot}}}
$$
````

SS stands for "sum of squares".

$R^2 = 1$ means the model explains all variance; $R^2 = 0$ means it performs no better than predicting the mean. $R^2$ can be negative when the model is worse than predicting the mean.

A key limitation is that $R^2$ never decreases when adding features, even irrelevant ones, because additional parameters can only reduce $SS_{\text{res}}$.

![R-squared calculation](/_static/figures/r_squared.png)
*The model fit (b) reduces the total deviations from the mean (a). $R^2$ is the fraction of total variance ($SS_{\text{tot}}$) eliminated by the model, computed as $1 - SS_{\text{res}} / SS_{\text{tot}}$.*

## Adjusted $R^2$

````{prf:definition} Adjusted $R^2$
:label: adjusted-r-squared

**Adjusted $R^2$** penalizes $R^2$ for the number of features $p$ relative to the number of observations $n$.

$$
R^2_{\text{adj}} = 1 - \frac{\left(1 - R^2\right)\left(n - 1\right)}{n - p - 1}
$$
````

Unlike $R^2$, adjusted $R^2$ can decrease when adding features that do not improve the model enough to justify the additional parameter. This makes it useful for comparing models with different numbers of features.
