def show_menu_items(menu_items):
    """Display all menu items with numbers"""
    print("\n🍽️ MENU:")
    print("-" * 40)

    # Loop through items with index
    for i in range(len(menu_items)):
        item_name = menu_items[i][0]
        item_price = menu_items[i][1]
        print(f"  {i+1}. {item_name} - ₹{item_price}")

    print("-" * 40)

def calculate_order_total(order_items):
    """Add up all prices in order"""
    total = 0

    # Loop to add each price
    for item in order_items:
        price = item[1]  # Price is second element
        total = total + price

    return total

def print_receipt(order_items):
    """Show detailed receipt"""
    print("\n📄 YOUR RECEIPT:")
    print("=" * 40)

    # Loop to show each item
    for item in order_items:
        name = item[0]
        price = item[1]
        print(f"  {name:<25} ₹{price:>10}")

    print("-" * 40)

    # Calculate and show total
    total = calculate_order_total(order_items)
    print(f"  {'TOTAL':<25} ₹{total:>10}")
    print("=" * 40)

# Menu (list of lists: [name, price])
menu = [
    ["Margherita Pizza", 299],
    ["Pasta Carbonara", 249],
    ["Caesar Salad", 199],
    ["Garlic Bread", 99]
]

# Customer's order
customer_order = [
    ["Margherita Pizza", 299],
    ["Garlic Bread", 99],
    ["Pasta Carbonara", 249]
]

# Use the functions:
show_menu_items(menu)
print_receipt(customer_order)
