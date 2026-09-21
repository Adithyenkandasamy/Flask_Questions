"""
PRACTICAL CHALLENGE: Protecting Sensitive Routes with @login_required (FLASK-H5-P10)
=====================================================
ID: FLASK-H5-P10
Curriculum Tier: Integration | Difficulty: Advanced
Task:
Protect the `/market` route with Flask-Login's `@login_required` decorator to restrict access to authenticated users.

Run this file with Python. Make any necessary changes so all assertion tests pass!
"""

from flask import Flask
from flask_login import LoginManager

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret'
login_manager = LoginManager(app)
login_manager.login_view = 'login_page'

@login_manager.user_loader
def load_user(user_id):
    return None

@app.route("/login")
def login_page():
    return "Login Page"

@app.route("/market")
def market_page():
    return "Market Content"

def test_protection():
    with app.test_client() as client:
        res = client.get('/market')
        assert res.status_code == 302, f"Expected 302 redirect, got {res.status_code}"

if __name__ == '__main__':
    test_protection()
    print("✓ Task 70 passed!")
