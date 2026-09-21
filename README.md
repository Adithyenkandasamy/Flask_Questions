# Flask Questions & Practice Repository

A comprehensive, structured curriculum of **360 Individual Theory Question Files** and **90 Practical Python Challenge Files** based directly on the full course tutorial and the official [FlaskSeries/](FlaskSeries/) source code repository (Parts 01 through 16).

> 📺 **Video Link**: [Python Flask Tutorial - Full Course for Beginners](https://www.youtube.com/watch?v=Qr4QMBUPxWo)  
> 💻 **Source Code Reference**: [FlaskSeries/](FlaskSeries/) (Parts 01 through 16)  
> 💡 **Solutions Repository**: [Adithyenkandasamy/Flask_Answers](https://github.com/Adithyenkandasamy/Flask_Answers)  

---

## 🗂️ Curriculum Overview: Theory & Practical per Hour

| Hour & Course Chapters | Theory Questions (60/hr) | Master Catalog | Practical Challenges (15/hr) | Official Source Reference |
| :--- | :---: | :---: | :---: | :---: |
| **Hour 1**: Basics, Routing & Templates | [📝 Hour 1 Directory](theory/hour_1/) | [📖 Hour 1 Catalog](theory/hour_1.md) | [💻 Tasks 01–15](practical/hour_1/) | [📂 Parts 01 – 03](FlaskSeries/) |
| **Hour 2**: Inheritance & SQLAlchemy | [📝 Hour 2 Directory](theory/hour_2/) | [📖 Hour 2 Catalog](theory/hour_2.md) | [💻 Tasks 16–30](practical/hour_2/) | [📂 Parts 04 – 05](FlaskSeries/) |
| **Hour 3**: Packages & Model Relations | [📝 Hour 3 Directory](theory/hour_3/) | [📖 Hour 3 Catalog](theory/hour_3.md) | [💻 Tasks 31–45](practical/hour_3/) | [📂 Parts 06 – 07](FlaskSeries/) |
| **Hour 4**: Forms, Validation & Flashing | [📝 Hour 4 Directory](theory/hour_4/) | [📖 Hour 4 Catalog](theory/hour_4.md) | [💻 Tasks 46–60](practical/hour_4/) | [📂 Parts 08 – 10](FlaskSeries/) |
| **Hour 5**: Bcrypt & User Authentication | [📝 Hour 5 Directory](theory/hour_5/) | [📖 Hour 5 Catalog](theory/hour_5.md) | [💻 Tasks 61–75](practical/hour_5/) | [📂 Parts 11 – 13](FlaskSeries/) |
| **Hour 6**: Market Logic & Modals | [📝 Hour 6 Directory](theory/hour_6/) | [📖 Hour 6 Catalog](theory/hour_6.md) | [💻 Tasks 76–90](practical/hour_6/) | [📂 Parts 14 – 16](FlaskSeries/) |

---

## 📂 Repository Architecture

```text
Flask_Questions/
├── README.md                      # Master repository guide and curriculum index
├── FlaskSeries/                   # Official source code stages (01 – 16)
│   ├── 01 - Introduction/
│   ├── 02 - Styling and Templates/
│   ├── 03 - Sending Data to Templates/
│   ├── 04 - Template Inheritance/
│   ├── 05 - Models and Databases/
│   ├── 06 - Project Restructure/
│   ├── 07 - Model Relationships/
│   ├── 08 - Flask Forms/
│   ├── 09 - Flask Validations/
│   ├── 10 - Flash Messages & Advanced Validations/
│   ├── 11 - User Authentication Part 1/
│   ├── 12 - User Authentication Part 2/
│   ├── 13 - Logout & Customizations/
│   ├── 14 - Item Purchasing Part 1/
│   ├── 15 - Item Purchasing Part 2/
│   └── 16 - Item Selling/
├── theory/
│   ├── hour_1/ to hour_6/         # 360 separate markdown files (q01_....md to q60_....md)
│   ├── hour_1.md to hour_6.md     # Master catalog files indexing each hour's questions
│   └── hour_1/README.md to hour_6/README.md
└── practical/
    ├── hour_1/                    # Tasks 01–15: app setup, routes, dynamic params, Jinja data, filters
    ├── hour_2/                    # Tasks 16–30: url_for, SQLite URIs, models, commits, rollbacks, queries
    ├── hour_3/                    # Tasks 31–45: packages, foreign keys, backref, relationships, cascades
    ├── hour_4/                    # Tasks 46–60: secret keys, POST methods, field validators, flashing
    ├── hour_5/                    # Tasks 61–75: bcrypt hashing, setters, login manager, @login_required
    ├── hour_6/                    # Tasks 76–90: budget checks, ownership transfers, sell refunds, modals
    └── hour_1/README.md to hour_6/README.md
```

---

## 🎯 How to Use This Repository

### 1. Theory Practice (Clean, Modular & Focused)
- Navigate into any hour folder under [`theory/`](theory/), e.g. [`theory/hour_1/`](theory/hour_1/).
- Open any individual question file (e.g. [`q01_framework_classification.md`](theory/hour_1/q01_framework_classification.md)) to practice concept retention with zero spoilers.
- You can also view the full hour catalogs in [`theory/hour_1.md`](theory/hour_1.md) through [`theory/hour_6.md`](theory/hour_6.md) for quick reference.

### 2. Practical Python Challenges
- Every task in [`practical/`](practical/) is a runnable standalone Python file.
- Each challenge specifies clear requirements based directly on the `FlaskSeries` architecture.
- Challenges contain **zero spoiler comments** or bug markers—diagnose and complete the implementation based on the task description and assertion tests.
- Run a task using Python:
  ```bash
  python practical/hour_1/task_01_app_initialization.py
  ```
- Edit the file to complete the implementation until all assertion tests pass and output `✓ Task XX passed!`.

---

## 💡 Solutions Repository

To maintain a true test/learning environment with zero spoilers in this repository, all reference solutions are maintained in the separate companion repository:
👉 **[Flask_Answers](https://github.com/Adithyenkandasamy/Flask_Answers)**
