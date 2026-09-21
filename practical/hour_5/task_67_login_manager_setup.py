"""
PRACTICAL CHALLENGE: Configuring Flask-Login LoginManager (FLASK-H5-P07)
=====================================================
ID: FLASK-H5-P07
Curriculum Tier: Integration | Difficulty: Advanced
Task:
Configure `LoginManager` on the Flask application, setting `login_view` to 'login_page' and `login_message_category` to 'info'.

Run this file with Python. Make any necessary changes so all assertion tests pass!
"""

from flask import Flask
from flask_login import LoginManager

app = Flask(__name__)
login_manager = LoginManager(app)

if __name__ == '__main__':
    assert login_manager.login_view == 'login_page'
    assert login_manager.login_message_category == 'info'
    print("✓ Task 67 passed!")
