"""
PRACTICAL CHALLENGE: Data Formatting for Jinja Loops (FLASK-H1-P08)
=====================================================
ID: FLASK-H1-P08
Curriculum Tier: Beginner | Difficulty: Beginner
Task:
Format the catalog records so that each item dictionary contains 'id', 'name', 'barcode' (12 digits), and 'price' keys.

Run this file with Python. Make any necessary changes so all assertion tests pass!
"""

items = [
    {"id": 1, "name": "Phone", "barcode": "123456789012", "price": 500},
    {"id": 2, "name": "Laptop", "price": 900}
]

def format_items(raw_items):
    formatted = []
    for item in raw_items:
        formatted.append({
            "id": item["id"],
            "name": item["name"],
            "barcode": item.get("barcode", "123456789012"),
            "price": item["price"]
        })
    return formatted

if __name__ == '__main__':
    out = format_items(items)
    for row in out:
        assert "barcode" in row
        assert len(row["barcode"]) == 12, "Barcode must be 12 digits"
    print("✓ Task 08 passed!")
