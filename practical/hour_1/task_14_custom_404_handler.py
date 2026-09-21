"""
PRACTICAL CHALLENGE: Custom 404 Error Handler (FLASK-H1-P14)
=====================================================
ID: FLASK-H1-P14
Curriculum Tier: Beginner | Difficulty: Beginner
Task:
Register a custom 404 error handler using `@app.errorhandler(404)` that returns a custom message and status 404.

Run this file with Python. Make any necessary changes so all assertion tests pass!
"""

from flask import Flask

app = Flask(__name__)

def test_404():
    with app.test_client() as client:
        res = client.get('/nonexistent_endpoint')
        assert res.status_code == 404
        assert b"Custom Page Not Found" in res.data

if __name__ == '__main__':
    test_404()
    print("✓ Task 14 passed!")
