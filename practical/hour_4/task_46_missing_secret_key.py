"""
PRACTICAL CHALLENGE: Configuring SECRET_KEY for CSRF Protection (FLASK-H4-P01)
=====================================================
ID: FLASK-H4-P01
Curriculum Tier: Advanced | Difficulty: Advanced
Task:
Configure `app.config['SECRET_KEY']` with a secret string so Flask-WTF CSRF protection functions properly.

Run this file with Python. Make any necessary changes so all assertion tests pass!
"""

from flask import Flask
from flask_wtf import FlaskForm
from wtforms import StringField

app = Flask(__name__)

class SimpleForm(FlaskForm):
    name = StringField('Name')

def test_form_creation():
    with app.test_request_context():
        form = SimpleForm()
        return form is not None

if __name__ == '__main__':
    assert test_form_creation() is True
    print("✓ Task 46 passed!")
