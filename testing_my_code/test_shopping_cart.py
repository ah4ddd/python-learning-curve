from shopping_cart import ShoppingCart

def test_new_cart_is_empty():
    """Test that a new cart starts empty."""
    cart = ShoppingCart()

    assert cart.is_empty() == True
    assert cart.get_item_count() == 0
    assert cart.get_total() == 0

def test_add_single_item():
    """Test adding one item to cart."""
    cart = ShoppingCart()

    cart.add_item("Apple", 1.50)

    assert cart.is_empty() == False
    assert cart.get_item_count() == 1
    assert cart.get_total() == 1.50

def test_add_multiple_items():
    """Test adding multiple different items."""
    cart = ShoppingCart()

    cart.add_item("Apple", 1.50)
    cart.add_item("Banana", 0.75)
    cart.add_item("Orange", 2.00)

    assert cart.get_item_count() == 3
    assert cart.get_total() == 4.25

def test_add_item_with_quantity():
    """Test adding multiple of the same item."""
    cart = ShoppingCart()

    cart.add_item("Apple", 1.50, quantity=5)

    assert cart.get_item_count() == 5
    assert cart.get_total() == 7.50  # 1.50 * 5

def test_add_same_item_twice():
    """Test adding the same item in separate calls."""
    cart = ShoppingCart()

    cart.add_item("Apple", 1.50, quantity=2)
    cart.add_item("Apple", 1.50, quantity=3)

    # Two separate entries, not combined
    assert cart.get_item_count() == 5
    assert cart.get_total() == 7.50

def test_remove_existing_item():
    """Test removing an item that exists."""
    cart = ShoppingCart()

    cart.add_item("Apple", 1.50)
    cart.add_item("Banana", 0.75)

    result = cart.remove_item("Apple")

    assert result == True
    assert cart.get_item_count() == 1
    assert cart.get_total() == 0.75

def test_remove_nonexistent_item():
    """Test removing an item that doesn't exist."""
    cart = ShoppingCart()

    cart.add_item("Apple", 1.50)

    result = cart.remove_item("Banana")

    assert result == False
    assert cart.get_item_count() == 1  # Nothing removed

def test_remove_from_empty_cart():
    """Test removing from an empty cart."""
    cart = ShoppingCart()

    result = cart.remove_item("Apple")

    assert result == False
    assert cart.is_empty() == True

def test_clear_cart():
    """Test clearing all items from cart."""
    cart = ShoppingCart()

    cart.add_item("Apple", 1.50)
    cart.add_item("Banana", 0.75)
    cart.add_item("Orange", 2.00)

    cart.clear()

    assert cart.is_empty() == True
    assert cart.get_item_count() == 0
    assert cart.get_total() == 0

import pytest # type: ignore

def test_add_item_with_negative_price():
    """Test that negative prices are rejected."""
    cart = ShoppingCart()

    with pytest.raises(ValueError) as exc_info:
        cart.add_item("Apple", -1.50)

    assert "Price cannot be negative" in str(exc_info.value)

def test_add_item_with_zero_quantity():
    """Test that zero quantity is rejected."""
    cart = ShoppingCart()

    with pytest.raises(ValueError) as exc_info:
        cart.add_item("Apple", 1.50, quantity=0)

    assert "Quantity must be at least 1" in str(exc_info.value)

def test_add_item_with_negative_quantity():
    """Test that negative quantity is rejected."""
    cart = ShoppingCart()

    with pytest.raises(ValueError):
        cart.add_item("Apple", 1.50, quantity=-5)

