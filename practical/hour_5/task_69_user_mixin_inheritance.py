"""
PRACTICAL CHALLENGE: UserMixin Inheritance for User Model (FLASK-H5-P09)
=====================================================
ID: FLASK-H5-P09
Curriculum Tier: Integration | Difficulty: Advanced
Task:
Update the `User` model to inherit from Flask-Login's `UserMixin` class.

Run this file with Python. Make any necessary changes so all assertion tests pass!
"""

from flask_login import UserMixin

class User:
    def __init__(self, uid):
        self.id = uid

if __name__ == '__main__':
    u = User(1)
    assert hasattr(u, 'is_authenticated')
    assert hasattr(u, 'is_active')
    assert hasattr(u, 'is_anonymous')
    assert hasattr(u, 'get_id')
    assert u.is_authenticated is True
    print("✓ Task 69 passed!")
