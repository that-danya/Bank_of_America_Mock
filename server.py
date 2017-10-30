from flask import Flask

app = Flask(__name__)
app.config.from_object(__name__)

# add key for debug
app.secret_key = 'BOA Portal Demo'

# debugger please yell at me if I do something weird
app.jinja_env.undefined = StrictUndefined
app.jinja_env.auto_reload = True




#####################################

if __name__ == "__main__":
    app.run(debug=True)
