def show_menu():
    print("\n🍕 Pizza Menu:")
    print("1. Margherita - $18")
    print("2. Pepperoni - $10")
    print("3. Four Cheese - $12")
    print("4. Gourmet Pizza - $15")

    print("\n🍝 Pasta Menu:")
    print("5. Alfredo - $9")
    print("6. Bolognese - $11")
    print("7. Pesto - $13")
    print("8. Gourmet Pasta - $14")

    print("\n🍰 Dessert Menu:")
    print("9. Tiramisu - $6")
    print("10. Cannoli - $5")
    print("11. Gelato - $4")
    print("12. Ricotta Cheesecake - $7")

    print("\n🍷 Beverage Menu:")
    print("13. Red Wine - $16")
    print("14. White Wine - $8")
    print("15. Sparkling Water - $2")
    print("16. Italian Soda - 3$")

def get_price(choice):
    """Returns price based on user choice"""
    if choice == 1:
        return 18
    elif choice == 2:
        return 10
    elif choice == 3:
        return 12
    elif choice == 4:
        return 15
    elif choice == 5:
        return 9
    elif choice == 6:
        return 11
    elif choice == 7:
        return 13
    elif choice == 8:
        return 14
    elif choice == 9:
        return 6
    elif choice == 10:
        return 5
    elif choice == 11:
        return 4
    elif choice == 12:
        return 7
    elif choice == 13:
        return 16
    elif choice == 14:
        return 8
    elif choice == 15:
        return 2
    elif choice == 16:
        return 3
    else:
        return 0
