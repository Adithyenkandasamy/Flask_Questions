"""
PRACTICAL CHALLENGE: Deducting Item Cost from User Budget (FLASK-H6-P02)
=====================================================
ID: FLASK-H6-P02
Curriculum Tier: Real-World Challenge | Difficulty: Expert
Task:
Implement `purchase_item` to deduct the item's price from the user's budget and return the updated balance.

Run this file with Python. Make any necessary changes so all assertion tests pass!
"""

class User:
    def __init__(self, budget: int):
        self.budget = budget

    def purchase_item(self, price: int) -> int:
        return self.budget

if __name__ == '__main__':
    u = User(1000)
    new_bal = u.purchase_item(350)
    assert u.budget == 650
    assert new_bal == 650
    print("✓ Task 77 passed!")
