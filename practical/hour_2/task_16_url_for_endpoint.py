"""
PRACTICAL CHALLENGE: View Function URL Generation with url_for (FLASK-H2-P01)
=====================================================
ID: FLASK-H2-P01
Curriculum Tier: Basic Application | Difficulty: Elementary
Task:
Use Flask's `url_for` function to dynamically generate the URL endpoint for the `market_page` view function.

Run this file with Python. Make any necessary changes so all assertion tests pass!
"""

from flask import Flask, url_for

app = Flask(__name__)

@app.route("/store/items")
def market_page():
    return "Market Items"

def get_market_url():
    with app.test_request_context():
        return url_for('/store/items')

if __name__ == '__main__':
    url = get_market_url()
    assert url == "/store/items"
    print("✓ Task 16 passed!")
