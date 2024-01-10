#!/usr/bin/env python3
'''
flask babel practice
'''
from typing import Union
from flask import Flask, request, render_template, g
from flask_babel import Babel, gettext
import pytz


class Config():
    '''configfor babel instance'''
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_TIMEZONE  = 'UTC'
    BABEL_DEFAULT_LOCALE = 'en'

users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}

app = Flask(__name__)

app.config.from_object(Config)


babel = Babel(app)

def get_user()->Union[dict, None] :
    '''mocking user db'''
    user_id = request.args.get('login_as')
    if user_id and user_id in users.keys():
        return users[int(user_id)]
    return None
    
@babel.localeselector
def get_locale():
    '''locale getter'''
    locale = request.args.get('locale')
    if locale and locale in Config.LANGUAGES:
        return locale
    if g.user:
        locale = g.user.get("locale")
        if locale and locale in app.config['LANGUAGES']:
            return locale

    locale = request.headers.get('locale')
    if locale and locale in app.config['LANGUAGES']:
        return locale

    return request.accept_languages.best_match(app.config['LANGUAGES'])



@app.before_request
def before_request()->Union[dict, None] :
    user = get_user()
    g.user = user

@app.route('/', methods=['GET'], strict_slashes=False)
def index():
    '''index render'''
    return render_template('6-index.html')




if __name__ == '__main__':
    app.run('0.0.0.0', 5000, debug=True)