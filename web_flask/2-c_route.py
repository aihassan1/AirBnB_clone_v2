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
    """Return a hello + text"""
    text = text.replace("_", " ")

    return f"C {text}"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
