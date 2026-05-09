from models import Expense
from storage import save_expenses, load_expenses
from business import (
    calculate_total_spent,
    calculate_total_by_category,
)


def display_menu():
    print("\n===== Personal Finance Manager =====")
    print("1. Add Expense")
    print("2. View Total Spending")
    print("3. View Spending by Category")
    print("4. Exit")


def main():
    expenses = load_expenses()

    while True:
        display_menu()
        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            date = input("Enter date (YYYY-MM-DD): ")
            category = input("Enter category: ")

            try:
                amount = float(input("Enter amount: "))
            except ValueError:
                print("Invalid amount!")
                continue

            description = input("Enter description: ")

            expense = Expense(date, category, amount, description)
            expenses.append(expense)

            save_expenses(expenses)
            print("Expense added!")

        elif choice == "2":
            total = calculate_total_spent(expenses)
            print(f"Total Spending: ${total:.2f}")

        elif choice == "3":
            category = input("Enter category: ")
            total = calculate_total_by_category(expenses, category)
            print(f"Total for '{category}': ${total:.2f}")

        elif choice == "4":
            print("Goodbye!")
            break

        else:
            print("Invalid choice!")


if __name__ == "__main__":
    main()