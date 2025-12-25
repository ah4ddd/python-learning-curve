def critical_operation():
    """Operation that logs errors before propagating."""
    try:
        risky_code()
    except Exception as e:
        # Log the error
        print(f"🚨 ERROR LOGGED: {e}")
        with open("error.log", "a") as f:
            f.write(f"Error: {e}\n")

        # Re-raise the same exception!
        raise  # <- This re-raises the caught exception!

def risky_code():
    raise ValueError("Something went wrong!")

# Use it
try:
    critical_operation()
except ValueError as e:
    print(f"❌ Caught at top level: {e}")

