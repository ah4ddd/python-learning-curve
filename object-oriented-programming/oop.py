from abc import ABC, abstractmethod

class PaymentMethod(ABC):
    """Abstract payment method"""

    @abstractmethod
    def process_payment(self, amount):
        """Every payment method MUST process payments!"""
        pass

    @abstractmethod
    def refund(self, amount):
        """Every payment method MUST support refunds!"""
        pass

class CreditCard(PaymentMethod):
    def process_payment(self, amount):
        print(f"💳 Processing ₹{amount} via Credit Card")

    def refund(self, amount):
        print(f"💳 Refunding ₹{amount} to Credit Card")

class UPI(PaymentMethod):
    def process_payment(self, amount):
        print(f"📱 Processing ₹{amount} via UPI")

    def refund(self, amount):
        print(f"📱 Refunding ₹{amount} to UPI")

# Use them:
card = CreditCard()
upi = UPI()

card.process_payment(5000)
upi.process_payment(3000)

upi.refund(1000)
