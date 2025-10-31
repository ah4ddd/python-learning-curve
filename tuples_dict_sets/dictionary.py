person = {
    "name": "Ahad",
    "age": 20,
    "city": "Lucknow",
    "name": "shey"
}

print(person["name"])
print(person["age"])
print(person["city"])

fruit_dict = {
    "apple": "A round fruit that's red or green",
    "banana": "A long yellow fruit",
    "cherry": "A small round red fruit"
}

contact1 = {
    "name": "Raja",
    "phone": "9876543210",
    "email": "raj@email.com"
}

print(contact1["phone"])

life ={
    "money": 9999999999999,
    "focus": True,
    "women": "Loving",
    "sex" : "byproduct",
}

print (life)
print(life["sex"])

student = {}

student["name"] = "Ahad"
student["age"] = 20
student["course"] = "Python"
student["day"] = 20

print(student)

student = {
    "name": "Ahad",
    "age": 20,
    "city": "Lucknow",
    "courses": ["Python", "JavaScript", "Design"],
    "grades": {
        "Python": "A",
        "JavaScript": "B+",
        "Design": "A+"
    },
    "is_enrolled": True,
    "gpa": 3.8
}

print(student["name"])
print(student["courses"])
print(student["courses"][0])
print(student["grades"]["JavaScript"])

