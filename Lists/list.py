products = []
sales = []

num_products = int(input("Enter number of products: "))

for i in range(num_products):
    product_name = input(f"Enter name of product {i+1}: ")
    products.append(product_name)

    days = int(input(f"How many days of sales for {product_name}? ")) #its just days not num_days
    daily_sales = [] #sublist for daily sales of current product

    for d in range(days):
        sale = int(input(f"Sales for {product_name} on day {d+1}: "))
        daily_sales.append(sale)

    sales.append(daily_sales)

print("\nProducts:", products)
print("Sales data:", sales)

print("\nTotal sales per product:")
for i in range(num_products):
    total = sum(sales[i])  # sum daily sales for product i
    print(f"{products[i]}: {total}")

overall_total = sum(sum(sales[i]) for i in range(num_products))
print(f"\nOverall total sales: {overall_total}")

combined = [[products[i], sum(sales[i])] for i in range(num_products)]

combined.sort(key=lambda x: x[1], reverse=True)

print("\nProducts sorted by total sales (high to low):")
for item in combined:
    print(f"{item[0]}: {item[1]}")

report = " | ".join(products)
print("\nProduct list report:")
print(report)

from collections import Counter

product_count = Counter(products)
print("\nProduct occurrences:")
for product, count in product_count.items():
    print(f"{product}: {count}")

top_seller = Counter({p: sum(sales[i]) for i, p in enumerate(products)}).most_common(1)[0]
least_seller = Counter({p: sum(sales[i]) for i, p in enumerate(products)}).most_common()[-1]

print(f"\nTop-selling product: {top_seller[0]} ({top_seller[1]} sold)")
print(f"Least-selling product: {least_seller[0]} ({least_seller[1]} sold)")

for i, product in enumerate(products):
    daily_report = ", ".join(str(s) for s in sales[i])
    print(f"{product} daily sales: {daily_report}")

