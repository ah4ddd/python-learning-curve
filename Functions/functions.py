def check_temperature(temp):
    if temp > 30:
        print("It's hot outside! 🥵")
    elif temp >= 20:
        print("Nice and warm ☀️")
    else:
        print("It's cold! 🥶")

check_temperature(3)

def grade_student(score):
    if score >= 90:
        return "A"
    elif score >= 75:
        return "B"
    elif score >= 50:
        return "C"
    else:
        return "F"

result = grade_student(35)
print(f"your result is {result} dogshit")

def can_vote(age, citizen):
    if age >= 18 and citizen == True:
        print("You can vote! 🗳️")
    elif age < 18:
        print("Too young to vote.")
    else:
        print("You’re not a citizen, sorry!")

can_vote(20,False)
