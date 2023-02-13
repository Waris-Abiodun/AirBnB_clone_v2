#!/usr/bin/python3

"""Starts a Flask web application.
The application listens on 0.0.0.0, port 5000.
Routes:
    /: Displays 'Hello HBNB!'
       /: Displays 'Hello HBNB!'.
    /hbnb: Displays 'HBNB'.
    /c/<text>: Displays 'C' followed by the value of <text>.
    /python/(<text>): Displays 'Python' followed by the value of <text>.
    /number/<n>: display “n is a number” only if n is an integer
    /number_template/<n>: display a HTML page only if n is an integer
    /number_odd_or_even/<n>: display html page saying whether num is odd|even
"""

from flask import Flask
from markupsafe import escape
from flask import render_template

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hnbn():
    """Display Hello HBNB"""
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hnbn():
    """Display HBNB"""
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def c_some_text(text):
    """Display c with some text"""
    text = text.replace('_', ' ')
    return 'C %s' % escape(text)


@app.route('/python/<text>', strict_slashes=False)
@app.route('/python/', strict_slashes=False, defaults={"text": "is cool"})
def python_some_text(text):
    """Display python with some text"""
    text = text.replace('_', ' ')
    return 'Python %s' % escape(text)


@app.route('/number/<int:n>', strict_slashes=False)
def anumber(n):
    """Display a number"""
    return str(n) + ' is a number'


@app.route('/number_template/<int:n>', strict_slashes=False)
def templat_number(n):
    """Display an HTML page"""
    return render_template('5-number.html', n=n)


@app.route('/number_odd_or_even/<n>', strict_slashes=False)
def odd_even_templat_number(n):
    """Display an HTML page showing when an odd or even number was
    passed
    """
    n = int(n)
    if n % 2 == 1:
        k = 'odd'
    else:
        k = 'even'

    return render_template('6-number_odd_or_even.html', n=n, k=k)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
