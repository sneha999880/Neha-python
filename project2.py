import json
import os

# File to save expenses
FILE_NAME = "expenses.json"

# Load existing expenses from the file
def load_expenses():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    return []

# Save expenses to the file
def save_expenses(expenses):
    with open(FILE_NAME, "w") as file:
        json.dump(expenses, file, indent=4)

# Add a new expense
def add_expense(expenses):
    category = input("Enter the category (e.g., Food, Travel, Shopping): ").strip()
    amount = float(input("Enter the amount: ").strip())
    description = input("Enter a description (optional): ").strip()

    expense = {
        "category": category,
        "amount": amount,
        "description": description
    }
    expenses.append(expense)
    save_expenses(expenses)
    print("Expense added successfully!")

# View all expenses
def view_expenses(expenses):
    if not expenses:
        print("No expenses found.")
        return

    total = 0
    print("\n--- Expense List ---")
    for idx, expense in enumerate(expenses, 1):
        print(f"{idx}. {expense['category']} - Rs{expense['amount']:.2f} {expense['description']}")
        total += expense["amount"]
    print(f"\nTotal Expenses: Rs{total:.2f}\n")

# Main program loop
def main():
    print("Welcome to the Expense Tracker!")
    expenses = load_expenses()

    while True:
        print("\nOptions:")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            add_expense(expenses)
        elif choice == "2":
            view_expenses(expenses)
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

# Run the program
if __name__ == "__main__":
    main()
