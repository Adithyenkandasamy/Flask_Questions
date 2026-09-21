"""
PRACTICAL CHALLENGE: Validating Password Confirmation with EqualTo (FLASK-H4-P05)
=====================================================
ID: FLASK-H4-P05
Curriculum Tier: Advanced | Difficulty: Advanced
Task:
Add the `EqualTo` validator to `password_confirm` to ensure it matches the value entered in `password`.

Run this file with Python. Make any necessary changes so all assertion tests pass!
"""

from flask import Flask
from flask_wtf import FlaskForm
from wtforms import PasswordField
from wtforms.validators import EqualTo

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret'

class RegisterForm(FlaskForm):
    password = PasswordField('Password')
    password_confirm = PasswordField('Confirm Password', validators=[EqualTo('wrong_field')])

if __name__ == '__main__':
    with app.test_request_context():
        form = RegisterForm()
        eq = [v for v in form.password_confirm.validators if isinstance(v, EqualTo)][0]
        assert eq.fieldname == 'password'
        print("✓ Task 50 passed!")

