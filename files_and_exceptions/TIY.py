paths = ['film.txt', 'tv.txt', 'dontknow.txt']

for path in paths:
    try:
        with open(path, "r") as f:
            content = f.read()
        print(f"\n--- {path} ---")
        print(content.strip())
    except FileNotFoundError:
        pass

while True:
    try:
        numb_one = int(input("first number: "))
        numb_two = int(input("second number: "))
    except ValueError:
        print("❌ Please enter numbers only.")
    else:
        print(numb_one + numb_two)
