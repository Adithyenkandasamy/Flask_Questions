"""
PRACTICAL CHALLENGE: Iterating Form Validation Error Messages (FLASK-H4-P09)
=====================================================
ID: FLASK-H4-P09
Curriculum Tier: Advanced | Difficulty: Advanced
Task:
Extract all validation error messages from `form.errors` into a flat list of strings for display.

Run this file with Python. Make any necessary changes so all assertion tests pass!
"""

errors_dict = {
    "username": ["Username is required.", "Username too short."],
    "password": ["Password is required."]
}

def extract_all_errors(errors: dict) -> list:
    out = []
    for k in errors:
        out.append(k)
    return out

if __name__ == '__main__':
    res = extract_all_errors(errors_dict)
    assert "Username is required." in res
    assert "Username too short." in res
    assert "Password is required." in res
    print("✓ Task 54 passed!")
