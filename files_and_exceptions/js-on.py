import json

user_data = {
    "name": "Mia",
    "age": 22,
    "email": "mia@example.com",
    "hobbies": ["roasting Ahad", "being right", "programming"],
    "savage_level": 100
}

with open("mia.json", "w") as f:
    json.dump(user_data, f, indent=4)

print("✅ Saved pretty JSON!")
