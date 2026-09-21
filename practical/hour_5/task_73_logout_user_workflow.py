"""
PRACTICAL CHALLENGE: User Logout Workflow with Flash Notification (FLASK-H5-P13)
=====================================================
ID: FLASK-H5-P13
Curriculum Tier: Integration | Difficulty: Advanced
Task:
Implement a `/logout` view function that calls `logout_user()`, flashes an `'info'` message, and redirects to `home_page`.

Run this file with Python. Make any necessary changes so all assertion tests pass!
"""

from flask import Flask, flash, redirect, url_for
from flask_login import LoginManager, logout_user

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret'
login_manager = LoginManager(app)
@login_manager.user_loader
def load_user(user_id):
    return None


@app.route('/home')
def home_page():
    return "Home"

@app.route('/logout')
def logout_page():
    return "Logged out"

def test_logout():
    with app.test_client() as client:
        res = client.get('/logout')
        assert res.status_code == 302
        assert res.headers['Location'].endswith('/home')

if __name__ == '__main__':
    test_logout()
    print("✓ Task 73 passed!")
