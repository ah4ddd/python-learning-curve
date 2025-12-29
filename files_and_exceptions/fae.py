from pathlib import Path

def count_words(path):
    try:
        contents = path.read_text(encoding="utf-8")
    except FileNotFoundError:
        pass
    else:
        words = contents.split()
        num_words = len(words)

        print(f"The file {path} has about {num_words} words")

literatures = ['crimeandpunishment.txt', 'metamorphosis.txt',"fuck.txt"]

for books in literatures:
    path = Path(books)
    count_words(path)
