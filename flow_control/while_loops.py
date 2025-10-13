# guess the number

import random

# Computer picks a number between 1 and 10
secret_number = random.randint(1, 10)
attempts = 0
max_attempts = 5

print("🎯 Welcome to Guess the Number!")
print("I have picked a number between 1 and 10.")
print("You have 5 attempts to guess it.\n")

# while loop begins
while attempts < max_attempts:
    guess = int(input("Enter your guess: "))
    attempts += 1  # increases attempt count

    if guess == secret_number:
        print(f"🔥 You got it right in {attempts} tries!")
        break  # stops the loop if correct
    elif guess < secret_number:
        print("Too low! Try again.\n")
    else:
        print("Too high! Try again.\n")

    # show attempts left
    print(f"Attempts left: {max_attempts - attempts}\n")

# when loop ends
if attempts == max_attempts and guess != secret_number:
    print(f"😢 Out of tries! The number was {secret_number}. Better luck next time.")
