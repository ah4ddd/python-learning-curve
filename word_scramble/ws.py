import random

# 1. List of words
words = ["python", "hangman", "developer", "function", "variable", "algorithm"]

# 2. Pick a random word
word = random.choice(words)

# 3. Scramble the word
scrambled = list(word)  # turn word into list of letters
random.shuffle(scrambled)  # shuffle letters randomly
scrambled_word = "".join(scrambled)  # join back into string

# 4. Set attempts
attempts = len(word) + 3  # give player extra tries

print("Welcome to Word Scramble!")
print(f"Unscramble this word: {scrambled_word}")
print(f"The word has {len(word)} letters. You have {attempts} attempts. Good luck, dumbass!")

# 5. Game loop
while attempts > 0:
    guess = input("Your guess: ").lower()  # take input, convert to lowercase

    if guess == word:  # check if correct
        print("Fuck yeah! You got it right!")
        break
    else:
        attempts -= 1  # wrong guess → reduce attempts
        print(f"Wrong, idiot! Attempts left: {attempts}")
        # Hint: show first letter after 2 wrong attempts
        if attempts == len(word) + 1:
            print(f"Hint: first letter is '{word[0]}'")

if attempts == 0:
    print(f"Game over, loser! The word was '{word}'")
