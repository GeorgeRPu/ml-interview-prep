from pathlib import Path

import matplotlib
matplotlib.use("agg")
import matplotlib.pyplot as plt

REPO_ROOT = Path(__file__).resolve().parent.parent.parent
FIGURES_DIR = REPO_ROOT / "_static" / "figures"
DPI = 300


def save(fig, name):
    FIGURES_DIR.mkdir(parents=True, exist_ok=True)
    fig.savefig(FIGURES_DIR / f"{name}.png", dpi=DPI, bbox_inches="tight")
    plt.close(fig)
    print(f"  Saved {name}.png")
