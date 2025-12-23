from datetime import datetime


class Expense:
    """
    Expense Model Class

    Represents a single expense entry with basic validation.
    """

    def __init__(self, date, amount, category, description):
        self.date = self.validate_date(date)
        self.amount = self.validate_amount(amount)
        self.category = category
        self.description = description

    def validate_date(self, date_str):
        """
        Validate and return date in YYYY-MM-DD format
        """
        try:
            datetime.strptime(date_str, "%Y-%m-%d")
            return date_str
        except ValueError:
            raise ValueError("Invalid date format. Use YYYY-MM-DD")

    def validate_amount(self, amount):
        """
        Validate expense amount
        """
        if amount <= 0:
            raise ValueError("Amount must be greater than zero")
        return amount

    def to_dict(self):
        """
        Convert Expense object to dictionary (for JSON storage)
        """
        return {
            "date": self.date,
            "amount": self.amount,
            "category": self.category,
            "description": self.description
        }
