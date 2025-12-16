from pathlib import Path

# Current script location
script_dir = Path(__file__).parent if '__file__' in globals() else Path.cwd()
print(f"Script directory: {script_dir}")

# Project root (assuming script is in a subfolder)
project_root = script_dir.parent
print(f"Project root: {project_root}")

# Build paths relative to project root
data_dir = project_root / "data"
config_file = project_root / "config" / "settings.json"
log_file = project_root / "logs" / "app.log"

print(f"\nPaths:")
print(f"  Data directory: {data_dir}")
print(f"  Config file: {config_file}")
print(f"  Log file: {log_file}")

# Check if data directory exists, create if not
if not data_dir.exists():
    data_dir.mkdir(parents=True)
    print(f"✅ Created: {data_dir}")
else:
    print(f"✅ Exists: {data_dir}")
