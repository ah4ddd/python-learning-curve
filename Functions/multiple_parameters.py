def calculate_item_price(base_price, tax, discount):
    final_price = base_price * (1 + tax/100) - discount
    return final_price

def calculate_total_order(*items):
    total = sum(items)
    return total

def suggest_tip(total, tip_percent=10):
    tip_amount = total * tip_percent / 100
    return tip_amount

latte = calculate_item_price(120, 5, 10)
espresso = calculate_item_price(80, 5, 5)
cappuccino = calculate_item_price(150, 5, 15)

total_bill = calculate_total_order(latte, espresso, cappuccino)

tip = suggest_tip(total_bill, tip_percent=12)

print(f"Latte: ₹{latte:.2f}, Espresso: ₹{espresso:.2f}, Cappuccino: ₹{cappuccino:.2f}")
print(f"Total Bill: ₹{total_bill:.2f}")
print(f"Suggested Tip (12%): ₹{tip:.2f}")
