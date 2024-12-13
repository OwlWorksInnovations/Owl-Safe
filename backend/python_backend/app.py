import flask
from flask import request, jsonify, redirect
import sqlite3
import hashlib
import os
import bcrypt
import jwt
import datetime

app = flask.Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(32)

def connect_to_database(db_name: str = "owlsafe.db") -> sqlite3.Connection:
    try:
        conn = sqlite3.connect(db_name)
        print(f"Opened SQLite database with version {sqlite3.sqlite_version} successfully.")
        return conn
    except sqlite3.OperationalError as e:
        print("Failed to open database:", e)
        return None

def create_users_table_if_not_exists(db_name: str = "owlsafe.db") -> None:
    conn = connect_to_database(db_name)
    if conn is None:
        return

    try:
        with conn:
            # Check if the 'salt' column exists, and if not, add it
            conn.execute(
                """
                CREATE TABLE IF NOT EXISTS users (
                    email TEXT PRIMARY KEY,
                    password TEXT NOT NULL,
                    salt TEXT NOT NULL,
                    app_passwords TEXT
                )
                """
            )
            # If the table already exists, attempt to add the 'salt' column if it doesn't exist
            try:
                conn.execute("ALTER TABLE users ADD COLUMN salt TEXT NOT NULL")
            except sqlite3.OperationalError:
                # 'salt' column already exists, so skip adding it
                pass
    except sqlite3.Error as e:
        print("Failed to create or alter users table:", e)

def insert_data(table: str, data: dict, db_name: str = "owlsafe.db") -> None:
    conn = connect_to_database(db_name)
    if conn is None:
        return

    placeholders = ', '.join('?' * len(data))
    columns = ', '.join(data.keys())
    sql = f"INSERT INTO {table} ({columns}) VALUES ({placeholders})"

    try:
        with conn:
            conn.execute(sql, tuple(data.values()))
            print("Data inserted successfully.")
    except sqlite3.Error as e:
        print("Failed to insert data:", e)
    finally:
        conn.close()

def check_data_in_table(table: str, query: str, params: tuple, db_name: str = "owlsafe.db") -> bool:
    conn = connect_to_database(db_name)
    if conn is None:
        return False

    try:
        with conn:
            cursor = conn.execute(query, params)
            if cursor.fetchone():
                print(f"Data exists in {table} table with query: {query}")
                return True
            else:
                print(f"No data found in {table} table for query: {query}")
                return False
    except sqlite3.Error as e:
        print("Failed to check data:", e)
        return False
    finally:
        conn.close()

@app.route("/")
def index():
    return flask.render_template("index.html")

@app.route("/register")
def register():
    return flask.render_template("register.html")

@app.route("/register-form", methods=["POST"])
def register_form():
    email = flask.request.form["email"]
    password = flask.request.form["password"]

    salt = bcrypt.gensalt()

    hashed_password = bcrypt.hashpw(password.encode(), salt)
    if check_data_in_table("users", "SELECT * FROM users WHERE email = ?", (email,)):
        return flask.redirect("/register-form-error")
    else:
        insert_data("users", {"email": email, "password": hashed_password.decode(), "salt": salt.decode()})
    return flask.redirect("/")

@app.route("/login-form", methods=["POST"])
def login_form():
    token = request.headers.get("Authorization")
    if token:
        try:
            token = token.split(" ")[1]  # Remove "Bearer" prefix
            jwt.decode(token, app.config['SECRET_KEY'], algorithms=["HS256"])
            return flask.redirect("/dashboard")
        except jwt.ExpiredSignatureError:
            return flask.redirect("/login-form-error")

    email = flask.request.form["email"]
    password = flask.request.form["password"]

    if email and password:
        conn = connect_to_database()
        if conn:
            cursor = conn.cursor()
            cursor.execute("SELECT password, salt FROM users WHERE email = ?", (email,))
            user = cursor.fetchone()

            if user:
                stored_password, stored_salt = user
                if bcrypt.checkpw(password.encode(), stored_password.encode()):
                    token = jwt.encode({"sub": email, "app_passwords": ""}, app.config['SECRET_KEY'], algorithm="HS256")
                    response = flask.redirect("/dashboard")
                    response.set_cookie('jwt', token, httponly=True, secure=True)
                    return response
                else:
                    return flask.redirect("/login-form-error")
            else:
                return flask.redirect("/login-form-error")

    return flask.redirect("/login-form-error")


@app.route("/auth", methods=["POST"])
def auth():
    token = request.headers.get("Authorization")
    if token:
        try:
            token = token.split(" ")[1]  # Remove "Bearer" prefix
            decoded = jwt.decode(token, app.config['SECRET_KEY'], algorithms=["HS256"])
            app_passwords = decoded['app_passwords']
            return jsonify({"status": "success", "app_passwords": app_passwords})
        except jwt.ExpiredSignatureError:
            return jsonify({"status": "pending", "message": "Token has expired"})
        except jwt.InvalidTokenError:
            return jsonify({"status": "invalid", "message": "Invalid token"})
    return jsonify({"status": "pending", "message": "Token missing"})

@app.route("/store-app-password", methods=["POST"])
def store_app_password():
    token = request.headers.get("Authorization")
    if token:
        try:
            # Verify the JWT token
            token = token.split(" ")[1]  # Remove "Bearer" prefix
            decoded = jwt.decode(token, app.config['SECRET_KEY'], algorithms=["HS256"])
            
            # Get the email from the decoded token
            email = decoded['sub']
            
            # Get the app password from the request
            app_password = request.json.get('app_password')
            
            if not app_password:
                return jsonify({"status": "error", "message": "No app password provided"}), 400
            
            # Hash the app password
            salt = bcrypt.gensalt()
            hashed_app_password = bcrypt.hashpw(app_password.encode(), salt)
            
            # Update the user's record with the app password
            conn = connect_to_database()
            if conn:
                cursor = conn.cursor()
                cursor.execute(
                    "UPDATE users SET app_passwords = ?, salt = ? WHERE email = ?", 
                    (hashed_app_password.decode(), salt.decode(), email)
                )
                conn.commit()
                conn.close()
                
                return jsonify({"status": "success", "message": "App password stored"}), 200
            
        except jwt.ExpiredSignatureError:
            return jsonify({"status": "error", "message": "Token expired"}), 401
        except jwt.InvalidTokenError:
            return jsonify({"status": "error", "message": "Invalid token"}), 401
    
    return jsonify({"status": "error", "message": "No token provided"}), 401

@app.route("/dashboard")
def dashboard():
    token = request.cookies.get('jwt')
    if token:
        try:
            decoded = jwt.decode(token, app.config['SECRET_KEY'], algorithms=["HS256"])
            email = decoded['sub']
            return f"<h1>Welcome {email}</h1>"
        except jwt.ExpiredSignatureError:
            return "<h1>Token has expired</h1>", 401
        except jwt.InvalidTokenError:
            return "<h1>Invalid token</h1>", 401

    return "<h1>Token missing</h1>", 401

if __name__ == "__main__":
    create_users_table_if_not_exists()
    app.run('0.0.0.0', 5000, debug=True)

