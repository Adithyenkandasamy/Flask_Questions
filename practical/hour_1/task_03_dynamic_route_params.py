"""
PRACTICAL CHALLENGE: Dynamic Routing with URL Arguments (FLASK-H1-P03)
=====================================================
ID: FLASK-H1-P03
Curriculum Tier: Beginner | Difficulty: Beginner
Task:
Define a route '/about/<username>' that accepts a dynamic username argument in the URL and reflects it in the response.

Run this file with Python. Make any necessary changes so all assertion tests pass!
"""

from flask import Flask

app = Flask(__name__)

@app.route("/about/<username>")
def about_page(username):
    
    return f"<h1>About Page of {username}</h1>"

def test_dynamic_route():
    with app.test_client() as client:
        res = client.get('/about/john')
        assert res.status_code == 200
        assert b"About Page of john" in res.data

if __name__ == '__main__':
    test_dynamic_route()
    print("✓ Task 03 passed!")

# Done -> After Getting the value from the api request we need to get that from a parameter in the function like "def app(name)""
