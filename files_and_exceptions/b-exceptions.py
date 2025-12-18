def read_file_safe(filename):

    try:
        with open(filename, "r") as f:
            content = f.read()
        print(f"✅ Successfully read {len(content)} characters!")
        return content
    except FileNotFoundError:
        print(f"❌ Error: File '{filename}' not found!")
        return None
    except PermissionError:
        print(f"❌ Error: No permission to read '{filename}'!")
        return None
    except Exception as e:
        print(f"❌ Unexpected error: {e}")
        return None

content = read_file_safe("data.json")
if content:
    print(f"First 50 characters: {content[:160]}")
else:
    print("Could not read file!")
