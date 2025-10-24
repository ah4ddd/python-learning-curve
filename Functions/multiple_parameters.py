def final_price(base_price,quantity,tax_rate,shipping_cost):
    tax_amount = base_price * tax_rate
    total_price = (base_price + tax_amount + shipping_cost) * quantity

    print(f"🧾 Final Price Calculation")
    print("=" * 40)
    print(f"Base Price: ${base_price:.2f}")
    print(f"Quantity: {quantity}")
    print(f"Tax Rate: {tax_rate*100:.2f}%")
    print(f"Shipping Cost: ${shipping_cost:.2f}")
    print("-" * 40)
    print(f"Total Price: ${total_price:.2f}")
    print("=" * 40)
    return total_price

order1 = final_price(20.0, 3, 0.07, 5.0)
order2 = final_price(15.5, 2, 0.05, 7.5)
order3 = final_price(50.0, 1, 0.08, 10.0)
