from flask import Flask, session, redirect, url_for, escape, request
import requests
import redis
from minilib import *

s = session
config = {
    "login_endpoint": "https://localhost:4747/"
}

app = Flask(__name__)
app.secret_key = "change me pls"


@app.route('/')
def index():
    if 'username' in session:
        return "ok login" + str(session['username']) + str(session['uuid']) 
    else:
        return "not logged"


@app.route("/set")
def set():
    session['username'] = '_'
    return redirect(url_for('index'))


@app.route("/login", methods=['POST'])
def login():
    req = requests.post(config["login_endpoint"], request.form['username'], request.form['password'],  # HERE SET 3 SEC DEADLINE)

    if req.text == "user" or "poweruser":
        session['username'] = 'non zero'; session['userlevel'] = req.text
    else:  # bad login

        @
    requires_roles("user"):

    def post():

    # get

    # validate

    # add


    if __name__ == '__main__':
        app.run(debug=True)
