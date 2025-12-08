class Order:
    total_orders = 0

    def __init__(self, product, price, quantity, discount=0):
        if not Order.is_valid_discount(discount):
            raise ValueError("Discount must be between 0 and 50")

        self.product = product
        self.price = price
        self.quantity = quantity
        self.discount = discount

        Order.increase_order_count()

    def total(self):
        return (self.price * self.quantity) * (1 - self.discount / 100)

    @classmethod
    def increase_order_count(cls):
        cls.total_orders += 1

    @classmethod
    def get_total_orders(cls):
        return cls.total_orders

    @staticmethod
    def is_valid_discount(discount):
        return 0 <= discount <= 50

o1 = Order("Laptop", 50000, 1, 10)
o2 = Order("Headphones", 2000, 2, 5)

print(o1.total())
print(o2.total())

print("Total orders:", Order.get_total_orders())

print(Order.is_valid_discount(-1))
