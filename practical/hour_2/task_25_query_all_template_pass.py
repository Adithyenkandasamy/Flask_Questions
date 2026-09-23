"""
PRACTICAL CHALLENGE: Querying Database Items for Template Rendering (FLASK-H2-P10)
=====================================================
ID: FLASK-H2-P10
Curriculum Tier: Basic Application | Difficulty: Elementary
Task:
Query all records from the `Item` table and render them through the template context.

Run this file with Python. Make any necessary changes so all assertion tests pass!
"""

from flask import Flask, render_template_string
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
db = SQLAlchemy(app)

class Item(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(30))

@app.route('/market')
def market_page():
    all_items = Item.query.all()
    return render_template_string("<ul>{% for i in items %}<li>{{ i.name }}</li>{% endfor %}</ul>",items=all_items)

def test_view():
    with app.app_context():
        db.create_all()
        db.session.add_all([Item(name="Item1"), Item(name="Item2")])
        db.session.commit()
    with app.test_client() as client:
        res = client.get('/market')
        assert b"Item1" in res.data
        assert b"Item2" in res.data

if __name__ == '__main__':
    test_view()
    print("✓ Task 25 passed!")


# Hewre we using the render template and import a list named as item ryt so we need to pass it we need to fetch all the things from the db so we use the Item.query.all() here so it fetch all the datas stored in the db 