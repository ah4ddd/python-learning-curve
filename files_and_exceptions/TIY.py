from pathlib import Path

paths = ['film.txt', 'tv.txt', 'dontknow.txt']

for path in paths:
    try:
        with open(path, "r") as f:
            content = f.read()
        print(f"\n--- {path} ---")
        print(content)
    except FileNotFoundError:
        print(f"❌ file {path} not found")

while True:
    try:
        numb_one = int(input("first number: "))
        numb_two = int(input("second number: "))
    except ValueError:
        print("❌ Please enter numbers only.")
    else:
        print(numb_one + numb_two)
