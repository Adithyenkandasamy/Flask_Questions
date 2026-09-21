"""
PRACTICAL CHALLENGE: Category-Based Flash Messages (FLASK-H4-P10)
=====================================================
ID: FLASK-H4-P10
Curriculum Tier: Advanced | Difficulty: Advanced
Task:
Flash user messages with appropriate categories (e.g. 'danger' for errors and 'success' for confirmations).

Run this file with Python. Make any necessary changes so all assertion tests pass!
"""

from flask import Flask, flash, get_flashed_messages

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret'

def send_alert(message: str, category: str):
    with app.test_request_context():
        flash(message)
        return get_flashed_messages(with_categories=True)

if __name__ == '__main__':
    messages = send_alert("Invalid username", "danger")
    assert messages == [("danger", "Invalid username")]
    print("✓ Task 55 passed!")
