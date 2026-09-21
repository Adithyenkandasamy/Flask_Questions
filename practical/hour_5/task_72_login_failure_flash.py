"""
PRACTICAL CHALLENGE: Login Failure Flash Notification (FLASK-H5-P12)
=====================================================
ID: FLASK-H5-P12
Curriculum Tier: Integration | Difficulty: Advanced
Task:
When credentials fail authentication, flash the warning message with category `'danger'`.

Run this file with Python. Make any necessary changes so all assertion tests pass!
"""

from flask import Flask, flash, get_flashed_messages

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret'

def handle_login_failure():
    with app.test_request_context():
        return get_flashed_messages(with_categories=True)

if __name__ == '__main__':
    with app.test_request_context():
        handle_login_failure()
        msgs = get_flashed_messages(with_categories=True)
        assert ("danger", "Username and password do not match! Please try again") in msgs
    print("✓ Task 72 passed!")
