import json

def load_user_data(filename):
    """Load user data with error context."""
    try:
        with open(filename, "r") as f:
            data = json.load(f)
        return data
    except FileNotFoundError as e:
        # Original error caused this new error
        raise RuntimeError(f"Cannot load user data from '{filename}'") from e
    except json.JSONDecodeError as e:
        raise RuntimeError(f"Invalid JSON in '{filename}'") from e

try:
    load_user_data("missing.json")
except RuntimeError as e:
    print(f"❌ Error: {e}")
    print(f"   Caused by: {e.__cause__}")
