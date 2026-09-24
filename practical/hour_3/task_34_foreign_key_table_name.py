"""
PRACTICAL CHALLENGE: SQLAlchemy ForeignKey Table Reference (FLASK-H3-P04)
=====================================================
ID: FLASK-H3-P04
Curriculum Tier: Intermediate | Difficulty: Intermediate
Task:
Define a foreign key column `owner` on `Item` referencing the `id` column of the `user` table.

Run this file with Python. Make any necessary changes so all assertion tests pass!
"""

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    username = db.Column(db.String(30))

class Item(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(30))
    owner = db.Column(db.Integer(), db.ForeignKey(User.id)) # foriegn key is mentioned as with ForeignKey(User.id)

if __name__ == '__main__':
    with app.app_context():
        fk = list(Item.__table__.foreign_keys)[0]
        assert fk.target_fullname == 'user.id', "ForeignKey must target lowercase SQL table name 'user.id'"
    print("✓ Task 34 passed!")
