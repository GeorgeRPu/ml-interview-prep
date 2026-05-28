# Classification Metrics

## Confusion matrix

````{prf:definition} Confusion matrix
:label: confusion-matrix

Let $\hat{y}$ be the predicted value and $y$ be the actual value. The **confusion matrix** is a table that counts the number of instances for each combination of $\hat{y}$ and $y$. The rows are the predicted value and the columns are the actual value.

$$
C_{ij} = \#\left[\hat{y} = i \land y = j\right]
$$
````

For binary classification, the confusion matrix is 2x2. Let $y, \hat{y} \in \{0, 1\}$ and $\#\left[\cdot\right]$ be the count of instances that satisfy the condition. Then the confusion matrix is

$$
C =
\begin{bmatrix}
\#\left[\hat{y} = 0 \land y = 0\right] & \#\left[\hat{y} = 0 \land y = 1\right] \\
\#\left[\hat{y} = 1 \land y = 0\right] & \#\left[\hat{y} = 1 \land y = 1\right]
\end{bmatrix}
=
\begin{bmatrix}
TN & FN \\
FP & TP
\end{bmatrix}
$$
````

where $TP$ is the number of true positives, $TN$ is the number of true negatives, $FP$ is the number of false positives, and $FN$ is the number of false negatives.

## Accuracy

````{prf:definition} Accuracy
:label: accuracy

**Accuracy** is the number of correct predictions divided by the number of total predictions $N$.

$$
A = \frac{\#\left[\hat{y} = y\right]}{N}
$$
````

Accuracy works well for balanced datasets but not imbalanced datasets as accuracy can be high even when a model performs poorly on the minority class.

## Precision

````{prf:definition} Precision
:label: precision

**Precision** is the number of correct predictions divided by the number of predictions for that class.

$$
P\left(c\right) = \frac{\#\left[\hat{y} = y\right]}{\#\left[\hat{y} = c\right]} = \frac{TP}{TP + FP}
$$
````

Precision (and recall) work even for imbalanced datasets.

## Recall

````{prf:definition} Recall
:label: recall

**Recall** is the number of correct predictions divided by the number of actual instances of that class.

$$
R\left(c\right) = \frac{\#\left[\hat{y} = y\right]}{\#\left[y = c\right]} = \frac{TP}{TP + FN}
$$
````

Recall is the dual of precision. While precision measures how good a model is when it makes a certain prediction, recall measures how much a model can recognize a certain class.

To have high precision, a model should only predict class $c$ when it is highly confident to avoid FPs. To have high recall, a model should not hesitate to predict class $c$ even when it has low confidence to avoid FNs.

## F-score

````{prf:definition} F-score
:label: f-score

The **F1-score** blends precision and recall by taking the harmonic mean.

$$
F_1 &= 2 \frac{PR}{P + R}
$$

More generally, the **F-beta score** is a weighted harmonic mean of precision and recall.

$$
F_\beta &= \left(1 + \beta^2\right) \frac{PR}{\beta^2 P + R}
$$
````

## Precision-recall curve

For many classifiers, they predict a score which tracks the probability of a class. Thus, precision and recall measure the performance of a classifier at a specific threshold. The precision-recall curve shows the performance of a classifier at different thresholds.

````{prf:definition} Precision-recall curve
:label: precision-recall-curve

The **precision-recall curve** plots the precision and recall of a scoring classifier at different decision thresholds. Given thresholds $t_1 < t_2 < \cdots < t_n$, the precision-recall curve plots the points $\left\{\left(R_i_, P_i_\right) : i = 1, 2, \ldots, n\right\}$.
````

The plot looks like a curve starting at $\left(0, 1\right)$ going to $\left(1, 0\right)$. The better the classifier, the more the plot looks like a right angle hinging at $\left(1, 1\right)$.

## Average precision

````{prf:definition} Average precision
:label: average-precision

**Average precision** weights the precision at different thresholds $t_1, t_2, \ldots, t_n$ by the change in recall.

$$
AP = \sum_{i=2}^{n} \left(R_i - R_{i-1}\right) P_i
$$

AP can be interpreted as the area under the precision-recall curve.
````

AP is a number from 0 to 1, with 1 being the AP of a perfect classifier.

![Precision-recall curve with average precision shading](/_static/figures/precision_recall_ap.png)
*Precision-recall curve for a logistic regression classifier on an imbalanced binary dataset. The shaded area represents the average precision (AP = 0.71), which summarizes the trade-off between precision and recall across all thresholds.*

## Receiver operating characteristic

````{prf:definition} ROC curve
:label: roc-curve

The **ROC curve** plots the true positive rate on the y-axis against the false positive rate on the x-axis of a classifier for different thresholds. Given thresholds $t_1 < t_2 < \cdots < t_n$, the ROC curve plots the points $\left\{\left(FPR_i, TPR_i\right) : i = 1, 2, \ldots, n\right\}$.
````

The ROC starts at $\left(0, 0\right)$ and goes to $\left(1, 1\right)$. A random classifier is a straight line from $\left(0, 0\right)$ to $\left(1, 1\right)$. A perfect classifier is a right angle hinging at $\left(0, 1\right)$.

````{prf:definition} ROC AUC
:label: roc-auc

**ROC area under curve (AUC)** is the area under the ROC curve, ranging from 0 to 1.
````

Unlike average precision, ROC AUC can be compared across datasets. A random classifier has ROC AUC of 0.5. Generally, ROC AUC above 0.85 is considered good.

![ROC curve with AUC shading](/_static/figures/roc_auc.png)
*ROC curve for the same classifier. The shaded area represents the AUC (0.88). The dashed diagonal is the ROC of a random classifier (AUC = 0.5).*

## How do you choose a classification threshold?

The choice of classification threshold depends on the specific application and desired trade-off between precision and recall. For example, in a medical diagnosis setting, we may want to prioritize recall to ensure that we do not miss any positive cases, even if it means having more false positives. In contrast, in a spam detection setting, we may want to prioritize precision to avoid flagging legitimate emails as spam, even if it means missing some spam emails.
