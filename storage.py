import json
from models import Expense


def save_expenses(expenses: list, filename: str = 'data.json') -> None:
    """Save a list of Expense objects to a JSON file."""
    expenses_data = []
    for expense in expenses:
        expenses_data.append({
            "date": expense.date,           # Fixed: was 'data' (typo)
            "category": expense.category,
            "amount": expense.amount,
            "description": expense.description
        })

    try:
        with open(filename, mode='w', encoding='utf-8') as file:
            json.dump(expenses_data, file, indent=4)
    except Exception as error:
        print(f"[!] Error saving data: {error}")


def load_expenses(filename: str = 'data.json') -> list:
    """Load Expense objects from a JSON file. Returns empty list if file missing."""
    expenses = []

    try:
        with open(filename, mode='r', encoding='utf-8') as file:
            data = json.load(file)

            for item in data:
                expenses.append(
                    Expense(
                        item["date"],       # Fixed: was 'data' (typo)
                        item["category"],
                        item["amount"],
                        item["description"]
                    )
                )

    except FileNotFoundError:
        return []                           # First run — no file yet, that's fine
    except (json.JSONDecodeError, KeyError) as error:
        print(f"[!] Corrupted data file: {error}")
        return []
    except Exception as error:
        print(f"[!] Error loading data: {error}")

    return expenses
