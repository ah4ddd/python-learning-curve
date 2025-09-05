# 1. Welcome the player
print("Welcome to the savage Quiz Game! Test your brain or cry!")

# 2. Create the quiz dictionary
quiz = {
    "What is the capital of France?": {
        "a": "Paris",
        "b": "London",
        "c": "Berlin",
        "d": "Rome",
        "answer": "a"
    },

    "What is 5 + 7?": {
        "a": "10",
        "b": "12",
        "c": "13",
        "d": "14",
        "answer": "b"
    },

    "Which planet is known as the Red Planet?": {
        "a": "Earth",
        "b": "Venus",
        "c": "Mars",
        "d": "Jupiter",
        "answer": "c"
    }
}

# 3. Initialize score
score = 0

# 4. Loop through questions
for question, options in quiz.items():
    print("\n" + question)  # Show question
    # Show all choices
    for key in ['a', 'b', 'c', 'd']:
        print(f"{key}: {options[key]}")

    # 5. Get user answer
    answer = input("Your answer (a/b/c/d): ").lower()

    # 6. Check if correct
    if answer == options["answer"]:
        print("Correct! You’re a brain god!")
        score += 1
    else:
        print(f"Wrong! The correct answer was {options['answer']}: {options[options['answer']]}")

# 7. Show final score
print(f"\nGame over, champ! Your final score is: {score}/{len(quiz)}")
