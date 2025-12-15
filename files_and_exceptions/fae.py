file_name = "txt/pi.txt"

with open(file_name) as pi_obj:
    pi_lines = pi_obj.readlines()

pi_string = ""
for line in pi_lines:
    pi_string += line.rstrip()

birthdays = {
    "Ahad": "121590",
    "Mia": "081595",
    "Sara": "031292"
}

with open("birthday_results.txt", "w") as f:
    f.write("🎂 BIRTHDAY IN PI CHECKER 🎂\n")
    f.write("="*40 + "\n\n")

    for name, bday in birthdays.items():
        if bday in pi_string:
            result = f"✅ {name}'s birthday ({bday}) IS in the first million digits!"
        else:
            result = f"❌ {name}'s birthday ({bday}) is NOT in the first million digits."

        f.write(result + "\n")
        print(result)

    f.write("\n" + "="*40 + "\n")
    f.write(f"Total digits of pi checked: {len(pi_string)}\n")

print("\n📄 Results saved to birthday_results.txt!")
