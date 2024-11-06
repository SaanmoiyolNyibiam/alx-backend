#!/usr/bin/env python3
"""
This is a module that basically sets up babel
"""
from flask import Flask, render_template, request
from flask_babel import Babel

app = Flask(__name__)


class Config():
    """
    Holds configuration values for the
    flask application
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


# applies the configuration to the flask instance
app.config.from_object(Config)
# intializes babel with the configuration values set in the config class
babel = Babel(app)


@babel.localeselector
def get_locale():
    """determines the best match between the list of available languages"""
    locale = request.args.get('locale')
    if locale in app.config['LANGUAGES']:
        return locale
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route("/")
def index():
    """
    This is a function that returns the index page of the application
    """
    return render_template("4-index.html")


if __name__ == "__main__":
    app.run()
