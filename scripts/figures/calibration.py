"""Calibration figures: Platt scaling vs. isotonic regression."""

import numpy as np
import matplotlib.pyplot as plt
from sklearn.calibration import calibration_curve
from sklearn.datasets import make_classification
from sklearn.ensemble import RandomForestClassifier
from sklearn.isotonic import IsotonicRegression
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split

from . import save


def _fit_uncalibrated_classifier():
    X, y = make_classification(
        n_samples=20000, n_features=20, n_informative=4,
        n_redundant=2, n_clusters_per_class=2,
        weights=[0.5, 0.5], flip_y=0.05, random_state=11,
    )
    X_train, X_rest, y_train, y_rest = train_test_split(
        X, y, test_size=0.6, random_state=11,
    )
    X_calib, X_test, y_calib, y_test = train_test_split(
        X_rest, y_rest, test_size=0.5, random_state=11,
    )
    base = RandomForestClassifier(
        n_estimators=50, max_depth=6, random_state=11,
    )
    base.fit(X_train, y_train)
    return base, X_calib, y_calib, X_test, y_test


def generate_calibration_comparison():
    base, X_calib, y_calib, X_test, y_test = _fit_uncalibrated_classifier()

    scores_calib = base.predict_proba(X_calib)[:, 1]
    scores_test = base.predict_proba(X_test)[:, 1]

    platt = LogisticRegression()
    platt.fit(scores_calib.reshape(-1, 1), y_calib)
    platt_test = platt.predict_proba(scores_test.reshape(-1, 1))[:, 1]

    isotonic = IsotonicRegression(out_of_bounds="clip")
    isotonic.fit(scores_calib, y_calib)
    isotonic_test = isotonic.predict(scores_test)

    grid = np.linspace(0.0, 1.0, 500)
    platt_mapping = platt.predict_proba(grid.reshape(-1, 1))[:, 1]
    isotonic_mapping = isotonic.predict(grid)

    fig, (ax_map, ax_rel) = plt.subplots(1, 2, figsize=(13, 5))

    ax_map.plot([0, 1], [0, 1], color="grey", linestyle="--", linewidth=1,
                label="Identity (no rescaling)")
    ax_map.plot(grid, platt_mapping, color="steelblue", linewidth=2,
                label="Platt scaling (sigmoid)")
    ax_map.plot(grid, isotonic_mapping, color="darkorange", linewidth=2,
                label="Isotonic regression (step)")
    ax_map.set_title("Learned Calibration Map", fontsize=14)
    ax_map.set_xlabel("Raw classifier score", fontsize=12)
    ax_map.set_ylabel("Calibrated probability", fontsize=12)
    ax_map.set_xlim([0.0, 1.0])
    ax_map.set_ylim([0.0, 1.0])
    ax_map.legend(loc="upper left", fontsize=10, framealpha=0.9)
    ax_map.grid(True, alpha=0.3)
    ax_map.text(0.5, -0.22,
                "(a) Learned mapping from raw score to calibrated probability.",
                transform=ax_map.transAxes, ha="center", va="top", fontsize=11)

    n_bins = 10
    frac_uncal, mean_uncal = calibration_curve(
        y_test, scores_test, n_bins=n_bins, strategy="quantile",
    )
    frac_platt, mean_platt = calibration_curve(
        y_test, platt_test, n_bins=n_bins, strategy="quantile",
    )
    frac_iso, mean_iso = calibration_curve(
        y_test, isotonic_test, n_bins=n_bins, strategy="quantile",
    )

    ax_rel.plot([0, 1], [0, 1], color="grey", linestyle="--", linewidth=1,
                label="Perfectly calibrated")
    ax_rel.plot(mean_uncal, frac_uncal, marker="o", color="firebrick",
                linewidth=2, label="Uncalibrated")
    ax_rel.plot(mean_platt, frac_platt, marker="s", color="steelblue",
                linewidth=2, label="Platt scaling")
    ax_rel.plot(mean_iso, frac_iso, marker="^", color="darkorange",
                linewidth=2, label="Isotonic regression")
    ax_rel.set_title("Reliability Diagram", fontsize=14)
    ax_rel.set_xlabel("Mean predicted probability", fontsize=12)
    ax_rel.set_ylabel("Fraction of positives", fontsize=12)
    ax_rel.set_xlim([0.0, 1.0])
    ax_rel.set_ylim([0.0, 1.0])
    ax_rel.legend(loc="upper left", fontsize=10, framealpha=0.9)
    ax_rel.grid(True, alpha=0.3)
    ax_rel.text(0.5, -0.22,
                "(b) Reliability diagram before and after each calibrator.",
                transform=ax_rel.transAxes, ha="center", va="top", fontsize=11)

    plt.tight_layout()
    save(fig, "calibration_platt_vs_isotonic")


def generate_all():
    generate_calibration_comparison()
