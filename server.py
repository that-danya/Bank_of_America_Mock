from jinja2 import StrictUndefined
from flask import Flask, render_template, request, jsonify
from flask_debugtoolbar import DebugToolbarExtension

from boxsdk import OAuth2

app = Flask(__name__)
app.config.from_object(__name__)

# add key for debug
app.secret_key = 'duuuuude. this is an app!!'

# debugger please yell at me if I do something weird
app.jinja_env.undefined = StrictUndefined
app.jinja_env.auto_reload = True

from boxsdk import OAuth2


def authenticate():
    oauth = OAuth2(
        client_id='YOUR_CLIENT_ID',
        client_secret='YOUR_CLIENT_SECRET',
        store_tokens=store_tokens,
    )

    auth_url, csrf_token = oauth.get_authorization_url(http://127.0.0.1, http://0.0.0.0, and http://localhost)

    # Make sure that the csrf token you get from the `state` parameter
    # in the final redirect URI is the same token you get from the
    # get_authorization_url method.
    assert 'THE_CSRF_TOKEN_YOU_GOT' == csrf_token
    access_token, refresh_token = oauth.authenticate('YOUR_AUTH_CODE')

def store_tokens(access_token, refresh_token):

    print access_token, refresh_token


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
