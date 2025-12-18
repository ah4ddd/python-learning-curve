import json

FILE_NAME = "data.json"

def load_data():
    try:
        with open(FILE_NAME, "r") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def save_data(data):
    with open(FILE_NAME, "w") as f:
        json.dump(data, f, indent=4)

def add_entry():
    title = input("Title: ").strip()
    note = input("Note: ").strip()

    entry = {
        "title": title,
        "note": note
    }

    data = load_data()
    data.append(entry)
    save_data(data)

    print("✅ Entry saved.\n")

def list_entries():
    data = load_data()

    if not data:
        print("📭 No entries found.\n")
        return

    print("\n📘 YOUR ENTRIES")
    print("=" * 40)

    for i, entry in enumerate(data, start=1):
        print(f"{i}. {entry['title']}")
        print(f"   {entry['note']}")
        print("-" * 40)

    print()

def main():
    while True:
        print("1. Add entry")
        print("2. List entries")
        print("3. Exit")

        choice = input("Choose: ").strip()

        if choice == "1":
            add_entry()
        elif choice == "2":
            list_entries()
        elif choice == "3":
            print("👋 Bye.")
            break
        else:
            print("❌ Invalid choice.\n")

if __name__ == "__main__":
    main()
