import random

player_money = 100  # Starting money

while player_money > 0:
    print(f"\nYou have ${player_money}. Let's gamble!")

    # Ask for bet
    bet = int(input("Enter your bet amount: "))

    if bet > player_money:
        print("You don't have that much, dumbass!")
        continue  # Go back to start of loop

    # Ask for guess
    guess = int(input("Guess the dice roll (1-6): "))

    if guess < 1 or guess > 6:
        print("Invalid guess! Only numbers 1-6, idiot!")
        continue

dice = random.randint(1, 6)
print(f"The dice rolled: {dice}")

if guess == dice:
    winnings = bet * 2
    player_money += winnings
    print(f"Fuck yeah! You won ${winnings}!")
else:
    player_money -= bet
    print(f"Lame! You lost ${bet}. Try again!")

play_again = input("Do you want to roll again? (yes/no): ").lower()
if play_again != "yes":
    print(f"You leave the table with ${player_money}. Bye, loser!")
    break

if player_money <= 0:
    print("You’re broke, idiot! Game over.")
