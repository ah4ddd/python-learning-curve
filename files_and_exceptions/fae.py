with open("output.txt", "w") as f:
    f.write("Hello, this is my first written file!")

with open("story.txt", "w") as f:
    f.write("Once upon a time...\n")
    f.write("There was a programmer named Ahad.\n")
    f.write("He mastered Python in 61 days.\n")
    f.write("The end.\n")

lines = [
    "Once upon a time...\n",
    "There was a programmer named Ahad.\n",
    "He mastered Python in 61 days.\n",
    "The end.\n"
]

with open("story.txt", "w") as f:
    f.writelines(lines)

story = """Once upon a time...
There was a programmer named Ahad.
He mastered Python in 61 days.
The end.
"""

with open("story.txt", "w") as f:
    f.write(story)

with open("important.txt", "w") as f:
    f.write("This is very important data!\n")
    f.write("Do not delete this!\n")

print("File created with important data!")

# Oops, accidentally open in "w" mode again!
with open("important.txt", "w") as f:
    f.write("New data\n")

print("Check the file now...")

# Create initial file
with open("log.txt", "w") as f:
    f.write("Day 1: Started learning Python\n")

print("Initial file created!")

# Add more data (APPEND mode!)
with open("log.txt", "a") as f:
    f.write("Day 2: Learned variables and loops\n")

print("Added Day 2!")

# Add even more
with open("log.txt", "a") as f:
    f.write("Day 3: Mastered functions\n")

print("Added Day 3!")

# Read and display the result
with open("log.txt", "r") as f:
    content = f.read()
    print("\nFile contents:")
    print(content)

quotes = [
    "Why are you still coding? Go touch grass.",
    "Your code works? Impressive. Barely.",
    "Did you even test that function?",
    "Stop snacking and finish the project.",
    "I'm not mad, just disappointed in your variable names."
]

# Save quotes to file
with open("mia_quotes.txt", "w") as f:
    for quote in quotes:
        f.write(quote + "\n")

print("✅ Mia's quotes saved!")

# Read them back
with open("mia_quotes.txt", "r") as f:
    print("\n📝 Mia's Wisdom:")
    print(f.read())
