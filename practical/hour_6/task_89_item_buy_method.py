"""
PRACTICAL CHALLENGE: Item Model Encapsulated buy Method (FLASK-H6-P14)
=====================================================
ID: FLASK-H6-P14
Curriculum Tier: Real-World Challenge | Difficulty: Expert
Task:
Implement `buy(self, user)` on Item that assigns `self.owner = user.id`, deducts `user.budget -= self.price`, and commits the session.

Run this file with Python. Make any necessary changes so all assertion tests pass!
"""

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    budget = db.Column(db.Integer(), default=1000)

class Item(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    price = db.Column(db.Integer(), nullable=False)
    owner = db.Column(db.Integer(), nullable=True)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        u = User(budget=1000)
        it = Item(price=300)
        db.session.add_all([u, it])
        db.session.commit()
        assert hasattr(it, 'buy'), "Item must implement buy(user)"
        it.buy(u)
        assert it.owner == u.id
        assert u.budget == 700
    print("✓ Task 89 passed!")
