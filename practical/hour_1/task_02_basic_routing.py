"""
PRACTICAL CHALLENGE: Basic Routing and View Return Types (FLASK-H1-P02)
=====================================================
ID: FLASK-H1-P02
Curriculum Tier: Beginner | Difficulty: Beginner
Task:
Configure a route for '/home' that returns an HTTP 200 response containing the welcome text 'Welcome to Flask Market!'.

Run this file with Python. Make any necessary changes so all assertion tests pass!
"""

from flask import Flask

app = Flask(__name__)

@app.route("/home")
def home():
    return {"message":"Welcome to Flask Market!"}

def test_route():
    with app.test_client() as client:
        res = client.get('/home')
        assert res.status_code == 200
        assert b"Welcome to Flask Market!" in res.data

if __name__ == '__main__':
    test_route()
    print("✓ Task 02 passed!")

#Done - > Here it Return 200 by default
