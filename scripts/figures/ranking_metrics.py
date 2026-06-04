"""Ranking metric figures: P@k/R@k vs k, AP ordering comparison, DCG/nDCG."""

import numpy as np
import matplotlib.pyplot as plt

from . import save


def _precision_recall_at_k(relevance):
    n = len(relevance)
    total_relevant = np.sum(relevance)
    cum_relevant = np.cumsum(relevance)
    ks = np.arange(1, n + 1)
    precision = cum_relevant / ks
    recall = cum_relevant / total_relevant
    return precision, recall


def _compute_ap(relevance):
    precision, recall = _precision_recall_at_k(relevance)
    total_relevant = np.sum(relevance)
    ap = np.sum(precision * relevance) / total_relevant
    return ap, precision, recall


def generate_precision_recall_at_k():
    relevance = np.array([1, 0, 1, 1, 0, 0, 1, 0, 0, 0])
    n = len(relevance)
    ks = np.arange(1, n + 1)
    precision, recall = _precision_recall_at_k(relevance)

    fig, (ax_list, ax_curve) = plt.subplots(1, 2, figsize=(13, 5))

    colors = ["tab:blue" if r else "tab:gray" for r in relevance]
    ax_list.barh(ks, np.ones(n), color=colors, edgecolor="white", height=0.6)
    ax_list.set_yticks(ks)
    ax_list.set_yticklabels([f"Item {i}" for i in ks], fontsize=10)
    ax_list.invert_yaxis()
    ax_list.set_xlim(0, 1.4)
    ax_list.set_xticks([])

    for i, r in enumerate(relevance):
        label = "Relevant" if r else "Non-relevant"
        ax_list.text(1.05, i + 1, label, va="center", fontsize=10,
                     color="tab:blue" if r else "tab:gray", fontweight="bold")

    ax_list.set_title("Ranked list with 4 relevant items")

    ax_curve.plot(ks, precision, color="tab:blue", marker="o", linewidth=2,
                  markersize=7, label="Precision@k", zorder=3)
    ax_curve.plot(ks, recall, color="tab:orange", marker="o", linewidth=2,
                  markersize=7, label="Recall@k", zorder=3)
    ax_curve.set_xlabel("$k$", fontsize=12)
    ax_curve.set_ylabel("Metric value", fontsize=12)
    ax_curve.set_xticks(ks)
    ax_curve.set_ylim(-0.05, 1.1)
    ax_curve.grid(True, alpha=0.3)
    ax_curve.set_title("Precision@k and Recall@k vs. $k$")

    plt.tight_layout()
    save(fig, "precision_recall_at_k")


def generate_ap_comparison():
    good = np.array([1, 1, 1, 0, 1, 0, 0, 0, 0, 0])
    poor = np.array([0, 0, 1, 0, 0, 1, 0, 1, 0, 1])

    fig, (ax_good, ax_poor) = plt.subplots(1, 2, figsize=(13, 5))

    for ax, relevance, color in [
        (ax_good, good, "tab:blue"),
        (ax_poor, poor, "tab:orange"),
    ]:
        ap, precision, recall = _compute_ap(relevance)

        rel_mask = relevance == 1
        rec_steps = np.concatenate([[0.0], recall[rel_mask]])
        prec_steps = np.concatenate([[1.0], precision[rel_mask]])

        ax.step(rec_steps, prec_steps, where="post", color=color, linewidth=2,
                label=f"AP = {ap:.2f}")
        ax.fill_between(rec_steps, prec_steps, step="post", alpha=0.2,
                        color=color)

        rel_positions = np.where(relevance == 1)[0]
        ax.scatter(recall[rel_positions], precision[rel_positions],
                   color=color, s=60, zorder=5, edgecolors="white", linewidths=1.5)

        ax.set_xlabel("Recall", fontsize=12)
        ax.set_ylabel("Precision", fontsize=12)
        ax.set_xlim(-0.05, 1.1)
        ax.set_ylim(-0.05, 1.1)
        ax.legend(loc="lower left", fontsize=11, framealpha=0.9)
        ax.grid(True, alpha=0.3)

        ranking_str = ", ".join(str(int(r)) for r in relevance)
        ax.set_title(f"Ranking [{ranking_str}]")

    plt.tight_layout()
    save(fig, "ap_comparison")


