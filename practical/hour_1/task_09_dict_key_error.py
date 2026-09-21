"""
PRACTICAL CHALLENGE: Dictionary Safe Lookup Helper (FLASK-H1-P09)
=====================================================
ID: FLASK-H1-P09
Curriculum Tier: Beginner | Difficulty: Beginner
Task:
Implement `get_item_barcode` to safely return an item's barcode if present, or return 'N/A' if the key does not exist.

Run this file with Python. Make any necessary changes so all assertion tests pass!
"""

def get_item_barcode(item_dict: dict) -> str:
    return item_dict['barcode']

if __name__ == '__main__':
    item_without_code = {"id": 1, "name": "Book"}
    item_with_code = {"id": 2, "name": "Pen", "barcode": "987654321012"}
    assert get_item_barcode(item_with_code) == "987654321012"
    assert get_item_barcode(item_without_code) == "N/A"
    print("✓ Task 09 passed!")
