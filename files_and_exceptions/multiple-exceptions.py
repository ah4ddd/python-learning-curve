
# WRONG ORDER!
try:
    number = int(input("Enter number: "))
except Exception:  # ❌ This catches EVERYTHING first!
    print("Caught some exception!")
except ValueError:  # type: ignore # ❌ This will NEVER run!
    print("Caught ValueError specifically!")
