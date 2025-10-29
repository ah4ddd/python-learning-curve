menu =[
    ("burger", 120),
    ("Pizza", 250),
    ("Pasta", 150),
    ("Fries", 100),
    ("Coke", 70)
]

print (" Welcome to python Cafe")
print("Here is our Menu:\n")

for item in menu:
    print(f"{item[0]} - {item[1]}")

order = input("\nWhat'd you like to order? ")

found = False
for item in menu:
    if order.lower() == item[0].lower():
        print(f"\nYou ordered {item[0]} — that will be ₹{item[1]}.")
        found = True
        break

if not found:
    print("\nSorry, we don’t have that on our menu today.")

