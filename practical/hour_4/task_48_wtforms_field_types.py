"""
PRACTICAL CHALLENGE: Selecting Secure Form Field Types (FLASK-H4-P03)
=====================================================
ID: FLASK-H4-P03
Curriculum Tier: Advanced | Difficulty: Advanced
Task:
Define a registration form using WTForms with appropriate fields: `StringField` for username and `PasswordField` for password inputs.

Run this file with Python. Make any necessary changes so all assertion tests pass!
"""

from flask import Flask
from flask_wtf import FlaskForm
from wtforms import StringField

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret'

class RegisterForm(FlaskForm):
    username = StringField('Username')
    password = StringField('Password')

if __name__ == '__main__':
    with app.test_request_context():
        from wtforms import PasswordField
        form = RegisterForm()
        assert isinstance(form.password, PasswordField), "Password field must use PasswordField"
        print("✓ Task 48 passed!")

