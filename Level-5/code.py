import binascii
import random
import secrets
import hashlib
import os
import bcrypt


class Random_generator:
    # generates a random token
    def generate_token(
        self,
        length=8,
        alphabet=(
            "0123456789" "abcdefghijklmnopqrstuvwxyz" "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        ),
    ):
        return "".join(secrets.choice(alphabet) for i in range(length))

    # generates salt
    def generate_salt(self):
        return bcrypt.gensalt(random.randint(4, 31))


class SHA256_hasher:
    # produces the password hash by combining password + salt because hashing
    def password_hash(self, password, salt):
        password = binascii.hexlify(hashlib.sha256(password.encode()).digest())
        password_hash = bcrypt.hashpw(password, salt)
        return password_hash.decode("ascii")

    # verifies that the hashed password reverses to the plain text version on verification
    def password_verification(self, password, password_hash):
        password = binascii.hexlify(hashlib.sha256(password.encode()).digest())
        password_hash = password_hash.encode("ascii")
        return bcrypt.checkpw(password, password_hash)


# a collection of sensitive secrets necessary for the software to operate
PRIVATE_KEY = os.environ.get("PRIVATE_KEY")
PUBLIC_KEY = os.environ.get("PUBLIC_KEY")
SECRET_KEY = "TjWnZr4u7x!A%D*G-KaPdSgVkXp2s5v8"
PASSWORD_HASHER = "SHA256_hasher"
