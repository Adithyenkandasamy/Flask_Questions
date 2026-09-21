"""
PRACTICAL CHALLENGE: Short-Circuiting Authentication Verification (FLASK-H5-P06)
=====================================================
ID: FLASK-H5-P06
Curriculum Tier: Integration | Difficulty: Advanced
Task:
Authenticate user credentials by verifying the user exists before calling password hash verification.

Run this file with Python. Make any necessary changes so all assertion tests pass!
"""

def authenticate(user_lookup_func, username, password) -> bool:
    user = user_lookup_func(username)
    return user.check_password(password)

class MockUser:
    def check_password(self, p):
        return p == "pass"

def mock_find(u):
    return MockUser() if u == "valid" else None

if __name__ == '__main__':
    assert authenticate(mock_find, "valid", "pass") is True
    assert authenticate(mock_find, "invalid", "pass") is False
    print("✓ Task 66 passed!")
