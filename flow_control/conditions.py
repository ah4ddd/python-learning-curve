print("🎬 Welcome to the Python Movie Theater!\n")

# User input
name = input("Enter your name: ")
age = int(input("Enter your age: "))
has_ticket = input("Do you have a ticket? (yes/no): ").lower() == "yes"
is_member = input("Are you a theater member? (yes/no): ").lower() == "yes"
vip_pass = input("Do you have a VIP pass? (yes/no): ").lower() == "yes"

# Store conditions in variables
can_enter = age >= 13 and has_ticket
vip_access = can_enter and vip_pass
free_snack = can_enter and (is_member or vip_pass)

# Decision making
if can_enter:
    print(f"\nWelcome, {name}! You can watch the movie.")

    if vip_access:
        print("You have VIP access! Enjoy the premium seats.")

    if free_snack:
        print("You get a free snack!")
    else:
        print("No free snack this time.")

elif age >= 13 and not has_ticket:
    print(f"\n{name}, you need a ticket to enter.")

else:
    print(f"\n{name}, sorry, you are underage and cannot watch the movie.")

# Extra advice
if not has_ticket:
    print("Tip: Buy your ticket online next time!")
if not is_member:
    print("Consider becoming a member for extra perks.")

print("\nThank you for visiting Python Movie Theater!")
