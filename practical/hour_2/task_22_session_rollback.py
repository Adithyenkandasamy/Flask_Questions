"""
PRACTICAL CHALLENGE: Transaction Rollback on Error (FLASK-H2-P07)
=====================================================
ID: FLASK-H2-P07
Curriculum Tier: Basic Application | Difficulty: Elementary
Task:
Safely attempt to add an item to the session, handling exceptions by rolling back the transaction and returning False.

Run this file with Python. Make any necessary changes so all assertion tests pass!
"""

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
db = SQLAlchemy(app)

class Item(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(10), unique=True, nullable=False)

def safe_add(name: str) -> bool:
    with app.app_context():
        db.create_all()
        item = Item(name=name)
        db.session.add(item)
        db.session.commit()
        return True

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        assert safe_add("Unique1") is True
        assert safe_add("Unique1") is False
    print("✓ Task 22 passed!")
