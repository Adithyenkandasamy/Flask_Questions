"""
PRACTICAL CHALLENGE: Clearing Item Ownership via None Assignment (FLASK-H3-P12)
=====================================================
ID: FLASK-H3-P12
Curriculum Tier: Intermediate | Difficulty: Intermediate
Task:
Disassociate an item from its owner by setting `item.owner = None` and verifying it no longer appears in `user.items`.

Run this file with Python. Make any necessary changes so all assertion tests pass!
"""

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    items = db.relationship('Item', backref='owned_user', lazy=True)

class Item(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    owner = db.Column(db.Integer(), db.ForeignKey('user.id'))

def disown_item(item: Item):
    item.owner=None

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        u = User()
        db.session.add(u)
        db.session.commit()
        item = Item(owner=u.id)
        db.session.add(item)
        db.session.commit()
        disown_item(item)
        db.session.commit()
        assert item.owner is None
        assert item not in u.items
    print("✓ Task 42 passed!")
