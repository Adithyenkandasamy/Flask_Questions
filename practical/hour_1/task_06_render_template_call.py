"""
PRACTICAL CHALLENGE: Template Context Variable Passing (FLASK-H1-P06)
=====================================================
ID: FLASK-H1-P06
Curriculum Tier: Beginner | Difficulty: Beginner
Task:
Render a template string displaying items by passing the items list into the template context.

Run this file with Python. Make any necessary changes so all assertion tests pass!
"""

from flask import Flask, render_template_string

app = Flask(__name__)

TEMPLATE = "<ul>{% for item in items %}<li>{{ item }}</li>{% endfor %}</ul>"

@app.route("/items")
def items_view():
    items = ["Phone", "Laptop"]
    return render_template_string(TEMPLATE)

def test_items_view():
    with app.test_client() as client:
        res = client.get('/items')
        assert b"Phone" in res.data
        assert b"Laptop" in res.data

if __name__ == '__main__':
    test_items_view()
    print("✓ Task 06 passed!")
