"""Classification metric figures: PR curve with AP, ROC curve with AUC."""

import matplotlib.pyplot as plt
from sklearn.datasets import make_classification
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import (
    average_precision_score,
    precision_recall_curve,
    roc_auc_score,
    roc_curve,
)
from sklearn.model_selection import train_test_split

from . import save


def _fit_and_score():
    X, y = make_classification(
        n_samples=3000, n_features=20, n_informative=3,
        n_redundant=2, n_clusters_per_class=2,
        weights=[0.85, 0.15], flip_y=0.05, random_state=7,
    )
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.4, random_state=7,
    )
    model = LogisticRegression(random_state=7, max_iter=200)
    model.fit(X_train, y_train)
    scores = model.predict_proba(X_test)[:, 1]
    return y_test, scores


def generate_precision_recall_ap():
    y_test, scores = _fit_and_score()

    precision, recall, _ = precision_recall_curve(y_test, scores)
    ap = average_precision_score(y_test, scores)

    fig, ax = plt.subplots(figsize=(7, 5))

    ax.step(recall, precision, where="post", color="steelblue", linewidth=2,
            label=f"PR curve (AP = {ap:.2f})")
    ax.fill_between(recall, precision, step="post", alpha=0.25, color="steelblue",
                    label="Average precision area")

    ax.set_xlabel("Recall", fontsize=12)
    ax.set_ylabel("Precision", fontsize=12)
    ax.set_xlim([0.0, 1.0])
    ax.set_ylim([0.0, 1.05])
    ax.legend(loc="lower left", fontsize=10, framealpha=0.9)
    ax.grid(True, alpha=0.3)

    plt.tight_layout()
    save(fig, "precision_recall_ap")


def generate_roc_auc():
    y_test, scores = _fit_and_score()

    fpr, tpr, _ = roc_curve(y_test, scores)
    auc = roc_auc_score(y_test, scores)

    fig, ax = plt.subplots(figsize=(7, 5))

    ax.plot(fpr, tpr, color="steelblue", linewidth=2,
            label=f"ROC curve (AUC = {auc:.2f})")
    ax.fill_between(fpr, tpr, alpha=0.25, color="steelblue",
                    label="AUC area")
    ax.plot([0, 1], [0, 1], color="grey", linestyle="--", linewidth=1,
            label="Random classifier")

    ax.set_xlabel("False Positive Rate", fontsize=12)
    ax.set_ylabel("True Positive Rate", fontsize=12)
    ax.set_xlim([0.0, 1.0])
    ax.set_ylim([0.0, 1.05])
    ax.legend(loc="lower right", fontsize=10, framealpha=0.9)
    ax.grid(True, alpha=0.3)

    plt.tight_layout()
    save(fig, "roc_auc")


def generate_all():
    generate_precision_recall_ap()
    generate_roc_auc()
