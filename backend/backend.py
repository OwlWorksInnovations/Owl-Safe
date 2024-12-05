import flask, flask_login
from flask import request
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user
import sqlite3
from werkzeug.security import generate_password_hash, check_password_hash

app = flask.Flask(__name__)
app.secret_key = "super secret key"
app.static_folder = 'static'
login_manager = LoginManager()
login_manager.init_app(app)

def get_db():
    if not hasattr(flask.g, 'db'):
        flask.g.db = sqlite3.connect('db.db')
        with flask.g.db:
            cursor = flask.g.db.cursor()
            cursor.execute("CREATE TABLE IF NOT EXISTS users (username TEXT PRIMARY KEY, password TEXT)")
            cursor.execute("CREATE TABLE IF NOT EXISTS passwords (username TEXT, identifier TEXT, password TEXT, FOREIGN KEY (username) REFERENCES users(username))")
    return flask.g.db

class User(UserMixin):
    def __init__(self, username):
        self.id = username

@login_manager.user_loader
def load_user(user_id):
    cursor = get_db().cursor()
    cursor.execute("SELECT * FROM users WHERE username = ?", (user_id,))
    user_data = cursor.fetchone()
    if user_data:
        return User(user_data[0])
    return None

@app.route("/")
def index():
    if flask_login.current_user.is_authenticated:
        return flask.render_template("index.html", user=flask_login.current_user.id)
    return flask.render_template("index.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    next_url = flask.request.args.get("next")
    if flask.request.method == "GET":
        return flask.render_template("login.html", next=next_url)
    else:
        username = flask.request.form["username"]
        password = flask.request.form["password"]
        cursor = get_db().cursor()
        cursor.execute("SELECT * FROM users WHERE username = ?", (username,))
        user_data = cursor.fetchone()
        if user_data and check_password_hash(user_data[1], password):
            user = load_user(username)
            login_user(user)
            return flask.redirect(next_url or "/")
        else:
            return flask.render_template("login.html", error="Invalid username or password", next=next_url)

@app.route("/register", methods=["GET", "POST"])
def register():
    if flask.request.method == "GET":
        return flask.render_template("register.html")
    else:
        username = flask.request.form["username"]
        password = flask.request.form["password"]
        cursor = get_db().cursor()

        cursor.execute("SELECT * FROM users WHERE username = ?", (username,))
        if cursor.fetchone():
            return flask.render_template("register.html", error="Username already exists")

        hashed_password = generate_password_hash(password)
        cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, hashed_password))
        get_db().commit()

        user = load_user(username)
        login_user(user)
        return flask.redirect("/")

@app.route("/logout")
def logout():
    logout_user()
    return flask.redirect("/")

@app.route("/authorize", methods=["POST"])
@login_required
def authorize():
    identifier = flask.request.form["identifier"]
    password = flask.request.form["password"]
    hashed_password = generate_password_hash(password)
    username = flask_login.current_user.id

    cursor = get_db().cursor()
    cursor.execute("INSERT INTO passwords (username, identifier, password) VALUES (?, ?, ?)", (username, identifier, hashed_password))
    get_db().commit()

    return flask.jsonify({"message": "Password saved successfully"})

@app.route('/authorize', methods=['POST'])
def authorize_not_logged_in():
    if not flask.login.current_user.is_authenticated:
        return flask.redirect(flask.url_for('login'))

if __name__ == "__main__":
    app.run(debug=True)


