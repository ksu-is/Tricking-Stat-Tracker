import json
import os
from password_manager import PasswordManager

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
        and username.isalnum()     # only letters + numbers
    )


def register_user():
    users = load_users()

    username = input("Choose a username: ").strip()

    if not is_valid_username(username):
        print("Username must be 3–20 characters, letters and numbers only.")
        return

    if username in users:
        print("That username is already taken.")
        return

    password = input("Choose a password: ").strip()

    password_hash = password_manager.hash_password(password)
    users[username] = password_hash

    save_users(users)
    print(f"User '{username}' created successfully.")