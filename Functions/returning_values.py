def calculate_bill(product, price, quantity, discount=0):
    total = price * quantity
    total_after_discount = total - (total * discount / 100)

    print(f"Product: {product}")
    print(f"Quantity: {quantity}")
    print(f"Price per item: ₹{price}")
    print(f"Discount: {discount}%")
    print(f"Total: ₹{total_after_discount}\n")

    return total_after_discount

bill1 = calculate_bill("Laptop", 50000, 1, 10)
bill2 = calculate_bill("Smartphone", 20000, 2)
bill3 = calculate_bill("Headphones", 1500, 3, 5)

grand_total = bill1 + bill2 + bill3
print(f"💰 GRAND TOTAL: ₹{grand_total}")

if grand_total > 50000:
    print("🎉 You get FREE SHIPPING!")
else:
    print(f"₹{50000 - grand_total} more for free shipping!")

