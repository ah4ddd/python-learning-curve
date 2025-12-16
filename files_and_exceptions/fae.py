from pathlib import Path
import platform

print(f"Operating System: {platform.system()}")
print(f"Python Platform: {platform.platform()}\n")

# These work on ALL platforms!
home = Path.home()
current = Path.cwd()
file_path = Path("data") / "users" / "ahad.txt"

print(f"Home directory: {home}")
print(f"Current directory: {current}")
print(f"File path: {file_path}")

# Path automatically uses correct separators!
print(f"\nPath as string: {str(file_path)}")
# Windows: data\users\ahad.txt
# Mac/Linux: data/users/ahad.txt

# Convert to absolute path
absolute = file_path.resolve()
print(f"Absolute path: {absolute}")
