products = [
    ("Laptop", 60000, 5),
    ("Phone", 25000, 10),
    ("Headphones", 2000, 15),
    ("Keyboard", 1500, 7)
]

print("🛍️ Available Products:\n")
for name, price, qty in products:
    print(f"{name} - ₹{price} ({qty} left)")

new_product = ("Mouse", 800, 20)
products.append(new_product)

print("\n✨ Added New Product:\n")
for name, price, qty in products:
    print(f"{name} - ₹{price} ({qty} left)")

total_value = 0
for name, price, qty in products:
    total_value += price * qty

print(f"\n💸 Total Stock Value: ₹{total_value}")

for p in products:
    if p[0] == "Keyboard":
        products.remove(p)
        break

print("\n🗑️ Updated Product List (after removing Keyboard):")
for name, price, qty in products:
    print(f"{name} - ₹{price} ({qty} left)")

most_expensive = max(products, key=lambda item: item[1])
print(f"\n👑 Most Expensive Product: {most_expensive[0]} — ₹{most_expensive[1]}")
