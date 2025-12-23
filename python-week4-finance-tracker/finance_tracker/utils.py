from datetime import datetime


# Allowed expense categories
CATEGORIES = [
    "Food",
    "Transport",
    "Entertainment",
    "Bills",
    "Shopping",
    "Health",
    "Other"
]


def validate_date(date_str):
    """
    Validate date format (YYYY-MM-DD)
    """
    try:
        datetime.strptime(date_str, "%Y-%m-%d")
        return True
    except ValueError:
        return False


def validate_amount(amount):
    """
    Validate expense amount
    """
    return amount > 0


def validate_category(category):
    """
    Validate expense category
    """
    return category in CATEGORIES
