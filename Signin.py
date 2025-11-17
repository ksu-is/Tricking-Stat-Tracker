from password_manager import PasswordManager

password_manager = PasswordManager()

# When creating a user:
plain_password = "my_secret"
hashed = password_manager.hash_password(plain_password)
# store `hashed` in your database/file, NOT the plain password

# When logging in:
is_valid = password_manager.verify_password("my_secret", hashed)
if is_valid:
    print("Password correct, log them in")
else:
    print("Wrong password")