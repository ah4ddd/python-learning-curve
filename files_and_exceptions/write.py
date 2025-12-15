file = "programming.txt"

with open(file, "w") as f:
    f.write("I love programming\n")
    f.write("This is my freedom\n")


with open(file, "a") as file_object:
    file_object.write("I also love finding meaning in large datasets.\n")
    file_object.write("I love creating apps that can run in a browser.\n")

print("=== Guest Book & Programming Poll ===")
print("Type 'n' anytime to quit.\n")

with open("guest.txt", "w") as f:
        f.write("Name | Reason to code\n")

while True:
    name = input("Your name: ").strip()
    if name.lower() == "n":
        break

    reason = input("Why do you like programming? ").strip()
    if reason.lower() == "n":
        break

    with open("guest.txt", "a") as f:
        f.write(f"{name} | {reason}\n")

    print(f"Logged: {name}\n")

with open("guest.txt", "r") as f:
    print("\n=== Guest & Whys ===")
    print(f.read())


print("\n=== Session Ended ===")


