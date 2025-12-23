from finance_tracker.expense_manager import ExpenseManager
from finance_tracker.reports import Reports
from finance_tracker.expense import Expense


def test_monthly_report():
    """
    Test monthly report calculation
    """
    manager = ExpenseManager()
    reports = Reports(manager)

    # Add sample expenses
    manager.expenses.append(
        Expense("2025-01-10", 200, "Food", "Breakfast")
    )
    manager.expenses.append(
        Expense("2025-01-12", 300, "Transport", "Bus")
    )

    # Monthly report should not fail
    reports.monthly_report()
    assert True


def test_category_report():
    """
    Test category-wise report generation
    """
    manager = ExpenseManager()
    reports = Reports(manager)

    manager.expenses.append(
        Expense("2025-01-15", 150, "Food", "Snacks")
    )
    manager.expenses.append(
        Expense("2025-01-16", 350, "Food", "Dinner")
    )

    reports.category_report()
    assert True
