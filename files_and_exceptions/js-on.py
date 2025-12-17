import json

def save_settings(settings):
    """Save user settings to JSON."""
    with open("settings.json", "w") as f:
        json.dump(settings, f, indent=4)
    print("✅ Settings saved!")

def load_settings():
    """Load user settings from JSON."""
    try:
        with open("settings.json", "r") as f:
            settings = json.load(f)
        print("✅ Settings loaded!")
        return settings
    except FileNotFoundError:
        print("⚠️ No settings file found, using defaults!")
        return {
            "volume": 80,
            "difficulty": "medium",
            "fullscreen": False,
            "language": "en"
        }

def display_settings(settings):
    """Display current settings."""
    print("\n⚙️  CURRENT SETTINGS:")
    for key, value in settings.items():
        print(f"  {key}: {value}")

# Load settings (or create defaults)
settings = load_settings()
display_settings(settings)

# User changes settings
print("\n🔧 Changing settings...")
settings["volume"] = 100
settings["difficulty"] = "hard"
settings["fullscreen"] = True

# Save changes
save_settings(settings)
display_settings(settings)
