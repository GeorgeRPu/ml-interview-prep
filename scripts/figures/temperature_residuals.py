"""Daily temperature residuals figure for the stationarity article.

Uses real daily mean temperature from Central Park, NYC (2021-2023)
via the Open-Meteo historical weather API.
"""

import json
from datetime import datetime
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import requests
from scipy.optimize import curve_fit

from . import save

CACHE_DIR = Path(__file__).resolve().parent.parent / ".cache"


def _seasonal_model(doy, mu, A, phi):
    return mu + A * np.sin(2 * np.pi * (doy - phi) / 365.25)


def generate_temperature_residuals():
    CACHE_DIR.mkdir(exist_ok=True)

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

    popt, _ = curve_fit(_seasonal_model, day_of_year, temps, p0=[12, 12, 110])
    seasonal = _seasonal_model(day_of_year, *popt)
    residuals = temps - seasonal

    days = np.arange(len(temps))
    fig, axes = plt.subplots(3, 1, figsize=(10, 7), sharex=True)

    axes[0].plot(days, temps, linewidth=0.5, color="tab:red")
    axes[0].set_ylabel("Temperature (°C)")
    axes[0].set_title("Daily mean temperature — Central Park, NYC (2021–2023)")

    axes[1].plot(days, seasonal, linewidth=1.5, color="tab:orange")
    axes[1].set_ylabel("Temperature (°C)")
    axes[1].set_title("Fitted seasonal component")

    axes[2].plot(days, residuals, linewidth=0.5, color="tab:blue")
    axes[2].axhline(0, color="black", linewidth=0.5, linestyle="--")
    axes[2].set_ylabel("Residual (°C)")
    axes[2].set_title("Residuals after removing seasonal trend (≈ weakly stationary)")
    axes[2].set_xlabel("Day")

    plt.tight_layout()
    save(fig, "daily_temperature_residuals")


def generate_all():
    generate_temperature_residuals()
