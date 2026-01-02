from character_analyzer import how_many_times

def test_basic_search():
    """Test basic character search."""
    results = how_many_times("test_book.txt", "Raskolnikov")

    # Should find 3 matches
    assert len(results) == 3

    # Check first match
    assert results[0]["line_number"] == 1
    assert "Raskolnikov walked" in results[0]["text"]
