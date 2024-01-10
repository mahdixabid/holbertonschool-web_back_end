#!/usr/bin/env python3
""""
flask babel practice
"""
from flask import Flask, request, render_template
from flask_babel import Babel, gettext
from typing import Union


class Config():
    """configfor babel instance"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_TIMEZONE = 'UTC'
    BABEL_DEFAULT_LOCALE = 'en'


app = Flask(__name__)

app.config.from_object(Config)


babel = Babel(app)


@babel.localeselector
def get_lcoale() -> Union[dict, None]:
    """locale getter
        that gets params from config class
        in this file"""
    try:
        locale = request.args.get('locale')
    except Exception:
        pass
    if locale and locale in Config.LANGUAGES:
        return locale
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/', methods=['GET'], strict_slashes=False)
def index() -> str:
    """index render template"""
    return render_template('1-index.html')


if __name__ == '__main__':
    app.run('0.0.0.0', 5000)
