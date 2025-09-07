import random

word_list = ["python", "hangman", "computer", "programming", "developer"]
word = random.choice(word_list)
guessed_letters = []
attempts = 6

print("Welcome to Hangman, loser! Guess the word one letter at a time.")

while attempts > 0:
    display_word = ""
    for letter in word:
        if letter in guessed_letters:
            display_word += letter
        else:
            display_word += "_"

    print(f"\nWord: {display_word}")

    if "_" not in display_word:
        print("Fuck yeah! You guessed the word and won!")
        break

    guess = input("Guess a letter: ").lower()

    if guess in guessed_letters:
        print("You already tried that, dumbass!")
        continue

    guessed_letters.append(guess)

    if guess in word:
        print("Nice! That letter is in the word.")
    else:
        attempts -= 1
        print(f"Wrong! You have {attempts} attempts left, loser!")

if attempts == 0:
    print(f"Game over, idiot! The word was '{word}'.")
