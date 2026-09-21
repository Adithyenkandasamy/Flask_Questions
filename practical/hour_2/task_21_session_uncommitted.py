"""
PRACTICAL CHALLENGE: SQLAlchemy Session Commit Workflow (FLASK-H2-P06)
=====================================================
ID: FLASK-H2-P06
Curriculum Tier: Basic Application | Difficulty: Elementary
Task:
Stage and persist the newly created Item instance to the database using SQLAlchemy's session workflow.

Run this file with Python. Make any necessary changes so all assertion tests pass!
"""

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
db = SQLAlchemy(app)

class Item(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(30), nullable=False)

def create_item(name: str):
    with app.app_context():
        db.create_all()
        item = Item(name=name)
        db.session.add(item)

if __name__ == '__main__':
    create_item("Keyboard")
    with app.app_context():
        saved = Item.query.filter_by(name="Keyboard").first()
        assert saved is not None, "Item must be saved to the database"
    print("✓ Task 21 passed!")
