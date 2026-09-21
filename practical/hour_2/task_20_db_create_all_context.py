"""
PRACTICAL CHALLENGE: Database Table Creation within Application Context (FLASK-H2-P05)
=====================================================
ID: FLASK-H2-P05
Curriculum Tier: Basic Application | Difficulty: Elementary
Task:
Create the SQLite database tables using `db.create_all()` within the Flask application context.

Run this file with Python. Make any necessary changes so all assertion tests pass!
"""

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
db = SQLAlchemy(app)

class Item(db.Model):
    id = db.Column(db.Integer(), primary_key=True)

def setup_db():
    db.create_all()

if __name__ == '__main__':
    setup_db()
    with app.app_context():
        assert db.engine.dialect.has_table(db.engine.connect(), "item")
    print("✓ Task 20 passed!")
