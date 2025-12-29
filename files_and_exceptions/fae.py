from pathlib import Path

try:
    path = Path('crimeandpunishment.txt')
    contents = path.read_text(encoding='utf-8')
except FileNotFoundError:
    print(f"Sorry, the file {path} does not exist.")

words = contents.splitlines()
num_words = len(words)

print(f"The file {path} has about {num_words} lines")
