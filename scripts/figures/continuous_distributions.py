"""Uniform, normal, and exponential distribution figures."""

import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import norm

from . import save


def generate_uniform():
    a, b = 0, 1
    margin = 0.5

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 3))
    fig.suptitle(f"Uniform Distribution [{a}, {b}]",
                 fontweight="bold", fontsize=14)

    x_pdf = [a - margin, a, a, b, b, b + margin]
    y_pdf = [0, 0, 1 / (b - a), 1 / (b - a), 0, 0]
    ax1.plot(x_pdf, y_pdf, linewidth=2)
    ax1.set_title("PDF")
    ax1.set_xlabel("x")
    ax1.set_ylabel("f(x)")
    ax1.grid(True, alpha=0.3)

    x_cdf = [a - margin, a, b, b + margin]
    y_cdf = [0, 0, 1, 1]
    ax2.plot(x_cdf, y_cdf, linewidth=2)
    ax2.set_title("CDF")
    ax2.set_xlabel("x")
    ax2.set_ylabel("F(x)")
    ax2.grid(True, alpha=0.3)

    plt.tight_layout()
    save(fig, "uniform")


def generate_normal():
    mu, sigma = 0, 1
    x = np.linspace(mu - 4 * sigma, mu + 4 * sigma, 400)

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 3))
    fig.suptitle(f"Normal Distribution (μ = {mu}, σ = {sigma})",
                 fontweight="bold", fontsize=14)

    ax1.plot(x, norm.pdf(x, mu, sigma), linewidth=2)
    ax1.set_title("PDF")
    ax1.set_xlabel("x")
    ax1.set_ylabel("f(x)")
    ax1.grid(True, alpha=0.3)

    ax2.plot(x, norm.cdf(x, mu, sigma), linewidth=2)
    ax2.set_title("CDF")
    ax2.set_xlabel("x")
    ax2.set_ylabel("F(x)")
    ax2.grid(True, alpha=0.3)

    plt.tight_layout()
    save(fig, "normal")


def generate_exponential():
    lam = 1
    x = np.linspace(0, 5, 400)

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 3))
    fig.suptitle(f"Exponential Distribution (λ = {lam})",
                 fontweight="bold", fontsize=14)

    ax1.plot(x, lam * np.exp(-lam * x), linewidth=2)
    ax1.set_title("PDF")
    ax1.set_xlabel("x")
    ax1.set_ylabel("f(x)")
    ax1.grid(True, alpha=0.3)

    ax2.plot(x, 1 - np.exp(-lam * x), linewidth=2)
    ax2.set_title("CDF")
    ax2.set_xlabel("x")
    ax2.set_ylabel("F(x)")
    ax2.grid(True, alpha=0.3)

    plt.tight_layout()
    save(fig, "exponential")


def generate_all():
    generate_uniform()
    generate_normal()
    generate_exponential()
