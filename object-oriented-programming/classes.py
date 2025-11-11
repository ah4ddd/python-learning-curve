class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance = self.balance + amount
            print(f"✅ Deposited ₹{amount}. New balance: ₹{self.balance}")
        else:
            print("❌ Deposit amount must be positive!")

    def withdraw(self, amount):
        if amount <= 0:
            print("❌ Withdrawal amount must be positive!")
        elif amount > self.balance:
            print(f"❌ Insufficient funds! Balance: ₹{self.balance}")
        else:
            self.balance = self.balance - amount
            print(f"✅ Withdrew ₹{amount}. New balance: ₹{self.balance}")

    def display(self):
        print(f"{self.owner}'s balance: ₹{self.balance}")

account = BankAccount("Ahad", 5000)

account.deposit(1)

account.withdraw(2000)

account.withdraw(10000)

account.deposit(-500)

account.display()
