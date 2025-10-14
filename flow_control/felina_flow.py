import random

print("🎮 Welcome to the Python Game Hub! 🎮")

# Player stats
player_score_rps = 0
player_score_guess = 0
round_rps = 0
round_guess = 0

while True:
    print("\nMain Menu:")
    print("1. Rock-Paper-Scissors")
    print("2. Number Guessing Game")
    print("3. Quit")

    choice = input("Choose a game or quit (1/2/3): ").lower()

    if choice == "3" or choice == "quit":
        print("\nThanks for playing! Final Scores:")
        print(f"RPS: {player_score_rps} | Number Guess: {player_score_guess}")
        break

    elif choice == "1":
        # --- Rock-Paper-Scissors ---
        while True:
            round_rps += 1
            print(f"\n--- RPS Round {round_rps} ---")
            player = input("Choose rock, paper, or scissors (or 'quit' to return): ").lower()

            if player == "quit":
                break

            # Random computer choice using numbers (no list)
            comp_number = random.randint(1, 3)
            if comp_number == 1:
                computer = "rock"
            elif comp_number == 2:
                computer = "paper"
            else:
                computer = "scissors"

            print(f"You chose: {player}")
            print(f"Computer chose: {computer}")

            if player == computer:
                print("It's a tie!")

            elif (player == "rock" and computer == "scissors") or \
                 (player == "paper" and computer == "rock") or \
                 (player == "scissors" and computer == "paper"):
                print("You win! 💪")
                player_score_rps += 1

            elif player in ("rock", "paper", "scissors"):
                print("Computer wins! 🤖")
            else:
                print("Invalid choice! Try again.")
                round_rps -= 1
                continue

            print(f"Score: You {player_score_rps}")

    elif choice == "2":
        # --- Number Guessing Game ---
        print("\nWelcome to Number Guessing Game!")
        number_to_guess = random.randint(1, 20)

        while True:
            round_guess += 1
            guess = input("Guess a number between 1-20 (or 'quit' to return): ").lower()

            if guess == "quit":
                break

            if not guess.isdigit():
                print("Invalid input! Enter a number.")
                round_guess -= 1
                continue

            guess = int(guess)

            if guess == number_to_guess:
                print("Correct! You win! 💪")
                player_score_guess += 1
                break
            elif guess < number_to_guess:
                print("Too low!")
            else:
                print("Too high!")

    else:
        print("Invalid menu choice! Pick 1, 2, or 3.")
