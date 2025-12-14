file = "programming.txt"

with open(file, "w") as f:
    f.write("I love programming\n")
    f.write("This is my freedom\n")


with open(file, "a") as file_object:
    file_object.write("I also love finding meaning in large datasets.\n")
    file_object.write("I love creating apps that can run in a browser.\n")

print("=== Guest Log ===")
print("Enter 'N' when you are done with your lil list\n")

while True :
    name = input("Put your name:").lower()
    more = input("you wanna put more name ? y/n:")
    with open("guest.txt", "a") as g:
        g.write(f"{name.title()}\n")
    if more == "n":
        break

print()

print("=== Programming Poll ===")
print("Enter 'n' when you are done with your lil torcher session\n")

while True :
    why = input("Why you even like programming ( i mean not touching grass)?").lower()
    more_why = input("you wanna put more reason or touch grass.. ? y/n:")
    with open("guest.txt", "a") as p:
        p.write(f"Why likes Programming: {why.title()}\n")
    if more_why == "n":
        break
