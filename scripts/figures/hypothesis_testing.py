"""Statistical power diagram for hypothesis testing."""

import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import norm, t

from . import save


def generate_power():
    mu_0 = 0
    delta = 2.5
    sigma = 1
    alpha = 0.05
    z_crit = norm.ppf(1 - alpha / 2)

    x = np.linspace(-4, delta + 4, 1000)
    y_null = norm.pdf(x, mu_0, sigma)
    y_alt = norm.pdf(x, delta, sigma)

    fig, ax = plt.subplots(figsize=(10, 4.5))

    ax.plot(x, y_null, color="steelblue", linewidth=2, label=r"$H_0$: $Z \sim \mathcal{N}(0, 1)$")
    ax.plot(x, y_alt, color="darkorange", linewidth=2,
            label=rf"$H_1$: $Z \sim \mathcal{{N}}({delta}, 1)$")

    # Rejection region (right tail) — shade under H1 to show power
    x_reject = np.linspace(z_crit, x[-1], 500)
    ax.fill_between(x_reject, norm.pdf(x_reject, delta, sigma),
                    alpha=0.4, color="darkorange", label="Power ($1 - \\beta$)")

    # Beta region — area under H1 that falls outside the rejection region
    x_beta = np.linspace(x[0], z_crit, 500)
    ax.fill_between(x_beta, norm.pdf(x_beta, delta, sigma),
                    alpha=0.25, color="grey", label=r"$\beta$ (Type II error)")

    # Critical value line
    ax.axvline(z_crit, color="black", linestyle="--", linewidth=1)
    ax.annotate(rf"$z_{{\alpha/2}} = {z_crit:.2f}$",
                xy=(z_crit, ax.get_ylim()[1] * 0.6),
                xytext=(z_crit + 0.3, ax.get_ylim()[1] * 0.75),
                fontsize=11, ha="left",
                arrowprops=dict(arrowstyle="->", color="black"))

    ax.set_xlabel("Test statistic $Z$")
    ax.set_ylabel("Density")
    ax.legend(loc="upper left", fontsize=9, framealpha=0.9)
    ax.grid(True, alpha=0.3)
    ax.set_xlim(x[0], x[-1])
    ax.set_ylim(bottom=0)

    plt.tight_layout()
    save(fig, "statistical_power")


def generate_t_vs_normal():
    x = np.linspace(-5, 5, 1000)
    dfs = [2, 5, 10]
    colors = ["tab:red", "tab:orange", "tab:green"]

    fig, ax = plt.subplots(figsize=(10, 4.5))

    ax.plot(x, norm.pdf(x), color="steelblue", linewidth=2.5,
            label=r"$\mathcal{N}(0,1)$")

    for df, color in zip(dfs, colors):
        ax.plot(x, t.pdf(x, df), linewidth=1.8, color=color,
                label=rf"$t$ (df$={df}$)")

    ax.set_xlabel("$x$")
    ax.set_ylabel("Density")
    ax.legend(fontsize=10, framealpha=0.9)
    ax.grid(True, alpha=0.3)
    ax.set_xlim(x[0], x[-1])
    ax.set_ylim(bottom=0)

    plt.tight_layout()
    save(fig, "t_vs_normal")


def generate_all():
    generate_power()
    generate_t_vs_normal()
