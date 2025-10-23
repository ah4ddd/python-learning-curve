def calculate_bill(product, price, quantity, discount=0):
    """
    Calculates total price for a product with optional discount.
    """
    total = price * quantity           # base total
    total_after_discount = total - (total * discount / 100)   # apply discount
    print(f"Product: {product}")
    print(f"Quantity: {quantity}")
    print(f"Price per item: ₹{price}")
    print(f"Discount: {discount}%")
    print(f"Total bill: ₹{total_after_discount}\n")

calculate_bill("Laptop", 50000, 1, 10)
calculate_bill("Smartphone", 20000, 2)
calculate_bill("Headphones", 1500, 3, 5)
calculate_bill("Monitor", 12000, 1, 15)
calculate_bill("Keyboard", 800, 4)
