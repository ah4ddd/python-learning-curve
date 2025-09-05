import random  # 1

print("Welcome to the number guessing game, loser!")  # 2
print("I have picked a number between 1 and 100. Try to guess it!")  # 3

# Computer picks a random number between 1 and 100
number_to_guess = random.randint(1, 100)  # 4
guess = None  # 5
attempts = 0  # 6

# Start the guessing loop
while guess != number_to_guess:  # 7
    guess = int(input("Enter your pathetic guess: "))  # 8
    attempts += 1  # 9

    if guess < number_to_guess:  # 10
        print("Too low! Try harder!")  # 11
    elif guess > number_to_guess:  # 12
        print("Too high! Come on!")  # 13
    else:  # 14
        print(f"Bullseye! You got it in {attempts} tries. Not too shabby.")  # 15
