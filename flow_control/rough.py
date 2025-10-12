print("🎶 Welcome to The Code Lounge 🎶")

age = int(input("How old are you? "))
is_member = input("Are you a member? (yes/no): ").lower() == "yes"
dress_code = input("Are you dressed to impress? (yes/no): ").lower() == "yes"

if age >= 18:
    if is_member:
        if dress_code:
            print("🔥 VIP access granted! You look sharp and ready to roll.")
        else:
            print("😬 Bro, you made it this far but no sneakers allowed. Dress better next time.")
    else:
        print("🪪 Sorry, no membership, no entry. Try applying online.")
else:
    print("🚫 You’re too young for this club, champ. Come back when you’ve seen some life.")


# age >= 18?
# ├─ Yes → is_member?
# │      ├─ Yes → dress_code?
# │      │       ├─ Yes → VIP Access ✅
# │      │       └─ No  → Dress Better ❌
# │      └─ No  → No Membership ❌
# └─ No  → Too Young ❌
