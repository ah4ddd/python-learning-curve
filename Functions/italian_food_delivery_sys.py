def greet_customer(name):
    print(f"Buongiorno, {name}! 👋 Welcome to La Bella Italia Food Order System.")

def show_menu():
    print("\n🍕 Pizza Menu:")
    print("1. Margherita - $8")
    print("2. Pepperoni - $10")
    print("3. Four Cheese - $12")

    print("\n🍝 Pasta Menu:")
    print("4. Alfredo - $9")
    print("5. Bolognese - $11")
    print("6. Pesto - $10")

def get_price(choice):
    if choice == 1:
        return 8
    elif choice == 2:
        return 10
    elif choice == 3:
        return 12
    elif choice == 4:
        return 9
    elif choice == 5:
        return 11
    elif choice == 6:
        return 10
    else:
        return 0

def apply_discount(price, discount_percent):
    return price * (1 - discount_percent / 100)

def apply_tax(price, tax_percent):
    return price * (1 + tax_percent / 100)

def calculate_final_bill(price, discount, tax):
    discounted = apply_discount(price, discount)
    final_price = apply_tax(discounted, tax)
    return final_price

def show_receipt(item_name, base_price, discount, tax, final_price):
    print("\n--- 🧾 YOUR RECEIPT ---")
    print(f"Item: {item_name}")
    print(f"Base Price: ${base_price:.2f}")
    print(f"Discount: {discount}%")
    print(f"Tax: {tax}%")
    print(f"Total Amount: ${final_price:.2f}")
    print("\nGrazie mille! 🍷 Enjoy your meal!")

def main():
    greet_customer("Liya")
    show_menu()

    choice = int(input("\nEnter your choice (1–6): "))
    price = get_price(choice)

    if price == 0:
        print("Invalid choice, caro mio 😅")
        return

    items = {
        1: "Margherita Pizza", 2: "Pepperoni Pizza", 3: "Four Cheese Pizza",
        4: "Alfredo Pasta", 5: "Bolognese Pasta", 6: "Pesto Pasta"
    }

    item_name = items[choice]

    discount = 10
    tax = 5

    final_price = calculate_final_bill(price, discount, tax)
    show_receipt(item_name, price, discount, tax, final_price)

main()
