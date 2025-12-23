import json
import csv
import os
from finance_tracker.expense import Expense


class FileHandler:
    """
    Handles all file operations:
    - Load expenses from JSON
    - Save expenses to JSON
    - Create backup
    - Export expenses to CSV
    """

    def __init__(self, manager):
        self.manager = manager
        self.data_file = "data/expenses.json"
        self.backup_dir = "data/backup"
        self.export_dir = "data/exports"

        os.makedirs(self.backup_dir, exist_ok=True)
        os.makedirs(self.export_dir, exist_ok=True)

    def load_data(self):
        """
        Load expense data from JSON file
        """
        if not os.path.exists(self.data_file):
            return

        try:
            with open(self.data_file, "r") as file:
                data = json.load(file)

                for item in data:
                    expense = Expense(
                        item["date"],
                        item["amount"],
                        item["category"],
                        item["description"]
                    )
                    self.manager.expenses.append(expense)

        except Exception as e:
            print(f"❌ Error loading data: {e}")

    def save_data(self):
        """
        Save expenses to JSON file with backup
        """
        try:
            self.create_backup()

            with open(self.data_file, "w") as file:
                json.dump(
                    self.manager.get_expenses_as_dict(),
                    file,
                    indent=4
                )

        except Exception as e:
            print(f"❌ Error saving data: {e}")

    def create_backup(self):
        """
        Create backup before saving data
        """
        if os.path.exists(self.data_file):
            backup_file = os.path.join(
                self.backup_dir,
                "expenses_backup.json"
            )
            with open(self.data_file, "r") as original:
                with open(backup_file, "w") as backup:
                    backup.write(original.read())

    def export_to_csv(self):
        """
        Export expenses to CSV file
        """
        try:
            csv_file = os.path.join(
                self.export_dir,
                "expenses_export.csv"
            )

            with open(csv_file, "w", newline="") as file:
                writer = csv.DictWriter(
                    file,
                    fieldnames=["date", "amount", "category", "description"]
                )
                writer.writeheader()
                writer.writerows(
                    self.manager.get_expenses_as_dict()
                )

            print("✅ Expenses exported to CSV successfully!")

        except Exception as e:
            print(f"❌ Error exporting CSV: {e}")
