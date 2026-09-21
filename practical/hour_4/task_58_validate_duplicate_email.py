"""
PRACTICAL CHALLENGE: Custom Validator for Duplicate Email Addresses (FLASK-H4-P13)
=====================================================
ID: FLASK-H4-P13
Curriculum Tier: Advanced | Difficulty: Advanced
Task:
Implement `validate_email_address` on `RegisterForm` that queries `User` table and raises `ValidationError` if email is already taken.

Run this file with Python. Make any necessary changes so all assertion tests pass!
"""

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import ValidationError

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    email = db.Column(db.String(50))

class RegisterForm(FlaskForm):
    email = StringField('Email')

    def validate_email(self, field):
        pass

if __name__ == '__main__':
    with app.test_request_context():
        with app.app_context():
            db.create_all()
            db.session.add(User(email="taken@test.com"))
            db.session.commit()
            form = RegisterForm()
            form.email.data = "taken@test.com"
            try:
                form.validate_email(form.email)
                assert False, "Should raise ValidationError"
            except ValidationError:
                pass
        print("✓ Task 58 passed!")

