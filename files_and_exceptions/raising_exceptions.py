# Custom exceptions
class RegistrationError(Exception):
    """Base exception for registration errors."""
    pass

class InvalidEmailError(RegistrationError):
    """Email format is invalid."""
    pass

class DuplicateUserError(RegistrationError):
    """User already exists."""
    pass

class WeakPasswordError(RegistrationError):
    """Password too weak."""
    pass

# User database (mock)
users_db = {}

def validate_email(email):
    """Validate email format."""
    if not isinstance(email, str):
        raise TypeError("Email must be a string!")
    if "@" not in email or "." not in email:
        raise InvalidEmailError(f"Invalid email format: {email}")
    return email.lower()

def validate_password(password):
    """Validate password strength."""
    if len(password) < 8:
        raise WeakPasswordError("Password must be at least 8 characters!")
    if password.isalpha():
        raise WeakPasswordError("Password must contain numbers!")
    if password.isdigit():
        raise WeakPasswordError("Password must contain letters!")
    return password

def register_user(email, password):
    """Register a new user with validation."""
    try:
        # Validate inputs
        email = validate_email(email)
        password = validate_password(password)

        # Check for duplicates
        if email in users_db:
            raise DuplicateUserError(f"User with email '{email}' already exists!")

        # Register user
        users_db[email] = {
            "email": email,
            "password": password  # In real code, HASH this!
        }

        print(f"✅ User registered successfully: {email}")
        return True

    except InvalidEmailError as e:
        print(f"❌ Email Error: {e}")
        return False
    except WeakPasswordError as e:
        print(f"❌ Password Error: {e}")
        return False
    except DuplicateUserError as e:
        print(f"❌ Duplicate User: {e}")
        return False
    except RegistrationError as e:
        print(f"❌ Registration Error: {e}")
        return False
    except Exception as e:
        print(f"❌ Unexpected Error: {e}")
        return False

# Test the system
print("=== Test 1: Valid registration ===")
register_user("ahad@example.com", "SecurePass123")

print("\n=== Test 2: Invalid email ===")
register_user("invalid-email", "SecurePass123")

print("\n=== Test 3: Weak password ===")
register_user("mia@example.com", "weak")

print("\n=== Test 4: Duplicate user ===")
register_user("ahad@example.com", "AnotherPass456")

print("\n=== Test 5: Password with no numbers ===")
register_user("sara@example.com", "OnlyLetters")

print("\n=== Current users ===")
print(f"Registered users: {list(users_db.keys())}")
