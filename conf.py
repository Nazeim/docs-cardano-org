

import sys
import os
import sphinx_rtd_theme
import recommonmark

from recommonmark.transform import AutoStructify
from os.path import abspath, join, dirname

sys.path.insert(0, abspath(join(dirname(__file__))))

# -- RTD configuration ------------------------------------------------

on_rtd = os.environ.get("READTHEDOCS", None) == "True"

# This is used for linking and such so we link to the thing we're building
rtd_version = os.environ.get("READTHEDOCS_VERSION", "latest")
if rtd_version not in ["stable", "latest"]:
    rtd_version = "stable"

# -- Project information -----------------------------------------------------

project = 'Cardano Documentation'
copyright = '2020, IOHK'
author = 'IOHK'

# The full version, including alpha/beta/rc tags
release = '1.0.0'


# -- General configuration ---------------------------------------------------
master_doc = 'index'
# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.

extensions = [
    "sphinx_rtd_theme",
    'recommonmark',
    'sphinx_markdown_tables',
    'sphinxemoji.sphinxemoji',
    "sphinx.ext.autodoc",
    "sphinx.ext.autosummary",
    "sphinx.ext.intersphinx",
    "sphinx.ext.viewcode",
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['.sphinx/_templates']
html_static_path = ['.sphinx/_static']

source_suffix = {
    '.rst': 'restructuredtext',
    '.md': 'markdown',
}

intersphinx_mapping = {
    "cardano-node": (
        "https://cardano.readthedocs.io/projects/cardano-node/en/%s/"
        % rtd_version,
        None,
    ),
}

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = "sphinx_rtd_theme"
#html_style = '.sphinx/css/modified-theme.css'

html_theme_options = {
    'logo_only': False,
    'display_version': False,
    'prev_next_buttons_location': 'bottom',
    'style_external_links': False,
    'vcs_pageview_mode': '',
    'style_nav_header_background': '#fcfcfc',
    # Toc options
    'collapse_navigation': True,
    'sticky_navigation': True,
    'navigation_depth': 4,
    'includehidden': True,
    'titles_only': False
}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".

html_logo = ".sphinx/cardano-logo.png"

html_context = {
  "display_github": True, # Add 'Edit on Github' link instead of 'View page source'
  "github_user": "cardano-foundation",
  "github_repo": "docs-cardano-org",
  "github_version": "main",
  "conf_py_path": "/",
  "source_suffix": source_suffix,
}

# -- Custom Document processing ----------------------------------------------

def setup(app):
    app.add_config_value('recommonmark_config', {
            'enable_auto_doc_ref': False,
            'enable_auto_toc_tree': False,
            }, True)
    app.add_transform(AutoStructify)