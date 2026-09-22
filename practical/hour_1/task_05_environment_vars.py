"""
PRACTICAL CHALLENGE: Environment Configuration and Debug Safety (FLASK-H1-P05)
=====================================================
ID: FLASK-H1-P05
Curriculum Tier: Beginner | Difficulty: Beginner
Task:
Implement `is_safe_for_production` such that it returns True only when debug mode is disabled ('0'), and False when debug mode is active ('1' or 'True').

Run this file with Python. Make any necessary changes so all assertion tests pass!
"""

def is_safe_for_production(debug_mode_value: str) -> bool:
    if debug_mode_value in ('1', 'True', 'true'):
        return False
    return True

if __name__ == '__main__':
    assert is_safe_for_production('1') is False, "Debug mode 1 is NOT safe for production"
    assert is_safe_for_production('0') is True, "Debug mode 0 IS safe for production"
    print("✓ Task 05 passed!")

# Done
