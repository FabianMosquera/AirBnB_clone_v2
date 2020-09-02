#!/usr/bin/python3
"""Flask"""
from flask import Flask, render_template
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


@app.route('/number/<int:n>', strict_slashes=False)
def num(n):
    """display “n is a number” only if n is an integer
    """
    return "%d is a number" % n


@app.route('/number_template/<int:n>', strict_slashes=False)
def num_template(n):
    """ Function that receives a number argument and render the template
    """
    return render_template('5-number.html', number=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def number_odd_even(n):
    """  Function that receives a number argument, render a template and
    a conditional
    """
    return render_template('6-number_odd_or_even.html', number=n)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
