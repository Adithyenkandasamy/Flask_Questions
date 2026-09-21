"""
PRACTICAL CHALLENGE: Password Hashing Property and Setter (FLASK-H5-P02)
=====================================================
ID: FLASK-H5-P02
Curriculum Tier: Integration | Difficulty: Advanced
Task:
Implement a `@property` and `@password.setter` on the User model that generates and stores a Bcrypt password hash.

Run this file with Python. Make any necessary changes so all assertion tests pass!
"""

from flask import Flask
from flask_bcrypt import Bcrypt

app = Flask(__name__)
bcrypt = Bcrypt(app)

class User:
    def __init__(self):
        self.password_hash = None

    def set_password(self, text):
        self.password_hash = text

if __name__ == '__main__':
    u = User()
    u.password = "secret123"
    assert u.password_hash != "secret123"
    assert bcrypt.check_password_hash(u.password_hash, "secret123")
    print("✓ Task 62 passed!")
