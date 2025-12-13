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
