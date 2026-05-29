# Overfitting and Underfitting

## What is overfitting?

Overfitting occurs when a model learns not just the general patterns in the training data but also its noise and outliers. This leads to the model performing poorly on new, unseen data.

## What is underfitting?

Underfitting occurs when a model fails to capture the underlying patterns in the training data, resulting in poor performance on both the training data and new, unseen data.

## Relationship to the bias-variance tradeoff

Overfitting is associated with high variance models, while underfitting is associated with high bias models.

## How do we detect overfitting and underfitting?

- Underfitting: Both train and test errors are high.
- Overfitting: Train error is low, but test error is high.

## How do we prevent overfitting and underfitting?

Underfitting:
- **Using a higher variance/more complex model**.
  - **Increasing model complexity**. For example, using more layers in a neural network or leaves for a decision tree.
  - **Training longer**.
- **Feature engineering**. Create new features that capture the underlying patterns in the data.

Overfitting:
- **More training data**. Providing more examples makes it harder for the model to memorize noise.
  - **Data augmentation**. A way to artificially increase the size of the training dataset by applying transformations to existing data points (e.g. rotating or flipping images).
- **Using a lower variance/simpler model**.
  - **Reducing model complexity**.
- **Early stopping**. Stop training when the validation error starts to increase.
- **Regularization**. Add a penalty term to the loss function to discourage complex models.
