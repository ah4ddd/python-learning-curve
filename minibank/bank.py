# Our main data structure
accounts = {}  # Empty dictionary to store accounts

while True:  # Infinite loop, will run until we break it
    print("\nWelcome to the Bank!")
    print("1. Create account")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Check balance")
    print("5. List accounts")
    print("6. Exit")

    choice = input("Choose your move (1-6): ")

    if choice == "1":
        username = input("Enter new username: ")
        if username in accounts:
            print("This account already exists, loser!")
        else:
            initial_balance = float(input("Enter initial balance: "))
            accounts[username] = initial_balance
            print(f"Account created for {username} with balance {initial_balance}")

    elif choice == "2":
        username = input("Enter your username: ")
        if username in accounts:
            deposit_amount = float(input("Enter amount to deposit: "))
            accounts[username] += deposit_amount
            print(f"{deposit_amount} added. New balance: {accounts[username]}")
        else:
            print("No such account, buddy!")

    elif choice == "3":
        username = input("Enter your username: ")
        if username in accounts:
            withdraw_amount = float(input("Enter amount to withdraw: "))
            if withdraw_amount <= accounts[username]:
                accounts[username] -= withdraw_amount
                print(f"{withdraw_amount} withdrawn. New balance: {accounts[username]}")
            else:
                print("Not enough balance, dumbass!")
        else:
            print("No such account!")

    elif choice == "4":
        username = input("Enter your username: ")
        if username in accounts:
            print(f"{username}'s balance: {accounts[username]}")
        else:
            print("No such account!")

    elif choice == "5":
        print("All accounts in the bank:")
        for user, balance in accounts.items():  # Loop through all accounts
            print(f"{user}: {balance}")

    elif choice == "6":
        print("Exiting the bank. Bye, loser!")
        break  # Stops the while loop

    else:
        print("Invalid choice, try again!")
