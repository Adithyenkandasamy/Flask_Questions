"""
PRACTICAL CHALLENGE: Path Route Converter for Multi-Segment URLs (FLASK-H1-P15)
=====================================================
ID: FLASK-H1-P15
Curriculum Tier: Beginner | Difficulty: Beginner
Task:
Configure a route '/files/<path:filepath>' to match multiple path segments including slashes.

Run this file with Python. Make any necessary changes so all assertion tests pass!
"""

from flask import Flask

app = Flask(__name__)

@app.route("/files/<filepath>")
def get_file(filepath):
    return f"Path: {filepath}"

def test_path():
    with app.test_client() as client:
        res = client.get('/files/docs/readme.txt')
        assert res.status_code == 200
        assert b"Path: docs/readme.txt" in res.data

if __name__ == '__main__':
    test_path()
    print("✓ Task 15 passed!")
