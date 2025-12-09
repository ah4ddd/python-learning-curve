from abc import ABC, abstractmethod

class Payment(ABC):
    @abstractmethod
    def pay(self, amount):
        pass

class CreditCardPayment(Payment):
    def __init__(self, card_number):
        self.card_number = card_number

    def pay(self, amount):
        return f"Paid ₹{amount} using Credit Card ending with {self.card_number[-4:]}"

class UPIPayment(Payment):
    def __init__(self, upi_id):
        self.upi_id = upi_id

    def pay(self, amount):
        return f"Paid ₹{amount} via UPI ({self.upi_id})"

class CryptoPayment(Payment):
    def __init__(self, wallet):
        self.wallet = wallet

    def pay(self, amount):
        return f"Paid ₹{amount} in crypto from wallet {self.wallet[:10]}..."

def checkout(payment_method, amount):
    print(payment_method.pay(amount))

card = CreditCardPayment("1234567890123456")
upi = UPIPayment("ahad@upi")
btc = CryptoPayment("0x742d35Cc6634C0532925a3b844Bc9e7595f")

checkout(card, 500)
checkout(upi, 999)
checkout(btc, 2000)

