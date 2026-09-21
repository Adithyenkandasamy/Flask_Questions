# Flask Questions & Answers Study Repository

A complete, structured curriculum of **360 Individual Theory Question Files** and **90 Practical Python Challenge Files** based directly on the full course tutorial and the official [FlaskSeries](FlaskSeries/) source code repository (Parts 01 to 16).

> 📺 **Video Link**: [Python Flask Tutorial - Full Course for Beginners](https://www.youtube.com/watch?v=Qr4QMBUPxWo)  
> 💻 **Official Course Stages**: [FlaskSeries/](FlaskSeries/) (Parts 01 through 16)  
> 📁 **Structure**: Both `questions/` and `answers/` are split into **`theory/`** (60 individual question files per hour) and **`practical/`** (15 runnable Python challenge files per hour) across all 6 hours of the course.

---

## 🗂️ Curriculum Overview: Theory & Practical per Hour

| Hour & Course Chapters | Theory Questions (60/hr in separate files) | Theory Answers (1:1 matching files) | Practical Challenges (15/hr) | Practical Solutions (100% tested) |
| :--- | :---: | :---: | :---: | :---: |
| **Hour 1**: Basics, Routing & Templates<br>*(FlaskSeries 01 – 03)* | [📝 Hour 1 Directory](questions/theory/hour_1/) | [💡 Hour 1 Answers](answers/theory/hour_1/) | [💻 Tasks 01–15](questions/practical/hour_1/) | [✅ Solutions 01–15](answers/practical/hour_1/) |
| **Hour 2**: Inheritance & SQLAlchemy<br>*(FlaskSeries 04 – 05)* | [📝 Hour 2 Directory](questions/theory/hour_2/) | [💡 Hour 2 Answers](answers/theory/hour_2/) | [💻 Tasks 16–30](questions/practical/hour_2/) | [✅ Solutions 16–30](answers/practical/hour_2/) |
| **Hour 3**: Packages & Model Relations<br>*(FlaskSeries 06 – 07)* | [📝 Hour 3 Directory](questions/theory/hour_3/) | [💡 Hour 3 Answers](answers/theory/hour_3/) | [💻 Tasks 31–45](questions/practical/hour_3/) | [✅ Solutions 31–45](answers/practical/hour_3/) |
| **Hour 4**: Forms, Validation & Flashing<br>*(FlaskSeries 08 – 10)* | [📝 Hour 4 Directory](questions/theory/hour_4/) | [💡 Hour 4 Answers](answers/theory/hour_4/) | [💻 Tasks 46–60](questions/practical/hour_4/) | [✅ Solutions 46–60](answers/practical/hour_4/) |
| **Hour 5**: Bcrypt & User Authentication<br>*(FlaskSeries 11 – 13)* | [📝 Hour 5 Directory](questions/theory/hour_5/) | [💡 Hour 5 Answers](answers/theory/hour_5/) | [💻 Tasks 61–75](questions/practical/hour_5/) | [✅ Solutions 61–75](answers/practical/hour_5/) |
| **Hour 6**: Market Logic & Modals<br>*(FlaskSeries 14 – 16)* | [📝 Hour 6 Directory](questions/theory/hour_6/) | [💡 Hour 6 Answers](answers/theory/hour_6/) | [💻 Tasks 76–90](questions/practical/hour_6/) | [✅ Solutions 76–90](answers/practical/hour_6/) |

---

## 📂 Repository Architecture

```text
Flask_Questions/
├── README.md
├── FlaskSeries/                   # Official source code stages (01 – 16)
├── questions/
│   ├── theory/
│   │   ├── hour_1/ to hour_6/     # 360 separate markdown files (q01_....md to q60_....md)
│   │   ├── hour_1.md to hour_6.md # Master index catalogs linking to each separate question file
│   └── practical/
│       ├── hour_1/                # Tasks 01–15: app setup, routes, dynamic params, Jinja data, filters
│       ├── hour_2/                # Tasks 16–30: url_for, SQLite URIs, models, commits, rollbacks, queries
│       ├── hour_3/                # Tasks 31–45: packages, foreign keys, backref, relationships, cascades
│       ├── hour_4/                # Tasks 46–60: secret keys, POST methods, field validators, flashing
│       ├── hour_5/                # Tasks 61–75: bcrypt hashing, setters, login manager, @login_required
│       └── hour_6/                # Tasks 76–90: budget checks, ownership transfers, sell refunds, modals
└── answers/
    ├── theory/
    │   ├── hour_1/ to hour_6/     # 360 separate solution files (matching question filenames 1:1)
    │   └── hour_1.md to hour_6.md # Master index catalogs linking to each separate answer file
    └── practical/
        ├── hour_1/ to hour_6/     # 90 working, 100% verified Python solution files
```

---

## 🛠️ Standalone, Decoupled Architecture

This repository is designed with **complete decoupling** between questions and answers so they can exist independently in separate GitHub repositories (e.g. a public repository for learners and an instructor/solutions repository):

1. **`questions/` (Learner Repository Ready)**:
   - Contains **360 individual theory question files** (60 per hour) and **90 practical Python challenge files** (15 per hour).
   - Completely free of spoilers, bug tags, solution links, or external dependencies.
   - Contains zero links to the `answers/` directory.

2. **`answers/` (Solutions Repository Ready)**:
   - Contains **360 individual theory answer files** and **90 verified practical Python solution files**.
   - **100% Self-Contained**: Each theory answer file includes the original question statement, direct answer, in-depth explanation, code snippet, and common pitfalls.
   - Each practical Python solution file contains the complete task description, explanation, and verified working code.
   - Zero links back to the `questions/` directory and zero previous/next chain links. You can copy the entire `answers/` folder to an independent GitHub repository and every file will remain fully contextual and functional.

---

## 🚀 How to Use

### 1. Theory Workflow
- Open any individual question file in [`questions/theory/hour_X/`](questions/theory/).
- Each question is isolated in its own file (e.g. `q01_framework_classification.md`) with clean formatting and no spoilers.
- The corresponding answer file in `answers/theory/hour_X/` has the exact same filename and includes both the original question and the comprehensive answer guide.

### 2. Practical Python Coding & Challenges
- Every task in [`questions/practical/`](questions/practical/) is a runnable standalone Python file.
- Challenges contain **zero spoiler comments** or bug markers—diagnose and complete the implementation based on the task description and assertion tests.
- Run a task using Python:
  ```bash
  python questions/practical/hour_1/task_01_app_initialization.py
  ```
- Edit the file to complete the implementation until all assertion tests pass and output `✓ Task XX passed!`.
- The matching solution in `answers/practical/hour_X/` provides the verified reference implementation (100% tested with 90/90 pass rate).

