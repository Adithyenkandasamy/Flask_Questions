"""
PRACTICAL CHALLENGE: SQLAlchemy Relationship Definition (FLASK-H3-P05)
=====================================================
ID: FLASK-H3-P05
Curriculum Tier: Intermediate | Difficulty: Intermediate
Task:
Declare a `db.relationship` on `User` linking to the `Item` model with backref `owned_user` and lazy=True.

Run this file with Python. Make any necessary changes so all assertion tests pass!
"""

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    username = db.Column(db.String(30))
    items = db.relationship("Item", backref="owned_user",lazy = True)
class Item(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    owner = db.Column(db.Integer(), db.ForeignKey('user.id'))

if __name__ == '__main__':
    assert hasattr(User, 'items'), "User must declare items relationship"
    print("✓ Task 35 passed!")
