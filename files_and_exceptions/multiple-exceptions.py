import traceback

def read_file(filename):
    try:
        with open(filename, "r") as f:
            return f.read()

    except FileNotFoundError:
        print("❌ File not found.")
    except PermissionError:
        print("❌ Permission denied.")
    except IsADirectoryError:
        print("❌ That is a directory, not a file.")
    except Exception:
        print("❌ Unexpected error while reading file.")
        traceback.print_exc()
    return None

def write_file(filename, content):
    try:
        with open(filename, "w") as f:
            f.write(content)
        print("✅ File written successfully.")

    except PermissionError:
        print("❌ Permission denied.")
    except IsADirectoryError:
        print("❌ Cannot write to a directory.")
    except Exception:
        print("❌ Unexpected error while writing file.")
        traceback.print_exc()

def main():
    while True:
        print("📁 SMART FILE TOOL")
        print("=" * 30)
        print("1. Read file")
        print("2. Write file")
        print("3. Exit")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            filename = input("Enter filename to read: ").strip()
            content = read_file(filename)
            if content is not None:
                print("\n📄 FILE CONTENT:")
                print("-" * 30)
                print(content)

        elif choice == "2":
            filename = input("Enter filename to write: ").strip()
            content = input("Enter content: ")
            write_file(filename, content)

        elif choice == "3":
            print("👋 Goodbye.")
            break

        else:
            print("❌ Invalid choice.")

main()
