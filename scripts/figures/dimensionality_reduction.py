"""Dimensionality reduction figures: PCA projection and MNIST 3D comparison."""

from pathlib import Path

import numpy as np
import matplotlib.pyplot as plt

from . import save

CACHE_DIR = Path(__file__).resolve().parent.parent / ".cache"


def generate_pca_projection():
    rng = np.random.RandomState(42)

    mean = [0, 0]
    cov = [[3, 2], [2, 2]]
    X = rng.multivariate_normal(mean, cov, 80)

    X_centered = X - X.mean(axis=0)
    _, _, Vt = np.linalg.svd(X_centered, full_matrices=False)
    pc1 = Vt[0]
    pc2 = Vt[1]

    projections_pc1 = X_centered @ pc1
    projected_points_pc1 = np.outer(projections_pc1, pc1)

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(13, 5.5))

    # Left panel: projection onto PC1
    ax1.scatter(X_centered[:, 0], X_centered[:, 1], alpha=0.4, s=30, color="tab:blue", zorder=2)

    extent = 4.5
    ax1.plot([-extent * pc1[0], extent * pc1[0]],
             [-extent * pc1[1], extent * pc1[1]],
             color="tab:red", linewidth=2, label="PC1", zorder=1)

    for i in range(len(X_centered)):
        ax1.plot([X_centered[i, 0], projected_points_pc1[i, 0]],
                 [X_centered[i, 1], projected_points_pc1[i, 1]],
                 color="tab:gray", alpha=0.3, linewidth=0.5, zorder=1)

    ax1.scatter(projected_points_pc1[:, 0], projected_points_pc1[:, 1],
                alpha=0.6, s=20, color="tab:red", zorder=3)

    ax1.set_xlabel("$x_1$")
    ax1.set_ylabel("$x_2$")
    ax1.set_title("Projection onto PC1")
    ax1.set_aspect("equal")
    ax1.legend()
    ax1.grid(True, alpha=0.2)

    # Right panel: projection onto PC2
    projections_pc2 = X_centered @ pc2
    projected_points_pc2 = np.outer(projections_pc2, pc2)

    ax2.scatter(X_centered[:, 0], X_centered[:, 1], alpha=0.4, s=30, color="tab:blue", zorder=2)

    ax2.plot([-extent * pc2[0], extent * pc2[0]],
             [-extent * pc2[1], extent * pc2[1]],
             color="tab:orange", linewidth=2, label="PC2", zorder=1)

    for i in range(len(X_centered)):
        ax2.plot([X_centered[i, 0], projected_points_pc2[i, 0]],
                 [X_centered[i, 1], projected_points_pc2[i, 1]],
                 color="tab:gray", alpha=0.3, linewidth=0.5, zorder=1)

    ax2.scatter(projected_points_pc2[:, 0], projected_points_pc2[:, 1],
                alpha=0.6, s=20, color="tab:orange", zorder=3)

    ax2.set_xlabel("$x_1$")
    ax2.set_ylabel("$x_2$")
    ax2.set_title("Projection onto PC2")
    ax2.set_aspect("equal")
    ax2.legend()
    ax2.grid(True, alpha=0.2)

    lim = 5.5
    for ax in (ax1, ax2):
        ax.set_xlim(-lim, lim)
        ax.set_ylim(-lim, lim)

    plt.tight_layout()
    save(fig, "pca_projection")


def _load_mnist(n_samples=3000, seed=0):
    """Load a cached subsample of MNIST (28x28). Downloads once via openml."""
    CACHE_DIR.mkdir(exist_ok=True)
    cache_path = CACHE_DIR / f"mnist_{n_samples}_{seed}.npz"
    if cache_path.exists():
        data = np.load(cache_path)
        print(f"  Loaded cached MNIST subsample ({n_samples} images)")
        return data["X"], data["y"]

    from sklearn.datasets import fetch_openml

    mnist = fetch_openml("mnist_784", version=1, as_frame=False, parser="liac-arff")
    X_full = mnist.data.astype(np.float32)
    y_full = mnist.target.astype(int)

    rng = np.random.RandomState(seed)
    idx = rng.choice(len(X_full), size=n_samples, replace=False)
    X, y = X_full[idx], y_full[idx]
    np.savez_compressed(cache_path, X=X, y=y)
    print(f"  Fetched MNIST and cached {n_samples}-image subsample")
    return X, y


def generate_mnist_comparison():
    from sklearn.decomposition import PCA
    from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
    from sklearn.manifold import TSNE
    from sklearn.preprocessing import StandardScaler
    from umap import UMAP

    X, y = _load_mnist(n_samples=3000, seed=0)
    X_scaled = StandardScaler().fit_transform(X)

    print("  Running PCA...")
    pca = PCA(n_components=3, random_state=0).fit_transform(X_scaled)
    print("  Running LDA...")
    lda = LinearDiscriminantAnalysis(n_components=3).fit_transform(X_scaled, y)
    print("  Running t-SNE (this is slow)...")
    tsne = TSNE(n_components=3, perplexity=30, init="pca", random_state=0).fit_transform(X_scaled)
    print("  Running UMAP...")
    umap = UMAP(n_components=3, random_state=0).fit_transform(X_scaled)

    embeddings = [
        ("PCA (linear, unsupervised)", pca),
        ("LDA (linear, supervised)", lda),
        ("t-SNE (nonlinear)", tsne),
        ("UMAP (nonlinear)", umap),
    ]

    fig = plt.figure(figsize=(13, 11))
    cmap = plt.get_cmap("tab10")

    for i, (title, emb) in enumerate(embeddings):
        ax = fig.add_subplot(2, 2, i + 1, projection="3d")
        sc = ax.scatter(emb[:, 0], emb[:, 1], emb[:, 2],
                        c=y, cmap=cmap, vmin=-0.5, vmax=9.5, s=4, alpha=0.6)
        ax.set_title(title)
        ax.set_xticklabels([])
        ax.set_yticklabels([])
        ax.set_zticklabels([])

    cbar = fig.colorbar(sc, ax=fig.axes, ticks=range(10), shrink=0.6, pad=0.02)
    cbar.set_label("Digit")

    save(fig, "mnist_dimensionality_reduction")


def generate_all():
    generate_pca_projection()
    generate_mnist_comparison()
