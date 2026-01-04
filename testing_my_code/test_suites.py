class ShoppingCart:
    """A simple shopping cart."""

    def __init__(self):
        """Initialize empty cart."""
        self.items = []

    def add_item(self, name, price, quantity=1):
        """
        Add an item to the cart.

        Args:
            name: Item name
            price: Item price
            quantity: How many items
        """
        if price < 0:
            raise ValueError("Price cannot be negative!")

        if quantity < 1:
            raise ValueError("Quantity must be at least 1!")

        item = {
            "name": name,
            "price": price,
            "quantity": quantity
        }
        self.items.append(item)

    def remove_item(self, name):
        """
        Remove an item from cart.

        Args:
            name: Item name to remove

        Returns:
            True if removed, False if not found
        """
        for item in self.items:
            if item["name"] == name:
                self.items.remove(item)
                return True
        return False

    def get_total(self):
        """Calculate total price of all items."""
        total = 0
        for item in self.items:
            total += item["price"] * item["quantity"]
        return total

    def get_item_count(self):
        """Get total number of items in cart."""
        count = 0
        for item in self.items:
            count += item["quantity"]
        return count

    def clear(self):
        """Remove all items from cart."""
        self.items = []

    def is_empty(self):
        """Check if cart is empty."""
        return len(self.items) == 0

cart = ShoppingCart()

cart.add_item("Notes from underground", 150, 2)

for item in cart.items:
    print(item)

