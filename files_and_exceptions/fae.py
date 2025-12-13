file_name = "txt/test.txt"

pi = "txt/pi.txt"

with open(file_name) as file_obj:
    lines = file_obj.readlines()

with open(pi) as pi_obj:
    pi_lines = pi_obj.readlines()

pi_string = ""
for line in pi_lines:
    pi_string += line.rstrip()

print(f"{pi_string[:52]}")
print(len(pi_string))

bday = input("Enter Bday in mmddyy: ")

if bday in pi_string:
    print("oh your bday is in first million digit of pi, not impressesed")
else:
    print("haha, no nicht nada nothing, pi bye")
