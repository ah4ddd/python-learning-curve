# --- Welcome to the Ultimate Flow Control Experience ---
print("🔥 Welcome to the Python Flow Control Adventure! 🔥\n")

# --- Step 1: Get user info ---
name = input("What's your name, brave coder? ").strip()
age = int(input(f"How old are you, {name}? "))
vip_status = input("Are you a VIP member? (yes/no) ").lower() == "yes"
dress_code = input("Are you dressed sharp? (yes/no) ").lower() == "yes"
favorite_drink = input("What's your favorite drink? ").strip()

# --- Step 2: Initial points (self-assigning example) ---
points = 0
print(f"\n{name}, your starting points: {points}\n")

# --- Step 3: Decision making ---
if age >= 18:  # First level decision
    print("You are old enough to enter the club.")

    if vip_status:  # Nested condition
        print("VIP access granted! 🚪💎")

        if dress_code:  # Nested inside VIP
            print("Looking sharp! Entry is smooth and fast. 🕺")
            points += 10  # self-assigning operator
        else:
            print("VIP, but dress better next time. 😎")
            points += 5

    elif not vip_status:  # elif part
        print("Regular entry, wait in line. ⏳")
        points += 2

    else:  # else for first-level nested
        print("Entry status unknown, security checking. 🤔")
        points += 1
else:  # Age < 18
    print("Sorry, you are underage. ❌")
    points = 0  # Reset points if underage

# --- Step 4: Complex decisions ---
if favorite_drink.lower() == "whiskey" and vip_status and dress_code:
    print("\nYou get a free whiskey shot! 🥃")
    points += 5
elif favorite_drink.lower() == "cocktail" or (not vip_status and age >= 18):
    print("\nYou get a cocktail voucher! 🍹")
    points += 3
else:
    print("\nStandard drinks only. 🍺")
    points += 1

# --- Step 5: Rock-Paper-Scissors mini-game ---
import random

print("\n🎮 Let's play Rock-Paper-Scissors for bonus points! 🎮")
options = ["rock", "paper", "scissors"]
player_choice = input("Choose rock, paper, or scissors: ").lower()
computer_choice = random.choice(options)
print(f"Computer chose: {computer_choice}")

if player_choice == computer_choice:
    print("It's a tie! 🤝")
    points += 1
elif player_choice == "rock":
    if computer_choice == "scissors":
        print("Rock crushes scissors! You win! 💪")
        points += 3
    else:
        print("Paper covers rock! Computer wins! 🤖")
elif player_choice == "paper":
    if computer_choice == "rock":
        print("Paper covers rock! You win! 💪")
        points += 3
    else:
        print("Scissors cut paper! Computer wins! 🤖")
elif player_choice == "scissors":
    if computer_choice == "paper":
        print("Scissors cut paper! You win! 💪")
        points += 3
    else:
        print("Rock crushes scissors! Computer wins! 🤖")
else:
    print("Invalid choice. No points awarded.")

# --- Step 6: Final summary ---
print("\n--- FINAL SUMMARY ---")
print(f"Name: {name}")
print(f"Age: {age}")
print(f"VIP Status: {vip_status}")
print(f"Dress Code: {'Sharp' if dress_code else 'Casual'}")
print(f"Favorite Drink: {favorite_drink}")
print(f"Total Points Earned: {points} 🏆")

if points >= 20:
    print("Legendary performance! You rule the club. 🔥")
elif points >= 10:
    print("Solid effort! Enjoy your night. ✨")
else:
    print("Keep practicing your Python skills! 💻")
