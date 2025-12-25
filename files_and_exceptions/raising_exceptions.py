def set_age(age):
    if not isinstance(age, int):
        raise ValueError("Age must be an integer!")
    if age < 0:
        raise ValueError("Age cannot be negative!")
    if age > 150:
        raise ValueError("Age too high!")
    return age

def add_numbers(a, b):
    if not isinstance(a, (int, float)):
        raise TypeError(f"First argument must be number, got {type(a).__name__}")
    if not isinstance(b, (int, float)):
        raise TypeError(f"Second argument must be number, got {type(b).__name__}")
    return a + b

print(set_age(90))

print(add_numbers("10", 10))

def get_user_name(user_dict):
    if "name" not in user_dict:
        raise KeyError("User dict must have 'name' key!")
    return user_dict["name"]
