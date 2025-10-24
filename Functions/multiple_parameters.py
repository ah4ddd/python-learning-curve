def calculate_restaurant_bill(food_cost, drinks_cost, num_people, tip_percent, tax_percent):

    subtotal = food_cost + drinks_cost

    tax_amount = subtotal * (tax_percent / 100)
    after_tax = subtotal + tax_amount

    tip_amount = after_tax * (tip_percent / 100)
    total = after_tax + tip_amount

    per_person = total / num_people

    print(f"💰 Restaurant Bill Breakdown")
    print("=" * 40)
    print(f"Food: ₹{food_cost}")
    print(f"Drinks: ₹{drinks_cost}")
    print(f"Subtotal: ₹{subtotal}")
    print(f"Tax ({tax_percent}%): ₹{tax_amount:.2f}")
    print(f"Tip ({tip_percent}%): ₹{tip_amount:.2f}")
    print(f"TOTAL: ₹{total:.2f}")
    print(f"Per person ({num_people} people): ₹{per_person:.2f}")

    return per_person

my_share = calculate_restaurant_bill(
    food_cost=2500,
    drinks_cost=800,
    num_people=4,
    tip_percent=15,
    tax_percent=18
)
