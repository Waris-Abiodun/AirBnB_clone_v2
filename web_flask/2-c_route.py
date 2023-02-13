#!/usr/bin/python3

"""Starts a Flask web application.
The application listens on 0.0.0.0, port 5000.
Routes:
    /: Displays 'Hello HBNB!'
"""

from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hnbn():
    """Display Hello HBNB"""
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hnbn():
    """Display HBNB"""
    return 'HBNB'


@app.route('/c/<username>', strict_slashes=False)
def c_some_text(username):
    """Display c with some text"""
    return 'C %s' % escape(username)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
