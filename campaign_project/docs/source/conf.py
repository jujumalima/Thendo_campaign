import os
import sys

# -- Path setup --------------------------------------------------------------
# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. Adjust the path as necessary.
sys.path.insert(0, os.path.abspath('../'))  # Adjust path to your Django project

# Setting up Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'campaign_project.settings')
import django
django.setup()

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Thendo Campaign_docs'
copyright = '2024, Thendo Malima'
author = 'Thendo Malima'
release = '2024/11/15'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'sphinx.ext.autodoc',        # Automatically document Python code
    'sphinx.ext.viewcode',       # Include source code links
    'sphinx.ext.napoleon',       # Support for Google-style and NumPy-style docstrings
    'sphinx.ext.intersphinx',    # Link to other projects’ documentation
    'sphinx.ext.todo',           # Support for TODOs in documentation
    'sphinx.ext.coverage',       # Coverage checking for docstrings
    'sphinx.ext.mathjax',        # Render mathematical expressions
    'sphinx.ext.githubpages',    # Publish HTML files to GitHub Pages
]

# Enable TODOs in the output
todo_include_todos = True

# Define patterns to exclude specific files and directories
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

templates_path = ['_templates']

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'alabaster'  # You can also use 'sphinx_rtd_theme' or other themes
html_static_path = ['_static']

# Custom sidebar for Alabaster theme
html_sidebars = {
    '**': [
        'about.html',
        'navigation.html',
        'searchbox.html',
    ]
}

# -- Options for Extensions --------------------------------------------------
# Napoleon settings for docstring styles
napoleon_google_docstring = True
napoleon_numpy_docstring = True

# Intersphinx mapping for external documentation linking
intersphinx_mapping = {
    'python': ('https://docs.python.org/3', None),
    'django': ('https://docs.djangoproject.com/en/stable/', 'https://docs.djangoproject.com/en/stable/objects.inv'),
}

# -- Additional Configuration ------------------------------------------------
# Add custom CSS or JavaScript
html_css_files = [
    'custom.css',  # Place custom.css in the _static folder for custom styles
]

html_js_files = [
    'custom.js',  # Place custom.js in the _static folder for custom scripts
]
