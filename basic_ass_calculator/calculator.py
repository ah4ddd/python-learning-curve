# 1. Welcome the user
print("Welcome to the calculator, baby!")
print("You can do +, -, *, /")

# 2. Start an infinite loop so we can calculate forever
while True:
    # 3. Get the operation from the user
    operation = input("Enter operation (+, -, *, /) or 'q' to quit: ")

    # 4. Check if the player wants to quit
    if operation.lower() == 'q':
        print("Exiting. Your calculator dreams are over. Bye!")
        break  # stops the loop

    # 5. Get the numbers from the player
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    # 6. Perform the operation
    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == '/':
        if num2 == 0:
            print("You can’t divide by zero, genius!")
            continue  # skip rest and go to next loop
        result = num1 / num2
    else:
        print("Invalid operation, moron! Try again.")
        continue  # skip rest and go to next loop

    # 7. Show the result
    print(f"The result is: {result}")
