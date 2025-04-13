# -*- coding: utf-8 -*-
# used for SPHINX documentation 
import sys, os

sys.path.insert(0, os.path.abspath('extensions'))
sys.path.insert(0, os.path.abspath('../src/'))

extensions = [ 'sphinx.ext.autodoc', 
               'sphinx.ext.doctest', 
               'sphinx.ext.todo',
               'sphinx.ext.coverage', 
               'sphinx.ext.ifconfig',
               "sphinx_copybutton",
          ]

todo_include_todos = True
templates_path = ['_templates']
source_suffix = '.rst'
master_doc = 'index'
exclude_patterns = []
add_function_parentheses = True
#add_module_names = True
# A list of ignored prefixes for module index sorting.
#modindex_common_prefix = []

project = u'FIS Test System'
copyright = u'2024-07-01, STAMA-QA, Manfred Gross - Andreas Häberle '

version = 'v2024.0.x'
release = 'v2024.0.x'
# -- Multilanguage  ------------------------------------------------------------

locale_dirs = ['locale/']   # path is example but recommended
gettext_compact = False     # optional

# -- Options for HTML output ---------------------------------------------------


html_theme_path = ['themes']
# html_theme =  "haiku" # 'book'
html_theme = "sphinx_rtd_theme"
html_title = "FisTs"
#html_short_title = None
#html_logo = None
#html_favicon = None
html_static_path = ['_static']
html_css_files = ["custom.css"]
html_domain_indices = False
html_use_index = False
html_show_sphinx = False
htmlhelp_basename = 'fists'
html_show_sourcelink = False

# TODO: needs codeexample extension
code_example_dir = "../example"
code_add_python_path = ["../examples", "../src"]


################################################################################


def setup(app):
     from sphinx.util.texescape import tex_replacements
     tex_replacements += [(u'♮', u'$\\natural$'),
                          (u'ē', u'\=e'),
                          (u'♩', u'\quarternote'),
                          (u'↑', u'$\\uparrow$'),
                          ]