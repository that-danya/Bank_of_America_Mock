from jinja2 import StrictUndefined
from flask import Flask, render_template, request, jsonify
from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)
app.config.from_object(__name__)

# add key for debug
app.secret_key = 'duuuuude. this is an app!!'

# debugger please yell at me if I do something weird
app.jinja_env.undefined = StrictUndefined
app.jinja_env.auto_reload = True


@app.route('/')
def index():
    """Auto loan application start page."""

    return render_template('loan_app.html')


@app.route('/signin')
def loan_application():
    """Sign in."""

    return render_template('signin.html')


@app.route('/review_app')
def review_app():

    return render_template('review.html')


# if running this page, run debugger, load to host
if __name__ == "__main__":

    DebugToolbarExtension(app)
    app.run(debug=True, host="0.0.0.0")
