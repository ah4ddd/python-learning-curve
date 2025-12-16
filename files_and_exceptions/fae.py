from pathlib import Path

def read_file_safely(filename):
    """Read a file with proper error checking."""
    file_path = Path(filename)

    # Check if exists
    if not file_path.exists():
        print(f"❌ Error: '{filename}' doesn't exist!")
        return None

    # Check if it's actually a file
    if not file_path.is_file():
        print(f"❌ Error: '{filename}' is not a file!")
        return None

    # Now safe to read
    with open(file_path, "r") as f:
        content = f.read()

    print(f"✅ Read {len(content)} characters from '{filename}'")
    return content

# Test it
content = read_file_safely("notes.txt")
if content:
    print(content)

# Try with non-existent file
content = read_file_safely("guest.txt")
