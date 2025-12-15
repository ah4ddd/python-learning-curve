from datetime import datetime

def add_note():
    """Add a new note."""
    note = input("Enter your note: ").strip()
    if note:
        with open("notes.txt", "a") as f:
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")
            f.write(f"[{timestamp}] {note}\n")
        print("✅ Note saved!")
    else:
        print("❌ Note cannot be empty!")

def view_notes():
    """View all notes."""
    try:
        with open("notes.txt", "r") as f:
            notes = f.read()
            if notes:
                print("\n📝 YOUR NOTES:")
                print("="*50)
                print(notes)
            else:
                print("📝 No notes yet!")
    except FileNotFoundError:
        print("📝 No notes yet!")

def clear_notes():
    """Delete all notes."""
    confirm = input("Are you sure you want to delete all notes? (yes/no): ")
    if confirm.lower() == "yes":
        with open("notes.txt", "w") as f:
            pass  # Open in write mode and write nothing = clears file
        print("✅ All notes deleted!")
    else:
        print("❌ Cancelled!")

# Main menu
while True:
    print("\n📓 NOTES APP")
    print("1. Add Note")
    print("2. View Notes")
    print("3. Clear All Notes")
    print("4. Exit")

    choice = input("\nChoose option: ").strip()

    if choice == "1":
        add_note()
    elif choice == "2":
        view_notes()
    elif choice == "3":
        clear_notes()
    elif choice == "4":
        print("👋 Goodbye!")
        break
    else:
        print("❌ Invalid choice!")
