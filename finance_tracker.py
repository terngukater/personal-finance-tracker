import json
import os
import matplotlib.pyplot as plt
from datetime import datetime

DATA_FILE = "transactions.json"

def load_transactions():
    """Load transactions from JSON file."""
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'r') as file:
            return json.load(file)
    return {"transactions": []}

def save_transactions(transactions):
    """Save transactions to JSON file."""
    with open(DATA_FILE, 'w') as file:
        json.dump(transactions, file, indent=4)

def add_transaction(transactions):
    """Add a new transaction."""
    try:
        amount = float(input("Enter amount: "))
        category = input("Enter category (e.g., Food, Salary, Rent): ")
        type_ = input("Enter type (income/expense): ").lower()
        date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        transaction = {
            "amount": amount,
            "category": category,
            "type": type_,
            "date": date
        }
        transactions["transactions"].append(transaction)
        save_transactions(transactions)
        print("Transaction added successfully!")
    except ValueError:
        print("Invalid amount. Please enter a number.")

def view_summary(transactions):
    """Display total income, expenses, and balance."""
    income = sum(t["amount"] for t in transactions["transactions"] if t["type"] == "income")
    expenses = sum(t["amount"] for t in transactions["transactions"] if t["type"] == "expense")
    balance = income - expenses
    print(f"Total Income: ${income:.2f}")
    print(f"Total Expenses: ${expenses:.2f}")
    print(f"Balance: ${balance:.2f}")

def plot_expenses_by_category(transactions):
    """Plot expenses by category using matplotlib."""
    categories = {}
    for t in transactions["transactions"]:
        if t["type"] == "expense":
            category = t["category"]
            categories[category] = categories.get(category, 0) + t["amount"]

    if not categories:
        print("No expenses to plot.")
        return

    plt.bar(categories.keys(), categories.values())
    plt.title("Expenses by Category")
    plt.xlabel("Category")
    plt.ylabel("Amount ($)")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

def main():
    """Main function to run the finance tracker."""
    transactions = load_transactions()

    while True:
        print("\nPersonal Finance Tracker")
        print("1. Add Transaction")
        print("2. View Summary")
        print("3. Plot Expenses by Category")
        print("4. Exit")
        try:
            choice = input("Choose an option (1-4): ")
            if choice == "1":
                add_transaction(transactions)
            elif choice == "2":
                view_summary(transactions)
            elif choice == "3":
                plot_expenses_by_category(transactions)
            elif choice == "4":
                print("Goodbye!")
                break
            else:
                print("Invalid choice. Try again.")
        except Exception as e:
            print(f"Error: {e}. Please try again.")

if __name__ == "__main__":
    main()