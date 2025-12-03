class Money:
    def __init__(self, amount):
        self.amount = amount

    def __add__(self, other):
        if isinstance(other, Money):
            return Money(self.amount + other.amount)
        return Money(self.amount + other)

    def __radd__(self, other):
        return Money(other + self.amount)

    def __iadd__(self, other):
        if isinstance(other, Money):
            self.amount += other.amount
        else:
            self.amount += other
        return self

    def __sub__(self, other):
        return Money(self.amount - other.amount)

    def __mul__(self, n):
        return Money(self.amount * n)

    def __truediv__(self, n):
        return Money(self.amount / n)

    def __str__(self):
        return f"₹{self.amount:.2f}"

    def __repr__(self):
        return f"Money({self.amount})"

class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = Money(price)

    def __str__(self):
        return f"{self.name} - {self.price}"

    def __repr__(self):
        return f"Product('{self.name}', {self.price})"

class ShoppingCart:
    def __init__(self):
        self.items = []

    def add(self, product):
        self.items.append(product)

    def __len__(self):
        return len(self.items)

    def __getitem__(self, index):
        return self.items[index]

    def __setitem__(self, index, value):
        self.items[index] = value

    def __delitem__(self, index):
        del self.items[index]

    def __contains__(self, item):
        return item in self.items

    def __iter__(self):
        return iter(self.items)

    def total(self):
        total = Money(0)
        for item in self.items:
            total += item.price
        return total

    def __str__(self):
        names = ", ".join(p.name for p in self.items)
        return f"Cart({len(self.items)} items: {names})"

class Discount:
    def __init__(self, percentage):
        self.percentage = percentage

    def __call__(self, money):
        discount_value = money.amount * (self.percentage / 100)
        return Money(money.amount - discount_value)

class Checkout:
    def __init__(self, cart, discount=None):
        self.cart = cart
        self.discount = discount

    def __enter__(self):
        print("Starting checkout...")
        total = self.cart.total()
        if self.discount:
            total = self.discount(total)
        self.final_total = total
        return self.final_total

    def __exit__(self, exc_type, exc, traceback):
        print("Checkout closed.")

cash = Money(10)
p1 = Product("Book", 300)
p2 = Product("Pen", 20)
p3 = Product("Laptop", 70000)

cart = ShoppingCart()
cart.add(p1)
cart.add(p2)
cart.add(p3)
print(cart.total)

print(cart)
print(len(cart))
print(cart[0])
print("Pen" in [p.name for p in cart])

cart[1] = Product("Marker", 25)

discount = Discount(10)

with Checkout(cart, discount) as final_amount:
    print("Final payable:", final_amount)

print(cash)
