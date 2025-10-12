print("🤖 Welcome to the AI Innovators Club Entry System 🤖\n")

# Gather user info
name = input("Enter your name: ")
age = int(input("Enter your age: "))
is_member = input("Are you a registered club member? (yes/no): ").lower() == "yes"
has_guest_pass = input("Do you have a guest pass? (yes/no): ").lower() == "yes"
is_vip = input("Are you a VIP? (yes/no): ").lower() == "yes"
banned = input("Have you ever been banned from the club? (yes/no): ").lower() == "yes"

# Complex Decision Logic

if not banned:  # Only proceed if user is not banned
    if (age >= 21 and is_member) or is_vip:
        print(f"\nWelcome {name}! You have full access to the AI Club Lounge 🧠💼")
    elif age >= 18 and (has_guest_pass or is_member):
        print(f"\nHey {name}, you can enter the general area but not the VIP lounge 🚪")
    elif (age < 18 and has_guest_pass) and not is_member:
        print(f"\n{name}, you’re allowed in as a guest but under supervision 👀")
    else:
        print(f"\nSorry {name}, you don’t meet the entry requirements ❌")
else:
    print(f"\nAccess Denied. {name}, you’re on the banned list 🚫")

print("\nSystem Log: Decision completed ✅")