def generate_dcg_ndcg():
    relevance = np.array([2, 0, 3, 1, 0, 3, 0, 2, 1, 0])
    n = len(relevance)
    positions = np.arange(1, n + 1)

    gains = 2.0 ** relevance - 1
    discounts = np.log2(positions + 1)
    discounted_gains = gains / discounts

    ideal_relevance = np.sort(relevance)[::-1]
    ideal_gains = 2.0 ** ideal_relevance - 1
    ideal_discounted_gains = ideal_gains / discounts

    cum_dcg = np.cumsum(discounted_gains)
    cum_idcg = np.cumsum(ideal_discounted_gains)
    ndcg = cum_dcg[-1] / cum_idcg[-1]

    fig, (ax_bars, ax_cum) = plt.subplots(1, 2, figsize=(13, 5))

    ax_bars.bar(positions, discounted_gains, color="tab:blue", edgecolor="white",
                width=0.6, label="Discounted gain", zorder=3)
    for i, (dg, r) in enumerate(zip(discounted_gains, relevance)):
        if dg > 0:
            ax_bars.text(positions[i], dg + 0.15, f"$R={int(r)}$",
                         ha="center", fontsize=9, color="tab:blue")

    ax_disc = ax_bars.twinx()
    ax_disc.plot(positions, 1.0 / discounts, color="tab:gray", linestyle="--",
                 linewidth=2, marker="o", markersize=5, label="Discount $1/\\log_2(i+1)$")
    ax_disc.set_ylabel("Discount factor", fontsize=12, color="tab:gray")
    ax_disc.tick_params(axis="y", colors="tab:gray")
    ax_disc.set_ylim(0, 1.15)

    ax_bars.set_xlabel("Rank position $i$", fontsize=12)
    ax_bars.set_ylabel("Discounted gain", fontsize=12)
    ax_bars.set_xticks(positions)
    ax_bars.grid(True, alpha=0.3, axis="y")

    lines_1, labels_1 = ax_bars.get_legend_handles_labels()
    lines_2, labels_2 = ax_disc.get_legend_handles_labels()
    ax_bars.legend(lines_1 + lines_2, labels_1 + labels_2,
                   loc="upper right", fontsize=10, framealpha=0.9)

    ax_bars.set_title("Per-position discounted gain with discount curve")

    ax_cum.plot(positions, cum_idcg, color="tab:orange", linewidth=2, marker="o",
                markersize=6, label=f"Ideal DCG ({cum_idcg[-1]:.2f})", zorder=3)
    ax_cum.plot(positions, cum_dcg, color="tab:blue", linewidth=2, marker="o",
                markersize=6, label=f"Actual DCG ({cum_dcg[-1]:.2f})", zorder=3)
    ax_cum.fill_between(positions, cum_dcg, cum_idcg, alpha=0.15, color="tab:gray")

    ax_cum.annotate(f"nDCG@{n} = {ndcg:.2f}",
                    xy=(0.97, 0.05), xycoords="axes fraction",
                    fontsize=12, ha="right", va="bottom",
                    bbox=dict(boxstyle="round,pad=0.3", facecolor="white",
                              edgecolor="tab:gray", alpha=0.9))

    ax_cum.set_xlabel("$k$", fontsize=12)
    ax_cum.set_ylabel("Cumulative DCG", fontsize=12)
    ax_cum.set_xticks(positions)
    ax_cum.legend(loc="upper left", fontsize=10, framealpha=0.9)
    ax_cum.grid(True, alpha=0.3)
    ax_cum.set_title("Actual vs. ideal cumulative DCG")

    plt.tight_layout()
    save(fig, "dcg_ndcg")


def generate_all():
    generate_precision_recall_at_k()
    generate_ap_comparison()
    generate_dcg_ndcg()
