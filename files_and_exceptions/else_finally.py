def divide_numbers(a, b):
    """Division with full exception handling."""
    print("🔢 Starting division...")

    try:
        result = a / b
        print(f"   Calculation: {a} / {b}")

    except ZeroDivisionError:
        print("   ❌ Cannot divide by zero!")
        return None

    except TypeError:
        print("   ❌ Invalid types for division!")
        return None

    else:
        print(f"   ✅ Result: {result}")
        return result

    finally:
        print("🧹 Cleanup: Operation finished!\n")

# Test different scenarios
print("=== Test 1: Valid division ===")
divide_numbers(10, 2)

print("=== Test 2: Division by zero ===")
divide_numbers(10, 0)

print("=== Test 3: Invalid types ===")
divide_numbers("10", 2)

print("=== Test 4: Another valid ===")
divide_numbers(100, 5)
