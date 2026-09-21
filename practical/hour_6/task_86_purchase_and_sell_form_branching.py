"""
PRACTICAL CHALLENGE: POST Request Action Branching for Purchase vs Sell (FLASK-H6-P11)
=====================================================
ID: FLASK-H6-P11
Curriculum Tier: Real-World Challenge | Difficulty: Expert
Task:
Distinguish between purchase actions (when 'purchased_item' is in form) and sell actions (when 'sold_item' is in form).

Run this file with Python. Make any necessary changes so all assertion tests pass!
"""

def process_post_action(form_data: dict) -> str:
    return "unknown"

if __name__ == '__main__':
    assert process_post_action({"purchased_item": "Phone"}) == "purchase"
    assert process_post_action({"sold_item": "Laptop"}) == "sell"
    assert process_post_action({}) == "unknown"
    print("✓ Task 86 passed!")
