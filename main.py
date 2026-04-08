import os

# =====================================================
# Desafio: Expense Tracker Roadmap.sh
# =====================================================

# -----------------------------------------------------
# Read expenses function

def readExpenses():
    # Return list with all expenses, without the ID
    expenses = []
    if not os.path.exists("expenses.txt"):
        return expenses
    
    with open("expenses.txt", "r") as file:
        for line in file:
            line = line.strip()
            if line:
                rest = line.split(" - ", 1)[1]
                expenses.append(rest)
    return expenses
# -----------------------------------------------------

# -----------------------------------------------------
# Save expenses function

def saveExpenses(expenses):
    # Save expenses to file, with ID starting from 1
    with open("expenses.txt", "w") as file:
        for index, expense in enumerate(expenses, start=1):
            file.write(f"{index} - {expense}\n")
            
# -----------------------------------------------------

# -----------------------------------------------------
# Add expenses function

def addExpenses():
    # Get expense details from user
    valor = float(input("Enter the expense amount: "))
    expense = input("Enter the expense description: ")
    month = input("Enter the month of the expense: ")

    # Save expense to list and from list to file
    expenses = readExpenses()
    expenses.append(f"{expense}: {valor} ({month})")
    saveExpenses(expenses)

# -----------------------------------------------------

# -----------------------------------------------------
# Delete expenses function

def deleteExpenses():
    # Get expense ID from user and delete it from list and file
    expenses = readExpenses()
    
    target_id = int(input("Enter the ID of the expense to delete: "))
    
    if target_id < 1 or target_id > len(expenses):
        print("Invalid ID.")
        return
    
    expenses.pop(target_id - 1)
    saveExpenses(expenses)
    
# -----------------------------------------------------

# -----------------------------------------------------
# Update expenses function

def updateExpense():
    # Get expense ID from user and update it in list and file
    expenses = readExpenses()
    target_id = int(input("Enter the ID of the expense to update: "))
    if target_id < 1 or target_id > len(expenses):
        print("Invalid ID.")
        return
    
    new_valor = float(input("Enter the new expense amount: "))
    new_expense = input("Enter the new expense description: ")
    new_month = input("Enter the new month of the expense: ")
    
    expenses[target_id - 1] = f"{new_expense}: {new_valor} ({new_month})"
    saveExpenses(expenses)

# -----------------------------------------------------

# -----------------------------------------------------
# View expenses function

def viewExpenses():
    # Print all expenses from file
    try:
        with open("expenses.txt", "r") as file:
            print(file.read())
    except FileNotFoundError:
        print("No expenses found.")

# View monthly expenses function

def viewMonth():
    # Get month from user and print all expenses from file for that month
    month = input("Enter the month to view expenses for: ")
    try:
        with open("expenses.txt", "r") as file:
            lines = file.readlines()
            for line in lines:
                if line.endswith(f" ({month})\n"):
                    print(line.strip())
    except FileNotFoundError:
        print("No expenses found.")
        
# -----------------------------------------------------

# -----------------------------------------------------
# Main function

def main():
    while True:
        print("1. Add Expense")
        print("2. Update Expense")
        print("3. Delete Expense")
        print("4. View Expenses")
        print("5. View Monthly Expenses")
        print("6. Exit")

        choice = input("Enter your choice: ")

        match choice:
            case "1":
                addExpenses()
            case "2":
                updateExpense()
            case "3":
                deleteExpenses()
            case "4":
                viewExpenses()
            case "5":
                viewMonth()
            case "6":
                print("Exiting...")
                break
            case _:
                print("Invalid choice. Please try again.")

# -----------------------------------------------------

if __name__ == "__main__":
    main()