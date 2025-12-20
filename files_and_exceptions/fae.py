def process_file(filename):
    """Read and process a file."""
    try:
        with open(filename, "r") as f:
            content = f.read()
    except FileNotFoundError:
        print(f"❌ File '{filename}' not found!")
        return None
    except PermissionError:
        print(f"❌ No permission to read '{filename}'!")
        return None
    else:
        # File was read successfully, now process it
        print(f"✅ File read successfully!")
        lines = content.split('\n')
        print(f"   Total lines: {len(lines)}")
        return content

# Use it
content = process_file("guest.txt")
if content:
    print(f"First 50 chars: {content[:50]}")
