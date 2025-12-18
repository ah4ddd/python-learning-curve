def get_number(prompt):
    """Get a valid number from user (keeps asking until valid)."""
    while True:
        try:
            number = float(input(prompt))
            return number
        except ValueError:
            print("❌ Invalid input! Please enter a number.")

# Use it
age = get_number("Enter your age: ")
print(f"You are {age} years old!")

score = get_number("Enter your score: ")
print(f"Your score: {score}")
