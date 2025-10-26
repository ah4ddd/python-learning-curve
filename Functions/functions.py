def show_shopping_list(items):
    print("🛒 Shopping List:")
    print("-" * 30)
    for item in items:
        print(f"  • {item}")
    print("-" * 30)

my_list = ["Milk", "Bread", "Eggs", "Butter"]
show_shopping_list(my_list)

def calculate_total_cost(prices):
    total = 0
    for price in prices:
        total = total + price
    return total

cart_prices = [100, 250, 75, 300]
total = calculate_total_cost(cart_prices)
print(f"Total: ₹{total}")

def is_movie_in_watchlist(watchlist, movie_title):
    for movie in watchlist:
        if movie == movie_title:
            return True  # Found it! Stop immediately!
    return False  # Checked all, didn't find it

my_watchlist = ["Stalker", "Persona", "8½", "Eraserhead"]

if is_movie_in_watchlist(my_watchlist, "Persona"):
    print("Already in your watchlist!")
else:
    print("Not in watchlist, adding it!")

def count_expensive_items(prices, threshold):
    count = 0
    for price in prices:
        if price > threshold:
            count += 1
    return count

# Use it:
item_prices = [100, 250, 75, 500, 150, 600]
expensive = count_expensive_items(item_prices, 200)

print(f"Items over ₹200: {expensive}")  # 3 items

def get_valid_age():
    while True:
        age = int(input("Enter your age: "))
        if age >= 0 and age <= 120:
            return age  # Valid! Return and exit loop
        else:
            print("Invalid age! Try again.")

# Use it:
user_age = get_valid_age()
print(f"Thanks! Your age is {user_age}")
