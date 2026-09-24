"""
PRACTICAL CHALLENGE: Item Count Property on User Model (FLASK-H3-P14)
=====================================================
ID: FLASK-H3-P14
Curriculum Tier: Intermediate | Difficulty: Intermediate
Task:
Implement an `item_count` property on the User model that returns the total count of owned items.

Run this file with Python. Make any necessary changes so all assertion tests pass!
"""

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import func

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    items = db.relationship('Item', backref='owned_user', lazy=True)

    @property
    def item_count(self):
        return len(self.items)

class Item(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    owner = db.Column(db.Integer(), db.ForeignKey('user.id'))

        
if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        u = User()
        db.session.add(u)
        db.session.commit()
        db.session.add_all([Item(owner=u.id), Item(owner=u.id)])
        db.session.commit()
        assert hasattr(u, 'item_count'), "User model must have item_count property"
        assert u.item_count == 2
    print("✓ Task 44 passed!")
