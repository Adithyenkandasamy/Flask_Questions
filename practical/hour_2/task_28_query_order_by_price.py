"""
PRACTICAL CHALLENGE: Sorting Database Results with order_by (FLASK-H2-P13)
=====================================================
ID: FLASK-H2-P13
Curriculum Tier: Basic Application | Difficulty: Elementary
Task:
Retrieve items sorted by price in descending order using `order_by(Item.price.desc())`.

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

def get_sorted_items():
    with app.app_context():
        db.create_all()
        db.session.add_all([Item(name="Phone", price=500), Item(name="Laptop", price=1200), Item(name="Mouse", price=50)])
        db.session.commit()
        return Item.query.order_by(Item.price.desc()).all()

if __name__ == '__main__':
    items = get_sorted_items()
    assert [i.price for i in items] == [1200, 500, 50]
    print("✓ Task 28 passed!")

#  here we can use this return Item.query.order_by(Item.price.desc()).all() like instead of filter we cazn use the order_by()then our things and .desc()or .asce() to orde it 
