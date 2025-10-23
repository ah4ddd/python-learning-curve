def calculate_price(price, quantity, discount_percent):
    total_price = price * quantity
    discounted_price = total_price * (1 - discount_percent/100)
    return discounted_price

products = []
num_products = int(input("How many products are you buying? "))

for i in range(num_products):
    name = input(f"Enter name of product {i+1}: ")
    price = float(input(f"Enter price for {name}: "))
    quantity = int(input(f"Enter quantity for {name}: "))
    discount = float(input(f"Enter discount % for {name}: "))

    total = calculate_price(price, quantity, discount)
    products.append((name, total))

# Step 3: Show per-product totals
print("\nTotals per product:")
for name, total in products:
    print(f"{name}: ${total:.2f}")

overall_total = sum(total for _, total in products)
print(f"\nOverall total to pay: ${overall_total:.2f}")
