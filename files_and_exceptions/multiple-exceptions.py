import json

def load_json_file(filename):
    try:
        with open(filename, "r") as f:
            data = json.load(f)
        return data
    except FileNotFoundError:
        print(f"❌ File '{filename}' doesn't exist!")
        print("   Create it or check the filename.")
        return None
    except json.JSONDecodeError as e:
        print(f"❌ File '{filename}' has invalid JSON!")
        print(f"   Error: {e.msg} at line {e.lineno}, column {e.colno}")
        return None
    except PermissionError:
        print(f"❌ No permission to read '{filename}'!")
        return None
    except Exception as e:
        print(f"❌ Unexpected error: {e}")
        return None

data = load_json_file("data.json")
