# Data Splitting

## Why do we need to split data into training and test sets?

Models perform better when evaluated on data they have seen during training. However, in real-world applications, our models will need to generalize to unseen data. To get an unbiased estimate of our model's performance, we need to evaluate it on data that was not used during training.

## Why do we need a separate validation set?

Because models have hyperparameters that can be tuned to improve performance, we need a separate validation set to evaluate different hyperparameter configurations. If we were to use the test set for hyperparameter tuning, we would risk overfitting to the test set and getting an overly optimistic estimate of our model's performance.

## What is cross-validation?

Cross-validation divides the data into $k$ subsets or **folds**. The model is trained on $k-1$ folds and evaluated on the remaining fold. This process is repeated $k$ times, with each fold serving as the test set once. The performance metrics are then averaged across all $k$ iterations to get a more robust estimate of the model's performance.

````{prf:algorithm} $k$-fold cross-validation
:label: alg-kfold-cv

**Input:** Dataset $\mathcal{D}$ with $N$ samples, number of folds $k$, learning algorithm $\mathcal{A}$, evaluation metric $M$

**Output:** Cross-validated performance estimate $\hat{m}$

1. Randomly partition $\mathcal{D}$ into $k$ disjoint subsets $\mathcal{D}_1, \mathcal{D}_2, \ldots, \mathcal{D}_k$ of approximately equal size.
2. For $i = 1, 2, \ldots, k$:
  1. Set $\mathcal{D}_{\text{val}} = \mathcal{D}_i$.
  2. Set $\mathcal{D}_{\text{train}} = \mathcal{D} \setminus \mathcal{D}_i$.
  3. Train the model $\hat{f}_i = \mathcal{A}\left(\mathcal{D}_{\text{train}}\right)$.
  4. Compute $m_i = M\left(\hat{f}_i, \mathcal{D}_{\text{val}}\right)$.
3. Return $\hat{m} = \frac{1}{k} \sum_{i=1}^{k} m_i$.
````

![5-fold cross-validation](https://scikit-learn.org/stable/_images/grid_search_cross_validation.png)
*Each row represents one iteration of 5-fold cross-validation. The validation fold (dark blue) rotates through all five positions while the remaining folds (light blue) form the training set.*

## What are the advantages and disadvantages of k-fold cross-validation compared to a single train/validation/test split?

Cross-validation provides a more robust estimate of model performance as it averages results across multiple train/test splits. However, it is $k$ times more computationally expensive than a single train/validation/test split, as the model needs to be trained and evaluated $k$ times.

## What is an out of time test set?

An out of time test set contains data collected after the training data.

## Why is out of time testing important?

Out of time testing is important because it simulates the real-world scenario where a model is trained on past data and needs to make predictions on future data.

Generally, models perform worse on out of time test sets compared to random splits because the data distribution may have changed over time (a phenomenon known as **concept drift**). This can lead to drops in model performance in production compared to what was observed during model development.
