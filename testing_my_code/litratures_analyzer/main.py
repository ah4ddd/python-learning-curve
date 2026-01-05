"""
Interactive literature analyzer.
Uses the analyzer module for core functionality.
"""

import json
from analyzer import how_many_times, save_results

literatures = [
    ("books/crimeandpunishment.txt", "Crime and Punishment"),
    ("books/metamorphosis.txt", "Metamorphosis"),
    ("books/macbeth.txt", "Macbeth")
]

# Display menu
for i, (_, title) in enumerate(literatures, start=1):
    print(f"{i}: {title}")

try:
    choice = int(input("\nChoose book file, via number: "))
    name = input("Enter a character name: ").strip()

    file_path, book_title = literatures[choice - 1]

    # Use analyzer module
    results = how_many_times(file_path, name)
    count = len(results)

    print(f"\n{name.title()} appears on {count} lines in {book_title}.\n")

    for idx, match in enumerate(results, start=1):
        print(f"{idx}. Line {match['line_number']}:")
        print(match['text'])
        print()

    # Save option
    save = input("Do you want to save this search to a file? (yes/no): ").lower()

    if save == "yes":
        saved = save_results(name, book_title, results)
        if saved:
            print(f"✅ Results saved to {name.lower()}.json")
        else:
            print("⚠️ This search already exists. Nothing was saved.")

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
