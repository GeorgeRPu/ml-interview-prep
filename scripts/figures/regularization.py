"""Regularization figures: L1 vs L2 constraint regions, regularization paths."""

import numpy as np
import matplotlib.pyplot as plt

from . import save


def generate_l1_vs_l2_constraint():
    fig, (ax_l1, ax_l2) = plt.subplots(1, 2, figsize=(13, 5.5))

    theta1 = np.linspace(-2.5, 2.5, 400)
    theta2 = np.linspace(-2.5, 2.5, 400)
    T1, T2 = np.meshgrid(theta1, theta2)

    center = np.array([1.8, 1.5])
    A = np.array([[1.0, 0.3], [0.3, 0.6]])
    Z = (A[0, 0] * (T1 - center[0]) ** 2
         + 2 * A[0, 1] * (T1 - center[0]) * (T2 - center[1])
         + A[1, 1] * (T2 - center[1]) ** 2)

    levels = [0.5, 1.5, 3.0, 5.0, 8.0, 12.0]

    # L1 constraint (diamond)
    t = np.linspace(0, 2 * np.pi, 500)
    diamond_x = np.cos(t) * np.sign(np.cos(t)) * np.abs(np.cos(t)) ** 0
    diamond_r = 1.0
    diamond_pts = np.array([
        [diamond_r, 0], [0, diamond_r], [-diamond_r, 0], [0, -diamond_r], [diamond_r, 0]
    ])

    ax_l1.contour(T1, T2, Z, levels=levels, colors="tab:blue", alpha=0.6, linewidths=1.5)
    ax_l1.fill(diamond_pts[:, 0], diamond_pts[:, 1], alpha=0.15, color="tab:orange")
    ax_l1.plot(diamond_pts[:, 0], diamond_pts[:, 1], color="tab:orange", linewidth=2.5)
    ax_l1.plot(*center, "x", color="tab:blue", markersize=10)
    ax_l1.plot(diamond_r, 0, "o", color="tab:red", markersize=5, zorder=5)
    ax_l1.annotate("$\\theta^*_{\\mathrm{L1}}$",
                   xy=(diamond_r, 0), xytext=(diamond_r + 0.25, -0.35),
                   fontsize=13, color="tab:red",
                   arrowprops=dict(arrowstyle="->", color="tab:red", lw=1.5))
    ax_l1.set_xlabel("$\\theta_1$", fontsize=13)
    ax_l1.set_ylabel("$\\theta_2$", fontsize=13)
    ax_l1.set_title("L1 constraint (diamond)")
    ax_l1.set_xlim(-2.5, 2.5)
    ax_l1.set_ylim(-2.5, 2.5)
    ax_l1.set_aspect("equal")
    ax_l1.axhline(0, color="tab:gray", linewidth=0.5, alpha=0.5)
    ax_l1.axvline(0, color="tab:gray", linewidth=0.5, alpha=0.5)
    ax_l1.grid(True, alpha=0.2)

    # L2 constraint (circle)
    circle_t = np.linspace(0, 2 * np.pi, 500)
    circle_r = 1.0
    circle_x = circle_r * np.cos(circle_t)
    circle_y = circle_r * np.sin(circle_t)

    ax_l2.contour(T1, T2, Z, levels=levels, colors="tab:blue", alpha=0.6, linewidths=1.5)
    ax_l2.fill(circle_x, circle_y, alpha=0.15, color="tab:orange")
    ax_l2.plot(circle_x, circle_y, color="tab:orange", linewidth=2.5)
    ax_l2.plot(*center, "x", color="tab:blue", markersize=10)

    # Find tangent point: project OLS onto circle
    norm = np.sqrt(center[0] ** 2 + center[1] ** 2)
    tangent = center / norm * circle_r
    ax_l2.plot(*tangent, "o", color="tab:red", markersize=5, zorder=5)
    ax_l2.annotate("$\\theta^*_{\\mathrm{L2}}$",
                   xy=tangent, xytext=(tangent[0] + 0.25, tangent[1] + 0.3),
                   fontsize=13, color="tab:red",
                   arrowprops=dict(arrowstyle="->", color="tab:red", lw=1.5))
    ax_l2.set_xlabel("$\\theta_1$", fontsize=13)
    ax_l2.set_ylabel("$\\theta_2$", fontsize=13)
    ax_l2.set_title("L2 constraint (circle)")
    ax_l2.set_xlim(-2.5, 2.5)
    ax_l2.set_ylim(-2.5, 2.5)
    ax_l2.set_aspect("equal")
    ax_l2.axhline(0, color="tab:gray", linewidth=0.5, alpha=0.5)
    ax_l2.axvline(0, color="tab:gray", linewidth=0.5, alpha=0.5)
    ax_l2.grid(True, alpha=0.2)

    plt.tight_layout()
    save(fig, "l1_vs_l2_constraint")


def generate_all():
    generate_l1_vs_l2_constraint()
