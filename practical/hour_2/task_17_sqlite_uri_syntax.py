"""
PRACTICAL CHALLENGE: SQLite Database URI Configuration (FLASK-H2-P02)
=====================================================
ID: FLASK-H2-P02
Curriculum Tier: Basic Application | Difficulty: Elementary
Task:
Configure `SQLALCHEMY_DATABASE_URI` for a local SQLite database named 'market.db' using standard URI formatting.

Run this file with Python. Make any necessary changes so all assertion tests pass!
"""

from flask import Flask

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///market.db'

if __name__ == '__main__':
    assert app.config['SQLALCHEMY_DATABASE_URI'] == 'sqlite:///market.db'
    print("✓ Task 17 passed!")

# Main thing we NEed The Three /// Slash Mandtory