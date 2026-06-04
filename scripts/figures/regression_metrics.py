"""Regression metric figures: MSE vs MAE outlier sensitivity, R² calculation."""

import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

from . import save


def generate_mse_vs_mae():
    rng = np.random.RandomState(42)
    n = 25
    x = np.linspace(0, 10, n)
    y_true = 2 * x + 1 + rng.normal(0, 1.5, n)

    outlier_idx = 20
    y_true[outlier_idx] += 12

    model = LinearRegression()
    model.fit(x.reshape(-1, 1), y_true)
    y_pred = model.predict(x.reshape(-1, 1))

    fig, (ax_scatter, ax_sweep) = plt.subplots(1, 2, figsize=(13, 5))

    ax_scatter.scatter(x, y_true, color="tab:blue", s=40, zorder=3)
    ax_scatter.plot(x, y_pred, color="tab:gray", linewidth=2, label="Fit")
    for i in range(n):
        color = "tab:red" if i == outlier_idx else "tab:blue"
        alpha = 0.8 if i == outlier_idx else 0.3
        lw = 2 if i == outlier_idx else 1
        ax_scatter.plot([x[i], x[i]], [y_true[i], y_pred[i]],
                        color=color, alpha=alpha, linewidth=lw)
    residuals = y_true - y_pred
    mse = np.mean(residuals ** 2)
    mae = np.mean(np.abs(residuals))
    ax_scatter.annotate(f"MSE = {mse:.1f}\nMAE = {mae:.1f}",
                        xy=(0.03, 0.95), xycoords="axes fraction",
                        fontsize=11, verticalalignment="top",
                        bbox=dict(boxstyle="round,pad=0.3", facecolor="white",
                                  edgecolor="tab:gray", alpha=0.9))
    ax_scatter.set_title("Residuals with one outlier (red)")
    ax_scatter.set_xlabel("$x$", fontsize=12)
    ax_scatter.set_ylabel("$y$", fontsize=12)
    ax_scatter.grid(True, alpha=0.3)

    base_residuals = rng.normal(0, 1.5, 20)
    outlier_magnitudes = np.linspace(0, 20, 200)
    mse_values = []
    mae_values = []
    for mag in outlier_magnitudes:
        residuals = np.append(base_residuals, mag)
        mse_values.append(np.mean(residuals ** 2))
        mae_values.append(np.mean(np.abs(residuals)))

    ax_sweep.plot(outlier_magnitudes, mse_values, color="tab:blue", linewidth=2,
                  label="MSE (quadratic)")
    ax_sweep.plot(outlier_magnitudes, mae_values, color="tab:orange", linewidth=2,
                  label="MAE (linear)")
    ax_sweep.set_title("MSE grows quadratically; MAE grows linearly")
    ax_sweep.set_xlabel("Outlier magnitude", fontsize=12)
    ax_sweep.set_ylabel("Metric value", fontsize=12)
    ax_sweep.legend(loc="upper left", fontsize=10, framealpha=0.9)
    ax_sweep.grid(True, alpha=0.3)

    plt.tight_layout()
    save(fig, "mse_vs_mae_outlier")


def generate_r_squared():
    rng = np.random.RandomState(17)
    n = 30
    x = np.linspace(0, 10, n)
    y_true = 1.8 * x + 3 + rng.normal(0, 3.0, n)

    model = LinearRegression()
    model.fit(x.reshape(-1, 1), y_true)
    y_pred = model.predict(x.reshape(-1, 1))

    y_bar = np.mean(y_true)
    ss_res = np.sum((y_true - y_pred) ** 2)
    ss_tot = np.sum((y_true - y_bar) ** 2)
    r2 = 1 - ss_res / ss_tot

    fig, (ax_tot, ax_res) = plt.subplots(1, 2, figsize=(13, 5))

    ylim = (min(y_true) - 2, max(y_true) + 2)

    for i in range(n):
        ax_tot.plot([x[i], x[i]], [y_bar, y_true[i]],
                    color="tab:blue", linewidth=1.5, alpha=0.5)
    ax_tot.scatter(x, y_true, color="tab:blue", s=40, zorder=3)
    ax_tot.axhline(y_bar, color="tab:gray", linestyle="--", linewidth=1.5,
                   label=f"Mean ($\\bar{{y}}$ = {y_bar:.1f})")
    ax_tot.annotate(f"$SS_{{\\mathrm{{tot}}}}$ = {ss_tot:.0f}",
                    xy=(0.03, 0.95), xycoords="axes fraction",
                    fontsize=12, verticalalignment="top",
                    bbox=dict(boxstyle="round,pad=0.3", facecolor="white",
                              edgecolor="tab:gray", alpha=0.9))
    ax_tot.set_title("Total variance: deviations from the mean")
    ax_tot.set_xlabel("$x$", fontsize=12)
    ax_tot.set_ylabel("$y$", fontsize=12)
    ax_tot.set_ylim(ylim)
    ax_tot.legend(loc="lower right", fontsize=10, framealpha=0.9)
    ax_tot.grid(True, alpha=0.3)

    for i in range(n):
        ax_res.plot([x[i], x[i]], [y_pred[i], y_true[i]],
                    color="tab:blue", linewidth=1.5, alpha=0.5)
    ax_res.scatter(x, y_true, color="tab:blue", s=40, zorder=3)
    ax_res.plot(x, y_pred, color="tab:orange", linewidth=2, label="Fit")
    ax_res.annotate(
        f"$SS_{{\\mathrm{{res}}}}$ = {ss_res:.0f}\n"
        f"$R^2 = 1 - \\frac{{{ss_res:.0f}}}{{{ss_tot:.0f}}} = {r2:.2f}$",
        xy=(0.03, 0.95), xycoords="axes fraction",
        fontsize=12, verticalalignment="top",
        bbox=dict(boxstyle="round,pad=0.5", facecolor="white",
                  edgecolor="tab:gray", alpha=0.9))
    ax_res.set_title("Residual variance: deviations from the fit")
    ax_res.set_xlabel("$x$", fontsize=12)
    ax_res.set_ylabel("$y$", fontsize=12)
    ax_res.set_ylim(ylim)
    ax_res.legend(loc="lower right", fontsize=10, framealpha=0.9)
    ax_res.grid(True, alpha=0.3)

    plt.tight_layout()
    save(fig, "r_squared")


def generate_all():
    generate_mse_vs_mae()
    generate_r_squared()
