# Step 1: Get input for number of products and days
num_products = int(input("How many products? "))
num_days = int(input("How many days of sales? "))

# Step 2: Store product names and their daily sales
products = []
sales = []

for p in range(num_products):
    name = input(f"Enter name of product {p+1}: ")
    products.append(name)

    daily_sales = []
    for d in range(num_days):
        sale = int(input(f"Sales for {name} on day {d+1}: "))
        daily_sales.append(sale)

    sales.append(daily_sales)

# Step 3: Sum sales per product
print("\nTotal sales per product:")
for i in range(num_products):
    total = sum(sales[i])  # sums the list of daily sales
    print(f"{products[i]}: {total}")

# Step 4: Sum overall sales
overall_total = sum(sum(sales[i]) for i in range(num_products))
print(f"\nOverall total sales: {overall_total}")
