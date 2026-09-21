"""
PRACTICAL CHALLENGE: Purchasing Budget Sufficiency Validation (FLASK-H6-P01)
=====================================================
ID: FLASK-H6-P01
Curriculum Tier: Real-World Challenge | Difficulty: Expert
Task:
Implement `can_purchase` to verify that a user has sufficient budget to purchase an item of a given price.

Run this file with Python. Make any necessary changes so all assertion tests pass!
"""

class User:
    def __init__(self, budget: int):
        self.budget = budget

    def can_purchase(self, item_price: int) -> bool:
        return True

if __name__ == '__main__':
    user = User(500)
    assert user.can_purchase(300) is True, "Budget 500 should be able to buy 300 item"
    assert user.can_purchase(600) is False, "Budget 500 should NOT be able to buy 600 item"
    assert user.can_purchase(500) is True, "Exact budget should be able to buy item"
    print("✓ Task 76 passed!")
