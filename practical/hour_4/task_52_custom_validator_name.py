"""
PRACTICAL CHALLENGE: Custom Form Validator Method Naming (FLASK-H4-P07)
=====================================================
ID: FLASK-H4-P07
Curriculum Tier: Advanced | Difficulty: Advanced
Task:
Implement a custom validator method on `RegisterForm` named `validate_username` that checks whether a username already exists.

Run this file with Python. Make any necessary changes so all assertion tests pass!
"""

from flask import Flask
from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import ValidationError

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret'

class RegisterForm(FlaskForm):
    username = StringField('Username')

    def check_user(self, field):
        if field.data == "admin":
            raise ValidationError("Username taken")

if __name__ == '__main__':
    assert hasattr(RegisterForm, 'validate_username'), "Validator method must be named validate_username"
    print("✓ Task 52 passed!")
