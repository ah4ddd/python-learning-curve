import pytest
from shopping_cart import ShoppingCart

def test_shopping_cart_comprehensive():
    """Comprehensive test using multiple assertion types."""
    cart = ShoppingCart()

    # Identity assertions
    assert cart.items is not None
    assert cart.is_empty() is True

    # Type assertions
    assert isinstance(cart.items, list)

    # Add item
    cart.add_item("Apple", 1.50, quantity=3)

    # Membership assertions
    assert len(cart.items) > 0
    assert "Apple" in [item["name"] for item in cart.items]

    # Comparison assertions
    assert cart.get_total() == pytest.approx(4.50)
    assert cart.get_item_count() >= 3

    # Exception assertion
    with pytest.raises(ValueError) as exc:
        cart.add_item("Banana", -0.75)
    assert "negative" in str(exc.value).lower()
