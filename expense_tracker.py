# expense_tracker.py

expenses = []

def add_expense(description, amount):
    expenses.append({"description": description, "amount": amount})

def view_expenses():
    total = 0
    print("Expenses:")
    for expense in expenses:
        print(f"{expense['description']}: ${expense['amount']}")
        total += expense['amount']
    print(f"Total: ${total}")

# Sample usage
add_expense("Coffee", 5)
add_expense("Groceries", 30)
view_expenses()
