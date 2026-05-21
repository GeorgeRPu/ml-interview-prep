# Basic Probability

## What is conditional probability?

````{prf:definition} Conditional Probability
The conditional probability $\Pr(A \mid B)$ is the probability of event $A$ given that event $B$ has occurred.

$$
\Pr(A \mid B) = \frac{\Pr(A \cap B)}{\Pr(B)}
$$
````

## When are two events independent?

Two events $A$ and $B$ are **independent** if the occurrence of one does not affect the probability of the other.

````{prf:definition} Independence
Events $A$ and $B$ are independent if

$$
\Pr(A \cap B) = \Pr(A) \Pr(B).
$$

or equivalently,

$$
\Pr(A \mid B) = \Pr(A) \quad \text{and} \quad \Pr(B \mid A) = \Pr(B).
$$
````

## What is the chain rule of probability?

````{prf:definition} Chain Rule of Probability
For events $A$ and $B$,

$$
\Pr(A \cap B) = \Pr(A \mid B) \Pr(B) = \Pr(B \mid A) \Pr(A).
$$

More generally, for events $A_1, A_2, \dots, A_n$,

$$
\Pr(A_1 \cap \dots \cap A_n) = \Pr(A_1) \Pr(A_2 \mid A_1) \Pr(A_3 \mid A_1 \cap A_2) \cdots \Pr(A_n \mid A_1 \cap \dots \cap A_{n-1}).
$$
````

## What is the law of total probability?

````{prf:definition} Law of Total Probability
If $B_1, B_2, \dots, B_n$ is a partition of the sample space, then

$$
\Pr(A) = \sum_{i=1}^{n} \Pr(A \mid B_i) \Pr(B_i).
$$
````
