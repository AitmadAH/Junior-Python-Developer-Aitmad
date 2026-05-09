from datetime import date as today_date


def calculate_total_spent(expenses: list) -> float:   # Fixed: was 'Float' (invalid)
    """Return the sum of all expense amounts."""
    return sum(expense.amount for expense in expenses)


# Alias so tests can import either name
calculate_total = calculate_total_spent


def calculate_total_by_category(expenses: list, category: str) -> float:  # Fixed: Float → float
    """Return the sum of expenses matching the given category (case-insensitive)."""
    return sum(
        expense.amount
        for expense in expenses
        if expense.category.lower() == category.strip().lower()
    )


# Alias so tests can import either name
calculate_by_category = calculate_total_by_category


def calculate_monthly_total(expenses: list, year: int = None, month: int = None) -> float:
    """Return total spent in a specific month/year (defaults to current month)."""
    if year is None:
        year = today_date.today().year
    if month is None:
        month = today_date.today().month

    total = 0.0
    for expense in expenses:
        try:
            parts = expense.date.split("-")
            exp_year, exp_month = int(parts[0]), int(parts[1])
            if exp_year == year and exp_month == month:
                total += expense.amount
        except (ValueError, IndexError):
            continue  # Skip expenses with invalid date format
    return total


def get_category_summary(expenses: list) -> dict:
    """Return a dict of {category: total_amount} for all expenses."""
    summary = {}
    for expense in expenses:
        cat = expense.category
        summary[cat] = summary.get(cat, 0.0) + expense.amount
    return summary
