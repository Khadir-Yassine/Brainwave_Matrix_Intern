# Dictionary to store user accounts
accounts = {}

# Function to create a new account
def create_account():
    print("📝 Create a New Account")
    print("========================")
    
    username = input("🔑 Enter a username: ")
    
    # Ensure the username is unique
    while username in accounts:
        print("🚫 Username already exists. Please choose a different username.")
        username = input("🔑 Enter a new username: ")
    
    pin = input_pin("🔐 Set a 4-digit PIN: ")
    confirm_pin = input_pin("🔄 Confirm your PIN: ")

    # Ensure the PIN is confirmed correctly
    while confirm_pin != pin:
        print("❌ PINs do not match. Please try again.")
        confirm_pin = input_pin("🔄 Confirm your PIN: ")
    
    # Create a new account with a balance of 0
    accounts[username] = {'pin': pin, 'balance': 0, 'transactions': []}
    print(f"✅ Account created successfully for {username}! 🎉")

# Function to log into an account
def login():
    print("🔑 Login to Your Account")
    print("========================")
    
    username = input("🔑 Enter your username: ")
    
    # Ensure the username exists
    while username not in accounts:
        print("🚫 Username not found. Please try again.")
        username = input("🔑 Enter your username: ")

    # Allow user to enter PIN and give them 3 attempts
    for i in range(3):
        pin = input_pin("🔐 Enter your 4-digit PIN: ")
        if accounts[username]['pin'] == pin:
            print("✅ Login successful! 🎉")
            return username
        else:
            print(f"❌ Incorrect PIN. You have {2 - i} attempts left.")
    
    print("🚫 Too many incorrect attempts. Exiting.")
    return None

# Function to view transaction history
def view_transaction_history(username):
    print("📜 Transaction History")
    print("======================")
    
    if accounts[username]['transactions']:
        for transaction in accounts[username]['transactions']:
            print(f"💸 {transaction}")
    else:
        print("📝 No transactions yet.")

# Function to withdraw money
def withdraw_money(username):
    print("💵 Withdraw Money")
    print("=================")
    
    while True:
        amount = float(input("💸 Enter amount to withdraw: "))
        if amount > accounts[username]['balance']:
            print(f"🚫 Insufficient funds. Your current balance is: 💰 {accounts[username]['balance']}")
            
            while True:  # Loop to ensure valid input
                choice = input("🔄 Would you like to enter a different amount? (y/n): ").lower()
                
                if choice == 'y':
                    break  # Re-enter amount
                elif choice == 'n':
                    return  # Exit function
                else:
                    print("❌ Invalid input. Please enter 'y' for yes or 'n' for no.")
        else:
            accounts[username]['balance'] -= amount
            print(f"✅ Withdrawal successful. Your new balance is: 💰 {accounts[username]['balance']}")
            accounts[username]['transactions'].append(f"Withdrew {amount}")
            break

# Function to deposit money
def deposit_money(username):
    print("💰 Deposit Money")
    print("================")
    
    while True:
        amount = float(input("💸 Enter amount to deposit: "))
        if amount > 0:
            accounts[username]['balance'] += amount
            print(f"✅ Deposit successful. Your new balance is: 💰 {accounts[username]['balance']}")
            accounts[username]['transactions'].append(f"Deposited {amount}")
            break
        else:
            print("❌ Invalid amount. Please enter a positive number.")
            while True:
                retry = input("🔄 Would you like to enter a different amount? (y/n): ").lower()
                if retry == 'y':
                    break  # Re-enter amount
                elif retry == 'n':
                    return  # Exit function
                else:
                    print("❌ Invalid input. Please enter 'y' for yes or 'n' for no.")

# Function to transfer money
def transfer_money(username):
    print("🔄 Transfer Money")
    print("=================")
    
    while True:  # Loop to ensure valid recipient username
        recipient = input("🔑 Enter recipient username: ")
        
        if recipient in accounts:
            while True:
                amount = float(input("💸 Enter amount to transfer: "))
                
                if amount > accounts[username]['balance']:
                    print(f"🚫 Insufficient funds. Your current balance is: 💰 {accounts[username]['balance']}")
                    
                    while True:
                        choice = input("🔄 Would you like to enter a different amount? (y/n): ").lower()
                        
                        if choice == 'y':
                            break  # Allows the user to re-enter the amount
                        elif choice == 'n':
                            return  # Exits the function if user doesn't want to proceed
                        else:
                            print("❌ Invalid input. Please enter 'y' for yes or 'n' for no.")
                
                else:
                    accounts[username]['balance'] -= amount
                    accounts[recipient]['balance'] += amount
                    print(f"✅ Transfer successful! Your new balance is: 💰 {accounts[username]['balance']}")
                    accounts[username]['transactions'].append(f"Transferred {amount} to {recipient}")
                    accounts[recipient]['transactions'].append(f"Received {amount} from {username}")
                    return  # Exit after successful transfer

        else:
            print("🚫 Recipient username not found.")
            
            while True:
                retry = input("🔄 Would you like to enter a different username? (y/n): ").lower()
                
                if retry == 'y':
                    break  # Re-enter recipient username
                elif retry == 'n':
                    return  # Exit function
                else:
                    print("❌ Invalid input. Please enter 'y' for yes or 'n' for no.")

# Main menu after login
def main_menu(username):
    while True:
        print("\n--- 🏦 Main Menu ---")
        print("1️⃣ View Balance")
        print("2️⃣ Withdraw Money")
        print("3️⃣ Deposit Money")
        print("4️⃣ Transfer Money")
        print("5️⃣ View Transaction History")
        print("6️⃣ Logout")
        
        choice = input("👉 Choose an option: ")
        
        if choice == '1':
            print(f"💰 Your current balance is: {accounts[username]['balance']}")
        elif choice == '2':
            withdraw_money(username)
        elif choice == '3':
            deposit_money(username)
        elif choice == '4':
            transfer_money(username)
        elif choice == '5':
            view_transaction_history(username)
        elif choice == '6':
            print("👋 Logging out...")
            break
        else:
            print("❌ Invalid option. Please choose a valid menu option.")

# Function to ensure input is a 4-digit number
def input_pin(prompt):
    while True:
        pin = input(prompt)
        if pin.isdigit() and len(pin) == 4:
            return pin
        else:
            print("❌ Invalid input. Please enter a 4-digit number.")

# Main function to start the ATM interface
def atm_interface():
    while True:
        print("\n--- 🏦 Welcome to the ATM ---")
        print("1️⃣ Create a New Account")
        print("2️⃣ Login to an Existing Account")
        print("3️⃣ Exit")
        
        choice = input("👉 Choose an option: ")
        
        if choice == '1':
            create_account()
        elif choice == '2':
            username = login()
            if username:
                main_menu(username)
        elif choice == '3':
            print("👋 Thank you for using the ATM. Goodbye! 👋")
            break
        else:
            print("❌ Invalid option. Please choose a valid menu option.")

# Run the ATM interface
atm_interface()


