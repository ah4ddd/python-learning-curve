class InvalidAgeError(Exception):
    """Raised when age is invalid."""

    def __init__(self, age, message):
        self.age = age
        self.message = message
        super().__init__(self.message)

def set_age(age):
    """Set age with validation."""
    if age < 0:
        raise InvalidAgeError(age, f"Age cannot be negative! Got: {age}")
    if age > 150:
        raise InvalidAgeError(age, f"Age too high! Got: {age}")
    return age

# Use it
try:
    age = set_age(900)
except InvalidAgeError as e:
    print(f"❌ Error: {e.message}")
    print(f"   Invalid value: {e.age}")
    print(f"   Suggestion: Enter age between 0 and 150")

