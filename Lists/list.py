fruits = ["apple", "banana", "cherry"]
numbers = [1, 2, 3, 4]
mixed = [1, "hello", True, 3.14]
nested = [1, [2, 3], 4]

fruits.append("orange")
fruits.insert(1, "kiwi")
fruits.extend(["mango", "pear"])
fruits[1] = "berry"

old_value = "banana"
new_value = "grapes"

if old_value in fruits:               # check if it exists
    index = fruits.index(old_value)  # find its index
    fruits[index] = new_value        # replace it
else:
    print(f"{old_value} not found in the list")

for i in range(len(fruits)):
    print(f"Fruit {i+1}: {fruits[i]}")


