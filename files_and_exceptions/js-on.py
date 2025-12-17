import json

with open("me.json", "r") as f:
    user = json.load(f)

print(user)
print(type(user))
