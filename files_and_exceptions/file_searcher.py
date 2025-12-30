literatures = [
    ("crimeandpunishment.txt", "Crime and Punishment"),
    ("metamorphosis.txt", "Metamorphosis"),
    ("macbeth.txt", "Macbeth")
]

for i, (_, title) in enumerate(literatures, start=1):
    print(f"{i}: {title}")

def how_many_times(path, search):
    matches = []
    with open(path, "r", encoding="utf-8") as f:
        for line_number, line in enumerate(f, start=1):
            if search.lower() in line.lower():
                matches.append((line_number, line.strip()))
    return matches

try:
    choice = int(input("Choose book file, via number: "))
    name = input("Enter a character name: ")

    file_path, book_title = literatures[choice - 1]

    results = how_many_times(file_path, name)
    count = len(results)

    print(f"\n{name.title()} appears on {count} lines in {book_title}.\n")

    for idx, (line_number, text) in enumerate(results, start=1):
        print(f"{idx}. Line {line_number}:")
        print(text)
        print()

except (ValueError, IndexError):
    print("❌ Invalid choice ❌")
except FileNotFoundError:
    print("❌ File not found ❌")
