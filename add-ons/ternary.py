def age_category(age):
    return "Adult" if age >= 18 else "Minor"

def temperature_status(temp):
    return "Hot" if temp > 25 else "Cold"

def score_result(score):
    return "Pass" if score >= 50 else "Fail"

def even_or_odd(num):
    return "Even" if num % 2 == 0 else "Odd"

age = int(input("Enter age: "))
print("Age category:", age_category(age))

temp = float(input("Enter temperature: "))
print("Weather:", temperature_status(temp))

score = int(input("Enter score: "))
print("Result:", score_result(score))

num = int(input("Enter a number: "))
print("Number is:", even_or_odd(num))

print(age_category(15))
print(age_category(22))

print(temperature_status(10))
print(temperature_status(30))

print(score_result(45))
print(score_result(80))

print(even_or_odd(7))
print(even_or_odd(12))
