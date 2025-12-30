data = (1, (10, 20))

a, (b, c) = data

print(a)
print(b)
print(c)

items = [
    (1, ("apple", "red")),
    (2, ("banana", "yellow")),
]

for idx, (fruit, color) in items:
    print(idx, fruit, color)

values = [("A", "alpha"), ("B", "beta")]

for idx, (letter, word) in enumerate(values, start=1):
    print(idx, letter, word)
