#!/usr/bin/python3

"""Starts a Flask web application.
The application listens on 0.0.0.0, port 5000.
Routes:
    /: Displays 'Hello HBNB!'
"""

from flask import Flask
from markupsafe import escape

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


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
