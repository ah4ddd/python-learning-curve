import json

class UserDataError(Exception):
    """High-level error shown to the user."""
    pass


def load_user_data(filename):
    """
    Load user data from a JSON file.

    - Returns data on success
    - Raises UserDataError on failure
    """
    try:
        with open(filename, "r") as f:
            data = json.load(f)

        # Normal validation → return, not raise
        if not isinstance(data, dict):
            return None  # expected but invalid structure

        return data

    except FileNotFoundError as e:
        # Low-level error → wrap into high-level error
        raise UserDataError("User data file not found.") from e

    except json.JSONDecodeError as e:
        raise UserDataError("User data file is corrupted.") from e


def main():
    try:
        data = load_user_data("users.json")

        if data is None:
            print("⚠️ User data format is invalid but program can continue.")
            return

        print("✅ User data loaded successfully!")
        print("Data:", data)

    except UserDataError as e:
        # USER-FACING MESSAGE
        print(f"❌ Error: {e}")

        # DEVELOPER-FACING CAUSE
        print(f"   Caused by: {e.__cause__}")


if __name__ == "__main__":
    main()
