import flask
import os
import sqlite3

app = flask.Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(512)

connection = sqlite3.connect('owlsafe.db')

connection.execute(''' CREATE TABLE users
         (FIND INT PRIMARY KEY NOT NULL,
         email TEXT NOT NULL,
         password INT NOT NULL,
         ''')

@app.route("/")
def index():
    return flask.render_template("index.html")

@app.route("/register")
def register():
    pass


if __name__ == "__main__":
    app.run('0.0.0.0', 5000, debug=True)