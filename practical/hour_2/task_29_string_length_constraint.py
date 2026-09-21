"""
PRACTICAL CHALLENGE: Description Column String Length Specification (FLASK-H2-P14)
=====================================================
ID: FLASK-H2-P14
Curriculum Tier: Basic Application | Difficulty: Elementary
Task:
Define the `description` column on the Item model with a length of 1024 characters, non-nullable and unique.

Run this file with Python. Make any necessary changes so all assertion tests pass!
"""

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
db = SQLAlchemy(app)

class Item(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    description = db.Column(db.String())

if __name__ == '__main__':
    col = Item.__table__.columns['description']
    assert col.type.length == 1024
    assert col.nullable is False
    assert col.unique is True
    print("✓ Task 29 passed!")
