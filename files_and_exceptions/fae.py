def save_settings(settings):
    """Save user settings to file."""
    with open("settings.txt", "w") as f:
        for key, value in settings.items():
            f.write(f"{key}={value}\n")
    print("✅ Settings saved!")

def load_settings():
    """Load user settings from file."""
    settings = {}
    try:
        with open("settings.txt", "r") as f:
            for line in f:
                line = line.strip()
                if line and "=" in line:
                    key, value = line.split("=", 1)
                    settings[key] = value
        return settings
    except FileNotFoundError:
        # Return defaults if file doesn't exist
        return {
            "volume": "80",
            "difficulty": "medium",
            "theme": "dark"
        }

# User changes settings
user_settings = {
    "volume": "100",
    "difficulty": "hard",
    "theme": "dark",
    "player_name": "Ahad"
}

save_settings(user_settings)

# Later, load settings
loaded = load_settings()
print("\n⚙️  Current Settings:")
for key, value in loaded.items():
    print(f"  {key}: {value}")
