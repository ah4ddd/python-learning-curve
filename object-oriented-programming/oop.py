class PaymentMethod:

    def process_payment(self, amount):
        raise NotImplementedError("Subclass must implement this!")

class CreditCard(PaymentMethod):
    def __init__(self, card_number, holder):
        self.card_number = card_number
        self.holder = holder

    def process_payment(self, amount):
        print(f"💳 Processing credit card payment: ₹{amount}")
        print(f"   Card: {self.card_number[-4:]} (last 4 digits)")
        print(f"   Amount debited from {self.holder}")
        return True

class UPI(PaymentMethod):
    def __init__(self, upi_id):
        self.upi_id = upi_id

    def process_payment(self, amount):
        print(f"📱 Processing UPI payment: ₹{amount}")
        print(f"   UPI ID: {self.upi_id}")
        print(f"   ✅ Payment successful!")
        return True

class Cryptocurrency(PaymentMethod):
    def __init__(self, wallet_address, coin_type):
        self.wallet_address = wallet_address
        self.coin_type = coin_type

    def process_payment(self, amount):
        print(f"🪙 Processing {self.coin_type} payment: ₹{amount}")
        print(f"   Wallet: {self.wallet_address[:10]}...")
        print(f"   ⛓️ Blockchain confirmed!")
        return True

class ShoppingCart:
    def __init__(self, total):
        self.total = total

    def checkout(self, payment_method):
        print(f"\n🛒 Checkout Total: ₹{self.total}")
        payment_method.process_payment(self.total)
        print("✅ Thank you for your purchase!\n")

cart = ShoppingCart(50000)

card = CreditCard("1234567890123456", "Ahad")
cart.checkout(card)


upi = UPI("ahad@upi")
cart.checkout(upi)

# Payment with crypto:
crypto = Cryptocurrency("0x742d35Cc6634C0532925a3b844Bc9e7595f", "Bitcoin")
cart.checkout(crypto)

