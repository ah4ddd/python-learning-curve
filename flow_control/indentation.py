# Club Entry Mini Project

print("Welcome to the Python Club!")

# Ask user for details
age = int(input("Enter your age: "))
has_id = input("Do you have an ID? (yes/no): ").lower() == "yes"
vip_pass = input("Do you have a VIP pass? (yes/no): ").lower() == "yes"

# Decision block
if age >= 18 and has_id:
    print("\nYou can enter the club!")

    if vip_pass:
        print("Wow! You also have a VIP pass. Enjoy the VIP lounge!")
    else:
        print("No VIP pass? That's fine, enjoy the regular area.")

elif age >= 18 and not has_id:
    print("\nYou are an adult but you need an ID to enter.")

else:
    print("\nSorry, you are underage and cannot enter.")

# End message
print("\nThank you for visiting the Python Club!")

