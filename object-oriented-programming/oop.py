class Bag:
    def __init__(self, items):
        self.items = items

    def __len__(self):
        return len(self.items)

    def __contains__(self, item):
        return item in self.items

    def __getitem__(self, index):
        return self.items[index]

    def __setitem__(self, index, value):
        self.items[index] = value

    def __delitem__(self, index):
        del self.items[index]

    def __iter__(self):
        return iter(self.items)

    def __reversed__(self):
        return reversed(self.items)

    def __str__(self):
        return f"Bag: {self.items}"

b = Bag(["knife", "rope", "key"])

print(len(b))          # 3
print("rope" in b)     # True
print(b[1])            # "rope"
b[1] = "silk"
del b[0]
print(list(b))         # ['silk', 'key']
print(list(reversed(b)))
