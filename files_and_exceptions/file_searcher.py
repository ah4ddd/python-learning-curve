import json
from pathlib import Path

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
                matches.append({
                    "line_number": line_number,
                    "text": line.strip()
                })
    return matches

def save_results(character, book_title, results):
    file_path = Path(f"{character.lower()}.json")

    entry = {
        "book": book_title,
        "count": len(results),
        "matches": results
    }

    if file_path.exists():
        data = json.loads(file_path.read_text())
    else:
        data = {
            "character": character,
            "searches": []
        }

    for search in data["searches"]:
        if search["book"] == book_title:
            return False

    data["searches"].append(entry)

    file_path.write_text(
        json.dumps(data, indent=4, ensure_ascii=False),
        encoding="utf-8"
    )
    return True

try:
    choice = int(input("\nChoose book file, via number: "))
    name = input("Enter a character name: ").strip()

    file_path, book_title = literatures[choice - 1]

    results = how_many_times(file_path, name)
    count = len(results)

    print(f"\n{name.title()} appears on {count} lines in {book_title}.\n")

    for idx, match in enumerate(results, start=1):
        print(f"{idx}. Line {match['line_number']}:")
        print(match['text'])
        print()

    save = input("Do you want to save this search to a file? (yes/no): ").lower()

    if save == "yes":
        saved = save_results(name, book_title, results)
    if saved:
        print(f"Results saved to {name.lower()}.json")
    else:
        print("This search already exists. Nothing was saved.")


except json.JSONDecodeError:
    print("❌ Saved JSON file is corrupted ❌")

except ValueError:
    print("❌ Please enter a valid number ❌")

except IndexError:
    print("❌ Choice out of range ❌")

except FileNotFoundError:
    print("❌ Book file not found ❌")

except Exception as e:
    print(f"❌ Unexpected error: {e} ❌")
