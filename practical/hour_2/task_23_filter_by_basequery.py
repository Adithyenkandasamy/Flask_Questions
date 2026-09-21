"""
PRACTICAL CHALLENGE: Query Record Extraction with .first() (FLASK-H2-P08)
=====================================================
ID: FLASK-H2-P08
Curriculum Tier: Basic Application | Difficulty: Elementary
Task:
Query the Item table for an item with barcode '123456789012' and extract the single model instance.

Run this file with Python. Make any necessary changes so all assertion tests pass!
"""

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
db = SQLAlchemy(app)

class Item(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    barcode = db.Column(db.String(12), unique=True)

def find_item():
    with app.app_context():
        db.create_all()
        db.session.add(Item(barcode='123456789012'))
        db.session.commit()
        return Item.query.filter_by(barcode='123456789012')

if __name__ == '__main__':
    result = find_item()
    assert isinstance(result, Item), "Should return the Item model instance, not BaseQuery"
    print("✓ Task 23 passed!")
