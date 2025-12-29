from pathlib import Path

try:
    path = Path('crimeandpunishment.txt')
    contents = path.read_text(encoding='utf-8')
except FileNotFoundError:
    print(f"Sorry, the file {path} does not exist.")

print(contents)
