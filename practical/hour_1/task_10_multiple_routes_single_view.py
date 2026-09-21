"""
PRACTICAL CHALLENGE: Multiple Route Decorators on Single View (FLASK-H1-P10)
=====================================================
ID: FLASK-H1-P10
Curriculum Tier: Beginner | Difficulty: Beginner
Task:
Bind both '/' and '/home' to the same `home_page()` view function.

Run this file with Python. Make any necessary changes so all assertion tests pass!
"""

from flask import Flask

app = Flask(__name__)

@app.route("/")
def home_page():
    return "Home Page Content"

def test_routes():
    with app.test_client() as client:
        res1 = client.get('/')
        res2 = client.get('/home')
        assert res1.status_code == 200
        assert res2.status_code == 200
        assert res1.data == res2.data

if __name__ == '__main__':
    test_routes()
    print("✓ Task 10 passed!")
