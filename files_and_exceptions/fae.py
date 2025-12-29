literatures = ['crimeandpunishment.txt', 'metamorphosis.txt']
for i,book in enumerate(literatures):
    print(f"{i+1}: {book}")

def how_many_times(path, search):
    with open(path, "r", encoding="utf-8") as f:
        return f.read().lower().count(search.lower())

try:
    file = int(input("Choose book file, via number: "))
    name = input("Enter a character name: ")
    if file == 1:
        file = "crimeandpunishment.txt"
    elif file == 2:
        file = "metamorphosis.txt"
    else:
        print("Invalid choice")
        raise ValueError

    count = how_many_times(file, name)
    print(f"{name.title()} appears {count} times.")

except FileNotFoundError:
    print(f"❌ file does not exist : {file} ❌")
except ValueError:
    print("❌ Please enter a valid number ❌")

