Sphinx Phimpme Theme
=====================

.. image:: https://travis-ci.org/fossasia/sphinx_phimpme_theme.svg?branch=master
    :target: https://travis-ci.org/fossasia/sphinx_phimpme_theme

Official bootstrap based Sphinx theme for FOSSASIA

Installation
------------

Download the package or add it to your `requirements.txt`

::

    pip install sphinx_phimpme_theme

In your conf.py file:

::

    html_theme = "sphinx_phimpme_theme"

Configuration
-------------

You can define the theme's project-wide configuration via `html_theme_options`. For example

.. code:: python

   html_theme_options = {
       'show_fossasia_logo': 'true',
       'link_about': '/about',
   }

Following is a list of all available options:

- *link_about*
- *link_docs*
- *link_blog*
- *link_donate*
- *link_contact*
- *link_twitter*
- *link_facebook*
- *show_fossasia_logo*
