from flask import Flask, render_template, request, redirect, url_for
import json
import os
from password_manager import PasswordManager

app = Flask(__name__)
USERS_FILE = "users.json"

password_manager = PasswordManager()

def load_users():
    if not os.path.exists(USERS_FILE):
        return {}
    with open(USERS_FILE, "r") as f:
        return json.load(f)


def save_users(users):
    with open(USERS_FILE, "w") as f:
        json.dump(users, f, indent=4)


def is_valid_username(username: str) -> bool:
    return (
        3 <= len(username) <= 20
        and username.isalnum()  # only letters + numbers
    )


@app.route("/")
def start():
    return redirect(url_for("login"))
@app.route("/login", methods=["GET", "POST"])
def login():
    #Post method keeps password info in hidden, get would put in url
    if request.method == "POST":
        username = request.form.get("username", "").strip()
        password = request.form.get("password", "")
        users = load_users()
        stored_hash = users.get(username)
        
        if stored_hash and password_manager.verify_password(password, stored_hash):
            return redirect(url_for("home"))
        #login worked
        #under login fail
        else:
            return render_template("login.html", error = "Invalid Login Credentials")
        
    return render_template("login.html")

@app.route("/create_account", methods=["GET", "POST"])
def create_account():
    if request.method == "POST":
        username = request.form.get("username", "").strip()
        password = request.form.get("password", "")
        print("RAW PASSWORD:", repr(password))

        users = load_users()
        #invalid user
        if not is_valid_username(username):
            return render_template("create_account.html", error=" Username must be 3–20 characters, letters and numbers only.")
        #username taken
        if username in users:
            return render_template("create_account.html", error="That username is already taken.")
        
        password = password[:72] # Limit password length for hashing
        
        password_hash = password_manager.hash_password(password)
        users[username] = password_hash
        save_users(users)
        return redirect(url_for("login"))

    return render_template("create_account.html")

@app.route("/home")
def home():
    return render_template('home.html')
@app.route("/store-achievement")
def store_achievement():
    return "Store Achievement"
@app.route("/current-achievements")
def current_achievements():
    return "Current Achievements"
@app.route("/set-goal")
def set_goal():
    return "Set Goal"

if __name__=="__main__":
    app.run(debug=True)
