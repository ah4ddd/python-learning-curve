class Money:
    def __init__(self, amount, currency="INR"):
        self.amount = amount
        self.currency = currency

    def __add__(self, other):
        """Called by +"""
        if isinstance(other, Money):
            if self.currency != other.currency:
                raise ValueError("Cannot add different currencies!")
            return Money(self.amount + other.amount, self.currency)
        elif isinstance(other, (int, float)):
            return Money(self.amount + other, self.currency)
        return NotImplemented

    def __sub__(self, other):
        """Called by -"""
        if isinstance(other, Money):
            if self.currency != other.currency:
                raise ValueError("Cannot subtract different currencies!")
            return Money(self.amount - other.amount, self.currency)
        elif isinstance(other, (int, float)):
            return Money(self.amount - other, self.currency)
        return NotImplemented

    def __mul__(self, multiplier):
        """Called by *"""
        if isinstance(multiplier, (int, float)):
            return Money(self.amount * multiplier, self.currency)
        return NotImplemented

    def __truediv__(self, divisor):
        """Called by /"""
        if isinstance(divisor, (int, float)):
            return Money(self.amount / divisor, self.currency)
        return NotImplemented

    def __str__(self):
        return f"{self.currency} {self.amount:.2f}"

    def __repr__(self):
        return f"Money({self.amount}, '{self.currency}')"

# Use it:
money1 = Money(1000)
money2 = Money(500)

# Add money:
total = money1 + money2
print(total)  # INR 1500.00

# Subtract:
difference = money1 - money2
print(difference)  # INR 500.00

# Multiply:
doubled = money1 * 2
print(doubled)  # INR 2000.00

# Divide:
half = money1 / 2
print(half)  # INR 500.00

# Add number:
more = money1 + 250
print(more)  # INR 1250.00

# Chain operations:
result = (money1 + money2) * 2 - 500
print(result)  # INR 2500.00
