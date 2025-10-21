# Step 1: Daily sales list
sales = [
    "soap", "cake", "soap", "shampoo", "cake",
    "soap", "bread", "cake", "bread", "shampoo"
]

# Step 2: List of unique products
products = list(set(sales))  # automatically removes duplicates

# Step 3: Count each product
print("Total sales per product:")
for product in products:
    total = sales.count(product)
    print(f"{product}: {total}")


###############*# Project 2 *###########################

#by using collections.Counter

from collections import Counter

sales = [
    "soap", "cake", "soap", "shampoo", "cake",
    "soap", "bread", "cake", "bread", "shampoo"
]

sales_counts = Counter(sales)

print("Total sales per product:")
for product, count in sales_counts.items():
    print(f"{product}: {count}")

