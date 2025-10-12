import random

print("🎲 Welcome to Rock-Paper-Scissors!")

# Step 1: Player makes a choice
player_choice = input("Choose rock, paper, or scissors: ").lower()

# Step 2: Computer randomly chooses
options = ["rock", "paper", "scissors"]
computer_choice = random.choice(options)

print(f"\nYou chose: {player_choice}")
print(f"Computer chose: {computer_choice}\n")

# Step 3: Determine the winner
if player_choice == computer_choice:
    print("It's a tie! Nobody wins.")
elif player_choice == "rock":
    if computer_choice == "scissors":
        print("Rock crushes scissors! You win! 💪")
    else:
        print("Paper covers rock! Computer wins! 🤖")
elif player_choice == "paper":
    if computer_choice == "rock":
        print("Paper covers rock! You win! 💪")
    else:
        print("Scissors cut paper! Computer wins! 🤖")
elif player_choice == "scissors":
    if computer_choice == "paper":
        print("Scissors cut paper! You win! 💪")
    else:
        print("Rock crushes scissors! Computer wins! 🤖")
else:
    print("Invalid choice! Please type rock, paper, or scissors next time.")

print("\nThanks for playing!")
