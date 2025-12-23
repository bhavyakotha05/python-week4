from finance_tracker.expense import Expense


def test_expense_creation():
    """
    Test whether an Expense object is created correctly
    """
    expense = Expense(
        date="2025-01-15",
        amount=250,
        category="Food",
        description="Lunch"
    )

    assert expense.date == "2025-01-15"
    assert expense.amount == 250
    assert expense.category == "Food"
    assert expense.description == "Lunch"


def test_invalid_amount():
    """
    Test invalid expense amount
    """
    try:
        Expense(
            date="2025-01-15",
            amount=-100,
            category="Food",
            description="Invalid test"
        )
        assert False  # Should not reach here
    except ValueError:
        assert True
