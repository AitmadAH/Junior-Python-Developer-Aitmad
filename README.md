# 💰 Personal Finance Manager

A command-line application to track your daily expenses, built with Python.
This is a Capstone Project completed as part of a structured Python learning roadmap (Days 23–27).

---

## 📋 Table of Contents

- [Features](#features)
- [Project Structure](#project-structure)
- [Requirements](#requirements)
- [Installation](#installation)
- [How to Run](#how-to-run)
- [How to Run Tests](#how-to-run-tests)
- [Usage Guide](#usage-guide)
- [Technologies Used](#technologies-used)

---

## ✨ Features

- ➕ Add expenses with date, category, amount, and description
- 📋 View all recorded expenses
- 💵 View total spending across all expenses
- 📂 Filter spending by category (e.g. Food, Transport)
- 📊 View a full category summary
- 📅 View total spending for the current month
- 💾 Data is saved automatically to `data.json` (persists after closing)
- ✅ Input validation — the app won't crash on invalid input

---

## 🗂️ Project Structure

```
personal_finance_manager/
│
├── main.py          # Entry point — CLI menu and user interaction
├── models.py        # Expense class (OOP model)
├── business.py      # Business logic — calculations and summaries
├── storage.py       # Save and load expenses from data.json
├── test_logic.py    # Automated unit tests (unittest)
├── data.json        # Auto-generated expense storage file
├── .gitignore       # Git ignore rules
└── README.md        # This file
```

---

## ⚙️ Requirements

- Python **3.8 or higher**
- No external libraries needed — uses Python standard library only

Check your Python version:
```bash
python --version
```

---

## 🚀 Installation

### Step 1 — Clone the repository
```bash
git clone https://github.com/your-username/personal_finance_manager.git
cd personal_finance_manager
```

### Step 2 — Create a Virtual Environment
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Mac / Linux
python3 -m venv venv
source venv/bin/activate
```

### Step 3 — Install dependencies
```bash
pip install -r requirements.txt
```
> ℹ️ This project uses only the Python standard library, so no packages are required.

---

## ▶️ How to Run

```bash
python main.py
```

You will see this menu:

```
========================================
   💰 Personal Finance Manager
========================================
1. Add Expense
2. View All Expenses
3. View Total Spending
4. View Spending by Category
5. View Category Summary
6. View This Month's Total
7. Exit
========================================
```

---

## 🧪 How to Run Tests

```bash
python test_logic.py
```

Expected output:

```
test_calculate_by_category_empty ... ok
test_calculate_by_category_food  ... ok
test_calculate_monthly_total     ... ok
test_calculate_total             ... ok
test_category_is_case_insensitive... ok

----------------------------------------------------------------------
Ran 5 tests in 0.001s

OK
```

---

## 📖 Usage Guide

### Adding an Expense
```
Enter date (YYYY-MM-DD): 2026-05-09
Enter category (e.g. Food, Transport): Food
Enter amount: 250
Enter description: Dinner at restaurant
✅ Expense added: [2026-05-09] Food: $250.00 - Dinner at restaurant
```

### Viewing by Category
```
Enter category to filter: Food
📂 Total for 'Food': $750.00
```

---

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python 3 | Core programming language |
| `json` module | Data storage and retrieval |
| `unittest` module | Automated testing |
| `re` module | Date format validation |
| Git | Version control |

---

## 👨‍💻 Author

**Aitmad Ahmed**
- GitHub: [@AitmadAhmed](https://github.com/AitmadAhmed)

---

## 📅 Project Timeline

| Day | Topic |
|---|---|
| Day 23 | Project setup + Expense class (OOP) |
| Day 24 | Storage engine (save/load JSON) |
| Day 25 | Business logic (calculations) |
| Day 26 | CLI interface (main.py) |
| Day 27 | Unit testing (unittest) |
| Day 28 | README + Polish |
