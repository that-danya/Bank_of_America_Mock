from flask import Flask, render_template
from jinja2 import StrictUndefined

app = Flask(__name__)
app.config.from_object(__name__)

# add key for debug
app.secret_key = 'BOA Portal Demo'

# debugger please yell at me if I do something weird
app.jinja_env.undefined = StrictUndefined
app.jinja_env.auto_reload = True


#landing page
@app.route('/')
def index():
    """Homepage with logon portal."""

    return render_template('homepage.html')


@app.route()
def loan_application():
    """Show loan application with uploading capability."""

    return render_template('loan_app.html')


#####################################

if __name__ == "__main__":
    app.run(debug=True)
