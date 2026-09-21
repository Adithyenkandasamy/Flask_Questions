"""
PRACTICAL CHALLENGE: Assigning Purchased Item Ownership (FLASK-H6-P03)
=====================================================
ID: FLASK-H6-P03
Curriculum Tier: Real-World Challenge | Difficulty: Expert
Task:
Transfer ownership of an item to a buyer by setting `item.owner` to `user.id` and committing the transaction.

Run this file with Python. Make any necessary changes so all assertion tests pass!
"""

class Item:
    def __init__(self, name):
        self.name = name
        self.owner = None

class User:
    def __init__(self, uid):
        self.id = uid

def assign_ownership(item: Item, buyer: User):
    pass

if __name__ == '__main__':
    it = Item("Laptop")
    u = User(42)
    assign_ownership(it, u)
    assert it.owner == 42
    print("✓ Task 78 passed!")
