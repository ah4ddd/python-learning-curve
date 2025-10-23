def calculate_bill(product, price, quantity, discount=0):
    total = price * quantity           # base total
    total_after_discount = total - (total * discount / 100)   # apply discount
    print(f"Product: {product}")
    print(f"Quantity: {quantity}")
    print(f"Price per item: ₹{price}")
    print(f"Discount: {discount}%")
    print(f"Total bill: ₹{total_after_discount}\n")
    return total_after_discount

calculate_bill("Laptop", 50000, 1, 10)
calculate_bill("Smartphone", 20000, 2)
calculate_bill("Headphones", 1500, 3, 5)
calculate_bill("Monitor", 12000, 1, 15)
calculate_bill("Keyboard", 800, 4)
