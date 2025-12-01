class ATM:
    def __init__(self, initial_balance=1000):
        self.balance = initial_balance
        self.pin = "1234"  # Hardcoded PIN for demo

    def check_pin(self, entered_pin):
        return self.pin == entered_pin

    def check_balance(self):
        return self.balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return True
        print("Deposit amount must be positive.")
        return False

    def withdraw(self, amount):
        if amount > 0:
            if self.balance >= amount:
                self.balance -= amount
                return True
            print("Insufficient funds.")
            return False
        print("Withdrawal amount must be positive.")
        return False


def main():
    atm = ATM()
    print("🟦 Welcome to the ATM!")

    pin_attempts = 0
    max_attempts = 3
    authenticated = False

    # --- PIN AUTHENTICATION ---
    while not authenticated and pin_attempts < max_attempts:
        entered_pin = input("Enter your PIN: ")

        if atm.check_pin(entered_pin):
            authenticated = True
            print("✅ PIN accepted.")
        else:
            pin_attempts += 1
            print(f"❌ Incorrect PIN. {max_attempts - pin_attempts} attempts remaining.")

    if not authenticated:
        print("🚫 Too many incorrect PIN attempts. Your card is blocked.")
        return

    # --- MAIN MENU ---
    while True:
        print("\n===== 🏦 ATM MENU =====")
        print("1. Check Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            print(f"💰 Current Balance: ${atm.check_balance():.2f}")

        elif choice == '2':
            try:
                amount = float(input("Enter deposit amount: $"))
                if atm.deposit(amount):
                    print(f"✅ Deposited ${amount:.2f}")
                print(f"New Balance: ${atm.check_balance():.2f}")
            except ValueError:
                print("⚠️ Invalid amount. Please enter a number.")

        elif choice == '3':
            try:
                amount = float(input("Enter withdrawal amount: $"))
                if atm.withdraw(amount):
                    print(f"💸 Withdrew ${amount:.2f}")
                print(f"New Balance: ${atm.check_balance():.2f}")
            except ValueError:
                print("⚠️ Invalid amount. Please enter a number.")

        elif choice == '4':
            print("👋 Thank you for using the ATM. Goodbye!")
            break

        else:
            print("❌ Invalid choice. Try again.")


if __name__ == "__main__":
    main()
