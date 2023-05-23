#!/usr/bin/python3
"""
Flask Web framework
"""
from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_route():
    """Hello route function.
    """
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """Hbnb Function.
    """
    return "HBNB"


if __name__ == "__main__":
    app.run()
