import json

def load_data(filename):
    try:
        with open(filename, "r") as f:
            data = json.load(f)
        return data
    except (FileNotFoundError, json.JSONDecodeError,):
        print(f"could not found '{filename}'(missing or invalid)")
        return {}

data = load_data("data.json")
print(type(data))
