sales = [
    "soap", "cake", "soap", "shampoo", "cake",
    "soap", "shampoo", "cake", "shampoo", "soap"
]

unique_products = list(set(sales))
manual_count = {}
for product in unique_products:
    manual_count[product] = sales.count(product)

print("Manual count of products:")
for product, count in manual_count.items():
    print(f"{product}: {count}")

print("\n---\n")

from collections import Counter

counter_count = Counter(sales)
print("Counter result:")
for product, count in counter_count.items():
    print(f"{product}: {count}")

print("\n---\n")

top_seller = counter_count.most_common(1)[0]
least_seller = counter_count.most_common()[-1]

print(f"Top-selling product: {top_seller[0]} ({top_seller[1]} sold)")
print(f"Least-selling product: {least_seller[0]} ({least_seller[1]} sold)")
