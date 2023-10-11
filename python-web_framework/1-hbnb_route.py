#!/usr/bin/python3
"""
    A script that starts a Flask web application
"""

from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    # function that return hello
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    # function that return HBNB in the next route
    return "HBNB"


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)
