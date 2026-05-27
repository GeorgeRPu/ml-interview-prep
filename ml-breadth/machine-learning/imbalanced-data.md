# Imbalanced Data

## Why is imbalanced data a problem?

Imbalanced data can lead models to be biased towards the majority class, resulting in poor performance on the minority class.

For example, suppose we are trying to build a model to detect fraudulent transactions. Only a small percentage, say 1% of transactions are fraudulent. Naively training a model on this data might lead to a model that always predicts "not fraudulent", achieving 99% accuracy but never catching a single instance of fraud.

## What strategies can we use to address imbalanced data?

There are 2 common strategies to address imbalanced data:

1. Resampling. We can oversampling the minority class by duplicating examples or generating synthetics examples via a technique like SMOTE. We can also undersample the majority class by randomly removing data points. Random oversampling is a good baseline since it doesn't throw away any data and is computationally inexpensive.
2. Modifying the loss function. One example is focal loss, which modifies cross-entropy loss to better deal with class imbalance by adding a modulating factor $\left(1 - p_t\right)^\gamma$.

$$
\begin{aligned}
L_{\text{cross-entropy}}\left(p\right) &= -\log\left(p_t\right)
L_{\text{focal}}\left(p\right) &= -\left(1 - p_t\right)^\gamma \log\left(p_t\right) \\
\end{aligned}
$$

  Here, $p$ is the predicted probability distribution and $t$ is the target class.

  Intuitively, the modulating factor reduces the loss contribution from easy examples and extends the range in which an example receives low loss. For instance, with $\gamma = 2$, an example classified with $p_t = 0.9$ would have 100x lower loss compared with cross-entropy, and with $p_t \approx 0.968$ it would have 1000x lower loss. This in turn increases the importance of correcting misclassified examples.
