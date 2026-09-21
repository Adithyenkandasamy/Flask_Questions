"""
PRACTICAL CHALLENGE: Adding Field Validators to WTForms (FLASK-H4-P04)
=====================================================
ID: FLASK-H4-P04
Curriculum Tier: Advanced | Difficulty: Advanced
Task:
Attach the `DataRequired()` validator to the username field in `RegisterForm` to reject empty or whitespace submissions.

Run this file with Python. Make any necessary changes so all assertion tests pass!
"""

from flask import Flask
from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret'

class RegisterForm(FlaskForm):
    username = StringField('Username', validators=[])

if __name__ == '__main__':
    with app.test_request_context():
        form = RegisterForm()
        assert any(isinstance(v, DataRequired) for v in form.username.validators)
        print("✓ Task 49 passed!")

