"""
PRACTICAL CHALLENGE: Flask Application Initialization (FLASK-H1-P01)
=====================================================
ID: FLASK-H1-P01
Curriculum Tier: Beginner | Difficulty: Beginner
Task:
Initialize a Flask application instance properly so that it exports an `app` object with a valid configuration and module name.

Run this file with Python. Make any necessary changes so all assertion tests pass!
"""

from flask import flask

app = None

def get_app():
    return app

if __name__ == '__main__':
    assert get_app() is not None, "App should be initialized"
    assert get_app().import_name is not None
    print("✓ Task 01 passed!")
