def calculate_bill(product, price, quantity, discount=0):
    total = price * quantity
    total_after_discount = total - (total * discount / 100)

    print(f"Product: {product}")
    print(f"Quantity: {quantity}")
    print(f"Price per item: ₹{price}")
    print(f"Discount: {discount}%")
    print(f"Total bill: ₹{total_after_discount}\n")

    return total_after_discount

laptop_bill = calculate_bill("Laptop", 50000, 1, 10)
phone_bill = calculate_bill("Smartphone", 20000, 2)

grand_total = laptop_bill + phone_bill
print(f"🛒 Grand Total: ₹{grand_total}")
