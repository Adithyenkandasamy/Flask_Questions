"""
PRACTICAL CHALLENGE: SQLAlchemy Column Constraints and Validation (FLASK-H2-P04)
=====================================================
ID: FLASK-H2-P04
Curriculum Tier: Basic Application | Difficulty: Elementary
Task:
Configure the `barcode` column in the `Item` model so that it is both non-nullable and strictly unique across all records.

Run this file with Python. Make any necessary changes so all assertion tests pass!
"""

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
db = SQLAlchemy(app)

class Item(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    barcode = db.Column(db.String(12),unique=True,nullable=False)

if __name__ == '__main__':
    with app.app_context():
        col = Item.__table__.columns['barcode']
        assert col.nullable is False
        assert col.unique is True
        print("✓ Task 19 passed!")
