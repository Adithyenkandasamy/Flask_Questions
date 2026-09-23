"""
PRACTICAL CHALLENGE: Primary Key Definition on SQLAlchemy Model (FLASK-H2-P03)
=====================================================
ID: FLASK-H2-P03
Curriculum Tier: Basic Application | Difficulty: Elementary
Task:
Define the `Item` model schema with an integer primary key column named `id`.

Run this file with Python. Make any necessary changes so all assertion tests pass!
"""

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
db = SQLAlchemy(app)

class Item(db.Model):
    id = db.Column(db.Integer(),primary_key=True,nullable=False)
    name = db.Column(db.String(30), nullable=False)
    price = db.Column(db.Integer(), nullable=False)

if __name__ == '__main__':
    with app.app_context():
        assert hasattr(Item, 'id')
        assert Item.id.primary_key is True
        print("✓ Task 18 passed!")
