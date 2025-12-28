import json

# -----------------------------
# Custom exception (high-level)
# -----------------------------
class UserProfileError(Exception):
    """Raised when user profile cannot be loaded or validated."""
    pass


# -----------------------------
# Low-level loader
# -----------------------------
def load_user_profile(filename):
    """
    Loads and validates a user profile from JSON.
    Returns profile dict on success.
    Raises UserProfileError on failure.
    """

    try:
        with open(filename, "r") as f:
            data = json.load(f)

    except FileNotFoundError as e:
        # Technical error → wrapped as user-level error
        raise UserProfileError("User profile file not found.") from e

    except json.JSONDecodeError as e:
        raise UserProfileError("User profile file is corrupted.") from e

    # -----------------------------
    # Validation (business rules)
    # -----------------------------
    if "username" not in data:
        raise UserProfileError("Profile missing username.")

    if "age" not in data:
        raise UserProfileError("Profile missing age.")

    if not isinstance(data["age"], int) or data["age"] <= 0:
        raise UserProfileError("Invalid age in profile.")

    # Normal outcome
    return data


# -----------------------------
# High-level application logic
# -----------------------------
def main():
    try:
        profile = load_user_profile("data.json")
        print("✅ Profile loaded successfully!")
        print(f"Username: {profile['username']}")
        print(f"Age: {profile['age']}")

    except UserProfileError as e:
        # User-facing message
        print("❌ Failed to load user profile.")
        print(f"Reason: {e}")

        # Developer-facing detail (optional)
        if e.__cause__:
            print(f"[DEBUG] Root cause: {e.__cause__}")


# -----------------------------
# Entry point
# -----------------------------
if __name__ == "__main__":
    main()
