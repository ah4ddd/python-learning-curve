import json
from pathlib import Path

class ConfigError(Exception):
    """Custom exception for config errors."""
    pass

def load_config(filename="config.json"):
    """Load configuration with comprehensive error handling."""
    config_path = Path(filename)

    # Check if file exists
    if not config_path.exists():
        print(f"⚠️ Config file '{filename}' not found!")
        print(f"   Creating default config...")
        return create_default_config(filename)

    # Try to load
    try:
        with open(config_path, "r") as f:
            config = json.load(f)

        # Validate required keys
        required_keys = ["app_name", "version", "settings"]
        missing = [key for key in required_keys if key not in config]
        if missing:
            raise ConfigError(f"Missing required keys: {missing}")

        print(f"✅ Config loaded successfully!")
        return config

    except json.JSONDecodeError as e:
        print(f"❌ Config file has invalid JSON!")
        print(f"   Error at line {e.lineno}, column {e.colno}")
        print(f"   Message: {e.msg}")
        return None

    except ConfigError as e:
        print(f"❌ Config validation failed: {e}")
        return None

    except (PermissionError, OSError) as e:
        print(f"❌ Cannot read config file: {e}")
        return None

    except Exception as e:
        print(f"❌ Unexpected error loading config: {e}")
        return None

def create_default_config(filename):
    """Create a default configuration file."""
    default_config = {
        "app_name": "My App",
        "version": "1.0.0",
        "settings": {
            "theme": "dark",
            "language": "en",
            "notifications": True
        }
    }

    try:
        with open(filename, "w") as f:
            json.dump(default_config, f, indent=4)
        print(f"✅ Created default config: {filename}")
        return default_config
    except Exception as e:
        print(f"❌ Failed to create config: {e}")
        return None

# Use it
config = load_config()
if config:
    print(f"\n📋 Config:")
    print(f"   App: {config['app_name']} v{config['version']}")
    print(f"   Theme: {config['settings']['theme']}")
