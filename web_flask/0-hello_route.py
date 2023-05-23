#!/usr/bin/python3
"""
Flask - Web Framework
"""
from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_route():
    """Hello route function.
    """
    return "Hello HBNB!"


if __name__ == "__main__":
    print(hello_route.__doc__)
    app.run()
