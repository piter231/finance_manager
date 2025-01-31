import json
import csv
import datetime
import os
import matplotlib.pyplot as plt
import numpy as np

DATA_FILE = "expenses.json"

def load_expenses():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as file:
            return json.load(file)
    return []

def save_expenses(expenses):
    with open(DATA_FILE, "w") as file:
        json.dump(expenses, file, indent=4)

def add_expense():
    amount = float(input("Enter amount: "))
    category = input("Enter category: ")
    date = datetime.date.today().isoformat()
    expense = {"amount": amount, "category": category, "date": date}
    expenses = load_expenses()
    expenses.append(expense)
    save_expenses(expenses)
    print("✅ Expense added!")

def show_summary():
    expenses = load_expenses()
    if not expenses:
        print("No recorded expenses.")
        return
    
    summary = {}
    for expense in expenses:
        category = expense["category"]
        summary[category] = summary.get(category, 0) + expense["amount"]
    
    print("\nExpense Summary:")
    for category, total in summary.items():
        print(f"{category}: {total:.2f} zł")

def export_to_csv():
    expenses = load_expenses()
    if not expenses:
        print("No data to export.")
        return
    
    with open("expenses.csv", "w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=["amount", "category", "date"])
        writer.writeheader()
        writer.writerows(expenses)
    print("📂 Data saved to expenses.csv")

def show_chart():
    expenses = load_expenses()
    if not expenses:
        print("No data for the chart.")
        return
    
    summary = {}
    for expense in expenses:
        category = expense["category"]
        summary[category] = summary.get(category, 0) + expense["amount"]
    
    plt.figure(figsize=(6,6))
    plt.pie(summary.values(), labels=summary.keys(), autopct="%1.1f%%")
    plt.title("Expense Distribution")
    plt.show()

def show_bar_chart():
    expenses = load_expenses()
    if not expenses:
        print("No data for the bar chart.")
        return
    
    summary = {}
    for expense in expenses:
        category = expense["category"]
        summary[category] = summary.get(category, 0) + expense["amount"]
    
    categories = list(summary.keys())
    amounts = list(summary.values())
    
    plt.figure(figsize=(8,5))
    plt.bar(categories, amounts, color=np.random.rand(len(categories), 3))
    plt.xlabel("Category")
    plt.ylabel("Amount (zł)")
    plt.title("Expenses by Category")
    plt.xticks(rotation=45)
    plt.show()

def main():
    while True:
        print("\n🔹 Mini Expense Manager")
        print("1. Add expense")
        print("2. Show summary")
        print("3. Export to CSV")
        print("4. Show pie chart")
        print("5. Show bar chart")
        print("6. Exit")
        
        choice = input("Choose an option: ")
        if choice == "1":
            add_expense()
        elif choice == "2":
            show_summary()
        elif choice == "3":
            export_to_csv()
        elif choice == "4":
            show_chart()
        elif choice == "5":
            show_bar_chart()
        elif choice == "6":
            print("👋 See you next time!")
            break
        else:
            print("❌ Invalid choice, please try again.")

if __name__ == "__main__":
    main()
