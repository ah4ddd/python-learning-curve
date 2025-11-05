contacts = {
    "ahad": {"phone": "9999999999", "email": "ahad@example.com"},
    "sara": {"phone": "8888888888", "email": "sara@example.com"},
    "zexo": {"phone": "7777777777", "email": "zex@example.com"},
}

def view_contacts(inv):
    print("\n📖 Contact List:")
    if not inv:
        print("No contacts found.")
    else:
        for name, info in inv.items():
            print(f" 🌐 {name.title()} 📞 → Phone: {info['phone']} | ✉️ Email: {info['email']}")

def add_contact(inv):
    name = input("Enter contact name: ").lower()
    if name in inv:
        print("Contact already exists.")
        return
    phone = input("Enter phone number: ")
    email = input("Enter email: ")
    inv[name] = {"phone": phone, "email": email}
    print(f"✅ {name.title()} added successfully!")

def update_contact(inv):
    name = input("Enter name to update: ").lower()
    if name not in inv:
        print("Contact not found.")
        return
    phone = input("Enter new phone: ")
    email = input("Enter new email: ")
    inv[name] = {"phone": phone, "email": email}
    print(f"✏️ {name.title()} updated successfully!")

def delete_contact(inv):
    name = input("Enter name to delete: ").lower()
    if name in inv:
        del inv[name]
        print(f"🗑️ {name.title()} deleted successfully!")
    else:
        print("Contact not found.")

def detect_duplicates(inv):
    names = list(inv.keys())
    name_set = set(names)
    if len(names) == len(name_set):
        print("✅ No duplicates found.")
    else:
        print(f"⚠️ Duplicate entries detected : {inv.title}!")

def compare_contacts(inv):
    friend_contacts = input("Enter your friend's contact names (comma separated): ").lower().split(",")
    your_set = set(inv.keys())
    friend_set = set([x.strip() for x in friend_contacts])

    common = your_set & friend_set
    unique_to_you = your_set - friend_set
    unique_to_friend = friend_set - your_set

    print("\n👥 Comparison Results:")
    print("Common contacts:", common if common else "None")
    print("Only in your list:", unique_to_you if unique_to_you else "None")
    print("Only in friend’s list:", unique_to_friend if unique_to_friend else "None")

def export_contacts(inv):
    unique_names = sorted(set(inv.keys()))
    print("\n📤 Exported unique contact names:")
    for n in unique_names:
        print(n.title())

def search_contact(inv):
    contact = input("search contacts by name :").lower()
    if contact not in inv:
        print(f"❌{contact} does not exist")
        return
    for name, info in inv.items():
        if contact == name:
             print(f" 🌐 {name.title()} 📞 → Phone: {info['phone']} | ✉️ Email: {info['email']}")

def count_contacts(inv):
    print(f"total contacts : {(len(inv))}")

def main():
    while True:
        print("\n===== SMART CONTACT MANAGER =====")
        print("1. View Contacts")
        print("2. Add Contact")
        print("3. Update Contact")
        print("4. Delete Contact")
        print("5. Detect Duplicates")
        print("6. Compare Contacts")
        print("7. Export Unique Names")
        print("8. Search Contacts By Name")
        print("9. Count Contacts")
        print("10. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            view_contacts(contacts)
        elif choice == "2":
            add_contact(contacts)
        elif choice == "3":
            update_contact(contacts)
        elif choice == "4":
            delete_contact(contacts)
        elif choice == "5":
            detect_duplicates(contacts)
        elif choice == "6":
            compare_contacts(contacts)
        elif choice == "7":
            export_contacts(contacts)
        elif choice == "8":
            search_contact(contacts)
        elif choice == "9":
            count_contacts(contacts)
        elif choice == "10":
            print("👋 Exiting Contact Manager...")
            break
        else:
            print("Invalid choice, try again.")

main()
