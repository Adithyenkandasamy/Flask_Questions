"""
PRACTICAL CHALLENGE: Initializing Flask-Bcrypt Extension (FLASK-H5-P01)
=====================================================
ID: FLASK-H5-P01
Curriculum Tier: Integration | Difficulty: Advanced
Task:
Initialize the `Bcrypt` extension instance with the Flask application.

Run this file with Python. Make any necessary changes so all assertion tests pass!
"""

from flask import Flask
from flask_bcrypt import Bcrypt

app = Flask(__name__)
bcrypt = None

def test_bcrypt():
    assert bcrypt is not None, "Bcrypt must be initialized"
    assert hasattr(bcrypt, 'generate_password_hash')

if __name__ == '__main__':
    test_bcrypt()
    print("✓ Task 61 passed!")
