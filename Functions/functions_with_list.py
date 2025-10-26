def affordable(items,tax):

    prices =[]
    for item in items:
        if item <= 500:
            prices.append(item)

    taxes =[]
    for price in prices:
        final_price = price *  (1 + tax/100)
        taxes.append(final_price)

    return taxes

cart = [450, 600, 700, 300, 200, 550]
processed = affordable(cart,18)

print(f"orignal: {cart}")
print(f"Processed: {processed}")
