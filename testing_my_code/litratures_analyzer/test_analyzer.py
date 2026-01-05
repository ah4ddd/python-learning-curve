"""
Tests for analyzer.py

Tests cover:
- Character search functionality
- Case-insensitive matching
- Line number accuracy
- JSON saving with duplicate prevention
"""

import pytest # type: ignore
import json
import os
from pathlib import Path
from analyzer import how_many_times, save_results


# ============================================================================
# BASIC SEARCH TESTS
# ============================================================================

def test_search_finds_matches():
    """Test that search finds character mentions."""
    results = how_many_times("books/test_book.txt", "Raskolnikov")

    # Should find 3 matches
    assert len(results) == 3

    # Each result should have required keys
    for result in results:
        assert "line_number" in result
        assert "text" in result


def test_search_is_case_insensitive():
    """Test that search ignores case."""
    results_lower = how_many_times("books/test_book.txt", "raskolnikov")
    results_upper = how_many_times("books/test_book.txt", "RASKOLNIKOV")
    results_mixed = how_many_times("books/test_book.txt", "RaSkoLniKov")

    # All should find the same 3 matches
    assert len(results_lower) == 3
    assert len(results_upper) == 3
    assert len(results_mixed) == 3


def test_search_returns_correct_line_numbers():
    """Test that line numbers are accurate."""
    results = how_many_times("books/test_book.txt", "Raskolnikov")

    # Extract line numbers
    line_numbers = [r["line_number"] for r in results]

    # Should be on lines 1, 3, and 5
    assert line_numbers == [1, 3, 5]


def test_search_returns_correct_text():
    """Test that returned text matches file content."""
    results = how_many_times("books/test_book.txt", "Raskolnikov")

    # Check first match
    assert "walked down the street" in results[0]["text"]

    # Check that text is stripped (no leading/trailing whitespace)
    for result in results:
        assert result["text"] == result["text"].strip()

# ============================================================================
# EDGE CASE TESTS
# ============================================================================

def test_search_with_no_matches():
    """Test when character isn't found."""
    results = how_many_times("books/test_book.txt", "Sherlock Holmes")

    assert len(results) == 0
    assert results == []


def test_search_with_partial_word():
    """Test that partial words are matched."""
    results = how_many_times("books/test_book.txt", "woman")

    # Should find lines 2 and 6
    assert len(results) == 2

    line_numbers = [r["line_number"] for r in results]
    assert 2 in line_numbers
    assert 6 in line_numbers


def test_search_with_empty_string():
    """Test with empty search term."""
    results = how_many_times("books/test_book.txt", "")

    # Empty string is in every line
    assert len(results) == 6


def test_search_nonexistent_file():
    """Test that missing file raises error."""
    with pytest.raises(FileNotFoundError):
        how_many_times("books/nonexistent.txt", "character")

# ============================================================================
# JSON SAVING TESTS
# ============================================================================

@pytest.fixture
def sample_results():
    """Provide sample search results."""
    return [
        {"line_number": 1, "text": "Raskolnikov walked down the street."},
        {"line_number": 3, "text": "Raskolnikov hesitated for a moment."},
    ]


@pytest.fixture
def cleanup_json():
    """Cleanup test JSON files after each test."""
    yield
    # Teardown: remove test JSON files
    test_files = ["testcharacter.json", "raskolnikov.json"]
    for file in test_files:
        if os.path.exists(file):
            os.remove(file)


def test_save_creates_json_file(sample_results, cleanup_json):
    """Test that save creates JSON file."""
    result = save_results("TestCharacter", "Test Book", sample_results)

    assert result is True
    assert Path("testcharacter.json").exists()


def test_save_creates_correct_structure(sample_results, cleanup_json):
    """Test that JSON structure is correct."""
    save_results("Raskolnikov", "Crime and Punishment", sample_results)

    # Load and check structure
    with open("raskolnikov.json", "r") as f:
        data = json.load(f)

    # Check top-level keys
    assert "character" in data
    assert "searches" in data

    # Check character name
    assert data["character"] == "Raskolnikov"

    # Check searches list
    assert len(data["searches"]) == 1

    # Check search entry
    search = data["searches"][0]
    assert search["book"] == "Crime and Punishment"
    assert search["count"] == 2
    assert len(search["matches"]) == 2


def test_save_prevents_duplicates(sample_results, cleanup_json):
    """Test that duplicate searches are prevented."""
    # Save once
    result1 = save_results("Raskolnikov", "Crime and Punishment", sample_results)
    assert result1 is True

    # Try to save again (same book!)
    result2 = save_results("Raskolnikov", "Crime and Punishment", sample_results)
    assert result2 is False

    # Check only ONE entry exists
    with open("raskolnikov.json", "r") as f:
        data = json.load(f)

    assert len(data["searches"]) == 1


def test_save_allows_different_books(sample_results, cleanup_json):
    """Test that different books can be saved."""
    # Save for first book
    result1 = save_results("Raskolnikov", "Crime and Punishment", sample_results)
    assert result1 is True

    # Save for different book
    result2 = save_results("Raskolnikov", "The Idiot", sample_results)
    assert result2 is True

    # Check TWO entries exist
    with open("raskolnikov.json", "r") as f:
        data = json.load(f)

    assert len(data["searches"]) == 2

    # Check both books are there
    books = [search["book"] for search in data["searches"]]
    assert "Crime and Punishment" in books
    assert "The Idiot" in books


