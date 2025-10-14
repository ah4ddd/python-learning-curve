# types of for loops in Python

#basic for loop to iterate over a range of numbers
# Print numbers 1–5
for i in range(1, 6):
    print(i)

# Output: 1 2 3 4 5

# for loop to iterate over a list
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(f"I love {fruit}")

# Output:
# I love apple
# I love banana
# I love cherry

# for loop to iterate over a string
for letter in "Python":
    print(letter)

# Output: P y t h o n

# for loop with enumerate to get index and value
names = ["Ahad", "Lily"]
ages = [23, 22]

for name, age in zip(names, ages):
    print(f"{name} is {age} years old")

# Output:
# Ahad is 23 years old
# Lily is 22 years old

# nested for loop to create a multiplication table
for i in range(1, 4):       # outer loop
    for j in range(1, 4):   # inner loop
        print(f"{i} x {j} = {i*j}")

# Output:
# 1 x 1 = 1
# 1 x 2 = 2
# 1 x 3 = 3
# 2 x 1 = 2
# 2 x 2 = 4
# 2 x 3 = 6
# 3 x 1 = 3
# 3 x 2 = 6
# 3 x 3 = 9

# for loop with a conditional statement
for i in range(1, 11):
    if i % 2 == 0:
        print(f"{i} is even")

# Output: 2 4 6 8 10

# for loop with break and continue statements
for i in range(1, 6):
    if i == 3:
        continue  # skip 3
    print(i)
for i in range(1, 6):
    if i == 3:
        break  # stop the loop when i is 3
    print(i)

# for loop with else clause
for i in range(1, 4):
    print(i)
else:
    print("Loop finished successfully!")

# Output:
# 1
# 2
# 3
# Loop finished successfully!
