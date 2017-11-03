from jinja2 import StrictUndefined
from flask import Flask, render_template, request, flash, redirect, session, jsonify
from flask_debugtoolbar import DebugToolbarExtension

import os
import re

app = Flask(__name__)
app.config.from_object(__name__)

# add key for debug
app.secret_key = 'duuuuude. this is an app!!'

# debugger please yell at me if I do something weird
app.jinja_env.undefined = StrictUndefined
app.jinja_env.auto_reload = True


@app.route('/')
def index():
    """Homepage with logon portal."""

    return render_template('homepage.html')


@app.route('/application')
def loan_application():
    """Show loan application with uploading capability."""

    return render_template('loan_app.html')


# if running this page, run debugger, load to host
if __name__ == "__main__":

    DebugToolbarExtension(app)
    app.run(debug=True, host="0.0.0.0")
