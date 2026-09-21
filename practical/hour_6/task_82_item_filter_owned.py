"""
PRACTICAL CHALLENGE: Querying User-Owned Items (FLASK-H6-P07)
=====================================================
ID: FLASK-H6-P07
Curriculum Tier: Real-World Challenge | Difficulty: Expert
Task:
Query all items in the database that belong to a specific user (`owner == user_id`).

Run this file with Python. Make any necessary changes so all assertion tests pass!
"""

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
db = SQLAlchemy(app)

class Item(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(30))
    owner = db.Column(db.Integer(), nullable=True)

def get_user_items(user_id: int):
    with app.app_context():
        return []

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        db.session.add_all([Item(name="ItemA", owner=7), Item(name="ItemB", owner=8), Item(name="ItemC", owner=7)])
        db.session.commit()
        my_items = get_user_items(7)
        assert len(my_items) == 2
        assert all(i.owner == 7 for i in my_items)
    print("✓ Task 82 passed!")
