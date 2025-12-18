try:
    age = int(input("Enter your age: "))
    print(f"You are {age} years old!")
except ValueError:
    print("❌ That's not a valid number!")

filename = input("Enter filename: ")

try:
    with open(filename, "r") as f:
        content = f.read()
    print(f"File contents:\n{content}")
except FileNotFoundError:
    print(f"❌ File '{filename}' not found!")

try:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    result = a / b
    print(f"Result: {result}")
except ZeroDivisionError:
    print("❌ Cannot divide by zero!")
except ValueError:
    print("❌ Please enter valid numbers!")

import json

filename = input("Enter JSON filename: ")

try:
    with open(filename, "r") as f:
        data = json.load(f)
    print(f"Loaded data: {data}")
except FileNotFoundError:
    print(f"❌ File '{filename}' doesn't exist!")
except json.JSONDecodeError:
    print(f"❌ File '{filename}' is not valid JSON!")
except PermissionError:
    print(f"❌ No permission to read '{filename}'!")
