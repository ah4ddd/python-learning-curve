from multiprocessing import Value


class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    def withdraw(self, amount):
        if amount > self.balance:
            raise ValueError("brokie")
        self.balance -= amount
        return True

acc1 = BankAccount(1000)

print(acc1.withdraw(10000))
