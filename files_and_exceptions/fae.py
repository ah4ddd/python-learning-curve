from pathlib import Path

# Create a single directory
data_dir = Path("data")
data_dir.mkdir(exist_ok=True)  # exist_ok=True means no error if already exists
print(f"✅ Created directory: {data_dir}")

# Create nested directories
nested_dir = Path("data") / "input" / "users"
nested_dir.mkdir(parents=True, exist_ok=True)  # parents=True creates all parents
print(f"✅ Created nested directories: {nested_dir}")

# Check it was created
if nested_dir.exists():
    print(f"✅ {nested_dir} exists!")
