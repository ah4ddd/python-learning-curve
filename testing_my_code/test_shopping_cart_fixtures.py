import pytest # type: ignore
from shopping_cart import ShoppingCart

@pytest.fixture
def empty_cart():
    """Provide an empty shopping cart."""
    return ShoppingCart()

@pytest.fixture
def cart_with_items():
    """Provide a cart with some items already in it."""
    cart = ShoppingCart()
    cart.add_item("Apple", 1.50, quantity=2)
    cart.add_item("Banana", 0.75, quantity=3)
    return cart

def test_empty_cart_has_zero_total(empty_cart):
    """Test empty cart total."""
    assert empty_cart.get_total() == 0

def test_cart_with_items_has_correct_total(cart_with_items):
    """Test cart with items total."""
    # 2 apples at 1.50 + 3 bananas at 0.75
    assert cart_with_items.get_total() == 5.25

def test_remove_item_from_populated_cart(cart_with_items):
    """Test removing from a cart that has items."""
    cart_with_items.remove_item("Apple")
    assert cart_with_items.get_total() == 2.25  # Only bananas left
