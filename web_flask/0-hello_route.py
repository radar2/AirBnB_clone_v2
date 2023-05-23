#!/usr/bin/python3
"""Flask"""
from flask import Flask, request
app = Flask(__name__)

@app.route('/', strict_slashes=False)
def hello_route():
    """hello route"""
    return "Hello HBNB!"

if __name__ == "__main__":
    app.run()
