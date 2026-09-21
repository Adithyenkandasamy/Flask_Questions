"""
PRACTICAL CHALLENGE: Extracting Form Field Data from Submission (FLASK-H6-P08)
=====================================================
ID: FLASK-H6-P08
Curriculum Tier: Real-World Challenge | Difficulty: Expert
Task:
Extract the integer item ID from the submitted purchase form data dictionary.

Run this file with Python. Make any necessary changes so all assertion tests pass!
"""

def extract_item_id(form_dict: dict) -> int:
    return 0

if __name__ == '__main__':
    data = {"purchased_item": "42"}
    assert extract_item_id(data) == 42
    print("✓ Task 83 passed!")
