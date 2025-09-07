import random

full_list = ["python", "hangman", "computer", "programming", "developer", "algorithm", "function", "variable"]

options = random.sample(full_list, 5)

word = random.choice(options)

guessed_letters = []
wrong_letters = []
attempts = 6

print("Welcome to Hangman, loser!")
print("Here are your possible words:")
print(", ".join(options))
print(f"The word has {len(word)} letters. Good luck, dumbass!")

while attempts > 0:
    display_word = ""
    for letter in word:
        if letter in guessed_letters:
            display_word += letter
        else:
            display_word += "_"

    print(f"\nWord: {display_word}")
    print(f"Wrong guesses: {', '.join(wrong_letters)}")

    if "_" not in display_word:
        print("Fuck yeah! You guessed the word and won!")
        break

    guess = input("Guess a single letter: ").lower()

    if len(guess) != 1 or not guess.isalpha():
        print("One letter only, dumbass!")
        continue

    if guess in guessed_letters or guess in wrong_letters:
        print("You already tried that, idiot!")
        continue

    if guess in word:
        print(f"Nice! The letter '{guess}' is in the word.")
        guessed_letters.append(guess)
    else:
        print(f"Wrong! '{guess}' is not in the word.")
        wrong_letters.append(guess)
        attempts -= 1
        print(f"You have {attempts} attempts left, loser!")

if attempts == 0:
    print(f"Game over, idiot! The word was '{word}'.")
