#!/usr/bin/python3

"""
    A script that starts a Flask web application
"""
from flask import Flask, render_template
from markupsafe import escape

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    # function that return hello
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    # function that return HBNB in the next route
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def cis(text):
    """
    function that return "C" followed by the
    value of the text in the /c/<text> route
    """
    editText = text.replace('_', ' ')
    return f'C {escape(editText)}'


@app.route('/python/<text>', strict_slashes=False)
@app.route('/python/', defaults={'text': 'is_cool'}, strict_slashes=False)
def python(text):
    """
    function that return "Python" followed by the
    value of the text(default->is cool) in the /c/<text> route
    """
    editText = text.replace('_', ' ')
    return f'Python {escape(editText)}'


@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    """
    function that return "n is a number" followed by the
    only if n is integer
    """
    return f'{escape(n)} is a number'


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    """
    function that redirect to templates/5-number.html and display
    Number: n inside body -> h1 tag only if n is integer
    """
    return render_template('5-number.html', number=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def number_template_mod(n):
    """
    function that redirect to templates/5-number.html and display
    Number: n inside body -> h1 tag only if n is integer
    """
    return render_template('6-number_odd_or_even.html', number=n)


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)
