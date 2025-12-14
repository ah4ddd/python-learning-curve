with open("learn.txt") as l:
    learn = l.read()

print("=== READ ENTIRE FILE ===")
print(learn)
print()

print("=== LOOP OVER FILE OBJECT ===")

with open("learn.txt") as f:
    for line in f:
        print(line.rstrip())

with open("learn.txt") as k:
    lines = k.readlines()

print("=== WORK FROM LIST ===")

for line in lines:
    print(line.rstrip())
