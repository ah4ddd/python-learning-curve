class InsufficientFundsError(Exception):
    """Raised when account has insufficient funds."""
    pass

class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def withdraw(self, amount):
        if amount > self.balance:
            raise InsufficientFundsError(
                f"Cannot withdraw ₹{amount}, balance is only ₹{self.balance}"
            )
        self.balance -= amount
        print(f"✅ Withdrew ₹{amount}. New balance: ₹{self.balance}")

# Use it
account = BankAccount("Ahad", 1000)

try:
    account.withdraw(500)   # ✅ Works
    account.withdraw(2000)  # ❌ Raises InsufficientFundsError
except InsufficientFundsError as e:
    print(f"❌ {e}")
