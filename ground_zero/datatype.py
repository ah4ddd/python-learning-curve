# ===========================
# BASIC TYPES
# ===========================
age = 20                 # int
price = 19.99            # float
name = "Ahad"            # str
is_active = True         # bool
nothing = None           # NoneType

print("=== Basic Types ===")
print(f"age = {age}, type: {type(age)}")
print(f"price = {price}, type: {type(price)}")
print(f"name = {name}, type: {type(name)}")
print(f"is_active = {is_active}, type: {type(is_active)}")
print(f"nothing = {nothing}, type: {type(nothing)}")

# ===========================
# COLLECTION TYPES
# ===========================
numbers_list = [1, 2, 3]
numbers_tuple = (4, 5, 6)
unique_set = {1, 2, 3}
user_dict = {"name": "Ahad", "age": 20}

print("\n=== Collections ===")
print(f"numbers_list = {numbers_list}, type: {type(numbers_list)}")
print(f"numbers_tuple = {numbers_tuple}, type: {type(numbers_tuple)}")
print(f"unique_set = {unique_set}, type: {type(unique_set)}")
print(f"user_dict = {user_dict}, type: {type(user_dict)}")

# ===========================
# ADVANCED / SPECIAL TYPES
# ===========================
complex_num = 2 + 3j
raw_bytes = b"hello"
range_example = range(5)
immutable_set = frozenset([1,2,3])

print("\n=== Advanced / Special Types ===")
print(f"complex_num = {complex_num}, type: {type(complex_num)}")
print(f"raw_bytes = {raw_bytes}, type: {type(raw_bytes)}")
print(f"range_example = {list(range_example)}, type: {type(range_example)}")
print(f"immutable_set = {immutable_set}, type: {type(immutable_set)}")

# ===========================
# TYPE CONVERSIONS
# ===========================
str_num = "17"
converted_int = int(str_num)
converted_float = float(str_num)
converted_bool = bool(str_num)
print("\n=== Type Conversions ===")
print(f"Original string: {str_num} -> int: {converted_int}, float: {converted_float}, bool: {converted_bool}")

num = 0
print(f"\nNumber {num} to bool: {bool(num)}")  # False
num2 = 42
print(f"Number {num2} to bool: {bool(num2)}")   # True

# Booleans to numbers
print(f"\nTrue to int: {int(True)}, float: {float(True)}")
print(f"False to int: {int(False)}, float: {float(False)}")

# ===========================
# EXPRESSIONS WITH TYPES
# ===========================
total = converted_int + converted_float
status_message = name + " is learning Python"
can_proceed = is_active and not nothing

print("\n=== Expressions & Logic ===")
print(f"total = {total}, type: {type(total)}")
print(f"status_message = {status_message}, type: {type(status_message)}")
print(f"can_proceed = {can_proceed}, type: {type(can_proceed)}")

# ===========================
# COMPARISONS
# ===========================
print("\n=== Comparisons ===")
print(f"converted_int == 17: {converted_int == 17}")
print(f"converted_int != 20: {converted_int != 20}")
print(f"converted_int < 20: {converted_int < 20}")
print(f"converted_int >= 17: {converted_int >= 17}")
