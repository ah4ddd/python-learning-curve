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

with open("names.txt", "r") as f:
    names = f.readlines()

names = [name.strip() for name in names]

a_names = [name for name in names if name.startswith('A')]

print(f"Total names: {len(names)}")
print(f"Names starting with 'A': {len(a_names)}")
print(f"Those names: {a_names}")
