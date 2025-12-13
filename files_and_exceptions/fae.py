file_name = "txt/test.txt"

with open(file_name) as file_obj:
    for line in file_obj:
        print(line.rstrip())
