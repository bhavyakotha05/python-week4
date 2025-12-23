from finance_tracker.expense_manager import ExpenseManager
from finance_tracker.reports import Reports
from finance_tracker.file_handler import FileHandler


class FinanceTracker:
    def __init__(self):
        self.manager = ExpenseManager()
        self.reports = Reports(self.manager)
        self.file_handler = FileHandler(self.manager)

        # Load saved expenses on startup
        self.file_handler.load_data()

    def run(self):
        while True:
            print("\n" + "=" * 45)
            print("        PERSONAL FINANCE TRACKER")
            print("=" * 45)
            print("1. Add Expense")
            print("2. View All Expenses")
            print("3. Monthly Expense Report")
            print("4. Category-wise Report")
            print("5. Export Expenses to CSV")
            print("0. Exit")
            print("=" * 45)

            choice = input("Enter your choice: ").strip()

            if choice == "1":
                self.manager.add_expense()

            elif choice == "2":
                self.manager.view_expenses()

            elif choice == "3":
                self.reports.monthly_report()

            elif choice == "4":
                self.reports.category_report()

            elif choice == "5":
                self.file_handler.export_to_csv()

            elif choice == "0":
                self.file_handler.save_data()
                print("\nThank you for using Personal Finance Tracker!")
                break

            else:
                print("Invalid choice! Please try again.")


def main():
    app = FinanceTracker()
    app.run()


if __name__ == "__main__":
    main()
