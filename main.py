import json
import os

class Expense:

    def __init__(self, date, category, amount, description):
        self.date = date
        self.category = category
        self.amount = amount
        self.description = description

    def __str__(self):
        return (
            f"Date: {self.date} | "
            f"Category: {self.category} | "
            f"Amount: ${self.amount:.2f} | "
            f"Description: {self.description}"
        )


if __name__ == '__main__':
    # Create example Expense objects
    expense1 = Expense(
        date="2026-04-23",
        category="Food",
        amount=12.50,
        description="Lunch at restaurant"
    )

    expense2 = Expense(
        date="2026-04-22",
        category="Transport",
        amount=3.75,
        description="Bus fare"
    )

    # Print expense details
    print(expense1)
    print(expense2)

class Expense:
    """
    A class to represent a personal financial expense.
    """
    def __init__(self, date: str, category: str, amount: float, description: str):
        self.date = date
        self.category = category
        self.amount = amount
        self.description = description

    def __str__(self):
        return f"[{self.date}] {self.category.capitalize()}: ${self.amount:.2f} - {self.description}"


def save_expenses(expenses: list, filename: str = 'data.json') -> None:
    """
    Serializes a list of Expense objects into dictionaries and saves them to a JSON file.
    """
    # Convert the list of Expense objects into a list of dictionaries
    expenses_data = []
    for expense in expenses:
        expenses_data.append({
            "date": expense.date,
            "category": expense.category,
            "amount": expense.amount,
            "description": expense.description
        })

    # Save the dictionary data to the JSON file safely
    try:
        with open(filename, mode='w', encoding='utf-8') as file:
            json.dump(expenses_data, file, indent=4)
        print(f"[*] Successfully saved {len(expenses)} expense(s) to '{filename}'.")
    except Exception as error:
        print(f"[!] An unexpected error occurred while saving: {error}")


def load_expenses(filename: str = 'data.json') -> list:
    """
    Reads a JSON file, deserializes the data, and converts it back into a list of Expense objects.
    Gracefully handles the scenario where the file does not exist yet.
    """
    loaded_expenses = []

    try:
        with open(filename, mode='r', encoding='utf-8') as file:
            expenses_data = json.load(file)
            
            # Convert each dictionary back into an Expense object
            for item in expenses_data:
                expense_obj = Expense(
                    date=item["date"],
                    category=item["category"],
                    amount=item["amount"],
                    description=item["description"]
                )
                loaded_expenses.append(expense_obj)
                
        print(f"[*] Successfully loaded {len(loaded_expenses)} expense(s) from '{filename}'.")
        
    except FileNotFoundError:
        # Graceful failure if the program is run for the very first time
        print(f"[!] '{filename}' not found. Returning an empty expense list to start fresh.")
    except json.JSONDecodeError:
        print(f"[!] '{filename}' contains invalid JSON data. Returning an empty expense list.")
    except Exception as error:
        print(f"[!] An unexpected error occurred while loading: {error}")

    return loaded_expenses


def main():
    """Main execution block to test the storage engine."""
    test_filename = 'data.json'
    
    print("--- Testing Storage Engine ---")
    
    # 1. Instantiate dummy Expense objects
    expense1 = Expense("2026-04-24", "Food", 25.50, "Lunch at cafe")
    expense2 = Expense("2026-04-24", "Transport", 15.00, "Uber ride home")
    my_expenses = [expense1, expense2]

    # 2. Save the expenses to data.json
    save_expenses(my_expenses, test_filename)

    # 3. Load the expenses back from data.json
    retrieved_expenses = load_expenses(test_filename)

    # 4. Print the retrieved objects to prove they were properly converted back to Expense instances
    print("\n--- Retrieved Expenses ---")
    for exp in retrieved_expenses:
        print(exp)


if __name__ == '__main__':
    main()