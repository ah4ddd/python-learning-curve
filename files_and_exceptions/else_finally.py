def test_return():
    try:
        print("Try block")
        return "Returning from try!"
    except:
        print("Except block")
    finally:
        print("Finally block")

result = test_return()
print(f"Result: {result}")

def tricky_function():
    try:
        return "From try"
    finally:
        return "From finally"  # This WINS!

result = tricky_function()
print(result)  # From finally
