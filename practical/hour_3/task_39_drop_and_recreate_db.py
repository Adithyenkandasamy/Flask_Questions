"""
PRACTICAL CHALLENGE: Database Reset Procedure with drop_all and create_all (FLASK-H3-P09)
=====================================================
ID: FLASK-H3-P09
Curriculum Tier: Intermediate | Difficulty: Intermediate
Task:
Implement a database reset routine that drops all existing tables and re-creates fresh tables.

Run this file with Python. Make any necessary changes so all assertion tests pass!
"""

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
db = SQLAlchemy(app)

class Item(db.Model):
    id = db.Column(db.Integer(), primary_key=True)

def reset_database():
    with app.app_context():
        db.drop_all() # we have deleted Now we need to Create new Table 
        db.create_all()

if __name__ == '__main__':
    reset_database()
    with app.app_context():
        assert db.engine.dialect.has_table(db.engine.connect(), "item")
    print("✓ Task 39 passed!")
