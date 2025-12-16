from pathlib import Path

file_path = Path("notes.txt")

# Check if exists
if file_path.exists():
    print("✅ File exists!")
else:
    print("❌ File doesn't exist!")

# Check if it's a file
if file_path.is_file():
    print("✅ its a file\nContents:")
    with open("notes.txt", "r") as n:
        notes = n.read()
        print(notes.rstrip())

# Check if it's a directory
if file_path.is_dir():
    print("✅ It's a directory!")
