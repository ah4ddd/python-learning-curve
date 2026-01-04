import pytest
from shopping_cart import ShoppingCart

@pytest.fixture
def empty_cart():
    """Provide an empty shopping cart."""
    return ShoppingCart()

def test_new_cart_is_empty(empty_cart):
    """Test that a new cart starts empty."""
    assert empty_cart.is_empty() == True
    assert empty_cart.get_item_count() == 0

def test_add_single_item(empty_cart):
    """Test adding one item."""
    empty_cart.add_item("Apple", 1.50)
    assert empty_cart.get_item_count() == 1

def test_add_multiple_items(empty_cart):
    """Test adding multiple items."""
    empty_cart.add_item("Apple", 1.50)
    empty_cart.add_item("Banana", 0.75)
    assert empty_cart.get_item_count() == 2
