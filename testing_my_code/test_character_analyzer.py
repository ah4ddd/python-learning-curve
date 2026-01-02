"""
Tests for character_analyzer.py

This test suite ensures the character search functionality works correctly
for various edge cases and error conditions.
"""

import pytest
import os
from pathlib import Path
from character_analyzer import how_many_times

# Test data setup
TEST_BOOK_CONTENT = """Raskolnikov walked down the street.
The old woman opened the door.
Raskolnikov hesitated for a moment.
He thought about his plan.
RASKOLNIKOV entered the room."""

@pytest.fixture
def test_book_file():
    """Create a temporary test book file."""
    filepath = "test_book_temp.txt"
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(TEST_BOOK_CONTENT)

    yield filepath  # This is what the test gets

    # Cleanup (runs after test)
    if os.path.exists(filepath):
        os.remove(filepath)

# ============================================================================
# BASIC FUNCTIONALITY TESTS
# ============================================================================

def test_basic_search(test_book_file):
    """Test basic character search returns correct matches."""
    results = how_many_times(test_book_file, "Raskolnikov")

    assert len(results) == 3
    assert results[0]["line_number"] == 1
    assert "Raskolnikov walked" in results[0]["text"]

def test_case_insensitive_search(test_book_file):
    """Test that search ignores case."""
    results_lower = how_many_times(test_book_file, "raskolnikov")
    results_upper = how_many_times(test_book_file, "RASKOLNIKOV")
    results_mixed = how_many_times(test_book_file, "RaSkoLniKov")

    # All should find the same 3 matches
    assert len(results_lower) == 3
    assert len(results_upper) == 3
    assert len(results_mixed) == 3

def test_partial_word_matching(test_book_file):
    """Test that partial words are matched."""
    results = how_many_times(test_book_file, "old")

    assert len(results) == 1
    assert results[0]["line_number"] == 2
    assert "old woman" in results[0]["text"]

# ============================================================================
# EDGE CASE TESTS
# ============================================================================

def test_no_matches(test_book_file):
    """Test when search term isn't found."""
    results = how_many_times(test_book_file, "Sherlock Holmes")

    assert len(results) == 0
    assert results == []

def test_empty_search_term(test_book_file):
    """Test with empty string (should match all lines)."""
    results = how_many_times(test_book_file, "")

    # Empty string is in every line
    assert len(results) == 5

def test_search_punctuation(test_book_file):
    """Test search terms with punctuation."""
    results = how_many_times(test_book_file, "street.")

    assert len(results) == 1
    assert "street" in results[0]["text"]

def test_line_numbers_are_correct(test_book_file):
    """Test that line numbers are accurate."""
    results = how_many_times(test_book_file, "Raskolnikov")

    # Should find on lines 1, 3, and 5
    line_numbers = [r["line_number"] for r in results]
    assert line_numbers == [1, 3, 5]

def test_whitespace_is_stripped(test_book_file):
    """Test that leading/trailing whitespace is removed."""
    results = how_many_times(test_book_file, "Raskolnikov")

    for result in results:
        # No leading/trailing whitespace
        assert result["text"] == result["text"].strip()

# ============================================================================
# ERROR HANDLING TESTS
# ============================================================================

def test_file_not_found_raises_error():
    """Test that missing file raises FileNotFoundError."""
    with pytest.raises(FileNotFoundError):
        how_many_times("nonexistent_book.txt", "character")

def test_empty_file_returns_empty_list():
    """Test that empty file returns no matches."""
    # Create empty file
    empty_file = "test_empty.txt"
    Path(empty_file).touch()

    try:
        results = how_many_times(empty_file, "anything")
        assert results == []
    finally:
        os.remove(empty_file)

# ============================================================================
# UNICODE AND ENCODING TESTS
# ============================================================================

def test_unicode_characters():
    """Test that unicode characters are handled correctly."""
    unicode_file = "test_unicode.txt"
    unicode_content = "Dostoevsky wrote Crime and Punishment.\nФёдор Михайлович Достоевский"

    with open(unicode_file, "w", encoding="utf-8") as f:
        f.write(unicode_content)

    try:
        results = how_many_times(unicode_file, "Достоевский")
        assert len(results) == 1
        assert "Достоевский" in results[0]["text"]
    finally:
        os.remove(unicode_file)

# ============================================================================
# PERFORMANCE TESTS (Optional but good!)
# ============================================================================

def test_large_file_performance():
    """Test that function handles large files reasonably fast."""
    import time

    # Create a large test file (1000 lines)
    large_file = "test_large.txt"
    with open(large_file, "w") as f:
        for i in range(1000):
            f.write(f"Line {i}: Raskolnikov walked around.\n")

    try:
        start = time.time()
        results = how_many_times(large_file, "Raskolnikov")
        duration = time.time() - start

        # Should find 1000 matches
        assert len(results) == 1000

        # Should complete in under 1 second
        assert duration < 1.0, f"Search took {duration}s, should be < 1s"
    finally:
        os.remove(large_file)
