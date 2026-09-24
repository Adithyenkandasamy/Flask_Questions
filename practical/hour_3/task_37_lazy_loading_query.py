"""
PRACTICAL CHALLENGE: Iterating Over Relationship Collections (FLASK-H3-P07)
=====================================================
ID: FLASK-H3-P07
Curriculum Tier: Intermediate | Difficulty: Intermediate
Task:
Calculate the total value of all items owned by a user by iterating through the user's `items` relationship collection.

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
    price = db.Column(db.Integer())
    owner = db.Column(db.Integer(), db.ForeignKey(User.id))

def calculate_owned_value(user: User) -> int:
    return sum(item.price for item in user.items)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        u = User(username="bob")
        db.session.add(u)
        db.session.commit()
        db.session.add_all([Item(price=100, owner=u.id), Item(price=250, owner=u.id)])
        db.session.commit()
        assert calculate_owned_value(u) == 350
    print("✓ Task 37 passed!")
