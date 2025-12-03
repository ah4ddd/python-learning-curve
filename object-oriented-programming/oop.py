class Money:
    def __init__(self, amount):
        self.amount = amount

    def __add__(self, other):
        return Money(self.amount + other.amount)

    def __str__(self):
        return f"₹{self.amount}"

class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = Money(price)

class ShoppingCart:
    def __init__(self):
        self.items = []

    def add(self, product):
        self.items.append(product)

    def total(self):
        total = Money(0)
        for item in self.items:
            total = total + item.price
        return total

cart = ShoppingCart()

cart.add(Product("Apple", 30))
cart.add(Product("Milk", 60))
cart.add(Product("Bread", 50))

print("Total price:", cart.total())
