#!/usr/bin/python3
"""This script defines a basic Flask application with a single route."""

from flask import Flask, render_template

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


@app.route("/python/<text>", strict_slashes=False)
def python_is_cool(text):
    """returns python + text"""
    text = text.replace("_", " ")
    return f"Python {text}"


@app.route("/python", strict_slashes=False)
def python_default():
    """returns default python message"""
    return "Python is cool"


@app.route("/number/<int:n>", strict_slashes=False)
def number(n):
    """returns a number if it is an int"""
    return f"{n} is a number"


@app.route("/number_template/<int:n>", strict_slashes=False)
def number_template(n):
    """returns a template for a number if it is an int"""
    return render_template("5-number.html", n=n)


@app.route("/number_odd_or_even/<int:n>")
def odd_or_even(n):
    """returns a template for a number if it is an int odd or even"""
    return render_template("6-number_odd_or_even.html", n=n)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
