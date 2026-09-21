"""
PRACTICAL CHALLENGE: Querying Available Market Items (FLASK-H6-P06)
=====================================================
ID: FLASK-H6-P06
Curriculum Tier: Real-World Challenge | Difficulty: Expert
Task:
Query all available items in the market where `owner == None`.

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

def get_available_items():
    with app.app_context():
        return []

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        db.session.add_all([Item(name="Unowned1", owner=None), Item(name="Owned", owner=1), Item(name="Unowned2", owner=None)])
        db.session.commit()
        unowned = get_available_items()
        assert len(unowned) == 2
        assert all(i.owner is None for i in unowned)
    print("✓ Task 81 passed!")
