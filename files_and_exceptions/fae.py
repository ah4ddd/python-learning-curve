try:
    x = int("abc")
except ValueError:
    print("That blew up.")

try:
    x = int("42")
except ValueError:
    print("Conversion failed")
else:
    print("Conversion worked")

try:
    x = 10 / 0
except ZeroDivisionError:
    print("Math betrayed you")
finally:
    print("This always runs")

try:
    x = 10 / 2
except ZeroDivisionError:
    print("Nope")
finally:
    print("Still runs")

try:
    file = open("data.json", "r")
    content = file.read()
except FileNotFoundError:
    print("File not found")
finally:
    file.close()

