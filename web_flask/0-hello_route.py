#!/usr/bin/python3
"""Flask"""
from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_route():
    """hello route"""
    return "Hello HBNB!"


if __name__ == "__main__":
    app.run()
