from os import path


def setup(app):
    app.add_html_theme('sphinx_fossasia_theme', path.abspath(path.dirname(__file__)))


def get_html_theme_path():
    return path.abspath(path.dirname(path.dirname(__file__)))
