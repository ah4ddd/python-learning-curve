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
