# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'ml-interview-prep'
copyright = '2026, George Pu'
author = 'George Pu'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ["myst_parser", "sphinx_proof", "sphinxcontrib.bibtex"]

myst_enable_extensions = ["dollarmath", "amsmath"]

bibtex_bibfiles = ["references.bib"]
bibtex_default_style = "alpha"
bibtex_reference_style = "author_year"

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store', '.venv']

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

mathjax3_config = {
    "tex": {
        "macros": {
            "argmin": "\\operatorname*{arg\\,min}",
            "argmax": "\\operatorname*{arg\\,max}",
        }
    }
}

html_theme = 'pydata_sphinx_theme'
html_static_path = ['_static']
html_css_files = ['custom.css']

html_theme_options = {
    "navbar_align": "left",
    "show_prev_next": False,
    "use_edit_page_button": False,
}
