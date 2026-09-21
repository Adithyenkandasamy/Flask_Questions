"""
PRACTICAL CHALLENGE: Model Dictionary Serialization Helper (FLASK-H3-P15)
=====================================================
ID: FLASK-H3-P15
Curriculum Tier: Intermediate | Difficulty: Intermediate
Task:
Implement a `to_dict()` method on the Item model returning a dictionary representation of `id`, `name`, and `price`.

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

if __name__ == '__main__':
    item = Item(id=1, name="Keyboard", price=45)
    assert hasattr(item, 'to_dict'), "Model must define to_dict method"
    data = item.to_dict()
    assert data == {"id": 1, "name": "Keyboard", "price": 45}
    print("✓ Task 45 passed!")
