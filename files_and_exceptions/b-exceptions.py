def calculator():
    """Simple calculator with error handling."""
    print("🔢 CALCULATOR")
    print("="*30)

    try:
        a = float(input("Enter first number: "))
        operator = input("Enter operator (+, -, *, /): ")
        b = float(input("Enter second number: "))

        if operator == "+":
            result = a + b
        elif operator == "-":
            result = a - b
        elif operator == "*":
            result = a * b
        elif operator == "/":
            result = a / b
        else:
            print("❌ Invalid operator!")
            return

        print(f"✅ Result: {a} {operator} {b} = {result}")

    except ValueError:
        print("❌ Invalid number! Please enter numbers only.")
    except ZeroDivisionError:
        print("❌ Cannot divide by zero!")
    except Exception as e:
        print(f"❌ Unexpected error: {e}")

# Run it
calculator()
