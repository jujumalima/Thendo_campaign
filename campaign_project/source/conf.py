# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information



import os
import sys

# Add Django project to the path
sys.path.insert(0, os.path.abspath('../../'))
os.environ['DJANGO_SETTINGS_MODULE'] = 'campaign_project.settings'

# Initialize Django
import django
django.setup()

project = 'Thendo Campaing'
copyright = '2024, Thendo Malima'
author = 'Thendo Malima'
release = '02'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration


extensions = [
    'sphinx.ext.autodoc',      # Generates documentation from docstrings
    'sphinx.ext.napoleon',     # Supports Google and NumPy style docstrings
    'sphinx.ext.viewcode',     # Adds links to source code
    'sphinx.ext.intersphinx',  # Links to external project docs
]


templates_path = ['_templates']
exclude_patterns = []



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'alabaster'
html_static_path = ['_static']
