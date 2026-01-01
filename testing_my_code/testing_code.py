def test_basic_math():
    """Test that basic math works."""
    assert 2 + 2 == 4
    assert 10 - 5 == 5
    assert 3 * 3 == 9

def test_strings():
    """Test string operations."""
    name = "Ahad"
    assert name.upper() == "AHAD"
    assert len(name) == 4
    assert "h" in name.lower()

def test_lists():
    """Test list operations."""
    numbers = [1, 2, 3, 4, 5]
    assert len(numbers) == 5
    assert 3 in numbers
    assert numbers[0] == 1

