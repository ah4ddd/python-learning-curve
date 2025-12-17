import json

dickionary = {"ahad": 20, "mia" : 23, "us": "we hate each other"}

with open("mia.json", "w") as xexy:
    json.dump(dickionary, xexy, indent=4)

with open("mia.json", "r") as m:
    mine = json.load(m)

print(mine)


