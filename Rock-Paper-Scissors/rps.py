import random

options = ["rock", "paper", "scissors"]  # list of possible moves
user_score = 0
computer_score = 0

while True:
    print(f"\nScore -> You: {user_score} | Computer: {computer_score}")
    user_choice = input("Choose rock, paper, or scissors (or 'quit' to exit): ").lower()

    if user_choice == "quit":
        print("You’re leaving the game, pussy. Final score:")
        print(f"You: {user_score} | Computer: {computer_score}")
        break

    if user_choice not in options:
        print("Invalid choice, idiot! Try again.")
        continue

    computer_choice = random.choice(options)
    print(f"Computer chose: {computer_choice}")

    if user_choice == computer_choice:
        print("Tie! Nobody wins this round.")

    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "paper" and computer_choice == "rock") or \
        (user_choice == "scissors" and computer_choice == "paper"):
        print("Fuck yeah! You win this round!")
        user_score += 1

    else:
        print("You lost this round, loser!")
        computer_score += 1
