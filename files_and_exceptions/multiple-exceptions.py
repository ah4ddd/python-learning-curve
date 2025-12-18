def divide_numbers():
    """Division with detailed error info."""
    try:
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))
        result = a / b
        print(f"Result: {result}")
    except ValueError as e:
        print(f"❌ Invalid number format!")
        print(f"   Details: {e}")
    except ZeroDivisionError as e:
        print(f"❌ Division by zero!")
        print(f"   Details: {e}")
    except Exception as e:
        print(f"❌ Unexpected error: {type(e).__name__}")
        print(f"   Details: {e}")

divide_numbers()
