import flask
import os

app = flask.Flask(__name__)
app.secret_key = os.urandom(32)

@app.route("/")
def index():
    return flask.render_template("index.html")

@app.route("/dashboard")
def dashboard():
    return flask.render_template("dashboard.html")

@app.route("/download")
def download():
    return flask.render_template("download.html")

if __name__ == "__main__":
    app.run(debug=True)