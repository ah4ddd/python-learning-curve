def calculate_stats(price, quantity):
    total = price * quantity
    tax = total * 0.18
    final = total + tax
    return total, tax, final  # ← Return THREE values!

total, tax, final = calculate_stats(100, 5)

print(f"Total: ₹{total}")
print(f"Tax: ₹{tax}")
print(f"Final: ₹{final}")
