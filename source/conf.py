# -*- coding: utf-8 -*-

from pkg_resources import DistributionNotFound, get_distribution



# General stuff
extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.intersphinx",
    "sphinx.ext.napoleon",
    "sphinx.ext.mathjax",
    "myst_nb",
]

myst_enable_extensions = ["dollarmath", "colon_fence"]
source_suffix = ".rst"
master_doc = "index"

project = "Ascopy"
copyright = "2023-today, Zunli Yuan & contributors"
version = '0.0.1'
release = '0.0.1'
exclude_patterns = ["_build"]

# HTML theme
html_theme = 'sphinx_rtd_theme'

html_copy_source = True
html_show_sourcelink = True
html_sourcelink_suffix = ""
html_title = "Ascopy"
html_favicon = "_static/favicon.png"
html_static_path = ["_static"]
html_theme_options = {
    "path_to_docs": "docs",
    "repository_url": "https://github.com/wenjie-astro/Ascopy",
    "repository_branch": "main",
    "launch_buttons": {
        "binderhub_url": "https://mybinder.org",
        "notebook_interface": "classic",
    },
    "use_edit_page_button": True,
    "use_issues_button": True,
    "use_repository_button": True,
    "use_download_button": True,
}
jupyter_execute_notebooks = "off"
execution_timeout = -1