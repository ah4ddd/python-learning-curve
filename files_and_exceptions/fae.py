try:
    age = int(input("Enter your age: "))
except ValueError:
    print("❌ Invalid input!")
else:
    print(f"✅ Valid age: {age}")
