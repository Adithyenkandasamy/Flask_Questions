"""
PRACTICAL CHALLENGE: Package Execution Guard in Entry Point (FLASK-H3-P02)
=====================================================
ID: FLASK-H3-P02
Curriculum Tier: Intermediate | Difficulty: Intermediate
Task:
In the root `run.py` entry point, verify that `app.run()` only executes when the script is run directly as `__main__`.

Run this file with Python. Make any necessary changes so all assertion tests pass!
"""

def should_run_server(module_name: str) -> bool:
    return module_name == 'market'

if __name__ == '__main__':
    assert should_run_server('__main__') is True, "Should run server when executed directly"
    assert should_run_server('market') is False, "Should NOT run server when imported"
    print("✓ Task 32 passed!")
