import json
import os
from flask import Flask, render_template, request, redirect, url_for
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
PASSWORD_FILE = os.path.join(BASE_DIR, "PASSWORD.json")
app = Flask(__name__)
PASSWORD = {}
if os.path.exists(PASSWORD_FILE):
          with open(PASSWORD_FILE, "r") as f:
           PASSWORD = json.load(f)
@app.route("/")
def login():
    return render_template("login.html")
@app.route("/login", methods=["POST"])
def check_login():
    password = request.form["password"]
    for user, passwrd in PASSWORD.items():
        if password == passwrd:
            return redirect(url_for("home"))
    return render_template(
        "login.html",
        message1="Your Password Not Found in my Database. Please Sign Up First."
    )
@app.route("/signup")
def signup():
    return render_template("signup.html")
@app.route("/register", methods=["POST"])
def register():
    username = request.form["name"]
    password = request.form["pass"]
    PASSWORD[username] = password
    with open(PASSWORD_FILE, "w") as f:
            json.dump(PASSWORD, f,indent=4)
    return render_template(
        "login.html",
        message2="Account Created Successfully. Please Login."
    )
@app.route("/home")
def home():
    return render_template("home.html")
if __name__ == "__main__":
    app.run(debug=True)