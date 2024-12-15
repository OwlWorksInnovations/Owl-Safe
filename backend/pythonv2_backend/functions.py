import flask
from flask import request
import time

def is_loggedin(loggedin, current_user_session_expired = []):
    # Checks if user is logged in
    if loggedin:
        # Gets user email
        loggedin_user = flask.request.cookies.get('email')

        # Checks if user session has expired
        for session in current_user_session_expired:
            if session == loggedin_user:
                # If the user session has expired, sets the variable to false
                loggedin = False
                break

        # If user session is not expired it sets the variable to true
        if loggedin:
            loggedin = True

    else:
        # If user is initially not logged in it redirects to login
        loggedin = False

    return loggedin
    
def start_session(loggedin_user, current_user_session = []):
    # Starts user session
    if loggedin_user:
        flask.session['user'] = loggedin_user
        current_user_session.append(loggedin_user)
        time_start = time.time()
        time_limit = 60 * 60
        time.sleep(time_limit - (time.time() - time_start))
        expire_session(current_user_session)

def expire_session(current_user_session = []):
    # Expires user session
    current_user_session_expired = []
    current_user_session.remove(flask.session['user'])
    current_user_session_expired.append(flask.session['user'])
    flask.session.clear()
