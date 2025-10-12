print("Welcome to Movie Classifier!")

age = int(input("Enter your age: "))
genre = input("Enter your favorite genre (action/comedy/horror): ").lower()

# First check age
if age < 13:
    print("You can only watch G-rated movies.")
elif age < 18:
    print("You can watch PG-13 movies.")
elif age < 21:
    print("You can watch R-rated movies.")
else:
    print("You can watch all movies!")

# Genre recommendation using another elif chain
if genre == "action":
    print("We recommend: Inception, John Wick, and Terminator.")
elif genre == "comedy":
    print("We recommend: The Mask, Superbad, and Step Brothers.")
elif genre == "horror":
    print("We recommend: The Conjuring, The Shining, and Possesion.")
else:
    print("We recommend exploring new genres!")

print("\nEnjoy your movies! 🎬")
