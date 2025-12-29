while True:
    try:
        numb_one = int(input("first number: "))
        numb_two = int(input("second number: "))
    except ValueError:
        print("❌ Please enter numbers only.")
    else:
        print(numb_one + numb_two)

