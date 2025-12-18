def get_positive_number(prompt):
    while True:
        try:
            number = float(input(prompt))
            if number <= 0:
                print("number must be positive")
                continue
            return number
        except (ValueError, EOFError, KeyboardInterrupt):
            print("\n invalid input ot interrupted!")
            return None

age = get_positive_number("Enter your age: ")
if age:
    print(f"age: {age}")
