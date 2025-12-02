class Bag:
    def __init__(self, items):
        self.items = items

    def __reversed__(self):
        return reversed(self.items)

    def __iter__(self):
        return iter(self.items)


b = Bag(["knife", "rope", "key"])

for item in reversed(b):
    print(item)

for item in b:
    print(item)

