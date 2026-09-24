"""
PRACTICAL CHALLENGE: User Model Schema Definition (FLASK-H3-P03)
=====================================================
ID: FLASK-H3-P03
Curriculum Tier: Intermediate | Difficulty: Intermediate
Task:
Define the `User` model schema with an `id` primary key, unique `username`, unique `email_address`, `password_hash`, and integer `budget` with default 1000.

Run this file with Python. Make any necessary changes so all assertion tests pass!
"""

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    username = db.Column(db.String(30), nullable=False, unique=True)
    email_address = db.Column(db.String(50), nullable=False, unique=True)
    password_hash = db.Column(db.String(60), nullable=False, unique=True)
    budget = db.Column(db.Integer(),default=1000)

def test_user_budget():
    with app.app_context():
        db.create_all()
        user = User(username="test", email_address="t@test.com", password_hash="hash")
        db.session.add(user)
        db.session.commit()
        assert hasattr(user, 'budget'), "User must have a budget column"
        assert user.budget == 1000, "Default budget must be 1000"

if __name__ == '__main__':
    test_user_budget()
    print("✓ Task 33 passed!")
