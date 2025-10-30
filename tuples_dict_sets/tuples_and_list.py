products = [
    ("Laptop", 60000, 5),
    ("Phone", 25000, 10),
    ("Headphones", 2000, 15),
    ("Keyboard", 1500, 7)
]

def show_products():
    print("\nAvailable producsts:")
    for name, price, qty in products:
        print(f"* {name} - ${price} {qty} in stocks")

def add_product(name,price,qty):
    new_product = (name,price,qty)
    products.append(new_product)
    print(f"\n Added: {name} - ${price}, ({qty} units)")

def remove_product(name):
    for product in products:
        if product[0].lower() == name.lower():
            products.remove(product)
            print(f"\nRemoved product: {name}")
            return
    print(f"\nProduct '{name} not found")

def search_product(keyword):
    found = False
    for name, price, qty in products:
        if keyword.lower() in name.lower():
            print(f"* {name} - ${price} ({qty} in stocks)")
            found = True
    if not found:
        print("No products matched your search")

def total_value():
    total = sum(price * qty for _, price, qty in products)
    print(f"\nTotal Store Value: ${total}")

def main():
    while True:
        print("\n" + "="*40)
        print("🏪 SMART STORE SYSTEM")
        print("="*40)
        print("1️⃣ View Products")
        print("2️⃣ Add Product")
        print("3️⃣ Remove Product")
        print("4️⃣ Search Product")
        print("5️⃣ Check Total Value")
        print("6️⃣ Exit")

        choice = input("\n👉 Enter your choice: ")

        if choice == "1":
            show_products()

        elif choice == "2":
            name = input("Product Name: ")
            price = int(input("Price: ₹"))
            qty = int(input("Quantity: "))
            add_product(name, price, qty)

        elif choice == "3":
            name = input("Enter product name to remove: ")
            remove_product(name)

        elif choice == "4":
            keyword = input("Enter search keyword: ")
            search_product(keyword)

        elif choice == "5":
            total_value()

        elif choice == "6":
            print("\n👋 Exiting... Goodbye!")
            break
        else:
            print("\n⚠️ Invalid choice. Try again!")

main()
