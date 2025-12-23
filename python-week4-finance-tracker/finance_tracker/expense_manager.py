from finance_tracker.expense import Expense


class ExpenseManager:
    """
    Handles all expense related operations
    (Add, View, Store in memory)
    """

    def __init__(self):
        self.expenses = []

    def add_expense(self):
        """
        Add a new expense with validation
        """
        print("\n--- ADD NEW EXPENSE ---")

        try:
            date = input("Enter date (YYYY-MM-DD): ").strip()
            amount = float(input("Enter amount: "))
            category = input("Enter category (Food/Transport/Bills/etc): ").strip()
            description = input("Enter description: ").strip()

            expense = Expense(date, amount, category, description)
            self.expenses.append(expense)

            print("✅ Expense added successfully!")

        except ValueError as e:
            print(f"❌ Error: {e}")

    def view_expenses(self):
        """
        Display all expenses
        """
        print("\n--- ALL EXPENSES ---")

        if not self.expenses:
            print("No expenses recorded.")
            return

        for idx, expense in enumerate(self.expenses, start=1):
            print(f"{idx}. {expense.date} | ₹{expense.amount} | "
                  f"{expense.category} | {expense.description}")

    def get_expenses_as_dict(self):
        """
        Return all expenses as list of dictionaries
        (used for file saving and reporting)
        """
        return [expense.to_dict() for expense in self.expenses]
