#!/usr/bin/python3
"""
Flask - Web Framework
"""
from flask import Flask

app = Flask(__name__)


@app.route('/', strick_slashes=False)
def hello_route():
    """hello route function
    """
    return "Hello HBNB!"


if __name__ == "__main__":
    app.run()
