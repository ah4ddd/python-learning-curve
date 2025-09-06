
---

# **Step 0: The setup**

```python
accounts = {}  # Empty dictionary to store accounts
```

* We create an **empty dictionary**.
* Key = username
* Value = account balance
* Right now it’s empty.

---

# **Step 1: Start the loop**

```python
while True:
```

* Infinite loop → the menu will **keep showing** until the user chooses to exit (`break`).
* Every iteration = one “turn” of the user interacting with the bank.

---

# **Step 2: Show the menu**

```python
print("\nWelcome to the Bank, savage!")
print("1. Create account")
print("2. Deposit")
print("3. Withdraw")
print("4. Check balance")
print("5. List accounts")
print("6. Exit")
```

* Just printing **all available actions**.
* `\n` → makes a **new line** so the menu looks neat.

---

# **Step 3: Ask for user choice**

```python
choice = input("Choose your move (1-6): ")
```

* `input()` → pauses the program and waits for user typing.
* Whatever they type = stored as string in `choice`.

---

# **Step 4: Create account**

```python
if choice == "1":
    username = input("Enter new username: ")
    if username in accounts:
        print("This account already exists, loser!")
    else:
        initial_balance = float(input("Enter initial balance: "))
        accounts[username] = initial_balance
        print(f"Account created for {username} with balance {initial_balance}")
```

* Checks if user wants **option 1**.
* Ask for `username`.
* If username exists → print warning.
* Else → ask initial balance → convert to `float` → store in `accounts` dictionary.
* Print confirmation.

---

# **Step 5: Deposit money**

```python
elif choice == "2":
    username = input("Enter your username: ")
    if username in accounts:
        deposit_amount = float(input("Enter amount to deposit: "))
        accounts[username] += deposit_amount
        print(f"{deposit_amount} added. New balance: {accounts[username]}")
    else:
        print("No such account, buddy!")
```

* Check if user wants **option 2**.
* Ask for `username`.
* If account exists → ask deposit amount → convert to float → **add it to balance**.
* Else → print error.

---

# **Step 6: Withdraw money**

```python
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
```

* Similar to deposit.
* Only difference → check if **enough balance** before subtracting.

---

# **Step 7: Check balance**

```python
elif choice == "4":
    username = input("Enter your username: ")
    if username in accounts:
        print(f"{username}'s balance: {accounts[username]}")
    else:
        print("No such account!")
```

* Simply **print the current balance** if account exists.

---

# **Step 8: List all accounts**

```python
elif choice == "5":
    print("All accounts in the bank:")
    for user, balance in accounts.items():
        print(f"{user}: {balance}")
```

* Loop through the **dictionary of accounts**:

  * `user` = key → username
  * `balance` = value → money in account
* Prints **all accounts** → similar to quiz questions/answers loop.

---

# **Step 9: Exit**

```python
elif choice == "6":
    print("Exiting the bank. Bye, loser!")
    break
```

* User chose to exit → print message → stop the `while` loop.
* Program ends.

---

# **Step 10: Invalid choice**

```python
else:
    print("Invalid choice, try again!")
```

* If the user types something **other than 1-6** → print error.
* Loop continues → menu shows again.

---

# **Execution Flow (step by step)**

1. Program starts → empty `accounts` dictionary.
2. `while True` → menu is printed.
3. User chooses an option → `choice`.
4. Program goes through `if/elif/else`:

   * Matches the choice → executes that block.
   * If choice is invalid → prints error.
5. After block finishes → loop restarts → menu prints again.
6. If choice is 6 → `break` → loop stops → program ends.

---

### **Example Run**

```
Welcome to the Bank, savage!
1. Create account
2. Deposit
3. Withdraw
4. Check balance
5. List accounts
6. Exit
Choose your move (1-6): 1
Enter new username: Ahad
Enter initial balance: 1000
Account created for Ahad with balance 1000

Choose your move (1-6): 2
Enter your username: Ahad
Enter amount to deposit: 500
500.0 added. New balance: 1500.0

Choose your move (1-6): 5
All accounts in the bank:
Ahad: 1500.0

Choose your move (1-6): 6
Exiting the bank. Bye, loser!
```

---

💡 **Blunt takeaways from this project:**

* `while True` → repeating menu
* `input()` → user interaction
* `if/elif/else` → decision-making
* `dictionary` → store and manage dynamic data
* `for user, balance in accounts.items()` → iterate over dictionary, like in the quiz
* Variables = current username, deposit/withdraw amounts, balances

---

