"""
PRACTICAL CHALLENGE: Appending Items to User Relationship Collection (FLASK-H3-P11)
=====================================================
ID: FLASK-H3-P11
Curriculum Tier: Intermediate | Difficulty: Intermediate
Task:
Append an item directly into the user's `items` relationship list, verifying that SQLAlchemy automatically associates the owner foreign key.

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
    items = db.relationship('Item', backref='owned_user', lazy=True)

class Item(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(30))
    owner = db.Column(db.Integer(), db.ForeignKey('user.id'))

def add_item_to_user(user: User, item: Item):
    pass

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        u = User(username="dan")
        db.session.add(u)
        db.session.commit()
        it = Item(name="Watch")
        add_item_to_user(u, it)
        db.session.commit()
        assert it in u.items
        assert it.owner == u.id
    print("✓ Task 41 passed!")
