class UserProfile:
    """User profile that saves to a file."""

    def __init__(self, username, filename):
        self.username = username
        self.filename = filename
        self.data = {}

    def set_preference(self, key, value):
        """Set a user preference."""
        self.data[key] = value

    def get_preference(self, key):
        """Get a user preference."""
        return self.data.get(key)

    def save(self):
        """Save profile to file."""
        with open(self.filename, "w") as f:
            f.write(f"{self.username}\n")
            for key, value in self.data.items():
                f.write(f"{key}:{value}\n")

    def load(self):
        """Load profile from file."""
        with open(self.filename, "r") as f:
            lines = f.readlines()
            self.username = lines[0].strip()
            for line in lines[1:]:
                if ":" in line:
                    key, value = line.strip().split(":", 1)
                    self.data[key] = value

u = UserProfile("Mia", "mia.txt")

u.set_preference("she", "mine")

print(u.data)

u.save()

print(u.data)
