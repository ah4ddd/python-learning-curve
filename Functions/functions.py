def person_age(age):
    return 100 - age

until_100 = person_age(22)
print(f"You will turn 100 in the year: {until_100}")

if until_100 < 95:
    print("You still have time to live!")
else:
    print("Hurry up! Time is running out!")
