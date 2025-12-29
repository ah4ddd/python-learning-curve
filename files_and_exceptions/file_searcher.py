literatures = ['crimeandpunishment.txt', 'metamorphosis.txt']

for i, book in enumerate(literatures, start=1):
    print(f"{i}: {book}")

def how_many_times(path, search):
    with open(path, "r", encoding="utf-8") as f:
        return f.read().lower().count(search.lower())

try:
    choice = int(input("Choose book file, via number: "))
    name = input("Enter a character name: ")

    file = literatures[choice - 1]
    count = how_many_times(file, name)

    print(f"{name.title()} appears {count} times in {file}")

except (ValueError, IndexError):
    print("❌ Invalid choice ❌")
except FileNotFoundError:
    print("❌ File not found ❌")
