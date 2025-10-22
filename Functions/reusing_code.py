def record_sale(product, quantity, sales_dict):
    if product in sales_dict:
        sales_dict[product] += quantity  # add to existing sales
    else:
        sales_dict[product] = quantity   # first sale
    print(f"Recorded {quantity} units of {product}")

sales = {}

record_sale("Soap", 5, sales)
record_sale("Cake", 3, sales)
record_sale("Bread", 7, sales)
record_sale("Soap", 2, sales)
record_sale("Cake", 4, sales)

print("\nTotal sales per product:")
for product, total in sales.items():
    print(f"{product}: {total} units")

def top_seller(sales_dict):
    top_product = max(sales_dict, key=sales_dict.get)
    print(f"Top-selling product: {top_product} ({sales_dict[top_product]} units)")

top_seller(sales)
