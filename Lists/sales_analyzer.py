from collections import Counter

print("📊 Welcome to Smart Sales Analyzer")
print("----------------------------------")

products = []
sales = []

num_products = int(input("Enter how many products you sold today: "))

for i in range(num_products):
    product_name = input(f"\nEnter product name {i+1}: ")
    products.append(product_name)

    days = int(input(f"How many days of sales data for {product_name}? "))

    daily_sales = []
    for d in range(days):
        sale = int(input(f"  Sales for day {d+1}: "))
        daily_sales.append(sale)

    sales.append(daily_sales)

print("\n✅ Data successfully collected!\n")

print("📦 Total Sales per Product:")
for i, product in enumerate(products):
    total = sum(sales[i])
    print(f"{product}: {total} units")

overall_total = sum(sum(sales[i]) for i in range(num_products))
print(f"\n💰 Overall total sales: {overall_total} units")

combined = [[products[i], sum(sales[i])] for i in range(num_products)]
combined.sort(key=lambda x: x[1], reverse=True)

print("\n🏆 Products sorted by sales:")
for name, total in combined:
    print(f"{name}: {total}")

report_line = " | ".join(products)
print("\n🗒️ Product report line:")
print(report_line)

product_counts = Counter(products)
print("\n🔢 Product name occurrences:")
for name, count in product_counts.items():
    print(f"{name}: {count} times")

counter_count = Counter({products[i]: sum(sales[i]) for i in range(num_products)})

top_seller = counter_count.most_common(1)[0]
least_seller = counter_count.most_common()[-1]

print(f"\n🔥 Top-selling product: {top_seller[0]} ({top_seller[1]} sold)")
print(f"🥶 Least-selling product: {least_seller[0]} ({least_seller[1]} sold)")

print("\n📅 Daily Sales Breakdown:")
for i, product in enumerate(products):
    daily_str = ", ".join(str(x) for x in sales[i])
    print(f"{product}: {daily_str}")
