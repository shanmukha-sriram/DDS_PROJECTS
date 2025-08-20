transactions = []
def add_transaction():
    t_type = input("Enter type (income/expense): ")
    amount = float(input("Enter amount: "))
    desc = input("Enter description: ")
    transactions.append({"type": t_type, "amount": amount, "desc": desc})
    print("Transaction Added!\n")

def view_transactions():
    print("\n--- All Transactions ---")
    for i, t in enumerate(transactions, start=1):
        print(f"{i}. {t['type']} - {t['amount']} - {t['desc']}")
    print()

def filter_expenses(limit):
    print(f"\n--- Expenses above {limit} ---")
    for t in transactions:
        if t["type"] == "expense" and t["amount"] > limit:
            print(f"{t['type']} - {t['amount']} - {t['desc']}")
    print()

def main():
    while True:
        print("1. Add Transaction")
        print("2. View Transactions")
        print("3. Filter Large Expenses")
        print("4. Exit")
        choice = int(input("Choice: "))

        if choice == 1:
            add_transaction()
        elif choice == 2:
            view_transactions()
        elif choice == 3:
            lim = float(input("Enter limit: "))
            filter_expenses(lim)
        elif choice == 4:
            break
        else:
            print("Invalid Option!\n")

if name == "main":
    main()
