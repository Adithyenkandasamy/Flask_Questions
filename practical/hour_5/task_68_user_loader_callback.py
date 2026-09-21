"""
PRACTICAL CHALLENGE: Flask-Login User Loader Callback (FLASK-H5-P08)
=====================================================
ID: FLASK-H5-P08
Curriculum Tier: Integration | Difficulty: Advanced
Task:
Implement the `@login_manager.user_loader` callback to fetch and return a user instance by its integer ID.

Run this file with Python. Make any necessary changes so all assertion tests pass!
"""

from flask import Flask
from flask_login import LoginManager

app = Flask(__name__)
login_manager = LoginManager(app)

users_db = {1: "Alice", 2: "Bob"}

def load_user(user_id):
    return users_db.get(user_id)

if __name__ == '__main__':
    fn = login_manager._user_callback
    assert fn is not None, "user_loader decorator must be applied"
    assert fn("1") == "Alice", "user_loader must cast user_id to int"
    print("✓ Task 68 passed!")
