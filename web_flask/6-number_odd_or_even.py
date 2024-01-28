#!/usr/bin/python3
"""
Starts a Flask web application
"""

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def index():
    """Route that displays 'Hello HBNB!'"""
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """Route that displays 'HBNB'"""
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def c_route(text):
    """Route that displays 'C ' followed by the value of the text"""
    return 'C ' + text.replace('_', ' ')


@app.route('/python/', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_route(text):
    """Route that displays 'Python ' followed by the value of the text"""
    return 'Python ' + text.replace('_', ' ')


@app.route('/number/<int:n>', strict_slashes=False)
def number_route(n):
    """Route that displays 'n is a number' only if n is an integer"""
    return "{:d} is a number".format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template_route(n):
    """Route that displays an HTML page only if n is an integer"""
    return render_template('6-number_template.html', n=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def number_odd_or_even_route(n):
    """page only if n is an integer, indicating if it's even or odd"""
    return render_template('6-number_odd_or_even.html', n=n)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
