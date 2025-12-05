class BankAccount:

    total_accounts = 0

    def __init__(self, owner, balance=0):
        """Constructor"""
        self.__owner = owner
        self.__balance = balance
        self.__transactions = []
        BankAccount.total_accounts += 1


    def __str__(self):
        """For humans"""
        return f"{self.__owner}'s account: ₹{self.__balance}"

    def __repr__(self):
        """For developers"""
        return f"BankAccount('{self.__owner}', {self.__balance})"

    # Comparison (based on balance):
    def __eq__(self, other):
        return self.__balance == other.__balance

    def __lt__(self, other):
        return self.__balance < other.__balance

    def __gt__(self, other):
        return self.__balance > other.__balance

    # Arithmetic:
    def __add__(self, amount):
        """Deposit money"""
        if isinstance(amount, (int, float)) and amount > 0:
            new_balance = self.__balance + amount
            new_account = BankAccount(self.__owner, new_balance)
            new_account.__transactions = self.__transactions.copy()
            new_account.__transactions.append(f"Deposited ₹{amount}")
            return new_account
        return NotImplemented

    def __sub__(self, amount):
        """Withdraw money"""
        if isinstance(amount, (int, float)) and amount > 0:
            if amount <= self.__balance:
                new_balance = self.__balance - amount
                new_account = BankAccount(self.__owner, new_balance)
                new_account.__transactions = self.__transactions.copy()
                new_account.__transactions.append(f"Withdrew ₹{amount}")
                return new_account
            else:
                raise ValueError("Insufficient funds!")
        return NotImplemented

    # Container methods:
    def __len__(self):
        """Number of transactions"""
        return len(self.__transactions)

    def __getitem__(self, index):
        """Get transaction by index"""
        return self.__transactions[index]

    def __contains__(self, transaction):
        """Check if transaction exists"""
        return transaction in self.__transactions

    def __iter__(self):
        """Iterate through transactions"""
        return iter(self.__transactions)

    # Properties:
    @property
    def balance(self):
        return self.__balance

    @property
    def owner(self):
        return self.__owner

    # Methods:
    def deposit(self, amount):
        """Deposit money (modifies in place)"""
        if amount > 0:
            self.__balance += amount
            self.__transactions.append(f"Deposited ₹{amount}")
            print(f"✅ Deposited ₹{amount}. New balance: ₹{self.__balance}")
        else:
            print("❌ Amount must be positive!")

    def withdraw(self, amount):
        """Withdraw money (modifies in place)"""
        if amount > 0:
            if amount <= self.__balance:
                self.__balance -= amount
                self.__transactions.append(f"Withdrew ₹{amount}")
                print(f"✅ Withdrew ₹{amount}. New balance: ₹{self.__balance}")
            else:
                print(f"❌ Insufficient funds! Balance: ₹{self.__balance}")
        else:
            print("❌ Amount must be positive!")

# Use it:
print("=== Creating Accounts ===")
account1 = BankAccount("Ahad", 5000)
account2 = BankAccount("Sara", 3000)
account3 = BankAccount("Zexo", 7000)

print(f"Total accounts: {BankAccount.total_accounts}\n")

print("=== String Representations ===")
print(account1)       # __str__
print(repr(account2)) # __repr__
print()

print("=== Comparisons ===")
print(f"account1 == account2: {account1 == account2}")  # False
print(f"account1 < account3: {account1 < account3}")    # True
print(f"account3 > account2: {account3 > account2}")    # True
print()

print("=== Arithmetic (returns new account) ===")
account1_after_deposit = account1 + 1000
print(account1_after_deposit)
print(f"Original account1: {account1}")  # Unchanged!
print()

print("=== In-place Operations ===")
account1.deposit(1000)
account1.deposit(500)
account1.withdraw(200)
print()

print("=== Container Operations ===")
print(f"Number of transactions: {len(account1)}")
print(f"First transaction: {account1[0]}")
print(f"Last transaction: {account1[-1]}")
print()

print("=== Iteration ===")
print("Transaction history:")
for i, transaction in enumerate(account1, 1):
    print(f"  {i}. {transaction}")
print()

print("=== Membership Test ===")
print(f"'Deposited ₹1000' in transactions: {'Deposited ₹1000' in account1}")
print()

print("=== Sorting Accounts ===")
accounts = [account1, account2, account3]
accounts.sort()  # Uses __lt__!
print("Sorted by balance:")
for acc in accounts:
    print(f"  {acc}")

