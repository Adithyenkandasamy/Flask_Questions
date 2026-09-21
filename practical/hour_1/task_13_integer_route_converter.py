"""
PRACTICAL CHALLENGE: Integer URL Route Converter (FLASK-H1-P13)
=====================================================
ID: FLASK-H1-P13
Curriculum Tier: Beginner | Difficulty: Beginner
Task:
Configure a route '/item/<int:item_id>' so that requests with non-integer segments return 404.

Run this file with Python. Make any necessary changes so all assertion tests pass!
"""

from flask import Flask

app = Flask(__name__)

@app.route("/item/<item_id>")
def show_item(item_id):
    return f"Item ID: {item_id}"

def test_converter():
    with app.test_client() as client:
        res_valid = client.get('/item/42')
        res_invalid = client.get('/item/abc')
        assert res_valid.status_code == 200
        assert res_invalid.status_code == 404

if __name__ == '__main__':
    test_converter()
    print("✓ Task 13 passed!")
