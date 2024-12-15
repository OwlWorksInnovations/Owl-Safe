import flask
import requests
from oauthlib.oauth2 import WebApplicationClient
import os
import sqlite3
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import Flow
from googleapiclient.discovery import build
from functions import is_loggedin, start_session

# GLOBAL VARIABLES
loggedin = False
current_user_session = []
current_user_session_expired = []

# Flask Things
app = flask.Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(512)
app.config['PREFERRED_URL_SCHEME'] = 'https'

# Google OAuth stuff
GOOGLE_CLIENT_ID = "client_id.txt"
GOOGLE_CLIENT_SECRET = "client_secret.json"
GOOGLE_SCOPES = [
    "https://www.googleapis.com/auth/userinfo.email",
    "openid"
]


def get_google_auth_flow(CLIENT_SECRETS_FILE, SCOPES):
    # Creates Google OAuth flow
    flow = Flow.from_client_secrets_file(
        CLIENT_SECRETS_FILE,
        scopes=SCOPES,
        redirect_uri=flask.url_for('oauth_callback', _external=True, _scheme='https')
    )
    return flow

# Main page
@app.route("/")
def index():
    # Checks if user is logged in, when logged in it displays the user's email on the index page
    global loggedin
    loggedin = is_loggedin(loggedin, current_user_session_expired)

    if loggedin:
        loggedin_user = flask.request.cookies.get('email')
        return flask.render_template("index.html", loggedin_user=loggedin_user)
    else:
        return flask.render_template("index.html")
    
@app.route("/dashboard")
def dashboard():
    # Checks if user is loggedin, when logged in it displays the dashboard else it redirects to login page
    global loggedin
    loggedin = is_loggedin(loggedin, current_user_session_expired)

    if loggedin:
        return flask.render_template("dashboard.html")
    else:
        return flask.redirect("/login")

@app.route("/login")
def login():
    global loggedin
    loggedin = is_loggedin(loggedin, current_user_session_expired)

    if loggedin:
        return flask.redirect("/dashboard")
    else:
        # Google OAuth login
        flow = get_google_auth_flow(GOOGLE_CLIENT_SECRET, GOOGLE_SCOPES)
        authorization_url, state = flow.authorization_url()
        return flask.redirect(authorization_url)

@app.route("/logout")
def logout():
    global loggedin
    loggedin = False
    flask.session.clear()
    return flask.redirect("/")

@app.route("/oauth_callback")
def oauth_callback():
    flow = get_google_auth_flow(GOOGLE_CLIENT_SECRET, GOOGLE_SCOPES)
    authorization_response = flask.request.url.replace("http://", "https://")
    flow.fetch_token(authorization_response=authorization_response)
    credentials = flow.credentials
    start_session(credentials, current_user_session)
    return flask.redirect("/dashboard")

if __name__ == "__main__":
    app.run('0.0.0.0', 5000, debug=True)


