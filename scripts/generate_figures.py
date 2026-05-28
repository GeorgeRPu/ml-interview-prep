"""Generate all figures for the ml-interview-prep site.

Run from the repo root:  python -m scripts.generate_figures
"""

from scripts.figures.continuous_distributions import generate_all as continuous
from scripts.figures.discrete_distributions import generate_all as discrete
from scripts.figures.hypothesis_testing import generate_all as hypothesis
from scripts.figures.temperature_residuals import generate_all as temperature

if __name__ == "__main__":
    print("Generating figures...")
    discrete()
    continuous()
    hypothesis()
    temperature()
    print("Done.")
