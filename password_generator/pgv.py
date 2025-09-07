# Step 0: Import modules
import random  # used to pick random items
import string  # gives us easy access to letters and digits

# Step 1: Ask the user how long the password should be
length = int(input("Enter desired password length (8+ recommended): "))

# Step 2: Define characters to use
letters = string.ascii_letters  # all lowercase + uppercase letters
digits = string.digits          # 0-9
symbols = "!@#$%^&*()"

all_chars = letters + digits + symbols  # combine everything

# Step 3: Generate random password
password = "".join(random.choice(all_chars) for _ in range(length))
# Explanation:
# - random.choice(all_chars) picks a single character from all_chars
# - for _ in range(length) repeats it 'length' times
# - "".join(...) combines the characters into a single string

# Step 4: Show the password
print(f"Generated password: {password}")

# Step 5: Validate strength
# Criteria: at least 1 lowercase, 1 uppercase, 1 number, 1 symbol, length >= 8
def check_strength(pw):
    has_lower = any(c.islower() for c in pw)  # is there any lowercase letter?
    has_upper = any(c.isupper() for c in pw)  # is there any uppercase letter?
    has_digit = any(c.isdigit() for c in pw)  # is there any number?
    has_symbol = any(c in symbols for c in pw)  # is there any symbol?

    if len(pw) >= 8 and has_lower and has_upper and has_digit and has_symbol:
        return "Strong password 💪"
    else:
        return "Weak password 😬"

# Step 6: Check and print strength
strength = check_strength(password)
print(f"Password strength: {strength}")

# A simple password generator and strength checker
