"""
PRACTICAL CHALLENGE: Static Asset Linking with url_for (FLASK-H2-P11)
=====================================================
ID: FLASK-H2-P11
Curriculum Tier: Basic Application | Difficulty: Elementary
Task:
Generate a relative URL to the static file 'css/main.css' using Flask's `url_for('static', filename='...')`.

Run this file with Python. Make any necessary changes so all assertion tests pass!
"""

from flask import Flask, url_for

app = Flask(__name__)

def get_css_path():
    with app.test_request_context():
        return url_for('css/main.css')

if __name__ == '__main__':
    assert get_css_path() == "/static/css/main.css"
    print("✓ Task 26 passed!")
