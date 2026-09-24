"""
PRACTICAL CHALLENGE: Assigning Foreign Key Ownership (FLASK-H3-P08)
=====================================================
ID: FLASK-H3-P08
Curriculum Tier: Intermediate | Difficulty: Intermediate
Task:
Assign ownership of an item to a user by setting the item's `owner` foreign key attribute to the user's ID.

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

class Item(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    owner = db.Column(db.Integer(), db.ForeignKey('user.id'))

def set_owner(item: Item, user: User):
    item.owner = user.id

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        u = User(username="carol")
        db.session.add(u)
        db.session.commit()
        item = Item()
        set_owner(item, u)
        assert item.owner == u.id
    print("✓ Task 38 passed!")
