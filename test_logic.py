import unittest
from models import Expense
from business import calculate_total, calculate_by_category, calculate_monthly_total
# Fixed: test now imports the correct aliased names that business.py exports


class TestFinanceLogic(unittest.TestCase):

    def setUp(self):
        """Create a shared set of mock expenses used by every test."""
        self.expense1 = Expense("2026-05-01", "Food", 15.00, "Lunch")
        self.expense2 = Expense("2026-05-02", "Transport", 20.00, "Bus")
        self.expense3 = Expense("2026-05-03", "Food", 10.00, "Coffee")
        self.expense4 = Expense("2026-04-15", "Food", 50.00, "Groceries")  # Different month

        self.my_expenses = [
            self.expense1,
            self.expense2,
            self.expense3,
            self.expense4,
        ]

    # ── Test 1 ───────────────────────────────────────────────────────────────
    def test_calculate_total(self):
        """Total of all expenses should be 15 + 20 + 10 + 50 = 95."""
        result = calculate_total(self.my_expenses)
        self.assertEqual(result, 95.00)

    # ── Test 2 ───────────────────────────────────────────────────────────────
    def test_calculate_by_category_food(self):
        """Food total = 15 (Lunch) + 10 (Coffee) + 50 (Groceries) = 75."""
        result = calculate_by_category(self.my_expenses, "Food")
        self.assertEqual(result, 75.00)

    # ── Test 3 ───────────────────────────────────────────────────────────────
    def test_calculate_by_category_empty(self):
        """A category with no matching expenses should return 0.00."""
        result = calculate_by_category(self.my_expenses, "Entertainment")
        self.assertEqual(result, 0.00)

    # ── Bonus Test 4 ─────────────────────────────────────────────────────────
    def test_calculate_monthly_total(self):
        """Only May 2026 expenses should count: 15 + 20 + 10 = 45."""
        result = calculate_monthly_total(self.my_expenses, year=2026, month=5)
        self.assertEqual(result, 45.00)

    # ── Bonus Test 5 ─────────────────────────────────────────────────────────
    def test_category_is_case_insensitive(self):
        """Category matching must be case-insensitive: 'food' == 'Food'."""
        result = calculate_by_category(self.my_expenses, "food")
        self.assertGreater(result, 0)


if __name__ == '__main__':
    unittest.main(verbosity=2)
