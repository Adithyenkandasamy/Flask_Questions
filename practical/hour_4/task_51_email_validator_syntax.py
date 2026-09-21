"""
PRACTICAL CHALLENGE: Email Field Validation (FLASK-H4-P06)
=====================================================
ID: FLASK-H4-P06
Curriculum Tier: Advanced | Difficulty: Advanced
Task:
Validate the `email_address` field in `RegisterForm` using WTForms' built-in `Email()` validator.

Run this file with Python. Make any necessary changes so all assertion tests pass!
"""

from flask import Flask
from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import Email

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret'

class RegisterForm(FlaskForm):
    email_address = StringField('Email Address', validators=[])

if __name__ == '__main__':
    with app.test_request_context():
        form = RegisterForm()
        assert any(isinstance(v, Email) for v in form.email_address.validators)
        print("✓ Task 51 passed!")

