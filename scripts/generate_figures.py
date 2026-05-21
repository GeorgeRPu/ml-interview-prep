"""Generate all figures for the ml-interview-prep site.

Run from the repo root:  python scripts/generate_figures.py
"""

import json
from datetime import datetime
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import requests
from scipy.optimize import curve_fit

REPO_ROOT = Path(__file__).resolve().parent.parent
FIGURES_DIR = REPO_ROOT / "_static" / "figures"
CACHE_DIR = REPO_ROOT / "scripts" / ".cache"


def generate_temperature_residuals():
    """Daily temperature residuals plot for the stationarity article.

    Uses real daily mean temperature from Central Park, NYC (2021-2023)
    via the Open-Meteo historical weather API.
    """
    CACHE_DIR.mkdir(exist_ok=True)
    FIGURES_DIR.mkdir(exist_ok=True)

    cache_path = CACHE_DIR / "temperature_cache.json"
    if cache_path.exists():
        with open(cache_path) as f:
            data = json.load(f)
        print("  Loaded cached temperature data")
    else:
        resp = requests.get(
            "https://archive-api.open-meteo.com/v1/archive",
            params={
                "latitude": 40.7829,
                "longitude": -73.9654,
                "start_date": "2021-01-01",
                "end_date": "2023-12-31",
                "daily": "temperature_2m_mean",
                "timezone": "America/New_York",
            },
            timeout=30,
        )
        resp.raise_for_status()
        data = resp.json()
        with open(cache_path, "w") as f:
            json.dump(data, f)
        print(f"  Fetched {len(data['daily']['time'])} days from Open-Meteo")

    temps = np.array(data["daily"]["temperature_2m_mean"], dtype=float)
    dates = [datetime.strptime(d, "%Y-%m-%d") for d in data["daily"]["time"]]
    day_of_year = np.array([d.timetuple().tm_yday for d in dates], dtype=float)

    def seasonal_model(doy, mu, A, phi):
        return mu + A * np.sin(2 * np.pi * (doy - phi) / 365.25)

    popt, _ = curve_fit(seasonal_model, day_of_year, temps, p0=[12, 12, 110])
    seasonal = seasonal_model(day_of_year, *popt)
    residuals = temps - seasonal

    days = np.arange(len(temps))
    fig, axes = plt.subplots(3, 1, figsize=(10, 7), sharex=True)

    axes[0].plot(days, temps, linewidth=0.5, color="tab:red")
    axes[0].set_ylabel("Temperature (°C)")
    axes[0].set_title("Daily Mean Temperature — Central Park, NYC (2021–2023)")

    axes[1].plot(days, seasonal, linewidth=1.5, color="tab:orange")
    axes[1].set_ylabel("Temperature (°C)")
    axes[1].set_title("Fitted Seasonal Component")

    axes[2].plot(days, residuals, linewidth=0.5, color="tab:blue")
    axes[2].axhline(0, color="black", linewidth=0.5, linestyle="--")
    axes[2].set_ylabel("Residual (°C)")
    axes[2].set_title("Residuals After Removing Seasonal Trend (≈ weakly stationary)")
    axes[2].set_xlabel("Day")

    plt.tight_layout()
    for ext in ("svg", "png"):
        out = FIGURES_DIR / f"daily_temperature_residuals.{ext}"
        fig.savefig(out, dpi=150, bbox_inches="tight")
    plt.close(fig)
    print("  Saved daily_temperature_residuals.svg and .png")


if __name__ == "__main__":
    print("Generating figures...")
    generate_temperature_residuals()
    print("Done.")
