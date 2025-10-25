MENU = {
    "pizzas": {
        "Margherita": 299,
        "Pepperoni": 399,
        "Vegetarian": 349,
        "BBQ Chicken": 449,
        "Four Cheese": 499
    },
    "pastas": {
        "Spaghetti Carbonara": 249,
        "Penne Arrabiata": 229,
        "Fettuccine Alfredo": 279,
        "Lasagna": 319
    },
    "drinks": {
        "Coke": 49,
        "Sprite": 49,
        "Orange Juice": 79,
        "Water": 29
    },
    "desserts": {
        "Tiramisu": 149,
        "Panna Cotta": 129,
        "Gelato": 99
    }
}

DISCOUNT_CODES = {
    "FIRST10": 10,
    "WELCOME20": 20,
    "VIP30": 30
}

def display_menu():
    print("\n" + "="*50)
    print("🍕 BELLA CUCINA - MENU 🍝")
    print("="*50)

    for category, items in MENU.items():
        print(f"\n📋 {category.upper()}")
        print("-" * 40)
        for item, price in items.items():
            print(f"  {item:.<30} ₹{price}")

    print("="*50 + "\n")

def format_price(amount):
    return f"₹{amount:.2f}"

def get_item_price(item_name):
    for category, items in MENU.items():
        if item_name in items:
            return items[item_name]
    return None

def calculate_subtotal(order_items):
    total = 0
    for item, quantity in order_items:
        price = get_item_price(item)
        if price:
            total += price * quantity
    return total

def apply_discount(price, discount_code):
    if discount_code.upper() in DISCOUNT_CODES:
        discount_percent = DISCOUNT_CODES[discount_code.upper()]
        discount_amount = price * (discount_percent / 100)
        final_price = price - discount_amount
        return final_price, discount_percent, discount_amount
    else:
        return price, 0, 0

def calculate_tax(price, tax_rate=5):
    tax_amount = price * (tax_rate / 100)
    return tax_amount

def calculate_delivery_fee(distance_km):
    if distance_km <= 2:
        return 0
    elif distance_km <= 5:
        return 30
    elif distance_km <= 10:
        return 60
    else:
        return 100

def calculate_tip(total, tip_percent):
    return total * (tip_percent / 100)

def validate_discount_code(code):
    if code.upper() in DISCOUNT_CODES:
        return True, DISCOUNT_CODES[code.upper()]
    return False, 0

def print_order_summary(order_items):
    print("\n" + "="*50)
    print("📝 YOUR ORDER")
    print("="*50)

    for item, quantity in order_items:
        price = get_item_price(item)
        item_total = price * quantity
        print(f"  {quantity}x {item:.<25} {format_price(item_total)}")

    print("="*50)

def print_final_receipt(order_items, discount_code, distance_km, tip_percent):

    print("\n" + "="*50)
    print("🧾 BELLA CUCINA - RECEIPT")
    print("="*50)

    print("\nITEMS:")
    print("-" * 50)
    subtotal = 0
    for item, quantity in order_items:
        price = get_item_price(item)
        item_total = price * quantity
        subtotal += item_total
        print(f"  {quantity}x {item:.<30} {format_price(item_total)}")

    print("-" * 50)
    print(f"{'Subtotal':.>38} {format_price(subtotal)}")

    discounted_price, discount_percent, discount_amount = apply_discount(subtotal, discount_code)
    if discount_amount > 0:
        print(f"{'Discount (' + discount_code.upper() + ' -' + str(discount_percent) + '%)':.<38} -{format_price(discount_amount)}")
        print(f"{'After Discount':.>38} {format_price(discounted_price)}")

    # Tax
    tax_amount = calculate_tax(discounted_price)
    after_tax = discounted_price + tax_amount
    print(f"{'Tax (5%)':.>38} +{format_price(tax_amount)}")

    delivery_fee = calculate_delivery_fee(distance_km)
    if delivery_fee == 0:
        print(f"{'Delivery (Free!)':.>38} {format_price(0)}")
    else:
        print(f"{'Delivery (' + str(distance_km) + 'km)':.>38} +{format_price(delivery_fee)}")

    after_delivery = after_tax + delivery_fee

    tip_amount = calculate_tip(after_delivery, tip_percent)
    if tip_amount > 0:
        print(f"{'Tip (' + str(tip_percent) + '%)':.>38} +{format_price(tip_amount)}")

    grand_total = after_delivery + tip_amount
    print("=" * 50)
    print(f"{'TOTAL TO PAY':.>38} {format_price(grand_total)}")
    print("=" * 50)

    print("\n🙏 Thank you for ordering from Bella Cucina!")
    print("🚚 Your food will arrive in 30-45 minutes!")
    print("\n")

    return grand_total

def main():

    print("\n🍕 Welcome to BELLA CUCINA! 🍝")
    print("Your favorite Italian food delivery!")

    display_menu()

    customer_order = [
        ("Pepperoni", 2),
        ("Spaghetti Carbonara", 1),
        ("Coke", 3),
        ("Tiramisu", 2)
    ]

    # Order details
    discount_code = "WELCOME20"
    delivery_distance = 4
    tip_percentage = 10

    # Show order summary
    print_order_summary(customer_order)

    total = print_final_receipt(
        customer_order,
        discount_code,
        delivery_distance,
        tip_percentage
    )

    print(f"💳 Please pay {format_price(total)}")

main()
