# Salary Manager CLI

A simple Python CLI application to manage your monthly salary using popular budgeting rules such as **50/30/20**, inspired by Elizabeth Warren's financial method.

---

## Features

- Input your net monthly salary
- Choose from built-in budgeting ratios:
- 50/30/20 → Needs/Wants/Savings
- 70/20/10, 30/10/60, etc.
- See the allocation of your salary based on your choice
- Built with Python and **Object-Oriented Programming (OOP)**

---

## How to Run

1. Clone this repository:

```bash
git clone https://github.com/your-username/salary-manager.git
cd salary-manager
py 
```

##Project Structure

```bash
salary-manager/
├── main.py                  # Entry point
├── manager/
│   ├── salary_manager.py    # App controller class
│   ├── user_interface.py    # Handles CLI input/output
│   ├── ratio_loader.py      # Loads budget ratio from JSON
│   ├── calculator.py        # Handles calculation logic
│   └── __init__.py
└── data/
    └── ratios.json          # Default ratio definitions
```

## Future Plans

 - Custom ratio input
 - Data saving (history log)
 - GUI version with Tkinter
 - Expense tracker per category

 
Author
Created by samez
🔗 GitHub: samezid
