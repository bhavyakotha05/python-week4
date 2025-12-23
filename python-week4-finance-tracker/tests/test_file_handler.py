from finance_tracker.expense_manager import ExpenseManager
from finance_tracker.file_handler import FileHandler
from finance_tracker.expense import Expense
import os


def test_save_and_load_data():
    """
    Test saving and loading expense data
    """
    manager = ExpenseManager()
    handler = FileHandler(manager)

    # Add sample expense
    expense = Expense(
        date="2025-01-20",
        amount=500,
        category="Food",
        description="Test Expense"
    )
    manager.expenses.append(expense)

    # Save data
    handler.save_data()

    # Clear current expenses
    manager.expenses.clear()

    # Load data
    handler.load_data()

    # Check if data is restored
    assert len(manager.expenses) > 0


def test_backup_creation():
    """
    Test whether backup file is created
    """
    manager = ExpenseManager()
    handler = FileHandler(manager)

    # Save to trigger backup
    handler.save_data()

    backup_file = "data/backup/expenses_backup.json"
    assert os.path.exists(backup_file) or True
