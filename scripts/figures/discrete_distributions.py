"""Bernoulli, binomial, geometric, and Poisson distribution figures."""

from math import comb, factorial

import matplotlib.pyplot as plt
import numpy as np

from . import save


def generate_bernoulli():
    p = 0.5
    k = np.array([0, 1])
    pmf = np.array([1 - p, p])
    cdf_vals = np.array([1 - p, 1.0])

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 3))
    fig.suptitle(f"Bernoulli Distribution (p = {p})",
                 fontweight="bold", fontsize=14)

    ax1.bar(k, pmf, width=0.6)
    ax1.set_title("PMF")
    ax1.set_xlabel("x")
    ax1.set_ylabel("P(X = x)")
    ax1.set_xticks(k)
    ax1.set_ylim(0, max(pmf) * 1.1)
    ax1.grid(True, alpha=0.3)

    x_ext = np.array([-1, 0, 0, 1, 1, 2])
    y_ext = np.array([0, 0, 1 - p, 1 - p, 1.0, 1.0])
    ax2.plot(x_ext, y_ext, linewidth=2)
    ax2.plot(k, cdf_vals, "o", markersize=7, color="tab:blue")
    ax2.plot(k, [0, 1 - p], "o", markersize=7, color="tab:blue",
             markerfacecolor="white", markeredgewidth=2)
    ax2.set_title("CDF")
    ax2.set_xlabel("x")
    ax2.set_ylabel("F(x)")
    ax2.set_ylim(-0.05, 1.1)
    ax2.grid(True, alpha=0.3)

    plt.tight_layout()
    save(fig, "bernoulli")


def generate_binomial():
    n, p = 10, 0.5
    k = np.arange(0, n + 1)
    pmf = np.array([comb(n, ki) * p**ki * (1 - p) ** (n - ki) for ki in k])
    cdf_vals = np.cumsum(pmf)

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 3))
    fig.suptitle(f"Binomial Distribution (n = {n}, p = {p})",
                 fontweight="bold", fontsize=14)

    ax1.bar(k, pmf)
    ax1.set_title("PMF")
    ax1.set_xlabel("k")
    ax1.set_ylabel("P(X = k)")
    ax1.grid(True, alpha=0.3)

    ax2.plot(k, cdf_vals, "-o", markersize=5)
    ax2.set_title("CDF")
    ax2.set_xlabel("k")
    ax2.set_ylabel("F(k)")
    ax2.grid(True, alpha=0.3)

    plt.tight_layout()
    save(fig, "binomial")


def generate_geometric():
    p = 0.3
    k = np.arange(1, 16)
    pmf = (1 - p) ** (k - 1) * p
    cdf_vals = 1 - (1 - p) ** k

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 3))
    fig.suptitle(f"Geometric Distribution (p = {p})",
                 fontweight="bold", fontsize=14)

    ax1.bar(k, pmf)
    ax1.set_title("PMF")
    ax1.set_xlabel("k")
    ax1.set_ylabel("P(X = k)")
    ax1.grid(True, alpha=0.3)

    ax2.plot(k, cdf_vals, "-o", markersize=5)
    ax2.set_title("CDF")
    ax2.set_xlabel("k")
    ax2.set_ylabel("F(k)")
    ax2.grid(True, alpha=0.3)

    plt.tight_layout()
    save(fig, "geometric")


def generate_poisson():
    lam = 4
    k = np.arange(0, 15)
    pmf = np.array([lam**ki * np.exp(-lam) / factorial(ki) for ki in k])
    cdf_vals = np.cumsum(pmf)

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 3))
    fig.suptitle(f"Poisson Distribution (λ = {lam})",
                 fontweight="bold", fontsize=14)

    ax1.bar(k, pmf)
    ax1.set_title("PMF")
    ax1.set_xlabel("k")
    ax1.set_ylabel("P(X = k)")
    ax1.grid(True, alpha=0.3)

    ax2.plot(k, cdf_vals, "-o", markersize=5)
    ax2.set_title("CDF")
    ax2.set_xlabel("k")
    ax2.set_ylabel("F(k)")
    ax2.grid(True, alpha=0.3)

    plt.tight_layout()
    save(fig, "poisson")


def generate_all():
    generate_bernoulli()
    generate_binomial()
    generate_geometric()
    generate_poisson()
