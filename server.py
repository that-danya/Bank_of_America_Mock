import os
from jinja2 import StrictUndefined
from flask import Flask, render_template, request, jsonify, redirect
from flask_debugtoolbar import DebugToolbarExtension

from boxsdk import OAuth2, Client

app = Flask(__name__)
app.config.from_object(__name__)

# add key for debug
app.secret_key = 'duuuuude. this is an app!!'

# debugger please yell at me if I do something weird
app.jinja_env.undefined = StrictUndefined
app.jinja_env.auto_reload = True


def oauth():
    YOUR_CLIENT_ID = os.environ['YOUR_CLIENT_ID']
    YOUR_CLIENT_SECRET = os.environ['YOUR_CLIENT_SECRET']
    YOUR_AUTH_CODE = os.environ['YOUR_AUTH_CODE']


    oauth = OAuth2(
        client_id=YOUR_CLIENT_ID,
        client_secret=YOUR_CLIENT_SECRET,

    )


    auth_url, csrf_token = oauth.get_authorization_url('http://localhost:5000/review_app')
    access_token, refresh_token = oauth.authenticate(YOUR_AUTH_CODE)

    client = Client(oauth)


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


@app.route('/review_app', methods=['GET'])
def review_app():

    return render_template('review.html')


@app.route('/review_app', methods=['POST'])
def get_file():

    filename = request.form['input-b1']
    upload_file(client, filename)

    return redirect('/success')


@app.route('/success')
def success():

    return render_template('success.html')


def upload_file(client, filename):
    root_folder = client.folder(folder_id='0')
    file_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), filename)
    a_file = root_folder.upload(file_path, file_name='i-am-a-file.txt')
    try:
        print('{0} uploaded: '.format(a_file.get()['name']))
    finally:
        print('Delete filename succeeded: {0}'.format(a_file.delete()))



# if running this page, run debugger, load to host
if __name__ == "__main__":

    DebugToolbarExtension(app)
    app.run(debug=True, host="0.0.0.0")
