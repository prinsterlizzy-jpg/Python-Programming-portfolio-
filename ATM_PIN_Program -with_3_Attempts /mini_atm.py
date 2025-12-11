 # Step 1: Create ATM PIN
pin = int(input("Create your 4-digit PIN: "))
print("✅ PIN successfully created!")

# Step 2: Initialize balance and attempts
balance = 0
attempts = 3

# Step 3: Login system with 3 tries
while attempts > 0:
    entered_pin = int(input("Enter your 4-digit PIN to access: "))

    if entered_pin == pin:
        print("\n💳 Welcome! Access granted.")
        
        # Step 4: Main ATM Menu
        while True:
            print("\n===== ATM MENU =====")
            print("1. Check Balance")
            print("2. Deposit Money")
            print("3. Withdraw Money")
            print("4. Exit")

            choice = input("Choose an option (1-4): ")

            # Check Balance
            if choice == "1":
                print(f"💰 Your current balance is: ₦{balance}")

            # Deposit Money
            elif choice == "2":
                amount = int(input("Enter amount to deposit: ₦"))
                balance += amount
                print(f"✅ ₦{amount} deposited successfully!")
                print(f"New balance: ₦{balance}")

            # Withdraw Money
            elif choice == "3":
                amount = int(input("Enter amount to withdraw: ₦"))
                if amount > balance:
                    print("⚠️ Insufficient funds.")
                else:
                    balance -= amount
                    print(f"💸 ₦{amount} withdrawn successfully!")
                    print(f"Remaining balance: ₦{balance}")

            # Exit
            elif choice == "4":
                print("👋 Thank you for using our ATM. Goodbye!")
                break

            else:
                print("❌ Invalid choice. Please try again.")

        break  # Exit login loop after successful access

    else:
        attempts -= 1
        print(f"❌ Wrong PIN. You have {attempts} attempt(s) left.")
        if attempts == 0:
            print("🚫 Account locked! Too many failed attempts.")
