from datetime import date
import csv
import os

FILE_NAME = "expenses.csv"

def add_expense():
    description = input("Enter description: ")
    amount = float(input("Enter amount: "))
    category = input("Enter category: ")
    today = date.today()

    file_exists = os.path.isfile(FILE_NAME)

    with open(FILE_NAME, "a", newline="") as file:
        writer = csv.writer(file)

        # Write header only once
        if not file_exists:
            writer.writerow(["Date", "Description", "Amount", "Category"])

        writer.writerow([today, description, amount, category])

    print("Expense added successfully!\n")


def view_expenses():
    if not os.path.isfile(FILE_NAME):
        print("No expenses found.\n")
        return

    total = 0
    print("\n--- Expense List ---")

    with open(FILE_NAME, "r") as file:
        reader = csv.reader(file)
        header = next(reader)  # skip header

        for row in reader:
            print(f"Date: {row[0]}, Description: {row[1]}, Amount: {row[2]}, Category: {row[3]}")
            total += float(row[2])

    print("--------------------")
    print(f"Total Expense: ₹{total}\n")


def main():
    while True:
        print("Expense Tracker")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            print("Exiting program...")
            break
        else:
            print("Invalid choice. Try again.\n")


if __name__ == "__main__":
    main()
    input("\nPress Enter to exit...")
