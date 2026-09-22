"""
PRACTICAL CHALLENGE: Custom HTTP Status Codes (FLASK-H1-P04)
=====================================================
ID: FLASK-H1-P04
Curriculum Tier: Beginner | Difficulty: Beginner
Task:
Configure the item endpoint to return a 404 status code with message 'Item not found' when an unrecognized item name is requested.

Run this file with Python. Make any necessary changes so all assertion tests pass!
"""

from flask import Flask, abort

app = Flask(__name__)

@app.route("/item/<name>")
def item_page(name):
    if name != "phone":
        abort(404,description="Item not found")
    return "Found item"

def test_status_code():
    with app.test_client() as client:
        res = client.get('/item/laptop')
        assert res.status_code == 404
        assert b"not found" in res.data

if __name__ == '__main__':
    test_status_code()
    print("✓ Task 04 passed!")

# Done NOt like Fastapi HTTPExection it will work with the abort function inside that we can mention the thing we need to give responce