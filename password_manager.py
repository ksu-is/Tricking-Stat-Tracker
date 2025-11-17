from passlib.context import CryptContext

# Create a global CryptContext for password hashing
pwd_context = CryptContext(
    schemes=["bcrypt"],     # hashing algorithm
    deprecated="auto"
)

class PasswordManager:
    """Hash and verify user passwords using passlib."""

    def hash_password(self, password: str) -> str:
        """Return a hashed version of the plaintext password."""
        return pwd_context.hash(password)

    def verify_password(self, password: str, password_hash: str) -> bool:
        """Return True if the password matches the stored hash."""
        return pwd_context.verify(password, password_hash)