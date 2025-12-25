def validate_email(email):
    """Validate email format."""
    if not isinstance(email, str):
        raise TypeError("Email must be a string!")

    if not email:
        raise ValueError("Email cannot be empty!")

    if "@" not in email:
        raise ValueError("Email must contain @!")

    if "." not in email.split("@")[1]:
        raise ValueError("Email domain must contain a dot!")

    return email.lower()

# Use it with error handling
def create_user(email):
    """Create user with email validation."""
    try:
        validated_email = validate_email(email)
        print(f"✅ User created with email: {validated_email}")
        return {"email": validated_email}
    except (TypeError, ValueError) as e:
        print(f"❌ Invalid email: {e}")
        return None

# Test cases
create_user("ahad@example.com")  # ✅ Valid
create_user("invalid")            # ❌ No @
create_user("invalid@domain")     # ❌ No dot in domain
create_user("")                   # ❌ Empty
create_user(123)                  # ❌ Not a string
