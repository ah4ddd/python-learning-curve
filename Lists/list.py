fruits = ["apple", "banana", "apple", "orange", "banana", "apple"]

unique_fruits = []  # store unique names
counts = []         # store counts

for fruit in fruits:
    if fruit in unique_fruits:
        index = unique_fruits.index(fruit)
        counts[index] += 1
    else:
        unique_fruits.append(fruit)
        counts.append(1)

for i in range(len(unique_fruits)):
    print(f"{unique_fruits[i]}: {counts[i]}")
