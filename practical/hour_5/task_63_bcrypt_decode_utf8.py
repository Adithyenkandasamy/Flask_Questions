"""
PRACTICAL CHALLENGE: Bcrypt Hash String Decoding (FLASK-H5-P03)
=====================================================
ID: FLASK-H5-P03
Curriculum Tier: Integration | Difficulty: Advanced
Task:
Generate a Bcrypt password hash and decode it to a UTF-8 string before storing it in the database column.

Run this file with Python. Make any necessary changes so all assertion tests pass!
"""

from flask import Flask
from flask_bcrypt import Bcrypt

app = Flask(__name__)
bcrypt = Bcrypt(app)

def create_hash(password: str):
    return bcrypt.generate_password_hash(password)

if __name__ == '__main__':
    hashed = create_hash("password123")
    assert isinstance(hashed, str), "Hash must be a string, not bytes"
    print("✓ Task 63 passed!")
