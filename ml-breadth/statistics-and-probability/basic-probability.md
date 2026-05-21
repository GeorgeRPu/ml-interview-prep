# Basic Probability

## What is conditional probability?

````{prf:definition} Conditional Probability
The conditional probability $\Pr\left(A \mid B\right)$ is the probability of event $A$ given that event $B$ has occurred.

$$
\Pr\left(A \mid B\right) = \frac{\Pr\left(A \cap B\right)}{\Pr\left(B\right)}
$$
````

## When are two events independent?

Two events $A$ and $B$ are **independent** if the occurrence of one does not affect the probability of the other.

````{prf:definition} Independence
Events $A$ and $B$ are independent if

$$
\Pr\left(A \cap B\right) = \Pr\left(A\right) \Pr\left(B\right).
$$

or equivalently,

$$
\Pr\left(A \mid B\right) = \Pr\left(A\right) \quad \text{and} \quad \Pr\left(B \mid A\right) = \Pr\left(B\right).
$$
````

## What is the chain rule of probability?

````{prf:definition} Chain Rule of Probability
For events $A$ and $B$,

$$
\Pr\left(A \cap B\right) = \Pr\left(A \mid B\right) \Pr\left(B\right) = \Pr\left(B \mid A\right) \Pr\left(A\right).
$$

More generally, for events $A_1, A_2, \dots, A_n$,

$$
\Pr\left(A_1 \cap \dots \cap A_n\right) = \Pr\left(A_1\right) \Pr\left(A_2 \mid A_1\right) \Pr\left(A_3 \mid A_1 \cap A_2\right) \cdots \Pr\left(A_n \mid A_1 \cap \dots \cap A_{n-1}\right).
$$
````

## What is the law of total probability?

````{prf:definition} Law of Total Probability
If $B_1, B_2, \dots, B_n$ is a partition of the sample space, then

$$
\Pr\left(A\right) = \sum_{i=1}^{n} \Pr\left(A \mid B_i\right) \Pr\left(B_i\right).
$$
````
