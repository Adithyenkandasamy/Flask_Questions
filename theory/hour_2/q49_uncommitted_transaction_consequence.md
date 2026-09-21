# FLASK-H2-T49: Uncommitted Transaction Consequence

> **Curriculum Path:** Hour 2 Theory → Level 7: Debugging Reasoning  
> **Difficulty:** `Advanced` | **Format:** `Multiple-Choice`  
> **Question ID:** `FLASK-H2-T49`  

---

### Question
What happens if you call `db.session.add(item)` but the script terminates before `db.session.commit()`?
A) Data is saved automatically on exit
B) The database is deleted
C) The staged changes are discarded and nothing is written to disk
D) A SyntaxError occurs
