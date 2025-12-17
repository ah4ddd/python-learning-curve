import json

def add_guest(name, reason):
    """Add a guest to the guest book."""
    # Load existing guests
    try:
        with open("guests.json", "r") as f:
            guests = json.load(f)
    except FileNotFoundError:
        guests = []

    # Add new guest
    guest = {
        "name": name,
        "reason": reason
    }
    guests.append(guest)

    # Save back to file
    with open("guests.json", "w") as f:
        json.dump(guests, f, indent=4)

    print(f"✅ Added {name}!")

def list_guests():
    """Display all guests."""
    try:
        with open("guests.json", "r") as f:
            guests = json.load(f)
    except FileNotFoundError:
        print("No guests yet!")
        return

    print("\n📖 GUEST BOOK:")
    print("="*50)
    for guest in guests:
        print(f"Name: {guest['name']}")
        print(f"Reason: {guest['reason']}")
        print("-"*50)

# Add some guests
add_guest("Ahad", "Building tech empire")
add_guest("Mia", "Making sure Ahad doesn't slack")
add_guest("Sara", "Learning Python too")

# Display all
list_guests()
