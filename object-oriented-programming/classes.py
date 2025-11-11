class BankAccount:
    total_accounts = 0  # Class attribute (shared counter)

    def __init__(self, owner, balance=0):
        self.owner = owner  # Instance attribute
        self.balance = balance  # Instance attribute

        # Increment the total counter:
        BankAccount.total_accounts = BankAccount.total_accounts + 1

    def display(self):
        print(f"{self.owner}: ₹{self.balance}")

# Create accounts:
account1 = BankAccount("Ahad", 5000)
account2 = BankAccount("Sara", 3000)
account3 = BankAccount("Zexo", 7000)

# Check total:
print(f"Total accounts created: {BankAccount.total_accounts}")
# Output: Total accounts created: 3

# Each object can also access it:
print(f"Total accounts: {account1.total_accounts}")
# Output: Total accounts: 3x
