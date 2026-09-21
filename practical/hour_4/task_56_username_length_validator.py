"""
PRACTICAL CHALLENGE: Username Length Constraints with WTForms Length Validator (FLASK-H4-P11)
=====================================================
ID: FLASK-H4-P11
Curriculum Tier: Advanced | Difficulty: Advanced
Task:
Configure `username` in `RegisterForm` to enforce a minimum length of 2 and maximum length of 30 characters using `Length(min=2, max=30)`.

Run this file with Python. Make any necessary changes so all assertion tests pass!
"""

from flask import Flask
from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import Length

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret'

class RegisterForm(FlaskForm):
    username = StringField('Username', validators=[])

if __name__ == '__main__':
    with app.test_request_context():
        form = RegisterForm()
        len_val = [v for v in form.username.validators if isinstance(v, Length)]
        assert len(len_val) > 0, "Length validator required"
        assert len_val[0].min == 2
        assert len_val[0].max == 30
        print("✓ Task 56 passed!")

