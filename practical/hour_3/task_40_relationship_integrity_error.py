"""
PRACTICAL CHALLENGE: Validating Foreign Key Assignment (FLASK-H3-P10)
=====================================================
ID: FLASK-H3-P10
Curriculum Tier: Intermediate | Difficulty: Intermediate
Task:
Safely assign an owner ID to an item, verifying that the target user ID exists in the database before assigning.

Run this file with Python. Make any necessary changes so all assertion tests pass!
"""

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer(), primary_key=True)

class Item(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    owner = db.Column(db.Integer(), db.ForeignKey('user.id'))

def safe_assign_owner(item: Item, target_user_id: int) -> bool:
    item.owner = target_user_id
    return True

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        u = User()
        db.session.add(u)
        db.session.commit()
        item = Item()
        assert safe_assign_owner(item, u.id) is True
        assert safe_assign_owner(item, 9999) is False
    print("✓ Task 40 passed!")
