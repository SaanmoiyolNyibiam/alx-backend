#!/usr/bin/env python3
"""
This is a module that defines a simple flask application
"""
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    """
    This is a function that returns the index page of the application
    """
    return render_template("0-index.html")


if __name__ == "__main__":
    app.run()
