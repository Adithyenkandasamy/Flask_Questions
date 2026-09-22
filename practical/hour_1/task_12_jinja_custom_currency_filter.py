    """
    PRACTICAL CHALLENGE: Custom Jinja Template Filter for Currency (FLASK-H1-P12)
    =====================================================
    ID: FLASK-H1-P12
    Curriculum Tier: Beginner | Difficulty: Beginner
    Task:
    Register a custom Jinja filter named 'currency' that appends '$' to the numeric value.

    Run this file with Python. Make any necessary changes so all assertion tests pass!
    """

    from flask import Flask, render_template_string

    app = Flask(__name__)

    TEMPLATE = "<p>{{ price | currency }}</p>"

    @app.template_filter('currency')
    def currency_filter(val):
        return f"{val}$"

    def render_price(price: int) -> str:
        with app.app_context():
            return render_template_string(TEMPLATE, price=price)

    if __name__ == '__main__':
        out = render_price(500)
        assert "<p>500$</p>" in out
        print("✓ Task 12 passed!")
