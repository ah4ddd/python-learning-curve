from pathlib import Path

# Current working directory (where your script is running)
current = Path.cwd()
print(f"Current directory: {current}")

# Home directory
home = Path.home()
print(f"Home directory: {home}")

# Create a path
data_file = Path("data") / "input.txt"
print(f"File path: {data_file}")
