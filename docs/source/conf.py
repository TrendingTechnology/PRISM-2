# -*- coding: utf-8 -*-
#
# Configuration file for the Sphinx documentation builder.
#
# This file does only contain a selection of the most common options. For a
# full list see the documentation:
# http://www.sphinx-doc.org/en/master/config

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os
import sys
from codecs import open
sys.path.insert(0, os.path.abspath('../..'))


# -- Project information -----------------------------------------------------

project = 'PRISM'
copyright = '2019, Ellert van der Velden'
author = 'Ellert van der Velden'

# The short X.Y version
version = 'latest'
# The full version, including alpha/beta/rc tags
exec(open('../../prism/__version__.py', 'r').read())
release = prism_version


# -- General configuration ---------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
#
needs_sphinx = '1.8'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.coverage',
    'sphinx.ext.mathjax',
    'sphinx.ext.viewcode',
    'sphinx.ext.napoleon',
    'sphinx.ext.intersphinx'
]

# Intersphinx configuration
intersphinx_mapping = {'python': ('https://docs.python.org/3', None),
                       'numpy': ('https://docs.scipy.org/doc/numpy', None),
                       'mpi4py': ('https://mpi4py.readthedocs.io/en/stable', None),
                       'matplotlib': ('https://matplotlib.org', None),
                       'h5py': ('https://h5py.readthedocs.io/en/stable', None)}

# Autodoc configuration
autodoc_default_options = {'members': None,
                           'private-members': None}
autodoc_member_order = 'groupwise'
autodoc_inherit_docstrings = False

# Napoleon configuration
napoleon_include_init_with_doc = True
napoleon_use_admonition_for_notes = True
napoleon_use_ivar = True
napoleon_use_param = False
napoleon_use_keyword = False
napoleon_use_rtype = False
napoleon_custom_sections = [
    ('Optional', 'Other Parameters'),
    ('Returns (if ndim(sam_set) > 1)', 'Returns'),
    ('Returns (if `figure` is *False*)', 'Returns'),
    ('Dict variables', 'Keyword Arguments'),
    'Description',
    'Generates',
    'Generates (if `figure` is *True*)',
    'Generates (for every emulator system)',
    'Props',
    'Formatting data_idx',
    'Notes (model_parameters)',
    'Notes (model_data)',
    'Prints (if ndim(sam_set) == 1)']

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
#
# source_suffix = ['.rst', '.md']
source_suffix = '.rst'

# The master toctree document.
master_doc = 'index'

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = None

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path .
exclude_patterns = []

# The name of the Pygments (syntax highlighting) style to use.
highlight_language = 'default'
pygments_style = 'sphinx'

add_function_parentheses = True
add_module_names = True
show_authors = True
numfig = True

# Reference formatting
numfig_format = {
    'figure': "Fig. %s",
    'table': "Tab. %s",
    'code-block': "Lst. %s",
    'section': "Sec. %s"}


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'sphinx_rtd_theme'

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
#
html_theme_options = {
    'prev_next_buttons_location': 'both',
    'collapse_navigation': False,
    'sticky_navigation': False,
    'includehidden': False,
    'titles_only': False
}

# Title formatting
html_title = "%s documentation" % (project, release)

# Date formatting
html_last_updated_fmt = '%a %d %b %Y'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# OpenSearch. Requires documentation to be online.
html_use_opensearch = 'https://prism-tool.readthedocs.io/en/latest'

# Custom sidebar templates, must be a dictionary that maps document names
# to template names.
#
# The default sidebars (for documents that don't match any pattern) are
# defined by theme itself.  Builtin themes are using these templates by
# default: ``['localtoc.html', 'relations.html', 'sourcelink.html',
# 'searchbox.html']``.
#
# html_sidebars = {}

html_split_index = True

html_favicon = 'py.png'

html_baseurl = 'https://prism-tool.readthedocs.io/en/latest'

html_extra_path = ['_static/google3ccf0e77d0aa4c22.html']


# -- Options for HTMLHelp output ---------------------------------------------

# Output file base name for HTML help builder.
htmlhelp_basename = 'PRISMdoc'


# -- Options for LaTeX output ------------------------------------------------

latex_elements = {
    # The paper size ('letterpaper' or 'a4paper').
    #
    # 'papersize': 'letterpaper',

    # The font size ('10pt', '11pt' or '12pt').
    #
    # 'pointsize': '10pt',

    # Additional stuff for the LaTeX preamble.
    #
    # 'preamble': '',

    # Latex figure (float) alignment
    #
    # 'figure_align': 'htbp',
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_documents = [
    (master_doc, 'PRISM.tex', html_title,
     author, 'manual'),
]


# -- Options for manual page output ------------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    (master_doc, project, html_title, [author], 1)
]


# -- Options for Texinfo output ----------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
    (master_doc, project, html_title,
     author, project, '"Probabilistic Regression Instrument for Simulating Models"',
     'Miscellaneous'),
]


# -- Extension configuration -------------------------------------------------
