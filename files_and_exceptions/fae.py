with open("txt/test.txt") as file_obj:
    contents = file_obj.read()
print(contents.rstrip())
