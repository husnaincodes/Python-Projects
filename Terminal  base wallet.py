
#           DIGITAL WALLET

# Initial wallet balance
balance = 0

# List to store transaction history
transactions = []

# Correct wallet PIN
correct_pin = "1234"

# ---------------- Login Function ------------------
def login():
    print("---------------------------------------")
    print("        WELCOME TO DIGITAL WALLET")
    print("---------------------------------------")

    attempts = 3

    while attempts > 0:
        pin = input("Enter PIN: ")

        if pin == correct_pin:
            print("\nLogin successful!\n")
            return True
        else:
            attempts -= 1
            print(f"Wrong PIN! Attempts left: {attempts}")

    print("Too many wrong attempts. Exiting...")
    return False


# ---------------- Main Menu Function ---------------
def show_menu():
    print("---------------------------------------")
    print("                 MAIN MENU")
    print("---------------------------------------")
    print("1. Check Balance")
    print("2. Add Money")
    print("3. Pay Money")
    print("4. Transaction History")
    print("5. Exit")
    print("---------------------------------------")


# ---------------- Check Balance --------------------
def check_balance():
    print(f"\nCurrent Balance: {balance} PKR\n")


# ---------------- Add Money ------------------------
def add_money():
    global balance

    amount = int(input("Enter amount to add: "))
    balance += amount

    transactions.append(("ADD", amount))
    print("Amount added successfully!\n")


# ---------------- Pay Money ------------------------
def pay_money():
    global balance

    receiver = input("Enter receiver name: ")
    amount = int(input("Enter amount to pay: "))

    if amount > balance:
        print("Not enough balance!\n")
    else:
        balance -= amount
        transactions.append(("PAY", receiver, amount))
        print(f"Payment sent to {receiver}!\n")


# ------------ Transaction History ------------------
def show_history():
    print("\n----- Transaction History -----")

    if len(transactions) == 0:
        print("No transactions yet.\n")
        return

    count = 1
    for t in transactions:
        if t[0] == "ADD":
            print(f"{count}. Added {t[1]} PKR")
        else:
            print(f"{count}. Paid {t[2]} PKR to {t[1]}")
        count += 1

    print("---------------------------------------\n")


# ---------------- Main Program ---------------------
if login():  # Only run menu if login is successful
    while True:
        show_menu()
        choice = input("Enter your choice: ")

        if choice == "1":
            check_balance()
        elif choice == "2":
            add_money()
        elif choice == "3":
            pay_money()
        elif choice == "4":
            show_history()
        elif choice == "5":
            print("Exiting... Thank you!")
            break
        else:
            print("Invalid choice! Try again.\n")
