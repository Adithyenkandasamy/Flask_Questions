"""
PRACTICAL CHALLENGE: Query Filtering with Comparison Operators (FLASK-H2-P12)
=====================================================
ID: FLASK-H2-P12
Curriculum Tier: Basic Application | Difficulty: Elementary
Task:
Query all items in the database whose price is greater than or equal to 500 using `Item.query.filter()`.

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
    price = db.Column(db.Integer())

def get_expensive_items():
    with app.app_context():
        db.create_all()
        db.session.add_all([Item(name="Pen", price=5), Item(name="Phone", price=500), Item(name="Laptop", price=1200)])
        db.session.commit()
        return Item.query.all()

if __name__ == '__main__':
    items = get_expensive_items()
    assert len(items) == 2
    assert all(i.price >= 500 for i in items)
    print("✓ Task 27 passed!")
