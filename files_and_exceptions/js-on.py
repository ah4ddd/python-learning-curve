import json

with open("me.json", "r") as f:
    user = json.load(f)

print(user)
print(type(user))

print(user["name"])     # Ahad
print(user["age"])      # 20
print(user["hobbies"])  # ['coding', 'gaming', 'learning']

for hobby in user["hobbies"]:
    print(f"Hobby: {hobby}")
