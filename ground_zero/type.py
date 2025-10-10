# ------------------------------
# BASIC TYPES
# ------------------------------
age = 20                 # int
price = 19.99            # float
name = "Ahad"            # str
is_active = True         # bool
result = None            # NoneType

print("=== Basic Types ===")
print(f"age = {age}, type: {type(age)}")
print(f"price = {price}, type: {type(price)}")
print(f"name = {name}, type: {type(name)}")
print(f"is_active = {is_active}, type: {type(is_active)}")
print(f"result = {result}, type: {type(result)}")

# ------------------------------
# COLLECTION TYPES
# ------------------------------
numbers_list = [1, 2, 3, 4]                     # list
numbers_tuple = (1, 2, 3, 4)                   # tuple
unique_numbers_set = {1, 2, 3, 4}              # set
user_data = {"name": "Ahad", "age": 25}        # dict

print("\n=== Collection Types ===")
print(f"numbers_list = {numbers_list}, type: {type(numbers_list)}")
print(f"numbers_tuple = {numbers_tuple}, type: {type(numbers_tuple)}")
print(f"unique_numbers_set = {unique_numbers_set}, type: {type(unique_numbers_set)}")
print(f"user_data = {user_data}, type: {type(user_data)}")

# ------------------------------
# ADVANCED / SPECIAL TYPES
# ------------------------------
complex_number = 2 + 3j                           # complex
raw_bytes = b"hello"                              # bytes
range_example = range(5)                          # range
immutable_set = frozenset([1, 2, 3, 4])          # frozenset

print("\n=== Advanced / Special Types ===")
print(f"complex_number = {complex_number}, type: {type(complex_number)}")
print(f"raw_bytes = {raw_bytes}, type: {type(raw_bytes)}")
print(f"range_example = {list(range_example)}, type: {type(range_example)}")
print(f"immutable_set = {immutable_set}, type: {type(immutable_set)}")

# ------------------------------
# EXPRESSIONS & COMBINED TYPES
# ------------------------------
total = age + price                                 # int + float → float
status_message = name + " is learning Python"      # str + str
can_proceed = is_active and not result             # bool expression

print("\n=== Expressions Combining Types ===")
print(f"total = {total}, type: {type(total)}")
print(f"status_message = {status_message}, type: {type(status_message)}")
print(f"can_proceed = {can_proceed}, type: {type(can_proceed)}")
