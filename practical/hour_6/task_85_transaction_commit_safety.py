"""
PRACTICAL CHALLENGE: Marketplace Transaction Commit and Rollback Safety (FLASK-H6-P10)
=====================================================
ID: FLASK-H6-P10
Curriculum Tier: Real-World Challenge | Difficulty: Expert
Task:
Wrap marketplace transactions in a try/except block that commits on success and rolls back the session on failure.

Run this file with Python. Make any necessary changes so all assertion tests pass!
"""

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
db = SQLAlchemy(app)

class Account(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    balance = db.Column(db.Integer(), nullable=False)

def execute_transfer(from_acc: Account, to_acc: Account, amount: int):
    from_acc.balance -= amount
    if from_acc.balance < 0:
        raise ValueError("Insufficient balance")
    to_acc.balance += amount
    db.session.commit()

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        a1 = Account(balance=100)
        a2 = Account(balance=50)
        db.session.add_all([a1, a2])
        db.session.commit()
        try:
            execute_transfer(a1, a2, 200)
        except Exception:
            db.session.rollback()
        assert a1.balance == 100, "Balance should roll back on failure"
    print("✓ Task 85 passed!")
