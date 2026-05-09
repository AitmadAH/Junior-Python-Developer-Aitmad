class Expense:
    """Represents a single expense entry."""

    def __init__(self, date: str, category: str, amount: float, description: str):
        self.date = date                        # Fixed: was 'data' (typo)
        self.category = category.strip().title()
        self.amount = float(amount)
        self.description = description.strip()

    def __str__(self) -> str:
        return (
            f"[{self.date}] {self.category}: "
            f"${self.amount:.2f} - {self.description}"
        )

    def __repr__(self) -> str:
        return (
            f"Expense(date='{self.date}', category='{self.category}', "
            f"amount={self.amount}, description='{self.description}')"
        )
