# ML Interview Prep

A growing collection of study notes for machine learning interviews, built into a searchable documentation site with Sphinx and deployed to GitHub Pages.

🌐 **Live site:** https://georgerpu.github.io/ml-interview-prep/

Covers **ML Breadth**, **ML Coding**, and **ML System Design** — from Bayes' Theorem to Gradient Boosting to Recommendation Systems.

## 📦 Installation

Install [`uv`](https://docs.astral.sh/uv/getting-started/installation/) if you don't have it, then install project dependencies:

```bash
uv sync
```

## 📖 Building the Documentation

```bash
uv run make clean
uv run make html
```

Open `_build/html/index.html` in your browser to preview locally.

## 🧪 Testing GitHub Actions with `act`

[`act`](https://github.com/nektos/act) lets you run the deploy workflow locally without pushing to GitHub.

`act` requires [Docker](https://docs.docker.com/get-started/get-docker/) to be installed and running.

Install [`act`](https://nektosact.com/installation/index.html) if you don't have it, then run the deploy workflow:

```bash
act push
```

**Run with a specific Docker image** (faster, smaller):

```bash
act push -P ubuntu-latest=catthehacker/ubuntu:act-latest
```

## 🗂️ Package Structure

```
ml-interview-prep/
├── ml-breadth/             # ML breadth concept notes
├── ml-system-design/       # ML system design case studies
├── _static/                # Static assets (images, CSS)
├── _templates/             # Sphinx HTML templates
├── _build/                 # Build output (gitignored)
├── conf.py                 # Sphinx configuration
├── index.rst               # Documentation homepage
├── ml-coding.rst           # ML coding section
├── Makefile                # Build automation
└── pyproject.toml          # Project metadata and dependencies
```

Each topic in `ml-breadth/` and `ml-system-design/` is a standalone `.md` file containing concept explanations, worked examples, and mathematical derivations rendered with MyST and sphinx-proof.
