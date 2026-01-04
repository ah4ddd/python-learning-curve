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
