#!/usr/bin/python3
"""Flask"""
from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_route():
    """Hello Flask!
    """
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """ Display a custom message
    """
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c_text(text):
    """replace underscore _ symbols with a space
    """
    return 'C %s' % text.replace('_', ' ')


@app.route('/python/', defaults={'text': "is_cool"})
@app.route('/python/<text>', strict_slashes=False)
def python_text(text):
    """replace underscore _ symbols with a space
    """
    return 'Python %s' % text.replace('_', ' ')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
