from character_analyzer import how_many_times
import pytest

def test_file_not_found():
    """Test that FileNotFoundError is raised for missing files."""
    with pytest.raises(FileNotFoundError):
        how_many_times("nonexistent_book.txt", "Raskolnikov")

def test_basic_search():
    """Test basic character search."""
    results = how_many_times("test_book.txt", "Raskolnikov")

    # Should find 3 matches
    assert len(results) == 3

    # Check first match
    assert results[0]["line_number"] == 1
    assert "Raskolnikov walked" in results[0]["text"]

def test_case_insensitive():
    """Test that search is case-insensitive."""
    results = how_many_times("test_book.txt", "raskolnikov")

    # Should still find 3 matches (case doesn't matter!)
    assert len(results) == 3

    # Should find the UPPERCASE one too
    assert any("RASKOLNIKOV" in r["text"] for r in results)

def test_no_matches():
    """Test when character isn't in the book."""
    results = how_many_times("test_book.txt", "Sherlock Holmes")

    # Should return empty list
    assert len(results) == 0
    assert results == []

def test_partial_match():
    """Test that partial words are matched."""
    results = how_many_times("test_book.txt", "old")

    # Should find "old woman" (line 2)
    assert len(results) == 1
    assert results[0]["line_number"] == 2
    assert "old woman" in results[0]["text"]

def test_special_characters():
    """Test search with punctuation."""
    # Create temp file with punctuation
    with open("test_special.txt", "w") as f:
        f.write("Hello, world!\n")
        f.write("Hello world\n")

    results = how_many_times("test_special.txt", "Hello")

    # Should find both lines
    assert len(results) == 2

    # Cleanup
    import os
    os.remove("test_special.txt")


