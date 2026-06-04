"""Generate all figures for the ml-interview-prep site.

Run from the repo root:  python -m scripts.generate_figures
"""

from scripts.figures.calibration import generate_all as calibration
from scripts.figures.classification_metrics import generate_all as classification
from scripts.figures.continuous_distributions import generate_all as continuous
from scripts.figures.discrete_distributions import generate_all as discrete
from scripts.figures.hypothesis_testing import generate_all as hypothesis
from scripts.figures.ranking_metrics import generate_all as ranking
from scripts.figures.regression_metrics import generate_all as regression
from scripts.figures.regularization import generate_all as regularization
from scripts.figures.temperature_residuals import generate_all as temperature

if __name__ == "__main__":
    print("Generating figures...")
    classification()
    calibration()
    discrete()
    continuous()
    hypothesis()
    ranking()
    regression()
    regularization()
    temperature()
    print("Done.")
