"""
PRACTICAL CHALLENGE: HiddenField for Modal Form Submissions (FLASK-H4-P14)
=====================================================
ID: FLASK-H4-P14
Curriculum Tier: Advanced | Difficulty: Advanced
Task:
Define a `PurchaseItemForm` with a `SubmitField` and a `HiddenField` named `purchased_item`.

Run this file with Python. Make any necessary changes so all assertion tests pass!
"""

from flask import Flask
from flask_wtf import FlaskForm
from wtforms import SubmitField

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret'

class PurchaseItemForm(FlaskForm):
    submit = SubmitField('Purchase')

if __name__ == '__main__':
    from wtforms import HiddenField
    with app.test_request_context():
        form = PurchaseItemForm()
        assert hasattr(form, 'purchased_item'), "Form must define purchased_item field"
        assert isinstance(form.purchased_item, HiddenField)
    print("✓ Task 59 passed!")
