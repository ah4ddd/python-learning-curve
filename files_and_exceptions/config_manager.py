import json
from pathlib import Path

# Custom exceptions
class ConfigError(Exception):
    """Base exception for config errors."""
    pass

class ConfigNotFoundError(ConfigError):
    """Config file not found."""
    pass

class ConfigInvalidError(ConfigError):
    """Config file has invalid structure."""
    pass

# Config manager class
class ConfigManager:
    """Manage application configuration with proper error handling."""

    def __init__(self, config_path="config.json"):
        """Initialize config manager.

        Args:
            config_path: Path to config file
        """
        self.config_path = Path(config_path)
        self.config = None

    def _get_default_config(self):
        """Get default configuration."""
        return {
            "app_name": "My App",
            "version": "1.0.0",
            "settings": {
                "theme": "dark",
                "language": "en",
                "notifications": True
            },
            "database": {
                "host": "localhost",
                "port": 5432
            }
        }

    def _validate_config(self, config):
        """Validate config structure.

        Args:
            config: Config dict to validate

        Raises:
            ConfigInvalidError: If config is invalid
        """
        required_keys = ["app_name", "version", "settings", "database"]

        for key in required_keys:
            if key not in config:
                raise ConfigInvalidError(f"Missing required key: {key}")

        # Validate nested structures
        if "theme" not in config["settings"]:
            raise ConfigInvalidError("Missing 'theme' in settings")

        if "host" not in config["database"]:
            raise ConfigInvalidError("Missing 'host' in database")

    def load(self):
        """Load configuration from file.

        Returns:
            dict: Configuration data

        Raises:
            ConfigNotFoundError: If file doesn't exist
            ConfigInvalidError: If config is invalid
        """
        # Check if file exists
        if not self.config_path.exists():
            raise ConfigNotFoundError(f"Config file not found: {self.config_path}")

        try:
            # Read and parse JSON
            with open(self.config_path, "r") as f:
                config = json.load(f)

            # Validate structure
            self._validate_config(config)

            # Store and return
            self.config = config
            return config

        except json.JSONDecodeError as e:
            # JSON is malformed
            raise ConfigInvalidError(f"Invalid JSON in config file: {e}")

        except Exception as e:
            # Unexpected error
            raise ConfigError(f"Failed to load config: {e}")

    def create_default(self):
        """Create default config file.

        Returns:
            dict: Default configuration
        """
        config = self._get_default_config()

        try:
            with open(self.config_path, "w") as f:
                json.dump(config, f, indent=4)

            self.config = config
            return config

        except Exception as e:
            raise ConfigError(f"Failed to create default config: {e}")

    def save(self):
        """Save current config to file.

        Raises:
            ConfigError: If no config loaded or save fails
        """
        if self.config is None:
            raise ConfigError("No config loaded to save!")

        try:
            # Write to temp file first (safer!)
            temp_path = self.config_path.with_suffix('.json.tmp')

            with open(temp_path, "w") as f:
                json.dump(self.config, f, indent=4)

            # Rename temp to actual (atomic)
            temp_path.replace(self.config_path)

        except Exception as e:
            raise ConfigError(f"Failed to save config: {e}")

    def get(self, key, default=None):
        """Get config value safely.

        Args:
            key: Config key (supports dot notation)
            default: Default if key not found

        Returns:
            Value or default
        """
        if self.config is None:
            return default

        # Support dot notation: "settings.theme"
        keys = key.split(".")
        value = self.config

        for k in keys:
            if isinstance(value, dict) and k in value:
                value = value[k]
            else:
                return default

        return value

    def set(self, key, value):
        """Set config value.

        Args:
            key: Config key (supports dot notation)
            value: Value to set
        """
        if self.config is None:
            raise ConfigError("No config loaded!")

        # Support dot notation
        keys = key.split(".")
        current = self.config

        for k in keys[:-1]:
            if k not in current:
                current[k] = {}
            current = current[k]

        current[keys[-1]] = value

# Usage example
def main():
    """Demo the config manager."""
    manager = ConfigManager("app_config.json")

    try:
        # Try to load existing config
        config = manager.load()
        print("✅ Config loaded successfully!")

    except ConfigNotFoundError:
        # Create default if missing
        print("⚠️ Config not found, creating default...")
        config = manager.create_default()
        print("✅ Default config created!")

    except ConfigInvalidError as e:
        # Config is broken
        print(f"❌ Config is invalid: {e}")
        print("   Creating fresh default...")
        config = manager.create_default()

    except ConfigError as e:
        # Other config error
        print(f"❌ Config error: {e}")
        return

    # Display current config
    print("\n📋 Current Configuration:")
    print(f"  App: {manager.get('app_name')} v{manager.get('version')}")
    print(f"  Theme: {manager.get('settings.theme')}")
    print(f"  Language: {manager.get('settings.language')}")
    print(f"  Database: {manager.get('database.host')}:{manager.get('database.port')}")

    # Modify config
    print("\n🔧 Modifying config...")
    manager.set("settings.theme", "light")
    manager.set("settings.language", "hi")

    # Save changes
    try:
        manager.save()
        print("✅ Config saved!")
    except ConfigError as e:
        print(f"❌ Failed to save: {e}")

if __name__ == "__main__":
    main()
