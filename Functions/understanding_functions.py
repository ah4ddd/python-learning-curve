def greet_user(name):
    return f"Hello {name}! Welcome to Smart Shopping Helper."

def apply_discount(price, discount_percent):
    discounted_price = price * (1 - discount_percent / 100)
    return discounted_price

def apply_tax(price, tax_percent):
    return price * (1 + tax_percent / 100)

def print_receipt(item_name, price, discount, tax):
    final_price = apply_tax(apply_discount(price, discount), tax)
    return f"Item: {item_name}\nOriginal Price: ${price:.2f}\nDiscount: {discount}%\nTax: {tax}%\nFinal Price: ${final_price:.2f}"

# User input
user_name = "Lily"
print(greet_user(user_name))

item1 = print_receipt("Raspberry-pi", 1200, 10, 5)
item2 = print_receipt("Keyboard", 150, 15, 5)

print("\n--- Receipt ---")
print(item1)
print()
print(item2)

