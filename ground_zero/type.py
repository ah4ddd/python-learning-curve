# ------------------------------
# VARIABLES OF DIFFERENT TYPES
# ------------------------------

# Numbers
age = 20                  # int
price = 19.99             # float

# Strings
name = "Ahad"
task = "Learn Python"

# Booleans
is_active = True
game_over = False

# NoneType (special type for "nothing")
result = None

# ------------------------------
# PRINTING VALUES AND TYPES
# ------------------------------
print("=== Numbers ===")
print(f"age = {age}, type: {type(age)}")
print(f"price = {price}, type: {type(price)}")

print("\n=== Strings ===")
print(f"name = {name}, type: {type(name)}")
print(f"task = {task}, type: {type(task)}")

print("\n=== Booleans ===")
print(f"is_active = {is_active}, type: {type(is_active)}")
print(f"game_over = {game_over}, type: {type(game_over)}")

print("\n=== NoneType ===")
print(f"result = {result}, type: {type(result)}")

# ------------------------------
# COMBINED EXPRESSIONS WITH TYPES
# ------------------------------
total = age + price
print("\n=== Expression Result ===")
print(f"total = age + price = {total}, type: {type(total)}")

status_message = name + " is learning Python"
print(f"status_message = {status_message}, type: {type(status_message)}")

can_proceed = is_active and not game_over
print(f"can_proceed = {can_proceed}, type: {type(can_proceed)}")
