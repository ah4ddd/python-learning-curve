inventory = {
    "beef": {"price": 100, "stock": 50},
    "fish": {"price": 150, "stock": 100},
    "salad": {"price": 75, "stock": 30},
    "banana": {"price": 50, "stock": 70},
    "mango": {"price": 80, "stock": 30}
}

def show_inventory(inv):
    print("\nCurrent Inventory:")
    for item, info in inv.items():
        print(f"{item.title()}: ₹{info['price']} | Stock: {info['stock']}")
        print("-"*25)

def add_item(inv):
    item = input("Enter item name: ").lower()
    price = float(input("Enter price: "))
    stock = int(input("Enter stock quantity: "))
    inv[item] = {"price": price, "stock": stock}
    print(f"{item.title()} added successfully!")

def update_item(inv):
    item = input("Enter item to update: ").lower()
    if item in inv:
        inv[item]["price"] = float(input("Enter new price: "))
        inv[item]["stock"] = int(input("Enter new stock: "))
        print(f"{item.title()} updated successfully!")
    else:
        print("Item not found.")

def sell_item(inv):
    item = input("Enter item to sell: ").lower()
    quantity = int(input("Enter quantity: "))
    if item in inv:
        if inv[item]["stock"] >= quantity:
            inv[item]["stock"] -= quantity
            total_price = quantity * inv[item]["price"]
            print(f"Sold {quantity} {item}(s) for ₹{total_price}")
            print(f"Remaining {item}(s): {inv[item]['stock']}")
        else:
            print("Not enough stock.")
    else:
        print("Item not found.")

def coupon_discount(inv):
    VALID_COUPON = "ahad25"
    print("\n--- 25% Coupon Discount ---")
    have_coupon = input("Do you have a coupon? (Y/N): ").lower()
    if have_coupon != 'y':
        print("Discount cancelled.")
        return
    user_coupon = input("Enter coupon code: ").lower()
    if user_coupon == VALID_COUPON:
        item_name = input("Choose item for 25% discount: ").lower()
        if item_name in inv:
            original_price = inv[item_name]["price"]
            final_price = original_price * 0.75
            inv[item_name]["price"] = round(final_price, 2)
            print(f"✅ Success! Price of {item_name.title()} discounted by 25%.")
            print(f"   New Price: ₹{inv[item_name]['price']:.2f}")
        else:
            print(f"❌ Item '{item_name.title()}' not found in inventory.")
    else:
        print("❌ Invalid coupon code.")

def total_value(inv):
    total = 0
    for info in inv.values():
        total += info["price"] * info["stock"]
    print(f"\nTotal inventory value: ₹{total}")

def main():
    while True:
        print("\n===== SHOP INVENTORY SYSTEM ===== Discount Coupon : ahad25 =====")
        print("1. Show Inventory")
        print("2. Add Item")
        print("3. Update Item")
        print("4. Sell Item")
        print("5. Total Inventory Value")
        print("6. Apply Discount")
        print("7. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            show_inventory(inventory)
        elif choice == "2":
            add_item(inventory)
        elif choice == "3":
            update_item(inventory)
        elif choice == "4":
            sell_item(inventory)
        elif choice == "5":
            total_value(inventory)
        elif choice == "6":
            coupon_discount(inventory)
        elif choice == "7":
            print("Exiting...")
            break
        else:
            print("Invalid choice, try again.")
main()
