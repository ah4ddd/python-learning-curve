file = "programming.txt"

with open(file, "w") as f:
    f.write("I love programming\n")
    f.write("This is my freedom\n")


with open(file, 'a') as file_object:
    file_object.write("I also love finding meaning in large datasets.\n")
    file_object.write("I love creating apps that can run in a browser.\n")
