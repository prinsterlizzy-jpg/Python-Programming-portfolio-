# ATM PIN Program with 3 Attempts


# Step 1: Create your ATM PIN
pin = int(input("Create your 4-digit PIN: "))
print("✅ PIN successfully created!")

# Step 2: Allow up to 3 attempts for login
attempts = 3

while attempts > 0:
    entered_pin = int(input("Enter your 4-digit PIN to access: "))

    if entered_pin == pin:
        print("💳 Welcome! Access granted.")
        break
    else:
        attempts -= 1
        print(f"❌ Wrong PIN. You have {attempts} attempt(s) left.")

        if attempts == 0:
            print("🚫 Account locked! Too many failed attempts.")
