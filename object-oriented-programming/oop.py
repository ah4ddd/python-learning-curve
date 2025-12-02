class Money:
    def __init__(self, amount):
        self.amount = amount

    def __iadd__(self, other):
        if isinstance(other, (int, float)):
            self.amount += other
            return self
        return NotImplemented

    def __isub__(self, other):
        if isinstance(other, (int, float)):
            self.amount -= other
            return self
        return NotImplemented

    def __imul__(self, other):
        if isinstance(other, (int, float)):
            self.amount *= other
            return self
        return NotImplemented

    def __str__(self):
        return f"₹{self.amount}"

paisa = Money(100)

paisa += 500

print(paisa)

paisa -= 500

print(paisa)

paisa *= 500

print(paisa)
