class BankAccount:
    # CLASS VARIABLE (shared by all accounts):
    total_accounts = 0
    interest_rate = 0.03  # 3%

    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance
        # Increment class variable:
        BankAccount.total_accounts += 1

    @classmethod
    def get_total_accounts(cls):
        """
        CLASS METHOD to access class variable

        Why class method?
        - We're accessing CLASS-LEVEL data (total_accounts)
        - Don't need any specific instance
        - Can call it on the class: BankAccount.get_total_accounts()
        """
        return cls.total_accounts

    @classmethod
    def set_interest_rate(cls, new_rate):
        """
        CLASS METHOD to modify class variable

        Why class method?
        - We're modifying CLASS-LEVEL data
        - Affects ALL instances
        - Semantic: "This changes the class, not one account"
        """
        if 0 <= new_rate <= 1:
            cls.interest_rate = new_rate
            print(f"✅ Interest rate updated to {new_rate * 100}%")
        else:
            print("❌ Invalid rate! Must be between 0 and 1")

    @classmethod
    def get_interest_rate(cls):
        """Get current interest rate"""
        return cls.interest_rate

    def apply_interest(self):
        """INSTANCE METHOD - applies interest to THIS account"""
        interest = self.balance * BankAccount.interest_rate
        self.balance += interest
        print(f"💰 Applied {interest:.2f} interest to {self.owner}'s account")

    def __str__(self):
        return f"{self.owner}: ₹{self.balance:.2f}"

# Create accounts:
account1 = BankAccount("Ahad", 10000)
account2 = BankAccount("Sara", 15000)
account3 = BankAccount("Zexo", 20000)

# Call CLASS METHOD (on the class):
print(f"Total accounts: {BankAccount.get_total_accounts()}")
# Output: Total accounts: 3

print(f"Current interest rate: {BankAccount.get_interest_rate() * 100}%")
# Output: Current interest rate: 3.0%

# Change interest rate (affects ALL accounts):
BankAccount.set_interest_rate(0.05)
# Output: ✅ Interest rate updated to 5.0%

# Apply interest to each account:
account1.apply_interest()
account2.apply_interest()
account3.apply_interest()

# Output:
# 💰 Applied 500.00 interest to Ahad's account
# 💰 Applied 750.00 interest to Sara's account
# 💰 Applied 1000.00 interest to Zexo's account

print(account1)
print(account2)
print(account3)

# Output:
# Ahad: ₹10500.00
# Sara: ₹15750.00
# Zexo: ₹21000.00
