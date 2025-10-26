def add_item(cart, item, price):
    cart.append({"item": item, "price": price})
    print(f"✅ Added {item} for ₹{price}")

def calculate_cart_total(cart):
    total = 0
    for item in cart:
        total += item["price"]
    return total

def apply_cart_discount(cart, discount_percent):
    for item in cart:
        original = item["price"]
        item["price"] = original * (1 - discount_percent/100)
    print(f"💰 {discount_percent}% discount applied!")

def show_cart(cart):
    print("\n🛒 Your Cart:")
    print("-" * 40)
    for item in cart:
        print(f"  {item['item']:<20} ₹{item['price']:.2f}")
    print("-" * 40)
    total = calculate_cart_total(cart)
    print(f"  Total: ₹{total:.2f}\n")

my_cart = []

add_item(my_cart, "Laptop", 50000)
add_item(my_cart, "Mouse", 500)
add_item(my_cart, "Keyboard", 1500)

show_cart(my_cart)

apply_cart_discount(my_cart, 10)

show_cart(my_cart)
