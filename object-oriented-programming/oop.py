import random
import string
from datetime import datetime

class PasswordGenerator:
    def __init__(self):
        self.lowercase = string.ascii_lowercase  # 'abcdefg...'
        self.uppercase = string.ascii_uppercase  # 'ABCDEFG...'
        self.digits = string.digits              # '0123456789'
        self.symbols = "!@#$%^&*"

    def generate(self, length=12, include_symbols=True):
        """Generate random password"""
        # Build character pool:
        chars = self.lowercase + self.uppercase + self.digits
        if include_symbols:
            chars += self.symbols

        # Generate password:
        password = ''.join(random.choice(chars) for _ in range(length))

        # Log generation time:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        return {
            "password": password,
            "length": length,
            "generated_at": timestamp
        }

    def generate_multiple(self, count=5, length=12):
        """Generate multiple passwords"""
        return [self.generate(length) for _ in range(count)]

# Use it:
gen = PasswordGenerator()

# Single password:
pwd = gen.generate(length=16)
print(f"Password: {pwd['password']}")
print(f"Length: {pwd['length']}")
print(f"Generated: {pwd['generated_at']}")

# Multiple passwords:
print("\nGenerate 5 passwords:")
passwords = gen.generate_multiple(count=5, length=12)
for i, pwd in enumerate(passwords, 1):
    print(f"{i}. {pwd['password']}")
