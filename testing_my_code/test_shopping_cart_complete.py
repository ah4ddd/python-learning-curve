import pytest # type: ignore
from shopping_cart import ShoppingCart

# ============================================================================
# BASIC FUNCTIONALITY TESTS
# ============================================================================

def test_new_cart_is_empty(empty_cart):
    """Test new cart starts empty."""
    assert empty_cart.is_empty() is True
    assert empty_cart.get_item_count() == 0
    assert empty_cart.get_total() == pytest.approx(0.0)

def test_add_item_parametrized(empty_cart, item_data):
    """Test adding various items."""
    name, price, quantity = item_data

    empty_cart.add_item(name, price, quantity)

    assert empty_cart.get_item_count() == quantity
    assert empty_cart.get_total() == pytest.approx(price * quantity)
    assert not empty_cart.is_empty()

# ============================================================================
# POPULATED CART TESTS
# ============================================================================

def test_cart_total(cart_with_items):
    """Test total calculation."""
    # 2*1.50 + 3*0.75 + 1*2.00 = 7.25
    expected = 7.25
    assert cart_with_items.get_total() == pytest.approx(expected)

def test_cart_item_count(cart_with_items):
    """Test item counting."""
    # 2 + 3 + 1 = 6 items
    assert cart_with_items.get_item_count() == 6

def test_remove_item_from_cart(cart_with_items):
    """Test removing item."""
    result = cart_with_items.remove_item("Apple")

    assert result is True
    assert cart_with_items.get_item_count() == 4  # 3 + 1 left
    assert cart_with_items.get_total() == pytest.approx(4.25)

# ============================================================================
# ERROR HANDLING TESTS
# ============================================================================

def test_negative_price_raises_error(empty_cart):
    """Test that negative price is rejected."""
    with pytest.raises(ValueError) as exc:
        empty_cart.add_item("Invalid", -10.00)

    assert "negative" in str(exc.value).lower(), \
        "Error message should mention negative price"

def test_zero_quantity_raises_error(empty_cart):
    """Test that zero quantity is rejected."""
    with pytest.raises(ValueError) as exc:
        empty_cart.add_item("Invalid", 1.00, quantity=0)

    assert "quantity" in str(exc.value).lower()
    assert "1" in str(exc.value)

# ============================================================================
# EDGE CASE TESTS
# ============================================================================

def test_remove_from_empty_cart(empty_cart):
    """Test removing from empty cart."""
    result = empty_cart.remove_item("Nonexistent")

    assert result is False
    assert empty_cart.is_empty()

def test_clear_populated_cart(cart_with_items):
    """Test clearing cart."""
    assert not cart_with_items.is_empty()  # Starts with items

    cart_with_items.clear()

    assert cart_with_items.is_empty()
    assert cart_with_items.get_item_count() == 0
    assert cart_with_items.get_total() == 0.0
