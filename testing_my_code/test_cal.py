from cal import add, subtract, multiply, divide

def test_add():
    """Test addition."""
    result = add(2, 3)
    assert result == 5

def test_subtract():
    """Test subtraction."""
    result = subtract(10, 4)
    assert result == 6

def test_multiply():
    """Test multiplication."""
    result = multiply(3, 4)
    assert result == 12

def test_divide():
    """Test division."""
    result = divide(10, 2)
    assert result == 5
