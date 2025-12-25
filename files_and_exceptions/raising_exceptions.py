try:
    age = int(input("Enter your age: "))

    if age < 0:
        raise ValueError("Age cannot be negative!")

    if age > 150:
        raise ValueError("Age seems unrealistic!")

    print(f"Valid age: {age}")

except ValueError as e:
    print(f"❌ Invalid age: {e}")
