# Step 1: Create some variables
x = 10
y = 5
z = 10

# Step 2: Boolean comparisons
print("x > y:", x > y)      # True, because 10 > 5
print("x < y:", x < y)      # False, because 10 is not < 5
print("x == z:", x == z)    # True, 10 equals 10
print("x != y:", x != y)    # True, 10 not equal 5

# Step 3: Store Boolean results in variables
is_x_greater = x > y
is_x_equal_z = x == z

print("\nStored Boolean values:")
print("is_x_greater:", is_x_greater)
print("is_x_equal_z:", is_x_equal_z)

# Step 4: Combine Booleans with logical operators
print("\nLogical operators:")
print("x > y and x == z:", (x > y) and (x == z))  # True and True = True
print("x > y or x < y:", (x > y) or (x < y))      # True or False = True
print("not(x > y):", not(x > y))                  # not True = False

# Step 5: Complex Boolean expressions
print("\nComplex Boolean expression:")
print(x > y and x == z or y > z)
# Python evaluates as: ((x > y) and (x == z)) or (y > z)
