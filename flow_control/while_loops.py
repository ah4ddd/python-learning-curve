counter = 1

while counter <= 5:
    print(f"Counter is at {counter}")
    counter += 1

password = ""

while password != "python123":
    password = input("Enter the password: ")
    if password != "python123":
        print("Wrong! Try again...")

print("Access granted!")

while True:
    print("This will never stop!")
