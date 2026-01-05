"""
Character frequency analyzer for literature.

This module provides functions to search for characters/words in text files
and save results to JSON format.
"""

import json
from pathlib import Path


def how_many_times(path, search):
    """
    Search for a character/word in a text file.

    Args:
        path: Path to the text file
        search: String to search for (case-insensitive)

    Returns:
        List of dicts with 'line_number' and 'text' keys

    Raises:
        FileNotFoundError: If file doesn't exist
    """
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
    """
    Save search results to JSON file.

    Args:
        character: Character/word searched for
        book_title: Title of the book searched
        results: List of match dicts from how_many_times()

    Returns:
        bool: True if saved successfully, False if duplicate
    """
    file_path = Path(f"{character.lower()}.json")

    entry = {
        "book": book_title,
        "count": len(results),
        "matches": results
    }

    # Load existing data or create new
    if file_path.exists():
        data = json.loads(file_path.read_text())
    else:
        data = {
            "character": character,
            "searches": []
        }

    # Check for duplicates
    for search in data["searches"]:
        if search["book"] == book_title:
            return False

    # Add new entry
    data["searches"].append(entry)

    # Save
    file_path.write_text(
        json.dumps(data, indent=4, ensure_ascii=False),
        encoding="utf-8"
    )

    return True
