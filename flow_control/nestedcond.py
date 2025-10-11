print("📚 Welcome to the Python Smart Library!\n")

# User input
name = input("Enter your name: ")
age = int(input("Enter your age: "))
is_member = input("Are you a library member? (yes/no): ").lower() == "yes"
book_type = input("Type of book (regular/premium): ").lower()
has_fines = input("Do you have unpaid fines? (yes/no): ").lower() == "yes"

# Outer condition: age check
if age >= 12:
    print(f"\n{name}, you are old enough to borrow books.")

    # Nested condition: membership
    if is_member:
        print("Membership verified!")

        # Nested inside membership: book type
        if book_type == "premium":
            print("Premium book requested.")

            # Nested inside book type: fines
            if has_fines:
                print("Cannot borrow premium books until fines are cleared.")
            else:
                print("You can borrow the premium book. Enjoy!")
        else:
            print("Regular book requested. You can borrow it!")

    else:  # not a member
        print("You must become a member to borrow books.")

else:  # age < 12
    print(f"Sorry {name}, you are too young to borrow books.")

# Additional advice based on fines
if has_fines:
    print("Reminder: Clear your fines to borrow more books.")

print("\nThanks for visiting the Python Smart Library!")
