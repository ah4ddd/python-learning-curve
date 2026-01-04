import pytest
from shopping_cart import ShoppingCart

@pytest.fixture
def empty_cart():
    """Provide empty cart."""
    return ShoppingCart()

@pytest.fixture
def cart_with_items():
    """Provide cart with multiple items."""
    cart = ShoppingCart()
    cart.add_item("Apple", 1.50, quantity=2)
    cart.add_item("Banana", 0.75, quantity=3)
    cart.add_item("Orange", 2.00, quantity=1)
    return cart

@pytest.fixture(params=[
    ("Apple", 1.50, 1),
    ("Banana", 0.75, 5),
    ("Orange", 2.00, 3),
])
def item_data(request):
    """Provide different item data for parametrized tests."""
    return request.param
