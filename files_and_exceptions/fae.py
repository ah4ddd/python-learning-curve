file = open("msg.txt", "r")

content = file.read()
print(content)

with open("msg.txt", "r") as f:
    content = f.read()
    print(content)

with open("msg.txt", "r") as f:
    lines = f.readlines()
    print(lines)
    print(type(lines))

print("\nEach line:")
for line in lines:
    print(repr(line))

print()

with open("msg.txt", "r") as f:
    for line in f:
        print(line.strip())

from random import choice

with open("mia_quotes.txt", "r") as f:
    quotes = f.readlines()

quotes = [quote.strip() for quote in quotes]

random_quote = choice(quotes)
print(f"Mia says: {random_quote}")
