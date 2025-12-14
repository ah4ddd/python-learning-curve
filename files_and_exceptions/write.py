file = "programming.txt"

with open(file, "w") as f:
    f.write("I love programming\n")
    f.write("This is my freedom\n")


with open(file, "a") as file_object:
    file_object.write("I also love finding meaning in large datasets.\n")
    file_object.write("I love creating apps that can run in a browser.\n")

print("=== Guest Book ===")
print("Enter 'n' to stop\n")

while True:
    name = input("Enter your name: ").strip()
    if name.lower() == "n":
        break

    print(f"Welcome, {name}!")

    with open("guest.txt", "a") as g:
        g.write(f"{name}\n")

print()

print("\n=== Programming Poll ===")
print("Enter 'n' to stop\n")

while True:
    reason = input("Why do you like programming? ").strip()
    if reason.lower() == "n":
        break

    with open("programming_poll.txt", "a") as p:
        p.write(reason + "\n")

