
# Bank Account Management System in Python

class BankAccount:
    def __init__(self, account_number, account_holder, balance=0.0):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        """Deposit money into the account."""
        if amount <= 0:
            print("Deposit amount must be positive.")
            return
        self.balance += amount
        print(f"₹{amount:.2f} deposited successfully.")

    def withdraw(self, amount):
        """Withdraw money from the account."""
        if amount <= 0:
            print("Withdrawal amount must be positive.")
            return
        if amount > self.balance:
            print("Insufficient balance.")
            return
        self.balance -= amount
        print(f"₹{amount:.2f} withdrawn successfully.")

    def check_balance(self):
        """Display the current balance."""
        print(f"Account Balance: ₹{self.balance:.2f}")


# Simple menu-driven interface
def main():
    accounts = {}

    while True:
        print("\n=== Bank Account Management ===")
        print("1. Create Account")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Check Balance")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ").strip()

        if choice == "1":
            acc_num = input("Enter account number: ").strip()
            if acc_num in accounts:
                print("Account already exists.")
                continue
            name = input("Enter account holder name: ").strip()
            try:
                initial_balance = float(input("Enter initial deposit: "))
                if initial_balance < 0:
                    print("Initial balance cannot be negative.")
                    continue
            except ValueError:
                print("Invalid amount.")
                continue
            accounts[acc_num] = BankAccount(acc_num, name, initial_balance)
            print("Account created successfully.")

        elif choice == "2":
            acc_num = input("Enter account number: ").strip()
            if acc_num not in accounts:
                print("Account not found.")
                continue
            try:
                amount = float(input("Enter deposit amount: "))
            except ValueError:
                print("Invalid amount.")
                continue
            accounts[acc_num].deposit(amount)

        elif choice == "3":
            acc_num = input("Enter account number: ").strip()
            if acc_num not in accounts:
                print("Account not found.")
                continue
            try:
                amount = float(input("Enter withdrawal amount: "))
            except ValueError:
                print("Invalid amount.")
                continue
            accounts[acc_num].withdraw(amount)

        elif choice == "4":
            acc_num = input("Enter account number: ").strip()
            if acc_num not in accounts:
                print("Account not found.")
                continue
            accounts[acc_num].check_balance()

        elif choice == "5":
            print("Thank you for using the Bank Account Management System.")
            break

        else:
            print("Invalid choice. Please select between 1-5.")


if __name__ == "__main__":
    main()
