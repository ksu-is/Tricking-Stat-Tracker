from passlib.context import CryptContext

# Create a global CryptContext for password hashing
pwd_context = CryptContext(
    schemes=["bcrypt"],     # hashing algorithm
    deprecated="auto"
)

class PasswordManager:
    def __init__(self):
        self.context = pwd_context

    """Hash and verify user passwords using passlib."""

    def hash_password(self, password: str) -> str:
        """Return a hashed version of the plaintext password."""
        password = password[:72]  # bcrypt limit
        return self.context.hash(password)

    def verify_password(self, password: str, password_hash: str) -> bool:
        """Return True if the password matches the stored hash."""
        password = password[:72]  # bcrypt limit
        return self.context.verify(password, password_hash)
    
    from passlib.context import CryptContext

pwd_context = CryptContext(
    schemes=["bcrypt"],
    deprecated="auto"
)
