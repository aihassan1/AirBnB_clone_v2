#!/usr/bin/python3
"""This script defines a basic Flask application with a single route."""

from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello():
    """Return a greeting message."""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def HBNB():
    """Return a HBNB"""
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c_is_fun(text):
    """Return a C + text"""
    text = text.replace("_", " ")

    return f"C {text}"


@app.route("/python/<text>")
def python_is_cool(text="is cool", strict_slashes=False):
    """returns python + text"""
    text = text.replace("_", " ")
    return f"Python {text}"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
