from collections import defaultdict


class Reports:
    """
    Generates analytical reports from expense data
    """

    def __init__(self, manager):
        self.manager = manager

    def monthly_report(self):
        """
        Generate total monthly expense report
        """
        if not self.manager.expenses:
            print("No expenses available.")
            return

        total = sum(expense.amount for expense in self.manager.expenses)

        print("\n--- MONTHLY EXPENSE REPORT ---")
        print(f"Total Expenses: ₹{total}")

    def category_report(self):
        """
        Generate category-wise expense breakdown
        """
        if not self.manager.expenses:
            print("No expenses available.")
            return

        category_totals = defaultdict(float)

        for expense in self.manager.expenses:
            category_totals[expense.category] += expense.amount

        print("\n--- CATEGORY-WISE EXPENSE REPORT ---")
        for category, amount in category_totals.items():
            print(f"{category}: ₹{amount}")

    def statistics(self):
        """
        Display expense statistics
        """
        if not self.manager.expenses:
            print("No expenses available.")
            return

        amounts = [expense.amount for expense in self.manager.expenses]

        print("\n--- EXPENSE STATISTICS ---")
        print(f"Total Expenses: ₹{sum(amounts)}")
        print(f"Highest Expense: ₹{max(amounts)}")
        print(f"Lowest Expense: ₹{min(amounts)}")
        print(f"Average Expense: ₹{sum(amounts) / len(amounts):.2f}")
