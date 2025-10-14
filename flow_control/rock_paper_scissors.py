import random

print("🎲 Welcome to Rock-Paper-Scissors!")

# Step 0: Initialize counters
player_score = 0
computer_score = 0
round_number = 0

# Step 1: Loop the game
while True:
    round_number += 1
    print(f"\n--- Round {round_number} ---")

    # Player choice
    player_choice = input("Choose rock, paper, or scissors (or 'quit' to exit): ").lower()

    # Computer choice
    options = ["rock", "paper", "scissors"]
    computer_choice = random.choice(options)

    print(f"\nYou chose: {player_choice}")
    print(f"Computer chose: {computer_choice}\n")

    # Determine winner
    if player_choice == computer_choice:
        print("It's a tie! Nobody wins.")

    elif player_choice == "rock": # rock case
        if computer_choice == "scissors":
            print("Rock crushes scissors! You win! 💪")
            player_score += 1
        else:
            print("Paper covers rock! Computer wins! 🤖")
            computer_score += 1

    elif player_choice == "paper": # paper case
        if computer_choice == "rock":
            print("Paper covers rock! You win! 💪")
            player_score += 1
        else:
            print("Scissors cut paper! Computer wins! 🤖")
            computer_score += 1

    elif player_choice == "scissors": # scissors case
        if computer_choice == "paper":
            print("Scissors cut paper! You win! 💪")
            player_score += 1
        else:
            print("Rock crushes scissors! Computer wins! 🤖")
            computer_score += 1

    else:
        print("Invalid choice! Please type rock, paper, or scissors next time.")
        round_number -= 1  # invalid round doesn't count
        continue

    if player_choice == "quit":
        print("\nThanks for playing!")
        break

    # Show current score
    print(f"\nScore: You {player_score} - Computer {computer_score}")

# Final score
print(f"\nFinal Score after {round_number} rounds: You {player_score} - Computer {computer_score}")

